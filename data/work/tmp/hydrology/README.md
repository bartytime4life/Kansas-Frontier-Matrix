<div align="center">

# 💧 Kansas Frontier Matrix — Temporary Hydrology Workspace  
`data/work/tmp/hydrology/`

**Mission:** Serve as a **sandbox workspace** for intermediate and temporary hydrology data —  
including rivers, watersheds, aquifers, floodplain previews, and flow model test outputs —  
generated during ETL, validation, and QA/QC processes in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/hydrology/` directory is a **temporary workspace** used for processing  
and validating hydrology-related datasets during pipeline execution.  

Typical contents include:
- Subsets of river or watershed GeoJSONs for testing  
- Temporary flood zone or aquifer extent rasters  
- Preprocessing or reprojection intermediates  
- Validation logs and flow model snapshots  

Files stored here are **not version-controlled**, **safe to delete**, and are fully **reproducible**  
through KFM’s hydrology ETL and validation pipelines.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/hydrology/
├── README.md
├── nhd_subset_test.geojson
├── flood_risk_preview.tif
├── aquifer_reprojection_test.tif
└── logs/
    └── hydrology_etl_debug.log
````

> **Note:** File names and contents vary based on active ETL processes, validation tests, or debugging tasks.

---

## ⚙️ Usage Guidelines

| Policy                   | Description                                                |
| :----------------------- | :--------------------------------------------------------- |
| **Ephemeral Storage**    | Files are short-lived and excluded from version control.   |
| **Reproducible Outputs** | All data must be regenerable using ETL commands.           |
| **CI/CD Exclusion**      | This directory is ignored by CI except during diagnostics. |
| **Temporary Purpose**    | Designed for staging or validation, not long-term storage. |
| **Cleanup Policy**       | Contents are auto-deleted or replaced on pipeline rerun.   |

---

## ⚙️ Typical Use Cases

| Task                            | Example                                                             |
| :------------------------------ | :------------------------------------------------------------------ |
| **Watershed Validation**        | Test-run watershed boundaries before generating full HUC-12 layers. |
| **Flood Zone Testing**          | Generate temporary rasters to verify FEMA floodplain alignment.     |
| **Groundwater Model Debugging** | Export aquifer or well test rasters for quick inspection.           |
| **River Network QA**            | Validate vector flow directionality and geometry consistency.       |
| **Checksum Comparison**         | Recalculate hashes to confirm reproducibility before integration.   |

---

## 🧹 Cleanup Policy

Temporary hydrology data should be cleaned regularly to avoid build clutter.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/hydrology/*
```

All validated and permanent hydrology datasets are stored in:

* `data/processed/hydrology/` — finalized and validated datasets
* `data/checksums/hydrology/` — SHA-256 checksums for integrity verification
* `data/processed/metadata/hydrology/` — STAC-compliant metadata files

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                       |
| :---------------------- | :------------------------------------------------------------------- |
| **Documentation-first** | README documents structure, policy, and intended use.                |
| **Reproducibility**     | All temporary files can be recreated from ETL logs or Makefile runs. |
| **Open Standards**      | Uses GeoJSON, GeoTIFF, CSV — no proprietary formats.                 |
| **Provenance**          | Files correspond directly to ETL stages and validation logs.         |
| **Auditability**        | ETL logs under `/logs/` preserve traceable hydrology operations.     |

---

## 📎 Related Directories

| Path                                 | Purpose                                                 |
| :----------------------------------- | :------------------------------------------------------ |
| `data/processed/hydrology/`          | Final hydrology datasets (rivers, basins, floods).      |
| `data/processed/metadata/hydrology/` | Metadata and STAC records for hydrology layers.         |
| `data/checksums/hydrology/`          | Hashes for reproducibility tracking.                    |
| `data/work/tmp/terrain/`             | Temporary terrain workspace for elevation dependencies. |
| `data/work/tmp/`                     | Root workspace for all temporary ETL operations.        |

---

## 📅 Version History

| Version | Date       | Summary                                                                      |
| :------ | :--------- | :--------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hydrology temporary workspace documentation (ETL and QA/QC sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Flow Verified: Where Water Meets Data Integrity.”*
📍 [`data/work/tmp/hydrology/`](.) · Transient workspace for hydrology ETL, validation, and debugging.

</div>
