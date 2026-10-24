#!/usr/bin/env python3
"""Build a portable, self-contained index package inside the digitalisation root.

Creates, next to the `LUS. NN/` image folders:

    INDICE-sistematico-por-volume.md   (entry point, relative links)
    catalogos/<note>.md                 (one file per catalogue, relative image links)
    catalogos/_assets/                  (any image that lived outside the root)

Everything uses *relative* paths, so the whole root folder can be copied to
another disk/location and still work (Obsidian, VS Code, GitHub, a browser, etc.).

Usage:
    python3 make_portable_package.py [--dest DIR] [--dry-run]
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
import unicodedata
import urllib.parse

DIGI = "/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19"
VAULT = "/Users/jrc/jrc-notes"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
INDEX_NAME = "INDICE-sistematico-por-volume.md"
CHRONO_NAME = "INDICE-cronologico.md"
TYPOLOGY_NAME = "TIPOLOGIA.md"
CAT_DIR = "catalogos"
ASSET_SUBDIR = "_assets"
NOTE_DIRS = ["03 Projectos", "01 Notes", "04 Biographies"]

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
TYPE_ORDER = ["T1", "T1S", "T1P", "T2", "T2P", "T3", "T3P", "T4", "T4P", "T5", "T5A", "T5B",
              "T6", "T6T7", "T7", "T8", "T9", "T10", "T10P", "T11"]

VOLUME_HEADINGS = {
    "LUS-39": "LUS 39", "LUS-40": "LUS 40", "LUS-40a": "LUS 40 a",
    "LUS-40b": "LUS 40 b", "LUS-41": "LUS 41", "LUS-42": "LUS 42",
    "LUS-43": "LUS 43 II a/b", "LUS-44": "LUS 44 I-II", "LUS-45": "LUS 45",
    "LUS-46": "LUS 46", "LUS-46a": "LUS 46 a", "LUS-47": "LUS 47",
}
VOLUME_SUBTITLES = {
    "LUS-39": "Catálogos breves, 1579-1686",
    "LUS-40": "miscelânea (séc. XVIII): catálogo de 1691 e listas de 1760-1795",
    "LUS-40a": "Catálogos de 1741 e 1742",
    "LUS-40b": "Status impresso de 1760 e catálogo de 1775",
    "LUS-41": "Catalogus generalis Assistenciae Lusitaniae, 1768",
    "LUS-42": "Catálogo alfabético de 1577",
    "LUS-43": "Catálogos 1548-1589",
    "LUS-44": "Catálogos trienais 1587-1645",
    "LUS-45": "Catálogos 1649-1676",
    "LUS-46": "Catálogos 1678-1696",
    "LUS-46a": "Catálogo I de 1700",
    "LUS-47": "Catálogos 1700-1726",
}
VOLUME_ORDER = ["LUS-39", "LUS-40", "LUS-40a", "LUS-40b", "LUS-41", "LUS-42",
                "LUS-43", "LUS-44", "LUS-45", "LUS-46", "LUS-46a", "LUS-47"]

ICLOUD_PREFIX = "/Users/jrc/Library/Mobile Documents/com~apple~CloudDocs/Documents/"
IMG_FILE_RE = re.compile(r"!\[([^\]]*)\]\((file://[^)]+)\)")
LINK_FILE_RE = re.compile(r"\[([^\]]+)\]\((file://[^)]+)\)")
IMG_REL_RE = re.compile(r"!\[([^\]]*)\]\((?!file://|https?://)([^)]+)\)")
LINK_REL_RE = re.compile(r"\[([^\]]+)\]\((?!file://|https?://)([^)]+)\)")
WIKI_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def nfc(text):
    return unicodedata.normalize("NFC", text)


def note_path(name):
    for d in NOTE_DIRS:
        for root, _dirs, files in os.walk(os.path.join(VAULT, d)):
            if name + ".md" in files:
                return os.path.join(root, name + ".md")
    return None


def entry_name(entry):
    if entry.get("note"):
        return entry["note"]
    existing = entry.get("existing_note") or ""
    return existing.split("/")[-1].replace(".md", "") or None


def build_file_index(root):
    """basename (NFC) -> list of paths relative to root, excluding catalogos/."""
    idx = {}
    skip = os.path.abspath(os.path.join(root, CAT_DIR))
    for dirpath, _dirs, files in os.walk(root):
        ap = os.path.abspath(dirpath)
        if ap == skip or ap.startswith(skip + os.sep):
            continue
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".pdf")):
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                idx.setdefault(nfc(f), []).append(rel)
    return idx


def score_folder(relpath, note_name):
    folder = os.path.dirname(relpath)
    parts = [p for p in re.split(r"[^a-z0-9]+", folder.lower()) if p]
    note = re.sub(r"[^a-z0-9]+", "", note_name.lower())
    return sum(1 for p in parts if p in note)


class PackageBuilder:
    def __init__(self, dest, package_names, dry_run=False):
        self.dest = dest
        self.cat_dir = os.path.join(dest, CAT_DIR)
        self.assets_dir = os.path.join(self.cat_dir, ASSET_SUBDIR)
        self.package_names = package_names
        self.file_index = build_file_index(dest)
        self.dry_run = dry_run
        self.assets = {}
        self.missing = []

    def relative_for_url(self, url):
        path = urllib.parse.unquote(url[len("file://"):])
        path = path.replace(ICLOUD_PREFIX, "/Users/jrc/Documents/")
        marker = "v2-2025-01-19/"
        if marker in path:
            rel = nfc(path.split(marker, 1)[1])
            if os.path.exists(os.path.join(self.dest, rel)):
                return "../" + urllib.parse.quote(rel)
            if os.path.exists(os.path.join(self.dest, nfc(rel))):
                return "../" + urllib.parse.quote(nfc(rel))
            # look in the sibling "pdfs-deprecated" folder (loose PDFs moved out of v2)
            fallback = os.path.join(os.path.dirname(self.dest), "pdfs-deprecated",
                                    os.path.basename(path))
            if os.path.exists(fallback):
                base = os.path.basename(fallback)
                self.assets[nfc(base)] = fallback
                return f"{ASSET_SUBDIR}/{urllib.parse.quote(base)}"
            return None
        if os.path.exists(path):
            base = os.path.basename(path)
            self.assets[nfc(base)] = path
            return f"{ASSET_SUBDIR}/{urllib.parse.quote(base)}"
        return None

    def relative_for_name(self, target, note_name):
        base = nfc(os.path.basename(urllib.parse.unquote(target)))
        candidates = self.file_index.get(base)
        if not candidates:
            return None
        if len(candidates) == 1:
            return "../" + urllib.parse.quote(candidates[0])
        best = max(candidates, key=lambda rel: score_folder(rel, note_name))
        if score_folder(best, note_name) > 0:
            return "../" + urllib.parse.quote(best)
        return None

    def rewrite(self, text, name):
        fm = ""
        body = text
        if text.startswith("---\n"):
            end = text.find("\n---", 4)
            if end != -1:
                fm, body = text[:end + 4], text[end + 4:].lstrip("\n")

        def img_file(m):
            alt, url = m.group(1), m.group(2)
            rel = self.relative_for_url(url)
            if rel is None:
                base = os.path.basename(urllib.parse.unquote(url))
                self.missing.append((name, base))
                return f"*[não incluída na digitalização: {base}]*"
            return f"![{alt}]({rel})"

        body = IMG_FILE_RE.sub(img_file, body)

        def link_file(m):
            label, url = m.group(1), m.group(2)
            rel = self.relative_for_url(url)
            if rel is None:
                self.missing.append((name, url))
                return label
            return f"[{label}]({rel})"

        body = LINK_FILE_RE.sub(link_file, body)

        def img_rel(m):
            alt, target = m.group(1), m.group(2)
            if target.startswith(("../", ASSET_SUBDIR + "/")):
                return m.group(0)
            rel = self.relative_for_name(target, name)
            if rel is None:
                base = os.path.basename(urllib.parse.unquote(target))
                self.missing.append((name, base))
                return f"*[não incluída na digitalização: {base}]*"
            return f"![{alt}]({rel})"

        body = IMG_REL_RE.sub(img_rel, body)

        def link_rel(m):
            label, target = m.group(1), m.group(2)
            if target.startswith(("../", ASSET_SUBDIR + "/")):
                return m.group(0)
            rel = self.relative_for_name(target, name)
            if rel is not None:
                return f"[{label}]({rel})"
            decoded = nfc(urllib.parse.unquote(target)).split("/")[-1]
            if decoded.endswith(".md"):
                decoded = decoded[:-3]
            if decoded in self.package_names:
                return f"[{label}]({urllib.parse.quote(decoded)}.md)"
            return label

        body = LINK_REL_RE.sub(link_rel, body)

        def wiki(m):
            target = m.group(1).strip()
            label = (m.group(2) or target).strip()
            if target in self.package_names:
                return f"[{label}]({urllib.parse.quote(target)}.md)"
            return label

        body = WIKI_RE.sub(wiki, body)
        body = body.replace("[[]]", "")
        if not re.search(r"^# ", body, re.M):
            body = f"# {name}\n\n" + body
        return (fm + "\n\n" if fm else "") + body.rstrip() + f"\n\n---\n[← Voltar ao índice](../{INDEX_NAME})\n"


def slugify(text):
    """GitHub / VS Code markdown heading slug (github-slugger-compatible enough)."""
    s = text.lower()
    s = re.sub(r"[\u2000-\u206F\u2E00-\u2E7F\\'!\"#$%&()*+,./:;<=>?@\[\]^`{|}~]", "", s)
    return s.replace(" ", "-")


def vol_short(base):
    return {"LUS-39": "LUS. 39", "LUS-40": "LUS. 40", "LUS-40a": "LUS. 40 a",
            "LUS-40b": "LUS. 40 b", "LUS-41": "LUS. 41", "LUS-42": "LUS. 42",
            "LUS-43": "LUS. 43", "LUS-44": "LUS. 44", "LUS-45": "LUS. 45",
            "LUS-46": "LUS. 46", "LUS-46a": "LUS. 46 a", "LUS-47": "LUS. 47"}.get(base, base)


def year_key(entry):
    text = str(entry.get("year") or "")
    m = re.search(r"(\d{4})", text)
    year = int(m.group(1)) if m else 9999
    type_order = TYPE_ORDER.index(entry.get("type")) if entry.get("type") in TYPE_ORDER else 99
    return (year, type_order, text, str(entry.get("folio_start")))


def build_chronological(tables):
    rows = []
    for base, _data, entries in tables:
        for e in entries:
            rows.append((base, e))
    rows.sort(key=lambda item: year_key(item[1]))
    lines = [
        "# ARSI Lusitania — índice cronológico dos catálogos",
        "",
        "> Todos os catálogos indexados, ordenados por ano e atravessando os volumes "
        "(LUS. 39 a LUS. 47). Cada linha liga ao catálogo (nota com as imagens) e à "
        "secção do volume no índice sistemático.",
        ">",
        "> **Ver também:** [Índice sistemático por volume](INDICE-sistematico-por-volume.md) · "
        "[Tipologia dos catálogos (T1, T4, T5…)](TIPOLOGIA.md) · "
        "[**versão HTML para browser**](index.html) · "
        "[Relatórios por volume e resumo](reports/README.md)",
        "",
        "| Ano | Tipo | Volume | Fólios | Catálogo | Índice do volume |",
        "|---|---|---|---|---|---|",
    ]
    for base, e in rows:
        name = entry_name(e)
        fs = e.get("folio_stamped_start") or e.get("folio_start", "")
        fe = e.get("folio_stamped_end") or e.get("folio_end", "")
        mark = "" if e.get("verified") is True else " ⚠️"
        heading = VOLUME_HEADINGS.get(base, base)
        volume_link = f"[{vol_short(base)}]({INDEX_NAME}#{slugify(heading)})"
        note_link = f"[{name}]({CAT_DIR}/{urllib.parse.quote(name)}.md)"
        lines.append(
            f"| {e.get('year','')} | {e.get('type','')} | {volume_link} | {fs}-{fe} | "
            f"{note_link}{mark} | {volume_link} |"
        )
    lines += ["", f"*Total: {len(rows)} catálogos em {len(tables)} volumes.*", ""]
    return "\n".join(lines)


TYPOLOGY = """# Tipologia dos catálogos jesuítas (T1, T2, … T11)

