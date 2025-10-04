<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain ETL Logs  
`data/work/tmp/terrain/logs/`

**Mission:** Record and manage **temporary processing logs** generated during terrain ETL, validation, and debugging operations —  
providing transparency and traceability while maintaining a clean, reproducible workflow under the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/terrain/logs/` directory temporarily stores **pipeline logs and debug reports**  
created during terrain data processing. These logs provide a record of intermediate operations —  
such as elevation reprojection, hillshade generation, slope/aspect calculation, and checksum verification.  

Logs are **ephemeral** and can be deleted or regenerated without loss of reproducibility.  
They exist to help developers, data engineers, and CI systems verify ETL progress, diagnose issues,  
and document intermediate results before cleanup.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/terrain/logs/
├── README.md
├── terrain_etl_debug.log
├── terrain_projection_test.log
└── terrain_validation_report.log
````

> **Note:** Log filenames follow a structured convention to reflect the pipeline stage or test type.
> All logs here are excluded from version control and automatically regenerated during ETL runs.

---

## ⚙️ Logging Guidelines

| Log Type                      | Purpose                                                                                            |
| :---------------------------- | :------------------------------------------------------------------------------------------------- |
| **`*_etl_debug.log`**         | Captures core ETL operations, including input/output paths, reprojection steps, and run durations. |
| **`*_projection_test.log`**   | Records CRS conversions, GDAL reprojection tests, and coordinate accuracy validation.              |
| **`*_validation_report.log`** | Summarizes checksum verification, data completeness, and STAC schema tests.                        |
| **`*_qa_metrics.log`**        | (Optional) Stores intermediate quality metrics or comparison scores from pipeline testing.         |

All logs follow UTF-8 text format for portability and readability across systems.

---

## ⚙️ Log Management Workflow

Logs are generated automatically by ETL and validation scripts.

**Example Makefile command:**

```bash
make terrain
```

**Equivalent Python invocation:**

```bash
python src/pipelines/terrain/terrain_pipeline.py --log data/work/tmp/terrain/logs/terrain_etl_debug.log
```

**Lifecycle:**

1. Pipeline starts and creates or overwrites the log file.
2. Operations (download, reprojection, transformation, checksum) are written in real time.
3. CI/CD or developers can inspect logs for diagnostics.
4. Logs are cleared with cleanup routines or on subsequent pipeline runs.

---

## 🧹 Cleanup Policy

This directory is **temporary** — logs are routinely purged after validation or deployment.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/terrain/logs/*
```

CI jobs may automatically delete or overwrite logs after successful validation to conserve space.

---

## 🧩 Integration with KFM Pipelines

| Linked Component                            | Function                                                            |
| :------------------------------------------ | :------------------------------------------------------------------ |
| `src/pipelines/terrain/terrain_pipeline.py` | Writes ETL logs during DEM and derivative processing.               |
| `data/processed/terrain/`                   | Target directory for processed terrain outputs.                     |
| `.github/workflows/stac-validate.yml`       | Uses logs for checksum and validation diagnostics.                  |
| `data/work/tmp/terrain/`                    | Parent directory for temporary terrain testing and sandbox outputs. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | This README defines structure, lifecycle, and purpose of logs.        |
| **Reproducibility**     | Log generation is deterministic and reproducible across environments. |
| **Open Standards**      | Logs are stored as plain UTF-8 text; no proprietary formats.          |
| **Provenance**          | Logs record intermediate pipeline steps for full traceability.        |
| **Auditability**        | Enables verification and debugging of ETL outputs before cleanup.     |

---

## 📎 Related Directories

| Path                      | Description                                                    |
| :------------------------ | :------------------------------------------------------------- |
| `data/work/tmp/terrain/`  | Temporary workspace for terrain data processing.               |
| `data/processed/terrain/` | Permanent location for validated terrain datasets.             |
| `data/checksums/terrain/` | SHA-256 checksums ensuring reproducibility of terrain outputs. |

---

## 📅 Version History

| Version | Date       | Summary                                                                                 |
| :------ | :--------- | :-------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial terrain log workspace documentation created for ETL and validation diagnostics. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Elevation Has a Story — and Every Process Leaves a Log.”*
📍 [`data/work/tmp/terrain/logs/`](.) · Temporary ETL logging space for terrain dataset processing.

</div>
