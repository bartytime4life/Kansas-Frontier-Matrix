---
title: "🌀 Kansas Frontier Matrix — Cultural Landscape Interaction Spheres (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-interaction-spheres-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Subcategory"
intent: "archaeology-interaction-spheres"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌀 **Kansas Frontier Matrix — Cultural Landscape Interaction Spheres**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/README.md`

**Purpose:**  
Define, document, and govern all **interaction sphere datasets** used in the Kansas Frontier Matrix (KFM).  
Interaction spheres represent **regional-scale cultural connectivity zones**, **shared material culture traits**, **overlapping trade/communication networks**, and **inter-group interactions** across prehistoric, protohistoric, and early historic Kansas.

These datasets feed directly into:

- Cultural-phase mapping  
- Story Node cultural network models  
- Focus Mode v2 interpretive overlays  
- MapLibre + Cesium landscape synthesis  
- AI-assisted movement & diffusion pattern modeling  
- Neo4j knowledge graph cultural-relationship linking  

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../../standards/faircare.md)  
[![License](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-success)](../../../../../../releases/v10.4.0/manifest.zip)

</div>

---

# 📘 Overview

Interaction spheres represent **broad cultural zones** defined by:

- Shared artifact styles  
- Similar technological traditions  
- Overlapping subsistence systems  
- Cross-regional trade or migration  
- Cultural/linguistic affiliations  
- Environmental co-adaptation  

Examples include:

- **Great Bend Aspect**  
- **Central Plains Tradition exchange zones**  
- **Protohistoric Wichita interaction corridors**  
- **Northern Plains–Central Plains contact regions**

These areas are always **generalized** to protect sensitive landscapes and avoid over-precision.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/
├── README.md                      # This file
├── great-bend-aspect/             # Generalized polygons & metadata
├── central-plains-exchange/       # Multi-era interaction zones
├── protohistoric-wichita/         # Ethnohistoric/archaeological overlap regions
├── stac/                          # STAC Items & Collections for interaction spheres
├── metadata/                      # DCAT, CARE, cultural notes
└── provenance/                    # PROV-O lineage & review logs
~~~

---

# 🌀 Dataset Definition

| Component | Description |
|---|---|
| **Interaction Sphere** | A cultural region defined by shared material culture and interaction patterns |
| **Temporal Span** | Usually multi-century; modeled using OWL-Time intervals |
| **Spatial Representation** | Generalized polygons or H3 mosaic surfaces |
| **Sources** | Archaeology literature, aggregated artifact inventories, ethnohistoric accounts |
| **Cultural Sensitivity** | Tribal review recommended; CARE required |

---

# 🧭 Examples of Cultural Interaction Spheres

## **Great Bend Aspect Interaction Sphere**
- Late Prehistoric / Protohistoric (AD 1300–1700)  
- Strong ceramic, lithic, and settlement pattern coherence  
- Linked to protohistoric Wichita ancestors  
- Environmentally tied to Central Plains + southern Flint Hills  

## **Central Plains Tradition Exchange Region**
- Material flow zone between Smoky Hill, Republican, and Platte drainages  
- Shared architectural traits, pottery motifs, and faunal exploitation patterns  

## **Protohistoric Wichita Corridor**
- Interaction route linking southern Plains, Great Bend, and early European trade networks  
- High cultural sensitivity — **tribal review mandatory**

---

# 📦 Required Metadata (All Interaction Sphere Datasets)

### ✔ STAC Item Fields
- `id` (versioned)  
- `bbox` (generalized)  
- `geometry` (Polygon or MultiPolygon only)  
- `kfm:culture_phase`  
- `care:sensitivity` (`generalized` or `restricted-generalized`)  
- `kfm:provenance`  

Example STAC snippet:

~~~json
{
  "id": "great-bend-aspect-v2",
  "type": "Feature",
  "stac_version": "1.0.0",
  "bbox": [-101.8, 37.0, -95.3, 40.5],
  "geometry": { "type": "MultiPolygon", "coordinates": [[[ ... ]]] },
  "properties": {
    "kfm:culture_phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "provenance/great-bend-v2.json"
  }
}
~~~

---

# ⚖️ Cultural & Ethical Requirements (FAIR+CARE)

Interaction spheres must:

- Avoid suggesting rigid boundaries (cultural areas are fluid)  
- Use **non-essentialist** and non-colonial terminology  
- Include cultural notes emphasizing interpretive uncertainty  
- Generalize territorial zones unless tribal approval is granted  
- Never include sacred or restricted ceremonial areas  
- Provide Indigenous review for protohistoric or ethnohistoric regions  

Forbidden content:

- Exact outlines of sacred geographies  
- Precise territorial claims without tribal consent  
- Raw archaeological site locations  

---

# 📊 Dataset Index

| Dataset | Category | Status | Last Review | Notes |
|---|---|---|---|---|
| `great-bend-aspect/v2` | Great Bend Aspect | 🟢 Active | 2025-11 | Generalized, culturally reviewed |
| `central-plains-exchange/v1` | Exchange Sphere | 🟢 Active | 2025-10 | STAC + DCAT compliant |
| `protohistoric-wichita/v1` | Protohistoric | 🟡 Needs Review | 2025-09 | Tribal consultation pending |

---

# 🧪 Integration Into KFM Ecosystem

### **Neo4j Graph**
Nodes:
- `InteractionSphere`  
- `CulturePhase`  
- `Region`  
- `MaterialPattern`  

Relationships:
- `INTERACTED_WITH`  
- `OVERLAPS`  
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  

### **Focus Mode v2**
Used to:

- Generate cultural network narratives  
- Visualize multi-era cultural diffusion  
- Provide contextual overlays for artifact patterns  

### **Story Nodes**
Enrich:

- Cultural timelines  
- Trade and migration sequences  
- Multi-region archaeological explanations  

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created interaction spheres directory; added metadata, CARE, and STAC requirements |
| v10.0.0 | 2025-11-10 | Cultural Landscape Team | Initial category structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscapes](../README.md)

</div>