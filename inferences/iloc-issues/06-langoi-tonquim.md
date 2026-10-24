# Place to identify

**Làngòi, Tonquim** — `vows location (jesuita-votos-local)`, **1741-11-12** (`17411112`)
- Tentative candidate: `Q36485` (Hien, Tonquim, score 0.71) — verify.

## Person(s)

**Manuel de Carvalho** (`deh-manuel-de-carvalho`) — Padre · Portugal · Dehergne P. 150

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | stay | China | — |
| 1710-01-14 | birth | Porto de Mós, diocese de Leiria | Q1012710 |
| 1736 | stay | Tonquim | Q622778 |
| 1741-11-12 | vows location | **Làngòi, Tonquim** | ❗️ **missing** |
| 1750 | stay | Tonquim | Q622778 |
| 1762-07-05 | stay | Macau | Q14773 |
| 1764-10-19 | stay | Lisboa (Forte de S. Julião) | Q597 |
| 1767-07-09 | stay | Itália | Q38 |
| 1775 | stay | Villa Rufinella | Q3558780 |
| 1787-03-23 | death | Urbania, Itália | Q190134 |

**Source note** (Dehergne):
> Carvalho, Manuel de (port.) (III) P. 150 N. Porto de Moz, d. de Leiria (ou selon d'autres, d. de Lisbonne) 14 janv. 1710 -E. 2 avril 1724 (Lus. 47, 309., 48, 20v). Emb. pour le Japon en 1732 (W 1800)., missionnaire au Tonkin, 1736- 1750., passe en Chine (Lus. 49, 59 n° 844., Lus. 49, f° 79, 94v et 109v)., capturé à Macao, 5 juill. 1762., emprisonné au fort St. Julien, 19 oct. 1764., déporté en Ita

## Identification

**Conclusion.** **Not identified** — no `@wikidata` id should be added to
`ls$jesuita-votos-local/Làngòi, Tonquim`. Dehergne gives the name without gloss,
district or characters, and it occurs nowhere else in the archive. The printed
form is **Làngòi** (verified on the page image: doc 65, p. 85, printed p. 47;
the OCR's "Längdi"/"Längôi" are mis-read diacritics); the vow is a
*coadjutor spiritualis* formula whose only source is ARSI *Lusitania* 24, 206,
not held here. The tentative candidate `Q36485` is **wrong**: that entity is
*Hưng Yên*, a Red River delta provincial city
([Q36485](https://www.wikidata.org/wiki/Q36485)); the match was a fuzzy string
score only. If an anchor is wanted meanwhile, use the province-level Tonkin
`Q622778`, which this person already carries for his two Tonquim stays.

*Inference, explicitly labelled:* "Làng" is the Vietnamese word for **village**
(làng), so "Làngòi" is "Làng + one syllable" — a village name, consistent with
Dehergne's Tonkin vow residences. It cannot be tied to a district; no register
or gazetteer in this archive names it.

Full research note: `notes/langoi-tonkin-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 150 (Carvalho III), **printed p. 47** | doc 65, p. 85, raw (image-checked) — `pha page 65 85` |
| WICKI, Josef. *Liste der Jesuiten-Indienfahrer 1541–1758* (1967) | no. 1800, **printed p. 325** (1732 sendung für Japan) | doc 66, p. 79, raw — `pha page 66 79` |
| PFISTER, Louis. *Notices biographiques…*, t. 2 | index p. 1087; "Pf. 981" = no. 445 Mauro de Azevedo, printed p. 981 | doc 50, pp. 553, 447, raw — `pha page 50 553` |
| ARSI *Lusitania* 24, f. 206 (register of the 1741 vow) | cited by Dehergne; **not in this archive** | — |
| [Q36485](https://www.wikidata.org/wiki/Q36485) | rejected candidate = Hưng Yên | — |
| [Q622778](https://www.wikidata.org/wiki/Q622778) | Tonkin, province-level anchor (already used in the source) | — |

**Note (PHA archive):** `notes/langoi-tonkin-identification.md`.

## Task

- [ ] Confirm the place and the Wikidata ID — **not identified**; no id can be
      added from this archive. Next step: read ARSI *Lusitania* 24, f. 206 (the
      vow register Dehergne cites) and *Lusitania* 47, 309 / 48, 20v (his entry
      records), none of which is held here.
- [x] Research note written: `notes/langoi-tonkin-identification.md`.


## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Vietnamese / Tonkin layer; the name was queried in the printed form, without
diacritics, and with the "Làng" element separated:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Làngòi` | — | 0 | — |
| `Langoi` | — | 0 | — |
| `Làng Gòi` | — | 0 | — |

**Verdict: `outside-coverage`.** All three queries returned 0 hits. TGAZ cannot
contribute to the identification of the Tonkin vow place; the name remains
unidentified from the archive, as the issue concludes.
