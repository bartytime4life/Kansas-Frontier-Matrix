<div align="center">

# 🌦 Kansas Frontier Matrix — Climate (Staging)
`data/work/staging/climate/`

**Purpose:** Temporary workspace for pre-processing, normalization, and QA/QC  
of climate and weather datasets prior to inclusion in the STAC catalog  
and integration into the Frontier-Matrix Knowledge Graph.

[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory holds **staging climate datasets** used to understand historical and contemporary  
weather patterns across Kansas. Data here form the foundation for climate-related analyses,  
such as drought reconstructions, temperature anomalies, and precipitation change detection.

**Staging purpose:** files here are *intermediate artifacts* produced during extraction and  
cleaning before promotion to `data/processed/climate/`. They are validated, reprojected,  
and formatted into COGs or CSVs ready for ingestion into the STAC catalog and graph database.

These climate data support:
- 🌡 **Temperature & precipitation trends** (annual, monthly, daily)
- ☀️ **Drought and heatwave chronologies**
- 💨 **Climate hazard overlays** (Dust Bowl, flood years, extreme cold/warm events)
- 📈 **Multi-source correlation** with hydrology and landcover datasets

---

## 🧩 Data Sources

| Source | Description | Format | Coverage | License |
|--------|--------------|---------|-----------|----------|
| [NOAA GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) | Daily station records (temperature, precipitation, snow) | CSV / API | 1880s–Present | Public Domain |
| [NASA Daymet V4](https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html) | Gridded daily weather (1 km) | NetCDF / GeoTIFF | 1980–Present | NASA Open Data |
| [NOAA U.S. Climate Normals (1991–2020)](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals) | 30-year station averages | CSV / GeoTIFF | 1991–2020 | Public Domain |
| [NOAA Paleoclimate Data (Tree Rings)](https://www.ncei.noaa.gov/products/paleoclimatology) | Drought and temperature reconstructions | CSV | 0–2000 CE | Public Domain |
| [PRISM Climate Group](https://prism.oregonstate.edu/) | Monthly precipitation & temperature rasters (4 km) | GeoTIFF / COG | 1895–Present | Public Domain |

All sources have metadata manifests in `data/sources/climate_*.json`  
and are indexed in the STAC catalog (`data/stac/catalog.json`).

---

## ⚙️ Workflow (ETL → STAC)

```mermaid
flowchart TD
  A["Raw Climate Data\n(NOAA, NASA, PRISM, Paleoclimate)"] --> B["ETL Pipeline\nsrc/pipelines/climate_etl.py"]
  B --> C["Reproject & Normalize\n(WGS84, temporal aggregation)"]
  C --> D["Generate COGs + CSV Series\n(temperature, precipitation, drought index)"]
  D --> E["QA/QC Validation\n(check CRS, anomalies, completeness)"]
  E --> F["STAC Item Creation\n(data/stac/items/climate_*.json)"]
  F --> G["Processed Output\n(data/processed/climate/)"]
  G --> H["Integration with Knowledge Graph\n(Climate↔Event↔Place links)"]
%% END OF MERMAID
````

**Make Targets**

```bash
make fetch-climate     # download all climate sources (NOAA, NASA, PRISM)
make process-climate   # normalize, reproject, generate summaries
make stac-climate      # create STAC items for all processed layers
make clean-climate     # clear temporary or staging files
```

---

## 🧠 Data Schema & Standards

* **Spatial Reference:** EPSG:4326 (WGS84)
* **Formats:**

  * Raster: Cloud-Optimized GeoTIFF (COG) for spatial layers
  * Tabular: CSV for time-series station data
* **Metadata:** STAC 1.0.0 JSON with temporal and spatial extent, source attribution, and provenance
* **Semantic Mapping:**

  * `Place` → CIDOC CRM `E53_Place`
  * `Event` (climate anomaly, drought, flood) → `E5_Event`
  * `Observation` → `E7_Activity` (with time-series attributes)
  * `TimeSpan` → OWL-Time interval
  * `Period` → [PeriodO](https://perio.do/) reference for eras (e.g., “Dust Bowl”, “Little Ice Age”)

---

## 🧮 Integrity & Provenance

Each dataset in this staging area is accompanied by:

* SHA-256 checksums (`checksums.sha256`)
* ETL logs (`climate_etl.log`)
* Validation reports (`stac_validate_report.json`)
* STAC metadata (`data/stac/items/climate_*.json`)

**Example checksum file**

```
b19f03e...  ghcn_kansas_1890_2025.csv
f4a7a12...  daymet_2023_precip_kansas.tif
c8d5e21...  prism_annual_temp_1900_2020.tif
```

All stages are validated in CI/CD and logged under **Master Coder Protocol (MCP)**
reproducibility rules (checksum verification, schema validation, containerized execution).

---

## 🧭 Integration Path

| Stage       | Upstream                         | Downstream                                          |
| ----------- | -------------------------------- | --------------------------------------------------- |
| Input       | `data/raw/climate/`              | `data/processed/climate/`                           |
| Output      | `data/stac/items/climate_*.json` | Neo4j Knowledge Graph                               |
| Consumed by | API (climate query endpoints)    | Web UI (MapLibre overlays, timeline climate layers) |

---

## 🧩 Example Layers (for Web UI)

| Layer                       | STAC ID                   | Temporal Range | Description                                  |
| --------------------------- | ------------------------- | -------------- | -------------------------------------------- |
| `climate_daymet_1980_2025`  | `daymet_kansas`           | 1980–Present   | Daily gridded climate (1 km)                 |
| `climate_prism_1895_2020`   | `prism_kansas`            | 1895–2020      | Long-term precipitation & temperature trends |
| `climate_normals_1991_2020` | `noaa_normals`            | 1991–2020      | 30-year climate normals for Kansas stations  |
| `climate_paleo_1000_1900`   | `paleoclimate_tree_rings` | 1000–1900      | Tree-ring derived drought indices            |

---

## 🔗 Related Documents

* [docs/architecture.md](../../../../docs/architecture.md)
* [data/sources/climate_sources.json](../../sources/climate_sources.json)
* [src/pipelines/climate_etl.py](../../../../src/pipelines/climate_etl.py)
* [docs/sop.md](../../../../docs/sop.md)
* [docs/experiment.md](../../../../docs/experiment.md)

---

<div align="center">

**Kansas Frontier Matrix**
*“Time · Terrain · History · Knowledge Graphs”*
[Docs · MCP](../../../../docs/) • [License](../../../../LICENSE)

</div>
