#!/usr/bin/env python3
"""Validate the ARSI catalogue index: JSON tables, notes, image links, coverage.

Usage:
    python3 validate.py [--data-dir DIR] [--notes-dir DIR]
"""
import argparse
import glob
import json
import os
import re
import sys
import urllib.parse

DIGI = "/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19"
VAULT = "/Users/jrc/jrc-notes"
DEFAULT_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DEFAULT_NOTES_DIRS = [os.path.join(VAULT, "03 Projectos"), os.path.join(VAULT, "01 Notes")]

LINK_RE = re.compile(r"\]\((file://[^)]+)\)")
RE_FOLIO = re.compile(r"^0*(\d+)(v)?$", re.I)


def folio(value):
    m = RE_FOLIO.match(str(value).strip())
    if not m:
        return None
    return (int(m.group(1)), 1 if m.group(2) else 0)


def check_file(json_path, notes_dirs):
    with open(json_path, encoding="utf-8") as fh:
        data = json.load(fh)
    rows = []
    problems = []
    ranges = []
    for entry in data.get("catalogues", []):
        note = entry.get("note")
        if not note:
            continue
        path = None
        exists = False
        for d in notes_dirs:
            cand = os.path.join(d, note + ".md")
            if os.path.exists(cand):
                path = cand
                exists = True
                break
        links = 0
        bad = []
        if exists:
            text = open(path, encoding="utf-8").read()
            urls = LINK_RE.findall(text)
            links = len(urls)
            for url in urls:
                raw = urllib.parse.unquote(url[len("file://"):])
                if not os.path.exists(raw):
                    bad.append(raw)
        else:
            problems.append(f"missing note: {note}")
        if bad:
            problems.append(f"{note}: {len(bad)} broken image link(s)")
        lo, hi = folio(entry.get("folio_start")), folio(entry.get("folio_end"))
        if lo and hi:
            ranges.append((lo, hi, note))
        rows.append({
            "note": note, "year": entry.get("year"), "type": entry.get("type"),
            "folios": f"{entry.get('folio_start')}-{entry.get('folio_end')}",
            "exists": exists, "links": links, "verified": entry.get("verified"),
        })
    ranges.sort()
    for (lo1, hi1, n1), (lo2, hi2, n2) in zip(ranges, ranges[1:]):
        if lo2 <= hi1:
            problems.append(f"overlapping ranges: {n1} and {n2}")
    return data, rows, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=DEFAULT_DATA_DIR)
    ap.add_argument("--notes-dir", nargs="+", default=DEFAULT_NOTES_DIRS)
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.data_dir, "*.json")))
    if not files:
        print(f"no JSON files in {args.data_dir}")
        return 1
    total_problems = 0
    for json_path in files:
        data, rows, problems = check_file(json_path, args.notes_dir)
        name = os.path.basename(json_path)
        vol = data.get("volume_note") or data.get("volume_folder")
        verified = sum(1 for r in rows if r["verified"] is True)
        print(f"\n=== {name} — {vol} ===")
        print(f"catalogues: {len(rows)} | verified: {verified} | "
              f"notes existing: {sum(1 for r in rows if r['exists'])} | "
              f"image links: {sum(r['links'] for r in rows)}")
        for p in problems:
            print(f"  PROBLEM: {p}")
        total_problems += len(problems)
    print(f"\nTOTAL PROBLEMS: {total_problems}")
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
