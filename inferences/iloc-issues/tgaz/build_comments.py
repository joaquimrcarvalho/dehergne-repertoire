#!/usr/bin/env python3
"""TGAZ check of the GitHub-issue comment drafts in ``inferences/iloc-issues/comments/``.

The 24 comment drafts in ``comments/`` are identification reports posted (or to
be posted) on the existing GitHub issues #2-#68.  Most of them describe places
that the main TGAZ pass already checked in the 34 issue files; five describe
places that were **not** covered there:

* #2   Lofeu (羅浮) — China-Tonkin frontier station
* #29  Chang-tsin do Yüansi — 鄖西縣, Hubei
* #30  Chang-si — Shanxi province
* #33  Ko-li-tsem do Kiating — 嘉定縣, Kiangnan
* #63  Tongko / "Tsangzo" — Changshu 常熟, Jiangsu (district level)

This script:

1. copies the verified TGAZ evidence from ``data/<NN>.json`` for the places
   already covered (cross-references), and runs fresh queries for the five new
   places (results stored in ``comments-data/<GH>.json``);
2. appends a ``## TGAZ (CHGIS) check`` section to each comment file;
3. writes ``tgaz/comments-data/*.json``.

Usage:
    python3 build_comments.py
"""

from __future__ import annotations

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ISSUES_DIR = os.path.dirname(HERE)
COMMENTS_DIR = os.path.join(ISSUES_DIR, "comments")
DATA_DIR = os.path.join(HERE, "data")
CDATA_DIR = os.path.join(HERE, "comments-data")

sys.path.insert(0, HERE)
from tgaz_tool import (  # noqa: E402
    canonical_summary,
    haversine_km,
    tgaz_get,
    tgaz_query,
    tgaz_results_to_records,
)

CHECKED = "2026-10-22"
TGW = "https://chgis.hudci.org/tgw/#usage"

# ---------------------------------------------------------------------------
# The 24 comment drafts.  ``cross`` points at the iloc issue JSON whose TGAZ
# evidence already covers the place; the five records without ``cross`` are
# new and carry their own query list.
# ---------------------------------------------------------------------------

