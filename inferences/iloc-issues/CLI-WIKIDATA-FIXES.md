# `.cli` Wikidata fixes — pending application

Compiled **2026-10-14** from the unidentified-location pass over the 34 top-level
issue files in this directory (see [`INDEX.md`](./INDEX.md), § *Clarification
results*). Nothing in `sources/` was changed: this is the application list.

**How it was verified.** Every *current* line below was re-read from the file on
disk on 2026-10-14 (line numbers are the ones in the working tree, not from the
research notes). Every Wikidata id was resolved against
`https://www.wikidata.org/wiki/Special:EntityData/<qid>.json` on the same date;
the label given in brackets is that item's own label. Evidence and page numbers
are in the note named in each entry, and in the issue file's `## References`.

**How to apply.** Edit the `.cli` line, then re-translate/re-import the affected
source (see `notebooks/0-kleio-files.ipynb`, or the `kleio-files` skill) so the
DB picks the value up. Two entries (31 Wouho, 26 T'ang-kia-hiang) also have a
*wrong or stale value already in the database* — noted there.

**Counts:** 28 lines to add an id across 20 issues · 1 wrong id to correct ·
1 probable awaiting a decision · 4 already correct (no action) · 8 leave as is.

---

## Summary

| # | Place | File:line | Action | Id |
|---|---|---|---|---|
| 04 | Kasuza, Arima | `dehergne-c.cli:1780` | add | Q6381698 |
| 08 | Leou-kia-tchouang | `dehergne-s.cli:435` | add | Q1015480 |
| 11 | Moulins | `dehergne-a.cli:1089` | add | Q184883 |
| 12 | Mscislaviae | `dehergne-s.cli:1750` | add | Q744167 |
| 13 | Pe-chieh du Sinfeng | `dehergne-g.cli:1440`, `:1435` | add (2 lines) | Q1356667 |
| 15 | Pé-tsiuen-chan | `dehergne-d.cli:360`, `:1082`; `dehergne-l.cli:310`; `dehergne-b.cli:341` | add (4 lines) | Q11108336 |
| 16 | Petit Tibet « Kinchuen » | `dehergne-r.cli:806`, `:807` | add (2 lines) | Q338033 |
| 17 | Ponti (in valle Tellina) | `dehergne-c.cli:633` | add | Q39321 |
| 18 | Vuen ngan | `dehergne-p.cli:1905` | add | Q1196389 |
| 19 | Rio Kan | `dehergne-b.cli:355`, `:359` | add + remove wrong gloss | Q1046685 |
| 21 | Shaohing | `dehergne-c.cli:1943`; `dehergne-k.cli:247` | add (2 lines) | Q42666 |
| 22 | Sian tan hien | `dehergne-d.cli:932` | add | Q215755 |
| 23 | Siao-tchai | `dehergne-f.cli:48` | add | Q1069968 |
| 24 | Sinhoua, Hué | `dehergne-s.cli:1078` | add + drop `#ILOC` | Q36167 |
| 25 | Sum Kiam | `dehergne-c.cli:2089` | add | Q11104671 |
| 29 | Tonkosz | `dehergne-m.cli:2089` | add | Q958741 |
| 30 | U cham fu | `dehergne-m.cli:2341` | add | Q11124318 |
| 32 | Yean-sam (Yenping) | `dehergne-a.cli:421` | add | Q1337959 |
| 33 | Yuwei do Shansi | `dehergne-r.cli:1722` | add | Q10916242 (alt Q1196894) |
| 34 | Zumbae | `dehergne-m.cli:92` | add | Q206368 |
| **31** | **Wouho** | `dehergne-l.cli:323` | **correct wrong id** | Q1334665 (was Q359990) |
| **01** | **Czerczerse** | `dehergne-m.cli:345` | **probable — decide first** | Q867722 |
| 03 | Tum cheu | `dehergne-f.cli:1867` | none — already there | Q393836 |
| 20 | San kiao hou kia | `dehergne-l.cli:883` | none — already there | Q14583988 |
| 26 | T'ang-kia-hiang | `dehergne-l.cli:328` | none — already there | Q11104671 |
| 27 | Tcha-yuen-keou | `dehergne-t.cli:1131`; `dehergne-l.cli:349` | none — already there | Q14091289 |
| 02, 05, 06, 07, 09, 10, 14, 28 | (see § E) | — | leave as is | — |

---

## A. Add a Wikidata id

### 04 — Kasuza, Arima, Japão (Q6381698, 加津佐町)
- file: `sources/dehergne-c.cli:1780`
- current: `ls$morte/Kasuza, Arima, Japão#ILOC/15900525#ou 15900507?`
- after:   `ls$morte/Kasuza, Arima, Japão#@wikidata:Q6381698/15900525#ou 15900507?`
- id: Q6381698 — 加津佐町 (Kazusa, Minamishimabara, Nagasaki; the Arima seminary town)
- note: `kasuza-arima-identification.md` · rejects Q1055394 (Kazusa province, Chiba)

### 08 — Leou-kia-tchouang do Chou-lou hien (Q1015480, 辛集市)
- file: `sources/dehergne-s.cli:435`
- current: `ls$jesuita-votos-local/Leou-kia-tchouang do Chou-lou hien#perto de Paoting fou/17440607`
- after:   `ls$jesuita-votos-local/Leou-kia-tchouang do Chou-lou hien#perto de Paoting fou @wikidata:Q1015480/17440607`
- id: Q1015480 — 辛集市 (Xinji), successor of 束鹿縣 Shulu; already used at `dehergne-locations-1644.cli:622`
- alt: Q113491787 — 束鹿縣 (historical Shulu County)
- note: `leou-kia-tchouang-identification.md` · village 呂家莊 itself has no item

### 11 — Moulins (Q184883, Moulins)
- file: `sources/dehergne-a.cli:1089`
- current: `ls$jesuita-votos-local/Moulins#ILOC/16890202`
- after:   `ls$jesuita-votos-local/Moulins# @wikidata:Q184883/16890202`
- id: Q184883 — Moulins (Allier, France); **reject Q2280 (Minsk)**
- note: `moulins-identification.md`

### 12 — Mscislaviae (Q744167, Mscislaŭ)
- file: `sources/dehergne-s.cli:1750`
- current: `ls$morte/Mscislaviae#? ILOC/17980208`
- after:   `ls$morte/Mscislau (Mścisław), Bielorrússia# @wikidata:Q744167/17980208`
- id: Q744167 — Mscislaŭ / Мсціслаў (Mahilioŭ region, Belarus)
- note: `mscislaviae-identification.md`

### 13 — « Pe-chieh » du Sinfeng, Kiangsi (Q1356667, 信丰县)
- files/lines: `sources/dehergne-g.cli:1440` and `:1435` (2 lines)
- current 1440: `ls$morte/« Pe-chieh » du Sinfeng, Kiangsi/16960303`
- after   1440: `ls$morte/« Pe-chieh » du Sinfeng, Kiangsi# @wikidata:Q1356667/16960303`
- current 1435: `ls$jesuita-tarefa/Funda a cristandade de « Pe-chieh » du Sinfeng, Kiangsi/1691`
- after   1435: `ls$jesuita-tarefa/Funda a cristandade de « Pe-chieh » du Sinfeng, Kiangsi# @wikidata:Q1356667/1691`
- id: Q1356667 — 信丰县 Xinfeng (Ganzhou, Jiangxi); already used at `dehergne-locations-1701.cli:322`
- note: `pe-chieh-sinfeng-identification.md` · the bourg itself is 白家/白加 (no item)

### 15 — Pé-tsiuen-chan, Hukwang (Q11108336, 柏泉街道) — 4 lines
- `sources/dehergne-d.cli:360`
  - current: `ls$estadia/Pé-tsiuen-chan, Hukwang`
  - after:   `ls$estadia/Pé-tsiuen-chan, Hukwang#柏泉山, Hubei @wikidata:Q11108336`
  - *(this line carries no date — the stay is 1737; see § F4)*
- `sources/dehergne-d.cli:1082`
  - current: `ls$jesuita-votos-local/Pe-tsien-chan, China/17400815`
  - after:   `ls$jesuita-votos-local/Pe-tsien-chan, China#柏泉山 @wikidata:Q11108336/17400815`
- `sources/dehergne-l.cli:310`
  - current: `ls$jesuita-votos-local/« Pe tsien schan »#a 30 km de Hankow/17400202`
  - after:   `ls$jesuita-votos-local/« Pe tsien schan »#a 30 km de Hankow @wikidata:Q11108336/17400202`
- `sources/dehergne-b.cli:341`
  - current: `ls$jesuita-votos-local/Petsiuenchan, Houkouang (Oratório)/17710815`
  - after:   `ls$jesuita-votos-local/Petsiuenchan, Houkouang (Oratório)#柏泉山 @wikidata:Q11108336/17710815`
- id: Q11108336 — 柏泉街道 (Baiquan, Dongxihu, Wuhan, Hubei); the historical hill 柏泉山 has no item
- alt: Q130298171 — 柏泉天主堂 (the Catholic site)
- note: `pe-tsiuen-chan-identification.md` · **reject Q144663** (Hengyang, Hunan)

### 16 — Petit Tibet « Kinchuen » (Q338033, 金川县) — 2 lines
- files/lines: `sources/dehergne-r.cli:806` and `:807`
- current 806: `ls$estadia/Petit Tibet «Kinchuen»/1774`
- after   806: `ls$estadia/Petit Tibet «Kinchuen» (金川, Szechwan)# @wikidata:Q338033/1774`
- current 807: `ls$estadia/Petit Tibet «Kinchuen»/1777`
- after   807: `ls$estadia/Petit Tibet «Kinchuen» (金川, Szechwan)# @wikidata:Q338033/1777`
- id: Q338033 — 金川县 Jinchuan County (Ngawa, Sichuan); alt Q1169539 小金縣
- note: `petit-tibet-kinchuen-identification.md` · **do not use Q10935029** (Jinchuan *campaigns*)

### 17 — « Ponti (in valle Tellina) » (Q39321, Ponte in Valtellina)
- file: `sources/dehergne-c.cli:633`
- current: `ls$jesuita-votos-local/«Ponti (in valle Tellina)/16850202`
- after:   `ls$jesuita-votos-local/Ponte in Valtellina, Sondrio# @wikidata:Q39321/16850202`
- id: Q39321 — Ponte in Valtellina (Sondrio, Lombardy)
- note: `ponti-valle-tellina-identification.md`

### 18 — Residência francesa « Vuen ngan … » (Q1196389, 文安县)
- file: `sources/dehergne-p.cli:1905`
- current: `ls$estadia/Residência francesa «Vuen ngan juxta murum qui Tartaros a Sinis dividit»`
- after:   `ls$estadia/Residência francesa «Vuen ngan (文安) juxta murum qui Tartaros a Sinis dividit»#@wikidata:Q1196389`
- id: Q1196389 — 文安县 Wen'an County (Langfang, Hebei)
- caveat: Dehergne 1953 identifies the name himself (文安), but the Latin tag *juxta murum qui Tartaros a Sinis dividit* is **not reconciled** and Pfister puts Prémare elsewhere; apply only if the caveat is accepted (otherwise keep `#ILOC`). The line carries no date — the stay is 1714.
- note: `vuen-ngan-premare-identification.md`

### 19 — Rio Kan (Q1046685, 赣江) — 2 lines, one also removes a wrong gloss
- `sources/dehergne-b.cli:355`
  - current: `ls$morte/Rio Kan#Rio Nam Khan, em Laos?/15940000#afogado no naufrágio, a caminho do noviciato`
  - after:   `ls$morte/Rio Kan#贛江 Gan Jiang, Jiangxi — naufrágio na viagem de Ricci a Pequim/@wikidata:Q1046685/15940000#afogado no naufrágio, a caminho do noviciato`
- `sources/dehergne-b.cli:359`
  - current: `ls$estadia/rio Kan#Rio Nam Khan, em Laos?/15940000`
  - after:   `ls$estadia/rio Kan#贛江 Gan Jiang, Jiangxi/@wikidata:Q1046685/15940000`
- id: Q1046685 — 赣江 Gan River (Jiangxi); optional Q16002863 (十八灘, the rapids)
- note: `rio-kan-identification.md` · the existing "#Rio Nam Khan, em Laos?" gloss is wrong and is replaced

### 21 — Shaohing (Q42666, 绍兴) — 2 lines
- `sources/dehergne-c.cli:1943`
  - current: `ls$jesuita-votos-local/Shaohing/17060114`
  - after:   `ls$jesuita-votos-local/Shaohing# @wikidata:Q42666/17060114`
- `sources/dehergne-k.cli:247` (birth of K'ieou Pierre, same city, no id)
  - current: `ls$nascimento/Shaohing (Chao-hing fou, Tchö-kiang)/16860501`
  - after:   `ls$nascimento/Shaohing (Chao-hing fou, Tchö-kiang)# @wikidata:Q42666/16860501`
- id: Q42666 — 绍兴 Shaoxing (Zhejiang)
- note: `shaohing-identification.md` · in the source note Dehergne prints **Gal.** (ARSI *Gallia*), not "Gai."

### 22 — Sian tan hien (Q215755, 湘潭)
- file: `sources/dehergne-d.cli:932`
- current: `ls$jesuita-votos-local/Sian tan hien/17060815`
- after:   `ls$jesuita-votos-local/Sian tan hien# @wikidata:Q215755/17060815`
- id: Q215755 — 湘潭 Xiangtan (Hunan), same id already used on the 1704 stay at `:931`
- alt: Q1375015 — 湘潭县 (modern Xiangtan County)
- note: `sian-tan-hien-identification.md` · **reject Q703818** (Yongjia, Zhejiang)

### 23 — Siao-tchai de Han-tchong, Shensi (Q1069968, 城固县)
- file: `sources/dehergne-f.cli:48`
- current: `ls$morte/Siao-tchai de Han-tchong, Shensi/16570510`
- after:   `ls$morte/Siao-tchai de Han-tchong, Shensi#小寨子, 城固縣 @wikidata:Q1069968/16570510`
- id: Q1069968 — 城固县 Chenggu (Hanzhong, Shaanxi)
- alt: Q13763015 — 董家营镇 (inferred modern village)
- note: `siao-tchai-hantchong-identification.md` · see § F3 for the companion character fix

### 24 — Sinhoua, Hué (Q36167, Huế)
- file: `sources/dehergne-s.cli:1078`
- current: `ls$jesuita-votos-local/Sinhoua, Hué#ILOC/17410528`
- after:   `ls$jesuita-votos-local/Sinhoua, Hué# @wikidata:Q36167/17410528`
- id: Q36167 — Huế; this man's death line already carries the same id
- note: `sinhoua-hue-identification.md`

### 25 — Sum Kiam (casa de um cristão) (Q11104671, 松江府)
- file: `sources/dehergne-c.cli:2089`
- current: `ls$jesuita-votos-local/Sum Kiam (casa de um cristão)/17320803`
- after:   `ls$jesuita-votos-local/Sum Kiam (casa de um cristão)#@wikidata:Q11104671/17320803`
- id: Q11104671 — 松江府 Songjiang Fu; alt Q662380 (modern 松江区)
- note: `sum-kiam-identification.md` · same man already linked at `:2084` and `:2090`

### 29 — Tonkosz (Q958741)
- file: `sources/dehergne-m.cli:2089`
- current: `ls$morte/Tonkosz#missão russo-alemã de Saratov ILOC/18050124`
- after:   `ls$morte/Tonkosz (Mariental, hoje Sovetskoje), Saratov# @wikidata:Q958741/18050124`
- id: Q958741 — Sowetskoje / Советское (Sovetsky district, Saratov oblast)
- note: `tonkosz-identification.md` · **reject Q13648980** (Tonkochourovka, Kazakhstan)

### 30 — U cham fu, Hou-kouang (Q11124318, 武昌府)
- file: `sources/dehergne-m.cli:2341`
- current: `ls$jesuita-votos-local/U cham fu, Hou-kouang/17671213`
- after:   `ls$jesuita-votos-local/U cham fu, Hou-kouang#@wikidata:Q11124318/17671213`
- id: Q11124318 — 武昌府 Wuchang Fu (Huguang)
- note: `u-cham-fu-identification.md` · **do not use Q28414894** (English label "Wuchang Fu" but zh 五常府, Manchuria)

### 32 — Yean-sam … Yenping, Fukien (Q1337959, 延平区)
- file: `sources/dehergne-a.cli:421`
- current: `ls$morte/Yean-sam, perto do monte chamado da Cruz, Yenping, Fukien/16490610`
- after (minimal): `ls$morte/Yean-sam, perto do monte chamado da Cruz, Yenping, Fukien#@wikidata:Q1337959/16490610`
- id: Q1337959 — 延平区 Yanping District; already used at `dehergne-locations-1644.cli:291`
- alt: Q68534 — 南平市 Nanping
- note: `yean-sam-aleni-identification.md` · **the village "Yean-sam" is not identified**; this anchors only the prefecture. The issue file also offers a fuller rewrite of the place text.

### 33 — Yuwei do Shansi (Q10916242, 右卫镇; alt Q1196894, 右玉县)
- file: `sources/dehergne-r.cli:1722`
- current: `ls$estadia/Yuwei do Shansi/1727`
- after:   `ls$estadia/Yuwei do Shansi#右衛 (Youwei) = 右卫镇, 右玉縣 @wikidata:Q10916242/1727`
- id: Q10916242 — 右卫镇 Youwei Town, P131 = Q1196894 右玉县 (Shuozhou, Shanxi); the old garrison town, the more precise anchor. County-level alternative: Q1196894 右玉县 (what the research note first proposed).
- note: `yuwei-shansi-identification.md` · **do not use Q56533878** (右卫 the imperial guard institution)

### 34 — Zumbae, Tchamp-pa (Q206368, Sumba Island)
- file: `sources/dehergne-m.cli:92`
- current: `ls$estadia/Zumbae, Tchamp-pa#?/16590000`
- after:   `ls$estadia/Zumbae (Sumba), Indonésia#@wikidata:Q206368/16590000`
- id: Q206368 — Sumba Island (East Nusa Tenggara, Indonesia)
- note: `zumbae-tchamp-pa-identification.md` · Dehergne's « Tcham-pa » is unsupported; distinct from Sumbawa Q186367

---

## B. Correct a wrong id already in the source

### 31 — Wouho (Q1334665, 五河县 — replaces Q359990, 芜湖)
- file: `sources/dehergne-l.cli:323`
- current: `ls$estadia/Wouho#Wuhu @wikidata:Q359990/1772`
- after:   `ls$estadia/Wouho#@wikidata:Q1334665/1772`
- id: Q1334665 — 五河县 Wuhe County (Bengbu, Anhui). The present anchor Q359990 is **Wuhu 蕪湖**, a different town on the Yangtze.
- DB: the database also holds `estadia@wikidata = Q359990 @ 1772`, so a re-import (not just the source edit) is required.
- note: `wouho-identification.md` · Pfister printed p. 767 « à Ou-ho 五河 (1772) »; Dehergne 1957 p. 52 « distinct du Wuhu (Ou-hou) »

---

## C. Probable — apply only on a decision

### 01 — Czerczerse (Q867722, Chachersk) — *probable, not certain*
- file: `sources/dehergne-m.cli:345`
- current: `ls$morte/Czerczerse#ILOC/17940421`
- after:   `ls$morte/Czeczersk (Chachersk), Rússia Branca# @wikidata:Q867722/17940421`
- id: Q867722 — Chachersk / Чачэрск (Homiel region, Belarus)
- why probable: Dehergne prints **Czerczerse** (page-image verified), Backer–Sommervogel prints **Czeczerse** for the same death and **Czeczersk (Russie Blanche)** for the town, and Załęski records a Jesuit *domicilium* at Czeczersk 1754–1820.
- decision: if not accepted, leave the line as it is (keep `#ILOC`).
- note: `czerczerse-identification.md`

---

## D. No action — the id is already in the source

| # | Place | File:line | Already present |
|---|---|---|---|
| 03 | Tum cheu / T'ong-tcheou | `dehergne-f.cli:1867` | `@wikidata:Q393836` |
| 20 | San kiao hou kia | `dehergne-l.cli:883` | `@wikidata:Q14583988` (and `@wikidata:Q15449420` for 瑞州府) |
| 26 | T'ang-kia-hiang | `dehergne-l.cli:328` | `@wikidata:Q11104671` — the issue's "missing" flag is a pipeline artefact |
| 27 | Tcha-yuen-keou | `dehergne-t.cli:1131`; `dehergne-l.cli:349` | `@wikidata:Q14091289` on both |

---

## E. No fix — leave without an id (documented negatives)

| # | Place | File:line | Guidance |
|---|---|---|---|
| 02 | Hirubale, Misore | `dehergne-r.cli:1437` | keep as is; the `%` note already preserves Dehergne's doubt |
| 05 | Ké Diet, Tonquim | `dehergne-c.cli:215` | no id; optional province anchor Q622778 (Tonkin); **reject Q36485** (Hưng Yên) |
| 06 | Làngòi, Tonquim | `dehergne-c.cli:756` | no id; optional province anchor Q622778; **reject Q36485** |
| 07 | Lao chan oua, Hou-kouang | `dehergne-r.cli:1932` | no id; optional province anchor Q2235155 (Qing Huguang) |
| 09 | Maxagongdong | `dehergne-z.cli:72` | keep `#ILOC` until the name is settled |
| 10 | Monzei, Filipinas | `dehergne-i.cli:185` | keep without id; **do not add Q928** (a country) |
| 14 | Pé-pou, Linkiang fou | `dehergne-y.cli:30` | no village id; optional prefecture anchor Q28414898 (临江府) or Q197394 (樟树市) |
| 28 | Tongko (casa de Philippe Wang) | `dehergne-h.cli:134` | keep as an `#ILOC`-style note |

---

## F. Non-Wikidata text corrections found in the same pass

Not part of the id work; listed so they are not lost.

- **F1 — `sources/dehergne-s.cli:1080`** (obs of Siebert, no. 766): the source reads
  `WB nos 549, 539, 708, 711`; the printed page (doc 65, p. 285, printed p. 247)
  reads **`WB nos 549, 589, 708, 711`** — 539 → **589** (verified in the raw and
  edited variants on 2026-10-14).
- **F2 — `sources/dehergne-r.cli:788`**: `ls$nascimento/Lisboa# @wikidata:Q597/17160831`
  — the birth of Félix da Rocha is **31 August 1713**, not 1716 (Dehergne notice 692,
  printed p. 223; Pfister t. 2, printed p. 773). Date edit only.
- **F3 — `sources/dehergne-locations-1701.cli:556`**: the geo3 record transcribes
  Dehergne's characters as **小塞子**; the printed page (doc 73, p. 111, read as an
  image on 2026-10-14) reads **小寨子**. The record also says `(?)No wikidata` — the
  companion fix is to add `@wikidata:Q1069968` there.
- **F4 — dateless `ls$estadia` lines** (Pé-tsiuen-chan `dehergne-d.cli:360`,
  Vuen ngan `dehergne-p.cli:1905`): each has a place but no `/date`. The stays are
  1737 and 1714 respectively, so whichever ids are added above would read more
  naturally once the date is supplied.

---

## G. Findings from the comments pass that are NOT `.cli` Wikidata fixes

Recorded so they are not lost — and, in the first case, so that a wrong action is
not taken.

- **Lofeu rows stay with Hinderer.** A reviewer draft proposed moving the two
  `estadia` rows at `sources/dehergne-h.cli:332,335` (Lofeu, 1722-12-28 and
  1723-04-14) from Romain Hinderer to Johann Hoppe, on the strength of the
  running head **HOPPE** at the top of printed p. 127. That is a false lead: the
  text at the top of p. 127 is the **continuation of Hinderer's notice 407**
  (it ends with his own bibliography, « *CHANEY, Th, Vie du P. Romain Hinderer* »,
  and « Pf. 611 »), while Hoppe's notice **409** begins lower on the same page
  (« N. … 1708 – E. 20 oct. 1724 … P. 1735 »; he entered in 1724 and cannot be at
  Lofeu in 1722–23). The `.cli` (`ls$dehergne/407/obs=…` at `dehergne-h.cli:347`)
  is **correct as it stands — do not move the rows.**
- **Posateri** — two data-quality observations from the same pass: the
  `ls$estadia/Chan-si%(missing)` obs at `sources/dehergne-p.cli:1835` reads
  “Chan-si=Shanxi 陕西 Q46913”, mixing 陕西 (Shaanxi) with 山西 (Shanxi); and
  `ls$estadia/Chang-si# @wikidata:Q46913` at `sources/dehergne-p.cli:1838`
  carries no date. Dehergne's printed
  notice (no. 659, printed p. 209) gives **Chen-si and Kan-sou** for 1691 and
  **Chan-si from 1696**; the province-level anchor `Q46913` is acceptable, but the
  two rows should be reconciled and dated. Not a Wikidata change as such.

---

*Compiled from the 34 issue files and the notes in `/Users/jrc/jesuit-archive/notes/`
(`*‑identification.md`, plus the five notes added by the comments pass). Do not
apply the § C entry without deciding on the probable identification first.*
