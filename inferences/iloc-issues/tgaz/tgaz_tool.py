#!/usr/bin/env python3
"""Small command-line client for the CHGIS Temporal Gazetteer (TGAZ).

This is the working tool for the TGAZ pass over ``inferences/iloc-issues``.
It is deliberately dependency-free (standard library only) so it runs with any
Python 3.9+.  It mirrors the TGAZ functions in ``notebooks/dehergne_util.py``
(``tgaz_query`` / ``tgaz_get`` / ``tgaz_results_to_records``) but adds two
things needed for the issue work:

* a ``wd`` command that fetches Wikidata P625 coordinates + labels, so a TGAZ
  point can be compared with the Wikidata anchor used in the issue files;
* a ``dist`` command implementing the haversine distance.

Commands
--------
    query NAME [--year Y] [--ft FT] [--src SRC]
        Faceted TGAZ search.  Prints every hit as a compact line plus the
        machine-readable JSON when --json is given.
    get SYS_ID
        Fetch the canonical record (spellings, feature type, temporal span,
        coordinates, historical parent chain, present location, source note).
    wd QID [QID ...]
        Fetch Wikidata label (en/zh) and P625 coordinates.
    dist LAT1 LON1 LAT2 LON2
        Haversine distance in km.

Notes verified live against https://chgis.hudci.org/tgaz (2026-10):
* name search is a *prefix* match ("Hue" also matches 湖耳...), so check the
  returned name;
* pinyin and Chinese characters both work; European spellings do not;
* the ``year`` facet silently drops records whose span end is recorded as 0
  ("open ended"), so also query without ``year`` and read the span yourself;
* TGAZ integrates several source layers: CHGIS (China 222 BC-1911, with
  village-level ``cun zhen`` records only in the 1820 and 1911 layers), HGR
  (Historical Gazetteer of the Russian Empire, 1785-1796), TBRC (Tibetan
  monasteries).  Japan, Korea, Vietnam, the Philippines, Europe and Indonesia
  are not covered.
* canonical JSON can contain raw control characters in the source note, so it
  is decoded with ``json.loads(..., strict=False)``.

Usage examples
--------------
    python3 tgaz_tool.py query "呂家莊"
    python3 tgaz_tool.py query "Xiangtan" --year 1706
    python3 tgaz_tool.py get hvd_135137
    python3 tgaz_tool.py wd Q1015480
    python3 tgaz_tool.py dist 37.94665 115.43684 37.94231 115.21181
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

TGAZ_BASE_URL = "https://chgis.hudci.org/tgaz"
TGAZ_VALID_YEARS = (-222, 1911)
USER_AGENT = "dehergne-tgaz-iloc/1.0 (research; joaquim.carvalho@mpu.edu.mo)"
WD_API = "https://www.wikidata.org/w/api.php"
TIMEOUT = 45


def _fetch(url, timeout=TIMEOUT, retries=3, retry_delay=2.0):
    last = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
            if attempt < retries:
                time.sleep(retry_delay * attempt)
    raise RuntimeError(f"request failed after {retries} attempts: {url} ({last})")


def _parse_xy(xy):
    if not xy:
        return None, None
    parts = str(xy).split(",")
    if len(parts) != 2:
        return None, None
    try:
        return float(parts[0]), float(parts[1])
    except ValueError:
        return None, None


def _to_int(value):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def tgaz_query(name, year=None, feature_type=None, source=None, parent=None,
               fmt="json"):
    """Faceted search.  Returns the parsed JSON dict."""
    if not name:
        raise ValueError("tgaz_query requires a name")
    params = {"n": name}
    if year is not None:
        year = int(year)
        lo, hi = TGAZ_VALID_YEARS
        if year < lo or year > hi:
            raise ValueError(f"year {year} outside TGAZ valid range {lo}..{hi}")
        params["yr"] = year
    for key, value in (("ftyp", feature_type), ("src", source), ("p", parent)):
        if value is not None:
            params[key] = value
    params["fmt"] = fmt
    url = f"{TGAZ_BASE_URL}/placename?{urllib.parse.urlencode(params)}"
    raw = _fetch(url)
    if not raw.strip():
        return {
            "memo": f"Empty response for query matching key '{name}%'",
            "count of displayed results": "0",
            "count of total results": "0",
            "placenames": [],
        }
    return json.loads(raw, strict=False)


def tgaz_get(sys_id, fmt="json"):
    """Canonical record by TGAZ identifier (e.g. hvd_135137)."""
    if not sys_id:
        raise ValueError("sys_id is required")
    url = f"{TGAZ_BASE_URL}/placename/{fmt}/{sys_id}"
    raw = _fetch(url)
    return json.loads(raw, strict=False)


def tgaz_results_to_records(response):
    """Normalise a faceted-search response into a list of flat dicts."""
    placenames = response.get("placenames", []) if isinstance(response, dict) else []
    records = []
    for p in placenames:
        years = (p.get("years") or "").strip()
        year_from = year_to = None
        if "~" in years:
            parts = years.split("~")
            year_from = _to_int(parts[0])
            year_to = _to_int(parts[1]) if len(parts) > 1 else None
        lon, lat = _parse_xy(p.get("xy coordinates"))
        records.append({
            "name": p.get("name", ""),
            "transcription": p.get("transcription", ""),
            "sys_id": p.get("sys_id", ""),
            "uri": p.get("uri", ""),
            "year_from": year_from,
            "year_to": year_to,
            "years": years,
            "parent_sys_id": p.get("parent sys_id", ""),
            "parent_name": p.get("parent name", ""),
            "feature_type": p.get("feature type", ""),
            "object_type": p.get("object type", ""),
            "lon": lon,
            "lat": lat,
            "data_source": p.get("data source", ""),
        })
    return records


def wd_entity(qid):
    """Fetch label(s) and P625 coordinates for a Wikidata item."""
    params = {
        "action": "wbgetentities",
        "ids": qid,
        "props": "labels|claims|descriptions",
        "languages": "en|zh|pt",
        "format": "json",
    }
    url = f"{WD_API}?{urllib.parse.urlencode(params)}"
    data = json.loads(_fetch(url))
    ent = data.get("entities", {}).get(qid, {})
    if not ent:
        return {"wikidata_id": qid, "error": "not found"}
    labels = {k: v.get("value") for k, v in ent.get("labels", {}).items()}
    claims = ent.get("claims", {}).get("P625", [])
    coord = None
    if claims:
        value = claims[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
        coord = {"lat": value.get("latitude"), "lon": value.get("longitude")}
    return {
        "wikidata_id": qid,
        "labels": labels,
        "coordinates": coord,
        "uri": f"https://www.wikidata.org/wiki/{qid}",
    }


def haversine_km(lat1, lon1, lat2, lon2):
    if any(v is None for v in (lat1, lon1, lat2, lon2)):
        return None
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return round(2 * 6371.0 * math.asin(math.sqrt(a)), 2)


def canonical_summary(record):
    """Flatten a canonical TGAZ record into the fields the issue notes need."""
    spellings = [s.get("written form") for s in record.get("spellings", [])]
    ft = record.get("feature_type", {}) or {}
    temp = record.get("temporal", {}) or {}
    spatial = record.get("spatial", {}) or {}
    context = record.get("historical_context", {}) or {}
    parents = []
    for p in context.get("part of", []) or []:
        parents.append({
            "name": p.get("name"),
            "transcribed": p.get("transcribed"),
            "parent_id": p.get("parent id"),
            "begin": p.get("begin year"),
            "end": p.get("end year"),
        })
    present = [
        {"text": p.get("text"), "source": p.get("source"), "country": p.get("country code")}
        for p in spatial.get("present_location", []) or []
    ]
    note = (record.get("source note") or "").strip()
    return {
        "sys_id": record.get("sys_id"),
        "uri": record.get("uri"),
        "spellings": spellings,
        "feature_type": {
            "name": ft.get("name"),
            "alternate": ft.get("alternate name"),
            "transcription": ft.get("transcription"),
            "english": ft.get("English"),
        },
        "temporal": {
            "begin": temp.get("begin"),
            "begin_rule": temp.get("begin rule"),
            "end": temp.get("end"),
            "end_rule": temp.get("end rule"),
        },
        "lat": _to_float(spatial.get("latitude")),
        "lon": _to_float(spatial.get("longitude")),
        "present_location": present,
        "parents": parents,
        "data_source": record.get("data source"),
        "source_note": note,
    }


def _to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description="TGAZ / Wikidata lookup tool")
    sub = parser.add_subparsers(dest="command", required=True)

    q = sub.add_parser("query", help="faceted TGAZ placename search")
    q.add_argument("name")
    q.add_argument("--year", type=int, default=None)
    q.add_argument("--ft", "--feature-type", dest="feature_type", default=None)
    q.add_argument("--src", "--source", dest="source", default=None)
    q.add_argument("--parent", default=None)
    q.add_argument("--json", action="store_true", help="emit raw JSON only")

    g = sub.add_parser("get", help="canonical TGAZ record by sys_id")
    g.add_argument("sys_id")
    g.add_argument("--json", action="store_true")
    g.add_argument("--full", action="store_true", help="include the source note")

    w = sub.add_parser("wd", help="Wikidata item label + P625 coordinates")
    w.add_argument("qids", nargs="+")
    w.add_argument("--json", action="store_true")

    d = sub.add_parser("dist", help="haversine distance in km")
    d.add_argument("lat1", type=float)
    d.add_argument("lon1", type=float)
    d.add_argument("lat2", type=float)
    d.add_argument("lon2", type=float)

    args = parser.parse_args(argv)

    if args.command == "query":
        response = tgaz_query(
            name=args.name,
            year=args.year,
            feature_type=args.feature_type,
            source=args.source,
            parent=args.parent,
        )
        records = tgaz_results_to_records(response)
        if args.json:
            print(json.dumps({
                "query": {
                    "name": args.name,
                    "year": args.year,
                    "feature_type": args.feature_type,
                    "source": args.source,
                    "parent": args.parent,
                },
                "memo": response.get("memo"),
                "total": response.get("count of total results"),
                "records": records,
            }, ensure_ascii=False, indent=2))
            return 0
        print(f"# query name={args.name!r} year={args.year} ft={args.feature_type} "
              f"src={args.source} parent={args.parent}")
        print(f"# {response.get('memo')}  (total {response.get('count of total results')})")
        for rec in records:
            print(
                f"{rec['sys_id']:>10} | {rec['name']} | {rec['transcription']} | "
                f"{rec['years']} | {rec['feature_type']} | parent={rec['parent_name']} | "
                f"({rec['lat']}, {rec['lon']}) | src={rec['data_source']}"
            )
        if not records:
            print("(no records)")
        return 0

    if args.command == "get":
        record = tgaz_get(args.sys_id)
        summary = canonical_summary(record)
        if not args.full:
            summary["source_note"] = summary["source_note"][:600]
        if args.json:
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 0
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    if args.command == "wd":
        result = [wd_entity(qid.strip()) for qid in args.qids]
        print(json.dumps(result if len(result) > 1 else result[0],
                         ensure_ascii=False, indent=2))
        return 0

    if args.command == "dist":
        print(haversine_km(args.lat1, args.lon1, args.lat2, args.lon2))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
