<div align="center">

# 💧 Kansas Frontier Matrix — Processed Hydrology Data  
`data/processed/hydrology/`

**Mission:** Maintain validated **hydrologic base surfaces** — sink-filled DEMs, D8 flow direction,  
base flow accumulation, water masks, and seed points — that power **stream networks**, **basins**,  
and **flood-risk modeling** across Kansas.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

⸻

📚 **Table of Contents**  
• 🌊 Overview  
• 🧱 Directory Layout  
• 💦 Core Hydrology Datasets  
• 🧩 STAC Metadata  
• ⚙️ Processing Workflow  
• 🔁 Reproducibility & Validation  
• 🧠 Contributing  
• 📖 References  

⸻

🌊 **Overview**

This directory contains **processed hydrologic surfaces and layers** created from DEM conditioning and flow-routing.  
These intermediate artifacts drive **flow accumulation, stream extraction, basin segmentation,** and **flood simulations**.

**Sources** — LiDAR 1 m DEMs (DASC / USGS 3DEP), historical 10–30 m DEMs, NLCD water, NHD hydrography, GNIS features.  
**Standards** — COG GeoTIFF (rasters) and GeoJSON (vectors), **EPSG:4326**.  
**Catalog** — Registered under `data/stac/items/hydro_*`.

⸻

🧱 **Directory Layout**

```bash
data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif           # Hydro-conditioned DEM (sink-filled)
        ├── flow_dir_d8_1m_ks.tif          # D8 flow direction grid (ESRI 1–128)
        ├── flow_accum_base_1m_ks.tif      # Base flow accumulation (pre-threshold)
        ├── watermask_ks.tif               # Binary water mask (1 = water)
        ├── stream_seed_points.geojson     # Candidate outlets / pour-points
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

💦 Core Hydrology Datasets

Product	File	Description	Source	Units	Format
Filled DEM	dem_filled_1m_ks.tif	1 m LiDAR DEM with sink filling for hydrologic continuity	KS LiDAR / USGS 3DEP	m	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	Downslope pointer grid (ESRI D8; 1–128)	Derived (WhiteboxTools)	int	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation prior to stream thresholding	Derived (WhiteboxTools)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary mask fused from NLCD water and NHD hydrography	USGS / DASC / Derived	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate outlets / pour-points for basins & QA	Derived	n/a	GeoJSON

⸻

🧩 STAC Metadata

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "description": "D8 pointer grid derived from hydro-conditioned 1 m DEM.",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "processing:steps": ["FillDepressions", "D8Pointer"],
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./flow_dir_d8_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "metadata": {
      "href": "./metadata/flow_dir_d8_1m_ks.json",
      "type": "application/json",
      "roles": ["metadata"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}

⸻

⚙️ Processing Workflow

flowchart TD
  A["Raw DEMs\n(1 m / 10–30 m)"] --> B["Fill Depressions\n(WhiteboxTools)"]

  %% Primary hydrology rasters
  B --> C["D8 Flow Direction\n(D8Pointer)"]
  B --> D["D8 Flow Accumulation\n(D8FlowAccumulation)"]

  %% Seed points from accumulation (threshold logic)
  C & D --> E["Seed Point Extraction\n(threshold logic)"]

  %% Water mask fusion
  F["NLCD Water\n+ NHD Hydrography"] --> G["Water Mask\n(GDAL Calc)"]

  %% Reprojection and COG are explicit, then QC
  B & C & D & E & G --> H["Reproject to EPSG:4326\n(GDAL)"]
  H --> I["Convert to COG\n(rio cogeo)"]
  I --> J["QC & Visual Check\n(QGIS vs NHD)"]

  %% Metadata & integrity
  I --> K["Emit STAC Items\n(STAC 1.0)"]
  I --> L["Compute Checksums\n(.sha256)"]
  K & L --> M["Ready for CI\n(Validate STAC • Verify hashes)"]
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
Integrity	.sha256 file for each artifact (verified in CI)
Metadata	STAC 1.0 schema validation (make stac-validate)
Pipeline	Rebuild with make hydrology or make validate-hydro
Environment	Docker toolchain (GDAL + WhiteboxTools + Python)
QA/QC	Visual inspection in QGIS; compare streams vs NHD

⸻

🧠 Contributing
	1.	Add new COG or GeoJSON outputs.
	2.	Create STAC JSON in metadata/ and checksum in checksums/.
	3.	Write DERIVATION.md — inputs, tools/versions, parameters.
	4.	Validate locally → make validate-hydro.
	5.	Open a PR with sources, licenses, screenshots (optional).

All new data must pass STAC + checksum validation before merge.

⸻

📖 References

• WhiteboxTools — https://www.whiteboxgeo.com/manual/wbt_book/hydro.html
• TauDEM — https://hydrology.usu.edu/taudem
• GDAL — https://gdal.org
• USGS NHD — https://www.usgs.gov/national-hydrography
• Kansas DASC Hub — https://hub.kansasgis.org
• STAC 1.0 Spec — https://stacspec.org
• MCP Docs — docs/standards/

⸻

<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>
```
