---
title: "🏋️ KFM v11.2.2 — AI Training Pipeline Layer (Deterministic · Provenance-Rich · FAIR+CARE) "
path: "docs/pipelines/ai/training/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pipeline Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/ai-training-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-training-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "AI-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "ai-training"
  - "model-cards"
  - "provenance"
  - "faircare-training"
  - "xai"
  - "evaluation"
  - "reproducibility"

scope:
  domain: "ai-training"
  applies_to:
    - "training-dags"
    - "training-configs"
    - "model-cards"
    - "evaluation-bundles"
    - "xai"
    - "provenance"
    - "dataset-linking"
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

# 🏋️ **KFM v11.2.2 — AI Training Pipeline Layer**  
`docs/pipelines/ai/training/README.md`

**Purpose:**  
Define the **deterministic, governed AI training system** used across all KFM AI model families (climate, hydrology, hazards, NLP, embeddings, focus-mode).  
This includes reproducible training DAGs, dataset governance, STAC-linked training sources, explainability generation, evaluation bundles, and energy/carbon reporting.

</div>

---

## 📘 Overview

The **Training Layer** is responsible for:

- Preparing training-ready datasets from KFM STAC Collections  
- Running fully deterministic and reproducible model training  
- Producing complete Model Cards (v11.2.2)  
- Logging training provenance using PROV-O + OpenLineage  
- Generating evaluation bundles (metrics, golden-record tests)  
- Emitting XAI artifacts at train-time  
- Producing energy & carbon telemetry  
- Ensuring FAIR+CARE and sovereignty compliance  
- Locking dataset versions to guarantee reproducibility  

The training layer is **mandatory** for any model deployed in production, staging, or research-mode pipelines.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/
    ├── 📄 README.md                                  # This file
    │
    ├── 📁 climate/                                   # Climate training pipelines/configs
    │   ├── 📄 training-config.yaml
    │   ├── 📄 dag.md
    │   └── 📄 evaluation-metrics.md
    │
    ├── 📁 hydrology/                                 # Hydrology training
    │   ├── 📄 training-config.yaml
    │   ├── 📄 dag.md
    │   └── 📄 evaluation-metrics.md
    │
    ├── 📁 hazards/                                   # Hazard training
    │   ├── 📄 training-config.yaml
    │   ├── 📄 dag.md
    │   └── 📄 evaluation-metrics.md
    │
    ├── 📁 nlp/                                       # NLP / NER / OCR training
    │   ├── 📄 training-config.yaml
    │   ├── 📄 dag.md
    │   └── 📄 evaluation-metrics.md
    │
    ├── 📁 embeddings/                                # Embedding model training
    │   ├── 📄 training-config.yaml
    │   ├── 📄 dag.md
    │   └── 📄 evaluation-metrics.md
    │
    └── 📁 focus-mode/                                # Focus Mode reasoning models
        ├── 📄 training-config.yaml
        ├── 📄 dag.md
        └── 📄 evaluation-metrics.md

---

## 🧬 Training Principles (v11.2.2)

### 1. 🧪 Determinism & Reproducibility  
Training MUST be:

- Seed-locked  
- Version-locked  
- Data-locked (STAC-sourced with multihash verification)  
- Container-fixed  

### 2. 📦 STAC–Linked Dataset Governance  
All training inputs must be loaded using:

- STAC Collections  
- STAC Items  
- Dataset manifests  
- Dataset license references  

Direct file paths are **forbidden**.

### 3. 🧠 Explainability at Train-Time  
Training MUST emit:

- SHAP global + local attribution  
- IG / CAMs if deep learning  
- JSON-LD explainability bundle  
- CARE-masked driver explanations  

### 4. 📊 Model Evaluation Standards  
Evaluation bundles include:

- Regression tests  
- Golden-record comparison  
- Skill/error metrics  
- Calibration curves  
- Drift baselines  

### 5. 🔐 FAIR+CARE & Sovereignty  
Training MUST:

- Respect CARE masking  
- Document training data sources  
- Avoid training on restricted or culturally sensitive content  
- Declare license + sovereignty constraints in Model Card  

### 6. 🧭 Provenance & Traceability  
All training runs MUST produce:

- PROV-O lineage  
- OpenLineage spans  
- Training event logs  
- Model version fingerprints  
- Full hyperparameter dictionaries  

### 7. ⚡ Energy / Carbon Reporting  
Training MUST report:

- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  
- Hardware environment summary  

---

## 🎛 Training DAG Requirements

Training DAGs MUST:

- Use clear step boundaries for lineage tracing  
- Enforce idempotency for dataset downloads + pre-processing  
- Emit success/failure spans  
- Produce rollback-safe checkpoints  
- Trigger sensitive-data audits (geospatial + NLP)  
- Register output artifacts to the Model Repository  

---

## 📈 Drift Baselines & Versioning

Training pipelines MUST generate:

- Drift baselines for future inference  
- Version fingerprints (`model_version`, dataset version)  
- Seed + hyperparameter snapshots  
- Training set statistics  

Version increments follow:

- **MAJOR** — architecture/semantics change  
- **MINOR** — training improvements or hyperparameter updates  
- **PATCH** — determinism or bug fixes  

---

## 🧪 Testing Requirements

Training pipelines MUST pass:

- Seed-locked reproducibility tests  
- STAC schema validation for training data  
- Training metadata schema validation  
- Hardware/compute reproducibility checks  
- FAIR+CARE masking and licensing tests  
- Evaluation regression tests  
- Explainability drift tests  
- Governance checks  

Any failure → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                  |
|----------|------------|--------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Complete v11.2.2 uplift; governance + telemetry update |
| v11.0.0  | 2025-11-22 | Initial AI Training Layer specification               |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Pipelines](../README.md) • [🧬 Model Cards](../models/README.md) • [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
