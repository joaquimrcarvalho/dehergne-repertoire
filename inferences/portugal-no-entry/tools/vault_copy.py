#!/usr/bin/env python3
"""Copy the «Portugal no entry» notes into the Obsidian vault with live pha links.

Reads the per-person notes in this folder and writes a vault copy in
`04 Biographies/dehergne/portugal_noentry/`, with:

* extra front matter recording origin, source and copy date (for future updates);
* every `pha page <doc> <page>` command turned into a live link to the page
  viewer served by `pha serve` (http://127.0.0.1:8765/doc/<slug>/p<page>)
  plus the `.jpg` render link.

Slug and page-count come from the pha archive DB (read-only, immutable).

    python3 tools/vault_copy.py --check      # only report, write nothing
    python3 tools/vault_copy.py              # write the vault copies
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from datetime import date

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(HERE, "tools")
ARCHIVE = os.environ.get("PHA_ARCHIVE_DIR", "/Users/jrc/jesuit-archive")
DB = os.path.join(ARCHIVE, "archive.db")
VAULT_DIR = "/Users/jrc/jrc-notes/04 Biographies/dehergne/portugal_noentry"
SERVE = "http://127.0.0.1:8765"
TODAY = date.today().isoformat()


# ---------------------------------------------------------------- slug / pages
# Prefer the canonical implementation shipped with pha (addresses.doc_slug), so
# the links cannot drift from the viewer's own rule.
try:  # PYTHONPATH must include the pha site-packages (see tools/README or run cmd)
    from personal_historical_archive.addresses import doc_slug as _pha_doc_slug  # type: ignore

    def slug_for(rel_path: str) -> str:
        return _pha_doc_slug(rel_path)

    SLUG_SOURCE = "pha.addresses.doc_slug"
except Exception:  # pragma: no cover - fallback mirrors the same rule
    import unicodedata
    from pathlib import PurePosixPath

    def slug_for(rel_path: str) -> str:
        parts = list(PurePosixPath(str(rel_path)).parts)
        if parts and parts[0] == "collections":
            parts = parts[1:]
        if not parts:
            return ""
        parts[-1] = PurePosixPath(parts[-1]).stem
        text = unicodedata.normalize("NFKD", "/".join(parts).lower())
        text = "".join(c for c in text if not unicodedata.combining(c))
        return re.sub(r"[^a-z0-9]+", "-", text).strip("-")

    SLUG_SOURCE = "local reimplementation of pha.addresses.doc_slug"


def dropbox_rel(doc_path: str, dir_path: str, filename: str) -> str:
    try:
        from pathlib import Path

        return Path(doc_path).resolve().relative_to(Path(ARCHIVE, "dropbox").resolve()).as_posix()
    except Exception:
        return f"{dir_path}/{filename}" if dir_path else filename


def load_docs() -> dict[int, dict]:
    conn = sqlite3.connect(f"file:{DB}?mode=ro&immutable=1", uri=True)
    conn.row_factory = sqlite3.Row
    docs: dict[int, dict] = {}
    for r in conn.execute(
        "select id, filename, dir_path, path, kind, page_count from documents"
    ):
        rel = dropbox_rel(r["path"], r["dir_path"], r["filename"])
        docs[r["id"]] = dict(
            id=r["id"], filename=r["filename"], dir_path=r["dir_path"], kind=r["kind"],
            pages=r["page_count"] or 0, slug=slug_for(rel), rel=rel,
        )
    return docs


def validate_slugs(docs: dict[int, dict]) -> dict:
    """Cross-check our slug against URLs that already exist in the archive notes."""
    urlre = re.compile(r"127\.0\.0\.1:8765/doc/([a-z0-9\-]+)/p\d+")
    by_slug = {d["slug"]: d["id"] for d in docs.values()}
    seen, ok, bad = set(), 0, []
    notes_dir = os.path.join(ARCHIVE, "notes")
    for root, _dirs, files in os.walk(notes_dir):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            try:
                txt = open(os.path.join(root, fn), encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for m in urlre.finditer(txt):
                s = m.group(1)
                if s in seen:
                    continue
                seen.add(s)
                if s in by_slug:
                    ok += 1
                else:
                    bad.append(s)
    return dict(checked=len(seen), matched=ok, unmatched=sorted(bad)[:10])


# ------------------------------------------------------------------ link logic
REF_RE = re.compile(
    r"doc\s+(\d+)[^\n;]{0,30}?p\.?\s*(\d+)"          # "doc 81, p. 50" / "doc 29, f. 271v"
    r"|(\d+)\s*f\.\s*(\d+)"                            # rare "44 f. 320"
)
CMD_BACKTICK_RE = re.compile(r"`[^`\n]*\bpha page\b[^`\n]*`")
CMD_RE = re.compile(r"`?\bpha page\b\s+(\d+)\s+(\d+)")
PROSE_RE = re.compile(r"\(doc\s+(\d+)\)[^\n]{0,60}?(?:\bp\.|\bpágina)\s*\.?\s*(\d+)")
LOOSE_RE = re.compile(r"doc\s+(\d+)[^\n]{0,40}?\b(?:p\.|página|page)\s*(\d+)")


def page_url(slug: str, page: int) -> str:
    return f"{SERVE}/doc/{slug}/p{page:03d}" if page < 1000 else f"{SERVE}/doc/{slug}/p{page}"


def resolve(docs: dict[int, dict], doc: int, page: int) -> str | None:
    d = docs.get(doc)
    if not d:
        return None
    if d["pages"] and not (1 <= page <= int(d["pages"])):   # page outside the document
        return None
    return page_url(d["slug"], page)


def first_evidence_pair(note: str, docs: dict[int, dict]) -> tuple[int, int] | None:
    """The first `pha page <doc> <page>` command whose doc/page resolves."""
    for m in CMD_RE.finditer(note):
        doc, page = int(m.group(1)), int(m.group(2))
        if resolve(docs, doc, page):
            return doc, page
    for m in REF_RE.finditer(note):
        doc = int(m.group(1) or m.group(3))
        page = int(m.group(2) or m.group(4))
        if resolve(docs, doc, page):
            return doc, page
    return None


def add_live_links(text: str, docs: dict[int, dict]) -> tuple[str, int]:
    """Turn each `pha page <doc> <page>` command into a live two-part link.

    Only the «5. Evidência» section is touched (that is where the commands live
    and where a reader wants to open the page); the code span itself is kept and
    the links are appended after it.
    """
    marker = "## 5. Evidência"
    idx = text.find(marker)
    if idx == -1:
        return text, 0
    head, tail = text[: idx + len(marker)], text[idx + len(marker):]
    done: dict[tuple[int, int], str] = {}

    def repl(m: re.Match) -> str:
        inner = m.group(0)                                  # `pha page 81 50 --edited`
        dm = re.search(r"pha page\s+(\d+)\s+(\d+)", inner)
        if not dm:
            return m.group(0)
        doc, page = int(dm.group(1)), int(dm.group(2))
        url = resolve(docs, doc, page)
        if not url:
            return m.group(0)
        key = (doc, page)
        if key in done:
            return m.group(0)
        done[key] = url
        return f"{m.group(0)} → [p. {page}]({url}) · [imagem]({url}.jpg)"

    tail = CMD_BACKTICK_RE.sub(repl, tail)
    text = head + tail

    # second pass: prose citations in the evidence section that name a doc and a
    # page but carry no command, e.g. "*História da Companhia…* (doc 64), p. 231"
    head, tail = text[: idx + len(marker)], text[idx + len(marker):]

    def repl_prose(m: re.Match) -> str:
        line_start = tail.rfind("\n", 0, m.start()) + 1
        line_end = tail.find("\n", m.end())
        line = tail[line_start: line_end if line_end != -1 else len(tail)]
        if "http://127.0.0.1:8765" in line:
            return m.group(0)
        doc, page = int(m.group(1)), int(m.group(2))
        url = resolve(docs, doc, page)
        if not url:
            return m.group(0)
        key = (doc, page)
        if key in done:
            return m.group(0)
        done[key] = url
        return f"{m.group(0)} → [p. {page}]({url})"

    tail = PROSE_RE.sub(repl_prose, tail)
    return head + tail, len(done)


def note_uses_arsi(text: str) -> bool:
    return bool(re.search(r"ARSI\s+Lus\.|_scratch/bnp47525", text))


def add_source_line(text: str, docs: dict[int, dict], pairs: list[tuple[int, int]]) -> str:
    """After each evidence bullet, add the document's collection, once per doc."""
    if not pairs:
        return text
    lines = text.split("\n")
    out: list[str] = []
    inserted: set[int] = set()
    for line in lines:
        out.append(line)
        m = re.match(r"^- .*?doc\s+(\d+)", line)
        if not m:
            continue
        doc = int(m.group(1))
        if doc in inserted or doc not in docs:
            continue
        d = docs[doc]
        inserted.add(doc)
        out.append(f"  - documento {doc}: `{d['rel']}` · coleção `{d['dir_path'] or '—'}` · {d['pages']} páginas")
    return "\n".join(out)


