---
title: "🌡️🟥📄 KFM v11.2.2 — Climate SHAP Local JSON-LD Explainability (Event Drivers · Semantic Attribution)"
path: "docs/pipelines/ai/explainability/climate/shap/local/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Local SHAP JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability-Local-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "shap-local-jsonld"
  - "event-driver-attribution"
  - "climate-feature-contributions"
  - "semantic-driver-mapping"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/climate/shap/local/jsonld"
  applies_to:
    - "xai-shap-local-jsonld"
    - "xai-shap-driver-codes-jsonld"
    - "local-driver-evidence"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
    - "story-node-xai"
    - "focus-mode-xai"

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

# 🌡️🟥📄 **Climate SHAP — Local JSON-LD Explainability Bundles**  
`docs/pipelines/ai/explainability/climate/shap/local/jsonld/README.md`

**Purpose:**  
Define the **semantic, JSON-LD-encoded explainability bundles** for **local (per-prediction)** SHAP climate drivers.  
These bundles support:  
- **Story Node v3** event narratives  
- **Focus Mode v3** local climate reasoning  
- **STAC v11** explainability assets  
- **FAIR+CARE governance**  
- **PROV-O lineage**

</div>

---

## 📘 Overview

Local SHAP JSON-LD bundles provide machine-readable explanations of *why a climate model produced a specific prediction for a specific place/time*.

They encode:

- Per-prediction SHAP driver vectors  
- Local climate variable semantics  
- Spatial/H3-masked context  
- CARE scope annotations  
- STAC item linkages  
- PROV-O provenance chains  
- Narrative-ready driver mappings  

These files are foundational for:

- Event-level explanation windows in Focus Mode  
- Story Node v3 evidence blocks  
- Model transparency dashboards  
- Governance audits and drift analysis  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/shap/local/jsonld/
    ├── 📄 README.md                              # This file
    │
    ├── 📄 xai-shap-local.jsonld                  # Local SHAP event driver bundle
    └── 📄 xai-shap-local-driver-codes.jsonld     # Narrative-safe driver code mapping

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 `xai-shap-local.jsonld`
Represents **single-event** SHAP explanations.

Contains:

- `@context` — KFM-XAI, PROV-O vocabularies  
- `xai:sample_id` — prediction/event identifier  
- `xai:drivers` — list of local SHAP driver objects  
  - feature name  
  - direction (positive/negative influence)  
  - normalized magnitude  
  - uncertainty indicators  
- `xai:spatial_context`  
  - H3-generalized region  
  - optional bounding metadata  
- `care:scope` — CARE category and rules triggered  
- `prov:*` — complete lineage  
- `kfm:input_items` — STAC Items used in inference  
- `kfm:model_version`  

Used by:

- Focus Mode local reasoning  
- Story Node v3 “event cause” explanations  
- XAI dashboards  

---

### 2. 🟩 `xai-shap-local-driver-codes.jsonld`
Maps raw SHAP features → **semantic & narrative-safe driver codes**.

Contains:

- `xai:driver_code` — canonical climate driver taxonomy  
- `xai:description` — human-readable but CARE-safe  
- `xai:linked_features` — raw features contributing to driver  
- `xai:care_annotations`  
- `xai:story_node_roles` — narrative positions (primary driver, secondary driver)  
- `prov:wasDerivedFrom` linkage to local JSON-LD  

Used for:

- Narrative generation  
- Summaries in Focus Mode v3  
- FAIR+CARE review processes  

---

## 📡 STAC Integration Requirements

Local SHAP JSON-LD MUST include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS/geometry (if spatial)  
- CARE masking metadata  
- PROV references  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD bundle MUST provide:

- `prov:wasGeneratedBy` — model + inference pipeline  
- `prov:used` — STAC datasets  
- `prov:generatedAtTime` — ISO timestamp  
- `prov:Agent` — model + execution identity  
- `prov:wasDerivedFrom` — optional narrative lineage  

These integrate with:

- KFM lineage dashboards  
- Story Node provenance graphs  
- Focus Mode reasoning timelines  

---

## 🔐 FAIR+CARE Requirements

Local SHAP JSON-LD must:

- Use **H3 generalization** for spatial context  
- Remove or abstract culturally sensitive drivers  
- Include `care:scope` + sovereignty information  
- Avoid speculative causal claims  
- Adhere to Data Contract v3 + Vertical Axis v11  

---

## 🧪 Testing Requirements

CI MUST validate:

- JSON-LD schema correctness  
- STAC XAI extension validity  
- Deterministic regeneration  
- CARE masking rules  
- Sovereignty-policy enforcement  
- PROV-O lineage completeness  
- Driver drift stability  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate SHAP Local JSON-LD explainability specification      |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to SHAP Local](../README.md) · [🌡️ Climate XAI Root](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