RECORDS = [
    # ---------------------------------------------------------------- new ---
    dict(
        gh="2",
        file="issue-2.md",
        place="Lofeu (羅浮), China–Tonkin frontier",
        year="1722-12-28 / 1723-04-14",
        dehergne_year=1722,
        region="China–Tonkin frontier (Qinzhou area / Tonkin side)",
        country="China/Vietnam border",
        identified_chinese="羅浮 (probable; no characters in the sources)",
        cross=None,
        wikidata={},
        dist_km=None,
        verdict="not-in-tgaz",
        verdict_note=(
            "TGAZ has no record of the cross-border 羅浮; its only 罗浮 is a "
            "village under 嘉應州 (Guangdong, 24.52 N 115.58 E), a homonym, "
            "and 羅浮洞 returns nothing. The Qing 欽州 is present at "
            "prefecture level."
        ),
        notes=(
            "Homonyms: 罗浮 hvd_16948 (1820, 村鎮, parent 嘉應州, present "
            "'广东兴宁县北'); 罗富哨 hvd_154047 (1911, 南丹土州, Guangxi); "
            "欽州 hvd_320 (1820, 州, parent 廉州府, 今广西钦州市). "
            "防城县 only from 1887 (French frontier), hvd_42648."
        ),
        queries=[
            ("羅浮", None, None, None, None),
            ("Luofu", None, None, None, None),
            ("羅浮洞", None, None, None, None),
            ("欽州", None, None, None, None),
            ("防城", None, None, None, None),
        ],
        body=(
            "The place is absent from TGAZ, and its **homonyms are instructive**. "
            "The prefix hit `hvd_16948` 罗浮 is a village of 嘉應州 (Jiaying Zhou, "
            "Guangdong) at 24.52 N 115.58 E — some 700 km from the Tonkin border "
            "and recorded on the 1820 layer only; 罗富哨 (Luofushao, "
            "`hvd_154047`) lies in 南丹土州 (north-west Guangxi), also far from "
            "the Qinzhou frontier. `羅浮洞` returns nothing. The Chinese side of "
            "the frontier *is* covered at prefecture level — 欽州 `hvd_320` "
            "(1820, 州, parent 廉州府, `present_location` 今广西钦州市) — but "
            "防城縣 appears only from 1887 (`hvd_42648`), i.e. after the French "
            "frontier settlement. TGAZ therefore cannot place 羅浮: the "
            "comment's reading as a China–Tonkin frontier locality stands on the "
            "modern scholarship it cites, and the probable older identification "
            "of 羅浮 with a locality on the Tonkin side is consistent with TGAZ "
            "having no record of it."
        ),
    ),
    dict(
        gh="29",
        file="issue-29.md",
        place="Chang-tsin do Yüansi",
        year="1786-12-03",
        dehergne_year=1786,
        region="Hubei (Yunyang fu / Yunxi county)",
        country="China",
        identified_chinese="鄖西縣 (county; the locality Chang-tsin is unidentified)",
        cross=None,
        wikidata={"id": "Q1154509", "label": "Yunxi County / 郧西县",
                  "lat": 32.99392, "lon": 110.42153},
        dist_km=0.69,
        verdict="partially-confirmed",
        verdict_note=(
            "TGAZ confirms 鄖西縣 (hvd_45962, county, 1476–1911, parent 鄖陽府, "
            "present '今湖北省郧西县'), 0.69 km from Q1154509; the locality "
            "'Chang-tsin' is absent."
        ),
        notes="Yunxi/homonym noise: 'Yunxi' prefix also returns 云溪 villages in Zhejiang, Hunan and Fujian.",
        best={"sys_id": "hvd_45962"},
        queries=[
            ("鄖西", None, None, None, None),
            ("鄖陽府", None, None, None, None),
            ("Yunxi", None, None, None, None),
        ],
        body=(
            "TGAZ records **鄖西縣** `hvd_45962` — county (縣), **1476–1911**, "
            "parent **鄖陽府** (year-ranged canonical parent 1476–1911), "
            "`present_location` \"今湖北省郧西县\" — at 32.99561 N 110.4188 E, "
            "**0.69 km** from the modern county item Q1154509. This is exactly "
            "the Qing county the comment establishes for *Yüansi*, and the "
            "prefecture has its own record (`hvd_34319` 鄖陽府, 1476–1911). "
            "The locality `Chang-tsin` itself cannot be queried — the comment "
            "shows that no source assigns it characters — and TGAZ has no "
            "candidate under 鄖西/鄖陽; the comment's **county-level-only** "
            "conclusion is therefore the right one. (Prefix noise: `Yunxi` also "
            "returns 云溪 villages in Zhejiang, Hunan and Fujian — the Chinese-"
            "character query avoids it.)"
        ),
    ),
    dict(
        gh="30",
        file="issue-30.md",
        place="Chang-si (Chan-si)",
        year="1691 / 1696",
        dehergne_year=1696,
        region="Shanxi province",
        country="China",
        identified_chinese="山西 (province)",
        cross=None,
        wikidata={"id": "Q46913", "label": "Shanxi / 山西省",
                  "lat": 37.873333, "lon": 112.564444},
        dist_km=0.06,
        verdict="confirmed",
        verdict_note=(
            "TGAZ has 山西省 (hvd_112103, province, 1644–1911, present "
            "'山西省太原市'), 0.06 km from Q46913; the province-level anchor "
            "is exactly right."
        ),
        notes="Pinyin 'Shanxi' prefix also matches 陕西 (Shaanxi) records — the Chinese-character query is the safe one.",
        best={"sys_id": "hvd_112103"},
        queries=[
            ("山西", None, None, None, None),
            ("Shanxi", None, None, None, None),
            ("山西布政使司", None, None, None, None),
        ],
        body=(
            "TGAZ has **山西省** `hvd_112103` — province (省), **1644–1911**, "
            "parent 清, `present_location` \"山西省太原市\" — at 37.87375 N "
            "112.56483 E, **0.06 km** from Q46913, and the 1820 layer carries "
            "the same unit (`hvd_25011`); the Ming predecessor is 山西布政使司 "
            "`hvd_112059` (1376–1644). The comment's reading of `Chang-si` as "
            "the **province** (not a town) is therefore gazetteer-exact: TGAZ "
            "has no sub-provincial place behind the name, and the province "
            "record is the only thing to anchor. **Method note:** the pinyin "
            "prefix `Shanxi` also returns 陕西 (Shaanxi) records — the classic "
            "Shanxi/Shaanxi collision; the Chinese-character query is the "
            "reliable one."
        ),
    ),
    dict(
        gh="33",
        file="candidate-issue-33.md",
        place="Ko-li-tsem do Kiating",
        year="1745 / 1753",
        dehergne_year=1745,
        region="Kiangnan (Jiading county, 太倉州 from 1724)",
        country="China",
        identified_chinese="嘉定縣 (county; the locality Ko-li-tsem is unidentified)",
        cross=None,
        wikidata={"id": "Q46539546", "label": "嘉定縣 (Qing county)",
                  "lat": 31.385845, "lon": 121.249023},
        dist_km=0.0,
        verdict="partially-confirmed",
        verdict_note=(
            "TGAZ confirms 嘉定縣 (hvd_40393, county, 1369–1911; parent chain "
            "蘇州府 1369–1723 → 太倉州 1724–1911), 0.0 km from the Qing county "
            "Q46539546; the locality Ko-li-tsem is absent."
        ),
        notes="Homonym trap: the 嘉定 prefix is dominated by 嘉定府 in Sichuan (29.57 N 103.75 E).",
        best={"sys_id": "hvd_40393"},
        queries=[
            ("嘉定", None, None, None, None),
            ("嘉定縣", None, None, None, None),
            ("Kiating", None, None, None, None),
            ("太倉", None, None, None, None),
        ],
        body=(
            "TGAZ records **嘉定縣** `hvd_40393` — county (縣), **1369–1911**, "
            "with the **year-ranged parent chain 蘇州府 1369–1723 → 太倉州 "
            "1724–1911** — at 31.38585 N 121.24902 E, `present_location` \"今上"
            "海嘉定县治嘉定镇\". That is **0.0 km** from the Qing county item "
            "Q46539546 and **5.6 km** from the modern district Q662101 — and it "
            "is precisely the administrative frame the comment establishes "
            "(Kiating = 嘉定, in 江蘇省太倉直隸州 from 1724; 太倉州 itself is "
            "`hvd_32082`, 1724–1911). The locality *Ko-li-tsem* is absent from "
            "TGAZ, as it is from the sources; the comment's decision to leave "
            "the station unlinked and anchor at the district is right. "
            "**Homonym trap:** the prefix 嘉定 returns twelve records, most of "
            "them **嘉定府 in Sichuan** (29.57 N 103.75 E) — a different "
            "province; only the Chinese full form or the parent chain separates "
            "them."
        ),
    ),
    dict(
        gh="63",
        file="candidate-issue-63.md",
        place='Tongko (near "Tsangtzo")',
        year="1747-12-21",
        dehergne_year=1747,
        region="Jiangsu (Changshu, Suzhou fu)",
        country="China",
        identified_chinese="常熟縣 (district anchor; the village Tongko is unidentified)",
        cross=None,
        wikidata={"id": "Q1015805", "label": "Changshu / 常熟市",
                  "lat": 31.65, "lon": 120.733333},
        dist_km=0.38,
        verdict="partially-confirmed",
        verdict_note=(
            "TGAZ confirms 常熟縣 (hvd_40382, county, 1369–1911, parent 蘇州府), "
            "0.38 km from Q1015805, supporting the comment's Changshu reading of "
            "'Tsangtzo'; Tongko itself is absent."
        ),
        notes=(
            "唐市鎮 hvd_23781 (1820, 村鎮, parent 常熟縣, 31.54781 N "
            "120.84787 E) is the only Tong-/Tang-named market town of the "
            "county in TGAZ; phonetically 'Tongko' ≠ 唐市 (Tangshi) and it is "
            "not adopted. 東港/塘橋/塘角: no record under 常熟."
        ),
        best={"sys_id": "hvd_40382"},
        queries=[
            ("常熟", None, None, None, None),
            ("Changshu", None, None, None, None),
            ("唐市", None, None, None, None),
            ("東港", None, None, None, None),
            ("塘橋", None, None, None, None),
        ],
        body=(
            "The comment's **district-level reading is gazetteer-confirmed**: "
            "TGAZ has **常熟縣** `hvd_40382` — county (縣), **1369–1911**, "
            "parent **蘇州府** — at 31.64658 N 120.73379 E, `present_location` "
            "\"今江苏常熟市区\", **0.38 km** from Q1015805 (Changshu). So "
            "Dehergne's own gloss *Tzang zo = Tch'ang-chou = Changshu*, on which "
            "the comment rests, is consistent with an independent gazetteer; and "
            "the \"entre Soochow et Kashing\" parenthesis in notice 401 remains "
            "the problem it is described as, not a pointer to 嘉興. The village "
            "**Tongko itself is still absent**: TGAZ's 1820/1911 village layer "
            "records one Tong-/Tang-named market town in the county — 唐市鎮 "
            "`hvd_23781` (1820, 村鎮, parent 常熟縣, 31.54781 N 120.84787 E) — "
            "but `Tongko` is not phonetically 唐市 (Tangshi), and no 東港/塘橋/"
            "塘角 village under 常熟 was found. The candidate is therefore "
            "recorded, **not adopted**, exactly as the comment leaves it. This "
            "also supersedes the earlier \"between Soochow and Kashing\" test in "
            "iloc issue 28, which checked 張澤/張渚/張涇 in that corridor and "
            "did not have the entry-51 gloss."
        ),
    ),

    # ------------------------------------------------- cross-referenced ----
    dict(
        gh="4",
        file="candidate-issue-4-check.md",
        place="Chayüankow / Tcha-yuen-keou",
        year="1759-04-01",
        dehergne_year=1759,
        region="Hubei (Gucheng county)",
        country="China",
        identified_chinese="茶園溝 (valley); 沈垭村 (modern village)",
        cross="27",
        wikidata={"id": "Q14091289", "label": "沈垭村", "lat": None, "lon": None},
        dist_km=None,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 27: 谷城縣 confirmed (hvd_631), 茶園溝 "
            "absent; the 1911 village 紫金洞塘 lies in the same 紫金鎮."
        ),
        notes="Anchor Q14091289 has no P625 coordinate; the county seat is 1.2 km from Q1199165.",
        body=(
            "TGAZ confirms the administrative frame — **谷城縣** `hvd_631` "
            "(1820 layer; county, parent 襄陽府) 1.2 km from Q1199165 — and the "
            "1911 village `hvd_128134` 紫金洞塘 whose `present_location` is "
            "\"湖北谷城县紫金镇\", i.e. the township that contains the comment's "
            "沈垭村 anchor (0.5 km from 紫金鎮 Q14083121). The valley **茶園溝 "
            "itself is absent** (茶園溝/茶园沟 = 0 hits), so TGAZ cannot confirm "
            "the 沟 reading — but it is consistent with it, and it gives no "
            "support to the contributed 衡山/Q1337942 reading, which is in "
            "another province."
        ),
    ),
    dict(
        gh="27",
        file="candidate-issue-27.md",
        place="Choui tcheou San Kia / San-kiao",
        year="1745-09-08",
        dehergne_year=1745,
        region="Jiangxi (Ruizhou fu / Gao'an)",
        country="China",
        identified_chinese="三橋 (village); 瑞州府 / 高安縣 (parents)",
        cross="20",
        wikidata={"id": "Q14583988", "label": "三桥村", "lat": None, "lon": None},
        dist_km=None,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 20: 瑞州府 hvd_32628 and 高安縣 confirmed, "
            "but no 三橋 village under them; Q14583988 has no P625."
        ),
        notes="The comment's spelling note (San-kiao 三橋, not san-kiao 三教) is not a gazetteer question.",
        body=(
            "TGAZ has the parents — **瑞州府** `hvd_32628` (府, 1369–1911; "
            "28.4256 N 115.37228 E) and **高安縣** (`hvd_41219`, county, "
            "622–1911; 0.4 km from the modern county seat Q1229428) — but "
            "**no 三橋 village under either of them**: the six 三桥 records are "
            "1820/1911 villages in Anhui, Jiangxi (Linchuan), Guizhou and "
            "elsewhere, and the parent-filtered queries return 0. The comment's "
            "village-level anchor Q14583988 therefore stands on the archive "
            "evidence and modern toponymy alone, not on TGAZ."
        ),
    ),
    dict(
        gh="38",
        file="candidate-issue-38.md",
        place="«in Tum cheu missionis Kim tum» / T'ong-tcheou",
        year="1767-11-04",
        dehergne_year=1767,
        region="Zhili / Hopei",
        country="China",
        identified_chinese="通州 (Zhili)",
        cross="03",
        wikidata={"id": "Q393836", "label": "Tongzhou District / 通州區",
                  "lat": 39.90858, "lon": 116.65133},
        dist_km=0.7,
        verdict="confirmed",
        verdict_note=(
            "Same place as iloc issue 03: hvd_103 通州 (州, parent 順天府, 1820) "
            "is 0.7 km from Q393836; the 1767 year filter returns only the "
            "Jiangsu homonym."
        ),
        notes="The historical counterpart Q15916190 (通州 of 順天府) corresponds to TGAZ hvd_103.",
        body=(
            "TGAZ records the Zhili **通州** `hvd_103` — department (州), CHGIS "
            "**1820** layer, parent **順天府** — at 39.90592 N 116.65881 E, "
            "`present_location` \"北京通县\", **0.7 km** from Q393836. This is "
            "the place behind the comment's identification, and corresponds to "
            "the historical item Q15916190 rather than to the modern district "
            "only. **The year filter would have produced the opposite**: at "
            "`year=1767` TGAZ returns only the **Jiangsu** 通州 (Nantong, "
            "`hvd_33310`, 955 km away), because the Zhili unit is preserved only "
            "in the 1820 layer — exactly the homonym the issue's parentheses "
            "reject."
        ),
    ),
    dict(
        gh="42",
        file="candidate-issue-42-check.md",
        place="Lao chan oua, Hou-kouang",
        year="1759-08-15",
        dehergne_year=1759,
        region="Huguang / Hubei",
        country="China",
        identified_chinese="老山洼 (inference only)",
        cross="07",
        wikidata={},
        dist_km=None,
        verdict="not-in-tgaz",
        verdict_note=(
            "Same place as iloc issue 07: no candidate reading (老山洼/老山窪/"
            "老山凹/牢山) is in TGAZ; 漢陽府 and 武昌府 are present but "
            "unattachable."
        ),
        notes="",
        body=(
            "TGAZ has **no record** of any candidate reading of *Lao chan oua* "
            "(老山洼, 老山窪, 老山凹, 牢山, Laoshanwa — 0 hits each; the only "
            "`Laoshan` hit is 劳山鎮 in Shaanxi, irrelevant). The mission "
            "province's prefectures 漢陽府 (`hvd_34302`, 1380–1911) and 武昌府 "
            "(`hvd_34300`, 1364–1911) are present, but Dehergne gives no "
            "prefecture or county to attach the name to. The comment's decision "
            "to leave the place unlinked, with 老山洼 labelled an inference, "
            "stands: TGAZ neither confirms nor rejects it."
        ),
    ),
    dict(
        gh="43",
        file="candidate-issue-43-check.md",
        place="Leou-kia-tchouang do Chou-lou hien",
        year="1744-06-07",
        dehergne_year=1744,
        region="Zhili / Hopei (Shulu county)",
        country="China",
        identified_chinese="呂家莊 / 束鹿縣",
        cross="08",
        wikidata={"id": "Q1015480", "label": "Xinji / 辛集市",
                  "lat": 37.94231, "lon": 115.21181},
        dist_km=19.74,
        verdict="confirmed",
        verdict_note=(
            "Same place as iloc issue 08: hvd_135137 呂家莊 (村鎮, parent 束鹿縣) "
            "and hvd_44783 束鹿縣 (1622–1911) confirm the reading; 19.7 km from "
            "the county town Q1015480."
        ),
        notes="",
        body=(
            "TGAZ independently records **呂家莊** `hvd_135137` — village/town "
            "(村鎮), **1911** layer, parent **束鹿縣** — at 37.94665 N "
            "115.43684 E, `present_location` \"河北辛集县吕家庄\"; and **束鹿縣** "
            "itself `hvd_44783` (county, **1622–1911**, parent 保定府), i.e. "
            "valid in 1744. The village is 19.7 km from the county town "
            "(Q1015480) — a normal village–county-seat distance. This is exactly "
            "the *Shulu + Lüjiazhuang* reading of the vow formula, and it "
            "contradicts the contributed 刘家庄 reading."
        ),
    ),
    dict(
        gh="48",
        file="candidate-issue-48.md",
        place="«Pe-chieh» du Sinfeng",
        year="1696-03-03",
        dehergne_year=1696,
        region="Jiangxi (Xinfeng county, Ganzhou fu)",
        country="China",
        identified_chinese="信豐縣 / 白家 (village)",
        cross="13",
        wikidata={"id": "Q1356667", "label": "Xinfeng County / 信丰县",
                  "lat": 25.288056, "lon": 114.901667},
        dist_km=10.47,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 13: 信豐縣 hvd_838 (parent 贛州府) is "
            "10.5 km from Q1356667; the 白家/白加 village is absent."
        ),
        notes="",
        body=(
            "TGAZ confirms the county and its prefecture — **信豐縣** "
            "(`hvd_838`, 1820 layer, parent **贛州府**; also `hvd_40841`, "
            "742–1911) at 25.3784 N 114.93108 E, **10.5 km** from Q1356667 — "
            "which is the administrative frame of the comment's reading. It has "
            "**no record of the 白家/白加 bourg** in its 1820/1911 village "
            "layers (the parent-filtered 白家/白家村/白家堡 queries return 0), so "
            "the village reading stands on Dehergne 1967 and Pfister, as the "
            "comment says. The rejected 新淦/新干 reading gets no support."
        ),
    ),
    dict(
        gh="49",
        file="candidate-issue-49-check.md",
        place="Pé-pou, Linkiang fou",
        year="1787-05",
        dehergne_year=1787,
        region="Jiangxi (Linjiang fu / Qingjiang)",
        country="China",
        identified_chinese="臨江府 / 清江縣 (prefecture only)",
        cross="14",
        wikidata={"id": "Q197394", "label": "Zhangshu / 樟树市",
                  "lat": 28.066667, "lon": 115.5375},
        dist_km=14.73,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 14: 臨江府 hvd_32539 and 清江縣 confirmed, "
            "14.7 km from the prefecture seat Q197394; no 白埠/北埠/百步/裴埠 "
            "candidate under 臨江府."
        ),
        notes="The comment's rejection of Q13802007 (白埠村 in Pizhou, Jiangsu, 756 km away) is consistent with the gazetteer.",
        body=(
            "TGAZ confirms **臨江府** `hvd_32539` (府, **1363–1911**, "
            "`present_location` \"江西樟树市西南临江镇\") and its seat county "
            "**清江縣** (`hvd_40941`), 14.7 km from the modern 樟樹 city centre "
            "(Q197394) — the prefecture-level anchor the comment recommends. "
            "None of the candidate village readings (**白埠, 北埠, 百步, 裴埠**) "
            "falls under 臨江府: 白埠 returns a village in 會昌縣 (far south, "
            "different prefecture), 百步 only 百步梯 in Guangdong, 北埠/裴埠 "
            "nothing. The comment's rejection of Q13802007 (白埠村 in Pizhou, "
            "Jiangsu — 756 km away) is therefore consistent with the gazetteer."
        ),
    ),
    dict(
        gh="50",
        file="candidate-issue-50.md",
        place="Pé-tsiuen-chan / Pe tsien schan",
        year="1740-08-15 etc.",
        dehergne_year=1740,
        region="Huguang / Hubei (Hanyang)",
        country="China",
        identified_chinese="柏泉山 / 柏泉",
        cross="15",
        wikidata={"id": "Q130298171", "label": "柏泉天主堂",
                  "lat": 30.72938, "lon": 114.13648},
        dist_km=23.8,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 15: 漢陽縣 hvd_664 / 漢陽府 confirmed "
            "(23.8 km from the 柏泉天主堂 anchor); 柏泉/柏泉山/茅廟集 absent."
        ),
        notes="",
        body=(
            "TGAZ confirms the county in which 柏泉 lies — **漢陽縣** "
            "(`hvd_664`, county; county and prefecture records span the "
            "Dehergne period) 24.4 km from 柏泉街道 Q11108336 and 23.8 km from "
            "the 柏泉天主堂 item Q130298171, all consistent with Dehergne's "
            "\"à 30 Kms de Hankow\" — but it has **no record of 柏泉/柏泉山/"
            "茅廟集 itself** in its 1820/1911 layers. The comment's reading, "
            "resting on Pfister p. 745 and the KU Leuven CCT rendering "
            "\"Boquanshan\", is neither confirmed nor rejected at locality level."
        ),
    ),
    dict(
        gh="51",
        file="candidate-issue-51.md",
        place="Petit Tibet «Kinchuen»",
        year="1774 / 1777",
        dehergne_year=1774,
        region="Sichuan (Jinchuan region)",
        country="China",
        identified_chinese="金川 (region); 懋功廳 (post-1783 unit)",
        cross="16",
        wikidata={"id": "Q338033", "label": "Jinchuan County / 金川县",
                  "lat": 31.47803, "lon": 102.06208},
        dist_km=60.72,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 16: TGAZ has no Qianlong '金川' unit, but "
            "懋功廳 hvd_96613 (1783–1911) covers the region; its 綏靖屯 is "
            "1.1 km from Q338033."
        ),
        notes="",
        body=(
            "TGAZ has **no Qianlong-era 金川 unit** — the plain 金川/金川县 "
            "query returns only a Sui-era 金川县 in Shaanxi (`hvd_71150`), a "
            "homonym — but it confirms the **region** the comment identifies: "
            "**懋功廳** `hvd_96613` (直隸廳, **1783–1911**, parent 四川省), with "
            "its sub-units 綏靖屯 (`hvd_21281`, 1820, parent 懋功廳, **1.1 km** "
            "from 金川县 Q338033), 崇化屯, 撫邊屯 and 章谷屯. The comment's "
            "金川 reading is thus supported at the level of the post-war "
            "reorganisation, not by a contemporaneous 1774 unit; the chronological "
            "caveat stands."
        ),
    ),
    dict(
        gh="55",
        file="candidate-issue-55-check.md",
        place="San kiao hou kia",
        year="1741-03-19",
        dehergne_year=1741,
        region="Jiangxi (Ruizhou fu / Gao'an)",
        country="China",
        identified_chinese="三橋 / 胡家",
        cross="20",
        wikidata={"id": "Q14583988", "label": "三桥村", "lat": None, "lon": None},
        dist_km=None,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 20: 瑞州府 hvd_32628 and 高安縣 confirmed; "
            "no 三橋 village under them (Q14583988 has no P625)."
        ),
        notes="The correction Q14583746 → Q14583988 is a Wikidata-item matter (Ruizhou subdistrict vs Sanqiao village), not a gazetteer one.",
        body=(
            "TGAZ has **瑞州府** `hvd_32628` (府, 1369–1911) and **高安縣** "
            "(`hvd_41219` / `hvd_793`, 0.4 km from the modern 高安市 seat), but "
            "**no 三橋 village under either parent** — the six 三桥 records are "
            "villages in other provinces, and the parent-filtered queries return "
            "0. TGAZ can confirm the prefecture/county frame of the comment but "
            "cannot adjudicate between the two Wikidata village-level items: "
            "Q14583746 (瑞州街道 Ruizhou Subdistrict) and Q14583988 (三桥村) are "
            "both modern items with no gazetteer record behind them. The "
            "comment's correction to Q14583988 is a Wikidata-structure argument, "
            "not a gazetteer one."
        ),
    ),
    dict(
        gh="56",
        file="candidate-issue-56.md",
        place="Shaohing",
        year="1706-01-14",
        dehergne_year=1706,
        region="Zhejiang (Shaoxing fu)",
        country="China",
        identified_chinese="紹興",
        cross="21",
        wikidata={"id": "Q42666", "label": "Shaoxing / 绍兴市",
                  "lat": 30.0, "lon": 120.583333},
        dist_km=0.7,
        verdict="confirmed",
        verdict_note=(
            "Same place as iloc issue 21: hvd_32185 紹興府 (府, 1367–1911) is "
            "0.7 km from Q42666."
        ),
        notes="",
        body=(
            "TGAZ records **紹興府** `hvd_32185` — superior prefecture (府), "
            "**1367–1911**, parent chain to 浙江省 — at 30.00451 N 120.57826 E, "
            "`present_location` \"今浙江绍兴市\", **0.7 km** from Q42666; the "
            "附郭 county 山陰縣 (`hvd_40762`, 815–1911) sits at the same point. "
            "This confirms the comment's 紹興 identification and its "
            "provincial context."
        ),
    ),
    dict(
        gh="57",
        file="candidate-issue-57.md",
        place="Sian tan hien",
        year="1706-08-15",
        dehergne_year=1706,
        region="Hunan (Xiangtan county)",
        country="China",
        identified_chinese="湘潭縣",
        cross="22",
        wikidata={"id": "Q215755", "label": "Xiangtan / 湘潭市",
                  "lat": 27.84306, "lon": 112.92283},
        dist_km=3.49,
        verdict="confirmed",
        verdict_note=(
            "Same place as iloc issue 22: hvd_41738 湘潭縣 (1370–1911) is 3.5 km "
            "from Q215755 and 10.6 km from the comment's candidate Q1375015 — "
            "the historic seat favours Q215755."
        ),
        notes="",
        body=(
            "TGAZ records **湘潭縣** `hvd_41738` — county (縣), **1370–1911** "
            "(parent chain 潭州府 then 長沙府), `present_location` "
            "\"今湖南省湘潭市\" — at 27.8727 N 112.91126 E. That is **3.5 km** "
            "from Q215755 (湘潭市) and **10.6 km** from the candidate "
            "Q1375015 (the residual modern Xiangtan **county**, whose seat moved "
            "in the 1950s — the comment itself advises against it): the "
            "gazetteer point is the historic county seat, "
            "so Q215755 is the closer and better anchor, in agreement with the "
            "comment's recommendation. The rejected Q703818 (永嘉/Yongjia, "
            "Zhejiang) has no TGAZ connection here."
        ),
    ),
    dict(
        gh="58",
        file="candidate-issue-58.md",
        place="Siao-tchai de Han-tchong",
        year="1657-05-10",
        dehergne_year=1657,
        region="Shaanxi (Chenggu county, Hanzhong fu)",
        country="China",
        identified_chinese="小寨子 / 城固縣",
        cross="23",
        wikidata={"id": "Q1069968", "label": "Chenggu County / 城固县",
                  "lat": 33.15405, "lon": 107.32536},
        dist_km=0.42,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 23: 城固縣 hvd_964 / hvd_71005 is 0.4 km "
            "from Q1069968; the village 小寨子 is absent (the one TGAZ record is "
            "a Zhili homonym), and Q515573 is Hanzhong city, 29 km away."
        ),
        notes="",
        body=(
            "TGAZ confirms **城固縣** (`hvd_964`, 1820 layer, parent **漢中府**; "
            "and the open-ended `hvd_71005`, 629–0, parent 漢中郡) at 33.15713 N "
            "107.32794 E, **0.42 km** from Q1069968 — the county anchor the "
            "comment recommends. The **village 小寨子 itself is absent**: the "
            "only 小寨子 in TGAZ is a Zhili homonym under 望都縣, and the "
            "parent-filtered queries under 城固/漢中 return 0. The comment's "
            "rejection of **Q515573** is consistent — TGAZ's county seat is "
            "**29 km** from Hanzhong city (Q515573's point), so linking the death "
            "there would assert only \"died in Hanzhong\", as the comment says. "
            "The year-filtered `1657` query returns 0 only because `hvd_71005` "
            "has an open end date."
        ),
    ),
    dict(
        gh="61",
        file="candidate-issue-61.md",
        place="T'ang-kia-hiang",
        year="1787-05-22",
        dehergne_year=1787,
        region="Kiangnan (Songjiang fu)",
        country="China",
        identified_chinese="唐家鄉 / 湯家巷 / 唐家巷 (candidate readings)",
        cross="26",
        wikidata={"id": "Q11104671", "label": "Songjiang Fu / 松江府",
                  "lat": 31.009476, "lon": 121.107758},
        dist_km=11.43,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 26: 松江府 hvd_32439 confirmed (11.4 km "
            "from Q11104671); 唐家鄉/唐家乡/唐家巷/湯家巷 all absent."
        ),
        notes="",
        body=(
            "TGAZ has **松江府** `hvd_32439` (府, 1328–1911) but **no record** "
            "of the comment's candidate readings 唐家鄉/唐家乡 (0 hits), nor of "
            "唐家巷 or 湯家巷 (0 each), so the village/chapel name remains open — "
            "including the 湯/唐 first-character question raised in iloc issue "
            "26. The coarse Songjiang anchor Q11104671 that the record already "
            "carries is the right one for TGAZ purposes."
        ),
    ),
    dict(
        gh="62",
        file="candidate-issue-62.md",
        place="Tcha-yuen-keou",
        year="1759-03-26",
        dehergne_year=1759,
        region="Hubei (Gucheng county)",
        country="China",
        identified_chinese="茶園溝 (valley); 沈垭村 (modern village)",
        cross="27",
        wikidata={"id": "Q14091289", "label": "沈垭村", "lat": None, "lon": None},
        dist_km=None,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issues 27 and comment #4: 谷城縣 confirmed, "
            "茶園溝 absent; the 紫金鎮 township is present in the 1911 layer."
        ),
        notes="",
        body=(
            "Same gazetteer evidence as comment #4 and iloc issue 27: **谷城縣** "
            "`hvd_631` (parent 襄陽府) is confirmed (1.2 km from Q1199165), the "
            "1911 village `hvd_128134` 紫金洞塘 lies in the **紫金鎮** township "
            "that contains 沈垭村, but the valley **茶園溝 is absent**. The "
            "comment's rejection of Q1337942 (衡山縣, Hunan) is consistent: no "
            "TGAZ record connects 谷城 with Hengshan."
        ),
    ),
    dict(
        gh="64",
        file="candidate-issue-64.md",
        place="Tonkosz",
        year="1805-01-24",
        dehergne_year=1805,
        region="Saratov, Russia (Volga-German colony)",
        country="Russia",
        identified_chinese="— (Tonkoszorówka / Mariental)",
        cross="29",
        wikidata={"id": "Q958741", "label": "Sovetskoye / Mariental",
                  "lat": 51.45, "lon": 46.733333},
        dist_km=51.61,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 29: HGR has Saratov city/uezd/namestnichestvo "
            "(hgr_345/hgr_70/hgr_29) but no Tonkosz/Mariental/Sovetskoye record."
        ),
        notes="",
        body=(
            "The HGR (Historical Gazetteer of the Russian Empire, 1785–1796) "
            "layer of TGAZ confirms the **named parent** — Саратов `hgr_345` "
            "(главный город), its уезд `hgr_70` and наместничество `hgr_29` — "
            "but has **no record of the colony** under any of the forms tried "
            "(Tonkosz, Tonkoszorowka, Тонкошуровка, Mariental, Мариенталь, "
            "Sovetskoye, Советское). The modern colony point Q958741 lies 51.6 km "
            "north-east of Saratov, a normal distance for a Volga-German colony "
            "in Saratov district. The comment's reading is supported at "
            "district/mission level only; the HGR layer ends in 1796, nine years "
            "before the death."
        ),
    ),
    dict(
        gh="65",
        file="candidate-issue-65.md",
        place="U cham fu, Hou-kouang",
        year="1767-12-13",
        dehergne_year=1767,
        region="Huguang / Hubei (Wuchang)",
        country="China",
        identified_chinese="武昌府",
        cross="30",
        wikidata={"id": "Q11124318", "label": "Wuchang Fu / 武昌府",
                  "lat": 30.57367, "lon": 114.30666},
        dist_km=1.96,
        verdict="confirmed",
        verdict_note=(
            "Same place as iloc issue 30: hvd_34300 武昌府 (府, 1364–1911) is "
            "1.96 km from Q11124318; the comment's correction of the galaxy code "
            "Q1112431 to Q11124318 is supported."
        ),
        notes="",
        body=(
            "TGAZ records **武昌府** `hvd_34300` — superior prefecture (府), "
            "**1364–1911**, `present_location` \"今湖北武汉市武昌\" — at "
            "30.57367 N 114.30666 E, **1.96 km** from Q11124318, and the "
            "year-1767 query returns the same record. The comment's correction "
            "of the contributed **Q1112431** (which is NGC 4546, a galaxy) to "
            "**Q11124318** is therefore supported by the gazetteer: the place the "
            "vow register names is the fu at the Wuchang seat, which is what "
            "Q11124318 describes. The second Manchurian \"Wuchang Fu\" item "
            "Q28414894 (五常府) has no counterpart in TGAZ."
        ),
    ),
    dict(
        gh="67",
        file="candidate-issue-67.md",
        place="Yean-sam, Yenping",
        year="1649-06-10",
        dehergne_year=1649,
        region="Fujian (Yanping fu)",
        country="China",
        identified_chinese="延平府 (district anchor; the locality is unidentified)",
        cross="32",
        wikidata={"id": "Q1337959", "label": "Yanping District / 延平区",
                  "lat": 26.63958, "lon": 118.1718},
        dist_km=0.39,
        verdict="partially-confirmed",
        verdict_note=(
            "Same place as iloc issue 32: 延平府 hvd_32131 is 0.39 km from "
            "Q1337959; 'Yean-sam' and 十字山 absent."
        ),
        notes="",
        body=(
            "TGAZ confirms **延平府** `hvd_32131` (府, **1368–1911**, "
            "`present_location` \"福建省南平市\") at 26.64217 N 118.16918 E, "
            "**0.39 km** from Q1337959 — the district-level anchor the comment "
            "retains. It has **no record** of the village *Yean-sam* nor of the "
            "十字山 (0 hits), so the comment's decision to keep the anchor at "
            "district level and drop the 盐山 reading is consistent with the "
            "gazetteer."
        ),
    ),
    dict(
        gh="68",
        file="candidate-issue-68.md",
        place="Yuwei do Shansi",
        year="1727",
        dehergne_year=1727,
        region="Shanxi (Youyu county)",
        country="China",
        identified_chinese="右衛 / 右玉縣",
        cross="33",
        wikidata={"id": "Q10916242", "label": "右卫镇 Youwei Town",
                  "lat": 40.16279, "lon": 112.35023},
        dist_km=0.63,
        verdict="confirmed",
        verdict_note=(
            "Same place as iloc issue 33: hvd_95557 右玉縣 (1725–1911, successor "
            "of 右玉衛) is 0.63 km from Q10916242."
        ),
        notes="",
        body=(
            "TGAZ records **右玉縣** `hvd_95557` — county, **1725–1911**, the "
            "direct successor of **右玉衛** (`hvd_95556`, 1644–1724) — at "
            "40.16037 N 112.34358 E, `present_location` \"今山西右玉县右卫镇\", "
            "**0.63 km** from Q10916242 (右卫镇) and 21.68 km from Q1196894 "
            "(the modern county seat, which moved). The **year-1727 query "
            "returns the county record itself**, so this is a contemporaneous "
            "confirmation of the comment's 右衛 = 右玉 reading."
        ),
    ),
]

