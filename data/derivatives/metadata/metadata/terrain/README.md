<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Derivative Metadata Summary  
`data/derivatives/metadata/metadata/terrain/`

**Purpose:** Provide an aggregated **terrain domain registry** summarizing all topographic, elevation, and geomorphologic  
derivative metadata files within KFM — unifying hillshades, slope maps, DEMs, and contour layers into a single validated summary.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory defines the **terrain domain summary registry** for all metadata describing KFM’s topographic and elevation derivatives.  
It consolidates metadata from `data/derivatives/terrain/metadata/` and records provenance links, STAC references, and ETL lineage  
for all terrain layers, including:

- 🗺️ Digital Elevation Models (DEMs) — LiDAR or 3DEP based  
- 🌄 Hillshade & slope rasters  
- 🧭 Contour line vectors  
- 🪨 Terrain classification and geomorphology models  

The summary enables STAC cross-validation, CI checks, and Knowledge Graph indexing for all terrain datasets in KFM.

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Terrain Metadata JSONs\n(data/derivatives/terrain/metadata/)"] --> B["Terrain Summary JSON\n(data/derivatives/metadata/metadata/terrain/)"]
  B --> C["Derivative Metadata Registry\n(data/derivatives/metadata/metadata/)"]
  C --> D["STAC Catalog\n(data/stac/)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

terrain/
├── terrain_metadata_summary.json
└── README.md

This summary JSON acts as the authoritative domain-level manifest for all processed terrain derivatives,
linking each dataset to its metadata file, checksum, and STAC item.

⸻

🧾 Summary JSON Schema (Example)

{
  "id": "terrain_metadata_summary",
  "title": "Terrain Derivative Metadata Summary",
  "description": "Aggregated metadata summary for terrain and topographic derivative datasets across Kansas Frontier Matrix.",
  "domain": "terrain",
  "entries": [
    {
      "id": "dem_1m_ks_lidar",
      "title": "Kansas 1m LiDAR Digital Elevation Model (USGS 3DEP)",
      "path": "../../../../terrain/metadata/dem_1m_ks_lidar.json",
      "temporal_range": "2018–2023",
      "variables": ["elevation"],
      "format": "COG",
      "source": "../../../../sources/usgs_3dep_dem.json",
      "stac_item": "../../../../stac/items/dem_1m_ks_lidar.json"
    },
    {
      "id": "hillshade_ks_1m",
      "title": "Hillshade Raster (Kansas 1m DEM-derived)",
      "path": "../../../../terrain/metadata/hillshade_ks_1m.json",
      "temporal_range": "Derived from DEM (2018–2023)",
      "variables": ["illumination"],
      "format": "COG",
      "source": "../../../../sources/usgs_3dep_dem.json",
      "stac_item": "../../../../stac/items/hillshade_ks_1m.json"
    },
    {
      "id": "slope_map_ks",
      "title": "Slope Map of Kansas (Degrees)",
      "path": "../../../../terrain/metadata/slope_map_ks.json",
      "temporal_range": "Derived from DEM (2018–2023)",
      "variables": ["slope"],
      "format": "COG",
      "source": "../../../../sources/usgs_3dep_dem.json",
      "stac_item": "../../../../stac/items/slope_map_ks.json"
    }
  ],
  "count": 3,
  "license": "CC-BY-4.0",
  "last_updated": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Always synchronize entries when new terrain metadata files are added in
data/derivatives/terrain/metadata/, and update the count and last_updated fields.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🏔️ Terrain Metadata	data/derivatives/terrain/metadata/	Individual terrain metadata files (DEM, slope, hillshade).
🧾 Domain Summary (This)	data/derivatives/metadata/metadata/terrain/	Aggregated summary for the terrain domain.
🧮 Global Registry	data/derivatives/metadata/metadata/	Central registry linking all domain summaries.
🗺️ STAC Catalog	data/stac/	Global index for spatial-temporal assets.
🧠 Knowledge Graph	(Neo4j)	Semantic mapping of terrain datasets and their relationships.


⸻

🧠 Usage in the Pipeline
	•	ETL Step: Once terrain derivatives are created, the pipeline automatically generates or updates this summary JSON.
	•	Validation: CI workflows confirm each metadata file is registered and matches its STAC and checksum.
	•	Graph Load: Neo4j importer uses this summary to link terrain assets to places, elevation attributes, and events.
	•	Frontend Discovery: Enables map viewers to query all terrain layers available in KFM.

⸻

🧱 Best Practices

Category	Guideline
✅ Completeness	Include all files from terrain/metadata/.
🔗 Cross-Referencing	Maintain valid relative paths to metadata, checksums, and STAC items.
🧾 Licensing	Default license: CC-BY-4.0.
🕓 Versioning	Update last_updated and increment count when datasets are modified.
🧪 Validation	Run make validate or rely on CI STAC checks for consistency.


⸻

🔒 Reproducibility & MCP Alignment

The terrain metadata summary aligns with Master Coder Protocol (MCP) principles by:
	•	Documenting all terrain derivatives in one machine-readable manifest.
	•	Linking datasets through STAC/DCAT metadata and checksum verification.
	•	Enabling reproducibility across ETL, Knowledge Graph, and UI layers.

This ensures topographic data — from LiDAR-derived DEMs to slope and hillshade models — remain traceable, validated, and reusable.

⸻

🧱 Related Documentation
	•	data/derivatives/terrain/metadata/README.md — terrain metadata schema
	•	data/derivatives/metadata/metadata/README.md — global derivative metadata registry
	•	data/stac/README.md — STAC catalog integration and validation
	•	docs/architecture.md — ETL and provenance workflow design

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of terrain metadata summary for domain-level registry.