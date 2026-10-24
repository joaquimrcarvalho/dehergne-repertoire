# Place to identify

**Shaohing** — `vows location (jesuita-votos-local)`, **1706-01-14** (`17060114`)

## Person(s)

**Cyr Contancin** (`deh-cyr-contancin`) — Padre · França · Chinese name: Kong Tang-Sin Tong-P'ing · Dehergne P. 192

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1670-05-25 | birth | Issoudun | Q210772 |
| 1688-09-09 | entered Jesuits | Paris | Q90 |
| 1701-11-15 | arrival | Kwangchowwan | Q1506615 |
| 1706-01-14 | vows location | **Shaohing** | ❗️ **missing** |
| 1707 | stay | Chekiang (Tchö-kiang) | Q16967 |
| 1711 | stay | Pequim | Q956 |
| 1718-10-20 | departure | Shansi | Q46913 |
| 1720 | stay | Kiangsi | Q57052 |
| 1721 | stay | Nanchang | Q171943 |
| 1725 | stay | Cantão | Q16572 |
| 1731 | stay | França | Q142 |
| 1732-11-10 | stay | Lorient | Q71724 |
| 1732-11-21 | death | [No mar, perto de Cádiz] | Q15682 |

**Source note** (Dehergne):
> …Halde., repart de Lorient, 10 nov. 1732. Supérieur général de la Mission française v. 1731. P. 1700 (Franc. 17, 29v). V. « Chao-him prov. Tche kiam »=Shaohing, 14 janv. 1706, pr. (Gai. 16, 108). M. 21 nov. 1732 (HS 50, 133) en mer, « non longe a freto Gaditano» vers Cadix (Franc. 27, Mv., Franc. 45 II, 469470). (Né et) baptisé le 25 mai 1670 « en l'église St Cyr à Issoudun, fils de Maistre Jean Contancin, docteur en médecine en la ville d'Issoudun, et de Marie Lanjon (ou Laujon)»., famille d'au …

## Identification

**Conclusion.** Identified: **Shaohing = 紹興 (Shaoxing), the 紹興府 of
Chekiang, between Hangchow and Ningpo → `Q42666`** (Shaoxing 紹興市, Zhejiang).
Dehergne himself equates the vow register's form — « V. "Chao-him prov. Tche
kiam"=**Shaohing**, 14 janv. 1706, pr. (**Gal.** 16, 108) » (notice 192, printed
pp. 59-60) — and his 1957 Ming gazetteer has the entry « **18. SHAOHING
(Chao-hing) 紹興 fou, entre Hangchow et Ningpo** … C'est le Sciaohino de Ricci,
distinct du Sciaochino (=Shiuching) au Kwangtung » (entry 18, printed p. 20;
index « Shaohing, Chao-hing … Che 18 », printed p. 133). The characters 紹興
were read on the page render, because the OCR of doc 73 drops CJK. Two details:
the siglum is printed **`Gal.`** (= ARSI *Gallia*; the issue file's "Gai." is a
misreading), and the ARSI register itself is **not in this archive**, so the
equation rests on Dehergne's explicit gloss plus the 1957 gazetteer. Full
research note: `notes/shaohing-identification.md`.

