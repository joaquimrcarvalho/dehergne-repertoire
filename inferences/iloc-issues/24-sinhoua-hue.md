# Place to identify

**Sinhoua, Hué** — `vows location (jesuita-votos-local)`, **1741-05-28** (`17410528`)

## Person(s)

**Johann Siebert** (`deh-johann-siebert`) — Padre · Boémia · Dehergne P. 766

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1708-05-28 | birth | Jihlava | Q183111 |
| 1739 | stay | Tonquim | — |
| 1739 | stay | Cochinchina | — |
| 1741-05-28 | vows location | **Sinhoua, Hué** | ❗️ **missing** |
| 1745-09-12 | death | Hué | Q36167 |

**Source note** (Dehergne):
> … Chine, 1737 (W 1842., JS 134, 434: «Germanus in via ad Sinas »)., envoyé au Tonkin, 1739, puis en Cochinchine: mathématicien du roi. V. « Sinoae » = Sinhoua, Hué, 28 mai 1741, pr. (Lus. 16, 26). M. 12 sept. 1745 à Hué (Streit VI n° 1612., HS 53, 317 l'ignore). Pf. 761., Koch (Vath)., WB nos 549, 539, 708, 711.

## Identification

**Conclusion.** **Identified as Huế → `Q36167`** (same place as the death entry,
which already carries that id). Dehergne equates the Latin vow form with the
vernacular and the city in the notice itself — « V. « Sinoae » = Sinhoua, Hué,
28 mai 1741, pr. (*Lus.* 16, 26) » (notice 766, printed p. 247 = PDF p. 285) —
and the identification is confirmed from three sides: Dehergne glosses "Sinoae"
as Hué elsewhere in the same volume (notice 407: « Sinoae Metropoli
Cochinchinae » = Hué, printed p. 127; notice 61: "Sinoa (Sin-Houa), ancien nom
de Hué?", printed p. 20); Pfister and Backer–Sommervogel both call Sinoa/Sinhoua
the capital of Cochinchina and give Siebert's letters from "Haubt-Lager Sinoa";
and Siebert himself died at Hué in 1745. Confidence **high**. The ARSI register
Dehergne cites (*Lus.* 16, 26) is not in this archive.

*Note on the quoted source text above:* the blockquote copied into this issue
file reads "WB nos 549, 539, 708, 711"; the printed page (doc 65, p. 285, read
as an image) has **"WB nos 549, 589, 708, 711"** — 589, not 539.

Source fix: `sources/dehergne-s.cli:1078` —
`ls$jesuita-votos-local/Sinhoua, Hué#ILOC/17410528` → add `@wikidata:Q36167`
and drop the `#ILOC` flag, e.g.
`ls$jesuita-votos-local/Sinhoua, Hué# @wikidata:Q36167/17410528`.

Full research note: `notes/sinhoua-hue-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 766, **printed p. 247** | doc 65, p. 285, raw (image-checked) — `pha page 65 285` |
| DEHERGNE, ibid. — supporting glosses | no. 61, p. 20; no. 210, p. 64; no. 407, p. 127; no. 579, p. 184 | doc 65, pp. 58, 102, 165, 222, raw — `pha page 65 58` |
| PFISTER, Louis. *Notices biographiques…*, t. 2 | printed p. 761 (Siebert at Hué, 1745); addenda p. 35* ("Sinoa, capitale de la Cochinchine", 1700) | doc 50, pp. 227, 629, raw — `pha page 50 227` |
| PFISTER, ibid., t. 1 | printed p. 412, no. 166 (Arnedo) — "Lettre de Sinoa, capitale de la Cochinchine", 1700 | doc 47, p. 451, raw — `pha page 47 451` |
| BACKER–SOMMERVOGEL. *Bibliothèque de la Compagnie de Jésus*, t. 7 | cols. 1189–1190 (Siebert: letters written "in dem Haubt-Lager Sinoa"; died at Hué) | doc 144, p. 603, raw — `pha page 144 603` |
| WICKI, Josef. *Liste der Jesuiten-Indienfahrer 1541–1758* (1967) | no. 1842, **printed p. 326** (1737 sendung für China) | doc 66, p. 80, raw — `pha page 66 80` |
| ARSI *Lusitania* 16, f. 26 (register of the 1741 vow) | cited by Dehergne; **not in this archive** | — |
| [Q36167](https://www.wikidata.org/wiki/Q36167) | Huế — the anchor | — |

**Note (PHA archive):** `notes/sinhoua-hue-identification.md`.

## Task

- [x] Confirm the place and the Wikidata ID — **identified as Huế `Q36167`**
      (Dehergne's own equation); the source `.cli` still needs the `@wikidata`
      comment (see *Identification*).
- [x] Research note written: `notes/sinhoua-hue-identification.md`.


## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ has no
Vietnamese layer; the Latin forms and the Chinese name 順化 were all queried:

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Hué` / `Hue` / `Huế` | — | 2 | `hvd_99230`/`hvd_99231` 湖耳蛮夷长官司 (Guizhou) |
| `Sinhoua` | — | 0 | — |
| `Sinoa` | — | 0 | — |
| `順化` / `顺化` | — | 4 | 順化郡, 順化堡 ×2, 順化軍節度使 — all Chinese |

**Result.** The `Hue` prefix hits are the Chinese *chang guan si* 湖耳蛮夷长官司
(Guizhou, 26.58 N 109.34 E, CHGIS) — the prefix-match homonym the protocol warns
about — not Huế. The `順化` hits are a Tang commandery (756–757, 36.01 N
107.88 E), two Gansu village records of 1820/1911 (順化堡, under 甘州府/張掖縣,
38.47 N 100.71 E) and a Later-Liang military prefecture (912–915, 37.62 N
117.55 E): Chinese homonyms, none anywhere near Huế (16.46 N, 107.58 E).

**Verdict: `outside-coverage`.** TGAZ has no layer covering Vietnam; its only
matches are unrelated Chinese homonyms. The identification as Huế `Q36167` is
Dehergne's own equation and is not affected by TGAZ.
