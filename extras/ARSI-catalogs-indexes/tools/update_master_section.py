#!/usr/bin/env python3
"""Replace the generated systematic section at the end of the Obsidian master list.

The section is rebuilt from `extras/ARSI-catalogs-indexes/data/*.json` by
`make_master_section.py`, so any correction made in the JSON tables (and in the
catalogue notes) is reflected in the master list.

Usage:
    python3 update_master_section.py [--dry-run]
"""
import argparse
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = "/Users/jrc/jrc-notes/03 Projectos/03.03.01.01 ARSI Lusitania - catálogos - digitalizados - em curso.md"
MARKER = "## Índice sistemático por volume (gerado 2026-10-22)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with tempfile.NamedTemporaryFile("r", suffix=".md", delete=False, encoding="utf-8") as tmp:
        tmp_path = tmp.name
    try:
        subprocess.run(
            [sys.executable, os.path.join(HERE, "make_master_section.py"), "--out", tmp_path],
            check=True, capture_output=True, text=True,
        )
        section = open(tmp_path, encoding="utf-8").read()
    finally:
        os.unlink(tmp_path)

    text = open(MASTER, encoding="utf-8").read()
    if MARKER not in text:
        print("marker not found in master list:", MARKER)
        return 1
    head = text.split(MARKER)[0].rstrip()
    new_text = head + "\n\n---\n\n" + section
    n = len([l for l in section.split("\n") if l.startswith("| ") and not l.startswith("| Ano")])
    if args.dry_run:
        print(f"would replace section: {n} catalogue rows")
        return 0
    with open(MASTER, "w", encoding="utf-8") as fh:
        fh.write(new_text)
    print(f"master list section updated: {n} catalogue rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
