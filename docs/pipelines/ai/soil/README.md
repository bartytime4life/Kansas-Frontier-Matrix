---
title: "🧠 KFM v11 — Soil AI Pipeline Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/soil/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · AI/ML Working Group · Soil Systems · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soil-ai-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-soil-suite-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A2-I1-R1"
care_label: "CARE · Soil / Ecology / Indigenous Landscape Sensitivity"
classification: "Public (Governed)"
sensitivity: "Low/Moderate (Spatially Masked Where Required)"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🧠 **KFM v11 — Soil AI Pipeline Suite**  
`docs/pipelines/ai/soil/`

**Purpose**  
Provide the governed root for all **soil-driven AI/ML pipelines**, including suitability modeling,  
terrain-informed predictions, hydrologic surrogate models, ecological affordance models,  
and archaeological landscape inference — all aligned with FAIR+CARE, ethical governance,  
and v11 reproducibility & provenance standards.

</div>

---

## 📘 1. Overview

Soil is a foundational environmental variable used throughout KFM:

- Archaeology (e.g., site affordances, cultural-landscape context)  
- Hydrology (e.g., infiltration, wetness, hydric layers)  
- Ecology (e.g., vegetation modeling, habitat suitability)  
- Agriculture (e.g., yield predictors, soil-quality classifiers)  
- Climate (downscaling & land-surface parameters)

Therefore, the **Soil AI Pipeline Suite** ensures:

- **Deterministic preprocessing** (harmonization, terrain alignment, masking)  
- **Reproducible model training/evaluation**  
- **STAC-encoded model metadata**  
- **OpenLineage provenance** (dataset + model + slice + run)  
- **Energy/carbon telemetry** for sustainable AI  
- **CARE-aware handling** of soils intersecting Indigenous or sensitive landscapes  
- **Continuous auditing** of drift using GE + SHAP (v11 audit suite)

---

## 🧱 2. Core Components of the Soil AI Suite

### 2.1 Soil Feature Engineering (FE)
Pipelines standardize:

- Soil taxonomy fields  
- Surface/terrain-derived factors (slope, aspect, TPI, wetness index)  
- Hydric indicators  
- H3 partitioning for model locality  
- Spatial masking & Indigenous-sensitive fuzzing where needed  
- Feature-scale harmonization for multi-model comparability

### 2.2 Model Training Pipelines
Soil AI pipelines include:

- Suitability models (e.g., agriculture, archaeology, ecology)  
- Regression models (soil moisture proxies, erosion predictors)  
- Classification tasks (soil group prediction, hydric classification)  
- Terrain-enhanced, soil-informed geospatial models

All are:

- **Deterministic**  
- **Version-pinned**  
- **CI-tested**  
- **Provenance-logged**

### 2.3 Model Evaluation + Promotion
Model promotion requires:

- Performance stability (metrics vs baselines)  
- Interpretability stability (SHAP drift gates)  
- GE validation success for input slices  
- Full STAC/PROV-O metadata bundles  
- CARE compliance (sensitive area tests)

### 2.4 Soil Model Drift Audits (GE + SHAP)
Performed via:

- `ai/soil/audits/ge-shap/`  
- Data drift  
- Performance drift  
- Interpretability drift  
- Sustainability telemetry  
- STAC audit item creation  
- Story Node integration  

This mechanism prevents untrustworthy soil model promotions.

---

## 🗂️ 3. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/soil/
├── 📄 README.md                        # This file
│
├── 🧪 audits/                           # GE + SHAP drift auditing layer
│   ├── 📄 README.md
│   ├── 🧪 ge-shap/
│   ├── 🧾 metrics/
│   ├── 🔍 explain/
│   ├── 🧬 lineage/
│   └── 📦 stac/
│
├── 🧠 models/                           # Model definitions (training, tuning, evaluation)
│   ├── 📄 README.md
│   ├── 🔨 training/
│   ├── 📊 evaluation/
│   ├── 📦 stac/
│   └── 🧪 tests/
│
├── 🔁 fe/                               # Soil feature-engineering pipelines
│   ├── 📄 README.md
│   ├── 🗂️ harmonization/
│   ├── 🏔️ terrain-derivatives/
│   ├── 💧 hydric/
│   ├── 🧭 h3-generalization/
│   ├── 🔧 transforms/
│   ├── 🌐 stac/
│   └── 🧪 tests/
│
└── 🔗 utils/                            # Shared utilities (schemas, helpers, validators)
    ├── 📄 README.md
    ├── 🧩 schema/
    ├── 📐 validators/
    └── 📦 stac/
~~~

---

## 🌐 4. Metadata & Provenance Requirements

For every soil AI model:

### Mandatory Artifacts
- **STAC Item**  
- **STAC Collection**  
- **DCAT dataset metadata**
- **Model card (v11)**  
- **OpenLineage job/run + slice references**  
- **Dataset version hashes**  
- **Training + evaluation slice IDs**

### Required Provenance Elements
- Input dataset lineage  
- Feature engineering lineage  
- Model training lineage  
- Validation slice provenance  
- Audit bundle (GE + SHAP)

---

## 🧮 5. Sustainability & Telemetry

Each soil AI pipeline run MUST emit:

- `energy_wh`  
- `carbon_gco2e`  
- `records_processed`  
- `fe_time_sec`, `train_time_sec`, `eval_time_sec`  
- Drift metrics (when applicable)  
- GE/SHAP anomaly counts  

Telemetry fed into governance dashboards for:

- AI carbon budgeting  
- Model lifecycle costing  
- Sustainable model management

---

## 🧩 6. Story Node Integration (Focus Mode v3)

Soil AI pipelines produce Story Nodes for:

- Model version evolution  
- Drift events  
- Feature engineering changes  
- Upstream soil dataset refresh impacts  
- Interpretability shifts  

These nodes allow the KFM UI to show **temporal narratives** of how soil models evolve.

---

## 🏁 7. Version History

| Version | Date       | Summary                                                                                       |
|--------:|------------|------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Root Soil AI suite created; aligned with GE+SHAP auditor + Soil Pipeline Suite + emoji index. |
| v11.2.2 | 2025-11-29 | Initial soil AI definitions prior to suite consolidation.                                      |

---

<div align="center">

🧠 **Kansas Frontier Matrix — Soil AI Pipeline Suite (v11.2.3)**  
FAIR+CARE · Sustainable AI · Provenance-Driven Modeling  

[📘 Docs Root](../../../..) · [🤖 AI Pipelines](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

