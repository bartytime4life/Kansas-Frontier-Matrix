---
title: "🌡️🟥📄 KFM v11.2.2 — Climate SHAP Global JSON-LD Explainability Bundles (Semantic Drivers · PROV · STAC-XAI)"
path: "docs/pipelines/ai/explainability/climate/shap/global/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Global SHAP JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
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
sensitivity: "Explainability-Global-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "shap-global-jsonld"
  - "climate-global-drivers"
  - "semantic-driver-maps"
  - "prov-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/shap/global/jsonld"
  applies_to:
    - "xai-shap-global-jsonld"
    - "xai-shap-driver-codes-jsonld"
    - "stac-xai"
    - "prov-xai"
    - "faircare-governance"
    - "h3-masking"
    - "semantic-driver-taxonomy"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_directory_layout_section: true
requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️🟥📄 **Climate SHAP Global — JSON-LD Explainability Bundles**  
`docs/pipelines/ai/explainability/climate/shap/global/jsonld/README.md`

**Purpose:**  
Define the **JSON-LD semantic explainability** outputs for **Global SHAP** drivers in climate models, including global driver vectors, semantic driver codes, CARE-filtered summaries, STAC-XAI integration, and PROV-O lineage for Story Node v3 + Focus Mode v3.

</div>

---

## 📘 Overview

Global SHAP JSON-LD bundles provide a **semantic, machine-readable representation** of global climate model drivers:

- Ranked feature importance  
- Aggregated climate-variable influence  
- Terrain–climate interaction signals  
- CARE-masked global evidence summaries  
- STAC v11 XAI linkage  
- PROV-O lineage for governance transparency  
- Story Node v3–compatible driver structures  
- Focus Mode v3 global reasoning overlays  

All JSON-LD must be:

- Deterministic  
- Governance-safe  
- FAIR+CARE aligned  
- Fully schema-validated  
- Version-pinned  
- Compatible with KFM XAI templates  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/shap/global/jsonld/
    ├── 📄 README.md                         # This file
    │
    ├── 📄 xai-shap-global.jsonld           # Global semantic explainability bundle
    └── 📄 xai-shap-driver-codes.jsonld     # Narrative-safe driver code mapping

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 `xai-shap-global.jsonld`  
Global semantic explainability object containing:

- `@context` (KFM-XAI + PROV-O vocabularies)  
- `xai:feature_importance` — SHAP-ranked climate drivers  
- `xai:global_drivers` — aggregated contributions  
- `xai:climate_variable_semantics`  
- `xai:care_scope` — CARE restrictions & sovereignty notes  
- `xai:spatial_context` — H3-masked abstraction if spatial patterns exist  
- `prov:*` lineage  
- `kfm:model_version`  
- `kfm:input_items` (STAC IDs)  
- `checksum:multihash`  

Used by:

- Story Node v3 global climate narratives  
- Focus Mode v3 “global reasoning” maps  
- Governance dashboards  

---

### 2. 🟩 `xai-shap-driver-codes.jsonld`  
Maps **raw SHAP global drivers → semantic narrative codes**:

- `xai:driver_code` (canonical KFM climate driver taxonomy)  
- `xai:description` (narrative-safe, CARE-aligned text)  
- `xai:linked_features` (model features contributing to the driver)  
- `xai:care_annotations` (masking rules, sensitivity details)  
- `xai:story_node_roles` (classification for narrative use)  
- `prov:*` provenance links  

Used for:

- Story Node v3 driver explanation blocks  
- Focus Mode v3 textual overlays  
- Summaries in explainability dashboards  

---

## 📡 STAC Integration Requirements

SHAP Global JSON-LD assets MUST supply:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global` → link to global JSON-LD  
- `kfm:model_version`  
- `kfm:input_items` (STAC IDs)  
- `checksum:multihash`  
- CRS metadata (if spatial)  
- CARE masking info  
- PROV references  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD object must include:

- `prov:wasGeneratedBy` (model + pipeline version)  
- `prov:used` (STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  
- *Optional:* `prov:wasDerivedFrom` (model → SHAP → narrative chain)  

Supports:

- Governance review  
- Story Node v3 provenance  
- Focus Mode v3 reasoning timelines  

---

## 🔐 FAIR+CARE Requirements

Global SHAP JSON-LD must:

- Use H3 generalization for spatial drivers  
- Mask culturally sensitive or sovereignty-restricted regions  
- Maintain CARE scope + sovereignty annotations  
- Avoid speculative explanations  
- Respect Data Contract v3 & Vertical Axis v11  

---

## 🧪 Testing Requirements

All JSON-LD outputs MUST pass:

- JSON-LD validator  
- KFM-XAI schema validation  
- STAC XAI extension validation  
- CARE + sovereignty rule tests  
- PROV-O lineage validation  
- Deterministic regeneration tests  
- Driver competitiveness drift checks  

PR failing → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial SHAP Global JSON-LD explainability layer, aligned with XAI suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to SHAP Global](../README.md) · [🌡️ Climate XAI Root](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

