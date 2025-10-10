<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Derivative Metadata  
`data/derivatives/terrain/metadata/`

**Purpose:** Define machine-readable metadata describing **terrain derivative layers**  
(DEMs, hillshades, slope maps, contours) created through the Kansas Frontier Matrix (KFM) ETL pipeline.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata JSON files** describing each processed terrain derivative product  
within the Kansas Frontier Matrix (KFM). These metadata files link derived raster and vector terrain layers  
to their **source datasets**, **checksum manifests**, and **STAC catalog items**, ensuring reproducibility,  
discoverability, and clear provenance.

Terrain derivatives include:
- **DEMs** (Digital Elevation Models)
- **Hillshade rasters**
- **Slope and aspect maps**
- **Contour line GeoJSONs**

Each metadata file conforms to KFM’s MCP-aligned schema and STAC/DCAT standards for interoperability.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Terrain Sources\nUSGS 3DEP · LiDAR · DASC Archive"] --> B["ETL Pipeline\nProcess · Mosaic · Reproject"]
  B --> C["Terrain Derivatives\nDEM · Hillshade · Slope · Contours"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\nSHA-256 manifests"]
  D --> F["STAC Items\nlink to assets + checksums"]
  F --> G["Knowledge Graph\nentity creation + provenance links"]
  G --> H["Web UI\nvisualization via MapLibre + timeline sync"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

metadata/
├── dem_1m_ks_lidar.json
├── hillshade_ks_1m.json
├── slope_map_ks.json
├── contour_ks_10m.json
└── README.md

Each .json metadata file documents an individual terrain product, describing its source lineage,
spatial and temporal coverage, coordinate system, checksum reference, and STAC item linkage.

⸻

🧾 Metadata Schema (JSON Example)

{
  "id": "dem_1m_ks_lidar",
  "title": "Kansas 1m LiDAR Digital Elevation Model (USGS 3DEP)",
  "description": "High-resolution digital elevation model of Kansas derived from USGS 3DEP LiDAR tiles, mosaicked and reprojected to WGS84.",
  "type": "raster",
  "format": "COG",
  "file": "../dem_1m_ks_cog.tif",
  "checksum": "../checksums/dem_1m_ks_cog.tif.sha256",
  "source": "../../../sources/usgs_3dep_dem.json",
  "stac_item": "../../../stac/items/dem_1m_ks_lidar.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "2018-01-01",
    "end": "2023-12-31"
  },
  "variables": [
    {
      "name": "elevation",
      "units": "meters",
      "description": "Elevation above mean sea level (NAVD88)."
    }
  ],
  "license": "Public Domain (USGS)",
  "created": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Update paths and CRS fields after any reprojection or processing step.
Ensure the checksum field matches the correct file in /checksums/.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🏔️ Terrain Metadata (This)	data/derivatives/terrain/metadata/	Documents ETL-produced terrain layers
🧾 Checksums	data/derivatives/terrain/checksums/	Ensures binary integrity of terrain files
🗺️ STAC Catalog	data/stac/	Registers geospatial and temporal metadata
🧠 Knowledge Graph	(Neo4j)	Links terrain datasets with provenance and usage context
⚙️ ETL Pipeline	Makefile + scripts/	Defines processing, mosaicking, and transformation logic


⸻

🧠 Usage in the Pipeline
	•	ETL Step: Each processed raster or vector layer automatically generates a corresponding metadata JSON.
	•	Validation: JSON Schema validation (in CI) ensures required fields and STAC linkage exist.
	•	Graph Load: Metadata attributes populate Neo4j nodes (TerrainLayer class) and relationships to sources.
	•	STAC Reference: The metadata connects to data/stac/items/*.json, allowing discoverability by map viewers.

⸻

🧱 Metadata Best Practices

Category	Guideline
✅ Completeness	Every terrain derivative file must have an associated .json metadata file.
🔗 Linkage	Always link to checksum, STAC item, and source manifest.
🕓 Timestamps	Record both creation and last updated fields in ISO 8601.
📐 Spatial Integrity	Ensure CRS and bounding boxes are accurate post-reprojection.
🧾 Licensing	Reflect data source license (Public Domain or CC).
🧪 Validation	Run make validate or rely on CI stac-validate.yml to ensure compliance.


⸻

🔒 Reproducibility & MCP Alignment

This metadata system exemplifies the Master Coder Protocol principles by:
	•	Documenting each derivative’s full provenance chain (source → ETL → checksum → STAC).
	•	Using open metadata standards (STAC, DCAT, GeoJSON).
	•	Enabling temporal + spatial interoperability across tools and visualizations.
	•	Making all terrain datasets traceable, verifiable, and semantically linked in the KFM knowledge system.

⸻

🧱 Related Documentation
	•	data/derivatives/terrain/checksums/README.md — integrity validation
	•	data/stac/README.md — STAC catalog and item linking
	•	docs/architecture.md — ETL + data lineage architecture overview
	•	docs/sop.md — reproducible workflow procedures

⸻

🗓 Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of terrain metadata schema and examples.