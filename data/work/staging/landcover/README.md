<div align="center">

# 🌾 Kansas Frontier Matrix — Landcover (Staging)
`data/work/staging/landcover/`

**Purpose:** Temporary workspace for harmonizing and validating Kansas landcover datasets  
before integration into the STAC catalog and Knowledge Graph.

[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Overview

This staging directory stores **intermediate landcover layers** that describe the  
vegetation, agriculture, and surface use of Kansas across time. These layers reveal  
the transformation from tallgrass prairie to cropland and urbanized land —  
central to understanding ecological and settlement history on the Kansas Frontier.

**Staging data are transient**: they are cleaned, standardized, and quality-checked here  
before being promoted to `data/processed/landcover/` and cataloged as STAC items.

Landcover data supports:
- 🗺 **Historical change detection** (prairie → cropland → developed)
- 🌿 **Ecological modeling** (habitat, carbon, fire regimes)
- 🚜 **Agricultural land-use tracking** (crop type, grazing, irrigation)
- 🌎 **Temporal storytelling** on the web map and timeline

---

## 🧩 Data Sources

| Source | Description | Format | Coverage | License |
|--------|--------------|---------|-----------|----------|
| [USGS NLCD (1992–2021)](https://www.mrlc.gov/) | National Land Cover Database | GeoTIFF / COG | Statewide | Public Domain |
| [USDA Cropland Data Layer (CDL)](https://nassgeodata.gmu.edu/CropScape/) | Crop type classification | GeoTIFF | 2008–Present | Public Domain |
| [Historical Vegetation Map (1850s–1900s)](https://pubs.usgs.gov/) | Derived from historical surveys and reconstructions | GeoTIFF / Raster | Kansas & Plains | Public Domain |
| [MODIS Land Cover (MCD12Q1)](https://modis.gsfc.nasa.gov/data/dataprod/mod12.php) | Annual global landcover (500m) | HDF / GeoTIFF | 2001–Present | NASA Open Data |
| [Kansas GIS Hub (DASC)](https://hub.kansasgis.org/) | Land use zoning, vegetation zones | Shapefile / GeoJSON | Statewide | Open Government |

Each dataset has a metadata manifest under `data/sources/landcover_*.json`  
and will be registered as a STAC item once validated.

---

## ⚙️ Workflow (ETL → STAC)

```mermaid
flowchart TD
  A["Raw Landcover Data\n(NLCD, MODIS, USDA CDL, Historical)"] --> B["ETL Pipeline\nsrc/pipelines/landcover_etl.py"]
  B --> C["Reproject & Harmonize\n(WGS84, 30m–500m resolution)"]
  C --> D["Generate COGs + GeoJSON Summaries"]
  D --> E["QA/QC & Validation\n(check CRS, reclassification, accuracy)"]
  E --> F["STAC Item Creation\n(data/stac/items/landcover_*.json)"]
  F --> G["Processed Output\n(data/processed/landcover/)"]
  G --> H["Integration with Knowledge Graph\n(Landuse↔Event↔Place links)"]
%% END OF MERMAID
````

**Make Targets**

```bash
make fetch-landcover     # download source rasters and shapefiles
make process-landcover   # reproject, reclassify, and mosaic datasets
make stac-landcover      # generate STAC items for all layers
make clean-landcover     # remove temporary files after processing
```

---

## 🧠 Data Schema & Standards

* **Spatial Reference:** EPSG:4326 (WGS84)
* **Raster Format:** Cloud-Optimized GeoTIFF (COG)
* **Vector Format:** GeoJSON (for polygons or summary zones)
* **Metadata:** STAC 1.0.0 JSON with temporal and spatial extent, source attribution, and DOI if applicable
* **Semantic Mapping:**

  * `Place` → CIDOC CRM `E53_Place`
  * `Event` (land transformation, burn, deforestation) → `E5_Event`
  * `TimeSpan` → OWL-Time interval
  * `Period` (e.g., “Dust Bowl”) → [PeriodO](https://perio.do/) references

---

## 🧮 Integrity & Provenance

Each file and artifact must include:

* SHA-256 checksums (`checksums.sha256`)
* Metadata manifest (`landcover_metadata.json`)
* Processing logs (`landcover_etl.log`)
* STAC validation reports (`stac_validate_report.json`)

**Example checksum file:**

```
af3a0d2...  nlcd_2019_kansas.tif
e0b4c91...  cdl_2022_kansas.tif
9f6f23b...  historic_veg_1880.tif
```

All checks are validated in CI as part of the **Master Coder Protocol (MCP)** reproducibility pipeline.

---

## 🧭 Integration Path

| Stage       | Upstream                           | Downstream                            |
| ----------- | ---------------------------------- | ------------------------------------- |
| Input       | `data/raw/landcover/`              | `data/processed/landcover/`           |
| Output      | `data/stac/items/landcover_*.json` | Neo4j Knowledge Graph                 |
| Consumed by | Web UI (MapLibre overlays)         | API timeline and AI narrative modules |

---

## 🧩 Example Layers (for Web UI)

| Layer                          | STAC ID        | Temporal Range | Description                                 |
| ------------------------------ | -------------- | -------------- | ------------------------------------------- |
| `landcover_nlcd_1992_2021`     | `nlcd_kansas`  | 1992–2021      | Annual NLCD maps for Kansas                 |
| `landcover_cdl_2008_2025`      | `usda_cdl`     | 2008–Present   | Crop distribution and trends                |
| `landcover_historic_1850_1900` | `historic_veg` | 1850–1900      | Reconstructed prairie and woodland coverage |

---

## 🔗 Related Documents

* [docs/architecture.md](../../../../docs/architecture.md)
* [data/sources/landcover_sources.json](../../sources/landcover_sources.json)
* [src/pipelines/landcover_etl.py](../../../../src/pipelines/landcover_etl.py)
* [docs/sop.md](../../../../docs/sop.md)
* [docs/experiment.md](../../../../docs/experiment.md)

---

<div align="center">

**Kansas Frontier Matrix**
*“Time · Terrain · History · Knowledge Graphs”*
[Docs · MCP](../../../../docs/) • [License](../../../../LICENSE)

</div>
