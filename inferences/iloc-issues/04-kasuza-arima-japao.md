# Place to identify

**Kasuza, Arima, Japão** — `death (morte)`, **1590-05-25** (`15900525`)

## Person(s)

**Gaspar Coelho** (`deh-gaspar-coelho`) — Padre · Portugal · Dehergne P. 186

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1531 | birth | Porto | Q36433 |
| 1556-03 | entered Jesuits | Goa | Q1171 |
| 1571 | departure | Japão | Q17 |
| 1572 | arrival | Japão | Q17 |
| 1587-07-24 | stay | Japão | Q17 |
| 1590-05-25 | death | **Kasuza, Arima, Japão** | ❗️ **missing** |

**Source note** (Dehergne):
> …ilé avec tous les jésuites du Japon, au nombre de 66, par Hideyoshi. P. 1560 (DI. IV. 704). -V. pr. des 3 V. en 1571 (Goa 24, 146v). M. 25 mai 1590 à Kasuza, Arima, Japon (D'Elia I, 231 n. 2). M. le 7 mai (Schutte, 333). DHGE (A. De Bil). Laures, Johannes, An ancient document on the early intercourses between Japan and the Philippine Islands, Cuttura Social 29 (Manille 1941)., Schurhammer et Voretzsch, Die Geschichte Japans 1549-1578 von P. Luis Froes, Leipzig, 1926., SchOtte, 900-901. Il envoie…

## Identification

**Conclusion.** Identified as **Kazusa 加津佐**, the Jesuit town of the Arima domain
on the Shimabara peninsula (Hizen; today Minamishimabara, Nagasaki) →
`Q6381698`. Dehergne's « Kasuza » is the same place the archive's Schütte volume
calls *Katsusa*, *Canzusa* and *Cazzuça*, and which it places inside the Arima
house ("in Domo Arimensi … in Canzusaensi quatuor"; college and seminary of Arima
moved to Canzusa in 1590). **Do not use Q1055394 (Kazusa Province, 上総, Chiba)** —
most "Kazusa" hits in the Japan collections are that province. Full research note:
`notes/kasuza-arima-identification.md`.

Source fix: `sources/dehergne-c.cli:1780` —
`ls$morte/Kasuza, Arima, Japão#ILOC/15900525#ou 15900507?`
→ add `@wikidata:Q6381698`, e.g.
`ls$morte/Kasuza, Arima, Japão#@wikidata:Q6381698/15900525#ou 15900507?`.

Note on Dehergne's citation: his « Schutte, 333 » is **not** the *Monumenta
historica Japoniae* volume held here (doc 18); his own bibliography (doc 65, p. 32)
defines `SCHÜTTE` as the *Introductio ad Historiam Societatis Jesu in Japonia*
(Rome, 1968), which is not in the archive. The archive's Schütte gives the same
death date elsewhere: printed p. 404 n. 89, « die 7. Maji 1590 in oppido Katsusa
(Takaku) ».

## Task

- [x] Confirm the place and the Wikidata ID — **identified as Kazusa 加津佐,
      Arima, Japan → `Q6381698`**; the source `.cli` still needs the `@wikidata`
      comment (see *Identification*).
- [x] Research note written: `notes/kasuza-arima-identification.md`.
- [ ] Optional residual: reconcile the 25 May (D'Elia I, 231 n. 2) and 7 May
      (Schütte) death dates — both authorities are outside this archive.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 186, **p. 58** | doc 65, p. 96, raw — `pha page 65 96` |
| DEHERGNE, *Répertoire*, bibliography (`SCHÜTTE` = *Introductio*, 1968) | **p. XXX** | doc 65, p. 32, raw — `pha page 65 32` |
| SCHÜTTE, J. F. *Monumenta historica Japoniae* I (Rome, 1975) | Doc. 31 A, **p. 404 n. 89**; **p. 405** | doc 18, pp. 442, 443 — `pha page 18 442` |
| SCHÜTTE, *Monumenta historica Japoniae* I | Doc. 29 D, **p. 326**; Doc. 27 A, **p. 229**; Cat. Br. 1589, **p. 272**; index, **p. 1156** | doc 18, pp. 364, 265, 308, 1204 |
| D'ELIA, *Fonti Ricciane* I, 231 n. 2 (Dehergne's 25 May) | — | **not in the archive** |

**Note (PHA archive):** `notes/kasuza-arima-identification.md`
(slug `kasuza-arima-identification`). Wikidata: [Q6381698](https://www.wikidata.org/wiki/Q6381698)
(checked 2026-10-15).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Japanese layer (CHGIS covers China, HGR the Russian Empire, TBRC Tibet), but the
place was queried deliberately in both romanised and Japanese-character forms:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Kazusa` | — | 0 | — |
| `Kasuza` | — | 0 | — |
| `加津佐` | — | 0 | — |
| `Arima` | — | 0 | — |
| `有馬` / `有马` | — | 0 | — |

**Verdict: `outside-coverage`.** All six queries returned 0 hits. TGAZ has no
layer for Japan, so it can neither confirm nor reject the identification as
Kazusa 加津佐, Arima (`Q6381698`, 32.6313 N, 130.1593 E); the issue's
identification stands on the archive evidence alone.
