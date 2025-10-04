<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Tiles Directory  
`data/tiles/`

**Mission:** Store and document **pre-rendered raster and vector map tiles** used by  
the Kansas Frontier Matrix (KFM) web mapping and visualization layers — enabling  
fast, reproducible access to geospatial data across time, scale, and theme.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/tiles/` directory contains **generated map tiles** used for rendering  
interactive maps in the Frontier Matrix web application and supporting STAC-linked  
visualization layers.  

Tiles are created from validated datasets under `data/processed/` and include both:  
- **Raster tiles** — Cloud-Optimized GeoTIFFs (COGs) or `.png` tilesets for basemaps, terrain, and climate.  
- **Vector tiles** — `.pbf` (Mapbox Vector Tile) layers for hydrology, boundaries, and features.  

These tiles provide performant, multi-resolution access for visualization tools such as  
**MapLibre**, **Leaflet**, and **Cesium**, supporting exploration of Kansas’s environmental, historical,  
and geospatial datasets.

---

## 🗂️ Directory Layout

```bash
data/tiles/
├── README.md
├── terrain/                 # Elevation, hillshade, and slope tiles
├── hydrology/               # Rivers, basins, and floodplain tiles
├── landcover/               # Vegetation, NLCD, and land-use classification tiles
├── climate/                 # Precipitation, temperature, and drought index tiles
├── hazards/                 # Tornado, wildfire, and flood hazard tiles
├── tabular/                 # Derived grids from structured data (e.g., population density)
└── text/                    # Text-based overlays or historical map annotations
````

> **Note:** Each subdirectory mirrors the domain structure of `data/processed/`,
> providing reproducible geospatial tiles for each dataset category.

---

## ⚙️ Tile Generation Workflow

Tiles are generated automatically from validated datasets using the ETL and rendering pipelines.

**Makefile target:**

```bash
make tiles
```

**Python command:**

```bash
python src/utils/generate_tiles.py --input data/processed/terrain/ks_1m_dem_2018_2020.tif \
                                   --output data/tiles/terrain/ks_dem_1m/
```

**Workflow Steps:**

1. Load validated geospatial datasets (COGs, GeoJSONs, or Parquets).
2. Define zoom levels and tile schema (Web Mercator, EPSG:3857).
3. Generate raster or vector tiles using GDAL, Tippecanoe, or MapTiler.
4. Save results to the appropriate domain subfolder.
5. Validate structure with the `stac-validate` GitHub workflow.

---

## 🧰 Tile Standards & Formats

| Type             | Format                        | Description                                                        |
| :--------------- | :---------------------------- | :----------------------------------------------------------------- |
| **Raster Tiles** | `.png`, `.jpg`, `.tif` (COG)  | Visual layers (terrain, landcover, climate).                       |
| **Vector Tiles** | `.pbf`                        | Encoded geometry and attribute data (rivers, hazards, boundaries). |
| **Schema**       | EPSG:3857                     | Default Web Mercator projection for global map compatibility.      |
| **Metadata**     | `metadata.json`, `tiles.json` | Defines layer info, bounding box, zoom levels, and attribution.    |

All tiles comply with [Mapbox Vector Tile Specification v2.1](https://docs.mapbox.com/data/tilesets/reference/).

---

## 🧩 Integration with the KFM Web Viewer

| Component                  | Function                                                        |
| :------------------------- | :-------------------------------------------------------------- |
| `web/config/layers.json`   | Defines layer visibility, styling, and tile endpoints.          |
| `web/app.js`               | Loads tiles dynamically in MapLibre via STAC or REST endpoints. |
| `data/processed/metadata/` | Links each tileset to its STAC item and asset metadata.         |
| `data/stac/tiles/`         | STAC catalog for spatial tile collections and coverage.         |

**Example Integration Snippet:**

```json
{
  "id": "terrain-hillshade",
  "type": "raster",
  "source": {
    "type": "raster",
    "tiles": ["data/tiles/terrain/ks_hillshade/{z}/{x}/{y}.png"],
    "tileSize": 256
  },
  "paint": {"raster-opacity": 0.85}
}
```

---

## 🧹 Cleanup & Regeneration

Tiles can be safely removed and regenerated as needed for updated datasets or styles.

**Makefile target:**

```bash
make clean-tiles
```

**Manual cleanup:**

```bash
rm -rf data/tiles/*/
```

> **Tip:** Regenerating tiles ensures consistency with the latest datasets and visualization styles.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | README defines directory purpose, workflow, and standards.            |
| **Reproducibility**     | Tiles generated deterministically via version-controlled ETL scripts. |
| **Open Standards**      | Mapbox Vector Tile Spec, GeoTIFF (COG), EPSG:3857 projection.         |
| **Provenance**          | All tiles linked to validated datasets and STAC metadata.             |
| **Auditability**        | CI workflows verify tile schema, structure, and version integrity.    |

---

## 📎 Related Directories

| Path                       | Description                                                |
| :------------------------- | :--------------------------------------------------------- |
| `data/processed/`          | Source datasets used to generate tiles.                    |
| `data/processed/metadata/` | STAC metadata describing tile provenance.                  |
| `web/config/`              | Layer configuration and visualization styles for web maps. |
| `data/stac/tiles/`         | STAC catalog of available tile layers.                     |

---

## 📅 Version History

| Version | Date       | Summary                                                                                           |
| :------ | :--------- | :------------------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial tile directory documentation — terrain, hydrology, landcover, climate, and hazard layers. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Rendering the Past and Present — One Tile at a Time.”*
📍 [`data/tiles/`](.) · Repository of reproducible raster and vector map tiles for the KFM web viewer.

</div>
