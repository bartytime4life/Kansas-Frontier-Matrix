<div align="center">

# 🧾 Kansas Frontier Matrix — **Climate ETL Logs**  
`data/work/tmp/climate/logs/`

**Mission:** Record **temporary ETL, transformation, and QA/QC logs** for climate datasets —  
capturing all operations on precipitation, temperature, drought, and climatological data  
to ensure full **traceability**, **transparency**, and **reproducibility** in the  
**Kansas Frontier Matrix (KFM)** data processing ecosystem.

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
title: "KFM • Climate ETL Logs (data/work/tmp/climate/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-climate"]
tags: ["climate","etl","logs","validation","temperature","precipitation","drought","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Interoperability & Traceability)
---
```

---

## 📚 Overview

The `data/work/tmp/climate/logs/` directory stores **temporary ETL and validation logs** generated  
during climate data transformation workflows. Each log file documents pipeline execution, schema validation,  
and QA/QC metrics for datasets derived from **NOAA**, **Daymet**, **Drought Monitor**, and **ERA5** sources.  

Logs record key events and metrics from every stage of the climate pipeline, including:

- Dataset extraction and reprojection (NetCDF → GeoTIFF → STAC)  
- Validation of temporal coverage and statistical ranges  
- Resampling and interpolation accuracy checks  
- Schema validation, checksum verification, and metadata generation  

All files are **ephemeral**, **excluded from version control**, and **automatically regenerated** on every pipeline run.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/climate/logs/
├── README.md
├── climate_etl_debug.log
├── noaa_normals_conversion.log
├── drought_monitor_validation.log
└── checksum_audit_report.log
```

> Filenames reflect pipeline context — e.g., “_conversion”, “_validation”, “_audit”.  
> Logs rotate or overwrite automatically between runs.

---

## ⚙️ Logging Schema & Standards

Logs follow a **consistent timestamped format** designed for audit and machine readability.

**Standard Line Schema**

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 message="free text"
```

**Example Entries**

```text
2025-10-16T13:10:01Z INFO climate.etl stage="init" dataset="NOAA_normals_1991-2020" message="Starting ETL pipeline"
2025-10-16T13:10:17Z INFO climate.reproject src_epsg=4326 dst_epsg=5070 method="bilinear" message="Reprojecting temperature grid"
2025-10-16T13:10:33Z WARNING climate.validate field="precip_mm" deviation=3.2 threshold=2.5 message="Value range exceeds climatological norm"
2025-10-16T13:10:49Z INFO climate.export file="noaa_temp_2020_cog.tif" format="COG" size_mb=48.6 message="Export completed successfully"
2025-10-16T13:11:04Z INFO climate.checksum file="noaa_temp_2020_cog.tif" sha256="f38b93..." result="match"
2025-10-16T13:11:09Z INFO climate.etl stage="complete" status="SUCCESS" duration_s=68.5
```

**Standards**

- UTF-8 plain-text, newline-terminated  
- ISO 8601 UTC timestamps  
- Component prefixes for filtering (`climate.etl`, `climate.reproject`, etc.)  
- Consistent field keys: `stage`, `dataset`, `file`, `status`, `sha256`, `result`

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
    filename: data/work/tmp/climate/logs/climate_etl_debug.log
    maxBytes: 2097152
    backupCount: 3
    encoding: utf-8
    formatter: default
loggers:
  kfm.climate:
    level: INFO
    handlers: [rotating]
    propagate: no
root:
  level: WARNING
  handlers: [rotating]
```

**Python Example**

```python
import logging
log = logging.getLogger("kfm.climate")
log.info('stage="init" dataset="DroughtMonitor_2024" message="Pipeline started"')
log.warning('field="precip_mm" deviation=4.8 message="Anomaly exceeds tolerance"')
```

---

## 🧾 Log Types & Purposes

| Log Type                         | Purpose                                                             |
| :------------------------------- | :------------------------------------------------------------------ |
| **`climate_etl_debug.log`**      | Full pipeline execution log (fetch, transform, export).             |
| **`noaa_normals_conversion.log`**| Tracks NetCDF to GeoTIFF conversions and reprojections.             |
| **`drought_monitor_validation.log`** | Validates PDSI/SPI index coverage and anomalies.                 |
| **`checksum_audit_report.log`**  | Verifies SHA-256 hashes and reproducibility consistency.            |

---

## 🧩 ETL Workflow Integration

**Makefile Target**

```bash
make climate
```

**Python CLI**

```bash
python src/pipelines/climate/climate_pipeline.py \
  --log data/work/tmp/climate/logs/climate_etl_debug.log
```

**Lifecycle Summary**

1. **Initialize:** Create logs and register pipeline configuration (dataset, CRS, commit).  
2. **Transform:** Capture ETL steps, reprojections, and conversions.  
3. **Validate:** Record schema, checksum, and QA results.  
4. **Finalize:** Append summary metrics and close logs.  

---

## 🧹 Cleanup Policy

Logs are **transient artifacts**, purged during or after successful ETL execution.

**Automated Cleanup**

```bash
make clean-logs
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/climate/logs/*
```

**Permanent Data Storage**

| Path | Description |
| :----| :----------- |
| `data/processed/climate/` | Final, validated climate datasets (precip, temp, drought). |
| `data/checksums/climate/` | SHA-256 manifests ensuring reproducibility. |
| `data/processed/metadata/climate/` | STAC metadata and provenance documentation. |

---

## 🔒 Security & Retention Policy

| Policy               | Implementation                                                             |
| :--------------------| :--------------------------------------------------------------------------|
| **Retention Period** | Logs retained for one ETL cycle or ≤7 days.                                |
| **Sensitive Data**   | Only metadata, metrics, and filenames are logged — never raw observations. |
| **Access Control**   | Logs are local only and excluded from Git.                                 |
| **Minimal Exposure** | Logs contain summary-level, non-identifiable data only.                    |

---

## 🧰 CI/CD Integration

| Component                             | Purpose                                                  |
| :------------------------------------ | :------------------------------------------------------- |
| `src/pipelines/climate/climate_pipeline.py` | Generates ETL, validation, and checksum audit logs.    |
| `.github/workflows/stac-validate.yml` | Consumes logs for schema and checksum QA testing.       |
| `data/work/tmp/climate/`              | Parent workspace for temporary ETL and QA intermediates. |
| `data/checksums/climate/`             | Tracks reproducibility validation manifests.             |
| `data/stac/climate/`                  | Maintains STAC metadata and lineage for climate data.    |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                            |
| :---------------------- | :------------------------------------------------------------------------ |
| **Documentation-first** | README defines structure, standards, and retention policies.              |
| **Reproducibility**     | Logs deterministically mirror ETL actions and validation outcomes.        |
| **Open Standards**      | UTF-8 plain text; ISO timestamps; FAIR metadata-compliant.                |
| **Provenance**          | Records dataset ID, CRS, source, and commit SHA for each operation.       |
| **Auditability**        | Structured, grep-friendly logs ensure transparent QA and CI/CD auditing.  |

---

## 📎 Related Directories

| Path                               | Description                                               |
| :--------------------------------- | :-------------------------------------------------------- |
| `data/work/tmp/climate/`           | Temporary workspace for ETL intermediates.                |
| `data/processed/climate/`          | Finalized climate datasets for publication.               |
| `data/checksums/climate/`          | Integrity manifests for reproducibility tracking.         |
| `data/processed/metadata/climate/` | STAC metadata for climate datasets and lineage records.   |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation for climate ETL log workspace.                  |
| **v1.2.0** | 2025-10-16 | Alignment pass: structured log schema, YAML metadata, FAIR compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Drop Logged. Every Anomaly Traced.”*  
📍 [`data/work/tmp/climate/logs/`](.) · Temporary ETL and QA logging workspace for climate datasets.

</div>
