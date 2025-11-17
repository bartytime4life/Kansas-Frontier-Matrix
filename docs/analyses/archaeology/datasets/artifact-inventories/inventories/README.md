---
title: "🏺 Kansas Frontier Matrix — Artifact Inventory Files (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/inventories/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-inventory-files-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Subcategory"
intent: "artifact-inventory-files"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Artifact Inventory Files**  
`docs/analyses/archaeology/datasets/artifact-inventories/inventories/README.md`

**Purpose:**  
Serve as the **canonical index** for *cleaned, normalized, culturally-reviewed* artifact inventory tables that power archaeological analysis, mapping, cultural-phase timelines, and AI-assisted narratives within the Kansas Frontier Matrix (KFM).

These files represent **final, validated** artifact inventories ready for:

- Neo4j graph ingestion  
- Story Node generation  
- Focus Mode v2 material culture explanations  
- Archaeological pattern modeling  
- MapLibre layer creation (generalized H3 density layers)  
- Cross-dataset joins (stratigraphy, paleoenvironment, cultural landscapes)

Only datasets that are **public-domain**, **open-license**, and **FAIR+CARE-approved** may appear in this directory.

</div>

---

## 📘 Overview

This directory contains **processed artifact datasets**—cleaned, categorized, generalized, and harmonized to KFM schema requirements.

Each dataset must include:

- Standardized schema fields  
- CARE classification  
- Cultural-phase attribution  
- Provenance file  
- STAC Item in the parent `stac/` directory  
- DCAT dataset record in the parent `metadata/` directory

Prohibited content:

- Human remains / funerary items  
- Sacred or sensitive ceremonial artifacts  
- Unprovenanced or illicitly obtained artifacts  
- Precise provenience of protected archaeological contexts  

All spatial references MUST be generalized using **H3 (levels 5–7)**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/inventories/
├── README.md                     # This file
├── flint-hills-lithics-v1.csv    # Cleaned lithic inventory (PD)
├── prairie-ceramics-v1.csv       # Ceramic types + motifs (generalized)
├── contact-era-metals-v1.csv     # Protohistoric metal artifacts (pending review)
├── fauna-open-v1.csv             # PD faunal dataset (non-sensitive)
└── ...                           # Additional curated inventory tables
~~~

---

## 📋 Required Schema (All Inventory Tables)

Every file in this directory MUST follow the standardized schema:

| Field | Description | Required |
|---|---|---|
| `artifact_id` | UUID for each artifact | ✔ |
| `material` | Lithic / ceramic / metal / bone / other | ✔ |
| `artifact_type` | Standardized classification term | ✔ |
| `culture_phase` | Associated phase (e.g., "Late Prehistoric") | ✔ |
| `dating_method` | Typology / associated layer / radiocarbon | ✔ |
| `temporal_range_start` | ISO 8601 or approximate (e.g., `"1200 CE"`) | ✔ |
| `temporal_range_end` | ISO 8601 or approximate | ✔ |
| `location_h3` | H3 cell (level 5–7) | ✔ |
| `site_class` | Generalized site category | ✔ |
| `quantity` | Count or measurement | ✔ |
| `description` | Neutral, culturally safe description | ✔ |
| `source` | Repository or dataset reference | ✔ |
| `provenance_file` | Path to PROV-O JSON | ✔ |

Forbidden fields:

- Exact coordinates  
- Excavation unit codes  
- Restricted cultural descriptors  
- Personally identifiable information  
- Provenience details from protected sites  

---

## 🧭 Dataset Inventory Index

| Dataset | Category | Status | Last Review | Notes |
|---|---|---|---|---|
| `flint-hills-lithics-v1.csv` | Lithics | 🟢 Active | 2025-11 | PD, culturally safe |
| `prairie-ceramics-v1.csv` | Ceramics | 🟢 Active | 2025-10 | Decoration types filtered for sensitivity |
| `contact-era-metals-v1.csv` | Protohistoric Metals | 🟡 Needs Review | 2025-09 | Tribal review pending |
| `fauna-open-v1.csv` | Faunal | 🟢 Active | 2025-11 | Sacred species excluded |

---

## 🧪 Data Quality & Validation Requirements

Each inventory MUST pass:

### **Scientific Validation**
- Correct material culture classification  
- Typological cross-check  
- Internal consistency checks  

### **Cultural Validation (FAIR+CARE)**
- Tone and description review  
- Removal of culturally sensitive classifications  
- Review for potential misinterpretation  
- Verification of open-access status  

### **Technical Metadata Validation**
- STAC Item created + valid  
- DCAT dataset present  
- Provenance logs complete  
- H3 generalization confirmed  
- UTF-8 encoding  

---

## 🛰️ Integration Into KFM Systems

### Knowledge Graph
Inventory tables generate:

Nodes:
- `Artifact`
- `ArtifactType`
- `Material`
- `CulturePhase`
- `GeneralizedSite`

Relationships:
- `BELONGS_TO`
- `FOUND_AT`
- `DATED_TO`
- `ASSOCIATED_WITH`

### Focus Mode v2
Inventories support:

- Material culture summaries  
- Temporal pattern generation  
- AI-assisted correlations  
- Provenance-aware descriptive output  

All Focus Mode outputs undergo **ethics-review-template** validation.

### Story Nodes
Artifact inventories drive:

- Cultural-phase descriptions  
- Chronological timelines  
- Material spread narratives  

---

## 📦 Example Artifact Inventory Snippet

~~~csv
artifact_id,material,artifact_type,culture_phase,dating_method,temporal_range_start,temporal_range_end,location_h3,site_class,quantity,description,source,provenance_file
"uuid-1234","lithic","projectile_point","Late Prehistoric","typology","1200 CE","1400 CE","872830fffffffff","village","1","Triangular point, smoothed edges.","WSU Open Collections","provenance/flint-hills-lithics-v1.json"
~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added inventory file index, schema, validation rules, cultural protections, and KFM integration details |
| v10.0.0 | 2025-11-10 | Artifact Dataset Team | Initial structure and placeholder inventory support |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact Inventories](../README.md)

</div>