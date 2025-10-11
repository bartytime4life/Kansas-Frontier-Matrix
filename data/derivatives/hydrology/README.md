<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Derivatives

`data/derivatives/hydrology/`

**Mission:** Maintain and document all **hydrology-derived products** — including flow direction, accumulation, watershed delineations, stream networks, and floodplain composites — generated from DEMs and hydrological datasets spanning the Kansas frontier.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/pre-commit.yml?label=Pre--Commit)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)
[![Version](https://img.shields.io/badge/Version-v1.3.2-blueviolet)](CHANGELOG.md)

</div>

---

## 📚 Table of Contents

* [Overview](#overview)
* [Directory Layout](#directory-layout)
* [Core Hydrology Products](#core-hydrology-products)
* [STAC Metadata](#stac-metadata)
* [Processing Workflow](#processing-workflow)
* [Reproducibility & Validation](#reproducibility--validation)
* [Versioning & Changelog](#versioning--changelog)
* [Contributing New Hydrology Layers](#contributing-new-hydrology-layers)
* [References](#references)

---

## 🌊 Overview

The **Hydrology Derivatives** subdirectory houses advanced geospatial layers representing Kansas’s water systems,
generated through reproducible ETL workflows using DEMs, LiDAR, and hydrological datasets.

These layers support:

* **Flood modeling and disaster risk analysis**
* **Watershed and drainage basin delineation**
* **Streamflow simulation and flow path tracing**
* **Hydrological network validation and stream mapping**

All derivative outputs adhere to **Master Coder Protocol (MCP)** documentation standards and are registered in the
[Kansas Frontier Matrix STAC catalog](../../stac/) for provenance, discoverability, and validation.

---

## 🧭 Version Metadata

| Field          | Value                                            |
| :------------- | :----------------------------------------------- |
| **Version**    | `v1.3.2`                                         |
| **Updated**    | `2025-10-11`                                     |
| **Maintainer** | KFM Hydrology & Terrain Team                     |
| **Schema**     | STAC 1.0.0 + MCP v2.1                            |
| **License**    | CC-BY 4.0 (Data) · MIT (Code)                    |
| **Validation** | STAC Schema, GeoJSON Topology, SHA-256 Integrity |

---

## 🗂️ Directory Layout

```bash
data/
└── derivatives/
    └── hydrology/
        ├── flow_direction_1m_ks.tif         # D8 flow direction raster
        ├── flow_accumulation_1m_ks.tif      # Flow accumulation grid
        ├── stream_network_ks.geojson        # Derived stream network (vector)
        ├── watersheds_ks.geojson            # Drainage basins / HUC-12 boundaries
        ├── flood_risk_zones_ks.tif          # Composite flood risk index
        ├── metadata/
        │   ├── flow_direction_1m_ks.json
        │   ├── flow_accumulation_1m_ks.json
        │   └── stream_network_ks.json
        ├── checksums/
        │   ├── flow_direction_1m_ks.tif.sha256
        │   ├── flow_accumulation_1m_ks.tif.sha256
        │   └── stream_network_ks.geojson.sha256
        └── README.md
```

---

## 💦 Core Hydrology Products

| Product                  | File                          | Description                                          | Source               | Units      | Format        |
| :----------------------- | :---------------------------- | :--------------------------------------------------- | :------------------- | :--------- | :------------ |
| **Flow Direction**       | `flow_direction_1m_ks.tif`    | D8 flow direction encoding steepest descent per cell | LiDAR DEM (1 m)      | 1–255      | GeoTIFF (COG) |
| **Flow Accumulation**    | `flow_accumulation_1m_ks.tif` | Upstream contributing area per cell                  | LiDAR DEM (1 m)      | cell count | GeoTIFF (COG) |
| **Stream Network**       | `stream_network_ks.geojson`   | Vectorized streams thresholded by flow accumulation  | Derived from FlowAcc | meters     | GeoJSON       |
| **Watershed Boundaries** | `watersheds_ks.geojson`       | Delineated basins (HUC-12 scale)                     | DEM + FlowDir        | polygons   | GeoJSON       |
| **Flood Risk Composite** | `flood_risk_zones_ks.tif`     | Composite slope × landcover × flow index             | Derived composite    | 0–1        | GeoTIFF (COG) |

---

## 🧩 STAC Metadata Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_direction_1m_ks",
  "properties": {
    "title": "Flow Direction – Kansas LiDAR 1 m DEM",
    "description": "D8 flow direction raster derived from LiDAR DEM. Encodes flow direction degrees.",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "mcp_provenance": "sha256:b8c9e2...",
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

```bash
# 1. Fill sinks to remove depressions
whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif

# 2. Derive D8 flow direction
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_direction_1m_ks.tif

# 3. Calculate flow accumulation grid
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accumulation_1m_ks.tif

# 4. Extract streams (>500 contributing cells)
whitebox_tools --run=ExtractStreams -i flow_accumulation_1m_ks.tif -o stream_network_ks.tif --threshold=500

# 5. Convert raster streams to GeoJSON
gdal_polygonize.py stream_network_ks.tif stream_network_ks.geojson

# 6. Optional: Delineate watersheds
whitebox_tools --run=Watershed -d8_pntr flow_direction_1m_ks.tif -pour_pts outlets.shp -o watersheds_ks.tif
```

All outputs are automatically **COG-optimized**, tiled, and linked via STAC for reproducible workflows.

---

## 🔁 Reproducibility & Validation

✅ **Checksums:** Every artifact includes `.sha256` integrity manifests
✅ **STAC Validation:** Auto-checked in CI for schema compliance
✅ **GeoJSON QA:** Topology and CRS validation with `geojson-lint`
✅ **Cross-verification:** NHD Flowlines and Kansas DASC datasets
✅ **Environment:** Dockerized GDAL + WhiteboxTools + TauDEM
✅ **Reproducible Targets:**

```bash
make hydrology         # build hydrologic layers
make validate-hydro    # run schema and checksum validations
```

---

## 🧾 Versioning & Changelog

| Version    | Date       | Description                                    | Author         |
| :--------- | :--------- | :--------------------------------------------- | :------------- |
| **v1.3.2** | 2025-10-11 | Added version table, badges, changelog section | KFM Docs Team  |
| **v1.3.1** | 2025-09-30 | Enhanced STAC JSON templates                   | KFM Data Ops   |
| **v1.3.0** | 2025-09-01 | Rebuilt hydrology workflows using MCP v2.1     | Hydrology Core |

*All future updates must bump version number and append changelog entries per MCP protocol.*

---

## 🧠 Contributing New Hydrology Layers

1. Create a new folder under `data/derivatives/hydrology/your_layer/`
2. Produce **COG** or **GeoJSON** outputs using open tools (GDAL, WhiteboxTools, TauDEM)
3. Add:

   * STAC metadata (`metadata/<layer>.json`)
   * SHA-256 checksums (`checksums/<layer>.sha256`)
   * `DERIVATION.md` with source datasets, methods, and parameters
4. Validate with:

   ```bash
   make validate-hydro
   ```
5. Open a Pull Request including:

   * data & metadata files
   * reproducible scripts or notebooks
   * updated changelog and version bump

All contributions are automatically tested through GitHub Actions (STAC + schema + integrity).

---

## 📖 References

* **WhiteboxTools Hydrology Suite:** [whiteboxgeo.com/manual/wbt_book/hydro.html](https://www.whiteboxgeo.com/manual/wbt_book/hydro.html)
* **TauDEM Toolbox:** [hydrology.usu.edu/taudem](https://hydrology.usu.edu/taudem/)
* **GDAL DEM Utilities:** [gdal.org/programs/gdaldem.html](https://gdal.org/programs/gdaldem.html)
* **STAC 1.0 Spec:** [stacspec.org](https://stacspec.org)
* **Cloud-Optimized GeoTIFF:** [cogeo.org](https://www.cogeo.org)
* **USGS NHD & Hydrography:** [usgs.gov/national-hydrography](https://www.usgs.gov/national-hydrography)
* **Kansas DASC Hydro Layers:** [hub.kansasgis.org](https://hub.kansasgis.org)
* **Master Coder Protocol Docs:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

> *“From prairie rains to river plains — these datasets trace the living hydrology of Kansas through space and time.”*
> **Version v1.3.2 · Compliant with MCP v2.1 · Validated STAC Schema · Reproducible Make Pipeline**

</div>
