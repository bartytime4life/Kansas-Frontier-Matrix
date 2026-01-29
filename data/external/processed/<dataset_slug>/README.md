# 📦 `<dataset_slug>` — External *Processed* Dataset

![Stage](https://img.shields.io/badge/stage-processed-blue)
![Scope](https://img.shields.io/badge/scope-external-lightgrey)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-brightgreen)
![Version](https://img.shields.io/badge/dataset%20version-TODO-orange)

**Path:** `data/external/processed/<dataset_slug>/` ✅

> [!IMPORTANT]
> In this system, datasets are expected to move **Raw → Processed → Catalog/Prov → Database → API → UI**.  
> Anything that shortcuts this flow (e.g., “just drop a file into the UI”) is treated as flawed unless explicitly justified. :contentReference[oaicite:0]{index=0}

---

## ✨ What this folder is for

This folder contains the **authoritative processed outputs** for the dataset **`<dataset_slug>`**:
- cleaned/standardized files ready for analysis and/or DB ingestion
- stable asset paths that metadata (STAC/DCAT/PROV) can safely point to
- versioned artifacts (so changes can be reviewed like code):contentReference[oaicite:1]{index=1}

> [!WARNING]
> **Do not “hand-edit” processed outputs.**  
> Update the upstream pipeline and regenerate outputs so provenance stays correct and reproducible. (Pipelines are intended to be deterministic and run end-to-end without manual steps.):contentReference[oaicite:2]{index=2}

---

<details>
<summary>🧭 Table of Contents</summary>

- [📍 Dataset card](#-dataset-card)
- [🗂️ Folder layout](#️-folder-layout)
- [🔗 Upstream sources](#-upstream-sources)
- [⚙️ Processing and reproducibility](#️-processing-and-reproducibility)
- [📦 Output inventory](#-output-inventory)
- [🧾 Schema and data dictionary](#-schema-and-data-dictionary)
- [🧭 Spatial and temporal reference](#-spatial-and-temporal-reference)
- [✅ Validation and QA](#-validation-and-qa)
- [🧬 Metadata and provenance](#-metadata-and-provenance)
- [🧷 Versioning and changelog](#-versioning-and-changelog)
- [🧩 System integration](#-system-integration)
- [🔐 Licensing and governance](#-licensing-and-governance)
- [🤝 How to update this dataset](#-how-to-update-this-dataset)
- [📇 Maintainers](#-maintainers)
- [📚 Project standards references](#-project-standards-references)

</details>

---

## 📍 Dataset card

| Field | Value |
|---|---|
| **Dataset slug** | `<dataset_slug>` |
| **Stage** | `external → processed` |
| **Short description** | TODO (1–2 sentences) |
| **Primary entity** | TODO (e.g., parcels / events / imagery / boundaries / stations) |
| **Spatial?** | ✅/❌ (vector / raster / tabular-with-geo) |
| **Geometry type** | TODO (Point / LineString / Polygon / Multi* / Raster) |
| **CRS** | TODO (e.g., EPSG:4326) |
| **Temporal coverage** | TODO (start–end) |
| **Spatial coverage** | TODO (bbox / region) |
| **Record count** | TODO |
| **Granularity** | TODO (daily / yearly / event-based / etc.) |
| **License (derived)** | TODO (SPDX identifier if possible) |
| **Upstream source(s)** | TODO (publisher + dataset title + release date) |
| **Pipeline entrypoint** | TODO (e.g., `pipelines/<dataset_slug>/...`) |
| **Provenance bundle** | TODO (link to PROV file path) |

---

## 🗂️ Folder layout

Recommended structure inside `data/external/processed/<dataset_slug>/`:

```text
📁 data/external/processed/<dataset_slug>/
├─ 📄 README.md                👈 you are here
├─ 📄 CHANGELOG.md             (optional but recommended)
├─ 📄 checksums.sha256         (recommended for large/binary assets)
├─ 📁 data/                    (processed outputs)
│  ├─ <dataset_slug>.parquet
│  ├─ <dataset_slug>.geojson
│  └─ ...
├─ 📁 schema/                  (data dictionary + schema artifacts)
│  ├─ schema.json
│  └─ data_dictionary.md
└─ 📁 validation/              (pipeline-produced reports)
   ├─ row_counts.json
   ├─ expectations.md
   └─ validation_report.md
```

> [!TIP]
> If an output is **large**, consider Git LFS or a “fetch by checksum” strategy; the key expectation is that the **identity and existence** of every processed dataset is tracked, even when storage is externalized. :contentReference[oaicite:3]{index=3}

---

## 🔗 Upstream sources

### 📥 Raw inputs live elsewhere
This processed dataset should trace back to one (or more) raw source artifacts. Typical convention:

- `data/external/raw/<dataset_slug>/...` *(or equivalent)*  
- Raw inputs are treated as **read-only snapshots** and should not be modified by pipelines.:contentReference[oaicite:4]{index=4}

### 📌 Source list
Fill this in with concrete citations/links appropriate for your repo:

- **Source 1:** TODO  
  - Publisher: TODO  
  - Dataset/product: TODO  
  - Access date: TODO  
  - License/terms: TODO  
  - Notes: TODO (rate limits, API keys, special conditions)

---

## ⚙️ Processing and reproducibility

### 🧪 Deterministic pipelines (required)
Pipelines should:
- produce the **same outputs** given the same inputs + config
- avoid manual/interactive steps
- avoid duplicating datasets when nothing changed (use checksums/version checks):contentReference[oaicite:5]{index=5}

### 🧰 Pipeline entrypoint
- `pipelines/<dataset_slug>/...` *(preferred)*  
  **or**
- `pipelines/import_<dataset_slug>.py` *(simple pattern)*

> Example patterns from project docs include scripts like `pipelines/import_census.py` and per-source raw folders like `data/raw/census_1900/...` (adapt to your `data/external/raw/...` layout).:contentReference[oaicite:6]{index=6}

### 🧩 Optional: plugin-style pipeline packaging
If you’re using a plugin/orchestrator pattern, document it here:

- `pipelines/plugins/<dataset_slug>/pipeline.yml`
- `pipelines/plugins/<dataset_slug>/run.py`

This lets the orchestrator “discover” pipelines by convention and run on schedules/configs.:contentReference[oaicite:7]{index=7}

### ▶️ Rebuild command
> Replace these placeholders with the real command(s) used in this repo.

```bash
# Example: run the dataset pipeline
python -m pipelines.<dataset_slug>.run \
  --config pipelines/<dataset_slug>/config.yml \
  --output data/external/processed/<dataset_slug>/
```

### 🧾 Required outputs from the pipeline (contract artifacts)
Each dataset pipeline is expected to emit:
- processed data files in this folder
- a **STAC** record(s)
- a **DCAT** dataset record
- a **PROV** lineage bundle (raw → work → processed)
- (recommended) validation reports & summary stats:contentReference[oaicite:8]{index=8}

If these are missing, CI is expected to flag/reject the contribution (“no data enters without documentation”).:contentReference[oaicite:9]{index=9}

---

## 📦 Output inventory

List every “blessed” output file that downstream components depend on.

| File | Format | Purpose | Row/feature count | Notes |
|---|---:|---|---:|---|
| `data/<dataset_slug>.parquet` | Parquet | TODO | TODO | TODO |
| `data/<dataset_slug>.geojson` | GeoJSON | TODO | TODO | TODO |
| `data/<dataset_slug>.tif` | GeoTIFF | TODO | n/a | TODO |

> [!NOTE]
> Processed datasets should be **consistent**: cleaned attributes, standardized units, and a deliberate CRS choice (often a common one like WGS84 unless there’s reason otherwise).:contentReference[oaicite:10]{index=10}

---

## 🧾 Schema and data dictionary

### 🔑 Column-level documentation
Include:
- field name
- type
- units
- allowed values / enumerations
- nullability
- how it was derived (if computed)

| Field | Type | Units | Nullable | Description |
|---|---|---:|:---:|---|
| `id` | string | — | ❌ | TODO |
| `name` | string | — | ✅ | TODO |
| `value` | float | TODO | ✅ | TODO |
| `geometry` | geometry | CRS units | ❌ | TODO |

### 🧠 Metadata best-practice checklist (geo + non-geo)
For dependable GIS datasets, metadata commonly includes: identification, quality, spatial reference (CRS/projection), entity & attribute info, distribution, citation, temporal info, and contact info.:contentReference[oaicite:11]{index=11}

---

## 🧭 Spatial and temporal reference

### 🗺️ CRS / Projection
- **CRS:** `EPSG:TODO`
- **Why this CRS:** TODO  
- **Reprojection rules:** TODO

> Pipelines often include coordinate conversion as part of the “process and clean” step, and projects may standardize on EPSG:4326 or a Kansas-specific projection depending on the dataset needs.:contentReference[oaicite:12]{index=12}

### 🧭 Coverage
- **Spatial extent (bbox):** TODO (minx, miny, maxx, maxy)
- **Temporal extent:** TODO (start–end)
- **Resolution / scale:** TODO (if raster)

---

## ✅ Validation and QA

### ✅ Required validations
- [ ] schema matches `schema/schema.json`
- [ ] geometry validity checks (if vector)
- [ ] expected column set present
- [ ] plausible ranges (min/max) verified
- [ ] null-rate thresholds enforced
- [ ] key uniqueness constraints (if applicable)

> Pipelines may produce **validation reports** and summary statistics (row counts, min/max, etc.) to make review easier.:contentReference[oaicite:13]{index=13}

### 📊 Recommended validation artifacts
- `validation/validation_report.md`
- `validation/row_counts.json`
- `validation/minmax.json`

---

## 🧬 Metadata and provenance

### 🌐 Required: STAC + DCAT + PROV (alignment policy)
Every dataset/evidence artifact is expected to have:
- **STAC collection + item(s)** (even non-spatial datasets often get a STAC collection for consistency)
- **DCAT dataset entry** (title, description, license, keywords, distribution links)
- **PROV activity bundle** (raw sources, steps, responsible agents, timestamps, configs):contentReference[oaicite:14]{index=14}

### 🔗 Cross-layer linkage expectations (keep everything in sync)
- STAC Items **must point to** actual assets in processed storage (this folder qualifies as “processed storage”) and carry source/license attribution.
- DCAT should link to STAC and/or direct downloads.
- PROV should connect raw → intermediate work → processed outputs and include run IDs/commit hashes.
- The knowledge graph should reference catalog IDs (STAC/DOI/etc.), not duplicate payloads.:contentReference[oaicite:15]{index=15}

### 📌 Put links here (update paths to match your repo)
- **STAC:** `data/catalog/.../<dataset_slug>...`
- **DCAT:** `data/catalog/.../<dataset_slug>...`
- **PROV:** `data/provenance/<dataset_slug>.prov.json` *(example pattern)*:contentReference[oaicite:16]{index=16}

---

## 🧷 Versioning and changelog

### 📌 Dataset versioning rules
When updating/reprocessing:
- create a new dataset version and link it to the previous version in **DCAT** and **PROV** (e.g., `prov:wasRevisionOf`)
- ideally assign a persistent identifier (DOI/ARK) for published versions:contentReference[oaicite:17]{index=17}

### 📝 Changelog (fill this in)
- **vX.Y.Z** — YYYY-MM-DD  
  - Added: TODO  
  - Changed: TODO  
  - Fixed: TODO  
  - Notes: TODO

---

## 🧩 System integration

### 🗃️ Database loading
Document target tables, schemas, or indexes here.

- **PostGIS table:** `TODO.schema.todo_table`
- **Primary key:** `TODO`
- **Geometry column:** `geom` (or `geometry`)  
- **Indexing:** TODO (GiST / SP-GiST / BRIN / etc.)

> Processed datasets are considered authoritative; updates can trigger re-indexing or reload into DBs as needed (e.g., a changed GeoJSON may cause a backend re-index).:contentReference[oaicite:18]{index=18}

### 🔌 API + UI touchpoints
- **API endpoint(s):** TODO
- **UI layer name:** TODO
- **Graph node IDs (if applicable):** TODO (prefer catalog references)

---

## 🔐 Licensing and governance

### 📜 Licensing
- **Upstream license:** TODO  
- **Derived dataset license:** TODO  
- **Attribution text:** TODO (copy/paste ready)

### 🧭 Ethics, access, and community controls
If the dataset contains sensitive content (locations of cultural sites, personal data, etc.), document:
- redaction rules
- tiered access strategy
- governance/approval requirements

> The project blueprint emphasizes embedding FAIR and CARE principles, including tiered data access and honoring community control over information.:contentReference[oaicite:19]{index=19}

---

## 🤝 How to update this dataset

### ✅ “Ready to merge” checklist
- [ ] Raw inputs stored/linked under `data/external/raw/<dataset_slug>/` (or equivalent)
- [ ] Pipeline is deterministic and non-interactive
- [ ] Processed outputs updated in `data/external/processed/<dataset_slug>/data/`
- [ ] STAC updated/created
- [ ] DCAT updated/created
- [ ] PROV bundle updated/created (includes run ID / commit hash)
- [ ] Validation reports updated
- [ ] This README updated (schema, counts, coverage, version)

---

## 📇 Maintainers

- **Owner:** TODO (@handle)
- **Domain reviewer:** TODO
- **Last reviewed:** YYYY-MM-DD
- **Contact:** TODO

---

## 📚 Project standards references

<details>
<summary>📌 Why the rules above exist (quick citations)</summary>

- Canonical pipeline sequence: Raw → Processed → Catalog/Prov → Database → API → UI:contentReference[oaicite:20]{index=20}
- Processed data tracked as authoritative, with options for Git LFS / checksums for large assets:contentReference[oaicite:21]{index=21}
- Pipelines should be deterministic, reproducible, and should not modify raw inputs:contentReference[oaicite:22]{index=22}
- Required metadata alignment: STAC + DCAT + PROV, with cross-linking expectations:contentReference[oaicite:23]{index=23}
- Dataset versioning: link new versions to predecessors via DCAT/PROV (`prov:wasRevisionOf`), prefer persistent identifiers:contentReference[oaicite:24]{index=24}
- Metadata categories commonly needed for dependable GIS data (identification, quality, spatial reference, etc.):contentReference[oaicite:25]{index=25}

</details>

