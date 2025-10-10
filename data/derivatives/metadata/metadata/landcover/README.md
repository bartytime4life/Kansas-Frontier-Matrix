<div align="center">

# 🌾 Kansas Frontier Matrix — Landcover Derivative Metadata Summary  
`data/derivatives/metadata/metadata/landcover/`

**Purpose:** Aggregate and summarize all **landcover derivative metadata** entries across the Kansas Frontier Matrix (KFM),  
providing a centralized registry for vegetation, land-use, and surface classification datasets derived through ETL workflows.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains the **domain summary registry** for all landcover derivative metadata JSON files from  
`data/derivatives/landcover/metadata/`.  

It provides a unified reference for:
- 🌿 Landcover change products (e.g., NLCD composites, historical vegetation rasters)  
- 🪵 Ecological layers (e.g., canopy height, biome zones, prairie extent)  
- 🌾 Land-use transformation grids and categorical classification models  

This summary aligns the domain with KFM’s **global derivative metadata registry** and **STAC catalog**, ensuring complete traceability and interoperability.

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Landcover Metadata JSONs\n(data/derivatives/landcover/metadata/)"] --> B["Landcover Summary JSON\n(data/derivatives/metadata/metadata/landcover/)"]
  B --> C["Derivative Metadata Registry\n(data/derivatives/metadata/metadata/)"]
  C --> D["STAC Catalog\n(data/stac/)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

landcover/
├── landcover_metadata_summary.json
└── README.md

Each summary file consolidates all processed landcover derivatives and references their metadata, checksum,
and STAC entries, serving as a complete domain-level manifest for validation and provenance.

⸻

🧾 Summary JSON Schema (Example)

{
  "id": "landcover_metadata_summary",
  "title": "Landcover Derivative Metadata Summary",
  "description": "Aggregated metadata summary of all landcover derivative datasets in KFM.",
  "domain": "landcover",
  "entries": [
    {
      "id": "nlcd_1992_2021",
      "title": "National Land Cover Database (1992–2021, Kansas)",
      "path": "../../../../landcover/metadata/nlcd_1992_2021.json",
      "temporal_range": "1992–2021",
      "variables": ["landcover_class"],
      "format": "COG",
      "source": "../../../../sources/usgs_nlcd.json",
      "stac_item": "../../../../stac/items/nlcd_1992_2021.json"
    },
    {
      "id": "vegetation_zones_1850_ks",
      "title": "Vegetation Zones (1850s, Kansas)",
      "path": "../../../../landcover/metadata/vegetation_zones_1850_ks.json",
      "temporal_range": "1850",
      "variables": ["vegetation_type"],
      "format": "GeoJSON",
      "source": "../../../../sources/kars_historic_veg.json",
      "stac_item": "../../../../stac/items/vegetation_zones_1850_ks.json"
    },
    {
      "id": "landuse_1900_2000_composite",
      "title": "Land Use Composite (1900–2000, Kansas)",
      "path": "../../../../landcover/metadata/landuse_1900_2000_composite.json",
      "temporal_range": "1900–2000",
      "variables": ["landuse_type"],
      "format": "COG",
      "source": "../../../../sources/usda_landuse.json",
      "stac_item": "../../../../stac/items/landuse_1900_2000_composite.json"
    }
  ],
  "count": 3,
  "license": "CC-BY-4.0",
  "last_updated": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Keep all landcover metadata entries synchronized here; update the count and last_updated fields whenever new datasets are added or revised.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🌾 Landcover Metadata	data/derivatives/landcover/metadata/	Individual metadata JSONs describing landcover derivatives.
🧾 Domain Summary (This)	data/derivatives/metadata/metadata/landcover/	Aggregated summary for the landcover domain.
🧮 Global Registry	data/derivatives/metadata/metadata/	Master registry linking all domain summaries.
🗺️ STAC Catalog	data/stac/	Global STAC item registry linking temporal and spatial assets.
🧠 Knowledge Graph	(Neo4j)	Semantic relationships for “Landcover Dataset Family” nodes.


⸻

🧠 Usage in the Pipeline
	•	ETL Stage: Scripts compile or update this summary JSON automatically after landcover metadata files are generated.
	•	Validation: CI workflows confirm each metadata file in landcover/metadata/ appears here and in the global registry.
	•	Graph Load: Neo4j ingester uses this index to construct landcover entity relationships.
	•	API/UI Integration: The summary allows domain-level dataset discovery and filtering by temporal range or variable type.

⸻

🧱 Best Practices

Category	Guideline
✅ Completeness	Include all metadata files from landcover/metadata/.
🔗 Cross-Referencing	Ensure paths to metadata, checksum, and STAC items are accurate.
🧾 Licensing	Default license is CC-BY-4.0 unless specified otherwise.
🕓 Versioning	Update last_updated and increment count for new datasets.
🧪 Validation	Run make validate or CI workflows to confirm consistency with STAC.


⸻

🔒 Reproducibility & MCP Alignment

This domain registry enforces MCP’s documentation-first reproducibility framework by:
	•	Defining the canonical summary of all landcover datasets.
	•	Maintaining provenance chains between ETL → STAC → Graph layers.
	•	Enabling semantic integration via CIDOC CRM and OWL-Time.

It guarantees every landcover dataset in KFM is discoverable, traceable, and interoperable.

⸻

🧱 Related Documentation
	•	data/derivatives/landcover/metadata/README.md — detailed metadata schema
	•	data/derivatives/metadata/metadata/README.md — global derivative metadata registry
	•	data/stac/README.md — STAC catalog and validation
	•	docs/architecture.md — data lineage and provenance documentation

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of landcover metadata domain summary for registry.