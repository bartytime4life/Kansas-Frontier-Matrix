<div align="center">


🏔️ Kansas Frontier Matrix — Terrain Source Manifests

data/sources/terrain/

“All stories rise from the ground — and all ground begins with terrain.”

</div>



⸻


---
title: "Kansas Frontier Matrix — Terrain Source Manifests"
version: "v1.2.0"
last_updated: "2025-10-13"
authors: ["KFM Terrain & Data Systems Team"]
status: "Stable"
maturity: "Production"
tags: ["terrain", "sources", "stac", "schema", "mcp"]
license: "CC-BY 4.0"
---


⸻

📚 Overview

The data/sources/terrain/ directory catalogs every terrain and elevation data source used by the Kansas Frontier Matrix (KFM) — the foundational layer powering Kansas’s environmental, hydrological, and historical reconstructions.

Sources include:
	•	🛰️ USGS 3DEP — National LiDAR-derived DEM
	•	🗺️ Kansas DASC LiDAR — High-resolution state DEMs
	•	🌎 Global DEM baselines — SRTM, Copernicus, NASADEM
	•	🧭 Derived layers — Hillshade, slope, aspect, accumulation

Each manifest is validated against data/sources/schema/source.schema.json, ensuring every dataset’s provenance, license, and schema are traceable and reproducible.

⸻

🗂️ Directory Layout

data/sources/terrain/
├── README.md
├── ks_lidar_2018_2020.json        # Kansas LiDAR DEM collection (DASC)
└── usgs_3dep_dem.json             # USGS 3DEP nationwide elevation model

Tip: Every JSON manifest specifies its ID, provider, temporal coverage, and links to downstream STAC metadata for provenance tracking.

⸻

🧩 Example Manifest — ks_lidar_2018_2020.json

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

🧭 System Context

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

⚙️ Terrain Source Summary

Manifest File	Provider	Description	Coverage	Format	Verified
ks_lidar_2018_2020.json	Kansas DASC	1 m LiDAR DEM mosaic for Kansas	Kansas	GeoTIFF	✅ 2025-10-13
usgs_3dep_dem.json	USGS	National 1 m LiDAR DEM (3DEP)	Continental US	GeoTIFF	✅ 2025-10-13


⸻

🧾 ETL Integration

Pipeline: src/pipelines/terrain_pipeline.py
Target Directory: data/processed/terrain/

Workflow Steps
	1.	✅ Validate manifests → make sources-validate
	2.	🌐 Fetch DEMs via HTTP or API
	3.	📏 Reproject to EPSG:3857
	4.	🧮 Generate COGs + hillshade + slope + aspect
	5.	🗂️ Register outputs in STAC and checksum directories

⸻

🧪 Validation & CI/CD

python src/utils/validate_sources.py data/sources/terrain/ \
  --schema data/sources/schema/source.schema.json

Makefile Targets

make terrain-sources
make terrain-validate

CI Automation
	•	JSON schema conformance
	•	URL & license verification
	•	Auto-changelog generation
	•	Provenance consistency between STAC & source manifests

⸻

🧩 Provenance Chain

Component	Role
data/raw/terrain/	Immutable elevation data archives
data/processed/terrain/	Reprojected, standardized COGs
data/stac/collections/terrain.json	STAC catalog linking processed outputs
data/checksums/terrain/	SHA-256 integrity verification
src/pipelines/terrain_pipeline.py	Automated ingestion + preprocessing pipeline


⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation Example
Documentation-first	Terrain datasets documented in versioned JSON manifests.
Reproducibility	Deterministic ETL + checksum validation.
Open Standards	JSON Schema · STAC 1.0 · GeoTIFF COG.
Provenance	Linked raw → processed → derivative layers.
Auditability	SHA-256 hashes + CI logs + schema reports.


⸻

🤖 AI Integration

AI agents index these manifests to:
	•	Detect terrain provider entities (USGS, DASC)
	•	Link terrain → hydrology → hazard layers
	•	Predict DEM updates and topographic evolution

⸻

🧾 Changelog

Version	Date	Highlights
v1.2.0	2025-10-13	Added AI integration, validation section, and Root Markdown format.
v1.1.0	2025-10-12	Expanded documentation, CI references, and examples.
v1.0.0	2025-10-04	Initial terrain source manifest directory.


⸻

🏷️ Version Block

Component: data/sources/terrain/README.md
SemVer: 1.2.0
Spec Dependencies: MCP v1.0 · STAC 1.0
Last Updated: 2025-10-13
Maintainer: @bartytime4life


⸻


<div align="center">


Kansas Frontier Matrix — “All stories rise from the ground — and all ground begins with terrain.”
📍 data/sources/terrain/ · Core elevation source registry powering KFM’s geospatial foundation.

</div>