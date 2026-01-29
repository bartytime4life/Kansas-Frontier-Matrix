# `<dataset_slug>` — Processed Dataset 📦🗺️

![Stage](https://img.shields.io/badge/stage-processed-blue)
![Domain](https://img.shields.io/badge/domain-external-lightgrey)
![Status](https://img.shields.io/badge/status-TBD-orange)
![License](https://img.shields.io/badge/license-TBD-red)

> ✅ This folder contains the **processed (analysis-ready)** outputs for the external dataset **`<dataset_slug>`**.  
> 🔒 Raw inputs should remain immutable; processed outputs live here for downstream use (catalogs → graph → API/UI).

---

## 📌 Quick facts

| Field | Value |
|---|---|
| Dataset slug | `<dataset_slug>` |
| Domain | `external` |
| Lifecycle stage | `processed` |
| Dataset version | `vX.Y.Z` (or `YYYY-MM-DD`) |
| Date last processed | `YYYY-MM-DD` |
| Pipeline | `pipelines/<pipeline_name>.py` (or `.ipynb`) |
| Primary formats | `Parquet / GeoJSON / GPKG / GeoTIFF / CSV` (pick) |
| Geometry type | `Point / LineString / Polygon / Raster / None` |
| CRS / Projection | `EPSG:4326` (or `TBD`) |
| Spatial coverage | `TBD` (bbox, region) |
| Temporal coverage | `TBD` (start–end) |
| License (upstream) | `TBD` |
| Citation / DOI | `TBD` |

---

## 🧭 Where this sits in the KFM pipeline

```mermaid
flowchart LR
  raw["📥 Raw evidence<br/>data/external/raw/<dataset_slug>/"] --> work["🧪 Work / staging<br/>data/external/work/<dataset_slug>/"]
  work --> proc["✅ Processed outputs<br/>data/external/processed/<dataset_slug>/data/"]
  proc --> stac["🛰️ STAC<br/>data/stac/..."]
  proc --> dcat["📚 DCAT<br/>data/catalog/dcat/..."]
  proc --> prov["🧾 PROV<br/>data/prov/..."]
  stac --> graph["🕸️ Graph (Neo4j refs)"]
  dcat --> graph
  prov --> graph
  graph --> api["⚙️ API"]
  api --> ui["🧭 UI / Story Nodes"]
```

---

## 🗂️ Folder layout

> You are here: `data/external/processed/<dataset_slug>/data/README.md`

```text
data/external/processed/<dataset_slug>/
├─ data/                              # ✅ analysis-ready outputs (this folder)
│  ├─ README.md                       # ⬅ you are here
│  ├─ <dataset_slug>.<ext>            # primary artifact (TBD)
│  ├─ <dataset_slug>_assets/          # optional: tiles, sidecars, thumbnails
│  └─ checksums.sha256                # optional but recommended
├─ metadata/                          # optional local helpers (schema + QA)
│  ├─ schema.json                     # optional JSON Schema / Parquet schema export
│  ├─ data_dictionary.md              # optional human-readable dictionary
│  └─ validation_report.md            # optional QA notes/results
└─ logs/                              # optional pipeline logs (run summaries)
   └─ <run_id>.log
```

---

## 📦 What’s in this `data/` directory

### 1) Primary outputs (required)
List the “contract outputs” that downstream systems should rely on.

- **`<dataset_slug>.<ext>`** — `TBD`: one-line description  
  - Rows/features: `TBD`  
  - Geometry: `TBD`  
  - CRS: `TBD`  
  - Expected consumer(s): `Graph ingest / API / UI / Analysis`

### 2) Supporting outputs (optional)
- `checksums.sha256` — integrity checks for reproducibility
- `<dataset_slug>_preview.png` — quick visual sanity check
- `<dataset_slug>_sample.<ext>` — small sample for tests/demos

---

## 🧪 How to use / load the data

### Python 🐍
```python
# Example: pick the right reader for your format
from pathlib import Path

p = Path("data/external/processed/<dataset_slug>/data/<dataset_slug>.<ext>")

# GeoPackage / GeoJSON
# import geopandas as gpd
# gdf = gpd.read_file(p)

# Parquet
# import pandas as pd
# df = pd.read_parquet(p)

print(p)
```

### R 📊
```r
# sf for vectors, arrow for parquet, readr for csv
# library(sf)
# x <- st_read("data/external/processed/<dataset_slug>/data/<dataset_slug>.<ext>")
```

### CLI sanity checks 🧰
```bash
# File size + hash
ls -lah data/external/processed/<dataset_slug>/data/
sha256sum data/external/processed/<dataset_slug>/data/<dataset_slug>.<ext> | head

# If vector:
# ogrinfo -so data/external/processed/<dataset_slug>/data/<dataset_slug>.gpkg <layer_name>
# If raster:
# gdalinfo data/external/processed/<dataset_slug>/data/<dataset_slug>.tif | head
```

---

## 🧾 Schema, semantics, and field definitions

> Treat this as the dataset’s **contract**. Keep it stable; if you must break it, create a new version.

### Data dictionary (fill this in ✅)

| Field | Type | Units | Description | Allowed values | Nullable | Notes |
|---|---|---:|---|---|:---:|---|
| `id` | string |  | Stable record identifier |  | ❌ | Prefer deterministic IDs |
| `source_id` | string |  | Upstream identifier |  | ✅ | Linkable to raw evidence |
| `name` | string |  | Human label |  | ✅ |  |
| `date_start` | date |  | Start date |  | ✅ | ISO-8601 |
| `date_end` | date |  | End date |  | ✅ | ISO-8601 |
| `geom` | geometry |  | Geometry (if spatial) |  | ✅ | If present, specify type/CRS |
| `confidence` | number |  | Uncertainty/confidence | 0–1 | ✅ | Explain scoring |

### Spatial specifics (if applicable)
- **Geometry type**: `TBD`
- **CRS**: `TBD`
- **Validity rules**: `TBD` (e.g., polygons must be valid; no self-intersections)
- **Precision / rounding**: `TBD`

### Temporal specifics (if applicable)
- **Time zone**: `UTC / local / TBD`
- **Granularity**: `year / month / day / timestamp`
- **Rules**: `date_end >= date_start`, missingness semantics, etc.

---

## 🔗 Required metadata “boundary artifacts” (STAC / DCAT / PROV)

> These records are what make the dataset discoverable, traceable, and reproducible.

| Artifact | Status | Expected location (relative) | Notes |
|---|:---:|---|---|
| 🛰️ STAC Collection | ⬜ | `../../../../stac/collections/<dataset_slug>/collection.json` | Required even if “mostly non-spatial” |
| 🛰️ STAC Item(s) | ⬜ | `../../../../stac/items/<dataset_slug>/` | Item assets must link to the files in this folder |
| 📚 DCAT Dataset | ⬜ | `../../../../catalog/dcat/<dataset_slug>.jsonld` | Include license + distributions |
| 🧾 PROV bundle | ⬜ | `../../../../prov/<dataset_slug>/prov.json` | Must link raw → work → processed + run info |

✅ **When updating this dataset**, update these artifacts in the same PR.

---

## 🧬 Provenance & processing notes

### Upstream sources (raw evidence)
- Source name: `TBD`
- Source URL(s): `TBD`
- Retrieval date(s): `TBD`
- Raw location: `data/external/raw/<dataset_slug>/...`

### Transformation summary (what changed from raw → processed)
Keep this concise but explicit:

1. **Ingest**: `TBD` (download/unzip/parse)  
2. **Normalize**: `TBD` (types, columns, units, CRS)  
3. **Clean**: `TBD` (dedupe, missing values, snapping/repair)  
4. **Enrich**: `TBD` (joins, geocoding, derived attributes)  
5. **Export**: `TBD` (format + partitioning)  
6. **Catalog/Lineage**: updated STAC/DCAT/PROV (required)

### Reproducible run command
```bash
# Example patterns (pick one that matches your repo)
# python pipelines/<pipeline_name>.py --config pipelines/config/<dataset_slug>.yml
# make data-external-<dataset_slug>
# docker-compose exec api python pipelines/<pipeline_name>.py --config ...
```

---

## ✅ Validation & QA checklist

> Make it easy for future-you to verify quality quickly.

### Automated checks (recommended)
- [ ] Schema validation passes (`metadata/schema.json` or equivalent)
- [ ] Geometry validity checks (if spatial)
- [ ] Row counts match expectation (document deltas if not)
- [ ] No duplicate primary keys
- [ ] Checksums updated (`checksums.sha256`)
- [ ] STAC/DCAT/PROV updated and cross-linked

### Manual spot checks (recommended)
- [ ] Visual inspection in QGIS/Kepler/Notebook
- [ ] Outlier scan (bounds, null rates, crazy values)
- [ ] Compare sample against raw evidence for fidelity

---

## 🧷 Versioning & change policy

- **Version format**: `vX.Y.Z` or `YYYY-MM-DD` (choose and keep consistent)
- **When version changes**:
  - Patch: metadata fix / non-semantic change  
  - Minor: additive columns / additive features (backwards compatible)  
  - Major: breaking schema changes

> 🧠 Tip: if you reprocess or update, record linkage in **DCAT + PROV** so newer versions point back to older ones.

---

## ⚖️ License, attribution, and citation

### License
- Upstream license: `TBD`
- Redistribution allowed? `TBD`
- Required attribution text:  
  > `TBD`

### How to cite
```bibtex
@dataset{<dataset_slug>,
  title        = {TBD},
  author       = {TBD},
  year         = {TBD},
  version      = {TBD},
  publisher    = {Kansas Frontier Matrix (KFM)},
  note         = {Processed dataset + provenance in repository},
  url          = {TBD}
}
```

---

## 🧭 Governance, FAIR/CARE & sensitivity (don’t skip) 🌱

- **FAIR** (Findable, Accessible, Interoperable, Reusable): `TBD`
- **CARE / sovereignty considerations** (if applicable): `TBD`
- Contains personal/sensitive data? `Yes/No`  
  - If yes: document redaction/aggregation rules + access constraints.
- Indigenous data present or adjacent? `Yes/No`  
  - If yes: add governance notes and constraints clearly.

---

## 🐛 Known issues / limitations

- `TBD` (e.g., gaps, uncertain geocodes, boundary mismatches, missing years)
- `TBD`

---

## 🧾 Changelog

| Date | Version | Summary | Author |
|---|---|---|---|
| YYYY-MM-DD | v0.1.0 | Initial processed release | @you |
| YYYY-MM-DD | v0.1.1 | Fix metadata / minor cleanup | @you |

---

## 👥 Maintainers

- Primary: `@TBD`
- Reviewer: `@TBD`
- Domain owner: `@TBD`

---

## 🔗 Related docs

- Dataset pipeline: `../../../../../pipelines/<pipeline_name>.py`
- Raw evidence: `../../../../raw/<dataset_slug>/`
- Work products: `../../../../work/<dataset_slug>/`
- STAC/DCAT/PROV profiles: `KFM_STAC_PROFILE.md`, `KFM_DCAT_PROFILE.md`, `KFM_PROV_PROFILE.md` (location may vary)

