# Place to identify

**Petit Tibet «Kinchuen»** — `stay (estadia)`, **1774** (`1774`)

**Petit Tibet «Kinchuen»** — `stay (estadia)`, **1777** (`1777`)

## Person(s)

**Félix da Rocha** (`deh-felix-da-rocha`) — Padre · Portugal · Chinese name: Fou Tso-Lin · Dehergne P. 692

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | stay | Dzungaria | — |
| — | stay | Szechwan | — |
| 1716-08-31 | birth | Lisboa | Q597 |
| 1737 | arrival | Macau (seminário) | Q14773 |
| 1737 | ordination | Macau | Q14773 |
| 1747-02-02 | vows location | Pequim | Q956 |
| 1753-05-01 | arrival | Pequim | Q956 |
| 1756-03-21 | stay | Pequim | Q956 |
| 1759 | stay | Pequim | Q956 |
| 1774 | stay | **Petit Tibet «Kinchuen»** | ❗️ **missing** |
| 1777 | stay | **Petit Tibet «Kinchuen»** | ❗️ **missing** |
| 1781-05-22 | death | Pequim | Q956 |

**Source note** (Dehergne):
> …. tumulaire)., vice-provincial 1753-1759., cartes de Dzoungarie (Eleuthes), part de Pékin le 21 mars 1756 (SOCP t. 51, 1757, f° 528), et 1759., et du Petit Tibet « Kinchuen » 1774 et 1777., délivre Gleyo, M.E.P., au Szechwan., 1774, président du Tribunal des Mathématiques (lettre d'AMiOT, 28 sept. 1777). Voyages, RHM 8 (1931), 43. P. avant 1737, Macao, où il poursuit les études de théologie (JS 134, 434). V. Pékin, 2 févr. 1747, pr. (Lus. 16, 265). M. Pékin, 22 mai 1781 (Planchet, p. 177). Pf. 7…

## Identification

**Conclusion.** Identified as the **金川 Jinchuan region of western Sichuan** — the "Two Jinchuan" (大小金川), today **金川縣 Jinchuan County `Q338033`** and **小金縣 Xiaojin County `Q1169539`** in 阿壩藏族羌族自治州 Ngawa prefecture — which Qianlong was conquering in the Second Jinchuan War (1771-1776). Dehergne's own notice pairs *« du Petit Tibet « Kinchuen » 1774 et 1777 »* with the Dzungar maps (no. 692, **p. 223**), and Pfister explains the two journeys: *« le 20 août 1774 … et en mars 1777 …, il fut envoyé dans le petit Tibet, **dont K'ien-long venait de faire la conquête, pour en lever le plan** »* (t. 2, **p. 774**). The reading **`Kinchuen` = 金川 is a phonetic inference** (the archive's OCR drops CJK, so no character can be quoted from it); the alternative **靖遠 Jingyuan** (Gansu) is excluded. Full research note: `notes/petit-tibet-kinchuen-identification.md`.

Source fix: `sources/dehergne-r.cli:806` and `:807` — `ls$estadia/Petit Tibet «Kinchuen»/1774` (and `/1777`) → gloss as 金川 Jinchuan (Sichuan) and add `@wikidata:Q338033` (金川縣), with `Q1169539` for 小金縣. Do **not** use `Q10935029` (Jinchuan Campaigns): it is a war, not a place.

## Task

- [x] Confirm the place and the Wikidata ID — **identified as the 金川 Jinchuan region, Sichuan; county anchor `Q338033`** (金川縣; `Q1169539` for 小金縣). The source `.cli` still needs the `@wikidata` comment (see *References*).
- [x] Research note written: `notes/petit-tibet-kinchuen-identification.md`.
- [ ] Side finding, out of scope here: the same Kleio block has the birth as `17160831` (`sources/dehergne-r.cli:788`), but Dehergne and Pfister both give **31 août 1713**.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 692, **p. 223** | doc 65, p. 261, raw — `pha page 65 261` |
| PFISTER, Louis. *Notices biographiques et bibliographiques…* t. 2 (Shanghai, 1934) | no. 353, **pp. 773-774** | doc 50, pp. 239-240 — `pha page 50 240` |
| WALEY-COHEN, Joanna. "China and Western Technology in the Late Eighteenth Century", *AHR* 98:5 (1993), 1525-1544 | pp. 1536-1537 (da Rocha at the Jinchuan front 1774; surveying Jinchuan 1777) | external PDF (IAHS/Fudan) — corroboration only, marked as an inference-check |
| *Lettres édifiantes* t. IV, p. 237; de Murr, *Journal*, t. VI, p. 265; *RHM* 8 (1931), 43 | the dates Dehergne/Pfister cite | **not in this archive** |

**Note (PHA archive):** `notes/petit-tibet-kinchuen-identification.md` (slug `petit-tibet-kinchuen-identification`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `金川` / `金川县` | — | 1 | `hvd_71150` 金川县 (縣), 607–617, parent 西城郡 — a **Sui-era Shaanxi** homonym, not the Sichuan region |
| `Jinchuan` | — | 4 | `hvd_71150` plus 锦川桥/锦川堡 villages (different characters, Sichuan/Yunnan and Liaoning) — no Sichuan 金川 |
| `大金川` | — | 0 | — |
| `小金川` | — | 1 | `hvd_167533`, a village in **Manchuria** (42.34/126.38) — homonym |
| `金川` | year 1774 | 0 | — |
| `懋功` | — | 7 | `hvd_96613` 懋功厅 (直隶厅), 1783–1911, parent 四川省 |
| `懋功` | year 1774 | 0 | — (the unit postdates the Dehergne stay) |
| `绥靖` | — | 3 | `hvd_21281` 绥靖屯 (村鎮), 1820, parent 懋功厅 |
| `崇化` | — | 5 | `hvd_21279` 崇化屯 (村鎮), 1820, parent 懋功厅 |
| `抚边` | — | 3 | `hvd_21276` 抚边屯 (村鎮), 1820, parent 懋功厅 |
| `章谷` | — | 4 | `hvd_21379` 章谷屯 (村鎮), 1820, parent 懋功厅 |

**The homonym trap.** The name **金川** itself is *not* in TGAZ as a
Qianlong-era Sichuan unit: the only 金川县 hit (`hvd_71150`, 607–617, parent
西城郡) is the Sui-era county in **Shaanxi** (32.69/109.03), and the two
`小金川`/`Jinchuan` pinyin hits are unrelated villages (one in Manchuria). A
plain "Jinchuan" search would therefore wrongly suggest the place is a Shaanxi
homonym.

**Best match — the administrative region.** `hvd_96613` — 懋功厅 (Maogong Ting),
independent sub-prefecture (直隶厅), CHGIS **1783–1911**, parent **四川省**
(Sichuan Sheng); 30.99286 N, 102.35508 E; `present_location`
"四川省小金县县治美兴镇". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hvd_96613>. This is the unit the
Qianlong government created out of the conquered **大小金川** region after the
Second Jinchuan War (1771–1776) — exactly the "Petit Tibet «Kinchuen»" of the
1774 and 1777 journeys. Its 1820 **屯** sub-units cover both modern counties:

* `hvd_21281` 绥靖屯 (村鎮, 1820, parent 懋功厅), 31.48682/102.05733,
  `present_location` "四川金川县";
* `hvd_21279` 崇化屯, `hvd_21276` 抚边屯, `hvd_21379` 章谷屯 — the other
  colonisation garrisons of the old Jinchuan territory;
* `hvd_21388` 懋功屯 (村鎮, 1820, parent 懋功厅).

**Coordinates.** TGAZ 懋功厅 30.99286, 102.35508 vs Wikidata `Q1169539`
(小金县 Xiaojin County) 31.00128, 102.36236 → **1.2 km** (the ting seat is
today's 美兴镇 in Xiaojin). The issue's primary anchor `Q338033` (金川县
Jinchuan County) 31.47803, 102.06208 is **60.7 km** from the ting seat but
**1.1 km** from TGAZ `hvd_21281` 绥靖屯 — i.e. the 金川县 seat corresponds to
the 绥靖屯 sub-unit of 懋功厅, exactly as expected.

**Verdict: `partially-confirmed`.** TGAZ has no Qianlong-era "金川" unit (only
the Sui-era Shaanxi homonym), but it confirms the **administrative region** the
issue identifies: 懋功厅, parent 四川省, whose seat and 屯 sub-units match both
`Q1169539` (小金县, 1.2 km) and `Q338033` (金川县, via 绥靖屯, 1.1 km). The
caveat is chronological: 懋功厅 begins in **1783**, *after* the 1774/1777 stays
— TGAZ records the post-war reorganisation of the same territory, not a
contemporaneous 1774 unit. The issue's identification (金川 region, Sichuan;
anchors `Q338033`/`Q1169539`) stands; it is not a Jingyuan/Gansu place.
