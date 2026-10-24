#!/usr/bin/env python3
"""Build the systematic master-list section from the volume JSON tables.

Usage:
    python3 make_master_section.py [--data-dir DIR] [--out FILE]

Prints (or writes) a markdown section, grouped by ARSI volume, that the Lead
appends to the Obsidian master list.
"""
import argparse
import glob
import json
import os
import re
import sys

DEFAULT_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

VOLUME_TITLES = {
    "LUS-39": "LUS. 39 — Catálogos breves, 1579-1686",
    "LUS-40": "LUS. 40 — miscelânea (séc. XVIII): catálogo de 1691 e listas de 1760-1795",
    "LUS-40a": "LUS. 40 a — Catálogos de 1741 e 1742",
    "LUS-40b": "LUS. 40 b — Status impresso de 1760 e catálogo de 1775",
    "LUS-41": "LUS. 41 — Catalogus generalis Assistenciae Lusitaniae, 1768",
    "LUS-42": "LUS. 42 — Catálogo alfabético de 1577",
    "LUS-43": "LUS. 43 II a/b — Catálogos 1548-1589",
    "LUS-44": "LUS. 44 I-II — Catálogos trienais 1587-1645",
    "LUS-45": "LUS. 45 — Catálogos 1649-1676",
    "LUS-46": "LUS. 46 — Catálogos 1678-1696",
    "LUS-46a": "LUS. 46 a — Catálogo I de 1700",
    "LUS-47": "LUS. 47 — Catálogos 1700-1726",
}
VOLUME_ORDER = ["LUS-39", "LUS-40", "LUS-40a", "LUS-40b", "LUS-41", "LUS-42",
                "LUS-43", "LUS-44", "LUS-45", "LUS-46", "LUS-46a", "LUS-47"]


def vol_key(data):
    folders = data.get("volume_folder") or []
    text = " ".join(folders) + " " + (data.get("volume_note") or "")
    m = re.search(r"LUS[.\s-]*(\d+)", text)
    return int(m.group(1)) if m else 999


def folio_key(entry):
    m = re.match(r"^0*(\d+)(v)?", str(entry.get("folio_start", "")))
    return (int(m.group(1)) if m else 10**6, 1 if m and m.group(2) else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=DEFAULT_DATA_DIR)
    ap.add_argument("--out")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.data_dir, "*.json")))
    if not files:
        print(f"no JSON in {args.data_dir}", file=sys.stderr)
        return 1
    tables = []
    total = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        def link_name(e):
            if e.get("note"):
                return e["note"]
            existing = e.get("existing_note") or ""
            base = existing.split("/")[-1]
            if base.endswith(".md"):
                base = base[:-3]
            return base or None
        for e in data.get("catalogues", []):
            if not e.get("note") and e.get("existing_note"):
                e["_link"] = link_name(e)
        entries = [e for e in data.get("catalogues", []) if link_name(e)]
        if not entries:
            continue
        entries.sort(key=lambda e: (folio_key(e), str(e.get("year"))))
        total += len(entries)
        tables.append((vol_key(data), data, entries, os.path.basename(path)))
    def order(item):
        name = item[3].replace(".json", "")
        return (VOLUME_ORDER.index(name) if name in VOLUME_ORDER else 99, name)
    tables.sort(key=order)

    lines = [
        "## Índice sistemático por volume (gerado 2026-10-22)",
        "",
        "> Completa o índice cronológico acima com todas as entradas verificadas "
        "volume a volume. Cada linha liga à nota que insere as imagens. "
        "Gerado a partir de `extras/ARSI-catalogs-indexes/data/*.json`; "
        "ver também `extras/ARSI-catalogs-indexes/reports/`.",
        "",
    ]
    for _, data, entries, filename in tables:
        folder = ", ".join(data.get("volume_folder") or [])
        base = filename.replace(".json", "")
        title = VOLUME_TITLES.get(base) or data.get("volume_title") or data.get("volume_note") or filename
        lines += [f"### {title}", ""]
        if folder:
            lines += [f"Pasta: `{folder}`", ""]
        lines += ["| Ano | Tipo | Fólios | Nota |", "|---|---|---|---|"]
        for e in entries:
            mark = "" if e.get("verified") is True else " ⚠️"
            desc = (e.get("description") or "").replace("|", "/").strip()
            if desc:
                desc = " — " + desc
            fs = e.get("folio_stamped_start") or e.get("folio_start", "")
            fe = e.get("folio_stamped_end") or e.get("folio_end", "")
            local = (e.get("local") or "").strip()
            if local:
                desc = f" ({local})" + desc
            lines.append(
                f"| {e.get('year','')} | {e.get('type','')} | "
                f"{fs}-{fe} | "
                f"[[{link_name(e)}]]{mark}{desc} |"
            )
        extra = []
        if data.get("gaps"):
            extra.append(f"**Lacunas:** {data['gaps']}")
        if data.get("unaccounted"):
            extra.append(f"**Fólios não atribuídos:** {data['unaccounted']}")
        if extra:
            lines += [""] + extra
        lines += [""]
    lines += [f"*Total: {total} catálogos em {len(tables)} volumes.*", ""]
    text = "\n".join(lines)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"written {args.out} ({total} catalogues, {len(tables)} volumes)")
    else:
        print(text)


if __name__ == "__main__":
    sys.exit(main())
