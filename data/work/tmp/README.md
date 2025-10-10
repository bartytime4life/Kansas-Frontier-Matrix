<div align="center">

# 🧩 Kansas Frontier Matrix — Temporary Workspace  
`data/work/tmp/`

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

> **Note:** Subfolders mirror KFM’s primary data domains, maintaining parity
> between temporary artifacts and final processed datasets.

---

## ⚙️ Usage Guidelines

| Policy                 | Description                                                             |
| :--------------------- | :---------------------------------------------------------------------- |
| **Ephemeral Only**     | Do not store permanent datasets here — contents can be deleted anytime. |
| **Reproducible State** | All files must be regenerable via Makefile targets or ETL scripts.      |
| **CI/CD Ignored**      | Excluded from validation unless explicitly called by debug tests.       |
| **Logs & Cache**       | Temporary debug logs and caches may reside here safely.                 |
| **File Size Limit**    | Keep individual files ≤ 1 GB to ensure efficient cleanup.               |

---

## ⚙️ Typical Use Cases

| Task                    | Example                                                    |
| :---------------------- | :--------------------------------------------------------- |
| **Raster Processing**   | Subset DEMs for regional validation.                       |
| **STAC Testing**        | Validate draft metadata before committing to `data/stac/`. |
| **Checksum Debugging**  | Regenerate hashes for validation tests.                    |
| **Thumbnail Testing**   | Render low-res previews for QA.                            |
| **Tabular ETL Testing** | Transform partial datasets for schema checks.              |

---

## 🧹 Cleanup Policy

Temporary files are cleared automatically by maintenance jobs or manually as needed.

**Makefile Target**

```bash
make clean-tmp
```

**Manual Command**

```bash
rm -rf data/work/tmp/*
```

All data here is **reproducible** through documented ETL pipelines
(e.g., `make terrain`, `make hydrology`, `make landcover`).

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                       |
| :---------------------- | :------------------------------------------------------------------- |
| **Documentation-first** | README explains structure and safe usage.                            |
| **Reproducibility**     | All temporary artifacts regenerable via ETL scripts.                 |
| **Open Standards**      | Temporary files follow KFM’s open-format policy (GeoJSON, COG, CSV). |
| **Provenance**          | Even ephemeral outputs maintain domain naming conventions.           |
| **Auditability**        | Logs and debug caches may be reviewed before cleanup.                |

---

## 📅 Version History

| Version    | Date       | Summary                                                                        |
| :--------- | :--------- | :----------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial creation of temporary workspace documentation (ETL scratch directory). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design, Reproducible by Principle.”*
📍 [`data/work/tmp/`](.) · Transient sandbox for pipeline debugging and ETL intermediates.

</div>
