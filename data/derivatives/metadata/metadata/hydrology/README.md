<div align="center">

# 💧 Kansas Frontier Matrix — Hydrology Derivative Metadata Summary  
`data/derivatives/metadata/metadata/hydrology/`

**Purpose:** Aggregate and summarize all **hydrology derivative metadata** files under  
`data/derivatives/hydrology/metadata/`, creating a domain-level index for provenance tracking,  
validation, and integration within KFM’s global metadata registry and STAC catalog.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory functions as the **hydrology domain summary registry**, consolidating all derivative  
metadata JSON files from `data/derivatives/hydrology/metadata/`.  

It provides a domain-level summary of hydrological datasets (streamflow, aquifer, floodplain, watershed),  
facilitating provenance validation and linking domain derivatives into the global metadata registry.  

Benefits include:
- 🌊 Unified discovery of hydrological datasets and variables  
- 🔗 Verified linkage between ETL outputs, STAC entries, and the knowledge graph  
- 🧠 Simplified CI validation and automated graph synchronization  

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Hydrology Metadata JSONs\n(data/derivatives/hydrology/metadata/)"] --> B["Hydrology Summary JSON\n(data/derivatives/metadata/metadata/hydrology/)"]
  B --> C["Derivative Metadata Registry\n(data/derivatives/metadata/metadata/)"]
  C --> D["STAC Catalog\n(data/stac/)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

hydrology/
├── hydrology_metadata_summary.json
└── README.md

Each summary JSON consolidates all hydrology derivatives and links them to their original metadata,
checksum files, and STAC records for reproducibility and validation.

⸻

🧾 Summary JSON Schema (Example)

{
  "id": "hydrology_metadata_summary",
  "title": "Hydrology Derivative Metadata Summary",
  "description": "Aggregated metadata summary for hydrology derivative datasets across Kansas Frontier Matrix.",
  "domain": "hydrology",
  "entries": [
    {
      "id": "streamflow_monthly_1990_2025",
      "title": "Monthly Streamflow Composite (1990–2025, USGS NWIS)",
      "path": "../../../../hydrology/metadata/streamflow_monthly_1990_2025.json",
      "temporal_range": "1990–2025",
      "variables": ["streamflow"],
      "format": "COG",
      "source": "../../../../sources/usgs_nwis_streamflow.json",
      "stac_item": "../../../../stac/items/streamflow_monthly_1990_2025.json"
    },
    {
      "id": "floodplain_extent_2020",
      "title": "Floodplain Extent Map (2020, FEMA NFHL)",
      "path": "../../../../hydrology/metadata/floodplain_extent_2020.json",
      "temporal_range": "2020",
      "variables": ["flood_extent"],
      "format": "COG",
      "source": "../../../../sources/fema_flood_zones.json",
      "stac_item": "../../../../stac/items/floodplain_extent_2020.json"
    },
    {
      "id": "aquifer_depth_ks",
      "title": "Aquifer Depth Grid (Kansas, USGS Water Data)",
      "path": "../../../../hydrology/metadata/aquifer_depth_ks.json",
      "temporal_range": "Static",
      "variables": ["depth_to_water_table"],
      "format": "COG",
      "source": "../../../../sources/usgs_aquifers.json",
      "stac_item": "../../../../stac/items/aquifer_depth_ks.json"
    }
  ],
  "count": 3,
  "license": "CC-BY-4.0",
  "last_updated": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Each hydrology metadata entry must be cross-referenced here, with correct relative paths to STAC and source files.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
💧 Hydrology Metadata	data/derivatives/hydrology/metadata/	Individual metadata files for hydrology derivatives.
🧾 Domain Summary (This)	data/derivatives/metadata/metadata/hydrology/	Aggregated hydrology metadata index.
🧮 Global Registry	data/derivatives/metadata/metadata/	Central cross-domain metadata registry.
🗺️ STAC Catalog	data/stac/	Global asset catalog for all spatial/temporal derivatives.
🧠 Knowledge Graph	(Neo4j)	Connects hydrological entities, models, and sources semantically.


⸻

🧠 Usage in the Pipeline
	•	ETL Stage: Automatically generated after hydrology metadata JSONs are updated or added.
	•	Validation: Ensures all hydrology derivatives have registered metadata and STAC entries.
	•	Graph Integration: Neo4j importer uses this registry to connect all hydrology-related datasets.
	•	CI/CD: The stac-validate.yml workflow validates completeness and linkage consistency.

⸻

🧱 Best Practices

Category	Guideline
✅ Completeness	Every hydrology derivative metadata file must be included.
🔗 Cross-Referencing	Maintain consistent relative paths to metadata and STAC items.
🧾 Licensing	Use consistent licensing across entries (default: CC-BY-4.0).
🕓 Versioning	Update last_updated upon registry or dataset modification.
🧪 Validation	Run make validate or CI workflows to confirm schema alignment.


⸻

🔒 Reproducibility & MCP Alignment

This domain summary reinforces MCP’s reproducibility and documentation-first principles by:
	•	Providing a single authoritative listing for all hydrology datasets.
	•	Ensuring traceability between ETL, STAC, and Knowledge Graph layers.
	•	Embedding semantic alignment using open ontologies (STAC · DCAT · CIDOC CRM · OWL-Time).

It enables KFM contributors to audit, discover, and interlink all hydrological data artifacts consistently.

⸻

🧱 Related Documentation
	•	data/derivatives/hydrology/metadata/README.md — detailed hydrology metadata schema
	•	data/derivatives/metadata/metadata/README.md — global metadata registry overview
	•	data/stac/README.md — STAC catalog integration
	•	docs/architecture.md — ETL and provenance design

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of hydrology metadata domain summary for registry.