<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology (Staging)
`data/work/staging/hydrology/`

**Purpose:** Temporary workspace for pre-processing, cleaning, and QA/QC of hydrological datasets  
before formal publication into the STAC catalog and Knowledge Graph.

[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Overview

The **Hydrology staging area** contains intermediate and derived data used to model and visualize  
Kansas’s waterways, aquifers, floodplains, and hydro-hazards across time.  
It serves as a **working directory** between raw external sources (`data/raw/`)  
and validated processed outputs (`data/processed/hydro/`).

Data here feed into:
- **Hydrological layers** (rivers, lakes, groundwater, flood zones)
- **Temporal datasets** (streamflow, precipitation, drought indices)
- **Hazard overlays** (flood declarations, storm tracks)
- **AI/ML correlation** with settlement and climate events

---

## 🧩 Data Sources

| Source | Description | Format | Coverage | License |
|--------|--------------|---------|-----------|----------|
| [USGS NWIS](https://waterdata.usgs.gov/nwis) | Streamflow & groundwater levels | CSV / JSON | 1890–Present | Public Domain |
| [NOAA Storm Events DB](https://www.ncei.noaa.gov/stormevents/) | Floods, storms, rainfall, droughts | CSV | 1950–Present | Public Domain |
| [FEMA Disaster Declarations](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries) | Federally declared floods & droughts | CSV / API | 1953–Present | US Gov Works |
| [Kansas GIS Hub (DASC)](https://hub.kansasgis.org/) | River basins, watersheds, NHD hydrology | Shapefile / GeoJSON | Statewide | Open Government |
| [KGS / USGS 3DEP DEMs](https://apps.nationalmap.gov/lidar-explorer/) | Elevation & hydro-derived terrain | GeoTIFF / COG | Statewide | Public Domain |

All datasets are **documented in `data/sources/hydro_*.json`** manifest files and  
linked in the project STAC index (`data/stac/catalog.json`).

---

## ⚙️ Workflow (ETL → STAC)

```mermaid
flowchart TD
  A["Raw Hydrology Data\n(CSV, GeoTIFF, Shapefile)"] --> B["ETL Scripts\nsrc/pipelines/hydro_etl.py"]
  B --> C["Normalized GeoJSON/COG"]
  C --> D["Validation & QA\n(check CRS, attributes)"]
  D --> E["STAC Item Generation\n(data/stac/items/hydro_*.json)"]
  E --> F["Processed Outputs\n(data/processed/hydro/)"]
  F --> G["Knowledge Graph Ingest\n(Neo4j: Place↔Event↔Hydrology links)"]
%% END OF MERMAID
````

**Make Targets**

```bash
make fetch-hydro     # downloads latest hydrology datasets (USGS, NOAA, FEMA)
make process-hydro   # runs normalization + validation
make stac-hydro      # generates STAC items + catalog entries
make clean-hydro     # clears temporary artifacts
```

---

## 🧠 Data Schema & Standards

* **Spatial Reference:** EPSG:4326 (WGS84)
* **File Standards:** GeoJSON for vector data, COG for rasters, CSV for time-series
* **Metadata:** STAC 1.0.0 compliant JSONs with bounding box, temporal extent, and source attribution
* **Semantic Mapping:**

  * `Place` → CIDOC CRM `E53_Place`
  * `Event` (flood, drought) → `E5_Event`
  * `TimeSpan` → OWL-Time interval
  * `Period` tags (e.g., “1930s Dust Bowl”) via [PeriodO](https://perio.do/) references

---

## 🧮 Integrity & Provenance

Each ingested file is accompanied by:

* SHA-256 checksum (`checksums.sha256`)
* Processing logs (`hydro_etl.log`)
* Validation report (`stac_validate_report.json`)

**Example checksum file**

```
8b4b0b1...  usgs_streamflow_2025.csv
6e9a412...  noaa_storm_events_ks_1950_2025.csv
```

These ensure that every hydrology artifact is traceable and verifiable
according to the **Master Coder Protocol (MCP)**.

---

## 🧭 Integration Path

| Stage       | Upstream                                        | Downstream                    |
| ----------- | ----------------------------------------------- | ----------------------------- |
| Input       | `data/raw/hydro/`                               | `data/processed/hydro/`       |
| Output      | `data/stac/items/hydro_*.json`                  | Neo4j Knowledge Graph         |
| Consumed by | Web UI (MapLibre layers), Timeline events (API) | Research notebooks, AI models |

---

## 🔗 Related Documents

* [docs/architecture.md](../../../../docs/architecture.md)
* [data/sources/hydro_sources.json](../../sources/hydro_sources.json)
* [src/pipelines/hydro_etl.py](../../../../src/pipelines/hydro_etl.py)
* [docs/sop.md](../../../../docs/sop.md)
* [docs/experiment.md](../../../../docs/experiment.md)

---

<div align="center">

**Kansas Frontier Matrix**
*“Time · Terrain · History · Knowledge Graphs”*
[Docs · MCP](../../../../docs/) • [License](../../../../LICENSE)

</div>
