<div align="center">

# 🧭 Kansas Frontier Matrix — STAC Catalog  
`data/stac/`

**Mission:** Maintain a **SpatioTemporal Asset Catalog (STAC)** archive describing all datasets  
within the Kansas Frontier Matrix (KFM) — providing a reproducible, discoverable, and  
interoperable framework for managing spatial and temporal data assets.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/stac/` directory contains the **STAC 1.0.0-compliant catalog**  
for all datasets and data products in the Kansas Frontier Matrix.  

Each STAC record describes:
- **What** the dataset is (title, description, schema)  
- **Where** and **when** it applies (spatial and temporal extent)  
- **How** it was created (provenance, providers, and processing)  
- **How** it can be accessed and reused (links, licenses, and assets)  

The STAC catalog ensures **discoverability, transparency, and reproducibility**  
across all KFM data domains — terrain, hydrology, climate, landcover, hazards, tabular, and text.

---

## 🗂️ Directory Layout

```bash
data/stac/
├── README.md
├── catalog.json                 # Root STAC catalog (links to collections)
├── terrain/                     # Terrain & elevation datasets
│   ├── collection.json
│   ├── ks_1m_dem_2018_2020.json
│   └── ks_hillshade_2018_2020.json
├── hydrology/                   # Rivers, basins, flood zones
│   ├── collection.json
│   └── watersheds_huc12_2019.json
├── landcover/                   # Vegetation, land use, crop maps
│   ├── collection.json
│   └── nlcd_1992_2021.json
├── climate/                     # Temperature, precipitation, drought indices
│   ├── collection.json
│   └── daymet_1980_2024.json
├── hazards/                     # Tornado, wildfire, flood, drought hazards
│   ├── collection.json
│   └── flood_events_1900_2025.json
├── tabular/                     # Structured data (census, agriculture, economy)
│   ├── collection.json
│   └── census_population_1860_2020.json
└── text/                        # Historical documents, transcripts, OCR text
    ├── collection.json
    └── newspaper_articles_1850_1920.json
````

> **Note:**
> Each subdirectory contains both a `collection.json` (group-level metadata)
> and individual STAC **Items** (`.json`) describing datasets and assets.

---

## 🧩 STAC Metadata Structure

Each dataset’s metadata follows the **STAC 1.0.0** specification
and the **Master Coder Protocol (MCP)** standards for reproducibility.

### 🧱 Example: STAC Item (`ks_1m_dem_2018_2020.json`)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "properties": {
    "title": "Kansas LiDAR DEM (1m, 2018–2020)",
    "description": "High-resolution Digital Elevation Model (DEM) derived from LiDAR data for Kansas.",
    "datetime": "2020-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "license": "Public Domain (USGS 3DEP)",
    "themes": ["terrain", "elevation", "topography"],
    "providers": [
      {"name": "USGS 3DEP", "roles": ["producer"]},
      {"name": "Kansas DASC", "roles": ["processor"]},
      {"name": "Kansas Frontier Matrix", "roles": ["curator"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../../processed/terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "../../processed/metadata/terrain/thumbnails/ks_1m_dem_2018_2020.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "links": [
    {"rel": "root", "href": "../catalog.json"},
    {"rel": "collection", "href": "collection.json"}
  ]
}
```

---

## ⚙️ STAC Validation & Automation

STAC metadata are **automatically validated** using the
[`stac-validate.yml`](../../.github/workflows/stac-validate.yml) workflow in GitHub Actions.

**Validation workflow:**

1. Generate STAC Items and Collections via ETL (`make stac`).
2. Run JSON Schema validation for structure compliance.
3. Verify asset links and relative paths.
4. Compute and confirm dataset checksums.
5. Publish validated catalog to the KFM web interface.

**Manual validation command:**

```bash
stac-validator data/stac/catalog.json
```

**Makefile target:**

```bash
make stac-validate
```

---

## 🧮 STAC Collections & Domains

| Domain        | Directory              | Description                                           |
| :------------ | :--------------------- | :---------------------------------------------------- |
| **Terrain**   | `data/stac/terrain/`   | DEMs, hillshades, and topographic derivatives.        |
| **Hydrology** | `data/stac/hydrology/` | Rivers, watersheds, aquifers, and flood zones.        |
| **Landcover** | `data/stac/landcover/` | Vegetation, crop distribution, and land use changes.  |
| **Climate**   | `data/stac/climate/`   | Temperature, precipitation, and drought indices.      |
| **Hazards**   | `data/stac/hazards/`   | Natural hazard maps and temporal event layers.        |
| **Tabular**   | `data/stac/tabular/`   | Structured data (census, agriculture, economy).       |
| **Text**      | `data/stac/text/`      | Documents, OCR outputs, and historical text archives. |

Each collection maintains a `collection.json` describing its datasets and
links to `catalog.json` for hierarchical navigation.

---

## 🧹 Maintenance & Rebuilding

The STAC catalog can be rebuilt or refreshed at any time to reflect new data additions or metadata updates.

**Makefile target:**

```bash
make stac
```

**Manual rebuild:**

```bash
python src/utils/build_stac_catalog.py --root data/stac/
```

**Cleanup (optional):**

```bash
make clean-stac
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | README documents STAC structure, workflow, and compliance.       |
| **Reproducibility**     | STAC catalog generated deterministically via ETL scripts.        |
| **Open Standards**      | Uses STAC 1.0.0, JSON Schema, and OGC metadata standards.        |
| **Provenance**          | Each STAC record contains source, process, and provider details. |
| **Auditability**        | Continuous STAC validation ensures full metadata traceability.   |

---

## 📎 Related Directories

| Path                       | Description                                                  |
| :------------------------- | :----------------------------------------------------------- |
| `data/processed/metadata/` | Dataset-level metadata files linked to STAC assets.          |
| `data/checksums/`          | SHA-256 verification ensuring asset integrity.               |
| `data/tiles/`              | Raster and vector tiles linked as STAC visualization assets. |
| `web/config/`              | Layer configuration files referencing STAC collections.      |

---

## 📅 Version History

| Version | Date       | Summary                                                                                    |
| :------ | :--------- | :----------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial STAC directory documentation — includes catalog hierarchy and validation workflow. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Cataloging Time, Terrain, and History — One Record at a Time.”*
📍 [`data/stac/`](.) · Central STAC catalog for all datasets in the Kansas Frontier Matrix.

</div>
