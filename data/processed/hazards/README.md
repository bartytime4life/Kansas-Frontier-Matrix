<div align="center">

# ⚠️ Kansas Frontier Matrix — Processed Hazard Data  
`data/processed/hazards/`

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
- [Version History](#version-history)
- [References](#references)

---

## 🌪️ Overview

This directory contains **processed hazard event datasets**, cleaned and standardized from **NOAA**, **FEMA**, **NASA**,  
and **USGS** archives to form the **historical hazard record** for Kansas.

Outputs include **event-level GeoJSONs** and **gridded hazard indices**, forming the base for derivative layers —  
density rasters, risk composites, and frequency models (see `data/derivatives/hazards/`).

Primary sources:
- **NOAA Storm Events** & **SPC** (tornado/hail/wind, floods)
- **FEMA Disaster Declarations** (county-level disasters since 1953)
- **NASA FIRMS** (wildfire detections)
- **U.S. Drought Monitor** & **NOAA CPC SPI** (drought intensity)
- **USGS Water Resources** (flood measurements & extents)

All outputs are reprojected to **EPSG:4326 (WGS84)** and formatted as **GeoTIFF (COG)** or **GeoJSON**.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hazards/
        ├── tornado_tracks_1950_2024.geojson    # Cleaned NOAA SPC tornado tracks (Kansas subset)
        ├── fema_disasters_1953_2024.geojson    # FEMA disaster declarations (KS counties)
        ├── drought_spi12_1950_2024.tif         # 12-month SPI drought index (COG)
        ├── wildfire_points_2000_2023.geojson   # NASA FIRMS active fire detections
        ├── flood_events_1900_2020.geojson      # Digitized flood polygons & attributes
        ├── metadata/
        │   ├── tornado_tracks_1950_2024.json
        │   ├── drought_spi12_1950_2024.json
        │   └── fema_disasters_1953_2024.json
        ├── checksums/
        │   ├── tornado_tracks_1950_2024.geojson.sha256
        │   ├── drought_spi12_1950_2024.tif.sha256
        │   └── fema_disasters_1953_2024.geojson.sha256
        └── README.md


⸻

🌩️ Core Hazard Datasets

Product	File	Description	Source	Units	Format
Tornado Tracks (1950–2024)	tornado_tracks_1950_2024.geojson	Cleaned tornado path polylines (Kansas subset)	NOAA SPC	categorical	GeoJSON
FEMA Disasters (1953–2024)	fema_disasters_1953_2024.geojson	County-level disaster declarations and types	FEMA Open Data	categorical	GeoJSON
Drought SPI (12-Month)	drought_spi12_1950_2024.tif	12-month standardized precipitation index	NOAA CPC	index	GeoTIFF (COG)
Wildfire Points (2000–2023)	wildfire_points_2000_2023.geojson	MODIS/NASA fire detections	NASA FIRMS	count	GeoJSON
Flood Events (1900–2020)	flood_events_1900_2020.geojson	Digitized flood polygons with event metadata	USGS · KGS	binary	GeoJSON


⸻

🧩 STAC Metadata

Each processed hazard file is registered as a STAC Item under data/stac/items/hazards_*, including provenance, lineage, and citation.

Example:

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "tornado_tracks_1950_2024",
  "properties": {
    "title": "NOAA SPC Tornado Tracks (1950–2024)",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Cleaned tornado path dataset from NOAA Storm Prediction Center (Kansas subset).",
    "processing:software": "Python + GeoPandas + Shapely + GDAL",
    "mcp_provenance": "sha256:e17a9b…",
    "derived_from": ["data/raw/noaa_tornado_tracks.zip"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./tornado_tracks_1950_2024.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}


⸻

⚙️ Processing Workflow

Processing and harmonization are automated via Makefile targets and Python tools in tools/hazards/
using Python, GeoPandas, Shapely, and GDAL. Rasters are converted to COGs with overviews.

Example CLI:

# 1) Clean tornado track shapefile
python tools/hazards/clean_tornado_tracks.py \
  --input data/raw/noaa_tornado_tracks.zip \
  --output data/processed/hazards/tornado_tracks_1950_2024.geojson

# 2) Process FEMA disaster declarations (KS subset)
python tools/hazards/fema_disasters.py \
  --input data/raw/fema_disasters.csv \
  --state "Kansas" \
  --output data/processed/hazards/fema_disasters_1953_2024.geojson

# 3) Generate SPI drought raster (12-month)
python tools/hazards/drought_spi.py \
  --input data/raw/noaa_precip_1950_2024.csv \
  --window 12 \
  --output data/processed/hazards/drought_spi12_1950_2024.tif


⸻

🔁 Reproducibility & Validation
	•	Checksums: Each dataset has a .sha256 digest under checksums/ for integrity verification.
	•	STAC Validation: All metadata JSON validated against STAC 1.0 schema in CI.
	•	Makefile Targets:
	•	make hazards → process all hazard datasets
	•	make validate-hazards → validate STAC and checksum integrity
	•	Containerized Runtime: Processing runs in a pinned Docker image (Python + GDAL + GeoPandas).
	•	QA Checks: Event counts, date ranges, and spatial bounds cross-checked against source providers (NOAA/FEMA/USGS).

⸻

🧠 Contributing New Hazard Data
	1.	Add cleaned raster/vector datasets to this folder.
	2.	Create a STAC Item in metadata/ and a checksum in checksums/.
	3.	Add a DERIVATION.md (inputs, methods, software, assumptions).
	4.	Validate:

make validate-hazards


	5.	Open a PR including:
	•	Data license and citations
	•	Script references and parameterization
	•	Visualization guidance (symbology, class breaks, temporal coverage)

All PRs are automatically checked by CI for schema and integrity compliance.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README with MCP front matter, CI targets, and QA verification details.
1.0.0	2025-10-04	Initial processed hazards datasets and documentation.


⸻

📖 References
	•	NOAA Storm Events: https://www.ncei.noaa.gov/stormevents/
	•	FEMA Declarations (OpenFEMA): https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2
	•	NASA FIRMS: https://firms.modaps.eosdis.nasa.gov/
	•	U.S. Drought Monitor: https://droughtmonitor.unl.edu/
	•	USGS Flood Science: https://www.usgs.gov/mission-areas/water-resources/science/floods
	•	GDAL / GeoPandas: https://gdal.org · https://geopandas.org
	•	STAC 1.0: https://stacspec.org
	•	MCP Standards: ../../../docs/standards/

⸻


<div align="center">


“From storm paths to drought scars — these processed datasets chronicle the forces that have shaped Kansas resilience.”
📍 data/processed/hazards/

</div>
```