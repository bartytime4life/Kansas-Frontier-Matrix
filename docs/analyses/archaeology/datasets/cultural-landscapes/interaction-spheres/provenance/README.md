---
title: "🧬 Kansas Frontier Matrix — Interaction Sphere Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/README.md"
description: "PROV-O + CARE JSON-LD provenance logs for KFM v11 interaction-sphere datasets, documenting lineage, generalization, and sovereignty-aligned review."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review (when required)"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-interaction-spheres-provenance-v11.2.3"
doc_kind: "Provenance Index"
intent: "interaction-sphere-provenance"
semantic_document_id: "kfm-doc-archaeology-interaction-spheres-provenance-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Provenance"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-provenance-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧬 Interaction Sphere Provenance Logs (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/README.md`

**Purpose**  
Serve as the **authoritative provenance index** for all interaction-sphere datasets in the Kansas Frontier Matrix (KFM) v11.

These logs document:

- Cultural interpretations and modeling assumptions  
- GIS processing and generalization steps  
- CARE and tribal/sovereignty review workflows  
- Dataset lineage from sources to KFM-ready layers  
- Ethical decisions and redaction choices  

Provenance is **mandatory** for every interaction-sphere dataset and is central to FAIR+CARE governance, transparency, reproducibility, and ethical AI interpretation (Story Nodes and Focus Mode v3).

---

## 📘 Overview

Interaction spheres represent culturally significant, multi-era networks of:

- Exchange and trade  
- Movement and mobility corridors  
- Social co-presence and overlapping use areas  
- Settlement interconnectivity and diffusion patterns  

Because they intersect sensitive cultural domains and multiple descendant communities, provenance logs must be:

- **Comprehensive** — covering raw, generalized, and processed states  
- **Machine-readable** — PROV-O JSON-LD with KFM + CARE extensions  
- **Ethically contextualized** — fully documenting review and redaction steps  
- **FAIR+CARE reviewed** — including tribal review where required  
- **Generalization-aware** — recording how precision was reduced  
- **Properly versioned** — for each dataset release (vN)

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/provenance/
├── 📄 README.md                         # This file (provenance index)
├── 📄 great-bend-aspect-v3.json         # Provenance for Great Bend Aspect interaction sphere
├── 📄 central-plains-exchange-v2.json   # Provenance for Central Plains exchange sphere
├── 📄 protohistoric-wichita-v2.json     # Provenance for Protohistoric Wichita corridor (high-sensitivity)
└── 📂 templates/                        # Templates for creating new provenance records
~~~

Each provenance file name (minus `.json`) should match the STAC Item ID stem and metadata/provenance conventions.

---

## 🧩 Required PROV-O & JSON-LD Components

All provenance logs MUST be valid **JSON-LD** with **PROV-O** semantics plus CARE and KFM extensions.

### 1️⃣ `@context`

Every log must define at least:

- `"prov"` — `http://www.w3.org/ns/prov#`  
- `"care"` — KFM CARE extension namespace  
- `"kfm"` — KFM core/extension namespace  

Optional, where relevant:

- `"dct"` — DCAT/DC metadata alignment  
- `"crm"` — CIDOC-CRM alignment for advanced use  

### 2️⃣ `prov:Entity`

Each provenance file must define entities capturing the main states of the dataset:

| Entity Key     | Notes                                                           |
|----------------|-----------------------------------------------------------------|
| `raw`          | Source/open data, literature synthesis, or pre-generalization state |
| `generalized`  | Spatially obfuscated version (H3 mosaic or simplified polygons) |
| `processed`    | Final KFM-ready dataset (referenced by STAC Item)              |
| `interpretive` | (Optional) explicitly modeled/synthetic representations         |

Each `prov:Entity` SHOULD include:

- `prov:label`  
- `prov:type` (for example, `"Dataset"`)  
- `kfm:source` (for `raw`) and `kfm:provenance_version` (for `processed`)  

### 3️⃣ `prov:Activity`

Activities represent processing, integration, review, and modeling steps, such as:

| Activity Key       | Description                                           |
|--------------------|-------------------------------------------------------|
| `cleaning`         | Attribute harmonization, schema normalization        |
| `generalization`   | H3 derivation, polygon simplification, masking       |
| `integration`      | Combining multiple data sources (archaeology + texts)|
| `ethics_review`    | FAIR+CARE + sovereignty review steps                 |
| `modeling`         | Environmental/diffusion modeling (if applicable)     |

Each `prov:Activity` must include:

- `prov:type`  
- `prov:startTime` (ISO 8601)  
- `prov:endTime` (ISO 8601)  
- `kfm:steps` — array of high-level processing steps  

### 4️⃣ `prov:Agent`

Agents represent people and organizations involved:

| Agent Type           | Examples                                     |
|----------------------|----------------------------------------------|
| Analyst              | GIS specialist, archaeologist                |
| FAIR+CARE Reviewer   | FAIR+CARE Council, independent reviewers     |
| Tribal Reviewer      | Tribal heritage office or advisory board     |
| Source Institution   | KHS, university repositories, PD archives    |

Typical properties:

- `prov:type` = `"Person"` or `"Organization"`  
- `prov:label`  
- Optionally `prov:actedOnBehalfOf` to show institutional relationships  

### 5️⃣ Lineage Relations

Minimum required PROV-O relations:

- `prov:wasDerivedFrom` — links `raw → generalized → processed`  
- `prov:wasGeneratedBy` — connects entities to activities that created them  
- `prov:used` — connects activities to prior entities or inputs  
- `prov:wasAttributedTo` — attributes entities to agents (analysts/reviewers)  

These relations form the **reproducible lineage chain** that underpins graph ingestion and audit trails.

---

## ⚖️ CARE & Sovereignty Requirements

Interaction-sphere datasets often cross sensitive cultural domains. Provenance logs must record the CARE and sovereignty context.

### Required CARE fields at provenance top-level

| Field                | Description / Rules                                      |
|----------------------|---------------------------------------------------------|
| `care:sensitivity`   | `"general"`, `"generalized"`, or `"restricted-generalized"` (no `"restricted"` in public catalog) |
| `care:review`        | `"faircare"`, `"tribal"`, or `"none-required"`          |
| `care:notes`         | Narrative explanation of safety decisions (mandatory for `generalized` / `restricted-generalized`) |
| `care:visibility_rules` | For example, `"h3-only"` or `"no-exact-points"`     |

Additional fields may appear as needed:

- `care:consent_status` (for example, `approved`, `conditional`, `not-approved`, `not-applicable`).

### Governance expectations

- Protohistoric / ethnohistoric interaction spheres typically require `care:review = "tribal"`.  
- High-sensitivity layers should adopt stricter `care:visibility_rules` (for example, `h3-only`).  
- `care:notes` should clearly describe:
  - What was generalized or removed.  
  - Which communities reviewed the representation.  
  - Any conditions attached to use (for example, story framing limitations).

---

## 🧪 Example Provenance Excerpt (Illustrative)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Historical synthesis of CPT exchange patterns",
      "prov:type": "Dataset",
      "kfm:source": "Open archaeological synthesis (PD)"
    },
    "generalized": {
      "prov:label": "Generalized interaction sphere (H3-r6)",
      "prov:type": "Dataset",
      "care:notes": "Boundaries generalized to protect cultural sovereignty."
    },
    "processed": {
      "prov:label": "Central Plains Exchange Sphere v2",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v2"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "SpatialGeneralization",
      "prov:startTime": "2025-10-15T10:22:00Z",
      "prov:endTime": "2025-10-15T10:47:00Z",
      "kfm:steps": ["H3 index derivation", "polygon simplification"]
    }
  },
  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "A. Barta"
    },
    "faircare": {
      "prov:type": "Organization",
      "prov:label": "FAIR+CARE Council"
    }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare"
}
~~~

