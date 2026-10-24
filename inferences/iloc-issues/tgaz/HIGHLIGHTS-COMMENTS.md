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
