
⸻

🏔️ KANSAS FRONTIER MATRIX — TERRAIN SOURCE MANIFESTS

data/sources/terrain/

MISSION: Catalog, validate, and preserve all external terrain and elevation data sources that form the topographic backbone of the Kansas Frontier Matrix (KFM) — powering hydrology, landcover, hazard modeling, and temporal storytelling across Kansas and beyond.

⸻



⸻

📚 OVERVIEW

The data/sources/terrain/ directory defines every terrain data source ingested into the KFM ecosystem, including:
	•	🛰️ USGS 3DEP national elevation datasets
	•	🗺️ Kansas LiDAR mosaics from DASC
	•	🌎 Global DEM baselines (SRTM, Copernicus)
	•	🧭 Derivative bases for slope, aspect, and hillshade generation

Each JSON manifest is validated against data/sources/schema/source.schema.json
and used by ETL pipelines to automate download, reprojection, and provenance capture.

⸻

🗂️ DIRECTORY LAYOUT

data/sources/terrain/
├── README.md
├── ks_lidar_2018_2020.json        # Kansas LiDAR DEM collection (DASC)
└── usgs_3dep_dem.json             # USGS 3DEP nationwide elevation model

Tip: Each .json manifest contains unique IDs, licensing, temporal coverage, and links to its STAC entry, ensuring reproducibility across KFM workflows.

⸻

🧩 EXAMPLE MANIFEST — ks_lidar_2018_2020.json

{
  "id": "ks_lidar_2018_2020",
  "title": "Kansas Statewide LiDAR DEM (2018–2020)",
  "provider": "Kansas Data Access & Support Center (DASC)",
  "description": "1-meter LiDAR-derived elevation data for Kansas, collected between 2018 and 2020.",
  "endpoint": "https://kansasgis.org/lidar/data/",
  "access_method": "HTTP download",
  "license": "CC-BY 4.0",
  "data_type": "raster",
  "format": "GeoTIFF",
  "spatial_coverage": "Kansas, USA",
  "temporal_coverage": "2018–2020",
  "update_frequency": "One-time collection",
  "last_verified": "2025-10-13",
  "linked_pipeline": "terrain_pipeline.py",
  "notes": "Primary DEM source for high-resolution terrain analysis."
}


⸻

🧭 SYSTEM CONTEXT (MERMAID DIAGRAM)

flowchart TD
  A["External Terrain Data\n(USGS · DASC · NASA)"] --> B["Source Manifests\n`data/sources/terrain/*.json`"]
  B --> C["ETL Pipelines\n`src/pipelines/terrain_pipeline.py`"]
  C --> D["Processed DEMs\n`data/processed/terrain/`"]
  D --> E["Derivative Layers\nSlope · Aspect · Hillshade"]
  D --> F["Hydrology Inputs\nFlow Direction · Accumulation"]
  D --> G["STAC Metadata\n`data/stac/collections/terrain.json`"]
  F --> H["Knowledge Graph\nTerrain ↔ Hydrology Relations"]
%%END OF MERMAID%%


⸻

⚙️ TERRAIN SOURCE SUMMARY

Manifest File	Provider	Description	Coverage	Format	Verified
ks_lidar_2018_2020.json	Kansas DASC	1 m LiDAR DEM mosaic for Kansas	Kansas	GeoTIFF	✅ 2025-10-13
usgs_3dep_dem.json	USGS	National 1 m LiDAR DEM (3DEP)	Continental US	GeoTIFF	✅ 2025-10-13


⸻

🧾 ETL INTEGRATION

Pipeline: src/pipelines/terrain_pipeline.py
Target Directory: data/processed/terrain/

Workflow Steps:
	1.	✅ Validate manifests (make sources-validate)
	2.	🌐 Fetch DEMs via HTTP or API
	3.	📏 Reproject to EPSG:3857
	4.	🧮 Generate COGs, hillshade, slope, and aspect
	5.	🗂️ Register outputs → STAC & checksum directories

⸻

🧪 VALIDATION & CI/CD

python src/utils/validate_sources.py data/sources/terrain/ \
  --schema data/sources/schema/source.schema.json

Makefile Targets

make terrain-sources
make terrain-validate

CI Automation
	•	Schema validation
	•	URL & license verification
	•	Auto-changelog generation
	•	Provenance validation between STAC and source manifests

⸻

🧩 PROVENANCE CHAIN

Component	Role
data/raw/terrain/	Immutable elevation data archives
data/processed/terrain/	Reprojected, standardized COGs
data/stac/collections/terrain.json	STAC catalog linking processed outputs
data/checksums/terrain/	SHA-256 integrity verification
src/pipelines/terrain_pipeline.py	Automated ingestion + preprocessing pipeline


⸻

🧠 MCP COMPLIANCE SUMMARY

MCP Principle	Implementation Example
Documentation-first	Terrain datasets documented in versioned JSON manifests.
Reproducibility	Deterministic ETL + checksum validation.
Open Standards	JSON Schema · STAC 1.0 · GeoTIFF COG.
Provenance	Linked raw → processed → derivative layers.
Auditability	SHA-256 + CI logs + schema validation reports.


⸻

🤖 AI INTEGRATION

AI agents index these manifests to:
	•	Detect terrain provider entities (USGS, DASC)
	•	Link terrain → hydrology → hazard layers
	•	Predict DEM updates + topographic evolution

⸻

🧾 CHANGELOG

Version	Date	Highlights
v1.2.0	2025-10-13	Added AI integration, validation section, large-title format.
v1.1.0	2025-10-12	Expanded documentation, CI references, updated examples.
v1.0.0	2025-10-04	Initial terrain source manifest directory.


⸻

🏷️ VERSION BLOCK

Component: data/sources/terrain/README.md
SemVer: 1.2.0
Spec Dependencies: MCP v1.0 · STAC 1.0
Last Updated: 2025-10-13
Maintainer: @bartytime4life


⸻

💬 KANSAS FRONTIER MATRIX

“All stories rise from the ground — and all ground begins with terrain.”

📍 data/sources/terrain/
Core elevation source registry powering the Kansas Frontier Matrix geospatial foundation.

⸻