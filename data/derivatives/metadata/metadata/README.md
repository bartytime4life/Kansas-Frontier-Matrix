<div align="center">

# 🧭 Kansas Frontier Matrix — Derivative Metadata Registry  
`data/derivatives/metadata/metadata/`

**Purpose:** Act as a **central registry** describing all derivative metadata layers across KFM domains  
(climate · hydrology · hazards · landcover · soils · geology), ensuring consistency, version traceability, and STAC cross-references.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC-BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory defines the **master metadata registry** for all KFM derivative domains.  
While each derivative group (`climate/`, `hydrology/`, `hazards/`, `landcover/`) maintains its own local `metadata/` folder,  
this registry aggregates high-level JSON entries summarizing **dataset families**, **data lineage**, and **cross-domain linkages**.

The registry provides:
- 🗂 Domain-level metadata summaries  
- 🔗 STAC catalog cross-references  
- 🧾 Consistent versioning and licensing  
- 🧠 Semantic tagging for CIDOC CRM and OWL-Time  
- 📅 Historical timeline alignment (PeriodO integration)

---

## 🧩 Registry Flow and Context

```mermaid
flowchart TD
  A["Domain Derivatives\n(climate · hydrology · hazards · landcover)"] --> B["Local Metadata\nDomain-level JSON metadata"]
  B --> C["Derivative Metadata Registry\nAggregate JSON summaries"]
  C --> D["STAC Catalog\nCross-domain metadata linkage"]
  D --> E["Knowledge Graph\nSemantic alignment (CIDOC CRM · OWL-Time)"]
  E --> F["API & Web UI\nSearch · Timeline · Map layers"]
%% END OF MERMAID

<!-- END OF MERMAID -->



⸻

🗂️ Directory Layout

metadata/
├── climate/
│   ├── climate_metadata_summary.json
│   └── README.md
│
├── hydrology/
│   ├── hydrology_metadata_summary.json
│   └── README.md
│
├── hazards/
│   ├── hazards_metadata_summary.json
│   └── README.md
│
├── landcover/
│   ├── landcover_metadata_summary.json
│   └── README.md
│
├── terrain/
│   ├── terrain_metadata_summary.json
│   └── README.md
│
├── schema/
│   ├── domain_metadata_summary.schema.json
│   ├── global_derivative_registry.schema.json
│   └── README.md
│
└── README.md

Each file acts as a domain-level metadata summary, describing all derivative datasets contained under that category
and linking to the relevant metadata JSONs (e.g., data/derivatives/climate/metadata/).

⸻

🧾 Registry Schema (JSON Example)

{
  "id": "climate_metadata_summary",
  "title": "Climate Derivative Metadata Summary",
  "description": "Registry of all climate derivative metadata entries, aggregating sources, time coverage, and variable definitions.",
  "domain": "climate",
  "count": 4,
  "entries": [
    {
      "id": "daymet_1980_2024_tmin_ks",
      "path": "../../climate/metadata/daymet_1980_2024_tmin_ks.json",
      "temporal_range": "1980–2024",
      "variables": ["tmin", "tmax", "prcp"],
      "format": "COG",
      "source": "../../sources/daymet.json"
    },
    {
      "id": "normals_1991_2020_prcp",
      "path": "../../climate/metadata/normals_1991_2020_prcp.json",
      "temporal_range": "1991–2020",
      "variables": ["prcp"],
      "format": "COG",
      "source": "../../sources/noaa_normals.json"
    }
  ],
  "last_updated": "2025-10-10",
  "mcp_stage": "derivatives"
}

💡 Tip: Each domain summary file should mirror the structure above, listing every processed derivative under that category and pointing to its full metadata JSON.

⸻

🧮 Purpose and Use
	•	Central Discovery: Acts as an index for all derivative metadata across domains.
	•	Cross-Domain Validation: Used by CI workflows to ensure every derivative dataset is accounted for in both its domain metadata and the registry.
	•	STAC Integration: Each summary links to STAC collections or items, serving as the bridge between domain metadata and the global STAC catalog.
	•	Knowledge Graph Context: The graph ingester reads this registry to populate domain nodes (e.g., Hydrology Dataset Family).

⸻

🧱 Metadata Registry Best Practices

Category	Guideline
✅ Completeness	Include every derivative domain represented in KFM.
🔗 Cross-Referencing	Link each domain entry to both STAC and local metadata.
🧾 Licensing	Use consistent license fields; default to CC-BY-4.0.
🕓 Versioning	Update last_updated upon any domain metadata changes.
🧪 Validation	Run make validate and CI to verify STAC–registry consistency.
🧮 Domain Count	Track total datasets per domain under the count field.


⸻

🔒 Reproducibility & MCP Alignment

The Derivative Metadata Registry embodies KFM’s documentation-first, multi-domain reproducibility standard.
It consolidates all metadata under one umbrella, linking derivative datasets with their provenance,
temporal coverage, and lineage across space, time, and source systems.

This registry supports:
	•	STAC + DCAT harmonization for open interoperability
	•	Cross-domain querying in the Knowledge Graph
	•	Audit-ready metadata lineage for MCP compliance

⸻

🧱 Related Documentation
	•	data/stac/README.md — STAC catalog and validation workflows
	•	data/derivatives/climate/metadata/README.md — domain-level climate metadata
	•	data/derivatives/hazards/metadata/README.md — domain-level hazard metadata
	•	data/derivatives/hydrology/metadata/README.md — domain-level hydrology metadata
	•	data/derivatives/landcover/metadata/README.md — domain-level landcover metadata
	•	docs/architecture.md — ETL and provenance system design

⸻

🗓️ Version History

Version	Date	Notes
0.1.0	2025-10-10	Initial creation of global derivative metadata registry.