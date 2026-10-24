# Place to identify

**Sum Kiam (casa de um cristão)** — `vows location (jesuita-votos-local)`, **1732-08-03** (`17320803`)

## Person(s)

**Martim Correa** (`deh-martim-correa`) — Padre · Portugal · Chinese name: Ngan Ma-eul-ti-no · Dehergne P. 197

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | stay | Kiangnan | — |
| — | stay | Cham-xo | — |
| — | stay | Songkiang | — |
| — | stay | Chang-hai | — |
| — | stay | Wusih | — |
| 1699-11-11 | birth | Lisboa | Q597 |
| 1726 | arrival | China | Q148 |
| 1732-08-03 | vows location | **Sum Kiam (casa de um cristão)** | ❗️ **missing** |
| 1785 | stay | Kiangnan | Q11133842 |
| 1786 | death | Sungkiang fou, Kiangnan | Q11104671 |

**Source note** (Dehergne):
> …)., A. 1726 (JS 134, 435v)., Kiangnan: « Cham-xo, Songkiang, Chang-hai » puis « Ou-si », Wusih. En 1785, seul missionnaire au « Kiang-nan ». V. « Sum kiam, in domo privata cujusdam Xmi » (dans la maison d'un chrétien), 3 août 1732, coadj. spir. (Lus. 24, 133) (et non en 1730, comme le dit JS 134, 446, suivi par Pf.). M. au Sungkiang fou, Kiangnan, 1786. Pf. 703.

## Identification

**Conclusion.** Identified as **Sungkiang (Songjiang 松江), Kiangnan** →
`Q11104671` (Songjiang Fu 松江府; `Q662380`, Songjiang 松江區, if the project prefers
present-day units). The vow formula `« Sum kiam »` is the mission's own romanisation of
Sungkiang: Dehergne's 1957 gazetteer prints the name-form table "SUNGKIANG (Song-kiang)
松江 fou […] En dial. Songkaong […] *CoupC.*: **Sumkiam**", and Dehergne glosses the
identical formula **"(Sungkiang)"** in three separate notices (195, 280, 647). The
adjective *in domo privata cujusdam X^mi* ("in the private house of a certain Christian")
describes the **house**, not a different town. Note that `Kiam-nam` in the sibling formula
`« Sum Kiam, Kiam-nam »` is **Kiangnan 江南**, the mission/vice-province, not part of the
place name. Full research note: `notes/sum-kiam-identification.md`.

Source fix: `sources/dehergne-c.cli:2089` —
`ls$jesuita-votos-local/Sum Kiam (casa de um cristão)/17320803`
→ `ls$jesuita-votos-local/Sum Kiam (casa de um cristão)#@wikidata:Q11104671/17320803`
(the same file already links this man's `Songkiang` stay at line 2084 and his
`Sungkiang fou` death at line 2090 to `Q11104671`).

## Task

- [x] Confirm the place and the Wikidata ID — **identified as Sungkiang 松江,
      Kiangnan `Q11104671`**; the source `.cli` still needs the `@wikidata` comment
      (see *References*).
- [x] Research note written: `notes/sum-kiam-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 197 (Correa, Martim), **p. 61** | doc 65, p. 99, raw (image verified) — `pha page 65 99` |
| ibid. — the sibling formula `« Sum Kiam, Kiam-nam » … Sungkiang` | no. 195 (Correa Tcheou, José), **p. 61** | doc 65, p. 99 — `pha page 65 99` |
| ibid. — `V. « Sum kiam » (Sungkiang)` | no. 280 (Faglia, Antonio), **p. 85** | doc 65, p. 123 — `pha page 65 123` |
| ibid. — `V. 15 août 1723 Sum kiam … (Sungkiang)` | no. 647 (Pinto, Manuel), **p. 206** | doc 65, p. 244 — `pha page 65 244` |
| DEHERGNE, Joseph. "Les chrétientés de Chine de la période Ming (1581–1650)", *Monumenta Serica* 16 (1957) | entry 14 SUNGKIANG, **p. 59** — `CoupC.: Sumkiam` | doc 73, p. 60, raw (image verified) — `pha page 73 60` |

**Note (PHA archive):** `notes/sum-kiam-identification.md`.

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `松江` | — | 8 | `hvd_32439` 松江府 (府), 1328–1911 |
| `松江府` | year 1732 | 2 | `hvd_32439` 松江府 (府), 1328–1911 |
| `Songjiang` | — | 8 | `hvd_32439` 松江府 (府), 1328–1911 |
| `華亭` (the 附郭 county) | — | 22 | `hvd_40495` 华亭县 (县), 1278–1911 |

**Best match.** `hvd_32439` — 松江府 (Songjiang Fu), superior prefecture (府),
1328–1911; parent chain 浙江行省 → 江南行省 → 南京/京师 (南直隶) →
**江南省** (1645–1666) → **江蘇省** (1667–1911); 31.00948 N, 121.22764 E;
`present_location` "今上海市松江县". Canonical record:
<https://chgis.hudci.org/tgaz/placename/hvd_32439>. The 1732 year-filtered
query returns exactly this record, so TGAZ has the unit for the Dehergne year;
the 附郭 county 華亭縣 (`hvd_40495`, 1278–1911) is at the same point.

**Coordinates.** TGAZ 31.00948, 121.22764 vs Wikidata `Q11104671` (松江府)
31.00948, 121.10776 → **11.4 km**; vs `Q662380` (松江區) 31.00583, 121.23333 →
**0.7 km**. The TGAZ point is the historical Songjiang seat (present Songjiang
district), agreeing with both anchors (well under the 50 km threshold; the
`Q11104671` point sits ~11 km west of the seat).

**Verdict: `confirmed`.** TGAZ records 松江府 as the prefecture of 江南省/江蘇省
in the Dehergne period at the Songjiang seat — exactly the identification of
the Romanised vow formula *Sum Kiam* the issue gives (`Q11104671`). No change to
the issue's conclusion.
