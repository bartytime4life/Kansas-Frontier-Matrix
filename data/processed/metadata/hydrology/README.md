<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Metadata (`data/processed/metadata/hydrology/`)

**Mission:** Curate, document, and standardize all **processed hydrological data layers**  
supporting Kansas Frontier Matrix’s time-aware exploration of rivers, watersheds, floods, and droughts.

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

This directory documents **hydrology-related processed datasets** for the  
Kansas Frontier Matrix (KFM) platform — integrating Kansas’s **rivers, watersheds, aquifers, and flood records**  
into a unified, reproducible geospatial data framework.

Each dataset includes:
- STAC 1.0-compliant metadata JSON files  
- Provenance records (`.sha256` checksums, license, and source URL)  
- Reproducible processing pipelines defined in `src/pipelines/hydrology/`  

These datasets power KFM’s **map and timeline layers** visualizing historical and modern hydrological changes —  
from the 1951 Kansas River Flood to modern groundwater decline in the Ogallala Aquifer.

---

## 🗺️ Hydrology Layers (Processed Assets)

| Layer | Source | Format | Spatial Unit | Temporal Coverage | Output |
|-------|---------|---------|---------------|------------------|---------|
| **Rivers & Streams (NHD Flowlines)** | USGS NHD / KS DASC | GeoJSON | Statewide | 2020 | `data/processed/hydrology/nhd_flowlines_ks.geojson` |
| **Watersheds (HUC-8/12)** | USGS WBD / EPA | GeoJSON | Subbasins | 2019 | `data/processed/hydrology/watersheds_huc12_ks.geojson` |
| **Flood Hazard Zones (NFHL)** | FEMA NFHL | GeoJSON | County | 2024 | `data/processed/hydrology/fema_nfhl_ks.geojson` |
| **Groundwater Levels (NWIS)** | USGS NWIS API | CSV → GeoJSON | Wells | 1950–2025 | `data/processed/hydrology/groundwater_levels_ks.geojson` |
| **Major Flood Events** | NOAA / USGS | CSV + GeoJSON | Event Points | 1900–2025 | `data/processed/hydrology/flood_events_ks.geojson` |

All data are standardized to **EPSG:4326 (WGS84)** and validated via  
the project’s **STAC catalog** (`data/stac/hydrology/`).

---

## 💾 Metadata Schema (STAC Example)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_watersheds_huc12_2019",
  "properties": {
    "title": "Kansas Watershed Boundaries (HUC-12, 2019)",
    "datetime": "2019-06-01T00:00:00Z",
    "description": "Watershed hydrologic units delineating Kansas subbasins under the WBD framework.",
    "proj:epsg": 4326,
    "themes": ["hydrology", "watersheds"],
    "license": "Public Domain (USGS/EPA)",
    "providers": [
      {"name": "USGS", "roles": ["producer"]},
      {"name": "EPA WBD", "roles": ["licensor"]},
      {"name": "Kansas DASC", "roles": ["processor"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../hydrology/watersheds_huc12_ks.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "../thumbnails/watersheds_huc12_ks.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
````

---

## 🧩 Semantic & Ontological Alignment

Hydrology metadata aligns with **CIDOC CRM**, **W3C OWL-Time**, and the
**HydroOntology (HY_Features)** model for cross-domain reasoning:

| Entity                  | Ontology Mapping                      | Example                 |
| ----------------------- | ------------------------------------- | ----------------------- |
| River segment           | `E26_Physical_Feature` + `E53_Place`  | Arkansas River reach    |
| Watershed               | `E27_Site` + `E53_Place`              | Smoky Hill Basin        |
| Flood Event             | `E5_Event` + `P7_took_place_at`       | 1951 Kansas River Flood |
| Observation (flow/well) | `E16_Measurement` + OWL-Time interval | NWIS groundwater record |

Each record can be temporally queried within KFM’s Neo4j graph
(e.g., *“show all hydrologic events between 1950–1970 in northeast Kansas”*).

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make hydrology` → executes `src/pipelines/hydrology/hydrology_pipeline.py`

**Dependencies:**
`geopandas`, `rasterio`, `rio-cogeo`, `requests`, `usgs`, `pandas`, `pyproj`

**ETL Steps:**

1. Fetch datasets via USGS, EPA, NOAA, and FEMA APIs
2. Harmonize geometry → `EPSG:4326` (WGS84)
3. Simplify polygons for web visualization
4. Merge multi-county shapefiles → state composite layers
5. Derive centroids, flow grids, or event points as needed
6. Export GeoJSON and generate STAC metadata
7. Compute `.sha256` checksums for provenance verification

Logs and hashes are retained in `data/processed/checksums/hydrology/`.

---

## 🧮 Provenance & Validation

* **Checksums:** SHA-256 sidecars for each file
* **Licensing:** Public domain (USGS/EPA/FEMA); derived composites → CC-BY 4.0
* **Validation:**

  * STAC Item structure validation
  * JSON Schema conformity (`data/processed/metadata/schema/`)
  * CI checks via GitHub Actions (`stac-validate.yml`)

All metadata and outputs are **traceable** from source → transformation → product.

---

## 🔗 Integration Points

| Component                      | Purpose                                   |
| ------------------------------ | ----------------------------------------- |
| `data/stac/hydrology/`         | STAC Items for all hydrology layers       |
| `web/config/layers.json`       | Map configuration for hydrology overlays  |
| `src/graph/hydrology_nodes.py` | Graph ingestion & relationships           |
| `docs/architecture.md`         | Documentation reference for ETL pipelines |
| `data/processed/hazards/`      | Linked hazard datasets (floods, droughts) |

Frontend visualizations (via MapLibreGL) use these metadata entries
to render animated flood extents, watercourse networks, and drought-affected basins
through time.

---

## 🧠 MCP Compliance Summary

| Principle               | Implementation                                     |
| ----------------------- | -------------------------------------------------- |
| **Documentation-first** | Every hydrology layer documented via STAC & README |
| **Reproducibility**     | Makefile + Python pipelines with logged parameters |
| **Open Standards**      | GeoJSON, COG, CSV, STAC, and JSON Schema           |
| **Provenance**          | Source URL, date, checksum, and license embedded   |
| **Auditability**        | CI-based validation and reproducible rebuilds      |

---

## 📅 Version History

| Version | Date       | Summary                                                                                               |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial hydrology metadata release — includes rivers, watersheds, floodplains, and groundwater layers |

---

## 📎 References

* [USGS National Hydrography Dataset (NHD)](https://www.usgs.gov/national-hydrography)
* [EPA Watershed Boundary Dataset (WBD)](https://www.epa.gov/waterdata/watershed-boundary-dataset)
* [USGS NWIS Water Data](https://waterdata.usgs.gov/nwis)
* [FEMA National Flood Hazard Layer (NFHL)](https://msc.fema.gov/portal/home)
* [NOAA Storm Events / Flood Records](https://www.ncei.noaa.gov/stormevents/)
* [Master Coder Protocol Documentation](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Tracing the Flow of Time and Water Across the Plains.”*
📍 [`data/processed/metadata/hydrology/`](.) · 🔗 Integrated with the STAC Data Catalog Layer

</div>
```
