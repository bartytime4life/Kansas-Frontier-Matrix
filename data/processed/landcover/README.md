<div align="center">

# 🌾 Kansas-Frontier-Matrix — Processed Landcover Data (`data/processed/landcover/`)

**Mission:** Store and document all **cleaned and standardized landcover datasets** — pre-processed imagery,  
classification rasters, and vegetation indices — used for ecological, agricultural, and land-use analysis  
across Kansas.

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
- [Core Landcover Datasets](#core-landcover-datasets)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Landcover Data](#contributing-new-landcover-data)
- [References](#references)

---

## 🌍 Overview

This subdirectory contains **processed landcover datasets** — cleaned, normalized, and aligned  
to a consistent spatial grid and projection for Kansas. These files represent intermediate  
outputs derived from satellite imagery (Landsat, Sentinel-2, MODIS) or historical map products  
(NLCD, USDA, KGS).  

These layers provide the foundation for derivative products like NDVI, NDWI, and change detection  
maps found under `data/derivatives/landcover/`.

All outputs are formatted as **Cloud-Optimized GeoTIFFs (COGs)** or **GeoJSONs**, reprojected to  
**EPSG:4326**, and registered in the [STAC catalog](../../stac/) with full provenance and schema validation.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── landcover/
        ├── nlcd_2021_ks.tif                # NLCD classified landcover raster
        ├── landsat_2021_ks.tif             # Landsat 8 imagery composite (bands stacked)
        ├── sentinel_2021_ks.tif            # Sentinel-2 imagery composite (resampled to 30 m)
        ├── vegetation_mask_ks.tif          # Binary vegetation mask (NDVI > 0.3)
        ├── water_mask_ks.tif               # Binary water mask from NIR threshold
        ├── metadata/
        │   ├── nlcd_2021_ks.json
        │   ├── vegetation_mask_ks.json
        │   └── water_mask_ks.json
        ├── checksums/
        │   ├── nlcd_2021_ks.tif.sha256
        │   ├── vegetation_mask_ks.tif.sha256
        │   └── water_mask_ks.tif.sha256
        └── README.md
````

---

## 🌾 Core Landcover Datasets

| Product                | File                     | Description                                                             | Source           | Units       | Format        |
| ---------------------- | ------------------------ | ----------------------------------------------------------------------- | ---------------- | ----------- | ------------- |
| **NLCD (2021)**        | `nlcd_2021_ks.tif`       | National Land Cover Database raster for Kansas                          | USGS MRLC        | categorical | GeoTIFF (COG) |
| **Landsat Composite**  | `landsat_2021_ks.tif`    | Landsat 8 composite (B4, B5, B6, B7 stacked, atmospherically corrected) | USGS Landsat     | reflectance | GeoTIFF (COG) |
| **Sentinel Composite** | `sentinel_2021_ks.tif`   | Sentinel-2 multispectral composite (10–30 m resampled)                  | ESA Sentinel Hub | reflectance | GeoTIFF (COG) |
| **Vegetation Mask**    | `vegetation_mask_ks.tif` | Binary vegetation map derived from NDVI threshold (>0.3)                | Derived          | binary      | GeoTIFF (COG) |
| **Water Mask**         | `water_mask_ks.tif`      | Binary water surface mask from NIR thresholding                         | Derived          | binary      | GeoTIFF (COG) |

---

## 🧩 STAC Metadata

All processed landcover layers are indexed in the Frontier Matrix **STAC catalog** (`data/stac/items/landcover_*`)
with lineage, temporal coverage, and license info.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "nlcd_2021_ks",
  "properties": {
    "title": "NLCD 2021 Landcover – Kansas",
    "datetime": "2021-01-01T00:00:00Z",
    "description": "National Land Cover Database 2021 for Kansas (30 m).",
    "processing:software": "GDAL 3.8.0",
    "mcp_provenance": "sha256:0ae19e…",
    "derived_from": ["data/raw/nlcd_2021_ks.tif"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./nlcd_2021_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## ⚙️ Processing Workflow

All data are generated and standardized via the **Makefile** and `tools/landcover/` scripts using **GDAL**, **rasterio**,
and **NumPy**. Processing ensures uniform resolution, projection, and radiometric scaling across sensors.

Example workflow:

```bash
# 1. Reproject and resample NLCD
gdalwarp nlcd_2021.tif nlcd_2021_ks.tif -t_srs EPSG:4326 -tr 0.00027778 0.00027778 -r near

# 2. Build Landsat composite (stacked reflectance bands)
gdal_merge.py -separate -o landsat_2021_ks.tif LC08_B4.tif LC08_B5.tif LC08_B6.tif LC08_B7.tif

# 3. Create Sentinel composite and resample
gdalwarp sentinel_2021_bands.tif sentinel_2021_ks.tif -t_srs EPSG:4326 -tr 30 30 -r cubic

# 4. Generate vegetation and water masks
gdal_calc.py -A ndvi_2021_ks.tif --outfile=vegetation_mask_ks.tif --calc="(A>0.3)"
gdal_calc.py -A sentinel_nir.tif --outfile=water_mask_ks.tif --calc="(A<0.05)"
```

All outputs are converted to **COG** format using:

```bash
rio cogeo create input.tif output_cog.tif --overview-level=5
```

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` integrity hashes accompany each file.
* **STAC Validation:** Metadata checked via CI (`.github/workflows/stac-validate.yml`).
* **Makefile Targets:**

  * `make landcover` → process all landcover data
  * `make validate-landcover` → run metadata and checksum validation
* **Containerization:** All scripts executed in a GDAL + rasterio Docker environment.
* **QA Checks:** Visual validation against NLCD legends and RGB composites in QGIS or MapLibre.

---

## 🧠 Contributing New Landcover Data

1. Place the cleaned raster or vector file in this directory.
2. Generate a `.sha256` checksum file:

   ```bash
   sha256sum new_file.tif > checksums/new_file.tif.sha256
   ```
3. Create a STAC metadata JSON entry under `metadata/`.
4. Include a `DERIVATION.md` explaining data sources, parameters, and projection.
5. Validate:

   ```bash
   make validate-landcover
   ```
6. Submit a PR with:

   * Data license and source citations
   * Processing method details
   * Visualization suggestions (color ramps, legend classes)

---

## 📖 References

* **USGS National Land Cover Database (NLCD):** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **Landsat Science:** [https://landsat.gsfc.nasa.gov](https://landsat.gsfc.nasa.gov)
* **Sentinel-2 Data Hub:** [https://scihub.copernicus.eu/](https://scihub.copernicus.eu/)
* **GDAL Utilities:** [https://gdal.org/](https://gdal.org/)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From prairie to plow and back to prairie — these processed maps reveal Kansas’s ever-changing green frontier.”*

</div>
```

