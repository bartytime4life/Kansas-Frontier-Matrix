---
title: "📘 KFM v11.2.2 — AI Pipeline Templates (Model Cards · Training Specs · Evaluation Bundles · XAI Schemas)"
path: "docs/pipelines/ai/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template Library"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/ai-templates-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-templates-v11.2.2.json"
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
sensitivity: "AI-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "ai-templates"
  - "model-cards"
  - "training-configs"
  - "evaluation-bundles"
  - "xai-templates"
  - "jsonld-schemas"
  - "ml-governance"

scope:
  domain: "ai-templates"
  applies_to:
    - "model-cards"
    - "training-specs"
    - "evaluation-reports"
    - "xai-bundles"
    - "inference-metadata"
    - "provenance-jsonld"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 📘 **KFM v11.2.2 — AI Pipeline Templates**  
`docs/pipelines/ai/templates/README.md`

**Purpose:**  
Provide **canonical, governed templates** for all AI/ML artifacts in KFM v11.2.2 — including **Model Cards**, **Training Specs**, **Evaluation Bundles**, **Explainability (XAI) bundles**, **Inference metadata**, and **Story Node v3 JSON-LD scaffolds**.  
These templates enforce **determinism**, **traceability**, **FAIR+CARE compliance**, and **STAC/PROV-O alignment** for all KFM AI pipelines.

</div>

---

## 📘 Overview

This template library ensures:

- Every AI model includes a **Model Card v11.2.2**  
- All training/inference pipelines use standardized metadata structures  
- All outputs are **reproducible**, **auditable**, and **story-node compatible**  
- All XAI outputs follow the same JSON-LD scaffolding  
- All provenance follows **PROV-O** + **STAC v11** conventions  
- All sensitive fields adhere to **CARE** masking & sovereignty policies  

These templates are **mandatory** for:

- Climate models  
- Hydrology models  
- Hazard/wildfire models  
- NLP/NER/geoparsing models  
- Embedding models  
- Focus Mode v3 reasoning engines  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/templates/
    ├── 📄 README.md                                      # This file
    │
    ├── 📁 model-cards/                                   # Model Card v11.2.2 templates
    │   ├── 📄 model-card-template.jsonld
    │   ├── 📄 training-metadata-template.json
    │   └── 📄 evaluation-report-template.md
    │
    ├── 📁 explainability/                                # XAI JSON-LD templates
    │   ├── 📄 xai-global-template.jsonld
    │   ├── 📄 xai-local-template.jsonld
    │   └── 📄 xai-visualization-template.md
    │
    ├── 📁 inference/                                     # Inference pipeline metadata templates
    │   ├── 📄 inference-metadata-template.json
    │   ├── 📄 stac-item-template.json
    │   └── 📄 provenance-template.jsonld
    │
    ├── 📁 story-nodes/                                   # Story Node v3 templates
    │   ├── 📄 story-node-template.jsonld
    │   └── 📄 narrative-scaffold-template.md
    │
    └── 📁 mlops/                                         # MLOps + drift monitoring templates
        ├── 📄 drift-monitoring-template.json
        ├── 📄 retraining-policy-template.md
        └── 📄 deployment-config-template.yaml

---

## 🧬 Template Types

### 1. 🧬 Model Cards (v11.2.2)
Mandatory components:

- Identity  
- Training provenance  
- Hyperparameters  
- Architecture  
- Evaluation bundle  
- Explainability  
- FAIR+CARE restrictions  
- Energy/Carbon telemetry  

Used in:

- All model families (climate, hydrology, hazards, NLP, embeddings, focus-mode)

---

### 2. 🧪 Training Specs & Metadata
Must include:

- Dataset sources (STAC Collections)  
- Seeds  
- Hyperparameters  
- Training lineage (OpenLineage spans)  
- CARE auditing rules  
- Energy/Carbon estimates  

---

### 3. 🔍 Explainability Bundles (XAI JSON-LD)
Provide:

- SHAP global & local attribution  
- Integrated Gradients  
- CAM/saliency maps  
- Spatial masking (if required)  
- Evidence graphs for Story Nodes  

---

### 4. ⚙️ Inference Metadata Templates
Support:

- Batch inference  
- Realtime inference  
- Model versioning  
- Deterministic outputs  
- Provenance → STAC mapping  
- Focus Mode v3 integration  

---

### 5. 📘 Story Node v3 Templates
Templates define:

- Narrative body  
- Temporal grounding  
- Spatial grounding  
- Explainability summary  
- Provenance block (`prov:*`)  
- CARE masking & abstraction rules  

These templates ensure **consistent narrative safety and governance compliance**.

---

### 6. 🧪 Drift Monitoring & MLOps Templates
Support:

- Model drift detection  
- Threshold policies  
- Retraining pipelines  
- Version promotion rules  
- Energy/Carbon trend tracking  

---

## 🔐 FAIR+CARE Governance

All templates enforce:

- Cultural data protection  
- H3 generalization for sensitive spatial outputs  
- No inference of tribal identity  
- Dataset license disclosure  
- Sovereignty policy integration  
- Provenance traceability  

Templates failing governance checks → **CI blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                  |
|----------|------------|--------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full template suite built for v11.2.2; emoji tree added |
| v11.0.0  | 2025-11-15 | Initial template library                               |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Pipelines Index](../README.md) · [🧠 AI Model Cards](../models/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
