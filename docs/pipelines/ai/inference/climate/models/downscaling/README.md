---
title: "🌡️⬇️🤖 KFM v11.2.2 — Climate Downscaling Models (High-Resolution Inference · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/downscaling/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Subcategory (Downscaling)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"

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
sensitivity: "Climate-Downscaling-Models"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "downscaling-models"
  - "high-resolution-climate-models"
  - "unet-downscaling"
  - "transformer-downscaling"
  - "seed-locked-downscalers"
  - "xai-ready-climate-models"
  - "stac-xai-models"
  - "story-node-climate"
  - "focus-mode-climate"

scope:
  domain: "pipelines/ai/inference/climate/models/downscaling"
  applies_to:
    - "unet-downscaler.md"
    - "transformer-downscaler.md"
    - "deterministic-downscaling"
    - "bias-aware-downscaling"
    - "xai-compatible-downscalers"

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

# 🌡️⬇️🤖 **Climate Downscaling Models — KFM v11.2.2**  
`docs/pipelines/ai/inference/climate/models/downscaling/README.md`

**Purpose**  
Define and govern the **high-resolution climate downscaling models** used for KFM realtime and batch inference, ensuring deterministic behaviour, XAI readiness, STAC-compatible outputs, and FAIR+CARE-compliant operation.

</div>

---

## 📘 Overview

Downscaling models convert **coarse-resolution climate fields** into **high-resolution gridded outputs** that drive:

- Realtime inference (tile-based downscaling for live maps)  
- Batch pipelines (daily or monthly statewide/regional downscaled fields)  
- Climate driver generation (inputs to hazard models)  
- Story Node v3 semantic timelines and spatial narratives  
- Focus Mode v3 climate overlays and context panes  

All downscaling models in this directory:

- Are **deterministic** when seed-locked  
- Expose **XAI compatibility** (SHAP, IG, and/or CAM)  
- Emit **CRS + vertical axis + STAC-XAI metadata** via the inference layer  
- Include **CARE + sovereignty compliance statements** in their model cards  
- Must pass **CI model-card validation** and governance review  

Model weights are not stored here; only **model cards and metadata**.

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/models/downscaling/
    ├── 📄 README.md                    # This file
    │
    ├── 📄 unet-downscaler.md           # U-Net based downscaling model card
    └── 📄 transformer-downscaler.md    # Transformer-based downscaler model card

---

## 🧩 Downscaling Model Types

### 1. 🧱 U-Net Downscaler

A convolutional encoder–decoder architecture tailored to climate gridded data.

Characteristics:

- High spatial fidelity for variables like temperature, RH, soil moisture  
- Well-suited for static or short-window downscaling  
- CAM and IG can be applied to inspect feature importance and spatial sensitivity  
- Deterministic inference with fixed seeds and stable pre-processing  

Typical uses:

- Daily state-level downscaled grids  
- Fine-scale diagnostics for Story Nodes and Focus Mode  

---

### 2. 🔮 Transformer Downscaler

A sequence-aware architecture that captures temporal and multi-variate dependencies.

Characteristics:

- Handles multi-step temporal windows  
- Supports joint downscaling of multiple climate fields  
- SHAP and IG are used for feature and time-step attribution  
- Effective for dynamic phenomena (e.g., frontal passages, heatwaves)  

Typical uses:

- Downscaled time series for anomaly detection  
- Multi-day rolling downscaled climate sequences  

---

## 🎛 Downscaling Model Requirements

All downscaling models MUST:

- Provide a **model card** including:
  - Architecture description  
  - Training dataset descriptions and licenses  
  - Pre-processing & normalization details  
  - Hyperparameters and random seeds  
  - Evaluation metrics (RMSE, MAE, spatial correlation, bias indices)  
  - Sustainability metrics (training energy Wh and gCO₂e)  

- Declare **XAI compatibility**:
  - SHAP global/local  
  - IG global/local  
  - CAM-based spatial attributions (when applicable)  

- Provide **governance content**:
  - CARE and sovereignty impact analysis  
  - Statement of acceptable use  
  - Known limitations and failure modes  

- Support **STAC-XAI output**:
  - `kfm:model_version`  
  - `kfm:explainability:*` fields at inference-time  

---

## 🧬 Conceptual Downscaling Flow

(If you want a Mermaid block in the repo, add a `flowchart TD` fenced with ```mermaid directly there; here it is shown as plain text to preserve the single-box rule in chat.)

    Coarse Climate Input
        ↓
    Load Downscaling Model (seed-locked)
        ↓
    Run Downscaling Inference
        ↓
    Postprocess and Enforce CRS / Vertical Axis
        ↓
    Optional XAI Processing (SHAP / IG / CAM)
        ↓
    Emit STAC-XAI Outputs and Telemetry

---

## 🧪 CI Validation

CI for downscaling models MUST check:

- Model card schema compliance  
- Deterministic output under identical seeds and inputs  
- XAI readiness (at least one method supported and documented)  
- CRS + vertical axis metadata consistency  
- CARE and sovereignty fields populated and valid  
- STAC-XAI compatibility metadata present in model references  
- Sustainability metrics fields provided (training and inference, if available)  

Any failure → **merge blocked** until the model card and metadata are corrected.

---

## 🕰 Version History

| Version  | Date       | Notes                                               |
|----------|------------|-----------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial downscaling model subcategory documentation |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Models](../README.md) · [🌡️ Climate Pipeline Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
