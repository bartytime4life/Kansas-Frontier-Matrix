---
title: "💾 Kansas Frontier Matrix — Hydrology TMP Cache (Preprocessed Data & Lookup Assets)"
path: "data/work/staging/tabular/normalized/hydrology/tmp/cache/README.md"
document_type: "Hydrology ETL · Temporary Cache and Preprocessing Layer"
version: "v2.0.0"
last_updated: "2025-10-25"
review_cycle: "Continuous / Nightly ETL"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v2.0.0/sbom.spdx.json"
manifest_ref: "releases/v2.0.0/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
owners: ["@kfm-data-engineering", "@kfm-hydrology"]
approvers: ["@kfm-validation", "@kfm-governance"]
status: "Active · FAIR+CARE+ISO Certified"
maturity: "Stable"
mcp_version: "MCP-DL v6.3"
tags: ["Hydrology", "TMP", "Cache", "ETL", "Data Pipeline", "FAIR", "Provenance", "Geospatial", "Preprocessing"]
---

<div align="center">

# 💾 Kansas Frontier Matrix — **Hydrology TMP Cache (Preprocessed Data & Lookup Assets)**  
`data/work/staging/tabular/normalized/hydrology/tmp/cache/README.md`

**Purpose:** Serve as the **temporary hydrological data cache** for preprocessed, cleaned, and geospatially aligned datasets prior to full ETL normalization.  
This layer accelerates repetitive hydrology workflows — e.g., streamflow extraction, aquifer depth interpolation, rainfall raster resampling — within the **Kansas Frontier Matrix (KFM)** ETL environment.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../docs/architecture/repo-focus.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Geospatial%20Metadata-yellow)]()
[![ETL Performance](https://img.shields.io/badge/ETL-Performance%20Optimized-green)]()
[![Status: Active](https://img.shields.io/badge/Status-Operational-brightgreen)]()

</div>

---

## 🗂️ Directory Layout

```plaintext
cache/
├── usgs_streamflow_cache.csv           # Cached streamflow station data (cleaned)
├── noaa_rainfall_cache.csv             # Processed rainfall records (daily aggregates)
├── kgs_aquifer_depth_cache.geojson     # Spatial cache of aquifer and groundwater data
├── hydro_lookup_tables.json            # Lookup dictionaries (station codes, hydrologic units)
├── crs_reference_cache.json            # Cached coordinate reference system transforms
├── qa_summary.json                     # Cache integrity validation report
├── manifest.json                       # Index of cached datasets and validity period
└── README.md                           # ← You are here
```

---

## 🧭 Overview

The **TMP Cache Layer** acts as an **accelerator and consistency buffer** for hydrology ETL workflows.  
It minimizes redundant computation by storing cleaned, formatted, and cross-referenced hydrological datasets between ETL runs.

### Objectives
- Enable **fast reloads** of intermediate hydrology data for iterative processing.  
- Maintain **geospatial consistency** across all temporary datasets (EPSG:4326 baseline).  
- Ensure **checksum-verified integrity** before reuse.  
- Support **FAIR data principles** — cached data are fully traceable and documented.  

This cache is automatically rebuilt **every 24 hours** or whenever raw hydrology sources (USGS, NOAA, KGS) update.

---

## ⚙️ Hydrology Cache Workflow

```mermaid
flowchart TD
    A["Raw Hydrology Sources (USGS, NOAA, KGS)"] --> B["Preprocessing Scripts (ETL Stage 0)"]
    B --> C["Hydrology TMP Cache (data/work/staging/tabular/normalized/hydrology/tmp/cache)"]
    C --> D["ETL Normalization Pipeline (Stage 1)"]
    D --> E["Validation & Provenance Stage"]
    E --> F["Governance Ledger Registration"]
```

---

## 🧩 Core Cached Assets

### 1️⃣ Streamflow Cache

**File:** `usgs_streamflow_cache.csv`

```csv
station_id,station_name,latitude,longitude,mean_discharge_cfs,last_updated
06866500,Arkansas River near Great Bend,38.34,-98.77,382,2025-10-25
07137500,Kansas River at Wamego,39.21,-96.29,512,2025-10-25
```

- Source: USGS NWIS API  
- Transformation: Unit normalization, coordinate validation, duplicate removal  
- Used by: `normalize_hydrology_data_v6.3`

---

### 2️⃣ NOAA Rainfall Cache

**File:** `noaa_rainfall_cache.csv`

```csv
station_id,date,total_precip_mm,avg_temp_c,source,last_updated
KS001,2025-10-24,8.2,13.5,NOAA,2025-10-25
