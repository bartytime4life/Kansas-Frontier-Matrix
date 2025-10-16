<div align="center">

# 🏔️ Kansas Frontier Matrix — **Temporary Terrain Workspace**  
`data/work/tmp/terrain/`

**Mission:** Maintain a **controlled sandbox** for intermediate terrain data —  
including DEM subsets, hillshade previews, slope/aspect calculations, and reprojection tests —  
produced during ETL, QA, and validation workflows within the **Kansas Frontier Matrix (KFM)**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Temporary Terrain Workspace (data/work/tmp/terrain/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-architecture"]
tags: ["terrain","tmp","etl","validation","raster","cog","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - Cloud-Optimized GeoTIFF (COG)
  - FAIR Principles (Reusable Geospatial Workflows)
---
```

---

## 📚 Overview

The `data/work/tmp/terrain/` directory is a **sandboxed workspace** for testing, validation,  
and quality assurance of **terrain and elevation datasets** within the **Kansas Frontier Matrix (KFM)**.

It is used by ETL pipelines and CI/CD validation routines for:

- DEM mosaicking, resampling, or reprojection validation  
- Hillshade, slope, and aspect derivation QA  
- Raster comparison and schema verification  
- Temporary checksum and metadata testing  

All files are **ephemeral** and **fully reproducible** using deterministic workflows.  
No files are tracked by Git — the workspace resets automatically between runs.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/terrain/
├── README.md
├── dem_test_subset.tif
├── hillshade_preview.tif
├── slope_aspect_test_area.tif
└── logs/
    └── terrain_etl_debug.log
```

> **Note:** Example files are placeholders.  
> Actual contents vary depending on ETL process or test configuration.

---

## ⚙️ Usage Guidelines

| Rule / Policy          | Description                                                                 |
| :--------------------- | :-------------------------------------------------------------------------- |
| **Ephemeral Data**     | Files are temporary and excluded from version control.                      |
| **Reproducible Output**| All data can be regenerated via Make or ETL pipeline.                       |
| **No Persistent Storage** | Do not store validated datasets here — promote to `processed/`.          |
| **CI/CD Exclusion**    | Ignored in validation jobs unless explicitly called for testing.            |
| **Naming Convention**  | Use descriptive, timestamped names (`hillshade_test_2025-10-16.tif`).       |

---

## 🧩 Typical Use Cases

| Workflow Stage             | Example                                                        |
| :-------------------------- | :------------------------------------------------------------- |
| **DEM Subsetting**          | Crop and reproject LiDAR DEM tiles for precision testing.      |
| **Hillshade Validation**    | Generate shaded-relief renderings for slope QA.                |
| **Slope/Aspect Derivation** | Test raster derivatives using GDAL, `rasterio`, or `whitebox`. |
| **Raster Comparison**       | Validate processed COG output against baseline references.     |
| **Checksum Testing**        | Stage SHA-256 tests before final manifest inclusion.           |

---

## 🧰 ETL Workflow Integration

Terrain test files are created and managed by the **Terrain ETL pipeline**.

**Make Target:**

```bash
make terrain
```

**Python Invocation:**

```bash
python src/pipelines/terrain/terrain_pipeline.py --tmp data/work/tmp/terrain/
```

### Lifecycle Summary

1. Temporary DEM and derived layers generated for QA.  
2. Validation and visualization performed on these artifacts.  
3. Logs written to `/logs/terrain_etl_debug.log`.  
4. Cleanup removes transient files post-verification.

---

## 🧹 Cleanup Policy

Temporary terrain data is automatically purged between pipeline executions.

**Automated Cleanup**

```bash
make clean-tmp
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/terrain/*
```

**Permanent Storage Locations**

| Path                          | Purpose                                             |
| :----------------------------- | :-------------------------------------------------- |
| `data/processed/terrain/`      | Finalized terrain products (DEMs, hillshades, etc.) |
| `data/checksums/terrain/`      | Verified integrity manifests (.sha256)              |
| `data/processed/metadata/terrain/` | STAC metadata documenting provenance             |

---

## 🔒 Integration with CI/CD and Metadata

| Component                             | Function                                               |
| :------------------------------------ | :---------------------------------------------------- |
| `src/pipelines/terrain_pipeline.py`   | Handles generation, validation, and cleanup.          |
| `.github/workflows/stac-validate.yml` | Validates processed terrain STAC assets.              |
| `data/work/tmp/`                      | Shared sandbox for transient ETL test domains.        |
| `data/checksums/terrain/`             | Hosts integrity checks for final datasets.            |
| `data/stac/terrain/`                  | Maintains STAC Items linking terrain provenance.      |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README describes scope, lifecycle, and operational policy.                  |
| **Reproducibility**     | Files regenerated deterministically through `make terrain` or ETL scripts.  |
| **Open Standards**      | Uses GeoTIFF, Cloud-Optimized GeoTIFF (COG), and VRT formats.              |
| **Provenance**          | Linked to pipeline logs and STAC metadata for lineage.                      |
| **Auditability**        | Logging ensures traceability before transient cleanup.                      |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Trigger `make clean-tmp` post-ETL or test execution.  
2. **Monitor Disk Space:** Limit workspace size to **≤10 GB** for efficient CI operations.  
3. **Validate Before Deletion:** Run `make stac-validate` before cleanup to confirm QA success.  
4. **Isolate Domains:** Keep `terrain/` separate from `hydrology/`, `climate/`, and other tmp subdomains.  
5. **Track Changes:** Use timestamped logs to correlate artifacts with ETL commits.  

---

## 📎 Related Directories

| Path                             | Description                                           |
| :------------------------------- | :---------------------------------------------------- |
| `data/processed/terrain/`        | Final, validated DEM and derivative terrain data.     |
| `data/checksums/terrain/`        | Integrity validation manifests (.sha256).             |
| `data/processed/metadata/terrain/` | STAC metadata describing terrain lineage.            |
| `data/work/tmp/`                 | Parent folder for all ETL domain temporary subspaces. |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial creation and documentation of temporary terrain workspace.     |
| **v1.1.0** | 2025-10-10 | Added workflow integration, usage table, and cleanup policies.        |
| **v1.2.0** | 2025-10-16 | Full MCP-DL v6.2 alignment: YAML metadata, CI/CD integration, QA rules.|

---

<div align="center">

**Kansas Frontier Matrix** — *“Temporary by Design · Verified by Process.”*  
📍 [`data/work/tmp/terrain/`](.) — ephemeral sandbox for terrain ETL experimentation, QA, and reproducibility testing.

</div>
