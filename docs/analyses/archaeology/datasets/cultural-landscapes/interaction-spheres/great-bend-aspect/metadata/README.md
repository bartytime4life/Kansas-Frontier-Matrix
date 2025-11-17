---
title: "🏺📑 Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Metadata"
intent: "great-bend-aspect-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Generalized)"
---

<div align="center">

# 🏺📑 **Great Bend Aspect Interaction Sphere — Metadata**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/README.md`

**Purpose:**  
Provide the complete metadata specification for the **Great Bend Aspect (GBA) Interaction Sphere**, ensuring FAIR+CARE alignment, STAC/DCAT interoperability, transparent provenance, and ethical depiction of a culturally significant Late Prehistoric–Protohistoric landscape zone.  

This metadata governs the dataset’s structure, cultural narrative framing, generalization level, and long-term reproducibility within the Kansas Frontier Matrix (KFM).

</div>

---

# 📘 Overview

The Great Bend Aspect Interaction Sphere is associated with:

- Ancestral Wichita cultural traditions  
- Late Prehistoric + Protohistoric settlement networks  
- Semi-sedentary horticulture & bison hunting  
- Ceramic, architectural, and subsistence pattern coherence  
- Prairie–riverine adaptive landscapes  
- Regional interaction with Central Plains, Southern Plains, and early European contacts

This metadata document ensures the dataset describing this sphere meets:

- STAC 1.0  
- DCAT 3.0  
- CIDOC-CRM/GeoSPARQL ontology alignment  
- KFM archaeology schema (`kfm:*`)  
- FAIR+CARE governance with tribal advisories recommended for protohistoric elements  
- Provenance traceability through PROV-O  

---

# 🗂️ Directory App Structure

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/metadata/
├── README.md                               # This file
└── great-bend-aspect-v2.json               # DCAT + CARE + KFM metadata
~~~

---

# 📦 Metadata Specification (DCAT + KFM + CARE)

The dataset metadata (`great-bend-aspect-v2.json`) must include all required fields:

---

## ✔ DCAT 3.0 Fields

| Field | Description | Example |
|---|---|---|
| `dct:title` | Dataset name | `"Great Bend Aspect Interaction Sphere v2"` |
| `dct:description` | Summary | `"Generalized Late Prehistoric–Protohistoric interaction region"` |
| `dct:license` | Open license | `"CC-BY-4.0"` |
| `dct:temporal` | Time interval | `"AD 1350–1700"` |
| `dcat:keyword` | Tags | `["Great Bend Aspect", "Wichita", "Late Prehistoric", "Protohistoric"]` |
| `dcat:distribution` | STAC link | `"../../stac/great-bend-aspect-v2.json"` |

---

## ✔ KFM Archaeology Metadata

| Field | Purpose | Example |
|---|---|---|
| `kfm:landscape_type` | Required type | `"interaction_sphere"` |
| `kfm:culture_phase` | Cultural phases | `["GBA-Early","GBA-Middle","GBA-Late"]` |
| `kfm:geometry_generalization` | Required for safety | `"H3-level-6"` |
| `kfm:source` | Primary data source | `"PD archaeological synthesis"` |
| `kfm:provenance` | PROV-O reference | `"../../provenance/great-bend-aspect-v2.json"` |
| `kfm:schema_version` | Document version | `"1.0.0"` |

---

## ✔ CARE Cultural Safety Metadata

Because GBA contains protohistoric components (AD 1600–1700) with potential descendant community significance, CARE metadata is mandatory.

| CARE Field | Recommended Value | Notes |
|---|---|---|
| `care:sensitivity` | `"generalized"` | Required for public-facing content |
| `care:review` | `"faircare"` | Tribal advisory recommended |
| `care:notes` | `"Generalized polygons used; sensitive narratives excluded."` | Ethical + contextual summary |
| `care:visibility_rules` | `"polygon-generalized"` | Avoid precise boundaries or site inference |

Forbidden:
- `"restricted"`  
- Exact sacred/ceremonial areas  
- Explicit ethnohistorical data without review  
- Embedding sensitive oral histories  

---

# 🌍 Spatial Metadata Requirements

- Geometry: **MultiPolygon**, highly generalized  
- CRS: **EPSG:4326**  
- H3 generalization required for sensitive sub-regions  
- No site-level spatial detail  
- Only territory-scale, interpretive-safe surfaces allowed  
- Bounding box must be included for DCAT & STAC  

---

# 🕰️ Temporal Metadata Requirements

- Must cover AD 1350–1700  
- Multi-phase OWL-Time intervals allowed  
- Provide phase-specific ranges (GBA-Early, Middle, Late)  
- Optional uncertainty metadata recommended  

---

# 🧪 Provenance Linkage

Metadata MUST reference the PROV-O provenance record:

kfm:provenance: “../../provenance/great-bend-aspect-v2.json”

Provenance records describe:

- Raw → generalized → processed lineage  
- Cultural review (FAIR+CARE + optional tribal advisory)  
- GIS generalization steps  
- Source materials  
- Ethical decision-making  

---

# ⚖️ Ethical Governance & Cultural Context

All GBA-related metadata must:

- Avoid colonial terminology  
- Clearly denote interpretive uncertainty  
- Treat ancestral Wichita heritage with respect  
- Avoid territorial claim implications  
- Maintain generalization as a core protection principle  
- Note when protohistoric content influences sensitivity classification  

---

# 🧠 Integration Into KFM Ecosystem

Metadata informs:

### Knowledge Graph
Nodes:
- `InteractionSphere`  
- `CulturalPhase`  
- `GeneralizedRegion`  
- `CulturalNetwork`  

Edges:
- `HAS_METADATA`  
- `OCCURRED_DURING`  
- `CARE_SENSITIVITY`  
- `HAS_PROVENANCE`  

### Story Nodes
- Anchors Great Bend narratives  
- Connects to artifact inventories, routes, and regions  

### Focus Mode v2
- Ethical warnings  
- Provenance chips  
- Cultural-phase overlays  
- Summary contextualization  

---

# 📊 Metadata Summary

| Field | Value |
|---|---|
| Title | Great Bend Aspect Interaction Sphere v2 |
| Sensitivity | generalized |
| Review | FAIR+CARE (Tribal advisories recommended) |
| Culture Phases | Early/Middle/Late GBA |
| Provenance | Included |
| Spatial Generalization | H3-level-6 |
| Status | 🟢 Active |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v2 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Updated for stronger CARE alignment; expanded metadata depth |
| v1 | 2025-11-10 | Landscape Metadata Team | Initial metadata draft |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Great Bend Aspect Dataset](../README.md)

</div>