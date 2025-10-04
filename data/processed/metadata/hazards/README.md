<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards Metadata  
`data/processed/metadata/hazards/`

**Mission:** Curate, document, and standardize all **processed natural hazard datasets**  
used in Kansas Frontier Matrix — including tornadoes, floods, droughts, wildfires, and severe weather events —  
to build a reproducible spatiotemporal understanding of risk and resilience across Kansas.

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
for all **hazard-related processed datasets** in the Kansas Frontier Matrix (KFM).  

These datasets represent **natural disasters and extreme events** — tornado tracks, flood zones,  
wildfire perimeters, drought indices, and storm records — all aligned to Kansas’s spatiotemporal framework.  

Each dataset includes:
- STAC 1.0-compliant metadata (`.json`)  
- SHA-256 checksum sidecars for reproducibility  
- Open license and provenance fields  
- Schema validation via JSON Schema + STAC CI checks  

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/hazards/
├── README.md
├── tornado_tracks_1950_2024.json
├── flood_events_1900_2025.json
├── wildfire_perimeters_2000_2024.json
└── thumbnails/
    ├── tornado_tracks_1950_2024.png
    ├── flood_events_1900_2025.png
    └── wildfire_perimeters_2000_2024.png
````

> **Note:** Each `.json` file here is a STAC-compliant metadata entry for
> its corresponding dataset in `data/processed/hazards/`.
> Thumbnails are used for the Frontier Matrix web map layer previews.

---

## 🌪️ Hazard Layers (Processed Assets)

| Layer                               | Source                     | Format        | Spatial Unit    | Temporal Coverage | Output                                                         |
| :---------------------------------- | :------------------------- | :------------ | :-------------- | :---------------- | :------------------------------------------------------------- |
| **Tornado Tracks (1950–2024)**      | NOAA SPC                   | GeoJSON       | Line            | 1950–2024         | `data/processed/hazards/tornado_tracks_1950_2024.geojson`      |
| **Flood Events (1900–2025)**        | NOAA / USGS / FEMA         | GeoJSON + CSV | Point / Polygon | 1900–2025         | `data/processed/hazards/flood_events_1900_2025.geojson`        |
| **Wildfire Perimeters (2000–2024)** | USGS / USDA Forest Service | GeoJSON       | Polygon         | 2000–2024         | `data/processed/hazards/wildfire_perimeters_2000_2024.geojson` |
| **Drought Severity Index**          | NOAA / USDA                | GeoTIFF (COG) | 5 km grid       | 2000–2025         | `data/processed/hazards/drought_index_2000_2025.tif`           |

All files are standardized to **EPSG:4326 (WGS84)** and registered under the STAC catalog (`data/stac/hazards/`).

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "tornado_tracks_1950_2024",
  "properties": {
    "title": "Kansas Tornado Tracks (1950–2024)",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "All recorded tornado tracks in Kansas from the NOAA Storm Prediction Center database.",
    "proj:epsg": 4326,
    "themes": ["hazards", "tornado", "severe_weather"],
    "license": "Public Domain (NOAA)",
    "providers": [
      {"name": "NOAA Storm Prediction Center", "roles": ["producer"]},
      {"name": "Kansas DASC", "roles": ["processor"]},
      {"name": "Kansas Frontier Matrix", "roles": ["curator"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../hazards/tornado_tracks_1950_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/tornado_tracks_1950_2024.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity        | Ontology Mapping                      | Example                                  |
| :------------ | :------------------------------------ | :--------------------------------------- |
| Tornado Track | `E5_Event` + `E53_Place`              | EF-scale 4 tornado near Greensburg, 2007 |
| Flood Event   | `E5_Event` + `P7_took_place_at`       | 1951 Kansas River Flood                  |
| Wildfire      | `E5_Event` + `E26_Physical_Feature`   | 2022 Clark County wildfire               |
| Drought Index | `E16_Measurement` + OWL-Time interval | Drought Monitor 2012                     |

Semantic alignment ensures that hazard data interconnects with
the climate, hydrology, and land cover datasets inside the Neo4j knowledge graph.

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make hazards` → executes `src/pipelines/hazards/hazards_pipeline.py`

**Dependencies:**
`geopandas`, `rasterio`, `rio-cogeo`, `pandas`, `requests`, `numpy`

**Steps:**

1. Fetch hazard data from NOAA, FEMA, USGS, and USDA APIs
2. Reproject geometries → EPSG:4326 (WGS84)
3. Standardize attribute schemas (date, type, intensity, area)
4. Generate COGs / GeoJSONs for each hazard type
5. Produce thumbnails and STAC metadata
6. Compute `.sha256` checksums for provenance
7. Validate via JSON Schema + STAC CI workflow

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` files accompany all hazard layers
* **Licensing:** NOAA / USGS data → Public Domain; derived composites → CC-BY 4.0
* **Validation:** JSON Schema + STAC 1.0 validation (automated in CI/CD)
* **Provenance:** Source, license, and date logged in `data/sources/hazards/*.json`

---

## 🔗 Integration Points

| Component                    | Role                                           |
| :--------------------------- | :--------------------------------------------- |
| `data/stac/hazards/`         | STAC Items & Collections for hazard discovery  |
| `web/config/layers.json`     | Frontend overlay configuration for hazard maps |
| `src/graph/hazards_nodes.py` | Knowledge graph integration                    |
| `docs/architecture.md`       | Pipeline & architecture documentation          |
| `data/processed/hydrology/`  | Linked flood and drought data layers           |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                              |
| :---------------------- | :------------------------------------------ |
| **Documentation-first** | README + STAC metadata per dataset          |
| **Reproducibility**     | Deterministic Makefile + Python ETL         |
| **Open Standards**      | GeoJSON, GeoTIFF (COG), CSV                 |
| **Provenance**          | Source URLs + SHA-256 checksums             |
| **Auditability**        | CI validation using STAC and checksum tests |

---

## 📅 Version History

| Version | Date       | Summary                                                                                    |
| :------ | :--------- | :----------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hazards metadata release — includes tornado, flood, wildfire, and drought datasets |

---

## 📎 References

* [NOAA Storm Events Database](https://www.ncei.noaa.gov/stormevents/)
* [FEMA Disaster Declarations Summaries](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* [USGS Wildfire Perimeter Data](https://www.usgs.gov/programs/wildland-fire-science-program)
* [USDA / NOAA U.S. Drought Monitor](https://droughtmonitor.unl.edu/)
* [Master Coder Protocol Templates](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Mapping the Footprints of Disaster Across Time.”*
📍 [`data/processed/metadata/hazards/`](.) · Integrated within the **STAC Data Catalog Layer**

</div>
