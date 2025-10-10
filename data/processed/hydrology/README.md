<div align="center">


💧 Kansas Frontier Matrix — Processed Hydrology Data

data/processed/hydrology/

Mission: Preserve validated hydrologic base surfaces — hydro-conditioned DEMs, D8 flow direction,
base flow accumulation, water masks, and seed points — forming the foundation for stream networks,
watershed delineations, and flood-risk modeling across Kansas.

</div>



⸻

📚 Table of Contents
	•	Overview
	•	Directory Layout
	•	Core Hydrology Datasets
	•	STAC Metadata
	•	Processing Workflow
	•	Reproducibility & Validation
	•	Contributing
	•	References

⸻

🌊 Overview

This directory stores processed hydrologic surfaces and layers generated from
DEM preprocessing and flow-routing routines.

These outputs serve as the base for derivative modeling — flow accumulation, stream extraction,
basin segmentation, and flood simulations — all reproducible via scripted ETL and STAC validation.

Sources: LiDAR-derived 1 m DEMs, historical 10–30 m DEMs, and auxiliary hydrologic datasets
from USGS NHD, NOAA, and Kansas DASC.

All rasters are standardized as Cloud-Optimized GeoTIFFs (COGs) in EPSG:4326 and indexed in
the STAC catalog under data/stac/items/hydro_*.

⸻

🧱 Directory Layout

data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif           # Hydrologically conditioned DEM (sink-filled)
        ├── flow_dir_d8_1m_ks.tif          # D8 flow direction raster
        ├── flow_accum_base_1m_ks.tif      # Base flow accumulation
        ├── watermask_ks.tif               # Binary water mask (1 = water)
        ├── stream_seed_points.geojson     # Outlets & pour points
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
Filled DEM	dem_filled_1m_ks.tif	1 m LiDAR DEM, hydrologically conditioned (sink-filled)	KS LiDAR / USGS 3DEP	meters	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	Downslope pointer grid (ESRI D8; 1–128)	Derived (WBT)	integer	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation before thresholding	Derived (WBT)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary raster (NLCD + NHD fusion)	USGS / DASC	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate outlets / pour points	Derived	n/a	GeoJSON


⸻

🧩 STAC Metadata

All layers are indexed via SpatioTemporal Asset Catalog (STAC 1.0) for discoverability, provenance,
and validation. Example item:

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
  A["Raw DEM (1 m / 10–30 m)"] --> B["Fill Depressions (WhiteboxTools)"]
  B --> C["D8 Flow Direction"]
  B --> D["D8 Flow Accumulation"]
  C & D --> E["Stream Seed Points"]
  F["NLCD + NHD"] --> G["Water Mask Fusion (GDAL calc)"]
  B & C & D & E & G --> H["Reproject + COG (rio cogeo)"]
  H --> I["STAC Items + Checksums"]
<!-- END OF MERMAID -->

Example CLI:

whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_dir_d8_1m_ks.tif
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accum_base_1m_ks.tif
gdal_calc.py -A nlcd_water_ks.tif -B nhd_water_ks.tif \
  --outfile=watermask_ks.tif --calc="((A>0)|(B>0)).astype(uint8)"
python tools/hydro/seed_points.py --accum flow_accum_base_1m_ks.tif --threshold 500

All outputs are reprojected and converted to COG via rio cogeo create.

⸻

🔁 Reproducibility & Validation

Check	Method
Integrity	.sha256 hashes verified in CI
Metadata	STAC 1.0 schema validation (make stac-validate)
Pipeline	Rebuild with make hydrology or make validate-hydro
Environment	Docker container (GDAL + WhiteboxTools + Python)
QA/QC	Visual inspection in QGIS vs USGS NHD baseline


⸻

🧠 Contributing
	1.	Add new processed files (COG / GeoJSON).
	2.	Create matching STAC JSON → metadata/ + checksum → checksums/.
	3.	Document derivation (DERIVATION.md) — inputs, tools, parameters.
	4.	Validate locally → make validate-hydro.
	5.	Submit PR with: sources + licenses + visual examples.

All new data must pass STAC and checksum validation before merge.

⸻

📖 References
	•	WhiteboxTools: whiteboxgeo.com/manual/wbt_book/hydro.html
	•	TauDEM: hydrology.usu.edu/taudem
	•	GDAL: gdal.org
	•	USGS NHD: usgs.gov/national-hydrography
	•	Kansas DASC GIS Hub: hub.kansasgis.org
	•	STAC Spec 1.0: stacspec.org
	•	MCP Docs: docs/standards/

⸻


<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>
