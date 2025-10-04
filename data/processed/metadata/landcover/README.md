<div align="center">

# 🌾 Kansas Frontier Matrix — Land Cover Metadata  
`data/processed/metadata/landcover/`

**Mission:** Curate, document, and standardize all **processed land cover and vegetation datasets**  
powering Kansas Frontier Matrix’s analysis of ecological change — from pre-settlement prairies to modern cropland.

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

This directory contains **metadata and provenance documentation**  
for all **processed land cover and vegetation datasets** within Kansas Frontier Matrix (KFM).  

It tracks source lineage, schema validation, and STAC indexing for datasets such as  
NLCD composites, historical vegetation maps, crop distribution layers, and derived land cover change grids.  

Each dataset includes:
- STAC 1.0 metadata (`.json`)  
- SHA-256 checksum sidecars (`.sha256`)  
- Open data license info and provenance trail  
- Validation against shared schemas in `data/processed/metadata/schema/`

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/landcover/
├── README.md
├── nlcd_1992_2021.json
├── vegetation_1850s.json
├── landcover_change_1992_2021.json
└── thumbnails/
    ├── nlcd_1992_2021.png
    ├── vegetation_1850s.png
    └── landcover_change_1992_2021.png
````

> **Note:** Each `.json` file is a STAC-compliant metadata record describing
> a processed land cover dataset under `data/processed/landcover/`.
> The optional `/thumbnails/` folder holds static preview images for the web map UI.

---

## 🗺️ Land Cover Layers (Processed Assets)

| Layer                             | Source                   | Format        | Spatial Resolution | Temporal Coverage | Output                                                        |
| :-------------------------------- | :----------------------- | :------------ | :----------------- | :---------------- | :------------------------------------------------------------ |
| **NLCD Land Cover (1992–2021)**   | USGS NLCD                | GeoTIFF (COG) | 30 m               | 1992–2021         | `data/processed/landcover/nlcd_1992_2021.tif`                 |
| **Pre-Settlement Vegetation Map** | Kansas Biological Survey | GeoTIFF (COG) | ~1 km              | ca. 1850s         | `data/processed/landcover/kansas_vegetation_1850s.tif`        |
| **Land Cover Change (1992–2021)** | Derived (NLCD)           | GeoJSON       | 30 m               | 1992–2021         | `data/processed/landcover/landcover_change_1992_2021.geojson` |

All rasters use **EPSG:4326 (WGS84)** and are validated in the STAC catalog under `data/stac/landcover/`.

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
    "description": "Land cover classification for Kansas derived from USGS NLCD.",
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
| Vegetation Type     | `E55_Type` + `P2_has_type`             | “Tallgrass Prairie”          |
| Change Event        | `E5_Event` + `P7_took_place_at`        | 1992–2021 cropland expansion |
| Dataset Publication | `E31_Document` + `P94_has_created`     | NLCD 2021 release            |

Semantic alignment ensures interoperability with the Frontier Matrix knowledge graph
and cross-domain ontologies like **ENVO** and **CIDOC CRM**.

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make landcover` → runs `src/pipelines/landcover/landcover_pipeline.py`

**Dependencies:**
`rasterio`, `rio-cogeo`, `geopandas`, `numpy`, `pandas`, `gdal`

**Steps:**

1. Fetch NLCD, vegetation, and crop datasets from USGS and DASC
2. Reproject → EPSG 4326 (WGS84)
3. Clip to Kansas boundary shapefile
4. Generate change-detection composites (1992–2021)
5. Convert rasters → COG and vectors → GeoJSON
6. Generate STAC metadata and checksums
7. Validate with JSON Schema and STAC tools

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` files for all outputs
* **Licensing:** USGS Public Domain; derived layers → CC-BY 4.0
* **Validation:** STAC + JSON Schema + CI tests
* **Provenance:** Full lineage recorded in `data/sources/landcover/`

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                      |
| :---------------------- | :---------------------------------- |
| **Documentation-first** | README + STAC metadata per dataset  |
| **Reproducibility**     | Deterministic Makefile + Python ETL |
| **Open Standards**      | GeoTIFF (COG), GeoJSON, CSV         |
| **Provenance**          | Source URLs + SHA-256 hashes        |
| **Auditability**        | CI validation and checksum tests    |

---

## 📅 Version History

| Version | Date       | Summary                                                                                       |
| :------ | :--------- | :-------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial land cover metadata release — includes NLCD, historical vegetation, and change layers |

---

## 📎 References

* [USGS National Land Cover Database (NLCD)](https://www.usgs.gov/centers/eros/science/national-land-cover-database)
* [Kansas Biological Survey — Vegetation Data](https://biosurvey.ku.edu/)
* [USDA Cropland Data Layer (CDL)](https://nassgeodata.gmu.edu/CropScape/)
* [Cloud-Optimized GeoTIFF Spec](https://www.cogeo.org/)
* [Master Coder Protocol Docs](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Living Surface of the Kansas Frontier.”*
📍 [`data/processed/metadata/landcover/`](.) · Integrated with the **STAC Data Catalog Layer**

</div>
