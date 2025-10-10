<div align="center">

💧 **Kansas Frontier Matrix — Processed Hydrology Data**  
`data/processed/hydrology/`

**Mission:** Maintain validated **hydrologic base surfaces** — sink-filled DEMs, D8 flow direction,  
flow accumulation, water masks, and seed points — that form the backbone of stream networks,  
watershed boundaries, and flood-risk modeling across Kansas.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC-BY%204.0-green)](../../../LICENSE)
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

This directory contains **processed hydrologic surfaces and layers** created through DEM conditioning  
and flow-routing routines. These are the intermediate datasets that support **flow accumulation, stream  
extraction, basin segmentation,** and **flood-risk modeling** throughout Kansas.

**Sources** — LiDAR 1 m DEMs, historical 10–30 m DEMs, and auxiliary hydrology from **USGS NHD**,  
**NOAA**, and **Kansas DASC**.  
**Formats** — Cloud-Optimized GeoTIFF (COG) in EPSG 4326; vector data in GeoJSON.  
**Catalog** — Indexed under `data/stac/items/hydro_*`.

⸻

🧱 **Directory Layout**

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

💦 Core Hydrology Datasets

Product	File	Description	Source	Units	Format
Filled DEM	dem_filled_1m_ks.tif	1 m LiDAR DEM with sink filling	KS LiDAR / USGS 3DEP	m	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	D8 pointer grid (1–128) for downslope flow	Derived (WBT)	int	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation prior to thresholding	Derived (WBT)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary mask (NLCD + NHD fusion) 1 = water	USGS / DASC	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate outlets / pour points	Derived	n/a	GeoJSON

⸻

🧩 STAC Metadata

Example Item (flow_dir_d8_1m_ks.json):

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
  A["Raw DEMs (1 m / 10–30 m)"] --> B["Fill Depressions\n(WhiteboxTools)"]
  B --> C["D8 Flow Direction\n(D8Pointer)"]
  B --> D["D8 Flow Accumulation\n(D8FlowAccumulation)"]
  C & D --> E["Seed Point Extraction\n(threshold logic)"]
  F["NLCD Water +\nNHD Hydrography"] --> G["Water Mask\n(GDAL Calc)"]
  B & C & D & E & G --> H["Reproject + COG\n(rio cogeo)"]
  H --> I["STAC Items\n+ Checksums"]
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
Integrity	.sha256 hash verification in CI
Metadata	STAC 1.0 schema validation (make stac-validate)
Pipeline	make hydrology or make validate-hydro
Environment	Docker (GDAL + WhiteboxTools + Python)
QA/QC	Visual inspection in QGIS vs USGS NHD baseline

⸻

🧠 Contributing

1️⃣ Add new COG or GeoJSON outputs.
2️⃣ Create STAC metadata → metadata/ and checksum → checksums/.
3️⃣ Add DERIVATION.md detailing inputs, tools, and parameters.
4️⃣ Validate locally → make validate-hydro.
5️⃣ Submit PR with sources, licenses, and visual examples.

All new data must pass STAC and checksum validation before merge.

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
