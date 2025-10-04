<div align="center">

# 📊 Kansas Frontier Matrix — Temporary Tabular Workspace  
`data/work/tmp/tabular/`

**Mission:** Provide a **temporary sandbox** for intermediate and experimental tabular data —  
including census extracts, agricultural yield samples, and economic indicators —  
generated during ETL, schema validation, or statistical analysis in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/tabular/` directory acts as a **scratch environment**  
for tabular datasets under active transformation, cleaning, or validation.  

Typical use cases include:
- Schema testing for CSV and Parquet outputs  
- Statistical aggregation and QA of historical population or economic data  
- Temporary result tables generated during feature engineering  
- Validation of data normalization routines or cross-domain joins  

All contents are **short-lived**, **excluded from version control**, and **fully reproducible**  
through deterministic ETL scripts (`make tabular` or `tabular_pipeline.py`).

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
````

> **Note:** Filenames and formats will vary depending on which ETL or validation step is active.
> No file in this directory is permanent — all are ephemeral and automatically regenerated.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                        |
| :---------------------- | :----------------------------------------------------------------- |
| **Ephemeral Storage**   | Files are temporary and auto-deleted on cleanup.                   |
| **Regenerable Outputs** | All tables can be re-created from source data using ETL pipelines. |
| **CI/CD Exclusion**     | This folder is excluded from validation and deployment workflows.  |
| **Open Standards**      | Data stored here must use open formats (CSV, JSON, Parquet).       |
| **Safe Cleanup**        | Automatically cleared using `make clean-tmp` or manual deletion.   |

---

## ⚙️ Typical Use Cases

| Task                         | Example                                                           |
| :--------------------------- | :---------------------------------------------------------------- |
| **Schema Validation**        | Validate tabular output columns against schema definitions.       |
| **Census QA**                | Check numeric consistency across decades of population data.      |
| **Agriculture Data Testing** | Sample crop yield records for schema or type validation.          |
| **Economic Aggregation**     | Generate temporary summaries for GDP, employment, or tax data.    |
| **Checksum Testing**         | Recreate small datasets to verify reproducibility against hashes. |

---

## 🧹 Cleanup Policy

Temporary tabular data is automatically cleared after pipeline runs or can be manually removed.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/tabular/*
```

Permanent datasets and their validation records are maintained in:

* `data/processed/tabular/` — Finalized and validated outputs
* `data/checksums/tabular/` — Integrity hashes for reproducibility tracking
* `data/processed/metadata/tabular/` — STAC metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                    |
| :---------------------- | :---------------------------------------------------------------- |
| **Documentation-first** | README documents workspace structure and policy.                  |
| **Reproducibility**     | Temporary tables are regenerable via deterministic ETL processes. |
| **Open Standards**      | CSV, JSON, and Parquet ensure open accessibility.                 |
| **Provenance**          | Temporary tables align with tracked ETL stages and metadata.      |
| **Auditability**        | Logs provide traceable records of temporary transformations.      |

---

## 📎 Related Directories

| Path                               | Description                                          |
| :--------------------------------- | :--------------------------------------------------- |
| `data/processed/tabular/`          | Final tabular datasets for analysis and publication. |
| `data/checksums/tabular/`          | Verification hashes for reproducibility.             |
| `data/processed/metadata/tabular/` | Metadata and STAC documentation for tabular data.    |
| `data/work/tmp/`                   | Root workspace for all temporary ETL outputs.        |

---

## 📅 Version History

| Version | Date       | Summary                                                                                |
| :------ | :--------- | :------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial tabular temporary workspace documentation (ETL and schema validation sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying Change, One Table at a Time.”*
📍 [`data/work/tmp/tabular/`](.) · Temporary workspace for tabular ETL, validation, and QA.

</div>
