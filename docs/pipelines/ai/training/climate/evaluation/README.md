---
title: "🌡🧪 KFM v11 — Climate AI Training Evaluation Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/training/climate/evaluation/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/climate-training-eval-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-training-climate-evaluation-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Evaluation Module"
intent: "climate-training-evaluation"
fair_category: "F1-A1-I2-R2"
care_label: "CARE-Compliant · Climate-Sensitive · Evaluation-Safe"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Climate + hazard / forecast implications)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌡🧪 **Climate AI Training Evaluation Framework (KFM v11)**  
`docs/pipelines/ai/training/climate/evaluation/`

**Purpose**  
Define the **governed v11 evaluation framework** for all KFM climate AI training pipelines:  
PM2.5 + ozone predictions, heat index inference, smoke/visibility, aerosol chemistry,  
fire danger, and climate–surface response models.  

Ensures evaluations are **reproducible, sustainable, FAIR+CARE-compliant, and provenance-rich**,  
with unified metrics, explainability hooks, and telemetry integration.

</div>

---

## 📘 1. Overview

Model evaluation in climate AI requires:

- High-frequency climate input (CAMS, ERA5, HRRR)  
- Hazard & pollutant ground truth (AQS/AirNow, USDA smoke plume, NOAA hazard datasets)  
- Spatial & temporal alignment  
- Explainability & interpretability  
- Sovereignty & sensitivity screening  
- Sustainability evaluation (energy/carbon per evaluation run)

This module defines standardized:

- Metrics  
- Evaluation procedures  
- Dataset slicing  
- FAIR+CARE checks  
- Telemetry and lineage emission  
- Promotion gating rules (Reliability Framework v11)

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/training/climate/evaluation/
├── 📄 README.md
│
├── 📊 metrics/                             # Metric definitions + schemas
│   ├── 📄 classification-metrics.yaml       # Binary/multi-class hazard metrics
│   ├── 📄 regression-metrics.yaml           # PM2.5/ozone regression metrics
│   ├── 📄 spatial-metrics.yaml              # H3/grid spatial scoring rules
│   ├── 📄 temporal-metrics.yaml             # Time-series skill metrics
│   └── 📄 outlier-detection.yaml            # Extreme-event performance rules
│
├── 🧠 evaluators/                          # Evaluation runners + configs
│   ├── 🧩 evaluator.py
│   ├── 🧩 spatial_evaluator.py
│   ├── 🧩 temporal_evaluator.py
│   └── 🧩 hazard_evaluator.py
│
├── 🧪 validation/                          # Ethical + data integrity checks
│   ├── 📄 validate-groundtruth-alignment.md
│   ├── 📄 validate-climate-linkage.md
│   ├── 📄 validate-faircare.md
│   ├── 📄 validate-sustainability.md
│   └── 📄 validate-provenance.md
│
├── 🔗 lineage/                             # PROV-O + OpenLineage templates
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 📡 telemetry/                           # Evaluation telemetry templates
│   ├── 📄 metrics-to-otel.yaml
│   ├── 📄 eval-telemetry.schema.json
│   └── 📄 eval-telemetry.shacl.ttl
│
└── 📁 examples/                            # Example evaluation outputs
    ├── 📁 pm25/
    ├── 📁 ozone/
    ├── 📁 heat-index/
    ├── 📁 smoke/
    └── 📁 fire-danger/
~~~

---

## 🧬 3. Evaluation Standards (v11)

### Required Evaluation Metadata

| Field | Description | Required |
|-------|-------------|----------|
| `model:version` | Model being evaluated | ✔ |
| `kfm:domain` | `"climate"` or `"air"` | ✔ |
| `evaluation_id` | Unique URN for evaluation run | ✔ |
| `datetime` | Evaluation timestamp | ✔ |
| `dataset_slice` | Train/val/test partition metadata | ✔ |
| `groundtruth_source` | AQS/AirNow/ERA5/etc. | ✔ |
| `kfm:sensitivity_flag` | CARE-handling | ✔ |
| `kfm:energy_wh` | Evaluation energy usage | ✔ |
| `kfm:carbon_gco2e` | Carbon cost | ✔ |
| `prov:*` | PROV-O lineage | ✔ |
| `openlineage:*` | recommended | conditional |
| Spatial/H3 fields | if spatial | conditional |

