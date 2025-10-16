<div align="center">

# 🧾 Kansas Frontier Matrix — **Landcover ETL Logs**  
`data/work/tmp/landcover/logs/`

**Mission:** Capture **temporary ETL and QA/QC logs** produced during landcover data extraction,  
classification validation, reprojection, and integrity testing — ensuring **traceability**,  
**reproducibility**, and **auditability** across all landcover workflows in the  
**Kansas Frontier Matrix (KFM)** data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/badge/Container%20Scan-Secure-orange)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Landcover ETL Logs (data/work/tmp/landcover/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-environment"]
tags: ["landcover","etl","logs","validation","nlcd","vegetation","checksum","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Transparent Geospatial Workflows)
---
```

---

## 📚 Overview

The `data/work/tmp/landcover/logs/` directory stores **temporary ETL and QA logs** for  
landcover-related data pipelines. It captures every **processing, transformation, and validation step**  
executed by the KFM landcover subsystem.

Logs cover:

- Raster ingestion, reprojection, and mosaicking  
- Classification QA for vegetation, urban, barren, and water categories  
- Temporal landcover change detection (multi-decade NLCD or MODIS analysis)  
- Checksum audits and STAC metadata validation  

Each log entry supports **MCP-governed transparency** and can be regenerated deterministically through reproducible ETL workflows.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/landcover/logs/
├── README.md
├── landcover_etl_debug.log
├── classification_validation.log
├── reprojection_test.log
└── checksum_audit_report.log
```

> **Note:** Filenames are regenerated for each pipeline run and may vary depending on the ETL stage or domain process.

---

## ⚙️ Logging Schema & Standards

Logs are structured, timestamped, and standardized across KFM’s ETL framework.

**Standard Log Schema**

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 message="free text"
```

**Examples**

```text
2025-10-16T13:45:08Z INFO landcover.etl stage="init" dataset="NLCD_2021_KS" message="Starting ETL pipeline."
2025-10-16T13:45:19Z INFO landcover.reproject src_epsg=5070 dst_epsg=4326 method="bilinear" tile="tile_47"
2025-10-16T13:45:34Z WARNING landcover.validate class="forest" conf=0.72 threshold=0.80 message="low confidence classification"
2025-10-16T13:45:57Z INFO landcover.change from_year=1992 to_year=2021 change_pixels=542903 message="change-detection summary"
2025-10-16T13:46:18Z INFO landcover.checksum file="nlcd_2021_classified.tif" sha256="a8b37c..." result="match"
2025-10-16T13:46:24Z INFO landcover.etl stage="complete" status="SUCCESS" duration_s=76.2
```

**Policy**

- UTF-8 plain-text format  
- One entry per line, newline-terminated  
- Timestamp (ISO 8601, UTC) required  
- Keys standardized for CI parsing: `stage`, `status`, `result`, `file`, `dataset`

---

## 🔧 Logging Configuration Example

```yaml
version: 1
formatters:
  default:
    format: "%(asctime)s %(levelname)s %(name)s %(message)s"
handlers:
  rotating:
    class: logging.handlers.RotatingFileHandler
    filename: data/work/tmp/landcover/logs/landcover_etl_debug.log
    maxBytes: 2097152
    backupCount: 3
    encoding: utf-8
    formatter: default
loggers:
  kfm.landcover:
    level: INFO
    handlers: [rotating]
    propagate: no
root:
  level: WARNING
  handlers: [rotating]
```

**Python Implementation**

```python
import logging
log = logging.getLogger("kfm.landcover")
log.info('stage="init" dataset="NLCD_2021_KS" message="Starting ETL pipeline."')
log.warning('class="forest" conf=0.72 threshold=0.80 message="low confidence classification"')
```

---

## 🧾 Log Types & Functions

| Log File                        | Function                                                                 |
| :------------------------------ | :----------------------------------------------------------------------- |
| **`landcover_etl_debug.log`**   | Captures entire pipeline flow: load, transform, export.                  |
| **`classification_validation.log`** | Logs class-based metrics, confusion matrices, accuracy stats.         |
| **`reprojection_test.log`**     | Tracks CRS transformations and raster alignment QA.                      |
| **`checksum_audit_report.log`** | Records SHA-256 hash verification and reproducibility tests.             |

---

## 🧩 Lifecycle & Workflow

**Makefile Target**

```bash
make landcover
```

**Python CLI**

```bash
python src/pipelines/landcover/landcover_pipeline.py \
  --log data/work/tmp/landcover/logs/landcover_etl_debug.log
```

**ETL Lifecycle**

1. **Initialize** — Start ETL session, create debug log, register dataset metadata.  
2. **Transform** — Process reprojection, classification, and QA steps.  
3. **Validate** — Check schema, STAC, and checksum consistency.  
4. **Summarize** — Write QA metrics and status report.  
5. **Cleanup** — Rotate or delete logs per retention policy.  

---

## 🧹 Cleanup Policy

Logs are **temporary** and automatically purged at the start of new ETL cycles or via cleanup routines.

**Automated Cleanup**

```bash
make clean-logs
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/landcover/logs/*
```

**Permanent Outputs**

| Path | Description |
| :----| :----------- |
| `data/processed/landcover/` | Final processed and validated landcover rasters. |
| `data/checksums/landcover/` | Integrity manifests for reproducibility assurance. |
| `data/processed/metadata/landcover/` | STAC metadata and lineage documentation. |

---

## 🔒 Security & Retention Policy

| Policy              | Implementation                                                             |
| :------------------ | :-------------------------------------------------------------------------- |
| **Retention**       | Logs persist for one ETL session or ≤7 days by default.                     |
| **Sensitive Data**  | Do not log raw pixel values or classified sample IDs.                       |
| **Access Control**  | Logs remain local; not pushed to remote repositories.                       |
| **Anonymization**   | Model IDs and paths redacted for production QA logs.                        |

---

## 🧰 CI/CD Integration

| Component                                | Purpose                                                   |
| :-------------------------------------- | :-------------------------------------------------------- |
| `src/pipelines/landcover_pipeline.py`   | Generates, writes, and cleans ETL and QA logs.            |
| `.github/workflows/stac-validate.yml`   | Uses logs to validate STAC schemas and data lineage.      |
| `data/work/tmp/landcover/`              | Parent workspace for ETL and QA intermediates.            |
| `data/processed/landcover/`             | Hosts validated, permanent landcover outputs.             |
| `data/checksums/landcover/`             | Stores reproducibility verification hashes.               |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                             |
| :---------------------- | :------------------------------------------------------------------------- |
| **Documentation-first** | README describes scope, structure, and retention lifecycle.                |
| **Reproducibility**     | Log generation deterministic via pipeline configuration.                   |
| **Open Standards**      | UTF-8 text, timestamped schema, FAIR metadata compliance.                  |
| **Provenance**          | Logs include dataset ID, CRS, run ID, and commit SHA for lineage tracking. |
| **Auditability**        | Human-readable, grep-friendly logs ensure transparent QA validation.       |

---

## 📎 Related Directories

| Path                                 | Description                                         |
| :----------------------------------- | :-------------------------------------------------- |
| `data/work/tmp/landcover/`           | Temporary workspace for raster and classification.  |
| `data/processed/landcover/`          | Final, validated landcover datasets (NLCD, MODIS).  |
| `data/checksums/landcover/`          | Reproducibility manifests via SHA-256 hashes.       |
| `data/processed/metadata/landcover/` | STAC metadata and dataset documentation.            |

---

## 📅 Version History

| Version | Date       | Summary                                                                      |
| :------ | :--------- | :--------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-09 | Initial creation of landcover ETL log documentation workspace.              |
| **v1.2.0** | 2025-10-16 | Alignment pass: YAML front matter, structured schema, and retention policy. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Pixel Proven. Every Process Logged.”*  
📍 [`data/work/tmp/landcover/logs/`](.) · Temporary ETL logging workspace for landcover datasets.

</div>
