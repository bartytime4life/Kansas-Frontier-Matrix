---
title: "⚡🟩🧬📈 KFM v11.2.2 — Hazard Integrated Gradients (IG) Global Template Suite (Semantic Drivers · JSON-LD · PROV · STAC-XAI)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/global/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Explainability Template Set (Hazard IG Global)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Hazard-IG-Global-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-global-templates"
  - "gradient-attribution-templates"
  - "semantic-driver-taxonomy"
  - "xai-global-jsonld"
  - "prov-xai-templates"
  - "stac-xai-templates"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"
  - "care-governance"

scope:
  domain: "explainability/hazard/integrated-gradients/templates/global"
  applies_to:
    - "ig-global-template.json"
    - "ig-global-summary-template.md"
    - "xai-ig-global-template.jsonld"
    - "hazard-ig-driver-codes-template.jsonld"
    - "semantic-driver-taxonomy"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
    - "narrative-driver-templates"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# ⚡🟩🧬📈 **Hazard IG Global Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/global/README.md`

**Purpose:**  
Define the **template set** for generating all **global Integrated Gradients (IG)** hazard explainability artifacts — including raw global gradient vectors, semantic JSON-LD bundles, driver-taxonomy templates, and governance-safe summary documents — ensuring deterministic, FAIR+CARE-aligned, STAC-XAI-compatible outputs for Story Node v3 and Focus Mode v3.

</div>

---

## 📘 Overview

Global IG templates define the canonical structure for:

- 📈 **Global gradient attribution vectors** (`ig-global.json`)  
- 🧾 **Global driver summary documents** (`summary.md`)  
- 📄 **Semantic JSON-LD evidence bundles** (`xai-ig-global.jsonld`)  
- 🧩 **Hazard IG driver-code taxonomies** (`hazard-ig-driver-codes.jsonld`)  

These templates guarantee that global hazard IG outputs are:

- Deterministic in structure and key ordering  
- FAIR+CARE and sovereignty compliant  
- Masked with H3 spatial generalization if spatial reasoning is included  
- Aligned with STAC v11 explainability metadata  
- Integrated with PROV-O lineage  
- Safe for narrative generation and public presentation  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/global/
    ├── 📄 README.md                                   # This file
    │
    ├── 📄 ig-global-template.json                     # Raw global IG vector template
    ├── 📄 ig-global-summary-template.md               # Template for global narrative summary
    │
    └── 📁 jsonld/                                     # Semantic JSON-LD templates
        ├── 📄 xai-ig-global-template.jsonld           # Global IG evidence (semantic)
        └── 📄 hazard-ig-driver-codes-template.jsonld  # IG hazard driver taxonomy

---

## 🔍 Template Definitions

### 1. 🟥 `ig-global-template.json`
Defines canonical fields for:

- Feature names  
- Normalized IG contributions  
- Hazard-domain labels (tornado|hail|wind|wildfire|flood|multi)  
- Uncertainty placeholders  
- CARE & sovereignty placeholders  
- `model_version`  
- Checksums & key-ordering  

CI will validate:

- Schema correctness  
- Deterministic key ordering  
- FAIR+CARE placeholder existence  

---

### 2. 🧾 `ig-global-summary-template.md`
Human-readable global summary template:

- Top hazard IG drivers (template tokens)  
- Cross-driver interactions (e.g., CAPE × shear, VPD × fuels)  
- Seasonal hazard relevance  
- CARE + sovereignty disclaimers  
- Template-safe narrative tone (no speculation, no sensitive geography)  
- References to STAC Items & global JSON-LD bundle  

Used by Story Node editors and governance reviewers.

---

### 3. 🟩 JSON-LD Templates (`/jsonld/`)

#### **`xai-ig-global-template.jsonld`**
Defines semantic IG global evidence:

- `@context` (KFM-XAI + PROV-O)  
- `xai:drivers` array  
- `xai:importance` values  
- `xai:hazard_domain`  
- H3 spatial abstraction  
- CARE metadata  
- STAC-XAI fields:
  - `kfm:model_version`
  - `kfm:input_items`
  - `checksum:multihash`
- Full PROV lineage placeholders  

#### **`hazard-ig-driver-codes-template.jsonld`**
Defines the semantic taxonomy for IG global hazard drivers:

- `xai:driver_code`  
- `xai:description` (CARE-safe placeholder)  
- `xai:hazard_domain`  
- `xai:linked_features`  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- CARE & sovereignty placeholders  
- `prov:wasDerivedFrom` placeholder  

This enforces semantic stability and narrative-safe driver definitions.

---

## 📡 STAC-XAI Template Requirements

All generated global IG hazard explainability outputs must contain:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata if spatial  
- CARE & sovereignty metadata  
- PROV-O references  

The templates enforce correct placement + ordering.

---

## 🧾 PROV-O Template Requirements

Templates require:

- `prov:wasGeneratedBy` (model pipeline)  
- `prov:used` (STAC hazard + climate datasets)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional lineage:
  - `prov:wasDerivedFrom` mappings to raw IG sources & STAC inputs  

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

Templates MUST include:

- H3 spatial abstraction placeholders  
- CARE scope fields  
- Sovereignty protection fields  
- Narrative-safety restrictions  
- Banned-term compliance  
- Data Contract v3 alignment  
- No culturally sensitive or speculative hazard interpretations  

All generated content must undergo governance review.

---

## 🧪 Template CI Rules

CI must verify:

- JSON-LD schema compliance  
- Deterministic key ordering  
- STAC-XAI required fields  
- PROV-O structural correctness  
- CARE + sovereignty placeholders  
- H3 masking existence  
- Narrative-safety linter  
- Hash reproducibility  

Failure → **PR blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                        |
|--------|------------|-------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard IG Global Template Suite (aligned with SHAP/IG/Spatial XAI)   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Templates](../README.md)  
[⚡ Hazard XAI Root](../../README.md)  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

