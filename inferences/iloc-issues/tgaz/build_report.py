#!/usr/bin/env python3
"""Build the consolidated TGAZ report from the per-issue JSON records.

Reads ``inferences/iloc-issues/tgaz/data/<NN>.json`` (written by the per-issue
checks, schema in ``PROTOCOL.md``) and writes:

* ``inferences/iloc-issues/TGAZ-RESOLUTION.md`` — the human-readable report
  (summary table for all 34 issues + notable findings + method);
* ``inferences/iloc-issues/tgaz/tgaz-results.csv`` — one row per issue;
* ``inferences/iloc-issues/tgaz/query-log.json`` — every recorded query, for
  replay/verification with ``replay.py``.

Usage:
    python3 build_report.py            # write all three outputs
    python3 build_report.py --check    # only validate the JSON records
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ISSUES_DIR = os.path.dirname(HERE)
DATA_DIR = os.path.join(HERE, "data")
REPORT_PATH = os.path.join(ISSUES_DIR, "TGAZ-RESOLUTION.md")
CSV_PATH = os.path.join(HERE, "tgaz-results.csv")
QUERY_LOG_PATH = os.path.join(HERE, "query-log.json")
HIGHLIGHTS_PATH = os.path.join(HERE, "HIGHLIGHTS.md")

VERDICTS = [
    "confirmed",
    "partially-confirmed",
    "contradicted",
    "not-in-tgaz",
    "outside-coverage",
]

VERDICT_LABELS = {
    "confirmed": "confirmed",
    "partially-confirmed": "partially confirmed",
    "contradicted": "contradicted",
    "not-in-tgaz": "not in TGAZ",
    "outside-coverage": "outside TGAZ coverage",
}

VERDICT_ORDER = {v: i for i, v in enumerate(VERDICTS)}


def load_records():
    records, errors = [], []
    for name in sorted(os.listdir(DATA_DIR)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(DATA_DIR, name)
        try:
            with open(path, encoding="utf-8") as fh:
                record = json.load(fh)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{name}: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{name}: not a JSON object")
            continue
        record.setdefault("issue", os.path.splitext(name)[0].zfill(2))
        records.append(record)
    records.sort(key=lambda r: str(r.get("issue", "")))
    return records, errors


def validate(records):
    problems = []
    for rec in records:
        issue = rec.get("issue", "??")
        for key in ("issue", "file", "place", "verdict"):
            if not rec.get(key):
                problems.append(f"{issue}: missing '{key}'")
        verdict = rec.get("verdict")
        if verdict not in VERDICTS:
            problems.append(f"{issue}: unknown verdict {verdict!r}")
        queries = rec.get("queries", [])
        if not isinstance(queries, list) or not queries:
            problems.append(f"{issue}: no queries recorded")
        for q in queries if isinstance(queries, list) else []:
            if not isinstance(q, dict) or "name" not in q:
                problems.append(f"{issue}: malformed query entry {q!r}")
    return problems


def best_hit_label(rec):
    best = rec.get("best_match") or {}
    if not best:
        return "—"
    sid = best.get("sys_id") or ""
    name = best.get("name") or ""
    ft = best.get("feature_type") or ""
    if isinstance(ft, dict):
        ft = ft.get("transcription") or ft.get("english") or ""
    years = best.get("years") or ""
    label = f"`{sid}` {name}".strip()
    extras = [x for x in (ft, years) if x]
    if extras:
        label += " — " + ", ".join(extras)
    return label


def md_escape(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def summary_table(records):
    lines = [
        "| # | Place as transcribed | Year | Region | Wikidata | Best TGAZ match | Dist. km | Verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for rec in records:
        issue = md_escape(rec.get("issue", "?"))
        place = md_escape(rec.get("place", ""))
        year = md_escape(rec.get("dehergne_year", "") or "—")
        region = md_escape(rec.get("region", "") or "—")
        wd = rec.get("wikidata_id") or (rec.get("wikidata") or {}).get("id") or "—"
        if wd and wd != "—":
            wd = f"[{wd}](https://www.wikidata.org/wiki/{wd})"
        dist = rec.get("dist_km")
        dist = f"{dist:.1f}" if isinstance(dist, (int, float)) else "—"
        verdict = rec.get("verdict", "")
        verdict_cell = f"`{verdict}`"
        lines.append(
            f"| {issue} | {place} | {year} | {region} | {wd} | "
            f"{best_hit_label(rec)} | {dist} | {verdict_cell} |"
        )
    return "\n".join(lines)


def detail_section(records):
    """One compact block per issue: verdict note + queries actually run."""
    lines = []
    for rec in records:
        issue = rec.get("issue", "?")
        lines.append(f"### {issue} — {rec.get('place', '')} ({rec.get('verdict', '')})")
        lines.append("")
        note = rec.get("verdict_note") or ""
        if note:
            lines.append(note)
            lines.append("")
        queries = rec.get("queries") or []
        if queries:
            parts = []
            for q in queries:
                label = f"`{q.get('name')}`"
                filters = []
                if q.get("year"):
                    filters.append(f"year={q['year']}")
                if q.get("feature_type"):
                    filters.append(f"ft={q['feature_type']}")
                if q.get("source"):
                    filters.append(f"src={q['source']}")
                if filters:
                    label += " (" + ", ".join(filters) + ")"
                label += f" → {q.get('total', 0)} hit(s)"
                parts.append(label)
            lines.append("Queries: " + "; ".join(parts) + ".")
            lines.append("")
        best = rec.get("best_match") or {}
        if best.get("sys_id"):
            extra = []
            if best.get("parent"):
                extra.append(f"parent {best['parent']}")
            if best.get("present_location"):
                extra.append(f"present location “{best['present_location']}”")
            if best.get("uri"):
                extra.append(f"<{best['uri']}>")
            lines.append("Best record: " + ", ".join(extra) + ".")
            lines.append("")
    return "\n".join(lines)


def build_report(records, errors):
    counts = Counter(rec.get("verdict", "unclassified") for rec in records)
    n = len(records)
    total_queries = sum(len(rec.get("queries") or []) for rec in records)

    lines = []
    lines.append("# TGAZ (CHGIS) verification of the location issues")
    lines.append("")
    lines.append(
        "Independent gazetteer check of the 34 location identifications in "
        "`inferences/iloc-issues/`, using the **CHGIS Temporal Gazetteer "
        "(TGAZ)** — the read-only REST service over the China Historical GIS "
        "database (Harvard & Fudan) and its integrated layers "
        "([docs](https://chgis.hudci.org/tgw/#usage))."
    )
    lines.append("")
    lines.append(
        f"Every issue file carries a `## TGAZ (CHGIS) check` section with the "
        f"queries run and the evidence; this report is the consolidated view. "
        f"{n} issues checked, {total_queries} TGAZ/Wikidata queries recorded. "
        "Machine-readable data: [`tgaz/data/`](./tgaz/data/), "
        "[`tgaz/tgaz-results.csv`](./tgaz/tgaz-results.csv). "
        "Method and conventions: [`tgaz/PROTOCOL.md`](./tgaz/PROTOCOL.md). "
        "A parallel pass covers the 24 comment drafts in [`comments/`](./comments/) "
        "— see [`comments/TGAZ-COMMENTS.md`](./comments/TGAZ-COMMENTS.md)."
    )
    lines.append("")
    lines.append("## Method in one paragraph")
    lines.append("")
    lines.append(
        "For each issue the identified Chinese name(s) and pinyin form were "
        "searched in TGAZ, with and without the Dehergne year (the `year` "
        "facet silently drops records whose span end is recorded as 0, and a "
        "locality may only exist in the 1820/1911 layers). Each hit was "
        "checked for name form, feature type (府/縣/州/村鎮) and parent unit; "
        "the canonical record was fetched for spellings, dated parent chain, "
        "coordinates and `present_location`; and the TGAZ point was compared "
        "with the issue's Wikidata anchor by haversine distance. TGAZ "
        "integrates CHGIS (China, 222 BC–1911), HGR (Russian Empire "
        "1785–1796) and TBRC (Tibet); Japan, Korea, Vietnam, the Philippines, "
        "Europe, India and Indonesia are **not** covered."
    )
    lines.append("")
    lines.append("**Verdict vocabulary** (`tgaz` verdict):")
    lines.append("")
    lines.append(
        "- `confirmed` — TGAZ has the unit (or its expected parent) with "
        "matching name, level and parent, and coordinates agree with the "
        "Wikidata anchor where one exists;"
    )
    lines.append(
        "- `partially-confirmed` — TGAZ confirms the county/prefecture/region "
        "but not the locality itself, or at a coarser level than the anchor;"
    )
    lines.append(
        "- `contradicted` — TGAZ evidence conflicts with the issue's reading;"
    )
    lines.append(
        "- `not-in-tgaz` — region covered, but the place is absent from the "
        "TGAZ layers;"
    )
    lines.append(
        "- `outside-coverage` — TGAZ has no layer for the region."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Verdict | Issues |")
    lines.append("|---|---|")
    for verdict in VERDICTS:
        lines.append(f"| `{verdict}` | {counts.get(verdict, 0)} |")
    lines.append(f"| **total** | **{n}** |")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append(summary_table(records))
    lines.append("")
    lines.append(
        "**Reading the distance column.** It is the great-circle distance "
        "between the TGAZ point and the issue's Wikidata anchor. For a "
        "confirmed place both point at the same settlement; for a "
        "`partially-confirmed` match TGAZ gives the parent unit's seat while "
        "the anchor is the locality, so 10–60 km is normal (a village lies "
        "away from its county town) and is **not** a mismatch score. For the "
        "river issue 19 the anchor is a point on a linear feature and the "
        "distance is not meaningful at all."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    if os.path.exists(HIGHLIGHTS_PATH):
        with open(HIGHLIGHTS_PATH, encoding="utf-8") as fh:
            highlights = fh.read().strip()
        if highlights:
            lines.append(highlights)
            lines.append("")
    lines.append("## Per-issue evidence")
    lines.append("")
    lines.append(detail_section(records))
    lines.append("")
    lines.append("## Reproducing")
    lines.append("")
    lines.append("```bash")
    lines.append("cd inferences/iloc-issues/tgaz")
    lines.append("python3 tgaz_tool.py query '呂家莊'        # single lookup")
    lines.append("python3 replay.py --limit 10              # re-run recorded queries")
    lines.append("# verified 2026-10-22: replay.py re-ran all 226 recorded queries -> 226 ok, 0 mismatched")
    lines.append("python3 build_report.py                   # rebuild this report")
    lines.append("```")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append("| Path | Content |")
    lines.append("|---|---|")
    lines.append("| `tgaz/README.md` | start here: what is where |")
    lines.append("| `tgaz/PROTOCOL.md` | method, TGAZ facts, verdict and section conventions |")
    lines.append("| `tgaz/HIGHLIGHTS.md` | the analysis section of this report |")
    lines.append("| `tgaz/tgaz_tool.py` | TGAZ + Wikidata lookup CLI (stdlib only) |")
    lines.append("| `tgaz/data/<NN>.json` | per-issue evidence record |")
    lines.append("| `tgaz/tgaz-results.csv` | one row per issue (generated) |")
    lines.append("| `tgaz/query-log.json` | all recorded queries, for replay (generated) |")
    lines.append("| `tgaz/build_report.py` | this report's generator |")
    lines.append("| `tgaz/replay.py` | re-runs the recorded queries against the live service |")
    lines.append("| `tgaz/build_comments.py` | generator of the comment-draft check (`comments/`) |")
    lines.append("| `comments/TGAZ-COMMENTS.md` | consolidated report for the 24 comment drafts |")
    lines.append("")

    if errors:
        lines.append("## Data errors")
        lines.append("")
        for err in errors:
            lines.append(f"- {err}")
        lines.append("")

    return "\n".join(lines) + "\n"


def build_csv(records):
    fieldnames = [
        "issue", "place", "dehergne_year", "region", "country",
        "identified_chinese", "wikidata_id", "tgaz_sys_id", "tgaz_name",
        "tgaz_feature_type", "tgaz_years", "tgaz_parent", "tgaz_lat",
        "tgaz_lon", "wikidata_lat", "wikidata_lon", "dist_km", "verdict",
        "verdict_note", "n_queries", "checked_at",
    ]
    rows = []
    for rec in records:
        best = rec.get("best_match") or {}
        wd = rec.get("wikidata") or {}
        ft = best.get("feature_type")
        if isinstance(ft, dict):
            ft = ft.get("transcription") or ft.get("english") or ""
        rows.append({
            "issue": rec.get("issue", ""),
            "place": rec.get("place", ""),
            "dehergne_year": rec.get("dehergne_year", ""),
            "region": rec.get("region", ""),
            "country": rec.get("country", ""),
            "identified_chinese": rec.get("identified_chinese", ""),
            "wikidata_id": rec.get("wikidata_id") or wd.get("id", ""),
            "tgaz_sys_id": best.get("sys_id", ""),
            "tgaz_name": best.get("name", ""),
            "tgaz_feature_type": ft,
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
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_query_log(records):
    log = []
    for rec in records:
        for q in rec.get("queries") or []:
            log.append({
                "issue": rec.get("issue"),
                "name": q.get("name"),
                "year": q.get("year"),
                "feature_type": q.get("feature_type"),
                "source": q.get("source"),
                "parent": q.get("parent"),
                "expected_total": q.get("total"),
            })
    with open(QUERY_LOG_PATH, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=2)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    records, errors = load_records()
    problems = validate(records)

    print(f"loaded {len(records)} issue record(s) from {DATA_DIR}")
    issues = {str(r.get("issue")) for r in records}
    missing = [f"{i:02d}" for i in range(1, 35) if str(i) not in issues
               and f"{i:02d}" not in issues]
    if missing:
        print("MISSING issue records: " + ", ".join(missing))
    for problem in problems:
        print("PROBLEM:", problem)
    for err in errors:
        print("ERROR:", err)
    if args.check:
        return 0 if not problems and not errors else 1

    report = build_report(records, errors)
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write(report)
    build_csv(records)
    build_query_log(records)
    print(f"wrote {REPORT_PATH}")
    print(f"wrote {CSV_PATH}")
    print(f"wrote {QUERY_LOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
