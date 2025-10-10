<div align="center">

# 🌦️ Kansas Frontier Matrix — Temporary Climate Workspace  
`data/work/tmp/climate/`

**Mission:** Provide a **sandbox workspace** for intermediate and experimental climate data —  
including precipitation grids, temperature rasters, drought index tiles, and climate-normal tests —  
used during ETL, validation, and analysis in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/climate/` directory serves as a **temporary workspace**  
for all climate-related data generated or transformed during ETL, QA, and validation workflows.  

It contains intermediate outputs such as:
- Downsampled precipitation rasters for visualization  
- Temperature anomalies and climatological averages  
- Drought index tiles (e.g., SPI, PDSI subsets)  
- Reprojection and resampling tests for Daymet or NOAA datasets  
- Temporary CSV/GeoTIFF/NetCDF artifacts used for metadata validation  

All contents are **ephemeral**, **excluded from version control**, and **fully regenerable**  
using deterministic ETL workflows (e.g., `make climate` or running the `climate_pipeline.py`).

---

## 🗂️ Directory Layout

```bash
data/work/tmp/climate/
├── README.md
├── precipitation_test_tile.tif
├── drought_index_sample_2020.tif
├── noaa_normals_preview.geojson
└── logs/
    └── climate_etl_debug.log
````

> **Note:** File examples are placeholders; actual content depends on the ETL stage and validation step.

---

## ⚙️ Usage Guidelines

| Policy               | Description                                                    |
| :------------------- | :------------------------------------------------------------- |
| **Ephemeral Only**   | Files here are temporary and omitted from Git.                 |
| **Reproducible**     | All data must be regenerable through reproducible ETL scripts. |
| **CI/CD Exclusion**  | Excluded from automated builds except diagnostic checks.       |
| **Open Formats**     | Only GeoTIFF, NetCDF, CSV, and GeoJSON formats are permitted.  |
| **Cleanup Required** | Automatically cleared on rebuild or maintenance.               |

---

## ⚙️ Typical Use Cases

| Task                           | Example                                                             |
| :----------------------------- | :------------------------------------------------------------------ |
| **Precipitation Validation**   | Clip and visualize tiles to test interpolation accuracy.            |
| **Temperature Testing**        | Compare Daymet vs. NOAA temperature averages.                       |
| **Drought Analysis Debugging** | Subset SPI or PDSI layers for anomaly validation.                   |
| **Checksum Comparison**        | Verify hash consistency before release or version tagging.          |
| **Metadata QA**                | Inspect temporal coverage attributes during NetCDF → GeoTIFF tests. |

---

## 🧹 Cleanup Policy

The workspace is cleared automatically between runs to ensure reproducibility and minimize clutter.

**Makefile target**

```bash
make clean-tmp
```

**Manual cleanup**

```bash
rm -rf data/work/tmp/climate/*
```

Permanent, validated datasets reside in:

* `data/processed/climate/` — finalized climate outputs
* `data/checksums/climate/` — SHA-256 integrity hashes
* `data/processed/metadata/climate/` — STAC metadata and documentation

---

## 🧩 Integration with Pipelines

| Linked Component                            | Function                                             |
| :------------------------------------------ | :--------------------------------------------------- |
| `src/pipelines/climate/climate_pipeline.py` | Handles ETL and validation for climate data sources. |
| `.github/workflows/stac-validate.yml`       | Runs schema validation and checksum verification.    |
| `data/work/tmp/climate/logs/`               | Stores temporary ETL and QA logs.                    |
| `data/processed/climate/`                   | Stores finalized, validated climate datasets.        |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | README defines structure, lifecycle, and cleanup policy.    |
| **Reproducibility**     | Data can be regenerated deterministically through ETL runs. |
| **Open Standards**      | Uses GeoTIFF, NetCDF, CSV, and GeoJSON formats.             |
| **Provenance**          | Pipeline logs and metadata track each ETL transformation.   |
| **Auditability**        | Logs enable transparency for QA and CI/CD review processes. |

---

## 📎 Related Directories

| Path                               | Purpose                                                       |
| :--------------------------------- | :------------------------------------------------------------ |
| `data/processed/climate/`          | Permanent processed datasets (Daymet, NOAA, Drought Monitor). |
| `data/checksums/climate/`          | Integrity tracking and reproducibility validation.            |
| `data/processed/metadata/climate/` | STAC metadata and documentation for climate layers.           |
| `data/work/tmp/`                   | Parent workspace for all temporary ETL domains.               |

---

## 📅 Version History

| Version | Date       | Summary                                                            |
| :------ | :--------- | :----------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial creation of temporary climate workspace documentation.     |
| v1.0.1  | 2025-10-09 | Added YAML metadata, JSON-LD schema, provenance, and CI/CD badges. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracking the Pulse of the Plains — One Tile at a Time.”*
📍 [`data/work/tmp/climate/`](.) · Temporary workspace for climate ETL, diagnostics, and validation.

</div>
