<div align="center">

# ⚠️ Kansas Frontier Matrix — **Temporary Hazards Workspace**  
`data/work/tmp/hazards/`

**Mission:** Provide a **sandbox workspace** for intermediate and experimental hazard datasets —  
including tornado tracks, floodplain models, wildfire perimeters, and drought zones —  
used during ETL, validation, visualization, and QA/QC workflows within the **Kansas Frontier Matrix (KFM)**.

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
title: "KFM • Temporary Hazards Workspace (data/work/tmp/hazards/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-hazards"]
tags: ["hazards","etl","validation","flood","tornado","wildfire","drought","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - FAIR Principles (Findable, Accessible, Interoperable, Reusable)
---
```

---

## 📚 Overview

The `data/work/tmp/hazards/` directory functions as a **transient, reproducible workspace**  
for testing, validating, and transforming hazard datasets within the **KFM ETL pipelines**.  
It provides an isolated environment for **disaster-related geospatial layers** under development,  
supporting reproducibility, QA transparency, and open-data traceability.

Typical temporary contents include:

- Floodplain or inundation extent rasters (FEMA, USGS, NOAA)  
- Tornado track and intensity GeoJSONs (EF scale validation)  
- Wildfire perimeter shapefiles and rasterized masks  
- Drought index (PDSI/SPI) grids for temporal QA  
- Metadata, checksum, and validation diagnostics  

All data are **short-lived**, **non-versioned**, and **regenerated automatically** on pipeline re-run.

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
```

> Example files represent typical ETL artifacts — actual contents vary per hazard workflow.  
> Files are purged and recreated at every pipeline execution.

---

## ⚙️ Usage Guidelines

| Policy                | Description                                                         |
| :-------------------- | :------------------------------------------------------------------ |
| **Ephemeral Storage** | Temporary use only; safe to delete at any time.                     |
| **Reproducible Data** | All outputs can be regenerated deterministically via ETL scripts.   |
| **CI/CD Exclusion**   | Ignored in build automation except for debug diagnostics.           |
| **Open Standards**    | Supports GeoTIFF, GeoJSON, CSV, JSON; no proprietary formats.       |
| **Cleanup Policy**    | Cleared automatically by `make clean-tmp` or scheduled maintenance. |

---

## 🧩 Typical Use Cases

| Workflow Task             | Example Application                                                |
| :------------------------- | :---------------------------------------------------------------- |
| **Flood Map QA**           | Generate temporary flood rasters for spatial alignment tests.      |
| **Tornado Path Debugging** | Merge GeoJSON segments to verify storm path continuity.            |
| **Wildfire Validation**    | Rasterize and compare perimeters to MODIS/VIIRS data.              |
| **Drought Analysis QA**    | Verify temporal PDSI or SPI datasets for interpolation accuracy.   |
| **Checksum Verification**  | Compare transient datasets to baseline hash manifests.             |

---

## 🧰 Workflow Integration

Hazard data in this workspace is produced and validated by the **Hazards ETL Pipeline**.

**Makefile Target**

```bash
make hazards
```

**Python CLI**

```bash
python src/pipelines/hazards/hazards_pipeline.py --tmp data/work/tmp/hazards/
```

### Lifecycle

1. Extract and transform raw hazard sources (tornado, flood, wildfire, drought).  
2. Generate test composites and raster derivatives.  
3. Validate classification accuracy, geometry alignment, and checksum consistency.  
4. Write QA results to `logs/hazards_etl_debug.log`.  
5. Purge workspace post-verification or via scheduled cleanup.

---

## 🧹 Cleanup Policy

The hazards workspace is **ephemeral** and cleared regularly to maintain system efficiency.

**Automated Cleanup**

```bash
make clean-tmp
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/hazards/*
```

**Permanent Data Locations**

| Directory | Description |
| :--------- | :----------- |
| `data/processed/hazards/` | Final validated hazard datasets (raster & vector). |
| `data/checksums/hazards/` | SHA-256 manifests for reproducibility tracking. |
| `data/processed/metadata/hazards/` | STAC metadata documenting hazard data lineage. |

---

## 🔒 Integration with CI/CD and Metadata Systems

| Component                             | Function                                                   |
| :------------------------------------ | :---------------------------------------------------------- |
| `src/pipelines/hazards/hazards_pipeline.py` | Handles ETL, QA, and log generation for hazard datasets.   |
| `.github/workflows/stac-validate.yml` | Validates STAC Items and checksum reproducibility.         |
| `data/work/tmp/hazards/logs/`         | Hosts temporary logs for diagnostics and QA.               |
| `data/checksums/hazards/`             | Maintains reproducibility manifests for final datasets.     |
| `data/stac/hazards/`                  | Documents lineage for hazard data collections.              |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | README defines structure, lifecycle, and policy for hazard data testing.|
| **Reproducibility**     | Deterministic ETL ensures identical regeneration for each dataset.     |
| **Open Standards**      | GeoTIFF, GeoJSON, and CSV formats ensure open accessibility.           |
| **Provenance**          | All temporary outputs linked to ETL logs and metadata lineage.         |
| **Auditability**        | QA metrics and logs reviewed prior to deletion.                        |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Integrate `make clean-tmp` in nightly CI/CD routines.  
2. **Validate Pre-Deletion:** Run `make stac-validate` before workspace purge.  
3. **Monitor Disk Usage:** Maintain workspace size ≤10 GB for large raster testing.  
4. **Enforce Naming Standards:** Use consistent prefixes (`tornado_`, `flood_`, `wildfire_`).  
5. **Log All QA Steps:** Capture metrics in `/logs/hazards_etl_debug.log` for traceability.  

---

## 📎 Related Directories

| Path                               | Description                                                |
| :--------------------------------- | :--------------------------------------------------------- |
| `data/work/tmp/hazards/logs/`      | Temporary ETL and QA logging workspace.                    |
| `data/processed/hazards/`          | Finalized hazard datasets for public release.              |
| `data/checksums/hazards/`          | SHA-256 reproducibility manifests.                         |
| `data/processed/metadata/hazards/` | STAC metadata and provenance records for hazard layers.    |
| `data/work/tmp/`                   | Root directory for all temporary ETL data domains.         |

---

## 📅 Version History

| Version | Date       | Summary                                                              |
| :------ | :--------- | :------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial hazards workspace documentation (ETL sandbox).              |
| **v1.1.0** | 2025-10-10 | Added CI/CD integration, STAC validation hooks, and cleanup policy. |
| **v1.2.0** | 2025-10-16 | Upgraded for MCP-DL v6.2 alignment and FAIR compliance.            |

---

<div align="center">

**Kansas Frontier Matrix** — *“Verifying Every Storm, Fire, and Flood — One Test at a Time.”*  
📍 [`data/work/tmp/hazards/`](.) · Temporary sandbox for hazard ETL, validation, and QA testing.

</div>
