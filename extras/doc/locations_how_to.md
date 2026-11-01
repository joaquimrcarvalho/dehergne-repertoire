# Technical Note: identifying place names

> Project Linking the West and the East: Reconstructing Itineraries and Networks between Europe and China through Macao" supported by Macao Polytechnic University, project RP/CIPFIC－01/2023

This note defines the rules for registering place names in the sources.

## Attributes that are place names

A certain number of attributes of
people in the sources are place names.

* baptizado (place of baptism)
* chegada (place of arrival)
* estadia (place of stay)
* jesuita-entrada (place of entry into the Jesuit order)
* jesuita-ordenacao-padre (place of ordination as a jesuit priest)
* jesuita-votos-local (place of taking vows as a jesuit)
* morte (place of death)
* nascimento (place of birth)
* partida (departed to)
* residência (place of residence)
* residencia-missão (place of residence in a mission)

## General rules

Several attributes involve the recording of locations. It is convenient to have some form of standardisation in the format of registration, especially when the place is referred to with some regional or national context.

If the source gives some geographic context use commas to separate different levels in place names, similarly to what is used modernly in postal addresses, ordering from particular to general. For example:

    ls$estadia/Navalafuente, diocese de Toledo

    ls$morte/Tusculum, Itália

In other cases the source may include more specific location information, using an expression of proximity or referring to a specific building. In that case we add the specificiation in parentheses. For example:

    ls$estadia/Macau (Colégio de S. Paulo)

The goal should be to make alphabetical lists of places keep variations of the same place close together and not separate entries in such a way that it is difficult to see all the variants of the same geographic name. So "Macau (Colégio de S. Paulo)" should be listed close to "Macau" and not under "C" for "Colégio de S. Paulo de Macau".

## Identifying place names

To provide an unambiguos reference to a place we use linked data identifiers. The identifiers are URIs that can be used to retrieve information about the place from the web.

The preferred source of identifiers is
Wikidata. Information on place names in Wikidata includes geographic coordinates, alternate names in different languages, administrative context, and links to other sources of information about the place, such as library catalogs.

