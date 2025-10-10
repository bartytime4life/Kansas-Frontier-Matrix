<div align="center">

# 🏔️ Kansas Frontier Matrix — Temporary Terrain Workspace  
`data/work/tmp/terrain/`

**Mission:** Provide a **scratch workspace** for intermediate and experimental terrain data products —  
including DEM subsets, hillshade drafts, slope/aspect previews, and projection tests —  
generated during ETL, validation, or QA workflows within the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/terrain/` directory functions as a **temporary workspace**  
for processing, testing, and validating terrain and elevation datasets.  

This workspace contains **non-persistent artifacts** produced during:
- DEM tiling, mosaicking, or reprojection  
- Hillshade or slope/aspect derivative generation  
- Quality control, visualization, and transformation testing  

All contents are **safe to delete** — they can be **recreated deterministically**  
using commands such as:

```bash
make terrain
# or
python src/pipelines/terrain/terrain_pipeline.py
````

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
```

> **Note:** Example files are placeholders — actual contents vary with each ETL operation.

---

## ⚙️ Usage Guidelines

| Policy                | Description                                                  |
| :-------------------- | :----------------------------------------------------------- |
| **Ephemeral Storage** | Files here are temporary and excluded from version control.  |
| **Reproducibility**   | All data can be regenerated via deterministic ETL pipelines. |
| **CI/CD Exclusion**   | Ignored in automated builds and validation workflows.        |
| **Debugging Only**    | Intended for visual checks and intermediate ETL outputs.     |
| **Safe Deletion**     | Auto-purged during cleanup tasks.                            |

---

## ⚙️ Typical Use Cases

| Task                          | Example                                                         |
| :---------------------------- | :-------------------------------------------------------------- |
| **DEM Cropping**              | Extract a tile from statewide LiDAR DEM for projection testing. |
| **Hillshade Validation**      | Generate shaded-relief previews for calibration.                |
| **Slope & Aspect Derivation** | Test gradient calculations prior to batch runs.                 |
| **Raster Comparison**         | Validate new outputs against checksum references.               |
| **Debug Logging**             | Output intermediate raster stats for QA review.                 |

---

## 🧹 Cleanup Policy

This directory is automatically cleared between pipeline runs
to prevent retention of outdated artifacts.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/terrain/*
```

Permanent datasets reside in:

* `data/processed/terrain/` — validated DEMs, hillshades, and derivatives
* `data/checksums/terrain/` — integrity hashes for reproducibility

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                 |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | README defines workspace scope, lifecycle, and cleanup policy. |
| **Reproducibility**     | All terrain artifacts recreated deterministically via ETL.     |
| **Open Standards**      | GeoTIFF/COG/VRT raster formats ensure interoperability.        |
| **Provenance**          | Logged ETL stages record lineage of each generated file.       |
| **Auditability**        | `/logs/` retains contextual trace data before cleanup.         |

---

## 📎 Related Directories

| Path                               | Purpose                                                 |
| :--------------------------------- | :------------------------------------------------------ |
| `data/processed/terrain/`          | Finalized DEMs, hillshades, and derived rasters.        |
| `data/checksums/terrain/`          | SHA-256 hashes for reproducibility validation.          |
| `data/processed/metadata/terrain/` | STAC metadata and documentation for terrain datasets.   |
| `data/work/tmp/`                   | Parent scratch directory for all temporary ETL outputs. |

---

## 📅 Version History

| Version | Date       | Summary                                                       |
| :------ | :--------- | :------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial terrain temporary workspace documentation.            |
| v1.0.1  | 2025-10-09 | Added YAML metadata, JSON-LD schema, CI badges, and MCP tags. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design. Verified by Process.”*
📍 [`data/work/tmp/terrain/`](.) · Short-term workspace for terrain ETL experimentation and QA validation.

</div>
