Got it. Here’s a minimal, “safe-mode”, fully working README.md that renders on GitHub end-to-end.
No front-matter, no HTML, no nested fences, no brittle characters — and the Mermaid block uses <br/>, explicit edges, and sits flush-left.

Paste this file as-is:

⸻

💧 Kansas Frontier Matrix — Processed Hydrology Data

Flow · Terrain · Reproducibility — Hydrologic foundation layers for Kansas Frontier Matrix

Build & Deploy •
STAC Validate •
CodeQL •
Trivy •
Docs · MCP •
License

⸻

1) Overview

Processed hydrologic layers produced from DEM conditioning and flow routing. These underpin:
	•	Stream extraction and basin delineation
	•	Flood/runoff modeling and hazard analysis
	•	Watershed and terrain morphology studies
	•	Historical hydrology comparison and climate linkage

Sources: LiDAR 1 m DEMs (Kansas DASC / USGS 3DEP), historic 10–30 m DEMs, NLCD Water, NHD hydrography
Formats: COG GeoTIFF (rasters) • GeoJSON (vectors) • EPSG 4326 (WGS84)
Catalog: STAC items under data/stac/items/hydro_*

⸻

2) Data Products

Product	File	Description	Source	Units	Format
Filled DEM	dem_filled_1m_ks.tif	Hydrologically conditioned/sink-filled DEM (1 m)	KS LiDAR / USGS 3DEP	m	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	D8 pointer grid (1–128)	Derived (WhiteboxTools)	int	COG GeoTIFF
Flow Accumulation	flow_accum_base_1m_ks.tif	Raw accumulation (pre-threshold)	Derived (WhiteboxTools)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary water layer (NLCD + NHD fusion)	USGS / DASC	binary	COG GeoTIFF
Stream Seeds	stream_seed_points.geojson	Candidate outlets / pour points	Derived	n/a	GeoJSON


⸻

3) Directory Layout

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

4) Processing Workflow

flowchart TD
  A["Raw DEMs<br/>1 m and 10-30 m"] --> B["Fill Depressions<br/>WhiteboxTools FillDepressions"]
  B --> C["D8 Flow Direction<br/>WhiteboxTools D8Pointer"]
  B --> D["D8 Flow Accumulation<br/>WhiteboxTools D8FlowAccumulation"]
  C --> E["Seed Point Extraction<br/>Threshold logic"]
  D --> E["Seed Point Extraction<br/>Threshold logic"]
  F["NLCD Water and NHD Hydrography"] --> G["Water Mask<br/>GDAL Calc"]
  B --> H["Reproject to EPSG 4326<br/>GDAL Warp"]
  C --> H["Reproject to EPSG 4326<br/>GDAL Warp"]
  D --> H["Reproject to EPSG 4326<br/>GDAL Warp"]
  E --> H["Reproject to EPSG 4326<br/>GDAL Warp"]
  G --> H["Reproject to EPSG 4326<br/>GDAL Warp"]
  H --> I["Convert to COG<br/>rio cogeo create"]
  I --> J["Visual QC and Validation<br/>QGIS vs NHD"]
  I --> K["Emit STAC Items<br/>STAC 1.0"]
  I --> L["Compute Checksums<br/>SHA-256"]
  K --> M["CI Validation<br/>STAC Validate and Hash Verify"]
  L --> M["CI Validation<br/>STAC Validate and Hash Verify"]


⸻

5) Example STAC Item

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "license": "CC-BY-4.0"
  },
  "assets": {
    "data": {
      "href": "./flow_dir_d8_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}


⸻

6) Reproducibility and Validation
	•	Integrity: sha256sum -c checksums/*.sha256 (CI verifies)
	•	STAC Schema: make stac-validate
	•	Pipeline: make hydrology or make validate-hydro
	•	Environment: Docker (GDAL, WhiteboxTools, Python)
	•	QA/QC: Visual cross-check in QGIS vs NHD

⸻

7) Contributing
	1.	Add new COG/GeoJSON outputs to this folder.
	2.	Create matching STAC JSON under metadata/ and SHA-256 in checksums/.
	3.	Record inputs, params, and versions in DERIVATION.md.
	4.	Run make validate-hydro.
	5.	Open a PR with sources, licenses, and preferably a preview PNG.

Gate: Checksums and STAC validation must pass before merge.

⸻

8) References

GDAL • WhiteboxTools • TauDEM • USGS NHD • Kansas DASC Geoportal • STAC 1.0 • MCP docs

⸻

If this still doesn’t render the Mermaid, you have a fence mismatch elsewhere in the file (or the block is nested in a list/table). In that case, paste the whole README and I’ll fix the exact fence that’s killing it.
