<div align="center">

# 🧾 Kansas Frontier Matrix — Landcover ETL Logs  
`data/work/tmp/landcover/logs/`

**Mission:** Capture **temporary ETL and QA/QC logs** produced during landcover data extraction,  
classification validation, reprojection, and integrity testing — maintaining full transparency  
and traceability across the Kansas Frontier Matrix (KFM) landcover data workflows.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/landcover/logs/` directory contains **transient process logs**  
generated during the ETL and QA phases of landcover data integration.  

These logs document:
- Raster ingestion and reprojection steps  
- Classification checks for vegetation, urban, and water categories  
- Temporal change detection (multi-year landcover comparison)  
- STAC metadata validation and checksum verification  

All logs are **ephemeral**, **non-versioned**, and **automatically recreated**  
whenever the landcover pipeline (`make landcover`) runs.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/landcover/logs/
├── README.md
├── landcover_etl_debug.log
├── classification_validation.log
├── reprojection_test.log
└── checksum_audit_report.log
````

> **Note:** Example names represent typical ETL outputs — actual filenames depend on pipeline parameters.

---

## ⚙️ Logging Guidelines

| Log Type                      | Purpose                                                                 |
| :---------------------------- | :---------------------------------------------------------------------- |
| **`*_etl_debug.log`**         | Tracks full ETL execution — input reads, reprojection, tiling, and I/O. |
| **`*_validation.log`**        | Captures classification and cross-dataset consistency tests.            |
| **`*_reprojection_test.log`** | Logs CRS conversions and GDAL warp results for alignment checks.        |
| **`*_checksum_audit.log`**    | Lists hash verifications for reproducibility validation.                |

All logs use **UTF-8 plain-text** format for maximum accessibility and open review.

---

## ⚙️ Log Generation Workflow

Logs are created automatically during ETL execution and QA tests.

**Makefile target:**

```bash
make landcover
```

**Python command:**

```bash
python src/pipelines/landcover/landcover_pipeline.py --log data/work/tmp/landcover/logs/landcover_etl_debug.log
```

**Lifecycle:**

1. Pipeline initializes and writes new log files.
2. Processing stages append transformations and validation results.
3. Logs are used for diagnostics, QA validation, and CI/CD review.
4. Files are purged on cleanup or re-run.

---

## 🧹 Cleanup Policy

Logs in this directory are **temporary** and safely deletable after QA completion.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/landcover/logs/*
```

Permanent, validated outputs are located in:

* `data/processed/landcover/` — finalized landcover rasters
* `data/checksums/landcover/` — reproducibility hashes
* `data/processed/metadata/landcover/` — STAC metadata records

---

## 🧩 Integration with Pipelines

| Linked Component                                | Function                                            |
| :---------------------------------------------- | :-------------------------------------------------- |
| `src/pipelines/landcover/landcover_pipeline.py` | Generates ETL and QA logs for landcover processing. |
| `.github/workflows/stac-validate.yml`           | Reads logs for checksum validation and diagnostics. |
| `data/work/tmp/landcover/`                      | Parent workspace for temporary raster files.        |
| `data/processed/landcover/`                     | Stores validated and published landcover datasets.  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | Defines log scope, lifecycle, and purpose for the landcover ETL.      |
| **Reproducibility**     | Log generation is deterministic and reproducible under CI/CD.         |
| **Open Standards**      | UTF-8 text format, aligned to STAC and DCAT metadata frameworks.      |
| **Provenance**          | Each ETL step timestamped and recorded for lineage tracking.          |
| **Auditability**        | Logs support transparent QA and checksum verification before cleanup. |

---

## 📎 Related Directories

| Path                                 | Description                                         |
| :----------------------------------- | :-------------------------------------------------- |
| `data/work/tmp/landcover/`           | Temporary workspace for ETL raster processing.      |
| `data/processed/landcover/`          | Finalized landcover datasets (NLCD, MODIS, etc.).   |
| `data/checksums/landcover/`          | Hash verifications ensuring reproducibility.        |
| `data/processed/metadata/landcover/` | STAC metadata and documentation for landcover data. |

---

## 📅 Version History

| Version | Date       | Summary                                                        |
| :------ | :--------- | :------------------------------------------------------------- |
| v1.0    | 2025-10-09 | Initial creation of landcover ETL log documentation workspace. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Pixel Proven. Every Process Logged.”*
📍 [`data/work/tmp/landcover/logs/`](.) · Temporary ETL logging workspace for landcover datasets.

</div>
