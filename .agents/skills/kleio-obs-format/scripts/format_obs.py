#!/usr/bin/env python3
"""Lay out `ls$dehergne/NNN/obs=TEXT` observations in Dehergne Kleio sources.

Only whitespace changes: the observation text is wrapped in triple quotes and
line breaks are inserted so that each event / reference starts a new line.
Every non-whitespace character is preserved verbatim.

Usage:
    python format_obs.py FILE [FILE ...]              # rewrite files in place
    python format_obs.py --check FILE [...]           # report, exit 1 if changes needed
    python format_obs.py --diff FILE [...]            # show unified diff, no writes
    python format_obs.py --entry 576 FILE             # only the obs of entry 576
    python format_obs.py --no-blank-line FILE         # do not insert the blank line

Options:
    --indent N     indent for wrapped text lines (default: obs line indent + 3)
    --width N      wrap width for long items (default: 100, 0 = never wrap)
    --no-blank-line  do not insert a blank line before the "N." line
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

OBS_RE = re.compile(r"(?P<head>[ \t]*ls\$dehergne/[0-9]+(?:-ref[0-9]+)?/obs=)(?P<rest>.*)", re.DOTALL)

EVENT_MARKERS = (
    "N.", "E.", "Emb.", "Arr.", "arr.", "Retenu", "V.", "M.", "Pf.",
    "Il signe", "Ne pas confondre", "ne pas confondre", "Distinct",
    "Vicaire", "En réalité", "en somme", "Notice", "Portrait", "Stèle",
    "Titres", "Séjour", "Séj.", "Départ", "Parti", "Reste", "Envoyé",
    "Nommé", "Supérieur", "Provincial", "Vice-provincial", "Visiteur",
    "Recteur", "Maître", "Missionnaire", "Chirurgien", "Horloger",
    "Peintre", "Musicien", "Mathématicien", "Astronome", "Médecin",
    "Interprète", "Auteur", "Traducteur", "Écrivain", "Prêtre", "Frère",
)

# A reference item starts with a person surname or a library siglum.
REFERENCE_START_RE = re.compile(
    r"^(?:"
    r"Pf\.|HS\b|JS\b|Lus\.|Goa\b|Hisp\.|Ital\.|Franc\.|Med\.|Neap\.|G\. Sup\.|"
    r"Philipp\.|ARSI\b|BN\b|Borg\.|Gai\.|Brotier\b|Verbo\b|NCE\b|EC\b|"
    r"DHGE\b|DBF\b|DLF\b|DBI\b|NDB\b|BNB\b|NBW\b|CE\b|EB\b|SF\b|FR\b|"
    r"SOCP\b|LEP\b|AHSI\b|MS\b|NZM\b|TP\b|CCS\b|RHE\b|BCP\b|LSF\b|"
    r"JA\b|DI\b|Sch[uû]tte\b|Planchet\b|W\.\s?K\b|W\s[0-9]|"
    r"[A-ZÉÈÀÂÊÎÔÛÇ][a-zéèêàâîôûçëïüö'’\-]+,\s"
    r")"
)

EVENT_START_RE = re.compile(r"^(?:" + "|".join(re.escape(m) for m in EVENT_MARKERS) + r")")
SENTENCE_END_RE = re.compile(r"[.!?][\"»”)]?$")
# "N." of the biographical header, e.g. "Moura, Luis de (port.) P. 576 N. 1618, ..."
HEADER_N_RE = re.compile(r"(?:\bP\.\s*\d+\s+|\d{1,4}\s+|\.\s+)N\.\s")


def split_items(text: str) -> list[str]:
    """Split observation text into items without altering its characters.

    Lines are joined only where a new item starts; the original spaces that
    separated the joined lines are kept as the joiner.
    """
    raw_lines = text.split("\n")
    items: list[str] = []
    current: list[str] = []

    for raw in raw_lines:
        stripped = raw.strip()
        if not stripped:
            if current:
                items.append("".join(current))
                current = []
            items.append("")
            continue
        if current:
            joined = "".join(current)
            starts_new = (
                EVENT_START_RE.match(stripped) is not None
                or REFERENCE_START_RE.match(stripped) is not None
                or SENTENCE_END_RE.search(joined.rstrip()) is not None
            )
            if starts_new:
                items.append("".join(current))
                current = [stripped]
                continue
            current.append(" " + stripped)
        else:
            current = [stripped]

    if current:
        items.append("".join(current))
    return items


def wrap_item(item: str, width: int) -> list[str]:
    """Wrap a long item at word boundaries, keeping all characters."""
    if width <= 0 or len(item) <= width:
        return [item]
    words = item.split(" ")
    lines: list[str] = []
    line = words[0]
    for word in words[1:]:
        if len(line) + 1 + len(word) <= width:
            line += " " + word
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def is_header_n(item: str) -> bool:
    """True for the "N." line of the biographical header (not a bare event)."""
    if not item.startswith("N."):
        return False
    if not HEADER_N_RE.search(item):
        return True
    return "P." in item or item.rstrip().endswith(tuple("0123456789"))


def render(items: list[str], indent: int, width: int, blank_line: bool) -> list[str]:
    pad = " " * indent
    out: list[str] = []
    blanks = 0
    header_seen = False
    for item in items:
        if item == "":
            blanks += 1
            continue
        if blank_line and not header_seen and is_header_n(item):
            out.append("")
            header_seen = True
        elif blanks:
            out.append("")
            blanks = 0
        for piece in wrap_item(item, width):
            out.append(pad + piece)
    return out


def format_obs_line(line: str, indent: int | None, width: int, blank_line: bool) -> list[str]:
    m = OBS_RE.match(line)
    if not m:
        return [line]
    head, rest = m.group("head"), m.group("rest")
    if not rest.strip():
        return [line]

    text_indent = indent if indent is not None else (len(head) - len(head.lstrip())) + 3
    body = render(split_items(rest), text_indent, width, blank_line)
    if not body:
        return [line]
    body[-1] = body[-1] + '"""'
    return [head + '"""'] + body


