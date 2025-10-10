<div align="center">

# ⚠️ Kansas Frontier Matrix — Temporary Hazards Workspace  
`data/work/tmp/hazards/`

**Mission:** Serve as a **sandbox workspace** for intermediate and experimental hazard datasets —  
including tornado tracks, floodplain models, wildfire perimeters, and drought zones —  
used during ETL, validation, visualization, and QA/QC workflows within the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/hazards/` directory is a **temporary workspace**  
for handling, transforming, and validating hazard-related data during ETL and QA/QC runs.  

It contains **short-lived intermediate files** generated during:
- Storm and flood boundary extraction  
- Wildfire perimeter clipping and reprojection  
- Tornado path QA alignment and buffer testing  
- Drought index resampling or temporal interpolation  
- Metadata and checksum validation diagnostics  

All contents are **ephemeral**, **excluded from version control**, and **deterministically regenerable**  
via `make hazards` or Python ETL commands.

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

> **Note:** File names vary by dataset and ETL stage.
> Artifacts are purged or replaced between runs.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                         |
| :---------------------- | :------------------------------------------------------------------ |
| **Ephemeral Storage**   | Files are temporary and safe to delete at any time.                 |
| **Reproducibility**     | All artifacts can be regenerated using deterministic ETL pipelines. |
| **CI/CD Exclusion**     | Ignored in builds except for debug review or manual QA.             |
| **Open Standards**      | Uses GeoTIFF, GeoJSON, CSV, and JSON for full interoperability.     |
| **Cleanup Enforcement** | Cleared automatically by `make clean-tmp` or scheduled maintenance. |

---

## ⚙️ Typical Use Cases

| Task                         | Example                                                            |
| :--------------------------- | :----------------------------------------------------------------- |
| **Flood Map QA**             | Generate temporary flood rasters for alignment testing.            |
| **Tornado Path Debugging**   | Merge or clip GeoJSON segments for storm-track verification.       |
| **Wildfire Boundary Checks** | Validate polygon accuracy and rasterize perimeters.                |
| **Drought Index Testing**    | Evaluate PDSI or SPI time-series subsets for temporal consistency. |
| **Checksum Comparison**      | Validate new hazard data against reference SHA-256 hashes.         |

---

## 🧹 Cleanup Policy

The hazards workspace is automatically cleared between pipeline runs to prevent clutter.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/hazards/*
```

Permanent datasets are stored in:

* `data/processed/hazards/` — validated ETL outputs
* `data/checksums/hazards/` — reproducibility hash validations
* `data/processed/metadata/hazards/` — STAC metadata documentation

---

## 🧩 Integration with Pipelines

| Linked Component                            | Function                                               |
| :------------------------------------------ | :----------------------------------------------------- |
| `src/pipelines/hazards/hazards_pipeline.py` | Handles hazard ETL, QA, and validation log generation. |
| `.github/workflows/stac-validate.yml`       | Consumes logs for checksum validation and diagnostics. |
| `data/work/tmp/hazards/logs/`               | Temporary log outputs for QA and ETL debugging.        |
| `data/processed/hazards/`                   | Destination for finalized hazard datasets.             |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                 |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | Defines structure, purpose, and lifecycle of hazard workspace. |
| **Reproducibility**     | Files regenerated deterministically through ETL workflows.     |
| **Open Standards**      | GeoTIFF, GeoJSON, and CSV ensure interoperability.             |
| **Provenance**          | Each file tied to ETL stage and metadata lineage logs.         |
| **Auditability**        | Logs under `/logs/` capture process details before cleanup.    |

---

## 📎 Related Directories

| Path                               | Purpose                                                 |
| :--------------------------------- | :------------------------------------------------------ |
| `data/work/tmp/hazards/logs/`      | Temporary ETL and QA logging workspace.                 |
| `data/processed/hazards/`          | Final validated hazard datasets.                        |
| `data/checksums/hazards/`          | Integrity verification and reproducibility tracking.    |
| `data/processed/metadata/hazards/` | STAC metadata and documentation for hazard data.        |
| `data/work/tmp/`                   | Parent scratch directory for all temporary KFM outputs. |

---

## 📅 Version History

| Version | Date       | Summary                                                    |
| :------ | :--------- | :--------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial documentation for temporary hazard workspace.      |
| v1.0.1  | 2025-10-09 | Added metadata, provenance, CI/CD badges, and MCP details. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Verifying Every Storm, Fire, and Flood — One Test at a Time.”*
📍 [`data/work/tmp/hazards/`](.) · Temporary workspace for hazard ETL, QA, and validation.

</div>
