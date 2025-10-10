<div align="center">

# 💧 Kansas Frontier Matrix — Processed Hydrology Data  
`data/processed/hydrology/`

**Mission:** Maintain validated **hydrologic base surfaces** — sink-filled DEMs, D8 flow direction,  
base flow accumulation, water masks, and seed points — used to derive **stream networks**,  
**watershed boundaries**, and **flood-risk models** across Kansas.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📘 Overview

This directory contains **processed hydrology datasets** created during DEM conditioning  
and terrain preprocessing. These rasters form the basis for hydrologic and geomorphic  
derivatives — such as **flow accumulation**, **stream network extraction**, and  
**basin delineation** — used throughout the Kansas Frontier Matrix.

**Primary Sources**
- 1 m LiDAR DEMs (Kansas DASC / USGS 3DEP)  
- 10–30 m Historical DEMs (USGS Topographic Series)  
- Auxiliary layers: NLCD Water, NHD Hydrography, GNIS Features  

**Data Standards**
- Format: **Cloud-Optimized GeoTIFF (COG)**  
- Projection: **EPSG 4326 – WGS 84**  
- Catalog: Registered under `data/stac/items/hydro_*`  

---

## 🗂 Directory Layout

```bash
data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif
        ├── flow_dir_d8_1m_ks.tif
        ├── flow_accum_base_1m_ks.tif
        ├── watermask_ks.tif
        ├── stream_seed_points.geojson
        ├── metadata/
        │   ├── dem_filled_1m_ks.json
        │   ├── flow_dir_d8_1m_ks.json
        │   └── flow_accum_base_1m_ks.json
        ├── checksums/
        │   ├── dem_filled_1m_ks.tif.sha256
        │   ├── flow_dir_d8_1m_ks.tif.sha256
        │   └── flow_accum_base_1m_ks.tif.sha256
        └── README.md


⸻

💦 Core Datasets

Product	File	Description	Source	Units	Format
Filled DEM	dem_filled_1m_ks.tif	1 m LiDAR DEM with sinks filled for hydrologic continuity	KS LiDAR / USGS 3DEP	m	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	Encodes downslope flow direction (ESRI D8 model 1–128)	Derived (WBT)	int	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation prior to stream thresholding	Derived (WBT)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary raster (NLCD + NHD fusion) — 1 = water	USGS / DASC	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate pour points / outlets for watershed modeling	Derived	n/a	GeoJSON


⸻

🧩 STAC Metadata Example

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
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


⸻

⚙️ Processing Workflow

flowchart TD
    A["Raw DEMs"] --> B["Fill Depressions (WhiteboxTools)"]
    B --> C["D8 Flow Direction"]
    B --> D["D8 Flow Accumulation"]
    C & D --> E["Seed Point Extraction (threshold logic)"]
    F["NLCD + NHD"] --> G["Water Mask (GDAL Calc)"]
    B & C & D & E & G --> H["Reproject + Convert to COG (rio cogeo)"]
    H --> I["STAC Item Generation + Checksums"]
<!-- END OF MERMAID -->

Example Commands

whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_dir_d8_1m_ks.tif
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accum_base_1m_ks.tif
gdal_calc.py -A nlcd_water_ks.tif -B nhd_water_ks.tif \
  --outfile=watermask_ks.tif --calc="((A>0)|(B>0)).astype(uint8)"
python tools/hydro/seed_points.py --accum flow_accum_base_1m_ks.tif --threshold 500


⸻

🔁 Reproducibility & Validation

Check	Method
Integrity	.sha256 hashes verified in CI
Metadata	STAC 1.0 validation (make stac-validate)
Pipeline	make hydrology or make validate-hydro
Environment	Docker (GDAL + WhiteboxTools + Python)
QA/QC	Visual check in QGIS vs USGS NHD baseline


⸻

🧠 Contributing
	1.	Add new processed files (COG or GeoJSON).
	2.	Create STAC JSON in metadata/ and checksum in checksums/.
	3.	Write DERIVATION.md documenting inputs + parameters.
	4.	Validate with make validate-hydro.
	5.	Submit a Pull Request including sources, licenses, and visual examples.

All new data must pass STAC and checksum validation before merge.

⸻

📖 References
	•	WhiteboxTools: https://www.whiteboxgeo.com/manual/wbt_book/hydro.html
	•	TauDEM: https://hydrology.usu.edu/taudem
	•	GDAL: https://gdal.org
	•	USGS NHD: https://www.usgs.gov/national-hydrography
	•	Kansas DASC Hub: https://hub.kansasgis.org
	•	STAC Spec 1.0: https://stacspec.org
	•	MCP Docs: docs/standards/

⸻


<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>
```
