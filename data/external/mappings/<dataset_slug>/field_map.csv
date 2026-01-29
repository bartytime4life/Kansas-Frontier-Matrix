# 🧭 External Dataset Field Map (`field_map.csv`)

> 🧩 **Purpose:** This CSV is the **contract** for mapping an external dataset’s raw fields into KFM’s normalized, processed schema during the **ETL + normalization** stage (Raw → ETL → catalogs/provenance → graph → API → UI).:contentReference[oaicite:0]{index=0}

---

## 📁 File placement

Create this file at:

```
data/external/mappings/<dataset_slug>/field_map.csv
```

This follows the repo expectation that each domain has a dedicated folder with `raw/`, `work/`, `processed/`, and `mappings/` sections.:contentReference[oaicite:1]{index=1}

---

## 🧾 Design rules (KFM-aligned)

- ✅ **Deterministic + reproducible:** The mapping is config-driven and should yield the same outputs given the same inputs.:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}
- 🔒 **Governance-aware:** New external sources can trigger governance review (e.g., copyright/license), so we include license/provenance hooks in the mapping template.:contentReference[oaicite:4]{index=4}

---

## 🧩 CSV contract (v1)

| Column | Required | Meaning |
|---|---:|---|
| `source_field` | ✅ | Exact column name from the raw dataset. Use `__derived__` for computed fields. |
| `target_field` | ✅ | Canonical normalized field name (output column). |
| `target_type` | ✅ | One of: `string`, `int`, `float`, `bool`, `date`, `datetime`, `geometry`, `json`. |
| `transform` | ➖ | Deterministic transform chain (see cheat sheet below). |
| `required` | ✅ | `true`/`false` — used for validation. |
| `default` | ➖ | Default value if missing (leave blank for none). |
| `sensitivity` | ✅ | `public` / `restricted` / `confidential` (policy hook). |
| `description` | ➖ | Human-readable meaning of the field. |

---

<details>
<summary>🔁 Transform DSL cheat sheet (suggested)</summary>

Use a simple **pipe** chain (left → right):

- `trim` → strip whitespace  
- `lower` / `upper` → normalize casing  
- `null_if_empty` → empty string → null  
- `parse_int` / `parse_float` → numeric parsing  
- `parse_date(%Y-%m-%d)` → parse date strings  
- `normalize_url` → canonicalize URLs  
- `make_point(lon,lat,epsg=4326)` → derive point geometry from numeric lon/lat  

✅ Keep transforms **pure** (no network calls, no randomness, no “now()”).

</details>

---

## 📄 `field_map.csv` template (copy/paste)

> ✍️ Replace `source_field` values to match your dataset’s raw headers exactly.

```csv
source_field,target_field,target_type,transform,required,default,sensitivity,description
id,source_record_id,string,trim,true,,public,Unique record identifier in the source dataset
name,name,string,trim,true,,public,Primary display label
description,description,string,trim|null_if_empty,false,,public,Human readable description or notes
type,feature_type,string,trim|lower,false,,public,Type or category label
start_date,valid_from,date,parse_date(%Y-%m-%d),false,,public,Start date if known
end_date,valid_to,date,parse_date(%Y-%m-%d),false,,public,End date if known
date,event_date,date,parse_date(%Y-%m-%d),false,,public,Single event date if known
lat,lat,float,parse_float,false,,public,Latitude in WGS84
lon,lon,float,parse_float,false,,public,Longitude in WGS84
__derived__,geometry,geometry,make_point(lon,lat,epsg=4326),false,,public,Derived point geometry from lon and lat
source_url,source_url,string,trim|normalize_url,false,,public,Canonical source URL
license,source_license,string,trim,false,,public,License identifier or text
citation,source_citation,string,trim,false,,public,Citation or provenance note
```

---

## ✅ Dataset checklist

- [ ] Folder exists: `data/external/mappings/<dataset_slug>/`
- [ ] `field_map.csv` exists in that folder
- [ ] All `source_field` values match raw headers (case-sensitive)
- [ ] Any `required=true` fields are actually present in raw inputs
- [ ] License + provenance fields are mapped or provided (governance hook).:contentReference[oaicite:5]{index=5}
- [ ] ETL remains deterministic/replayable end-to-end.:contentReference[oaicite:6]{index=6}

---

## 🔗 Project references

- 📘 Master Guide (structure + pipeline invariants): :contentReference[oaicite:7]{index=7}  
- 🧱 KFM Technical Blueprint (system overview context): :contentReference[oaicite:8]{index=8}  

