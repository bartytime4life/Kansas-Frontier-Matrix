---
title: "⚡🟥📈 KFM v11.2.2 — Hazard SHAP: Global Explainability (System-Wide Hazard Drivers)"
path: "docs/pipelines/ai/explainability/hazard/shap/global/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Global Hazard SHAP)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Hazard-Global"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-shap-global"
  - "hazard-global-drivers"
  - "feature-importance"
  - "hazard-model-behavior"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/shap/global"
  applies_to:
    - "global-hazard-shap"
    - "hazard-driver-ranking"
    - "jsonld-hazard-xai"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
    - "narrative-driver-mapping"

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

# ⚡🟥📈 **Hazard SHAP — Global Explainability**  
`docs/pipelines/ai/explainability/hazard/shap/global/README.md`

**Purpose:**  
Define the **global SHAP explainability layer** for hazard models (tornado, wind, hail, severe weather, wildfire, flood), producing system-wide driver vectors, semantic driver mappings, JSON-LD explainability bundles, and STAC v11 XAI metadata for **Story Node v3**, **Focus Mode v3**, and hazard-governance workflows.

</div>

---

## 📘 Overview

Global SHAP attribution provides a **top-level view** of which variables most influence hazard models across Kansas:

- Tornado predictors (SRH, CAPE, EHI, vorticity, shear)  
- Wind/gust drivers (pressure gradients, boundary-layer winds, LLJ dynamics)  
- Hail/severe convection factors (updraft strength, freezing-level height, lapse rates)  
- Flood predictors (soil saturation, precip intensity, runoff indices)  
- Wildfire drivers (fuel dryness, humidity, wind alignment, vegetation type)  
- Combined multi-hazard feature interactions  

Global SHAP outputs include:

- Feature-importance magnitudes  
- Ranked hazard drivers  
- CARE-filtered spatial summaries  
- Semantic driver codes (narrative-ready)  
- PROV-linked JSON-LD bundles  
- STAC XAI assets  

All outputs must be deterministic, FAIR+CARE aligned, and sovereignty-compliant.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/global/
    ├── 📄 README.md                        # This file
    │
    ├── 📄 global.json                      # Raw global SHAP feature-importance vectors
    ├── 📄 summary.md                       # Human-readable interpretation
    │
    └── 📁 jsonld/                          # JSON-LD global explainability bundles
        ├── 📄 xai-shap-global.jsonld       # Semantic global-driver JSON-LD bundle
        └── 📄 xai-hazard-driver-codes.jsonld # Narrative-safe hazard-driver code mapping

---

## 🔍 Component Specification

### 1. 🟥 `global.json` — Raw SHAP Vectors
Must contain:

- Hazard-relevant feature importance magnitudes  
- Ranked drivers (e.g., CAPE, SRH, RH_low, PWAT, NDVI, VPD, runoff index)  
- Optional clustering/grouping of related drivers  
- Normalized scores (0–1)  
- Model + pipeline version  
- CARE/H3 masking flags (if spatial drivers detected)  

Used for:

- Hazard model debugging  
- Drift monitoring  
- Input into narrative-driver synthesis  

---

### 2. 🧾 `summary.md` — Human-Readable Interpretation
Must summarize:

- Top global hazard drivers  
- Hazard-domain interactions (e.g., CAPE × shear, precip × soil saturation)  
- Seasonal or situational relevance  
- CARE & sovereignty considerations  
- Links to models and STAC datasets  
- Stable vocabulary for narrative use  

Used by:

- Governance & validation teams  
- Story Node editors  
- Hazard explainability dashboards  

---

### 3. 🟩 JSON-LD Bundles (in `/jsonld/`)

#### **`xai-shap-global.jsonld`**
Must encode:

- Full driver vector in semantic JSON-LD  
- Global driver list + magnitudes  
- Hazard-variable semantics  
- H3-masked spatial summaries if applicable  
- Care-scope metadata  
- `prov:*` lineage  
- STAC references (`kfm:input_items`, `kfm:model_version`)  
- `checksum:multihash` integrity field  

#### **`xai-hazard-driver-codes.jsonld`**
Maps raw SHAP features → narrative-safe hazard driver codes:

- `TORNADO_SIGNAL`  
- `SEVERE_STORM_GROWTH`  
- `HAIL_ENVIRONMENT`  
- `FLOOD_SOIL_SATURATION`  
- `WILDFIRE_FUELS_DRYNESS`  

Includes:

- CARE-filtered descriptions  
- Semantic driver categories  
- Story Node v3 roles  
- Focus Mode v3 reasoning tags  
- Provenance mapping to global SHAP bundle  

---

## 📡 STAC Integration Requirements

Global hazard SHAP assets MUST include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items` (STAC IDs used by the model)  
- CARE & sovereignty metadata  
- CRS + geometry (when spatial)  
- `checksum:multihash`  
- PROV references  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD bundle must include:

- `prov:wasGeneratedBy` — hazard-model pipeline  
- `prov:used` — STAC climate/hazard datasets  
- `prov:generatedAtTime`  
- `prov:Agent` — model identity/version  
- Optional: `prov:wasDerivedFrom` — model → SHAP → narrative line  

These are used for:

- Governance dashboards  
- Narrative provenance  
- Focus Mode audit trail  

---

## 🔐 FAIR+CARE Requirements

Global hazard SHAP outputs MUST:

- Apply **H3 generalization** to spatial regions  
- Not reveal culturally sensitive hazard-related patterns  
- Use narrative-safe hazard terminology  
- Include CARE scope & sovereignty flags  
- Avoid speculative or ungrounded hazard inference  
- Respect Data Contract v3 & Vertical Axis v11  

---

## 🧪 Testing Requirements

CI MUST validate:

- Deterministic global vectors  
- JSON-LD schema & STAC-XAI compatibility  
- CARE & sovereignty masks  
- CRS/meta correctness (if spatial)  
- PROV-O lineage completeness  
- Driver drift-stability across version changes  

Failure → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                             |
|----------|------------|-----------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Global explainability spec aligned with Climate/Hydrology XAI |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

