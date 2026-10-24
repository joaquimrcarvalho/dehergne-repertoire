# Place to identify

**Wouho** — `stay (estadia)`, **1772** (`1772`)

## Person(s)

**Gottfried Xaver von Laimbeckhoven** (`deh-gottfried-xaver-von-laimbeckhoven`) — Padre · Áustria · Chinese name: Nan Houai-Jen, Ngo-tö · Dehergne P. 446

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | stay | Moçambique | — |
| — | stay | Goa | — |
| 1707-01-09 | birth | Viena | Q1741 |
| 1722-01-27 | entered Jesuits | Viena | Q1741 |
| 1738-08-05 | stay | Macau | Q14773 |
| 1739-03 | stay | Hukwang | Q2235155 |
| 1740-02-02 | vows location | « Pe tsien schan » | — |
| 1749-01 | stay | Macau | Q14773 |
| 1749-12 | stay | Pequim | Q956 |
| 1755-07-22 | stay | Macau | Q14773 |
| 1756-01-21 | stay | Pequim | Q956 |
| 1771 | stay | Honan, Luyi hien | — |
| 1771 | stay | Changchow fou, Nanquim | — |
| 1772 | stay | **Wouho** | ❗️ **missing** |
| 1778-11-13 | stay | Ilha de Tsungming (Tch'ong-ming) | Q788812 |
| 1780 | stay | Nanquim | Q16666 |
| 1781 | stay | Sungkiang | Q11104671 |
| 1787-05-22 | death | T'ang-kia-hiang | — |

**Source note** (Dehergne):
> …eur (contesté par Macao) du diocèse de Pékin du 31 août 1757 à 1780., persécution au Honan, Luyi hien, 1771., réside au Nankin: Changchow fou, 1771., Wouho 1772., île de Tsungming (Tch'ong-ming, dialecte: Tsung-ming) pour voir la possibilité d'aider les chrétiens du Japon, 13 nov. 1778 Nankin 1780., Sungkiang 1781., v. 1785 aurait été réinscrit dans la Compagnie (erreur de Pf.: son nom n'est pas aux catalogues de la Russie blanche). Projets sur le Japon 1752, 1779 (Delplace, II, 250 et 259-261.,…

## Identification

**Conclusion.** Identified as **Wuhe 五河** (Wuhe *hien*), in **Anhui** (north of the
province, near Szechow 泗州) — **not Wuhu 蕪湖**. Pfister, whose notice Dehergne cites at
the head of this entry ("Pf. 760"), prints the characters at the corresponding point of
his list: "*à Tch'ang-tcheou fou 常州 (1771), à **Ou-ho 五河** (1772), à Pao-chan hien
寶山 1773…*" (t. 2, printed p. 767 — read from the page image, since the OCR of that page
drops all CJK), and Dehergne 1957 warns explicitly: "*…à **Wuho (Ou-ho) 五河** hien, sud
de Szechow […] — **distinct du Wuhu (Ou-hou)** hien du Taiping fou, sud de Nankin*"
(printed p. 52). Dehergne uses the same spelling, "Wou-ho, Anhwei", for a birth in that
province (notice 408, printed p. 127). Anchor: **`Q1334665`** (Wuhe County 五河縣, Anhui).
`Q359990` (Wuhu) is **not** supported. Full research note:
`notes/wouho-identification.md`.

**Source fix — the source currently holds a wrong guess.**
`sources/dehergne-l.cli:323` reads
`ls$estadia/Wouho#Wuhu @wikidata:Q359990/1772` (and the database holds the same
`estadia@wikidata = Q359990 @ 1772`); it must become
`ls$estadia/Wouho#@wikidata:Q1334665/1772`. Note that this is why the issue's `❗missing`
flag is misleading here: the row is not unlinked, it is linked to the wrong town.

## Task

- [x] Confirm the place and the Wikidata ID — **identified as Wuhe 五河, Anhui
      `Q1334665`**, not Wuhu 蕪湖; the existing `Q359990` (Wuhu) comment in the source is
      wrong and must be corrected (see *References*).
- [x] Research note written: `notes/wouho-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 446 (Laimbeckhoven), **p. 141** | doc 65, p. 179, raw — `pha page 65 179` |
| PFISTER, Louis. *Notices biographiques…* t. 2 | no. 352, **p. 767** — `à Ou-ho 五河 (1772)` | doc 50, p. 233, raw **+ render** — `pha page 50 233` |
| DEHERGNE, Joseph. *Répertoire* — `N. Wou-ho, Anhwei, 1697` | no. 408 (Hiu, Ignace), **p. 127** | doc 65, p. 165, raw — `pha page 65 165` |
| DEHERGNE, Joseph. "Les chrétientés de Chine de la période Ming (1581–1650)", *Monumenta Serica* 16 (1957) | ANHWEI, **p. 52** — `Wuho (Ou-ho) 五河 … distinct du Wuhu (Ou-hou)` | doc 73, p. 53, raw **+ render** — `pha page 73 53` |

**Note (PHA archive):** `notes/wouho-identification.md`.

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `五河` | — | 5 | `hvd_43268` 五河县 (县), 1549–1911 |
| `五河` | year 1772 | 1 | `hvd_43268` 五河县 (县), 1549–1911 |
| `五河县` | — | 5 | `hvd_43268` 五河县 (县), 1549–1911 |
| `Wuhe` | — | 6 | `hvd_43268` 五河县 (县); other hits are 乌河县 618–626 etc. |

**Best match.** `hvd_43268` — 五河县 (Wuhe Xian), county (县), CHGIS
**1549–1911** (spellings 五河縣 / 五河县 / Wuhe Xian); 33.13974 N,
117.88253 E; `present_location` "安徽五河县治". Its parent chain is
**凤阳府** (Fengyang Fu) 1549–1723 and **泗州** (Si Zhou) 1724–1911 — for the
Dehergne year 1772 the parent is exactly 泗州, i.e. Dehergne's "near Szechow
泗州". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hvd_43268>.

**Coordinates.** TGAZ 33.13974, 117.88253 vs Wikidata `Q1334665` (五河县 Wuhe
County) 33.14653, 117.88618 → **0.83 km** (county seat — agreement). For
contrast, `Q359990` (芜湖市 Wuhu) is at 31.33398, 118.36223, **205.8 km** away,
and Dehergne 1957 places that Wuhu in a different prefecture (the Taiping fou)
— the existing `@wikidata:Q359990` comment in `sources/dehergne-l.cli:323` is
contradicted.

**Verdict: `confirmed`.** TGAZ independently records **五河县** — the Wouho of
Dehergne's notice — in the right province, with the right 泗州 parent for 1772;
the coordinates agree with `Q1334665` to under 1 km. This is Wuhe, not Wuhu;
the wrong `Q359990` link in the source should be corrected (reported, not
edited here).