The Wikidata identifier is a URI that can be used to retrieve information about the place from the web. For example, the URI for Macau is [https://www.wikidata.org/wiki/Q14773](https://www.wikidata.org/wiki/Q14773). The identifier is the part of the URI after the last slash, `Q14773`.

To identify a place in the sources we use the Wikidata identifier after the place name, as a comment. Comments are introduced with the cardonal sign(#) For example:

    ls$estadia/macau#@wikidata:Q14773

If there was a previous comment on the entry the new comment is added after a space. For example:

      ls$morte/Changchow, China#no rio, a caminho do Japão @wikidata:Q57970/16110000

If the identifier is not available in Wikidata, or there
ambiguity in the identification, add a comment with the word ILOC. For example:

    ls$estadia/Changchow, China#ILOC

## How to deal with missing wikidata ids

Sometimes the place name can be located (we know which town, village or
district it is) but there is no suitable Wikidata item for it. In that case:

* **do not invent a Wikidata id**, and do not attach the id of a nearby or
  homonymous place merely to fill the field;
* keep the place name (and `#ILOC` if the identification is still ambiguous),
  and record the best available location evidence in the comment;
* try **TGAZ** first for Chinese places, and **coordinates from an independent
  source** (OpenStreetMap/Nominatim or GeoNames) when TGAZ has no record or the
  place is outside China.

### 1. Try TGAZ (CHGIS Temporal Gazetteer)

TGAZ is the CHGIS gazetteer of historical Chinese places. Unlike Wikidata,
which usually describes the modern place, TGAZ records the historical name,
feature type (`府`, `县`, `村镇`, …), administrative parent and period, with
coordinates. It is the best first check for a Chinese place that has no
Wikidata item.

**For humans, through the web interface:**

1. Open [https://chgis.hudci.org/tgaz](https://chgis.hudci.org/tgaz).
2. Search with the **Chinese characters** or **pinyin**, never with the
   European spelling of the source ("Ou-yuen" finds nothing; use `婺源` or
   `Wuyuan`).
3. Read all records returned: the same place normally appears several times
   under different periods and administrative levels.
4. Choose the record whose **period** and **feature type/parent** fit the
   event in the source (a 1644 village is not the 1911 district seat). Note:
   CHGIS has village (`村镇`) records only for the **1820** and **1911**
   layers; many 17th–18th-century villages therefore have no record at all.
5. Note the TGAZ id (`hvd_…`) and coordinates, and use them as the location
   evidence in the comment. If the TGAZ record corresponds to a Wikidata item,
   prefer that item; if there is no Wikidata item, keep the coordinates and
   the TGAZ id in the comment instead of a `@wikidata` id.

TGAZ covers **China (222 BC–1911)**, plus separate HGR (Russian Empire) and
TBRC (Tibet) layers. It does **not** cover Japan, Korea, Vietnam, the
Philippines or Europe: for those places go directly to step 2.

**In this project, through the notebook:**

The project has a TGAZ client and a demonstration/cross-check notebook:

* `notebooks/chgis-tgaz.ipynb` — cells 3–5 show how to search by name and
  read the multiple temporal records; cell 19 explains the cross-check of
  TGAZ coordinates against Wikidata; the long code cell (cell 24) runs the
  cross-check and writes
  `inferences/wikidata-references/wikidata_chgis_matches.xlsx`.
  Read the markdown cells before running it: the notebook queries the live
  TGAZ service and the Wikidata API.
* The helper functions are in `notebooks/dehergne_util.py`:
  `tgaz_query`, `tgaz_get`, `tgaz_results_to_records`, and `haversine_km`
  (great-circle distance in km). They can be imported in any notebook in
  `notebooks/`.
* For a single place from the shell, the project also has
  `inferences/iloc-issues/tgaz/tgaz_tool.py`:

  python3 inferences/iloc-issues/tgaz/tgaz_tool.py query 孟家溪
  python3 inferences/iloc-issues/tgaz/tgaz_tool.py get hvd_128475 --full

When comparing a TGAZ point with a candidate Wikidata item, compute the
distance with `haversine_km`. A distance of tens of kilometres is a warning
that the two are different places; a few kilometres is supporting evidence,
not proof.

### 2. Use coordinates from an independent source

If TGAZ has no record (or the place is outside its coverage), obtain the
coordinates from a source that can be cited, such as:

* **OpenStreetMap / Nominatim** — search the modern place name, or use the
  coordinates shown for a settlement in the OSM interface;
* **GeoNames** — search and take the decimal latitude/longitude of the
  settlement, not of the administrative district centroid.

Put the coordinates in the **comment** on the location line, in a format the
project's parser recognises. The recommended form is:

    ls$estadia/Some place, Context#coordinates: 31.79946N, 120.75405E

The parser in `notebooks/dehergne_util.py` (`extract_coordinates`, line 202)
also accepts:

* `latitude: <decimal>, longitude: <decimal>`
* signed decimal degrees: `<+/-decimal>, <+/-decimal>`
* DMS: `<deg>°<min>'<sec>"<N/S> <deg>°<min>'<sec>"<E/W>`

The residences notebook (`notebooks/residences.ipynb`, cells 16 and 31) reads
these comment coordinates into the `latitude`/`longitude` columns when no
Wikidata coordinate exists, so the place still appears on the maps.

Always add the source and access date to the comment, e.g.:

    ls$estadia/Some place, Context#coordinates: 31.79946N, 120.75405E (OSM/Nominatim, 2026-10-31)

Only add `@wikidata:Q…` when a Wikidata item genuinely represents the place;
coordinates are location evidence, not an identifier. If the identification
is still uncertain, keep `#ILOC` as well.
