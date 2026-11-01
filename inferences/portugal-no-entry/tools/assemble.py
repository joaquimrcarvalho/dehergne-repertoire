#!/usr/bin/env python3
"""Assemble the final per-person notes from the research results.

    python3 tools/assemble.py                 # all results present
    python3 tools/assemble.py deh-diogo-pinto # one person

Reads:
  tools/packets.json            Timelink DB + Obsidian packet per person
  results/<id>.json             research result written by the subagents
Writes:
  <id>.md                       the final note (this folder)
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from datetime import date

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # portugal-no-entry/
TOOLS = os.path.join(HERE, "tools")
RESULTS = os.path.join(HERE, "results")
ARCHIVE = os.environ.get("PHA_ARCHIVE_DIR", "/Users/jrc/jesuit-archive")
DB = os.path.join(ARCHIVE, "archive.db")

CONF_ORDER = {"alta": "alta", "média": "média", "media": "média", "baixa": "baixa", "nenhuma": "nenhuma"}

VAULT = "/Users/jrc/jrc-notes"


def _vault_index() -> set[str]:
    """All note names in the vault (basename without .md), for wikilink checks."""
    names: set[str] = set()
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in {"copilot", "attachments"}]
        for f in files:
            if f.endswith(".md"):
                names.add(f[:-3])
    return names


VAULT_NOTES = _vault_index()


def fix_wikilinks(text: str) -> str:
    """Keep [[Note]] only when the note exists in the vault; else plain text."""
    if not text:
        return text

    def repl(m: re.Match) -> str:
        target = m.group(1)
        label = m.group(2) or target
        base = target.split("/")[-1].split("#")[0].strip()
        if base in VAULT_NOTES:
            return f"[[{target}{'|' + label if m.group(2) else ''}]]"
        return label

    return re.sub(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]", repl, text)


def load_packets() -> dict:
    with open(os.path.join(TOOLS, "packets.json"), encoding="utf-8") as fh:
        return json.load(fh)


def bib_for(doc_ids: set[int]) -> dict[int, dict]:
    out: dict[int, dict] = {}
    try:
        conn = sqlite3.connect(f"file:{DB}?mode=ro&immutable=1", uri=True)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error:
        return out
    for did in doc_ids:
        r = conn.execute(
            """select d.id, d.filename, d.dir_path, d.page_count, b.citation, b.record_origin
               from documents d left join document_bibliography b on b.document_id = d.id
               where d.id = ?""",
            (did,),
        ).fetchone()
        if r:
            out[did] = dict(r)
    return out


def fmt_date(d: str) -> str:
    d = (d or "").strip()
    if not d or d == "0":
        return "—"
    if len(d) == 8:
        y, m, dd = d[:4], d[4:6], d[6:]
        if m == "00" and dd == "00":
            return y
        if m == "00":
            return f"{y}?"
        if dd == "00":
            return f"{y}-{m}"
        return f"{y}-{m}-{dd}"
    return d


def timeline_table(packet: dict) -> str:
    rows = []
    for a in sorted(
        packet["timeline"], key=lambda x: ((x["d"] or "0").ljust(8, "0"), x["t"])
    ):
        value = (a["v"] or "").strip()
        if a["t"].endswith("@wikidata"):
            label = a["t"].replace("@wikidata", "")
            value = f"[{value.rsplit('/', 1)[-1]}]({value})"
            t = f"{label} (wikidata)"
        else:
            t = a["t"]
        if a["obs"]:
            value += f" — *obs:* {a['obs'].strip()}"
        rows.append((fmt_date(a["d"]), t, value))
    if not rows:
        return "_sem atributos na base._"
    out = ["| Data | Atributo | Valor |", "|---|---|---|"]
    for d, t, v in rows:
        out.append(f"| {d} | `{t}` | {v} |")
    return "\n".join(out)


def evidence_block(res: dict, bibs: dict[int, dict]) -> tuple[str, list[str]]:
    """Return the markdown for the evidence section and the footnote lines."""
    lines: list[str] = []
    footnotes: list[str] = []
    n = 0
    for ev in res.get("evidencias") or []:
        cit = (ev.get("citacao") or "").strip()
        if not cit:
            continue
        n += 1
        cmd = (ev.get("comando") or "").strip()
        proves = (ev.get("o_que_prova") or "").strip()
        forca = (ev.get("forca") or "").strip()
        suffix = f" · `{cmd}`" if cmd else ""
        if forca:
            suffix += f" · prova {forca}"
        lines.append(f"- {cit}{suffix}")
        if proves:
            lines.append(f"  - {proves}")
        footnotes.append(f"[^{n}]: {cit}" + (f" — `{cmd}`" if cmd else ""))
    return "\n".join(lines), footnotes


def doc_reference_line(ev: dict, bibs: dict[int, dict]) -> str | None:
    cit = ev.get("citacao") or ""
    m = re.search(r"doc\s+(\d+)", cit)
    if not m:
        return None
    did = int(m.group(1))
    b = bibs.get(did)
    if not b:
        return None
    if b.get("citation"):
        return f"- **doc {did}** — {b['citation']}" + (f" ({b['record_origin']})" if b.get("record_origin") else "")
    return None


def build_note(pid: str, packet: dict, res: dict, bibs: dict[int, dict]) -> str:
    name = packet["name"] or pid
    lugar = res.get("lugar") or "não determinado"
    data = res.get("data") or "—"
    conf = CONF_ORDER.get((res.get("confianca") or "nenhuma").strip().lower(), "nenhuma")
    sugestao = res.get("sugestao_tabela") or (packet["obsidian_rows"][0]["suggestion"] or "").strip() or "—"
    validacao = res.get("validacao") or ""
    surname = name.split()[-1].lower()

    parts: list[str] = []
    parts.append("---")
    parts.append(f"title: {name} — lugar de entrada")
    parts.append(f"person_id: {pid}")
    parts.append(f"name: {name}")
    parts.append(f"dehergne_no: {packet['dehergne_no']}")
    parts.append("nationality: Portugal")
    parts.append(f"entry_place: {lugar}")
    parts.append(f"entry_date: {data}")
    parts.append(f"confidence: {conf}")
    parts.append('source: "[[0 Portugal no entry]]"')
    parts.append(f"created: {date.today().isoformat()}")
    parts.append("tags: [dehergne, jesuita-entrada, portugal, china]")
    parts.append("---")
    parts.append("")
    parts.append(f"# {name} (`{pid}`)")
    parts.append("")
    parts.append(f"**Lugar de entrada: {lugar}** — {data} (confiança: **{conf}**).")
    if sugestao and sugestao != "—":
        parts.append("")
        parts.append(f"> Sugestão na tabela [[0 Portugal no entry]]: **{sugestao}**" + (f" — {validacao}" if validacao else ""))
    parts.append("")
    if res.get("resumo"):
        parts.append(res["resumo"].strip())
        parts.append("")

    parts.append("## Identificação")
    parts.append("")
    parts.append("| | |")
    parts.append("|---|---|")
    parts.append(f"| id Timelink | `{pid}` |")
    parts.append(f"| Dehergne | nº {packet['dehergne_no']} |")
    parts.append(f"| Nacionalidade | Portugal |")
    parts.append(f"| Fonte (.cli) | `{packet['source']}` (linha {packet.get('line')}) |")
    je = "; ".join(f"`{a['v']}` / {a['d']}" for a in packet["current_jesuita_entrada"]) or "—"
    parts.append(f"| `jesuita-entrada` na base | {je} |")
    row = packet["obsidian_rows"][0]
    parts.append(f"| Embarque | {row['embarque']} |")
    parts.append(f"| Ficha Obsidian | `{packet['vault_note']}` |")
    parts.append("")

    # quick comparison table
    deh_txt = packet["dehergne_text"] or ""
    m = re.search(r"\bE\.\s*([^,\(\.]{1,28})", deh_txt)
    deh_e = m.group(1).strip() if m else "—"
    parts.append("| | valor |")
    parts.append("|---|---|")
    parts.append(f"| Dehergne, entrada (`E.`) | {deh_e} |")
    parts.append(f"| Base Timelink (actual) | {je} |")
    parts.append(f"| Tabela Obsidian (sugestão) | {sugestao} |")
    parts.append(f"| **Proposta desta nota** | **{lugar}** — {data} ({conf}) |")
    parts.append("")

    parts.append("## 1. Notícia de Dehergne (base Timelink)")
    parts.append("")
    txt = (packet["dehergne_text"] or "").strip()
    if txt:
        parts.append("> " + txt.replace("\n", "\n> "))
    else:
        parts.append("_sem texto._")
    if packet["dehergne_no"]:
        parts.append("")
        parts.append(
            f"Dehergne (doc 65, nº {packet['dehergne_no']}) — ver `/Users/jrc/jesuit-archive/dropbox/collections/reference-works/"
            f"Joseph Dehergne - 1973 - Répertoire des Jésuites de Chine, de 1542 à 1800.pdf`."
        )
    parts.append("")

    parts.append("## 2. Biografia")
    parts.append("")
    parts.append((res.get("biografia") or "").strip() or "_a completar._")
    parts.append("")

    parts.append("## 3. Cronologia (base Timelink)")
    parts.append("")
    parts.append(timeline_table(packet))
    parts.append("")

    parts.append("## 4. Verificação no arquivo pha")
    parts.append("")
    analise = res.get("analise") or []
    if analise:
        for i, sec in enumerate(analise, 1):
            titulo = (sec.get("titulo") or f"Ponto {i}").strip()
            parts.append(f"### 4.{i} {titulo}")
            parts.append("")
            parts.append((sec.get("texto") or "").strip())
            parts.append("")
    else:
        parts.append("_sem análise registada._")
        parts.append("")

    if res.get("nao_encontrado"):
        parts.append("### O que não foi encontrado")
        parts.append("")
        parts.append(res["nao_encontrado"].strip())
        parts.append("")

    parts.append("## 5. Evidência")
    parts.append("")
    ev_md, _ = evidence_block(res, bibs)
    parts.append(ev_md or "_sem evidência._")
    parts.append("")

    parts.append("## 6. Referências")
    parts.append("")
    refs = res.get("refs_obsidian") or ["[[0 Portugal no entry]]", f"[[{pid}]]"]
    for r in refs:
        parts.append(f"- {r}")
    for ev in res.get("evidencias") or []:
        line = doc_reference_line(ev, bibs)
        if line:
            parts.append(line)
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("Ver também: [[0 Portugal no entry]]")
    parts.append("")
    return fix_wikilinks("\n".join(parts))


def main() -> int:
    packets = load_packets()
    targets = sys.argv[1:] or sorted(
        p[:-5] for p in os.listdir(RESULTS) if p.endswith(".json")
    )
    doc_ids: set[int] = set()
    loaded: list[tuple[str, dict]] = []
    for pid in targets:
        rp = os.path.join(RESULTS, f"{pid}.json")
        if not os.path.exists(rp):
            print(f"!! no result for {pid}", file=sys.stderr)
            continue
        with open(rp, encoding="utf-8") as fh:
            res = json.load(fh)
        loaded.append((pid, res))
        for ev in res.get("evidencias") or []:
            m = re.search(r"doc\s+(\d+)", ev.get("citacao") or "")
            if m:
                doc_ids.add(int(m.group(1)))
    bibs = bib_for(doc_ids)
    for pid, res in loaded:
        if pid not in packets:
            print(f"!! unknown id {pid}", file=sys.stderr)
            continue
        note = build_note(pid, packets[pid], res, bibs)
        out = os.path.join(HERE, f"{pid}.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(note)
        print(f"wrote {out} ({len(note)} chars, place={res.get('lugar')!r}, conf={res.get('confianca')!r})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
