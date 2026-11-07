# AGENTS.md

Guidance for AI coding agents working in this repository. Humans may follow it too.

## What this repository is

A **Timelink project directory**: Kleio source files associated with a
database. It serves as `timelink-home` in single-user, single-project mode,
and can also live inside the `projects/` directory of a multi-project home,
being used either standalone or as part of it.

This project is the transcription of Joseph Dehergne, *Répertoire des Jésuites
de Chine de 1552 à 1800* (Bibliotheca Instituti Historici S.I 37, Roma/Paris,
1973). See `README.md` for the scope of the work and `extras/doc/` for the
transcription conventions.

## Layout

| directory             | content                                                     |
|-----------------------|-------------------------------------------------------------|
| `sources/`            | Kleio source files (`.cli`): one per letter (`dehergne-a.cli` … `dehergne-z.cli`), plus `dehergne-0-abrev.cli` (abbreviations) and `dehergne-locations-1644.cli` / `dehergne-locations-1701.cli` |
| `structures/`         | structure files describing each type of source              |
| `inferences/`         | inference rules and derived data (Wikidata references, place-of-stay tables, ILOCl issues) |
| `identifications/`    | exports of the identification (record linking) process      |
| `database/sqlite/`    | SQLite database files (generated)                           |
| `extras/`             | auxiliary project files: documentation (`extras/doc/`), scripts, VS Code Kleio extension (`extras/vscode/`) |
| `notebooks/`          | Jupyter notebooks and shared Python modules working with the project data |
| `etc/doc/`            | pointers to the documentation                               |

## Rules

* **Never commit generated files.** Databases and Kleio translation
  byproducts (`*.err`, `*.ids`, `*.org`, `*.old`, `*.cli-renamed`, `*.rpt`,
  `*.rep`, `*.files.json`, `strs/`, `sources/*-auto-structure.*`) are covered
  by `.gitignore`; do not force-add them.
* **Kleio sources are transcriptions.** Files in `sources/` are scholarly
  work, and each file is copyright of its transcriber. Never rewrite them
  mechanically; content changes go through the researcher. Validate
  translations with the Kleio server before importing.
* **The database is derived data.** Everything in `database/` can be rebuilt
  from `sources/` by translating and importing; treat it as disposable.
* **Transcription conventions.** Follow `extras/doc/Dehergne_transcription_format.md`
  (person ids `deh-<nome>`, `ls$` attribute conventions, Wicki fleet numbers)
  and `extras/doc/How_to_transcribe.md` before editing any `.cli` file.
  Notebook cell outputs are stripped on commit via `nbstripout`
  (see `notebooks/README.md`).
* **Version stamping.** Infrastructure alignments with the Timelink project
  template are recorded in `CHANGELOG.md`.

## Processing the kleio sources (`.cli` files)

Sources are translated by the Kleio server (Docker) and imported into the
project database. `TimelinkNotebook` wraps the whole pipeline and is the
entry point used by the project notebooks. Run the notebooks from this
directory or from `notebooks/` so that the project is found.

1. Set up and verify:

```python
from timelink.notebooks import TimelinkNotebook

tlnb = TimelinkNotebook()   # starts/attaches the Kleio server, connects the database
tlnb.print_info()
```

2. List the sources with their translation status
   (`translated`, `errors`, `warnings` columns):

```python
kleio_files = tlnb.get_kleio_files(recurse=True)
```

3. Translate and import. Only changed files are retranslated; import is
   per file and replaces previous data for that file, so rerunning after
   editing a source is safe:

```python
tlnb.update_from_sources()
```

Force a full retranslation of everything by first cleaning the
translations:

```python
tlnb.kleio_server.translation_clean("", recurse="yes")
tlnb.update_from_sources()
```

4. Check the results. Import errors and warnings are per file:

```python
imported_files_df = tlnb.get_import_status()
errors = imported_files_df.query("import_errors > 0 or errors > 0")
if len(errors) > 0:
    print(errors)

rpt = tlnb.get_translation_report(imported_files_df, 0)   # 0 = first file
print(rpt)
rpt = tlnb.get_import_rpt(imported_files_df, rows=[0])
print(rpt)
```

Full walkthroughs live in `notebooks/README.md`: `9-tutorial.ipynb` (API
basics), `0-kleio-files.ipynb` (file processing),
`database-overview.ipynb` (schema), `01-background-importer.ipynb`
(batch import). Read them for project-specific variants before inventing new
code.

## Public replica: Editor and Server databases

A project can keep more than one version of the database from the same
sources. The usual setup is an **Editor** version — work in progress, on the
contributors' machines — and a **Server** (public) version that contains only
verified sources and identifications.

Git is the synchronization mechanism; this repository is the shared
repository between the two.

* **Editor side** (the normal way this checkout is used): translate, import
  and validate sources, make the identifications, then commit and push the
  validated `sources/` files and the identification exports in
  `identifications/`.
* **Server side** (the public replica): periodically pulls the repository and
  imports what changed. It does **not** translate or edit sources —
  translations are produced on the Editor side and arrive through git. Files
  are imported by change date, most recently changed last.
* Only validated sources and identifications are pushed for the public
  replica. Work in progress stays in the Editor's database, which is derived,
  disposable data (`database/` is never pushed).

Because translation byproducts are not committed here (see Rules), the
replica retranslates changed files itself, then imports them.

## Answering common data queries

All recipes use the `tlnb` from the previous section. Attribute names below
(`nacionalidade`, `jesuita-entrada`) are examples — discover the actual
attribute types of this project with `attribute_values` or
`tlnb.db.describe('attribute')`.

* **People by name**:

```python
from timelink.pandas import pname_to_df

df = pname_to_df("Abreu", db=tlnb.db)                # exact/like match
df = pname_to_df("Abreu", db=tlnb.db, similar=True)  # with variants
```