# ------------------------------------------------------------------ frontmatter
def rewrite_frontmatter(text: str, pid: str, src_name: str, uses_arsi: bool) -> str:
    lines = text.split("\n")
    assert lines[0].strip() == "---"
    end = lines.index("---", 1)
    fm = lines[1:end]
    body = lines[end + 1:]
    keep = [ln for ln in fm if not ln.startswith(("created:", "copied:", "source_note", "source_repo", "copy", "arsi_"))]
    add = [
        f"source_note: inferences/portugal-no-entry/{src_name}",
        "source_repo: mhk-home/sources/dehergne",
        f"copied: {TODAY}",
        "copy: cópia automática — editar o original em inferences/portugal-no-entry/ e re-copiar",
    ]
    if uses_arsi:
        add.append("arsi_images: true")
    return "\n".join(["---"] + keep + add + ["---"] + body)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    docs = load_docs()
    report = validate_slugs(docs)
    print(f"slug validation: {report['checked']} URLs in archive notes, "
          f"{report['matched']} matched by our slug, unmatched={report['unmatched']}")

    notes = sorted(f for f in os.listdir(HERE) if f.endswith(".md") and f != "Índice - Portugal no entry.md")
    if not args.check:
        os.makedirs(VAULT_DIR, exist_ok=True)

    total_links = 0
    no_link: list[str] = []
    arsi_notes = 0
    for fn in notes:
        src = os.path.join(HERE, fn)
        text = open(src, encoding="utf-8").read()
        pid = fn[:-3]
        uses_arsi = note_uses_arsi(text)
        arsi_notes += uses_arsi
        text, n = add_live_links(text, docs)
        total_links += n
        if not n:
            no_link.append(pid)
        text = rewrite_frontmatter(text, pid, fn, uses_arsi)
        text += (
            "\n\n---\n\n"
            f"> [!info] Origem e actualização\n"
            f"> Cópia automática da nota de inferência `inferences/portugal-no-entry/{fn}` "
            f"do projecto Timelink (`mhk-home/sources/dehergne`), copiada a {TODAY}.\n"
            f"> A nota original é a fonte de verdade: alterações devem ser feitas lá e "
            f"re-copiadas com `python3 tools/vault_copy.py`.\n"
            f"> As ligações `pha serve` (127.0.0.1:8765) só resolvem com o servidor de leitura "
            f"a correr: `pha serve`.\n"
        )
        if uses_arsi:
            text += (
                "\n> [!note] Provas em manuscrito (fora do pha)\n"
                "> Esta nota cita manuscritos ARSI/BNP lidos em imagem; essas ligações são "
                "caminhos locais, não endereços `pha serve`.\n"
            )
        if not args.check:
            with open(os.path.join(VAULT_DIR, fn), "w", encoding="utf-8") as fh:
                fh.write(text)

    # the synthesis note, copied with its own front matter
    idx = "Índice - Portugal no entry.md"
    if os.path.exists(os.path.join(HERE, idx)):
        text = open(os.path.join(HERE, idx), encoding="utf-8").read()
        text = rewrite_frontmatter(text, "indice", idx, note_uses_arsi(text))
        text = text.replace(
            "## Referências",
            "## Referências\n\n- [[ARSI Lusitania - fólios em falta - Portugal no entry]] — índice dos volumes/fólios em falta.",
            1,
        )
        text += (
            "\n\n---\n\n"
            f"> [!info] Origem e actualização\n"
            f"> Cópia automática de `inferences/portugal-no-entry/{idx}` "
            f"(projecto Timelink, `mhk-home/sources/dehergne`), copiada a {TODAY}.\n"
        )
        if not args.check:
            with open(os.path.join(VAULT_DIR, idx), "w", encoding="utf-8") as fh:
                fh.write(text)

    print(f"notes: {len(notes)} | live links inserted: {total_links} | "
          f"notes without pha links: {len(no_link)} | notes citing ARSI/BNP images: {arsi_notes}")
    if no_link:
        print("  sem ligações pha: " + ", ".join(no_link[:20]))
    print("vault dir:", VAULT_DIR, "(written)" if not args.check else "(check only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
