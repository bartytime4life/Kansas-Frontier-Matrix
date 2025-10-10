<div align="center">

# 🌡️ Kansas Frontier Matrix — Climate Derivative Metadata Summary  
`data/derivatives/metadata/metadata/climate/`

**Purpose:** Aggregate and summarize all **climate derivative metadata** files across the Kansas Frontier Matrix (KFM),  
providing a domain-level registry for provenance, validation, and cross-linking within the global derivative metadata system.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory serves as the **climate domain index** for all derivative metadata JSON files under  
`data/derivatives/climate/metadata/`. It summarizes key datasets, variables, time ranges, and lineage links  
to create a **machine-readable and human-readable snapshot** of all climate derivatives.

This summary enables:
- Rapid discovery of all available climate layers (temperature, precipitation, drought, etc.)  
- Verification of dataset registration in both the **STAC catalog** and **Knowledge Graph**  
- Consistent domain-level validation within the MCP documentation-first workflow  

---

## 🧭 Metadata Summary Flow

```mermaid
flowchart TD
  A["Domain Metadata JSONs\n(data/derivatives/climate/metadata/)"] --> B["Climate Summary JSON\n(data/derivatives/metadata/metadata/climate/)"]
  B --> C["Derivative Metadata Registry\n(data/derivatives/metadata/metadata/)"]
  C --> D["STAC Catalog\n(data/stac/)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

climate/
├── climate_metadata_summary.json
└── README.md

This folder acts as the climate section of the global derivative metadata registry, providing
an aggregated metadata summary for all processed climate datasets.

⸻

🧾 Summary JSON Schema (Example)

{
  "id": "climate_metadata_summary",
  "title": "Climate Derivative Metadata Summary",
  "description": "Aggregated summary of all processed climate derivative metadata files in KFM.",
  "domain": "climate",
  "entries": [
    {
      "id": "daymet_1980_2024_tmin_ks",
      "title": "Daily Minimum Temperature (Daymet, 1980–2024, Kansas)",
      "path": "../../../../climate/metadata/daymet_1980_2024_tmin_ks.json",
      "temporal_range": "1980–2024",
      "variables": ["tmin"],
      "format": "COG",
      "source": "../../../../sources/daymet.json",
      "stac_item": "../../../../stac/items/daymet_1980_2024_tmin_ks.json"
    },
    {
      "id": "normals_1991_2020_prcp",
      "title": "Precipitation Normals (1991–2020, NOAA)",
      "path": "../../../../climate/metadata/normals_1991_2020_prcp.json",
      "temporal_range": "1991–2020",
      "variables": ["prcp"],
      "format": "COG",
      "source": "../../../../sources/noaa_normals.json",
      "stac_item": "../../../../stac/items/normals_1991_2020_prcp.json"
    },
    {
      "id": "drought_index_annual_ks",
      "title": "Annual Drought Severity Index (Kansas, 1895–2024)",
      "path": "../../../../climate/metadata/drought_index_annual_ks.json",
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

💡 Tip: Update the entries array whenever new derivative metadata files are added or modified in the climate domain.

⸻

🧩 Relationship to Other Metadata Layers

Layer	Path	Purpose
🌡️ Climate Metadata	data/derivatives/climate/metadata/	Source of individual climate metadata files.
🧾 Domain Summary (This)	data/derivatives/metadata/metadata/climate/	Aggregated index summarizing climate derivatives.
🧮 Global Registry	data/derivatives/metadata/metadata/	Multi-domain metadata registry including all domains.
🗺️ STAC Catalog	data/stac/	Registers all climate assets and metadata cross-links.
🧠 Knowledge Graph	(Neo4j)	Populates domain-level nodes for “Climate Dataset Family.”


⸻

🧠 Usage in the Pipeline
	•	ETL Stage: After generating or updating climate metadata JSONs, a summarization script compiles them into this registry.
	•	CI/CD: The stac-validate.yml workflow ensures all derivative metadata entries are registered here and cross-checked against STAC items.
	•	Graph Ingestion: The registry provides domain-level linkage for climate datasets, supporting timeline visualization and domain-based queries.

⸻

🧱 Best Practices

Category	Guideline
✅ Completeness	Every metadata file in climate/metadata/ must be referenced here.
🔗 Cross-References	Maintain accurate relative paths to source and STAC items.
🧾 Licensing	Default license is CC-BY-4.0 unless otherwise specified.
🕓 Versioning	Update last_updated whenever new datasets are added.
🧮 Validation	Run make validate to verify alignment with STAC and registry schema.


⸻

🔒 Reproducibility & MCP Alignment

This summary file exemplifies the Master Coder Protocol approach by maintaining:
	•	A single source of truth for climate derivative metadata.
	•	Cross-linkage between raw metadata, STAC entries, and graph nodes.
	•	Versioned provenance for transparent change tracking.

It ensures that all climate datasets within KFM are traceable, auditable, and interoperable across analytical and visualization systems.

⸻

🧱 Related Documentation
	•	data/derivatives/climate/metadata/README.md — detailed climate metadata schema
	•	data/derivatives/metadata/metadata/README.md — global derivative metadata registry
	•	data/stac/README.md — STAC catalog integration
	•	docs/architecture.md — ETL and metadata design overview

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of climate metadata summary index for derivative registry.