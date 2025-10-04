<div align="center">

# 🏔️ Kansas-Frontier-Matrix — Terrain Derivatives (`data/derivatives/terrain/`)

**Mission:** Curate and maintain all **terrain-derived raster products** — slope, aspect, curvature, hillshade,  
and elevation composites — generated from canonical DEMs in `data/cogs/`.

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
- [Core Terrain Products](#core-terrain-products)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Terrain Layers](#contributing-new-terrain-layers)
- [References](#references)

---

## 🗺️ Overview
This subdirectory contains **terrain analysis outputs** derived from Kansas’s statewide and regional  
Digital Elevation Models (DEMs). These datasets quantify slope, aspect, hillshade, and surface morphology,  
forming the foundation for hydrologic modeling, landform classification, and historical topography studies.

All files follow **open geospatial standards** and are registered in the project’s  
[STAC catalog](../../stac/) with complete provenance, license, and temporal metadata.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── terrain/
        ├── slope_1m_ks.tif              # Percent slope derived from 1-m LiDAR DEM
        ├── aspect_1m_ks.tif             # Aspect (azimuth) in degrees
        ├── curvature_1m_ks.tif          # Surface curvature (profile + plan)
        ├── hillshade_1m_ks.tif          # Analytical hillshade (45° sun angle)
        ├── elevation_10m_hist.tif       # Historic generalized DEM (10 m res)
        ├── metadata/
        │   ├── slope_1m_ks.json         # STAC item metadata
        │   ├── aspect_1m_ks.json
        │   └── hillshade_1m_ks.json
        ├── checksums/
        │   ├── slope_1m_ks.tif.sha256
        │   └── aspect_1m_ks.tif.sha256
        └── README.md                    # (this file)
````

---

## 🌄 Core Terrain Products

| Product          | File                     | Description                                | Source DEM         | Units    | Format        |
| ---------------- | ------------------------ | ------------------------------------------ | ------------------ | -------- | ------------- |
| **Slope**        | `slope_1m_ks.tif`        | Rate of elevation change (percent rise)    | KS 1-m LiDAR       | %        | GeoTIFF (COG) |
| **Aspect**       | `aspect_1m_ks.tif`       | Direction of slope faces (azimuth degrees) | KS 1-m LiDAR       | °        | GeoTIFF (COG) |
| **Curvature**    | `curvature_1m_ks.tif`    | Combined plan/profile curvature            | KS 1-m LiDAR       | unitless | GeoTIFF (COG) |
| **Hillshade**    | `hillshade_1m_ks.tif`    | Simulated shaded relief (45° sun)          | KS 1-m LiDAR       | DN 0–255 | GeoTIFF (COG) |
| **Historic DEM** | `elevation_10m_hist.tif` | Reconstructed 19th-century DEM (10 m)      | USGS topo archives | m        | GeoTIFF       |

All files are **Cloud-Optimized GeoTIFFs (COGs)** to support fast, range-based HTTP access and
render seamlessly in MapLibreGL or GIS tools.

---

## 🧩 STAC Metadata

Each raster layer is indexed as a STAC Item under `data/stac/items/terrain_*` with complete metadata.
Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "hillshade_1m_ks",
  "properties": {
    "title": "Hillshade – Kansas LiDAR 1 m DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Analytical hillshade from Kansas 1 m LiDAR DEM, azimuth 315°, altitude 45°.",
    "processing:software": "GDAL 3.8.0",
    "mcp_provenance": "sha256:fb2e5e…",
    "license": "CC-BY 4.0",
    "derived_from": ["data/cogs/dem_1m_ks.tif"]
  },
  "assets": {
    "data": {
      "href": "./hillshade_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "links": []
}
```

---

## ⚙️ Processing Workflow

Terrain derivatives are generated from DEMs using reproducible **GDAL- and rasterio-based** workflows
invoked via `Makefile` targets or Python scripts in `tools/terrain/`.

Typical processing sequence:

```bash
# 1. Compute slope (percent rise)
gdaldem slope dem_1m_ks.tif slope_1m_ks.tif -s 111120

# 2. Compute aspect (azimuth)
gdaldem aspect dem_1m_ks.tif aspect_1m_ks.tif -zero_for_flat yes

# 3. Generate curvature
gdaldem TRI dem_1m_ks.tif curvature_1m_ks.tif

# 4. Generate analytical hillshade
gdaldem hillshade dem_1m_ks.tif hillshade_1m_ks.tif -az 315 -alt 45 -z 1.0
```

All outputs are automatically tiled and converted to **COG** via `rio cogeo create`.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` sidecars verify file integrity.
* **Metadata validation:** JSON metadata is tested in CI against the STAC 1.0 schema.
* **Makefile targets:**

  * `make terrain` — rebuild all terrain derivatives.
  * `make validate-terrain` — run metadata and checksum checks.
* **Containerized build:** Terrain processing runs in a Dockerized GDAL environment for consistency.
* **Visualization QA:** Each raster is previewed in QGIS and via `maplibre-gl` test tiles.

---

## 🧠 Contributing New Terrain Layers

1. Place the source DEM or derivative script in `data/cogs/` or `tools/terrain/`.
2. Generate the raster as a COG GeoTIFF (WGS84 or EPSG:4326).
3. Add STAC metadata JSON under `metadata/` and `.sha256` checksum under `checksums/`.
4. Document your process in a short `DERIVATION.md` (inputs, parameters, software).
5. Run:

   ```bash
   make validate-terrain
   ```

   to confirm schema and checksums pass.
6. Submit a pull request with a clear description, data license, and visual style suggestion.

---

## 📖 References

* **GDAL DEM utilities:** [https://gdal.org/programs/gdaldem.html](https://gdal.org/programs/gdaldem.html)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **USGS 3DEP LiDAR for Kansas:** [https://www.usgs.gov/3DEP](https://www.usgs.gov/3DEP)
* **Kansas DASC GIS Hub:** [https://hub.kansasgis.org](https://hub.kansasgis.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“Every contour holds a story — from prairie swales to frontier bluffs, Kansas terrain is the canvas of history.”*

</div>
```
