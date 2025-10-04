<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate Metadata  
`data/processed/metadata/climate/`

**Mission:** Curate, document, and standardize all **processed climate datasets**  
used to analyze temperature, precipitation, drought, and extreme weather trends  
across Kansas — integrated within the Frontier Matrix spatiotemporal knowledge system.

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

This directory contains metadata and provenance documentation for all **processed climate datasets**  
included in the Kansas Frontier Matrix (KFM). These datasets describe Kansas’s **temperature, precipitation, drought,  
and extreme climate events** — standardized for reproducibility and integration with the temporal map timeline.

Each dataset includes:
- STAC 1.0-compliant metadata (`.json`)
- SHA-256 checksums for data integrity
- JSON Schema validation entries (`data/processed/metadata/schema/`)
- Provenance fields including source URLs, license, and date of acquisition

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/climate/
├── README.md
├── daymet_1980_2024.json
├── noaa_normals_1991_2020.json
├── drought_monitor_2000_2025.json
└── thumbnails/
    ├── daymet_1980_2024.png
    ├── noaa_normals_1991_2020.png
    └── drought_monitor_2000_2025.png
````

> **Note:** Each `.json` file is a STAC-compliant metadata record for a processed climate layer
> under `data/processed/climate/`, and `/thumbnails/` holds preview images for the web app.

---

## 🌡️ Climate Layers (Processed Assets)

| Layer                                | Source          | Format                 | Spatial Resolution | Temporal Coverage | Output                                                  |
| :----------------------------------- | :-------------- | :--------------------- | :----------------- | :---------------- | :------------------------------------------------------ |
| **Daymet Daily Climate Data**        | NASA ORNL DAAC  | NetCDF → GeoTIFF (COG) | 1 km               | 1980–2024         | `data/processed/climate/daymet_1980_2024.tif`           |
| **NOAA Climate Normals (1991–2020)** | NOAA NCEI       | CSV → GeoJSON          | Station Points     | 1991–2020         | `data/processed/climate/noaa_normals_1991_2020.geojson` |
| **U.S. Drought Monitor (2000–2025)** | USDA / NOAA CPC | GeoTIFF (COG)          | 5 km               | 2000–2025         | `data/processed/climate/drought_monitor_2000_2025.tif`  |

All datasets are standardized to **EPSG:4326 (WGS84)** and indexed in the project’s STAC catalog (`data/stac/climate/`).

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "daymet_1980_2024",
  "properties": {
    "title": "Daymet Daily Surface Weather Data (1980–2024)",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Gridded daily temperature and precipitation for Kansas (1 km resolution).",
    "proj:epsg": 4326,
    "themes": ["climate", "temperature", "precipitation"],
    "license": "Public Domain (NASA ORNL DAAC)",
    "providers": [
      {"name": "NASA ORNL DAAC", "roles": ["producer"]},
      {"name": "Kansas Frontier Matrix", "roles": ["processor"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../climate/daymet_1980_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity              | Ontology Mapping                       | Example                        |
| :------------------ | :------------------------------------- | :----------------------------- |
| Climate Raster      | `E73_Information_Object` + `E53_Place` | Daymet temperature grid        |
| Drought Index       | `E16_Measurement` + OWL-Time interval  | U.S. Drought Monitor           |
| Observation Station | `E53_Place` + `E39_Actor`              | NOAA station at Topeka, KS     |
| Normals Dataset     | `E31_Document` + `P94_has_created`     | NOAA 1991–2020 normals release |

Ontology alignment enables reasoning across climate, hydrology, and landcover domains within KFM’s Neo4j knowledge graph.

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make climate` → runs `src/pipelines/climate/climate_pipeline.py`

**Dependencies:**
`xarray`, `rioxarray`, `rasterio`, `rio-cogeo`, `geopandas`, `pandas`, `requests`

**Steps:**

1. Fetch Daymet, NOAA, and Drought Monitor datasets from APIs
2. Reproject → EPSG:4326 (WGS84)
3. Clip to Kansas boundary
4. Convert NetCDF → COG / CSV → GeoJSON
5. Generate STAC metadata + thumbnails
6. Compute `.sha256` checksums for validation
7. Run schema + STAC validation in CI

All logs and provenance are stored under `data/processed/checksums/climate/`.

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` files for every processed product
* **Licensing:** NASA/NOAA public domain; derived composites → CC-BY 4.0
* **Validation:** JSON Schema + STAC 1.0 compliance (checked in CI/CD)
* **Cross-links:** Data sources referenced in `data/sources/climate/*.json`

---

## 🔗 Integration Points

| Component                    | Role                                                                        |
| :--------------------------- | :-------------------------------------------------------------------------- |
| `data/stac/climate/`         | STAC Items & Collections for discovery                                      |
| `web/config/layers.json`     | Frontend configuration for temperature, precipitation, and drought overlays |
| `src/graph/climate_nodes.py` | Knowledge graph integration                                                 |
| `docs/architecture.md`       | System design and pipeline documentation                                    |
| `data/processed/hazards/`    | Linked extreme events and drought hazard layers                             |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                             |
| :---------------------- | :----------------------------------------- |
| **Documentation-first** | README + STAC metadata per dataset         |
| **Reproducibility**     | Makefile + Python ETL pipelines            |
| **Open Standards**      | NetCDF, GeoTIFF (COG), GeoJSON             |
| **Provenance**          | URLs + SHA-256 sidecars                    |
| **Auditability**        | CI validation via STAC + JSON Schema tests |

---

## 📅 Version History

| Version | Date       | Summary                                                                                        |
| :------ | :--------- | :--------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial climate metadata release — includes Daymet, NOAA Normals, and Drought Monitor datasets |

---

## 📎 References

* [NASA ORNL DAAC Daymet](https://daac.ornl.gov/DAYMET/)
* [NOAA Climate Normals (1991–2020)](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals)
* [USDA/NOAA U.S. Drought Monitor](https://droughtmonitor.unl.edu/)
* [Cloud-Optimized GeoTIFF Specification](https://www.cogeo.org/)
* [Master Coder Protocol Documentation](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracking the Pulse of Climate Across Time and Terrain.”*
📍 [`data/processed/metadata/climate/`](.) · Integrated within the **STAC Data Catalog Layer**

</div>
