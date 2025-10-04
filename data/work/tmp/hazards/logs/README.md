<div align="center">

# 🧾 Kansas Frontier Matrix — Hazards ETL Logs  
`data/work/tmp/hazards/logs/`

**Mission:** Store **temporary ETL and QA logs** generated during hazard data processing —  
including tornado, flood, wildfire, and drought datasets — to provide full traceability  
and diagnostic transparency within the Kansas Frontier Matrix (KFM) data pipeline.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/hazards/logs/` directory temporarily stores **pipeline and validation logs**  
created during hazard data ETL and QA workflows.  

These logs document:
- ETL steps for tornado, flood, wildfire, and drought data  
- CRS reprojection, resampling, and raster/vector conversion details  
- Checksum validation and STAC compliance test results  
- Diagnostic messages from hazard metadata generation  

Logs in this directory are **ephemeral**, **not version-controlled**, and **safe to delete**.  
All logs can be regenerated during subsequent ETL runs.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/hazards/logs/
├── README.md
├── hazards_etl_debug.log
├── flood_validation_report.log
├── wildfire_projection_test.log
└── drought_index_checksum_audit.log
````

> **Note:** The filenames above are examples.
> Actual logs depend on active ETL operations or debugging sessions.

---

## ⚙️ Logging Guidelines

| Log Type                      | Purpose                                                                         |
| :---------------------------- | :------------------------------------------------------------------------------ |
| **`*_etl_debug.log`**         | Records pipeline operations (file ingestion, reprojection, and export events).  |
| **`*_validation_report.log`** | Summarizes QA/QC results, STAC validation, and schema conformity checks.        |
| **`*_projection_test.log`**   | Logs reprojection accuracy and alignment diagnostics for spatial datasets.      |
| **`*_checksum_audit.log`**    | Captures checksum generation and comparison outcomes for reproducibility tests. |

All logs are stored as plain-text UTF-8 files for maximum portability and transparency.

---

## ⚙️ Log Generation Workflow

Logs are created automatically during hazard pipeline runs.

**Makefile target:**

```bash
make hazards
```

**Python command:**

```bash
python src/pipelines/hazards/hazards_pipeline.py --log data/work/tmp/hazards/logs/hazards_etl_debug.log
```

**Lifecycle:**

1. Pipeline initializes and begins writing logs in real time.
2. Each log documents key ETL and validation events.
3. Logs are reviewed for QA, CI/CD validation, or debugging.
4. Logs are cleared after successful execution or during cleanup.

---

## 🧹 Cleanup Policy

This directory is cleaned automatically during maintenance operations.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/hazards/logs/*
```

All validated hazard outputs are stored under:

* `data/processed/hazards/` — Final hazard data (GeoJSON/GeoTIFF)
* `data/checksums/hazards/` — SHA-256 checksum verification
* `data/processed/metadata/hazards/` — STAC metadata for hazard datasets

---

## 🧩 Integration with Pipelines

| Linked Component                            | Function                                             |
| :------------------------------------------ | :--------------------------------------------------- |
| `src/pipelines/hazards/hazards_pipeline.py` | Generates ETL and validation logs for hazard data.   |
| `.github/workflows/stac-validate.yml`       | References logs for checksum and schema diagnostics. |
| `data/work/tmp/hazards/`                    | Parent directory for temporary hazard ETL work.      |
| `data/processed/hazards/`                   | Stores validated and permanent hazard datasets.      |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                 |
| :---------------------- | :----------------------------------------------------------------------------- |
| **Documentation-first** | README defines purpose, structure, and cleanup of hazard logs.                 |
| **Reproducibility**     | Logs capture deterministic ETL steps for audit and regeneration.               |
| **Open Standards**      | Stored as plain UTF-8 text; no proprietary formats.                            |
| **Provenance**          | Logs establish traceable linkage between data processing and metadata outputs. |
| **Auditability**        | Logs ensure transparency and accountability in pipeline results.               |

---

## 📎 Related Directories

| Path                               | Description                                       |
| :--------------------------------- | :------------------------------------------------ |
| `data/work/tmp/hazards/`           | Temporary workspace for hazard ETL intermediates. |
| `data/processed/hazards/`          | Final processed hazard datasets.                  |
| `data/checksums/hazards/`          | Integrity hashes ensuring reproducibility.        |
| `data/processed/metadata/hazards/` | STAC metadata catalog for hazard data.            |

---

## 📅 Version History

| Version | Date       | Summary                                                                                  |
| :------ | :--------- | :--------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hazard ETL log documentation for tornado, flood, wildfire, and drought datasets. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Logging Every Storm, Fire, and Flood — Integrity in Every Line.”*
📍 [`data/work/tmp/hazards/logs/`](.) · Temporary ETL and QA logging workspace for hazard datasets.

</div>
