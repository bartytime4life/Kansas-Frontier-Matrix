<div align="center">

# ⚠️ Kansas-Frontier-Matrix — Processed Hazard Data (`data/processed/hazards/`)

**Mission:** Store and document all **processed hazard datasets** — cleaned, merged, and standardized records  
of droughts, floods, wildfires, tornadoes, and severe weather — used for temporal analysis and risk modeling  
in the Kansas Frontier Matrix system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Core Hazard Datasets](#core-hazard-datasets)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Hazard Data](#contributing-new-hazard-data)
- [References](#references)

---

## 🌪️ Overview

This subdirectory contains **processed hazard event datasets**, cleaned and standardized  
from NOAA, FEMA, and NASA archives to form Kansas’s historical hazard record.  

These datasets represent **event-level summaries** and gridded hazard indices, forming the base  
for derivative layers such as density rasters, risk composites, and frequency models  
in `data/derivatives/hazards/`.

Primary sources include:
- **NOAA Storm Events Database** (tornado, hail, flood events)
- **FEMA Disaster Declarations** (county-level disasters since 1953)
- **NASA FIRMS Fire Archive** (wildfire detections)
- **US Drought Monitor & CPC SPI** (drought intensity)
- **USGS Water Resources** (flood measurements)

All outputs are formatted as **GeoTIFF (COG)** or **GeoJSON** and reprojected to **EPSG:4326 (WGS84)**.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hazards/
        ├── tornado_tracks_1950_2024.geojson    # Cleaned NOAA SPC tornado tracks
        ├── fema_disasters_1953_2024.geojson    # FEMA disaster declarations (Kansas subset)
        ├── drought_spi12_1950_2024.tif         # 12-month SPI drought index
        ├── wildfire_points_2000_2023.geojson   # MODIS active fire detections
        ├── flood_events_1900_2020.geojson      # Historical flood extents / events
        ├── metadata/
        │   ├── tornado_tracks_1950_2024.json
        │   ├── drought_spi12_1950_2024.json
        │   └── fema_disasters_1953_2024.json
        ├── checksums/
        │   ├── tornado_tracks_1950_2024.geojson.sha256
        │   ├── drought_spi12_1950_2024.tif.sha256
        │   └── fema_disasters_1953_2024.geojson.sha256
        └── README.md
````

---

## 🌩️ Core Hazard Datasets

| Product                         | File                                | Description                                 | Source         | Units       | Format        |
| ------------------------------- | ----------------------------------- | ------------------------------------------- | -------------- | ----------- | ------------- |
| **Tornado Tracks (1950–2024)**  | `tornado_tracks_1950_2024.geojson`  | Cleaned NOAA SPC tornado path dataset       | NOAA SPC       | categorical | GeoJSON       |
| **FEMA Disasters (1953–2024)**  | `fema_disasters_1953_2024.geojson`  | County-level disaster declarations          | FEMA Open Data | categorical | GeoJSON       |
| **Drought SPI (1950–2024)**     | `drought_spi12_1950_2024.tif`       | 12-month standardized precipitation index   | NOAA CPC       | index       | GeoTIFF (COG) |
| **Wildfire Points (2000–2023)** | `wildfire_points_2000_2023.geojson` | MODIS/NASA fire detection points            | NASA FIRMS     | count       | GeoJSON       |
| **Flood Events (1900–2020)**    | `flood_events_1900_2020.geojson`    | Digitized flood polygons and event metadata | USGS + KGS     | binary      | GeoJSON       |

---

## 🧩 STAC Metadata

Each processed hazard file is indexed as a **STAC Item** under `data/stac/items/hazards_*`,
containing its provenance, lineage, and source citation.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "tornado_tracks_1950_2024",
  "properties": {
    "title": "NOAA SPC Tornado Tracks (1950–2024)",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Cleaned tornado path dataset from NOAA Storm Prediction Center (Kansas subset).",
    "processing:software": "Python + GeoPandas + Shapely",
    "mcp_provenance": "sha256:e17a9b…",
    "derived_from": ["data/raw/noaa_tornado_tracks.zip"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./tornado_tracks_1950_2024.geojson",
      "type": "application/geo+json"
    }
  }
}
```

---

## ⚙️ Processing Workflow

All hazard datasets are processed and harmonized via `tools/hazards/` scripts using **Python**, **GDAL**, and **GeoPandas**,
then validated through `Makefile` targets.

Example CLI workflow:

```bash
# 1. Clean tornado track shapefile
python tools/hazards/clean_tornado_tracks.py \
  --input data/raw/noaa_tornado_tracks.zip \
  --output data/processed/hazards/tornado_tracks_1950_2024.geojson

# 2. Process FEMA disaster declarations
python tools/hazards/fema_disasters.py \
  --input data/raw/fema_disasters.csv \
  --state "Kansas" \
  --output data/processed/hazards/fema_disasters_1953_2024.geojson

# 3. Generate SPI drought raster
python tools/hazards/drought_spi.py \
  --input data/raw/noaa_precip_1950_2024.csv \
  --window 12 \
  --output data/processed/hazards/drought_spi12_1950_2024.tif
```

All GeoJSONs are simplified for web use, and rasters are converted to **COGs** with overviews.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` hashes accompany every output file.
* **STAC Validation:** All metadata JSON files are schema-validated in CI.
* **Makefile Targets:**

  * `make hazards` → processes all hazard datasets
  * `make validate-hazards` → validates checksums and metadata
* **Containerized Processing:** All workflows execute in a Docker environment with Python + GDAL.
* **QA Verification:** Cross-validation of event counts and geospatial extents against source datasets (NOAA, FEMA).

---

## 🧠 Contributing New Hazard Data

1. Add cleaned raster/vector files here.
2. Include `.sha256` checksums and STAC metadata JSON under `metadata/`.
3. Document the derivation process in `DERIVATION.md` (sources, methods, and software).
4. Validate with:

   ```bash
   make validate-hazards
   ```
5. Submit a Pull Request including:

   * Data citations and licenses
   * Methodology summary
   * Suggested visualization styling (color ramp, classification breaks).

All PRs are automatically validated by GitHub Actions for schema and integrity compliance.

---

## 📖 References

* **NOAA Storm Events Database:** [https://www.ncei.noaa.gov/stormevents/](https://www.ncei.noaa.gov/stormevents/)
* **FEMA Open Data Portal:** [https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* **NASA FIRMS Fire Data:** [https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)
* **US Drought Monitor:** [https://droughtmonitor.unl.edu/](https://droughtmonitor.unl.edu/)
* **USGS Flood Data:** [https://www.usgs.gov/mission-areas/water-resources/science/floods](https://www.usgs.gov/mission-areas/water-resources/science/floods)
* **GDAL & GeoPandas:** [https://gdal.org](https://gdal.org) / [https://geopandas.org](https://geopandas.org)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From storm paths to drought scars — these processed datasets chronicle the forces that have shaped Kansas resilience.”*

</div>
```

