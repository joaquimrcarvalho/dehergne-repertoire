# Place to identify

**Czerczerse** — `death (morte)`, **1794-04-21** (`17940421`)

## Person(s)

**Agostino Magnani** (`deh-magnani-ref1`) — Padre · Itália · **referido** (person referenced, not the missionary) · Dehergne P. 508-ref1

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| — | birth | Bolonha | Q1891 |
| 1746-08-28 | stay | Rússia Branca | Q184 |
| 1794-04-21 | death | **Czerczerse** | ❗️ **missing** |

**Source note** (Dehergne):
> Deux frères de ce nom en Russie Blanche, Agostino (28 août 1746 -E. 12 oct. 1762 et M. à Czerczerse 21 avril 1794) (...) Tous les deux N. à Bologne et tous deux prêtres.

## Identification

**Conclusion.** Probably **Czeczersk — Chachersk (Чачэрск / Чэчэрск)**, on the river
Sozh in the Rahačoŭ (Rogachev) district, today the Homiel region of Belarus →
`Q867722`. The archive's three witnesses are: Backer–Sommervogel, which prints the
same death as "**Czeczerse**" and uses "**Czeczersk (Russie Blanche)**" for the town
(t. 5, col. 315; t. 8, col. 1442); Załęski's history of the Polish province, which
gives the Jesuits a **domicilium at Czeczersk** from 1754 until 1820; and the
*Słownik geograficzny Królestwa Polskiego*, t. I, p. 782 ("**Jezuici mieli tu
kościół i domicilium**"). **Confidence: medium-high — probable, not certain**:
Dehergne's "Czerczerse" and Backer–Sommervogel's "Czeczerse" are one letter apart
from each other and neither is exactly "Czeczersk", and the ARSI Polotsk registers
that would settle it are not in this archive. Full research note:
`notes/czerczerse-identification.md`.

Source fix: `sources/dehergne-m.cli:345` —
`ls$morte/Czerczerse#ILOC/17940421` → `ls$morte/Czeczersk (Chachersk), Rússia
Branca# @wikidata:Q867722/17940421` (proposed; `#ILOC` to be dropped only if the
coordinator accepts the probable identification).

## Task

- [x] Confirm the place and the Wikidata ID — **probably Czeczersk / Chachersk
      `Q867722`** (medium-high confidence); the source `.cli` still needs the
      `@wikidata` comment (see *Source fix* above and *References*).
- [x] Research note written: `notes/czerczerse-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 508, **p. 162** | doc 65, p. 200, raw — `pha page 65 200` (page image: `renders/dd9040…/p200.jpg`); bibliography s.v. OTTO, doc 65, p. 30 |
| BACKER, Augustin de; SOMMERVOGEL, Carlos. *Bibliothèque de la Compagnie de Jésus*, t. 5 | **col. 315** ("mourut à Czeczerse, le 21 avril 1794") | doc 142, p. 166, raw — `pha page 142 166` (page image: `renders/7c2124b8…/p166.jpg`) |
| Ibid., t. 8 | **col. 1442** ("né Czeczersk (Russie Blanche)") | doc 145, p. 729, raw — `pha page 145 729` |
| *Słownik geograficzny Królestwa Polskiego…*, t. I (1880), s.v. "Czeczersk" | **p. 782** | not in the archive (Wikisource full text) |
| ZAŁĘSKI, Stanisław. *Jezuici w Polsce*, t. V, cz. 1, § 39 | **pp. 363, 369** | not in the archive (Internet Archive `cz1jezuiciwpol05zals`) |

**Note (PHA archive):** `notes/czerczerse-identification.md` in the PHA archive notes folder (`/Users/jrc/jesuit-archive/notes/`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ is not
China-only: its **HGR** layer is the Historical Gazetteer of the Russian Empire,
1785–1796, so the place was searched there (Latin, Polish, Belarusian and
Russian forms).

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Чечерск` | — | 1 | `hgr_619` Чечерск (местечко) |
| `Chechersk` | — | 1 | `hgr_619` |
| `Czeczersk` | — | 0 | — |
| `Czerczerse` | — | 0 | — |
| `Чечерск` | year 1794 | 1 | `hgr_619` |
| `Chachersk` | year 1794 | 0 | — |
| `Rogachev` | — | 2 | `hgr_399` Рогачев (город), `hgr_141` Рогачевский уезд |

**Best match.** `hgr_619` — Чечерск / Chechersk, a *mestechko* (местечко, "town")
in the HGR layer, **1785–1796**, parent **Рогачевский уезд** (Rogachevskii uezd,
`hgr_141`); 52.9164 N, 30.9179 E; `present_location` "Čačersk, Homiel Province,
Belarus". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hgr_619>. The Russian source note
reads "ЧЕЧЕРСКЪ, мѣстечко Могилевскаго Намѣстничества въ уѣздѣ города Рогачева" —
a small town of **Mogilev namestnichestvo** in **Rogachev uezd**, exactly the
Rahačoŭ district / Homiel region of the issue.

**Coordinates.** TGAZ 52.9164, 30.9179 vs Wikidata `Q867722` 52.91667, 30.91667 →
**0.09 km** (the same town).

**Verdict: `confirmed`.** TGAZ independently records Chachersk as a small town of
Rogachev uezd, Mogilev namestnichestvo — the parent unit and region the issue
assigns; the HGR span (1785–1796) contains the 1794 death. TGAZ spells it
Чечерск/Chechersk, not Dehergne's "Czerczerse" / Backer–Sommervogel's
"Czeczersk", so it confirms the place but cannot adjudicate the one-letter
variant in the transcription; the identification is otherwise unchanged. (The
`--year` facet dropped the Latin-spelling record while keeping the Cyrillic one;
the unfiltered query is the reliable one, as the protocol warns.)
