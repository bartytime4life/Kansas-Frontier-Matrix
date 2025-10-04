<div align="center">

# 🌦️ Kansas Frontier Matrix — Temporary Climate Workspace  
`data/work/tmp/climate/`

**Mission:** Provide a **sandbox workspace** for intermediate and experimental climate data —  
including precipitation grids, temperature rasters, drought index tiles, and climate-normal tests —  
used during ETL, validation, and analysis in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/climate/` directory is a **temporary workspace**  
for all climate-related data produced or transformed during ETL, QA, and validation workflows.  

Common temporary artifacts include:
- Downsampled precipitation rasters for visualization  
- Temperature anomalies or averages during ETL testing  
- Drought index tiles (e.g., SPI or PDSI subsets)  
- Reprojection or resampling tests for Daymet and NOAA datasets  
- Temporary CSVs or GeoTIFFs created during metadata and checksum validation  

All contents are **ephemeral**, **excluded from version control**, and **safe to delete**.  
They can be **fully regenerated** from the climate ETL pipeline using deterministic processes.

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

> **Note:** File examples above are placeholders; actual content depends on the
> ETL stage, dataset type, and diagnostic test currently being executed.

---

## ⚙️ Usage Guidelines

| Policy               | Description                                                    |
| :------------------- | :------------------------------------------------------------- |
| **Ephemeral Only**   | Data stored here are temporary and excluded from Git.          |
| **Reproducible**     | All data must be regenerable through ETL workflows.            |
| **CI/CD Exclusion**  | Not used in automated builds except for diagnostics.           |
| **Open Formats**     | Use open formats only (GeoTIFF, NetCDF, CSV, GeoJSON).         |
| **Cleanup Required** | Files are purged automatically during maintenance or rebuilds. |

---

## ⚙️ Typical Use Cases

| Task                           | Example                                                              |
| :----------------------------- | :------------------------------------------------------------------- |
| **Precipitation Validation**   | Create clipped tiles to check grid accuracy or resampling effects.   |
| **Temperature Testing**        | Compare annual averages between datasets (e.g., Daymet vs. NOAA).    |
| **Drought Analysis Debugging** | Generate subsets of drought indices for anomaly verification.        |
| **Checksum Comparison**        | Validate hash consistency before final publication.                  |
| **Metadata QA**                | Inspect temporal attributes in sample NetCDF-to-GeoTIFF conversions. |

---

## 🧹 Cleanup Policy

Temporary climate data should be cleared routinely to maintain reproducibility and disk efficiency.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/climate/*
```

All permanent climate datasets and metadata are located in:

* `data/processed/climate/` — validated and finalized outputs
* `data/checksums/climate/` — SHA-256 integrity verification files
* `data/processed/metadata/climate/` — STAC metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                |
| :---------------------- | :------------------------------------------------------------ |
| **Documentation-first** | README defines workspace scope and handling policy.           |
| **Reproducibility**     | All temporary outputs can be regenerated through ETL scripts. |
| **Open Standards**      | Uses GeoTIFF, NetCDF, CSV, and GeoJSON formats.               |
| **Provenance**          | Temporary data maintains traceability through ETL logs.       |
| **Auditability**        | Logs capture workflow events for debugging and transparency.  |

---

## 📎 Related Directories

| Path                               | Purpose                                                           |
| :--------------------------------- | :---------------------------------------------------------------- |
| `data/processed/climate/`          | Permanent processed climate data (Daymet, NOAA, Drought Monitor). |
| `data/checksums/climate/`          | Integrity tracking and reproducibility validation.                |
| `data/processed/metadata/climate/` | Metadata and STAC entries for climate layers.                     |
| `data/work/tmp/`                   | Parent workspace for all temporary ETL subdomains.                |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial climate temporary workspace documentation (ETL and QA sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracking the Pulse of the Plains — One Tile at a Time.”*
📍 [`data/work/tmp/climate/`](.) · Temporary workspace for climate ETL, diagnostics, and validation.

</div>
