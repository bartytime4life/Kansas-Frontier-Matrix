---
title: "⚡🟥📄 KFM v11.2.2 — Hazard SHAP Global JSON-LD Explainability (Semantic Drivers · PROV · STAC-XAI)"
path: "docs/pipelines/ai/explainability/hazard/shap/global/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard SHAP Global JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
sensitivity: "Explainability-Hazard-Global-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-shap-global-jsonld"
  - "hazard-driver-semantics"
  - "system-wide-hazard-drivers"
  - "prov-xai"
  - "stac-xai"
  - "story-node-hazard"
  - "focus-mode-hazard"

scope:
  domain: "explainability/hazard/shap/global/jsonld"
  applies_to:
    - "xai-shap-global-jsonld"
    - "xai-hazard-driver-codes-jsonld"
    - "hazard-driver-taxonomy"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
    - "h3-masking"
    - "narrative-driver-mapping"

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

# ⚡🟥📄 **Hazard SHAP — Global JSON-LD Explainability**  
`docs/pipelines/ai/explainability/hazard/shap/global/jsonld/README.md`

**Purpose:**  
Define the **JSON-LD semantic layer** for **Global SHAP hazard explainability**, translating system-wide SHAP feature-importance into FAIR+CARE-safe, PROV-linked, STAC-compliant semantic drivers powering:

- ⚡ Hazard Story Node v3 narratives  
- 🧭 Focus Mode v3 hazard reasoning  
- 🗺️ Hazard explainability dashboards  
- 🏛 Governance & audit workflows (lineage, CARE scope, sovereignty)  

</div>

---

## 📘 Overview

This layer expresses **global hazard drivers** in structured JSON-LD form.  
Hazards covered include:

- 🌀 **Tornado / Shear / Rotation**  
- 💨 **Wind / Gust / LLJ**  
- 🌩️ **Hail / Severe Convection**  
- 🌧️ **Flood / Flash-Flood / Runoff / Soil Saturation**  
- 🔥 **Wildfire / Fuels / VPD / Wind alignment**  
- ⚡ **Multi-hazard fusion drivers**  

Global hazard JSON-LD integrates:

- Feature-importance rankings  
- Climate–terrain–hydrology–fuel interactions  
- CARE/H3 spatial abstraction  
- Provenance (PROV-O)  
- STAC v11 explainability metadata  
- Narrative-safe semantic driver codes  

All outputs must be deterministic, schema-valid, and sovereignty-compliant.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/global/jsonld/
    ├── 📄 README.md                             # This file
    │
    ├── 📄 xai-shap-global.jsonld                # Semantic global hazard-driver bundle
    └── 📄 xai-hazard-driver-codes.jsonld        # Narrative-safe hazard driver taxonomy

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 `xai-shap-global.jsonld` — Global Hazard Driver Evidence
Contains:

- `@context` — KFM-XAI + PROV-O vocabularies  
- `xai:drivers` — system-wide hazard driver list  
- `xai:importance` — normalized SHAP global rankings  
- `xai:hazard_domain` — tornado, wind, hail, flood, wildfire, etc.  
- `xai:spatial_context` — **H3-generalized** geography (if spatial)  
- `care:scope` — CARE classification + governance flags  
- `prov:*` — lineage (model, data, timestamp, agent)  
- `kfm:model_version` — required  
- `kfm:input_items` — STAC Item IDs used in inference  
- `checksum:multihash` — asset integrity  

Used for:

- Global hazard narrative generation  
- Focus Mode global reasoning overlays  
- Hazard model audit & validation  

---

### 2. 🟩 `xai-hazard-driver-codes.jsonld` — Narrative Hazard Driver Taxonomy
Maps raw SHAP features → semantic, governance-safe hazard drivers:

Examples:

- `TORNADO_SIGNAL`  
- `SEVERE_STORM_ENV`  
- `HAIL_GROWTH_WINDOW`  
- `WILDFIRE_FUEL_DRYNESS`  
- `FLOOD_SOIL_SATURATION`  

Each record MUST include:

- `xai:driver_code`  
- `xai:description` (CARE-filtered)  
- `xai:linked_features` (raw SHAP features)  
- `xai:story_node_roles` (e.g., primary hazard driver)  
- `xai:focus_mode_tags`  
- `xai:care_annotations`  
- `prov:wasDerivedFrom` → link to global bundle  

Used by:

- Hazard Story Node v3  
- Focus Mode hazard evidence panels  

---

## 📡 STAC Integration Requirements

Each JSON-LD hazard global file MUST specify:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS metadata (if spatial)  
- `checksum:multihash`  
- CARE & sovereignty fields  
- PROV-O references  

---

## 🧾 PROV-O Lineage Requirements

Mandatory fields:

- `prov:wasGeneratedBy` — hazard model inference pipeline  
- `prov:used` — hazard + climate STAC datasets  
- `prov:generatedAtTime`  
- `prov:Agent` — model identity/version  
- Optional: `prov:wasDerivedFrom` — model → SHAP → narrative  

Supports:

- Governance dashboards  
- Story Node v3 provenance trees  
- Focus Mode backtracking  

---

## 🔐 FAIR+CARE Requirements

All JSON-LD hazard SHAP output MUST:

- Use **H3 generalization** for any spatial drivers  
- Mask/remove culturally sensitive hazard-related signals  
- Include CARE scopes & sovereignty indicators  
- Avoid speculative or non-data-grounded hazard explanations  
- Respect Data-Contract v3 + hazard ethics policies  

---

## 🧪 Testing Requirements

CI MUST validate:

- JSON-LD schema correctness  
- KFM-XAI & PROV-O compliance  
- STAC XAI metadata fields  
- CARE/h3 masking enforcement  
- Deterministic generation  
- Hazard-driver ranking drift detection  
- Sovereignty compliance  

Any failure → ❌ **merge blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                   |
|--------|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard SHAP Global JSON-LD explainability spec aligned with suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Global](../README.md) · [⚡ Hazard XAI Root](../../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

