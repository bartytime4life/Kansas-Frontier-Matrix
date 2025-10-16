<div align="center">

# 🧾 Kansas Frontier Matrix — **Staging ETL & Validation Logs**  
`data/work/staging/logs/`

**Mission:** Capture **temporary ETL, validation, and promotion logs** generated during dataset transfer  
from processing to publication — ensuring full transparency, reproducibility, and lineage traceability  
within the **Kansas Frontier Matrix (KFM)** data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Staging ETL & Validation Logs (data/work/staging/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-validation"]
tags: ["staging","logs","etl","validation","promotion","checksum","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Transparency & Auditability)
---
```

---

## 📚 Overview

The `data/work/staging/logs/` directory houses **temporary validation and audit logs**  
produced while datasets transition from the ETL layer to the staging area for pre-publication checks.

Each log provides a detailed record of **integrity verification**, **STAC validation**, and **promotion events**,  
ensuring that all datasets meet MCP and FAIR standards before entering `data/processed/`.

**Key actions recorded include:**
- Checksum and integrity validation for incoming datasets  
- STAC and schema validation before catalog integration  
- Attribute, CRS, and structure consistency checks  
- Transfer operations and promotion diagnostics  

Logs are **ephemeral**, **excluded from Git**, and **automatically regenerated** during ETL and CI/CD validation cycles.

---

## 🗂️ Directory Layout

```bash
data/work/staging/logs/
├── README.md
├── staging_etl_debug.log
├── stac_validation_report.log
├── checksum_verification.log
└── promotion_audit.log
```

> **Note:** Filenames correspond to specific validation types or ETL events.  
> Logs are cleared after successful validation or promotion to processed datasets.

---

## ⚙️ Logging Schema & Conventions

All staging logs follow a **timestamped, machine- and human-readable structure**.

**Standard Format**

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 message="free text"
```

**Example Entries**

```text
2025-10-16T14:32:08Z INFO staging.etl stage="start" dataset="terrain_dem_2020" message="Initializing staging validation"
2025-10-16T14:32:27Z INFO staging.checksum file="terrain_dem_2020.tif" sha256="abf38e..." result="match"
2025-10-16T14:32:48Z INFO staging.stac schema="stac_item.json" result="valid" message="Metadata conforms to STAC 1.0.0"
2025-10-16T14:33:02Z WARNING staging.qa file="floodplain_mask.tif" issue="nodata mismatch" message="Correcting nodata values"
2025-10-16T14:33:21Z INFO staging.promote src="staging/terrain/" dst="processed/terrain/" result="success"
2025-10-16T14:33:23Z INFO staging.etl stage="complete" status="SUCCESS" duration_s=75.2
```

**Schema Guidelines**
- UTF-8 plain text  
- ISO 8601 UTC timestamps  
- One log entry per line (newline-terminated)  
- Consistent components: `staging.etl`, `staging.checksum`, `staging.stac`, `staging.promote`

---

## 🔧 Logging Configuration Example

```yaml
version: 1
formatters:
  line:
    format: "%(asctime)s %(levelname)s %(name)s %(message)s"
handlers:
  rotating:
    class: logging.handlers.RotatingFileHandler
    filename: data/work/staging/logs/staging_etl_debug.log
    maxBytes: 2097152
    backupCount: 3
    encoding: utf-8
    formatter: line
loggers:
  kfm.staging:
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
log = logging.getLogger("kfm.staging")
log.info('stage="checksum" dataset="climate_normals_1991-2020" result="valid"')
log.warning('dataset="hydrology_river_2020" issue="projection mismatch" message="EPSG correction applied"')
```

---

## 🧾 Log Types & Purposes

| Log File                       | Function                                                                 |
| :------------------------------ | :---------------------------------------------------------------------- |
| **`staging_etl_debug.log`**     | Captures staging-level ETL operations and data transfer events.         |
| **`stac_validation_report.log`**| Documents schema and metadata validation results for STAC conformance.  |
| **`checksum_verification.log`** | Logs hash generation and verification results for dataset integrity.    |
| **`promotion_audit.log`**       | Records dataset movements from staging → processed directories.         |

---

## 🧩 ETL & Validation Lifecycle

**Makefile Target**

```bash
make validate
```

**Python Invocation**

```bash
python src/pipelines/validate.py --log data/work/staging/logs/stac_validation_report.log
```

**Lifecycle Steps**

1. **Initialize:** Create and timestamp logs for validation events.  
2. **Validate:** Run schema, checksum, and STAC tests.  
3. **Audit:** Append promotion and movement logs post-verification.  
4. **Cleanup:** Purge logs after successful promotion or CI completion.  

---

## 🧹 Cleanup Policy

Logs are **transient** and cleared automatically or via scheduled maintenance.

**Automated Cleanup**

```bash
make clean-logs
```

**Manual Cleanup**

```bash
rm -rf data/work/staging/logs/*
```

**Permanent Storage**

| Directory | Purpose |
| :--------- | :------- |
| `data/processed/` | Final validated datasets and logs. |
| `data/checksums/` | Integrity manifests for reproducibility. |
| `data/stac/` | STAC 1.0.0-compliant metadata catalogs. |

---

## 🔒 Security & Governance

| Policy               | Implementation                                                        |
| :--------------------| :---------------------------------------------------------------------|
| **Access Control**   | Local-only artifacts, excluded from repository commits.               |
| **Retention Period** | Logs persist only until validation and promotion succeed.             |
| **Sensitive Data**   | Only metadata and metrics logged; no raw data contents.               |
| **Anonymization**    | Dataset identifiers use UUIDs or STAC IDs for audit compliance.       |

---

## 🧰 CI/CD Integration

| Linked Component                      | Purpose                                                     |
| :------------------------------------ | :----------------------------------------------------------- |
| `src/pipelines/validate.py`           | Writes checksum, schema, and promotion logs.                |
| `.github/workflows/stac-validate.yml` | Consumes logs for schema and checksum validation audits.    |
| `data/work/staging/`                  | Parent directory for datasets pending validation.           |
| `data/processed/`                     | Target location for promoted datasets.                      |
| `data/stac/`                          | References validated datasets for STAC ingestion.           |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                               |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | Defines lifecycle, governance, and audit policy for staging logs.            |
| **Reproducibility**     | Logs deterministically record each validation and transfer step.             |
| **Open Standards**      | UTF-8 text, ISO timestamps, and STAC/DCAT-aligned event structures.          |
| **Provenance**          | Each dataset’s log connects ETL origin → staging validation → promotion.     |
| **Auditability**        | Logs serve as verifiable records for CI/CD validation and QA review.         |

---

## 📎 Related Directories

| Path                 | Description                                          |
| :------------------- | :--------------------------------------------------- |
| `data/work/staging/` | Workspace for datasets pending validation.           |
| `data/processed/`    | Final validated datasets ready for publication.      |
| `data/checksums/`    | SHA-256 manifests for reproducibility verification.  |
| `data/stac/`         | STAC 1.0.0 catalog for discoverable data assets.     |

---

## 📅 Version History

| Version | Date       | Summary                                                         |
| :------ | :--------- | :-------------------------------------------------------------- |
| **v1.0.0** | 2025-10-09 | Initial staging ETL and validation log documentation created. |
| **v1.2.0** | 2025-10-16 | Upgraded to MCP-DL v6.2 alignment and full FAIR compliance.  |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Passes Through the Gate of Validation.”*  
📍 [`data/work/staging/logs/`](.) · Temporary validation and promotion log workspace.

</div>
