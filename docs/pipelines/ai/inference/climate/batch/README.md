---
title: "🌡️🤖⏱️ KFM v11.2.2 — Climate AI Batch Inference Pipelines (Deterministic · STAC-XAI · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/batch/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Pipeline Subcomponent (Batch Climate Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Inference-Batch"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "batch-climate-inference"
  - "scheduled-climate-prediction"
  - "downscaling-batch"
  - "bias-correction-batch"
  - "hazard-linked-climate-batch"
  - "xai-ready-inference"
  - "stac-xai"
  - "prov-xai"
  - "focus-mode-climate"
  - "story-node-climate"

scope:
  domain: "pipelines/ai/inference/climate/batch"
  applies_to:
    - "daily-batch-inference"
    - "weekly-inference"
    - "downscaling-jobs"
    - "bias-correction-jobs"
    - "climate-driver-generation"
    - "hazard-climate-driver-pipelines"
    - "xai-export"
    - "otel-lineage"
    - "faircare-governance"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️🤖⏱️ **Climate AI Batch Inference Pipelines**  
`docs/pipelines/ai/inference/climate/batch/README.md`

**Purpose:**  
Define the **scheduled/batch inference layer** for KFM climate AI pipelines, supporting deterministic nightly/weekly inference of downscaled climate fields, anomaly scores, bias-corrected datasets, and hazard-linked climate drivers — all exported with **STAC-XAI**, **JSON-LD explainability**, and **PROV-O** lineage.

</div>

---

## 📘 Overview

The **Climate Batch Inference** subsystem executes scheduled workflows that generate:

- High-resolution downscaled climate fields  
- Bias-corrected climate time series  
- Seasonal/long-range anomaly indicators  
- Derived hazard-ready climate drivers (e.g., CAPE/SRH/lapse-rate composites)  
- STAC-registered datasets with full lineage  
- XAI JSON-LD explainability bundles (SHAP/IG/CAM/spatial attribution)  

Batch pipelines run via:

- Airflow 3.x  
- Prefect durable flows  
- LangGraph DAGs  
- lakeFS versioned branches  

All outputs are deterministic, FAIR+CARE aligned, sovereignty-compliant, and Story Node + Focus Mode ready.

---

## ⏱️ Batch Pipeline Purposes

### 1. 🌡️ Nightly Downscaling  
Generates high-resolution gridded climate surfaces using ML downscalers.

### 2. 🧭 Daily Climate Driver Updates  
Produces environmental variables that link into hazard pipelines:

- CAPE, CIN, SRH  
- Lapse rates  
- Low-level jet metrics  
- Moisture transport indices  

### 3. 📉 Bias Correction Cycles  
Scheduled correction against observation sources (ASOS, CoCoRaHS, reanalysis).

### 4. 🔮 Weekly/Monthly Climate Outlooks  
Transformer/ensemble seasonal forecasting.

### 5. 🌍 Multi-Model Fusion  
Combines ERA5, Daymet, NLDAS, HRRR, CMIP6 analog features.

---

## 🏗️ Architecture Flow (Batch Climate Inference)

```mermaid
flowchart TD
    A[Fetch STAC Inputs] --> B[Load ML Climate Model]
    B --> C[Deterministic Inference Run (Seed Locked)]
    C --> D[Bias Correction Module]
    D --> E[Generate Climate Drivers]
    E --> F[Export GeoTIFF / NetCDF / Parquet]
    F --> G[Generate JSON-LD XAI Bundles]
    G --> H[Emit STAC Items + PROV-O Lineage]
    H --> I[Telemetry + CARE / Sovereignty Checks]
```

---

## 🧂 Default Batch Cadence (v11.2.2)

| Pipeline | Interval | Notes |
|----------|----------|-------|
| Downscaling | Daily at 03:00 UTC | Deterministic seed-lock |
| Bias Correction | Daily at 04:00 UTC | Requires observation sync |
| Climate Driver Generation | Daily at 05:00 UTC | Hazard pipelines depend on this |
| Anomaly Detection | Weekly | Computes seasonality offsets |
| Long-Range Forecast Fusion | Monthly | Transformer-based |

---

## 📦 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/batch/
    ├── 📄 README.md                              # This file
    │
    ├── 🧠 batch_inference_flow.py                 # Airflow/Prefect/LangGraph entrypoint
    ├── 📄 batch-config.yaml                       # Thresholds, seeds, routing
    ├── 📁 tasks/                                  # Modular pipeline tasks
    │   ├── 📄 load_inputs.py
    │   ├── 📄 run_model.py
    │   ├── 📄 postprocess.py
    │   └── 📄 export_stac.py
    │
    ├── 📁 stac/                                   # Auto-generated STAC Items
    │   └── 📄 collection.json
    │
    └── 📁 jsonld/                                 # Semantic/XAI outputs
        ├── 📄 xai-climate-local.jsonld
        ├── 📄 xai-climate-global.jsonld
        └── 📄 climate-driver-taxonomy.jsonld

---

## 📡 STAC-XAI & Metadata Rules

Batch inference outputs MUST include:

- `kfm:explainability:method` (shap|integrated-gradients|cams|spatial)  
- `kfm:explainability:{local|global}`  
- CRS + vertical datum  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- `kfm:domain="climate"`  
- CARE + sovereignty metadata  

STAC Items must reference JSON-LD explainability bundles.

---

## 🧾 PROV-O Requirements

Every batch run MUST produce lineage metadata:

- `prov:wasGeneratedBy` (run id / pipeline hash)  
- `prov:used` (STAC climate inputs + model version)  
- `prov:generatedAtTime`  
- `prov:Agent` (pipeline+model identity)  

Optional: multimodal lineage (e.g., “derived from SHAP + IG + CAM fusion”).

---

## 🔐 FAIR+CARE Requirements

Climate inference MUST:

- Respect sovereignty protocols and Data Contract v3  
- Avoid culturally sensitive or tribal interpretations  
- Apply H3 masking for sensitive spatial outputs  
- Ensure access constraints follow governance directives  
- Produce narrative-safe climate descriptors  

---

## 🧪 CI & Validation Requirements

CI enforcement includes:

- Deterministic output verification (seed-locked)  
- JSON-LD schema validation  
- STAC-XAI compliance checks  
- CARE/scope and sovereignty checks  
- CRS/vertical axis validation  
- Drift detection tests  
- Bias correction accuracy thresholds  
- PROV-O lineage completeness  

Any failure → ❌ merge blocked.

---

## 🕰 Version History

| Version | Date       | Notes                                                               |
|---------|------------|---------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial batch climate inference specification under KFM v11.2.2     |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Inference](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

