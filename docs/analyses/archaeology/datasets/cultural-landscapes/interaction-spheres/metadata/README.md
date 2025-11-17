---
title: "🧾 Kansas Frontier Matrix — Cultural Landscape Interaction Sphere Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-metadata-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Metadata Standard"
intent: "cultural-landscape-interaction-spheres-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Cultural Landscape Interaction Sphere Metadata Standards**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/README.md`

**Purpose:**  
Provide the **metadata specification and governance framework** for all **Interaction Sphere datasets** in the Kansas Frontier Matrix (KFM).  
Interaction Spheres model **broad-scale cultural networks**, **exchange systems**, and **inter-group relationships** across the prehistoric, protohistoric, and early historic Plains.

Metadata produced in this directory ensures that all Interaction Sphere datasets comply with:

- **FAIR+CARE governance**  
- **STAC 1.0 + KFM archaeology extension**  
- **DCAT 3.0**  
- **CIDOC-CRM & GeoSPARQL ontology mapping**  
- **PROV-O provenance linkage**  
- **KFM-MDP v10.4 documentation requirements**

Metadata is essential for graph ingestion, map visualization, Story Node integration, Focus Mode v2 narrative generation, and versioned governance.

</div>

---

# 📘 Overview

Interaction Sphere metadata provides:

- Cultural and archaeological context  
- Provenance transparency  
- Ethical review details  
- Spatial and temporal definition (generalized)  
- Dataset discoverability through STAC/DCAT  
- Ethical safeguards for culturally sensitive areas  

These metadata JSON files describe Interaction Sphere datasets stored under:

- `great-bend-aspect/`  
- `central-plains-exchange/`  
- Additional spheres added over time  

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/
├── README.md                        
├── great-bend-aspect-v2.json        # Metadata for Great Bend Aspect interaction sphere
├── central-plains-exchange-v1.json  # Metadata for Central Plains Exchange sphere
└── templates/                       # Templates for creating new metadata JSON files
~~~

---

# 📦 Required Metadata Components (All Interaction Spheres)

Metadata must include **all** of the following components:

---

## ✔ DCAT 3.0 Metadata

| Field | Description | Example |
|---|---|---| 
| `dct:title` | Dataset title | `"Great Bend Aspect Interaction Sphere v2"` |
| `dct:description` | Summary of sphere | `"Generalized Late Prehistoric–Protohistoric cultural interaction region"` |
| `dct:license` | SPDX license | `"CC-BY-4.0"` |
| `dct:temporal` | OWL-Time interval | `"AD 1350–1700"` |
| `dcat:keyword` | Tags | `["interaction sphere", "archaeology", "Kansas"]` |
| `dcat:distribution` | Link to STAC Item | `"stac/great-bend-aspect-v2.json"` |

---

## ✔ KFM Archaeology Metadata

| Field | Description | Example |
|---|---|---| 
| `kfm:landscape_type` | `"interaction_sphere"` | `"interaction_sphere"` |
| `kfm:culture_phase` | Cultural-phase set | `["GBA-Early", "GBA-Middle", "GBA-Late"]` |
| `kfm:source` | Dataset origin | `"Published archaeological synthesis"` |
| `kfm:geometry_generalization` | Generalization method | `"H3 level 6"` |
| `kfm:provenance` | PROV-O link | `"provenance/great-bend-aspect-v2.json"` |
| `kfm:schema_version` | Metadata schema version | `"1.0.0"` |

---

## ✔ CARE Cultural Safety Metadata

Interaction Spheres often contain sensitive cultural material.  
All metadata must include:

| CARE Field | Values | Notes |
|---|---|---| 
| `care:sensitivity` | `"generalized"` / `"restricted-generalized"` | `"restricted-generalized"` often required for protohistoric spheres |
| `care:review` | `"faircare"` / `"tribal"` | `"tribal"` required if any protohistoric or ethnohistoric content exists |
| `care:notes` | Explanation of generalization & safeguards | Must cite cultural considerations |
| `care:visibility_rules` | `"polygon-generalized"` / `"h3-only"` / `"no-exact-boundaries"` | `"h3-only"` recommended for high-sensitivity zones |

Forbidden:
- `"restricted"` — not allowed in the public KFM dataset  
- Exact boundaries for sacred/ceremonial landscapes  
- Sensitive oral-historical content without approval  

---

## ✔ Provenance Linkage (PROV-O)

Metadata must reference a PROV-O file documenting:

- Raw source descriptions  
- Generalization steps  
- Spatial/temporal modeling  
- Ethical & cultural review  
- Decision-making logs  
- Analyst + reviewer attribution  

Field: