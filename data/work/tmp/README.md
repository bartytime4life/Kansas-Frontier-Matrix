<div align="center">

# 🧩 Kansas Frontier Matrix — **Temporary Workspace**  
`data/work/tmp/`

**Mission:** Provide a **controlled, short-term sandbox** for temporary files generated  
during ETL, validation, testing, and data transformation — enabling rapid experimentation,  
debugging, and reproducibility without contaminating long-term data directories.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Temporary Workspace (data/work/tmp/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-architecture"]
tags: ["tmp","work","sandbox","etl","validation","mcp","ci-cd","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Draft Validation)
  - FAIR Principles (Reusable & Transparent Workflows)
---
```

---

## 📚 Overview

The `data/work/tmp/` directory serves as a **sandboxed, ephemeral workspace**  
for temporary, regenerable artifacts created during KFM’s ETL, validation, and testing processes.  

It enables **safe experimentation**, **debugging**, and **short-term persistence**  
of intermediate files without affecting permanent data directories.

Files here are **non-persistent**, **excluded from version control**,  
and fully **reproducible** using Makefile or ETL pipelines.

> 🧭 *“Temporary by design — reproducible by principle.”*

---

## 🗂️ Directory Layout

```bash
data/work/tmp/
├── README.md
├── terrain/           # Temporary DEM, slope, and hillshade intermediates
├── hydrology/         # Watershed, river, or flood polygon staging
├── landcover/         # NLCD or vegetation classification intermediates
├── climate/           # Temperature, precipitation, and drought test data
├── hazards/           # Tornado, wildfire, or flood overlay test files
├── tabular/           # CSV or Parquet slices for schema validation
└── text/              # OCR/NLP intermediate text files and debug outputs
```

> Each subdirectory mirrors its counterpart in `data/processed/`, maintaining **schema consistency** between transient and finalized datasets.

---

## ⚙️ Usage Guidelines

| Policy                 | Description                                                                     |
| :--------------------- | :------------------------------------------------------------------------------ |
| **Ephemeral Only**     | Store only disposable, temporary files.                                         |
| **Reproducible State** | All contents must be regenerable via documented Make or ETL workflows.          |
| **CI/CD Exclusion**    | Automatically ignored except when explicitly used for testing.                  |
| **Logging Permitted**  | Debug or validation logs may reside here safely.                                |
| **Storage Discipline** | Individual files ≤ 1 GB; directory auto-cleared during scheduled maintenance.    |

---

## 🧩 Typical Use Cases

| Workflow Stage       | Example Use                                                    |
| :------------------- | :------------------------------------------------------------- |
| **ETL Prototyping**  | Test raster reprojection, clipping, or CSV normalization.      |
| **Checksum Drafts**  | Generate SHA-256 digests before official manifest inclusion.   |
| **STAC Validation**  | Build and review temporary STAC Items pre-publication.         |
| **Visualization QA** | Render draft thumbnails or map tiles for pre-release review.   |
| **ML Staging**       | Tokenized text, small validation splits, or cached embeddings. |

---

## 🧹 Cleanup Policy

This directory is routinely cleaned and can be cleared at any time.  
All contents can be reproduced from deterministic ETL pipelines.

### 🧩 Automated Cleanup

```bash
make clean-tmp
```

### 🧼 Manual Cleanup

```bash
rm -rf data/work/tmp/*
```

**Safety:** All files here are **temporary** — no archival or versioning required.

---

## 🧰 Integration with CI/CD & ETL

| Component            | Role / Function                                                            |
| :------------------- | :------------------------------------------------------------------------- |
| `.github/workflows/` | Stores CI debug outputs and test artifacts temporarily.                    |
| `src/pipelines/*`    | Writes intermediate files here during ETL or preprocessing runs.            |
| `data/work/logs/`    | Logs all transient tasks for traceability and debugging.                   |
| `data/checksums/`    | Uses this area to generate hashes before manifest promotion.               |
| `data/stac/`         | Validates draft STAC JSONs before committing to main catalog.              |

---

## 🧠 MCP Compliance Matrix

| MCP Principle       | Implementation Example                                            |
| :------------------ | :--------------------------------------------------------------- |
| **Documentation-first** | README documents lifecycle and reproducibility scope.           |
| **Reproducibility**     | All temporary artifacts regenerable via Make or pipeline runs.  |
| **Open Standards**      | Supports COG, GeoJSON, CSV, JSONL, and Parquet intermediate data. |
| **Provenance**          | Subfolders inherit lineage from matching `data/processed/` domain. |
| **Auditability**        | Logs stored in `data/work/logs/` before automated cleanup.      |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Schedule weekly cleanup in CI/CD to manage disk usage.  
2. **Log Traceability:** Always write transformation logs to `data/work/logs/`.  
3. **Prefix Convention:** Use timestamps or ETL run IDs in file names.  
4. **Avoid Backups:** Never store long-term or irreplaceable data here.  
5. **Monitor Size:** CI should trigger an alert if `tmp/` exceeds 5 GB.

---

## 📎 Related Directories

| Directory              | Description                                         |
| :----------------------| :-------------------------------------------------- |
| `data/work/cache/`     | Persistent cache for validation and test artifacts. |
| `data/work/staging/`   | Transitional data before moving to `processed/`.    |
| `data/work/logs/`      | Logs from ETL and CI/CD validation runs.           |
| `data/processed/`      | Final, validated, and version-controlled datasets.  |

---

## 🧾 Version History

| Version | Date | Summary |
| :-------| :----| :-------|
| **v1.0.0** | 2025-10-04 | Initial creation and structure of tmp workspace. |
| **v1.1.0** | 2025-10-10 | Added CI/CD workflow integration and policies. |
| **v1.2.0** | 2025-10-16 | Full alignment with MCP-DL v6.2 standards and ETL schema conventions. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design · Reproducible by Principle.”*  
📍 [`data/work/tmp/`](.) — ephemeral sandbox for ETL debugging, validation, and QA testing.

</div>
