<div align="center">

# 🖼️ Kansas Frontier Matrix — Terrain Thumbnails  
`data/processed/terrain/metadata/thumbnails/`

**Mission:** Store and describe **thumbnail preview images** for processed terrain datasets —  
including DEMs, hillshades, slope/aspect rasters, and topographic overlays —  
to support Kansas Frontier Matrix’s visualization, cataloging, and storytelling components.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **thumbnail images (PNGs)** generated automatically  
from terrain datasets under `data/processed/terrain/`.  

These small previews provide fast-loading **visual references** for:
- The **Kansas Frontier Matrix web viewer** (MapLibre interface)  
- **STAC catalog assets** for map discovery  
- **Documentation and dashboards** used in the KFM ecosystem  

Each thumbnail represents a downsampled, colorized rendering of elevation or derivative terrain data.

---

## 🗂️ Directory Layout

```bash
data/processed/terrain/metadata/thumbnails/
├── README.md
├── ks_1m_dem_2018_2020.png
├── ks_hillshade_2018_2020.png
└── slope_aspect_2018_2020.png
````

> **Note:**
> Each `.png` corresponds to a STAC metadata record under
> `data/processed/terrain/metadata/` and is referenced via the `"thumbnail"` field
> in its STAC JSON metadata file.

---

## 🏔️ Thumbnail Index

| Dataset                       | Thumbnail File               | Source Data                                         | Description                                                                 |
| :---------------------------- | :--------------------------- | :-------------------------------------------------- | :-------------------------------------------------------------------------- |
| **DEM (1m LiDAR, 2018–2020)** | `ks_1m_dem_2018_2020.png`    | `data/processed/terrain/ks_1m_dem_2018_2020.tif`    | Elevation preview rendered in grayscale gradient showing Kansas topography. |
| **Hillshade (Derived)**       | `ks_hillshade_2018_2020.png` | `data/processed/terrain/ks_hillshade_2018_2020.tif` | Shaded-relief visualization emphasizing elevation and slope variation.      |
| **Slope & Aspect (Derived)**  | `slope_aspect_2018_2020.png` | `data/processed/terrain/slope_aspect_2018_2020.tif` | Colorized visualization showing slope steepness and directional aspect.     |

---

## ⚙️ Thumbnail Generation Workflow

Thumbnails are generated automatically by the **terrain ETL pipeline**.

**Makefile target:**

```bash
make terrain-thumbnails
```

**Python command:**

```bash
python src/pipelines/terrain/terrain_pipeline.py --generate-thumbnails
```

**Workflow Steps:**

1. Load raster datasets (DEM, hillshade, slope/aspect).
2. Render previews using `rasterio`, `matplotlib`, or `Pillow`.
3. Apply KFM terrain color ramps (gray for DEMs, shaded for hillshade, hue-coded for slope/aspect).
4. Downsample to ≤1024×1024 resolution.
5. Save `.png` to this directory and register in STAC JSON metadata.

Each thumbnail is automatically regenerated whenever the terrain data changes.

---

## 🧮 Specifications & Provenance

| Property            | Specification                                                           |
| :------------------ | :---------------------------------------------------------------------- |
| **File Type**       | PNG                                                                     |
| **Resolution**      | ≤1024×1024 px                                                           |
| **Projection**      | EPSG:4326 (WGS84)                                                       |
| **Color Palette**   | Grayscale for DEMs, shaded relief for hillshade, rainbow-hue for aspect |
| **Attribution**     | Derived from USGS 3DEP and Kansas DASC LiDAR data                       |
| **Regeneration**    | Safe to delete — recreated during ETL pipeline runs                     |
| **Storage Purpose** | Lightweight visual representation for cataloging and UI preview         |

---

## 🧩 Integration with Metadata & STAC

| Linked Component                            | Purpose                                                         |
| :------------------------------------------ | :-------------------------------------------------------------- |
| `data/processed/terrain/metadata/*.json`    | Each metadata record links to its thumbnail                     |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates and attaches thumbnail paths                          |
| `data/stac/terrain/`                        | STAC Items include thumbnails as `"assets"` for visual indexing |
| `web/config/layers.json`                    | Displays thumbnails in the layer selector and preview cards     |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                               |
| :---------------------- | :----------------------------------------------------------- |
| **Documentation-first** | Every dataset includes a thumbnail reference and description |
| **Reproducibility**     | Generated deterministically via scripted ETL workflows       |
| **Open Standards**      | PNG previews referenced through STAC metadata                |
| **Provenance**          | Derived directly from processed raster layers                |
| **Auditability**        | Regeneration logs and CI verification ensure consistency     |

---

## 📅 Version History

| Version | Date       | Summary                                                                                |
| :------ | :--------- | :------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial terrain thumbnail release — includes DEM, hillshade, and slope/aspect previews |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Elevation of the Past and Present.”*
📍 [`data/processed/terrain/metadata/thumbnails/`](.) · Linked to the **Terrain STAC Collection**

</div>
