<div align="center">

# ⚙️ Kansas Frontier Matrix — Cache Directory  
`data/work/cache/`

**Mission:** Provide a **local caching system** for intermediate data, derived results, and temporary assets  
used during ETL, validation, and build processes — optimizing performance and reproducibility  
within the Kansas Frontier Matrix (KFM) pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/cache/` directory serves as a **temporary storage layer**  
for cached intermediate datasets, downloaded assets, and re-usable results generated during ETL or analysis.  

Caching improves pipeline performance by:
- Reducing redundant network requests (e.g., repeated data downloads)  
- Minimizing computational overhead by reusing processed intermediates  
- Supporting reproducible, restartable ETL runs without recomputation  

All cache contents are **automatically generated**, **excluded from version control**, and **safe to delete**.  
They can be fully **reconstructed deterministically** through pipeline execution.

---

## 🗂️ Directory Layout

```bash
data/work/cache/
├── README.md
├── terrain/                 # Cached DEM tiles and hillshade intermediates
├── hydrology/               # Cached flowline, flood, or basin shape downloads
├── climate/                 # Cached precipitation and temperature NetCDF data
├── landcover/               # Cached NLCD and crop mask assets
├── tabular/                 # Cached CSV/Parquet files from repeated fetch operations
└── text/                    # Cached OCR or NLP preprocessing results
````

> **Note:** Cached files mirror the KFM data domain structure to maintain consistency
> and are regenerated automatically as needed during ETL runs.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                                          |
| :---------------------- | :----------------------------------------------------------------------------------- |
| **Ephemeral Caching**   | Files are temporary and excluded from version control.                               |
| **Performance Focused** | Cache enables faster ETL iteration by reusing intermediate results.                  |
| **Reproducibility**     | Cached data must be regenerable via `make` or pipeline scripts.                      |
| **Automatic Expiry**    | Cache is cleared during full rebuilds or after successful pipeline runs.             |
| **CI/CD Exclusion**     | This folder is ignored by continuous integration except for performance diagnostics. |

---

## ⚙️ Typical Use Cases

| Task                      | Example                                                             |
| :------------------------ | :------------------------------------------------------------------ |
| **Terrain Processing**    | Store DEM tiles and mosaics fetched from USGS 3DEP for reuse.       |
| **Hydrology ETL**         | Cache NHD flowline and WBD basin data to avoid redundant downloads. |
| **Climate Data Handling** | Temporarily retain large NetCDF grids from Daymet or NOAA.          |
| **Land Cover Analysis**   | Cache NLCD or USDA CDL data tiles for repeated sampling.            |
| **Text Processing**       | Hold OCR-preprocessed or tokenized corpora for NLP re-use.          |
| **Tabular QA**            | Cache cleaned but unvalidated CSV/Parquet files for later checks.   |

---

## 🧹 Cleanup Policy

Cache contents are routinely purged to ensure reproducibility and prevent disk bloat.

**Makefile target:**

```bash
make clean-cache
```

**Manual cleanup:**

```bash
rm -rf data/work/cache/*
```

To rebuild all pipelines from a clean slate:

```bash
make rebuild-all
```

> **Tip:** Removing cache files will increase ETL runtime temporarily but ensures full reproducibility.

---

## 🧩 Integration with KFM Pipelines

| Linked Component      | Purpose                                                             |
| :-------------------- | :------------------------------------------------------------------ |
| `src/pipelines/*`     | Uses cache to store temporary intermediate data between ETL stages. |
| `data/work/tmp/`      | Works in tandem with `/tmp/` for ephemeral processing.              |
| `.github/workflows/*` | Cache ignored in CI/CD except for ETL timing diagnostics.           |
| `data/checksums/`     | Final outputs validated independently of cache files.               |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | README clearly defines structure, purpose, and cleanup.          |
| **Reproducibility**     | Cached data always regenerable via deterministic pipelines.      |
| **Open Standards**      | Only open formats (GeoTIFF, CSV, JSON, Parquet, NetCDF).         |
| **Provenance**          | Cached outputs align directly with ETL logs and source datasets. |
| **Auditability**        | Cache access logged via pipeline logging for transparency.       |

---

## 📎 Related Directories

| Path              | Description                                        |
| :---------------- | :------------------------------------------------- |
| `data/work/tmp/`  | Temporary workspace for in-progress ETL artifacts. |
| `data/processed/` | Permanent, validated datasets and results.         |
| `data/checksums/` | Project-wide integrity validation records.         |
| `data/raw/`       | Immutable raw source data (original downloads).    |

---

## 📅 Version History

| Version | Date       | Summary                                                                          |
| :------ | :--------- | :------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial cache directory documentation created for reproducible ETL optimization. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Caching Time and Terrain for Reproducible Science.”*
📍 [`data/work/cache/`](.) · Temporary storage for ETL intermediates and reusable data artifacts.

</div>
