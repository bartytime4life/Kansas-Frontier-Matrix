<div align="center">


💧 Kansas-Frontier-Matrix — Processed Hydrology Data

data/processed/hydrology/

Mission: Preserve validated hydrologic base surfaces—hydro-conditioned DEMs, D8 flow direction, base flow accumulation, water masks, and seed points—used to derive stream networks, basins, flood pathways, and other hazards across Kansas.

</div>



⸻

📚 Table of Contents
	•	Overview
	•	Directory Layout
	•	Core Hydrology Datasets
	•	STAC & Provenance
	•	Processing Workflow
	•	Visualization Hints
	•	Reproducibility & Validation
	•	Contributing New Hydrology Data
	•	References

⸻

🌊 Overview

This folder stores processed hydrologic base layers generated from DEM pre-processing and flow routing.
They serve as inputs for downstream products (see data/derivatives/hydrology/) such as:
	•	Flow accumulation thresholds → stream networks
	•	Seeds + flow dir/accum → watershed/basin delineations
	•	Hydro DEM + water mask → flood extent prototyping & hydraulic pre-conditioning

Sources: LiDAR-derived DEM (1 m), historical topo DEMs (10–30 m), and auxiliary hydrology from USGS NHD, NOAA, and Kansas DASC.
Formats: Cloud-Optimized GeoTIFF (COG) for rasters, GeoJSON for vectors, EPSG:4326 (WGS84).
Catalog: Indexed in STAC under data/stac/items/*.

⸻

🧱 Directory Layout

data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif           # Hydro-conditioned DEM (sink-filled)
        ├── flow_dir_d8_1m_ks.tif          # D8 flow direction grid
        ├── flow_accum_base_1m_ks.tif      # Base (pre-threshold) accumulation
        ├── watermask_ks.tif               # Binary water mask (1=water, 0=land)
        ├── stream_seed_points.geojson     # Outlets / pour-points
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
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	Downslope flow direction codes (ESRI D8; 1–128)	Derived (WBT)	integer	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw cell-based accumulation prior to any stream thresholding	Derived (WBT)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary water mask fused from NLCD + hydrography (1=water, 0=land)	USGS / DASC / Derived	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate outlets / pour-points for basin segmentation & QC of drainage	Derived	n/a	GeoJSON

Note: Where historical DEM resolutions are used (10–30 m), filenames follow the same pattern with a _10m/_30m suffix.

⸻

🧩 STAC & Provenance

All files are registered as STAC Items with lineage, software, parameters, and licensing. Example:

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "description": "D8 pointer grid from hydro-conditioned 1 m DEM.",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "processing:steps": ["FillDepressions", "D8Pointer"],
    "parameters": { "fill": { "flat_treatment": "breach_or_fill" }, "d8": { "force_four": false } },
    "mcp_provenance": "sha256:4be51c…",
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "license": "CC-BY-4.0"
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
  A["Raw DEM (1 m / 10–30 m)\nLiDAR / topo"] --> B["Fill sinks\n(WhiteboxTools: FillDepressions)"]
  B --> C["Flow direction (D8)\n(WhiteboxTools: D8Pointer)"]
  B --> D["Flow accumulation\n(WhiteboxTools: D8FlowAccumulation)"]
  E["Water sources\nNLCD water, NHD/GNIS"] --> F["Water mask fusion\nGDAL calc · logical OR"]
  C --> G["Seed points\n(threshold & outlet logic)"]
  D --> G
  B & C & D & F & G --> H["Reproject + COG\n(rio cogeo)"]
  H --> I["STAC Items + checksums\n(data/stac/items/* , *.sha256)"]
<!-- END OF MERMAID -->

Example CLI (reproducible)

# 1) Hydrologic conditioning (fill/breach)
whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif

# 2) D8 pointer
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_dir_d8_1m_ks.tif

# 3) D8 flow accumulation
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accum_base_1m_ks.tif

# 4) Water mask from NLCD + hydrography
gdal_calc.py -A nlcd_water_ks.tif -B nhd_water_ks.tif \
  --outfile=watermask_ks.tif --calc="((A>0) | (B>0)).astype(uint8)"

# 5) Seed points (choose threshold by scale)
python tools/hydro/seed_points.py --accum flow_accum_base_1m_ks.tif --threshold 500

# 6) COG conversion & STAC emit are handled by Make targets


⸻

🎨 Visualization Hints
	•	Flow Dir (D8) — categorical scheme (e.g., 8 hues for the 8 directions; 0 or NoData transparent).
	•	Flow Accumulation — log stretch; suggested ramp: #f7fbff → #6baed6 → #08519c (blue scale).
	•	Water Mask — 1 = #2b8cbe (water), 0 = transparent.
	•	Filled DEM — hillshade for QC; keep grayscale underlays subtle to emphasize flow features.

⸻

🔁 Reproducibility & Validation

Make targets

make hydrology           # rebuild hydrologic processed layers
make validate-hydro      # validate STAC + checksums
make stac-validate       # run STAC schema checks repo-wide

Integrity & CI
	•	Checksums: .sha256 for each artifact (verified in CI).
	•	STAC Validation: All items validated against STAC 1.0 schema in CI.
	•	Containers: Workflows run in Docker images with GDAL + WhiteboxTools + Python pinned by digest.
	•	QC: Visual QA in QGIS; compare extracted streams vs. NHD high-res; spot-check sinks & flats.

Caveats
	•	Flat prairie zones may require breach-depressions or least-cost carving; document chosen method in metadata/*.json.
	•	When mixing 1 m and 10–30 m DEMs, maintain separate products or resample explicitly—record resampling kernel & scale in metadata.

⸻

🧠 Contributing New Hydrology Data
	1.	Place files (COG GeoTIFF or GeoJSON) in this folder with clear, consistent names.
	2.	Create metadata in metadata/ (STAC-aligned JSON) and a .sha256 in checksums/.
	3.	Add DERIVATION.md summarizing:
	•	Inputs (derived_from), sources & licenses
	•	Tools & versions (e.g., WBT 2.2.0, GDAL 3.8.x)
	•	Key params (e.g., accumulation thresholds, breach/fill options)
	4.	Validate locally

make validate-hydro

	5.	Open a PR including:
	•	Purpose & intended derivatives (streams, basins, flood work)
	•	STAC snippet(s) and any style guidance (ramps, legends)
	•	Screenshots/GIFs for reviewer QC (optional but helpful)

⸻

📖 References
	•	WhiteboxTools (Hydrology): https://www.whiteboxgeo.com/manual/wbt_book/hydro.html
	•	TauDEM: https://hydrology.usu.edu/taudem/
	•	GDAL: https://gdal.org/
	•	USGS National Hydrography Dataset (NHD): https://www.usgs.gov/national-hydrography
	•	Kansas DASC GIS Hub: https://hub.kansasgis.org
	•	STAC 1.0 Spec: https://stacspec.org
	•	Project Standards (MCP): docs/standards/

⸻


<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>
