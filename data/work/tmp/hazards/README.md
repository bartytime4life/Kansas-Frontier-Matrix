<div align="center">

# ⚠️ Kansas Frontier Matrix — Temporary Hazards Workspace  
`data/work/tmp/hazards/`

**Mission:** Serve as a **sandbox workspace** for intermediate and experimental hazard datasets —  
including tornado tracks, floodplain models, wildfire perimeters, and drought zones —  
used during ETL, validation, visualization, and QA/QC workflows within the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/hazards/` directory is a **temporary workspace**  
for handling and validating hazard-related data during ETL and QA/QC runs.  

It hosts short-lived files generated during:
- Storm and flood boundary extraction  
- Wildfire perimeter clipping or reprojection  
- Tornado path QA checks and alignment tests  
- Drought index resampling and visualization  
- Temporary metadata or checksum validation reports  

All contents are **ephemeral**, **excluded from version control**, and **fully regenerable**  
using KFM’s reproducible pipelines and documented commands.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/hazards/
├── README.md
├── tornado_preview_tracks.geojson
├── flood_extent_test.tif
├── wildfire_perimeter_preview.geojson
└── logs/
    └── hazards_etl_debug.log
````

> **Note:** The file list is representative; actual filenames and content
> depend on current ETL or QA operations.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                            |
| :---------------------- | :--------------------------------------------------------------------- |
| **Ephemeral Storage**   | Files are temporary and may be deleted at any time.                    |
| **Reproducibility**     | All artifacts must be reproducible via documented ETL workflows.       |
| **CI/CD Exclusion**     | This directory is ignored in automated pipelines except for debugging. |
| **Open Standards**      | Only GeoJSON, GeoTIFF, CSV, or JSON formats are used.                  |
| **Cleanup Enforcement** | Data here is wiped automatically during `make clean-tmp`.              |

---

## ⚙️ Typical Use Cases

| Task                         | Example                                                          |
| :--------------------------- | :--------------------------------------------------------------- |
| **Flood Map QA**             | Generate temporary flood rasters for alignment testing.          |
| **Tornado Path Debugging**   | Clip or merge small GeoJSON segments for storm track validation. |
| **Wildfire Boundary Checks** | Verify perimeter accuracy or rasterize polygons for analysis.    |
| **Drought Index Testing**    | Evaluate SPI or PDSI subsets for time consistency.               |
| **Checksum Comparison**      | Validate new hazard files against reference hashes.              |

---

## 🧹 Cleanup Policy

This directory is automatically cleared during maintenance or after pipeline execution.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/hazards/*
```

Permanent and validated hazard datasets are preserved under:

* `data/processed/hazards/` — verified ETL outputs
* `data/checksums/hazards/` — SHA-256 integrity validation
* `data/processed/metadata/hazards/` — STAC metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                 |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | README defines directory purpose, workflow, and cleanup.       |
| **Reproducibility**     | Temporary outputs are fully regenerable through ETL pipelines. |
| **Open Standards**      | Uses interoperable formats (GeoTIFF, GeoJSON, CSV).            |
| **Provenance**          | Files correspond to logged ETL steps and checksum records.     |
| **Auditability**        | Logs provide traceability and diagnostics before cleanup.      |

---

## 📎 Related Directories

| Path                               | Purpose                                                         |
| :--------------------------------- | :-------------------------------------------------------------- |
| `data/processed/hazards/`          | Final hazard datasets (tornadoes, floods, wildfires, droughts). |
| `data/checksums/hazards/`          | Integrity verification for hazard data.                         |
| `data/processed/metadata/hazards/` | STAC metadata and documentation for hazard datasets.            |
| `data/work/tmp/`                   | Root temporary workspace for all KFM data domains.              |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hazards temporary workspace documentation (ETL and QA sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Verifying Every Storm, Fire, and Flood — One Test at a Time.”*
📍 [`data/work/tmp/hazards/`](.) · Temporary workspace for hazard ETL, validation, and debugging.

</div>
