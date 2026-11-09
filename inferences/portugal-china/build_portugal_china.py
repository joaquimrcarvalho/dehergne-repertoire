"""Portuguese missionaries of the Dehergne Répertoire who are documented in China.

Reads the project SQLite database with timelink (no Kleio server needed) and the
Wikidata place->country cache (inferences/wikidata-references/locations_wikidata_info.xlsx),
keeps the 346 person records whose `nacionalidade` is Portugal, and decides for each
whether a *presence* place falls in China:

    presence types: estadia, chegada, partida, morte, jesuita-votos-local,
                    jesuita-ordenacao-padre, residencia, trajeto (+ -x variants)
    excluded types: jesuita-entrada, baptizado, jesuita-fundador (origin, not presence)

China = P17 in {PRC (includes Macau), Qing, Ming, Republic of China, Yuan}; place
values without a Wikidata id that are Chinese toponyms ("China", "Cantão", ...) are
resolved by name. Values in brackets ("[No mar, a caminho da China]") are deaths on
the voyage, not presence, and are never matched.

Output: inferences/portugal-china/portugal_china.xlsx
    china_residents  246 people with China evidence (id, name, places, dates)
    excluded         100 people with no China place + reason
    review           13 excluded whose biography hints at a possible China presence
    reasons, summary counts

Run from notebooks/ (so dehergne_util is importable):
    ~/venvs/timelink/bin/python ../inferences/portugal-china/build_portugal_china.py
"""
import sys, json, re, os
sys.path.insert(0, "/Users/jrc/develop/dehergne-repertoire-mbook-air/notebooks")
import pandas as pd
from dehergne_util import extract_wikidata_id, locations_wikidata_info_file
from timelink.api.database import TimelinkDatabase
from timelink.pandas import entities_with_attribute
from timelink.api.models import Person
from sqlalchemy import select

ROOT = "/Users/jrc/develop/dehergne-repertoire-mbook-air"
db = TimelinkDatabase(db_name="dehergne_repertoire_mbook_air", db_type="sqlite",
                      db_path=ROOT + "/database/sqlite")
BASE = ["estadia","chegada","partida","jesuita-entrada","jesuita-votos-local",
        "jesuita-ordenacao-padre","morte","residencia","baptizado","jesuita-fundador","trajeto"]
PA = BASE + [f"{t}-x" for t in BASE]
PRESENCE = [t for t in PA if not t.startswith(("jesuita-entrada","baptizado","jesuita-fundador"))]

nat = entities_with_attribute(the_type="nacionalidade", the_value="Portugal",
        entity_type="person", show_elements=["name","groupname"], db=db)
pt = nat[nat["groupname"]=="n"]
pt_ids = set(pt.index.astype(str))

places = entities_with_attribute(entity_type="person",
    show_elements=["name","groupname","the_line","the_order","extra_info"],
    the_type=PA, column_name="place", db=db)
places["person_id"] = places.index.astype(str)
ph = places["place"].isna() | (places["place"].astype(str).str.strip().isin(["","?","None"]))
places = places[~ph].copy()
sub = places[places["person_id"].isin(pt_ids)].copy()
def as_dict(v):
    if isinstance(v, dict): return v
    if isinstance(v, str) and v.strip().startswith("{"):
        try: return json.loads(v)
        except ValueError: return {}
    return {}
sub["place.extra_info"] = sub["place.extra_info"].apply(as_dict)
sub["wikidata_id"] = sub["place.extra_info"].apply(extract_wikidata_id, if_missing=pd.NA)
wd = pd.read_excel(ROOT + "/" + locations_wikidata_info_file.replace("../",""), dtype=str)
wd = wd.drop_duplicates("wikidata_id").set_index("wikidata_id")
sub = sub.join(wd[["country_label","english_label"]], on="wikidata_id", how="left")
CHINA_LABELS = {"People's Republic of China","Qing dynasty","Ming dynasty","Republic of China","Yuan dynasty"}

# Chinese toponyms for place values that carry no wikidata id (not inside brackets:
# "[No mar, a caminho da China]" is a death on the voyage, not a presence in China)
CN_NAMES = re.compile(r"(china|chine|cant[ãa]o|canton|macau|macao|pequim|p[ée]kin|peking|"
                      r"nankin|nanquim|nanquim|chekiang|kiang|shanghai|yangchow|hainan|"
                      r"fukien|fou-kien|tch[öo]-kiang|kan-tcheou|quemoy)", re.I)
def resolved_china(row):
    if pd.notna(row["country_label"]):
        return row["country_label"] in CHINA_LABELS
    v = str(row["place"]).strip()
    if v.startswith("["):
        return False
    return bool(CN_NAMES.search(v))
