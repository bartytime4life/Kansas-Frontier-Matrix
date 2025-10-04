<div align="center">

# ⚠️ Kansas-Frontier-Matrix — Hazard Derivatives (`data/derivatives/hazards/`)

**Mission:** Contain all **hazard-related geospatial derivatives** — drought, flood, wildfire, tornado,  
and severe weather composites — derived from historical records, remote sensing data, and NOAA/FEMA archives.  

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
- [Core Hazard Products](#core-hazard-products)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Hazard Layers](#contributing-new-hazard-layers)
- [References](#references)

---

## 🌪️ Overview

This directory hosts **hazard-related derivative layers** representing Kansas’s exposure and vulnerability  
to natural disasters across time — including droughts, floods, tornado outbreaks, wildfires, and severe storms.  

Derived from sources such as **NOAA Storm Events**, **FEMA Disaster Declarations**, **US Drought Monitor**,  
and **NASA MODIS Fire products**, these composites help visualize the spatial distribution and frequency  
of hazard events and support risk modeling and historical analysis.

All hazard products are standardized to **Cloud-Optimized GeoTIFFs (COG)** or **GeoJSON** for web visualization  
and are documented in the [STAC catalog](../../stac/) for discoverability and traceability.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── hazards/
        ├── drought_spi_1950_2020.tif         # Standardized Precipitation Index (SPI)
        ├── flood_extent_1993_ks.tif          # 1993 flood event extent composite
        ├── tornado_density_1950_2024.tif     # Kernel density of tornado tracks
        ├── wildfire_frequency_2000_2023.tif  # MODIS-based fire frequency map
        ├── hazards_summary.geojson           # Combined hazard risk zones
        ├── metadata/
        │   ├── drought_spi_1950_2020.json
        │   ├── flood_extent_1993_ks.json
        │   └── tornado_density_1950_2024.json
        ├── checksums/
        │   ├── drought_spi_1950_2020.tif.sha256
        │   ├── flood_extent_1993_ks.tif.sha256
        │   └── tornado_density_1950_2024.tif.sha256
        └── README.md
````

---

## 🌩️ Core Hazard Products

| Product                            | File                               | Description                                                          | Source                   | Units                  | Format        |
| ---------------------------------- | ---------------------------------- | -------------------------------------------------------------------- | ------------------------ | ---------------------- | ------------- |
| **Drought SPI (1950–2020)**        | `drought_spi_1950_2020.tif`        | 12-month standardized precipitation index (SPI) for drought severity | NOAA + PRISM             | unitless               | GeoTIFF (COG) |
| **Flood Extent (1993)**            | `flood_extent_1993_ks.tif`         | Composite of observed flood zones from the 1993 Midwest floods       | USGS + FEMA              | binary (0/1)           | GeoTIFF (COG) |
| **Tornado Density (1950–2024)**    | `tornado_density_1950_2024.tif`    | Kernel density raster of tornado tracks from SPC dataset             | NOAA SPC                 | events/km²             | GeoTIFF (COG) |
| **Wildfire Frequency (2000–2023)** | `wildfire_frequency_2000_2023.tif` | MODIS fire pixel composite showing annual burn frequency             | NASA FIRMS               | % occurrence           | GeoTIFF (COG) |
| **Hazard Summary Zones**           | `hazards_summary.geojson`          | Combined risk index integrating all hazards                          | Composite (multi-source) | normalized index (0–1) | GeoJSON       |

---

## 🧩 STAC Metadata

Each hazard layer is registered as a STAC Item under `data/stac/items/hazards_*`,
with temporal extent and provenance.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "tornado_density_1950_2024",
  "properties": {
    "title": "Tornado Density (1950–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Kernel density raster of tornado paths across Kansas using NOAA SPC data (1950–2024).",
    "processing:software": "Python + GDAL + QGIS",
    "mcp_provenance": "sha256:b52f8e…",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/sources/noaa_storm_events.csv",
      "data/sources/tornado_tracks.shp"
    ]
  },
  "assets": {
    "data": {
      "href": "./tornado_density_1950_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## ⚙️ Processing Workflow

Hazard layers are built using **Python (GeoPandas, rasterio, NumPy)** and **GIS tools (GDAL, QGIS, GRASS)**,
automated through `tools/hazards/` scripts and the `Makefile`.

Example workflow:

```bash
# 1. Generate SPI (Standardized Precipitation Index)
python tools/hazards/drought_spi.py --input=precip_1950_2020.csv --output=drought_spi_1950_2020.tif

# 2. Rasterize historical flood polygons
gdal_rasterize -a value -tr 30 30 -a_nodata 0 -ot Byte \
  -te -102.1 36.9 -94.6 40.1 flood_extent_1993.shp flood_extent_1993_ks.tif

# 3. Generate tornado density heatmap
python tools/hazards/tornado_density.py --input=tornado_tracks.shp --output=tornado_density_1950_2024.tif

# 4. Create wildfire frequency map
python tools/hazards/fire_frequency.py --input=modis_fires_2000_2023.csv --output=wildfire_frequency_2000_2023.tif

# 5. Combine into multi-hazard index (weighted average)
python tools/hazards/hazard_index.py --layers "drought,flood,tornado,fire" --output=hazards_summary.geojson
```

All raster outputs are converted to **COG** format and registered with STAC.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` hashes verify every artifact.
* **STAC Validation:** JSON metadata validated in CI for schema and completeness.
* **Makefile Targets:**

  * `make hazards` → builds all hazard derivatives
  * `make validate-hazards` → runs checksum & schema tests
* **Containerization:** Processing occurs in Docker containers with GDAL, rasterio, and Python libraries.
* **Data QA:** Outputs are visually inspected in QGIS and MapLibre; statistical checks compare SPI & event counts
  to NOAA benchmarks for consistency.

---

## 🧠 Contributing New Hazard Layers

1. Prepare input data (NOAA, FEMA, NASA, USGS) under `data/sources/`.
2. Generate new derivative in GeoTIFF or GeoJSON (EPSG:4326 projection).
3. Add corresponding STAC item JSON and `.sha256` checksum under `metadata/`.
4. Include a concise `DERIVATION.md` documenting source data, parameters, and equations.
5. Validate locally:

   ```bash
   make validate-hazards
   ```
6. Submit a Pull Request including:

   * Citation for data sources,
   * Description of method and parameterization,
   * Suggested visualization (color ramp, legend).

All PRs must pass automated CI checks for schema and checksum validation.

---

## 📖 References

* **NOAA Storm Events Database:** [https://www.ncei.noaa.gov/stormevents/](https://www.ncei.noaa.gov/stormevents/)
* **FEMA Disaster Declarations:** [https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
* **US Drought Monitor:** [https://droughtmonitor.unl.edu/](https://droughtmonitor.unl.edu/)
* **NASA FIRMS Fire Data:** [https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)
* **USGS Flood Hazards:** [https://www.usgs.gov/mission-areas/water-resources/science/floods](https://www.usgs.gov/mission-areas/water-resources/science/floods)
* **GDAL Utilities:** [https://gdal.org/](https://gdal.org/)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From drought cracks to storm tracks — these maps trace the forces that shaped Kansas resilience.”*

</div>
```