# Add the remaining cross-referenced records with shared fields in a compact
# form (they reuse the iloc evidence unchanged).
COMPACT = {
    "3": None,  # placeholder, not used
}


def load_cross(cross_id):
    path = os.path.join(DATA_DIR, f"{cross_id}.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def run_queries(specs, max_hits=8):
    queries = []
    for name, year, ft, src, parent in specs:
        try:
            response = tgaz_query(name=name, year=year, feature_type=ft,
                                  source=src, parent=parent)
            records = tgaz_results_to_records(response)
            total = response.get("count of total results")
        except Exception as exc:  # noqa: BLE001
            records, total = [], None
            print(f"  query {name!r} failed: {exc}")
        queries.append({
            "name": name,
            "year": year,
            "feature_type": ft,
            "source": src,
            "parent": parent,
            "total": total,
            "hits": records[:max_hits],
        })
        time.sleep(0.5)
    return queries


def canonical_best(sys_id):
    record = tgaz_get(sys_id)
    summary = canonical_summary(record)
    parents = "; ".join(
        f"{p['name']} ({p['begin']}–{p['end']})" for p in summary["parents"]
    )
    present = "; ".join(p["text"] for p in summary["present_location"] if p["text"])
    return {
        "sys_id": summary["sys_id"],
        "name": summary["spellings"][1] if len(summary["spellings"]) > 1 else summary["spellings"][0],
        "transcription": summary["spellings"][-1],
        "feature_type": summary["feature_type"]["transcription"],
        "english": summary["feature_type"]["english"],
        "years": f"{summary['temporal']['begin']} ~ {summary['temporal']['end']}",
        "parent": parents,
        "lat": summary["lat"],
        "lon": summary["lon"],
        "data_source": summary["data_source"],
        "uri": summary["uri"].replace("/placename/", "/placename/json/"),
        "present_location": present,
    }


def query_table(queries, limit=6):
    lines = ["| Query | Filters | Hits | Best hit |", "|---|---|---|---|"]
    for q in queries[:limit]:
        filters = []
        if q.get("year"):
            filters.append(f"year={q['year']}")
        if q.get("feature_type"):
            filters.append(f"ft={q['feature_type']}")
        if q.get("source"):
            filters.append(f"src={q['source']}")
        if q.get("parent"):
            filters.append(f"parent={q['parent']}")
        hits = q.get("hits") or []
        best = "—"
        if hits:
            h = hits[0]
            best = f"`{h['sys_id']}` {h['name']}"
            if h.get("parent_name"):
                best += f" (parent {h['parent_name']})"
        lines.append(
            f"| `{q['name']}` | {', '.join(filters) if filters else '—'} | "
            f"{q.get('total', 0)} | {best} |"
        )
    if len(queries) > limit:
        lines.append("")
        extra = len(queries) - limit
        lines.append(
            f"*({extra} further quer{'y' if extra == 1 else 'ies'} recorded in "
            f"`tgaz/comments-data/{RECORDS_INDEX['current']}.json`.)*"
        )
    return "\n".join(lines)


RECORDS_INDEX = {"current": ""}


def make_section(rec, queries, best):
    lines = ["## TGAZ (CHGIS) check", ""]
    lines.append(
        f"Checked {CHECKED} with `tgaz/tgaz_tool.py` against the "
        f"[CHGIS Temporal Gazetteer]({TGW})."
    )
    if rec.get("cross"):
        cross = rec["cross"]
        lines.append(
            f"Same place as iloc issue {cross} — full evidence in "
            f"[{cross}-…](../{cross_file(cross)}#tgaz-chgis-check); the same "
            f"queries are reproduced here."
        )
    lines.append("")
    lines.append(query_table(queries))
    lines.append("")
    if best:
        extras = []
        if best.get("feature_type"):
            extras.append(best["feature_type"])
        if best.get("years"):
            extras.append(best["years"])
        label = (
            f"**Best match.** `{best['sys_id']}` — {best.get('name', '')}"
            f" ({', '.join(extras)})"
        )
        if best.get("parent"):
            label += f", parent {best['parent']}"
        if best.get("lat") is not None:
            label += f"; {best['lat']} N, {best['lon']} E"
        if best.get("present_location"):
            label += f"; `present_location` \"{best['present_location']}\""
        if best.get("uri"):
            label += f". Canonical record: <{best['uri']}>."
        else:
            label += "."
        lines.append(label)
        lines.append("")
    wd = rec.get("wikidata") or {}
    dist = rec.get("dist_km")
    if wd.get("id") and wd.get("lat") is not None:
        dist_txt = f"**{dist:.1f} km**" if isinstance(dist, (int, float)) else "—"
        lines.append(
            f"**Coordinates.** TGAZ vs Wikidata `{wd['id']}` "
            f"({wd.get('label', '')}) {wd['lat']}, {wd['lon']} → {dist_txt}."
        )
        lines.append("")
    elif wd.get("id"):
        lines.append(
            f"**Coordinates.** The comment's anchor `{wd['id']}` "
            f"({wd.get('label', '')}) carries no P625 coordinate, so no "
            f"point comparison is possible."
        )
        lines.append("")
    lines.append(f"**Verdict: `{rec['verdict']}`.** {rec['body']}")
    lines.append("")
    return "\n".join(lines)


def cross_file(cross):
    # resolve the iloc issue file name for the cross-reference link
    import glob
    matches = glob.glob(os.path.join(ISSUES_DIR, f"{cross}-*.md"))
    return os.path.basename(matches[0])


def main():
    if not os.path.isdir(CDATA_DIR):
        os.makedirs(CDATA_DIR)
    count = 0
    for rec in RECORDS:
        gh = rec["gh"]
        RECORDS_INDEX["current"] = gh
        if rec.get("cross"):
            cross_json = load_cross(rec["cross"])
            queries = cross_json.get("queries", [])
            best = cross_json.get("best_match", {})
            if not best and rec.get("best"):
                best = canonical_best(rec["best"]["sys_id"])
        else:
            queries = run_queries(rec["queries"])
            best = canonical_best(rec["best"]["sys_id"]) if rec.get("best") else {}
        out = {
            "github_issue": gh,
            "comment_file": rec["file"],
            "issue": gh,
            "cross_ref": rec.get("cross"),
            "place": rec["place"],
            "dehergne_year": rec["dehergne_year"],
            "region": rec["region"],
            "country": rec["country"],
            "identified_chinese": rec["identified_chinese"],
            "wikidata_id": (rec.get("wikidata") or {}).get("id"),
            "queries": queries,
            "best_match": best,
            "wikidata": rec.get("wikidata") or {},
            "dist_km": rec.get("dist_km"),
            "verdict": rec["verdict"],
            "verdict_note": rec["verdict_note"],
            "notes": rec.get("notes", ""),
            "checked_at": CHECKED,
        }
        out_path = os.path.join(CDATA_DIR, f"{gh}.json")
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=2)
        section = make_section(rec, queries, best)
        md_path = os.path.join(COMMENTS_DIR, rec["file"])
        with open(md_path, encoding="utf-8") as fh:
            text = fh.read()
        marker = "\n## TGAZ (CHGIS) check"
        if marker in text:
            text = text.split(marker)[0].rstrip() + "\n"
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(text + "\n" + section)
        print(f"written: {rec['file']}")
        count += 1
    print(f"\n{count} comment file(s) updated; {len(RECORDS)} records written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
