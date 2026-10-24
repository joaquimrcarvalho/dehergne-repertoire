# Place to identify

**Zumbae, Tchamp-pa** — `stay (estadia)`, **1659** (`16590000`)

## Person(s)

**Germain Macret** (`deh-germain-macret`) — Padre · França · Chinese name: Fang Ma-no Yun-Tchong · Dehergne P. 502

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | stay | Timor | — |
| — | stay | Macau | — |
| — | stay | Hukwang | — |
| 1620-08-13 | birth | Bourg-en-Bresse | Q133069 |
| 1637 | stay | Foochow | Q68481 |
| 1637-09-03 | entered Jesuits | Avignon | Q6397 |
| 1654 | stay | Vannes | Q6593 |
| 1654-07-05 | vows location | Lyon (igreja de S. José) | Q456 |
| 1655-03-23 | stay | Lisboa | Q597 |
| 1659 | stay | **Zumbae, Tchamp-pa** | ❗️ **missing** |
| 1664-12-23 | stay | Kanchow (Kan-tcheou) fou, Kiangsi | Q363166 |
| 1666-03-25 | stay | Cantão | Q16572 |
| 1667 | stay | Macau | Q14773 |
| 1676-09-04 | death | Fou-tcheou fou | Q68481 |

**Source note** (Dehergne):
> … 1655 sur le gallion S. Francisco (W 1004)., Timor. Le catal. Japon 1659 dit qu'il a été recteur du Séminaire de Macao un an., « nunc est in missione Zumbae» (JS 25, 170v), au Tcham-pa (?). Le 23 déc. 1664, on le trouve à Kanchow (Kan-tcheou) fou, Kiangsi., puis Hukwang., Canton, 25 mars 1666., Macao, 1667 (JS 134, 352)., Foochow, 1673 (JS 25, 204v). -P. v. 1653. V. Lyon, église St Joseph, 5 juill. 1654, c. spir. (Gai. 8, 302). M. 4 sept. 1676, Fou-tcheou fou, « apud Sinas » (HS 49, 93v). Pf. 36…

## Identification

**Conclusion.** Identified as **Sumba** — Pfister's « l'île **Soumba** » — the
island of Sumba in the Lesser Sunda Islands (East Nusa Tenggara, Indonesia), in the
Timor-Macassar sphere → `Q206368`. Dehergne's « au Tcham-pa (?) » is **not
supported** by anything in the archive: Pfister notice 129 says Macret and P.
Saccano (the very companion Schütte's 1659-catalogue note names) set out for the
island *Soumba*, and Pfister's index files "Soumba (L'ile): le P. Macret, 368".
Schütte quotes the same catalogue phrase, « nunc in Missione Zumbae » (J. 25 169v,
for Saccano; Dehergne cites 170v for Macret — adjacent entries of one list).
Distinct from Sumbawa (`Q186367`), whose Portuguese form is *Sumbava*. Full
research note: `notes/zumbae-tchamp-pa-identification.md`.

Source fix: `sources/dehergne-m.cli:92` —
`ls$estadia/Zumbae, Tchamp-pa#?/16590000` → add the anchor and drop Dehergne's
conjecture, e.g.
`ls$estadia/Zumbae (Sumba), Indonésia#@wikidata:Q206368/16590000`
(minimal fix, keeping the text: `ls$estadia/Zumbae, Tchamp-pa#@wikidata:Q206368/16590000`).

## Task

- [x] Confirm the place and the Wikidata ID — **identified as Sumba (Soumba),
      Indonesia → `Q206368`**; Dehergne's « Tcham-pa (?) » is a wrong conjecture.
      The source `.cli` still needs the `@wikidata` comment and the corrected
      place text (see *Identification*).
- [x] Research note written: `notes/zumbae-tchamp-pa-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 502, **p. 160** | doc 65, p. 198, raw — `pha page 65 198` |
| PFISTER, Louis. *Notices biographiques…* t. 1 | notice 129, **p. 368** (« l'ile Soumba ») | doc 47, p. 407, raw — `pha page 47 407` |
| PFISTER, *Notices…* t. 2, *Table alphabétique* | **p. 1089** (« Soumba (L'ile): le P. Macret, 368 ») | doc 50, p. 555 — `pha page 50 555` |
| SCHÜTTE, J. F. *Monumenta historica Japoniae* I (Rome, 1975) | **p. 1042 n. 37** and **p. 1089** (« nunc in Missione Zumbae »: J. 25 169v) | doc 18, pp. 1090, 1137, edited — `pha page 18 1090` |
| ARSI *Japonica-Sinica* 25, ff. 169v-170v (the 1659 catalogue) | — | **not in the archive** |

**Note (PHA archive):** `notes/zumbae-tchamp-pa-identification.md`
(slug `zumbae-tchamp-pa-identification`). Wikidata:
[Q206368](https://www.wikidata.org/wiki/Q206368) (checked 2026-10-15).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Indonesian layer; the Latin forms and the Chinese name 松巴 were queried:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Zumbae` | — | 0 | — |
| `Sumba` | — | 0 | — |
| `Sumbawa` | — | 0 | — |
| `松巴` | — | 1 | `TBRC_G1KR1946` sum pa ri khrod (Tibetan monastery) |

**Result.** The single 松巴 hit is a TBRC Tibetan monastery (`sum pa ri khrod`,
1750–9999, 34.66 N 103.12 E, Gansu/Qinghai) — a homonym unrelated to the island
of Sumba (−9.73 N, 120.00 E).

**Verdict: `outside-coverage`.** TGAZ has no layer covering Indonesia; the single
match is unrelated. TGAZ cannot confirm or reject the identification as Sumba
`Q206368`; the issue's identification stands on the archive evidence alone.
