# Place to identify

**Moulins** — `vows location (jesuita-votos-local)`, **1689-02-02** (`16890202`)
- Tentative candidate: `Q2280` (Minsk, score 0.67) — verify.

## Person(s)

**Pierre Amys** (`deh-pierre-amys`) — Padre · França · Dehergne P. 38

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1653-09-05 | birth | Angers | Q38380 |
| 1670-09-26 | entered Jesuits | Paris | Q90 |
| 1689-02-02 | vows location | **Moulins** | ❗️ **missing** |
| 1701 | stay | Paris | Q90 |
| 1735-11-04 | death | Paris (colégio) | Q90 |

**Source note** (Dehergne):
> …ur le Séminaire que les Jésuites français voulaient fonder à Nankin (PRO SP 9-239-38)., mais Mgr Cicero, évêque de Nankin, s'y oppose. V. « Molini », Moulins, 2 févr. 1689, pr. (Gai. 13, 489). M. 4 nov. 1735, au collège de Paris (HS 53a, 4., Franc. 20, 266). Pf. 451., DBF (E. G. Ledos).

## Identification

**Conclusion.** Identified as **Moulins, chef-lieu of the Allier department,
Auvergne-Rhône-Alpes, France** → `Q184883`. Dehergne's own text glosses the Latin
vow formula "« **Molini** », Moulins, 2 févr. 1689" (notice 38, printed p. 13), and
Backer–Sommervogel independently states that Amys "**1688, il était professeur de
logique à Moulins**" (t. 1, col. 308) — the Jesuit college of Moulins, one year
before the profession. **Confidence: high.** The issue's tentative candidate
**Q2280 is Minsk** ("capital and largest city of Belarus", checked on Wikidata) and
must be rejected; it is a *Moulins*/*Minsk* string confusion. Pfister has no notice
for Amys and says nothing about Moulins (his "Pf. 451" is a mention inside
Gerbillon's notice). Full research note: `notes/moulins-identification.md`.

Source fix: `sources/dehergne-a.cli:1089` —
`ls$jesuita-votos-local/Moulins#ILOC/16890202` →
`ls$jesuita-votos-local/Moulins# @wikidata:Q184883/16890202`.

## Task

- [x] Confirm the place and the Wikidata ID — **Moulins (Allier) `Q184883`**; the
      source `.cli` still needs the `@wikidata` comment (see *Source fix* above and
      *References*), and the tentative `Q2280` (Minsk) must not be used.
- [x] Research note written: `notes/moulins-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 38, **p. 13** | doc 65, p. 51, raw — `pha page 65 51` |
| BACKER, Augustin de; SOMMERVOGEL, Carlos. *Bibliothèque de la Compagnie de Jésus*, t. 1 | **col. 308** ("1688, il était professeur de logique à Moulins") | doc 138, p. 182, raw — `pha page 138 182` |
| PFISTER, Louis. *Notices biographiques…*, t. 1 | no. 173, **p. 451** (mention only) | doc 47, p. 490, raw — `pha page 47 490` |
| Wikidata | Q184883 (Moulins, Allier) — kept; Q2280 (Minsk) — rejected | `wbsearchentities`/`wbgetentities`, read 2026-10-15 |

**Note (PHA archive):** `notes/moulins-identification.md` in the PHA archive notes folder (`/Users/jrc/jesuit-archive/notes/`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
European layer; the French form and the Latin vow form were queried:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Moulins` | — | 0 | — |
| `Molins` | — | 0 | — |
| `Molini` | — | 0 | — |

**Verdict: `outside-coverage`.** All three queries returned 0 hits. TGAZ cannot
contribute to the identification as Moulins (Allier) `Q184883`; it neither
confirms nor rejects it, and the issue's identification stands on the archive
evidence alone.
