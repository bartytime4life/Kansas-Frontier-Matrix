---
title: "⚡🟩📄 KFM v11.2.2 — Hazard Integrated Gradients Global JSON-LD Templates (Semantic Drivers · STAC-XAI · PROV-O)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/global/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard IG Global JSON-LD)"

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
sensitivity: "Explainability-Hazard-Global-IG-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-global-jsonld-templates"
  - "hazard-driver-taxonomy-templates"
  - "global-gradient-driver-mapping"
  - "prov-xai-templates"
  - "stac-xai-templates"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"
  - "care-governance"

scope:
  domain: "explainability/hazard/integrated-gradients/templates/global/jsonld"
  applies_to:
    - "xai-ig-global-template.jsonld"
    - "hazard-ig-driver-codes-template.jsonld"
    - "semantic-driver-taxonomy"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
    - "h3-masking"
    - "narrative-driver-templates"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# ⚡🟩📄 **Hazard IG Global — JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/global/jsonld/README.md`

**Purpose:**  
Define the **canonical JSON-LD templates** for **global Integrated Gradients (IG) hazard explainability**, covering:

- System-wide gradient-based hazard drivers  
- Narrative-safe hazard driver code mappings  
- STAC v11 XAI integration fields  
- PROV-O lineage scaffolding  
- FAIR+CARE + sovereignty placeholders  

These templates ensure every generated **global hazard IG JSON-LD bundle** is structurally consistent, governance-safe, and interoperable with Story Node v3 and Focus Mode v3.

</div>

---

## 📘 Overview

This template suite is used to generate:

- `xai-ig-global.jsonld` — semantic global hazard IG evidence bundles  
- `xai-hazard-ig-driver-codes.jsonld` — semantic, narrative-safe hazard-driver taxonomy  

The templates:

- Enforce JSON-LD structure and key ordering  
- Embed placeholder fields for CARE + sovereignty annotations  
- Encode STAC-XAI metadata fields  
- Provide PROV-O lineage skeletons  
- Support deterministic hashing and CI-based drift detection  

Hazard domains covered:

- 🌀 Tornado / severe rotation  
- 💨 Wind / gust / LLJ  
- 🌩️ Hail / severe convection  
- 🌧️ Flood / flash-flood  
- 🔥 Wildfire / fuels / VPD  
- ⚡ Multi-hazard fusion  

---

## 🗂 Directory Layout (v11.2.2)

> Note: This README governs the **template files**, which live alongside this document:

    docs/pipelines/ai/explainability/hazard/integrated-gradients/global/jsonld/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 xai-ig-global-template.jsonld              # Template for global IG evidence bundle
    └── 📄 hazard-ig-driver-codes-template.jsonld     # Template for IG-based hazard driver taxonomy

---

## 🟥 `xai-ig-global-template.jsonld` — Global IG Evidence Template

Defines the JSON-LD structure of **global hazard IG explainability** files.

### Required Structural Sections

- `@context`
  - KFM-XAI vocabularies  
  - PROV-O vocabularies  

- **Global Driver Block**
  - `xai:drivers` — array of driver objects:
    - `xai:driver_code` (template reference into driver taxonomy)  
    - `xai:importance` (normalized IG magnitude)  
    - `xai:hazard_domain` (tornado | hail | wind | wildfire | flood | multi)  
    - `xai:description` (placeholder, final content must be CARE-reviewed)  

- **Spatial Context (Optional / Masked)**
  - `xai:spatial_context`:
    - `xai:h3_regions` — placeholder for generalized H3 indices  
    - `xai:region_summary` — high-level region descriptions (no direct sensitive locations)  

- **Model & Dataset Metadata**
  - `kfm:model_version`  
  - `kfm:input_items` — array of STAC Item IDs  
  - `checksum:multihash` — placeholder for integrity hash  

- **CARE & Sovereignty Metadata**
  - `care:scope`  
  - `care:notes`  
  - `sovereignty:flags`  

- **PROV-O Lineage**
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:generatedAtTime`  
  - `prov:Agent`  

The template strictly defines **field presence and ordering**, enabling deterministic generation and CI validation.

---

## 🟩 `hazard-ig-driver-codes-template.jsonld` — IG Driver Taxonomy Template

Defines a JSON-LD taxonomy for **IG-based hazard drivers**, mapping raw deep-model features to **semantic driver codes**.

### Template Fields for Each Driver

- `xai:driver_code`
  - Canonical hazard driver ID (e.g., `TORNADO_SIGNAL_IG`, `WILDFIRE_DRYNESS_IG`)  

- `xai:description`
  - Narrative-safe description; actual text must be CARE-reviewed  

- `xai:hazard_domain`
  - `tornado | hail | wind | wildfire | flood | multi`  

- `xai:linked_features`
  - Placeholder array of raw feature names (input to model)  

- `xai:story_node_roles`
  - e.g., `primary_driver`, `secondary_driver`, `contextual_driver`  

- `xai:focus_mode_tags`
  - Tags for Focus Mode v3 UI (e.g., `global-risk-driver`, `map-overlay-driver`)  

- `care:annotations`
  - CARE sensitivity + mitigation placeholders  

- `sovereignty:*`
  - Placeholder for Indigenous/sovereignty-related policy notes  

- `prov:wasDerivedFrom`
  - Template link to `xai-ig-global.jsonld` evidence  

This taxonomy template guarantees that hazard drivers are:

- Consistent across models and releases  
- Semantically robust  
- Governed and FAIR+CARE-aligned  

---

## 📡 STAC-XAI Template Fields

The template suite enforces presence of STAC explainability fields:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:global` (reference from STAC Item to JSON-LD)  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  

These fields are **required** by CI to validate any generated IG global XAI bundle.

---

## 🧾 PROV-O Template Requirements

Templates encode the expected PROV-O structure:

- `prov:wasGeneratedBy` → hazard IG pipeline run  
- `prov:used` → STAC climate/hazard inputs  
- `prov:Agent` → model and pipeline identity  
- `prov:generatedAtTime` → explanation timestamp  

Optional:

- `prov:wasDerivedFrom` → model weights + dataset version  

This ensures hazard IG explainability is fully traceable.

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

All templates MUST:

- Include H3-based spatial abstraction fields  
- Provide CARE scope and notes placeholders  
- Provide sovereignty flag placeholders  
- Exclude any embedded sensitive or speculative narrative content  
- Align with Data Contract v3 and hazard-ethics policies  

Actual content inserted at runtime MUST be governance-reviewed.

---

## 🧪 Template CI Rules

Any change to these templates MUST pass:

- JSON-LD schema validation  
- STAC-XAI integration checks  
- PROV-O structure checks  
- CARE/scope fields presence checks  
- Sovereignty field checks  
- Key-ordering/determinism checks  
- Narrative-safety lexical lint  

Failing checks → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                                |
|----------|------------|--------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard Integrated Gradients Global JSON-LD Template Suite (KFM XAI v11.2.2) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Global Templates](../README.md) · [⚡ Hazard XAI Root](../../../../README.md) · [🏛 Governance](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

