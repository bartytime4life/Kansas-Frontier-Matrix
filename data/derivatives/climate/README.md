<div align="center">

# 🌦️ Kansas-Frontier-Matrix — Climate Derivatives (`data/derivatives/climate/`)

**Mission:** Maintain and document all **climate and atmospheric derivative datasets** — temperature, precipitation,  
evapotranspiration, anomalies, and climate indices — derived from historical observations, reanalyses, and gridded data  
to reveal how Kansas’s climate has shifted across time.

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
- [Core Climate Products](#core-climate-products)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Climate Layers](#contributing-new-climate-layers)
- [References](#references)

---

## 🌤️ Overview

This subdirectory contains **climate and meteorological derivative products** for Kansas —  
gridded temperature, precipitation, drought indices, and long-term climate normals.  
They represent both observed and reanalyzed data, capturing historical trends and variability from  
the 19th century to the present.

Derived datasets include **anomaly rasters**, **trend analyses**, and **multi-year summaries**  
calculated from sources such as NOAA, PRISM, NASA Daymet, and NCEI.  
They support historical climate reconstructions, agricultural risk modeling, and ecological studies  
within the Kansas Frontier Matrix knowledge system.

All files follow open standards (**COG GeoTIFF**, **Parquet**, or **CSV**)  
and are referenced in the project [STAC catalog](../../stac/) for full provenance and reproducibility.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── climate/
        ├── temp_anomaly_1895_2024.tif        # Temperature anomaly map (baseline 1991–2020)
        ├── precip_anomaly_1895_2024.tif      # Precipitation deviation (mm) from baseline
        ├── evapotranspiration_ks.tif         # Annual potential evapotranspiration
        ├── climate_normals_1991_2020.parquet # Station-based climate normals (aggregated)
        ├── drought_index_spi12.tif           # 12-month Standardized Precipitation Index
        ├── metadata/
        │   ├── temp_anomaly_1895_2024.json
        │   ├── precip_anomaly_1895_2024.json
        │   └── climate_normals_1991_2020.json
        ├── checksums/
        │   ├── temp_anomaly_1895_2024.tif.sha256
        │   ├── precip_anomaly_1895_2024.tif.sha256
        │   └── evapotranspiration_ks.tif.sha256
        └── README.md
````

---

## 🌡️ Core Climate Products

| Product                               | File                                | Description                                                | Source             | Units    | Format        |
| ------------------------------------- | ----------------------------------- | ---------------------------------------------------------- | ------------------ | -------- | ------------- |
| **Temperature Anomaly (1895–2024)**   | `temp_anomaly_1895_2024.tif`        | Mean annual temperature deviation from 1991–2020 baseline  | NOAA NCEI + PRISM  | °C       | GeoTIFF (COG) |
| **Precipitation Anomaly (1895–2024)** | `precip_anomaly_1895_2024.tif`      | Precipitation difference from climatological mean          | NOAA NCEI + Daymet | mm       | GeoTIFF (COG) |
| **Evapotranspiration**                | `evapotranspiration_ks.tif`         | Annual potential evapotranspiration grid                   | NASA SSE + PRISM   | mm/year  | GeoTIFF (COG) |
| **Climate Normals (1991–2020)**       | `climate_normals_1991_2020.parquet` | 30-year average temperature and precipitation              | NOAA NCEI          | °C, mm   | Parquet       |
| **Drought SPI (12-Month)**            | `drought_index_spi12.tif`           | Standardized Precipitation Index for 12-month accumulation | NOAA, CPC          | unitless | GeoTIFF (COG) |

---

## 🧩 STAC Metadata

Each climate derivative is registered as a **STAC item** with detailed metadata including
source, processing method, time coverage, and lineage.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "temp_anomaly_1895_2024",
  "properties": {
    "title": "Temperature Anomaly (1895–2024) – Kansas",
    "datetime": "2024-01-01T00:00:00Z",
    "description": "Raster of mean annual temperature anomalies relative to 1991–2020 climate normal. Data aggregated from NOAA NCEI and PRISM.",
    "processing:software": "Python + xarray + rasterio",
    "mcp_provenance": "sha256:ce04a1…",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/sources/noaa_ghcn.csv",
      "data/sources/prism_temperature.nc"
    ]
  },
  "assets": {
    "data": {
      "href": "./temp_anomaly_1895_2024.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## ⚙️ Processing Workflow

Climate derivatives are generated using reproducible **Python workflows** under `tools/climate/`,
leveraging **xarray**, **rasterio**, **NumPy**, and **Pandas** for temporal aggregation and regridding.
All tasks are orchestrated by the `Makefile`.

Example:

```bash
# 1. Calculate temperature anomaly
python tools/climate/temp_anomaly.py \
  --input data/sources/prism_temp_monthly.nc \
  --baseline 1991-2020 \
  --output data/derivatives/climate/temp_anomaly_1895_2024.tif

# 2. Compute precipitation anomaly
python tools/climate/precip_anomaly.py \
  --input data/sources/daymet_precip.nc \
  --baseline 1991-2020 \
  --output data/derivatives/climate/precip_anomaly_1895_2024.tif

# 3. Generate drought index (SPI)
python tools/climate/spi_index.py \
  --precip data/sources/noaa_precip.csv \
  --window 12 \
  --output data/derivatives/climate/drought_index_spi12.tif
```

All rasters are reprojected to **EPSG:4326** and converted to **Cloud-Optimized GeoTIFFs (COG)**.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` integrity files accompany each artifact.
* **STAC Validation:** Schema compliance automatically tested in CI/CD.
* **Makefile Targets:**

  * `make climate` → builds all derivatives
  * `make validate-climate` → validates checksums & STAC metadata
* **Containerized Processing:** Built inside Docker with pinned versions of Python, GDAL, and xarray.
* **Cross-Verification:** Outputs validated against NOAA Climate Normals and Daymet aggregates.

---

## 🧠 Contributing New Climate Layers

1. Place source data under `data/sources/climate/`.
2. Generate derivative output using open tools (xarray, GDAL, rasterio).
3. Add STAC metadata JSON and `.sha256` checksum under `metadata/`.
4. Include a short `DERIVATION.md` explaining the method, baseline, and parameters.
5. Validate locally:

   ```bash
   make validate-climate
   ```
6. Submit a Pull Request containing:

   * Data source citations and license
   * Processing script or notebook reference
   * Visualization guidance (color ramp, unit scale, legend).

---

## 📖 References

* **NOAA NCEI Climate Data:** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **PRISM Climate Group:** [https://prism.oregonstate.edu/](https://prism.oregonstate.edu/)
* **NASA Daymet:** [https://daac.ornl.gov/DAYMET/](https://daac.ornl.gov/DAYMET/)
* **CPC Drought Monitoring:** [https://www.cpc.ncep.noaa.gov/](https://www.cpc.ncep.noaa.gov/)
* **xarray Documentation:** [https://docs.xarray.dev/](https://docs.xarray.dev/)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From Dust Bowl droughts to warming plains — these layers trace Kansas’s climate heartbeat through time.”*

</div>
```

