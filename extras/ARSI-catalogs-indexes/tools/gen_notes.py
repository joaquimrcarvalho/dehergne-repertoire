#!/usr/bin/env python3
"""Generate Obsidian catalogue notes from a volume JSON index.

Usage:
    python3 gen_notes.py ../../data/LUS-45.json [--notes-dir DIR] [--dry-run] [--force]

The JSON schema is documented in ../METHOD.md. For each catalogue with a "note"
name, the script embeds every image of the volume folder(s) whose stamped folio
falls inside [folio_start, folio_end], in natural order, using the same
`file://` markdown format as the existing notes.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse

DIGI = "/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19"
VAULT = "/Users/jrc/jrc-notes"
DEFAULT_NOTES_DIR = os.path.join(VAULT, "03 Projectos")

RE_SINGLE = re.compile(r"^0*(\d+)(v)?\.(?:jpg|jpeg)$", re.I)
RE_DOUBLE = re.compile(r"^0*(\d+)(v)?-0*(\d+)(v)?\.(?:jpg|jpeg)$", re.I)
RE_FOLIO = re.compile(r"^0*(\d+)(v)?$", re.I)


def parse_folio(value):
    s = str(value).strip()
    m = RE_FOLIO.match(s)
    if not m:
        raise ValueError(f"invalid folio: {value!r}")
    return (int(m.group(1)), 1 if m.group(2) else 0)


def scan_images(folders):
    items = []
    for folder in folders:
        path = os.path.join(DIGI, folder)
        if not os.path.isdir(path):
            print(f"WARNING: folder not found: {path}", file=sys.stderr)
            continue
        for filename in os.listdir(path):
            m = RE_DOUBLE.match(filename)
            if m:
                a, va, b, vb = m.group(1), m.group(2), m.group(3), m.group(4)
                items.append({
                    "file": filename, "folder": folder,
                    "start": (int(a), 1 if va else 0),
                    "end": (int(b), 1 if vb else 0),
                })
                continue
            m = RE_SINGLE.match(filename)
            if m:
                n, v = m.group(1), m.group(2)
                pos = (int(n), 1 if v else 0)
                items.append({"file": filename, "folder": folder, "start": pos, "end": pos})
    items.sort(key=lambda x: (x["start"], x["end"], x["file"]))
    return items


def image_url(item):
    base = urllib.parse.quote(DIGI + "/" + item["folder"], safe="/")
    return f"file://{base}/{urllib.parse.quote(item['file'])}"


def in_range(item, lo, hi):
    return item["end"] >= lo and item["start"] <= hi


def note_text(entry, volume_note, index_sources):
    title = entry.get("title") or entry.get("note", "Catalogue")
    desc = entry.get("description") or ""
    sources = ", ".join(f"`{s}`" for s in index_sources) if index_sources else ""
    lines = [f"# {title}", ""]
    if desc:
        lines += [desc, ""]
    src = "Índice dactilografado: " + sources if sources else ""
    if src and volume_note:
        src += f". Ver [[{volume_note}]]."
    if src:
        lines += [src, ""]
    embeds = []
    for item in entry["_images"]:
        embeds.append(f"![{item['file']}]({image_url(item)})")
    lines += ["\n\n".join(embeds), ""]
    return "\n".join(lines).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_file")
    ap.add_argument("--notes-dir", default=DEFAULT_NOTES_DIR)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", nargs="+", default=None,
                    help="regenerate only these note names")
    args = ap.parse_args()

    with open(args.json_file, encoding="utf-8") as fh:
        data = json.load(fh)

    folders = data.get("volume_folder") or []
    volume_note = data.get("volume_note", "")
    index_sources = data.get("index_sources") or []
    images = scan_images(folders)

    created, skipped, failed = [], [], []
    for entry in data.get("catalogues", []):
        note = entry.get("note")
        if not note:
            continue
        if args.only and note not in args.only:
            continue
        if entry.get("skip"):
            skipped.append((note, "skip flag"))
            continue
        # Optional exact image range (for volumes whose filenames are not the
        # stamped folio numbers, e.g. LUS. 44 I): image_start_file /
        # image_end_file name the first and last image file to embed.
        if entry.get("image_start_file"):
            folder = entry.get("image_folder")
            pool = [it for it in images if not folder or it["folder"] == folder]
            start = entry["image_start_file"]
            end = entry.get("image_end_file") or start
            i = next((n for n, it in enumerate(pool) if it["file"] == start), None)
            j = next((n for n, it in enumerate(pool) if it["file"] == end), None)
            if i is None or j is None:
                failed.append((note, f"image_start_file/image_end_file not found: {start} .. {end}"))
                continue
            selected = pool[min(i, j):max(i, j) + 1]
        else:
            lo = parse_folio(entry["folio_start"])
            hi = parse_folio(entry["folio_end"])
            selected = [it for it in images if in_range(it, lo, hi)]
        if not selected:
            failed.append((note, "no images found for the folio range"))
            continue
        entry["_images"] = selected
        text = note_text(entry, volume_note, index_sources)
        path = os.path.join(args.notes_dir, note + ".md")
        if os.path.exists(path) and not args.force:
            skipped.append((note, "already exists"))
            continue
        if args.dry_run:
            created.append((note, len(selected), "(dry-run)"))
            continue
        os.makedirs(args.notes_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        created.append((note, len(selected), path))

    print(f"volume: {volume_note or folders}")
    print(f"catalogues: {len(data.get('catalogues', []))} | images scanned: {len(images)}")
    for name, count, path in created:
        print(f"  CREATED {name} ({count} images) {path}")
    for name, reason in skipped:
        print(f"  SKIPPED {name} ({reason})")
    for name, reason in failed:
        print(f"  FAILED  {name} ({reason})")
    print(f"summary: {len(created)} created, {len(skipped)} skipped, {len(failed)} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
