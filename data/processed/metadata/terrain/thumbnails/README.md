<div align="center">

# 🖼️ Kansas Frontier Matrix — Terrain Thumbnails  
`data/processed/metadata/terrain/thumbnails/`

**Mission:** Store and document **thumbnail preview images** for all processed terrain datasets —  
including DEMs, hillshades, and slope/aspect layers — providing quick visual references  
for the Kansas Frontier Matrix web viewer, documentation, and STAC catalog.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **thumbnail images (PNGs)** automatically generated  
from processed terrain datasets documented in `data/processed/metadata/terrain/`.

Each thumbnail provides a **visual preview** of a dataset’s spatial coverage and characteristics,  
helping users identify layers in:
- The **Kansas Frontier Matrix web interface** (MapLibre map + timeline)  
- The **STAC catalog**, where each thumbnail is referenced as an asset  
- **Documentation and reports**, offering a consistent visual index  

Thumbnails are regenerated automatically whenever datasets are updated.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/terrain/thumbnails/
├── README.md
├── ks_1m_dem_2018_2020.png
├── ks_hillshade_2018_2020.png
└── slope_aspect_2018_2020.png
````

> **Note:**
> Each `.png` corresponds to a dataset described in
> `data/processed/metadata/terrain/` and is referenced by its STAC metadata JSON file
> under the `"thumbnail"` asset field.

---

## 🏔️ Thumbnail Index

| Dataset                       | Thumbnail File               | Source Data                                         | Description                                                                        |
| :---------------------------- | :--------------------------- | :-------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **DEM (1m LiDAR, 2018–2020)** | `ks_1m_dem_2018_2020.png`    | `data/processed/terrain/ks_1m_dem_2018_2020.tif`    | Grayscale elevation map derived from 1m LiDAR tiles covering Kansas.               |
| **Hillshade (Derived)**       | `ks_hillshade_2018_2020.png` | `data/processed/terrain/ks_hillshade_2018_2020.tif` | Simulated illumination effect providing topographic relief visualization.          |
| **Slope & Aspect (Derived)**  | `slope_aspect_2018_2020.png` | `data/processed/terrain/slope_aspect_2018_2020.tif` | Colorized depiction of slope steepness and aspect direction derived from DEM data. |

---

## ⚙️ Thumbnail Generation Workflow

Thumbnails are produced automatically by the **terrain ETL pipeline**.

**Makefile target:**

```bash
make terrain-thumbnails
```

**Python command:**

```bash
python src/pipelines/terrain/terrain_pipeline.py --generate-thumbnails
```

**Workflow Steps:**

1. Load terrain rasters (DEM, hillshade, slope/aspect).
2. Visualize using `matplotlib` and `rasterio.plot` with KFM-standard color schemes.
3. Scale to 1024×1024 pixels (max).
4. Save as `.png` thumbnails to this directory.
5. Update STAC metadata with thumbnail references.

Each run overwrites older previews to maintain synchronization with dataset updates.

---

## 🧮 Specifications & Provenance

| Property         | Specification                                                       |
| :--------------- | :------------------------------------------------------------------ |
| **File Type**    | PNG                                                                 |
| **Resolution**   | ≤1024×1024 px                                                       |
| **Projection**   | EPSG:4326 (WGS84)                                                   |
| **Color Scheme** | Gray ramp for DEMs, shaded relief for hillshade, rainbow aspect map |
| **Attribution**  | Derived from USGS 3DEP and Kansas DASC LiDAR data                   |
| **Regeneration** | Safe to delete; regenerated automatically by ETL pipeline           |

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                       |
| :------------------------------------------ | :------------------------------------------------------------ |
| `data/processed/metadata/terrain/*.json`    | Each STAC item links to its thumbnail via `"thumbnail"` asset |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates thumbnails automatically during ETL runs            |
| `data/stac/terrain/`                        | STAC catalog includes thumbnails in item definitions          |
| `web/config/layers.json`                    | Used as layer icons within the Frontier Matrix map interface  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                            |
| :---------------------- | :-------------------------------------------------------- |
| **Documentation-first** | Each dataset includes README + thumbnail reference        |
| **Reproducibility**     | Generated deterministically from processed terrain layers |
| **Open Standards**      | PNG format with STAC-compliant asset linking              |
| **Provenance**          | Derived from validated DEM and derivative datasets        |
| **Auditability**        | Verified via ETL logging and CI/CD regeneration           |

---

## 📅 Version History

| Version | Date       | Summary                                                                              |
| :------ | :--------- | :----------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial terrain thumbnails release — DEM, hillshade, and slope/aspect previews added |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Ground Beneath Our Feet.”*
📍 [`data/processed/metadata/terrain/thumbnails/`](.) · Linked to the **Terrain STAC Collection**

</div>
