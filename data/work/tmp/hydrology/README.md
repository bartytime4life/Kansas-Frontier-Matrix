<div align="center">

# 💧 Kansas Frontier Matrix — **Temporary Hydrology Workspace**  
`data/work/tmp/hydrology/`

**Mission:** Provide a **sandbox environment** for intermediate and experimental hydrology datasets —  
including rivers, watersheds, aquifers, floodplain previews, and hydrologic model outputs —  
used during ETL, validation, and QA/QC processes within the **Kansas Frontier Matrix (KFM)**.

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
title: "KFM • Temporary Hydrology Workspace (data/work/tmp/hydrology/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-hydro"]
tags: ["hydrology","etl","validation","watershed","floodplain","aquifer","checksum","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Metadata)
  - Cloud-Optimized GeoTIFF (COG)
  - FAIR Principles (Transparent & Reusable Hydrologic Workflows)
---
```

---

## 📚 Overview

The `data/work/tmp/hydrology/` directory serves as a **temporary, reproducible sandbox** for hydrologic datasets processed during ETL and QA/QC workflows in KFM.  
This environment supports rapid testing, model evaluation, and intermediate data validation without committing transient files to version control.

Typical contents include:

- Subset river and watershed GeoJSONs for ETL validation  
- Temporary floodplain or aquifer rasters for QA visualization  
- Flow accumulation and hydrologic connectivity test results  
- CRS reprojection or raster alignment checks  
- Schema validation summaries and model performance logs  

All artifacts are **short-lived**, **regenerable**, and **excluded from persistent storage**.

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
```

> **Note:** File names and contents vary depending on the ETL pipeline, test type, or QA validation being performed.

---

## ⚙️ Usage Guidelines

| Policy                   | Description                                                              |
| :----------------------- | :----------------------------------------------------------------------- |
| **Ephemeral Storage**    | All files are temporary; automatically deleted or replaced per ETL cycle. |
| **Reproducible Output**  | Artifacts can be recreated via `make hydrology` or pipeline reruns.       |
| **CI/CD Exclusion**      | Ignored by automated validation unless explicitly invoked for testing.    |
| **Open Formats Only**    | Use GeoTIFF, GeoJSON, or CSV — no proprietary formats allowed.            |
| **Safe Cleanup**         | Contents purged automatically after QA completion.                        |
| **Consistent Naming**    | Prefix files by type and date (e.g., `flood_model_2025-10-16_test.tif`).  |

---

## 🧩 Typical Use Cases

| Workflow Task             | Example Use Case                                                         |
| :------------------------- | :----------------------------------------------------------------------- |
| **Watershed Validation**  | Generate HUC-12 test subsets for watershed integrity verification.        |
| **Flood Zone QA**         | Preview and validate FEMA floodplain alignment in ETL runs.              |
| **Aquifer Model Testing** | Check spatial accuracy of well and groundwater rasters.                  |
| **Hydrology Flow Models** | Test flow accumulation or drainage delineations.                         |
| **Checksum Comparisons**  | Verify reproducibility of hydro outputs before promotion.                |

---

## 🧰 Workflow Integration

Hydrology ETL intermediates are generated automatically by the **Hydrology ETL Pipeline**.

**Makefile Target**

```bash
make hydrology
```

**Python CLI**

```bash
python src/pipelines/hydrology/hydrology_pipeline.py --tmp data/work/tmp/hydrology/
```

**Lifecycle**

1. Data is fetched and preprocessed (`data/sources/hydrology/*.json`).  
2. Temporary artifacts (GeoJSONs, rasters, tables) created under this directory.  
3. QA/QC tasks generate validation logs to `/logs/`.  
4. Upon successful verification, results are published to `data/processed/hydrology/`.  
5. Temporary data is purged automatically during cleanup.

---

## 🧹 Cleanup Policy

Hydrology workspace contents are cleared after each pipeline execution to prevent stale data retention.

**Automated Cleanup**

```bash
make clean-tmp
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/hydrology/*
```

**Permanent Artifacts**

| Directory | Purpose |
| :--------- | :------- |
| `data/processed/hydrology/` | Finalized hydrologic products (rivers, aquifers, flood zones). |
| `data/checksums/hydrology/` | SHA-256 manifests for reproducibility verification. |
| `data/processed/metadata/hydrology/` | STAC metadata documenting lineage and parameters. |

---

## 🔒 Integration with CI/CD and Metadata

| Component                              | Function                                                        |
| :------------------------------------ | :-------------------------------------------------------------- |
| `src/pipelines/hydrology_pipeline.py` | Generates, validates, and manages temporary hydrology outputs.  |
| `.github/workflows/stac-validate.yml` | Validates STAC compliance for processed hydrology datasets.     |
| `data/work/tmp/`                      | Parent workspace for transient ETL and validation outputs.      |
| `data/checksums/hydrology/`           | Maintains dataset integrity verification manifests.             |
| `data/stac/hydrology/`                | Catalogs hydrology lineage and provenance for discoverability.  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README outlines lifecycle, standards, and data flow.                        |
| **Reproducibility**     | Deterministic ETL and Make targets ensure identical regeneration.           |
| **Open Standards**      | Uses GeoTIFF, GeoJSON, CSV; STAC-aligned metadata for interoperability.     |
| **Provenance**          | Each temporary artifact traceable via logs and checksum entries.            |
| **Auditability**        | All hydrology transformations logged and reviewable before deletion.        |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Run `make clean-tmp` after each ETL cycle or CI/CD job.  
2. **Validate Before Deletion:** Always confirm `make stac-validate` passes before cleanup.  
3. **Monitor Disk Usage:** Keep workspace ≤10 GB for optimal performance.  
4. **Separate Domains:** Use domain subfolders (`hydrology/`, `terrain/`, etc.) for isolation.  
5. **Log QA Metrics:** Record validation metrics in `/logs/hydrology_etl_debug.log`.  

---

## 📎 Related Directories

| Path                                 | Description                                               |
| :----------------------------------- | :-------------------------------------------------------- |
| `data/processed/hydrology/`          | Final validated hydrology datasets.                       |
| `data/checksums/hydrology/`          | Integrity manifests for reproducibility.                  |
| `data/processed/metadata/hydrology/` | STAC metadata and lineage documentation for hydrology.    |
| `data/work/tmp/terrain/`             | Temporary workspace for related terrain data workflows.   |
| `data/work/tmp/`                     | Root workspace for all ETL temporary domains.             |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial hydrology temporary workspace documentation (ETL and QA sandbox). |
| **v1.1.0** | 2025-10-10 | Added workflow integration, provenance details, and MCP compliance.    |
| **v1.2.0** | 2025-10-16 | Upgraded for MCP-DL v6.2 alignment, FAIR data handling, and CI/CD sync.|

---

<div align="center">

**Kansas Frontier Matrix** — *“Flow Verified: Where Water Meets Data Integrity.”*  
📍 [`data/work/tmp/hydrology/`](.) · Temporary sandbox for hydrology ETL, validation, and QA testing.

</div>
