# Place to identify

**Tonkosz** — `death (morte)`, **1805-01-24** (`18050124`)

## Person(s)

**Aloys Moriz** (`deh-aloys-moriz`) — Padre · Áustria · Dehergne P. 570

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1738-04-08 | birth | Landeck, Tirol | Q660183 |
| 1757-10-09 | entered Jesuits | Landsberg | Q494299 |
| 1772 | stay | Lorient | Q71724 |
| 1773-11 | arrival | Cantão | Q16572 |
| 1776 | stay | Alemanha | Q183 |
| 1786 | stay | Rússia Branca | Q184 |
| 1787-08-15 | vows location | Rússia Branca | Q184 |
| 1805-01-24 | death | **Tonkosz** | ❗️ **missing** |
| 1773 | stay | Europa | Q46 |

**Source note** (Dehergne):
> … rentre en 1786 chez les Jésuites de la Russie Blanche. V. 15 août 1787 en Russie Blanche (Vitebsk?). M. 24 janv. 1805, Tonkosz (mission russo-allemande de Saratov). Pf. 976., Prof. Georg Pfeilschifter, P. Alois Moriz iiber seine Chinareise 1772-1773, Stimmen der Zeit CXXI (Fribourg 1931), 176-195. """

## Identification

**Conclusion.** Identified as the Volga-German colony **Tonkoszorówka / Mariental**,
today **Sowetskoje (Советское)**, Sovetsky district, Saratov oblast, Russia →
`Q958741`. All three archive witnesses give the death as "Tonkosz" and localise it
only as the German mission of Saratov (Dehergne notice 570, printed p. 181; Pfister
t. 2, printed p. 976; Backer–Sommervogel t. 5, col. 1326). The colony is fixed by
Załęski's history of the Polish province (not in this archive, read from the
Internet Archive full text), which records the 1803 division of the Saratov mission:
"**O. Moritza do Tonkoszorowskiej, którą Niemcy przezwali Marienthal**" (printed
p. 396) — i.e. Father Moriz was posted to Tonkoszorówka, "which the Germans called
Mariental", and died there on 24 Jan. 1805. **Confidence: high for the colony**, with
the caveat that this equation comes from outside the PHA archive; note also that
"Tonkosz" is not a modern gazetteer form (the Russian name Тонкошуровка was official
only 1914-1928). ARSI Polotsk-province catalogues for 1803-1805 are **not held in
this archive**. Full research note: `notes/tonkosz-identification.md`.

Source fix: `sources/dehergne-m.cli:2089` —
`ls$morte/Tonkosz#missão russo-alemã de Saratov ILOC/18050124` →
`ls$morte/Tonkosz (Mariental, hoje Sovetskoje), Saratov# @wikidata:Q958741/18050124`.

## Task

- [x] Confirm the place and the Wikidata ID — **Tonkoszorówka / Mariental, today
      Sovetskoje (Saratov) `Q958741`**; the source `.cli` still needs the
      `@wikidata` comment (see *Source fix* above and *References*). Do **not** use
      `Q13648980` (Tonkochourovka, Kazakhstan — a 1909 daughter settlement).
- [x] Research note written: `notes/tonkosz-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 570, **p. 181** | doc 65, p. 219, raw — `pha page 65 219` |
| PFISTER, Louis. *Notices biographiques…*, t. 2 | no. 441, **p. 976** | doc 50, p. 442, raw — `pha page 50 442`; table, p. 1059 = doc 50, p. 525 |
| BACKER, Augustin de; SOMMERVOGEL, Carlos. *Bibliothèque de la Compagnie de Jésus*, t. 5 | **col. 1326** ("mourut à Tonkosz, le 24 janvier 1805") | doc 142, p. 671, raw — `pha page 142 671` |
| ZAŁĘSKI, Stanisław. *Jezuici w Polsce*, t. V, cz. 1, § 43 | **pp. 394, 396** | not in the archive (Internet Archive `cz1jezuiciwpol05zals`) |
| Wikidata | Q958741 (Sovetskoye, Saratov oblast) — kept; Q13648980 (Tonkochourovka, Kazakhstan) — rejected | `wbgetentities`, read 2026-10-15 |

**Note (PHA archive):** `notes/tonkosz-identification.md` in the PHA archive notes folder (`/Users/jrc/jesuit-archive/notes/`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ carries the
**HGR** layer (Historical Gazetteer of the Russian Empire, 1785–1796), which was
searched for both the colony and its district.

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Saratov` / `Саратов` | — | 3 | `hgr_345` Саратов (главный город), `hgr_70` Саратовский уезд, `hgr_29` Саратовское Наместничество |
| `Саратов` | year 1795 | 3 | the same three |
| `Saratov` | year 1805 | 0 | — |
| `Tonkosz` | — | 0 | — |
| `Tonkoszorowka` | — | 0 | — |
| `Тонкошуровка` | — | 0 | — |
| `Mariental` / `Мариенталь` | — | 0 | — |
| `Sovetskoye` / `Советское` | — | 0 | — |

**Best match (parent only).** `hgr_345` — Саратов / Saratov, *glavnyi gorod*
(главный город, "chief town"), HGR **1785–1796**, parent **Саратовский уезд**
(`hgr_70`), itself under **Саратовское Наместничество** (`hgr_29`); 51.5333 N,
46.0 E; `present_location` "Saratov, Saratov Oblast, Russia". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hgr_345>. The colony itself is
**not** in TGAZ: neither the Polish forms "Tonkosz"/"Tonkoszorowka", the Russian
"Тонкошуровка", the German "Mariental", nor the modern "Sovetskoye" returns a
record.

**Coordinates.** Wikidata `Q958741` (Sovetskoye / Mariental) 51.45, 46.7333 vs
TGAZ Saratov 51.5333, 46.0 → **51.6 km**; the colony lay northeast of the city, a
normal distance for a Volga-German colony in Saratov district.

**Verdict: `partially-confirmed`.** TGAZ confirms the named parent (Saratov city,
uezd and namestnichestvo — the "mission russo-allemande de Saratov" of Dehergne)
but has no record of the Tonkosz / Mariental colony, so it cannot confirm the
locality itself; that identification rests on the archive and Załęski evidence in
the issue alone. Note the HGR layer ends in 1796, nine years before the 1805
death, and its coverage of the Volga-German colonies is not established by these
queries.