sub["in_china"] = sub.apply(resolved_china, axis=1)
sub["date"] = sub["place.date"].astype(str)
pres = sub[sub["place.type"].isin(PRESENCE)].copy()
china_ids = set(pres.loc[pres["in_china"], "person_id"])

# biographies + key data
def attr(p, t):
    return next((a for a in p.attributes if a.the_type == t), None)
records = {}
with db.session() as session:
    for pid in sorted(pt_ids):
        p = session.execute(select(Person).where(Person.id==pid)).scalars().first()
        g = lambda t: (attr(p,t).the_value if attr(p,t) else "")
        records[pid] = {
            "name": p.name,
            "obs": " ".join((str(attr(p,"dehergne").obs) if attr(p,"dehergne") else "").split()),
            "nascimento": g("nascimento"),
            "nascimento_date": (attr(p,"nascimento").the_date if attr(p,"nascimento") else ""),
            "jesuita_entrada": g("jesuita-entrada"),
            "entrada_date": (attr(p,"jesuita-entrada").the_date if attr(p,"jesuita-entrada") else ""),
            "embarque": g("embarque"),
            "embarque_date": (attr(p,"embarque").the_date if attr(p,"embarque") else ""),
        }

res, exc = [], []
for pid in sorted(pt_ids):
    d = pres[pres["person_id"] == pid]
    dd = d[d["in_china"]]
    r = records[pid]
    if len(dd):
        places_list = sorted(set(dd["place"].astype(str)))
        res.append({"id": pid, "name": r["name"],
            "nascimento": r["nascimento"], "nascimento_date": r["nascimento_date"],
            "jesuita_entrada": r["jesuita_entrada"], "entrada_date": r["entrada_date"],
            "embarque": r["embarque"], "embarque_date": r["embarque_date"],
            "n_china_attrs": len(dd),
            "china_places": " | ".join(places_list),
            "attr_types": ", ".join(sorted(set(dd["place.type"].astype(str)))),
            "first_date": dd["date"].min(), "last_date": dd["date"].max(),
            "macau_only": all(x.strip().lower() in ("macau","macao") for x in places_list),
            "evidence": "; ".join(f"{x['place.type']}:{x['place']}/{x['date']}"
                                  for _, x in dd.sort_values("date").iterrows()),
        })
    else:
        other = d
        countries = sorted(set(other["country_label"].dropna())) if len(other) else []
        morte = other[other["place.type"].str.startswith("morte")]
        mplace = "; ".join(str(x) for x in morte["place"]) if len(morte) else ""
        exc.append({"id": pid, "name": r["name"],
            "nascimento": r["nascimento"],
            "jesuita_entrada": r["jesuita_entrada"], "entrada_date": r["entrada_date"],
            "embarque": r["embarque"], "embarque_date": r["embarque_date"],
            "presence": "; ".join(f"{x['place.type']}:{x['place']}" for _, x in other.iterrows()) or "(none)",
            "countries": " | ".join(countries),
            "death_place": mplace,
            "obs": r["obs"]})

res_df = pd.DataFrame(res).sort_values("name")
exc_df = pd.DataFrame(exc).sort_values("name")

def reason(row):
    t = (row["obs"] or "").lower()
    death = (row["death_place"] or "").lower()
    if death.startswith("[") or "no mar" in death or "naufr" in death:
        return "died at sea / on the voyage (never reached China)"
    if re.search(r"(m\. en mer|mort en mer|m\. durant le voyage|m\. en route|m\. au cours du voyage|in via|naufrage|avant d'arriver)", t):
        return "died on the voyage (never reached China)"
    if re.search(r"(m\. à batavia|mort à batavia|batavia)", t) and "chine" in t:
        return "died in transit (Batavia), destined for China"
    if row["countries"] in ("India",) or row["countries"].startswith("India") or "goa" in row["presence"].lower():
        return "stayed in India/Goa, never went to China"
    if row["countries"] in ("Japan","Vietnam","Thailand","British Raj") or any(c in row["countries"] for c in ("Japan","Vietnam","Thailand","Malaysia")):
        return "mission elsewhere in Asia (Japan/Tonkin/Siam/Malacca)"
    if re.search(r"(1755-1758|1755 et 1758|1755- 1758)", row["obs"] or ""):
        return "embarked 1755-58 for China, deported/exiled to Italy before reaching"
    if re.search(r"(destin|pour la chine|à la chine|mission de chine)", t) and not row["countries"]:
        return "destined for China, no evidence of arrival"
    if row["countries"] and set(row["countries"].split(" | ")) <= {"Portugal","Italy","France","Spain"}:
        return "stayed in Europe, never sailed for China"
    if not row["countries"]:
        return "no place evidence (unknown)"
    return "other / review"

exc_df["reason"] = exc_df.apply(reason, axis=1)

