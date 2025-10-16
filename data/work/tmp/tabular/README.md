<div align="center">

# 📊 Kansas Frontier Matrix — **Temporary Tabular Workspace**  
`data/work/tmp/tabular/`

**Mission:** Provide a **temporary sandbox** for intermediate and experimental tabular data —  
including census extracts, agricultural yield samples, and economic indicators —  
generated during ETL, schema validation, or statistical analysis in the **Kansas Frontier Matrix (KFM)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/badge/Container%20Scan-Secure-orange)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Temporary Tabular Workspace (data/work/tmp/tabular/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-etl"]
tags: ["tabular","etl","validation","csv","parquet","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - FAIR Principles (Interoperable Data Management)
  - CSVW, JSON Schema, Apache Parquet
---
```

---

## 📚 Overview

The `data/work/tmp/tabular/` directory serves as a **sandbox** for tabular datasets under active transformation, validation, or aggregation.  
It supports **schema testing**, **statistical QA**, and **ETL debugging** for numeric, demographic, and economic datasets.

Typical operations include:

- Schema conformance testing for CSV and Parquet outputs  
- Validation of historical population, agriculture, and economic time-series  
- Data aggregation and normalization QA before publication  
- Testing feature engineering and model-ready tabular generation  

All files are **ephemeral**, **excluded from version control**, and **reproducible** via deterministic ETL pipelines or Makefile targets.

```bash
make tabular
# or
python src/pipelines/tabular/tabular_pipeline.py
```

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

> **Note:** File names and formats vary by pipeline stage.  
> All temporary tables regenerate automatically during workflow execution.

---

## ⚙️ Usage Guidelines

| Rule / Policy           | Description                                                                |
| :---------------------- | :------------------------------------------------------------------------- |
| **Ephemeral Storage**   | Files are temporary and auto-deleted on cleanup.                           |
| **Reproducible Output** | Every table can be regenerated deterministically via ETL pipelines.        |
| **CI/CD Exclusion**     | Ignored by automated validation unless explicitly referenced.              |
| **Open Standards Only** | Allowable formats: CSV, JSON, Parquet (UTF-8 encoding, no proprietary files). |
| **Safe Cleanup**        | Auto-cleared via `make clean-tmp` or manual deletion.                     |
| **Consistent Naming**   | Use clear prefixes (e.g., `census_`, `agriculture_`, `econ_`).             |

---

## 🧩 Typical Use Cases

| Task                         | Example                                                           |
| :--------------------------- | :---------------------------------------------------------------- |
| **Schema Validation**        | Validate tabular outputs against JSON Schema definitions.          |
| **Census QA**                | Verify demographic totals across temporal ranges.                  |
| **Agriculture Data Testing** | Sample crop yield records for data type and range verification.    |
| **Economic Aggregation**     | Summarize GDP, trade, or labor datasets pre-ingestion.             |
| **Checksum Testing**         | Generate SHA-256 hashes to confirm deterministic reproduction.     |
| **ETL Debugging**            | Inspect merge/join steps in feature engineering pipelines.         |

---

## 🧮 Data Standards & Formats

| Format Type | File Extension | Standard / Specification | Example Tooling |
| :----------- | :--------------| :------------------------| :--------------- |
| **Flat File** | `.csv` | CSVW (W3C) with schema annotations | `pandas`, `pyarrow` |
| **Columnar** | `.parquet` | Apache Parquet 2.0 | `fastparquet`, `duckdb` |
| **Metadata** | `.json` | JSON Schema 2020-12 | `jsonschema`, `jq` |
| **Logs** | `.log` | UTF-8 plain text | `logging`, `pytest` |

---

## 🧰 Workflow Integration

Temporary tabular files are generated as part of the **Tabular ETL pipeline** and used during integration or test phases.

**Makefile Target**

```bash
make tabular
```

**Python CLI**

```bash
python src/pipelines/tabular/tabular_pipeline.py --tmp data/work/tmp/tabular/
```

**Lifecycle**

1. Load input sources from `data/raw/tabular/` or remote APIs.  
2. Apply cleaning, normalization, and schema alignment steps.  
3. Output intermediate artifacts to `data/work/tmp/tabular/`.  
4. Run QA/validation checks (`schema`, `checksum`, `statistics`).  
5. Promote validated outputs to `data/processed/tabular/`.  

---

## 🧹 Cleanup Policy

Tabular files here are **temporary and transient**, purged automatically between runs.

**Automated Cleanup**

```bash
make clean-tmp
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/tabular/*
```

Permanent artifacts reside in:

| Location | Purpose |
| :-- | :-- |
| `data/processed/tabular/` | Final, validated tabular datasets for distribution. |
| `data/checksums/tabular/` | SHA-256 manifests ensuring reproducibility. |
| `data/processed/metadata/tabular/` | STAC-compliant metadata and lineage tracking. |

---

## 🔒 Integration with CI/CD & Governance

| Component                               | Function                                                      |
| :-------------------------------------- | :------------------------------------------------------------- |
| `src/pipelines/tabular/tabular_pipeline.py` | Generates, validates, and cleans tabular data intermediates.   |
| `.github/workflows/stac-validate.yml`   | Consumes schema and checksum results for audit pipelines.      |
| `data/work/tmp/`                        | Root workspace for all temporary ETL domains.                  |
| `data/checksums/tabular/`               | Stores reproducibility manifests for verified outputs.          |
| `data/stac/tabular/`                    | Tracks STAC lineage and provenance metadata for tabular data.  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                            |
| :---------------------- | :------------------------------------------------------------------------ |
| **Documentation-first** | README documents purpose, standards, and reproducibility practices.        |
| **Reproducibility**     | Deterministic ETL and versioned schema tests guarantee identical outputs.  |
| **Open Standards**      | CSV, JSON, Parquet (UTF-8), JSON Schema — all openly documented formats.   |
| **Provenance**          | Logs, manifests, and metadata cross-reference ETL pipelines and STAC IDs. |
| **Auditability**        | QA/validation logs and schema definitions ensure full transparency.        |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Include `make clean-tmp` in post-run CI/CD routines.  
2. **Validate Early:** Run `jsonschema --instance file.json schema.json` before ETL promotion.  
3. **Monitor Size:** Limit intermediate CSV/Parquet files to ≤ 2 GB for local testing.  
4. **Use Compression:** Prefer `.parquet` with Snappy/ZSTD to reduce disk usage.  
5. **Ensure Consistency:** Keep schemas synced with STAC metadata definitions.  

---

## 📎 Related Directories

| Path                               | Description                                       |
| :--------------------------------- | :------------------------------------------------ |
| `data/processed/tabular/`          | Finalized tabular datasets for analysis.          |
| `data/checksums/tabular/`          | Integrity validation hashes for reproducibility.  |
| `data/processed/metadata/tabular/` | STAC metadata and documentation for tabular data. |
| `data/work/tmp/`                   | Parent temporary workspace for all ETL domains.   |

---

## 📅 Version History

| Version | Date       | Summary                                                             |
| :------ | :--------- | :------------------------------------------------------------------ |
| **v1.0.0** | 2025-10-04 | Initial documentation of temporary tabular workspace.              |
| **v1.1.0** | 2025-10-09 | Added provenance mapping, schema references, and cleanup policies. |
| **v1.2.0** | 2025-10-16 | Full MCP-DL v6.2 alignment with FAIR principles and ETL integration.|

---

<div align="center">

**Kansas Frontier Matrix** — *“Quantifying Change, One Table at a Time.”*  
📍 [`data/work/tmp/tabular/`](.) · Ephemeral workspace for tabular ETL, validation, and QA operations.

</div>
