<div align="center">

# 💧 Kansas-Frontier-Matrix — Hydrology Derivatives (`data/derivatives/hydrology/`)

**Mission:** Contain all **hydrology-derived products** — flow direction, accumulation, watershed delineations,  
stream networks, and floodplain composites — derived from DEMs and hydrological datasets across Kansas.

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
- [Core Hydrology Products](#core-hydrology-products)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Hydrology Layers](#contributing-new-hydrology-layers)
- [References](#references)

---

## 🌊 Overview

This subdirectory hosts **hydrologic analyses and derivative layers** generated from Kansas DEMs,  
surface-water inventories, and watershed datasets. It includes raster products (flow direction, accumulation)  
and vectorized hydrological features (stream networks, watershed polygons).

These layers power **flood modeling**, **streamflow visualization**, and **environmental change detection**,  
enabling researchers to visualize Kansas’s dynamic hydrological systems across time.

All derivatives are standardized as **Cloud-Optimized GeoTIFF (COG)** and **GeoJSON** files  
and registered within the [STAC catalog](../../stac/) for transparency and reproducibility.

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── hydrology/
        ├── flow_direction_1m_ks.tif         # D8 flow direction raster
        ├── flow_accumulation_1m_ks.tif      # Flow accumulation grid
        ├── stream_network_ks.geojson        # Extracted stream polylines
        ├── watersheds_ks.geojson            # HUC-12 / derived watershed polygons
        ├── flood_risk_zones_ks.tif          # Composite floodplain risk index
        ├── metadata/
        │   ├── flow_direction_1m_ks.json
        │   ├── flow_accumulation_1m_ks.json
        │   └── stream_network_ks.json
        ├── checksums/
        │   ├── flow_direction_1m_ks.tif.sha256
        │   ├── flow_accumulation_1m_ks.tif.sha256
        │   └── stream_network_ks.geojson.sha256
        └── README.md
````

---

## 💦 Core Hydrology Products

| Product                  | File                          | Description                                            | Source               | Units           | Format        |
| ------------------------ | ----------------------------- | ------------------------------------------------------ | -------------------- | --------------- | ------------- |
| **Flow Direction**       | `flow_direction_1m_ks.tif`    | Encodes direction of steepest descent using D8 method  | DEM 1 m LiDAR        | Integer (1–255) | GeoTIFF (COG) |
| **Flow Accumulation**    | `flow_accumulation_1m_ks.tif` | Cell-wise count of upstream contributing area          | DEM 1 m LiDAR        | cell count      | GeoTIFF (COG) |
| **Stream Network**       | `stream_network_ks.geojson`   | Vectorized streams from thresholded flow accumulation  | Derived from FlowAcc | meters          | GeoJSON       |
| **Watershed Boundaries** | `watersheds_ks.geojson`       | Delineated drainage basins (HUC-12 scale)              | DEM + FlowDir        | polygon         | GeoJSON       |
| **Flood Risk Composite** | `flood_risk_zones_ks.tif`     | Combined slope, landcover, and flow accumulation index | Derived composite    | 0–1             | GeoTIFF (COG) |

Each product provides insight into Kansas’s hydrologic patterns — from high plains ephemeral streams
to flood-prone alluvial zones along the Kansas and Arkansas Rivers.

---

## 🧩 STAC Metadata

Each hydrology layer includes a **STAC item JSON** in `metadata/`, enabling catalog discovery and
linking to its source datasets (`data/cogs/` DEMs, `data/sources/hydro/`).

Example:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_direction_1m_ks",
  "properties": {
    "title": "Flow Direction – Kansas LiDAR 1 m DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "D8 flow direction raster derived from Kansas LiDAR 1 m DEM. Encodes flow angle in degrees.",
    "processing:software": "WhiteboxTools 2.2.0",
    "mcp_provenance": "sha256:b8c9e2…",
    "license": "CC-BY 4.0",
    "derived_from": ["data/cogs/dem_1m_ks.tif"]
  },
  "assets": {
    "data": {
      "href": "./flow_direction_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## ⚙️ Processing Workflow

Hydrology derivatives are built using **GDAL**, **WhiteboxTools**, and **TauDEM**,
scripted through the project’s Makefile and Python ETL modules in `tools/hydro/`.

Example CLI workflow:

```bash
# 1. Fill sinks (depressions)
whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif

# 2. Generate flow direction (D8)
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_direction_1m_ks.tif

# 3. Calculate flow accumulation
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accumulation_1m_ks.tif

# 4. Extract streams using threshold (e.g., >500 cells)
whitebox_tools --run=ExtractStreams -i flow_accumulation_1m_ks.tif -output stream_network_ks.tif --threshold=500

# 5. Vectorize stream network
gdal_polygonize.py stream_network_ks.tif stream_network_ks.geojson

# 6. Delineate watersheds (optional)
whitebox_tools --run=Watershed -d8_pntr flow_direction_1m_ks.tif -pour_pts outlets.shp -o watersheds_ks.tif
```

Outputs are automatically tiled and converted to **COG** for optimal web access.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` files accompany each artifact.
* **Validation:** CI runs STAC schema and GeoJSON topology checks.
* **Makefile targets:**

  * `make hydrology` → builds all hydrologic layers
  * `make validate-hydro` → runs metadata and schema tests
* **Containerized Tools:** WhiteboxTools + GDAL run inside a Dockerized environment for consistency.
* **Cross-verification:** Derived stream networks are validated against USGS NHD Flowlines.

---

## 🧠 Contributing New Hydrology Layers

1. Create a new subfolder (e.g. `data/derivatives/hydrology/flood_model/`).
2. Generate outputs (COG GeoTIFF or GeoJSON) using documented, open-source tools.
3. Add STAC metadata JSON and `.sha256` checksum.
4. Include `DERIVATION.md` detailing data sources, parameters, and methods.
5. Run:

   ```bash
   make validate-hydro
   ```
6. Submit a Pull Request with:

   * STAC metadata,
   * method reference (script or notebook),
   * appropriate data license.

All submissions are automatically validated by GitHub Actions for schema compliance and integrity.

---

## 📖 References

* **WhiteboxTools Hydrology Suite:** [https://www.whiteboxgeo.com/manual/wbt_book/hydro.html](https://www.whiteboxgeo.com/manual/wbt_book/hydro.html)
* **TauDEM Toolbox:** [https://hydrology.usu.edu/taudem/](https://hydrology.usu.edu/taudem/)
* **GDAL DEM Utilities:** [https://gdal.org/programs/gdaldem.html](https://gdal.org/programs/gdaldem.html)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **COG Format:** [https://www.cogeo.org](https://www.cogeo.org)
* **USGS NHD & Hydrography:** [https://www.usgs.gov/national-hydrography](https://www.usgs.gov/national-hydrography)
* **Kansas DASC Hydro Layers:** [https://hub.kansasgis.org](https://hub.kansasgis.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From prairie rains to river plains — these layers trace the pulse of Kansas water through time.”*

</div>
```

