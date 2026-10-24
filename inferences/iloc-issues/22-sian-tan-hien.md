# Place to identify

**Sian tan hien** — `vows location (jesuita-votos-local)`, **1706-08-15** (`17060815`)
- Tentative candidate: `Q703818` (Suian, Souei-ngan hien, score 0.69) — verify.

## Person(s)

**João Duarte** (`deh-joao-duarte`) — Padre · Portugal · Chinese name: Nié Jo-wang · Dehergne P. 266

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1671-11-27 | birth | Lisboa | Q597 |
| 1703 | stay | Hunan | Q45761 |
| 1704 | stay | Siangtan, Hunan | Q215755 |
| 1706-08-15 | vows location | **Sian tan hien** | ❗️ **missing** |
| 1725 | stay | Hukwang | Q2235155 |
| 1740 | stay | Hukwang | Q2235155 |
| 1752-01-06 | death | Macau | Q14773 |

**Source note** (Dehergne):
> …ngtan au Hunan., 1725, Hukwang (JS 134, 422a)., vice-provincial de Chine, 1728-1729., 1740, Hukwang., provincial du Japon 1741-1746. V. 15 août 1706, Sian tan hien, pr. (Lus. 13, 19). Il signe Joannes Eduardus. M. 6 janv. 1752, Macao (HS 53a, 75). Borg. Cin. 376: Duarte. Pf. 558. Homonymes: HS 53a, 10 cite un fr. Joannes Duarte mort à Goa en avril 1735 et le marque de la province « Senen. ». HS 53a. 116 fait mourir un P. Joannes Duarte à Malacca le 17 mai 1762

## Identification

**Conclusion.** Identified, and the tentative candidate is **wrong**. **"Sian tan
hien" = 湘潭縣 Xiangtan (Siang-t'an) hien, Hunan → `Q215755`** (Xiangtan 湘潭,
Hunan) — the id this repository already uses for the 1704 "Siangtan, Hunan" stay
in the same entry (`sources/dehergne-d.cli:931`). The decisive evidence is inside
Dehergne's own notice 266 (printed p. 80), where the 1704 line reads
« **Siangtan au Hunan** » and the 1706 vow line reads « V. 15 août 1706,
**Sian tan hien**, pr. (Lus. 13, 19) »; and Pfister's notice 247 (printed
p. 558) spells it « **Siang-t'an 湘潭縣 (Hou-nan)** » — characters read on the
page render, since the OCR of docs 65/73/150 drops CJK. Dehergne's gazetteer
of Hunan states it is a **hien** ("Siangtan (Siang-t'an) hien, sud-ouest de
Changsha, sur le fleuve Siang-kiang"), which excludes the other, non-*hien*
Siangtan in Hupeh. **Candidate `Q703818` rejected**: on Wikidata it is
**Yongjia County 永嘉縣 (Wenzhou, Zhejiang)**, unconnected with Duarte; nothing
in doc 65, doc 73 or Pfister links him with Zhejiang (Backer–Sommervogel t. 3 has
no notice for this China missionary — only other men of the name). If a
county-level id is preferred, `Q1375015` (Xiangtan County 湘潭縣) is the modern
county, but it is not the historic county seat; `Q215755` is recommended for
consistency with the 1704 stay. Full research note:
`notes/sian-tan-hien-identification.md`.

Source fix: `sources/dehergne-d.cli:932` —
`ls$jesuita-votos-local/Sian tan hien/17060815` → add `# @wikidata:Q215755`.

## Task

- [x] Confirm the Wikidata ID for **Sian tan hien** — **identified as 湘潭縣
      Xiangtan hien, Hunan → `Q215755`** (candidate `Q703818` = Yongjia County,
      Zhejiang, rejected). The source `.cli` still needs the `@wikidata`
      comment (see *References*).
- [x] Research note written: `notes/sian-tan-hien-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | notice **266**, **p. 80** (« 1704, Siangtan au Hunan … V. 15 août 1706, Sian tan hien ») | doc 65, p. 118, raw — `pha page 65 118` |
| PFISTER, Louis. *Notices biographiques…* t. 1 | notice **247** (Duarte), **p. 558** (« Siang-t'an 湘潭縣 (Hou-nan) ») | doc 47, p. 597, raw + render — `pha page 47 597` |
| DEHERGNE, *Répertoire*, Hukwang 1701 residence list | « Changsha R'; et Siangtan R », **p. 358** | doc 65, p. 402, raw — `pha page 65 402` |
| DEHERGNE, Joseph. « La Chine centrale vers 1700. III », *AHSI* 36 (1967), fasc. 71 | « A. LE HUNAN 湖南 », entry **4** « Siangtan 湘潭 (Siang-t'an) hien », **pp. 35-36** | **not in the PHA archive** — Internet Archive scan `ahsi-1967`, leaves `page/n36.jpg`, `page/n37.jpg` |
| [Q215755](https://www.wikidata.org/wiki/Q215755) | Xiangtan 湘潭市, Hunan — recommended | Wikidata API, checked 2026-10-15 |
| [Q1375015](https://www.wikidata.org/wiki/Q1375015) | Xiangtan County 湘潭縣 — county-level alternative | Wikidata API, checked 2026-10-15 |
| [Q703818](https://www.wikidata.org/wiki/Q703818) | Yongjia County 永嘉縣, Wenzhou, Zhejiang — **rejected candidate** | Wikidata API, checked 2026-10-15 |

**Note (PHA archive):** `notes/sian-tan-hien-identification.md`
(slug `sian-tan-hien-identification`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `湘潭` | — | 9 | `hvd_41738` 湘潭县 (县), 1370–1911 |
| `湘潭縣` | year 1706 | 1 | `hvd_41738` 湘潭县 (县), 1370–1911 |
| `Xiangtan` | — | 15 | `hvd_41738` 湘潭县 (县), 1370–1911 |
| `長沙府` | — | 8 | `hvd_32753` 长沙府 (府), 1372–1911 |

**Best match.** `hvd_41738` — 湘潭縣 (Xiangtan Xian), county (县), 1370–1911,
parent chain **潭州府** (1370–1371) → **长沙府** (1372–1911); 27.8727 N,
112.91126 E; `present_location` "湖南省湘潭市". Canonical record:
<https://chgis.hudci.org/tgaz/placename/hvd_41738>. The CHGIS source note is
explicit: 湘潭县 was "降湘潭州置" in 1370, was under 潭州府, passed to 长沙府 in
1372, and its "治所即今湖南省湘潭市驻地" (the seat is the present Xiangtan city
seat) — exactly the reading the issue argues, and it also accounts for the
issue's point that the place is a *hien* and not the non-*hien* Siangtan in
Hupeh. The 1820 layer record `hvd_717` (parent 长沙府) is at the same point.

**Coordinates.** TGAZ 27.8727, 112.91126 vs Wikidata `Q215755` (湘潭市)
27.84306, 112.92283 → **3.5 km** (vs the county-level alternative `Q1375015`,
10.6 km). Agreement, and closer to the recommended `Q215755` anchor.

**Verdict: `confirmed`.** TGAZ independently records 湘潭縣 as a county of
潭州府/長沙府, Hunan, at the Xiangtan city seat — which matches the issue's
identification (`Q215755`) and confirms that the rejected candidate `Q703818`
(永嘉县, Wenzhou, Zhejiang) has no TGAZ connection here. No change to the
issue's conclusion.
