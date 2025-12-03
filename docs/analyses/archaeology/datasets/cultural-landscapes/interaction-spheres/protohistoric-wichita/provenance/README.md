---
title: "🪶🧬 Kansas Frontier Matrix — Protohistoric Wichita Interaction Sphere Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/README.md"
description: "High-sensitivity PROV-O + CARE provenance logs for the Protohistoric Wichita interaction-sphere dataset in KFM v11, documenting lineage, generalization, and sovereignty-aligned review."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Sovereignty Advisory Board (Mandatory)"
content_stability: "stable"
status: "Active / Enforced (High Sensitivity · Tribal Review Required)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:protohistoric-wichita-interaction-sphere-provenance-v11.2.3"
doc_kind: "Provenance Index"
intent: "protohistoric-wichita-provenance"
semantic_document_id: "kfm-doc-archaeology-protohistoric-wichita-interaction-sphere-provenance-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Provenance"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-protohistoric-wichita-provenance-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Sovereignty Advisory Board"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🪶🧬 Protohistoric Wichita Interaction Sphere — Provenance Logs (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/README.md`

**Purpose**  
Provide the **authoritative provenance documentation** for the **Protohistoric Wichita Interaction Sphere**, a high-sensitivity cultural-landscape dataset requiring **mandatory tribal review**, full CARE compliance, and rigorous FAIR+CARE auditability.

These provenance logs ensure **transparent lineage tracking** for all **raw → generalized → processed** transformations, and anchor Story Nodes, Focus Mode, and graph ingestion in a governed evidence trail.

---

## 📘 Overview

The Protohistoric Wichita interaction-sphere provenance logs capture:

- Original data sources (public-domain + tribally approved content).  
- GIS processing and generalization workflows (H3-based and polygon simplification).  
- Removal and masking of sensitive cultural knowledge.  
- Ethical and cultural review procedures, including mandatory tribal review.  
- FAIR+CARE audit metadata and cultural risk assessments.  
- Versioned lineage using **PROV-O JSON-LD** plus KFM extensions.  
- Script, tool, and environment metadata for reproducible transformations.

Given the **high sensitivity** of this dataset, it must **not** be included in any public-facing KFM release without **documented and current tribal approval**.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/provenance/
├── 📄 README.md                               # This file
└── 📄 protohistoric-wichita-v2.json           # PROV-O lineage & tribal review record (v2)
~~~

Additional provenance files (for prior versions or internal-only datasets) may be added as versioned JSON-LD, but v2 is the authoritative record in KFM v11.

---

## 🧩 Required PROV-O & JSON-LD Components

All provenance logs MUST:

- Be valid **JSON-LD**.  
- Conform to **PROV-O** and KFM provenance schemas.  
- Include CARE and sovereignty metadata at the record level.

### 1️⃣ `@context`

Provenance logs must define at least:

- `"prov"` — `http://www.w3.org/ns/prov#`  
- `"care"` — CARE extension namespace for KFM  
- `"kfm"` — KFM core/extension namespace  
- `"dct"` — `http://purl.org/dc/terms/` (for DCAT-aligned fields)  

Optional:

- `"crm"` — CIDOC-CRM mapping (when advanced heritage semantics are used).

---

### 2️⃣ `prov:Entity`

Entities must represent the main dataset states:

| Entity Key     | Description                                               |
|----------------|-----------------------------------------------------------|
| `raw`          | PD + tribal-approved inputs (not including raw sensitive details) |
| `generalized`  | H3/generalized, masked representation (mandatory)        |
| `processed`    | Final KFM-ready dataset used by STAC Item(s)             |
| `interpretive` | (Optional) model-based or synthetic interpretive layers   |

Restrictions:

- `raw` MUST NOT include:
  - Exact settlement coordinates.  
  - Ceremonial or sacred geographies.  
  - Unapproved oral histories or restricted ethnographic content.  
  - High-resolution archaeological site data.

Typical entity fields:

- `prov:type` = `"Dataset"`  
- `prov:label` = human-readable label  
- `kfm:source` and `kfm:provenance_version` as appropriate  

---

### 3️⃣ `prov:Activity`

Activities must document each transformation and review step, for example:

| Activity Key       | Description                                            |
|--------------------|--------------------------------------------------------|
| `generalization`   | H3 mosaic generation, polygon simplification, masking |
| `filtering`        | Removal of sensitive attributes or features           |
| `cleaning`         | Data normalization, CRS standardization               |
| `integration`      | Multi-source synthesis (archaeology + ethnohistory)   |
| `tribal_review`    | Required tribal/sovereignty review                    |
| `faircare_review`  | FAIR+CARE council review                              |

Each `prov:Activity` must record:

- `prov:type`  
- `prov:startTime` and `prov:endTime` (ISO 8601)  
- `kfm:steps` — ordered list of descriptive step labels  

---

### 4️⃣ `prov:Agent`

Agents represent people and organizations responsible for creation, review, and governance.

Required agent types:

| Type              | Examples                                      |
|-------------------|-----------------------------------------------|
| Analyst           | GIS specialist, archaeologist                 |
| Tribal Reviewer   | Tribal Sovereignty Advisory Board members     |
| FAIR+CARE Reviewer| FAIR+CARE Council participants                |
| Source Institution| KHS, tribal archives, university repositories |

Agent entries should respect privacy and sovereignty guidelines (for example, using roles or groups when individual names are not appropriate).

---

### 5️⃣ Lineage Relationships

Each provenance file must define core PROV-O relations:

- `prov:wasDerivedFrom` — link `raw → generalized → processed`.  
- `prov:wasGeneratedBy` — link entities to the activities producing them.  
- `prov:used` — link activities to the entities they consume.  
- `prov:wasAttributedTo` — attribute entities to agents (analysts, reviewers, institutions).

These relations jointly describe the reproducible lineage of the dataset.

---

## ⚖️ CARE & Sovereignty Requirements

This interaction-sphere dataset is rated **restricted-generalized** under CARE.

### Required CARE Fields (Top-Level)

| Field                | Expected Value / Behavior                                |
|----------------------|---------------------------------------------------------|
| `care:sensitivity`   | `"restricted-generalized"`                               |
| `care:review`        | `"tribal"` (and FAIR+CARE where applicable)             |
| `care:notes`         | Required; explains cultural-safety and sovereignty decisions |
| `care:visibility_rules` | `"h3-only"` (or stricter) for public-facing outputs |

Forbidden for public provenance:

- `care:sensitivity = "restricted"`  
- Any indication that reveals exact sacred or ceremonial locations.  
- Direct inclusion of restricted oral histories without explicit consent.  

CARE fields in provenance must be consistent with CARE fields in:

- STAC Item: `../stac/items/protohistoric-wichita-v2.json`  
- DCAT/metadata: `../metadata/protohistoric-wichita-v2.json`

---

## 🧪 Example PROV-O Record (Excerpt)

Illustrative excerpt of a governed provenance log:

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
      "prov:label": "Protohistoric Wichita synthesis (PD + tribal-approved sources)",
      "kfm:source": "Ethnohistoric summaries and archaeological syntheses approved for generalized use"
    },
    "generalized": {
      "prov:type": "Dataset",
      "prov:label": "H3-generalized interaction sphere (level 7)",
      "care:notes": "Removed ceremonial references, precise pathways, and sacred knowledge prior to H3 aggregation."
    },
    "processed": {
      "prov:type": "Dataset",
      "prov:label": "Protohistoric Wichita Interaction Sphere v2",
      "kfm:provenance_version": "v2"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "SpatialGeneralization",
      "prov:startTime": "2025-10-18T10:32:00Z",
      "prov:endTime": "2025-10-18T11:12:00Z",
      "kfm:steps": [
        "H3 mosaic generation (level 7)",
        "polygon simplification",
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
        "Approval for generalized-only use in governed catalog"
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
  "care:notes": "Dataset generalized using H3; all sensitive cultural content removed or masked before public catalog inclusion.",
  "care:visibility_rules": "h3-only"
}
~~~

Actual provenance files must also satisfy KFM provenance schemas and pass CI validation.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

From this dataset, provenance logs drive creation of:

**Nodes**

- `InteractionSphere` (Protohistoric Wichita)  
- `GeneralizedRegion` entities  
- `ProvenanceActivity` nodes (generalization, review, cleaning, etc.)  
- `ReviewEvent` nodes (FAIR+CARE and tribal reviews)  
- CARE-related nodes (for example, `CareSensitivityState`)

**Relationships**

- `HAS_PROVENANCE` (InteractionSphere → ProvenanceRecord)  
- `GENERALIZED_FROM` (Processed ↔ Generalized ↔ Raw entities)  
- `REVIEWED_BY` (ProvenanceRecord → Agents)  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE state)  
- `ASSOCIATED_WITH` (InteractionSphere ↔ supporting datasets and narratives)

### Story Nodes & Focus Mode v3

- Provenance logs back Story Nodes and Focus Mode:

  - Provide provenance chips and ethical context.  
  - Control narrative scope and sensitivity-aware phrasing.  
  - Drive warnings, notes, and “about this data” sections.

---

## 🔗 Related Specifications

- `../README.md`  
  – Protohistoric Wichita interaction-sphere dataset overview.  
- `../stac/README.md`  
  – Protohistoric Wichita STAC Collection documentation.  
- `../stac/items/README.md`  
  – Protohistoric Wichita STAC Item documentation.  
- `../metadata/README.md`  
  – DCAT + CARE metadata for Protohistoric Wichita.  
- `../../provenance/README.md`  
  – Global interaction-sphere provenance standards and QA templates.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Sovereignty Advisory Board | Updated to KFM v11.2.3; aligned with global interaction-sphere provenance; added telemetry refs and clarified CARE/sovereignty semantics. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisors | Initial high-sensitivity provenance documentation for Protohistoric Wichita interaction sphere. |
| v10.0.0   | 2025-11-12 | Landscape Provenance Team                         | Prototype lineage and generalization workflows.                        |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Protohistoric Wichita Dataset](../README.md)