Source fix: `sources/dehergne-c.cli:1943` —
`ls$jesuita-votos-local/Shaohing/17060114` → add `# @wikidata:Q42666`.
(The same city, without an id, also occurs at `sources/dehergne-k.cli:247`,
birth of K'ieou Pierre 1686.)

## Task

- [x] Confirm the Wikidata ID for **Shaohing** — **identified as 紹興 Shaoxing,
      Chekiang → `Q42666`**. The source `.cli` still needs the `@wikidata`
      comment (see *References*).
- [x] Research note written: `notes/shaohing-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | notice **192**, **pp. 59-60** | doc 65, pp. 97-98, raw — `pha page 65 98` |
| DEHERGNE, Joseph. *Les Chrétientés de Chine de la période Ming (1581-1650)*, *Monumenta Serica* 16 (1957) | entry **18**, **p. 20** (« SHAOHING (Chao-hing) 紹興 fou ») | doc 73, p. 21, raw + render — `pha page 73 21` |
| Ibid., place index | « Shaohing … Che 18 », **p. 133** | doc 73, p. 134, raw — `pha page 73 134` |
| Ibid., entry 13 (SHIUHING / Tchao-k'ing) | « Distinct de Shaohing (Chao-hing) fou du Chekiang », **p. 90** | doc 73, p. 91, raw — `pha page 73 91` |
| DEHERGNE, *Répertoire*, notice 431 (K'ieou, Pierre) | « N. Shaohing (Chao-hing fou, Tchô-kiang), 1 mai 1686 », **p. 135** | doc 65, p. 173, raw — `pha page 65 173` |
| DEHERGNE, *Répertoire*, sigla table | « Gal. Gallia, Jésuites de l'Assistance de France, section des ARSI » | doc 65, p. 36 (printed p. XXXIV), raw — `pha page 65 36` |
| [Q42666](https://www.wikidata.org/wiki/Q42666) | Shaoxing 紹興市, Zhejiang | Wikidata API, checked 2026-10-15 |

**Note (PHA archive):** `notes/shaohing-identification.md`
(slug `shaohing-identification`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `紹興` / `绍兴` | — | 10 | `hvd_32185` 绍兴府 (府), 1367–1911 |
| `紹興府` | year 1706 | 2 | `hvd_32185` 绍兴府 (府), 1367–1911 |
| `Shaoxing` | — | 10 | `hvd_32185` 绍兴府 (府), 1367–1911 |
| `Shanyin` (山陰, the 附郭 county) | — | 12 | `hvd_40762` 山阴县 (县), 815–1911 |
| `Ciquione` (Dehergne's 1586 spelling) | — | 0 | — (TGAZ indexes no European spellings) |
| `Shaoshing` / `Shaohing` (Dehergne) | — | 0 | — |
| `紹興府` | year 1586 | 2 | `hvd_32185` 绍兴府 (府), 1367–1911 |
| `山陰縣` / `會稽縣` (the two 附郭 counties) | year 1586 | 2 / 1 | `hvd_40762` / `hvd_40763`, both at 30.00451, 120.57826 |
| `Cixi` (慈谿, the anchor now in the sources) | year 1586 | 1 | `hvd_40732` 慈谿县 (县), parent **寧波府 Ningpo Fu** |

**Best match.** `hvd_32185` — 紹興府 (Shaoxing Fu), superior prefecture (府),
1367–1911, parent chain 江南行省 → 浙江行省 → 浙江布政使司 → **浙江省**
(1645–1911); 30.00451 N, 120.57826 E; `present_location` "今浙江绍兴市".
Canonical record:
<https://chgis.hudci.org/tgaz/placename/hvd_32185>. The same seat point is
carried by the earlier 府 (1131–1275, `hvd_32187`) and 路 (1276–1366,
`hvd_32186`) records, and the 附郭 county 山陰縣 (`hvd_40762`, 815–1911) sits
at the same coordinates — a continuous prefectural seat, valid throughout the
Dehergne period.

**Coordinates.** TGAZ 30.00451, 120.57826 vs Wikidata `Q42666` (紹興市)
30.00000, 120.58333 → **0.7 km**.

**Verdict: `confirmed`.** TGAZ records 紹興府 in Zhejiang at exactly the city
identified by the issue (`Q42666`), with a matching name, level, province and
point. No change to the issue's conclusion.

**Alias `Ciquione` (António de Almeida's 1586 stay, `sources/dehergne-a.cli:513`).**
Dehergne prints the form in guillemets and glosses it in the same line —
*« Ciquione » (Shaoshing, Chao-hing), Tchö-kiang* — and his 1957 gazetteer lists
it among the spellings of 紹興: *« Écrit: Ciquione (CorB II 794), Ciaushino,
Sciauhim … Schauhsing »* (entry 18, printed p. 20). TGAZ returns **0 hits** for
`Ciquione`, `Ciquion`, `Shaoshing`, `Shaohing` and `Xaohing` — it indexes only
Chinese characters and pinyin, so a European source spelling can never be
matched directly. Read through the gloss, the alias lands on the same
prefecture: `紹興府` with `year=1586` returns `hvd_32185` (and the duplicate
`hvd_90439`), and the two 附郭 counties of the prefectural seat, 山陰縣
(`hvd_40762`) and 會稽縣 (`hvd_40763`), both sit on 30.00451 N, 120.57826 E.
A village-level check is impossible for 1586 in any case: TGAZ's 村鎮 layer
exists only for the 1820 and 1911 layers. The alias therefore does not change
the verdict (prefecture level **confirmed**), but it does make the point that
**the resolution has to go through Dehergne's own gloss, not through the
spelling**.

**Data-quality by-product (Lead review).** The 紹興 identification is contradicted
by four pre-existing `@wikidata` links in the sources, which use `Q706161` — that
is **慈溪 Cixi (Ningbo)**, not Shaoxing: `sources/dehergne-a.cli:513`
(«Ciquione»), `sources/dehergne-locations-1644.cli:158` (geo2$Shaoshing),
`sources/dehergne-r.cli:2045` and `:2064` (Chao-hing stays). They should be
`Q42666`. (The `Q706161` at `sources/dehergne-locations-1644.cli:155`,
geo3$Tzeki, is correctly Cixi.) Not changed here: this pass is read-only on
the sources. TGAZ corroborates the correction independently: 慈谿县
(`hvd_40732`, 1418–1911) is recorded under **寧波府 Ningpo Fu**, not 紹興府, so
a `Q706161` anchor cannot be right on a place Dehergne places in Shaohing
(and Dehergne glosses the 1586 stay as Shaohing, not Cixi).
