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
Serve as the authoritative provenance catalog for the **Protohistoric Wichita Interaction Sphere**, a **high-sensitivity** cultural dataset requiring the strictest cultural governance within the Kansas Frontier Matrix (KFM).  
This directory contains validated **PROV-O JSON-LD lineage records** documenting all transformations, ethical decisions, tribal-review checkpoints, and generalization steps applied to the dataset.

</div>

---

## 📘 Overview

The provenance logs here describe:

- Raw inputs used in constructing the interaction sphere  
- Generalization (H3-level ≥6, polygon → H3-only conversion)  
- Removal of sacred, ceremonial, or descendant-relevant content  
- Tribal advisory review outcomes (required)  
- FAIR+CARE oversight details  
- All GIS processing and metadata generation  
- Versioning and lineage from raw → generalized → processed datasets  
- Cultural risk assessment notes  
- Ethical decision pathways recorded for audit and transparency  

This dataset is **high sensitivity**.  
Provenance is not merely optional—it is **mandatory**, and all updates must pass:

- Tribal Review  
- FAIR+CARE review  
- MCP-DL v6.3 documentation-first governance  
- KFM-MDP v10.4 formatting verification  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/
├── README.md
└── protohistoric-wichita-v1.json
~~~

---

# 🧩 Required PROV-O Structure

All provenance logs for the Protohistoric Wichita sphere must include the following PROV-O components:

---

## ✔ `@context` (Mandatory)

Must define:

- `prov` — W3C PROV-O ontology  
- `care` — CARE cultural-safety extension  
- `kfm` — KFM archaeology extension  
- `dct` — DCAT crosswalk  
- `crm` — (optional) CIDOC-CRM alignment  

---

## ✔ `prov:Entity`

Required entity definitions:

| Entity | Description |
|---|---|
| **raw** | Raw, public-domain, or tribal-approved content used as input |
| **generalized** | H3-mosaic output with all sensitive details removed |
| **processed** | Final validated dataset used by KFM |
| **interpretive** | (Optional) synthetic/harmonized cultural models |

The **raw** entity **must never** include:

- Exact village/settlement coordinates  
- Sacred or ceremonial areas  
- Restricted tribal knowledge  
- Highly specific ethnohistorical detail  

---

## ✔ `prov:Activity`

Activities must trace all processing, including:

| Activity | Description |
|---|---|
| `generalization` | Converting polygons → H3-only mosaic, removing all spatially sensitive detail |
| `cleaning` | Data harmonization, CRS enforcement, type normalization |
| `ethics_review` | FAIR+CARE ethical audit of dataset |
| `tribal_review` | Mandatory review by affiliated tribal nation(s) |
| `integration` | Combining archaeological, ecological, and ethnohistoric sources |
| `filtering` | Removing or masking high-risk cultural information |

Each activity must contain:

- `prov:type`  
- `prov:startTime`  
- `prov:endTime`  
- `kfm:steps` (array of procedural steps)  

---

## ✔ `prov:Agent`

Agents must represent:

| Agent Type | Required |
|---|---|
| Analyst | GIS/archaeology specialist |
| FAIR+CARE Reviewer | Yes |
| Tribal Reviewer | **Mandatory** |
| Source Institution | If applicable |

Agent identities must be provided according to FAIR+CARE privacy and sovereignty rules.

---

## ✔ Lineage Relationships

Every provenance file must include:

- `prov:wasDerivedFrom` — raw → generalized → processed  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  

These describe the full transformation lineage.

---

# ⚖️ CARE Cultural Safety Requirements

The Protohistoric Wichita dataset is classified as **restricted-generalized**, the highest allowed level for public release.

### Required CARE fields:

| Field | Value |
|---|---|
| `care:sensitivity` | `"restricted-generalized"` |
| `care:review` | `"tribal"` |
| `care:notes` | Documenting all removed/filter content and rationale |
| `care:visibility_rules` | `"h3-only"` |

### Forbidden:

- `"restricted"`  
- Exact cultural boundaries  
- Precise movement corridors  
- Any sacred/ceremonial spatial information  
- Ethnohistoric content lacking explicit tribal approval  

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
      "prov:type": "Dataset",
      "prov:label": "Protohistoric Wichita synthesis (PD + tribal-approved)",
      "kfm:source": "Open literature synthesis + tribal-approved summaries"
    },
    "generalized": {
      "prov:type": "Dataset",
      "prov:label": "H3 generalized dataset (level 7)",
      "care:notes": "Removed ceremonial references; H3 mosaic used for all geometries."
    },
    "processed": {
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1",
      "prov:label": "Protohistoric Wichita Interaction Sphere v1"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-18T10:32:00Z",
      "prov:endTime": "2025-10-18T11:12:00Z",
      "kfm:steps": [
        "H3 mosaic (level 7)",
        "polygon removal",
        "boundary smoothing",
        "sensitive-feature filtering"
      ]
    },
    "tribal_review": {
      "prov:type": "Review",
      "prov:endTime": "2025-10-20T17:40:00Z",
      "kfm:steps": [
        "Ethical content verification",
        "Approval for generalized-only release",
        "Cultural risk assessment"
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

Nodes created:

- `InteractionSphere`  
- `