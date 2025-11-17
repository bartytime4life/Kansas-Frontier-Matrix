---
title: "🪶🧬 Kansas Frontier Matrix — Protohistoric Wichita Interaction Sphere Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Sovereignty Advisory Board (Mandatory)"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-protohistoric-wichita-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced (High Sensitivity)"
doc_kind: "Provenance Index"
intent: "protohistoric-wichita-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-High-Sensitivity"
---

<div align="center">

# 🪶🧬 **Protohistoric Wichita Interaction Sphere — Provenance Logs**
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/README.md`

**Purpose:**  
Provide the authoritative **provenance documentation** for the **Protohistoric Wichita Interaction Sphere**, a culturally sensitive dataset requiring **mandatory tribal review**, full CARE compliance, and rigorous FAIR+CARE auditability.  
These provenance records ensure transparent lineage tracking for all raw → generalized → processed transformations.

</div>

---

## 📘 Overview

The provenance logs capture:

- Original data sources (PD + tribal-approved content)
- GIS generalization workflows (H3-only)
- Removal of sensitive cultural knowledge
- Ethical + cultural review procedures
- Tribal review sign-off (required)
- FAIR+CARE audit metadata
- Cultural risk assessment
- Versioned lineage (PROV-O JSON-LD)
- Script, tool, and environment metadata
- Data transformation reproducibility

This dataset is **high-sensitivity** and cannot be included in any public KFM release without **complete tribal approval**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/
├── README.md
└── protohistoric-wichita-v1.json
~~~

---

# 🧩 Required PROV-O Components

Each provenance file must adhere to the PROV-O JSON-LD specification and KFM provenance rules.

---

## ✔ `@context`

Must define:

- `prov` — W3C PROV-O vocabulary  
- `care` — Cultural-sensitivity extension  
- `kfm` — KFM archaeology metadata vocabulary  
- `dct` — DCAT terms  
- `crm` — (Optional) CIDOC-CRM mapping  

---

## ✔ `prov:Entity`

Required:

| Entity | Description |
|---|---|
| **raw** | PD + tribal-approved input materials |
| **generalized** | H3-6/7 generalized output (mandatory) |
| **processed** | Final published KFM-compatible dataset |
| **interpretive** | (Optional) generated cultural synthesis layers |

### Forbidden in `raw`:
- Exact settlement coordinates  
- Ceremonial/sacred geography  
- Unapproved oral histories  
- Restricted ethnographic content  
- High-resolution archaeological data  

---

## ✔ `prov:Activity`

Activities must document all transformations, including:

| Activity | Description |
|---|---|
| `generalization` | H3 mosaic generation, polygon suppression |
| `filtering` | Removal of sensitive variables |
| `cleaning` | Data normalization, CRS standardization |
| `integration` | Combining multi-source PD + tribal-approved content |
| `tribal_review` | Required phase verifying cultural safety |
| `faircare_review` | Ethical oversight by FAIR+CARE Council |

Activity metadata must include:

- `prov:type`
- `prov:startTime`
- `prov:endTime`
- `kfm:steps` (array describing pipeline actions)

---

## ✔ `prov:Agent`

Agents represent responsible contributors:

| Type | Required |
|---|---|
| Analyst | GIS or archaeology specialist |
| Tribal Reviewer | **Required** for dataset approval |
| FAIR+CARE Reviewer | Required |
| Source Institution | If applicable |

Agents must follow privacy/sovereignty guidelines.

---

## ✔ Lineage Relationships

Each provenance file MUST include:

- `prov:wasDerivedFrom`
- `prov:wasGeneratedBy`
- `prov:used`
- `prov:wasAttributedTo`

These describe the complete lineage of dataset creation.

---

# ⚖️ CARE Cultural-Safety Protocols

This dataset is rated **restricted-generalized**.

### Required

| Field | Value |
|---|---|
| `care:sensitivity` | `"restricted-generalized"` |
| `care:review` | `"tribal"` |
| `care:notes` | Must explain all cultural-safety decisions |
| `care:visibility_rules` | `"h3-only"` |

### Forbidden

- `"restricted"` classification  
- Any exact geometries  
- Polygon boundaries  
- Sensitive oral histories without approval  
- Any non-generalized spatial features  

---

# 🧪 Example PROV-O Record (Excerpt)

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
      "prov:type": "Dataset",
      "prov:label": "Protohistoric Wichita synthesis (PD + tribal-approved)",
      "kfm:source": "Ethnohistoric summaries approved for public generalized use"
    },
    "generalized": {
      "prov:type": "Dataset",
      "prov:label": "H3-only generalized dataset (level 7)",
      "care:notes": "Removed ceremonial references, precise pathways, and sacred knowledge."
    },
    "processed": {
      "prov:type": "Dataset",
      "prov:label": "Protohistoric Wichita Interaction Sphere v1",
      "kfm:provenance_version": "v1"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-18T10:32:00Z",
      "prov:endTime": "2025-10-18T11:12:00Z",
      "kfm:steps": [
        "H3 mosaic generation (level 7)",
        "polygon suppression",
        "boundary smoothing",
        "removal of sensitive cultural features"
      ]
    },
    "tribal_review": {
      "prov:type": "Review",
      "prov:endTime": "2025-10-20T17:40:00Z",
      "kfm:steps": [
        "Ethical content inspection",
        "Ancestral sovereignty compliance",
        "Approval for generalized-only release"
      ]
    }
  },
  "prov:Agent": {
    "analyst": { "prov:label": "A. Barta", "prov:type": "Person" },
    "tribal": { "prov:label": "Tribal Sovereignty Advisory Board", "prov:type": "Group" },
    "faircare": { "prov:label": "FAIR+CARE Council", "prov:type": "Group" }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "restricted-generalized",
  "care:review": "tribal",
  "care:notes": "Dataset generalized using H3; all sensitive content removed."
}
~~~

---

# 🧠 KFM Knowledge Graph Integration

### Nodes Created
- InteractionSphere  
- CulturalPhase  
- GeneralizedRegion  
- CulturalSensitivityLevel  
- MetadataRecord  
- ProvenanceActivity  
- ReviewEvent  

### Relationships Formed
- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  
- `GENERALIZED_FROM`  
- `REVIEWED_BY`  
- `OCCURRED_DURING`  
- `ASSOCIATED_WITH`  

These relationships ensure strong temporal alignment, cultural-sovereign compliance, and interpretive clarity across KFM.

---

# 🎛️ Story Nodes & Focus Mode Integration

- Powers Protohistoric Wichita storyline modules  
- Triggers sovereignty warnings  
- Displays provenance chips  
- Enforces H3-only rendering  
- Provides contextual interpretive overlays  
- Carries uncertainty & ethical metadata into Focus Mode  

---

# 📊 Dataset Status Summary

| Field | Value |
|---|---|
| Version | v1 |
| Sensitivity | restricted-generalized |
| Review | Tribal (mandatory) |
| Spatial Visibility | H3-only |
| Provenance | Complete |
| FAIR+CARE | Verified |
| Publication | 🟡 Pending tribal approval |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | Initial high-sensitivity provenance documentation |
| v0.1 | 2025-11-12 | Landscape Provenance Team | Prototype lineage and generalization workflow |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Tribal Oversight Required · FAIR+CARE Governance  
MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Protohistoric Wichita Dataset](../README.md)

</div>