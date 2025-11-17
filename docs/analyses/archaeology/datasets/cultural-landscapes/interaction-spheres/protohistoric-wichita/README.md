---
title: "🪶 Kansas Frontier Matrix — Protohistoric Wichita Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review Required"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-protohistoric-wichita-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced (Tribal Review Required)"
doc_kind: "Dataset"
intent: "cultural-landscape-interaction-sphere-protohistoric-wichita"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-High-Sensitivity"
---

<div align="center">

# 🪶 **Protohistoric Wichita Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/README.md`

**Purpose:**  
Define, document, and ethically govern the **Protohistoric Wichita Interaction Sphere**, a culturally sensitive, multi-layered interaction region emerging in the **AD 1500–1700** period, during which ancestral Wichita groups engaged in widespread mobility, trade, diplomacy, and early European contact.

This dataset is treated with **high cultural sensitivity**, requiring **mandatory tribal review** under CARE governance.

</div>

---

# ⚠️ Cultural Sensitivity Statement

The Protohistoric Wichita Interaction Sphere contains culturally significant, descendant-community–relevant information.  
It includes historically sensitive contexts related to:

- Early contact  
- Migration  
- Ceremonial interactions  
- Trade and diplomacy  
- Possible conflict and displacement  

Therefore:

- **No exact settlement, burial, ceremonial, or sacred locations** are included.  
- All geometries are highly **generalized** (polygon simplification + H3 mosaic).  
- **Tribal review is required** before publication or modification.  
- Narrative framing must avoid colonial-era biases and harmful terminology.

---

# 📘 Overview

The **Protohistoric Wichita Sphere** represents an evolving cultural region bridging:

- Late Great Bend Aspect continuity  
- Emerging protohistoric Wichita identities  
- Interaction with Plains Apache, Caddoan groups, and early European expeditions  
- Shifting settlement patterns along the **Arkansas**, **Walnut**, **Ninnescah**, and **Little Arkansas** Rivers  
- Expanding trade networks (metal, shell, pigment, stone)  
- Oral histories (included only in high-level generalized form, if approved)

This dataset models a *generalized cultural landscape*, not a territorial claim or boundary.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/
├── README.md                                 # This file
├── protohistoric-wichita.geojson             # Generalized MultiPolygon (H3-7 mosaic)
├── stac/
│   └── protohistoric-wichita-v1.json         # STAC Item for this interaction sphere
├── metadata/
│   └── protohistoric-wichita-v1.json         # DCAT + CARE metadata
└── provenance/
    └── protohistoric-wichita-v1.json         # PROV-O lineage & tribal review record
~~~

---

# 🧭 Cultural Definition

### Cultural Identity
- Late Great Bend Aspect descendants  
- Emerging Wichita-speaking communities  
- Interactions with Caddoan, Plains Apache, proto-Pawnee groups  

### Subsistence & Economy
- Mixed horticulture (maize, beans, squash)  
- Bison hunting (communal + opportunistic)  
- Seasonal mobility between prairie, riparian, and wooded ecotones  

### Trade & Diplomacy
- Broad exchange networks (stone, metal, pigments)  
- Contact with early Spanish expeditions (high-sensitivity topic)  
- Riverine mobility corridors connecting settlement clusters  

---

# 🌍 Spatial Representation

This dataset uses:

- **Generalized MultiPolygon** shapes  
- **H3 generalization (levels 5–7)**  
- Avoids:
  - Site-level detail  
  - Sacred landscape geometry  
  - Exact settlement patterning  

CRS: **EPSG:4326**

Generalization protects culturally sensitive insights.

---

# 🕰️ Temporal Context

| Phase | Approx. Dates | Notes |
|---|---|---|
| Early Protohistoric | AD 1500–1580 | Transition from Late Prehistoric patterns |
| Middle Protohistoric | AD 1580–1650 | Highest mobility + trade activity |
| Late Protohistoric | AD 1650–1700 | Reorganization under colonial pressures |

Temporal metadata fully encoded in DCAT + STAC.

---

# 📦 STAC Item Summary (Excerpt)

~~~json
{
  "id": "protohistoric-wichita-v1",
  "stac_version": "1.0.0",
  "type": "Feature",
  "bbox": [-102.2, 36.8, -94.7, 40.6],
  "properties": {
    "kfm:culture_phase": ["Protohistoric-Wichita"],
    "care:sensitivity": "restricted-generalized",
    "care:review": "tribal",
    "kfm:provenance": "../provenance/protohistoric-wichita-v1.json"
  }
}
~~~

Full STAC metadata is located in `/stac/`.

---

# ⚖️ FAIR+CARE Cultural Governance

### Required Protections
- **Tribal review mandatory** for dataset creation/modification  
- **No depiction of sensitive ceremonial geographies**  
- **Strict generalization** (H3 + polygon simplification)  
- **No colonial terminology**  
- **Culturally contextual narratives only**  
- **Ethical disclaimers included in metadata**

### CARE Fields (required)
- `care:sensitivity: "restricted-generalized"`  
- `care:review: "tribal"`  
- `care:notes`: Must document cultural review outcomes  
- `care:visibility_rules: "h3-only"` for public-facing layers  

---

# 🧪 Provenance Requirements (PROV-O)

Provenance logs must describe:

- Data origins (literature, PD datasets, approved oral histories)  
- GIS generalization steps  
- Cultural/tribal review summary  
- Ethical considerations  
- Model assumptions & uncertainties  
- Processing timestamps  
- Analyst + reviewer identities  

Stored as:  
`provenance/protohistoric-wichita-v1.json`

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Nodes
- `InteractionSphere`  
- `CulturalPhase`  
- `EnvironmentalZone`  
- `CulturalRegion`  

### Relationships
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  
- `OCCURRED_DURING`  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  

### Story Nodes
Supports:
- Protohistoric movement narratives  
- Cultural diffusion sequences  
- Diplomatic/trade network explanations  

### Focus Mode v2
- Applies ethical warning banners  
- Provides provenance chips  
- Interprets uncertainty in generalized cultural regions  

---

# 📊 Dataset Status

| Version | Status | Review | Notes |
|---|---|---|---|
| v1 | 🟡 Needs Review | Tribal Review Required | High-sensitivity dataset; cannot be public-facing until review completed |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | First standardized version of Protohistoric Wichita Interaction Sphere |
| v0.1 | 2025-11-12 | Landscape Modeling Team | Generalized polygon prototype |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Tribal Review Required  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Interaction Spheres](../README.md)

</div>