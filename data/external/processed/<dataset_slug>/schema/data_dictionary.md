# 📘 Data Dictionary — `<dataset_slug>`

![status](https://img.shields.io/badge/status-draft-orange)
![pipeline](https://img.shields.io/badge/pipeline-processed-blue)
![schema](https://img.shields.io/badge/schema_version-v0.1.0-informational)
![metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-2ea44f)

> 🧭 **Purpose:** This document defines the **field-level schema** and usage rules for the processed dataset:  
> `data/external/processed/<dataset_slug>/`

---

## ✨ Quick Facts

| Item | Value |
|---|---|
| **Dataset slug** | `<dataset_slug>` |
| **Human name** | `TBD` |
| **Domain / module** | `external` (or `TBD`) |
| **Primary data type** | `Vector` ☐ / `Raster` ☐ / `Tabular` ☐ / `Document` ☐ |
| **Primary format(s)** | `GeoJSON` ☐ / `GeoParquet` ☐ / `CSV` ☐ / `Parquet` ☐ / `GeoTIFF (COG)` ☐ / `JSONL` ☐ |
| **Spatial reference (CRS)** | `TBD (recommended: EPSG:4326 unless justified otherwise)` |
| **Temporal coverage** | `TBD` |
| **Spatial coverage** | `TBD (e.g., Kansas statewide)` |
| **Update cadence** | `TBD (one-time / annual / monthly / ad-hoc)` |
| **License** | `TBD` |
| **Source / provider** | `TBD` |
| **Data steward** | `TBD` |
| **Sensitivity** | `Public` ☐ / `Restricted` ☐ / `Sensitive` ☐ |

---

## 🗂️ Package Layout

```text
data/external/processed/<dataset_slug>/
├─ data/                         # ✅ canonical deliverables (what downstream loads/serves)
│  ├─ <dataset_slug>.<ext>        # e.g., .geojson / .parquet / .csv / .tif
│  └─ (optional) assets/          # rasters, attachments, thumbnails, etc.
├─ schema/
│  ├─ data_dictionary.md          # 📘 (this file)
│  ├─ schema.json                 # (optional) JSON Schema / GeoParquet schema
│  └─ (optional) code_lists/      # enumerations (CSV/JSON)
└─ README.md                      # (recommended) dataset overview + runbook
```

> ✅ **Rule of thumb:** `processed/` is authoritative “ready-to-use” output and should be clean, standardized, and documented.

---

## 🔗 Required KFM “Truth Path” Links

Fill these in so this dataset is traceable end-to-end (Raw → Processed → Catalog/Prov → DB → API → UI):

### 1) Data artifacts (this package)
- **Primary data file:** `data/external/processed/<dataset_slug>/data/<dataset_slug>.<ext>`
- **Schema file (optional):** `data/external/processed/<dataset_slug>/schema/schema.json`

### 2) Catalog artifacts (STAC / DCAT)
- **STAC Collection:** `data/stac/collections/<dataset_slug>.json` (or `TBD`)
- **STAC Item(s):** `data/stac/items/<dataset_slug>/…` (or `TBD`)
- **DCAT dataset entry:** `data/catalog/dcat/<dataset_slug>.jsonld` (or `TBD`)

### 3) Provenance artifacts (PROV)
- **PROV lineage bundle:** `data/prov/<dataset_slug>.json` (or `data/provenance/<dataset_slug>.json`)  

### 4) Database + API (if loaded/served)
- **PostGIS table(s):** `TBD`
- **Neo4j nodes/edges (if applicable):** `TBD`
- **API endpoint(s):** `TBD` (e.g., `/api/v1/datasets/<dataset_slug>`)

---

## 📦 Files & Distributions

| Path | Format | Role | Notes |
|---|---:|---|---|
| `data/<dataset_slug>.<ext>` | `TBD` | primary distribution | `TBD` |
| `schema/schema.json` | JSON | schema contract | `optional but recommended` |
| `schema/code_lists/*` | CSV/JSON | controlled vocabularies | `optional` |

---

## 🧱 Record Model

Describe what **one record** means:

- **Record unit:** `TBD` (e.g., “one feature = one land parcel boundary”, “one row = one observation”, “one pixel = one value per band”)
- **Primary key:** `TBD` (recommended: stable, string-based `kfm_id`)
- **Uniqueness rule:** `TBD` (e.g., `(kfm_id)` unique; or `(source_id, date)` unique)
- **Granularity:**  
  - Spatial: `TBD`  
  - Temporal: `TBD`  
  - Administrative: `TBD` (county/tract/etc)

---

## 🧾 Schema

> **How to use this section:**  
> Keep the tables that match your dataset type ✅ and delete the rest 🧹

---

### ✅ A) Vector datasets (GeoJSON / GeoParquet)

#### A1) Top-level structure (GeoJSON)
| Component | Type | Required | Description |
|---|---|:--:|---|
| `type` | string | ✅ | Always `"FeatureCollection"` |
| `features[]` | array | ✅ | Array of GeoJSON Features |

#### A2) Feature structure
| Field | Type | Required | Nullable | Description |
|---|---|:--:|:--:|---|
| `type` | string | ✅ | ⛔ | Always `"Feature"` |
| `id` | string/integer | ☐ | ✅ | Optional GeoJSON feature id (do not rely on it unless guaranteed stable) |
| `geometry` | object | ✅ | ⛔ | GeoJSON Geometry |
| `properties` | object | ✅ | ✅ | Attribute dictionary |

#### A3) Geometry rules
| Rule | Value |
|---|---|
| Allowed geometry types | `Point` ☐ / `LineString` ☐ / `Polygon` ☐ / `MultiPolygon` ☐ / `TBD` |
| CRS | `TBD` (recommended: EPSG:4326 unless justified otherwise) |
| Validity | `Must be valid geometry; no self-intersections; no empty geometries` |
| Precision | `TBD` |

#### A4) Properties table (the real “columns”)
> ✍️ Fill in **every property key** expected in `properties{}`.

| Field | Type | Required | Nullable | Units | Example | Description |
|---|---|:--:|:--:|---|---|---|
| `kfm_id` | string | ✅ | ⛔ | — | `kfm.<dataset_slug>.000001` | Stable, global identifier for the record |
| `source_id` | string | ☐ | ✅ | — | `12345` | Original identifier from source system |
| `name` | string | ☐ | ✅ | — | `TBD` | Human-readable name/label |
| `valid_start` | date/datetime | ☐ | ✅ | ISO-8601 | `1870-01-01` | Start of real-world validity (if temporal) |
| `valid_end` | date/datetime | ☐ | ✅ | ISO-8601 | `1875-12-31` | End of real-world validity (if temporal) |
| `confidence` | number | ☐ | ✅ | 0–1 | `0.82` | Confidence/uncertainty score (if derived) |
| `notes` | string | ☐ | ✅ | — | `digitized from map sheet…` | Free-text notes (keep short) |
| `stac_item_id` | string | ☐ | ✅ | — | `<dataset_slug>-item-0001` | Links record to STAC item (if applicable) |
| `prov_entity_id` | string | ☐ | ✅ | — | `prov:entity:...` | Links record to PROV entity/activity (if applicable) |

> 🧠 Tip: If your dataset is large, consider **GeoParquet** and maintain a `schema.json` mirroring the column types.

---

### ✅ B) Tabular datasets (CSV / Parquet)

| Column | Type | Required | Nullable | Units | Example | Description |
|---|---|:--:|:--:|---|---|---|
| `kfm_id` | string | ✅ | ⛔ | — | `kfm.<dataset_slug>.000001` | Stable, global identifier |
| `...` | ... | ☐ | ☐ | ☐ | ☐ | ☐ |

#### Tabular constraints
- Primary key: `TBD`
- Index candidates: `TBD` (e.g., `county_fips`, `date`, `source_id`)
- Null handling: `TBD`
- Encoding: `UTF-8`

---

### ✅ C) Raster datasets (GeoTIFF / COG)

#### C1) Raster asset summary
| Item | Value |
|---|---|
| File(s) | `TBD` |
| Raster type | `GeoTIFF` ☐ / `COG` ✅ / `TBD` |
| CRS | `TBD` |
| Pixel size / resolution | `TBD` |
| NoData value | `TBD` |
| Data type | `uint8` ☐ / `int16` ☐ / `float32` ☐ / `TBD` |
| Bands | `TBD` |

#### C2) Band dictionary
| Band | Name | Type | Units | NoData | Description |
|---:|---|---|---|---|---|
| 1 | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |

> 🗺️ Raster datasets should be described in **STAC Items** (assets, bbox, datetime/range) and linked to PROV lineage.

---

### ✅ D) Document / text corpora (JSONL / extracted text)

| Field | Type | Required | Nullable | Example | Description |
|---|---|:--:|:--:|---|---|
| `doc_id` | string | ✅ | ⛔ | `doc.0001` | Stable document identifier |
| `source_uri` | string | ☐ | ✅ | `https://…` | Original location of the artifact |
| `text` | string | ✅ | ✅ | `…` | Extracted or normalized text |
| `page` | integer | ☐ | ✅ | `12` | Page number if scanned/PDF |
| `bbox` | object | ☐ | ✅ | `{...}` | Optional spatial bounding box |
| `datetime` | datetime | ☐ | ✅ | `1890-05-01T00:00:00Z` | Extracted or assigned time |
| `confidence` | number | ☐ | ✅ | `0.91` | OCR/NLP confidence (if derived) |

---

## 🧪 Validation & QA Rules

### ✅ Minimum validation checks
- [ ] Schema matches this dictionary (types + required fields)
- [ ] No duplicate primary keys
- [ ] No malformed dates / datetimes (ISO-8601)
- [ ] Units are consistent and documented
- [ ] For geospatial: geometry validity checks pass (no empty/invalid geometries)
- [ ] If temporal: `valid_start <= valid_end` for all records
- [ ] If controlled vocabularies exist: all coded fields match allowed values

### 🧯 Known issues / caveats (fill in)
- `TBD`

---

## 🧬 Lineage & Provenance

> This dataset should be reproducible from raw sources via pipelines and traceable via STAC/DCAT/PROV.

### Inputs
- Raw source(s): `TBD` (e.g., `data/raw/<source>/…`)
- External references: `TBD`

### Processing
- Pipeline script/notebook: `TBD` (e.g., `pipelines/<domain>/<dataset_slug>.py`)
- Key transforms:
  - `TBD`
  - `TBD`

### Outputs (this package)
- Processed dataset file(s): `TBD`
- Catalog metadata: `TBD`
- PROV bundle: `TBD`

---

## 🔁 Versioning & Change Log

| Version | Date | Change |
|---|---|---|
| `v0.1.0` | `TBD` | Initial data dictionary scaffold |

---

## ✅ Definition of Done (DoD)

- [ ] `<dataset_slug>` filled in everywhere
- [ ] All files listed under **Files & Distributions**
- [ ] One schema section fully completed (Vector **or** Tabular **or** Raster **or** Document)
- [ ] Validation rules updated to match actual constraints
- [ ] STAC/DCAT/PROV paths linked and present
- [ ] README.md exists with dataset overview + usage
- [ ] Any code lists added under `schema/code_lists/`

---

<details>
<summary>📌 Naming & conventions (recommended)</summary>

- **Dataset slug:** `lower_snake_case` (stable, no version suffix)
- **IDs:** stable, opaque strings (avoid reusing source row numbers if they can change)
- **Dates:** ISO-8601 (`YYYY-MM-DD`); datetimes ISO-8601 with timezone
- **Numbers:** specify units + scale (especially for indexes)
- **Text:** UTF-8; avoid embedding huge blobs into attribute fields when possible

</details>

