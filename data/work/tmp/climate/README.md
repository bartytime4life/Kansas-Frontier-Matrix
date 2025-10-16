<div align="center">

# 🌦️ Kansas Frontier Matrix — **Temporary Climate Workspace**  
`data/work/tmp/climate/`

**Mission:** Serve as a **controlled sandbox environment** for intermediate and experimental climate data —  
including precipitation grids, temperature rasters, drought index tiles, and climatological test products —  
generated during ETL, validation, and QA/QC workflows within the **Kansas Frontier Matrix (KFM)** system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Temporary Climate Workspace (data/work/tmp/climate/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-climate"]
tags: ["climate","etl","validation","precipitation","temperature","drought","metadata","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Transparency & Interoperability)
  - NetCDF CF Conventions (Climate Standards)
---
```

---

## 📚 Overview

The `data/work/tmp/climate/` directory functions as a **temporary workspace** for processing, testing, and validating  
climate-related datasets within the Kansas Frontier Matrix.  

It supports the generation and verification of datasets from **NOAA**, **Daymet**, and **US Drought Monitor**,  
providing intermediate files for visual inspection, checksum validation, and model evaluation.  

**Typical contents include:**
- Precipitation and temperature rasters for test sampling  
- Drought index tiles (SPI/PDSI/NDVI subsets)  
- Reprojection tests for NetCDF → GeoTIFF conversion  
- Climate anomaly or normalization validation grids  
- Metadata and schema validation outputs  

All files are **ephemeral**, **excluded from version control**, and **regenerable deterministically** through ETL scripts or Makefile targets.

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
```

> File names and structures vary depending on ETL stage, dataset type, and QA objective.  
> All contents are deleted automatically after pipeline execution or CI/CD cleanup.

---

## ⚙️ Usage Guidelines

| Policy               | Description                                                       |
| :------------------- | :---------------------------------------------------------------- |
| **Ephemeral Only**   | All files are temporary and removed on rebuild or cleanup.        |
| **Reproducible**     | Each artifact can be recreated deterministically via `make climate`. |
| **CI/CD Exclusion**  | Ignored during builds except for diagnostic tests or validation.  |
| **Open Standards**   | Permitted formats: GeoTIFF, NetCDF, GeoJSON, CSV (UTF-8).         |
| **Cleanup Enforced** | Cleared automatically with each new ETL execution.                |
| **Naming Scheme**    | Prefix files with dataset and date (e.g., `noaa_precip_2025-10.tif`). |

---

## 🧩 Typical Use Cases

| Task                           | Example Application                                           |
| :----------------------------- | :------------------------------------------------------------ |
| **Precipitation Validation**   | Compare NOAA vs. Daymet precipitation rasters for accuracy.   |
| **Temperature Testing**        | Test downscaled temperature datasets against 30-year normals. |
| **Drought Analysis QA**        | Subset PDSI or SPI tiles to check index consistency.          |
| **Checksum Verification**      | Generate temporary hashes to confirm deterministic results.   |
| **Metadata Validation**        | Validate NetCDF metadata fields during GeoTIFF conversions.   |

---

## 🧰 Workflow Integration

Climate ETL and validation processes automatically generate temporary intermediates here.

**Makefile Target**

```bash
make climate
```

**Python CLI**

```bash
python src/pipelines/climate/climate_pipeline.py --tmp data/work/tmp/climate/
```

**Lifecycle Summary**

1. Ingest raw climate data from NOAA/Daymet/Drought Monitor APIs.  
2. Transform and validate grids (interpolation, reproject, resample).  
3. Store intermediate files and QA metrics under `data/work/tmp/climate/`.  
4. Promote validated outputs to `data/processed/climate/`.  
5. Purge workspace automatically during cleanup.

---

## 🧹 Cleanup Policy

Climate workspace data is **transient** and removed after each ETL run to maintain reproducibility.

**Automated Cleanup**

```bash
make clean-tmp
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/climate/*
```

**Permanent Data Directories**

| Directory | Purpose |
| :--------- | :------- |
| `data/processed/climate/` | Finalized, validated climate rasters and grids. |
| `data/checksums/climate/` | SHA-256 integrity manifests for reproducibility tracking. |
| `data/processed/metadata/climate/` | STAC-compliant metadata describing climate datasets. |

---

## 🔒 Integration with CI/CD and Metadata

| Component                             | Role                                                      |
| :------------------------------------ | :--------------------------------------------------------- |
| `src/pipelines/climate/climate_pipeline.py` | Executes ETL, QA, and provenance tracking.              |
| `.github/workflows/stac-validate.yml` | Validates STAC Items and checksum reproducibility.        |
| `data/work/tmp/climate/logs/`         | Stores temporary logs for ETL debugging and QA metrics.   |
| `data/checksums/climate/`             | Maintains reproducibility manifests for validated outputs. |
| `data/stac/climate/`                  | Hosts STAC entries describing climate datasets.           |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                           |
| :---------------------- | :------------------------------------------------------------------------ |
| **Documentation-first** | README defines lifecycle, scope, and reproducibility requirements.        |
| **Reproducibility**     | ETL pipelines regenerate deterministic intermediate artifacts.           |
| **Open Standards**      | Uses GeoTIFF, NetCDF, GeoJSON, and CSV under FAIR data principles.        |
| **Provenance**          | Each transformation logged with timestamps and metadata lineage.          |
| **Auditability**        | CI/CD workflows and logs enable transparent QA and trace verification.    |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Run `make clean-tmp` after every ETL execution.  
2. **Validate Before Deletion:** Ensure `make stac-validate` passes before cleanup.  
3. **Monitor Storage:** Keep total size ≤10 GB to prevent CI resource overflow.  
4. **Use Compression:** Prefer compressed GeoTIFFs (COG) for efficiency.  
5. **Log QA Steps:** Capture performance and validation metrics in `/logs/climate_etl_debug.log`.  

---

## 📎 Related Directories

| Path                               | Description                                                 |
| :--------------------------------- | :---------------------------------------------------------- |
| `data/processed/climate/`          | Final, validated climate datasets (precip, temp, drought).  |
| `data/checksums/climate/`          | Integrity validation via SHA-256 manifests.                 |
| `data/processed/metadata/climate/` | STAC metadata documenting lineage and dataset attributes.   |
| `data/work/tmp/`                   | Root workspace for all temporary ETL data subdomains.       |

---

## 📅 Version History

| Version | Date       | Summary                                                              |
| :------ | :--------- | :------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation for temporary climate workspace.              |
| **v1.1.0** | 2025-10-10 | Added ETL workflow, metadata, and STAC validation integration.      |
| **v1.2.0** | 2025-10-16 | Upgraded for MCP-DL v6.2 alignment, FAIR compliance, and CI/CD sync.|

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracking the Pulse of the Plains — One Tile at a Time.”*  
📍 [`data/work/tmp/climate/`](.) · Temporary workspace for climate ETL, validation, and QA testing.

</div>
