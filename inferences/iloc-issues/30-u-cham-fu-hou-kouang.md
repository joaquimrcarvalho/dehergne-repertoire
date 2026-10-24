# Place to identify

**U cham fu, Hou-kouang** — `vows location (jesuita-votos-local)`, **1767-12-13** (`17671213`)

## Person(s)

**Manuel da Motta** (`deh-manuel-da-motta`) — Padre · Portugal · Dehergne P. 575

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1720-07-20 | birth | Braga | Q83247 |
| 1754 | stay | China central | Q148 |
| 1757 | stay | Hou-nan | Q45761 |
| 1765 | stay | Hou-kouang | Q2235155 |
| 1767-12-13 | vows location | **U cham fu, Hou-kouang** | ❗️ **missing** |
| 1782 | death | Hou-nan | Q45761 |

**Source note** (Dehergne):
> …355)., en 1765 il a 82 chrétientés dispersées au Hou-kouang et très souvent « plerumque » peu nombreuses (SOCP 55, 1765, 355). V. « Emanuel da Motta, U cham fu, Hu Kuam », 13 déc. 1767, pr. (Hisp. 34, 476). M. 1782, au Hou-nan. Pf. 835. — Il signe Emmanuel de Motta (SOCP 55, 1765, 355)., ne pas confondre avec le P. Manuel da Matta.

## Identification

**Conclusion.** Identified as **Wuchang fu 武昌府**, the capital of **Huguang
(Hou-kouang / `Hu Kuam` 湖廣)** — modern Wuchang, Wuhan (Hubei) → `Q11124318`
(Wuchang Fu 武昌府; `Q1014420`, Wuchang District 武昌區, if the project prefers
present-day units). This is not a phonetic guess: Dehergne glosses this romanisation
**"(Wuchang)"** in four notices of the *Répertoire*, and on one of them — notice 54,
Avellar — he is reporting **the same vow register and the same folio as Motta's**,
`Hisp. 34 II, 476`, so the gloss attaches to the identical document. A fifth gloss reads
`« V-cham [Wuchang], metropolis prov. Huquang »`, and Dehergne 1957 calls `"Hukam"`
`(=Wuchang au Hukwang)`. `fu` 府 is the prefecture, and the vow was made in the
prefectural capital. **Warning on the id:** do **not** use `Q28414894` — it also carries
the English label "Wuchang Fu" but its Chinese label is **五常府**, a Manchurian
prefecture. Full research note: `notes/u-cham-fu-identification.md`.

Source fix: `sources/dehergne-m.cli:2341` —
`ls$jesuita-votos-local/U cham fu, Hou-kouang/17671213`
→ `ls$jesuita-votos-local/U cham fu, Hou-kouang#@wikidata:Q11124318/17671213`.

## Task

- [x] Confirm the place and the Wikidata ID — **identified as Wuchang fu 武昌府,
      Huguang `Q11124318`** (not `Q28414894` = 五常府); the source `.cli` still needs the
      `@wikidata` comment (see *References*).
- [x] Research note written: `notes/u-cham-fu-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 575 (Motta, Manuel da), **p. 183** | doc 65, p. 221, raw — `pha page 65 221` |
| ibid. — `à « U Cham fu » (Wuchang) en 1767 (Hisp. 34 II, 476)`, the same folio as the vow | no. 54 (Avellar, Agostinho de), **p. 18** | doc 65, p. 56, raw (image verified) — `pha page 65 56` |
| ibid. — `« Vu Cham » (Wuchang, Wou-tch'ang) fou` | no. 50 (Arxó, José Ramón), **p. 16** | doc 65, p. 54, raw (image verified) — `pha page 65 54` |
| ibid. — `« Jos. MONTEYRO, Vu Cham » (Wuchang)` | no. 563 (Monteiro, José), **p. 179** | doc 65, p. 217 — `pha page 65 217` |
| ibid. — `« V-cham [Wuchang], metropolis prov. Huquang »` | no. 770 (Silva Tchang, Emmanuel de), **p. 248** | doc 65, p. 286 — `pha page 65 286` |
| DEHERGNE, Joseph. "Les chrétientés de Chine de la période Ming (1581–1650)", *Monumenta Serica* 16 (1957) | §IV. Wuchang, **p. 49** — "capitale du Hukwang"; `"Hukam" (=Wuchang au Hukwang)` | doc 73, p. 50, raw — `pha page 73 50` |
| ARSI *Hisp.* 34, f. 476 (the vow entry itself) | cited by Dehergne | **not in this archive** |

**Note (PHA archive):** `notes/u-cham-fu-identification.md`.

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `武昌府` | — | 11 | `hvd_34300` 武昌府 (府), 1364–1911 |
| `武昌府` | `--ft fu` | 11 | `hvd_34300` 武昌府 (府), 1364–1911 |
| `Wuchang` | `--ft fu` | 14 | `hvd_34300` 武昌府 (府), 1364–1911 |
| `武昌府` | year 1767 | 3 | `hvd_34300` 武昌府 (府), 1364–1911 |
| `湖北` | — | 6 | `hvd_25005` 湖北 (省), 1820 |

**Best match.** `hvd_34300` — 武昌府 (Wuchang Fu), superior prefecture (府),
CHGIS **1364–1911**; 30.57367 N, 114.30666 E; `present_location`
"今湖北武汉市武昌". Its `source_note` (钱林书) states that from 元至正二十四年
(1364) the seat was 江夏县, "今湖北武汉市武昌", unchanged to 1911. Canonical
record: <https://chgis.hudci.org/tgaz/placename/json/hvd_34300>. The query
filtered to the Dehergne year (1767) returns the same record.

**Coordinates.** TGAZ 30.57367, 114.30666 vs Wikidata `Q11124318` (武昌府
Wuchang Fu) 30.55639, 114.31056 → **1.96 km** (prefecture seat vs the modern
Wuchang district centre — agreement).

**Verdict: `confirmed`.** TGAZ independently records 武昌府 as an Hu-guang
prefecture continuously through Dehergne's period (1364–1911), seated at
Wuchang (Wuhan) — exactly the gloss Dehergne himself gives ("U cham fu
(Wuchang)"). No change to the issue's conclusion; the `Q11124318` anchor is
supported.
