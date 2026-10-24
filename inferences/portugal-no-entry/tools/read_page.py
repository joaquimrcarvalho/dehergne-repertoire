#!/usr/bin/env python3
"""Read one archive page in full (raw + edited) from the pha DB (read-only).

    python3 tools/read_page.py 81 50
    python3 tools/read_page.py 29 4 --raw

Prints the document metadata (filename, collection, variants, page file) and the
full text of each variant, so it can be quoted and cited.
"""

from __future__ import annotations

import os
import sqlite3
import sys

ARCHIVE = os.environ.get("PHA_ARCHIVE_DIR", "/Users/jrc/jesuit-archive")
DB = os.path.join(ARCHIVE, "archive.db")


def main() -> int:
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        return 1
    doc, page = int(args[0]), int(args[1])
    only_raw = "--raw" in args
    conn = sqlite3.connect(f"file:{DB}?mode=ro&immutable=1", uri=True)
    conn.row_factory = sqlite3.Row
    d = conn.execute(
        "select id, filename, dir_path, page_count, editor, palaeographer from documents where id=?",
        (doc,),
    ).fetchone()
    if d is None:
        print(f"!! no document {doc}", file=sys.stderr)
        return 1
    print(f"# doc {d['id']}  {d['filename']}")
    print(f"  collection: {d['dir_path']}")
    print(f"  pages: {d['page_count']}  editor: {d['editor']}  palaeographer: {d['palaeographer']}")
    bib = conn.execute(
        "select citation, record_origin, sidecar_path from document_bibliography where document_id=?",
        (doc,),
    ).fetchone()
    if bib:
        print(f"  reference: {bib['citation']}")
        print(f"  origin: {bib['record_origin']}")
    variants = conn.execute(
        """select ch.variant, ch.chunk_no, ch.text from chunks ch
           join pages p on p.id=ch.page_id
           where ch.document_id=? and p.page_no=?
           order by ch.variant, ch.chunk_no""",
        (doc, page),
    ).fetchall()
    if not variants:
        print("!! no text for that page", file=sys.stderr)
        return 1
    for v in variants:
        if only_raw and v["variant"] != "raw":
            continue
        if v["chunk_no"] > 0:
            print(f"\n--- {v['variant']} chunk {v['chunk_no']} ---")
            print(v["text"])
            continue
        print(f"\n{'=' * 78}\n## variant: {v['variant']}\n{'=' * 78}")
        print(v["text"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
