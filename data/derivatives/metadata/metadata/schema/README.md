<div align="center">

# 🧩 Kansas Frontier Matrix — Derivative Metadata Registry Schema  
`data/derivatives/metadata/metadata/schema/`

**Purpose:** Define and validate **JSON Schema specifications** for all domain-level and global derivative metadata summaries  
within the Kansas Frontier Matrix (KFM) system — ensuring semantic consistency, reproducibility, and interoperability.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **JSON Schema definitions** governing the structure and validation rules  
for all derivative metadata summary files found under `data/derivatives/metadata/metadata/`.

Schemas defined here apply to:
- 🌦️ Climate metadata summaries (`climate_metadata_summary.json`)  
- ⚠️ Hazard metadata summaries (`hazards_metadata_summary.json`)  
- 💧 Hydrology metadata summaries (`hydrology_metadata_summary.json`)  
- 🌾 Landcover metadata summaries (`landcover_metadata_summary.json`)  
- 🧭 Global derivative registry (`derivative_metadata_registry.json`)

These schemas enable automated validation within KFM’s CI/CD workflows, ensuring uniform field naming,  
consistent key structure, and interoperability between STAC, DCAT, and Knowledge Graph entities.

---

## 🧭 Schema Integration Flow

```mermaid
flowchart TD
  A["Domain Metadata Summaries\n(climate, hazards, hydrology, landcover)"] --> B["Schema Definitions\n(data/derivatives/metadata/metadata/schema/)"]
  B --> C["JSON Schema Validation\n(stac-validate.yml workflow)"]
  C --> D["STAC Catalog\nCross-domain metadata references"]
  D --> E["Knowledge Graph\nSemantic entity creation"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

schema/
├── domain_metadata_summary.schema.json
├── global_derivative_registry.schema.json
└── README.md

Each schema defines the required structure, types, and properties for derivative metadata summaries.
These are used by make validate and CI workflows to check compliance before merging.

⸻

🧾 Example — Domain Metadata Summary Schema

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.data/schema/domain_metadata_summary.schema.json",
  "title": "KFM Domain Metadata Summary Schema",
  "description": "JSON Schema for validating domain-level derivative metadata summary files.",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "description": { "type": "string" },
    "domain": { "type": "string", "enum": ["climate", "hazards", "hydrology", "landcover"] },
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "title": { "type": "string" },
          "path": { "type": "string" },
          "temporal_range": { "type": "string" },
          "variables": { "type": "array", "items": { "type": "string" } },
          "format": { "type": "string" },
          "source": { "type": "string" },
          "stac_item": { "type": "string" }
        },
        "required": ["id", "title", "path", "format", "source"]
      }
    },
    "count": { "type": "integer", "minimum": 1 },
    "license": { "type": "string" },
    "last_updated": { "type": "string", "format": "date" },
    "mcp_stage": { "type": "string" }
  },
  "required": ["id", "title", "domain", "entries", "count", "last_updated"]
}

💡 Tip: This schema is used to validate each domain-level summary (e.g., climate_metadata_summary.json),
confirming the presence and structure of required fields.

⸻

🧱 Validation Workflow

Stage	Tool	Description
Local Validation	make validate	Runs jsonschema checks against schema definitions locally.
CI Validation	stac-validate.yml	Executes JSON Schema and STAC validation on all metadata summary files.
Cross-Referencing	Python ETL	Scripts confirm that all entries in summaries correspond to actual metadata and STAC files.
Knowledge Graph Sync	Neo4j Loader	Validated summaries are imported into graph nodes as “domain registry” entities.


⸻

🔒 Reproducibility & MCP Alignment

These schemas implement MCP’s documentation-first and data integrity mandates:
	•	Uniform validation of all derivative metadata domains
	•	Machine-readable consistency between JSON and STAC/DCAT metadata
	•	Cross-domain interoperability enabling graph-based provenance tracking

The schema system ensures that every derivative dataset—from climate rasters to hydrological models—
is fully documented, auditable, and verifiable.

⸻

🧱 Related Documentation
	•	data/derivatives/metadata/metadata/README.md — global metadata registry overview
	•	data/stac/README.md — STAC catalog integration and validation
	•	docs/architecture.md — ETL and provenance system design
	•	docs/templates/sop.md — MCP standard operating procedure format

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial schema definitions for KFM domain and global metadata registries.