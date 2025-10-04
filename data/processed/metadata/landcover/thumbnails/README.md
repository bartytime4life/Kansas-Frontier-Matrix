<div align="center">

# 🖼️ Kansas Frontier Matrix — Land Cover Thumbnails  
`data/processed/metadata/landcover/thumbnails/`

**Mission:** Store and document **thumbnail preview images** for Kansas Frontier Matrix’s  
processed land cover datasets — including historical vegetation, NLCD classifications, and  
derived change-detection maps — for use in the web viewer, STAC catalog, and documentation.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **thumbnail preview images (PNGs)** generated from processed  
land cover datasets documented in `data/processed/metadata/landcover/`.

Each image provides a quick visual reference for:
- The **Kansas Frontier Matrix web map** and **layer selection menus**  
- The **STAC catalog** (`thumbnail` asset field)  
- Documentation previews and reports  

Thumbnails are auto-generated during the ETL process (`make landcover`) and can be safely regenerated at any time.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/landcover/thumbnails/
├── README.md
├── nlcd_1992_2021.png
├── kansas_vegetation_1850s.png
├── landcover_change_1992_2021.png
└── crop_distribution_2020.png
````

> **Note:**
> Each `.png` corresponds to a dataset in `data/processed/metadata/landcover/` and is
> referenced via the `"thumbnail"` field in its respective STAC metadata file.

---

## 🌾 Thumbnail Index

| Dataset                               | Thumbnail File                   | Source Data                                                   | Description                                                                            |
| :------------------------------------ | :------------------------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------------- |
| **NLCD Land Cover (1992–2021)**       | `nlcd_1992_2021.png`             | `data/processed/landcover/nlcd_1992_2021.tif`                 | Map visualization of Kansas land cover classes from 1992–2021 (USGS NLCD).             |
| **Historic Vegetation (ca. 1850s)**   | `kansas_vegetation_1850s.png`    | `data/processed/landcover/kansas_vegetation_1850s.tif`        | Reconstruction of pre-settlement vegetation across Kansas (prairie, forest, wetlands). |
| **Land Cover Change Map (1992–2021)** | `landcover_change_1992_2021.png` | `data/processed/landcover/landcover_change_1992_2021.geojson` | Depicts spatial shifts from natural vegetation to cropland or urban development.       |
| **Crop Distribution (2020)**          | `crop_distribution_2020.png`     | `data/processed/landcover/crop_distribution_2020.geojson`     | Choropleth showing dominant crop types across Kansas counties (USDA CDL).              |

---

## ⚙️ Thumbnail Generation Workflow

Thumbnails are generated automatically during the **land cover ETL pipeline**.

**Makefile target:**

```bash
make landcover-thumbnails
```

**Python command:**

```bash
python src/pipelines/landcover/landcover_pipeline.py --generate-thumbnails
```

**Workflow Steps:**

1. Load raster and vector layers from `data/processed/landcover/`.
2. Visualize datasets using `matplotlib`, `geopandas`, or `rasterio.plot`.
3. Apply the Frontier Matrix color palette (green–tan–gray gradient).
4. Export each preview to PNG format (`≤1024×1024`, ≤500 KB).
5. Save to this directory and link each file in its STAC metadata JSON.

All thumbnails are automatically updated when the corresponding dataset is reprocessed.

---

## 🧮 Specifications & Provenance

| Property          | Specification                                                  |
| :---------------- | :------------------------------------------------------------- |
| **File Type**     | PNG                                                            |
| **Resolution**    | 1024×1024 px (max)                                             |
| **Projection**    | EPSG:4326 (WGS84)                                              |
| **Color Palette** | Green (vegetation), tan (cropland), gray (urban/barren)        |
| **Attribution**   | Derived from USGS, USDA, and Kansas Biological Survey datasets |
| **Regeneration**  | Safe to delete — recreated during `make landcover` runs        |

---

## 🧩 Integration with Metadata & STAC

| Linked Component                                | Purpose                                                        |
| :---------------------------------------------- | :------------------------------------------------------------- |
| `data/processed/metadata/landcover/*.json`      | Each STAC metadata file references its corresponding thumbnail |
| `src/pipelines/landcover/landcover_pipeline.py` | Generates and embeds thumbnail file paths automatically        |
| `data/stac/landcover/`                          | STAC Items include `"thumbnail"` assets for catalog previews   |
| `web/config/layers.json`                        | Displays thumbnail previews in the layer selection menu        |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                           |
| :---------------------- | :------------------------------------------------------- |
| **Documentation-first** | Every dataset has a README + thumbnail metadata          |
| **Reproducibility**     | Thumbnails generated deterministically via pipeline      |
| **Open Standards**      | PNG format, linked via STAC `"thumbnail"` assets         |
| **Provenance**          | Derived from open USGS/USDA datasets                     |
| **Auditability**        | Thumbnails validated and regenerated automatically in CI |

---

## 📅 Version History

| Version | Date       | Summary                                                                                           |
| :------ | :--------- | :------------------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial release of land cover thumbnails — NLCD, historical vegetation, crop, and change datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Changing Landscape of the Great Plains.”*
📍 [`data/processed/metadata/landcover/thumbnails/`](.) · Linked to the **Land Cover STAC Collection**

</div>
