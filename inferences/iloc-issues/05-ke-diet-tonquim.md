# Place to identify

**Ké Diet, Tonquim** — `vows location (jesuita-votos-local)`, **1754-08-15** (`17540815`)
- Tentative candidate: `Q36485` (Hien, Tonquim, score 0.76) — verify.

## Person(s)

**Paulo de Campos** (`deh-paulo-de-campos`) — Padre · Portugal · Dehergne P. 133

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1721-07-07 | birth | Bobadela, diocese de Coimbra | Q888363 |
| 1754-08-15 | vows location | **Ké Diet, Tonquim** | ❗️ **missing** |
| 1769-11-01 | death | Tonquim | Q622778 |

**Source note** (Dehergne):
> …ampoz), Paulo de (port.) P. 133 N. Babadella, d. de Coïmbre, 7 juill. 1721. E. 2 mai 1737 (Lus. 48, 264). Emb., mais pour le Japon, 1746 (W 1917). V. Ké Diet, au Tonkin, 15 août 1754, pr. (Lus. 17, 177): de Campoz. M. au Tonkin, 1 nov. 1769, il est marqué de la vice-prov. de Chine (HS 53a, 160). Par erreur, pensons-nous.

## Identification

**Conclusion.** **Not identified** — no `@wikidata` id should be added to
`ls$jesuita-votos-local/Ké Diet, Tonquim`. Dehergne (notice 133, printed p. 42 =
PDF p. 80) prints the place bare, with no gloss, no district and no characters,
and the form occurs **nowhere else in the archive** except that one page. The
Tonkin mission registers that could place it (ARSI *Lusitania* 17, f. 177, the
register Dehergne cites for this very profession) are not in this archive. The
tentative candidate `Q36485` is **wrong**: that entity is *Hưng Yên*, a
provincial city of the Red River delta ([Q36485](https://www.wikidata.org/wiki/Q36485)),
and nothing but a fuzzy string score connects it with Ké Diet.

Places in the biography are already anchored as follows: birth `Q888363`
(Bobadela); death `Tonquim` → `Q622778`. If a link is wanted for the vow place
meanwhile, use the province-level Tonkin `Q622778` (already the death anchor),
not `Q36485`.

*Inference, explicitly labelled:* "Ké" is Dehergne's French rendering of
Vietnamese **Kẻ**, the ordinary Tonkin prefix for a market town or settlement
(cf. *Kẻ Chợ* = Hanoi), so the name is "Kẻ + one syllable", a village/market
name. That does **not** locate it — hundreds of Tonkin settlements are named on
this pattern and the archive offers no candidate list.

Full research note: `notes/ke-diet-tonkin-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 133, **printed p. 42** | doc 65, p. 80, raw — `pha page 65 80` |
| WICKI, Josef. *Liste der Jesuiten-Indienfahrer 1541–1758* (1967) | no. 1917, **printed p. 329** | doc 66, p. 83, raw — `pha page 66 83` |
| DEHERGNE, Joseph. "Les chrétientés de Chine de la période Ming (1581–1650)", *Monumenta Serica* 16 (1957) | printed pp. 76, 82, 86 — 17th-c. Tonkin only, no residence list | doc 73, pp. 77, 83, 87, raw — `pha page 73 77` |
| ARSI *Lusitania* 17, f. 177 (register of the 1754 profession) | cited by Dehergne; **not in this archive** | — |
| [Q36485](https://www.wikidata.org/wiki/Q36485) | rejected candidate = Hưng Yên | — |
| [Q622778](https://www.wikidata.org/wiki/Q622778) | Tonkin, province-level anchor (already used in the source) | — |

**Note (PHA archive):** `notes/ke-diet-tonkin-identification.md`.

## Task

- [ ] Confirm the place and the Wikidata ID — **not identified**; no id can be
      added from this archive. Next step: read the register Dehergne cites,
      ARSI *Lusitania* 17, f. 177, and ARSI *Lusitania* 48, 264 (his entry),
      neither of which is held here.
- [x] Research note written: `notes/ke-diet-tonkin-identification.md`.


## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Vietnamese / Tonkin layer; the Vietnamese and French forms were queried
deliberately:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Kẻ Diet` | — | 0 | — |
| `Ké Diet` | — | 0 | — |
| `Ke Diet` | — | 0 | — |
| `Kẻ Diệt` (candidate reading) | — | 0 | — |

**Verdict: `outside-coverage`.** All four queries returned 0 hits. TGAZ cannot
contribute to the identification of the Tonkin vow place; the name remains
unidentified from the archive, as the issue concludes.
