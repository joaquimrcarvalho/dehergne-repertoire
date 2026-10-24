# Place to identify

**Rio Kan** — `death (morte)`, **1594** (`15940000`)

**rio Kan** — `stay (estadia)`, **1594** (`15940000`)

## Person(s)

**João Barradas** (`deh-joao-barradas`) — China · Dehergne P. 77

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1570 | birth | Macau | Q14773 |
| 1594 | death | **Rio Kan** | ❗️ **missing** |

**Source note** (Dehergne):
> Barradas, João (macaïste) 77 N. à Macao (v. 1570?). En 1594, en route pour entrer au noviciat, accompagne Ricci sur la rivière Kan où il fait naufrage et se noie. Pf. 25., DElia, I 341 et 344 n.

**Matteo Ricci** (`deh-joao-barradas-ref1`) — **referido** (person referenced, not the missionary)

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1594 | stay | **rio Kan** | ❗️ **missing** |

## Identification

**Conclusion.** Identified as the **贛江 Gan Jiang**, the great river of **Jiangxi** → **`Q1046685`**. Pfister prints the character beside the name: *« Après avoir traversé les monts Mei-ling **梅嶺**, il s'embarqua sur la rivière Kan **贛**, fameuse par ses récifs et ses naufrages »*, and continues with the drowning of *« Jean Barradas »* (t. 1, no. 9, **p. 25**, read from the page image). Ricci/Trigault's Latin *De Christiana expeditione* (1615), **pp. 288-290**, tells the same voyage and names the rapids ***Scie pathan*** — read as **十八灘 Shíbātān**, the eighteen rapids, Wikidata `Q16002863` (the phonetic step is flagged in the note); the Italian *Entrata nella China* (1622), pp. 232-234, tells it without naming the river. The comment currently in the sources, `#Rio Nam Khan, em Laos?`, is **wrong**. Full research note: `notes/rio-kan-identification.md`.

Source fix: `sources/dehergne-b.cli:355` and `:359` — replace `#Rio Nam Khan, em Laos?` with a Gan-river gloss and add `@wikidata:Q1046685`, e.g. `ls$morte/Rio Kan#贛江 Gan Jiang, Jiangxi — naufrágio na viagem de Ricci a Pequim/@wikidata:Q1046685/15940000` and `ls$estadia/rio Kan#贛江 Gan Jiang, Jiangxi/@wikidata:Q1046685/15940000`.

## Task

- [x] Confirm the place and the Wikidata ID — **identified as 贛江 Gan Jiang, Jiangxi, `Q1046685`**. The source `.cli` still needs the `@wikidata` comment and the *Nam Khan* comment must be removed (see *References*).
- [x] Research note written: `notes/rio-kan-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 77, **p. 25** | doc 65, p. 63, raw — `pha page 65 63` |
| PFISTER, Louis. *Notices biographiques et bibliographiques…* t. 1 (Shanghai, 1932) | no. 9, **p. 25** (chars 梅嶺 / 贛 from the page image) | doc 47, p. 64 — `pha page 47 64` |
| RICCI, Matteo; TRIGAULT, Nicolas. *De Christiana expeditione apud Sinas* (Augsburg, 1615), lib. III | **pp. 288-290** ("Scie pathan"; *Ioannem Barradas … è flumine nunquam emersit*) | doc 76, pp. 310-312, raw — `pha page 76 312` |
| RICCI, Matteo; TRIGAULT, Nicolas. *Entrata nella China* (Naples, 1622), lib. III | **pp. 232-234** (same voyage; river unnamed) | doc 72, pp. 254-256, raw — `pha page 72 255` |
| D'ELIA, Pasquale M. *Fonti Ricciane* I, 341 and 344 n. 21 | cited by Dehergne | **not in this archive** |

**Note (PHA archive):** `notes/rio-kan-identification.md` (slug `rio-kan-identification`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `贛江` / `赣江` | — | 0 | — |
| `Ganjiang` | — | 4 | unrelated villages: 甘江场 (Sichuan), 干江铺 (Sichuan), 干江头 (Gansu), 甘江墟 (Guangdong) |
| `十八灘` / `十八滩` | — | 0 | — |
| `贛縣` | — | 8 | `hvd_841` 赣县 (縣), 1820, parent 赣州府 |
| `贛縣` | year 1594 | 1 | `hvd_40834` 赣县 (縣), 553–1911 |
| `贛州府` | — | 9 | `hvd_32567` 赣州府 (府), 1365–1911 |
| `萬安` | — | 39 | `hvd_831` 万安县 (縣), 1820, parent 吉安府 (the county of the 十八灘) |

**No river layer.** TGAZ is a gazetteer of administrative units and
settlements, not of hydrography: `贛江`/`赣江` return **0**, and the pinyin
`Ganjiang` only returns four unrelated villages (甘江场, 干江铺, 干江头,
甘江墟). `十八灘` is also **0**. The river itself is therefore outside what
TGAZ records.

**Administrative frame confirmed.** The county at the head of the river,
`hvd_841` — 赣县 (Gan Xian), county (縣), CHGIS **1820** layer, parent
**赣州府** (Ganzhou Fu); 25.847 N, 114.93248 E; `present_location`
"江西赣州市". The record valid in 1594 is `hvd_40834` 赣县 (553–1911). The
prefecture `hvd_32567` 赣州府 spans 1365–1911, and `hvd_831` 万安县 (1820,
parent 吉安府) is the county on whose stretch the eighteen rapids lie.
Canonical record: <https://chgis.hudci.org/tgaz/placename/json/hvd_841>.

**Coordinates.** A river is a line, so a point comparison is not meaningful:
the Wikidata `Q1046685` (Gan River) P625 point 29.7475, 116.21167 sits on the
river's lower course, **451.6 km** from the TGAZ 贛縣 county seat at its head
(and 391.4 km from 萬安縣) — the distance measures the river's length, not a
discrepancy.

**Verdict: `partially-confirmed`.** TGAZ confirms the administrative units
that define the Kan river's upper valley — 贛縣 under 贛州府 (and 萬安縣 under
吉安府 further down) — but it has **no river or rapids record at all**, so it
neither confirms nor rejects the identification of the *Rio Kan* as the
**贛江 Gan Jiang**. That identification stands on the archive evidence
(Pfister's 贛, Ricci/Trigault's *Scie pathan* = 十八灘).