outdir = ROOT + "/inferences/portugal-china"
os.makedirs(outdir, exist_ok=True)
with pd.ExcelWriter(outdir + "/portugal_china.xlsx") as w:
    res_df.to_excel(w, sheet_name="china_residents", index=False)
    exc_df.to_excel(w, sheet_name="excluded", index=False)
    pd.DataFrame({"metric": ["portuguese_n","residents_in_china","residents_macau_only",
                             "residents_with_mainland_place","excluded"],
                  "value": [len(pt_ids), len(res_df), int(res_df["macau_only"].sum()),
                            int((~res_df["macau_only"]).sum()), len(exc_df)]}
                ).to_excel(w, sheet_name="summary", index=False)
print("WRITTEN", outdir + "/portugal_china.xlsx")
print("Portuguese:", len(pt_ids), "| in China:", len(res_df), "| macau-only:", int(res_df['macau_only'].sum()),
      "| with mainland place:", int((~res_df['macau_only']).sum()), "| excluded:", len(exc_df))
print("\nexcluded reasons:")
print(exc_df["reason"].value_counts().to_string())
print("\n--- review candidates (reason contains review / other) ---")
print(exc_df[exc_df["reason"].str.contains("review|other")][["id","name","presence","countries","reason"]].to_string(index=False))

# ---- review sheet: excluded whose biography suggests a possible China presence ----
REVIEW = {
 "deh-francisco-rodrigues": "Dehergne: 'habitant sans doute Macao'; one of the two homonyms arrived at Macao 2 Feb 1730 and died there 9 Jul 1731, but the two cannot be distinguished and the record has no places.",
 "deh-manuel-carvalho-ii": "A P. Manuel Carvalho writes from Macao on 20 Dec 1700; Dehergne: 'Nous ignorons s'il a travaillé en Chine' — identification with this person uncertain.",
 "deh-joao-antonio-de-azevedo": "Alleged at Nanchang (Kiangsi) in 1692, but Dehergne suspects a confusion with J. A. Arnedo and notes he embarked 'pas pour la Chine'.",
 "deh-joao-da-fonseca-ii": "Pfister (882) 'le met en Chine'; possibly the João da Fonseca Campos who was a magistrate at Macao. No place recorded.",
 "deh-jose-montanha-i": "Signs the annuelle of Fou-kien and Kiang-si in 1660 — implies presence in China, but he is in none of the China catalogues and has no places.",
 "deh-joao-da-silva": "Goa catalogues of 1678 and 1681 call him 'envoyé en Chine'; described as lent from Goa to the Japan province (Macao). No place recorded.",
 "deh-jose-de-lima": "In 1767 an 'ancien missionnaire de Chine' in Italy; probably only attached to the China vice-province (embarked 1755-58, no arrival evidence).",
 "deh-manuel-da-fonseca": "Same 1767 formula: 'ancien missionnaire de Chine exilé en Italie'; embarked 1755-58, deported to Italy, no China place.",
 "deh-mauro-de-azevedo": "A catalogue 'le croit venu en Chine', but Dehergne reads 'Sineu' as Sinoa (Hué) and thinks he stayed in India.",
 "deh-manuel-cortese": "'macaïste' — born at Macao of Portuguese parents; his recorded mission presence is Goa.",
 "deh-antonio-dias": "'est dit missionnaire de Chine', but his recorded stays are Siam/Madurai/Goa; the rectorship of the Macao seminary belongs to a homonym.",
 "deh-francisco-nogueira": "Visitor of Japan and China 1691-1693, vicar general 'pour toute la Chine' in 1694, but his recorded stays are Goa, Malacca and Tonkin.",
 "deh-antonio-veloso": "Visitor of China and Japan (patent 1656), but he was in Cochin and died at sea in 1657.",
}
rev = exc_df[exc_df["id"].isin(REVIEW)].copy()
rev["review_note"] = rev["id"].map(REVIEW)
rev = rev.sort_values("name")
with pd.ExcelWriter(outdir + "/portugal_china.xlsx") as w:
    res_df.to_excel(w, sheet_name="china_residents", index=False)
    exc_df.to_excel(w, sheet_name="excluded", index=False)
    rev[["id","name","presence","countries","reason","review_note"]].to_excel(w, sheet_name="review", index=False)
    pd.DataFrame({"metric": ["portuguese_n","residents_in_china","residents_macau_only",
                             "residents_with_mainland_place","residents_single_attribute","excluded","excluded_flagged_for_review"],
                  "value": [len(pt_ids), len(res_df), int(res_df["macau_only"].sum()),
                            int((~res_df["macau_only"]).sum()), int((res_df["n_china_attrs"]==1).sum()),
                            len(exc_df), len(rev)]}
                ).to_excel(w, sheet_name="summary", index=False)
print("\nreview sheet rows:", len(rev))
print("single China attribute among residents:", int((res_df['n_china_attrs']==1).sum()))
