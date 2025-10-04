<div align="center">

# 💧 Kansas-Frontier-Matrix — Processed Hydrology Data (`data/processed/hydrology/`)

**Mission:** Store and document all **hydrology-processed datasets** — sink-filled DEMs, flow direction grids,  
and pre-derivative hydrologic surfaces — that serve as the foundation for stream networks, watershed delineations,  
and flood-risk modeling across Kansas.

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
- [Core Hydrology Datasets](#core-hydrology-datasets)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Hydrology Data](#contributing-new-hydrology-data)
- [References](#references)

---

## 🌊 Overview

This subdirectory contains **processed hydrologic surfaces and layers** generated from  
DEM preprocessing and flow modeling routines.  

These datasets are used as inputs for derivative products such as flow accumulation,  
stream extraction, and watershed boundary delineation (see `data/derivatives/hydrology/`).

Data sources include LiDAR-derived DEMs (1 m), historical topographic DEMs (10–30 m),  
and auxiliary hydrologic datasets from **USGS NHD**, **NOAA**, and **Kansas DASC**.  

All outputs are standardized as **Cloud-Optimized GeoTIFFs (COGs)**, reprojected to  
EPSG:4326, and cataloged via [STAC metadata](../../stac/).

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif           # Hydrologically conditioned DEM (sink-filled)
        ├── flow_dir_d8_1m_ks.tif          # D8 flow direction raster
        ├── flow_accum_base_1m_ks.tif      # Base accumulation raster
        ├── stream_seed_points.geojson     # Outlets and pour points for basins
        ├── watermask_ks.tif               # Binary raster water mask (water=1)
        ├── metadata/
        │   ├── dem_filled_1m_ks.json
        │   ├── flow_dir_d8_1m_ks.json
        │   └── flow_accum_base_1m_ks.json
        ├── checksums/
        │   ├── dem_filled_1m_ks.tif.sha256
        │   ├── flow_dir_d8_1m_ks.tif.sha256
        │   └── flow_accum_base_1m_ks.tif.sha256
        └── README.md
````

Each product here represents a validated, intermediate hydrologic surface ready for
further derivative generation (streamlines, basins, hazard mapping).

---

## 💦 Core Hydrology Datasets

| Product                      | File                         | Description                                                         | Source          | Units   | Format        |
| ---------------------------- | ---------------------------- | ------------------------------------------------------------------- | --------------- | ------- | ------------- |
| **Filled DEM**               | `dem_filled_1m_ks.tif`       | 1 m LiDAR DEM with hydrologic sink filling                          | KS LiDAR / 3DEP | meters  | GeoTIFF (COG) |
| **Flow Direction (D8)**      | `flow_dir_d8_1m_ks.tif`      | Encodes downslope flow direction (1–255)                            | Derived         | integer | GeoTIFF (COG) |
| **Flow Accumulation (Base)** | `flow_accum_base_1m_ks.tif`  | Raw flow accumulation before thresholding                           | Derived         | cells   | GeoTIFF (COG) |
| **Stream Seed Points**       | `stream_seed_points.geojson` | Candidate outlet/pour points for watershed segmentation             | Derived         | n/a     | GeoJSON       |
| **Water Mask**               | `watermask_ks.tif`           | Binary raster (1 = water, 0 = land) derived from NLCD + Hydrography | USGS / DASC     | binary  | GeoTIFF (COG) |

---

## 🧩 STAC Metadata

All processed hydrology files are indexed in the project’s STAC catalog (`data/stac/items/hydro_*`)
with full provenance, lineage, and temporal coverage.

Example STAC Item:

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Flow direction grid computed using D8 algorithm from hydrologically conditioned 1 m DEM.",
    "processing:software": "WhiteboxTools 2.2.0",
    "mcp_provenance": "sha256:4be51c…",
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./flow_dir_d8_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

---

## ⚙️ Processing Workflow

All processing follows reproducible steps using **WhiteboxTools**, **GDAL**, and **Python**
scripts in `tools/hydro/`. These workflows are invoked through the project `Makefile`.

Example CLI sequence:

```bash
# 1. Hydrologic conditioning – fill sinks
whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif

# 2. Generate flow direction (D8)
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_dir_d8_1m_ks.tif

# 3. Compute base flow accumulation
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accum_base_1m_ks.tif

# 4. Create water mask (from NLCD & NHD)
gdal_calc.py -A nlcd_water_ks.tif -B nhd_water_ks.tif --outfile=watermask_ks.tif --calc="(A>0)|(B>0)"

# 5. Export pour points for basin modeling
python tools/hydro/seed_points.py --accum flow_accum_base_1m_ks.tif --threshold 500
```

Outputs are automatically reprojected and converted to COG format via `rio cogeo create`.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` hashes ensure file integrity.
* **STAC Validation:** Metadata tested in CI against STAC 1.0 schema.
* **Makefile Targets:**

  * `make hydrology` — rebuild all hydrologic processed layers
  * `make validate-hydro` — validate metadata and checksums
* **Containerization:** Runs within Docker (GDAL + WhiteboxTools + Python) for full reproducibility.
* **QA Checks:** Stream outlets and DEM fills visually verified in QGIS and compared against NHD baselines.

---

## 🧠 Contributing New Hydrology Data

1. Add new processed outputs (COG or GeoJSON) to this folder.
2. Create a STAC metadata JSON under `metadata/` and a `.sha256` checksum under `checksums/`.
3. Add a `DERIVATION.md` documenting:

   * input datasets (`derived_from`),
   * tools used,
   * key parameters (e.g., D8 threshold).
4. Validate locally with:

   ```bash
   make validate-hydro
   ```
5. Submit a Pull Request including:

   * data sources & licenses,
   * description of purpose,
   * visualization suggestions (color ramp, legend).

---

## 📖 References

* **WhiteboxTools:** [https://www.whiteboxgeo.com/manual/wbt_book/hydro.html](https://www.whiteboxgeo.com/manual/wbt_book/hydro.html)
* **TauDEM (Hydrologic Modeling):** [https://hydrology.usu.edu/taudem/](https://hydrology.usu.edu/taudem/)
* **GDAL Utilities:** [https://gdal.org/](https://gdal.org/)
* **USGS NHD Dataset:** [https://www.usgs.gov/national-hydrography](https://www.usgs.gov/national-hydrography)
* **Kansas DASC GIS Hub:** [https://hub.kansasgis.org](https://hub.kansasgis.org)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **MCP Documentation:** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”*

</div>
```

