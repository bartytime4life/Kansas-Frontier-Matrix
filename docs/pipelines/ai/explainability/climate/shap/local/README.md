---
title: "🌡️🟥🧪 KFM v11.2.2 — Climate SHAP: Local Explainability (Per-Prediction Drivers · Event Attribution)"
path: "docs/pipelines/ai/explainability/climate/shap/local/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Local SHAP)"

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
sensitivity: "Explainability-Local"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "shap-local"
  - "climate-local-drivers"
  - "event-attribution"
  - "local-feature-importance"
  - "prov-xai"
  - "stac-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/shap/local"
  applies_to:
    - "shap-local-vectors"
    - "sample-driver-attribution"
    - "jsonld-xai"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "story-node-xai"
    - "focus-mode-xai"

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

# 🌡️🟥🧪 **Climate SHAP — Local Explainability**  
`docs/pipelines/ai/explainability/climate/shap/local/README.md`

**Purpose:**  
Define **local (per-prediction)** SHAP explainability outputs for climate models — providing event-level feature importance, localized climate-driver vectors, CARE-masked spatial context, and JSON-LD explainability bundles for **Story Node v3** and **Focus Mode v3**.

</div>

---

## 📘 Overview

Local SHAP explanations answer:

- *“Why did the model produce this climate prediction here/now?”*  
- *“Which variables mattered the most at this location/time?”*  
- *“What signals contributed to this anomaly/event?”*

Local SHAP is essential for:

- Event-level Story Nodes  
- Focus Mode “local reasoning windows”  
- Climate anomaly debugging  
- Governance review of model behavior  

Outputs must be:

- Deterministic  
- FAIR+CARE compliant  
- Version-pinned  
- JSON-LD structured  
- STAC v11 compatible  
- Provenance linked  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/shap/local/
    ├── 📄 README.md                        # This file
    │
    ├── 📄 local.json                      # Per-prediction SHAP vectors
    ├── 📄 samples.json                    # Optional: multiple example event explanations
    │
    └── 📁 jsonld/                         # JSON-LD explainability bundles
        ├── 📄 xai-shap-local.jsonld       # Local semantic explainability
        └── 📄 xai-shap-driver-codes.jsonld# Narrative driver categories

---

## 🔍 Local SHAP Explainability Components

### 1. 🟥 `local.json`
Contains local SHAP vectors per prediction:

- Feature contributions (positive/negative)  
- Climate variable mapping (temp, precip, winds, humidity, terrain, etc.)  
- Normalized impact magnitudes  
- Confidence estimates  
- CARE masking indicators  
- Model version metadata  
- STAC input dataset IDs (if provided)  

Used for:

- Climate event analysis  
- Drift detection  
- Narrative driver extraction  

---

### 2. 🧾 `samples.json`
Optional curated set of:

- Multiple local event explanations  
- Cross-sample driver comparisons  
- Climate anomaly case studies (masking applied)  

---

### 3. 🟩 JSON-LD Bundles (in `/jsonld`)

#### **`xai-shap-local.jsonld`**  
Local semantic explainability for one event or group of events:

- `xai:drivers` list (feature → magnitude)  
- `xai:spatial_context` (H3 generalized)  
- `xai:care_scope`  
- `prov:*` lineage  
- `kfm:model_version`  
- `kfm:input_items`  

#### **`xai-shap-driver-codes.jsonld`**  
Maps raw SHAP features → human/narrative-safe driver codes:

- Canonical climate driver codes  
- CARE-filtered descriptions  
- Story Node v3 semantic roles  
- Focus Mode v3 reasoning labels  

---

## 📡 STAC Integration Requirements

Local SHAP MUST supply:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- Input STAC datasets (`kfm:input_items`)  
- Multihash checksums  
- CRS + spatial metadata (if applicable)  
- CARE masking metadata  

---

## 🧾 PROV-O Lineage Requirements

Each local SHAP asset must include:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (input climate STAC Items)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` (model → SHAP → narrative chain)  

---

## 🔐 FAIR+CARE Requirements

Local SHAP must:

- Apply H3 generalization for any geospatial references  
- Mask/remove culturally sensitive or sovereignty-restricted correlations  
- Include `<care:scope>` metadata  
- Use narrative-safe text in driver summaries  
- Avoid speculative or non-evidence-based climate claims  

---

## 🧪 Testing Requirements

Local SHAP pipelines MUST pass:

- Deterministic output comparison  
- JSON-LD schema validation  
- STAC XAI extension validation  
- CRS/vertical-datum checks  
- CARE masking + sovereignty tests  
- Drift baseline stability checks  

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate SHAP Local explainability spec aligned with suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate SHAP](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

