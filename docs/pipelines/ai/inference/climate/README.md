---
title: "🌡️🤖 KFM v11.2.2 — Climate AI Inference Pipelines (Realtime · Batch · STAC-Aligned · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Pipeline Layer (AI Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Inference"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-inference-pipelines"
  - "ai-prediction-climate"
  - "batch-and-realtime-inference"
  - "xai-ready-inference"
  - "prov-xai"
  - "stac-xai"
  - "story-node-climate"
  - "focus-mode-climate"
  - "care-governance"

scope:
  domain: "pipelines/ai/inference/climate"
  applies_to:
    - "realtime-climate-inference"
    - "batch-climate-inference"
    - "deep-climate-models"
    - "climate-downscaling"
    - "bias-correction"
    - "hazard-linked-climate"
    - "xai-integration"
    - "care-governance"
    - "stac-xai"
    - "prov-xai"
    - "focus-mode-ai"

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

# 🌡️🤖 **Climate AI Inference Pipelines (KFM v11.2.2)**  
`docs/pipelines/ai/inference/climate/README.md`

**Purpose:**  
Define the **AI inference layer for climate modeling** in KFM v11.2.2, including realtime + batch inference of downscaled climate variables, anomaly detection, bias correction, hazard-linked climate drivers, and XAI-aligned outputs compatible with **Story Node v3**, **Focus Mode v3**, and **STAC-XAI v11**.

</div>

---

## 📘 Overview

Climate inference pipelines transform curated climate datasets into **operational predictions**, semantic climate drivers, and XAI outputs.

Supports:

- **Realtime inference** (API streaming, sub-hourly)
- **Batch inference** (nightly/weekly DAGs)
- **Downscaling**  
- **Bias correction**
- **Seasonal/long-range anomaly detection**
- **Hazard-linked climate predictors** (e.g., tornado-supporting environments)
- **Multi-model fusion** (e.g., ERA5 × Daymet × HRRR × CMIP6 analogs)

All inference outputs:

- Are **STAC-aligned**  
- Are **deterministic under seed lock**  
- Produce **JSON-LD XAI metadata**  
- Carry **FAIR+CARE + sovereignty compliance**  
- Include **complete PROV-O lineage**  
- Feed directly into Story Nodes + Focus Mode v3  

---

## 🧠 Supported Climate Inference Types

### 1. 🌎 Downscaling Pipelines  
Models: CNN downscalers · UNet · Transformer downscalers  

Outputs:  
- High-resolution temperature, RH, wind, soil moisture, precip  
- Deterministic seeds  
- STAC Items  
- Optional CAMs/IG/SHAP attribution  

### 2. 🌡️ Anomaly Detection  
Models: Autoencoders · seq2seq · LSTM/Transformer anomaly detectors  

Outputs:  
- Seasonal + sub-seasonal anomalies  
- Climate cluster deviations  
- Semantic JSON-LD anomaly descriptors  

### 3. 💨 Severe-Weather Climate Drivers  
Models: Multi-hazard climate classifier, env-parameter predictor  

Outputs:  
- CAPE, CIN, SRH, lapse rates  
- Derived hazard-linked drivers  
- XAI-ready climate driver semantics  

### 4. 📉 Bias Correction  
Methods: Quantile-mapping, ML-based Q-mapping, analog ML correction  

Outputs:  
- Bias-corrected climate series  
- STAC lineage to input raw climate layers  
- Metadata linking to training sets  

### 5. 🔮 Long-Range Climate Forecasting  
Models: Transformer climate-forecast models, extended analog ensembles  

Outputs:  
- 10–90-day forecasts  
- Extremes predictions  
- Global/local JSON-LD semantic forecasts  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/
    ├── 📄 README.md                              # This file
    │
    ├── 📁 batch/                                 # Batch DAG inference pipelines
    │   ├── 📄 README.md
    │   └── 🧠 batch_inference_flow.py
    │
    ├── 📁 realtime/                              # Streaming/realtime inference
    │   ├── 📄 README.md
    │   └── ⚡ realtime_inference_server.py
    │
    ├── 📁 models/                                # Climate inference model cards (no weights)
    │   ├── 📄 README.md
    │   ├── 📁 downscaling/
    │   ├── 📁 anomalies/
    │   ├── 📁 hazards/
    │   └── 📁 bias-correction/
    │
    ├── 📁 jsonld/                                # Semantic inference outputs
    │   ├── 📄 README.md
    │   ├── 📄 xai-climate-local.jsonld
    │   ├── 📄 xai-climate-global.jsonld
    │   └── 📄 climate-driver-taxonomy.jsonld
    │
    └── 📁 telemetry/                             # OTel + lineage metrics
        ├── 📄 README.md
        └── 📊 inference-metrics.json

---

## 📡 STAC-XAI Requirements

All climate inference outputs MUST include:

- `kfm:explainability:method` (shap|integrated-gradients|cams|spatial)
- `kfm:explainability:{local|global}`
- `kfm:model_version`
- `kfm:input_items` (STAC dataset lineage)
- CRS/vertical metadata (if spatial)
- `checksum:multihash`
- CARE & sovereignty metadata  
- Link to JSON-LD explainability bundles  

---

## 🧾 PROV-O Lineage Requirements

Each inference product MUST encode:

- `prov:wasGeneratedBy` (inference run ID)
- `prov:used` (input STAC Items + model metadata)
- `prov:generatedAtTime`
- `prov:Agent` (model identity, pipeline version)
- Optional: `prov:wasDerivedFrom` (multimodal XAI fusion)

---

## 🔐 FAIR+CARE Requirements

All inference pipelines must:

- Follow CARE-safe climate representation  
- Avoid sensitive tribal/cultural speculation  
- Use H3 masking for spatial outputs when applicable  
- Provide CARE labels & sovereignty metadata  
- Adhere to Data Contract v3  
- Maintain reproducibility and non-speculative climate narratives  

---

## 🧪 Testing & CI Requirements

Pipelines MUST pass:

- Deterministic inference reproducibility tests  
- JSON-LD schema validation  
- STAC-XAI lints  
- PROV-O lineage tests  
- CARE + sovereignty rule checks  
- CRS/vertical axis validation  
- Bias-correction correctness tests  
- Drift detection tests  

Failures → ❌ merge blocked.

---

## 🕰 Version History

| Version | Date       | Notes                                                      |
|---------|------------|------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Climate AI Inference Layer spec for KFM v11.2.2    |
| v11.0.0 | 2025-11-22 | First AI inference integration into KFM                    |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Inference](../README.md) · [🧠 AI Pipeline Layer](../../README.md) · [🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

