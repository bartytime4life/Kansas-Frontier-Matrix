<div align="center">

# 🌦️ Kansas Frontier Matrix — Climate **Derivatives**

`data/derivatives/climate/`

**Mission:** Maintain and document all **climate & atmospheric derivative datasets** — temperature, precipitation, evapotranspiration, anomalies, and climate indices — derived from historical observations, reanalyses, and gridded products to reveal how Kansas’s climate has shifted over time.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/pre-commit.yml?label=Pre--Commit)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)
[![Version](https://img.shields.io/badge/Version-v1.2.0-blueviolet)](#-versioning--changelog)

</div>

---

## 📚 Table of Contents

* [Overview](#overview)
* [Version & Metadata](#version--metadata)
* [Directory Layout](#directory-layout)
* [Core Climate Products](#core-climate-products)
* [STAC Metadata](#stac-metadata)
* [Processing Workflow](#processing-workflow)
* [Reproducibility & Validation](#reproducibility--validation)
* [Versioning & Changelog](#-versioning--changelog)
* [Contributing New Climate Layers](#contributing-new-climate-layers)
* [References](#references)

---

## 🌤️ Overview

This directory provides **climate and meteorological derivatives** for Kansas — gridded temperature, precipitation, drought indices, climate normals, anomalies, and trend layers. Datasets combine **observations, reanalyses, and satellite-driven grids** (e.g., NOAA, PRISM, Daymet) to support historical reconstructions, agricultural risk modeling, hydrology coupling, and ecological analyses within the KFM knowledge system.

All outputs use open formats (**COG GeoTIFF**, **Parquet**, **CSV**) and are discoverable via the project **STAC catalog** for provenance and reproducibility.

---

## 🧭 Version & Metadata

| Field            | Value                                        |
| :--------------- | :------------------------------------------- |
| **Version**      | `v1.2.0`                                     |
| **Last Updated** | `2025-10-11`                                 |
| **Maintainer**   | KFM Climate & Hazards Team                   |
| **Schema**       | STAC 1.0.0 · MCP v2.1                        |
| **Licenses**     | CC-BY 4.0 (Data), MIT (Code)                 |
| **Validation**   | STAC schema, checksum, CRS & topology checks |

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── climate/
        ├── temp_anomaly_1895_2024.tif        # Temperature anomaly (baseline 1991–2020)
        ├── precip_anomaly_1895_2024.tif      # Precipitation deviation (mm) from baseline
        ├── evapotranspiration_ks.tif         # Annual potential evapotranspiration
        ├── climate_normals_1991_2020.parquet # 30-year normals (aggregated)
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
```

---

## 🌡️ Core Climate Products

| Product                               | File                                | Description                                               | Source               | Units    | Format        |
| :------------------------------------ | :---------------------------------- | :-------------------------------------------------------- | :------------------- | :------- | :------------ |
| **Temperature Anomaly (1895–2024)**   | `temp_anomaly_1895_2024.tif`        | Mean annual temperature deviation from 1991–2020 baseline | NOAA NCEI + PRISM    | °C       | GeoTIFF (COG) |
| **Precipitation Anomaly (1895–2024)** | `precip_anomaly_1895_2024.tif`      | Difference from climatological mean precipitation         | NOAA NCEI + Daymet   | mm       | GeoTIFF (COG) |
| **Potential Evapotranspiration**      | `evapotranspiration_ks.tif`         | Annual PET grid (energy-balance/Thornthwaite variant)     | NASA/PRISM composite | mm·yr⁻¹  | GeoTIFF (COG) |
| **Climate Normals (1991–2020)**       | `climate_normals_1991_2020.parquet` | 30-year normals (T/P, station-aggregated)                 | NOAA NCEI            | °C, mm   | Parquet       |
| **Drought SPI (12-mo)**               | `drought_index_spi12.tif`           | Standardized Precipitation Index (12-month window)        | NOAA CPC             | unitless | GeoTIFF (COG) |

---

## 🧩 STAC Metadata

Each derivative is a **STAC Item** with full lineage, processing notes, time coverage, and licensing.

**Example**

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "temp_anomaly_1895_2024",
  "properties": {
    "title": "Temperature Anomaly (1895–2024) – Kansas",
    "description": "Mean annual temperature anomalies relative to 1991–2020 baseline; aggregated from NOAA NCEI and PRISM.",
    "datetime": "2024-01-01T00:00:00Z",
    "processing:software": "Python 3.11 · xarray · rasterio",
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
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## ⚙️ Processing Workflow

Climate derivatives are generated with reproducible **Python** pipelines under `tools/climate/` (xarray, rasterio, NumPy, Pandas) orchestrated by the **Makefile**.

```bash
# 1) Temperature anomaly (baseline 1991–2020)
python tools/climate/temp_anomaly.py \
  --input data/sources/prism_temp_monthly.nc \
  --baseline 1991-2020 \
  --output data/derivatives/climate/temp_anomaly_1895_2024.tif

# 2) Precipitation anomaly
python tools/climate/precip_anomaly.py \
  --input data/sources/daymet_precip.nc \
  --baseline 1991-2020 \
  --output data/derivatives/climate/precip_anomaly_1895_2024.tif

# 3) Drought SPI (12-month window)
python tools/climate/spi_index.py \
  --precip data/sources/noaa_precip.csv \
  --window 12 \
  --output data/derivatives/climate/drought_index_spi12.tif
```

> All rasters are reprojected to **EPSG:4326** and written as **COG** with internal overviews.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` files for every artifact (see `checksums/`).
* **STAC Validation:** CI enforces STAC schema + asset linkage + checksum parity.
* **Make Targets:**

  ```bash
  make climate            # build all climate derivatives
  make validate-climate   # run checksum + STAC validation
  ```
* **Containers:** Dockerized GDAL/xarray environments with pinned versions.
* **Cross-checks:** Compare outputs to NOAA Normals & Daymet aggregates; sanity checks on units, CRS, and bounds.

---

## 🧾 Versioning & Changelog

|   Version  |    Date    | Changes                                                                                  |
| :--------: | :--------: | :--------------------------------------------------------------------------------------- |
| **v1.2.0** | 2025-10-11 | Added version panel, clarified PET notes, expanded Make targets, tightened STAC example. |
| **v1.1.0** | 2025-09-28 | Added SPI layer & checksums; refined anomaly baseline handling.                          |
| **v1.0.0** | 2025-09-10 | Initial climate derivatives & STAC registration.                                         |

> Bump the version with any structural change (new sections, datasets, schema fields) and append a line here.

---

## 🧠 Contributing New Climate Layers

1. Place raw inputs in `data/sources/climate/`.
2. Generate derivatives with open tools (xarray, GDAL, rasterio).
3. Add:

   * STAC item JSON under `metadata/`
   * `.sha256` checksum under `checksums/`
   * `DERIVATION.md` (method, baseline, parameters)
4. Validate locally:

   ```bash
   make validate-climate
   ```
5. Open a PR with citations, script/notebook references, and suggested visualization (color ramp, legend, units).

---

## 📖 References

* **NOAA NCEI:** [https://www.ncei.noaa.gov/](https://www.ncei.noaa.gov/)
* **PRISM Climate Group:** [https://prism.oregonstate.edu/](https://prism.oregonstate.edu/)
* **NASA Daymet:** [https://daac.ornl.gov/DAYMET/](https://daac.ornl.gov/DAYMET/)
* **CPC Drought Monitoring:** [https://www.cpc.ncep.noaa.gov/](https://www.cpc.ncep.noaa.gov/)
* **xarray Docs:** [https://docs.xarray.dev/](https://docs.xarray.dev/)
* **STAC 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **MCP Standards:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

> *“From Dust Bowl droughts to warming plains — these layers track Kansas’s climate heartbeat through time.”*
> **Version v1.2.0 · MCP v2.1 · STAC Validated · Reproducible ETL**

</div>