def collect_block(lines: list[str], i: int) -> tuple[list[str], int]:
    """Return the obs block starting at line i and the index of its last line."""
    block = [lines[i]]
    if '"""' in lines[i].split("obs=", 1)[-1][3:]:
        return block, i
    j = i + 1
    while j < len(lines):
        block.append(lines[j])
        if '"""' in lines[j]:
            return block, j
        j += 1
    return block, j - 1


def format_file(
    path: Path, entry: str | None, indent: int | None, width: int, blank_line: bool
) -> tuple[list[str], list[str]]:
    original = path.read_text(encoding="utf-8").split("\n")
    result: list[str] = []
    i = 0
    while i < len(original):
        line = original[i]
        m = OBS_RE.match(line)
        if m and (entry is None or re.search(rf"/{re.escape(entry)}(?:-ref[0-9]+)?/obs=", line)):
            block, last = collect_block(original, i)
            text = "\n".join(block).split("obs=", 1)[1]
            if text.startswith('"""'):
                text = text[3:]
            if text.endswith('"""'):
                text = text[:-3]
            result.extend(format_obs_line(m.group("head") + text, indent, width, blank_line))
            i = last + 1
            continue
        result.append(line)
        i += 1
    return original, result


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--check", action="store_true", help="report only; exit 1 if changes are needed")
    ap.add_argument("--diff", action="store_true", help="print unified diff; do not write")
    ap.add_argument("--entry", help="only format the obs of this Dehergne number")
    ap.add_argument("--indent", type=int, default=None, help="indent for wrapped text lines")
    ap.add_argument("--width", type=int, default=100, help="wrap width (0 = never wrap)")
    ap.add_argument("--no-blank-line", dest="blank_line", action="store_false", help="do not insert blank line before N.")
    args = ap.parse_args(argv)

    status = 0
    for path in args.files:
        original, result = format_file(path, args.entry, args.indent, args.width, args.blank_line)
        if original == result:
            continue
        if args.check:
            print(f"needs formatting: {path}")
            status = 1
        elif args.diff:
            sys.stdout.writelines(
                difflib.unified_diff(
                    [line + "\n" for line in original],
                    [line + "\n" for line in result],
                    fromfile=str(path),
                    tofile=str(path) + " (formatted)",
                )
            )
        else:
            path.write_text("\n".join(result), encoding="utf-8")
            print(f"formatted: {path}")
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
