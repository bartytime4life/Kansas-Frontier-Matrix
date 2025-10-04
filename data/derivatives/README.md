<div align="center">

# 🧭 Kansas-Frontier-Matrix — Derived Geospatial Products (`data/derivatives/`)

**Mission:** Store and document **analysis-ready geospatial derivatives** — terrain products, composites,  
and synthesized overlays generated from canonical data in `data/cogs/` and `data/sources/`.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC-BY%204.0-green)](../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Core Products](#core-products)
- [STAC Integration](#stac-integration)
- [Reproducibility & Provenance](#reproducibility--provenance)
- [Contributing New Derivatives](#contributing-new-derivatives)
- [References](#references)

---

## 🗺️ Overview
This directory contains **value-added layers** derived from foundational data in  
`data/sources/` and `data/cogs/`.  Each product is reproducible via documented ETL workflows and  
registered in the project’s **SpatioTemporal Asset Catalog (STAC)**.

Typical examples:
- **Terrain products** — slope, aspect, curvature, hillshade.
- **Hydrology derivatives** — flow direction, accumulation, watershed boundaries.
- **Land-use and vegetation indices** — NDVI, NDWI, historical land-cover change maps.
- **Hazard analytics** — drought, flood, wildfire intensity composites.
- **Composited rasters** — time-series mosaics or county-level COG stacks.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    ├── terrain/           # DEM-based slope, aspect, curvature
    ├── hydrology/         # flow accumulation, drainage networks
    ├── landcover/         # NDVI, land-use transitions
    ├── hazards/           # drought/flood/fire composite layers
    ├── climate/           # interpolated temperature/precipitation grids
    ├── metadata/          # JSON schema + STAC item entries
    ├── README.md          # (this file)
    └── .gitkeep
````

Each subfolder corresponds to a **domain theme** and may contain multiple derivative layers.
Heavy GeoTIFF outputs are tracked via **DVC or Git LFS**; light CSV/JSON derivatives are versioned normally.

---

## 🌐 Core Products

| Category  | File Format       | Description                                   | Example Product                               |
| --------- | ----------------- | --------------------------------------------- | --------------------------------------------- |
| Terrain   | COG GeoTIFF       | Slope, aspect, curvature, hillshade           | `terrain/slope_1m_ks.tif`                     |
| Hydrology | GeoTIFF + GeoJSON | Flow direction & drainage vectorization       | `hydrology/flowdir_ks.tif`, `streams.geojson` |
| Landcover | COG GeoTIFF       | 1992–2021 NLCD comparative rasters            | `landcover/nlcd_change_1992_2021.tif`         |
| Hazards   | GeoTIFF           | Drought severity or wildfire density heatmaps | `hazards/drought_spi_1950_2020.tif`           |
| Climate   | CSV + Parquet     | Aggregated climate normals (county level)     | `climate/temp_normals_1991_2020.parquet`      |

---

## 🧩 STAC Integration

Every derivative layer is registered under `data/stac/items/` with full metadata:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "terrain_slope_1m_ks",
  "properties": {
    "datetime": "2020-01-01",
    "description": "1-m statewide slope map derived from Kansas LiDAR DEM.",
    "created_by": "ETL pipeline v2.3",
    "mcp_provenance": "sha256:abcd1234...",
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "../terrain/slope_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

STAC validation runs automatically in CI (see `.github/workflows/stac-validate.yml`) ensuring consistency
of temporal/spatial metadata and reproducibility across layers.

---

## 🔁 Reproducibility & Provenance

* **Makefile Targets:**  `make derivatives` builds all products from source COGs.
* **Checksums:**  Every derivative includes a `.sha256` sidecar.
* **Schemas:**  JSON Schemas for derivative metadata reside under `data/derivatives/metadata/schema/`.
* **Versioning:**  Each artifact embeds a `kfm_version` tag in metadata and STAC entries.
* **Lineage:**  The STAC link `derived_from` traces each file back to its originating dataset(s).

All processes are fully reproducible following the **Master Coder Protocol** documentation standards.

---

## 🧠 Contributing New Derivatives

1. Create a new subfolder (e.g. `landcover/forest_density/`).
2. Generate output in open format (COG, GeoJSON, CSV).
3. Add a STAC item JSON under `data/stac/items/`.
4. Include a `.sha256` checksum and short `DERIVATION.md` explaining the method.
5. Run `make validate` to verify schema and checksums.
6. Submit a Pull Request with:

   * data license/source citation,
   * processing workflow reference (`tools/` script or notebook),
   * visualization suggestion (color ramp, opacity, legend).

Bad PRs will fail CI if STAC/JSON Schema validation fails.

---

## 🔍 References

* **STAC 1.0.0 Spec:** [https://stacspec.org](https://stacspec.org)
* **OGC GeoTIFF & COG Standards**
* **GeoJSON RFC 7946**
* **Master Coder Protocol (MCP) Docs:** [`docs/standards/`](../../docs/standards/)
* **Kansas LiDAR & DEM Data:** Kansas GIS Hub & USGS 3DEP

---

<div align="center">

*“Every derived layer tells a story of Kansas — terrain, water, and time woven into data.”*

</div>
```

---

✅ **Highlights**

* Uses all project-standard badges and formatting.
* Mirrors your `data/sources` and `data/cogs` READMEs in tone and structure.
* Adds full STAC integration, provenance, and CI details.
* Includes explicit contributor workflow and reproducibility notes.
