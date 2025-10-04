<div align="center">

# 🌦️ Kansas-Frontier-Matrix — Processed Climate Data (`data/processed/climate/`)

**Mission:** Contain all **cleaned and standardized climate datasets** — temperature, precipitation, drought indices,  
and atmospheric summaries — prepared for analysis, visualization, and derivative generation across Kansas’s history.  

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
- [Core Climate Datasets](#core-climate-datasets)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Climate Data](#contributing-new-climate-data)
- [References](#references)

---

## 🌤️ Overview

This subdirectory contains **processed, analysis-ready climate datasets** derived from raw historical  
and contemporary climate observations. These include daily, monthly, and annual summaries of temperature,  
precipitation, and drought indicators used for further analysis or derivative generation in  
`data/derivatives/climate/`.

Sources include **NOAA NCEI**, **NASA Daymet**, **PRISM**, and the **U.S. Drought Monitor**, covering  
records from the late 1800s through the present.  

All processed datasets are standardized to **EPSG:4326 (WGS84)** for interoperability and formatted  
as **Cloud-Optimized GeoTIFFs (COG)**, **CSV**, or **Parquet** for numerical summaries.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── climate/
        ├── temp_mean_annual_1895_2024.tif        # Gridded mean annual temperature
        ├── precip_total_annual_1895_2024.tif     # Annual total precipitation (mm)
        ├── drought_spi12_1895_2024.tif           # 12-month SPI drought index
        ├── climate_normals_1991_2020.parquet     # Station-based 30-year climate normals
        ├── station_climate_summary.csv           # Aggregated station-level data
        ├── metadata/
        │   ├── temp_mean_annual_1895_2024.json
        │   ├── precip_total_annual_1895_2024.json
        │   └── drought_spi12_1895_2024.json
        ├── checksums/
        │   ├── temp_mean_annual_1895_2024.tif.sha256
        │   ├── precip_total_annual_1895_2024.tif.sha256
        │   └── drought_spi12_1895_2024.tif.sha256
        └── README.md
````

Each file has a corresponding metadata record under `metadata/` and a checksum file under `checksums/`.

---

## 🌡️ Core Climate Datasets

| Product                             | File                                | Description                                                   | Source             | Units  | Format        |
| ----------------------------------- | ----------------------------------- | ------------------------------------------------------------- | ------------------ | ------ | ------------- |
| **Mean Temperature (1895–2024)**    | `temp_mean_annual_1895_2024.tif`    | Gridded mean annual temperature across Kansas                 | NOAA NCEI / PRISM  | °C     | GeoTIFF (COG) |
| **Total Precipitation (1895–2024)** | `precip_total_annual_1895_2024.tif` | Annual precipitation sums (mm) interpolated from station data | NOAA NCEI / Daymet | mm     | GeoTIFF (COG) |
| **Drought SPI (12-Month)**          | `drought_spi12_1895_2024.tif`       | Standardized Precipitation Index for 12-month accumulation    | NOAA CPC           | index  | GeoTIFF (COG) |
| **Climate Normals (1991–2020)**     | `climate_normals_1991_2020.parquet` | 30-year temperature and precipitation normals per station     | NOAA NCEI          | °C, mm | Parquet       |
| **Station Climate Summary**         | `station_climate_summary.csv`       | Aggregated mean and extremes by county/station                | Derived            | °C, mm | CSV           |

---

## 🧩 STAC Metadata

Each processed file is indexed as a **STAC Item** under `data/stac/items/climate_*`
with complete metadata and lineage tracking.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "temp_mean_annual_1895_2024",
  "properties": {
    "title": "Mean Annual Temperature (1895–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Gridded average annual temperature anomaly relative to 1991–2020 baseline, aggregated from NOAA NCEI and PRISM datasets.",
    "processing:software": "Python + xarray + rasterio",
    "mcp_provenance": "sha256:a83c1b…",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/raw/noaa_temp_station.csv",
      "data/raw/prism_temp_monthly.nc"
    ]
  },
  "assets": {
    "data": {
      "href": "./temp_mean_annual_1895_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## ⚙️ Processing Workflow

Processing is automated via `Makefile` targets and Python scripts under `tools/climate/`.
Workflows leverage **xarray**, **rasterio**, and **NumPy** to aggregate, interpolate, and format data.

Example CLI:

```bash
# 1. Aggregate station temperature data to yearly mean
python tools/climate/temp_aggregate.py \
  --input data/raw/noaa_temp_station.csv \
  --output data/processed/climate/temp_mean_annual_1895_2024.tif

# 2. Generate precipitation total grid
python tools/climate/precip_total.py \
  --input data/raw/prism_precip_monthly.nc \
  --output data/processed/climate/precip_total_annual_1895_2024.tif

# 3. Compute drought SPI index (12-month)
python tools/climate/spi_index.py \
  --input data/raw/noaa_precip.csv \
  --output data/processed/climate/drought_spi12_1895_2024.tif
```

All outputs are reprojected to **EPSG:4326**, compressed (LZW), and converted to **COG**
for efficient cloud-based visualization and analysis.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` files verify dataset integrity.
* **STAC Validation:** JSON metadata tested against STAC schema in CI.
* **Makefile Targets:**

  * `make climate` → builds all processed climate layers
  * `make validate-climate` → validates STAC and checksum integrity
* **Containerized Tools:** Processing runs inside a Docker container (Python + GDAL + xarray).
* **Cross-Validation:** Temperature and precipitation grids are validated against NCEI and Daymet baselines.

---

## 🧠 Contributing New Climate Data

1. Place your cleaned raster or tabular output here.
2. Add a `.sha256` checksum file and a STAC metadata JSON under `metadata/`.
3. Include a short `DERIVATION.md` describing:

   * input datasets and periods,
   * software/tools used,
   * baseline reference period (if applicable).
4. Validate with:

   ```bash
   make validate-climate
   ```
5. Submit a Pull Request including:

   * data license and source,
   * processing script reference,
   * visualization guidance (color ramp, units, temporal coverage).

---

## 📖 References

* **NOAA NCEI Climate Data:** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **PRISM Climate Group:** [https://prism.oregonstate.edu/](https://prism.oregonstate.edu/)
* **NASA Daymet:** [https://daac.ornl.gov/DAYMET/](https://daac.ornl.gov/DAYMET/)
* **CPC Drought Indices:** [https://www.cpc.ncep.noaa.gov/](https://www.cpc.ncep.noaa.gov/)
* **xarray Documentation:** [https://docs.xarray.dev/](https://docs.xarray.dev/)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From Dust Bowl heat to modern extremes — these grids trace the climate pulse of the Kansas plains.”*

</div>
```

