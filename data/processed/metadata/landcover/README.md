<div align="center">

# 🌾 Kansas Frontier Matrix — Land Cover Metadata  
`data/processed/metadata/landcover/`

**Mission:** Curate, document, and standardize all **processed land cover and vegetation datasets**  
to power Kansas Frontier Matrix’s long-term analysis of ecological change — from tallgrass prairie to cropland,  
and from historic vegetation surveys to modern satellite classifications.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains metadata for **land cover, vegetation, and ecological datasets**  
processed within the **Kansas Frontier Matrix (KFM)** data hub.  

These layers capture the transformation of Kansas’s surface over time —  
from the **pre-settlement prairie and forest mosaics** of the 1800s  
to the **cropland, rangeland, and urban cover** seen in modern NLCD and Landsat-era datasets.

Each dataset includes:
- STAC 1.0-compliant metadata JSON files  
- Provenance sidecars (`.sha256` checksums, source URLs, and licenses)  
- JSON Schema validation definitions (`data/processed/metadata/schema/`)  
- Full reproducibility through `make landcover` and the MCP-aligned ETL pipeline  

---

## 🗂️ Directory Layout

```bash
data/
└── processed/
    ├── landcover/                     # Processed land cover and vegetation datasets
    │   ├── nlcd_1992_2021.tif
    │   ├── kansas_vegetation_1850s.tif
    │   ├── crop_distribution_2020.geojson
    │   ├── landcover_change_1992_2021.geojson
    │   └── checksums/                 # SHA-256 validation hashes
    │
    ├── metadata/
    │   ├── landcover/                 # ← This directory (metadata, STAC, schema docs)
    │   │   ├── README.md
    │   │   ├── nlcd_1992_2021.json
    │   │   ├── vegetation_1850s.json
    │   │   └── landcover_change_1992_2021.json
    │   └── schema/                    # Shared JSON Schemas
    │       ├── landcover.schema.json
    │       └── examples/
    │           └── landcover_example.json
    │
    └── stac/
        └── landcover/                 # STAC Items / Collections
            ├── ks_landcover_collection.json
            ├── nlcd_1992_2021.json
            └── vegetation_1850s.json
````

> **Note:** Each dataset has an accompanying STAC Item for indexing and metadata validation.
> These are automatically checked in CI workflows for schema compliance.

---

## 🗺️ Land Cover Layers (Processed Assets)

| Layer                             | Source                         | Format        | Spatial Resolution | Temporal Coverage | Output                                                        |
| :-------------------------------- | :----------------------------- | :------------ | :----------------- | :---------------- | :------------------------------------------------------------ |
| **NLCD Land Cover (1992–2021)**   | USGS NLCD                      | GeoTIFF (COG) | 30 m               | 1992–2021         | `data/processed/landcover/nlcd_1992_2021.tif`                 |
| **Pre-Settlement Vegetation Map** | Kansas Biological Survey / KGS | GeoTIFF (COG) | ~1 km              | ca. 1850s         | `data/processed/landcover/kansas_vegetation_1850s.tif`        |
| **Land Cover Change Map**         | Derived from NLCD composites   | GeoJSON       | 30 m               | 1992–2021         | `data/processed/landcover/landcover_change_1992_2021.geojson` |
| **Crop Distribution (Modern)**    | USDA Cropland Data Layer (CDL) | GeoJSON       | 30 m               | 2020              | `data/processed/landcover/crop_distribution_2020.geojson`     |

All rasters use **EPSG:4326 (WGS84)** and are optimized as **Cloud-Optimized GeoTIFFs (COGs)**.
Each layer is indexed under `data/stac/landcover/`.

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "nlcd_1992_2021",
  "properties": {
    "title": "National Land Cover Database (NLCD 1992–2021)",
    "datetime": "2021-01-01T00:00:00Z",
    "description": "Land cover classification for Kansas derived from USGS NLCD data.",
    "proj:epsg": 4326,
    "themes": ["landcover", "ecology", "vegetation"],
    "license": "Public Domain (USGS)",
    "providers": [
      {"name": "USGS", "roles": ["producer"]},
      {"name": "Kansas DASC", "roles": ["processor"]},
      {"name": "Kansas Biological Survey", "roles": ["curator"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../landcover/nlcd_1992_2021.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🌐 Semantic & Ontological Alignment

| Entity              | Ontology Mapping                       | Example                      |
| :------------------ | :------------------------------------- | :--------------------------- |
| Land Cover Raster   | `E73_Information_Object` + `E53_Place` | NLCD classified raster       |
| Vegetation Class    | `E55_Type` + `P2_has_type`             | “Tallgrass Prairie”          |
| Change Event        | `E5_Event` + `P7_took_place_at`        | 1992–2021 cropland expansion |
| Dataset Publication | `E31_Document` + `P94_has_created`     | NLCD 2021 dataset release    |

These mappings support linkage to ecological and environmental ontologies
(e.g., ENVO – Environment Ontology, and CIDOC CRM extensions).

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make landcover` → executes `src/pipelines/landcover/landcover_pipeline.py`

**Dependencies:**
`rasterio`, `rio-cogeo`, `geopandas`, `numpy`, `xarray`, `pandas`, `gdal`

**ETL Steps:**

1. Fetch NLCD and vegetation datasets from USGS & Kansas DASC
2. Reproject → EPSG:4326
3. Clip to Kansas boundary
4. Generate change detection (1992–2021 composites)
5. Convert rasters to COGs and vectors to GeoJSON
6. Compute `.sha256` checksums
7. Generate and validate STAC metadata

All transformations are logged with provenance under `data/processed/checksums/landcover/`.

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` files for all products
* **Licensing:** USGS data → Public Domain; derived datasets → CC-BY 4.0
* **Validation:** STAC 1.0 + JSON Schema checks in CI
* **Provenance Chain:** All metadata references stored in `data/sources/landcover/`

---

## 🔗 Integration Points

| Component                      | Role                                                       |
| :----------------------------- | :--------------------------------------------------------- |
| `data/stac/landcover/`         | STAC Items & Collections for discovery                     |
| `web/config/layers.json`       | MapLibre configuration for vegetation & landcover overlays |
| `src/graph/landcover_nodes.py` | Knowledge graph integration (Ecosystem nodes)              |
| `docs/architecture.md`         | Architecture & ETL design reference                        |
| `data/processed/climate/`      | Linked with precipitation and drought datasets             |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                     |
| :---------------------- | :------------------------------------------------- |
| **Documentation-first** | Every layer documented with README + STAC metadata |
| **Reproducibility**     | Deterministic Makefile + Python pipelines          |
| **Open Standards**      | GeoTIFF (COG), GeoJSON, CSV                        |
| **Provenance**          | Source URLs + checksums logged                     |
| **Auditability**        | Continuous CI validation and STAC tests            |

---

## 📅 Version History

| Version | Date       | Summary                                                                                                 |
| :------ | :--------- | :------------------------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial land cover metadata release — includes NLCD, historical vegetation, and landcover change layers |

---

## 📎 References

* [USGS National Land Cover Database (NLCD)](https://www.usgs.gov/centers/eros/science/national-land-cover-database)
* [Kansas Biological Survey – Vegetation Data](https://biosurvey.ku.edu/)
* [USDA Cropland Data Layer](https://nassgeodata.gmu.edu/CropScape/)
* [Cloud-Optimized GeoTIFF Specification](https://www.cogeo.org/)
* [Master Coder Protocol Documentation](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Living Surface of the Kansas Frontier.”*
📍 [`data/processed/metadata/landcover/`](.) · Integrated within the **STAC Data Catalog Layer**

</div>
