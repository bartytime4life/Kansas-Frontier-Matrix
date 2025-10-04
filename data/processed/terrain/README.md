<div align="center">

# 🏔️ Kansas-Frontier-Matrix — Processed Terrain Data (`data/processed/terrain/`)

**Mission:** Maintain all **cleaned and standardized terrain datasets** —  
Digital Elevation Models (DEMs), filled surfaces, and pre-analysis terrain rasters —  
serving as the foundation for slope, aspect, and hydrology derivatives.

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
- [Core Terrain Datasets](#core-terrain-datasets)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Terrain Data](#contributing-new-terrain-data)
- [References](#references)

---

## 🗺️ Overview

This subdirectory contains **processed terrain datasets** that have been cleaned,  
reprojected, and standardized to serve as inputs for derivative generation.  

The layers here represent **analysis-ready elevation surfaces** — such as filled DEMs,  
hydrologically conditioned rasters, and historical elevation reconstructions —  
built from LiDAR, 3DEP, or legacy topographic sources.

All files are formatted as **Cloud-Optimized GeoTIFFs (COGs)** and referenced in the  
[`data/stac/`](../../stac/) catalog with complete provenance and processing metadata.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── terrain/
        ├── dem_1m_ks_filled.tif          # Sink-filled statewide 1 m DEM
        ├── dem_10m_hist_ks.tif           # Historical 10 m DEM (approx. 1950s–1970s topo)
        ├── dem_30m_ned_ks.tif            # 30 m NED elevation grid
        ├── contours_10m_ks.geojson       # Vectorized 10 m contours
        ├── hillshade_preview_ks.tif      # Pre-generated hillshade for quick QA
        ├── metadata/
        │   ├── dem_1m_ks_filled.json
        │   ├── dem_10m_hist_ks.json
        │   └── contours_10m_ks.json
        ├── checksums/
        │   ├── dem_1m_ks_filled.tif.sha256
        │   ├── dem_10m_hist_ks.tif.sha256
        │   └── contours_10m_ks.geojson.sha256
        └── README.md
````

---

## 🏞️ Core Terrain Datasets

| Product                 | File                       | Description                                                          | Source              | Units    | Format        |
| ----------------------- | -------------------------- | -------------------------------------------------------------------- | ------------------- | -------- | ------------- |
| **Filled DEM (1 m)**    | `dem_1m_ks_filled.tif`     | Kansas LiDAR-derived DEM with hydrologic sink filling applied        | KS DASC / USGS 3DEP | meters   | GeoTIFF (COG) |
| **Historic DEM (10 m)** | `dem_10m_hist_ks.tif`      | Historical elevation raster reconstructed from mid-century topo maps | USGS DRG series     | meters   | GeoTIFF (COG) |
| **NED DEM (30 m)**      | `dem_30m_ned_ks.tif`       | Coarse-resolution DEM for statewide modeling                         | USGS NED            | meters   | GeoTIFF (COG) |
| **Contours (10 m)**     | `contours_10m_ks.geojson`  | Vectorized contour lines derived from DEM surfaces                   | Derived             | meters   | GeoJSON       |
| **Hillshade Preview**   | `hillshade_preview_ks.tif` | Shaded relief map used for quality assessment                        | Derived             | DN 0–255 | GeoTIFF (COG) |

---

## 🧩 STAC Metadata

Each dataset is indexed in the project’s **STAC catalog** with full provenance and schema compliance.

Example STAC item:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "dem_1m_ks_filled",
  "properties": {
    "title": "Filled DEM (1 m) – Kansas LiDAR",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Hydrologically conditioned 1 m digital elevation model for Kansas, generated from LiDAR (2018–2020).",
    "processing:software": "WhiteboxTools 2.2.0 + GDAL 3.8.0",
    "mcp_provenance": "sha256:52a9e4…",
    "derived_from": ["data/raw/dem_1m_ks.tif"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./dem_1m_ks_filled.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## ⚙️ Processing Workflow

Terrain data in this directory is produced via the `Makefile` and Python ETL modules
located in `tools/terrain/`, using open-source tools such as **GDAL**, **WhiteboxTools**, and **PDAL**.

Example pipeline:

```bash
# 1. Fill sinks and remove voids
whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_1m_ks_filled.tif

# 2. Generate hillshade preview
gdaldem hillshade dem_1m_ks_filled.tif hillshade_preview_ks.tif -az 315 -alt 45 -z 1.0

# 3. Vectorize contours (10 m interval)
gdal_contour -i 10 dem_1m_ks_filled.tif contours_10m_ks.geojson -a elev

# 4. Convert to Cloud-Optimized GeoTIFF
rio cogeo create dem_1m_ks_filled.tif dem_1m_ks_filled_cog.tif --overview-level=5
```

All outputs are reprojected to **EPSG:4326 (WGS84)** and compressed using **Deflate/LZW**.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` files for all outputs ensure bit-level reproducibility.
* **STAC Compliance:** Metadata JSON validated via CI (STAC 1.0 + MCP schema).
* **Makefile Targets:**

  * `make terrain` — builds terrain products from raw data
  * `make validate-terrain` — runs metadata, checksum, and schema checks
* **Containerization:** Processing runs inside a Docker GDAL + WhiteboxTools environment.
* **QA Visualization:** Hillshade previews and contour overlays verified in QGIS/MapLibre.

---

## 🧠 Contributing New Terrain Data

1. Place the new DEM source file (GeoTIFF or LAS/LAZ) in `data/raw/` or `data/cogs/`.
2. Run your processing script (Python, GDAL, or PDAL) to produce a cleaned, filled, or resampled DEM.
3. Save output here in GeoTIFF (COG) or GeoJSON format.
4. Add:

   * `.sha256` checksum under `checksums/`
   * STAC metadata JSON under `metadata/`
   * `DERIVATION.md` describing parameters and software versions
5. Validate:

   ```bash
   make validate-terrain
   ```
6. Submit a PR with:

   * Input data citation
   * Processing workflow
   * Visualization suggestions (hillshade, contour style)

---

## 📖 References

* **USGS 3DEP LiDAR Data:** [https://www.usgs.gov/3dep](https://www.usgs.gov/3dep)
* **GDAL DEM Tools:** [https://gdal.org/programs/gdaldem.html](https://gdal.org/programs/gdaldem.html)
* **WhiteboxTools Documentation:** [https://www.whiteboxgeo.com/manual/](https://www.whiteboxgeo.com/manual/)
* **PDAL (LiDAR Processing):** [https://pdal.io/](https://pdal.io/)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)
* **Kansas DASC GIS Hub:** [https://hub.kansasgis.org](https://hub.kansasgis.org)

---

<div align="center">

*“The foundation of Kansas history lies in its contours — from Flint Hills to river valleys,
every elevation tells a story of the frontier.”*

</div>
```

