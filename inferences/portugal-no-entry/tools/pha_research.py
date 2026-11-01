#!/usr/bin/env python3
"""Research helper for the "Portugal no entry" task.

Searches the pha archive (read-only) for a person's name variants and prints,
for every hit, the document, page, variant and the surrounding text, so that an
agent can decide the place of entry in the Society of Jesus.

Usage
-----
    python3 tools/pha_research.py --name "Diogo Pinto" \
        --variant "Diego Pinto" --variant "Didacus Pintus" \
        --year 1561-1570

    python3 tools/pha_research.py --sql "select ..."     # ad-hoc (read-only)

Options
-------
--name        principal name (searched as a phrase, and as name+/-1 word)
--variant     extra spelling / Latin form (repeatable)
--year        restrict hits whose page text mentions a year in the range
--context     characters of context around each match (default 260)
--limit       max hits printed per query (default 8)
--docs        also print the archive document map (id  filename  collection)

Only the archive DB is queried (immutable, read-only).  Full page text is read
from library/*.md through `pha_page.py`-style access; this script prints
snippets, and the page file path, for the agent to read in full.
"""

from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys

ARCHIVE = os.environ.get("PHA_ARCHIVE_DIR", "/Users/jrc/jesuit-archive")
DB = os.path.join(ARCHIVE, "archive.db")

# Documents whose content is about the Society in Portugal / the China mission.
RELEVANT_DIRS = (
    "jesuit-catalogues",
    "documenta-indica",
    "DocHistMissPadPortOriente",
    "reference-works",
    "franco-imagens",
    "matteo-ricci-fontes",
    "epistolae-mixtae",
    "litterae-quadrimestres",
    "letter",
    "monumenta",
    "pfister",
    "schute",
    "jesuit-early-authors",
    "inacio-loyola",
    "academic-works",
    "archives",
    "bpe",
)


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{DB}?mode=ro&immutable=1", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def doc_map(conn: sqlite3.Connection) -> None:
    print("### archive documents")
    print(f"{'id':>4}  {'pages':>5}  collection / filename")
    for r in conn.execute(
        "select id, filename, dir_path, page_count, status from documents order by dir_path, filename"
    ):
        print(f"{r['id']:>4}  {r['page_count'] or 0:>5}  {r['dir_path']}/{r['filename']}  [{r['status']}]")


def hits(conn: sqlite3.Connection, phrase: str, context: int, limit: int) -> list[dict]:
    q = """
    select d.id as doc, d.filename as filename, d.dir_path as dir_path,
           p.page_no as page_no, d.page_count as page_count,
           ch.variant as variant, ch.text as text,
           p.id as page_id
    from chunks_fts f
    join chunks ch on ch.id = f.rowid
    join pages p on p.id = ch.page_id
    join documents d on d.id = ch.document_id
    where chunks_fts match ?
    order by rank
    limit ?
    """
    out = []
    try:
        rows = conn.execute(q, (f'"{phrase}"', limit * 3)).fetchall()
    except sqlite3.OperationalError as exc:  # pragma: no cover
        print(f"FTS error for {phrase!r}: {exc}", file=sys.stderr)
        return out
    pat = re.compile(re.escape(phrase), re.IGNORECASE)
    for r in rows:
        text = r["text"] or ""
        m = pat.search(text)
        if not m:
            # FTS may match a different tokenisation; skip
            continue
        s = max(0, m.start() - context)
        e = min(len(text), m.end() + context)
        out.append(
            {
                "doc": r["doc"],
                "filename": r["filename"],
                "dir_path": r["dir_path"],
                "page_no": r["page_no"],
                "page_count": r["page_count"],
                "variant": r["variant"],
                "snippet": text[s:e].replace("\n", " "),
            }
        )
        if len(out) >= limit:
            break
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name")
    ap.add_argument("--variant", action="append", default=[])
    ap.add_argument("--year", help="YYYY or YYYY-YYYY filter on the page text")
    ap.add_argument("--context", type=int, default=260)
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--docs", action="store_true")
    ap.add_argument("--sql")
    args = ap.parse_args()

    conn = connect()
    if args.docs:
        doc_map(conn)
        if not args.name:
            return 0

    if args.sql:
        for r in conn.execute(args.sql):
            print(dict(r))
        return 0

    if not args.name:
        ap.error("--name is required (or --docs)")

    names = [args.name] + args.variant
    ymin = ymax = None
    if args.year:
        parts = args.year.split("-")
        ymin = int(parts[0])
        ymax = int(parts[-1])

    for nm in names:
        print(f"\n{'=' * 78}\n### query: {nm!r}\n{'=' * 78}")
        found = hits(conn, nm, args.context, args.limit * 4)
        shown = 0
        for h in found:
            if ymin is not None:
                years = [int(y) for y in re.findall(r"\b(1[5-8]\d\d)\b", h["snippet"])]
                if years and not any(ymin <= y <= ymax for y in years):
                    continue
            shown += 1
            print(
                f"\n--- doc {h['doc']}  {h['filename']}  p.{h['page_no']}/{h['page_count']}  "
                f"[{h['variant']}]  ({h['dir_path']})"
            )
            print(f"    {h['snippet']}")
            if shown >= args.limit:
                break
        if shown == 0:
            print("    (no hits)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
