---
title: "🪶📑 Kansas Frontier Matrix — Protohistoric Wichita Interaction Sphere Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Sovereignty Advisory Review Required"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-protohistoric-wichita-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced (High Sensitivity)"
doc_kind: "Dataset Metadata"
intent: "protohistoric-wichita-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-High-Sensitivity"
---

<div align="center">

# 🪶📑 **Protohistoric Wichita Interaction Sphere — Metadata**
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/README.md`

**Purpose:**  
Define the **official metadata specification** for the **Protohistoric Wichita Interaction Sphere**, a high-sensitivity cultural dataset requiring **mandatory tribal review**, full CARE governance, and strict spatial generalization.  
This metadata ensures ethical representation, sovereignty protection, and compliance with KFM’s FAIR+CARE, STAC, DCAT, CIDOC-CRM, GeoSPARQL, and PROV-O systems.

</div>

---

## 📘 Overview

The **Protohistoric Wichita Interaction Sphere** represents interaction networks, mobility patterns, exchange corridors, and cultural transformations across **AD 1500–1700** involving ancestral Wichita communities.

This metadata:

- Documents temporal, spatial, cultural, and ethical details  
- Ensures generalization and restricted visibility modes for sensitive areas  
- Provides cross-standard compatibility (DCAT/STAC/PROV-O)  
- Supports Story Nodes & Focus Mode interpretive layers  
- Feeds structured nodes into the KFM Knowledge Graph  
- Guarantees MCA/FAIR+CARE constraints are satisfied before ingestion  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/metadata/
├── README.md
└── protohistoric-wichita-v1.json
~~~

---

## 📦 Required Metadata Specification

Every Interaction Sphere metadata file must include all DCAT, KFM, CARE, and PROV-O crosswalk fields.  
Below outlines the required content of `protohistoric-wichita-v1.json`.

---

# 🧾 DCAT 3.0 Metadata

| Field | Description | Example |
|---|---|---|
| `dct:title` | Dataset Title | `"Protohistoric Wichita Interaction Sphere v1"` |
| `dct:description` | Generalized cultural summary | `"Generalized protohistoric Wichita interaction region across Arkansas–Walnut–Ninnescah valleys."` |
| `dct:license` | License (must be open) | `"CC-BY-4.0"` |
| `dct:temporal` | OWL-Time interval | `"AD 1500–1700"` |
| `dcat:keyword` | Tags | `["Wichita", "Protohistoric", "Kansas", "Interaction Sphere"]` |
| `dcat:distribution` | STAC Item reference | `"../../stac/protohistoric-wichita-v1.json"` |

---

# 🧭 KFM Archaeology Metadata

| Field | Purpose | Example |
|---|---|---|
| `kfm:landscape_type` | Dataset class | `"interaction_sphere"` |
| `kfm:culture_phase` | Cultural phases represented | `["Protohistoric-Wichita"]` |
| `kfm:geometry_generalization` | Spatial safety mechanism | `"H3-level-7"` |
| `kfm:source` | PD or tribal-approved source | `"Archaeological synthesis + approved ethnohistoric summaries"` |
| `kfm:provenance` | PROV-O lineage reference | `"../../provenance/protohistoric-wichita-v1.json"` |
| `kfm:schema_version` | Template version | `"1.0.0"` |

---

# ⚖️ CARE Cultural Safety Metadata  
**This dataset is high-sensitivity.**  
CARE metadata determines which parts of the dataset can be published and how they can be shown.

| CARE Field | Required Values | Notes |
|---|---|---|
| `care:sensitivity` | `"restricted-generalized"` | Required due to protohistoric sensitivity |
| `care:review` | `"tribal"` | Mandatory tribal review before inclusion in ANY release |
| `care:notes` | Explanation of cultural considerations | `"Dataset generalized; ceremonial and oral-history data removed."` |
| `care:visibility_rules` | `"h3-only"` | No polygons allowed; only H3 mosaic permitted for safety |

### Forbidden:
- `"restricted"`  
- Exact cultural boundaries  
- Sensitive oral-historical or ceremonial content  
- Any content absent explicit tribal approval  

---

# 🌍 Spatial Metadata Requirements

- CRS: **EPSG:4326**  
- Geometry: **H3 mosaic only (levels 6–7)**  
- No polygons allowed due to sensitivity  
- No site-level inference permitted  
- Bounding boxes may only reflect large regions  
- Hydrology & environmental context must be **generalized**  

---

# 🕰️ Temporal Metadata Requirements

- Must strictly reflect Protohistoric span: **AD 1500–1700**  
- OWL-Time compliant  
- Should note uncertainty windows if data origin varies  
- Must align with KFM cultural-phase ontology  

---

# 🧪 Provenance Requirements

The PROV-O lineage file (`protohistoric-wichita-v1.json`) must include:

- All raw → generalized → processed steps  
- Tribal review verification metadata  
- Documentation of removed or masked content  
- GIS generalization parameters (H3, simplification thresholds)  
- FAIR+CARE review logs  
- Analyst + reviewer identities  
- Cultural risk assessment summary  

---

# 🧠 KFM Knowledge Graph Integration

### Nodes Created:
- `InteractionSphere`  
- `CulturalPhase`  
- `GeneralizedRegion`  
- `CulturalSensitivityLevel`  
- `MetadataRecord`  

### Relationships:
- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  
- `OCCURRED_DURING`  
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  

This metadata controls the visibility, queryability, and narrative integration of the dataset.

---

# 🎛️ Story Nodes & Focus Mode Integration

Metadata drives:

- Context-aware AI narrative generation  
- Ethical narrative framing  
- Provenance-chip transparency  
- Sensitivity banners and warnings  
- Timeline-phase contextualization  
- Controlled spatial rendering (H3-only)  

---

# 📊 Metadata Summary

| Field | Value |
|---|---|
| Title | Protohistoric Wichita Interaction Sphere v1 |
| Sensitivity | restricted-generalized |
| Review | Tribal (mandatory) |
| Geometry | H3-level-7 (no polygons) |
| Phase | Protohistoric Wichita |
| Provenance | Linked |
| Status | 🟡 Needs Review (cannot publish until approved) |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | Initial metadata release; contains all CARE requirements |
| v0.1 | 2025-11-12 | Landscape Metadata Team | Prototype metadata file |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Tribal Approval Required · FAIR+CARE  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Protohistoric Wichita Dataset](../README.md)

</div>