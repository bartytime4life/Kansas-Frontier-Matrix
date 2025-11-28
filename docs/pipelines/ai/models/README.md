---
title: "🧬 KFM v11.2.2 — AI Model Repository (Model Cards · Training Metadata · FAIR+CARE Compliance)"
path: "docs/pipelines/ai/models/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Repository Index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/ai-models-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-models-v11.2.2.json"
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
sensitivity: "AI Models"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "ai-models"
  - "model-cards"
  - "governed-ml"
  - "traceable-ai"
  - "faircare-compliant"

scope:
  domain: "ai-models"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "explainability"
    - "provenance"

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

# 🧬 **KFM v11.2.2 — AI Model Repository**  
`docs/pipelines/ai/models/README.md`

**Purpose:**  
Provide the **canonical index** for all **AI/ML model cards**, **training metadata**, **evaluation bundles**, and **provenance records** used across the Kansas Frontier Matrix AI Pipeline Layer.  
This directory defines the **Model Card v11.2.2 standard**, governs all model lifecycle metadata, and ensures complete **FAIR+CARE**, **STAC**, and **PROV-O** compliance for any deployed or experimental model.

</div>

---

## 📘 Overview

The **AI Models Repository** organizes:

- Model Cards (v11.2.2)  
- Training lineage & metadata  
- Evaluation/metrics bundles  
- Explainability artifacts (global/local XAI)  
- FAIR+CARE compliance documentation  
- Environmental impact telemetry (energy & carbon)  
- STAC-compatible metadata and schema-linked properties  

Every model in KFM must include:

- **Model Card v11.2.2**  
- **Provenance (PROV-O)**  
- **Training dataset registry references**  
- **Hyperparameter history**  
- **Eval metrics + golden-record regression results**  
- **Fairness/CARE audits**  
- **Explainability bundle**  
- **Version fingerprint (model_version)**  
- **Energy/carbon usage profile**  

No model is permitted in production **without a complete Model Card**.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/
    ├── 📄 README.md                                  # This file
    │
    ├── 📁 climate/                                   # Models for climate inference
    │   ├── 📄 model-card.jsonld                      # Model Card v11.2.2
    │   ├── 📄 training-metadata.json                 # Hyperparams, datasets, seeds
    │   ├── 📄 evaluation-report.md                   # Metrics + regression tests
    │   └── 📄 explainability.json                    # Global/Local XAI
    │
    ├── 📁 hydrology/                                 # Hydrology prediction models
    │   ├── 📄 model-card.jsonld
    │   ├── 📄 training-metadata.json
    │   ├── 📄 evaluation-report.md
    │   └── 📄 explainability.json
    │
    ├── 📁 hazards/                                   # Hazard/wildfire/tornado models
    │   ├── 📄 model-card.jsonld
    │   ├── 📄 training-metadata.json
    │   ├── 📄 evaluation-report.md
    │   └── 📄 explainability.json
    │
    ├── 📁 nlp/                                       # NLP + entity extraction models
    │   ├── 📄 model-card.jsonld
    │   ├── 📄 vocabulary-metadata.json
    │   ├── 📄 alignment-tests.md
    │   └── 📄 xai.json
    │
    ├── 📁 embeddings/                                # Embedding models (vector search)
    │   ├── 📄 model-card.jsonld
    │   ├── 📄 training-metadata.json
    │   ├── 📄 evaluation-report.md
    │   └── 📄 explainability.json
    │
    └── 📁 focus-mode/                                # Focus Mode v3 reasoning models
        ├── 📄 model-card.jsonld
        ├── 📄 training-metadata.json
        ├── 📄 narrative-evaluation.md
        └── 📄 explainability.json

(**Note:** Model binaries/checkpoints are *not stored in the repo*—only metadata, lineage, and documentation.)

---

## 🧠 Model Card Requirements (v11.2.2)

All Model Cards MUST include:

### 🔹 **1. Identity**
- `model_name`  
- `model_version` (semver)  
- `model_uuid`  
- `release_stage` (dev, staging, prod)  

### 🔹 **2. Training Provenance**
- STAC Collection(s) used as training sources  
- Dataset ID list + version tags  
- `prov:used` relations  
- Training environment / container fingerprint  

### 🔹 **3. Hyperparameters & Architecture**
- Model architecture  
- Loss function  
- Optimizer + LR schedule  
- Random seed (locked)  

### 🔹 **4. Evaluation Bundle**
- Regression metrics (destined for nightly diff)  
- Golden-record comparisons  
- Drift detection metrics  

### 🔹 **5. Explainability**
- SHAP global attribution  
- Local attributions  
- CAMs / saliency (if spatial)  
- Integrated Gradients (if deep learning)  

### 🔹 **6. FAIR+CARE**
- CARE masking rules  
- Restrictions or exclusions  
- Ethical guidelines for use  
- Validity caveats (no speculation, no ungrounded inference)  

### 🔹 **7. Energy/Carbon**
- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  

---

## 🤖 Model Lifecycle (v11.2.2)

### 🟧 Training Phase
- Dataset loading via STAC only  
- Hyperparam logging  
- Seed locking  
- Explainability capture  

### 🟦 Evaluation Phase
- Metrics saved into evaluation bundles  
- Golden-record diffs  
- CARE-mask checking  

### 🟩 Production Deployment
- Model Card frozen  
- Training metadata stored  
- STAC + PROV-O lineage published  
- Telemetry enabled  

Any model failing reproducibility or fairness checks → **blocked**.

---

## 📡 Integration with Inference & Story Nodes

All models must support:

- **Inference metadata injection**  
- **Focus Mode v3 reasoning**  
- **Story Node v3 narrative generation**  
- **Explainability → narrative mapping**  
- XAI sidecars attached to STAC Items  

---

## 🧪 Testing Requirements

Required unit tests:

- Seed-locked reproducibility  
- Model Card schema validation  
- Evaluation metric regression tests  
- Explainability drift tests  
- Governance (FAIR+CARE) compliance tests  

PRs failing any test → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                 |
|----------|------------|-------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade to v11.2.2; new telemetry schema; emoji tree |
| v11.0.0  | 2025-11-20 | Initial AI Model Repository structure                 |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Pipelines](../README.md) · [🤖 Inference Layer](../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
