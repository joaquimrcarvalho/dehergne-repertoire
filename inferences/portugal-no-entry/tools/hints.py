#!/usr/bin/env python3
"""Generate per-person hint files for the no-suggestion group.

For every person without a provisional place of entry, run the archive search on
the plausible name variants and write `hints/<id>.md`: packet summary, Obsidian
ficha extract and every archive hit with enough context to decide what to read in
full.

    python3 tools/hints.py            # all missing
    python3 tools/hints.py deh-...    # selected
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
import unicodedata

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(HERE, "tools")
HINTS = os.path.join(HERE, "hints")
ARCHIVE = os.environ.get("PHA_ARCHIVE_DIR", "/Users/jrc/jesuit-archive")
DB = os.path.join(ARCHIVE, "archive.db")

STOP = {"de", "da", "do", "dos", "das", "e"}


def strip_ac(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def variants(name: str) -> list[str]:
    out = []
    base = name.strip()
    if not base:
        return out
    parts = base.split()
    out.append(base)
    out.append(strip_ac(base))

    def add(s: str) -> None:
        if s and s not in out:
            out.append(s)

    # first-name variants
    first = parts[0]
    fmaps = {
        "António": ["Antonio", "Antônio", "Ant.onio", "Antº"],
        "João": ["Joao", "Ioão", "Ioao", "Juan", "Giovanni", "Joannes", "Ioannes"],
        "Manuel": ["Manoel", "Emanuel", "Emmanuel", "Manuel"],
        "Francisco": ["Fran.co", "Franciscus", "Francesco"],
        "Pedro": ["Pero", "Pierre", "Petrus"],
        "Diogo": ["Diego", "Didaco", "Didacus", "Jacobus"],
        "Luís": ["Luis", "Ludovicus", "Aloysius", "Luiz"],
        "José": ["Jose", "Joseph", "Josephus", "Giuseppe"],
        "Inácio": ["Inacio", "Ignacio", "Ignatius", "Ignazio"],
        "Gonçalo": ["Goncalo", "Gonzalo", "Gundisalvus"],
        "Jerónimo": ["Jeronimo", "Hieronimo", "Hieronymus", "Girolamo"],
        "Bartolomeu": ["Bartolomeu", "Bartholomeu", "Bartholomaeus", "Bartolomeo"],
        "Estêvão": ["Estevao", "Stephanus", "Stefano", "Esteban"],
        "Félix": ["Felix", "Felice"],
        "Tomé": ["Tome", "Thomas", "Tomas"],
        "Domingos": ["Domingos", "Domingo", "Dominicus"],
        "Agostinho": ["Agostinho", "Agustin", "Augustinus", "Agostino"],
        "Bento": ["Bento", "Benedictus", "Benedetto"],
        "Caetano": ["Caetano", "Caietano", "Cajetanus"],
    }
    for k, vs in fmaps.items():
        if strip_ac(first) == strip_ac(k) or first == k:
            for v in vs:
                add(base.replace(first, v, 1))
    # surname-only search (may be too noisy but useful with the FTS ranking)
    if len(parts) >= 2:
        add(parts[-1])
    return out[:8]


def obsidian_extract(pid: str) -> str:
    path = f"/Users/jrc/jrc-notes/04 Biographies/dehergne/{pid}.md"
    if not os.path.exists(path):
        return ""
    txt = open(path, encoding="utf-8").read()
    head = txt.split("### Timeline")[0]
    return head[:2500]


def main() -> int:
    os.makedirs(HINTS, exist_ok=True)
    packets = json.load(open(os.path.join(TOOLS, "packets.json"), encoding="utf-8"))
    targets = sys.argv[1:] or [
        pid
        for pid, p in packets.items()
        if not (p["obsidian_rows"][0]["suggestion"] or "").strip()
    ]
    conn = sqlite3.connect(f"file:{DB}?mode=ro&immutable=1", uri=True)
    conn.row_factory = sqlite3.Row
    for pid in sorted(targets):
        p = packets[pid]
        name = p["name"]
        lines = [f"# Hints — {name} (`{pid}`)", ""]
        lines.append(f"Dehergne nº {p['dehergne_no']} · fonte `{p['source']}` · ficha `{p['vault_note']}`")
        row = p["obsidian_rows"][0]
        lines.append(
            f"Embarque: {row['embarque']} · jesuita-entrada (BD): "
            + "; ".join(f"{a['v']}/{a['d']}" for a in p["current_jesuita_entrada"])
            + f" · nascimento: {row['nasc']} ({row['nasc_date']})"
        )
        lines.append("")
        lines.append("## Dehergne (base Timelink)")
        lines.append("")
        lines.append("> " + (p["dehergne_text"] or "").replace("\n", "\n> "))
        lines.append("")
        lines.append("## Ficha Obsidian (excerto)")
        lines.append("")
        lines.append(obsidian_extract(pid) or "_sem ficha._")
        lines.append("")
        lines.append("## Resultados no arquivo pha")
        lines.append("")
        seen = set()
        for v in variants(name):
            try:
                rows = conn.execute(
                    """select d.id doc, d.filename, d.dir_path, d.page_count, p.page_no, ch.variant, ch.text
                       from chunks_fts f join chunks ch on ch.id=f.rowid
                       join pages p on p.id=ch.page_id join documents d on d.id=ch.document_id
                       where chunks_fts match ? order by rank limit 24""",
                    (f'"{v}"',),
                ).fetchall()
            except sqlite3.OperationalError:
                continue
            pat = re.compile(re.escape(v), re.IGNORECASE)
            n = 0
            for r in rows:
                text = r["text"] or ""
                m = pat.search(text)
                if not m:
                    continue
                key = (r["doc"], r["page_no"], r["variant"])
                if key in seen:
                    continue
                seen.add(key)
                s = max(0, m.start() - 300)
                e = min(len(text), m.end() + 300)
                lines.append(
                    f"- **{v}** → doc {r['doc']} ({r['filename']}) p.{r['page_no']}/{r['page_count']} "
                    f"[{r['variant']}] ({r['dir_path']})"
                )
                lines.append(f"  > {text[s:e].replace(chr(10), ' ')}")
                n += 1
                if n >= 6:
                    break
        open(os.path.join(HINTS, f"{pid}.md"), "w", encoding="utf-8").write("\n".join(lines))
        print(f"hint {pid}: {len(lines)} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