* **People with an attribute, optionally filtered by value** — the standard
  answer to "who has attribute X with value Y":

```python
from timelink.pandas import entities_with_attribute

df = entities_with_attribute(
    entity_type="person",
    the_type="nacionalidade",
    the_value="Portugal",                   # optional; SQL wildcards allowed
    show_elements=["name"],
    more_attributes=["jesuita-estatuto"],   # extra columns to join in
    db=tlnb.db,
)
```

* **Attributes within a date window**: add `dates_in=(after, before)`, dates
  in `AAAAMMDD` form. To list the existing values of an attribute first
  (recommended before filtering by value):

```python
from timelink.pandas import attribute_values

values = attribute_values("nacionalidade", db=tlnb.db)
values = attribute_values("jesuita-entrada", dates_between=("16000101", "16501231"),
                          db=tlnb.db)
```

* **Acts at certain dates**: use the ORM. `Act.the_date` is a string in Kleio
  `AAAAMMDD` format (unknown parts zeroed), indexed, so range comparisons work
  as string comparisons:

```python
from sqlalchemy import select
from timelink.api.models import Act

with tlnb.db.session() as session:
    stmt = (
        select(Act)
        .where(Act.the_type == "baptismo")
        .where(Act.the_date.between("16400101", "16491231"))
    )
    acts = session.execute(stmt).scalars().all()
    for act in acts[:10]:
        print(act.id, act.the_date, act.the_type, act.loc, act.ref)
```

The DataFrame alternative for acts with attributes of participants is
`entities_with_attribute(entity_type="act", ...)`, with `name_like` to filter
by act name.

* **Deep inspection of one entity**: `entity.to_kleio()` dumps the full record
  (attributes, relations, group info) in kleio notation — much more
  informative than the table row:

```python
from timelink.api.models import Person, Attribute
from sqlalchemy import select

with tlnb.db.session() as session:
    stmt = select(Person).join(
        Person.attributes.and_(
            Attribute.the_type == "jesuita-entrada",
            Attribute.the_value.like("Coimbra"),
        )
    )
    for person in session.execute(stmt).scalars().all()[:10]:
        print(person.to_kleio())
```

* **Schema and table sizes** when facing an unfamiliar database:

```python
tlnb.table_row_count_df()                  # row counts per table
tlnb.db.get_models_ids()                   # ORM models
tlnb.db.describe("person", show=True)      # columns of a table/model
```

Dates in timelink are `AAAAMMDD` strings, possibly incomplete
(`16400000` = some month in 1640) and sometimes uncertain; compare them as
strings, not as datetime objects.

## Python environment: one shared venv, OUTSIDE this project

Do not create a virtual environment inside this repository, and do not accept
VS Code's *Create Environment* prompt — it always writes `.venv` into the
workspace root, and per-project venvs accumulate silently.

Instead, create one shared venv outside the project and register it as a
Jupyter kernel:

```bash
python3.12 -m venv ~/venvs/timelink
~/venvs/timelink/bin/pip install -U pip
~/venvs/timelink/bin/pip install timelink
~/venvs/timelink/bin/pip install -r notebooks/requirements.txt
# or, to exercise unreleased code:
~/venvs/timelink/bin/pip install -e /path/to/timelink-py-checkout

~/venvs/timelink/bin/python -m ipykernel install --user --name timelink \
    --display-name "Python (timelink)"
```

Kernel registrations are user-level, not per-folder: every notebook on the
machine can pick **Python (timelink)** from the kernel picker.

To stop VS Code from offering to create environments, preselect the
interpreter in this project's `.vscode/settings.json` (not in the template:
the path is machine specific):

```json
{ "python.defaultInterpreterPath": "/ABSOLUTE/PATH/TO/venvs/timelink/bin/python" }
```

Project resolution never depended on the venv location: it depends on the
working directory. Run notebooks from this directory or from `notebooks/`;
`find_local_kleio_home()` finds the project.

Maintenance: `~/venvs/timelink/bin/pip install -U timelink`.

## VS Code extension for Kleio

A Kleio extension for VS Code (syntax support for `.cli` files) ships in
`extras/vscode/`. Install the version provided with:

```bash
code --install-extension extras/vscode/kleio-1.0.9.vsix
```

## Project specifics

* **Sources.** One `.cli` file per letter of the alphabet (`dehergne-a.cli` …
  `dehergne-z.cli`), each with a single `lista$dehergne-notices-<letter>`
  act; `dehergne-0-abrev.cli` holds the abbreviations; the location files
  (`dehergne-locations-1644.cli`, `dehergne-locations-1701.cli`) carry the
  place lists for the two catalog years.
* **Person ids** are `deh-<nome-em-minusculas>`; homonyms get a numeric
  suffix (`deh-antonio-de-abreu-2`).
* **Voyage fleets.** Dehergne keeps Wicki's missionary numbers but not the
  fleet numbers; fleet numbers were recovered from Wicki & Boxer (1967) and
  added to each entry — see `extras/doc/Dehergne_transcription_format.md`.
* **Place names** are identified with Wikidata links
  (`ls$estadia/Goa# @wikidata:Q1171`); the ongoing location work lives in the
  fork `https://github.com/joaquimrcarvalho/dehergne-locations`.
* **Complementary sources.** Missing information (places of entry, places of
  stay, tasks) is added from the *Cartas ânuas* editions listed in
  `README.md`.
* **Notebooks.** Shared modules `dehergne_util.py`, `temporal_semantics.py`,
  `copresence.py` and `biographical_note.py` in `notebooks/`; their specs are
  the `*_spec.md` files next to them. See `notebooks/README.md` for the index.
