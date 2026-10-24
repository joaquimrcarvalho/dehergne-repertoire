#!/usr/bin/env python3
"""Record a correction to one catalogue and propagate it through the indexes.

The JSON tables in `extras/ARSI-catalogs-indexes/data/` are the source of truth.
This tool:
  1. changes one field of one catalogue (normally `folio_end`);
  2. appends an entry to the catalogue's `corrections` history (audit trail);
  3. appends a row to `extras/ARSI-catalogs-indexes/CORRECTIONS.md` (human log);
  4. regenerates the affected note, the portable package, the Obsidian indexes,
     the master-list section, the reports copy and the HTML pages.

Usage:
    python3 correct_entry.py --volume LUS-45 --note 1658-T1-LUS-45-251 \
        --field folio_end --value 266v \
        --reason "the range included the first page of the next catalogue" \
        --evidence "f.267 shows the title of the next catalogue (read image)"

    # only record, do not regenerate:
    python3 correct_entry.py ... --no-refresh
    # preview:
    python3 correct_entry.py ... --dry-run
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
LOG = os.path.join(ROOT, "CORRECTIONS.md")
VAULT = "/Users/jrc/jrc-notes"
CORRECTABLE = {"folio_start", "folio_end", "year", "type", "title", "description",
               "verified", "image_start_file", "image_end_file"}


def find_json(volume):
    if os.path.exists(volume):
        return volume
    name = volume if volume.endswith(".json") else volume + ".json"
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        raise SystemExit(f"JSON not found for volume {volume!r} (looked for {path})")
    return path


def find_entry(data, note):
    for entry in data.get("catalogues", []):
        name = entry.get("note")
        if not name:
            existing = entry.get("existing_note") or ""
            name = existing.split("/")[-1].replace(".md", "")
        if name == note:
            return entry
    return None


def append_log(row):
    header = (
        "# Correções registadas\n\n"
        "> Registo cronológico das correções feitas ao índice dos catálogos. "
        "Cada correção é aplicada primeiro na tabela JSON do volume "
        "(`data/LUS-XX.json`, campo `corrections`) e depois propagada às notas, "
        "aos índices (Markdown/HTML/Obsidian) e aos relatórios.\n\n"
        "| Data | Volume | Nota | Campo | Antes | Depois | Motivo | Evidência |\n"
        "|---|---|---|---|---|---|---|---|\n"
    )
    exists = os.path.exists(LOG)
    text = open(LOG, encoding="utf-8").read() if exists else ""
    if not exists or "| Data | Volume |" not in text:
        text = header
    text = text.rstrip() + "\n" + row + "\n"
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write(text)


def run(label, cmd):
    print(f"  → {label}")
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout[-2000:])
        print(result.stderr[-2000:])
        raise SystemExit(f"FAILED: {label}")
    tail = (result.stdout.strip().splitlines() or [""])[-1]
    print(f"     {tail}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--volume", required=True, help="volume label or JSON path, e.g. LUS-45")
    ap.add_argument("--note", required=True, help="note name of the catalogue")
    ap.add_argument("--field", default="folio_end", choices=sorted(CORRECTABLE))
    ap.add_argument("--value", required=True)
    ap.add_argument("--reason", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--by", default="")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-refresh", action="store_true")
    args = ap.parse_args()

    json_path = find_json(args.volume)
    data = json.load(open(json_path, encoding="utf-8"))
    entry = find_entry(data, args.note)
    if entry is None:
        raise SystemExit(f"catalogue note not found in {json_path}: {args.note}")

    old = entry.get(args.field)
    new_value = args.value
    if args.field in ("folio_start", "folio_end", "image_start_file", "image_end_file"):
        new_value = args.value
    elif args.field == "verified":
        new_value = args.value.lower() in ("1", "true", "yes", "sim")
    elif args.field == "year":
        new_value = args.value
    print(f"{os.path.basename(json_path)} :: {args.note}")
    print(f"  {args.field}: {old!r} → {new_value!r}")

    if args.dry_run:
        print("  (dry-run: JSON, log and indexes not changed)")
        print("  refresh pipeline would run: gen_notes --only, make_portable_package,"
              " make_vault_indexes, update_master_section, copy_reports, make_html_package")
        return 0

    entry[args.field] = new_value
    if args.field in ("folio_start", "folio_end", "image_start_file", "image_end_file"):
        entry["verified"] = True
    entry.setdefault("corrections", []).append({
        "date": args.date,
        "field": args.field,
        "old": old,
        "new": new_value,
        "reason": args.reason,
        "evidence": args.evidence,
        "by": args.by,
    })
    evidence = entry.get("evidence") or ""
    entry["evidence"] = (evidence + " | correção " + args.date + ": " + args.evidence).strip(" |")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    print("  JSON updated (with corrections history)")

    row = (f"| {args.date} | {os.path.basename(json_path)[:-5]} | {args.note} | {args.field} | "
           f"{old} | {new_value} | {args.reason} | {args.evidence} |")
    append_log(row)
    print(f"  log updated: {LOG}")

    if args.no_refresh:
        print("  --no-refresh: indexes not regenerated")
        return 0

    print("propagating:")
    run("catalogue note", [sys.executable, os.path.join(HERE, "gen_notes.py"),
                           json_path, "--force", "--only", args.note])
    run("portable package", [sys.executable, os.path.join(HERE, "make_portable_package.py")])
    run("Obsidian index notes", [sys.executable, os.path.join(HERE, "make_vault_indexes.py")])
    run("master list section", [sys.executable, os.path.join(HERE, "update_master_section.py")])
    run("reports copy", [sys.executable, os.path.join(HERE, "copy_reports.py")])
    run("HTML pages", [sys.executable, os.path.join(HERE, "make_html_package.py")])
    print("done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
