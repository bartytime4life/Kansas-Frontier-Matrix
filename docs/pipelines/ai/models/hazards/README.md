---
title: "⚡ KFM v11.2.2 — Hazard & Severe Weather AI Models (Wildfire · Tornado · Flood · Drought · Risk Forecasting)"
path: "docs/pipelines/ai/models/hazards/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Family"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-models-hazards-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-models-hazards-v11.2.2.json"
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
sensitivity: "Hazard-Model"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-forecasting"
  - "wildfire-risk"
  - "severe-weather"
  - "flood-drought"
  - "risk-models"
  - "xai"
  - "story-node"
  - "focus-mode"

scope:
  domain: "ai-models-hazards"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "hazard-ai"
    - "xai"
    - "stac-hazard-outputs"
    - "focus-mode-integration"

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

# ⚡ **KFM v11.2.2 — Hazard & Severe Weather AI Model Family**  
`docs/pipelines/ai/models/hazards/README.md`

**Purpose:**  
Define and govern all **hazard-related AI models** in KFM, including wildfire, tornado, hail, wind, flood, drought, heat-wave, and severe-weather prediction models.  
These models power **risk maps**, **hazard STAC Items**, **Story Node v3 hazard narratives**, and **Focus Mode v3 environmental reasoning**.

</div>

---

## 📘 Overview

The **Hazard AI Model Family** includes models that estimate or forecast:

- **Wildfire probability & spread**  
- **Tornado / hail / wind severity**  
- **Flood risk (DEM + hydrology + rain)**  
- **Flash flood nowcasting**  
- **Drought severity & soil-moisture anomaly detection**  
- **Heat-wave & extreme temperature events**  
- **Multi-hazard clustering / compound risk**  

These models must be:

- Deterministic & reproducible  
- FAIR+CARE-governed  
- Provenance-rich (STAC + PROV-O + telemetry)  
- Explainable (XAI mandatory)  
- Versioned & lineage-safe  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/hazards/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 model-card.jsonld                          # Model Card v11.2.2
    ├── 📄 training-metadata.json                     # Hyperparams, datasets, seeds
    ├── 📄 evaluation-report.md                       # Metrics + regression results
    ├── 📄 explainability.json                        # SHAP / IG / CAMs / attribution
    │
    ├── 📁 examples/                                  # Example hazard maps, XAI outputs
    │   ├── 📄 wildfire-sample.png
    │   ├── 📄 tornado-risk-map.png
    │   ├── 📄 hazard-saliency.png
    │   └── 📄 drivers.json
    │
    ├── 📁 stac/                                      # STAC hazard templates
    │   ├── 📄 hazard-item.json                       # STAC Item (hazard forecast/risk output)
    │   └── 📄 assets-template.json                   # GeoParquet/COG metadata templates
    │
    └── 📁 mlops/                                     # Deployment, drift, monitoring
        ├── 📄 inference-config.yaml
        ├── 📄 threshold-policy.md
        └── 📄 drift-monitoring.md

---

## ⚡ Hazard Model Categories

### 1. 🔥 Wildfire Models
- Spread probability  
- Fuel + terrain integration  
- Smoke + meteorology fusion  
- CAMs/saliency for landscape drivers  

### 2. 🌪️ Severe Weather Models
- Tornado intensity & path likelihood  
- Hail/wind severity  
- Supercell detection  
- Radar + HRRR fusion inputs  

### 3. 💧 Flood / Flash Flood Models
- DEM hydrology fusion  
- Rainfall-runoff ML models  
- Compound risk (rain × soil moisture × terrain)  
- STAC raster output (risk grids)  

### 4. 🌡️ Heat & Drought Models
- Heat index prediction  
- Drought anomaly (soil + climate)  
- Long-term risk assessment  

### 5. 🧭 Multi-Hazard Fusion
- Combine wildfire + wind + drought  
- Flood + soil + climate + land use  
- Story Node-level explanations & risk narratives  

---

## 📡 STAC Integration (KFM-STAC v11)

Hazard models MUST publish their outputs as STAC Items with:

- `kfm:hazard:model_name`  
- `kfm:hazard:model_version`  
- `kfm:hazard:method`  
- `kfm:hazard:severity` or classification  
- `kfm:explainability:*`  
- `kfm:input_items` (array of upstream STAC Item IDs)  
- CRS + vertical datum  
- Bounding geometry  
- Asset checksums (`checksum:multihash`)  
- PROV-O lineage: `prov:used`, `prov:wasGeneratedBy`  

Outputs include:

- COG rasters  
- GeoParquet grids  
- Localized risk polygons  
- Combined hazard surfaces  

---

## 🧠 Explainability Requirements (XAI)

All hazard models MUST provide:

- SHAP global attribution vectors  
- Local attributions for each scored region  
- Integrated Gradients (for deep geospatial models)  
- Saliency maps for DEM- or remote-sensing-based ML  
- JSON-LD explainability bundles  

HAZARD-SPECIFIC RULES:

- Drivers MUST be interpretable (slope, fuel, dryness, HRRR variables, etc.)  
- Sensitive/Indigenous areas must be generalized (H3 masking)  
- Multi-hazard fusion MUST specify weights/importance per input domain  

---

## 🔐 FAIR+CARE Requirements

Hazard models MUST:

- Generalize or mask any sensitive archaeological or Indigenous areas  
- Avoid speculative correlations or unsupported causal claims  
- Document ALL training datasets  
- Include CARE scope & usage restrictions in Model Cards  
- Provide full licensing and provenance for upstream datasets  
- Provide governance policy IDs for restricted content  

---

## 📊 Evaluation Requirements

Evaluation bundles MUST include:

- Skill scores by hazard type  
- AUROC / Brier / F1 / CRPS / RMSE (depending on model class)  
- Golden-record samples (regression tests)  
- XAI drift metrics  
- Seasonal + geographic stratified evaluation  
- Narrative-validation tests (for Story Node integration)  

---

## 🧪 Testing Requirements

Hazard models must pass:

- Deterministic seed-locked reproducibility  
- STAC schema validation  
- CARE compliance checks  
- Explainability schema tests  
- Evaluation regression tests  
- Input dataset version checks  
- Deployment MLOps tests (drift, threshold policy, fallback logic)  

All failures → **PR blocked**.

---

## 🧭 Story Node & Focus Mode Integration

Hazard models feed directly into:

### **Story Node v3**
- Hazard impacts  
- Confidence intervals  
- Explanatory drivers  
- Spatially masked narratives (H3)  
- Historical linkage (hydrology × climate × soil)

### **Focus Mode v3**
- Multi-hop hazard reasoning  
- Layered evidence summaries  
- Provenance-backed risk explanations  
- SAFETY: Never overstate hazard; only grounded outputs allowed  

---

## 🕰 Version History

| Version  | Date       | Notes                                                     |
|----------|------------|-----------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full uplift; XAI, STAC, MLOps drift monitoring; emoji tree |
| v11.0.0  | 2025-11-22 | Initial hazard model family specification                 |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Models Index](../README.md) · [⚙️ Inference Layer](../../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

