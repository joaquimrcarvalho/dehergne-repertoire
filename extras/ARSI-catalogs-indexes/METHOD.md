# METHOD — building the ARSI Lusitania catalogue index

Read this together with [ARSI-catalogs-index-plan.md](ARSI-catalogs-index-plan.md).

## Ground rules

1. **Never move, rename, copy or edit files in the digitalisation folder.**
   `/Users/jrc/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19/`
   is read-only for this job.
2. **Do not edit the Obsidian master list.**
   `03 Projectos/03.03.01.01 ARSI Lusitania - catálogos - digitalizados - em curso.md`
   is updated by the Lead only. Teammates write only their JSON, their notes
   (new files) and their report.
3. **Read index pages with the image tool** (`read_image`), not OCR
   (tesseract on these typewritten pages is slow and unreliable).
4. **Never create a note for a catalogue whose first folio you have not read**
   (or mark it `"verified": false` and say why in the report).
5. Notes go to `/Users/jrc/jrc-notes/03 Projectos/`.
6. Do not create a note if a note for the same catalogue already exists —
   record it in `already_existed` instead.

## 1. Find and read the typewritten index

Per volume, the index lists year → type → folio per house. Look:

- first 3–5 images of the folder (e.g. `000.jpg`, `000v.jpg`, `000a.jpg`, `000i1.jpg`);
- last 2–3 images;
- root PDFs (e.g. `LUS.39.0.index.pdf`, render with
  `pdftoppm -r 150 -png -f 1 -l 2 <pdf> /tmp/idx`).

Read each index page with `read_image`. Transcribe, per catalogue:
year, type (T1/T2/T3/T4/T5/T6/T7/T8/T10/T11…), first folio, last folio,
short title/remark.

If a volume has no typed index, use the existing VLM tables
(`01 Notes/ARSI Lusitania Catalogues LUS. XX.md`) as a hypothesis and verify
every segment start against the image.

## 2. Build the JSON table

Write `extras/ARSI-catalogs-indexes/data/<VOL>.json`
(`<VOL>` = `LUS-39`, `LUS-43`, `LUS-44`, `LUS-45`, `LUS-46`, `LUS-47`, `LUS-42`, …):

```json
{
  "volume_folder": ["LUS. 45"],
  "volume_note": "ARSI Lusitania 45",
  "index_sources": ["LUS. 45/000i1.jpg", "LUS. 45/000i2.jpg", "LUS. 45/000i3.jpg"],
  "catalogues": [
    {
      "year": "1658",
      "type": "T1",
      "title": "Catalogus I Provinciae Lusitanae",
      "description": "Catálogo I de 1658 (ff. 251-268); começa pelo Colégio de Coimbra.",
      "local": "",
      "folio_start": "251",
      "folio_end": "267v",
      "note": "1658-T1-LUS-45-251",
      "verified": true,
      "evidence": "f. 251, carimbo 251: «Catalogus 1us Collegy Conimbricensis»",
      "already_existed": false
    }
  ],
  "unaccounted": "folios not covered by any catalogue, if any",
  "gaps": "expected catalogues not present / folios missing"
}
```

- `folio_start` / `folio_end`: stamped folio, `v` for verso (`"267v"`),
  `"0420v"`-style accepted; for the continuation folder with two-folio images
  use the first and last stamped folio.
- `note`: the Obsidian note name (without `.md`), following
  `ANO-TIPO[-LOCAL]-LUS-VOL[-parte]-FÓLIO` (e.g. `1658-T1-LUS-45-251`,
  `1568-T6P-Coimbra-LUS-43-II-a-326`). Old notes keep their old names.
- `description`: 1–3 sentences, Portuguese preferred (project convention).
- `verified` + `evidence`: what you actually saw on the start page.

## 3. Generate the notes

```bash
cd /Users/jrc/mhk-home/sources/dehergne
python3 extras/ARSI-catalogs-indexes/tools/gen_notes.py \
    extras/ARSI-catalogs-indexes/data/LUS-45.json
```

The generator embeds every image whose folio falls in the range, in order,
using the same `file://` format as the existing notes. Options:

- `--dry-run` — print what would be written, write nothing;
- `--force` — overwrite existing notes (only for your own volume);
- `--notes-dir` — destination (default `03 Projectos`).

Then check the result: open the note and confirm the embed count equals the
expected number of folios (recto+verso).

## 4. Validate

```bash
python3 extras/ARSI-catalogs-indexes/tools/validate.py
```

It checks: every note exists, every `file://` link resolves, no two ranges
overlap inside a volume, verified/not-verified counts, folios not covered.

## 5. Report

Write `extras/ARSI-catalogs-indexes/reports/<VOL>.md` with:

- index sources used and a short transcription summary;
- table: year | type | folios | note | verified + evidence;
- existing notes reused / names that deviate from the convention;
- gaps, duplicates, ambiguities;
- anything the Lead must decide.

## 6. Corrigir um erro (fonte de verdade e propagação)

> Registo humano: nota Obsidian «Correções ao índice dos catálogos (entrada)».
> Procedimento completo (humano + agente): `CORRECTIONS-WORKFLOW.md`.

A **fonte de verdade** é a tabela JSON do volume (`data/LUS-XX.json`). As notas,
os índices (Markdown, HTML e notas do Obsidian) e a secção gerada do master list
são **derivados** dela — por isso uma correção faz-se no JSON e propaga-se por
regeneração, não editando cada índice à mão.

```bash
cd /Users/jrc/mhk-home/sources/dehergne
python3 extras/ARSI-catalogs-indexes/tools/correct_entry.py   --volume LUS-45 --note 1658-T1-LUS-45-251   --field folio_end --value 266v   --reason "o intervalo incluía a primeira página do catálogo seguinte"   --evidence "f.267 mostra o título do catálogo seguinte (imagem lida)"
```

O comando:

1. altera o campo na entrada do JSON;
2. acrescenta o histórico `corrections` a essa entrada (data, campo, antes,
   depois, motivo, evidência);
3. acrescenta uma linha a `CORRECTIONS.md` (registo humano);
4. regenera, por esta ordem: a **nota** do catálogo (`gen_notes.py --only
   --force`), o **pacote portátil** (`make_portable_package.py` → `catalogos/`,
   `INDICE-sistematico`, `INDICE-cronologico`), as **notas-índice do Obsidian**
   (`make_vault_indexes.py`), a **secção do master list**
   (`update_master_section.py`), a **cópia dos relatórios** (`copy_reports.py`) e
   as **páginas HTML** (`make_html_package.py`).

Opções úteis: `--dry-run` (pré-visualizar), `--no-refresh` (só registar e deixar a
propagação para depois), `--field` (por omissão `folio_end`; também aceita
`folio_start`, `year`, `type`, `title`, `description`, `verified`,
`image_start_file`, `image_end_file`).

**Erro típico «páginas a mais / dois catálogos numa nota»**: o `folio_end` está
demasiado à frente. Corrigir para o fólio imediatamente anterior ao início do
catálogo seguinte (por exemplo, se o seguinte começa em f. 268, o fim é 267v).
O `note`/nome do ficheiro mantém-se (o fólio inicial não muda).

## Definition of done for a volume

- `data/<VOL>.json` exists and parses;
- all `note` files exist in the vault and their image links resolve;
- every catalogue has `verified: true` with concrete evidence, or an explicit
  note in the report explaining why not;
- `reports/<VOL>.md` written;
- shared task completed and a 5-line summary sent to the Lead.
