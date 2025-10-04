<div align="center">

# 🌾 Kansas-Frontier-Matrix — Landcover Derivatives (`data/derivatives/landcover/`)

**Mission:** Contain all **landcover and vegetation-derived products** — NDVI, NDWI, classification maps,  
change detection rasters, and ecological indices — generated from multispectral imagery and historical datasets  
spanning Kansas’s prairies, farmlands, and urban zones.

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
- [Core Landcover Products](#core-landcover-products)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Landcover Layers](#contributing-new-landcover-layers)
- [References](#references)

---

## 🌍 Overview

This directory holds **landcover and vegetation derivative layers** derived from satellite imagery  
(Landsat, Sentinel, MODIS) and historical vegetation maps (e.g., USGS, USDA, KGS).  
Products include vegetation indices (NDVI, NDWI), multi-epoch landcover classifications, and  
land-use change composites (e.g., 1992–2021 transitions from the NLCD dataset).

These layers illustrate the **ecological evolution of Kansas** — from tallgrass prairie and  
riparian corridors to modern agricultural and urban land patterns — and enable  
comparisons of vegetation health and land conversion across decades.

All data are **open-format COG GeoTIFFs and GeoJSONs** registered in the  
[`data/stac/`](../../stac/) catalog with complete metadata, lineage, and provenance tracking.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── landcover/
        ├── ndvi_2021_ks.tif               # Normalized Difference Vegetation Index (NDVI)
        ├── ndwi_2021_ks.tif               # Normalized Difference Water Index (NDWI)
        ├── nlcd_1992_2021_change.tif      # Landcover change (NLCD 1992–2021)
        ├── vegetation_density_ks.tif      # Fractional vegetation cover (FVC)
        ├── cropland_extent_ks.geojson     # Vectorized cropland polygons
        ├── metadata/
        │   ├── ndvi_2021_ks.json
        │   ├── nlcd_1992_2021_change.json
        │   └── vegetation_density_ks.json
        ├── checksums/
        │   ├── ndvi_2021_ks.tif.sha256
        │   └── nlcd_1992_2021_change.tif.sha256
        └── README.md
````

---

## 🌾 Core Landcover Products

| Product                      | File                         | Description                                                | Source                 | Units    | Format        |
| ---------------------------- | ---------------------------- | ---------------------------------------------------------- | ---------------------- | -------- | ------------- |
| **NDVI**                     | `ndvi_2021_ks.tif`           | Normalized Difference Vegetation Index (NIR-Red)/(NIR+Red) | Landsat 8 / Sentinel-2 | -1 to 1  | GeoTIFF (COG) |
| **NDWI**                     | `ndwi_2021_ks.tif`           | Normalized Difference Water Index (Green-NIR)/(Green+NIR)  | Sentinel-2             | -1 to 1  | GeoTIFF (COG) |
| **Landcover Change**         | `nlcd_1992_2021_change.tif`  | Categorical difference map (NLCD epochs)                   | USGS NLCD              | category | GeoTIFF (COG) |
| **Vegetation Density (FVC)** | `vegetation_density_ks.tif`  | Fractional Vegetation Cover (%)                            | Landsat 8 NDVI scaled  | 0–100    | GeoTIFF (COG) |
| **Cropland Extent**          | `cropland_extent_ks.geojson` | Polygonized cropland mask (threshold NDVI>0.4)             | Derived                | ha       | GeoJSON       |

---

## 🧩 STAC Metadata

Each landcover layer is indexed as a STAC Item under `data/stac/items/landcover_*`
with lineage and semantic tags for interoperability.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "nlcd_1992_2021_change",
  "properties": {
    "title": "NLCD Landcover Change (1992–2021) – Kansas",
    "datetime": "2021-01-01T00:00:00Z",
    "description": "Multi-epoch comparison of NLCD landcover classes highlighting major agricultural and urban expansion across Kansas.",
    "processing:software": "GDAL 3.8.0 + NumPy",
    "mcp_provenance": "sha256:a18bce…",
    "license": "CC-BY 4.0",
    "derived_from": ["data/sources/nlcd_1992.tif", "data/sources/nlcd_2021.tif"]
  },
  "assets": {
    "data": {
      "href": "./nlcd_1992_2021_change.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## ⚙️ Processing Workflow

All vegetation indices and landcover composites are reproducibly generated using
Python scripts under `tools/landcover/` and orchestrated by Makefile targets.

Example NDVI workflow:

```bash
# 1. Compute NDVI from Landsat 8 bands (B5=NIR, B4=RED)
gdal_calc.py -A LC08_B5.tif -B LC08_B4.tif --outfile=ndvi_2021_ks.tif \
  --calc="(A-B)/(A+B)" --type=Float32 --NoDataValue=-9999

# 2. Convert to Cloud-Optimized GeoTIFF (COG)
rio cogeo create ndvi_2021_ks.tif ndvi_2021_ks_cog.tif --overview-level=5

# 3. Generate landcover change composite (NLCD 1992 vs 2021)
python tools/landcover/nlcd_diff.py data/sources/nlcd_1992.tif data/sources/nlcd_2021.tif \
  -o nlcd_1992_2021_change.tif

# 4. Calculate vegetation density (FVC)
gdal_calc.py -A ndvi_2021_ks.tif --outfile=vegetation_density_ks.tif --calc="(A+1)*50"
```

All derived layers are reprojected to **EPSG:4326** for global consistency.

---

## 🔁 Reproducibility & Validation

* **Checksums:** Every raster/vector file includes a `.sha256` integrity hash.
* **STAC Validation:** Automated schema checks in CI ensure valid metadata.
* **Makefile Targets:**

  * `make landcover` → regenerates all products
  * `make validate-landcover` → runs STAC & checksum tests
* **Containerized Environment:** Processing uses GDAL + rasterio + NumPy inside Docker for exact reproducibility.
* **QA Verification:** Visual validation performed via QGIS and MapLibre overlays.

---

## 🧠 Contributing New Landcover Layers

1. Add raw imagery (or reference) under `data/sources/` or `data/cogs/`.
2. Produce your derivative in an open format (GeoTIFF or GeoJSON).
3. Create a corresponding STAC item JSON and `.sha256` checksum under `metadata/`.
4. Write a brief `DERIVATION.md` summarizing methods and parameters.
5. Validate locally with:

   ```bash
   make validate-landcover
   ```
6. Submit a Pull Request including:

   * Data source citation & license,
   * Processing workflow or script reference,
   * Visualization style suggestion (colormap, legend, units).

---

## 📖 References

* **USGS National Land Cover Database (NLCD):** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **Landsat Science:** [https://landsat.gsfc.nasa.gov](https://landsat.gsfc.nasa.gov)
* **Sentinel Hub Documentation:** [https://docs.sentinel-hub.com](https://docs.sentinel-hub.com)
* **GDAL Raster Utilities:** [https://gdal.org](https://gdal.org)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **Kansas DASC GIS Hub:** [https://hub.kansasgis.org](https://hub.kansasgis.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From prairie grass to plowed field — these layers chronicle Kansas’s ecological heartbeat through time.”*

</div>
```

