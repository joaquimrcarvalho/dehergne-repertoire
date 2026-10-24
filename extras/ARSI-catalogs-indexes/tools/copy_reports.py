#!/usr/bin/env python3
"""Copy the volume reports + summary into the digitalisation root (`reports/`).

Source: extras/ARSI-catalogs-indexes/reports/*.md
Dest:   <digitalisation-root>/reports/*.md  (+ generated README.md index)

The HTML versions are produced by make_html_package.py.
"""
import glob
import os
import shutil
import sys
import urllib.parse

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reports")
DEST = "/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19"
MAIN_INDEX = "INDICE-sistematico-por-volume.html"

DESCRIPTIONS = {
    "SUMMARY": "Resumo geral: números por volume, fontes, lacunas, decisões pendentes e nota operacional sobre o iCloud.",
    "CORRECTIONS": "Registo das correções aplicadas ao índice (com histórico por catálogo).",
    "LUS-39": "Índice dactilografado do LUS. 39 (23 catálogos, 1579–1686); desvio de foliação.",
    "LUS-40": "LUS. 40 / 40a / 40b: os três volumes distintos (registo de 1691, catálogos de 1741–42, Status de 1760 + catálogo de 1775).",
    "LUS-41": "LUS. 41: Catalogus generalis Assistenciae Lusitaniae, 1768 (catálogo files 3–196).",
    "LUS-42": "LUS. 42: catálogo alfabético de 1577 (volume único).",
    "LUS-43": "LUS. 43 II a/b: catálogos 1548–1589, sem índice dactilografado; mapeamento ficheiro↔fólio.",
    "LUS-44": "LUS. 44 I–II: catálogos trienais 1587–1645; desvios de foliação e lacunas.",
    "LUS-45": "LUS. 45: catálogos 1649–1676 a partir do índice dactilografado em três páginas.",
    "LUS-46": "LUS. 46 / 46a: catálogos 1678–1696 e o Catálogo I de 1700.",
    "LUS-47": "LUS. 47: catálogos 1700–1726; fólios 253–349 não digitalizados.",
}


def main():
    if not os.path.isdir(SRC):
        print("no reports dir:", SRC)
        return 1
    dest = os.path.join(DEST, "reports")
    os.makedirs(dest, exist_ok=True)
    files = sorted(glob.glob(os.path.join(SRC, "*.md")))
    corrections = os.path.join(os.path.dirname(SRC), "CORRECTIONS.md")
    if os.path.exists(corrections):
        files.append(corrections)
    copied = []
    for path in files:
        name = os.path.basename(path)
        shutil.copy2(path, os.path.join(dest, name))
        copied.append(name)
    print("copied:", ", ".join(copied))

    # README index
    lines = [
        "# Relatórios de indexação — ARSI Lusitania",
        "",
        "> Relatórios por volume e resumo geral do índice dos catálogos. "
        "Versão Markdown (a versão HTML está em `index.html` nesta pasta).",
        "",
        f"**Ver também:** [índice sistemático](../INDICE-sistematico-por-volume.md) · "
        f"[índice cronológico](../INDICE-cronologico.md) · [tipologia](../TIPOLOGIA.md)",
        "",
        "| Relatório | Conteúdo |",
        "|---|---|",
    ]
    ordered = ([f for f in copied if f == "SUMMARY.md"]
               + [f for f in copied if f.startswith("LUS-")]
               + [f for f in copied if f == "CORRECTIONS.md"])
    for name in ordered:
        base = name[:-3]
        desc = DESCRIPTIONS.get(base, "")
        lines.append(f"| [{base}]({urllib.parse.quote(name)}) | {desc} |")
    lines += ["", f"*{len(copied)} relatórios copiados de `extras/ARSI-catalogs-indexes/reports/`.*", ""]
    with open(os.path.join(dest, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("wrote", os.path.join(dest, "README.md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
