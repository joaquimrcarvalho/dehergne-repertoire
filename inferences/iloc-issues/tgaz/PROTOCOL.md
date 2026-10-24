# TGAZ pass over the iloc-issues — working protocol

This directory holds the CHGIS **Temporal Gazetteer (TGAZ)** verification pass
over the 34 location-identification issues in `inferences/iloc-issues/`.

The goal is **not** to re-do the archive research in the issue files: each
issue already states its identification (with archive references). The goal is
to add an **independent gazetteer check** — does TGAZ, which records historical
Chinese (and Russian/Tibetan) administrative units with dates and coordinates,
have the place, at what administrative level, in which parent unit, and does its
point agree with the Wikidata anchor the issue proposes? When TGAZ has the
locality, it can also **confirm or reject a candidate reading** for the issues
that are still unresolved.

## 1. What TGAZ is (verified live, 2026-10-22)

Endpoint: <https://chgis.hudci.org/tgaz> (docs <https://chgis.hudci.org/tgw/#usage>).

* **Coverage**: it integrates several layers, not only China:
  * `CHGIS` — China, 222 BC–1911, with prefecture/county units for all periods
    and **village/small-town (`cun zhen`) records only in the 1820 and 1911
    layers**;
  * `HGR` — Historical Gazetteer of the Russian Empire, ~1785–1796;
  * `TBRC` — Tibetan monasteries.
  * **Not covered**: Japan, Korea, Vietnam/Tonkin, the Philippines, Europe,
    India, Indonesia, the Americas.
* **Searching**: pinyin (`Xiangtan`, `Lvjiazhuang`) and Chinese characters
  (traditional or simplified) both work; European spellings do not. The match
  is a **prefix** match (`Hue` also returns 湖耳…), so check the returned name.
* **`--year`**: keep `year` to test which record was valid then, but **always
  also query without a year** — records whose span ends in `0` ("open ended")
  are silently dropped by the year filter, and the Jinchuan/Chenggu-type
  county records are such. A place may also exist only in the 1820/1911 layer
  (e.g. the Zhili 通州 is `hvd_103`, 1820 layer only), so a `year=1767` query
  misses it.
* **Canonical record** (`get`) is the richest output: spellings, feature type
  with English, temporal span with rules, coordinates, `present_location`,
  the year-ranged **parent chain** (`historical_context.part of`), and a
  Chinese `source_note` on the source map/layer — quote the layer and the
  `present_location` when useful.
* Records dated 1820/1911 (after the Dehergne period) are still evidence: the
  gazetteer is recording a *later* state of a locality whose name and parent
  county are continuous. Say so explicitly ("the 1911 layer records…"), never
  present a later record as contemporaneous.
* Some records have `(0, 0)` or a 0 longitude — flag as "no TGAZ coordinates".

## 2. Tool

`tgaz_tool.py` (this directory), standard library only, so plain `python3`
works. Run it from anywhere:

```bash
cd inferences/iloc-issues/tgaz

python3 tgaz_tool.py query "呂家莊"              # all hits (prefix match)
python3 tgaz_tool.py query "Shulu" --year 1744   # year-filtered
python3 tgaz_tool.py query "Tongzhou" --ft zhou  # feature-type filter
python3 tgaz_tool.py get hvd_135137 --full       # canonical record
python3 tgaz_tool.py wd Q1015480                 # Wikidata label + P625
python3 tgaz_tool.py dist 37.94665 115.43684 37.94231 115.21181
python3 tgaz_tool.py query "吕家庄" --json        # raw JSON
```

There is a 3-attempt retry in the tool. Keep roughly **0.4–1 s between
queries** (a `time.sleep(0.5)` in a loop is enough); don't hammer the server.

## 3. Per-issue procedure

1. Read your issue file. Extract: the place as transcribed, the Dehergne date,
   the province/region Dehergne gives, the **identified Chinese name(s)** and
   the **Wikidata QID** from the *Identification → Conclusion* section (if any).
2. Build a candidate query list:
   * the Chinese characters from the issue (both traditional and simplified
     forms when they differ: 呂/吕, 縣/县, 橋/桥 …);
   * the pinyin spelling of that Chinese form;
   * if the issue is unresolved, the **phonetic candidate readings** proposed
     in the issue (e.g. 老山洼, 東港/同港/塘口, 白埠/北埠/百步) and 1–3 further
     plausible readings. Be explicit that these are candidate readings.
   * add the parent unit as a query too (e.g. `Shulu`, `Linjiang`, `Gaizhou`),
     because the parent record is often what TGAZ has even when the village is
     missing.
3. Query:
   * `query NAME` (no year) → see all layers/homonyms;
   * `query NAME --year <dehergne year>` → contemporary record if any;
   * disambiguate homonyms with `--ft` (`fu`, `xian`, `zhou`, `cun zhen`) or
     `--parent`; the `parent` facet only works together with a name.
4. Pick the best match: check **name** (exact form), **feature type** (does it
   match the expected level: 府/縣/州/村鎮?), **parent chain** (same province /
   same county as the issue), and **coordinates**. Fetch `get <sys_id> --full`.
5. Compare coordinates: fetch the Wikidata item with `wd Q…`, compute `dist`.
   Under ~50 km for a county seat/city is agreement; a village 20 km from its
   county town is normal.
