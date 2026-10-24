#!/usr/bin/env python3
"""Build the consolidated report for the TGAZ check of the comment drafts.

Reads ``tgaz/comments-data/<GH>.json`` (written by ``build_comments.py``) and
writes:

* ``inferences/iloc-issues/comments/TGAZ-COMMENTS.md`` — consolidated report;
* ``tgaz/comments-results.csv`` — one row per comment draft;
* ``tgaz/comments-query-log.json`` — all recorded queries, for replay.

Usage:
    python3 build_comments_report.py
"""

from __future__ import annotations

import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ISSUES_DIR = os.path.dirname(HERE)
COMMENTS_DIR = os.path.join(ISSUES_DIR, "comments")
CDATA_DIR = os.path.join(HERE, "comments-data")
REPORT_PATH = os.path.join(COMMENTS_DIR, "TGAZ-COMMENTS.md")
CSV_PATH = os.path.join(HERE, "comments-results.csv")
QUERY_LOG_PATH = os.path.join(HERE, "comments-query-log.json")
HIGHLIGHTS_PATH = os.path.join(HERE, "HIGHLIGHTS-COMMENTS.md")

VERDICTS = ["confirmed", "partially-confirmed", "contradicted", "not-in-tgaz",
            "outside-coverage"]
VERDICT_ORDER = {v: i for i, v in enumerate(VERDICTS)}


def load_records():
    records = []
    for name in sorted(os.listdir(CDATA_DIR)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(CDATA_DIR, name), encoding="utf-8") as fh:
            records.append(json.load(fh))
    records.sort(key=lambda r: int(r.get("github_issue", 0)))
    return records


