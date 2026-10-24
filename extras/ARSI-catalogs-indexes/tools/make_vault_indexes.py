#!/usr/bin/env python3
"""Generate the same portable indexes as Obsidian notes (wikilinks, heading anchors).

Creates in /Users/jrc/jrc-notes/03 Projectos/:
  - Índice sistemático por volume (gerado 2026-10-22).md
  - Índice cronológico dos catálogos ARSI Lusitania.md
  - Tipologia dos catálogos jesuítas (T1-T11).md
"""
import glob
import json
import os
import re
import sys
import unicodedata

VAULT = "/Users/jrc/jrc-notes"
OUT = os.path.join(VAULT, "03 Projectos")
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
SYS_NOTE = "Índice sistemático por volume (gerado 2026-10-22)"
CHRONO_NOTE = "Índice cronológico dos catálogos ARSI Lusitania"
TYPOLOGY_NOTE = "Tipologia dos catálogos jesuítas (T1-T11)"
MASTER = "03.03.01.01 ARSI Lusitania - catálogos - digitalizados - em curso"

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
VOLUME_ORDER = list(VOLUME_TITLES)
TYPE_ORDER = ["T1", "T1S", "T1P", "T2", "T2P", "T3", "T3P", "T4", "T4P", "T5", "T5A", "T5B",
              "T6", "T6T7", "T7", "T8", "T9", "T10", "T10P", "T11"]


def entry_name(entry):
    if entry.get("note"):
        return entry["note"]
    return (entry.get("existing_note") or "").split("/")[-1].replace(".md", "") or None


def load_tables():
    tables = []
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        entries = [e for e in data.get("catalogues", []) if entry_name(e)]
        if entries:
            tables.append((os.path.basename(path)[:-5], data, entries))
    tables.sort(key=lambda t: VOLUME_ORDER.index(t[0]) if t[0] in VOLUME_ORDER else 99)
    return tables


def fkey(e):
    m = re.match(r"^0*(\d+)", str(e.get("folio_start") or ""))
    return (int(m.group(1)) if m else 10**6, str(e.get("year")))


def year_key(e):
    text = str(e.get("year") or "")
    m = re.search(r"(\d{4})", text)
    year = int(m.group(1)) if m else 9999
    t = TYPE_ORDER.index(e.get("type")) if e.get("type") in TYPE_ORDER else 99
    return (year, t, text, str(e.get("folio_start")))


def build_systematic(tables):
    lines = [
        f"# {SYS_NOTE}",
        "",
        "> Índice dos catálogos contidos nas digitalizações ARSI *Lusitania* "
        "(vols. 39-47). Cada linha liga à nota que insere as páginas do catálogo. "
        "Esta nota é a versão com **âncoras por volume**, usada pelo índice cronológico.",
        "",
        f"**Ver também:** [[{CHRONO_NOTE}]] · [[{TYPOLOGY_NOTE}]] · "
        f"[[{MASTER}]]",
        "",
        "---",
        "",
    ]
    total = 0
    for base, data, entries in tables:
        heading = VOLUME_TITLES.get(base, base)
        folders = data.get("volume_folder") or []
        lines += [f"## {heading}", ""]
        if folders:
            lines += ["Pastas: " + ", ".join(f"`{f}`" for f in folders), ""]
        lines += ["| Ano | Tipo | Fólios | Catálogo |", "|---|---|---|---|"]
        for e in sorted(entries, key=fkey):
            name = entry_name(e)
            mark = "" if e.get("verified") is True else " ⚠️"
            desc = (e.get("description") or e.get("title") or "").replace("|", "/").strip()
            desc = f" — {desc}" if desc else ""
            lines.append(
                f"| {e.get('year','')} | {e.get('type','')} | "
                f"{e.get('folio_stamped_start') or e.get('folio_start','')}-"
                f"{e.get('folio_stamped_end') or e.get('folio_end','')} | "
                f"[[{name}]]{mark}{desc} |"
            )
            total += 1
        extra = []
        if data.get("gaps"):
            extra.append(f"**Lacunas:** {data['gaps']}")
        if data.get("unaccounted"):
            extra.append(f"**Fólios não atribuídos:** {data['unaccounted']}")
        if extra:
            lines += [""] + extra
        lines += [""]
    lines += ["---", "", f"*Total: {total} catálogos em {len(tables)} volumes.*", ""]
    return "\n".join(lines)


def build_chrono(tables):
    rows = [(base, e) for base, _d, entries in tables for e in entries]
    rows.sort(key=lambda item: year_key(item[1]))
    lines = [
        f"# {CHRONO_NOTE}",
        "",
        "> Todos os catálogos indexados, ordenados por ano e atravessando os volumes "
        "(LUS. 39 a LUS. 47). Cada linha liga ao catálogo e à secção do volume no "
        "[[Índice sistemático por volume (gerado 2026-10-22)|índice sistemático]].",
        "",
        f"**Ver também:** [[{SYS_NOTE}]] · [[{TYPOLOGY_NOTE}]]",
        "",
        "| Ano | Tipo | Volume | Fólios | Catálogo |",
        "|---|---|---|---|---|",
    ]
    for base, e in rows:
        name = entry_name(e)
        fs = e.get("folio_stamped_start") or e.get("folio_start", "")
        fe = e.get("folio_stamped_end") or e.get("folio_end", "")
        mark = "" if e.get("verified") is True else " ⚠️"
        heading = VOLUME_TITLES.get(base, base)
        vol_link = f"[[{SYS_NOTE}#{heading}]]"
        lines.append(f"| {e.get('year','')} | {e.get('type','')} | {vol_link} | {fs}-{fe} | [[{name}]]{mark} |")
    lines += ["", f"*Total: {len(rows)} catálogos em {len(tables)} volumes.*", ""]
    return "\n".join(lines)


