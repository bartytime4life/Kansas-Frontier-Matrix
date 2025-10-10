<div align="center">

# 🧾 Kansas Frontier Matrix — Tabular ETL Logs  
`data/work/tmp/tabular/logs/`

**Mission:** Store **temporary log files** generated during tabular ETL, validation, and QA/QC workflows —  
ensuring full transparency and traceability for census, agricultural, and economic datasets processed within  
the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/tabular/logs/` directory holds **transient ETL and validation logs**  
produced when tabular data (e.g., census, agricultural, or economic tables)  
is being processed, cleaned, normalized, or verified.  

These logs support:
- Schema and format validation of CSV and Parquet files  
- Quality control and unit consistency checks  
- Cross-decade statistical QA for time-series datasets  
- Checksum verification reports for reproducibility audits  

All logs are **ephemeral**, **excluded from version control**, and **automatically regenerated**  
with each tabular ETL execution.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/tabular/logs/
├── README.md
├── tabular_etl_debug.log
├── census_schema_validation.log
├── agriculture_cleaning_report.log
└── checksum_audit_report.log
````

> **Note:** Filenames and contents vary with each ETL or validation task.
> All files are auto-overwritten and excluded from persistent storage.

---

## ⚙️ Logging Guidelines

| Log Type                    | Purpose                                                               |
| :-------------------------- | :-------------------------------------------------------------------- |
| **`*_etl_debug.log`**       | Captures ETL stages — load, clean, transform, and export operations.  |
| **`*_validation.log`**      | Records schema validation, type checks, and unit consistency reports. |
| **`*_cleaning_report.log`** | Summarizes normalization routines, missing-data fills, and anomalies. |
| **`*_checksum_audit.log`**  | Details reproducibility and hash verification outcomes.               |

All logs are stored as **UTF-8 plain text** for portability and open review.

---

## ⚙️ Log Generation Workflow

Logs are generated automatically by KFM’s tabular ETL pipeline or may be invoked manually.

**Makefile target**

```bash
make tabular
```

**Python execution**

```bash
python src/pipelines/tabular/tabular_pipeline.py --log data/work/tmp/tabular/logs/tabular_etl_debug.log
```

**Lifecycle**

1. Pipeline starts and creates/overwrites log files.
2. ETL and validation steps append detailed output sequentially.
3. Logs assist QA analysts and CI/CD diagnostics.
4. Cleared automatically after successful runs or via cleanup command.

---

## 🧹 Cleanup Policy

Logs are temporary and purged between runs.

**Makefile target**

```bash
make clean-logs
```

**Manual cleanup**

```bash
rm -rf data/work/tmp/tabular/logs/*
```

Permanent, reproducible data reside in:

* `data/processed/tabular/` — finalized, validated tables
* `data/checksums/tabular/` — integrity verification hashes
* `data/processed/metadata/tabular/` — STAC metadata and schema docs

---

## 🧩 Integration with Pipelines

| Linked Component                            | Function                                                  |
| :------------------------------------------ | :-------------------------------------------------------- |
| `src/pipelines/tabular/tabular_pipeline.py` | Writes ETL, validation, and audit logs during processing. |
| `.github/workflows/stac-validate.yml`       | Consumes logs for schema and checksum QA diagnostics.     |
| `data/work/tmp/tabular/`                    | Parent temporary workspace for tabular intermediates.     |
| `data/processed/tabular/`                   | Stores verified tabular outputs.                          |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                    |
| :---------------------- | :---------------------------------------------------------------- |
| **Documentation-first** | README defines purpose, lifecycle, and integration policy.        |
| **Reproducibility**     | Deterministic log generation ensures traceable ETL audit trails.  |
| **Open Standards**      | UTF-8 text format; aligned to STAC/DCAT for metadata consistency. |
| **Provenance**          | Each ETL step recorded with timestamps and lineage data.          |
| **Auditability**        | Enables CI/CD verification, checksum tests, and QA replays.       |

---

## 📎 Related Directories

| Path                               | Description                                     |
| :--------------------------------- | :---------------------------------------------- |
| `data/work/tmp/tabular/`           | Temporary workspace for tabular ETL operations. |
| `data/processed/tabular/`          | Finalized, validated tabular datasets.          |
| `data/checksums/tabular/`          | SHA-256 validation for reproducibility.         |
| `data/processed/metadata/tabular/` | STAC metadata and dataset documentation.        |

---

## 📅 Version History

| Version | Date       | Summary                                                                |
| :------ | :--------- | :--------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial creation of tabular ETL log documentation.                     |
| v1.0.1  | 2025-10-09 | Added metadata header, JSON-LD, MCP badges, and provenance references. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Table Has a Trail — Logged, Verified, and Reproducible.”*
📍 [`data/work/tmp/tabular/logs/`](.) · Temporary ETL logging workspace for tabular datasets.

</div>
