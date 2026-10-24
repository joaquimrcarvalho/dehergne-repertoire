# TGAZ (CHGIS) check of the GitHub-issue comment drafts

The 24 identification reports in `inferences/iloc-issues/comments/` — comments drafted for the existing GitHub issues [#2](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/2) to [#68](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/68) — have been checked against the **CHGIS Temporal Gazetteer (TGAZ)**, the same service used for the 34 issue files in the main pass. Every comment file now carries a `## TGAZ (CHGIS) check` section. 24 drafts checked (19 cross-referenced to the main pass, 5 new places), 166 recorded queries. Full main-pass report: [TGAZ-RESOLUTION.md](../TGAZ-RESOLUTION.md); method: [tgaz/PROTOCOL.md](../tgaz/PROTOCOL.md).

## Relationship to the main pass

Nineteen of the comment drafts describe places already checked in the 34 issue files; their sections reproduce the recorded queries and link to the issue section that holds the full evidence. **Five drafts describe places not covered there** and were given fresh TGAZ queries:

- **#2 Lofeu** — China–Tonkin frontier station, 1722–23;
- **#29 Chang-tsin do Yüansi** — 鄖西縣, Hubei;
- **#30 Chang-si** — Shanxi province;
- **#33 Ko-li-tsem do Kiating** — 嘉定縣, Kiangnan;
- **#63 Tongko / "Tsangzo"** — the Changshu 常熟 district (Jiangsu).

## Summary

| Verdict | Comment drafts |
|---|---|
| `confirmed` | 7 |
| `partially-confirmed` | 15 |
| `not-in-tgaz` | 2 |
| **total** | **24** |

## Results

| GH issue | Place | Year | Region | Anchor | Best TGAZ match | Dist. km | Verdict | TGAZ pass ref. |
|---|---|---|---|---|---|---|---|---|
| [#2](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/2) | Lofeu (羅浮), China–Tonkin frontier | 1722 | China–Tonkin frontier (Qinzhou area / Tonkin side) | — | — | — | `not-in-tgaz` | **new** |
| [#4](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/4) | Chayüankow / Tcha-yuen-keou | 1759 | Hubei (Gucheng county) | [Q14091289](https://www.wikidata.org/wiki/Q14091289) | `hvd_631` 谷城县 (xian) | — | `partially-confirmed` | [issue 27](../27-tcha-yuen-keou.md) |
| [#27](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/27) | Choui tcheou San Kia / San-kiao | 1745 | Jiangxi (Ruizhou fu / Gao'an) | [Q14583988](https://www.wikidata.org/wiki/Q14583988) | `hvd_32628` 瑞州府 (fu) | — | `partially-confirmed` | [issue 20](../20-san-kiao-hou-kia.md) |
| [#29](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/29) | Chang-tsin do Yüansi | 1786 | Hubei (Yunyang fu / Yunxi county) | [Q1154509](https://www.wikidata.org/wiki/Q1154509) | `hvd_45962` 郧西县 (xian) | 0.7 | `partially-confirmed` | **new** |
| [#30](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/30) | Chang-si (Chan-si) | 1696 | Shanxi province | [Q46913](https://www.wikidata.org/wiki/Q46913) | `hvd_112103` 山西省 (sheng) | 0.1 | `confirmed` | **new** |
| [#33](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/33) | Ko-li-tsem do Kiating | 1745 | Kiangnan (Jiading county, 太倉州 from 1724) | [Q46539546](https://www.wikidata.org/wiki/Q46539546) | `hvd_40393` 嘉定县 (xian) | 0.0 | `partially-confirmed` | **new** |
| [#38](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/38) | «in Tum cheu missionis Kim tum» / T'ong-tcheou | 1767 | Zhili / Hopei | [Q393836](https://www.wikidata.org/wiki/Q393836) | `hvd_103` 通州 (zhou) | 0.7 | `confirmed` | [issue 03](../03-in-tum-cheu-missionis-kim-tum-au-tong-tcheou-du-ho.md) |
| [#42](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/42) | Lao chan oua, Hou-kouang | 1759 | Huguang / Hubei | — | — | — | `not-in-tgaz` | [issue 07](../07-lao-chan-oua-hou-kouang.md) |
| [#43](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/43) | Leou-kia-tchouang do Chou-lou hien | 1744 | Zhili / Hopei (Shulu county) | [Q1015480](https://www.wikidata.org/wiki/Q1015480) | `hvd_135137` 吕家庄 (cun zhen) | 19.7 | `confirmed` | [issue 08](../08-leou-kia-tchouang-do-chou-lou-hien.md) |
| [#48](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/48) | «Pe-chieh» du Sinfeng | 1696 | Jiangxi (Xinfeng county, Ganzhou fu) | [Q1356667](https://www.wikidata.org/wiki/Q1356667) | `hvd_838` 信丰县 (xian) | 10.5 | `partially-confirmed` | [issue 13](../13-pe-chieh-du-sinfeng-kiangsi.md) |
| [#49](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/49) | Pé-pou, Linkiang fou | 1787 | Jiangxi (Linjiang fu / Qingjiang) | [Q197394](https://www.wikidata.org/wiki/Q197394) | `hvd_32539` 臨江府 (fu) | 14.7 | `partially-confirmed` | [issue 14](../14-pe-pou-linkiang-fou.md) |
| [#50](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/50) | Pé-tsiuen-chan / Pe tsien schan | 1740 | Huguang / Hubei (Hanyang) | [Q130298171](https://www.wikidata.org/wiki/Q130298171) | `hvd_664` 汉阳县 (xian) | 23.8 | `partially-confirmed` | [issue 15](../15-pe-tsiuen-chan-hukwang.md) |
| [#51](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/51) | Petit Tibet «Kinchuen» | 1774 | Sichuan (Jinchuan region) | [Q338033](https://www.wikidata.org/wiki/Q338033) | `hvd_96613` 懋功厅 (zhi li ting) | 60.7 | `partially-confirmed` | [issue 16](../16-petit-tibet-kinchuen.md) |
| [#55](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/55) | San kiao hou kia | 1741 | Jiangxi (Ruizhou fu / Gao'an) | [Q14583988](https://www.wikidata.org/wiki/Q14583988) | `hvd_32628` 瑞州府 (fu) | — | `partially-confirmed` | [issue 20](../20-san-kiao-hou-kia.md) |
| [#56](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/56) | Shaohing | 1706 | Zhejiang (Shaoxing fu) | [Q42666](https://www.wikidata.org/wiki/Q42666) | `hvd_32185` 绍兴府 (fu) | 0.7 | `confirmed` | [issue 21](../21-shaohing.md) |
| [#57](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/57) | Sian tan hien | 1706 | Hunan (Xiangtan county) | [Q215755](https://www.wikidata.org/wiki/Q215755) | `hvd_41738` 湘潭县 (xian) | 3.5 | `confirmed` | [issue 22](../22-sian-tan-hien.md) |
| [#58](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/58) | Siao-tchai de Han-tchong | 1657 | Shaanxi (Chenggu county, Hanzhong fu) | [Q1069968](https://www.wikidata.org/wiki/Q1069968) | `hvd_964` 城固县 (xian) | 0.4 | `partially-confirmed` | [issue 23](../23-siao-tchai-de-han-tchong-shensi.md) |
| [#61](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/61) | T'ang-kia-hiang | 1787 | Kiangnan (Songjiang fu) | [Q11104671](https://www.wikidata.org/wiki/Q11104671) | `hvd_32439` 松江府 (fu) | 11.4 | `partially-confirmed` | [issue 26](../26-tang-kia-hiang.md) |
| [#62](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/62) | Tcha-yuen-keou | 1759 | Hubei (Gucheng county) | [Q14091289](https://www.wikidata.org/wiki/Q14091289) | `hvd_631` 谷城县 (xian) | — | `partially-confirmed` | [issue 27](../27-tcha-yuen-keou.md) |
| [#63](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/63) | Tongko (near "Tsangtzo") | 1747 | Jiangsu (Changshu, Suzhou fu) | [Q1015805](https://www.wikidata.org/wiki/Q1015805) | `hvd_40382` 常熟县 (xian) | 0.4 | `partially-confirmed` | **new** |
| [#64](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/64) | Tonkosz | 1805 | Saratov, Russia (Volga-German colony) | [Q958741](https://www.wikidata.org/wiki/Q958741) | `hgr_345` Саратов (главный город (glavnyi gorod)) | 51.6 | `partially-confirmed` | [issue 29](../29-tonkosz.md) |
| [#65](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/65) | U cham fu, Hou-kouang | 1767 | Huguang / Hubei (Wuchang) | [Q11124318](https://www.wikidata.org/wiki/Q11124318) | `hvd_34300` 武昌府 (fu) | 2.0 | `confirmed` | [issue 30](../30-u-cham-fu-hou-kouang.md) |
| [#67](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/67) | Yean-sam, Yenping | 1649 | Fujian (Yanping fu) | [Q1337959](https://www.wikidata.org/wiki/Q1337959) | `hvd_32131` 延平府 (fu) | 0.4 | `partially-confirmed` | [issue 32](../32-yean-sam-perto-do-monte-chamado-da-cruz-yenping-fu.md) |
| [#68](https://github.com/joaquimrcarvalho/dehergne-repertoire/issues/68) | Yuwei do Shansi | 1727 | Shanxi (Youyu county) | [Q10916242](https://www.wikidata.org/wiki/Q10916242) | `hvd_95557` 右玉縣 (xian) | 0.6 | `confirmed` | [issue 33](../33-yuwei-do-shansi.md) |

**Reading the distance column.** It is the great-circle distance between the TGAZ point and the anchor proposed or recommended in the comment. For a confirmed place both point at the same settlement; for a `partially-confirmed` match TGAZ gives the parent unit's seat while the comment's anchor is the locality, so a 10–60 km gap is normal and is not a mismatch score.

---

## What the check added

Seven drafts are **independently confirmed** by TGAZ — **#30, #38, #43, #56,
#57, #65, #68** — two are **not in TGAZ** (**#2, #42**), and fifteen are
**partially confirmed** (the county/prefecture/region is in the gazetteer, the
locality or colony is not). The 19 drafts that describe places already covered
by the main pass reproduce those verdicts; the five new places add real
evidence:

| GH issue | Place | TGAZ record | Result |
|---|---|---|---|
| #30 | Chang-si = 山西 | `hvd_112103` 山西省, 1644–1911 | **0.06 km** from Q46913 — the province-level anchor is exact |
| #33 | Ko-li-tsem do Kiating | `hvd_40393` 嘉定縣, parent chain **蘇州府 1369–1723 → 太倉州 1724–1911** | **0.0 km** from the Qing county Q46539546; the comment's 1724 frame is reproduced by the gazetteer |
| #63 | Tongko / "Tsangzo" | `hvd_40382` 常熟縣, 1369–1911, parent 蘇州府 | **0.38 km** from Q1015805 — confirms the **Changshu** gloss at district level |
| #29 | Chang-tsin do Yüansi | `hvd_45962` 鄖西縣, 1476–1911, parent 鄖陽府 | **0.69 km** from Q1154509 — county-only conclusion vindicated |
| #2 | Lofeu (羅浮) | none | `not-in-tgaz`; homonyms only |

### #63 changes the answer for Tongko

The strongest result is **#63**. Its argument rests on Dehergne's own cross-entry
gloss in notice 51 — «l'église de Tong ko, près de "Tzang zo" (**Tch'ang-chou**,
Changshu)» — which reads *Tsangtzo* as the Wu-dialect form of **常熟** and puts
the village near Changshu, not "entre Soochow et Kashing". TGAZ independently
records **常熟縣** `hvd_40382` (county, 1369–1911, parent 蘇州府) at 31.64658 N
120.73379 E, `present_location` "今江苏常熟市区", **0.38 km** from Q1015805. The
district-level reading is therefore gazetteer-confirmed, and the earlier TGAZ
test in iloc issue 28 (which checked 張澤/張渚/張涇 inside the Soochow–Kashing
corridor and could not find the village) was testing the wrong frame. Tongko
itself is still absent: TGAZ's 1820/1911 village layer has one Tong-/Tang-named
market town in the county, **唐市鎮** `hvd_23781` (1820, 村鎮, parent 常熟縣,
31.54781 N 120.84787 E), but `Tongko` is not phonetically 唐市 (Tangshi), so it
is recorded and **not adopted**. Issue 28 now carries a cross-reference note.

### Wikidata codes adjudicated by the gazetteer

* **#65** — the draft corrects the contributed `Q1112431` (which is **NGC 4546,
  a galaxy**) to `Q11124318`; TGAZ `hvd_34300` 武昌府 (1364–1911, `present_location`
  "今湖北武汉市武昌") is 1.96 km from Q11124318, so the corrected item is the
  right one. The second "Wuchang Fu" item `Q28414894` (五常府, Manchuria) has no
  TGAZ counterpart.
* **#57** — TGAZ 湘潭縣 `hvd_41738` (1370–1911, seat = present Xiangtan city) is
  **3.5 km** from the draft's recommended `Q215755` and **10.6 km** from the
  contributed `Q1375015` (the residual modern county, whose seat moved in the
  1950s): the gazetteer supports the draft's choice.
* **#58** — TGAZ 城固縣 `hvd_964` (1820, parent 漢中府) is **0.42 km** from
  `Q1069968` and **29 km** from `Q515573` (Hanzhong city, the contributed code):
  the draft's rejection of Q515573 as "only asserting died in Hanzhong" is
  consistent, and the village 小寨子 is absent from TGAZ (its only record is a
  Zhili homonym under 望都縣).
* **#49** — 臨江府 `hvd_32539` (1363–1911) is confirmed and none of 白埠/北埠/
  百步/裴埠 falls under it; the contributed `Q13802007` (白埠村 in Pizhou,
  Jiangsu, 756 km away) has no gazetteer connection — the draft rejects it.
* **#55 / #27** — the parent units are confirmed (瑞州府 `hvd_32628`, 高安縣
  `hvd_41219`), but **no 三橋 village is recorded under either**, so neither
  `Q14583746` (瑞州街道) nor `Q14583988` (三桥村) is gazetteer-confirmable; the
  draft's Q14583746 → Q14583988 correction is a Wikidata-structure argument,
  not a gazetteer one.
* **#38** — `hvd_103` 通州 (州, 1820, parent 順天府) is **0.7 km** from Q393836;
  the year-filtered query at 1767 would have returned only the **Jiangsu**
  通州 (Nantong, 955 km away), the homonym the draft rejects.
* **#4 / #62** — 谷城縣 `hvd_631` is confirmed and the 1911 village `hvd_128134`
  紫金洞塘 lies in **紫金鎮**, the township containing the drafts' 沈垭村 anchor;
  but the valley 茶園溝 itself is absent, and the contributed `Q1337942`
  (衡山縣, Hunan) has no gazetteer connection.
* **#43, #48, #50, #51, #56, #61, #64, #67, #68** — reproduce the main-pass
  confirmations: 呂家莊/束鹿縣 (#43), 信豐縣/贛州府 (#48), 漢陽縣 (#50),
  懋功廳/綏靖屯 (#51), 紹興府 (#56), 松江府 (#61), HGR Saratov (#64), 延平府
  (#67), 右玉縣/右玉衛 (#68).

## What TGAZ could not do for the drafts

* **#2 Lofeu** — the only 罗浮 in TGAZ is a village under 嘉應州 (Guangdong,
  24.52 N 115.58 E), ~700 km from the Tonkin border; 羅浮洞 returns nothing;
  罗富哨 is in 南丹土州 (north-west Guangxi). The Qing **欽州** `hvd_320` is
  present at prefecture level, but **防城縣** appears only from 1887. The
  cross-border 羅浮 of the 1722 persecution is outside the gazetteer, which is
  consistent with its probable location on the Tonkin side.
* **#42 Lao chan oua** — reproduces the main pass: no candidate reading
  (老山洼/老山窪/老山凹/牢山) is in TGAZ, and 漢陽府/武昌府 are present but
  unattachable because Dehergne gives no prefecture.
* **#29, #33, #63, #4/62, #27/55, #61** — the locality (village, valley or
  chapel) is absent, because CHGIS village-level coverage exists only in the
  1820/1911 layers; only the administrative frame can be confirmed.

## Caveats

* The 19 cross-referenced sections reproduce the queries recorded in the main
  pass, not new ones; the five new places (#2, #29, #30, #33, #63) were queried
  afresh on 2026-10-22.
* TGAZ is a **prefix** search: `嘉定` returns mostly 嘉定府 in Sichuan, and
  `Shanxi` returns both 山西 and 陕西 — every claimed match was checked on the
  full name, feature type and parent chain.
* A `partially-confirmed` distance compares the TGAZ **parent seat** with the
  comment's **locality anchor**; a 10–60 km gap is normal and is not a mismatch
  score (rivers and colonies are flagged separately).

## Per-draft evidence

### #2 — Lofeu (羅浮), China–Tonkin frontier (`not-in-tgaz`)

TGAZ has no record of the cross-border 羅浮; its only 罗浮 is a village under 嘉應州 (Guangdong, 24.52 N 115.58 E), a homonym, and 羅浮洞 returns nothing. The Qing 欽州 is present at prefecture level.

Queries: `羅浮` → 1 hit(s); `Luofu` → 2 hit(s); `羅浮洞` → 0 hit(s); `欽州` → 25 hit(s); `防城` → 3 hit(s).

### #4 — Chayüankow / Tcha-yuen-keou (`partially-confirmed`)

Same place as iloc issue 27: 谷城縣 confirmed (hvd_631), 茶園溝 absent; the 1911 village 紫金洞塘 lies in the same 紫金鎮.

Queries: `茶园沟` → 0 hit(s); `茶園溝` → 0 hit(s); `Chayuangou` → 0 hit(s); `茶园` → 10 hit(s); `茶园` (parent=谷城县) → 0 hit(s); `谷城` → 6 hit(s); `谷城` (year=1759) → 0 hit(s); `紫金` (parent=谷城县) → 1 hit(s); … 1 more.

Best record: parent 襄阳府 (Xiangyang Fu), present location “湖北谷城县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_631>.

### #27 — Choui tcheou San Kia / San-kiao (`partially-confirmed`)

Same place as iloc issue 20: 瑞州府 hvd_32628 and 高安縣 confirmed, but no 三橋 village under them; Q14583988 has no P625.

Queries: `三橋` → 6 hit(s); `三桥` (parent=高安县) → 0 hit(s); `三桥` (parent=瑞州府) → 0 hit(s); `瑞州府` (year=1741) → 2 hit(s); `高安县` (year=1741) → 1 hit(s).

Best record: parent 江西省 (Jiangxi Sheng), 1645-1911, present location “江西高安县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32628>.

### #29 — Chang-tsin do Yüansi (`partially-confirmed`)

TGAZ confirms 鄖西縣 (hvd_45962, county, 1476–1911, parent 鄖陽府, present '今湖北省郧西县'), 0.69 km from Q1154509; the locality 'Chang-tsin' is absent.

Queries: `鄖西` → 4 hit(s); `鄖陽府` → 6 hit(s); `Yunxi` → 19 hit(s).

Best record: parent 郧阳府 (1476–1911), present location “今湖北省郧西县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_45962>.

### #30 — Chang-si (Chan-si) (`confirmed`)

TGAZ has 山西省 (hvd_112103, province, 1644–1911, present '山西省太原市'), 0.06 km from Q46913; the province-level anchor is exactly right.

Queries: `山西` → 6 hit(s); `Shanxi` → 36 hit(s); `山西布政使司` → 1 hit(s).

Best record: parent 清 (1644–1911), present location “山西省太原市”, <https://chgis.hudci.org/tgaz/placename/json/hvd_112103>.

### #33 — Ko-li-tsem do Kiating (`partially-confirmed`)

TGAZ confirms 嘉定縣 (hvd_40393, county, 1369–1911; parent chain 蘇州府 1369–1723 → 太倉州 1724–1911), 0.0 km from the Qing county Q46539546; the locality Ko-li-tsem is absent.

Queries: `嘉定` → 12 hit(s); `嘉定縣` → 3 hit(s); `Kiating` → 0 hit(s); `太倉` → 6 hit(s).

Best record: parent 苏州府 (1369–1723); 太仓州 (1724–1911), present location “今上海嘉定县治嘉定镇”, <https://chgis.hudci.org/tgaz/placename/json/hvd_40393>.

### #38 — «in Tum cheu missionis Kim tum» / T'ong-tcheou (`confirmed`)

Same place as iloc issue 03: hvd_103 通州 (州, parent 順天府, 1820) is 0.7 km from Q393836; the 1767 year filter returns only the Jiangsu homonym.

Queries: `通州` → 22 hit(s); `通州` (ft=zhou) → 5 hit(s); `通州` (parent=顺天府) → 2 hit(s); `通州` (year=1767) → 2 hit(s); `Tongzhou` (year=1767) → 0 hit(s); `通縣` → 0 hit(s); `南通` → 0 hit(s).

Best record: parent 顺天府 (Shuntian Fu), present location “北京通县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_103>.

### #42 — Lao chan oua, Hou-kouang (`not-in-tgaz`)

Same place as iloc issue 07: no candidate reading (老山洼/老山窪/老山凹/牢山) is in TGAZ; 漢陽府 and 武昌府 are present but unattachable.

Queries: `老山洼` → 0 hit(s); `老山窪` → 0 hit(s); `老山凹` → 0 hit(s); `牢山` → 0 hit(s); `Laoshanwa` → 0 hit(s); `Laoshan` → 1 hit(s); `老山` → 0 hit(s); `老山湾` → 0 hit(s); … 5 more.

### #43 — Leou-kia-tchouang do Chou-lou hien (`confirmed`)

Same place as iloc issue 08: hvd_135137 呂家莊 (村鎮, parent 束鹿縣) and hvd_44783 束鹿縣 (1622–1911) confirm the reading; 19.7 km from the county town Q1015480.

Queries: `呂家莊` → 2 hit(s); `Shulu` → 6 hit(s); `束鹿縣` → 5 hit(s); `Shulu` (year=1744) → 1 hit(s); `呂家莊` (year=1744) → 0 hit(s).

Best record: parent 束鹿县 (Shulu Xian), present location “河北辛集县吕家庄”, <https://chgis.hudci.org/tgaz/placename/json/hvd_135137>.

### #48 — «Pe-chieh» du Sinfeng (`partially-confirmed`)

Same place as iloc issue 13: 信豐縣 hvd_838 (parent 贛州府) is 10.5 km from Q1356667; the 白家/白加 village is absent.

Queries: `白家` → 50 hit(s); `白家` (parent=信丰县) → 0 hit(s); `白家村` (parent=信丰县) → 0 hit(s); `白家堡` (parent=信丰县) → 0 hit(s); `白加` → 0 hit(s); `信豐` → 4 hit(s); `信豐` (year=1696) → 1 hit(s); `贛州府` → 9 hit(s); … 1 more.

Best record: parent 赣州府 (Ganzhou Fu), present location “江西信丰县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_838>.

### #49 — Pé-pou, Linkiang fou (`partially-confirmed`)

Same place as iloc issue 14: 臨江府 hvd_32539 and 清江縣 confirmed, 14.7 km from the prefecture seat Q197394; no 白埠/北埠/百步/裴埠 candidate under 臨江府.

Queries: `臨江府` → 7 hit(s); `临江府` (year=1787) → 2 hit(s); `Linjiang` → 49 hit(s); `清江县` → 16 hit(s); `清江县` (year=1787) → 1 hit(s); `白埠` → 1 hit(s); `白埠` (parent=临江府) → 0 hit(s); `北埠` → 0 hit(s); … 3 more.

Best record: parent 江西行省, 江西布政使司, 江西省, present location “江西樟树市西南临江镇”, <https://chgis.hudci.org/tgaz/placename/hvd_32539>.

### #50 — Pé-tsiuen-chan / Pe tsien schan (`partially-confirmed`)

Same place as iloc issue 15: 漢陽縣 hvd_664 / 漢陽府 confirmed (23.8 km from the 柏泉天主堂 anchor); 柏泉/柏泉山/茅廟集 absent.

Queries: `柏泉` → 0 hit(s); `柏泉山` → 0 hit(s); `柏泉` (year=1740) → 0 hit(s); `茅廟集` → 0 hit(s); `茅庙集` → 0 hit(s); `Baiquan` → 7 hit(s); `漢陽府` → 10 hit(s); `漢陽府` (year=1740) → 2 hit(s); … 1 more.

Best record: parent 汉阳府 (Hanyang Fu), present location “湖北武汉市汉阳”, <https://chgis.hudci.org/tgaz/placename/json/hvd_664>.

### #51 — Petit Tibet «Kinchuen» (`partially-confirmed`)

Same place as iloc issue 16: TGAZ has no Qianlong '金川' unit, but 懋功廳 hvd_96613 (1783–1911) covers the region; its 綏靖屯 is 1.1 km from Q338033.

Queries: `金川` → 1 hit(s); `金川县` → 1 hit(s); `Jinchuan` → 4 hit(s); `大金川` → 0 hit(s); `小金川` → 1 hit(s); `金川` (year=1774) → 0 hit(s); `懋功` → 7 hit(s); `懋功` (year=1774) → 0 hit(s); … 4 more.

Best record: parent 四川省 (Sichuan Sheng), present location “四川省小金县县治美兴镇”, <https://chgis.hudci.org/tgaz/placename/json/hvd_96613>.

### #55 — San kiao hou kia (`partially-confirmed`)

Same place as iloc issue 20: 瑞州府 hvd_32628 and 高安縣 confirmed; no 三橋 village under them (Q14583988 has no P625).

Queries: `三橋` → 6 hit(s); `三桥` (parent=高安县) → 0 hit(s); `三桥` (parent=瑞州府) → 0 hit(s); `瑞州府` (year=1741) → 2 hit(s); `高安县` (year=1741) → 1 hit(s).

Best record: parent 江西省 (Jiangxi Sheng), 1645-1911, present location “江西高安县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32628>.

### #56 — Shaohing (`confirmed`)

Same place as iloc issue 21: hvd_32185 紹興府 (府, 1367–1911) is 0.7 km from Q42666.

Queries: `紹興` → 10 hit(s); `紹興府` (year=1706) → 2 hit(s); `Shaoxing` → 10 hit(s); `Shanyin` → 12 hit(s); `Ciquione` → 0 hit(s); `Shaoshing` → 0 hit(s); `紹興府` (year=1586) → 2 hit(s); `山陰縣` (year=1586) → 2 hit(s); … 2 more.

Best record: parent 浙江省 (Zhejiang Sheng), 1645-1911, present location “今浙江绍兴市”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32185>.

### #57 — Sian tan hien (`confirmed`)

Same place as iloc issue 22: hvd_41738 湘潭縣 (1370–1911) is 3.5 km from Q215755 and 10.6 km from the comment's candidate Q1375015 — the historic seat favours Q215755.

Queries: `湘潭` → 9 hit(s); `湘潭縣` (year=1706) → 1 hit(s); `Xiangtan` → 15 hit(s); `長沙府` → 8 hit(s).

Best record: parent 潭州府 (1370-1371) → 长沙府 (1372-1911), present location “湖南省湘潭市”, <https://chgis.hudci.org/tgaz/placename/json/hvd_41738>.

### #58 — Siao-tchai de Han-tchong (`partially-confirmed`)

Same place as iloc issue 23: 城固縣 hvd_964 / hvd_71005 is 0.4 km from Q1069968; the village 小寨子 is absent (the one TGAZ record is a Zhili homonym), and Q515573 is Hanzhong city, 29 km away.

Queries: `小寨子` → 1 hit(s); `小寨` → 11 hit(s); `小寨子` (parent=城固縣) → 0 hit(s); `小寨子` (parent=漢中府) → 0 hit(s); `城固` → 5 hit(s); `城固` (year=1657) → 0 hit(s).

Best record: parent 汉中府 (Hanzhong Fu), present location “陕西城固县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_964>.

### #61 — T'ang-kia-hiang (`partially-confirmed`)

Same place as iloc issue 26: 松江府 hvd_32439 confirmed (11.4 km from Q11104671); 唐家鄉/唐家乡/唐家巷/湯家巷 all absent.

Queries: `唐家巷` → 0 hit(s); `湯家巷` → 0 hit(s); `汤家巷` → 0 hit(s); `Tangjiaxiang` → 0 hit(s); `唐家巷` (parent=松江府) → 0 hit(s); `湯家巷` (parent=松江府) → 0 hit(s); `唐家` → 27 hit(s); `松江府` (year=1787) → 2 hit(s).

Best record: parent 江南省 (1645-1666) → 江蘇省 (1667-1911), present location “今上海市松江县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_32439>.

### #62 — Tcha-yuen-keou (`partially-confirmed`)

Same place as iloc issues 27 and comment #4: 谷城縣 confirmed, 茶園溝 absent; the 紫金鎮 township is present in the 1911 layer.

Queries: `茶园沟` → 0 hit(s); `茶園溝` → 0 hit(s); `Chayuangou` → 0 hit(s); `茶园` → 10 hit(s); `茶园` (parent=谷城县) → 0 hit(s); `谷城` → 6 hit(s); `谷城` (year=1759) → 0 hit(s); `紫金` (parent=谷城县) → 1 hit(s); … 1 more.

Best record: parent 襄阳府 (Xiangyang Fu), present location “湖北谷城县”, <https://chgis.hudci.org/tgaz/placename/json/hvd_631>.

### #63 — Tongko (near "Tsangtzo") (`partially-confirmed`)

TGAZ confirms 常熟縣 (hvd_40382, county, 1369–1911, parent 蘇州府), 0.38 km from Q1015805, supporting the comment's Changshu reading of 'Tsangtzo'; Tongko itself is absent.

Queries: `常熟` → 6 hit(s); `Changshu` → 8 hit(s); `唐市` → 3 hit(s); `東港` → 4 hit(s); `塘橋` → 2 hit(s).

Best record: parent 苏州府 (1369–1911), present location “今江苏常熟市区”, <https://chgis.hudci.org/tgaz/placename/json/hvd_40382>.

### #64 — Tonkosz (`partially-confirmed`)

Same place as iloc issue 29: HGR has Saratov city/uezd/namestnichestvo (hgr_345/hgr_70/hgr_29) but no Tonkosz/Mariental/Sovetskoye record.

Queries: `Saratov` → 3 hit(s); `Саратов` → 3 hit(s); `Саратов` (year=1795) → 3 hit(s); `Saratov` (year=1805) → 0 hit(s); `Tonkosz` → 0 hit(s); `Tonkoszorowka` → 0 hit(s); `Тонкошуровка` → 0 hit(s); `Mariental` → 0 hit(s); … 3 more.

Best record: parent Саратовский уезд (Saratovskii uezd), present location “Saratov, Saratov Oblast, Russia”, <https://chgis.hudci.org/tgaz/placename/json/hgr_345>.

### #65 — U cham fu, Hou-kouang (`confirmed`)

Same place as iloc issue 30: hvd_34300 武昌府 (府, 1364–1911) is 1.96 km from Q11124318; the comment's correction of the galaxy code Q1112431 to Q11124318 is supported.

Queries: `武昌府` → 11 hit(s); `武昌府` (ft=fu) → 11 hit(s); `Wuchang` (ft=fu) → 14 hit(s); `武昌府` (year=1767) → 3 hit(s); `湖北` → 6 hit(s).

Best record: present location “今湖北武汉市武昌”, <https://chgis.hudci.org/tgaz/placename/hvd_34300>.

### #67 — Yean-sam, Yenping (`partially-confirmed`)

Same place as iloc issue 32: 延平府 hvd_32131 is 0.39 km from Q1337959; 'Yean-sam' and 十字山 absent.

Queries: `延平府` → 8 hit(s); `延平` (year=1649) → 2 hit(s); `Yanping` → 21 hit(s); `十字山` → 0 hit(s).

Best record: parent 福建行省, 福建布政使司, 福建省, present location “福建省南平市”, <https://chgis.hudci.org/tgaz/placename/hvd_32131>.

### #68 — Yuwei do Shansi (`confirmed`)

Same place as iloc issue 33: hvd_95557 右玉縣 (1725–1911, successor of 右玉衛) is 0.63 km from Q10916242.

Queries: `右玉` → 6 hit(s); `右玉` (year=1727) → 1 hit(s); `右玉卫` → 1 hit(s); `Youyu` → 13 hit(s).

Best record: parent 朔平府, present location “今山西右玉县右卫镇”, <https://chgis.hudci.org/tgaz/placename/hvd_95557>.


## Reproducing

```bash
cd inferences/iloc-issues/tgaz
python3 build_comments.py            # re-run the checks + sections
python3 replay.py --log comments-query-log.json   # verify the queries
python3 build_comments_report.py     # rebuild this report
```

## Files

| Path | Content |
|---|---|
| `tgaz/comments-data/<GH>.json` | per-draft evidence record |
| `tgaz/comments-results.csv` | one row per draft (generated) |
| `tgaz/comments-query-log.json` | recorded queries, for replay (generated) |
| `tgaz/build_comments.py` | generator of the sections and JSON records |
| `tgaz/build_comments_report.py` | this report's generator |
| `comments/<draft>.md` | the draft with its `## TGAZ (CHGIS) check` section |

