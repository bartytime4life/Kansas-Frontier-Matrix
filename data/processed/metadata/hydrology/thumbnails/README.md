<div align="center">

# 🖼️ Kansas Frontier Matrix — Hydrology Thumbnails  
`data/processed/metadata/hydrology/thumbnails/`

**Mission:** Store and document **thumbnail preview images** for processed hydrology datasets —  
including rivers, watersheds, flood zones, and groundwater maps — used in the web viewer, STAC catalog,  
and documentation interfaces of the Kansas Frontier Matrix.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **static PNG thumbnails** that visually summarize processed hydrology datasets  
documented in `data/processed/metadata/hydrology/`.

Thumbnails are:
- **Auto-generated** during the ETL pipeline (`make hydrology`)  
- **Linked directly** to their corresponding STAC metadata files  
- **Used by** the KFM web UI, map overlays, and documentation previews  

Each thumbnail provides a lightweight image (typically ≤500 KB) showing key hydrological features  
— rivers, watershed boundaries, flood zones, or well distributions.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/hydrology/thumbnails/
├── README.md
├── nhd_flowlines_ks_2020.png
├── watersheds_huc12_2019.png
├── fema_nfhl_2024.png
└── groundwater_levels_2025.png
````

> **Note:** Each `.png` file is referenced under the `"thumbnail"` asset field
> in its respective STAC metadata JSON under `data/processed/metadata/hydrology/`.

---

## 🌊 Thumbnail Index

| Dataset                              | Thumbnail File                | Source Data                                              | Description                                                  |
| :----------------------------------- | :---------------------------- | :------------------------------------------------------- | :----------------------------------------------------------- |
| **Rivers & Streams (NHD Flowlines)** | `nhd_flowlines_ks_2020.png`   | `data/processed/hydrology/nhd_flowlines_ks.geojson`      | Map visualization of Kansas’s river and stream network.      |
| **Watersheds (HUC-12)**              | `watersheds_huc12_2019.png`   | `data/processed/hydrology/watersheds_huc12_ks.geojson`   | Polygon overlay showing hydrologic unit boundaries.          |
| **Flood Hazard Zones (NFHL)**        | `fema_nfhl_2024.png`          | `data/processed/hydrology/fema_nfhl_ks.geojson`          | Floodplain and hazard zone visualization from FEMA data.     |
| **Groundwater Levels (NWIS)**        | `groundwater_levels_2025.png` | `data/processed/hydrology/groundwater_levels_ks.geojson` | Spatial distribution of monitoring wells and depth contours. |

---

## ⚙️ Thumbnail Generation Workflow

Thumbnails are created automatically by the hydrology ETL pipeline.

**Makefile Target:**

```bash
make hydrology-thumbnails
```

**Python Command:**

```bash
python src/pipelines/hydrology/hydrology_pipeline.py --generate-thumbnails
```

**Workflow Steps:**

1. Load datasets (`GeoJSON`, `COG`, or raster files).
2. Render hydrological features using `matplotlib`, `rasterio`, or `geopandas.plot()`.
3. Apply KFM visual style (blue-cyan gradients, transparent backgrounds).
4. Export previews as `.png` files (max 1024×1024 resolution).
5. Save here and register file paths in each STAC metadata JSON.

Each run regenerates thumbnails to reflect the latest dataset versions.

---

## 🧮 Specifications & Provenance

| Property          | Specification                                                              |
| :---------------- | :------------------------------------------------------------------------- |
| **File Type**     | PNG                                                                        |
| **Max Size**      | 1024×1024 px (≤500 KB)                                                     |
| **Projection**    | EPSG:4326 (WGS84)                                                          |
| **Color Palette** | Hydrology scheme: deep blue (rivers), cyan (flood zones), tan (watersheds) |
| **Attribution**   | Derived from USGS, EPA, FEMA, and KS DASC open data                        |
| **Regeneration**  | Safe to delete — automatically recreated during ETL runs                   |

---

## 🧩 Integration with Metadata & STAC

| Linked Component                                | Purpose                                                                 |
| :---------------------------------------------- | :---------------------------------------------------------------------- |
| `data/processed/metadata/hydrology/*.json`      | Each STAC metadata file references its thumbnail                        |
| `src/pipelines/hydrology/hydrology_pipeline.py` | Automates generation and assignment of previews                         |
| `data/stac/hydrology/`                          | Thumbnails embedded in STAC Item assets for discovery and visualization |
| `web/config/layers.json`                        | Uses thumbnail previews for legend icons and layer cards                |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                    |
| :---------------------- | :---------------------------------------------------------------- |
| **Documentation-first** | Each hydrology dataset includes an associated thumbnail reference |
| **Reproducibility**     | Thumbnails generated deterministically via ETL script             |
| **Open Standards**      | PNG format, referenced via STAC-compliant assets                  |
| **Provenance**          | Derived from documented hydrology data sources                    |
| **Auditability**        | Regenerated and verified in CI/CD processes                       |

---

## 📅 Version History

| Version | Date       | Summary                                                                     |
| :------ | :--------- | :-------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of hydrology thumbnails — NHD, WBD, NFHL, and NWIS datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Flow: Rivers, Basins, and Beyond.”*
📍 [`data/processed/metadata/hydrology/thumbnails/`](.) · Linked to the **Hydrology STAC Collection**

</div>