def typology():
    return f"""# {TYPOLOGY_NOTE}

> Tipologia de trabalho usada no índice dos catálogos das digitalizações ARSI
> *Lusitania*. **Não é uma sigla do ARSI**: é a grelha adotada no projeto,
> inspirada na prática dos catálogos jesuítas e no
> [Jesuit Catalogs Database](https://jesuitcatalogs.bc.edu/project/), para
> descrever o conteúdo de cada documento. O sufixo **P** indica versão
> **parcial** (só uma comunidade ou só um grupo de pessoas).

**Ver também:** [[{SYS_NOTE}]] · [[{CHRONO_NOTE}]]

| Tipo | Designação | O que contém | Exemplos |
|---|---|---|---|
| **T1** | Catálogo primeiro | Lista geral, numerada, por comunidade e residência, com informação pessoal (naturalidade, idade, tempo de Companhia, estudos, ofícios, apreciação). É a base prosopográfica. | [[1649-T1-LUS-45-C8]] |
| **T1S** | T1 sem comunidades | Como o T1, mas sem divisão interna por casas: não permite saber onde cada pessoa estava. | [[1577-T1S-LUS-42-f1]] |
| **T2** | Catálogo segundo (secreto) | A mesma lista do T1, mas **sem nomes** nem comunidades: números com apreciações (Complexio, Prudentia, Ingenium, Talentum…). Cruzado com o T1, permite ler as avaliações. | [[1649-T2-LUS-45-C29]] |
| **T3** | Catálogo terceiro / «de casas» | Informação geral das comunidades (totais de pessoas, rendas, obrigações, ministérios), **sem nomes**. | [[1599-T3-LUS-39-c19]] |
| **T4** | Catálogo breve | Lista por comunidade, com nomes e funções/ministérios, **sem avaliação**; inclui mestres, estudantes e o que estudam. É o tipo mais frequente para seguir a distribuição anual. | [[1579-T4-LUS-39-1]] |
| **T5** | Índice alfabético | Índice do catálogo primeiro, com nome, fólio e número. **T5A** = índice geral, sem distinguir comunidades; **T5B** = índice por comunidade. | [[1649-T5-LUS-45-C1]] |
| **T6** | Suplemento do T1 | Entrados ao longo do ano (noviços), com a informação pessoal do T1. | [[1678-T6-LUS-46-22]] |
| **T7** | Suplemento do T2 | Entrados ao longo do ano, na forma «secreta» do T2 (avaliações sem nomes). | [[1594-T6T7-LUS-44-I-105]] |
| **T8** | Defuntos e despedidos | Lista separada dos que morreram, saíram ou foram despedidos no período. | [[1693-T8-LUS-46-300]] |
| **T9** | Pessoas nas missões | Lista das pessoas em missão (Índia, China, Brasil, etc.), com o lugar. | [[1652-T9-Elenchus-Missiones-LUS-45-51]] |
| **T10** | Listas parcelares | Listas com um fim específico: recebidos num intervalo, superiores, elencos, informações para professos, etc. | [[1600-1652-T10-Superiores-LUS-45-73]] |
| **T11** | Sumários e notas | Contagens, sumários, memoriais e notas variadas, geralmente sem nomes. | [[1651-T11-Memoriale-Visitatore-LUS-45-170]] |

## Como usar a tipologia

1. **T1 + T2** do mesmo ano lidos em paralelo dão a lista nominal e as avaliações.
2. **T4** (breve) é o melhor ponto de partida para seguir pessoas e ofícios ano a ano.
3. **T3** e **T11** dão o quadro institucional (casas, totais, rendas, notas).
4. **T5** acelera a procura de uma pessoa dentro de um catálogo grande.
5. **T6/T7/T8** completam o T1/T2 com os movimentos do ano (entradas, mortes, saídas).
6. **T10/T9** cobrem listas temáticas (missões, superiores, professos).

> A classificação de alguns documentos é discutível (por exemplo, catálogos
> «breves» que também dão apreciações); nesses casos o índice indica o tipo
> atribuído e, quando existe, a classificação da nota antiga. As entradas
> marcadas com ⚠️ têm atribuição inferida e aguardam confirmação.
"""


def main():
    tables = load_tables()
    notes = {
        SYS_NOTE: build_systematic(tables),
        CHRONO_NOTE: build_chrono(tables),
        TYPOLOGY_NOTE: typology(),
    }
    for name, text in notes.items():
        path = os.path.join(OUT, name + ".md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
