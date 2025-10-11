<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain ETL Logs  
`data/work/tmp/terrain/logs/`

**Mission:** Record, track, and manage **temporary logs** generated during terrain ETL, validation, and QA operations —  
ensuring **reproducibility, transparency, and auditability** across all elevation-related data workflows  
in the **Kansas Frontier Matrix (KFM)** project.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/terrain/logs/` directory contains **temporary ETL and QA logs**  
created during terrain data processing and validation workflows.  

These logs document the complete lifecycle of terrain ETL activities:
- DEM reprojection, tiling, and mosaicking  
- Hillshade, slope, and aspect derivation  
- Raster alignment and geospatial transformation testing  
- Checksum validation, schema compliance, and STAC verification  

All files are **ephemeral**, regenerated automatically on each run, and **excluded from version control**.  
They serve as short-term, human-readable diagnostics for both developers and CI/CD systems.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/terrain/logs/
├── README.md
├── terrain_etl_debug.log
├── terrain_projection_test.log
├── terrain_validation_report.log
└── qa_metrics_summary.log
````

> **Note:** Example files above are placeholders — actual filenames depend on
> the active ETL operation or QA pipeline in progress.

---

## ⚙️ Logging Schema & Standards

All logs follow a **structured and timestamped format** based on MCP guidelines
for reproducible, auditable output.

**Example format:**

```
2025-10-10 15:45:02 [INFO] Initiating terrain ETL pipeline.
2025-10-10 15:45:08 [INFO] Reprojecting DEM from EPSG:26914 → EPSG:4326.
2025-10-10 15:45:27 [WARNING] Minor pixel alignment offset detected at boundary tile 47.
2025-10-10 15:45:40 [SUCCESS] Hillshade generated: data/work/tmp/terrain/hillshade_preview.tif
2025-10-10 15:45:44 [INFO] Checksum validation passed for slope_aspect_2020.tif
```

**Logging policy:**

* UTF-8 plain text, readable in any editor.
* No binary data or embedded ANSI color codes.
* Retains detailed timing and process metadata for traceability.

---

## 🧾 Log Types & Purposes

| Log Type                            | Purpose                                                                                       |
| :---------------------------------- | :-------------------------------------------------------------------------------------------- |
| **`terrain_etl_debug.log`**         | Captures complete ETL activity — source, reprojection, raster processing, and output summary. |
| **`terrain_projection_test.log`**   | Records CRS conversions, resampling methods, and transformation accuracy checks.              |
| **`terrain_validation_report.log`** | Summarizes checksum verification, data completeness, and STAC compliance.                     |
| **`qa_metrics_summary.log`**        | Optional; aggregates terrain QA metrics (e.g., RMSE, pixel variance, DEM void ratio).         |

---

## ⚙️ Log Management Workflow

Logs are generated automatically during the execution of the **terrain ETL pipeline**.

**Makefile Target:**

```bash
make terrain
```

**Python CLI:**

```bash
python src/pipelines/terrain/terrain_pipeline.py --log data/work/tmp/terrain/logs/terrain_etl_debug.log
```

**Lifecycle Stages:**

1. Pipeline start → log file initialized (timestamp + run ID).
2. Each ETL stage appends real-time entries for operations, warnings, and metrics.
3. QA tools and validation tasks append results to validation reports.
4. Logs are inspected for anomalies and deleted automatically during cleanup.

---

## 🧹 Cleanup Policy

Logs in this directory are **temporary and automatically purged** between pipeline runs.
This ensures efficient disk use and prevents retention of outdated debug artifacts.

**Makefile Target:**

```bash
make clean-logs
```

**Manual Cleanup:**

```bash
rm -rf data/work/tmp/terrain/logs/*
```

Permanent validated outputs are stored in:

* `data/processed/terrain/` — Final DEMs, slopes, and hillshades
* `data/checksums/terrain/` — SHA-256 integrity manifests
* `data/processed/metadata/terrain/` — STAC-compliant metadata

---

## 🧩 Integration with KFM Pipelines

| Linked Component                            | Role                                                   |
| :------------------------------------------ | :----------------------------------------------------- |
| `src/pipelines/terrain/terrain_pipeline.py` | Writes ETL logs, QA metrics, and error reports.        |
| `.github/workflows/stac-validate.yml`       | Consumes logs for checksum and metadata validation.    |
| `data/work/tmp/terrain/`                    | Parent workspace for all terrain ETL intermediates.    |
| `data/processed/terrain/`                   | Destination for final validated terrain datasets.      |
| `data/checksums/terrain/`                   | Provides integrity verification logs and cross-checks. |

---

## 🔒 Security & Retention Policy

| Rule                   | Implementation                                             |
| :--------------------- | :--------------------------------------------------------- |
| **Retention Duration** | Logs persist only for the duration of the pipeline run.    |
| **Sensitive Data**     | No raw coordinates or confidential content logged.         |
| **Access Scope**       | Logs local to ETL execution — not uploaded or versioned.   |
| **Anonymization**      | File paths or system metadata redacted in production logs. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                  |
| :---------------------- | :------------------------------------------------------------------------------ |
| **Documentation-first** | This README documents structure, lifecycle, and cleanup policies.               |
| **Reproducibility**     | Logs deterministically mirror all ETL and QA operations.                        |
| **Open Standards**      | UTF-8 formatted plain text; consistent naming conventions.                      |
| **Provenance**          | Each log entry links operations to source data and transformation stages.       |
| **Auditability**        | Logs preserve full traceability until cleanup; CI/CD pipelines archive results. |

---

## 📎 Related Directories

| Path                               | Description                                                  |
| :--------------------------------- | :----------------------------------------------------------- |
| `data/work/tmp/terrain/`           | Temporary workspace for terrain ETL and QA intermediates.    |
| `data/processed/terrain/`          | Final processed terrain datasets (DEMs, hillshades, slopes). |
| `data/checksums/terrain/`          | Hash manifests for reproducibility verification.             |
| `data/processed/metadata/terrain/` | STAC metadata entries for terrain datasets.                  |

---

## 📅 Version History

| Version | Date       | Summary                                                                        |
| :------ | :--------- | :----------------------------------------------------------------------------- |
| v1.0.0  | 2025-10-04 | Initial documentation for terrain ETL logging.                                 |
| v1.0.1  | 2025-10-09 | Added YAML metadata and provenance fields.                                     |
| v1.1.0  | 2025-10-10 | Expanded log schema examples, retention policy, and CI/CD integration details. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Elevation Has a Story — and Every Process Leaves a Log.”*
📍 [`data/work/tmp/terrain/logs/`](.) · Temporary ETL logging hub for terrain processing, validation, and QA.

</div>
```
