# Place to identify

**Mscislaviae** — `death (morte)`, **1798-02-08** (`17980208`)

## Person(s)

**Manswet Skokowvski** (`deh-manswet-skokowski`) — Padre · Polónia · Dehergne P. 791

### Places in the biography (chronological)

| Date | Event | Place | Wikidata |
|------|-------|-------|----------|
| 1751-02-20 | birth | Polónia | Q36 |
| 1770-08-13 | entered Jesuits | Mazowsze (província) | Q643843 |
| 1787-08-15 | vows location | Polotsk | Q200797 |
| 1792-05-08 | departure | China | Q148 |
| 1798-02-08 | death | **Mscislaviae** | ❗️ **missing** |

**Source note** (Dehergne):
> …ter secours aux missionnaires de Chine. Le voyage avorta. V. 15 août 1787 « veteris styli, Polociae » (Polotsk), pr. (Pol. 91, 97). M. 8 févr. 1798 « Mscislaviae » (= ? ). Otto, 67. Nous n'avons pas trouvé son nom aux catal. de 1771 (Pol. Maj., Pol. min., Lithuanie et Rome)

## Identification

**Conclusion.** Identified as **Mscislaŭ** (Belarusian Мсціслаў, Polish Mścisław,
Russian Мстиславль), Mahilioŭ region, Belarus → `Q744167`. "Mscislaviae" is the
Latin locative of *Mscislavia*; Backer–Sommervogel uses "**Mscislav**" for the town
and "*Mscislaviensis*" as its Latin adjective, and names **Mohilev, Orsza and
Mscislav** as houses of the Society in White Russia (t. 5, col. 1156; t. 4,
col. 160; t. 9, col. 49). Załęski's history of the Polish province has a
**Jesuit college at Mścisław** (residence from 1772, college from 1779, 10-12 men,
until 1820), so Skokowski's death there on 8 Feb. 1798 is exactly what the
province's geography predicts. **Confidence: high** for the place. Dehergne's own
"(= ? )" is thus answered; his sources for the man — ARSI ***Pol*. 91, 97** and
**Otto, p. 67** — are **not held in this archive** (it holds no Polish or Russian
province registers). Full research note: `notes/mscislaviae-identification.md`.

Source fix: `sources/dehergne-s.cli:1750` —
`ls$morte/Mscislaviae#? ILOC/17980208` →
`ls$morte/Mscislau (Mścisław), Bielorrússia# @wikidata:Q744167/17980208`.

## Task

- [x] Confirm the place and the Wikidata ID — **Mscislaŭ / Mścisław `Q744167`**; the
      source `.cli` still needs the `@wikidata` comment (see *Source fix* above and
      *References*).
- [x] Research note written: `notes/mscislaviae-identification.md`.

## References

| Work | Locator | Archive |
|---|---|---|
| DEHERGNE, Joseph. *Répertoire des Jésuites de Chine de 1552 à 1800* (Rome/Paris, 1973) | no. 791, **p. 254** | doc 65, p. 292, raw — `pha page 65 292`; index of names, doc 65, p. 468 |
| BACKER, Augustin de; SOMMERVOGEL, Carlos. *Bibliothèque de la Compagnie de Jésus*, t. 4 | **col. 160** ("dans le Palatinat de Mscislav") | doc 141, p. 88, raw — `pha page 141 88` |
| Ibid., t. 5 | **col. 1156** ("Societate Jesu Mohiloviensi, Orsensi et Mscislav") | doc 142, p. 586, raw — `pha page 142 586` |
| Ibid., t. 9 | **col. 49** ("Terrestris Palatin. Mscislav.") | doc 146, p. 33, raw — `pha page 146 33` |
| ZAŁĘSKI, Stanisław. *Jezuici w Polsce*, t. V, cz. 1, § 40 | **p. 371** | not in the archive (Internet Archive `cz1jezuiciwpol05zals`) |
| ARSI *Pol*. 91, 97; OTTO, *Gründung der Neuen Jesuitenmission…* (1939), p. 67 | cited by Dehergne, notice 791 | **not held in this archive** |

**Note (PHA archive):** `notes/mscislaviae-identification.md` in the PHA archive notes folder (`/Users/jrc/jesuit-archive/notes/`).

## TGAZ (CHGIS) check

Checked 2026-10-22 with `tgaz/tgaz_tool.py` against the
[CHGIS Temporal Gazetteer](https://chgis.hudci.org/tgw/#usage). TGAZ carries the
**HGR** layer (Historical Gazetteer of the Russian Empire, 1785–1796), which was
searched for the place.

| Query | Filters | Hits | Best hit |
|---|---|---|---|
| `Mstislavl` | — | 1 | `hgr_390` Мстиславль (город) |
| `Мстиславль` | — | 1 | `hgr_390` |
| `Mstislav` | — | 2 | `hgr_390`, `hgr_128` Мстиславский уезд |
| `Mscislaviae` | — | 0 | — |
| `Mscislaw` | — | 0 | — |
| `Mstislavl` | year 1798 | 0 | — |
| `Мстиславль` | year 1798 | 0 | — |

**Best match.** `hgr_390` — Мстиславль / Mstislavl', a *gorod* (город, "town") in
the HGR layer, **1785–1796**, parent **Мстиславский уезд** (Mstislavskii uezd,
`hgr_128`), itself under Могилевское Наместничество; 54.0185 N, 31.7217 E;
`present_location` "Mstsislaw, Mogilev Province, Belarus". Canonical record:
<https://chgis.hudci.org/tgaz/placename/json/hgr_390>. The source note reads
"МСТИСЛАВЛЬ, городъ Могилевскаго Намѣстничества".

**Coordinates.** TGAZ 54.0185, 31.7217 vs Wikidata `Q744167` 54.0196, 31.7247 →
**0.23 km** (the same town).

**Verdict: `confirmed`.** TGAZ independently records Mscislaŭ / Mścisław as a town
of Mstislavskii uezd in the Mogilev namestnichestvo — the Belarusian town and
region the issue proposes. The HGR span is 1785–1796, so the 1798 death falls just
outside it and the `--year 1798` queries return nothing while the unfiltered ones
return the record; the place's existence and parentage are unaffected. TGAZ
carries only the Russian spelling (Мстиславль / Mstislavl'); the Latin
"Mscislaviae" and the Belarusian "Мсціслаў" are absent. No change to the issue's
conclusion.
