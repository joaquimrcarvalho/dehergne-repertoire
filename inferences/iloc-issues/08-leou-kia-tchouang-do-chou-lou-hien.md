# Place to identify

**Leou-kia-tchouang do Chou-lou hien** — `vows location (jesuita-votos-local)`, **1744-06-07** (`17440607`)

## Person(s)

**Joseph Saraiva Chen** (`deh-joseph-saraiva-chen`) — Padre · China · Chinese name: Chen Tong-Hing Jo-chö · Dehergne P. 745

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1709-10-31 | birth | Sou-kiang fou, Kiangnan | — |
| 1733-10-31 | entered Jesuits | Pequim | Q956 |
| 1739-03-01 | arrival | Pequim | Q956 |
| 1744-06-07 | vows location | **Leou-kia-tchouang do Chou-lou hien** | ❗️ **missing** |
| 1746 | stay | Soochow | Q42622 |
| 1766-12-17 | death | Pequim | Q956 |

**Source note** (Dehergne):
> … (JS 134, 436, 442v)., en 1746, Soochow (Pf. 709). P. 1739. V. « Xu le leu kia chuom », 7 juin 1744, c. spir.: « Joseph Sarayva » (Lus. 24, 227) -- à Leou-kia-tchouang du Chou-lou hien, près de Paoting fou (AHSI, 22 (1953), 326). M. 17 déc. 1766, près de Pékin (Planchet, p. 157)., le 16 déc. dit HS 53a, 142. Pf. 736.

## Identification

**Conclusion.** Identified as **呂家莊 Lüjiazhuang, in 束鹿縣 Shulu hien** (Zhili / Hopei; the county is today **辛集市 Xinji**, Hebei) — the Christian village Dehergne himself lists, on the very page he cites (*AHSI* 22 (1953), **p. 326**, §31), as the first of the *anciennes chrétientés* of Shulu hien: **`Lu-kia-tchoang 呂家莊`**. The vow formula *« Xu le leu kia chuom »* reads the same way — **束鹿呂家莊**, i.e. Shulu (county) + Lüjiazhuang (village). No Wikidata item exists for the village, so the anchor is the county. Full research note: `notes/leou-kia-tchouang-identification.md`.

Source fix: `sources/dehergne-s.cli:435` — `ls$jesuita-votos-local/Leou-kia-tchouang do Chou-lou hien#perto de Paoting fou/17440607` → add `@wikidata:Q1015480` (辛集市 Xinji, the successor of 束鹿縣 Shulu; the same id is already used for *Chou-lou / Shulu* at `sources/dehergne-locations-1644.cli:622`). Alternative county anchor: `Q113491787` (束鹿縣 Shulu County, historical administrative division). Romanisation caveat: the *Répertoire* prints **Leou**-kia-tchouang where the 1953 article prints **Lu**-kia-tchoang 呂家莊.

## Task

- [x] Confirm the place and the Wikidata ID — **identified as 呂家莊 in 束鹿縣 Shulu (today 辛集市 Xinji), `Q1015480`** (county-level anchor; no item exists for the village). The source `.cli` still needs the `@wikidata` comment (see *References*).
- [x] Research note written: `notes/leou-kia-tchouang-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 745, **p. 240** | doc 65, p. 278, raw — `pha page 65 278` |
| DEHERGNE, Joseph. « La mission de Pékin vers 1700 », *AHSI* 22 (1953), 314-338 | §31, **p. 326** | doc 150, p. 13 — `pha page 150 13` (CJK read from the page image) |
| DEHERGNE, Joseph. « Les chrétientés de Chine de la période Ming (1581-1650) », *Monumenta Serica* 16 (1957), 1-136 | §12, **p. 96** | doc 73, p. 97 — `pha page 73 97` |
| PFISTER, Louis. *Notices biographiques et bibliographiques…* t. 2 (Shanghai, 1934) | no. 336, **p. 736** (gives no vow place) | doc 50, p. 202 — `pha page 50 202` |
| *Bulletin catholique de Pékin* 1939, p. 207; 1942, p. 153 | cited by Dehergne for the Shulu village list | **not in this archive** |

**Note (PHA archive):** `notes/leou-kia-tchouang-identification.md` (slug `leou-kia-tchouang-identification`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `呂家莊` | — | 2 | `hvd_135137` 吕家庄 (村鎮), 1911 |
| `Shulu` | — | 6 | `hvd_44783` 束鹿县 (縣), 1622–1911 |
| `束鹿縣` | — | 5 | `hvd_44783` 束鹿县 (縣), 1622–1911 |
| `Shulu` | year 1744 | 1 | `hvd_44783` 束鹿县 (縣), 1622–1911 |
| `呂家莊` | year 1744 | 0 | — |

**Best match.** `hvd_135137` — 吕家庄 (Lvjiazhuang), village/town (村鎮), CHGIS
**1911** layer (spellings 呂家莊 / 吕家庄 / Lvjiazhuang), parent **束鹿县**
(Shulu Xian); 37.94665 N, 115.43684 E; `present_location`
"河北辛集县吕家庄". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hvd_135137>.

**Parent unit.** `hvd_44783` — 束鹿县 (Shulu Xian), county (縣), **1622–1911**,
parent **保定府** (Baoding Fu) through 1911 (the 1744 parent, `hvd_87649`);
37.84853 N, 115.30855 E;
`present_location` "今河北省辛集市东南新城镇" — i.e. the county town is today's
辛集市东南新城镇, matching the issue's "the county is today 辛集市".

**Coordinates.** TGAZ village 37.94665, 115.43684 vs Wikidata `Q1015480`
(辛集市 Xinji) 37.94231, 115.21181 → **19.7 km** (the village lies ~20 km
east of the county town — a normal village–county-seat distance).

**Verdict: `confirmed`.** TGAZ independently records 呂家莊 as a village of
束鹿縣 (Shulu Xian) — exactly the *Chou-lou hien* of Dehergne's vow formula —
and has 束鹿縣 itself for the Dehergne year (1744, `hvd_44783`). The village
record is from the 1911 layer (later than 1744) but records the same
village/county continuity, and the county record spans 1622–1911. No change to
the issue's conclusion.
