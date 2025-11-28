---
title: "🌡️🟥📈 KFM v11.2.2 — Climate SHAP: Global Explainability (Feature Importance · Climate Drivers)"
path: "docs/pipelines/ai/explainability/climate/shap/global/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (SHAP Global)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability-Global"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "shap-global"
  - "climate-global-drivers"
  - "global-feature-importance"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"

scope:
  domain: "explainability/climate/shap/global"
  applies_to:
    - "shap-global-vectors"
    - "driver-ranking"
    - "jsonld-xai"
    - "stac-xai"
    - "faircare-governance"
    - "h3-masking"
    - "prov-xai"

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

# 🌡️🟥📈 **Climate SHAP — Global Feature-Importance Attribution**  
`docs/pipelines/ai/explainability/climate/shap/global/README.md`

**Purpose:**  
Define the **global SHAP explainability subsystem** for climate models, generating deterministic global driver vectors, climate-variable importance rankings, masked spatial summaries, and JSON-LD explainability bundles used in **Story Node v3**, **Focus Mode v3**, and climate governance review.

</div>

---

## 📘 Overview

Global SHAP attribution provides a high-level understanding of **what climate variables drive model behavior across Kansas**.

This layer reveals:

- Highest-impact climate variables  
- Multi-scale interactions (e.g., terrain × temperature)  
- Seasonally relevant drivers  
- Persistent long-term patterns  
- Global climate-model semantics  

Global SHAP outputs feed:

- STAC v11 XAI assets  
- Story Node v3 climate narratives  
- Focus Mode v3 global climate reasoning  
- Governance dashboards + drift monitoring  

All outputs must be:

- Deterministic  
- JSON-LD structured  
- FAIR+CARE compliant  
- PROV-O lineage rich  
- CRS-correct (when spatial)

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/shap/global/
    ├── 📄 README.md                        # This file
    │
    ├── 📄 global.json                      # Raw global SHAP feature-importance vectors
    ├── 📄 summary.md                       # Human-readable global driver explanation
    │
    └── 📁 jsonld/                          # JSON-LD global explainability bundles
        ├── 📄 xai-shap-global.jsonld       # Semantic global explainability bundle
        └── 📄 xai-shap-driver-codes.jsonld # Narrative-ready driver mapping

---

## 🔍 Component Specification

### 1. 🟥 `global.json` — Raw Global SHAP Vectors

Contains:

- Global feature-importance magnitudes  
- Climate variable names (temp, precip, humidity, wind, terrain-derivatives…)  
- Sorted ranking  
- Confidence estimates or clustering indices (optional)  
- Model version metadata  
- CARE masking indicators (spatial masking flags)

Used directly by:

- Climate model debugging  
- Drift detection  
- Training monitoring  

---

### 2. 🧾 `summary.md` — Human-Readable Interpretation

Must summarize:

- Top global climate drivers  
- Cross-variable interactions  
- Seasonal patterns (e.g., winter temp vs. summer humidity)  
- CARE + sovereignty notes  
- Linkages to model type and STAC input datasets  
- Vocabulary safe for narrative use  

Used by:

- Governance  
- Climate explainability dashboards  
- Story Node editorial tools  

---

### 3. 🟩 JSON-LD Bundles (in `/jsonld`)

#### **`xai-shap-global.jsonld`**
Global semantic explainability object containing:

- Feature-importance vector  
- Ranked driver list  
- Climate variable semantics  
- CARE masking metadata  
- STAC input dataset links  
- PROV-O lineage (model, data, timestamp)

#### **`xai-shap-driver-codes.jsonld`**
Maps global SHAP drivers → narrative-safe driver categories:

- Driver codes (`TEMP_MAX`, `DROUGHT_SIGNAL`, etc.)  
- Natural-language descriptions  
- CARE-filtered variants  
- Role in Story Node v3 (“global climate driver”, “anomaly driver”)  
- Focus Mode v3 integration tags  

---

## 📡 STAC Integration Requirements

Global SHAP assets MUST include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS/geometry (if spatial)  
- `checksum:multihash`  
- Provenance (`prov:*`)  

---

## 🧾 PROV-O Lineage Requirements

Each output must include:

- `prov:wasGeneratedBy` (model version, inference pipeline)  
- `prov:used` (STAC input climate datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  
- Optional: `prov:wasDerivedFrom` (model → SHAP → narrative)

---

## 🔐 FAIR+CARE Requirements

Global SHAP outputs MUST:

- Apply H3 generalization to sensitive spatial data  
- Mask/abstract climate drivers tied to culturally sensitive geographic patterns  
- Include CARE scope + sovereignty flags  
- Avoid speculative causal explanations  
- Comply with Data-Contract v3 + Vertical Axis v11  

---

## 🧪 Testing Requirements

CI tests MUST validate:

- Deterministic `global.json` values  
- JSON-LD schema compliance  
- STAC XAI extension compliance  
- CARE masking correctness  
- Sovereignty compliance  
- Drift stability across model versions  

---

## 🕰 Version History

| Version  | Date       | Notes                                                               |
|----------|------------|---------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate SHAP Global explainability spec aligned with XAI suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate SHAP](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

