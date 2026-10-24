#!/usr/bin/env python3
"""Build a browser-browsable HTML version of the portable package.

Reads the Markdown package in the digitalisation root and writes, next to it:

    index.html                          landing page
    INDICE-sistematico-por-volume.html
    INDICE-cronologico.html
    TIPOLOGIA.html
    style.css
    catalogos/<note>.html               one page per catalogue

All links/images stay relative, so the folder can still be copied anywhere and
opened with a normal browser (file://...) or served with `python3 -m http.server`.

Usage:
    python3 make_html_package.py [--dest DIR] [--dry-run]
"""
import argparse
import glob
import os
import re
import subprocess
import sys
import urllib.parse

DIGI = "/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19"
INDEX_MD = "INDICE-sistematico-por-volume.md"
CHRONO_MD = "INDICE-cronologico.md"
TYPOLOGY_MD = "TIPOLOGIA.md"
CAT_DIR = "catalogos"
STYLE = "style.css"

TEMPLATE = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title$</title>
<link rel="stylesheet" href="$css$">
</head>
<body>
$body$
</body>
</html>
"""

CSS = """
:root { --fg:#1f2328; --muted:#57606a; --bg:#ffffff; --line:#d0d7de; --accent:#8c2f1b; --soft:#f6f8fa; }
* { box-sizing: border-box; }
body { margin:0; padding:0 0 4rem; background:var(--bg); color:var(--fg);
       font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       line-height:1.55; }
nav { position:sticky; top:0; z-index:10; background:var(--soft); border-bottom:1px solid var(--line);
      padding:.6rem 1.2rem; font-size:.92rem; }
nav a { color:var(--accent); text-decoration:none; margin-right:1rem; }
nav a:hover { text-decoration:underline; }
main, body > h1, body > p, body > h2, body > h3, body > table, body > blockquote,
body > ol, body > ul, body > hr, body > div { max-width: 1150px; margin-left:auto; margin-right:auto; }
body > * { padding-left:1.2rem; padding-right:1.2rem; }
h1, h2, h3 { line-height:1.25; }
h1 { font-size:1.7rem; margin-top:1.4rem; }
h2 { font-size:1.25rem; margin-top:2rem; border-bottom:1px solid var(--line); padding-bottom:.25rem; }
h3 { font-size:1.05rem; margin-top:1.4rem; }
a { color:var(--accent); }
table { border-collapse:collapse; width:100%; margin:.8rem 0 1.4rem; font-size:.9rem; }
th, td { border:1px solid var(--line); padding:.45rem .6rem; text-align:left; vertical-align:top; }
th { background:var(--soft); position:sticky; top:2.6rem; }
tr:nth-child(even) td { background:#fbfcfd; }
blockquote { margin:.8rem 0; padding:.6rem 1rem; border-left:4px solid var(--accent); background:var(--soft); color:var(--muted); }
blockquote p { margin:.3rem 0; }
img { max-width:100%; height:auto; display:block; margin:1rem auto; border:1px solid var(--line); }
figure { margin:1rem auto; text-align:center; }
figcaption { color:var(--muted); font-size:.85rem; }
code { background:var(--soft); padding:.1rem .3rem; border-radius:4px; font-size:.9em; }
hr { border:0; border-top:1px solid var(--line); margin:2rem auto; }
.lead { color:var(--muted); font-size:1.02rem; }
.cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1rem; margin:1.5rem 0; }
.card { border:1px solid var(--line); border-radius:8px; padding:1rem 1.1rem; background:var(--soft); }
.card h3 { margin:.1rem 0 .4rem; }
.card p { margin:.2rem 0 .8rem; color:var(--muted); font-size:.92rem; }
.card a.button { display:inline-block; background:var(--accent); color:#fff; padding:.4rem .8rem; border-radius:6px; text-decoration:none; }
.stats { display:flex; gap:2rem; flex-wrap:wrap; margin:1rem 0 1.5rem; }
.stats div { font-size:.9rem; color:var(--muted); }
.stats b { display:block; font-size:1.5rem; color:var(--fg); }
footer { max-width:1150px; margin:2rem auto 0; padding:1rem 1.2rem; color:var(--muted); font-size:.85rem; border-top:1px solid var(--line); }
@media (max-width:700px) { th { position:static; } }
"""

NAV_ROOT = (
    '<nav><a href="index.html">Início</a>'
    '<a href="INDICE-sistematico-por-volume.html">Índice sistemático</a>'
    '<a href="INDICE-cronologico.html">Índice cronológico</a>'
    '<a href="TIPOLOGIA.html">Tipologia T1–T11</a>'
    '<a href="reports/README.html">Relatórios</a></nav>'
)
NAV_CAT = (
    '<nav><a href="../index.html">Início</a>'
    '<a href="../INDICE-sistematico-por-volume.html">Índice sistemático</a>'
    '<a href="../INDICE-cronologico.html">Índice cronológico</a>'
    '<a href="../TIPOLOGIA.html">Tipologia T1–T11</a>'
    '<a href="../reports/README.html">Relatórios</a></nav>'
)
NAV_REPORT = (
    '<nav><a href="../index.html">Início</a>'
    '<a href="../INDICE-sistematico-por-volume.html">Índice sistemático</a>'
    '<a href="../INDICE-cronologico.html">Índice cronológico</a>'
    '<a href="../TIPOLOGIA.html">Tipologia T1–T11</a>'
    '<a href="README.html">Relatórios</a></nav>'
)

INDEX_HTML = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ARSI Lusitania — Catálogos digitalizados</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
{nav}
<main>
<h1>ARSI Lusitania — catálogos digitalizados</h1>
<p class="lead">Índice dos catálogos contidos nas digitalizações ARSI <em>Lusitania</em>
(vols. 39–47), com as páginas de cada catálogo e as imagens originais na mesma pasta.
Versão HTML gerada a partir do pacote Markdown autónomo.</p>

<div class="stats">
  <div><b>{n_catalogues}</b>catálogos</div>
  <div><b>{n_volumes}</b>volumes</div>
  <div><b>{n_pages}</b>páginas de catálogo</div>
  <div><b>{n_images}</b>imagens referenciadas</div>
</div>

<div class="cards">
  <div class="card">
    <h3>Índice sistemático por volume</h3>
    <p>Os catálogos agrupados por volume ARSI, com ano, tipo, fólios e descrição.</p>
    <a class="button" href="INDICE-sistematico-por-volume.html">Abrir índice</a>
  </div>
  <div class="card">
    <h3>Índice cronológico</h3>
    <p>Todos os catálogos por ordem de ano, atravessando os volumes; cada linha liga ao
       catálogo e à secção do volume.</p>
    <a class="button" href="INDICE-cronologico.html">Abrir índice</a>
  </div>
  <div class="card">
    <h3>Tipologia dos catálogos (T1–T11)</h3>
    <p>Explicação dos tipos T1, T2, T3, T4, T5… com exemplos.</p>
    <a class="button" href="TIPOLOGIA.html">Abrir tipologia</a>
  </div>
  <div class="card">
    <h3>Relatórios de indexação</h3>
    <p>Relatórios por volume (LUS. 39 a LUS. 47) e resumo geral: fontes,
       mapeamento ficheiro↔fólio, lacunas e decisões pendentes.</p>
    <a class="button" href="reports/README.html">Abrir relatórios</a>
    <a class="button" href="reports/SUMMARY.html">Resumo geral</a>
  </div>
</div>

<h2>Como usar</h2>
<ol>
  <li>Escolher um dos índices acima e clicar no catálogo pretendido.</li>
  <li>Cada página de catálogo mostra as imagens das páginas, na ordem dos fólios.</li>
  <li>Todos os caminhos são relativos: a pasta pode ser copiada para outro disco ou
      aberta diretamente no browser (<code>file://…/index.html</code>) ou servida com
      <code>python3 -m http.server</code>.</li>
</ol>

<p class="lead"><strong>Nota:</strong> as imagens são os JPEG originais das pastas
<code>LUS. NN/</code>. Se estiverem apenas no iCloud Drive como ficheiros “dataless”,
o browser não as consegue mostrar até serem descarregadas.</p>
</main>
<footer>Gerado a 2026-10-23 a partir de <code>INDICE-sistematico-por-volume.md</code>,
<code>INDICE-cronologico.md</code> e <code>catalogos/*.md</code>.</footer>
</body>
</html>
"""


def strip_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def run_pandoc(src, title, css, template_path):
    text = strip_frontmatter(open(src, encoding="utf-8").read())
    cmd = [
        "pandoc", "-", "-f", "markdown-yaml_metadata_block", "-t", "html5", "--standalone",
        "--template", template_path, "--metadata", f"title={title}",
        "--metadata", "lang=pt", "--css", css,
    ]
    result = subprocess.run(cmd, input=text, capture_output=True, text=True)
    if result.returncode != 0:
        print("pandoc failed:", src, "\n", result.stderr[:500])
        raise subprocess.CalledProcessError(result.returncode, cmd)
    return result.stdout


def postprocess(html, nav, depth):
    html = html.replace("<body>", "<body>" + nav, 1)
    # .md links -> .html (relative links only)
    html = re.sub(r'href="([^"]+?)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', html)
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", default=DIGI)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    dest = args.dest

    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_html_template.html")
    with open(template_path, "w", encoding="utf-8") as fh:
        fh.write(TEMPLATE)

    root_pages = [
        (INDEX_MD, "Índice sistemático por volume"),
        (CHRONO_MD, "Índice cronológico dos catálogos"),
        (TYPOLOGY_MD, "Tipologia dos catálogos (T1–T11)"),
    ]
    cat_mds = sorted(glob.glob(os.path.join(dest, CAT_DIR, "*.md")))
    total = 0
    for md, title in root_pages:
        src = os.path.join(dest, md)
        if not os.path.exists(src):
            print("missing:", src)
            continue
        html = run_pandoc(src, title, STYLE, template_path)
        html = postprocess(html, NAV_ROOT, 0)
        out = os.path.join(dest, md[:-3] + ".html")
        if not args.dry_run:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(html)
        total += 1

    for md in cat_mds:
        name = os.path.basename(md)[:-3]
        html = run_pandoc(md, name, "../" + STYLE, template_path)
        html = postprocess(html, NAV_CAT, 1)
        out = os.path.join(dest, CAT_DIR, name + ".html")
        if not args.dry_run:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(html)
        total += 1

    report_mds = sorted(glob.glob(os.path.join(dest, "reports", "*.md")))
    for md in report_mds:
        name = os.path.basename(md)[:-3]
        if name == "CORRECTIONS":
            title = "Correções registadas — índice dos catálogos"
        elif name == "SUMMARY":
            title = "Resumo geral — índice dos catálogos ARSI Lusitania"
        elif name == "README":
            title = "Relatórios de indexação — ARSI Lusitania"
        elif name.startswith("LUS-"):
            title = f"{name} — relatório de indexação"
        else:
            title = name
        html = run_pandoc(md, title, "../" + STYLE, template_path)
        html = postprocess(html, NAV_REPORT, 1)
        out = os.path.join(dest, "reports", name + ".html")
        if not args.dry_run:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(html)
        total += 1

    if not args.dry_run:
        with open(os.path.join(dest, STYLE), "w", encoding="utf-8") as fh:
            fh.write(CSS)
        if os.path.exists(os.path.join(dest, CHRONO_MD)):
            chrono = open(os.path.join(dest, CHRONO_MD), encoding="utf-8").read()
            chrono_rows = len([l for l in chrono.split("\n") if l.startswith("| ") and not l.startswith("| Ano")])
        else:
            chrono_rows = 0
        sys_files = sorted(glob.glob(os.path.join(dest, CAT_DIR, "*.html")))
        n_volumes = len([p for p in glob.glob(os.path.join(dest, "LUS.*")) if os.path.isdir(p)])
        index_html = INDEX_HTML.format(
            nav=NAV_ROOT, n_catalogues=len(cat_mds), n_volumes=n_volumes,
            n_pages=len(sys_files), n_images=sum(
                1 for p in sys_files
                for _ in re.finditer(r'<img ', open(p, encoding="utf-8").read())
            ),
        )
        with open(os.path.join(dest, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(index_html)
        total += 1

    print(f"HTML pages generated: {total} (root: {len(root_pages)} + index.html, catalogues: {len(cat_mds)})")
    print("DEST:", dest)


if __name__ == "__main__":
    sys.exit(main())
