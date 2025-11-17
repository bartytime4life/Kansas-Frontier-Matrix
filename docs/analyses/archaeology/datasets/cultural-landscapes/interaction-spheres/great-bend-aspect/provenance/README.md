---
title: "🏺🧬 Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review Recommended"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Provenance Record Index"
intent: "great-bend-aspect-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Elevated Sensitivity)"
---

<div align="center">

# 🏺🧬 **Great Bend Aspect Interaction Sphere — Provenance Logs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/README.md`

**Purpose:**  
Serve as the complete **provenance record index** for the **Great Bend Aspect (GBA) Interaction Sphere**, documenting all transformations, cultural reviews, generalizations, and ethical safeguards applied in the production of this culturally sensitive dataset.

Great Bend Aspect datasets contain **Late Prehistoric + Protohistoric** components tied to ancestral **Wichita** peoples; therefore additional **CARE review** and **optional Tribal advisory review** are recommended for transparency and cultural safety.

</div>

---

# 📘 Overview

The provenance logs in this folder record:

- Dataset origin and citations  
- Spatial generalization processes (H3 mosaic, polygon simplification)  
- Cultural phase synthesis  
- Ethical and CARE reviews  
- Tribal advisory consult notes (if applicable)  
- Uncertainty statements and interpretive limitations  
- Lineage from raw → generalized → processed representations  
- All FAIR+CARE compliance actions and ethical guardrails  

These logs use **PROV-O JSON-LD** to ensure machine readability, graph compatibility, and reproducibility.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/
├── README.md                                 # This file
└── great-bend-aspect-v2.json                 # PROV-O lineage & cultural review metadata
~~~

---

# 🧩 Required PROV-O Components for GBA Provenance

### ✔ `@context`
Must include:
- `"prov"` — PROV-O core ontology  
- `"care"` — CARE cultural-sensitivity extension  
- `"kfm"` — KFM archaeology metadata  
- `"crm"` — Optional CIDOC-CRM alignment  
- `"dct"` — DCAT crosswalk  

---

### ✔ `prov:Entity`

Required entities:

| Entity | Description |
|---|---|
| `raw` | Aggregated public-domain archaeological synthesis (no restricted data) |
| `generalized` | Spatially obfuscated form (H3-level-6, polygon simplification) |
| `processed` | Final dataset used in KFM | 
| `interpretive` | (Optional) cultural synthesis layer |

---

### ✔ `prov:Activity`

Must include:

| Activity | Purpose |
|---|---|
| `generalization` | H3 mosaic + simplification; essential for cultural safety |
| `cleaning` | Harmonization of attributes, CRS, naming |
| `integration` | Multi-source archaeological & environmental synthesis |
| `ethics_review` | FAIR+CARE compliance review |
| `tribal_advisory_review` | Optional but recommended for protohistoric components |

Each activity must include:

- `prov:startTime`  
- `prov:endTime`  
- `prov:type`  
- `kfm:steps`  

---

### ✔ `prov:Agent`

Agents represent:

| Type | Example |
|---|---|  
| Analyst | GIS/archaeology specialist |
| FAIR+CARE Reviewer | KFM Ethics Council |
| Tribal Reviewer (Optional) | Wichita-affiliated tribal heritage office |
| Source Institution | Public domain archival/literature sources |

---

### ✔ Lineage Relationships

Mandatory provenance relationships:

- `prov:wasDerivedFrom`  
- `prov:used`  
- `prov:wasGeneratedBy`  
- `prov:wasAttributedTo`

These ensure dataset lineage from **raw → generalized → processed**.

---

# ⚖️ CARE Cultural Safety Requirements

GBA contains **elevated cultural sensitivity**, especially for protohistoric contexts.

### Required:
- `care:sensitivity = "generalized"`  
- `care:review = "faircare"`  
- `care:notes` describing removed/filtered or culturally sensitive content  
- `care:visibility_rules = "polygon-generalized"` or `"h3-only"`  

### Recommended:
- Tribal advisory review for protohistoric (AD 1600–1700) components

### Forbidden:
- `"restricted"`  
- Exact site coordinates  
- Sacred or ceremonial landscape outlines  
- Unapproved ethnohistoric content  

---

# 🧪 Example Provenance Snippet (Excerpt)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#",
    "dct": "http://purl.org/dc/terms/"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Late Prehistoric GBA synthesis from PD archaeological literature",
      "prov:type": "Dataset"
    },
    "generalized": {
      "prov:label": "Generalized GBA polygon (H3-level-6)",
      "care:notes": "Exact settlement clusters removed; cultural safety protocols applied."
    },
    "processed": {
      "prov:label": "Great Bend Aspect Interaction Sphere v2",
      "kfm:provenance_version": "v2"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-14T13:12:00Z",
      "prov:endTime": "2025-10-14T13:55:00Z",
      "kfm:steps": ["H3 derivation", "polygon simplification", "boundary smoothing"]
    },
    "faircare_review": {
      "prov:type": "Review",
      "prov:endTime": "2025-10-15T17:30:00Z",
      "kfm:steps": ["ethical language audit", "sensitivity classification"]
    }
  },
  "prov:Agent": {
    "analyst": { "prov:type": "Person", "prov:label": "A. Barta" },
    "faircare": { "prov:type": "Group", "prov:label": "FAIR+CARE Council" }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare"
}
~~~

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph
Entities created:
- `InteractionSphere`
- `GeneralizedRegion`
- `CulturalPhase`
- `ReviewEvent`
- `ProvenanceActivity`

Edges:
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  
- `OCCURRED_DURING`  

### Story Nodes
Provenance informs:
- GBA cultural narratives  
- Temporal storylines  
- Ethical warning banners  

### Focus Mode v2
Uses provenance for:
- Interpretive transparency  
- Cultural-safety prompts  
- Provenance chips (user-visible evidence trails)

---

# 📊 Provenance Index

| Provenance File | Version | Sensitivity | Review | Status |
|---|---|---|---|---|
| `great-bend-aspect-v2.json` | v2 | generalized | FAIR+CARE (tribal recommended) | 🟢 Active |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v2 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Updated provenance documentation; applied enhanced CARE notes |
| v1 | 2025-11-10 | Landscape Provenance Team | Initial provenance entry |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Tribal Advisory Recommended  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Great Bend Aspect](../README.md)

</div>