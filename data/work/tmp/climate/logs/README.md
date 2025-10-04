<div align="center">

# 🧾 Kansas Frontier Matrix — Climate ETL Logs  
`data/work/tmp/climate/logs/`

**Mission:** Store **temporary log files** generated during climate ETL, transformation, validation,  
and QA/QC operations — providing transparency and traceability across the Kansas Frontier Matrix (KFM)  
climate data processing pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/climate/logs/` directory contains **ephemeral diagnostic logs**  
created during ETL and validation of climate-related datasets, including temperature, precipitation,  
drought indices, and NOAA climate normals.  

These logs help developers and CI/CD systems:
- Track ETL progress and processing duration  
- Debug NetCDF conversions and reprojection tasks  
- Record checksum and metadata validation reports  
- Audit temporary climate data transformations  

Logs are **not version-controlled** and are regenerated automatically each time pipelines run.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/climate/logs/
├── README.md
├── climate_etl_debug.log
├── noaa_normals_conversion.log
├── drought_monitor_validation.log
└── checksum_audit_report.log
````

> **Note:** Log names and contents vary based on current ETL tasks,
> diagnostic runs, or metadata validation sessions.

---

## ⚙️ Logging Guidelines

| Log Type                   | Purpose                                                                                      |
| :------------------------- | :------------------------------------------------------------------------------------------- |
| **`*_etl_debug.log`**      | Captures the complete ETL process, including file reads, transformations, and reprojections. |
| **`*_conversion.log`**     | Records raster or NetCDF-to-GeoTIFF conversion operations.                                   |
| **`*_validation.log`**     | Summarizes QA/QC checks for drought or temperature datasets.                                 |
| **`*_checksum_audit.log`** | Stores validation results comparing dataset hashes to reference checksums.                   |

All logs use plain-text UTF-8 format to ensure readability and cross-platform compatibility.

---

## ⚙️ Log Management Workflow

Logs are generated automatically during pipeline execution.

**Makefile target:**

```bash
make climate
```

**Python example:**

```bash
python src/pipelines/climate/climate_pipeline.py --log data/work/tmp/climate/logs/climate_etl_debug.log
```

**Lifecycle:**

1. ETL process starts → log file initialized or overwritten.
2. Key events (download, reprojection, aggregation, checksum) are streamed in real time.
3. Logs are used by developers or CI jobs for validation and review.
4. Logs are cleared automatically on cleanup or pipeline completion.

---

## 🧹 Cleanup Policy

Climate logs are **temporary** and can be safely deleted or automatically purged
once ETL operations have completed successfully.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/climate/logs/*
```

All pipeline-critical outputs are safely stored under:

* `data/processed/climate/` — finalized climate datasets
* `data/checksums/climate/` — integrity verification files
* `data/processed/metadata/climate/` — STAC metadata and documentation

---

## 🧩 Integration with Pipelines

| Linked Component                            | Function                                                       |
| :------------------------------------------ | :------------------------------------------------------------- |
| `src/pipelines/climate/climate_pipeline.py` | Writes ETL and validation logs during processing.              |
| `.github/workflows/stac-validate.yml`       | Uses logs for diagnostics in checksum validation.              |
| `data/work/tmp/climate/`                    | Parent temporary directory for all intermediate climate files. |
| `data/processed/climate/`                   | Final climate data products validated via logs.                |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | README defines logging structure, policies, and workflow integration. |
| **Reproducibility**     | Logs capture deterministic pipeline steps for full traceability.      |
| **Open Standards**      | Logs are plain UTF-8 text; no proprietary formats used.               |
| **Provenance**          | Each log captures ETL lineage between raw and processed datasets.     |
| **Auditability**        | Logs serve as transparent records for debugging and QA verification.  |

---

## 📎 Related Directories

| Path                               | Description                                            |
| :--------------------------------- | :----------------------------------------------------- |
| `data/work/tmp/climate/`           | Temporary workspace for climate ETL intermediates.     |
| `data/processed/climate/`          | Final climate outputs (Daymet, NOAA, drought indices). |
| `data/checksums/climate/`          | SHA-256 verification of processed datasets.            |
| `data/processed/metadata/climate/` | Metadata and STAC catalog for climate layers.          |

---

## 📅 Version History

| Version | Date       | Summary                                                       |
| :------ | :--------- | :------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial creation of climate ETL logs workspace documentation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Drop Logged. Every Anomaly Traced.”*
📍 [`data/work/tmp/climate/logs/`](.) · Temporary ETL and QA logging workspace for climate datasets.

</div>
