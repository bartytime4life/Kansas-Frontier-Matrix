<div align="center">

# 🧾 Kansas Frontier Matrix — Terrain ETL Logs  
`data/work/tmp/terrain/logs/`

**Mission:** Record and manage **temporary processing logs** generated during terrain ETL, validation, and debugging operations —  
providing transparency and traceability while maintaining a clean, reproducible workflow under the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/terrain/logs/` directory temporarily stores **pipeline logs and debug reports**  
created during terrain data processing. These logs record key intermediate operations —  
such as elevation reprojection, hillshade generation, slope/aspect calculation, and checksum verification.  

Logs are **ephemeral** and regenerable for full reproducibility.  
They enable developers, data engineers, and CI/CD systems to validate ETL progress,  
diagnose issues, and document QA outputs prior to cleanup.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/terrain/logs/
├── README.md
├── terrain_etl_debug.log
├── terrain_projection_test.log
└── terrain_validation_report.log
````

> **Note:** File names mirror pipeline stages.
> Logs are excluded from version control and regenerated during each ETL cycle.

---

## ⚙️ Logging Guidelines

| Log Type                      | Purpose                                                                                            |
| :---------------------------- | :------------------------------------------------------------------------------------------------- |
| **`*_etl_debug.log`**         | Captures core ETL operations, including input/output paths, reprojection steps, and run durations. |
| **`*_projection_test.log`**   | Records CRS conversions, GDAL reprojection trials, and coordinate accuracy checks.                 |
| **`*_validation_report.log`** | Summarizes checksum verification, completeness audits, and STAC schema validation.                 |
| **`*_qa_metrics.log`**        | (Optional) Stores terrain quality metrics or raster comparison statistics.                         |

All logs are **UTF-8 plain-text** for portability and transparency.

---

## ⚙️ Log Management Workflow

Logs are automatically created and managed by terrain ETL and QA scripts.

**Makefile target:**

```bash
make terrain
```

**Python command:**

```bash
python src/pipelines/terrain/terrain_pipeline.py --log data/work/tmp/terrain/logs/terrain_etl_debug.log
```

**Lifecycle**

1. Pipeline initializes → log file created or overwritten.
2. Processing operations stream progress and errors in real time.
3. Logs inspected manually or via CI/CD diagnostics.
4. Auto-purged after validation or on next pipeline run.

---

## 🧹 Cleanup Policy

This directory is **non-persistent** and cleared automatically to prevent clutter.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/terrain/logs/*
```

Automated cleanup runs post-validation during GitHub Actions workflows.

Permanent terrain datasets and metadata live under:

* `data/processed/terrain/` — verified DEMs, hillshades, and derivatives
* `data/checksums/terrain/` — reproducibility hashes

---

## 🧩 Integration with KFM Pipelines

| Linked Component                            | Function                                                   |
| :------------------------------------------ | :--------------------------------------------------------- |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates terrain ETL logs and QA metrics.                 |
| `data/processed/terrain/`                   | Receives final processed raster outputs.                   |
| `.github/workflows/stac-validate.yml`       | References logs for checksum and schema validation.        |
| `data/work/tmp/terrain/`                    | Parent directory for all temporary terrain workspace data. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | README defines structure, lifecycle, and purpose of terrain logs.     |
| **Reproducibility**     | Log generation is deterministic and reproducible across environments. |
| **Open Standards**      | UTF-8 plain text ensures cross-platform transparency.                 |
| **Provenance**          | Logs trace intermediate pipeline stages for terrain data lineage.     |
| **Auditability**        | Each ETL stage provides verifiable QA evidence before cleanup.        |

---

## 📎 Related Directories

| Path                      | Description                                                |
| :------------------------ | :--------------------------------------------------------- |
| `data/work/tmp/terrain/`  | Temporary workspace for terrain ETL and QA.                |
| `data/processed/terrain/` | Final validated DEMs, hillshades, and derived rasters.     |
| `data/checksums/terrain/` | SHA-256 checksum validation for reproducibility assurance. |

---

## 📅 Version History

| Version | Date       | Summary                                                      |
| :------ | :--------- | :----------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial creation of terrain ETL log workspace documentation. |
| v1.0.1  | 2025-10-09 | Added YAML metadata, JSON-LD schema, badges, and provenance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Elevation Has a Story — and Every Process Leaves a Log.”*
📍 [`data/work/tmp/terrain/logs/`](.) · Temporary ETL logging space for terrain dataset processing.

</div>
