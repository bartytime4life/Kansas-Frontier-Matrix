<div align="center">


💧 Kansas Frontier Matrix — Processed Hydrology Data

data/processed/hydrology/

Mission: Preserve validated hydrologic base surfaces — hydro-conditioned DEMs, D8 flow direction,
base flow accumulation, water masks, and seed points — forming the foundation for stream networks,
watershed delineations, and flood-risk modeling across Kansas.

</div>



⸻

📚 Table of Contents
	•	🌊 Overview
	•	🧱 Directory Layout
	•	💦 Core Hydrology Datasets
	•	🧩 STAC Metadata
	•	⚙️ Processing Workflow
	•	🔁 Reproducibility & Validation
	•	🧠 Contributing
	•	📖 References

⸻

🌊 Overview

This directory stores processed hydrologic surfaces and layers generated from
DEM preprocessing and flow-routing workflows.

These are the intermediate, validated surfaces used to derive
flow accumulation, stream extraction, basin segmentation, and flood simulations.

Sources: LiDAR 1 m DEMs, historical 10–30 m DEMs, and auxiliary hydrology from USGS NHD, NOAA, and Kansas DASC.
Formats: Cloud-Optimized GeoTIFF (COG) in EPSG:4326; vectors in GeoJSON.
Catalog: Indexed via STAC under data/stac/items/hydro_*.

⸻

🧱 Directory Layout

data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif           # Hydro-conditioned DEM (sink-filled)
        ├── flow_dir_d8_1m_ks.tif          # D8 flow direction grid
        ├── flow_accum_base_1m_ks.tif      # Base flow accumulation
        ├── watermask_ks.tif               # Binary water mask (1 = water)
        ├── stream_seed_points.geojson     # Outlets & pour-points
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
Filled DEM	dem_filled_1m_ks.tif	1 m LiDAR DEM after hydrologic sink filling	KS LiDAR / USGS 3DEP	meters	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	Downslope pointer grid (ESRI D8; 1–128)	Derived (WBT)	integer	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation prior to thresholding	Derived (WBT)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary raster (NLCD + NHD fusion)	USGS / DASC	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate outlets / pour points	Derived	n/a	GeoJSON


⸻

🧩 STAC Metadata

Each layer includes a STAC 1.0 JSON with full provenance and lineage.

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
  C & D --> E["Seed Points (threshold logic)"]
  F["NLCD + NHD"] --> G["Water Mask (GDAL calc)"]
  B & C & D & E & G --> H["Reproject + COG (rio cogeo)"]
  H --> I["STAC Items + Checksums"]
<!-- END OF MERMAID -->

Example CLI

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
Pipeline	Rebuild via make hydrology or make validate-hydro
Environment	Docker container (GDAL + WhiteboxTools + Python)
QA/QC	Visual check in QGIS vs USGS NHD baseline


⸻

🧠 Contributing

1️⃣ Add new COG / GeoJSON outputs.
2️⃣ Create metadata → metadata/ and checksum → checksums/.
3️⃣ Write DERIVATION.md (includes inputs, tools, parameters).
4️⃣ Validate → make validate-hydro.
5️⃣ Submit PR with sources, licenses, and visual examples.

All new data must pass STAC + checksum validation before merge.

⸻

📖 References
	•	WhiteboxTools: whiteboxgeo.com/manual/wbt_book/hydro.html
	•	TauDEM: hydrology.usu.edu/taudem
	•	GDAL: gdal.org
	•	USGS NHD: usgs.gov/national-hydrography
	•	Kansas DASC Hub: hub.kansasgis.org
	•	STAC Spec 1.0: stacspec.org
	•	MCP Docs: docs/standards/

⸻


<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>


✅ Now all header sizes, div spacing, and typographic hierarchy match your other finalized KFM markdowns — large H2 section headers, consistent horizontal rules, and properly scaled emoji titles for uniform rendering on GitHub.