> Tipologia de trabalho usada neste índice para classificar os catálogos das
> digitalizações ARSI *Lusitania*. **Não é uma sigla do ARSI**: é a grelha adotada
> no projeto (inspirada na prática dos catálogos jesuítas e no
> [Jesuit Catalogs Database](https://jesuitcatalogs.bc.edu/project/)) para
> descrever o conteúdo de cada documento. O sufixo **P** indica uma versão
> **parcial** (por exemplo, só uma comunidade ou só um grupo de pessoas).

**Ver também:** [Índice sistemático por volume](INDICE-sistematico-por-volume.md) · [Índice cronológico](INDICE-cronologico.md) · [**versão HTML para browser**](index.html)

| Tipo | Designação | O que contém | Exemplos |
|---|---|---|---|
| **T1** | Catálogo primeiro | Lista geral, numerada, por comunidade e residência, com informação pessoal (naturalidade, idade, tempo de Companhia, estudos, ofícios, apreciação). É a base prosopográfica. | [1649-T1-LUS-45-C8](catalogos/1649-T1-LUS-45-C8.md) |
| **T1S** | T1 sem comunidades | Como o T1, mas sem divisão interna por casas/comunidades: não permite saber onde cada pessoa estava. | [1577-T1S-LUS-42-f1](catalogos/1577-T1S-LUS-42-f1.md) |
| **T2** | Catálogo segundo (secreto) | A mesma lista do T1, mas **sem nomes** nem comunidades visíveis: números com apreciações (Complexio, Prudentia, Ingenium, Talentum…). Cruzado com o T1, permite ler as avaliações. | [1649-T2-LUS-45-C29](catalogos/1649-T2-LUS-45-C29.md) |
| **T3** | Catálogo terceiro / «de casas» | Informação geral das comunidades (totais de pessoas, rendas, obrigações, ministérios), **sem nomes**. | [1599-T3-LUS-39-c19](catalogos/1599-T3-LUS-39-c19.md) |
| **T4** | Catálogo breve | Lista por comunidade, com nomes e funções/ministérios, **sem avaliação**; inclui mestres, estudantes e o que estudam. É o tipo mais frequente para seguir a distribuição anual. | [1579-T4-LUS-39-1](catalogos/1579-T4-LUS-39-1.md) |
| **T5** | Índice alfabético | Índice do catálogo primeiro, com nome, fólio e número. **T5A** = índice geral, sem distinguir comunidades; **T5B** = índice por comunidade. | [1649-T5-LUS-45-C1](catalogos/1649-T5-LUS-45-C1.md) |
| **T6** | Suplemento do T1 | Entrados ao longo do ano (noviços), com a informação pessoal do T1. | [1678-T6-LUS-46-22](catalogos/1678-T6-LUS-46-22.md) |
| **T7** | Suplemento do T2 | Entrados ao longo do ano, na forma «secreta» do T2 (avaliações sem nomes). | [1594-T6T7-LUS-44-I-105](catalogos/1594-T6T7-LUS-44-I-105.md) |
| **T8** | Defuntos e despedidos | Lista separada dos que morreram, saíram ou foram despedidos no período. | [1693-T8-LUS-46-300](catalogos/1693-T8-LUS-46-300.md) |
| **T9** | Pessoas nas missões | Lista das pessoas em missão (Índia, China, Brasil, etc.), com o lugar. | [1652-T9-Elenchus-Missiones-LUS-45-51](catalogos/1652-T9-Elenchus-Missiones-LUS-45-51.md) |
| **T10** | Listas parcelares | Listas com um fim específico: recebidos num intervalo, superiores, elenchos, informações para professos, etc. | [1600-1652-T10-Superiores-LUS-45-73](catalogos/1600-1652-T10-Superiores-LUS-45-73.md) |
| **T11** | Sumários e notas | Contagens, sumários, memoriais e notas variadas, geralmente sem nomes. | [1651-T11-Memoriale-Visitatore-LUS-45-170](catalogos/1651-T11-Memoriale-Visitatore-LUS-45-170.md) |

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


def load_tables():
    tables = []
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        entries = [e for e in data.get("catalogues", []) if entry_name(e)]
        if not entries:
            continue
        base = os.path.basename(path)[:-5]
        tables.append((base, data, entries))
    tables.sort(key=lambda t: VOLUME_ORDER.index(t[0]) if t[0] in VOLUME_ORDER else 99)
    return tables


def build_index(tables):
    lines = [
        "# ARSI Lusitania — índice sistemático por volume",
        "",
        "> Índice dos catálogos contidos nas digitalizações ARSI *Lusitania* "
        "(vols. 39-47), gerado a 2026-10-22. Cada linha liga a uma nota em "
        f"`{CAT_DIR}/` que insere as páginas do catálogo.",
        ">",
        f"> **Pacote autónomo:** este ficheiro + `{CAT_DIR}/` + as pastas `LUS. NN/` "
        "com as imagens. Todos os caminhos são **relativos** — a pasta pode ser "
        "copiada para outro disco ou local e continua a funcionar.",
        "",
        "## Como usar",
        "",
        "1. Abrir este ficheiro num leitor de Markdown (Obsidian, VS Code, etc.).",
        f"2. Clicar no nome do catálogo para abrir a nota em `{CAT_DIR}/`.",
        "3. Os embeds `![…]` de cada nota apontam para `../LUS. NN/…` (imagens originais).",
        "4. Os links para secções usam as **âncoras nativas dos títulos Markdown** "
        "(por exemplo `…-por-volume.md#lus-39`), que funcionam em GitHub, VS Code, "
        "Pandoc, MkDocs, etc.",
        "",
        "**Ver também:** [Índice cronológico](INDICE-cronologico.md) · "
        "[Tipologia dos catálogos (T1, T4, T5…)](TIPOLOGIA.md) · "
        "[**versão HTML para browser**](index.html) · "
        "[Relatórios por volume e resumo](reports/README.md)",
        "",
        "---",
        "",
    ]
    total = 0
    for base, data, entries in tables:
        heading = VOLUME_HEADINGS.get(base, base)
        subtitle = VOLUME_SUBTITLES.get(base, "")
        folders = data.get("volume_folder") or []
        lines += [f"## {heading}", ""]
        if subtitle:
            lines += [f"*{subtitle}*", ""]
        if folders:
            lines += ["Pastas: " + ", ".join(f"`{f}`" for f in folders), ""]
        lines += ["| Ano | Tipo | Fólios | Catálogo |", "|---|---|---|---|"]

        def fkey(e):
            m = re.match(r"^0*(\d+)", str(e.get("folio_start") or ""))
            return (int(m.group(1)) if m else 10**6, str(e.get("year")))

        for e in sorted(entries, key=fkey):
            name = entry_name(e)
            mark = "" if e.get("verified") is True else " ⚠️"
            desc = (e.get("description") or e.get("title") or "").replace("|", "/").strip()
            desc = f" — {desc}" if desc else ""
            link = f"{CAT_DIR}/{urllib.parse.quote(name)}.md"
            lines.append(
                f"| {e.get('year','')} | {e.get('type','')} | "
                f"{e.get('folio_stamped_start') or e.get('folio_start','')}-"
                f"{e.get('folio_stamped_end') or e.get('folio_end','')} | "
                f"[{name}]({link}){mark}{desc} |"
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
    lines += [
        "---",
        "",
        f"*Total: {total} catálogos em {len(tables)} volumes. "
        f"Fonte: índice gerado em 2026-10-22 a partir das digitalizações "
        f"`v2-2025-01-19`; notas originais no vault Obsidian.*",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", default=DIGI)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tables = load_tables()
    names = {entry_name(e) for _b, _d, entries in tables for e in entries if entry_name(e)}
    builder = PackageBuilder(args.dest, names, dry_run=args.dry_run)
    if not args.dry_run:
        os.makedirs(builder.cat_dir, exist_ok=True)

    copied = 0
    for _base, _data, entries in tables:
        for e in entries:
            name = entry_name(e)
            src = note_path(name)
            if not src:
                print("MISSING VAULT NOTE:", name)
                continue
            out = builder.rewrite(open(src, encoding="utf-8").read(), name)
            copied += 1
            if not args.dry_run:
                with open(os.path.join(builder.cat_dir, name + ".md"), "w", encoding="utf-8") as fh:
                    fh.write(out)

    index = build_index(tables)
    if args.dry_run:
        print(index[:800])
    else:
        with open(os.path.join(args.dest, INDEX_NAME), "w", encoding="utf-8") as fh:
            fh.write(index)
        with open(os.path.join(args.dest, CHRONO_NAME), "w", encoding="utf-8") as fh:
            fh.write(build_chronological(tables))
        with open(os.path.join(args.dest, TYPOLOGY_NAME), "w", encoding="utf-8") as fh:
            fh.write(TYPOLOGY)
        if builder.assets:
            os.makedirs(builder.assets_dir, exist_ok=True)
            for base, src in builder.assets.items():
                shutil.copy2(src, os.path.join(builder.assets_dir, base))

    print(f"\nnotes: {copied} | external assets: {len(builder.assets)} | unresolved links: {len(builder.missing)}")
    if builder.missing:
        for name, target in builder.missing[:40]:
            print("  unresolved:", name, "->", target)
    print("DEST:", args.dest)


if __name__ == "__main__":
    main()
