<div align="center">

# 📊 Kansas Frontier Matrix — Temporary Tabular Workspace  
`data/work/tmp/tabular/`

**Mission:** Provide a **temporary sandbox** for intermediate and experimental tabular data —  
including census extracts, agricultural yield samples, and economic indicators —  
generated during ETL, schema validation, or statistical analysis in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/tabular/` directory serves as a **scratch environment**  
for tabular datasets under active transformation, cleaning, or validation.  

Typical use cases include:
- Schema testing for CSV and Parquet outputs  
- Statistical aggregation and QA of historical population or economic data  
- Temporary result tables generated during feature engineering  
- Validation of normalization routines or cross-domain data joins  

All files here are **short-lived**, **excluded from version control**, and **fully reproducible**  
via deterministic ETL scripts such as:

```bash
make tabular
# or
python src/pipelines/tabular/tabular_pipeline.py
````

---

## 🗂️ Directory Layout

```bash
data/work/tmp/tabular/
├── README.md
├── census_population_sample.csv
├── agricultural_yield_preview.parquet
├── economic_stats_validation.json
└── logs/
    └── tabular_etl_debug.log
```

> **Note:** File names and formats vary depending on which ETL or validation task is active.
> All files are ephemeral and automatically regenerated during workflow execution.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                       |
| :---------------------- | :---------------------------------------------------------------- |
| **Ephemeral Storage**   | Files are temporary and auto-deleted on cleanup.                  |
| **Regenerable Outputs** | All tables can be re-created via deterministic ETL processes.     |
| **CI/CD Exclusion**     | Ignored by automated build and validation workflows.              |
| **Open Standards**      | Only CSV, JSON, or Parquet formats are allowed for compatibility. |
| **Safe Cleanup**        | Auto-cleared using `make clean-tmp` or manual deletion.           |

---

## ⚙️ Typical Use Cases

| Task                         | Example                                                        |
| :--------------------------- | :------------------------------------------------------------- |
| **Schema Validation**        | Validate tabular outputs against schema definitions.           |
| **Census QA**                | Check numeric consistency across decades of population data.   |
| **Agriculture Data Testing** | Sample crop yield records for schema or type validation.       |
| **Economic Aggregation**     | Create temporary GDP, employment, or tax summaries.            |
| **Checksum Testing**         | Generate small datasets to confirm reproducibility via hashes. |

---

## 🧹 Cleanup Policy

Temporary tabular data is cleared automatically post-pipeline or may be removed manually.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/tabular/*
```

Permanent data products reside in:

* `data/processed/tabular/` — validated and published tabular datasets
* `data/checksums/tabular/` — SHA-256 reproducibility checksums
* `data/processed/metadata/tabular/` — STAC metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                  |
| :---------------------- | :-------------------------------------------------------------- |
| **Documentation-first** | README defines structure, workflow, and cleanup rules.          |
| **Reproducibility**     | Every table can be recreated deterministically via ETL scripts. |
| **Open Standards**      | CSV, JSON, and Parquet formats ensure open accessibility.       |
| **Provenance**          | Files linked to upstream ETL scripts and metadata lineage.      |
| **Auditability**        | Logs and checksums support transparent QA verification.         |

---

## 📎 Related Directories

| Path                               | Description                                       |
| :--------------------------------- | :------------------------------------------------ |
| `data/processed/tabular/`          | Finalized tabular datasets for analysis.          |
| `data/checksums/tabular/`          | Integrity validation hashes for reproducibility.  |
| `data/processed/metadata/tabular/` | STAC metadata and documentation for tabular data. |
| `data/work/tmp/`                   | Root temporary workspace for all ETL pipelines.   |

---

## 📅 Version History

| Version | Date       | Summary                                                             |
| :------ | :--------- | :------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial documentation for temporary tabular workspace.              |
| v1.0.1  | 2025-10-09 | Added YAML/JSON-LD metadata, MCP badges, provenance, and standards. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying Change, One Table at a Time.”*
📍 [`data/work/tmp/tabular/`](.) · Temporary workspace for tabular ETL, validation, and QA operations.

</div>
