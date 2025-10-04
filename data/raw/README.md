<div align="center">

# 🗃️ Kansas Frontier Matrix — Raw Data Directory  
`data/raw/`

**Mission:** Store and document all **immutable, original datasets** downloaded or collected  
from verified external sources — providing the foundational inputs for every ETL,  
validation, and scientific workflow in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/raw/` directory contains **original, unmodified data** acquired from  
registered external sources (see `data/sources/`).  
These files represent the **ground truth** for all downstream transformations and analyses.

Key characteristics of raw data in KFM:
- Immutable — no editing, cleaning, or reformatting  
- Reproducible — every file linked to a documented manifest in `data/sources/`  
- Traceable — origin, license, and retrieval method are logged  
- Validated — checksum and metadata captured at acquisition  

> ⚠️ **Do not modify these files.**  
> If updates are needed, acquire new data through the pipeline and update its manifest.

---

## 🗂️ Directory Layout

```bash
data/raw/
├── README.md
├── terrain/             # LiDAR DEMs, USGS 3DEP data
│   ├── ks_3dep_tiles.zip
│   └── lidar_tile_index.geojson
├── hydrology/           # NHD, WBD, NFHL datasets
│   ├── nhd_flowlines.zip
│   ├── wbd_huc12.zip
│   └── fema_nfhl.zip
├── landcover/           # NLCD, CDL, and vegetation maps
│   ├── nlcd_1992_2021.zip
│   └── usda_cdl_2020.tif
├── climate/             # Daymet, NOAA, and Drought Monitor data
│   ├── daymet_1980_2024.nc
│   ├── noaa_normals_1991_2020.csv
│   └── drought_monitor_2000_2025.zip
├── hazards/             # Tornado, flood, wildfire, drought source data
│   ├── noaa_storm_events.csv
│   ├── usgs_wildfire_perimeters.zip
│   └── fema_flood_events.geojson
├── tabular/             # Census, USDA, BEA, BLS tabular data
│   ├── census_population_1860_2020.csv
│   ├── usda_agriculture_production.csv
│   └── bea_economic_indicators.csv
└── text/                # OCR documents, transcripts, treaties, newspapers
    ├── loc_chronicling_america.zip
    ├── kshs_oral_histories.json
    └── yale_avalon_treaties.txt
````

> **Note:**
> Each subdirectory mirrors the project’s data domain structure (`terrain`, `hydrology`, `landcover`, etc.)
> and directly corresponds to a manifest in `data/sources/`.

---

## ⚙️ Acquisition Workflow

All raw datasets are fetched via automated ETL pipelines using their **source manifests**.

**Makefile target:**

```bash
make fetch-raw
```

**Python command:**

```bash
python src/utils/fetch_data.py --manifest data/sources/hydrology/usgs_nhd_flowlines.json
```

**Workflow Steps:**

1. Validate source manifest (`data/sources/*.json`).
2. Fetch data via API, FTP, or HTTPS as specified.
3. Store in `data/raw/<domain>/` using standardized filenames.
4. Generate `.sha256` hash and metadata record.
5. Log acquisition in `data/checksums/` and `data/sources/`.

---

## 🧾 Raw Data Metadata Schema

| Field              | Description                            | Example                    |
| :----------------- | :------------------------------------- | :------------------------- |
| `source_id`        | Reference to the source manifest ID.   | `usgs_3dep_dem`            |
| `retrieved_on`     | Acquisition timestamp.                 | `2025-10-04T12:30:00Z`     |
| `checksum`         | SHA-256 integrity hash.                | `b8494a...3b61cb6ac8d`     |
| `file_size`        | File size in MB.                       | `1420.5`                   |
| `license`          | Data usage license.                    | `Public Domain (US Govt)`  |
| `retrieval_method` | Method used for acquisition.           | `REST API`, `FTP`, `HTTP`  |
| `linked_pipeline`  | ETL script responsible for processing. | `terrain_pipeline.py`      |
| `notes`            | Additional metadata or warnings.       | `Downloaded via USGS API.` |

---

## 🧩 Integration with KFM Pipelines

| Linked Component              | Purpose                                               |
| :---------------------------- | :---------------------------------------------------- |
| `data/sources/`               | Defines provenance and metadata for each raw dataset. |
| `src/pipelines/*`             | Processes raw data into standardized outputs.         |
| `data/processed/`             | Stores cleaned, validated, and derived products.      |
| `data/checksums/`             | Verifies the integrity of downloaded files.           |
| `.github/workflows/fetch.yml` | Automates fetching and validation in CI/CD.           |

---

## 🧹 Cleanup & Validation

Raw datasets should remain **immutable**, but may be revalidated or refreshed when sources are updated.

**Revalidate checksums:**

```bash
make validate-raw
```

**Re-fetch updated data:**

```bash
make fetch-raw-refresh
```

**Manual cleanup (rarely used):**

```bash
rm -rf data/raw/<domain>/*
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                       |
| :---------------------- | :------------------------------------------------------------------- |
| **Documentation-first** | README defines structure, purpose, and workflow for raw data.        |
| **Reproducibility**     | All files fetched deterministically using `data/sources/` manifests. |
| **Open Standards**      | Uses open data formats and public APIs only.                         |
| **Provenance**          | Every dataset traceable to its source manifest and checksum.         |
| **Auditability**        | CI/CD workflows log acquisition events and verification results.     |

---

## 📎 Related Directories

| Path                       | Description                                             |
| :------------------------- | :------------------------------------------------------ |
| `data/sources/`            | Source manifests defining dataset origins and metadata. |
| `data/checksums/`          | Integrity validation for raw and processed files.       |
| `data/processed/`          | Cleaned, validated datasets derived from raw inputs.    |
| `data/processed/metadata/` | STAC-compliant metadata linking raw sources to outputs. |

---

## 📅 Version History

| Version | Date       | Summary                                                            |
| :------ | :--------- | :----------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial raw data directory documentation and acquisition workflow. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Begins Here — Untouched, Immutable, and Proven.”*
📍 [`data/raw/`](.) · Archive of original datasets used to build the Kansas Frontier Matrix.

</div>
