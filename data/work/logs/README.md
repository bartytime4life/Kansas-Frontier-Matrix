<div align="center">

# 🧾 Kansas Frontier Matrix — Global Logs Directory  
`data/work/logs/`

**Mission:** Centralize **pipeline and validation logs** generated during data processing,  
ETL execution, and QA/QC workflows — ensuring full transparency, provenance, and traceability  
across all Kansas Frontier Matrix (KFM) data domains.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/logs/` directory consolidates **runtime logs** from all data processing pipelines,  
providing a unified, temporary record of system events, validation results, and debug output.  

Logs are used to:
- Track ETL progress and runtime performance  
- Record validation and checksum verification events  
- Provide provenance for intermediate data transformations  
- Support CI/CD diagnostics and workflow audits  

All log files are **ephemeral**, **excluded from version control**, and **automatically regenerated**  
on each pipeline run.

---

## 🗂️ Directory Layout

```bash
data/work/logs/
├── README.md
├── terrain_etl.log
├── hydrology_etl.log
├── landcover_etl.log
├── climate_etl.log
├── hazards_etl.log
└── tabular_etl.log
````

> **Note:** Actual logs may vary based on pipeline activity.
> Each log corresponds to one domain (terrain, hydrology, climate, etc.) and is overwritten
> on each execution for reproducibility and space efficiency.

---

## ⚙️ Logging Policy

| Policy                | Description                                                              |
| :-------------------- | :----------------------------------------------------------------------- |
| **Temporary Storage** | Logs are transient and auto-deleted on cleanup.                          |
| **Reproducible**      | Each ETL run regenerates identical logs for traceability.                |
| **Human-readable**    | Logs are plain-text UTF-8 with timestamps and context.                   |
| **CI/CD-Aware**       | Logs provide detailed output for GitHub Actions validation.              |
| **Non-Persistent**    | Logs are not tracked in Git; they are for temporary audit purposes only. |

---

## ⚙️ Typical Log Types

| Log Name                | Description                                                           |
| :---------------------- | :-------------------------------------------------------------------- |
| **`terrain_etl.log`**   | Documents DEM, hillshade, and terrain derivative processes.           |
| **`hydrology_etl.log`** | Records hydrological network generation and flow QA/QC.               |
| **`landcover_etl.log`** | Captures vegetation, NLCD, and land use ETL events.                   |
| **`climate_etl.log`**   | Logs climate data conversions, aggregation, and anomaly analysis.     |
| **`hazards_etl.log`**   | Summarizes hazard model creation and validation steps.                |
| **`tabular_etl.log`**   | Stores schema validation, aggregation, and normalization diagnostics. |

All logs are formatted with standardized headers including:

```
[YYYY-MM-DD HH:MM:SS] [INFO|WARNING|ERROR] Message
```

---

## ⚙️ Log Management Workflow

Logs are generated automatically during pipeline execution.

**Makefile target:**

```bash
make all
```

**Python command example:**

```bash
python src/pipelines/hydrology/hydrology_pipeline.py --log data/work/logs/hydrology_etl.log
```

**Lifecycle:**

1. Pipeline execution starts → log file created or overwritten.
2. Logs capture major ETL milestones, warnings, and validation steps.
3. Logs are used for debugging and QA review.
4. Logs are cleared automatically on cleanup or upon successful validation.

---

## 🧹 Cleanup Policy

Logs are cleared automatically during maintenance or manually when rebuilding.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/logs/*
```

> **Tip:** Always review recent logs before cleanup to capture any diagnostic details or validation notes.

---

## 🧩 Integration with KFM Pipelines

| Linked Component                      | Purpose                                                    |
| :------------------------------------ | :--------------------------------------------------------- |
| `src/pipelines/*`                     | Writes runtime logs for ETL, validation, and QA processes. |
| `.github/workflows/stac-validate.yml` | Parses logs for STAC and checksum validation diagnostics.  |
| `data/work/tmp/`                      | Logs reference temporary files generated during ETL.       |
| `data/checksums/`                     | Logs record hash verification and data integrity results.  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | README describes log structure, policy, and workflow.       |
| **Reproducibility**     | Logs record deterministic ETL events reproducibly.          |
| **Open Standards**      | UTF-8 plain-text format ensures accessibility.              |
| **Provenance**          | Logs document the complete lineage of data transformations. |
| **Auditability**        | Logs enable transparent review and CI/CD traceability.      |

---

## 📎 Related Directories

| Path                       | Description                                         |
| :------------------------- | :-------------------------------------------------- |
| `data/work/tmp/`           | Temporary workspace for all ETL and QA files.       |
| `data/checksums/`          | Directory for dataset integrity validation records. |
| `data/processed/`          | Final validated datasets for each domain.           |
| `data/processed/metadata/` | STAC metadata and schema documentation.             |

---

## 📅 Version History

| Version | Date       | Summary                                                        |
| :------ | :--------- | :------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial documentation for centralized ETL and validation logs. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Run Logged. Every Process Proven.”*
📍 [`data/work/logs/`](.) · Global ETL and validation logging directory for all KFM data pipelines.

</div>
