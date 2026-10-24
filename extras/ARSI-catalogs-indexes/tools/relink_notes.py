#!/usr/bin/env python3
"""Re-point the file:// image links of the catalogue notes to a new base folder.

Prepared for moving the ARSI Lusitania digitalisation from iCloud Drive
(~/Documents/.../ARSI Lusitania/v2-2025-01-19) to an external SSD.

Usage:
    # see what would change
    python3 relink_notes.py --old "/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania" \
                            --new "/Volumes/ARSI/ARSI Lusitania"

    # apply
    python3 relink_notes.py --old "..." --new "..." --apply

    # only check that every link resolves
    python3 relink_notes.py --check

Notes are searched in /Users/jrc/jrc-notes (01 Notes, 03 Projectos,
04 Biographies). Only `file://` links are rewritten; note names and everything
else stay untouched.
"""
import argparse
import glob
import os
import re
import sys
import urllib.parse

VAULT = "/Users/jrc/jrc-notes"
DEFAULT_DIRS = ["01 Notes", "03 Projectos", "04 Biographies"]
LINK_RE = re.compile(r"\]\((file://[^)]+)\)")


def note_paths(dirs):
    for d in dirs:
        for p in glob.glob(os.path.join(VAULT, d, "**", "*.md"), recursive=True):
            yield p


def decode(url):
    return urllib.parse.unquote(url[len("file://"):])


def encode(path):
    return "file://" + urllib.parse.quote(path, safe="/")


def cmd_check(dirs):
    total = missing = 0
    for p in note_paths(dirs):
        text = open(p, encoding="utf-8").read()
        for url in LINK_RE.findall(text):
            if "v2-2025-01-19" not in url:
                continue
            total += 1
            if not os.path.exists(decode(url)):
                missing += 1
                if missing <= 20:
                    print("MISSING:", os.path.relpath(p, VAULT), "->", decode(url))
    print(f"\nlinks to v2-2025-01-19: {total} | missing files: {missing}")
    return 1 if missing else 0


def cmd_relink(old, new, apply, dirs):
    old_enc = urllib.parse.quote(old, safe="/")
    changed_notes = changed_links = 0
    for p in note_paths(dirs):
        text = open(p, encoding="utf-8").read()
        if old_enc not in text and old not in text:
            continue
        new_text = text.replace(old_enc, urllib.parse.quote(new, safe="/"))
        new_text = new_text.replace(old, new)
        if new_text == text:
            continue
        n = text.count(old_enc) + text.count(old)
        changed_notes += 1
        changed_links += n
        print(f"{'REWRITE' if apply else 'WOULD REWRITE'}: {os.path.relpath(p, VAULT)} ({n} links)")
        if apply:
            open(p, "w", encoding="utf-8").write(new_text)
    print(f"\nnotes: {changed_notes} | links: {changed_links} | apply={apply}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old")
    ap.add_argument("--new")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dirs", nargs="+", default=DEFAULT_DIRS)
    args = ap.parse_args()
    if args.check:
        return cmd_check(args.dirs)
    if not args.old or not args.new:
        ap.error("--old and --new are required (or use --check)")
    return cmd_relink(args.old, args.new, args.apply, args.dirs)


if __name__ == "__main__":
    sys.exit(main())
