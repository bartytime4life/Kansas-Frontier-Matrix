<div align="center">

# ⚠️ Kansas Frontier Matrix — Hazard Derivative Metadata Summary  
`data/derivatives/metadata/metadata/hazards/`

**Purpose:** Provide a domain-level registry of all **hazard derivative metadata** entries  
(tornado tracks, floods, droughts, disaster composites, etc.) under the Kansas Frontier Matrix (KFM)  
for provenance tracking, validation, and STAC cross-linkage.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains the **hazard domain summary registry**, aggregating all hazard derivative metadata from  
`data/derivatives/hazards/metadata/`. It lists core datasets (tornado, flood, drought, storm reports, etc.)  
and links them to their respective **source manifests**, **checksums**, and **STAC items**.

This summary ensures:
- ✅ Domain-level metadata completeness  
- 🔗 Consistent provenance across ETL → STAC → Graph workflows  
- 🧾 Easy validation in CI and graph synchronization  
- 🌍 Unified hazard layer discovery in API and UI  

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Hazard Metadata JSONs\n(data/derivatives/hazards/metadata/)"] --> B["Hazard Summary JSON\n(data/derivatives/metadata/metadata/hazards/)"]
  B --> C["Derivative Metadata Registry\n(data/derivatives/metadata/metadata/)"]
  C --> D["STAC Catalog\n(data/stac/)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

hazards/
├── hazards_metadata_summary.json
└── README.md

This directory summarizes all hazard derivative datasets registered within the KFM system.

⸻

🧾 Summary JSON Schema (Example)

{
  "id": "hazards_metadata_summary",
  "title": "Hazard Derivative Metadata Summary",
  "description": "Aggregated summary of hazard derivative datasets across Kansas Frontier Matrix.",
  "domain": "hazards",
  "entries": [
    {
      "id": "tornado_tracks_1950_2024",
      "title": "Kansas Tornado Tracks (1950–2024)",
      "path": "../../../../hazards/metadata/tornado_tracks_1950_2024.json",
      "temporal_range": "1950–2024",
      "variables": ["tornado_path", "EF_rating"],
      "format": "GeoJSON",
      "source": "../../../../sources/noaa_spc_tornadoes.json",
      "stac_item": "../../../../stac/items/tornado_tracks_1950_2024.json"
    },
    {
      "id": "flood_zones_1990_2025",
      "title": "FEMA Flood Zones (1990–2025)",
      "path": "../../../../hazards/metadata/flood_zones_1990_2025.json",
      "temporal_range": "1990–2025",
      "variables": ["flood_extent"],
      "format": "COG",
      "source": "../../../../sources/fema_flood_zones.json",
      "stac_item": "../../../../stac/items/flood_zones_1990_2025.json"
    },
    {
      "id": "drought_index_annual_ks",
      "title": "Kansas Drought Severity Index (1895–2024)",
      "path": "../../../../hazards/metadata/drought_index_annual_ks.json",
      "temporal_range": "1895–2024",
      "variables": ["drought_index"],
      "format": "Parquet",
      "source": "../../../../sources/noaa_ncei_drought.json",
      "stac_item": "../../../../stac/items/drought_index_annual_ks.json"
    }
  ],
  "count": 3,
  "license": "CC-BY-4.0",
  "last_updated": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Update this JSON when adding or modifying any hazard derivative metadata in data/derivatives/hazards/metadata/.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
⚠️ Hazard Metadata	data/derivatives/hazards/metadata/	Individual hazard derivative metadata files.
🧾 Domain Summary (This)	data/derivatives/metadata/metadata/hazards/	Aggregated hazard metadata index.
🧮 Global Registry	data/derivatives/metadata/metadata/	Cross-domain metadata registry (climate, hydrology, hazards, landcover).
🗺️ STAC Catalog	data/stac/	Links each hazard dataset to its temporal/spatial asset metadata.
🧠 Knowledge Graph	(Neo4j)	Represents domain relationships between events and datasets.


⸻

🧠 Usage in the Pipeline
	•	ETL Step: Once hazard derivatives are generated, metadata summaries are automatically compiled into this folder.
	•	Validation: The CI workflow stac-validate.yml ensures every hazard derivative metadata file is indexed here.
	•	Graph Load: The registry allows Neo4j to populate “Hazard Dataset Family” nodes linking events, maps, and timespans.
	•	API & UI: Used by the web UI to render available hazard datasets dynamically on map and timeline interfaces.

⸻

🧱 Best Practices

Category	Guideline
✅ Completeness	Include every file in hazards/metadata/ in this registry.
🔗 Cross-Referencing	Maintain valid relative paths to metadata, checksum, and STAC files.
🧾 Licensing	Default to CC-BY-4.0 unless restricted by source.
🕓 Versioning	Update last_updated whenever datasets change.
🧪 Validation	Run make validate to ensure registry aligns with STAC and global derivative metadata.


⸻

🔒 Reproducibility & MCP Alignment

This summary upholds KFM’s Master Coder Protocol standards:
	•	Single authoritative source for all hazard derivatives.
	•	Links all derivative assets to their provenance and STAC entries.
	•	Provides full lineage and audit trail from raw data → processed layers → registry.

It ensures that every hazard dataset can be verified, reproduced, and semantically aligned across MCP, STAC, and Neo4j layers.

⸻

🧱 Related Documentation
	•	data/derivatives/hazards/metadata/README.md — detailed hazard metadata schema
	•	data/derivatives/metadata/metadata/README.md — global derivative metadata registry
	•	data/stac/README.md — STAC catalog and validation
	•	docs/architecture.md — ETL and metadata provenance architecture

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial hazard metadata summary for domain-level registry.