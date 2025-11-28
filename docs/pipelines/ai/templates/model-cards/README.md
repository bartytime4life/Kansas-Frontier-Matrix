---
title: "📄 KFM v11.2.2 — Model Card Templates (AI/ML Governance · Provenance · FAIR+CARE · XAI)"
path: "docs/pipelines/ai/templates/model-cards/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template Specification"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-model-cards-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-model-cards-v11.2.2.json"
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
sensitivity: "Model-Metadata"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "model-card-templates"
  - "training-metadata"
  - "evaluation-bundles"
  - "xai-metadata"
  - "provenance-jsonld"
  - "ai-governance"

scope:
  domain: "ai-model-card-templates"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "xai-bundles"
    - "provenance-jsonld"
    - "stac-ready-model-metadata"

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

# 📄 **KFM v11.2.2 — Model Card Templates**  
`docs/pipelines/ai/templates/model-cards/README.md`

**Purpose:**  
Provide the **authoritative template suite** for **Model Card v11.2.2**, **Training Metadata**, and **Evaluation Bundles** used across all AI/ML models in KFM.  
These templates enforce **AI governance**, **FAIR+CARE**, **deterministic reproducibility**, **STAC v11 integration**, and **PROV-O traceability**.

</div>

---

## 📘 Overview

Every KFM AI model (climate, hydrology, hazards, NLP, embeddings, focus-mode) MUST publish:

- **Model Card (v11.2.2)**  
- **Training metadata bundle**  
- **Evaluation/metrics report**  
- **Explainability (XAI) bundle**  
- **Provenance JSON-LD**  
- **Energy/Carbon impact profile**  
- **CARE governance metadata**  

This directory provides the **blessed templates** ensuring:

- Predictable structure  
- Machine-extractable JSON-LD  
- Schema validation during CI  
- Cross-model consistency  
- Publication-ready STAC metadata  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/templates/model-cards/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 model-card-template.jsonld               # Model Card v11.2.2 canonical schema
    ├── 📄 training-metadata-template.json          # Training environment + hyperparams + seeds
    ├── 📄 evaluation-report-template.md            # Evaluation bundle (metrics, regression tests)
    ├── 📄 explainability-template.json             # XAI JSON-LD schema
    │
    ├── 📁 extras/                                  # Optional add-ons for model governance
    │   ├── 📄 fairness-audit-template.md
    │   ├── 📄 care-scope-template.json
    │   └── 📄 energy-carbon-template.json
    │
    └── 📁 stac/                                    # Templates for STAC model publication
        ├── 📄 model-stac-item-template.json
        └── 📄 assets-template.json

---

## 🧬 Model Card v11.2.2 — Required Sections

### 1. Identity
- `model_name`  
- `model_version`  
- `model_uuid` (required)  
- `release_stage`  
- `security_notes` (optional, for sensitive models)

### 2. Training Provenance
- STAC training dataset list  
- Dataset licenses & restrictions  
- Training lineage (`prov:used`, `prov:wasGeneratedBy`)  
- Training environment (container, code version)  
- Random seed (locked)  

### 3. Architecture & Hyperparameters
- Model architecture description  
- Hyperparameter table (JSON-LD)  
- Loss functions, optimizers, learning-rate schedule  

### 4. Evaluation Bundle
- All metrics relevant to domain  
- Golden-record regression tests  
- Drift detection snapshot  
- Confidence estimates  
- Data split documentation  

### 5. Explainability (XAI)
- SHAP global attribution  
- SHAP/LIME/IG local attribution  
- CAMs/saliency (for spatial models)  
- JSON-LD XAI bundle (`kfm:explainability:*`)  
- CARE-masked explanations when appropriate  

### 6. FAIR+CARE Governance
- CARE scope  
- Forbidden inference rules  
- Sensitive term/region handling  
- Ethical constraints  
- Sovereignty notes  

### 7. Energy & Carbon
Required via `energy_schema` + `carbon_schema`:

- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  
- Notes on inference/training compute footprint  

### 8. STAC Publishing Metadata
When model outputs feed into geospatial pipelines:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- `kfm:input_items` (upstream STAC Items)  
- CRS / vertical datum  
- Multihash checksums  
- PROV-O links  

---

## 🧾 Training Metadata Template (Summary)

The training metadata template MUST include:

- Dataset list (STAC-linked)  
- Preprocessing steps  
- Input schema version  
- Hyperparameter dictionary  
- Seed + reproducibility keys  
- Training runtime telemetry  
- CARE notes  

---

## 📊 Evaluation Template (Summary)

Evaluation bundles MUST include:

- Accuracy / RMSE / MAE / AUROC / F1 (domain dependent)  
- Calibration curves  
- Fairness metrics  
- Drift detection snapshots  
- Golden-record comparisons  

---

## 🔍 Explainability Template (Summary)

XAI JSON-LD template covers:

- Local explanations  
- Global drivers  
- Saliency / CAM maps  
- CARE-masked output fields  
- Provenance relationships  

Used by:

- Story Node v3  
- Focus Mode v3  
- Audit dashboards  
- MLOps drift detection  

---

## 📡 STAC Integration Templates

STAC templates provide:

- Full STAC Item JSON for model outputs  
- Optional asset templates (e.g., GeoParquet, COG, sidecar JSON-LD)  
- CRS, bounding boxes (if spatial)  
- Provenance via `prov:*`  

These ensure that **model outputs integrate seamlessly** into KFM’s spatial-temporal framework.

---

## 🔐 FAIR+CARE Enforcement

Templates enforce:

- No speculative content  
- No inference of tribal identity  
- H3 generalization for sensitive geospatial outputs  
- CARE scope included in every Model Card  
- Full provenance for every dataset used  

Failures in CARE tests → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                         |
|----------|------------|---------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full v11.2.2 uplift; added governance templates & STAC schema |
| v11.0.0  | 2025-11-15 | Initial Model Card template suite                             |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Templates](../README.md) · [📘 AI Models Index](../../models/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

