---
title: "⚡🟩📄🧬 KFM v11.2.2 — Hazard IG Local JSON-LD Template Specification (Event-Level Semantic Drivers · Governed XAI)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/local/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Template Specification (Hazard IG Local JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Hazard-IG-Local-JSONLD-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-local-jsonld-template"
  - "local-driver-xai-template"
  - "semantic-driver-mapping"
  - "prov-xai-template"
  - "stac-xai-template"
  - "focus-mode-hazard"
  - "story-node-hazard"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/integrated-gradients/templates/local/jsonld"
  applies_to:
    - "xai-ig-local-template.jsonld"
    - "hazard-ig-driver-codes-local-template.jsonld"
    - "semantic-driver-taxonomy"
    - "prov-xai"
    - "stac-xai"
    - "h3-masking"
    - "care-governance"
    - "narrative-safe-xai"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# ⚡🟩📄🧬 **Hazard IG — Local JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/local/jsonld/README.md`

**Purpose:**  
Define the **canonical JSON-LD templates** for **event-level Hazard Integrated Gradients (IG)** explainability, including the core semantic evidence bundle and the narrative-safe hazard-driver taxonomy.

These templates ensure that every generated hazard IG local JSON-LD file is:  
**deterministic**, **FAIR+CARE aligned**, **sovereignty-protected**, **H3-masked**, **STAC-XAI compatible**, **PROV-linked**, and **Story Node v3 / Focus Mode v3 ready**.

</div>

---

## 📘 Overview

This directory defines **two required JSON-LD templates**:

1. **`xai-ig-local-template.jsonld`**  
   → Semantic local IG evidence bundle (event-level attribution)

2. **`hazard-ig-driver-codes-local-template.jsonld`**  
   → Narrative-safe hazard driver taxonomy for IG outputs

These templates are enforced across:

- Hazard IG inference pipelines  
- KFM Explainability CI  
- Story Node semantic generation  
- Focus Mode hazard reasoning  
- Governance & audit workflows  

Templates include:

- Required structural fields  
- Deterministic key ordering  
- CARE + sovereignty placeholders  
- H3 generalized location placeholders  
- PROV-O lineage skeleton  
- STAC-XAI metadata anchors  
- Narrative safety constraints  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/local/jsonld/
    ├── 📄 README.md                                          # This file
    │
    ├── 📄 xai-ig-local-template.jsonld                       # Template for IG local semantic evidence
    └── 📄 hazard-ig-driver-codes-local-template.jsonld       # Template for semantic hazard driver taxonomy

---

## 🟥 Template: `xai-ig-local-template.jsonld`  
*Semantic Event-Level IG Evidence Blueprint*

### Required Structural Fields

**1. @context**  
- KFM-XAI ontology  
- PROV-O ontology  

**2. Event Metadata**  
- `xai:event_id` (placeholder)  
- `xai:hazard_domain` (`tornado|wind|hail|wildfire|flood|multi`)  
- `xai:timestamp` (optional placeholder)

**3. Local IG Drivers Block**  
Array of driver objects with deterministic ordering:

- `xai:driver_code`  
- `xai:importance` (float placeholder)  
- `xai:linked_features` (list placeholder)  
- `xai:uncertainty` (optional placeholder)

**4. Spatial Context (Masked)**  
- `xai:spatial_context`  
  - `xai:h3_regions` (H3-masked region list)  
  - `xai:region_summary` (abstract description)

**5. CARE & Sovereignty Metadata**  
- `care:scope`  
- `care:notes`  
- `sovereignty:flags`

**6. STAC-XAI Required Fields**  
- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`

**7. PROV-O Lineage**  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`

---

## 🟩 Template: `hazard-ig-driver-codes-local-template.jsonld`  
*Narrative-Safe IG Hazard Driver Taxonomy Blueprint*

### Required Fields Per Driver Entry

- `xai:driver_code`  
  - e.g., `TORNADO_SIGNAL_IG_LOCAL`, `FLOOD_SATURATION_IG_LOCAL`, etc.  

- `xai:description`  
  - CARE-safe narrative explanation placeholder  

- `xai:hazard_domain`  
  - Hazard category (tornado|wind|hail|wildfire|flood|multi)  

- `xai:linked_features`  
  - Placeholder for raw IG features  

- `xai:story_node_roles`  
  - e.g., `primary_driver`, `secondary_driver`, `contextual_driver`  

- `xai:focus_mode_tags`  
  - e.g., `map-overlay`, `timeline-driver`, `risk-driver`

- `care:annotations`  
- `sovereignty:*` (required)

- `prov:wasDerivedFrom`  
  - Template linking driver code → local IG evidence template

This ensures deterministic, governance-aligned, narrative-safe semantics for hazard drivers.

---

## 📡 STAC-XAI Template Requirements

Generated JSON-LD MUST satisfy:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS/vertical datum (if spatial)  
- CARE + sovereignty metadata  
- PROV lineage fields  

Templates enforce the correct locations & order for these fields.

---

## 🧾 PROV-O Template Requirements

Both templates must include:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional:  
  - `prov:wasDerivedFrom` (linking global & local IG evidence)

These relationships are essential for:

- Lineage graph integration  
- Story Node provenance  
- Focus Mode reasoning traceability  

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

**Every template MUST include placeholders for:**

- H3 spatial masking  
- CARE scope + notes  
- Sovereignty flags  
- No culturally sensitive text  
- No hazardous or speculative language  
- Compliance with Data Contract v3 and Indigenous governance  

Generated content must pass governance review before release.

---

## 🧪 Template CI Requirements

Edits to this template directory MUST pass:

- JSON-LD schema checks  
- STAC-XAI lint checks  
- PROV-O structure validation  
- CARE + sovereignty placeholder presence  
- H3-mask placeholder presence  
- Deterministic key ordering tests  
- Narrative-safety lexical lint  
- Hash-stability tests  

Failure → **PR rejected**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                                 |
|--------|------------|---------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard IG Local JSON-LD Template Suite (aligned with global IG + SHAP suites) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Local Templates](../README.md) · [⚡ Hazard XAI Root](../../../../README.md) · [🏛 Governance](../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

