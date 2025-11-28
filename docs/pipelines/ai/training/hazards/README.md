---
title: "⚡ KFM v11.2.2 — Hazard Model Training Pipelines (Wildfire · Tornado · Flood · Drought · Severe Weather)"
path: "docs/pipelines/ai/training/hazards/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Training Pipeline"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-training-hazards-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-training-hazards-v11.2.2.json"
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
sensitivity: "Hazard-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ai-training"
  - "wildfire"
  - "tornado"
  - "hail-wind"
  - "flood-risk"
  - "drought-anomalies"
  - "terrain-hazard-fusion"
  - "provenance"
  - "faircare-governance"
  - "xai-training"
  - "energy-carbon"

scope:
  domain: "ai-training-hazards"
  applies_to:
    - "training-configs"
    - "training-dags"
    - "evaluation-bundles"
    - "model-cards"
    - "hazard-xai"
    - "provenance"
    - "stac-linked-training"
    - "drift-handling"
    - "energy-carbon-telemetry"

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

# ⚡ **KFM v11.2.2 — Hazard AI Training Pipelines**  
`docs/pipelines/ai/training/hazards/README.md`

**Purpose:**  
Define the deterministic, reproducible, STAC-linked training pipelines for **hazard AI models**, covering wildfire, tornado, hail, wind, severe weather, flood, flash-flood, drought, and compound hazard fusion models, with strict **FAIR+CARE**, **PROV-O**, **XAI**, and **Energy/Carbon** reporting.

</div>

---

## 📘 Overview

Hazard Training Pipelines generate:

- Wildfire probability/spread predictors  
- Tornado/hail/wind severity models  
- Flash-flood risk models (DEM × rainfall × soils)  
- Flood inundation ML layers  
- Drought & heatwave anomaly detection  
- Compound hazard fusion (climate × terrain × hydrology × vegetation)  
- Train-time explainability bundles (SHAP, Integrated Gradients, CAMs)  
- Evaluation bundles (skill scores, regression tests)  
- Complete Model Cards v11.2.2  
- PROV-O + OpenLineage training provenance  
- Energy/Carbon telemetry (sustainability governance)

All training:

- MUST use STAC v11 datasets  
- MUST be deterministic and seed-locked  
- MUST include Data Contract v3 validation  
- MUST include CARE masking where needed (Indigenous or sensitive landforms)

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/hazards/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 training-config.yaml                    # Hyperparams, seeds, STAC sources
    ├── 📄 dag.md                                  # DAG overview (Airflow / LangGraph)
    ├── 📄 evaluation-metrics.md                   # Metrics + regression tests
    │
    ├── 📁 datasets/                               # STAC-linked dataset manifests
    │   ├── 📄 stac-inputs.json
    │   └── 📄 dataset-license-notes.md
    │
    ├── 📁 explainability/                         # Train-time XAI outputs (examples)
    │   ├── 📄 shap-global.json
    │   ├── 📄 integrated-gradients.json
    │   └── 📄 hazard-saliency.png
    │
    ├── 📁 evaluation/                             # Evaluation bundles
    │   ├── 📄 metrics.json
    │   ├── 📄 skill-scores.md
    │   └── 📄 regression-tests.json
    │
    └── 📁 provenance/                             # Training provenance
        ├── 📄 prov-trace.jsonld
        └── 📄 lineage-facets.json

---

## ⚡ Hazard Training Categories

### 1. 🔥 Wildfire Training
- Inputs: vegetation, fuel moisture, slope, terrain derivatives, HRRR wind/smoke  
- Outputs: probability grids, spread indicators  
- Required XAI: IG + saliency + SHAP global drivers  

### 2. 🌪️ Tornado & Severe Weather Training
- Inputs: radar-derived features, HRRR atmospheric variables, terrain influence  
- Outputs: tornado likelihood, hail/wind severity  
- Required evaluation: spatial skill scores + false-alarm metrics  

### 3. 🌧️ Flood & Flash-Flood Training
- Inputs: DEM, slope curvature, rainfall intensity, soils, climate anomalies  
- Outputs: flood probability rasters, composite risk grids  
- Required XAI: CAMs + IG to map terrain drivers  
- CARE notes: mask culturally sensitive floodplain regions  

### 4. 🌡️ Drought & Heatwave Training
- Inputs: climate anomalies, soil moisture, NDVI/land cover  
- Output: drought severity classes  
- Required evaluation: class imbalance metrics, temporal drift tests  

### 5. 🧬 Multi-Hazard Fusion Training
- Combines wildfire × drought × wind × terrain × hydrology  
- Required:  
  - Provenance chain across all domains  
  - Explicit fusion weights  
  - XAI mapping of driver contributions  
  - CARE masking for sensitive landscapes  

---

## ⚙️ Training Requirements

### Determinism
Training MUST:

- Lock all seeds  
- Version-lock hyperparameters  
- Version-lock STAC inputs  
- Record training environment fingerprint  

### STAC-Linked Governance
All inputs MUST declare:

- STAC Item/Collection IDs  
- Dataset license  
- CRS + vertical datum  
- Data Contract v3 compliance  

### Explainability (Train-Time)
Training MUST emit:

- SHAP (global + local)  
- Integrated Gradients (for deep geospatial models)  
- CAM/saliency maps for hazard/terrain models  
- JSON-LD XAI bundles (`kfm:explainability:*`)  

### Evaluation Bundle Requirements
Must include:

- RMSE, MAE, AUROC, Brier Score, CRPS (per hazard type)  
- Golden-record comparisons  
- Drift baselines  
- Calibration curves  

### Provenance & OpenLineage
Training MUST output:

- PROV-O `prov:*` relations  
- OpenLineage job/task spans  
- Training hash, model_version, dataset fingerprints  

### Energy/Carbon Telemetry
Training MUST record:

- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  
- Hardware & resource usage  

---

## 📡 STAC Publishing (Training Outputs)

Hydrology training MUST publish STAC metadata:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- `kfm:ml:training_inputs` (STAC IDs)  
- XAI bundle references  
- Evaluation bundle references  
- CRS + vertical axis  
- Multi-hash checksums  

Outputs may include:

- XAI bundles  
- Evaluation bundles  
- Risk grid examples  
- Model metadata  

---

## 🔐 FAIR+CARE Requirements

Hazard training MUST:

- Mask sacred/heritage floodplain areas (H3 generalization)  
- Remove sensitive Indigenous context from training text/labels  
- Declare CARE scope in Model Card  
- Avoid training on culturally restricted geographies  
- Follow ethical rules for hazard narratives  

---

## 🧪 Testing Requirements

Training MUST pass:

- Seed-locked reproducibility  
- STAC schema + dataset validation  
- Data Contract v3 schema validation  
- Explainability drift tests  
- Evaluation regression tests  
- CARE compliance tests  
- Carbon/Energy telemetry validation  
- Provenance schema checks  

All failures → **pipeline block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                            |
|----------|------------|------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade; governance, telemetry, XAI templates, emoji tree   |
| v11.0.0  | 2025-11-22 | Initial hazard training specification                             |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Training Index](../README.md) · [⚡ Hazard Models](../../models/hazards/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

