# Place to identify

**«Ponti (in valle Tellina)** — `vows location (jesuita-votos-local)`, **1685-02-02** (`16850202`)

## Person(s)

**Filippo-Felice Carrocci** (`deh-filippo-felice-carrocci`) — Padre · Sabóia · Chinese name: Lo Fei-li · Dehergne P. 144

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1646 | birth | Sabóia | Q14118 |
| 1685-02-02 | vows location | **«Ponti (in valle Tellina)** | ❗️ **missing** |
| 1688 | stay | Cantão | Q16572 |
| 1689 | stay | Kiangsi | Q57052 |
| 1690 | stay | Hainan | Q42200 |
| 1691 | stay | Cantão | — |
| 1691 | stay | Shangchuan | — |
| 1692 | stay | Hukwang | — |
| 1692 | stay | Kiangsi | — |
| 1695 | stay | Shensi | — |
| 1695-12-25 | death | [No caminho entre Kiangchow e Taiyuan, Shansi] | — |
| 1695 | stay | Hanchung, Shansi | — |
| 1695 | stay | Kiangchow, Shansi | — |

**Source note** (Dehergne):
> …690, Hainan., 1691, Canton et voyage à Sancian., 1692, Hukwang (JS 134, 375a) et Kiangsi., 1695, Shensi., puis Hanchung et Kiangchow, au Shansi. V. « Ponti (in valle Tellina) » 2 févr. 1685, pr. Il signe en latin Carrocius (Ital. 18, 364). M. « apud Sinas », en Chine, 25 déc. 1695 (HS 49, 221 et 50, 48v) Borg. Lat. 523 f° 59 le fait mourir au Shensi., en fait, il est mort 25 déc. 1695, en route entre Kiangchow et Taiyuan, Shansi (JS 148, 220 et RBS 462 du 15 oct. 1950). JS 134, 376: « obiit anno…

## Identification

**Conclusion.** Identified as **Ponte in Valtellina**, province of Sondrio,
Lombardy, Italy → `Q39321`. "Ponti" is the locative of *Pons / Ponte*, and the
archive supplies the Latin form of the place independently: the *Litterae
Quadrimestres* of 1557-1558 call it "**Pons, oppidum Vallis Tellinae**" and record a
**Jesuit college founded in that town** — "de collegio fundato ab hoc viro, **in
oppido Ponte, in Valle Tellina**" (doc 107, printed pp. 682 and 1032). **Confidence:
high for the place.** Two caveats: Pfister gives no vow place at all for Carrocci
(his notice only says "né en Savoie", printed p. 414), and the archive does not show
that a Jesuit house was still functioning at Ponte in 1685 — the identification
rests on the Latin place-name, not on a 1685 station list. The vow register itself
(ARSI ***Ital*. 18, f. 364**) is **not in this archive**. Full research note:
`notes/ponti-valle-tellina-identification.md`.

Source fix: `sources/dehergne-c.cli:633` —
`ls$jesuita-votos-local/«Ponti (in valle Tellina)/16850202` →
`ls$jesuita-votos-local/Ponte in Valtellina, Sondrio# @wikidata:Q39321/16850202`.

## Task

- [x] Confirm the place and the Wikidata ID — **Ponte in Valtellina (Sondrio)
      `Q39321`**; the source `.cli` still needs the `@wikidata` comment (see *Source
      fix* above and *References*).
- [x] Research note written: `notes/ponti-valle-tellina-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 144, **p. 46** | doc 65, p. 84, raw — `pha page 65 84` |
| PFISTER, Louis. *Notices biographiques…*, t. 1 | no. 168, **p. 414** (no vow place given) | doc 47, p. 453, raw — `pha page 47 453` |
| *Litterae Quadrimestres*, t. V (1557-1558) | **p. 682** n. 2 ("in oppido Ponte, in Valle Tellina"); index, **p. 1032** ("Pons, opp. Vallis Tellinae") | doc 107, pp. 712 and 1062, raw — `pha page 107 712`, `pha page 107 1062` |
| Wikidata | Q39321 (Ponte in Valtellina) | `wbsearchentities`/`wbgetentities`, read 2026-10-15 |
| ARSI *Ital*. 18, f. 364; MARGIOTTI, p. 174 | cited by Dehergne, notice 144 | **not held in this archive** |

**Note (PHA archive):** `notes/ponti-valle-tellina-identification.md` in the PHA archive notes folder (`/Users/jrc/jesuit-archive/notes/`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
European layer; the Latin locative, the Italian forms and the valley name were
queried:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Ponti` | — | 0 | — |
| `Ponte` | — | 0 | — |
| `Ponte in Valtellina` | — | 0 | — |
| `Valtellina` | — | 0 | — |

**Verdict: `outside-coverage`.** All four queries returned 0 hits. TGAZ cannot
contribute to the identification as Ponte in Valtellina `Q39321`; the issue's
identification stands on the archive evidence alone.
