<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazards (Staging)
`data/work/staging/hazards/`

**Purpose:** Workspace for processing, harmonizing, and validating Kansas natural-hazard datasets  
before publishing to the STAC catalog and Knowledge Graph.

[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Overview

This staging directory contains **hazard and disaster data** related to Kansas —  
including tornadoes, floods, droughts, wildfires, severe storms, and earthquakes.  
Data here are **intermediate artifacts** created during extraction and quality control  
before being finalized under `data/processed/hazards/`.

These layers underpin visualizations and analyses for:
- 🌪 **Severe weather** (tornadoes, hail, wind, thunderstorms)
- 🌊 **Hydrological hazards** (floods, flash floods, dam breaks)
- 🔥 **Fire regimes and wildfire perimeters**
- 🌵 **Droughts and climate-driven stress events**
- 🌎 **Seismic events and geological hazards**

Each dataset is tracked through ETL → STAC → Knowledge Graph to ensure provenance and  
reproducibility following **Master Coder Protocol (MCP)** standards.

---

## 🧩 Data Sources

| Source | Description | Format | Coverage | License |
|--------|--------------|---------|-----------|----------|
| [NOAA Storm Events DB](https://www.ncei.noaa.gov/stormevents/) | Severe weather events (tornado, hail, wind, flood) | CSV / API | 1950–Present | Public Domain |
| [FEMA Disaster Declarations](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries) | Declared federal disasters (flood, drought, storm) | CSV / JSON | 1953–Present | Public Domain |
| [Kansas Geological Survey (KGS)](https://www.kgs.ku.edu/) | Seismic events, sinkholes, landslides | CSV / GeoJSON | 1900–Present | Public Domain |
| [USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/search/) | Seismic activity (magnitude, depth, date) | GeoJSON / API | 1900–Present | Public Domain |
| [Kansas Forest Service / USFS](https://data.fs.usda.gov/geodata/) | Historical wildfire perimeters | Shapefile / GeoJSON | 1980–Present | Public Domain |

All datasets are defined in `data/sources/hazards_*.json`  
and registered as STAC items in `data/stac/catalog.json`.

---

## ⚙️ Workflow (ETL → STAC)

```mermaid
flowchart TD
  A["Raw Hazard Data\n(NOAA, FEMA, KGS, USGS, USFS)"] --> B["ETL Pipeline\nsrc/pipelines/hazards_etl.py"]
  B --> C["Reproject & Normalize\n(WGS84, harmonized schema)"]
  C --> D["Merge Multi-Source Layers\n(tornado, flood, quake, fire)"]
  D --> E["Generate GeoJSON & COG Overlays"]
  E --> F["Validate + QA/QC\n(check CRS, attributes, duplicates)"]
  F --> G["STAC Item Creation\n(data/stac/items/hazards_*.json)"]
  G --> H["Processed Outputs\n(data/processed/hazards/)"]
  H --> I["Knowledge Graph Ingest\n(Hazard↔Event↔Place links)"]
%% END OF MERMAID
````

**Make Targets**

```bash
make fetch-hazards     # download or update hazard datasets (NOAA, FEMA, USGS)
make process-hazards   # normalize, merge, and validate hazard data
make stac-hazards      # create STAC metadata entries
make clean-hazards     # remove temporary artifacts
```

---

## 🧠 Data Schema & Standards

* **Spatial Reference:** EPSG:4326 (WGS84)
* **Formats:** GeoJSON (vector), CSV (tabular), GeoTIFF/COG (raster hazard density)
* **Metadata:** STAC 1.0.0 JSON with temporal and spatial extent, source, license, and DOI (if available)
* **Semantic Mapping:**

  * `Place` → CIDOC CRM `E53_Place`
  * `Event` (hazard occurrence) → `E5_Event`
  * `Observation` (magnitude, intensity) → `E7_Activity`
  * `TimeSpan` → OWL-Time interval
  * `Period` → [PeriodO](https://perio.do/) (e.g., “Dust Bowl”, “2011 Tornado Outbreak”)

---

## 🧮 Integrity & Provenance

Every dataset includes:

* SHA-256 checksum file (`checksums.sha256`)
* ETL logs (`hazards_etl.log`)
* STAC validation report (`stac_validate_report.json`)
* Metadata manifest (`hazards_metadata.json`)

**Example checksum file**

```
bfa410e...  noaa_storm_events_ks_1950_2025.csv
2b7dc8a...  fema_disaster_declarations_ks.csv
12c93fe...  usgs_quakes_ks.geojson
```

Data integrity and reproducibility are enforced in CI via
checksum verification, STAC validation, and containerized builds (Trivy, CodeQL).

---

## 🧭 Integration Path

| Stage       | Upstream                           | Downstream                     |
| ----------- | ---------------------------------- | ------------------------------ |
| Input       | `data/raw/hazards/`                | `data/processed/hazards/`      |
| Output      | `data/stac/items/hazards_*.json`   | Neo4j Knowledge Graph          |
| Consumed by | Web UI (hazard overlays & filters) | Timeline + AI narrative layers |

---

## 🧩 Example Layers (for Web UI)

| Layer                       | STAC ID               | Temporal Range | Description                               |
| --------------------------- | --------------------- | -------------- | ----------------------------------------- |
| `hazards_tornado_1950_2025` | `noaa_tornadoes`      | 1950–Present   | Tornado tracks and intensities (NOAA SPC) |
| `hazards_flood_1953_2025`   | `fema_floods`         | 1953–Present   | Flood disaster declarations (FEMA)        |
| `hazards_fire_1980_2024`    | `wildfire_perimeters` | 1980–Present   | Fire perimeters and ignition points       |
| `hazards_quake_1900_2025`   | `usgs_quakes`         | 1900–Present   | Recorded earthquakes and magnitudes       |
| `hazards_drought_1890_2025` | `noaa_drought`        | 1890–Present   | Drought indices and severity maps         |

---

## 🔗 Related Documents

* [docs/architecture.md](../../../../docs/architecture.md)
* [data/sources/hazards_sources.json](../../sources/hazards_sources.json)
* [src/pipelines/hazards_etl.py](../../../../src/pipelines/hazards_etl.py)
* [docs/sop.md](../../../../docs/sop.md)
* [docs/experiment.md](../../../../docs/experiment.md)

---

<div align="center">

**Kansas Frontier Matrix**
*“Time · Terrain · History · Knowledge Graphs”*
[Docs · MCP](../../../../docs/) • [License](../../../../LICENSE)

</div>