6. **Verdict** — one of exactly these strings:
   * `confirmed` — TGAZ has the (or the expected parent) unit, with a matching
     name, level and parent/region; coordinates agree with the Wikidata anchor
     where one exists.
   * `partially-confirmed` — TGAZ confirms the county/prefecture/parent but not
     the locality itself (village or chapel absent from its layers), or the
     level differs from the issue's anchor.
   * `contradicted` — TGAZ evidence conflicts with the issue's reading (wrong
     province, the name resolves only to a different homonym, etc.). Explain.
   * `not-in-tgaz` — region covered by TGAZ, but the place/locality is absent
     from its layers (and no parent-level match was possible).
   * `outside-coverage` — TGAZ has no layer for that region (Japan, Vietnam,
     Philippines, Europe, India, Indonesia …). One or two empty queries are
     enough; say which were tried.
7. Append a section to the issue file (template §4) and write the JSON record
   `data/<NN>.json` (schema §5).

## 4. Section template (append to the issue `.md`)

Append at the end of the file, after the last existing section. Keep it
compact: a reader should get the evidence and the verdict in under a minute.

```markdown
## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `呂家莊` | — | 2 | `hvd_135137` 吕家庄 (村鎮) |
| `Shulu` | year 1744 | 1 | `hvd_44783` 束鹿县 (縣), 1622–1911 |

**Best match.** `hvd_135137` — 吕家庄 (Lvjiazhuang), village/town (村鎮),
CHGIS **1911** layer, parent **束鹿县** (Shulu Xian); 37.94665 N, 115.43684 E;
`present_location` "河北辛集县吕家庄". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hvd_135137>.

**Coordinates.** TGAZ 37.94665, 115.43684 vs Wikidata `Q1015480` 37.94231,
115.21181 → **19.7 km** (the county town, not the village itself — normal).

**Verdict: `confirmed`.** TGAZ independently records 呂家莊 as a village of
束鹿縣, exactly the *Chou-lou hien* of Dehergne's vow formula; it also has
束鹿縣 itself for the Dehergne year. No change to the issue's conclusion.
```

For a negative result:

```markdown
## TGAZ (CHGIS) check

Checked 2026-10-22 … Queries: `Laoshanwa`, `老山洼`, `Laoshan` — **0 hits**
each; no `村鎮` record in Huguang. The county-level anchor `hvd_…` (Hanyang)
*is* in TGAZ.

**Verdict: `not-in-tgaz`.** TGAZ has no village layer for 1552–1800, so it
neither confirms nor rejects the 老山洼 reading; the issue's conclusion stands
on the archive evidence alone.
```

Rules for the section:
* every query in the table must be one you actually ran (name + filters);
* cite the `sys_id` and the JSON URL;
* state the layer/date of the record explicitly when it postdates 1552–1800;
* do not overstate: TGAZ is an *independent check*, not a primary source.

## 5. JSON record schema (`data/<NN>.json`)

```json
{
  "issue": "08",
  "file": "08-leou-kia-tchouang-do-chou-lou-hien.md",
  "place": "Leou-kia-tchouang do Chou-lou hien",
  "dehergne_year": 1744,
  "region": "Zhili / Hopei",
  "country": "China",
  "identified_chinese": "呂家莊 / 束鹿縣",
  "wikidata_id": "Q1015480",
  "queries": [
    {"name": "呂家莊", "year": null, "feature_type": null, "source": null,
     "total": 2,
     "hits": [{"sys_id": "hvd_135137", "name": "吕家庄", "transcription": "Lvjiazhuang",
               "years": "1911 ~ 1911", "feature_type": "村镇 (cun zhen)",
               "parent_name": "束鹿县 (Shulu Xian)", "lat": 37.94665,
               "lon": 115.43684, "data_source": "CHGIS"}]}
  ],
  "best_match": {"sys_id": "hvd_135137", "name": "吕家庄",
    "transcription": "Lvjiazhuang", "feature_type": "cun zhen",
    "english": "villages and small towns", "years": "1911 ~ 1911",
    "parent": "束鹿县 (Shulu Xian)", "lat": 37.94665, "lon": 115.43684,
    "data_source": "CHGIS",
    "uri": "https://chgis.hudci.org/tgaz/placename/json/hvd_135137",
    "present_location": "河北辛集县吕家庄"},
  "wikidata": {"id": "Q1015480", "label": "Xinji / 辛集市",
               "lat": 37.94231, "lon": 115.21181},
  "dist_km": 19.74,
  "verdict": "confirmed",
  "verdict_note": "TGAZ records 呂家莊 as a village of 束鹿縣; matches the issue.",
  "notes": "1911 layer; village-level TGAZ coverage is only 1820/1911.",
  "checked_at": "2026-10-22"
}
```

Keep `queries` to the informative ones (2–6 normally, up to ~15 for the hard
unresolved issues). If a query returned 0 hits, keep it in `queries` with
`"total": 0, "hits": []` — the negative results are part of the evidence.

## 6. Boundaries

* **Only write** the issue file(s) assigned to you and `tgaz/data/<NN>.json`
  for those issues. Do not touch the `.cli` sources, other issues,
  `INDEX.md`, `TGAZ-RESOLUTION.md`, or `tgaz_tool.py`.
* Do not invent TGAZ records, coordinates, or `sys_id`s: everything in the
  section/JSON must come from a query you ran.
* If the issue's identification is **unresolved**, TGAZ evidence may support a
  candidate reading or show it is unattested — report that as
  `partially-confirmed` / `not-in-tgaz` with the exact readings tried. Do **not**
  upgrade an inference to certain.
