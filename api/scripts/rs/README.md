# 🛰️ Remote Sensing Scripts (`api/scripts/rs`)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2b6cb0)
![Remote Sensing](https://img.shields.io/badge/Domain-Remote%20Sensing%20%26%20EO-0ea5e9)
![STAC](https://img.shields.io/badge/Metadata-STAC-22c55e)
![DCAT](https://img.shields.io/badge/Metadata-DCAT-16a34a)
![PROV](https://img.shields.io/badge/Lineage-W3C%20PROV-8b5cf6)
![COG](https://img.shields.io/badge/Rasters-COG%20ready-f59e0b)
![Parquet](https://img.shields.io/badge/Tables-Parquet-64748b)

> **What this folder is:** API-adjacent scripts for **Remote Sensing / Earth Observation (RS/EO)** workflows in the Kansas Frontier Matrix (KFM).  
> **What “done” means:** a dataset is only “published” when the **data artifact + STAC + DCAT + PROV** boundary artifacts exist, pass validation, and are promoted atomically ✅

---

## 🧭 Quick Jump

- [🎯 Responsibilities](#-responsibilities)
- [📦 The KFM “boundary artifacts” contract](#-the-kfm-boundary-artifacts-contract)
- [🚀 Running scripts](#-running-scripts)
- [🧾 Provenance-first outputs](#-provenance-first-outputs)
- [🧪 Validation checklist](#-validation-checklist)
- [🔐 Security, ethics, governance](#-security-ethics-governance)
- [🧩 Add a new RS script](#-add-a-new-rs-script)
- [📚 Project Library (all project files)](#-project-library-all-project-files)

---

## 🎯 Responsibilities

These scripts exist to turn raw RS/EO sources into **KFM-grade** products:

- 🛰️ **Compute derived layers** (e.g., NDVI/NDWI/NDBI, composites, classifications, change/anomaly products)
- 🧱 **Export in scalable formats** (COGs for rasters, Parquet/GeoParquet for tables, GeoJSON for small vectors)
- 🧾 **Emit catalogs + lineage**  
  - **STAC** item/collection
  - **DCAT** dataset JSON-LD
  - **PROV** lineage bundle (machine-readable provenance)
- 🧠 **Make results “API-ready”** (clean contracts, stable identifiers, safe defaults, optional redaction)

---

## 📦 The KFM “boundary artifacts” contract

KFM treats metadata + provenance as *first-class outputs*.

### ✅ Non‑negotiables (for every RS script)

- [ ] **Declared Inputs/Outputs** (no hidden side effects; outputs are discoverable & repeatable)
- [ ] **Deterministic & reproducible** (same inputs + same code commit ⇒ same results)
- [ ] **Schema & bounds validation** (Kansas bounds where appropriate; sane ranges; correct CRS)
- [ ] **License + attribution captured** (source, author, terms, citations)
- [ ] **Provenance emitted** (W3C PROV with run parameters + code version + inputs used)
- [ ] **Atomic publish** (stage → validate → publish; no half-published datasets)
- [ ] **Idempotency** (support `--run-id` / `--idempotency-key` patterns so replays are safe)

---

## 🗂️ Suggested folder map 🧩

> Your actual contents may vary — this is the recommended structure to keep scripts composable and testable.

```text
📦 api/
 └─ 🧪 scripts/
    └─ 🛰️ rs/
       ├─ 📄 README.md                 👈 you are here
       ├─ 🧠 _lib/                     (shared helpers)
       │  ├─ gee.py                    (Earth Engine helpers, optional)
       │  ├─ raster.py                 (COG/warp/QA helpers)
       │  ├─ stac.py                   (STAC emit/validate helpers)
       │  ├─ dcat.py                   (DCAT JSON-LD emit helpers)
       │  └─ prov.py                   (PROV bundle emit helpers)
       ├─ 🧾 pipelines/                (script entrypoints)
       │  ├─ ndvi_county.py
       │  ├─ ndwi_water.py
       │  ├─ landcover_dynamic_world.py
       │  └─ change_detection.py
       └─ 🧪 tests/                    (fast checks; schema + smoke)
```

---

## 🚀 Running scripts

### 1) Discover what’s available

```bash
ls api/scripts/rs
# or
find api/scripts/rs -maxdepth 2 -type f -name "*.py"
```

### 2) Run a script (two common patterns)

```bash
# pattern A: direct file execution
python api/scripts/rs/pipelines/<script>.py --help

# pattern B: module execution (preferred if packaged)
python -m api.scripts.rs.pipelines.<script> --help
```

### 3) A realistic example (NDVI by county)

```bash
python api/scripts/rs/pipelines/ndvi_county.py \
  --aoi data/processed/boundaries/kansas_counties.geojson \
  --start 2022-07-01 \
  --end 2022-07-31 \
  --sensor landsat \
  --out data/work/rs/ndvi_county__2022-07.parquet \
  --publish
```

> 💡 Tip: **Default to “dry-run”** behavior unless `--publish` is explicitly set.

---

## ⚙️ Configuration (env vars) 🧰

| Variable | Purpose | Example |
|---|---|---|
| `KFM_ENV` | runtime environment | `dev` / `prod` |
| `KFM_DATA_DIR` | base data directory | `data` |
| `KFM_RAW_DIR` | raw inputs root | `data/raw` |
| `KFM_WORK_DIR` | staging/work outputs | `data/work` |
| `KFM_PROCESSED_DIR` | published outputs | `data/processed` |
| `KFM_STAC_DIR` | STAC output root | `data/stac` |
| `KFM_DCAT_DIR` | DCAT output root | `data/catalog/dcat` |
| `KFM_PROV_DIR` | provenance output root | `data/prov` |
| `KFM_RUN_ID` | stable run UUID (optional) | `2026-01-12T...` |
| `KFM_IDEMPOTENCY_KEY` | safe replay key (optional) | `rs-ndvi-ks-2022-07` |
| `KFM_POSTGIS_URL` | PostGIS connection (optional) | `postgresql://...` |
| `KFM_NEO4J_URL` | Graph connection (optional) | `neo4j://...` |
| `KFM_GEE_PROJECT` | Earth Engine project (optional) | `my-gee-project` |
| `KFM_GEE_CREDENTIALS` | EE creds path (optional) | `/secrets/gee.json` |

---

## 🧾 Provenance-first outputs

KFM wants outputs that are **traceable years later**.

### 📌 Expected outputs per published dataset

```text
📦 data/processed/rs/<dataset_id>/        ✅ final “user-facing” artifacts
 ├─ 🗺️ <dataset_id>.tif                   (COG raster)  OR
 ├─ 🧮 <dataset_id>.parquet               (table)       OR
 └─ 🧩 <dataset_id>.geojson               (small vector)

📦 data/stac/items/rs/<dataset_id>.json   ✅ STAC Item
📦 data/catalog/dcat/<dataset_id>.jsonld  ✅ DCAT Dataset
📦 data/prov/<dataset_id>.jsonld          ✅ PROV lineage bundle
```

### 🧬 Minimal PROV fields we expect

- **Entities:** inputs (source collections, AOIs), outputs (COG/Parquet), intermediate work artifacts (optional)
- **Activities:** “compute NDVI”, “mask clouds”, “reduce time series”, “export”, “validate”, “publish”
- **Agents:** script name + git SHA, user or CI bot, optional external service (Earth Engine)

<details>
  <summary>🧾 Example: “script contract header” (copy/paste template)</summary>

```yaml
# --- kfm:script ---
id: rs__ndvi_county__monthly
title: "NDVI by county (monthly)"
description: >
  Computes per-county NDVI summary statistics for Kansas using a chosen sensor
  and date range, then publishes a Parquet table + STAC/DCAT/PROV.
inputs:
  - aoi: "data/processed/boundaries/kansas_counties.geojson"
  - sensor: "landsat|sentinel2"
  - date_range: ["YYYY-MM-DD", "YYYY-MM-DD"]
  - compute_backend: "local|gee"
outputs:
  - data: "data/processed/rs/<dataset_id>/<dataset_id>.parquet"
  - stac_item: "data/stac/items/rs/<dataset_id>.json"
  - dcat: "data/catalog/dcat/<dataset_id>.jsonld"
  - prov: "data/prov/<dataset_id>.jsonld"
validation:
  - "schema: parquet columns/types"
  - "bounds: Kansas"
  - "license: required"
determinism:
  - "run_id + git_sha + params → stable dataset_id"
publish:
  - "atomic promote from data/work → data/processed"
# --- /kfm:script ---
```

</details>

---

## 🧪 Validation checklist

### 🔎 Fast-fail checks (before heavy compute)

- ✅ parameters parse + defaults
- ✅ AOI loads + valid geometry
- ✅ date range sane (start < end)
- ✅ backend creds present if required (e.g., GEE)
- ✅ output location writable

### 🧠 RS-specific QA (after compute, before publish)

- ✅ nodata ratio under threshold (configurable)
- ✅ expected band names / column names
- ✅ value ranges plausible (e.g., NDVI ∈ [-1, 1])
- ✅ spatial bounds not outside Kansas (unless explicitly allowed)
- ✅ CRS recorded correctly in outputs + STAC

### 📦 Publish gate

- ✅ data artifact exists (COG/Parquet/etc.)
- ✅ STAC Item exists + references assets
- ✅ DCAT exists + matches dataset id + license
- ✅ PROV exists + references run + inputs + script version
- ✅ publish is atomic (no partial datasets)

---

## 🛰️ Earth Engine patterns (optional backend)

> If you use GEE here, keep the pipeline **server-side**, avoid pulling huge data to the client, and treat exports as **jobs**.

**Recommended patterns:**
- ✅ process small AOIs first (debug quickly)
- ✅ avoid `.getInfo()` loops on large collections
- ✅ record dataset IDs, date ranges, and parameters in metadata
- ✅ export results + bring back only the product (COG/table) + metadata

---

## 🧊 Raster performance notes (COGs + tiles)

Remote sensing rasters get big fast. Preferred output strategies:

- 🧱 **COGs** for random access (HTTP range requests)
- 🧩 **pre-generated tiles** for common baselayers / heavy rasters
- 🗃️ keep **raw** vs **processed** separate (and don’t accidentally “publish” raw)
- ⚡ parallelize by scene, year, or tile (within backend limits)

---

## 🔐 Security, ethics, governance

### 🛡️ Security basics (don’t skip)
- 🔑 secrets only via env vars / secret mounts (never commit credentials)
- 🧼 sanitize all user-controlled inputs (paths, dataset IDs, SQL parameters)
- 🧾 log with a **trace id** (and keep logs clean of secrets)

### 🤝 Ethical data handling (FAIR/CARE vibes)
- 🧭 be explicit about license, attribution, and reuse conditions
- 🧯 protect sensitive locations / PII: aggregate, redact, or restrict outputs when needed
- 🔍 keep provenance transparent: *who/what/when/how produced the dataset*

### 🧬 Supply chain & automation (CI-friendly)
- ✅ prefer workflows that open PRs for changes (human review)
- ✅ attach SBOM/provenance attestations where supported
- ✅ keep a “kill switch” config for automated executors

---

## 🧩 Add a new RS script

### ✅ Checklist (copy/paste)

- [ ] Create entrypoint in `api/scripts/rs/pipelines/<name>.py`
- [ ] Add a **contract header** (inputs/outputs/validation/determinism)
- [ ] Implement `--dry-run` and `--publish`
- [ ] Write to `data/work/rs/...` first
- [ ] Validate (schema/bounds/ranges/license)
- [ ] Emit STAC/DCAT/PROV to canonical folders
- [ ] Promote atomically to `data/processed/rs/...`
- [ ] Add a smoke test in `api/scripts/rs/tests/`
- [ ] Document the dataset ID scheme + examples in this README or a sibling doc

---

## 📚 Project Library (all project files)

> These are the “reference shelf” documents available in this project. RS scripts should borrow patterns from them (performance, metadata rigor, modeling discipline, security hygiene, and human-centered governance).

<details>
  <summary>🛰️ Remote Sensing, EO, Geospatial</summary>

- **Cloud-Based Remote Sensing with Google Earth Engine – Fundamentals and Applications** 📘  
- **python-geospatial-analysis-cookbook** 🐍🗺️  
- **making-maps-a-visual-guide-to-map-design-for-gis** 🎨🗺️  
- **Mobile Mapping: Space, Cartography and the Digital** 📱🧭  

</details>

<details>
  <summary>🗃️ Data, Databases, Scale, Systems</summary>

- **PostgreSQL Notes for Professionals** 🐘  
- **Scalable Data Management for Future Hardware** ⚡🧠  
- **Data Spaces** 🌐📦  

</details>

<details>
  <summary>📊 Statistics, ML, Analytics</summary>

- **Understanding Statistics & Experimental Design** 🧪📈  
- **regression-analysis-with-python** 🐍📉  
- **Regression analysis using Python (slides)** 🎞️📉  
- **think-bayes-bayesian-statistics-in-python** 🧠🎲  
- **graphical-data-analysis-with-r** 📊🧾  

</details>

<details>
  <summary>🧪 Modeling, Simulation, Optimization, Graphs</summary>

- **Scientific Modeling and Simulation: A Comprehensive NASA-Grade Guide** 🚀🧪  
- **Generalized Topology Optimization for Structural Design** 🏗️🧩  
- **Spectral Geometry of Graphs** 🕸️📐  

</details>

<details>
  <summary>🧑‍⚖️ Ethics, Humanism, Policy</summary>

- **Introduction to Digital Humanism** 🤝🌍  
- **Principles of Biological Autonomy** 🧬🧠  
- **On the path to AI Law’s prophecies... (conceptual foundations of the ML age)** ⚖️🤖  

</details>

<details>
  <summary>🛡️ Security & Hardening</summary>

- **ethical-hacking-and-countermeasures-secure-network-infrastructures** 🛡️🕵️  
- **Gray Hat Python (2009)** 🐍🧨  
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp** 🖼️🗜️  

</details>

<details>
  <summary>🌐 UI / Web / Visualization</summary>

- **responsive-web-design-with-html5-and-css3** 📱💻  
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl** 🧊🖥️  

</details>

<details>
  <summary>📚 Programming Compendiums (A–X)</summary>

- **A programming Books** 📚 A  
- **B-C programming Books** 📚 B–C  
- **D-E programming Books** 📚 D–E  
- **F-H programming Books** 📚 F–H  
- **I-L programming Books** 📚 I–L  
- **M-N programming Books** 📚 M–N  
- **O-R programming Books** 📚 O–R  
- **S-T programming Books** 📚 S–T  
- **U-X programming Books** 📚 U–X  

</details>

<details>
  <summary>📜 Core KFM docs</summary>

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** 🧭📘  
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals** 💡🧬  

</details>

---

## 🧷 Glossary (tiny but useful)

- **RS/EO**: Remote Sensing / Earth Observation  
- **COG**: Cloud-Optimized GeoTIFF (efficient partial reads)  
- **STAC**: SpatioTemporal Asset Catalog (geospatial metadata standard)  
- **DCAT**: Data Catalog Vocabulary (catalog/discovery standard)  
- **PROV**: W3C Provenance model (lineage/audit trails)  
- **AOI**: Area of Interest  
- **Zonal stats**: aggregations over polygons (counties, watersheds, etc.)

---

## ✅ Done means…

A script is “KFM-complete” when it can be run by anyone (with the same inputs), produces the same outputs, passes validation, and publishes data + STAC + DCAT + PROV as a cohesive, auditable dataset. 🧾✨

