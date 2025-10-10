<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology ETL Logs  
`data/work/tmp/hydrology/logs/`

**Mission:** Record and manage **temporary hydrologic ETL logs** produced during dataset ingestion,  
validation, and analysis — ensuring transparent, reproducible, and auditable workflows for Kansas water,  
streamflow, and groundwater data in the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/hydrology/logs/` directory temporarily stores **pipeline and validation logs**  
produced while processing hydrologic datasets such as stream gauge data, watersheds, river networks,  
and groundwater measurements.  

These logs document:
- Extraction and preprocessing of raw NWIS, FEMA, and USGS data  
- CRS reprojection, interpolation, and catchment aggregation steps  
- Quality control and schema validation for tabular/raster hydrology data  
- Checksum and reproducibility verification  

All logs are **ephemeral**, **excluded from Git**, and **regenerated deterministically**  
whenever `make hydrology` or equivalent ETL commands are executed.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/hydrology/logs/
├── README.md
├── hydrology_etl_debug.log
├── watershed_validation_report.log
├── streamflow_cleaning.log
└── checksum_audit_report.log
````

> **Note:** Log names correspond to the pipeline stage (e.g., “_cleaning”, “_validation”, “_audit”).
> Logs are replaced or purged automatically between runs.

---

## ⚙️ Logging Guidelines

| Log Type                      | Purpose                                                               |
| :---------------------------- | :-------------------------------------------------------------------- |
| **`*_etl_debug.log`**         | Records main ETL execution, transformations, and performance metrics. |
| **`*_validation_report.log`** | Summarizes schema and value validation for hydrologic datasets.       |
| **`*_cleaning.log`**          | Documents null fills, normalization, and statistical corrections.     |
| **`*_checksum_audit.log`**    | Contains hash verification results for reproducibility audits.        |

All logs use **UTF-8 text** format and standardized timestamping for audit traceability.

---

## ⚙️ Log Generation Workflow

Logs are generated automatically by the hydrology ETL pipeline or can be manually invoked.

**Makefile target:**

```bash
make hydrology
```

**Python command:**

```bash
python src/pipelines/hydrology/hydrology_pipeline.py --log data/work/tmp/hydrology/logs/hydrology_etl_debug.log
```

**Lifecycle**

1. ETL process initializes → log file created.
2. Operations (download, cleaning, reprojection, merge) append live updates.
3. QA or CI/CD processes read logs for diagnostics.
4. Logs are cleared after validation or cleanup.

---

## 🧹 Cleanup Policy

Logs are temporary and automatically deleted after successful pipeline validation.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/hydrology/logs/*
```

Permanent, validated data reside in:

* `data/processed/hydrology/` — Final hydrologic datasets
* `data/checksums/hydrology/` — Reproducibility hashes
* `data/processed/metadata/hydrology/` — STAC metadata for hydrology layers

---

## 🧩 Integration with Pipelines

| Linked Component                                | Function                                              |
| :---------------------------------------------- | :---------------------------------------------------- |
| `src/pipelines/hydrology/hydrology_pipeline.py` | Generates ETL, QA, and checksum logs during runs.     |
| `.github/workflows/stac-validate.yml`           | References logs for CI schema validation diagnostics. |
| `data/work/tmp/hydrology/`                      | Parent workspace for temporary hydrology ETL outputs. |
| `data/processed/hydrology/`                     | Destination for finalized hydrology data products.    |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | Defines structure, workflow, and cleanup policy for hydrology logs. |
| **Reproducibility**     | Logs regenerate deterministically with every pipeline execution.    |
| **Open Standards**      | UTF-8 text format aligned to STAC/DCAT metadata conventions.        |
| **Provenance**          | ETL timestamps and filenames provide lineage and traceability.      |
| **Auditability**        | QA and checksum logs guarantee full transparency before cleanup.    |

---

## 📎 Related Directories

| Path                                 | Description                                            |
| :----------------------------------- | :----------------------------------------------------- |
| `data/work/tmp/hydrology/`           | Temporary workspace for hydrology ETL intermediates.   |
| `data/processed/hydrology/`          | Validated streamflow, watershed, and groundwater data. |
| `data/checksums/hydrology/`          | SHA-256 integrity checks for reproducibility.          |
| `data/processed/metadata/hydrology/` | STAC metadata for hydrologic assets.                   |

---

## 📅 Version History

| Version | Date       | Summary                                              |
| :------ | :--------- | :--------------------------------------------------- |
| v1.0    | 2025-10-09 | Initial creation of hydrology ETL log documentation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Stream Recorded. Every Drop Accounted For.”*
📍 [`data/work/tmp/hydrology/logs/`](.) · Temporary ETL logging workspace for hydrologic datasets.

</div>
