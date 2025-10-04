<div align="center">

# 🧩 Kansas Frontier Matrix — Temporary Workspace (`data/work/tmp/`)

**Mission:** Provide a **short-term scratch space** for temporary files generated  
during ETL, validation, testing, or data transformation processes —  
ensuring reproducibility without polluting the main data directories.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/` directory is a **sandbox environment** for short-lived files  
created during Kansas Frontier Matrix workflows. It supports debugging, validation, and  
staging of intermediate data products that are not stored permanently in the repository.

Files placed here are **ephemeral**, automatically regenerated when needed,  
and excluded from version control via `.gitignore`.

Common uses include:
- Partial ETL outputs and batch processing fragments  
- Temporary raster/vector exports for validation  
- In-memory cache dumps or preview renderings  
- Experimentation with new dataset transformations  

---

## 🗂️ Directory Layout

```bash
data/work/tmp/
├── README.md
├── terrain/           # Temporary elevation & hillshade intermediates
├── hydrology/         # Watershed/flood data staging
├── landcover/         # Land use classification scratch outputs
├── climate/           # Climate or drought index test tiles
├── hazards/           # Tornado/flood overlay test maps
├── tabular/           # Census or agriculture ETL fragments
└── text/              # NLP and OCR text preprocessing dumps
````

> **Note:** The subfolders mirror KFM’s primary data domains, ensuring structural
> consistency between temporary and processed datasets.

---

## ⚙️ Usage Guidelines

| Policy                 | Description                                                                            |
| :--------------------- | :------------------------------------------------------------------------------------- |
| **Ephemeral Only**     | Do not store permanent datasets here. Contents may be deleted at any time.             |
| **Reproducible State** | All files must be regenerable using documented Makefile targets or scripts.            |
| **CI/CD Ignored**      | This directory is excluded from automated validation, except for specific debug tests. |
| **Logs & Cache**       | Temporary debug logs or processing caches may be stored here.                          |
| **File Size Limit**    | Keep individual files ≤ 1 GB to maintain build and cleanup efficiency.                 |

---

## ⚙️ Typical Use Cases

| Task                    | Example                                          |
| :---------------------- | :----------------------------------------------- |
| **Raster Processing**   | Subset DEMs for regional validation.             |
| **STAC Testing**        | Validate metadata generation before commit.      |
| **Checksum Debugging**  | Regenerate test hashes for pipeline validation.  |
| **Thumbnail Testing**   | Render low-resolution previews for QA.           |
| **Tabular ETL Testing** | Transform partial datasets for schema alignment. |

---

## 🧹 Cleanup Policy

Temporary files are cleared automatically during maintenance operations
and may also be purged manually.

**Makefile target:**

```bash
make clean-tmp
```

**Manual command:**

```bash
rm -rf data/work/tmp/*
```

All data here is reproducible through the documented ETL pipelines.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                       |
| :---------------------- | :------------------------------------------------------------------- |
| **Documentation-first** | README documents structure and use of temporary workspace.           |
| **Reproducibility**     | All temporary artifacts are regenerable from ETL scripts.            |
| **Open Standards**      | Temporary files conform to project-wide formats (GeoJSON, COG, CSV). |
| **Provenance**          | Even short-lived data follows consistent file naming conventions.    |
| **Auditability**        | Logs and debug outputs can be reviewed before cleanup.               |

---

## 📅 Version History

| Version | Date       | Summary                                                                        |
| :------ | :--------- | :----------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial creation of temporary workspace documentation (ETL scratch directory). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design, Reproducible by Principle.”*
📍 [`data/work/tmp/`](.) · Transient sandbox for pipeline debugging and ETL intermediates.

</div>
