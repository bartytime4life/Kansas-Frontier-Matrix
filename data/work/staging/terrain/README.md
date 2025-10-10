<div align="center">

# 🧾 Kansas Frontier Matrix — Staging ETL & Validation Logs  
`data/work/staging/logs/`

**Mission:** Capture **temporary ETL, validation, and promotion logs** created while datasets  
transition from processing to publication — ensuring transparent validation, reproducibility,  
and lineage tracking across Kansas Frontier Matrix (KFM) workflows.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/staging/logs/` directory stores **short-lived validation and audit logs**  
produced when data move from ETL to the staging layer.  

These logs document:
- Checksum creation and verification for incoming data  
- STAC metadata validation prior to catalog promotion  
- Schema, CRS, or attribute consistency checks  
- File transfer and promotion diagnostics between environments  

Logs are **temporary**, **not version-controlled**, and are automatically recreated  
by validation and promotion scripts.

---

## 🗂️ Directory Layout

```bash
data/work/staging/logs/
├── README.md
├── staging_etl_debug.log
├── stac_validation_report.log
├── checksum_verification.log
└── promotion_audit.log
````

> **Note:** Log names correspond to the type of validation performed.
> Files are cleared once data are promoted or cleaned.

---

## ⚙️ Logging Guidelines

| Log Type                          | Purpose                                                         |
| :-------------------------------- | :-------------------------------------------------------------- |
| **`*_etl_debug.log`**             | Records staging input/output operations and validation results. |
| **`*_validation_report.log`**     | Summarizes STAC, schema, and checksum validation steps.         |
| **`*_checksum_verification.log`** | Lists generated hashes and match results against references.    |
| **`*_promotion_audit.log`**       | Tracks dataset movements from staging → processed directories.  |

All logs use **UTF-8 text format** for universal readability.

---

## ⚙️ Log Generation Workflow

Logs are created automatically by ETL and validation utilities or may be triggered manually.

**Makefile target**

```bash
make validate
```

**Python example**

```bash
python src/pipelines/validate.py --log data/work/staging/logs/stac_validation_report.log
```

**Lifecycle**

1. Validation scripts initialize new logs.
2. Each checksum or metadata test appends details in real time.
3. Promotion routines read logs to verify completion.
4. Logs are purged once promotion succeeds.

---

## 🧹 Cleanup Policy

Logs are **temporary** and deleted during scheduled cleanups or after data promotion.

**Makefile target**

```bash
make clean-logs
```

**Manual cleanup**

```bash
rm -rf data/work/staging/logs/*
```

Validated datasets and permanent logs reside in:

* `data/processed/` — final storage for approved datasets
* `data/checksums/` — integrity hashes for reproducibility
* `data/stac/` — canonical metadata catalog

---

## 🧩 Integration with Pipelines

| Linked Component                      | Function                                            |
| :------------------------------------ | :-------------------------------------------------- |
| `src/pipelines/*`                     | Writes validation logs before data promotion.       |
| `.github/workflows/stac-validate.yml` | Consumes logs for CI/CD QA and schema verification. |
| `data/work/staging/`                  | Parent directory for data awaiting validation.      |
| `data/processed/`                     | Receives datasets after validation passes.          |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | README defines structure, workflow, and cleanup for staging logs.      |
| **Reproducibility**     | Deterministic log generation ensures traceable QA validation.          |
| **Open Standards**      | UTF-8 text format; aligns with STAC/DCAT metadata conventions.         |
| **Provenance**          | Logs tie each staged dataset to validation outcomes and promotion IDs. |
| **Auditability**        | CI/CD audits parse logs to verify validation and promotion workflows.  |

---

## 📎 Related Directories

| Path                 | Description                                   |
| :------------------- | :-------------------------------------------- |
| `data/work/staging/` | Workspace for validated but unpublished data. |
| `data/processed/`    | Finalized datasets promoted from staging.     |
| `data/checksums/`    | Integrity verification for promoted data.     |
| `data/stac/`         | STAC metadata catalog for validated datasets. |

---

## 📅 Version History

| Version | Date       | Summary                                                  |
| :------ | :--------- | :------------------------------------------------------- |
| v1.0    | 2025-10-09 | Initial creation of staging ETL & validation log module. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Passes Through the Gate of Validation.”*
📍 [`data/work/staging/logs/`](.) · Temporary validation and promotion log workspace.

</div>
