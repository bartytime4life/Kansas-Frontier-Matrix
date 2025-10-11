<div align="center">

# 🧩 Kansas Frontier Matrix — Temporary Workspace  
`data/work/tmp/`

**Mission:** Provide a **controlled, short-term sandbox** for temporary files generated  
during ETL, validation, testing, and data transformation — enabling rapid experimentation,  
debugging, and reproducibility without contaminating long-term data directories.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/` directory is a **sandboxed environment** for short-lived, regenerable files  
created during **Kansas Frontier Matrix (KFM)** workflows.  
It supports validation, debugging, and QA operations that require intermediate data persistence  
without polluting the core repository with transient content.

Files here are **ephemeral**, automatically **excluded from version control**,  
and fully **reproducible** via Makefile or ETL targets.

### Primary Use Cases
- Intermediate ETL computations and testing  
- Checksum or metadata validation drafts  
- Previews and low-resolution test exports  
- Pipeline stress testing and profiling  
- Cache staging for ML/NLP data preparation  

---

## 🗂️ Directory Layout

```bash
data/work/tmp/
├── README.md
├── terrain/           # Temporary DEM, slope, and hillshade intermediates
├── hydrology/         # Watershed, river, or flood polygon staging
├── landcover/         # NLCD or vegetation classification intermediates
├── climate/           # Temperature, precipitation, and drought test data
├── hazards/           # Tornado, wildfire, or flood overlay test files
├── tabular/           # CSV or Parquet slices for schema validation
└── text/              # OCR/NLP intermediate text files and debug outputs
````

> **Note:** Subdirectories mirror the structure of `data/processed/` to maintain
> consistency between transient and finalized datasets.

---

## ⚙️ Usage Guidelines

| Policy                 | Description                                                                     |
| :--------------------- | :------------------------------------------------------------------------------ |
| **Ephemeral Only**     | Do not store permanent or official datasets here — all contents are disposable. |
| **Reproducible State** | All temporary artifacts must be regenerable via ETL or Makefile targets.        |
| **CI/CD Exclusion**    | Ignored by validation unless explicitly invoked in a test pipeline.             |
| **Logging Allowed**    | Temporary debug logs and cache files may safely reside here.                    |
| **Storage Discipline** | Keep individual files ≤ 1 GB to maintain manageable cleanup cycles.             |

---

## 🧩 Typical Use Cases

| Task                   | Example                                                       |
| :--------------------- | :------------------------------------------------------------ |
| **Raster Testing**     | Subsetting DEMs or flood rasters for validation.              |
| **STAC Previews**      | Generating metadata drafts before committing to `data/stac/`. |
| **Checksum Debugging** | Recomputing hashes for reproducibility testing.               |
| **Visualization QA**   | Rendering thumbnails and map tiles for review.                |
| **Pipeline Profiling** | Stress-testing ETL steps with small batch data.               |

---

## 🧹 Cleanup Policy

The contents of this directory are **not persistent** and may be deleted automatically or manually.

**Makefile Target:**

```bash
make clean-tmp
```

**Manual Command:**

```bash
rm -rf data/work/tmp/*
```

Cleanup is safe because all transient data can be regenerated
from the deterministic ETL pipelines (e.g., `make terrain`, `make hydrology`, `make climate`).

---

## 🧰 Integration with CI/CD and ETL Workflows

| Component            | Function                                                              |
| :------------------- | :-------------------------------------------------------------------- |
| `.github/workflows/` | CI may write or reference temporary outputs here for debug testing.   |
| `src/pipelines/*`    | ETL scripts use `tmp/` for intermediate transformations.              |
| `data/work/logs/`    | Logs cross-reference transient operations stored under `tmp/`.        |
| `data/checksums/`    | Checksum scripts use this directory for intermediate hash generation. |
| `data/stac/`         | Temporary STAC drafts validated here before publication.              |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                           |
| :---------------------- | :----------------------------------------------------------------------- |
| **Documentation-first** | This README defines usage scope, retention, and safe handling.           |
| **Reproducibility**     | Every file is regenerable through scripted ETL processes.                |
| **Open Standards**      | Temporary artifacts use open formats (COG, GeoJSON, CSV, JSONL).         |
| **Provenance**          | Domain-based subfolders maintain consistent lineage with final datasets. |
| **Auditability**        | Logs and debug artifacts allow inspection before cleanup.                |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Schedule `make clean-tmp` weekly in CI/CD to avoid space bloat.
2. **Validate Before Deletion:** Review `data/work/logs/` for active pipeline operations before purging.
3. **Tag for Debug:** Prefix temporary files with a date/time or ETL run ID for traceability.
4. **Avoid Manual Backups:** Nothing in this directory should require archiving; rely on reproducible builds.
5. **Monitor Size:** CI should alert if `tmp/` exceeds a 5 GB threshold to maintain build efficiency.

---

## 📎 Related Directories

| Path                 | Purpose                                               |
| :------------------- | :---------------------------------------------------- |
| `data/work/cache/`   | Persistent cache for recurring validation results.    |
| `data/work/staging/` | Transitional data awaiting promotion to `processed/`. |
| `data/work/logs/`    | Logs for ETL, validation, and QA processes.           |
| `data/processed/`    | Canonical, validated datasets for publication.        |

---

## 📅 Version History

| Version    | Date       | Summary                                                                          |
| :--------- | :--------- | :------------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation of temporary ETL scratch directory.                        |
| **v1.1.0** | 2025-10-10 | Expanded CI integration, maintenance best practices, and MCP compliance updates. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design, Reproducible by Principle.”*
📍 [`data/work/tmp/`](.) · Ephemeral sandbox for ETL debugging, validation, and QA testing.

</div>
```
