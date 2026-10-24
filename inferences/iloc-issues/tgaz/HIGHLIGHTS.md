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
