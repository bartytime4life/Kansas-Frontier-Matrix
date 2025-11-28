---
title: "🌡️ KFM v11.2.2 — Climate AI Models (Forecasting · Downscaling · Bias Correction · Explainability)"
path: "docs/pipelines/ai/models/climate/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Family"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-models-climate-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-models-climate-v11.2.2.json"
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
sensitivity: "Climate-Model"
sensitivity_level: "Medium"
public_exposure_risk: "Low"

semantic_intent:
  - "climate-ml"
  - "forecasting"
  - "downscaling"
  - "bias-correction"
  - "model-cards"
  - "xai-stac"
  - "governed-ml"

scope:
  domain: "ai-models-climate"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "stac-integrated-climate-models"
    - "xai"
    - "focus-mode-integration"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🌡️ **KFM v11.2.2 — Climate AI Model Family**  
`docs/pipelines/ai/models/climate/README.md`

**Purpose:**  
Define, govern, and document all **Climate AI models** used by KFM, including forecasting, downscaling, bias correction, anomaly detection, and climate-derived environmental indicators.  
All models here must follow **Model Card v11.2.2**, **FAIR+CARE**, **PROV-O lineage**, and **KFM-STAC v11** publishing rules.

</div>

---

## 📘 Overview

The *Climate Model Family* includes all ML/AI models used to:

- Downscale climate data  
- Predict anomalies and deviations  
- Generate seasonal/annual forecasts  
- Bias-correct historical or reanalysis datasets  
- Produce hydrology-relevant climate indicators  
- Generate explainability outputs (SHAP, IG, CAMs)  
- Provide semantic inputs for Focus Mode v3 and Story Nodes  

Every model in this directory must include:

- **Model Card v11.2.2**  
- **Complete training metadata**  
- **Evaluation bundle** (regression, skill scores, golden-data comparison)  
- **Explainability artifacts**  
- **STAC publishing template**  
- **Energy/Carbon usage profile**  
- **CARE masking & governance metadata**  

No model may transition to production without all required metadata.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/climate/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 model-card.jsonld                        # Model Card (v11.2.2)
    ├── 📄 training-metadata.json                   # Hyperparams, datasets, seeds
    ├── 📄 evaluation-report.md                     # Metrics + regression results
    ├── 📄 explainability.json                      # SHAP / IG / CAMs / feature attribution
    │
    ├── 📁 examples/                                # Example results + artifacts
    │   ├── 📄 shap-global.json
    │   ├── 📄 shap-local.json
    │   ├── 📄 attribution-map.png
    │   └── 📄 model-forecast-sample.png
    │
    ├── 📁 stac/                                    # STAC metadata templates
    │   ├── 📄 climate-model-item.json
    │   └── 📄 assets-template.json
    │
    └── 📁 mlops/                                   # Deployment + monitoring configs
        ├── 📄 inference-config.yaml
        ├── 📄 retraining-policy.md
        └── 📄 drift-monitoring.md

---

## 🧬 Climate Model Categories

### 1. 📈 Forecasting Models
Used for:

- Seasonal climate prediction  
- Deterministic & probabilistic forecasts  
- Weather-derived indicators  

Must provide:

- Skill scores (RMSE, MAE, CRPS, etc.)  
- Feature attribution (SHAP mandatory)  
- PROV-O lineage: upstream STAC → model → STAC outputs  

---

### 2. 🪶 Downscaling Models
Sources: Daymet, ERA5, PRISM, gridMET, etc.

Downscaling pipelines must:

- Lock random seeds  
- Publish spatial metadata (CRS, extent)  
- Emit explainability graphics for hydrology-critical variables  
- Produce STAC Items for all geospatial outputs  

---

### 3. 🎯 Bias-Correction Models
- Quantile mapping  
- ML-based bias adjustment  
- Hybrid climate-informed correction  

Must include:

- Before/after comparison artifacts  
- FAIR+CARE masking for sensitive climatology if derived from Indigenous knowledge sources  

---

### 4. 🌡️ Anomaly Detection Models
- Detect climate anomalies (temperature, precipitation, drought indices)  
- Provide anomaly classification + severity levels  
- All outputs must pass reproducibility checks  
- XAI explanations required for anomaly scores  

---

### 5. 🧭 Focus Mode v3 Climate Reasoners
Specialized semantic reasoning modules that:

- Synthesize climatic, hydrological, and landform features  
- Generate contextual explanations  
- Integrate with Story Node v3 narratives  
- Enforce CARE masking and Indigenous sovereignty policies  

---

## 📡 STAC Integration (KFM-STAC v11)

Climate-model outputs MUST publish:

- `kfm:climate:model_name`  
- `kfm:climate:model_version`  
- `kfm:climate:method`  
- `kfm:explainability:*`  
- `kfm:input_items` (array of STAC IDs used as input)  
- CRS, vertical datum, bounding boxes  
- Asset checksums (`checksum:multihash`)  
- PROV-O lineage specifying training + inference  

---

## 🧠 Explainability Requirements

All climate models require:

- **SHAP (global + local)**  
- **Integrated Gradients (for deep models)**  
- **CAMs/saliency (for spatial CNNs)**  
- Masked/abstracted explanations for sensitive regions  
- JSON-LD exports for:
  - Story Nodes  
  - Focus Mode evidence maps  
  - Internal audit dashboards  

---

## 🔐 FAIR+CARE Requirements

Climate models MUST:

- Use STAC-validated datasets  
- Include training data licenses + constraints  
- Apply CARE masking to any Indigenous or culturally sensitive regions  
- Avoid speculative interpretations  
- Maintain full transparency in:
  - data provenance  
  - model provenance  
  - inference provenance  

---

## 🧪 Testing Requirements

Climate AI models must pass:

- Seed-locked reproducibility tests  
- Evaluation regression tests  
- Explainability drift tests  
- STAC schema validation  
- CARE/FAIR governance checks  
- Training metadata schema validation  
- Golden-record tests  

ALL failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                            |
|----------|------------|------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full uplift to v11.2.2; XAI bundles; STAC templates; emoji tree |
| v11.0.0  | 2025-11-22 | Initial climate model family introduction                        |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Models Index](../README.md) · [🤖 AI Inference Layer](../../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

