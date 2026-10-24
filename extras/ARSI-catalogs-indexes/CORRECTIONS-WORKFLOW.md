# Correction workflow — how a human reports, how an agent applies

The human-facing inbox is the Obsidian note
`03 Projectos/Correções ao índice dos catálogos (entrada).md`
(one correction per row, in plain language). The agent turns each row into a
precise change in the JSON tables and propagates it.

## 1. What the human needs to provide (and nothing more)

One row per correction, with:

1. **Volume** (e.g. `LUS-44`).
2. **Catalogue** — the note name (`1625-T5-LUS-44II-430`) or, if unknown,
   year + first folio/image (`1625, começa em 0429v-0430`).
3. **Where you saw it** — image filename(s) and/or folio, e.g.
   `0432v-0433 / 0433v-0434`.
4. **What is wrong** — e.g. "the note merges two catalogues", "too many pages",
   "missing catalogue", "wrong type", "wrong year".
5. **What it should be** — the correct last page, or the new note that should
   exist.
6. Optional but very useful: a **photo/screenshot** or the exact title read on
   the boundary page.

The human does **not** edit JSON, run scripts or rename notes.

## 2. Agent procedure (for each unchecked row)

1. **Locate the entry** in `extras/ARSI-catalogs-indexes/data/LUS-XX.json`
   (by `note`; fall back to year + `folio_start`).
2. **Verify with the images** — open the cited image(s) with `read_image` and
   confirm what actually starts/ends there. Never apply a correction you have
   not seen; if the row is ambiguous, move it to “Em análise” and ask.
3. **Classify and apply** (see table below).
4. **Regenerate** (the tool does it for field corrections; for structural
   changes run the pipeline manually).
5. **Record**: `CORRECTIONS.md` row (the tool appends it; add manually for
   structural changes) and the per-volume report (`reports/LUS-XX.md`
   § Correções) if it discusses the range.
6. **Write back** in the inbox: `Estado = ✅ aplicada <data> — resumo`, and add
   a short line in “Aplicadas”.
7. **Verify**: `validate.py` → 0 problems; check the note's image count; check
   the row in `INDICE-cronologico.md`; check the HTML page has the right
   `<img>` count.

## 3. Error types → operation

| What the human reports | Operation |
|---|---|
| Range too wide / one note includes pages of the next catalogue | `correct_entry.py --field folio_end` (or `image_end_file`) to the folio just before the next catalogue |
| Range too narrow / missing last page | `--field folio_end` (or `image_end_file`) to the correct last folio/image |
| Two catalogues merged into one note and both should exist | shorten the existing entry, **add a new entry** in the JSON (new `note`), then `gen_notes.py --only <new> <old>` |
| A catalogue is missing from the index (no note at all) | **add an entry** (`year`, `type`, `title`, `description`, `folio_start/end` or `image_start_file`/`image_end_file`, `note`, `evidence`) then generate |
| Wrong type / year / title / description | `correct_entry.py --field type|year|title|description` |
| Wrong note name / duplicate note | structural: rename in JSON + regenerate, then update wikilinks (ask the Lead) |
| Broken image link / filename↔folio offset | fix the JSON range or image fields; for old notes in `01 Notes`, re-point or regenerate in `03 Projectos` |
| Stale note in `01 Notes` shadowing the generated one | archive the old note to `extras/ARSI-catalogs-indexes/backup/obsidian-notes/` and regenerate |

## 4. Commands

Single-field correction (most cases):

```bash
cd /Users/jrc/mhk-home/sources/dehergne
python3 extras/ARSI-catalogs-indexes/tools/correct_entry.py \
  --volume LUS-44 --note 1627-T10-LUS-44II-438 \
  --field folio_end --value 438v \
  --reason "faltava a última página do rol" \
  --evidence "f.438v continua a lista (imagem 0438v-0439)"
```

Structural change (add/split entry): edit the JSON, then:

```bash
python3 extras/ARSI-catalogs-indexes/tools/gen_notes.py \
  extras/ARSI-catalogs-indexes/data/LUS-44.json --force --only <note1> <note2>
python3 extras/ARSI-catalogs-indexes/tools/make_portable_package.py
python3 extras/ARSI-catalogs-indexes/tools/make_vault_indexes.py
python3 extras/ARSI-catalogs-indexes/tools/update_master_section.py
python3 extras/ARSI-catalogs-indexes/tools/copy_reports.py
python3 extras/ARSI-catalogs-indexes/tools/make_html_package.py
```

Then add a row to `CORRECTIONS.md` (and the report section) manually.

## 5. Guard rails

- Never move/rename/edit files in `v2-2025-01-19/LUS. NN/`.
- Never edit generated notes/indexes by hand — change the JSON and regenerate.
- Do not delete old notes silently: archive them under
  `extras/ARSI-catalogs-indexes/backup/obsidian-notes/`.
- One correction per command; run `validate.py` after each batch.
- If the evidence contradicts the report, stop and ask the human rather than
  inventing a range.

## 6. Ready-to-paste prompt for an agent

> Read `03 Projectos/Correções ao índice dos catálogos (entrada).md` and
> process every row in “Por aplicar”, one at a time. For each: locate the entry
> in `extras/ARSI-catalogs-indexes/data/LUS-XX.json`, open the cited images with
> `read_image` to confirm the boundary, apply the correction with
> `correct_entry.py` (or add/split the JSON entry for structural cases), run the
> regeneration pipeline, verify with `validate.py` and a spot check of the note
> and index row, then mark the row `✅ aplicada <data>` with a one-line summary
> and append the “Aplicadas” line. Never guess: if the evidence is ambiguous,
> move the row to “Em análise” and state exactly what is missing.
