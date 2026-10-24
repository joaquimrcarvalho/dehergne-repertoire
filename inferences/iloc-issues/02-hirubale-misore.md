# Place to identify

**Hirubale, Misore** — `vows location (jesuita-votos-local)`, **1675-08-15** (`16750815`)
- Original transcription: « Kubale (Hirubale?, le mot est peu lisible), in Regno Maiçurensi » (Mysore)

## Person(s)

**Emanuel Rodriguez** (`deh-manuel-rodrigues-ii-ref4`) — **referido** (person referenced, not the missionary) · Dehergne P. 710-ref4

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1675-08-15 | vows location | **Hirubale, Misore** | ❗️ **missing** |

**Source note** (Dehergne):
> Par contre, nous avons vu celles [fórmulas de votos] de deux homonymes: l'une, signée à « Kubale (Hirubale?, le mot est peu lisible), in Regno Maiçurensi » (Mysore), 15 août 1675, Em. Rodriguez, et il signe Roiz (!) (Lus. 9, 190).

## Identification

**Conclusion.** **Not identified.** The town cannot be resolved from the archive:
the only witness is the barely legible vow formula in ARSI *Lusitania* 9, f. 190
(which the archive does not hold), and no archive source mentions *Kubale* or
*Hirubale*. The one certain element is the kingdom, stated in the formula itself —
"in Regno Maiçurensi" = the **Kingdom of Mysore** (`Q266923`) — but that is a
kingdom-level, not a place-level, anchor. The archive's Documenta Indica stops in
1597, eighty years before the 1675 vow, and its only near-match, **Hubli**, appears
in a 1577 editor's footnote (printed p. 940) as a stage on the São Tomé–Bellary–Goa
route, not in Mysore. **Recommendation: keep the `#ILOC` marker and do not add a
`@wikidata` comment for the town**; if a fallback anchor is required, use the
kingdom with a comment saying the town is unread. Full research note:
`notes/hirubale-misore-identification.md`.

There is no source fix to make yet. `sources/dehergne-r.cli:1437` —
`ls$jesuita-votos-local/Hirubale, Misore%« Kubale (Hirubale?, le mot est peu lisible), in Regno Maiçurensi » (Mysore)#ILOC/16750815`
— stays as it is (the `%` note already preserves Dehergne's doubt) until ARSI
*Lus.* 9, f. 190 is read.

## Task

- [ ] Confirm the Wikidata ID for **Hirubale, Misore** — **not possible from this
      archive**; only the kingdom (Mysore, `Q266923`) is certain. Next step: read
      **ARSI *Lusitania* 9, f. 190** (the vow formula) to decide between *Kubale*
      and *Hirubale*; ARSI registers are not held here.
- [x] Research note written: `notes/hirubale-misore-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 710, **p. 229** | doc 65, p. 267, raw — `pha page 65 267` |
| DEHERGNE, *Répertoire*, abbreviation table (`Lus.` = ARSI Lusitania) | **p. XXXIV** | doc 65, p. 36, raw — `pha page 65 36` |
| PFISTER, Louis. *Notices biographiques…* t. 1 | notice 160, **p. 399** (« Mission du Maïssour ») | doc 47, p. 438, raw — `pha page 47 438` |
| WICKI, J. (ed.). *Documenta Indica*, vol. 1575-1577 | doc. 79, **p. 940 n. 4** (« Bellary et Hubli ») | doc 81, p. 1010, raw — `pha page 81 1010` |
| ARSI *Lusitania* 9, f. 190 (the vow formula) | — | **not in the archive** |

**Note (PHA archive):** `notes/hirubale-misore-identification.md`
(slug `hirubale-misore-identification`). Kingdom anchor, if wanted:
[Q266923](https://www.wikidata.org/wiki/Q266923) (checked 2026-10-15).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Indian layer; both readings of the illegible word and the kingdom were queried
deliberately:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Hirubale` | — | 0 | — |
| `Kubale` | — | 0 | — |
| `Hubli` (the archive's near-match) | — | 0 | — |
| `Mysore` | — | 0 | — |
| `Misore` | — | 0 | — |

**Verdict: `outside-coverage`.** All five queries returned 0 hits. TGAZ has no
layer covering India and so cannot help decide between *Kubale* and *Hirubale*;
the town remains unidentified, with only the kingdom anchor `Q266923` (12.3 N,
76.65 E) certain.
