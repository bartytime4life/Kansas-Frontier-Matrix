---
title: "🌡️🤖📚 KFM v11.2.2 — Climate AI Inference Models (Downscaling · Drivers · Anomalies · Bias-Correction)"
path: "docs/pipelines/ai/inference/climate/models/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Reference Layer (Climate Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256-of-this-file>"

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
sensitivity: "Climate-Model-Cards"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-model-cards"
  - "downscaling-models"
  - "anomaly-models"
  - "climate-driver-models"
  - "bias-correction-models"
  - "seed-locked-models"
  - "xai-ready-models"
  - "story-node-climate"
  - "focus-mode-climate"

scope:
  domain: "pipelines/ai/inference/climate/models"
  applies_to:
    - "downscaling"
    - "anomalies"
    - "bias-correction"
    - "hazard-linked-climate"
    - "drivers"
    - "xai-ready-models"
    - "governed-model-cards"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_version_history: true
requires_purpose_block: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️🤖📚 **Climate AI Inference — Models Reference Layer**  
`docs/pipelines/ai/inference/climate/models/README.md`

**Purpose**  
Document, version, and govern all Climate AI inference models used in KFM v11.2.2, including downscalers, anomaly detectors, climate-driver predictors, and bias-correction models.  
This directory stores **model cards**, **metadata**, and **lineage**, but **never model weights**.

</div>

---

## 📘 Overview

The Climate AI model layer provides the **authoritative registry** for all models consumed by:

- Realtime inference  
- Batch inference  
- Long-range and seasonal predictive pipelines  
- Hazard-linked climate driver generation  
- XAI explainability pipelines (SHAP, IG, CAM, spatial attribution)  
- Story Node v3 semantic narration  
- Focus Mode v3 map and timeline reasoning  

All models registered here:

- Are **fully deterministic** under seed-lock  
- Emit **PROV-O lineage metadata**  
- Contain **CARE and sovereignty compliance statements**  
- Declare **XAI integration** capabilities  
- Use **STAC-compatible metadata blocks**  
- Must pass **CI model-card validation**  

Model weights and large artifacts live **outside** the repository and are referenced from model cards.

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/models/
    ├── 📄 README.md                   # This file
    │
    ├── 📁 downscaling/                # Downscaling model cards
    │   ├── 📄 unet-downscaler.md
    │   └── 📄 transformer-downscaler.md
    │
    ├── 📁 anomalies/                  # Seasonal / subseasonal anomaly detectors
    │   ├── 📄 autoencoder.md
    │   └── 📄 transformer-anomaly.md
    │
    ├── 📁 drivers/                    # Climate-driver prediction models
    │   ├── 📄 cape-cin-srh-model.md
    │   ├── 📄 lapse-rate-model.md
    │   └── 📄 llj-metrics-model.md
    │
    ├── 📁 bias-correction/            # Bias-correction models
    │   ├── 📄 quantile-mapping.md
    │   └── 📄 ml-bias-corrector.md
    │
    └── 📁 metadata/                   # Shared metadata and governance attachments
        ├── 📄 model-card-template.md
        ├── 📄 model-governance.md
        └── 📄 model-xai-compatibility.md

---

## 🔧 Model Categories

### 1. 🌎 Downscaling Models

Upscale coarse climate products to high-resolution fields.

Typical models:

- U-Net Downscaler  
- Transformer Downscaler  

Requirements:

- CRS and vertical axis correctness  
- STAC-compatible outputs  
- XAI compatibility (SHAP and/or IG)  
- Deterministic inference under fixed seeds  

---

### 2. 📉 Anomaly Detection Models

Detect departures from climatology or expected patterns.

Examples:

- Autoencoder anomaly detector  
- Temporal Transformer anomaly model  

Outputs:

- Anomaly scores and binary indicators  
- JSON-LD semantic anomaly descriptions  
- Inputs to Story Node anomaly narratives and Focus Mode “anomaly views”  

---

### 3. 🌡️ Climate Driver Models

Predict key environmental drivers that feed hazard models and decision tools:

- CAPE and CIN  
- SRH, bulk shear, LLJ metrics  
- Lapse rates, stability indices  
- Moisture transport, freeze–thaw indicators  

Outputs must:

- Be STAC-registered  
- Provide JSON-LD driver semantics  
- Support explainability (SHAP/IG)  

---

### 4. 🧪 Bias-Correction Models

Correct systematic biases in model outputs via:

- Quantile mapping  
- ML-based bias correctors  

These models:

- Must declare reference observations  
- Provide before/after metrics  
- Log energy and carbon footprint of training  
- Guarantee deterministic correction under seed-lock  

---

### 5. 📑 Metadata and Governance

Shared metadata resources:

- `model-card-template.md`  
  - Standardized model documentation (purpose, assumptions, training data, metrics, risks).  

- `model-governance.md`  
  - Approval workflows, review cycles, and deprecation rules.  

- `model-xai-compatibility.md`  
  - Matrix indicating which models support which XAI methods and in which modes (global/local/spatial).  

---

## 🧩 Model Lifecycle (Conceptual)

Model lifecycle for Climate AI inference:

1. **Author Model Card**  
2. **Run CI Validation (schema + governance + XAI readiness)**  
3. **Register Model in Climate Model Index**  
4. **Wire into Realtime / Batch pipelines**  
5. **Emit telemetry and PROV lineage for every use**  
6. **Periodically review for drift, performance, ethics, and CARE compliance**  

(If you want a Mermaid diagram here, add a `flowchart TD` block directly in the repo; this answer keeps a single fence for chat compliance.)

---

## 🧪 Model Requirements

All KFM Climate AI models MUST:

- Provide a **complete model card** using the template.  
- Declare **training datasets**, license terms, and data lineage.  
- Document **hyperparameters**, seed, and training routines.  
- Declare **XAI support** (SHAP, IG, CAM, Spatial Attribution).  
- Include **sustainability metrics** (energy Wh, carbon gCO₂e).  
- Include **CARE and sovereignty risk assessment**.  
- Pass **CI model-card validation and governance checks**.  
- Produce **deterministic outputs** given the same inputs and configuration.  

---

## 🕰 Version History

| Version  | Date       | Notes                                          |
|----------|------------|-----------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate AI model-layer specification. |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Inference](../README.md) · [🌡️ Climate Pipeline Root](../../README.md) · [🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