Actual production logs MUST adhere to the project’s provenance schemas and reflect current review status.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

Interaction-sphere provenance logs support creation of:

**Nodes**

- `InteractionSphere` and `GeneralizedRegion` entities  
- `ProvenanceActivity` nodes (cleaning, generalization, review)  
- `ReviewEvent` nodes (CARE, tribal, FAIR+CARE events)  
- Source/agent nodes representing institutions and people  

**Relationships**

- `GENERALIZED_FROM` (Processed ↔ Generalized ↔ Raw)  
- `HAS_PROVENANCE` (InteractionSphere ↔ ProvenanceRecord)  
- `REVIEWED_BY` (InteractionSphere/Provenance ↔ Agents)  
- `HAS_CARE_SENSITIVITY` (InteractionSphere ↔ CARE state)  

### Story Nodes

- Surface provenance context at paragraph or story-block level.  
- Provide transparent evidence for interaction narratives.  
- Allow Story Nodes to reference specific provenance versions when summarizing.

### Focus Mode v3

- Uses provenance to:
  - Render provenance chips in explanations.  
  - Adjust narrative framing based on review status and CARE sensitivity.  
  - Enforce additional constraints for high-sensitivity spheres.

---

## 📊 Provenance Index (Illustrative)

| Provenance File                | Dataset                          | Sensitivity           | Review              | Status   |
|--------------------------------|----------------------------------|-----------------------|---------------------|----------|
| `great-bend-aspect-v3.json`   | Great Bend Aspect v3             | generalized           | FAIR+CARE           | 🟢 Active |
| `central-plains-exchange-v2.json` | Central Plains Exchange v2    | generalized           | FAIR+CARE           | 🟢 Active |
| `protohistoric-wichita-v2.json`   | Protohistoric Wichita v2      | restricted-generalized | Tribal + FAIR+CARE | 🟡 Review |

Authoritative status and flags live in manifests, metadata, and governance records; this table is illustrative.

---

## 🔗 Related Specifications

- `../README.md`  
  – Interaction Sphere provenance overview and directory-level governance.  
- `../stac/README.md`  
  – Interaction Sphere STAC catalog (Items + Collections).  
- `../stac/items/README.md`  
  – STAC Item requirements and integration patterns.  
- `../metadata/README.md`  
  – DCAT + CARE metadata standards for interaction spheres.  
- `../../../../artifact-inventories/provenance/README.md`  
  – Artifact-inventory provenance patterns reused in this domain.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Tribal Advisory Review | Updated to KFM v11.2.3; added energy/carbon telemetry refs; aligned with v11 interaction-sphere governance and Focus Mode v3 usage. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council         | Defined Interaction Sphere provenance standards; added tribal review enforcement and PROV-O/CARE requirements. |
| v10.0.0   | 2025-11-10 | Landscape Provenance Team                         | Initial provenance directory structure.                                |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Spheres](../README.md)
