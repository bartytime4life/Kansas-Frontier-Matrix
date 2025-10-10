<div align="center">

# 🧾 Kansas Frontier Matrix — Climate ETL Logs  
`data/work/tmp/climate/logs/`

**Mission:** Store **temporary log files** generated during climate ETL, transformation, validation,  
and QA/QC operations — providing transparency and traceability across the Kansas Frontier Matrix (KFM)  
climate data processing pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/climate/logs/` directory contains **ephemeral diagnostic logs**  
produced during the ETL and QA stages of climate datasets — including precipitation, temperature,  
drought indices, and NOAA climate normals.  

These logs help developers and CI/CD systems:
- Track ETL progress and runtime performance  
- Debug NetCDF conversions, reprojections, and metadata extraction  
- Record checksum and schema validation results  
- Document QA/QC steps before final publishing  

Logs are **transient**, **not version-controlled**, and **automatically regenerated**  
each time the climate ETL pipeline executes.

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

> **Note:** Filenames and contents vary by dataset and active ETL step.
> All files are replaced or cleared between pipeline runs.

---

## ⚙️ Logging Guidelines

| Log Type                   | Purpose                                                                         |
| :------------------------- | :------------------------------------------------------------------------------ |
| **`*_etl_debug.log`**      | Captures the full ETL process — download, reprojection, transformation, export. |
| **`*_conversion.log`**     | Records NetCDF → GeoTIFF or CSV conversion diagnostics.                         |
| **`*_validation.log`**     | Summarizes QA/QC for precipitation, drought, or temperature products.           |
| **`*_checksum_audit.log`** | Lists hash comparisons to verify dataset reproducibility.                       |

All logs are plain-text **UTF-8** files for open review and long-term readability.

---

## ⚙️ Log Management Workflow

Logs are produced automatically during ETL runs and optionally via manual invocation.

**Makefile target**

```bash
make climate
```

**Python command**

```bash
python src/pipelines/climate/climate_pipeline.py --log data/work/tmp/climate/logs/climate_etl_debug.log
```

**Lifecycle**

1. Pipeline starts and initializes or overwrites log files.
2. Each ETL stage writes process details and validation results.
3. Logs are reviewed by developers and CI/CD validators.
4. Cleared automatically after QA completion or via `make clean-logs`.

---

## 🧹 Cleanup Policy

Logs are **temporary artifacts** and deleted between workflow executions.

**Makefile target**

```bash
make clean-logs
```

**Manual cleanup**

```bash
rm -rf data/work/tmp/climate/logs/*
```

Validated datasets and metadata reside in:

* `data/processed/climate/` — permanent climate rasters and tables
* `data/checksums/climate/` — integrity hashes for reproducibility
* `data/processed/metadata/climate/` — STAC metadata for dataset publication

---

## 🧩 Integration with Pipelines

| Linked Component                            | Function                                                  |
| :------------------------------------------ | :-------------------------------------------------------- |
| `src/pipelines/climate/climate_pipeline.py` | Generates ETL and QA logs during processing.              |
| `.github/workflows/stac-validate.yml`       | References logs for checksum and metadata validation.     |
| `data/work/tmp/climate/`                    | Parent directory for temporary climate data artifacts.    |
| `data/processed/climate/`                   | Destination for finalized and validated climate datasets. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | README defines log purpose, structure, and cleanup protocols.    |
| **Reproducibility**     | Log generation is deterministic and reproducible across runs.    |
| **Open Standards**      | UTF-8 text ensures cross-platform transparency.                  |
| **Provenance**          | Logs record timestamps, dataset lineage, and ETL stage metadata. |
| **Auditability**        | Logs guarantee traceability for QA, CI/CD, and checksum reviews. |

---

## 📎 Related Directories

| Path                               | Description                                               |
| :--------------------------------- | :-------------------------------------------------------- |
| `data/work/tmp/climate/`           | Temporary workspace for ETL and diagnostics.              |
| `data/processed/climate/`          | Validated climate datasets (Daymet, NOAA, Drought).       |
| `data/checksums/climate/`          | SHA-256 integrity checks for reproducibility tracking.    |
| `data/processed/metadata/climate/` | STAC metadata and dataset documentation for climate data. |

---

## 📅 Version History

| Version | Date       | Summary                                                 |
| :------ | :--------- | :------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial climate ETL log documentation created.          |
| v1.0.1  | 2025-10-09 | Added metadata, badges, provenance, and MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Drop Logged. Every Anomaly Traced.”*
📍 [`data/work/tmp/climate/logs/`](.) · Temporary ETL and QA logging workspace for climate datasets.

</div>
