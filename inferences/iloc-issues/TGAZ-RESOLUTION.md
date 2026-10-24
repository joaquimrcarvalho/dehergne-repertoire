# TGAZ (CHGIS) verification of the location issues

Independent gazetteer check of the 34 location identifications in `inferences/iloc-issues/`, using the **CHGIS Temporal Gazetteer (TGAZ)** — the read-only REST service over the China Historical GIS database (Harvard & Fudan) and its integrated layers ([docs](https://chgis.hudci.org/tgw/#usage)).

Every issue file carries a `## TGAZ (CHGIS) check` section with the queries run and the evidence; this report is the consolidated view. 34 issues checked, 226 TGAZ/Wikidata queries recorded. Machine-readable data: [`tgaz/data/`](./tgaz/data/), [`tgaz/tgaz-results.csv`](./tgaz/tgaz-results.csv). Method and conventions: [`tgaz/PROTOCOL.md`](./tgaz/PROTOCOL.md). A parallel pass covers the 24 comment drafts in [`comments/`](./comments/) — see [`comments/TGAZ-COMMENTS.md`](./comments/TGAZ-COMMENTS.md).

## Method in one paragraph

For each issue the identified Chinese name(s) and pinyin form were searched in TGAZ, with and without the Dehergne year (the `year` facet silently drops records whose span end is recorded as 0, and a locality may only exist in the 1820/1911 layers). Each hit was checked for name form, feature type (府/縣/州/村鎮) and parent unit; the canonical record was fetched for spellings, dated parent chain, coordinates and `present_location`; and the TGAZ point was compared with the issue's Wikidata anchor by haversine distance. TGAZ integrates CHGIS (China, 222 BC–1911), HGR (Russian Empire 1785–1796) and TBRC (Tibet); Japan, Korea, Vietnam, the Philippines, Europe, India and Indonesia are **not** covered.

**Verdict vocabulary** (`tgaz` verdict):

- `confirmed` — TGAZ has the unit (or its expected parent) with matching name, level and parent, and coordinates agree with the Wikidata anchor where one exists;
- `partially-confirmed` — TGAZ confirms the county/prefecture/region but not the locality itself, or at a coarser level than the anchor;
- `contradicted` — TGAZ evidence conflicts with the issue's reading;
- `not-in-tgaz` — region covered, but the place is absent from the TGAZ layers;
- `outside-coverage` — TGAZ has no layer for the region.

## Summary

| Verdict | Issues |
|---|---|
| `confirmed` | 11 |
| `partially-confirmed` | 11 |
| `contradicted` | 0 |
| `not-in-tgaz` | 2 |
| `outside-coverage` | 10 |
| **total** | **34** |

## Results

| # | Place as transcribed | Year | Region | Wikidata | Best TGAZ match | Dist. km | Verdict |
|---|---|---|---|---|---|---|---|
| 01 | Czerczerse | 1794 | Belarus (Rogachev district, Homiel region) | [Q867722](https://www.wikidata.org/wiki/Q867722) | `hgr_619` Чечерск — местечко (mestechko), 1785 ~ 1796 | 0.1 | `confirmed` |
| 02 | Hirubale, Misore | 1675 | Kingdom of Mysore, India | — | — | — | `outside-coverage` |
| 03 | «in Tum cheu missionis Kim tum», au T'ong-tcheou du Hopei | 1767 | Zhili / Hopei | [Q393836](https://www.wikidata.org/wiki/Q393836) | `hvd_103` 通州 — zhou, 1820 ~ 1820 | 0.7 | `confirmed` |
| 04 | Kasuza, Arima, Japão | 1590 | Japan (Arima domain, Shimabara peninsula) | [Q6381698](https://www.wikidata.org/wiki/Q6381698) | — | — | `outside-coverage` |
| 05 | Ké Diet, Tonquim | 1754 | Tonkin, Vietnam | — | — | — | `outside-coverage` |
| 06 | Làngòi, Tonquim | 1741 | Tonkin, Vietnam | — | — | — | `outside-coverage` |
| 07 | Lao chan oua, Hou-kouang | 1759 | Huguang / Hubei | [Q2235155](https://www.wikidata.org/wiki/Q2235155) | — | — | `not-in-tgaz` |
| 08 | Leou-kia-tchouang do Chou-lou hien | 1744 | Zhili / Hopei | [Q1015480](https://www.wikidata.org/wiki/Q1015480) | `hvd_135137` 吕家庄 — cun zhen, 1911 ~ 1911 | 19.7 | `confirmed` |
| 09 | Maxagongdong | 1725 | Philippines | — | — | — | `outside-coverage` |
| 10 | Monzei, Filipinas | 1699 | Philippines | — | — | — | `outside-coverage` |
| 11 | Moulins | 1689 | Allier, Auvergne-Rhône-Alpes, France | [Q184883](https://www.wikidata.org/wiki/Q184883) | — | — | `outside-coverage` |
| 12 | Mscislaviae | 1798 | Belarus (Mogilev region) | [Q744167](https://www.wikidata.org/wiki/Q744167) | `hgr_390` Мстиславль — город (gorod), 1785 ~ 1796 | 0.2 | `confirmed` |
| 13 | « Pe-chieh » du Sinfeng, Kiangsi | 1696 | Kiangsi / Jiangxi | [Q1356667](https://www.wikidata.org/wiki/Q1356667) | `hvd_838` 信丰县 — xian, 1820 ~ 1820 | 10.5 | `partially-confirmed` |
| 14 | Pé-pou, Linkiang fou | 1787 | Jiangxi | [Q197394](https://www.wikidata.org/wiki/Q197394) | `hvd_32539` 臨江府 — fu, 1363 ~ 1911 | 14.7 | `partially-confirmed` |
| 15 | Pé-tsiuen-chan / Pe-tsien-chan / Petsiuenchan, Hukwang | 1740 | Hukwang / Hubei | [Q11108336](https://www.wikidata.org/wiki/Q11108336) | `hvd_664` 汉阳县 — xian, 1820 ~ 1820 | 24.4 | `partially-confirmed` |
| 16 | Petit Tibet «Kinchuen» | 1774 | Sichuan / Kham (Petit Tibet) | [Q338033](https://www.wikidata.org/wiki/Q338033) | `hvd_96613` 懋功厅 — zhi li ting, 1783 ~ 1911 | 60.7 | `partially-confirmed` |
| 17 | Ponti (in valle Tellina) | 1685 | Ponte in Valtellina, Sondrio, Lombardy, Italy | [Q39321](https://www.wikidata.org/wiki/Q39321) | — | — | `outside-coverage` |
| 18 | Residência francesa «Vuen ngan juxta murum qui Tartaros a Sinis dividit» | 1714 | Zhili / Hopei (Shuntian fu) | [Q1196389](https://www.wikidata.org/wiki/Q1196389) | `hvd_88202` 文安县 — xian, 0 ~ 1911 | 0.8 | `confirmed` |
| 19 | Rio Kan / rio Kan | 1594 | Kiangsi / Jiangxi | [Q1046685](https://www.wikidata.org/wiki/Q1046685) | `hvd_841` 赣县 — xian, 1820 ~ 1820 | 451.6 | `partially-confirmed` |
| 20 | San kiao hou kia | 1741 | Jiangxi / Ruizhou fu | [Q14583988](https://www.wikidata.org/wiki/Q14583988) | `hvd_32628` 瑞州府 — fu, 1369 ~ 1911 | 0.4 | `partially-confirmed` |
| 21 | Shaohing | 1706 | Zhejiang / Shaoxing fu | [Q42666](https://www.wikidata.org/wiki/Q42666) | `hvd_32185` 绍兴府 — fu, 1367 ~ 1911 | 0.7 | `confirmed` |
| 22 | Sian tan hien | 1706 | Hunan / Changsha fu (Xiangtan) | [Q215755](https://www.wikidata.org/wiki/Q215755) | `hvd_41738` 湘潭县 — xian, 1370 ~ 1911 | 3.5 | `confirmed` |
| 23 | Siao-tchai de Han-tchong, Shensi | 1657 | Shaanxi / Hanzhong fu / Chenggu | [Q1069968](https://www.wikidata.org/wiki/Q1069968) | `hvd_964` 城固县 — xian, 1820 ~ 1820 | 0.4 | `partially-confirmed` |
| 24 | Sinhoua, Hué | 1741 | Huế, central Vietnam | [Q36167](https://www.wikidata.org/wiki/Q36167) | — | — | `outside-coverage` |
| 25 | Sum Kiam (casa de um cristão) | 1732 | Kiangnan / Songjiang fu | [Q11104671](https://www.wikidata.org/wiki/Q11104671) | `hvd_32439` 松江府 — fu, 1328 ~ 1911 | 11.4 | `confirmed` |
| 26 | T'ang-kia-hiang | 1787 | Kiangnan / Songjiang fu | [Q11104671](https://www.wikidata.org/wiki/Q11104671) | `hvd_32439` 松江府 — fu, 1328 ~ 1911 | 11.4 | `partially-confirmed` |
| 27 | Tcha-yuen-keou (Chayuangou) | 1759 | Huguang / Hubei / Gucheng county | [Q14091289](https://www.wikidata.org/wiki/Q14091289) | `hvd_631` 谷城县 — xian, 1820 ~ 1820 | 1.2 | `partially-confirmed` |
| 28 | Tongko (casa de Philippe Wang) | 1747 | Jiangsu / Zhejiang | — | — | — | `not-in-tgaz` |
| 29 | Tonkosz | 1805 | Saratov oblast, Russia (Volga-German colony) | [Q958741](https://www.wikidata.org/wiki/Q958741) | `hgr_345` Саратов — главный город (glavnyi gorod), 1785 ~ 1796 | 51.6 | `partially-confirmed` |
| 30 | U cham fu, Hou-kouang | 1767 | Huguang / Hubei | [Q11124318](https://www.wikidata.org/wiki/Q11124318) | `hvd_34300` 武昌府 — fu, 1364 ~ 1911 | 2.0 | `confirmed` |
| 31 | Wouho | 1772 | Anhui | [Q1334665](https://www.wikidata.org/wiki/Q1334665) | `hvd_43268` 五河縣 — xian, 1549 ~ 1911 | 0.8 | `confirmed` |
| 32 | Yean-sam, perto do monte chamado da Cruz, Yenping, Fukien | 1649 | Fujian | [Q1337959](https://www.wikidata.org/wiki/Q1337959) | `hvd_32131` 延平府 — fu, 1368 ~ 1911 | 0.4 | `partially-confirmed` |
| 33 | Yuwei do Shansi | 1727 | Shanxi | [Q10916242](https://www.wikidata.org/wiki/Q10916242) | `hvd_95557` 右玉縣 — xian, 1725 ~ 1911 | 0.6 | `confirmed` |
| 34 | Zumbae, Tchamp-pa | 1659 | Sumba, Lesser Sunda Islands, Indonesia | [Q206368](https://www.wikidata.org/wiki/Q206368) | — | — | `outside-coverage` |

**Reading the distance column.** It is the great-circle distance between the TGAZ point and the issue's Wikidata anchor. For a confirmed place both point at the same settlement; for a `partially-confirmed` match TGAZ gives the parent unit's seat while the anchor is the locality, so 10–60 km is normal (a village lies away from its county town) and is **not** a mismatch score. For the river issue 19 the anchor is a point on a linear feature and the distance is not meaningful at all.

---

## What the gazetteer check added

Eleven of the 34 identifications are now **independently confirmed** by TGAZ,
with the historical administrative parent and a point that agrees with the
issue's Wikidata anchor: **01, 03, 08, 12, 18, 21, 22, 25, 30, 31, 33**. For six
of them the two gazetteers agree to under a kilometre, which is as strong as
independent gazetteer evidence gets:

| Issue | Place | TGAZ record | TGAZ vs Wikidata |
|---|---|---|---|
| 01 | Czerczerse / Chachersk (Belarus) | `hgr_619` Чечерск, местечко, 1785–1796 | **0.09 km** |
| 12 | Mscislaviae / Mstsislaw (Belarus) | `hgr_390` Мстиславль, город, 1785–1796 | **0.23 km** |
| 33 | Yuwei / 右衛 = 右玉 (Shanxi) | `hvd_95557` 右玉县, 1725–1911 (前身 右玉卫) | **0.63 km** |
| 03 | T'ong-tcheou, Zhili (Hebei) | `hvd_103` 通州, 州, parent 順天府, 1820 | **0.7 km** |
| 21 | Shaohing / 紹興 (Zhejiang) | `hvd_32185` 绍兴府, 1367–1911 | **0.7 km** |
| 31 | Wouho / 五河 (Anhui) | `hvd_43268` 五河县, 1549–1911 | **0.8 km** |

Ten of the China identifications are **partially confirmed**: TGAZ has the
county or prefecture but not the locality itself, because CHGIS records
villages and small towns only in its **1820 and 1911 layers** — after the
Dehergne period — and has no river layer at all. These are **13, 14, 15, 16,
19, 20, 23, 26, 27, 32** (and 29 outside China). That is a limitation of the
gazetteer, not a weakness of the identifications: in each case the
administrative frame the issue argues for is confirmed, and in several the
TGAZ point sits on the anchor almost exactly (20: 0.4 km from 高安市; 23:
0.4 km from 城固县; 32: 0.4 km from 延平区; 27: 1.2 km from 谷城县).

Two issues are **not in TGAZ** at any level for the locality — **07 (Lao chan
oua)** and **28 (Tongko)** — and TGAZ attests none of the candidate readings
tested, so those remain archive-only inferences. Ten issues lie **outside
TGAZ coverage** entirely (Japan, Vietnam, Philippines, France, Italy, India,
Indonesia); for them the section records the queries run and the negative
result, so the absence of evidence is documented rather than assumed.

## The year facet and the homonyms it hides

The single most useful methodological result: a year-filtered query alone can
return the **wrong homonym**, and only the unfiltered query plus the parent
chain exposes it.

* **03 (通州)** — `year=1767` returns only the **Jiangsu** 通州 (today 南通,
  Nantong, `hvd_33310`, 955 km away), because the Zhili 通州 exists only in the
  1820 layer (`hvd_103`, parent 順天府, 0.7 km from Q393836). The year filter
  would have "confirmed" exactly the place Dehergne's parenthesis rejects.
* **23 (小寨子)** — the only 小寨子 in TGAZ is a village under 望都县 in
  Zhili (`hvd_134896`), not the Shaanxi village; the parent county 城固縣 is
  the confirmable part.
* **16 (Kinchuen)** — plain 金川 returns only a Sui-era 金川县 in Shaanxi
  (`hvd_71150`); the historical unit of the Jinchuan region is 懋功厅
  (`hvd_96613`, 1783–1911), whose seat is 1.2 km from 小金县 and whose 绥靖屯
  sub-unit (`hvd_21281`) is 1.1 km from 金川县.
* **31 (Wouho)** — 五河县 (`hvd_43268`) is 0.8 km from Q1334665 and 205.8 km
  from Q359990 (Wuhu), the id the `.cli` currently carries — a direct
  gazetteer demonstration that the existing link is wrong.
* **12 (Mscislaviae)** — the Latin-spelling records are dropped by the
  `--year` facet while the Cyrillic ones are kept; the unfiltered query is the
  reliable one for HGR.
* **18 (文安)** — TGAZ places 文安县 118.9 km south of the 順天府 seat, which
  confirms the *name* and the administrative frame but gives **no support** to
  the Latin tag *« iuxta murum qui Tartaros a Sinis dividit »*; the issue's
  qualification is left exactly as it stands.

## What TGAZ could not settle

* **07 (Lao chan oua)** — 老山洼 / 老山窪 / 老山凹 / 牢山 / Laoshanwa: no
  record; the prefectures 漢阳府 and 武昌府 exist but Dehergne gives no
  prefecture to attach the name to. The 老山洼 reading remains an inference.
* **14 (Pé-pou)** — 白埠 / 北埠 / 百步 / 裴埠: none under 臨江府; the
  prefecture and 清江縣 are confirmed, so the issue's "prefecture-level anchor
  only" conclusion is the right one.
* **28 (Tongko / "Tsangzo")** — 同港 / 董港 return nothing; 東港 / 塘口 hits are
  in other provinces. The only corridor-fitting candidate is 張涇匯
  (`hvd_139331`, 嘉善縣 → 嘉興府), phonetically possible but with no
  documentary link — not promoted. 張澤 (松江府) and 張渚 (常州府) were checked
  and rejected.
* **26 (T'ang-kia-hiang)** — TGAZ has 松江府 but neither 湯家巷 nor 唐家巷, so
  the 湯/唐 first-character question stays open.
* **19 (Rio Kan)** — no river layer (贛江 / 十八灘 = 0); only the
  administrative frame 贛縣 / 贛州府 / 萬安縣 is confirmed, so the Wikidata
  point (451.6 km from 贛縣) says nothing about the river.
* **European alias spellings (`Ciquione` and the like)** — TGAZ indexes only
  Chinese characters and pinyin, so Dehergne's source spellings return **0**
  (`Ciquione`, `Ciquion`, `Shaoshing`, `Shaohing`, `Xaohing`). The alias can
  only be resolved through the author's own gloss: Dehergne prints
  *«Ciquione» (Shaoshing, Chao-hing), Tchö-kiang* on the 1586 António de
  Almeida line and lists the form among the spellings of 紹興 in 1957
  (*« Écrit: Ciquione (CorB II 794), Ciaushino, Sciauhim … »*, entry 18,
  printed p. 20) — which lands on the same prefecture as issue 21,
  `hvd_32185` (2 hits with `year=1586`), with the 附郭 counties 山陰縣
  `hvd_40762` and 會稽縣 `hvd_40763` on the same point. A village-level check
  is impossible for 1586 in any case: the 村鎮 layer exists only for 1820 and
  1911. This is a general caution for the pass — a 0-hit TGAZ result for a
  Dehergne spelling is not evidence that the place is missing from the
  gazetteer, only that the spelling is European.

## Data-quality by-products (reported, not applied)

The pass is read-only on the sources, as the issue files are the deliverables.
Two pre-existing wrong `@wikidata` links surfaced from the gazetteer evidence
and should be fixed in the `.cli` files:

1. **Shaoshing is linked to Cixi.** Four lines use `Q706161` (Cixi 慈溪,
   Ningbo) for Shaoshing/Chao-hing, the place issue 21 identifies as 紹興
   `Q42666`: `sources/dehergne-a.cli:513`, `sources/dehergne-locations-1644.cli:158`,
   `sources/dehergne-r.cli:2045` and `:2064`. (The `Q706161` at
   `sources/dehergne-locations-1644.cli:155`, geo3$Tzeki, is correctly Cixi.)
   TGAZ corroborates the correction: 慈谿县 (`hvd_40732`, 1418–1911) is
   recorded under **寧波府 Ningpo Fu**, not 紹興府 — the two prefectures are
   neighbours, and Dehergne himself glosses the 1586 Almeida stay as
   Shaohing (Chao-hing), Tchö-kiang.
2. **Wouho is linked to Wuhu.** `sources/dehergne-l.cli:323` carries
   `@wikidata:Q359990` (蕪湖 Wuhu) for Wouho; the gazetteer shows 五河县
   `Q1334665`, 205.8 km from Wuhu. This is the fix already proposed in issue
   31.

## Caveats

* TGAZ records the **state of a place in a documented layer**, not a continuous
  history. 1820/1911 records for a village and a 1622–1911 county record are
  evidence of name and parent-unit continuity, not proof that the same
  settlement existed in 1552–1800; the issue sections say so where it matters.
* Coordinates are compared only as a sanity check. For a **parent-only** match
  the distance is the distance from the issue's anchor to the parent's seat —
  for a locality that is normal (a village is often 10–30 km from its county
  town), for a river it is meaningless, and it is never by itself a measure of
  identification quality.
* TGAZ searches are **prefix** matches, so a "hit" can be a different name
  with the same first characters (e.g. `Hue` → 湖耳蛮夷长官司). Every claimed
  match was checked on the full returned name, feature type and parent.
* The service has no SLA. All 226 queries recorded here are replayable with
  `tgaz/replay.py`; the copies of the evidence live in `tgaz/data/*.json`.

## Per-issue evidence

### 01 — Czerczerse (confirmed)

TGAZ HGR records Чечерск (Chechersk) as a mestechko of Rogachev uezd, Mogilev namestnichestvo, 0.09 km from the Wikidata point; matches the issue's Chachersk/Rogachev identification.

Queries: `Чечерск` → 1 hit(s); `Chechersk` → 1 hit(s); `Czeczersk` → 0 hit(s); `Czerczerse` → 0 hit(s); `Chachersk` (year=1794) → 0 hit(s); `Чечерск` (year=1794) → 1 hit(s); `Rogachev` → 2 hit(s).

Best record: parent Рогачевский уезд (Rogachevskii uezd), present location “Čačersk, Homiel Province, Belarus”, <https://chgis.hudci.org/tgaz/placename/json/hgr_619>.

### 02 — Hirubale, Misore (outside-coverage)

TGAZ has no Indian layer; all five queries (both readings of the illegible word, Hubli, and Mysore) returned 0 hits. TGAZ cannot help decide between Kubale and Hirubale.

Queries: `Hirubale` → 0 hit(s); `Kubale` → 0 hit(s); `Hubli` → 0 hit(s); `Mysore` → 0 hit(s); `Misore` → 0 hit(s).

### 03 — «in Tum cheu missionis Kim tum», au T'ong-tcheou du Hopei (confirmed)

TGAZ records the Zhili 通州 as a 州 under 順天府 at 39.90592/116.65881, 0.7 km from Wikidata Q393836; the Jiangsu 通州 (hvd_33310) returned by the 1767 year filter is the homonym the issue rejects, 955 km away.

Queries: `通州` → 22 hit(s); `通州` (ft=zhou) → 5 hit(s); `通州` → 2 hit(s); `通州` (year=1767) → 2 hit(s); `Tongzhou` (year=1767) → 0 hit(s); `通縣` → 0 hit(s); `南通` → 0 hit(s).

Best record: parent 顺天府 (Shuntian Fu), present location “北京通县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_103>.

### 04 — Kasuza, Arima, Japão (outside-coverage)

TGAZ has no Japanese layer (CHGIS covers China, HGR the Russian Empire, TBRC Tibet). All six queries returned 0 hits, so TGAZ can neither confirm nor reject the identification.

Queries: `Kazusa` → 0 hit(s); `Kasuza` → 0 hit(s); `加津佐` → 0 hit(s); `Arima` → 0 hit(s); `有馬` → 0 hit(s); `有马` → 0 hit(s).

### 05 — Ké Diet, Tonquim (outside-coverage)

TGAZ has no Vietnamese/Tonkin layer; all queries (Vietnamese and French forms) returned 0 hits. Nothing supports or rejects the place.

Queries: `Kẻ Diet` → 0 hit(s); `Ke Diet` → 0 hit(s); `Ké Diet` → 0 hit(s); `Kẻ Diệt` → 0 hit(s).

### 06 — Làngòi, Tonquim (outside-coverage)

TGAZ has no Vietnamese/Tonkin layer; all queries returned 0 hits.

Queries: `Làngòi` → 0 hit(s); `Langoi` → 0 hit(s); `Làng Gòi` → 0 hit(s).

### 07 — Lao chan oua, Hou-kouang (not-in-tgaz)

No village record matches any candidate reading: 老山洼 / 老山窪 / 老山凹 / 牢山 / 老山 / Laoshanwa all return 0; the only 'Laoshan' hit is 劳山镇 in distant 延安府 (Shaanxi). TGAZ neither confirms nor rejects the 老山洼 inference.

Queries: `老山洼` → 0 hit(s); `老山窪` → 0 hit(s); `老山凹` → 0 hit(s); `牢山` → 0 hit(s); `Laoshanwa` → 0 hit(s); `Laoshan` → 1 hit(s); `老山` → 0 hit(s); `老山湾` → 0 hit(s); `老山窝` → 0 hit(s); `老山口` → 0 hit(s); `汉阳府` → 14 hit(s); `武昌府` → 11 hit(s); `汉阳府` (year=1759) → 3 hit(s).

### 08 — Leou-kia-tchouang do Chou-lou hien (confirmed)

TGAZ records 呂家莊 as a village of 束鹿縣 (Shulu Xian) and has 束鹿縣 itself for 1744; matches the issue's identification.

Queries: `呂家莊` → 2 hit(s); `Shulu` → 6 hit(s); `束鹿縣` → 5 hit(s); `Shulu` (year=1744) → 1 hit(s); `呂家莊` (year=1744) → 0 hit(s).

Best record: parent 束鹿县 (Shulu Xian), present location “河北辛集县吕家庄”, <https://chgis.hudci.org/tgaz/placename/json/hvd_135137>.

### 09 — Maxagongdong (outside-coverage)

TGAZ has no Philippine layer; all queries returned 0 hits, so it can neither confirm nor reject the unidentified name.

Queries: `Maxagongdong` → 0 hit(s); `Maxagong` → 0 hit(s); `Filipinas` → 0 hit(s).

### 10 — Monzei, Filipinas (outside-coverage)

TGAZ has no Philippine layer. Monzei/Monzey return 0 hits; the only 'Manila' hit is 玛泥兰 (Manilan), an 1820 CHGIS village under 三姓 in Manchuria, a pure homonym, not Manila.

Queries: `Monzei` → 0 hit(s); `Monzey` → 0 hit(s); `Manila` → 1 hit(s).

### 11 — Moulins (outside-coverage)

TGAZ has no European layer; all three queries (French and the Latin 'Molini') returned 0 hits.

Queries: `Moulins` → 0 hit(s); `Molins` → 0 hit(s); `Molini` → 0 hit(s).

### 12 — Mscislaviae (confirmed)

TGAZ HGR records Мстиславль as a town (город) of Mstislavskii uezd, Mogilev namestnichestvo, 0.23 km from the Wikidata point; matches the issue's Mscislaŭ identification.

Queries: `Mstislavl` → 1 hit(s); `Мстиславль` → 1 hit(s); `Mstislav` → 2 hit(s); `Mscislaviae` → 0 hit(s); `Mscislaw` → 0 hit(s); `Mstislavl` (year=1798) → 0 hit(s); `Мстиславль` (year=1798) → 0 hit(s).

Best record: parent Мстиславский уезд (Mstislavskii uezd), present location “Mstsislaw, Mogilev Province, Belarus”, <https://chgis.hudci.org/tgaz/placename/json/hgr_390>.

### 13 — « Pe-chieh » du Sinfeng, Kiangsi (partially-confirmed)

TGAZ confirms 信豐縣 under 赣州府 (hvd_838, 1820; hvd_40841 spans 742-1911) but has no 白家/白加 village record under either unit, so the chrétienté itself is not attested.

Queries: `白家` → 50 hit(s); `白家` → 0 hit(s); `白家村` → 0 hit(s); `白家堡` → 0 hit(s); `白加` → 0 hit(s); `信豐` → 4 hit(s); `信豐` (year=1696) → 1 hit(s); `贛州府` → 9 hit(s); `白家` (year=1696) → 1 hit(s).

Best record: parent 赣州府 (Ganzhou Fu), present location “江西信丰县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_838>.

### 14 — Pé-pou, Linkiang fou (partially-confirmed)

TGAZ confirms 臨江府 (superior prefecture, 1363–1911; present_location '江西樟树市西南临江镇'; 14.73 km from Q197394 樟树市) and the county 清江县, but no candidate for 'Pé-pou' matches: 白埠 returns only 白埠圩 in distant 会昌县, 百步 only 百步梯 in Guangdong, while 北埠 and 裴埠 return 0 (and parent-filtered 白埠/百步 under 临江府 return 0). The village remains unidentified.

Queries: `臨江府` → 7 hit(s); `临江府` (year=1787) → 2 hit(s); `Linjiang` → 49 hit(s); `清江县` → 16 hit(s); `清江县` (year=1787) → 1 hit(s); `白埠` → 1 hit(s); `白埠` → 0 hit(s); `北埠` → 0 hit(s); `百步` → 1 hit(s); `百步` → 0 hit(s); `裴埠` → 0 hit(s).

Best record: parent 江西行省, 江西布政使司, 江西省, present location “江西樟树市西南临江镇”, <https://chgis.hudci.org/tgaz/placename/hvd_32539>.

### 15 — Pé-tsiuen-chan / Pe-tsien-chan / Petsiuenchan, Hukwang (partially-confirmed)

TGAZ confirms 汉阳县 under 汉阳府 (hvd_664, 1820; hvd_43463 spans 621-1911) and its coordinates are 24.4 km from 柏泉街道 Q11108336, consistent with Dehergne's 'a 30 Kms de Hankow'; but TGAZ has no record of 柏泉/柏泉山 or 茅廟集 itself.

Queries: `柏泉` → 0 hit(s); `柏泉山` → 0 hit(s); `柏泉` (year=1740) → 0 hit(s); `茅廟集` → 0 hit(s); `茅庙集` → 0 hit(s); `Baiquan` → 7 hit(s); `漢陽府` → 10 hit(s); `漢陽府` (year=1740) → 2 hit(s); `漢陽縣` → 7 hit(s).

Best record: parent 汉阳府 (Hanyang Fu), present location “湖北武汉市汉阳”, <https://chgis.hudci.org/tgaz/placename/json/hvd_664>.

### 16 — Petit Tibet «Kinchuen» (partially-confirmed)

TGAZ has no Qianlong-era 金川 unit (the only 金川 is a Sui-era Shaanxi homonym) but confirms the region as 懋功厅 (直隶厅, 1783-1911, parent 四川省), whose seat matches Q1169539 小金县 (1.2 km) and whose 绥靖屯 sub-unit matches Q338033 金川县 (1.1 km). The unit postdates the 1774/1777 stays.

Queries: `金川` → 1 hit(s); `金川县` → 1 hit(s); `Jinchuan` → 4 hit(s); `大金川` → 0 hit(s); `小金川` → 1 hit(s); `金川` (year=1774) → 0 hit(s); `懋功` → 7 hit(s); `懋功` (year=1774) → 0 hit(s); `绥靖` → 3 hit(s); `崇化` → 5 hit(s); `抚边` → 3 hit(s); `章谷` → 4 hit(s).

Best record: parent 四川省 (Sichuan Sheng), present location “四川省小金县县治美兴镇”, <https://chgis.hudci.org/tgaz/placename/json/hvd_96613>.

### 17 — Ponti (in valle Tellina) (outside-coverage)

TGAZ has no European layer; all four queries (Latin locative, Italian forms, valley name) returned 0 hits.

Queries: `Ponti` → 0 hit(s); `Ponte` → 0 hit(s); `Ponte in Valtellina` → 0 hit(s); `Valtellina` → 0 hit(s).

### 18 — Residência francesa «Vuen ngan juxta murum qui Tartaros a Sinis dividit» (confirmed)

TGAZ records 文安县 as a county under 顺天府 at the 1714/1717 date (hvd_88202, parent chain 顺天府 1403-1724 then 顺天府南路厅), 0.8 km from Q1196389; it confirms the issue's name identification and administrative frame.

Queries: `文安` → 9 hit(s); `文安县` → 6 hit(s); `文安` (year=1714) → 1 hit(s); `文安县` (year=1717) → 1 hit(s); `Wenan` → 3 hit(s); `順天府` → 11 hit(s).

Best record: parent 顺天府 (1403-1724) → 顺天府南路厅 (1725-1911), present location “今河北文安县文安镇”, <https://chgis.hudci.org/tgaz/placename/json/hvd_88202>.

### 19 — Rio Kan / rio Kan (partially-confirmed)

TGAZ has no river layer (贛江 = 0 hits, 十八灘 = 0) but confirms the administrative units defining the Kan valley: 贛縣 under 贛州府 (hvd_841/hvd_40834) and 萬安縣 under 吉安府 (hvd_831). The 451.6 km to the river's Wikidata P625 point reflects the river's length, not a discrepancy.

Queries: `贛江` → 0 hit(s); `赣江` → 0 hit(s); `Ganjiang` → 4 hit(s); `十八灘` → 0 hit(s); `十八滩` → 0 hit(s); `贛縣` → 8 hit(s); `贛縣` (year=1594) → 1 hit(s); `贛州府` → 9 hit(s); `萬安` → 39 hit(s).

Best record: parent 赣州府 (Ganzhou Fu), present location “江西赣州市”, <https://chgis.hudci.org/tgaz/placename/json/hvd_841>.

### 20 — San kiao hou kia (partially-confirmed)

TGAZ confirms the parents 瑞州府 (hvd_32628) and 高安县 (hvd_41219) but has no record of the village 三橋/Sanqiao itself; no 三桥 village under 瑞州府 in the 1820/1911 layers.

Queries: `三橋` → 6 hit(s); `三桥` → 0 hit(s); `三桥` → 0 hit(s); `瑞州府` (year=1741) → 2 hit(s); `高安县` (year=1741) → 1 hit(s).

Best record: parent 江西省 (Jiangxi Sheng), 1645-1911, present location “江西高安县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32628>.

### 21 — Shaohing (confirmed)

TGAZ records 紹興府 (府, 1367-1911, Zhejiang) at the same point as Q42666 (0.7 km); name, level and province match the issue.

Queries: `紹興` → 10 hit(s); `紹興府` (year=1706) → 2 hit(s); `Shaoxing` → 10 hit(s); `Shanyin` → 12 hit(s); `Ciquione` → 0 hit(s); `Shaoshing` → 0 hit(s); `紹興府` (year=1586) → 2 hit(s); `山陰縣` (year=1586) → 2 hit(s); `會稽縣` (year=1586) → 1 hit(s); `Cixi` (year=1586) → 1 hit(s).

Best record: parent 浙江省 (Zhejiang Sheng), 1645-1911, present location “今浙江绍兴市”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32185>.

### 22 — Sian tan hien (confirmed)

TGAZ records 湘潭縣 (county, 1370-1911, parent 潭州府→長沙府, seat = present Xiangtan city) at 3.5 km from Q215755. Confirms the hien reading; rejected Q703818 (Yongjia, Zhejiang) is unrelated.

Queries: `湘潭` → 9 hit(s); `湘潭縣` (year=1706) → 1 hit(s); `Xiangtan` → 15 hit(s); `長沙府` → 8 hit(s).

Best record: parent 潭州府 (1370-1371) → 长沙府 (1372-1911), present location “湖南省湘潭市”, <https://chgis.hudci.org/tgaz/placename/json/hvd_41738>.

### 23 — Siao-tchai de Han-tchong, Shensi (partially-confirmed)

TGAZ confirms 城固縣 (hvd_964, 1820, parent 漢中府; continuous hvd_71005) but not the village 小寨子 itself: its only 小寨子 record is a 1911 village under 望都县, Zhili (homonym).

Queries: `小寨子` → 1 hit(s); `小寨` → 11 hit(s); `小寨子` → 0 hit(s); `小寨子` → 0 hit(s); `城固` → 5 hit(s); `城固` (year=1657) → 0 hit(s).

Best record: parent 汉中府 (Hanzhong Fu), present location “陕西城固县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_964>.

### 24 — Sinhoua, Hué (outside-coverage)

TGAZ has no Vietnamese layer. The only hits are Chinese homonyms: the prefix query 'Hue' returns 湖耳蛮夷长官司 (Guizhou, CHGIS) and 順化 returns four Chinese 顺化 units (a Tang commandery, two Gansu villages, a Later-Liang military prefecture), none anywhere near Huế (16.46 N, 107.58 E).

Queries: `Hué` → 2 hit(s); `Hue` → 2 hit(s); `Huế` → 2 hit(s); `Sinhoua` → 0 hit(s); `Sinoa` → 0 hit(s); `順化` → 4 hit(s); `顺化` → 4 hit(s).

### 25 — Sum Kiam (casa de um cristão) (confirmed)

TGAZ records 松江府 (府, 1328-1911; Jiangnan/Jiangsu) at the Songjiang seat; 11.4 km from Q11104671 and 0.7 km from Q662380. Confirms Sum Kiam = Songjiang fu.

Queries: `松江` → 8 hit(s); `松江府` (year=1732) → 2 hit(s); `Songjiang` → 8 hit(s); `華亭` → 22 hit(s).

Best record: parent 江南省 (1645-1666) → 江蘇省 (1667-1911), present location “今上海市松江县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32439>.

### 26 — T'ang-kia-hiang (partially-confirmed)

TGAZ confirms 松江府 (hvd_32439, 1328-1911) but has no record of the chrétienté 湯家巷/唐家巷: all four name variants return 0, as do the --parent 松江府 facets. No village-level coordinate exists to compare.

Queries: `唐家巷` → 0 hit(s); `湯家巷` → 0 hit(s); `汤家巷` → 0 hit(s); `Tangjiaxiang` → 0 hit(s); `唐家巷` → 0 hit(s); `湯家巷` → 0 hit(s); `唐家` → 27 hit(s); `松江府` (year=1787) → 2 hit(s).

Best record: parent 江南省 (1645-1666) → 江蘇省 (1667-1911), present location “今上海市松江县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32439>.

### 27 — Tcha-yuen-keou (Chayuangou) (partially-confirmed)

TGAZ confirms 谷城县 (hvd_631, 1820, parent 襄阳府) and even a 1911 village in 紫金鎮 (hvd_128134, present_location 湖北谷城县紫金镇), but 茶园沟/茶園溝 itself is absent from all layers (0 hits, also with --parent 谷城县).

Queries: `茶园沟` → 0 hit(s); `茶園溝` → 0 hit(s); `Chayuangou` → 0 hit(s); `茶园` → 10 hit(s); `茶园` → 0 hit(s); `谷城` → 6 hit(s); `谷城` (year=1759) → 0 hit(s); `紫金` → 1 hit(s); `襄阳府` → 11 hit(s).

Best record: parent 襄阳府 (Xiangyang Fu), present location “湖北谷城县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_631>.

### 28 — Tongko (casa de Philippe Wang) (not-in-tgaz)

TGAZ has no record of 'Tongko': 同港 and 董港 return 0; the 東港 (4) and 塘口 (4) hits are all in other provinces (Taiwan, Guangdong, Jiangxi, Zhejiang, Shaanxi) and none under 蘇州府/嘉興府/松江府 (parent-filtered: 0). No candidate is adopted.

Queries: `東港` → 4 hit(s); `同港` → 0 hit(s); `塘口` → 4 hit(s); `董港` → 0 hit(s); `东港` → 0 hit(s); `东港` → 0 hit(s); `东港` → 0 hit(s); `張澤` → 4 hit(s); `張渚` → 2 hit(s); `張涇` → 6 hit(s); `蘇州府` (ft=fu) → 6 hit(s); `嘉興府` (ft=fu) → 6 hit(s); `松江府` (ft=fu) → 6 hit(s); `苏州府` (year=1747) → 2 hit(s); `嘉兴府` (year=1747) → 2 hit(s).

### 29 — Tonkosz (partially-confirmed)

TGAZ HGR has Saratov (chief town) and Saratov uezd/namestnichestvo, the parent the issue names, but no record of Tonkosz / Tonkoszorowka / Mariental / Sovetskoye; the locality itself is absent from the HGR layer.

Queries: `Saratov` → 3 hit(s); `Саратов` → 3 hit(s); `Саратов` (year=1795) → 3 hit(s); `Saratov` (year=1805) → 0 hit(s); `Tonkosz` → 0 hit(s); `Tonkoszorowka` → 0 hit(s); `Тонкошуровка` → 0 hit(s); `Mariental` → 0 hit(s); `Мариенталь` → 0 hit(s); `Sovetskoye` → 0 hit(s); `Советское` → 0 hit(s).

Best record: parent Саратовский уезд (Saratovskii uezd), present location “Saratov, Saratov Oblast, Russia”, <https://chgis.hudci.org/tgaz/placename/json/hgr_345>.

### 30 — U cham fu, Hou-kouang (confirmed)

TGAZ records 武昌府 (superior prefecture, 1364–1911) at the Huguang capital, with present_location '今湖北武汉市武昌'; coordinates agree with the Wikidata anchor to 1.96 km. No change to the issue's conclusion.

Queries: `武昌府` → 11 hit(s); `武昌府` (ft=fu) → 11 hit(s); `Wuchang` (ft=fu) → 14 hit(s); `武昌府` (year=1767) → 3 hit(s); `湖北` → 6 hit(s).

Best record: present location “今湖北武汉市武昌”, <https://chgis.hudci.org/tgaz/placename/hvd_34300>.

### 31 — Wouho (confirmed)

TGAZ records 五河县 (county, 1549–1911), parent 泗州 from 1724 (凤阳府 before), present_location '安徽五河县治'; its point is 0.83 km from Wikidata Q1334665 (Wuhe County) and 205.8 km from Q359990 (Wuhu) — definitively Wuhe, not Wuhu.

Queries: `五河` → 5 hit(s); `五河` (year=1772) → 1 hit(s); `五河县` → 5 hit(s); `Wuhe` → 6 hit(s).

Best record: parent 凤阳府, 泗州, present location “安徽五河县治”, <https://chgis.hudci.org/tgaz/placename/hvd_43268>.

### 32 — Yean-sam, perto do monte chamado da Cruz, Yenping, Fukien (partially-confirmed)

TGAZ confirms 延平府 (prefecture, 1368–1911; present_location '福建省南平市'; 0.39 km from Q1337959 延平区), the prefectural anchor of the issue, but has no record of the village 'Yean-sam' nor of 十字山 (0 hits). The issue's own conclusion — only the Yenping anchor is justified — stands.

Queries: `延平府` → 8 hit(s); `延平` (year=1649) → 2 hit(s); `Yanping` → 21 hit(s); `十字山` → 0 hit(s).

Best record: parent 福建行省, 福建布政使司, 福建省, present location “福建省南平市”, <https://chgis.hudci.org/tgaz/placename/hvd_32131>.

### 33 — Yuwei do Shansi (confirmed)

TGAZ records 右玉县 (county, 1725–1911) as the direct successor of 右玉卫 (garrison, 1644–1724); its present_location is exactly '今山西右玉县右卫镇', 0.63 km from Q10916242 (右卫镇) and 21.68 km from Q1196894 (modern 右玉县 seat). Strong independent confirmation of the 右衛 = 右玉 reading.

Queries: `右玉` → 6 hit(s); `右玉` (year=1727) → 1 hit(s); `右玉卫` → 1 hit(s); `Youyu` → 13 hit(s).

Best record: parent 朔平府, present location “今山西右玉县右卫镇”, <https://chgis.hudci.org/tgaz/placename/hvd_95557>.

### 34 — Zumbae, Tchamp-pa (outside-coverage)

TGAZ has no Indonesian layer. Zumbae/Sumba/Sumbawa return 0 hits; the single 松巴 hit is a TBRC Tibetan monastery (sum pa ri khrod, 34.66 N 103.12 E, Gansu/Qinghai), a homonym unrelated to Sumba.

Queries: `Zumbae` → 0 hit(s); `Sumba` → 0 hit(s); `Sumbawa` → 0 hit(s); `松巴` → 1 hit(s).


## Reproducing

```bash
cd inferences/iloc-issues/tgaz
python3 tgaz_tool.py query '呂家莊'        # single lookup
python3 replay.py --limit 10              # re-run recorded queries
# verified 2026-10-22: replay.py re-ran all 226 recorded queries -> 226 ok, 0 mismatched
python3 build_report.py                   # rebuild this report
```

## Files

| Path | Content |
|---|---|
| `tgaz/README.md` | start here: what is where |
| `tgaz/PROTOCOL.md` | method, TGAZ facts, verdict and section conventions |
| `tgaz/HIGHLIGHTS.md` | the analysis section of this report |
| `tgaz/tgaz_tool.py` | TGAZ + Wikidata lookup CLI (stdlib only) |
| `tgaz/data/<NN>.json` | per-issue evidence record |
| `tgaz/tgaz-results.csv` | one row per issue (generated) |
| `tgaz/query-log.json` | all recorded queries, for replay (generated) |
| `tgaz/build_report.py` | this report's generator |
| `tgaz/replay.py` | re-runs the recorded queries against the live service |
| `tgaz/build_comments.py` | generator of the comment-draft check (`comments/`) |
| `comments/TGAZ-COMMENTS.md` | consolidated report for the 24 comment drafts |