### Required Evaluation Outputs

- Metrics JSON (regression/classification/spatial/temporal)  
- STAC Item for evaluation  
- Model card update hooks  
- Explainability references (SHAP/IG)  
- Telemetry record (energy/carbon/latency)

---

## 📊 4. Metric Categories

### **Regression Metrics**
Used for PM2.5, ozone, temperature, humidity, wind component prediction.

- MAE  
- RMSE  
- MAPE  
- Pearson R  
- Seasonal/diurnal skill metrics  
- Extreme-event RMSE  

### **Classification Metrics**
Used for hazard categories (AQI levels, smoke visibility tiers, heat alerts).

- Accuracy  
- F1 (macro/micro)  
- Balanced Accuracy  
- AUROC  
- Precision/Recall  

### **Spatial Metrics**
Important for grid/H3 outputs.

- H3-cell RMSE  
- Spatial correlation  
- Neighborhood consistency (H3 ring metrics)  
- Spatial bias  

### **Temporal Metrics**
For dynamic climate sequences.

- Autocorrelation skill  
- Lead-time decay curves  
- Sequence RMSE/MAE  
- Event alignment  

### **Extreme-Event Metrics**
For hazard spikes (wildfire smoke, PM2.5 surges, heat waves).

- Tail RMSE  
- Peak detection accuracy  
- High-percentile MAE  

---

## 🧪 5. Validation Requirements

### ✔ Groundtruth Alignment  
- Climate → groundtruth mapping validated  
- Temporal alignment exact  
- Spatial interpolation documented  

### ✔ FAIR+CARE  
- Sensitive-region masking where necessary  
- Responsible risk-exposure handling  
- Ethics block in evaluation artifact  

### ✔ Provenance  
- PROV-O & OpenLineage required  
- Full dataset lineage  

### ✔ Sustainability  
- Energy/carbon < evaluation budget  
- Logged to telemetry  

### ✔ Reliability  
- SLO compliance  
- Error budget remaining  

Fail → rollback or human governance review.

---

## 🌐 6. STAC/DCAT Integration

Each evaluation run MUST publish a STAC Item including:

- Metrics assets  
- Provenance links  
- Explainability references  
- Temporal interval  
- Spatial extent  
- Model version  
- Energy & carbon metadata  

DCAT mapping required for dataset-level reporting.

---

## 🔗 7. Provenance (PROV-O + OpenLineage)

Evaluation runs MUST include:

- `prov:Activity`: evaluation run  
- `prov:used`: model artifact + groundtruth dataset  
- `prov:generated`: evaluation-output metrics  
- `prov:wasAssociatedWith`: CI/compute agent  

OpenLineage run should include:

- Inputs/Outputs  
- Resource usage  
- Event time & duration  

---

## 📡 8. Telemetry (OTel v11)

Evaluation telemetry MUST capture:

- `kfm.eval_energy_wh`  
- `kfm.eval_carbon_gco2e`  
- `kfm.eval_latency_ms`  
- Metrics summary fields  
- Rows/cells processed  
- GPU/CPU/memory footprint  

This telemetry must be linked into:

- STAC items  
- Evaluation JSON-LD  
- Release telemetry bundle  

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Each evaluation run SHOULD generate:

- Summary of model performance  
- Critical variables driving success/failure  
- Extreme-event explanations  
- Narrative: “How reliable is this model iteration?”  
- Sustainability footprint  
- FAIR+CARE compliance story  

These nodes drive climate-reliability storytelling.

---

## 🧭 10. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 climate model evaluation module; full telemetry + CARE + STAC alignment. |

---

<div align="center">

🌡🧪 **Kansas Frontier Matrix — Climate AI Training Evaluation (v11.2.3)**  
Reliable · Transparent · FAIR+CARE · Provenance-Driven  

[📘 Docs Root](../../../../../..) · [🌡 Climate Training Pipelines](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>