<div align="center">

# 🏔️ Kansas Frontier Matrix — Temporary Terrain Workspace  
`data/work/tmp/terrain/`

**Mission:** Provide a **scratch workspace** for intermediate and experimental terrain data products —  
including DEM subsets, hillshade drafts, slope/aspect previews, and projection tests —  
generated during ETL, validation, or QA workflows within the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/terrain/` directory is a **temporary workspace**  
used for processing, testing, and validating terrain and elevation datasets.  

This folder contains **non-persistent artifacts** created during:
- DEM tiling, mosaicking, or reprojection  
- Hillshade or slope/aspect derivative generation  
- Quality control, visualization, and transformation testing  

All contents are **safe to delete** — they can be **recreated deterministically**  
via pipeline commands such as `make terrain` or `python src/pipelines/terrain/terrain_pipeline.py`.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/terrain/
├── README.md
├── dem_test_subset.tif
├── hillshade_preview.tif
├── slope_test_area.tif
└── logs/
    └── terrain_etl_debug.log
````

> **Note:** Example files are placeholders.
> Actual contents vary by current ETL operations and testing scope.

---

## ⚙️ Usage Guidelines

| Policy                | Description                                                          |
| :-------------------- | :------------------------------------------------------------------- |
| **Ephemeral Storage** | Files here are temporary and excluded from version control.          |
| **Reproducibility**   | All data must be regenerable through KFM’s reproducible pipelines.   |
| **CI/CD Exclusion**   | This folder is ignored in automated builds and validation workflows. |
| **Debugging Only**    | For intermediate tests, visual checks, or ETL validation output.     |
| **Safe Deletion**     | May be cleared automatically during cleanup operations.              |

---

## ⚙️ Typical Use Cases

| Task                          | Example                                                               |
| :---------------------------- | :-------------------------------------------------------------------- |
| **DEM Cropping**              | Extract a small tile from statewide LiDAR DEM for projection testing. |
| **Hillshade Validation**      | Generate sample shaded-relief images for display calibration.         |
| **Slope & Aspect Derivation** | Test gradient calculations before batch processing.                   |
| **Raster Comparison**         | Compare newly processed files with existing checksums.                |
| **Debug Logging**             | Output intermediate raster statistics for QA review.                  |

---

## 🧹 Cleanup Policy

This directory should remain **empty between major pipeline runs**
to prevent residual or outdated artifacts.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/terrain/*
```

All reproducible datasets are permanently stored under:

* `data/processed/terrain/` — validated terrain outputs
* `data/checksums/terrain/` — integrity and reproducibility hashes

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                  |
| :---------------------- | :-------------------------------------------------------------- |
| **Documentation-first** | README defines workspace scope and lifecycle policy.            |
| **Reproducibility**     | All files can be recreated through deterministic ETL scripts.   |
| **Open Standards**      | Only open raster formats (GeoTIFF, COG, VRT) used in testing.   |
| **Provenance**          | Temporary files retain traceable lineage via logged ETL stages. |
| **Auditability**        | Logs under `/logs/` provide traceable context before cleanup.   |

---

## 📎 Related Directories

| Path                               | Purpose                                                 |
| :--------------------------------- | :------------------------------------------------------ |
| `data/processed/terrain/`          | Finalized DEMs, hillshades, and derived rasters.        |
| `data/checksums/terrain/`          | SHA-256 checksums for reproducibility tracking.         |
| `data/processed/metadata/terrain/` | STAC metadata and documentation for terrain datasets.   |
| `data/work/tmp/`                   | Parent scratch directory for all KFM temporary outputs. |

---

## 📅 Version History

| Version | Date       | Summary                                                                         |
| :------ | :--------- | :------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial terrain temporary workspace documentation (ETL and validation sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design. Verified by Process.”*
📍 [`data/work/tmp/terrain/`](.) · Short-term workspace for terrain ETL experimentation and QA validation.

</div>
