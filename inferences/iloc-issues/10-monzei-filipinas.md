# Place to identify

**Monzei, Filipinas** — `death (morte)`, **1699-10-13** (`16991013`)
- Tentative candidate: `Q928` (Filipinas, score 0.69) — verify.

## Person(s)

**Juan Miguel de Irigoyen** (`deh-juan-miguel-de-irigoyen`) — Padre · Espanha · Chinese name: Lou Je-Mong Yu-Tchai · Dehergne P. 415

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | stay | Kiangnan | — |
| — | stay | Foochow | — |
| 1646-04-19 | birth | Pamplona, Navarra | Q10282 |
| 1667 | arrival | Filipinas | Q928 |
| 1678-06 | stay | Amoy, Fukien | Q68744 |
| 1679 | stay | Tch'ang chou | Q113497198 |
| 1679-08-15 | vows location | Ham cheu | Q4970 |
| 1680 | stay | Tch'ang chou | Q113497198 |
| 1685-02-06 | departure | Cantão | Q16572 |
| 1699-10-13 | death | **Monzei, Filipinas** | ❗️ **missing** |
| 1685-02-06 | stay | Manila | Q1461 |

**Source note** (Dehergne):
> … de 1696). V. 15 août 1679, « in collegio Hâm cheu », pr. (Lus. 9, 274)., il signe de Yrigoyen. M. 13 oct. 1699 à Monzei, Philippines (HS 49, 167: P. Jo: Michael de Yrigoyen). [S'il ne s'agit pas d'un homonyme? cf. Tolet. 21 II, 290]? Pf. 389."""

## Identification

**Conclusion.** **Not identified.** The only witness is `HS 49, 167` — i.e. ARSI
*Historia Societatis* 49, f. 167, one of the chronological lists of the dead
(defined by Dehergne himself, doc 65, p. 36) — which the archive does not hold.
The archive's independent witness, Pfister notice 147 (printed p. 389), gives no
place and says only "M. après 1688, **probablement aux Philippines**"; Pfister's
index has no "Monzei". The tentative candidate **Q928 is the country (Philippines),
not a place**, so it cannot serve as a town anchor; and Dehergne himself marks the
entry as possibly an homonym. Full research note:
`notes/monzei-filipinas-identification.md`.

No source fix. `sources/dehergne-i.cli:185` —
`ls$morte/Monzei, Filipinas#ILOC/16991013` — should stay **without** a `@wikidata`
comment; `#@wikidata:Q928` would assert a country for a place-name that is still
unread.

## Task

- [ ] Confirm the Wikidata ID for **Monzei, Filipinas** — **not possible from this
      archive**: no place-level identification; `Q928` is the country. Next step:
      read **ARSI *Historia Societatis* 49, f. 167** and check the homonym against
      **ARSI *Toletanum* 21 II, 290**; neither is held here.
- [x] Research note written: `notes/monzei-filipinas-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 415, **p. 130** | doc 65, p. 168, raw — `pha page 65 168` |
| DEHERGNE, *Répertoire*, abbreviation table (`HS` = ARSI *Historia Societatis*, lists of the dead) | **p. XXXIV** | doc 65, p. 36, raw — `pha page 65 36` |
| PFISTER, Louis. *Notices biographiques…* t. 1 | notice 147, **pp. 389-390** | doc 47, pp. 428-429, raw — `pha page 47 428` |
| PFISTER, *Notices…* t. 2, *Table alphabétique* | **p. 1089** (« de Yrigoyen, 389 »; no Monzei) | doc 50, p. 555 — `pha page 50 555` |
| SCHÜTTE, *Monumenta historica Japoniae* I | Doc. 74, **p. 894** (the 1621 Philippine catalogue, described but not printed) | doc 18, p. 940, edited — `pha page 18 940` |
| ARSI *Historia Societatis* 49, f. 167; *Toletanum* 21 II, 290 | — | **not in the archive** |

**Note (PHA archive):** `notes/monzei-filipinas-identification.md`
(slug `monzei-filipinas-identification`). Country (not place) item:
[Q928](https://www.wikidata.org/wiki/Q928) (checked 2026-10-15).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Philippine layer; the name and the country were queried deliberately:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Monzei` | — | 0 | — |
| `Monzey` | — | 0 | — |
| `Manila` | — | 1 | `hvd_19499` 玛泥兰 (Manilan), 1820 村鎮 under 三姓 |

**Result.** The only hit is 玛泥兰 / Manilan, an **1820** CHGIS village under
三姓 in Manchuria (46.31 N, 129.90 E) — a pinyin prefix homonym, not Manila.

**Verdict: `outside-coverage`.** TGAZ has no layer covering the Philippines; the
single match is unrelated. It can neither confirm nor reject the unidentified
name, which remains unidentified from the archive, as the issue concludes.
