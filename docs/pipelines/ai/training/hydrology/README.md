---
title: "💧 KFM v11.2.2 — Hydrology Model Training Pipelines (Streamflow · Flood · Soil Moisture · Reservoir · Fusion Models)"
path: "docs/pipelines/ai/training/hydrology/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Training Pipeline"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-training-hydrology-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-training-hydrology-v11.2.2.json"
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
sensitivity: "Hydrology-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hydrology-ai-training"
  - "streamflow"
  - "soil-moisture"
  - "reservoir"
  - "flood-risk"
  - "terrain-hydro-fusion"
  - "provenance"
  - "faircare-governance"
  - "xai-training"
  - "energy-carbon"

scope:
  domain: "ai-training-hydrology"
  applies_to:
    - "training-configs"
    - "training-dags"
    - "evaluation-bundles"
    - "model-cards"
    - "hydro-xai"
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

# 💧 **KFM v11.2.2 — Hydrology Training Pipelines**  
`docs/pipelines/ai/training/hydrology/README.md`

**Purpose:**  
Define the deterministic, reproducible, STAC-driven training pipelines for all **hydrology models**: streamflow, soil moisture, reservoir elevation, flood/flash flood risk, and terrain–hydrology fusion models.  
Integrates **PROV-O**, **OpenLineage**, **FAIR+CARE**, **XAI**, and **Energy/Carbon v2 telemetry**.

</div>

---

## 📘 Overview

Hydrology training pipelines generate:

- Streamflow models (deterministic + probabilistic)
- Reservoir level predictors
- Flood risk ML models (rain × runoff × DEM)
- Soil moisture anomaly detectors
- Terrain–hydrology hybrid feature models
- Hydrological anomaly classification
- Train-time explainability bundles (SHAP / IG / CAMs)
- Full Model Cards (v11.2.2)
- Evaluation bundles (golden-record tests)
- PROV-O lineage + OpenLineage job facets
- Energy/Carbon usage reports

Training consumes canonical KFM inputs:

- STAC collections: **3DEP DEM**, **Hydrology Flowlines**, **Soils**, **Climate**, **Land Cover**
- All datasets must be version-locked with checksums.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/hydrology/
    ├── 📄 README.md                              # This file
    │
    ├── 📄 training-config.yaml                   # Hyperparams, STAC sources, seeds
    ├── 📄 dag.md                                 # DAG overview (Airflow / LangGraph)
    ├── 📄 evaluation-metrics.md                  # Metrics + regression tests
    │
    ├── 📁 datasets/                              # STAC-linked dataset manifests
    │   ├── 📄 stac-inputs.json
    │   └── 📄 dataset-license-notes.md
    │
    ├── 📁 explainability/                        # Train-time XAI outputs (examples)
    │   ├── 📄 shap-global.json
    │   ├── 📄 integrated-gradients.json
    │   └── 📄 cam-saliency.png
    │
    ├── 📁 evaluation/                            # Evaluation bundles from training
    │   ├── 📄 metrics.json
    │   ├── 📄 skill-scores.md
    │   └── 📄 regression-tests.json
    │
    └── 📁 provenance/                            # Training provenance bundles
        ├── 📄 prov-trace.jsonld
        └── 📄 lineage-facets.json

---

## 💧 Hydrology Training Categories

### 1. 🌊 Streamflow Training
- Input: climate forecasts, upstream flow, soils, DEM derivatives  
- Output: flow prediction models  
- Mandatory:
  - SHAP global attribution  
  - Permutation importance  
  - PROV-O training lineage  

### 2. 🚰 Reservoir Elevation Training
- Inputs: inflow/outflow, climate drivers  
- Must record:
  - Confidence intervals  
  - Seasonal calibration  
  - Telemetry footprint  

### 3. 🌧️ Flood / Flash Flood Training  
- Inputs: DEM, rainfall-runoff, soil moisture, slope/curvature  
- Produces: Flood-risk rasters (COG/GeoParquet)  
- XAI: Saliency + IG required for DEM-based models  

### 4. 🌱 Soil Moisture AI Training
- Inputs: soils, DEM, climate, radar  
- Tasks: anomaly detection, seasonal trends  
- XAI: SHAP + feature correlation  

### 5. 🧬 Terrain–Hydrology Fusion Training
- Blend DEM derivatives, flow accumulation, channel depth  
- Required for geomorphology-based hydrology (KFM v11)  
- Must log:
  - Derived features  
  - Explainability bundles  
  - Multi-source provenance  

---

## ⚙️ Training Requirements

### Deterministic Training
Training MUST:

- Lock all seeds  
- Fix hyperparameters  
- Version-pin STAC inputs  
- Embed environment fingerprint  
- Produce stable Model Cards  

### STAC-Linked Data Governance
All input datasets must include:

- `stac_item` IDs  
- dataset license  
- Data Contract v3 validation  
- Geography + vertical axis metadata  

### Explainability (Train-Time)
Training MUST emit:

- SHAP (global + local)  
- Integrated Gradients (deep models)  
- Saliency/CAMs for terrain models  
- JSON-LD XAI bundles  

### Evaluation
Must include:

- RMSE / MAE / NSE / KGE (domain-specific)  
- Golden-record tests  
- Drift testing snapshots  
- Confidence & calibration metrics  

### Provenance
Training MUST output:

- PROV-O JSON-LD bundle  
- OpenLineage facets  
- Model version + training hash  
- STAC training source fingerprints  

### Energy/Carbon Reporting
Training MUST record:

- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  

Required for climate & hydrology models per FAIR+CARE + sustainability charter.

---

## 📡 STAC Publishing (Training Outputs)

Hydrology training MUST produce STAC metadata:

Required fields:
- `kfm:ml:model_name`
- `kfm:ml:model_version`
- `kfm:ml:training_inputs` (STAC Items)
- CRS + vertical metadata
- Asset checksums (`checksum:multihash`)
- Explainability references
- Provenance (`prov:*`)

Outputs include:

- XAI bundles  
- Evaluation bundles  
- Optional generated rasters/vectors  

---

## 🔐 FAIR+CARE Requirements

Hydrology training MUST:

- Mask sacred / culturally sensitive hydrology-adjacent features  
- Apply H3 spatial generalization  
- Avoid speculative ecological or cultural narratives  
- Include CARE scope in Model Cards  
- Document sovereign datasets  

---

## 🧪 Testing Requirements

Training MUST pass:

- Seed-locked reproducibility  
- STAC schema validation  
- Dataset license + Data Contract v3 checks  
- Model Card schema tests  
- Explainability drift tests  
- Regression testing  
- Carbon/Energy telemetry validation  
- CARE compliance tests  

All failures → **pipeline block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                      |
|----------|------------|------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade; governance + telemetry + STAC alignment     |
| v11.0.0  | 2025-11-22 | Initial hydrology training specification                  |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Training Index](../README.md) · [💧 Hydrology Models](../../models/hydrology/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

