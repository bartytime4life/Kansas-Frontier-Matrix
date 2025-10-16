<div align="center">

# 🌾 Kansas Frontier Matrix — **Temporary Land Cover Workspace**  
`data/work/tmp/landcover/`

**Mission:** Provide a **sandbox workspace** for intermediate and experimental land cover files —  
including vegetation classification subsets, NLCD composites, change-detection outputs, and crop map test layers —  
used during ETL, validation, and visualization within the **Kansas Frontier Matrix (KFM)**.

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
title: "KFM • Temporary Land Cover Workspace (data/work/tmp/landcover/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-environment"]
tags: ["landcover","etl","validation","nlcd","vegetation","classification","mcp","stac"]
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

The `data/work/tmp/landcover/` directory is a **temporary, regenerable sandbox** for all **land cover ETL and QA/QC operations**  
within the Kansas Frontier Matrix (KFM) data system.  

It supports **classification, change detection, and vegetation analysis workflows**, providing a safe workspace for transient files that are automatically regenerated and purged during CI/CD cycles.

Typical contents include:

- Cropped NLCD tiles or test composites  
- Change-detection rasters for validation and QA  
- Vegetation and crop mask overlays for preview  
- Model outputs from classification algorithms (e.g., RandomForest, CNN)  
- Projection, alignment, and resampling test layers  

All data are **ephemeral**, **excluded from version control**, and **reproducible** using deterministic ETL pipelines.

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
```

> Example files are placeholders only. Actual outputs depend on current ETL operations and validation routines.

---

## ⚙️ Usage Guidelines

| Rule / Policy          | Description                                                             |
| :---------------------- | :---------------------------------------------------------------------- |
| **Ephemeral Data**      | Contents are temporary; deleted and regenerated during ETL runs.        |
| **Reproducible Output** | All data recreated deterministically using ETL workflows or Makefiles.  |
| **No Persistent Storage** | Permanent datasets belong in `data/processed/landcover/`.             |
| **CI/CD Exclusion**     | Ignored by CI except during debug or test workflows.                   |
| **Open Formats Only**   | Supported formats: GeoTIFF (COG), GeoJSON, and CSV.                    |
| **Naming Convention**   | Use descriptive names: `nlcd_preview_2025-10-16.tif`, `crop_mask_test.geojson`. |

---

## 🧩 Typical Use Cases

| Task                           | Example Description                                            |
| :------------------------------ | :------------------------------------------------------------- |
| **Classification Testing**     | Generate sample NLCD or CDL rasters for accuracy validation.   |
| **Change Detection QA**        | Compare 1992–2021 classification layers for historical trends. |
| **Vegetation Cross-Checks**    | Overlay native vegetation with NLCD-derived maps.             |
| **Crop Distribution Sampling** | Extract partial CDL datasets for regional validation.          |
| **Projection & Alignment QA**  | Reproject and align NLCD tiles with DEM or hydrology data.     |

---

## 🧰 Workflow Integration

The workspace integrates directly with KFM’s **Land Cover ETL pipeline**.

**Makefile target**

```bash
make landcover
```

**Python CLI**

```bash
python src/pipelines/landcover/landcover_pipeline.py --tmp data/work/tmp/landcover/
```

**Lifecycle Summary**

1. Raw inputs downloaded or sourced from `data/sources/landcover/`.  
2. ETL pipeline generates temporary test layers.  
3. QA/validation metrics written to `logs/landcover_etl_debug.log`.  
4. Cleanup removes temporary files post-validation or on next run.

---

## 🧹 Cleanup Policy

Temporary land cover files are **not retained** beyond the pipeline cycle.

**Automated Cleanup**

```bash
make clean-tmp
```

**Manual Cleanup**

```bash
rm -rf data/work/tmp/landcover/*
```

**Permanent Artifacts**

| Directory | Purpose |
| :--------- | :------- |
| `data/processed/landcover/` | Final processed and validated land cover datasets. |
| `data/checksums/landcover/` | SHA-256 manifests for reproducibility verification. |
| `data/processed/metadata/landcover/` | STAC metadata and lineage documentation. |

---

## 🔒 Integration with CI/CD and Metadata

| Component                             | Function                                                      |
| :------------------------------------ | :------------------------------------------------------------- |
| `src/pipelines/landcover_pipeline.py` | Generates temporary land cover intermediates and QA logs.     |
| `.github/workflows/stac-validate.yml` | Validates STAC metadata and processed land cover outputs.      |
| `data/work/tmp/`                      | Root workspace for all temporary ETL and QA subdomains.       |
| `data/checksums/landcover/`           | Hosts hash verification manifests for reproducible outputs.   |
| `data/stac/landcover/`                | STAC catalog entries linking land cover provenance.           |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README defines scope, lifecycle, and reproducibility rules.                 |
| **Reproducibility**     | Pipelines deterministically regenerate all intermediate data.               |
| **Open Standards**      | GeoTIFF (COG), GeoJSON, and CSV ensure universal interoperability.          |
| **Provenance**          | Temporary artifacts linked to logged ETL operations and metadata lineage.  |
| **Auditability**        | Logs provide traceable QA/QC history before deletion.                      |

---

## 🧩 Maintenance Recommendations

1. **Automate Cleanup:** Include `make clean-tmp` in post-ETL CI workflows.  
2. **Monitor Disk Usage:** Keep workspace ≤10 GB to avoid disk bloat.  
3. **Validate Before Deletion:** Run `make stac-validate` prior to cleanup.  
4. **Separate Domains:** Use dedicated subfolders (`landcover/`, `climate/`, etc.) for isolation.  
5. **Log Performance:** Capture QA metrics in `/logs/landcover_etl_debug.log` for performance tracking.  

---

## 📎 Related Directories

| Path                                 | Description                                            |
| :----------------------------------- | :----------------------------------------------------- |
| `data/processed/landcover/`          | Final land cover datasets and derivatives.             |
| `data/checksums/landcover/`          | Integrity validation via SHA-256 manifests.            |
| `data/processed/metadata/landcover/` | STAC metadata describing data lineage.                 |
| `data/work/tmp/`                     | Root workspace for all temporary ETL data domains.     |

---

## 📅 Version History

| Version | Date       | Summary                                                                    |
| :------ | :--------- | :------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial land cover temporary workspace documentation (ETL, QA/QC sandbox). |
| **v1.1.0** | 2025-10-10 | Added workflow integration, MCP alignment, and cleanup automation.        |
| **v1.2.0** | 2025-10-16 | Full upgrade: YAML front matter, FAIR alignment, CI/CD compliance, logs. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Living Surface, One Test at a Time.”*  
📍 [`data/work/tmp/landcover/`](.) · Temporary workspace for land cover ETL, validation, and reproducibility testing.

</div>
