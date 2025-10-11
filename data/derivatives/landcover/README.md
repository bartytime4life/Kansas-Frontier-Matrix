<div align="center">

# 🌾 Kansas Frontier Matrix — Landcover Derivatives  
`data/derivatives/landcover/`

**Mission:** Host and document all **landcover and vegetation-derived products** — NDVI, NDWI, classification maps,  
change detection rasters, and ecological indices — generated from multispectral imagery and historical datasets  
spanning Kansas’s prairies, farmlands, and urban zones.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📘 Table of Contents
- [Overview](#-overview)
- [Directory Layout](#-directory-layout)
- [Core Landcover Products](#-core-landcover-products)
- [STAC Metadata](#-stac-metadata)
- [Processing Workflow](#-processing-workflow)
- [Reproducibility & Validation](#-reproducibility--validation)
- [Contribution Guidelines](#-contribution-guidelines)
- [MCP Compliance](#-mcp-compliance)
- [References](#-references)
- [License & Provenance](#-license--provenance)

---

## 🌍 Overview

This directory hosts **landcover and vegetation derivative layers** derived from multi-sensor imagery  
(Landsat, Sentinel, MODIS) and historical vegetation maps (USGS, USDA, KGS).  
Products include vegetation indices (NDVI, NDWI), multi-epoch classifications, and  
land-use change composites (e.g., **1992–2021 NLCD** transitions).

These data portray the **ecological evolution of Kansas** — from native tallgrass prairie  
and riparian corridors to modern agricultural and urban landscapes — and enable  
quantitative analysis of vegetation health and conversion trends.

All files are distributed as **open-format COG GeoTIFFs or GeoJSONs**,  
registered in the [`data/stac/`](../../stac/) catalog with full lineage and provenance tracking.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── landcover/
        ├── ndvi_2021_ks.tif               # NDVI raster
        ├── ndwi_2021_ks.tif               # NDWI raster
        ├── nlcd_1992_2021_change.tif      # Landcover change composite
        ├── vegetation_density_ks.tif      # Fractional Vegetation Cover (FVC)
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
| :--------------------------- | :--------------------------- | :--------------------------------------------------------- | :--------------------- | :------- | :------------ |
| **NDVI**                     | `ndvi_2021_ks.tif`           | Normalized Difference Vegetation Index (NIR-Red)/(NIR+Red) | Landsat 8 / Sentinel-2 | -1 to 1  | GeoTIFF (COG) |
| **NDWI**                     | `ndwi_2021_ks.tif`           | Normalized Difference Water Index (Green-NIR)/(Green+NIR)  | Sentinel-2             | -1 to 1  | GeoTIFF (COG) |
| **Landcover Change**         | `nlcd_1992_2021_change.tif`  | Categorical difference map (NLCD epochs)                   | USGS NLCD              | category | GeoTIFF (COG) |
| **Vegetation Density (FVC)** | `vegetation_density_ks.tif`  | Fractional Vegetation Cover (%)                            | Landsat 8 NDVI scaled  | 0–100    | GeoTIFF (COG) |
| **Cropland Extent**          | `cropland_extent_ks.geojson` | Polygonized cropland mask (NDVI > 0.4)                     | Derived                | ha       | GeoJSON       |

---

## 🧩 STAC Metadata

Each layer is indexed as a **STAC Item** under `data/stac/items/landcover_*`,
with lineage, schema compliance, and MCP provenance tracking.

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "nlcd_1992_2021_change",
  "properties": {
    "title": "NLCD Landcover Change (1992–2021) – Kansas",
    "datetime": "2021-01-01T00:00:00Z",
    "description": "Comparison of NLCD landcover classes showing agricultural and urban expansion.",
    "processing:software": "GDAL 3.8 + NumPy",
    "mcp_provenance": "sha256:a18bce…",
    "license": "CC-BY 4.0",
    "derived_from": [
      "data/sources/nlcd_1992.tif",
      "data/sources/nlcd_2021.tif"
    ]
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

Vegetation indices and composites are reproducibly generated via
Python scripts in `tools/landcover/` orchestrated by **Makefile targets**.

Example NDVI workflow:

```bash
# 1. Compute NDVI
gdal_calc.py -A LC08_B5.tif -B LC08_B4.tif --outfile=ndvi_2021_ks.tif \
  --calc="(A-B)/(A+B)" --type=Float32 --NoDataValue=-9999

# 2. Convert to Cloud-Optimized GeoTIFF (COG)
rio cogeo create ndvi_2021_ks.tif ndvi_2021_ks_cog.tif --overview-level=5

# 3. Generate NLCD change composite
python tools/landcover/nlcd_diff.py data/sources/nlcd_1992.tif data/sources/nlcd_2021.tif \
  -o nlcd_1992_2021_change.tif

# 4. Calculate vegetation density (FVC)
gdal_calc.py -A ndvi_2021_ks.tif --outfile=vegetation_density_ks.tif --calc="(A+1)*50"
```

All layers are re-projected to **EPSG:4326** for global consistency.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` files verify dataset integrity.
* **STAC Validation:** CI enforces schema & extension compliance.
* **Makefile Targets:**

  * `make landcover` → regenerate all derivatives
  * `make validate-landcover` → run checksum + STAC tests
* **Containerization:** Dockerized GDAL + rasterio + NumPy ensures consistent environments.
* **QA Verification:** Visual QA via QGIS + MapLibre overlays.

---

## 🧠 Contribution Guidelines

1. Add source data under `data/sources/` or `data/cogs/`.
2. Produce new derivative (GeoTIFF/GeoJSON).
3. Add STAC item JSON + `.sha256` in `metadata/`.
4. Document workflow in `DERIVATION.md`.
5. Validate locally:

   ```bash
   make validate-landcover
   ```
6. Submit PR including:

   * Data source citation + license
   * Processing workflow or script reference
   * Visualization style suggestion (colormap, legend, units)

---

## ✅ MCP Compliance

| MCP Principle       | Implemented | Evidence                              |
| :------------------ | :---------: | :------------------------------------ |
| Documentation-First |      ✅      | README + front-matter + DERIVATION.md |
| Provenance Tracking |      ✅      | STAC + checksums + metadata           |
| Reproducibility     |      ✅      | Docker + Makefile + CI pipelines      |
| Validation          |      ✅      | STAC + checksum CI tests              |
| Transparency        |      ✅      | Public repository + open formats      |

---

## 📖 References

* **USGS NLCD:** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **Landsat Science:** [https://landsat.gsfc.nasa.gov](https://landsat.gsfc.nasa.gov)
* **Sentinel Hub:** [https://docs.sentinel-hub.com](https://docs.sentinel-hub.com)
* **GDAL Utilities:** [https://gdal.org](https://gdal.org)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **Kansas DASC GIS Hub:** [https://hub.kansasgis.org](https://hub.kansasgis.org)
* **MCP Docs:** [`docs/standards/`](../../../docs/standards/)

---

## 🪶 License & Provenance

**License:** [CC-BY 4.0](../../../LICENSE) (Data) | [MIT](../../../LICENSE) (Code)
**Provenance:** Authored under the **Master Coder Protocol (MCP)** — documentation-first, reproducible, and validated.
**Maintainers:** Kansas Frontier Matrix Landcover & Ecology Integration Team
**Last Updated:** 2025-10-11

---

<div align="center">

*“From prairie grass to plowed field — these layers chronicle Kansas’s ecological heartbeat through time.”*

</div>
```
