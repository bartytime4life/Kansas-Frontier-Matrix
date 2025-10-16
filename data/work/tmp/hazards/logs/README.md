<div align="center">

# 🧾 Kansas Frontier Matrix — **Hazards ETL Logs**  
`data/work/tmp/hazards/logs/`

**Mission:** Maintain **temporary ETL and QA/QC logs** for hazard datasets —  
including tornado tracks, floodplain rasters, wildfire perimeters, and drought indices —  
to ensure full **traceability**, **auditability**, and **reproducibility** across  
the **Kansas Frontier Matrix (KFM)** hazard data pipelines.

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
title: "KFM • Hazards ETL Logs (data/work/tmp/hazards/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-hazards"]
tags: ["hazards","etl","logs","validation","tornado","flood","wildfire","drought","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Traceability & Transparency)
---
```

---

## 📚 Overview

The `data/work/tmp/hazards/logs/` directory contains **temporary ETL and validation logs**  
produced during hazard dataset processing, quality assurance, and reproducibility audits.  

Each log captures stepwise details for **hazard domain workflows**, including:

- Tornado path ingestion, buffer creation, and reprojection  
- Floodplain raster validation and cross-checks against FEMA data  
- Wildfire perimeter rasterization and overlay testing  
- Drought index temporal interpolation and metadata verification  
- Checksum, schema, and STAC compliance validation  

Logs are **ephemeral**, **excluded from Git**, and **recreated deterministically** with each pipeline run.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/hazards/logs/
├── README.md
├── hazards_etl_debug.log
├── flood_validation_report.log
├── wildfire_projection_test.log
└── drought_index_checksum_audit.log
```

> Filenames follow their associated pipeline stage or hazard domain.  
> All logs are replaced or rotated automatically between runs.

---

## ⚙️ Logging Schema & Standards

Logs follow a **standardized timestamped text format**, enabling CI/CD parsing and human readability.

**Format:**

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 message="free text"
```

**Examples:**

```text
2025-10-16T13:45:01Z INFO hazards.etl stage="start" dataset="tornado_tracks_2024" message="Hazard ETL initialized"
2025-10-16T13:45:12Z INFO hazards.reproject src_epsg=5070 dst_epsg=4326 method="bilinear" result="ok"
2025-10-16T13:45:24Z WARNING hazards.validate type="polygon" issue="geometry overlap" file="flood_zone_2023.geojson"
2025-10-16T13:45:37Z INFO hazards.checksum file="wildfire_perimeter_2022.tif" sha256="a8e3d1..." result="match"
2025-10-16T13:45:52Z INFO hazards.etl stage="complete" status="SUCCESS" duration_s=51.2
```

**Logging Rules**

- Plain-text UTF-8 encoding  
- ISO 8601 UTC timestamps  
- One entry per line, newline-terminated  
- Prefix component namespace (`hazards.etl`, `hazards.validate`, etc.)  

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
    filename: data/work/tmp/hazards/logs/hazards_etl_debug.log
    maxBytes: 2097152
    backupCount: 3
    encoding: utf-8
    formatter: default
loggers:
  kfm.hazards:
    level: INFO
    handlers: [rotating]
    propagate: no
root:
  level: WARNING
  handlers: [rotating]
```

**Python Emission Example**

```python
import logging
log = logging.getLogger("kfm.hazards")
log.info('stage="start" dataset="tornado_tracks_2024" message="Pipeline started"')
log.warning('dataset="flood_extent_2023" issue="overlap" message="Validation warning"')
```

---

## 🧾 Log Types & Purposes

| Log File Name                 | Function                                                               |
| :-----------------------------| :----------------------------------------------------------------------|
| **`hazards_etl_debug.log`**   | Main ETL trace (file ingestion, transform, export).                    |
| **`flood_validation_report.log`** | Flood data QA: hydrologic model comparison, schema conformity.       |
| **`wildfire_projection_test.log`** | Wildfire CRS reprojection and vector-to-raster validation.          |
| **`drought_index_checksum_audit.log`** | Drought index reproducibility and checksum verification.        |

---

## 🧩 ETL Lifecycle & Workflow

**Makefile Target**

```bash
make hazards
```

**Python CLI**

```bash
python src/pipelines/hazards/hazards_pipeline.py \
  --log data/work/tmp/hazards/logs/hazards_etl_debug.log
```

**Lifecycle Summary**

1. **Initialize:** Create log files and record run metadata (commit SHA, run ID).  
2. **Process:** ETL steps append transformations, QA results, and schema checks.  
3. **Validate:** QA and checksum comparisons added to audit logs.  
4. **Cleanup:** Logs purged at next ETL cycle; validated data promoted to `processed/`.

---

## 🧹 Cleanup Policy

Logs are **temporary** and automatically purged during each pipeline execution or via cleanup routines.

**Automated Cleanup**

```bash
make clean-logs
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/hazards/logs/*
```

**Permanent Artifacts**

| Directory | Description |
| :--------- | :----------- |
| `data/processed/hazards/` | Final validated hazard datasets. |
| `data/checksums/hazards/` | SHA-256 integrity manifests for reproducibility. |
| `data/processed/metadata/hazards/` | STAC metadata and provenance records. |

---

## 🔒 Security & Retention Policy

| Policy               | Implementation                                                             |
| :--------------------| :--------------------------------------------------------------------------|
| **Retention**        | Logs retained for active session only; purged after pipeline completion.   |
| **Sensitive Data**   | No personal or proprietary content logged.                                 |
| **Access Control**   | Local-only; logs excluded from GitHub repository.                          |
| **Minimal Exposure** | Capture metrics and IDs only; omit full dataset content.                   |

---

## 🧰 CI/CD Integration

| Component                             | Function                                                |
| :------------------------------------ | :------------------------------------------------------ |
| `src/pipelines/hazards/hazards_pipeline.py` | Generates and manages ETL/QA logs for hazards.        |
| `.github/workflows/stac-validate.yml` | Uses logs for schema and checksum validation.          |
| `data/work/tmp/hazards/`              | Parent workspace for intermediate hazard datasets.     |
| `data/checksums/hazards/`             | Provides reproducibility verification manifests.       |
| `data/stac/hazards/`                  | Maintains STAC catalog of hazard datasets.             |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                            |
| :---------------------- | :------------------------------------------------------------------------ |
| **Documentation-first** | README defines log structure, workflow, and retention.                    |
| **Reproducibility**     | Logs mirror ETL and QA actions for each hazard dataset.                   |
| **Open Standards**      | UTF-8 text; ISO timestamps; STAC/DCAT metadata alignment.                 |
| **Provenance**          | Entries include dataset ID, CRS, run ID, and commit SHA.                  |
| **Auditability**        | Logs support transparent QA/QC review across hazard domains.              |

---

## 📎 Related Directories

| Path                               | Description                                            |
| :--------------------------------- | :----------------------------------------------------- |
| `data/work/tmp/hazards/`           | Temporary workspace for hazard ETL intermediates.      |
| `data/processed/hazards/`          | Final validated tornado, flood, wildfire, drought data.|
| `data/checksums/hazards/`          | Integrity verification and reproducibility tracking.   |
| `data/processed/metadata/hazards/` | STAC metadata documentation for hazard datasets.       |

---

## 📅 Version History

| Version | Date       | Summary                                                          |
| :------ | :--------- | :--------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial hazards ETL log documentation created.                 |
| **v1.2.0** | 2025-10-16 | Upgraded: YAML metadata, log schema, FAIR + MCP-DL v6.2 alignment. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Logging Every Storm, Fire, and Flood — Integrity in Every Line.”*  
📍 [`data/work/tmp/hazards/logs/`](.) · Temporary ETL and QA logging workspace for hazard datasets.

</div>
