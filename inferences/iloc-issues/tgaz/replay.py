#!/usr/bin/env python3
"""Re-run the queries recorded in ``query-log.json`` against the live TGAZ.

Used to check that the evidence in the issue sections is reproducible: the
recorded hit count for each query is compared with the live server response
(exact counts can drift if CHGIS updates the database, so a mismatch is
reported, not raised).

Usage:
    python3 replay.py                 # all queries
    python3 replay.py --limit 10      # first 10
    python3 replay.py --issue 08      # one issue
    python3 replay.py --quiet         # summary only
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

from tgaz_tool import tgaz_query

HERE = os.path.dirname(os.path.abspath(__file__))
QUERY_LOG_PATH = os.path.join(HERE, "query-log.json")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--issue", default=None)
    parser.add_argument("--sleep", type=float, default=0.5)
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--log", default=QUERY_LOG_PATH,
                        help="query log to replay (default: query-log.json)")
    args = parser.parse_args(argv)

    with open(args.log, encoding="utf-8") as fh:
        log = json.load(fh)

    if args.issue is not None:
        wanted = str(args.issue).zfill(2)
        log = [q for q in log if str(q.get("issue")).zfill(2) == wanted]
    if args.limit:
        log = log[: args.limit]

    ok = mismatch = failed = 0
    for i, entry in enumerate(log, 1):
        try:
            response = tgaz_query(
                name=entry["name"],
                year=entry.get("year"),
                feature_type=entry.get("feature_type"),
                source=entry.get("source"),
                parent=entry.get("parent"),
            )
            total = int(response.get("count of total results") or 0)
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"[{i}/{len(log)}] issue {entry.get('issue')} {entry['name']!r}: "
                  f"ERROR {exc}")
            time.sleep(args.sleep)
            continue
        expected = entry.get("expected_total")
        expected = int(expected) if expected is not None else None
        if expected is not None and total != expected:
            mismatch += 1
            status = f"MISMATCH expected {expected}, got {total}"
        else:
            ok += 1
            status = f"ok ({total})"
        if not args.quiet or status.startswith("MISMATCH"):
            print(f"[{i}/{len(log)}] issue {entry.get('issue')} "
                  f"{entry['name']!r} year={entry.get('year')} "
                  f"ft={entry.get('feature_type')} parent={entry.get('parent')}: {status}")
        time.sleep(args.sleep)

    print(f"\nreplayed {len(log)}: {ok} ok, {mismatch} mismatched, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
