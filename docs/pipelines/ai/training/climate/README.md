---
title: "🌡️ KFM v11.2.2 — Climate Model Training Pipelines (Downscaling · Forecasting · Bias Correction · FAIR+CARE)"
path: "docs/pipelines/ai/training/climate/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Training Pipeline"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-training-climate-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-training-climate-v11.2.2.json"
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
sensitivity: "Climate-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-ai-training"
  - "downscaling"
  - "bias-correction"
  - "forecast-training"
  - "xai-training"
  - "provenance"
  - "energy-carbon"
  - "faircare-training"

scope:
  domain: "ai-training-climate"
  applies_to:
    - "training-configs"
    - "training-dags"
    - "evaluation-bundles"
    - "model-cards"
    - "xai"
    - "provenance"
    - "stac-linked-training"

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

# 🌡️ **KFM v11.2.2 — Climate AI Training Pipelines**  
`docs/pipelines/ai/training/climate/README.md`

**Purpose:**  
Define the **deterministic, reproducible, STAC-driven AI training pipelines** for all climate models in KFM — including downscaling, seasonal forecasting, anomaly detection, and bias correction — with strict FAIR+CARE, PROV-O lineage, and explainability (XAI) integration.

</div>

---

## 📘 Overview

The **Climate Training Subsystem** is responsible for generating:

- Downscaled climate predictors  
- Seasonal/annual forecasts  
- Bias-corrected reanalysis datasets  
- Climate anomaly detectors  
- Explainability drivers (SHAP/IG/CAMs)  
- Evaluation bundles (skill scores, regression tests)  
- Full Model Cards v11.2.2  
- Training provenance (OpenLineage, PROV-O)  
- Energy/Carbon telemetry  

All pipelines use:

- **STAC v11 datasets** as canonical inputs  
- Seed-locked determinism  
- FAIR+CARE dataset handling  
- Version-locked hyperparameters  
- Governed training metadata schemas  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/climate/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 training-config.yaml                    # Config (hyperparams, dataset sources, seeds)
    ├── 📄 dag.md                                  # DAG overview (Airflow / LangGraph)
    ├── 📄 evaluation-metrics.md                   # Metrics + regression tests
    │
    ├── 📁 datasets/                               # STAC-linked dataset manifests
    │   ├── 📄 stac-inputs.json
    │   └── 📄 dataset-license-notes.md
    │
    ├── 📁 explainability/                         # Train-time XAI outputs (example-only)
    │   ├── 📄 shap-global.json
    │   ├── 📄 integrated-gradients.json
    │   └── 📄 cam-saliency.png
    │
    ├── 📁 evaluation/                             # Evaluation bundles from training
    │   ├── 📄 metrics.json
    │   ├── 📄 skill-scores.md
    │   └── 📄 regression-tests.json
    │
    └── 📁 provenance/                             # Training provenance bundles
        ├── 📄 prov-trace.jsonld
        └── 📄 lineage-facets.json

---

## 🧬 Training Pipeline Types

### 1. 🌡️ Downscaling Models
- Convert coarse-gridded data → high-resolution predictions  
- Input: ERA5, Daymet, PRISM, gridMET (via STAC Collections)  
- Output: COG / GeoParquet layers  
- Mandatory XAI: IG + CAMs  

### 2. 🎯 Bias-Correction Models
- Quantile mapping  
- Hybrid RF/NN bias correction  
- Required evaluation deliverables:
  - Before/after plots  
  - Distribution shift analysis  
  - Careful separation of STAC-derived vs model-derived values  

### 3. 📈 Forecasting Models
- Seasonal climate forecasting  
- Deterministic + probabilistic forecasts  
- Must log:
  - Skill metrics (RMSE, MAE, CRPS)  
  - Model Card  
  - Evaluation bundle  
  - XAI justification  

### 4. 🔍 Anomaly Detection Models
- Temperature / precip anomaly identifiers  
- Drought-state predictors  
- Required to generate:
  - anomaly_explainability.json  
  - anomaly_class_distribution.json  

---

## ⚙️ Training Requirements

### Determinism
Training MUST:

- Lock all seeds  
- Use versioned STAC datasets  
- Store hyperparameters in `training-config.yaml`  
- Log code version and environment fingerprint  

### Data Governance
All training inputs MUST declare:

- STAC IDs  
- Dataset license  
- Data Contract v3 compliance  
- CARE constraints  

### Explainability (Train-Time)
Training MUST produce:

- SHAP global & local vectors  
- Integrated Gradients for deep models  
- Saliency/CAM maps if spatial  
- JSON-LD explainability bundles  

### Evaluation
Evaluation bundle MUST include:

- All domain-relevant metrics  
- Golden-record test suite  
- Drift baselines for inference  
- Calibration curves  

### Provenance & Telemetry
Training processes MUST write:

- PROV-O lineage bundles  
- OpenLineage job/task spans  
- Energy/Carbon metrics  
- Training environment metadata  

---

## 📡 STAC Publishing (Training Outputs)

Training pipelines MUST publish to STAC:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- `kfm:ml:training_inputs` (STAC-linked)  
- Explainability asset references  
- Provenance metadata  
- Data Contract v3 alignment fields  
- CRS + vertical axis  

Outputs include:

- Evaluation assets  
- XAI bundles  
- Derived indicator tiles (optional)  

---

## 🔐 FAIR+CARE Requirements

Climate training MUST:

- Apply H3 masking for sensitive regions  
- Avoid training on restricted cultural/Indigenous data  
- Record CARE scope in Model Card  
- Enforce ethical review for any climate/hazard intersection  
- Disallow speculative content in narrative-linked models  

---

## 🧪 Testing Requirements

Climate training pipelines MUST pass:

- Seed-locked reproducibility tests  
- STAC dataset validation  
- Data Contract v3 schema validation  
- Evaluation regression tests  
- Explainability drift tests  
- Governance (FAIR+CARE) compliance tests  
- Carbon/Energy validation  

All failures block PR merges.

---

## 🕰 Version History

| Version  | Date       | Notes                                                        |
|----------|------------|--------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full uplift; governance, telemetry, STAC alignment           |
| v11.0.0  | 2025-11-22 | Initial climate training specification                        |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Training Index](../README.md) · [🌡️ Climate Models](../../models/climate/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

