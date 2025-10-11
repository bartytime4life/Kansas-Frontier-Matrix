<div align="center">

# 🖼️ Kansas Frontier Matrix — Terrain Thumbnails  
`data/processed/terrain/metadata/thumbnails/`

**Mission:** Store and describe **thumbnail preview images** for processed terrain datasets —  
including DEMs, hillshades, slope/aspect rasters, and topographic overlays —  
to support Kansas Frontier Matrix’s visualization, cataloging, and storytelling components.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **thumbnail images (PNG format)** automatically generated  
from processed terrain datasets under `data/processed/terrain/`.  

These previews serve as fast-loading **visual summaries** for:

- 🗺️ **MapLibre viewer and timeline interfaces**  
- 📂 **STAC catalog assets** (for discovery and visual indexing)  
- 📖 **Documentation, dashboards, and story maps**

Each thumbnail is a downsampled, color-rendered depiction of elevation or terrain derivatives.

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Terrain Rasters\n(data/processed/terrain/*.tif)"] --> B["Thumbnail Generator\n(Python · Matplotlib · Pillow)"]
  B --> C["Thumbnails (.png)\n(data/processed/terrain/metadata/thumbnails)"]
  C --> D["STAC Metadata\n(data/processed/terrain/metadata/*.json)"]
  D --> E["Catalog + UI\n(web/config/layers.json · MapLibre Viewer)"]
  %% END OF MERMAID
````

---

## 🗂️ Directory Layout

```bash
data/processed/terrain/metadata/thumbnails/
├── README.md
├── ks_1m_dem_2018_2020.png
├── ks_hillshade_2018_2020.png
└── slope_aspect_2018_2020.png
```

> **Note:**
> Each `.png` corresponds to a STAC metadata record in
> `data/processed/terrain/metadata/` and is referenced by the `"thumbnail"` field.

---

## 🏔️ Thumbnail Index

| Dataset                        | Thumbnail File               | Source Raster                                       | Description                                                                |
| :----------------------------- | :--------------------------- | :-------------------------------------------------- | :------------------------------------------------------------------------- |
| **DEM (1 m LiDAR, 2018–2020)** | `ks_1m_dem_2018_2020.png`    | `data/processed/terrain/ks_1m_dem_2018_2020.tif`    | Grayscale elevation preview showing statewide relief patterns.             |
| **Hillshade (Derived)**        | `ks_hillshade_2018_2020.png` | `data/processed/terrain/ks_hillshade_2018_2020.tif` | Shaded-relief rendering emphasizing slope and illumination.                |
| **Slope & Aspect (Derived)**   | `slope_aspect_2018_2020.png` | `data/processed/terrain/slope_aspect_2018_2020.tif` | Hue-coded visualization showing gradient steepness and directional aspect. |

---

## ⚙️ Thumbnail Generation Workflow

**Makefile Target**

```bash
make terrain-thumbnails
```

**Python Command**

```bash
python src/pipelines/terrain/terrain_pipeline.py --generate-thumbnails
```

### Steps

1. Load raster datasets (DEM, hillshade, slope/aspect).
2. Render using **Rasterio**, **Matplotlib**, or **Pillow**.
3. Apply KFM color ramps (grayscale → DEM, shaded → hillshade, hue → slope/aspect).
4. Downsample ≤ 1024×1024 px for quick loading.
5. Save `.png` in this folder and link to STAC JSON metadata.

> 🔁 Thumbnails are **auto-regenerated** whenever terrain data changes.

---

## 🧮 Specifications & Provenance

| Property          | Specification                                                   |
| :---------------- | :-------------------------------------------------------------- |
| **File Type**     | PNG (8-bit RGB)                                                 |
| **Resolution**    | ≤ 1024×1024 px                                                  |
| **Projection**    | EPSG:4326 (WGS 84)                                              |
| **Color Palette** | DEM → Grayscale · Hillshade → Shaded Relief · Aspect → Hue Ramp |
| **Attribution**   | Derived from USGS 3DEP & Kansas DASC LiDAR data                 |
| **Regeneration**  | Safe to delete – recreated in ETL pipeline                      |
| **Purpose**       | Lightweight visual reference for catalogs & UI                  |

---

## 🔗 Integration & Cross-References

| Linked Component                            | Role / Purpose                                         |
| :------------------------------------------ | :----------------------------------------------------- |
| `data/processed/terrain/metadata/*.json`    | References each thumbnail via `"assets.thumbnail"`     |
| `data/stac/terrain/`                        | STAC Items include thumbnails for visual discovery     |
| `src/pipelines/terrain/terrain_pipeline.py` | Generates and attaches thumbnail paths                 |
| `web/config/layers.json`                    | Displays thumbnails in layer selectors & preview cards |
| `docs/architecture.md`                      | Describes rendering and data integration architecture  |

---

## 🤖 AI & Visualization Integration

* **Feature Extraction:** AI processes analyze thumbnail color distributions to detect terrain types (plains, hills, ridges).
* **Auto-Tagging:** Preview files can carry machine-generated tags (e.g., “Flint Hills”, “Smoky Hills”) stored in `ai_metadata/`.
* **Confidence Fields:** Each AI annotation records a `confidence` value (0–1).
* **Re-Training:** Feedback from human curators improves the thumbnail classification model via `src/ai/training/terrain_visuals.py`.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                         |
| :---------------------- | :----------------------------------------------------- |
| **Documentation-first** | README + linked thumbnail descriptions per dataset     |
| **Reproducibility**     | Deterministic Makefile + scripted generation           |
| **Open Standards**      | PNG assets referenced in STAC 1.0 metadata             |
| **Provenance**          | Derived directly from processed terrain rasters        |
| **Auditability**        | Regeneration logs + CI verification ensure consistency |

---

## 🧾 Version History

| Version   | Date       | Summary of Changes                                                                            |
| :-------- | :--------- | :-------------------------------------------------------------------------------------------- |
| **1.1.0** | 2025-10-11 | Added front-matter, Mermaid flow, AI integration, and expanded badges for full MCP compliance |
| 1.0.0     | 2025-10-04 | Initial terrain thumbnail release (DEMs, hillshade, slope/aspect previews)                    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Elevation of the Past and Present.”*
📍 [`data/processed/terrain/metadata/thumbnails/`](.) · Linked to the **Terrain STAC Collection**

</div>
```
