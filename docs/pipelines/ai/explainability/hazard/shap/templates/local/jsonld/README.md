---
title: "⚡🟥📄🧬 KFM v11.2.2 — Hazard SHAP Local JSON-LD Template Suite (Event Drivers · Semantic Codes · Provenance)"
path: "docs/pipelines/ai/explainability/hazard/shap/templates/local/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard SHAP Local JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Hazard-Local-JSONLD-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-local-shap-jsonld-templates"
  - "event-driver-taxonomy-templates"
  - "semantic-driver-mapping"
  - "prov-xai-templates"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/shap/templates/local/jsonld"
  applies_to:
    - "xai-shap-local-template.jsonld"
    - "hazard-driver-codes-local-template.jsonld"
    - "semantic-driver-taxonomy"
    - "faircare-governance"
    - "prov-xai"
    - "stac-xai"
    - "h3-masking"
    - "narrative-driver-templates"

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

# ⚡🟥📄🧬 **Hazard SHAP — Local JSON-LD Templates**  
`docs/pipelines/ai/explainability/hazard/shap/templates/local/jsonld/README.md`

**Purpose:**  
Define the canonical, deterministic **JSON-LD template suite** for **event-level hazard SHAP** explainability, covering:

- Local driver vectors → semantic JSON-LD  
- Narrative-safe hazard driver codes  
- CARE + sovereignty compliant masking  
- STAC-XAI linkage  
- PROV-O lineage scaffolding  
- Story Node v3 + Focus Mode v3 integration

These templates guarantee that all local hazard explainability outputs are structurally identical, governance-safe, reproducible, and interoperable across the entire KFM knowledge architecture.

</div>

---

## 📘 Overview

This directory defines the **“schema-of-schemas”** for local hazard SHAP JSON-LD outputs.  
Templates include placeholders for:

- Hazard domain  
- Local SHAP contributions  
- Per-event semantic driver classification  
- H3-generalized spatial masking  
- CARE scopes  
- STAC XAI metadata  
- PROV-O lineage skeleton  
- Narrative driver codes  

Hazards supported:

- Tornado / rotational shear  
- Wind & gust / LLJ  
- Hail / severe convection  
- Flood & flash-flood hydrology  
- Wildfire fuels & VPD  
- Multi-hazard fusion  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/templates/local/jsonld/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 xai-shap-local-template.jsonld             # Local hazard JSON-LD evidence template
    └── 📄 hazard-driver-codes-local-template.jsonld  # Narrative-safe hazard driver taxonomy template

---

## 🔍 Template Definitions

### 1. 🟥 `xai-shap-local-template.jsonld`
Defines the **semantic JSON-LD envelope** for local hazard explainability.

Must contain placeholders for:

- `@context`  
  - KFM-XAI vocabulary  
  - PROV-O vocabulary  

- **Event Metadata**  
  - `xai:event_id`  
  - `xai:hazard_domain` (tornado|hail|wind|wildfire|flood|multi)  

- **Driver List**  
  - `xai:drivers` array with:  
    - `driver_id` or feature placeholder  
    - `importance` placeholder  
    - `direction` (optional)  
    - `linked_features`  

- **Spatial Context**  
  - `xai:spatial_context` with H3-generalization fields  
  - `xai:region_summary` placeholder  

- **CARE & Sovereignty Metadata**  
  - `care:scope`  
  - `care:notes`  
  - `sovereignty:flags`  

- **Model Metadata**  
  - `kfm:model_version`  
  - `kfm:input_items`  
  - `checksum:multihash`  

- **PROV-O Lineage**  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:Agent`  
  - `prov:generatedAtTime`  

This template ensures all produced JSON-LD files are machine-valid and CI-reproducible.

---

### 2. 🟩 `hazard-driver-codes-local-template.jsonld`
Defines the **taxonomy of narrative-safe local hazard drivers**, mapping raw SHAP features to semantically governed hazard-driver categories.

Each driver entry template includes:

- `xai:driver_code`  
- `xai:description` (CARE filtered)  
- `xai:hazard_domain`  
- `xai:linked_features` placeholder  
- `xai:story_node_roles` (primary/secondary/contextual driver)  
- `xai:focus_mode_tags`  
- `care:annotations`  
- `prov:wasDerivedFrom` → link to local evidence template  

This ensures narrative outputs remain safe, non-speculative, and governance-aligned.

---

## 📡 STAC-XAI Template Fields

Generated hazard JSON-LD must contain:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- Optional CRS metadata (if spatial patterns are encoded)  

Templates include placeholders in the correct positions.

---

## 🧾 PROV-O Template Requirements

Templates enforce structure for:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  

and optional:

- `prov:wasDerivedFrom` — linking narrative codes → local SHAP evidence.

---

## 🔐 FAIR+CARE Template Rules

All templates MUST:

- Include H3 spatial abstraction fields  
- Provide CARE scope placeholders  
- Provide sovereignty metadata placeholders  
- Contain no culturally sensitive or speculative text  
- Obey Data Contract v3 hazard restrictions  
- Produce narrative-safe semantics only  

The template structure ensures that *any* generated content is validated for ethical compliance.

---

## 🧪 Template CI Requirements

Before a template can be modified, CI MUST confirm:

- JSON-LD schema validity  
- STAC XAI extension validity  
- CARE, sovereignty & masking placeholders exist  
- Deterministic hash/stability tests  
- Narrative-safety linter passes  
- PROV-O consistency  

Failure → **PR rejected**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                            |
|----------|------------|----------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Local JSON-LD Template Suite (aligned with global template) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Local Templates](../README.md)  
[⚡ Hazard XAI Root](../../../../README.md)  
[🏛 Governance](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

