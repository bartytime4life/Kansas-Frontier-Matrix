---
title: "🏺 Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset"
intent: "cultural-landscape-interaction-sphere-great-bend-aspect"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🏺 **Great Bend Aspect Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/README.md`

**Purpose:**  
Define, document, and ethically govern the **Great Bend Aspect Interaction Sphere**, a major Late Prehistoric–Protohistoric cultural landscape spanning central Kansas and associated with the ancestors of the **Wichita** and related Plains horticultural groups.

This dataset integrates archaeological, geomorphological, ecological, and ethnohistoric evidence into a **generalized, culturally safe interaction region** compatible with KFM’s FAIR+CARE governance standards.

</div>

---

# 📘 Overview

The **Great Bend Aspect (GBA)** represents a cohesive cultural complex typically dated to **AD 1350–1700**, characterized by:

- Distinctive ceramic traditions  
- Semi-sedentary horticultural settlements  
- Bison hunting & mixed subsistence practices  
- Earthlodge/grass house architectural patterns  
- Extensive trade networks (stone, shell, metal in late phases)  
- Regional cultural interaction with Central Plains, southern Plains, and protohistoric European trade corridors  

The GBA is modeled here as a **generalized interaction sphere**, not an exact territorial boundary.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/
├── README.md                               # This file
├── great-bend-aspect.geojson               # Generalized MultiPolygon representation
├── stac/                                   
│   └── great-bend-aspect-v2.json           # STAC Item (generalized)
├── metadata/
│   └── great-bend-aspect-v2.json           # DCAT + CARE metadata
└── provenance/
    └── great-bend-aspect-v2.json           # PROV-O lineage & ethics review
~~~

---

# 🧭 Cultural Definition

### Cultural Cohesion
- Highly consistent ceramics (Ninnescah, Pratt, Quivira variants—generalized)  
- Shared house forms & subsistence strategies  
- Dense occupation along Arkansas River valley and tributaries  

### Interaction & Exchange
- Trade networks connecting southern Plains, Central Plains, and protohistoric contacts  
- Shared features with earlier Plains Woodland and Central Plains Tradition  

### Environmental Setting
- Prairie–riparian interface  
- Hydrologically rich valley systems  
- Ecotonal transitions influencing subsistence & settlement  

---

# 🌍 Spatial Representation

The dataset includes:

- A **generalized MultiPolygon** representing probable cultural–interaction extent  
- H3 mosaic (levels 5–7) to preserve confidentiality  
- Generalization applied to:
  - Settlement clusters  
  - Excavation locations  
  - Sacred or sensitive ethnographic sites  

CRS: **EPSG:4326**  
No exact site coordinates included.

---

# 🕰️ Temporal Context

| Sub-Phase | Approx. Dates | Notes |
|---|---|---|
| Early GBA | AD 1350–1450 | Emergent ceramic/architectural patterns |
| Middle GBA | AD 1450–1600 | Peak settlement density + trade networks |
| Late GBA / Protohistoric | AD 1600–1700 | Increased European contact; high sensitivity |

OWL-Time metadata appears in STAC + DCAT.

---

# 📦 STAC Item Overview (Excerpt)

~~~json
{
  "id": "great-bend-aspect-v2",
  "type": "Feature",
  "stac_version": "1.0.0",
  "bbox": [-101.8, 37.0, -95.3, 40.5],
  "properties": {
    "kfm:culture_phase": ["GBA-Early", "GBA-Middle", "GBA-Late"],
    "care:sensitivity": "generalized",
    "kfm:provenance": "../provenance/great-bend-aspect-v2.json"
  }
}
~~~

Full STAC Item located in `stac/`.

---

# ⚖️ Cultural & Ethical Governance (FAIR+CARE)

The Great Bend Aspect holds significant meaning for Wichita descendants and other Indigenous nations.

### Required Protections  
- **No exact settlement locations**  
- **No ceremonial site representation**  
- **Generalized archaeological boundaries only**  
- **No colonial interpretive framings**  
- **Culturally respectful narrative language**  
- **Tribal review recommended for protohistoric features**

### CARE Fields (as required by schema)
- `care:sensitivity: "generalized"`  
- `care:review: "faircare"` (or `"tribal"` for later-period data)  
- `care:notes` explaining spatial + cultural generalizations  
- `care:visibility_rules: "polygon-generalized"` for map layers  

---

# 🧪 Provenance Requirements (PROV-O)

Provenance logs document:

- Source literature & datasets (public-domain only)  
- GIS steps (polygon simplification, H3 grid construction)  
- Interpretive synthesis standards  
- Cultural review and ethical audit outcomes  
- Schema versioning & processing timestamps  
- All generalization + obfuscation methods  

Provenance file:  
`provenance/great-bend-aspect-v2.json`

---

# 🧠 Integration Into KFM

### Knowledge Graph Nodes
- `InteractionSphere`  
- `CulturalPhase`  
- `CulturalRegion`  
- `EnvironmentalZone`  

### Relationships
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  
- `CONNECTS_TO`  
- `OCCURRED_DURING`  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  

### Story Nodes
- Foundation for Great Bend–related cultural narratives  
- Integration with artifact inventories, routes, regions  

### Focus Mode v2
- Spatial overlays  
- Cultural-network explanations  
- Ethical prompt enforcement  
- Provenance-chip transparency  

---

# 📊 Dataset Status

| Version | Status | Review | Notes |
|---|---|---|---|
| v2 | 🟢 Active | 2025-11 | Generalized; CARE-reviewed; STAC/DCAT compliant |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v2 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Updated generalization, metadata, STAC compliance |
| v1 | 2025-11-10 | Landscape Modeling Team | Initial draft with early polygon model |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Interaction Spheres](../README.md)

</div>