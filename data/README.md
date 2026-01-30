# 📦 `data/` — Versioned Datasets, Metadata, & Provenance (KFM) 🗺️

![data](https://img.shields.io/badge/data-versioned-informational)
![truth-path](https://img.shields.io/badge/truth%20path-raw%E2%86%92processed%E2%86%92catalog%E2%86%92api-blue)
![catalogs](https://img.shields.io/badge/catalogs-STAC%20%2B%20DCAT-purple)
![provenance](https://img.shields.io/badge/provenance-W3C%20PROV-005a9c)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-brightgreen)
![fail-closed](https://img.shields.io/badge/policy-fail--closed-critical)
![ci-gated](https://img.shields.io/badge/CI-metadata%20%2B%20license%20gates-orange)
![formats](https://img.shields.io/badge/formats-geojson%20%7C%20parquet%20%7C%20cog%20%7C%20csv-lightgrey)

Welcome to the **canonical source-of-truth** for Kansas Frontier Matrix (KFM) datasets 🧾  
This folder is **not “just a dump of files”** — it’s a *provenance-first* data vault where **every processed layer is traceable back to raw sources** and **discoverable via catalogs**.

> ✅ **KFM invariant:** if it’s used by the system, it must be **(1) processed**, **(2) cataloged**, and **(3) provenance-linked**.  
> ⛔ Anything missing metadata / lineage / license is treated as **not publishable** (fail-closed by design). 🔒

---

## 🧭 Quick Nav

- [📁 Folder layout (v13 canonical)](#folder-layout-v13-canonical)
- [🧩 Legacy path compatibility map](#legacy-path-compatibility-map)
- [🔁 The Truth Path lifecycle](#the-truth-path-lifecycle)
- [🧱 What goes where](#what-goes-where)
- [🧾 STAC / DCAT / PROV alignment](#stac--dcat--prov-alignment)
- [🏷️ Dataset naming & conventions](#dataset-naming--conventions)
- [✅ Publishing checklist (Definition of Done)](#publishing-checklist-definition-of-done)
- [🧪 Example: dataset “bundle”](#example-dataset-bundle)
- [📦 Handling large files](#handling-large-files)
- [🤖 Evidence artifacts (AI + analysis outputs)](#evidence-artifacts-ai--analysis-outputs)
- [🧪 Validation & CI gates](#validation--ci-gates)
- [📚 Further reading](#further-reading)

---

<a id="folder-layout-v13-canonical"></a>
## 📁 Folder layout (v13 canonical)

> Goal: make data **diffable**, **reviewable**, **rebuildable** — like code. ✅  
> Databases are **derivative performance caches**, not the authoritative store.

```text
📦 data/
├─ 🧾 raw/                         # Immutable source snapshots (evidence)
│  └─ 📁 <domain>/                 # e.g., census_1900/, usgs_water/, historical_maps/
│
├─ 🧪 work/                        # Intermediate artifacts (recommended staging)
│  └─ 📁 <domain>/
│
├─ ✅ processed/                   # Curated outputs used by DB/API/UI
│  └─ 📁 <domain>/
│
├─ 🗺️ stac/                        # Spatial/temporal discovery metadata
│  ├─ 📁 collections/              # STAC Collections
│  └─ 📁 items/                    # STAC Items
│
├─ 🗂️ catalog/
│  └─ 📁 dcat/                     # DCAT dataset records (JSON-LD / TTL)
│
├─ 🧬 prov/                        # Lineage logs (W3C PROV bundles)
│
└─ 🧱 external/                    # Manifests/pointers for large assets (LFS/S3/etc.)
   └─ 📄 manifest.*                # JSON/YAML w/ sha256, size, retrieval method
```

### 🔗 Nearby (not inside `data/`, but tightly coupled)
```text
🧾 schemas/                        # JSON Schemas for STAC/DCAT/PROV + contracts
⚙️ src/pipelines/                  # Deterministic ETL that writes raw→work→processed
📚 docs/data/<domain>/README.md     # Domain runbooks & source notes (required for new domains)
```

---

<a id="legacy-path-compatibility-map"></a>
## 🧩 Legacy path compatibility map

KFM evolved over time. Some repos may still contain older folder names. ✅  
**Preferred rule:** write *new* work to the **v13 canonical** layout above, and migrate/alias legacy paths as needed.

| Concept | v13 canonical | Legacy patterns you may still see |
|---|---|---|
| STAC metadata | `data/stac/...` | `data/catalog/stac/...` |
| DCAT metadata | `data/catalog/dcat/...` | `data/catalog/dcat/...` (usually same) |
| Provenance | `data/prov/...` | `data/provenance/...` |
| Intermediate artifacts | `data/work/...` | *(missing; pipelines wrote temp files elsewhere)* |

> 💡 If you can’t migrate immediately: consider **symlinks** or a **thin redirect** (README + pointers) so tooling can find canonical outputs.

---

<a id="the-truth-path-lifecycle"></a>
## 🔁 The Truth Path lifecycle (non-negotiable ordering)

```mermaid
flowchart LR
  subgraph Data["📦 Data"]
    A[🧾 Raw Sources<br/>data/raw/] --> B[🧪 Work Artifacts<br/>data/work/]
    B --> C[✅ Processed Assets<br/>data/processed/]
    C --> D[🗺️ STAC<br/>data/stac/]
    C --> E[🗂️ DCAT<br/>data/catalog/dcat/]
    C --> F[🧬 PROV<br/>data/prov/]
  end

  subgraph Knowledge["🧠 Storage & Knowledge"]
    D --> G[(🗃️ PostGIS<br/>spatial cache)]
    D --> H[(🕸️ Neo4j<br/>semantic graph)]
    F --> G
    F --> H
  end

  subgraph Delivery["🚀 Delivery"]
    G --> I[🧰 API Layer<br/>(contracts + redaction)]
    H --> I
    I --> J[🗺️ Map UI<br/>React · MapLibre · (optional) Cesium]
    J --> K[📖 Story Nodes<br/>governed narratives]
    K --> L[🎯 Focus Mode<br/>provenance-linked context bundle]
  end
```

**Key idea:** wipe the DB? No problem. Rebuild from `data/processed/` + STAC/DCAT/PROV + pipeline code. ♻️

---

<a id="what-goes-where"></a>
## 🧱 What goes where

### 🧾 `raw/` — immutable “evidence”
- Exact snapshots from original sources (ZIPs, CSVs, Shapefiles, PDFs, imagery, etc.)
- **Never edited by pipelines**
- If a source is wrong: add a corrected **new snapshot** and document the change in metadata + provenance

✅ Good:
- `data/raw/census_1900/census_1900.csv`
- `data/raw/historical_maps/1930_county_map.pdf`

⛔ Not allowed:
- Hand-editing raw CSV rows “just to fix a typo” without a new snapshot + provenance

---

### 🧪 `work/` — intermediate artifacts (recommended)
- Temporary outputs that matter for auditability or reproducibility
- Examples: cloud masks, cleaned-but-not-final tables, intermediate joins, QA summaries

✅ Good:
- `data/work/weather/noaa_cleaned_1900_1950.parquet`
- `data/work/imagery/landsat_cloudmask_2010.tif`

> 💡 Pipelines may also use ephemeral temp dirs, but if an intermediate step affects interpretability, capture it here and link it in PROV.

---

### ✅ `processed/` — curated “ready-to-serve”
- Cleaned, standardized, analysis-ready products
- Primary inputs to DB loaders and API serving
- Prefer **open formats** + **review-friendly diffs** (when possible)

Recommended format defaults:
- Vector: GeoJSON / GeoParquet
- Tabular/time-series: Parquet (partitioned by time/region if large)
- Raster: Cloud Optimized GeoTIFF (COG) or Zarr (when appropriate)

✅ Good:
- `data/processed/census/1900_population.geojson`
- `data/processed/weather/daily_rainfall.parquet`
- `data/processed/imagery/landsat_2010_kansas.cog.tif`

---

### 🗺️ `stac/` — spatial/temporal asset metadata (Findable ✅)
STAC should answer:  
- “What is this layer?”  
- “Where/when does it apply?”  
- “How do I access the actual asset?”  
- “What provenance explains this output?”

Recommended structure:
- `data/stac/collections/<collection_id>.json`
- `data/stac/items/<item_id>.json`

---

### 🗂️ `catalog/dcat/` — dataset discovery metadata (Discoverable 🔎)
DCAT provides higher-level dataset records:
- title, description, publisher/creator, keywords
- license and access notes
- distributions (links to STAC, direct files, or external manifests)

Recommended structure:
- `data/catalog/dcat/<dataset_id>.jsonld`

---

### 🧬 `prov/` — provenance bundles (Trustworthy 🧠)
Provenance should answer:
- **What inputs produced this output?**
- **Which pipeline + parameters were used?**
- **When did it run, and under what repo version/commit?**
- **Who/what ran it (agent)?**

> 🚩 If a dataset has no provenance bundle, treat it as *suspect* until proven otherwise.

Recommended structure:
- `data/prov/<dataset_id>.prov.json`

---

### 🧱 `external/` — pointers/manifests for huge assets
Used when assets are too large for normal Git storage:
- Git LFS pointer files
- S3/Blob object storage references
- chunked stores (Zarr) with checksums

Recommended: keep **a manifest** that records:
- logical name
- storage location
- size
- checksum (sha256)
- retrieval method & credentials assumptions (if any)

---

<a id="stac--dcat--prov-alignment"></a>
## 🧾 STAC / DCAT / PROV alignment

KFM expects **cross-linking** between boundary artifacts so downstream stages can navigate evidence.

### 🔗 Cross-linking expectations (minimum)
- **STAC Item → PROV** (link: “provenance”)
- **STAC Item → asset(s)** (local file or external pointer)
- **DCAT Dataset → STAC** (distribution link)
- **PROV → raw + work + processed entities** (entities with hashes where possible)

> ✅ Think of STAC/DCAT/PROV as the **API contract** for the data layer.

### 🧩 Recommended “dataset contract”
A dataset is considered complete when these exist (at minimum):

- `data/processed/<domain>/<something>.<ext>`
- `data/stac/items/<dataset_id>.json`
- `data/catalog/dcat/<dataset_id>.jsonld`
- `data/prov/<dataset_id>.prov.json`

Optional but encouraged:
- `data/stac/collections/<collection_id>.json` (when introducing a new collection)
- `data/external/manifest.json` (when any asset is external/LFS-managed)
- `docs/data/<domain>/README.md` (domain runbook)

---

<a id="dataset-naming--conventions"></a>
## 🏷️ Dataset naming & conventions

### 📛 Domain folders
Use `snake_case` domain names that match the real-world theme/source:
- `census`, `weather`, `land_treaties`, `railroads`, `soil`, `historical_maps`, `imagery`

### 🧩 Dataset IDs (recommended)
A stable dataset identifier keeps catalogs + provenance + narratives aligned:

**Format**
- `kfm.<domain>.<topic>.<version_or_year>`

**Examples**
- `kfm.census.population.1900`
- `kfm.weather.precip.daily.v1`
- `kfm.historical_maps.county_boundaries.1930`

### 🗂️ Processed file naming (recommended)
Make file names “scan readable”:

`<topic>__<coverage>__<time>__<vX>.<ext>`

Example:
- `population__kansas__1900__v1.geojson`
- `precip__kansas__daily__1850-2020__v2.parquet`

### 🗺️ Spatial reference & units
Every processed dataset must document:
- CRS / EPSG
- units
- null conventions
- temporal resolution & timezone assumptions (for time series)

> 💡 Put the human-friendly notes in DCAT + domain README, and the machine-critical fields in STAC + PROV.

---

<a id="publishing-checklist-definition-of-done"></a>
## ✅ Publishing checklist (Definition of Done)

A dataset PR is only “done” when **all** required artifacts exist and pass validation.

### ✅ Required
- [ ] 📥 Raw snapshot stored under `data/raw/<domain>/...` (or referenced via `data/external/`)
- [ ] 🧼 Deterministic pipeline exists/updated (writes `raw → work → processed`)
- [ ] ✅ Outputs written to `data/processed/<domain>/...`
- [ ] 🗺️ STAC Item created/updated (assets + bbox/time + links)
- [ ] 🗂️ DCAT record created/updated (title/desc/license/keywords/distributions)
- [ ] 🧬 PROV bundle created/updated (entities, activities, agents, parameters)
- [ ] ⚖️ License clearly declared (and compatible with repo policy)
- [ ] 🧪 Validation passes (schemas, geometry validity, required fields)
- [ ] 🔍 Review includes **data diffs + metadata diffs** (not just code)

### 🌟 Strongly recommended
- [ ] 📚 Domain runbook updated: `docs/data/<domain>/README.md`
- [ ] 🔐 Sensitivity classification recorded (CARE-aware handling)
- [ ] 🧾 External manifest includes sha256 for any off-repo asset

---

<a id="example-dataset-bundle"></a>
## 🧪 Example: dataset bundle

Let’s say we add a historical census extract:

```text
data/
├─ raw/
│  └─ census_1900/
│     └─ census_1900.csv
│
├─ work/
│  └─ census/
│     └─ census_1900_cleaned.parquet
│
├─ processed/
│  └─ census/
│     └─ population__kansas__1900__v1.geojson
│
├─ stac/
│  ├─ collections/
│  │  └─ kfm.census.population.json
│  └─ items/
│     └─ kfm.census.population.1900.json
│
├─ catalog/
│  └─ dcat/
│     └─ kfm.census.population.1900.jsonld
│
└─ prov/
   └─ kfm.census.population.1900.prov.json
```

✅ Now the dataset is:
- **Usable** (processed file exists)
- **Findable** (STAC + DCAT exist)
- **Auditable** (PROV exists)
- **Rebuildable** (pipeline + raw evidence exist)

---

<a id="handling-large-files"></a>
## 📦 Handling large files

Geospatial assets get big fast (rasters, point clouds, dense time-series). KFM’s stance:

- ✅ Small–medium: store directly in Git (prefer diff-friendly formats)
- 🧱 Large binaries: store via one of these patterns:
  1) **Git LFS** pointer files  
  2) **External object storage** (S3/Blob) + **checksum/hash recorded in-repo**  
  3) **Chunked, diffable** structures (e.g., partitioned Parquet; Zarr for rasters)

### 🧾 External manifest (recommended)
Store a manifest under `data/external/` for anything that isn’t fully in Git:

```json
{
  "assets": [
    {
      "logical_name": "landsat_2010_kansas.cog.tif",
      "storage": "s3",
      "uri": "s3://kfm-data/imagery/landsat_2010_kansas.cog.tif",
      "sha256": "REPLACE_ME",
      "size_bytes": 1234567890,
      "retrieval": "aws s3 cp ..."
    }
  ]
}
```

---

<a id="evidence-artifacts-ai--analysis-outputs"></a>
## 🤖 Evidence artifacts (AI + analysis outputs)

KFM treats AI outputs and analysis artifacts as **first-class datasets** 🧠  
Examples:
- OCR-derived corpora
- model-predicted map layers
- simulation outputs
- QA-derived “confidence layers”

**Rule:** if an artifact can influence a narrative, map, or query result, it must be:
- ✅ stored in `data/processed/...`
- 🗺️ cataloged (STAC/DCAT)
- 🧬 provenance-linked (PROV)
- 🔐 governed (license + sensitivity + validation)

> 🧯 No “black box” evidence: derived artifacts must be explainable, traceable, and reviewable.

---

<a id="validation--ci-gates"></a>
## 🧪 Validation & CI gates

KFM is designed to **fail closed** 🔒  
CI should block merges when:
- metadata is missing
- provenance is missing
- license is missing/unclear
- schemas don’t validate
- geometries are invalid
- external assets lack checksums

### ✅ Minimum checks (suggested)
- STAC JSON schema validation
- DCAT JSON-LD validation (or shape constraints)
- PROV schema validation
- “bundle completeness” check (processed ↔ STAC ↔ DCAT ↔ PROV)
- basic geometry validity + bounding-box sanity
- required fields present (domain-specific)
- checksum verification for external manifests

---

## 📚 Further reading

These project references influenced how `data/` is organized:

- 📘 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint* 🧩
- 🧭 *MARKDOWN_GUIDE_v13* (pipeline ordering, governance, STAC/DCAT/PROV alignment) 🏗️
- 🧠 *Data Spaces* (data ecosystems, access control patterns, governance) 🔐
- 🛰️ *Cloud-Based Remote Sensing with Google Earth Engine* (remote sensing workflows & dataset patterns) ☁️
- ⏳ *Visualization of Time-Oriented Data* (spatiotemporal/time-series analysis & visualization ideas) 🕰️

---