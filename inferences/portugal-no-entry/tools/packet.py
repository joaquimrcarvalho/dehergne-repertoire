#!/usr/bin/env python3
"""Print the research packet (Timelink DB + Obsidian) for one or more people.

    python3 tools/packet.py deh-diogo-pinto deh-amador-da-costa
    python3 tools/packet.py --list            # one line per person
"""

from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACKETS = os.path.join(HERE, "packets.json")


def load() -> dict:
    with open(PACKETS, encoding="utf-8") as fh:
        return json.load(fh)


def show(pid: str, p: dict) -> None:
    print("=" * 78)
    print(f"# {p['name']}  ({pid})")
    print(f"  Dehergne nº {p['dehergne_no']} | source {p['source']} | inside {p['inside']} | line {p.get('line')}")
    print(f"  Obsidian note: {p['vault_note']}")
    for r in p["obsidian_rows"]:
        print(
            "  table row: suggestion={!r} | embarque={} | tabela jesuita-entrada={} ({}) | nascimento={} ({})".format(
                r["suggestion"], r["embarque"], r["je_table"], r["je_date"], r["nasc"], r["nasc_date"]
            )
        )
    print("  DB jesuita-entrada actual: " + "; ".join(f"{a['v']}/{a['d']}" for a in p["current_jesuita_entrada"]))
    print("-" * 78)
    print("  DEHERGNE NOTICE (from Timelink db attribute obs):")
    for line in (p["dehergne_text"] or "").splitlines():
        print("   ", line.strip())
    print("-" * 78)
    print("  TIMELINE (Timelink db attributes):")
    for a in sorted(p["timeline"], key=lambda x: (x["d"] or "0")):
        print(f"    {a['d']:>8}  {a['t']:<28} {a['v']}" + (f"   [obs: {a['obs']}]" if a["obs"] else ""))
    print()


def main() -> int:
    pk = load()
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "--list":
        for pid, p in sorted(pk.items(), key=lambda kv: (kv[1]["name"] or "")):
            sug = (p["obsidian_rows"][0]["suggestion"] or "").strip() or "-"
            print(f"{pid:<42} {p['name']:<34} sug={sug}")
        return 0
    for pid in args:
        if pid not in pk:
            print(f"!! unknown id {pid}", file=sys.stderr)
            continue
        show(pid, pk[pid])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
