<div align="center">

# 🌾 Kansas Frontier Matrix — Temporary Land Cover Workspace  
`data/work/tmp/landcover/`

**Mission:** Provide a **sandbox workspace** for intermediate and experimental land cover files —  
including vegetation classification subsets, NLCD composites, change-detection outputs, and crop map test layers —  
used during ETL, validation, and visualization within the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/landcover/` directory acts as a **temporary sandbox** for  
land cover–related datasets during ETL and QA/QC operations.  

Typical contents include:
- Cropped NLCD tiles or derived composites  
- Change-detection test rasters for visual validation  
- Vegetation and crop mask previews  
- Reprojection or resampling test layers  
- Diagnostic outputs from classification model testing  

All contents are **short-lived**, **excluded from version control**, and **safe to delete**.  
Any file stored here can be fully **recreated deterministically** using reproducible ETL pipelines.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/landcover/
├── README.md
├── nlcd_preview_tile.tif
├── landcover_change_test.tif
├── crop_mask_temp.geojson
└── logs/
    └── landcover_etl_debug.log
````

> **Note:** File names and content examples are placeholders.
> Actual contents depend on current ETL runs, testing, or validation scenarios.

---

## ⚙️ Usage Guidelines

| Policy                | Description                                                    |
| :-------------------- | :------------------------------------------------------------- |
| **Ephemeral Storage** | Temporary files only; do not store permanent data here.        |
| **Regenerable Data**  | All outputs must be reproducible through documented pipelines. |
| **CI/CD Exclusion**   | This directory is ignored in automated validation pipelines.   |
| **Open Formats**      | Only open-standard data types (GeoTIFF, GeoJSON, CSV).         |
| **Safe Deletion**     | Contents are purged during cleanup or ETL restarts.            |

---

## ⚙️ Typical Use Cases

| Task                           | Example                                                            |
| :----------------------------- | :----------------------------------------------------------------- |
| **Classification Testing**     | Generate small NLCD sample rasters for validation.                 |
| **Change Detection**           | Create test composites to verify 1992–2021 classification shifts.  |
| **Vegetation QA**              | Visualize pre-settlement vegetation overlays against NLCD results. |
| **Crop Distribution Sampling** | Extract partial USDA CDL datasets for debugging.                   |
| **Projection Validation**      | Check alignment between NLCD and other spatial layers.             |

---

## 🧹 Cleanup Policy

Temporary land cover data should be purged regularly to keep the workspace clean.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/landcover/*
```

Permanent, validated data are maintained in:

* `data/processed/landcover/` — final processed datasets
* `data/checksums/landcover/` — reproducibility hashes
* `data/processed/metadata/landcover/` — STAC metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                           |
| :---------------------- | :------------------------------------------------------- |
| **Documentation-first** | README defines structure, lifecycle, and cleanup policy. |
| **Reproducibility**     | All temporary data are regenerated deterministically.    |
| **Open Standards**      | Uses GeoTIFF, GeoJSON, CSV — no proprietary formats.     |
| **Provenance**          | Temporary files correspond to logged ETL operations.     |
| **Auditability**        | Logs provide traceable evidence of temporary workflows.  |

---

## 📎 Related Directories

| Path                                 | Description                                            |
| :----------------------------------- | :----------------------------------------------------- |
| `data/processed/landcover/`          | Final land cover datasets and derivatives.             |
| `data/checksums/landcover/`          | Integrity validation via SHA-256 hashes.               |
| `data/processed/metadata/landcover/` | STAC metadata and documentation for land cover layers. |
| `data/work/tmp/`                     | Root workspace for all temporary ETL data domains.     |

---

## 📅 Version History

| Version | Date       | Summary                                                                    |
| :------ | :--------- | :------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial land cover temporary workspace documentation (ETL, QA/QC sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Living Surface, One Test at a Time.”*
📍 [`data/work/tmp/landcover/`](.) · Temporary workspace for land cover ETL, validation, and debugging.

</div>
