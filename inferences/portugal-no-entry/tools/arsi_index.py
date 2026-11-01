#!/usr/bin/env python3
"""Query the ARSI Lusitania catalogue index that ships with the digitised volumes.

The SSD «ARSI» copy of the digitised volumes carries a complete index of the
catalogues (274 catalogues, 12 volumes/parts), built from the typewritten
indexes bound in each volume:

    /Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/
    ├── AGENTS.md                  instructions for agents working on the package
    ├── indexes/INDICE-cronologico.md
    ├── indexes/INDICE-sistematico-por-volume.md
    ├── indexes/catalogos/<note>.md     one note per catalogue, images embedded
    ├── indexes/reports/LUS-NN.md       per-volume indexing report + corrections
    └── indexes/_data/LUS-NN.json       THE AUTHORITATIVE DATA (one per volume)

`indexes/_data/LUS-NN.json` is the source of truth of the index: each catalogue
has `year`, `type` (T1…T11), `local`, `folio_start`, `folio_end`,
`image_start_file`, `image_end_file`, `note` (→ indexes/catalogos/<note>.md),
`verified`, `evidence` (what was read on the first page) and an optional
`corrections` audit trail.

Examples
--------
    python3 tools/arsi_index.py --year 1655            # every 1655 catalogue
    python3 tools/arsi_index.py --year 1649 1651 --volume 45
    python3 tools/arsi_index.py --type T1 --local Transstagana
    python3 tools/arsi_index.py --note 1655-T1-LUS-45-177     # full record
    python3 tools/arsi_index.py --gaps --volume 45            # gaps/unaccounted

The folder is read-only for us: never edit `LUS. NN/` images. If an index entry
is wrong, report it as described in `AGENTS.md` §6 (CORRECTIONS.md + _data +
note) — not by editing images or inventing folios.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys

ROOT = os.environ.get(
    "ARSI_INDEX_DIR", "/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19"
)
DATA = os.path.join(ROOT, "indexes", "_data")


def load(volume: str | None = None) -> list[tuple[str, dict]]:
    if not os.path.isdir(DATA):
        sys.exit(
            f"index data not found: {DATA}\n"
            "Mount the external SSD «ARSI» (or set ARSI_INDEX_DIR)."
        )
    pattern = f"LUS-{volume}.json" if volume else "LUS-*.json"
    out = []
    for path in sorted(glob.glob(os.path.join(DATA, pattern))):
        vol = os.path.basename(path)[:-5]
        try:
            out.append((vol, json.load(open(path, encoding="utf-8"))))
        except json.JSONDecodeError as exc:  # pragma: no cover
            print(f"warning: {path}: {exc}", file=sys.stderr)
    return out


def fmt_row(vol: str, c: dict) -> str:
    local = c.get("local") or "—"
    folios = f"{c.get('folio_start', '?')}–{c.get('folio_end', '?')}"
    imgs = ""
    if c.get("image_start_file"):
        imgs = f"  imgs {c['image_start_file']}…{c.get('image_end_file') or ''}"
    note = c.get("note") or c.get("existing_note") or "—"
    ok = "✔" if c.get("verified") else "?"
    return f"{vol:8} {str(c.get('year', '?')):10} {c.get('type', '?'):4} {local:14} ff. {folios:12} {ok}  {note}{imgs}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--year", nargs="+", help="year(s) of the catalogue, e.g. 1655 or 1654-1655")
    ap.add_argument("--type", help="catalogue type, e.g. T1 (see indexes/TIPOLOGIA.md)")
    ap.add_argument("--local", help="place/community substring, e.g. Transstagana")
    ap.add_argument("--volume", help="volume, e.g. 45 (LUS-45.json)")
    ap.add_argument("--note", help="show the full record of one catalogue note")
    ap.add_argument("--gaps", action="store_true", help="print the volume gaps/unaccounted notes")
    ap.add_argument("--root", help=f"image root (default {ROOT})")
    args = ap.parse_args()
    if args.root:
        globals()["ROOT"] = args.root
        globals()["DATA"] = os.path.join(args.root, "indexes", "_data")

    volumes = load(args.volume)

    if args.note:
        for vol, d in volumes:
            for c in d.get("catalogues", []):
                if args.note in (c.get("note"), c.get("existing_note")):
                    print(f"# {args.note}  ({vol} — {ROOT}/{vol.replace('-', '. ')}/)")
                    print(json.dumps(c, ensure_ascii=False, indent=2))
                    return 0
        print(f"note not found: {args.note}", file=sys.stderr)
        return 1

    if args.gaps:
        for vol, d in volumes:
            print(f"## {vol}")
            for key in ("gaps", "unaccounted", "stray_files", "missing_images"):
                if d.get(key):
                    print(f"  {key}: {d[key]}")
            for c in d.get("catalogues", []):
                for corr in c.get("corrections") or []:
                    print(f"  correction {c.get('note')}: {json.dumps(corr, ensure_ascii=False)}")
        return 0

    rows = []
    for vol, d in volumes:
        for c in d.get("catalogues", []):
            if args.year:
                year = str(c.get("year", ""))
                if not any(y == year or year.startswith(y) for y in args.year):
                    continue
            if args.type and c.get("type") != args.type:
                continue
            if args.local and args.local.lower() not in (c.get("local") or "").lower():
                continue
            rows.append(fmt_row(vol, c))

    if not rows:
        print("no catalogue matches the filters", file=sys.stderr)
        return 1
    print(f"{'volume':8} {'year':10} {'type':4} {'local':14} {'folios':17} ok  note")
    print("\n".join(rows))
    print(
        f"\n{len(rows)} catalogue(s). Notes with images: "
        f"{ROOT}/indexes/catalogos/<note>.md — read AGENTS.md there before editing anything."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
