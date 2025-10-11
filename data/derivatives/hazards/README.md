<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazard Derivatives

`data/derivatives/hazards/`

**Mission:** Curate and document all **hazard-related geospatial derivatives** — drought, flood, wildfire, tornado,
and severe-weather composites — generated from historical archives, remote sensing products, and national hazard databases.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/pre-commit.yml?label=Pre--Commit)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)
[![Version](https://img.shields.io/badge/Version-v1.2.0-blueviolet)](#-version-history)

</div>

---

## 📚 Table of Contents

* [Overview](#overview)
* [Directory Layout](#directory-layout)
* [Core Hazard Products](#core-hazard-products)
* [STAC Metadata](#stac-metadata)
* [Processing Workflow](#processing-workflow)
* [Reproducibility & Validation](#reproducibility--validation)
* [Versioning & Changelog](#versioning--changelog)
* [Contributing New Hazard Layers](#contributing-new-hazard-layers)
* [References](#references)

---

## 🌪️ Overview

The **Hazard Derivatives** directory provides spatiotemporal layers representing Kansas’s historical and environmental risk patterns.
These composites integrate **drought, flood, wildfire, tornado, and severe storm** data from national and state-level archives.

Data sources include:

* **NOAA Storm Events** & **SPC Tornado Tracks**
* **FEMA Disaster Declarations**
* **US Drought Monitor** (NDMC / USDA / NOAA)
* **NASA FIRMS** Fire and Thermal Anomaly data
* **USGS** hydrological flood models

Outputs are harmonized to **EPSG:4326**, published as **COGs** and **GeoJSON**, and registered within the
[Kansas Frontier Matrix STAC catalog](../../stac/) for open access and validation.

---

## 🧭 Metadata Snapshot

| Field            | Value                        |
| :--------------- | :--------------------------- |
| **Version**      | `v1.2.0`                     |
| **Last Updated** | `2025-10-11`                 |
| **Maintainer**   | KFM Hazards & Climate Team   |
| **Schema**       | STAC 1.0.0 + MCP v2.1        |
| **Licenses**     | CC-BY 4.0 (Data), MIT (Code) |

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── hazards/
        ├── drought_spi_1950_2020.tif         # 12-month SPI index
        ├── flood_extent_1993_ks.tif          # 1993 Midwest flood composite
        ├── tornado_density_1950_2024.tif     # Kernel density of tornado tracks
        ├── wildfire_frequency_2000_2023.tif  # MODIS fire frequency raster
        ├── hazards_summary.geojson           # Combined hazard risk index
        ├── metadata/
        │   ├── drought_spi_1950_2020.json
        │   ├── flood_extent_1993_ks.json
        │   └── tornado_density_1950_2024.json
        ├── checksums/
        │   ├── drought_spi_1950_2020.tif.sha256
        │   ├── flood_extent_1993_ks.tif.sha256
        │   └── tornado_density_1950_2024.tif.sha256
        └── README.md
```

---

## 🌩️ Core Hazard Products

| Product                            | File                               | Description                                                    | Source       | Units            | Format        |
| :--------------------------------- | :--------------------------------- | :------------------------------------------------------------- | :----------- | :--------------- | :------------ |
| **Drought SPI (1950–2020)**        | `drought_spi_1950_2020.tif`        | 12-month Standardized Precipitation Index for drought severity | NOAA + PRISM | unitless         | GeoTIFF (COG) |
| **Flood Extent (1993)**            | `flood_extent_1993_ks.tif`         | Composite flood zones from 1993 Midwest flood                  | USGS + FEMA  | binary (0/1)     | GeoTIFF (COG) |
| **Tornado Density (1950–2024)**    | `tornado_density_1950_2024.tif`    | Kernel density raster of tornado tracks                        | NOAA SPC     | events/km²       | GeoTIFF (COG) |
| **Wildfire Frequency (2000–2023)** | `wildfire_frequency_2000_2023.tif` | MODIS-derived fire frequency raster                            | NASA FIRMS   | % occurrence     | GeoTIFF (COG) |
| **Hazard Summary Zones**           | `hazards_summary.geojson`          | Combined hazard index across all hazard types                  | Composite    | normalized (0–1) | GeoJSON       |

---

## 🧩 STAC Metadata Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "tornado_density_1950_2024",
  "properties": {
    "title": "Tornado Density (1950–2024) – Kansas",
    "description": "Kernel density raster of tornado paths derived from NOAA SPC dataset.",
    "datetime": "2024-01-01T00:00:00Z",
    "processing:software": "Python 3.11 + GDAL 3.8",
    "mcp_provenance": "sha256:b52f8e...",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/sources/noaa_storm_events.csv",
      "data/sources/tornado_tracks.shp"
    ]
  },
  "assets": {
    "data": {
      "href": "./tornado_density_1950_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## ⚙️ Processing Workflow

Hazard derivatives are built using **Python** (GeoPandas, Rasterio, NumPy)
and **GIS toolchains** (GDAL, GRASS, QGIS) orchestrated via `tools/hazards/` and the project Makefile.

```bash
# 1. Compute drought SPI (1950–2020)
python tools/hazards/drought_spi.py --input=precip_1950_2020.csv --output=drought_spi_1950_2020.tif

# 2. Rasterize historical flood polygons
gdal_rasterize -a value -tr 30 30 -a_nodata 0 -ot Byte \
  -te -102.1 36.9 -94.6 40.1 flood_extent_1993.shp flood_extent_1993_ks.tif

# 3. Generate tornado density kernel
python tools/hazards/tornado_density.py --input=tornado_tracks.shp --output=tornado_density_1950_2024.tif

# 4. Derive wildfire frequency from MODIS FIRMS
python tools/hazards/fire_frequency.py --input=modis_fires_2000_2023.csv --output=wildfire_frequency_2000_2023.tif

# 5. Create multi-hazard summary index
python tools/hazards/hazard_index.py --layers "drought,flood,tornado,fire" --output=hazards_summary.geojson
```

All raster outputs are standardized to **COG** and validated via **STAC Schema**.

---

## 🔁 Reproducibility & Validation

* **Integrity:** `.sha256` checksum manifests for all derivatives
* **Schema Validation:** STAC JSON checked automatically in CI
* **Makefile Targets:**

  ```bash
  make hazards           # build all hazard layers
  make validate-hazards  # run checksum + metadata validation
  ```
* **Containerization:** All processing runs in Dockerized GDAL + Python environments
* **QA/QC:** Outputs visually reviewed in QGIS/MapLibre; SPI, fire frequency, and tornado densities benchmarked to source datasets

---

## 🧾 Versioning & Changelog

| Version    | Date       | Description                                                     | Maintainer       |
| :--------- | :--------- | :-------------------------------------------------------------- | :--------------- |
| **v1.2.0** | 2025-10-11 | Added version badge, MCP compliance, and updated metadata table | KFM Docs Team    |
| **v1.1.0** | 2025-09-15 | Added wildfire and summary composites; improved workflows       | KFM Hazards Team |
| **v1.0.0** | 2025-08-01 | Initial hazard derivatives and STAC integration                 | KFM Core Devs    |

---

## 🧠 Contributing New Hazard Layers

1. Add input datasets under `data/sources/hazards/`.
2. Produce new GeoTIFF/GeoJSON in EPSG:4326.
3. Generate:

   * `.sha256` checksum
   * STAC item (`metadata/<id>.json`)
   * `DERIVATION.md` file with data lineage and methods
4. Validate:

   ```bash
   make validate-hazards
   ```
5. Submit PR with:

   * Updated metadata and changelog entry
   * Data source citation and processing details

All PRs undergo automatic validation through **CodeQL**, **STAC**, and **MCP compliance checks**.

---

## 📖 References

* **NOAA Storm Events:** [ncei.noaa.gov/stormevents](https://www.ncei.noaa.gov/stormevents/)
* **FEMA Disaster Declarations:** [fema.gov/openfema-data-page](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* **US Drought Monitor:** [droughtmonitor.unl.edu](https://droughtmonitor.unl.edu/)
* **NASA FIRMS Fire Data:** [firms.modaps.eosdis.nasa.gov](https://firms.modaps.eosdis.nasa.gov/)
* **USGS Flood Hazards:** [usgs.gov/water-resources/science/floods](https://www.usgs.gov/mission-areas/water-resources/science/floods)
* **STAC Spec 1.0:** [stacspec.org](https://stacspec.org)
* **MCP Standards:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

> *“From drought cracks to storm tracks — these layers chronicle the forces that shaped Kansas resilience.”*
> **Version v1.2.0 · MCP v2.1 · STAC Validated · Reproducible ETL Pipeline**

</div>
