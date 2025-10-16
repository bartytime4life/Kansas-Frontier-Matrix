<div align="center">

# 💧 Kansas Frontier Matrix — **Hydrology ETL Logs**  
`data/work/tmp/hydrology/logs/`

**Mission:** Record and manage **temporary hydrologic ETL logs** produced during dataset ingestion,  
validation, and QA/QC — ensuring transparent, reproducible, and auditable workflows for streamflow,  
watershed, and groundwater datasets in the **Kansas Frontier Matrix (KFM)** ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Hydrology ETL Logs (data/work/tmp/hydrology/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-hydro"]
tags: ["hydrology","etl","logs","validation","watershed","streamflow","checksum","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Traceability & Auditability)
---
```

---

## 📚 Overview

The `data/work/tmp/hydrology/logs/` directory contains **transient ETL and validation logs**  
generated during hydrologic dataset processing — including rivers, aquifers, and watershed layers.  

These logs document the **entire hydrology data pipeline**, including:

- Stream gauge and discharge data extraction  
- CRS reprojection and hydrologic boundary harmonization  
- Raster and vector schema validation  
- Flow accumulation, model calibration, and QA metrics  
- Checksum and STAC metadata verification  

All files are **temporary**, **excluded from version control**, and **regenerated deterministically**  
on every pipeline execution (`make hydrology`).

---

## 🗂️ Directory Layout

```bash
data/work/tmp/hydrology/logs/
├── README.md
├── hydrology_etl_debug.log
├── watershed_validation_report.log
├── streamflow_cleaning.log
└── checksum_audit_report.log
```

> Filenames correspond to pipeline stages (e.g., `*_validation`, `*_cleaning`, `*_checksum`),  
> and are automatically rotated or replaced between runs.

---

## ⚙️ Logging Schema & Standards

Logs adhere to a **timestamped, structured text format** suitable for both human and machine reading.

**Example Line Format:**

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 message="free text"
```

**Example Entries:**

```text
2025-10-16T12:40:03Z INFO hydrology.etl stage="init" dataset="USGS_NWIS_2025" message="Pipeline started"
2025-10-16T12:40:09Z INFO hydrology.clean step="normalize" rows=15704 nulls_filled=83 message="Streamflow normalization complete"
2025-10-16T12:40:21Z WARNING hydrology.reproject src_epsg=5070 dst_epsg=4326 method="bilinear" message="Minor edge distortion detected"
2025-10-16T12:40:43Z INFO hydrology.validate file="watershed_huc12.geojson" result="PASS" message="Schema validated successfully"
2025-10-16T12:40:55Z INFO hydrology.checksum file="streamflow_cleaned.parquet" sha256="4a1f9e..." result="match"
2025-10-16T12:41:01Z INFO hydrology.etl stage="complete" status="SUCCESS" duration_s=58.3
```

**Rules:**

- UTF-8 encoded plain text  
- ISO 8601 timestamps  
- No color codes or special characters  
- One log entry per line  

---

## 🧾 Log Types & Purposes

| Log Type                          | Description                                                            |
| :-------------------------------- | :--------------------------------------------------------------------- |
| **`hydrology_etl_debug.log`**     | Primary ETL process trace (load → transform → validate → export).      |
| **`watershed_validation_report.log`** | Schema compliance, geometry, and metadata validation summaries.       |
| **`streamflow_cleaning.log`**     | Documents cleaning, normalization, and missing-data imputation steps.  |
| **`checksum_audit_report.log`**   | Records SHA-256 integrity checks and reproducibility validations.      |

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
    filename: data/work/tmp/hydrology/logs/hydrology_etl_debug.log
    maxBytes: 2097152
    backupCount: 3
    encoding: utf-8
    formatter: default
loggers:
  kfm.hydrology:
    level: INFO
    handlers: [rotating]
    propagate: no
root:
  level: WARNING
  handlers: [rotating]
```

**Python Implementation Example**

```python
import logging
log = logging.getLogger("kfm.hydrology")
log.info('stage="init" dataset="NWIS_KS" message="Pipeline initialized"')
log.warning('src_epsg=5070 dst_epsg=4326 message="Edge mismatch detected"')
```

---

## 🧩 Lifecycle & Workflow

**Makefile Target**

```bash
make hydrology
```

**Python CLI**

```bash
python src/pipelines/hydrology/hydrology_pipeline.py \
  --log data/work/tmp/hydrology/logs/hydrology_etl_debug.log
```

**Lifecycle Summary**

1. **Initialize:** Create debug log and record pipeline configuration.  
2. **Process:** Record extraction, reprojection, and normalization operations.  
3. **Validate:** Log schema checks, QA metrics, and checksum results.  
4. **Complete:** Summarize outcomes and cleanup temporary entries.  

---

## 🧹 Cleanup Policy

All hydrology logs are **temporary** and automatically purged during cleanup.

**Automated Cleanup**

```bash
make clean-logs
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/hydrology/logs/*
```

**Permanent Records**

| Path | Description |
| :----| :----------- |
| `data/processed/hydrology/` | Final hydrologic datasets (rivers, basins, flood zones). |
| `data/checksums/hydrology/` | Integrity verification manifests (SHA-256). |
| `data/processed/metadata/hydrology/` | STAC-compliant provenance metadata. |

---

## 🔒 Security & Retention Policy

| Rule                | Implementation                                                            |
| :------------------ | :------------------------------------------------------------------------ |
| **Retention**       | Logs persist for one ETL cycle (default ≤ 7 days).                        |
| **Sensitive Data**  | Raw coordinates and proprietary hydrologic models excluded from logs.      |
| **Access Control**  | Logs stored locally and excluded from GitHub repository tracking.          |
| **Minimal Exposure**| Capture parameters, metrics, and identifiers only — not full datasets.     |

---

## 🧰 CI/CD Integration

| Linked Component                            | Function                                                   |
| :------------------------------------------ | :--------------------------------------------------------- |
| `src/pipelines/hydrology/hydrology_pipeline.py` | Emits ETL and QA logs, manages rotation and cleanup.       |
| `.github/workflows/stac-validate.yml`       | Consumes logs for checksum, schema, and validation audits. |
| `data/work/tmp/hydrology/`                  | Parent workspace for hydrology ETL intermediates.          |
| `data/checksums/hydrology/`                 | Provides reproducibility verification manifests.           |
| `data/stac/hydrology/`                      | Maintains STAC Items for lineage and discovery.            |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README defines schema, workflow, and retention lifecycle.                   |
| **Reproducibility**     | Logs deterministically mirror pipeline steps and validation results.         |
| **Open Standards**      | UTF-8 plain text; timestamped and STAC/DCAT-compliant.                      |
| **Provenance**          | Entries include dataset ID, CRS, timestamps, and commit SHA.                |
| **Auditability**        | Logs ensure transparency and verifiable hydrology transformations.          |

---

## 📎 Related Directories

| Path                                 | Description                                               |
| :----------------------------------- | :-------------------------------------------------------- |
| `data/work/tmp/hydrology/`           | Temporary workspace for hydrology ETL intermediates.      |
| `data/processed/hydrology/`          | Final processed and validated hydrology datasets.         |
| `data/checksums/hydrology/`          | Reproducibility manifests for integrity checks.           |
| `data/processed/metadata/hydrology/` | STAC metadata and dataset documentation for hydrology.    |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-09 | Initial creation of hydrology ETL log documentation.                  |
| **v1.2.0** | 2025-10-16 | Upgraded: structured schema, YAML metadata, CI/CD, and FAIR alignment. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Stream Recorded. Every Drop Accounted For.”*  
📍 [`data/work/tmp/hydrology/logs/`](.) · Temporary ETL logging workspace for hydrologic datasets.

</div>