def md(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def best_label(rec):
    best = rec.get("best_match") or {}
    if not best:
        return "—"
    label = f"`{best.get('sys_id')}` {best.get('name', '')}".strip()
    ft = best.get("feature_type")
    if ft:
        label += f" ({ft})"
    return label


def cross_ref_link(cross):
    import glob
    files = glob.glob(os.path.join(ISSUES_DIR, f"{cross}-*.md"))
    if not files:
        return f"issue {cross}"
    return f"[issue {cross}](../{os.path.basename(sorted(files)[0])})"


def results_table(records):
    lines = [
        "| GH issue | Place | Year | Region | Anchor | Best TGAZ match | Dist. km | Verdict | TGAZ pass ref. |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for rec in records:
        gh = rec.get("github_issue", "?")
        cross = rec.get("cross_ref")
        ref = cross_ref_link(cross) if cross else "**new**"
        wd = (rec.get("wikidata") or {}).get("id") or "—"
        if wd != "—":
            wd = f"[{wd}](https://www.wikidata.org/wiki/{wd})"
        dist = rec.get("dist_km")
        dist = f"{dist:.1f}" if isinstance(dist, (int, float)) else "—"
        lines.append(
            f"| [#{gh}](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/{gh}) "
            f"| {md(rec.get('place', ''))} | {md(rec.get('dehergne_year', ''))} "
            f"| {md(rec.get('region', ''))} | {wd} | {best_label(rec)} | {dist} "
            f"| `{rec.get('verdict', '')}` | {ref} |"
        )
    return "\n".join(lines)


def detail(records):
    lines = []
    for rec in records:
        gh = rec.get("github_issue", "?")
        lines.append(
            f"### #{gh} — {rec.get('place', '')} (`{rec.get('verdict', '')}`)"
        )
        lines.append("")
        if rec.get("verdict_note"):
            lines.append(rec["verdict_note"])
            lines.append("")
        queries = rec.get("queries") or []
        if queries:
            parts = []
            for q in queries[:8]:
                label = f"`{q.get('name')}`"
                filters = []
                if q.get("year"):
                    filters.append(f"year={q['year']}")
                if q.get("feature_type"):
                    filters.append(f"ft={q['feature_type']}")
                if q.get("parent"):
                    filters.append(f"parent={q['parent']}")
                if filters:
                    label += " (" + ", ".join(filters) + ")"
                label += f" → {q.get('total', 0)} hit(s)"
                parts.append(label)
            if len(queries) > 8:
                parts.append(f"… {len(queries) - 8} more")
            lines.append("Queries: " + "; ".join(parts) + ".")
            lines.append("")
        best = rec.get("best_match") or {}
        if best.get("sys_id"):
            bits = []
            if best.get("parent"):
                bits.append(f"parent {best['parent']}")
            if best.get("present_location"):
                bits.append(f"present location “{best['present_location']}”")
            if best.get("uri"):
                bits.append(f"<{best['uri']}>")
            lines.append("Best record: " + ", ".join(bits) + ".")
            lines.append("")
    return "\n".join(lines)


def build_report(records):
    from collections import Counter

    counts = Counter(rec.get("verdict", "unclassified") for rec in records)
    n = len(records)
    total_queries = sum(len(rec.get("queries") or []) for rec in records)
    cross = sum(1 for rec in records if rec.get("cross_ref"))
    new = n - cross

    lines = []
    lines.append("# TGAZ (CHGIS) check of the GitHub-issue comment drafts")
    lines.append("")
    lines.append(
        "The 24 identification reports in `inferences/iloc-issues/comments/` — "
        "comments drafted for the existing GitHub issues "
        "[#2](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/2) "
        "to [#68](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/68) "
        "— have been checked against the **CHGIS Temporal Gazetteer (TGAZ)**, "
        "the same service used for the 34 issue files in the main pass. "
        f"Every comment file now carries a `## TGAZ (CHGIS) check` section. "
        f"{n} drafts checked ({cross} cross-referenced to the main pass, "
        f"{new} new places), {total_queries} recorded queries. Full main-pass "
        "report: [TGAZ-RESOLUTION.md](../TGAZ-RESOLUTION.md); method: "
        "[tgaz/PROTOCOL.md](../tgaz/PROTOCOL.md)."
    )
    lines.append("")
    lines.append("## Relationship to the main pass")
    lines.append("")
    lines.append(
        "Nineteen of the comment drafts describe places already checked in the "
        "34 issue files; their sections reproduce the recorded queries and link "
        "to the issue section that holds the full evidence. **Five drafts "
        "describe places not covered there** and were given fresh TGAZ queries:"
    )
    lines.append("")
    lines.append(
        "- **#2 Lofeu** — China–Tonkin frontier station, 1722–23;"
    )
    lines.append(
        "- **#29 Chang-tsin do Yüansi** — 鄖西縣, Hubei;"
    )
    lines.append(
        "- **#30 Chang-si** — Shanxi province;"
    )
    lines.append(
        "- **#33 Ko-li-tsem do Kiating** — 嘉定縣, Kiangnan;"
    )
    lines.append(
        "- **#63 Tongko / \"Tsangzo\"** — the Changshu 常熟 district (Jiangsu)."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Verdict | Comment drafts |")
    lines.append("|---|---|")
    for verdict in VERDICTS:
        if counts.get(verdict):
            lines.append(f"| `{verdict}` | {counts[verdict]} |")
    lines.append(f"| **total** | **{n}** |")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append(results_table(records))
    lines.append("")
    lines.append(
        "**Reading the distance column.** It is the great-circle distance "
        "between the TGAZ point and the anchor proposed or recommended in the "
        "comment. For a confirmed place both point at the same settlement; for "
        "a `partially-confirmed` match TGAZ gives the parent unit's seat while "
        "the comment's anchor is the locality, so a 10–60 km gap is normal and "
        "is not a mismatch score."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    if os.path.exists(HIGHLIGHTS_PATH):
        with open(HIGHLIGHTS_PATH, encoding="utf-8") as fh:
            lines.append(fh.read().strip())
        lines.append("")
    lines.append("## Per-draft evidence")
    lines.append("")
    lines.append(detail(records))
    lines.append("")
    lines.append("## Reproducing")
    lines.append("")
    lines.append("```bash")
    lines.append("cd inferences/iloc-issues/tgaz")
    lines.append("python3 build_comments.py            # re-run the checks + sections")
    lines.append("python3 replay.py --log comments-query-log.json   # verify the queries")
    lines.append("python3 build_comments_report.py     # rebuild this report")
    lines.append("```")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append("| Path | Content |")
    lines.append("|---|---|")
    lines.append("| `tgaz/comments-data/<GH>.json` | per-draft evidence record |")
    lines.append("| `tgaz/comments-results.csv` | one row per draft (generated) |")
    lines.append("| `tgaz/comments-query-log.json` | recorded queries, for replay (generated) |")
    lines.append("| `tgaz/build_comments.py` | generator of the sections and JSON records |")
    lines.append("| `tgaz/build_comments_report.py` | this report's generator |")
    lines.append("| `comments/<draft>.md` | the draft with its `## TGAZ (CHGIS) check` section |")
    lines.append("")
    return "\n".join(lines) + "\n"


def build_csv(records):
    fields = [
        "github_issue", "comment_file", "place", "dehergne_year", "region",
        "country", "identified_chinese", "cross_ref", "wikidata_id",
        "tgaz_sys_id", "tgaz_name", "tgaz_feature_type", "tgaz_years",
        "tgaz_parent", "tgaz_lat", "tgaz_lon", "wikidata_lat", "wikidata_lon",
        "dist_km", "verdict", "verdict_note", "n_queries", "checked_at",
    ]
    rows = []
    for rec in records:
        best = rec.get("best_match") or {}
        wd = rec.get("wikidata") or {}
        rows.append({
            "github_issue": rec.get("github_issue", ""),
            "comment_file": rec.get("comment_file", ""),
            "place": rec.get("place", ""),
            "dehergne_year": rec.get("dehergne_year", ""),
            "region": rec.get("region", ""),
            "country": rec.get("country", ""),
            "identified_chinese": rec.get("identified_chinese", ""),
            "cross_ref": rec.get("cross_ref") or "",
            "wikidata_id": wd.get("id", ""),
            "tgaz_sys_id": best.get("sys_id", ""),
            "tgaz_name": best.get("name", ""),
            "tgaz_feature_type": best.get("feature_type", ""),
            "tgaz_years": best.get("years", ""),
            "tgaz_parent": best.get("parent", ""),
            "tgaz_lat": best.get("lat", ""),
            "tgaz_lon": best.get("lon", ""),
            "wikidata_lat": wd.get("lat", ""),
            "wikidata_lon": wd.get("lon", ""),
            "dist_km": rec.get("dist_km", ""),
            "verdict": rec.get("verdict", ""),
            "verdict_note": rec.get("verdict_note", ""),
            "n_queries": len(rec.get("queries") or []),
            "checked_at": rec.get("checked_at", ""),
        })
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def build_query_log(records):
    log = []
    for rec in records:
        for q in rec.get("queries") or []:
            log.append({
                "issue": rec.get("github_issue"),
                "name": q.get("name"),
                "year": q.get("year"),
                "feature_type": q.get("feature_type"),
                "source": q.get("source"),
                "parent": q.get("parent"),
                "expected_total": q.get("total"),
            })
    with open(QUERY_LOG_PATH, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=2)


def main():
    records = load_records()
    report = build_report(records)
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write(report)
    build_csv(records)
    build_query_log(records)
    print(f"loaded {len(records)} record(s)")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote {CSV_PATH}")
    print(f"wrote {QUERY_LOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
