---
title: "💧 KFM v11.2.2 — Hydrology AI Models (Streamflow · Flood · Soil Moisture · Reservoir · Terrain-Hydro Fusion)"
path: "docs/pipelines/ai/models/hydrology/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Family"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-models-hydrology-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-models-hydrology-v11.2.2.json"
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
sensitivity: "Hydrology-Model"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hydrology-ml"
  - "streamflow"
  - "flood-risk"
  - "soil-moisture"
  - "reservoir-models"
  - "terrain-hydro-fusion"
  - "xai"
  - "story-node"
  - "focus-mode"

scope:
  domain: "ai-models-hydrology"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "hydro-ai"
    - "xai"
    - "stac-hydro-outputs"
    - "focus-mode-integration"
    - "provenance"
    - "drift-monitoring"

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

# 💧 **KFM v11.2.2 — Hydrology AI Model Family**  
`docs/pipelines/ai/models/hydrology/README.md`

**Purpose:**  
Define and govern all **Hydrology AI models** used in KFM — including streamflow prediction, reservoir level forecasting, flood-risk estimation, soil-moisture modeling, and hybrid terrain–hydrology fusion.  
All models must use **Model Card v11.2.2**, **STAC v11**, **FAIR+CARE**, and fully deterministic, reproducible ML workflows.

</div>

---

## 📘 Overview

Hydrology AI models in KFM produce:

- River/streamflow forecasts  
- Reservoir elevation predictions  
- Flash-flood risk indicators  
- Soil-moisture inference (DEM × soils × climate)  
- DEM + terrain + hydrology composite indicators  
- Hydrologic anomaly detection  
- Terrain-conditioned hydrological behavior  

Hydrology models feed:

- Hydrology STAC layers  
- Focus Mode v3 environmental reasoning  
- Story Node v3 hydrology narratives  
- Hazard + climate + terrain fusion pipelines  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/hydrology/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 model-card.jsonld                          # Model Card v11.2.2
    ├── 📄 training-metadata.json                     # Hyperparams, datasets, seeds
    ├── 📄 evaluation-report.md                       # Metrics + golden-record tests
    ├── 📄 explainability.json                        # SHAP / IG / CAMs / attribution
    │
    ├── 📁 examples/                                  # Example hydrology outputs
    │   ├── 📄 streamflow-forecast.png
    │   ├── 📄 soil-moisture-anomaly.json
    │   ├── 📄 flood-risk-map.cog.tif
    │   └── 📄 attribution-drivers.json
    │
    ├── 📁 stac/                                      # STAC templates for hydro outputs
    │   ├── 📄 hydrology-item.json                    # STAC Item template (hydrology output)
    │   └── 📄 assets-template.json                   # Asset metadata (GeoParquet/COG)
    │
    └── 📁 mlops/                                     # Deployment, drift, monitoring
        ├── 📄 inference-config.yaml
        ├── 📄 drift-monitoring.md
        └── 📄 retraining-policy.md

---

## 💧 Hydrology Model Categories

### 1. 🌊 Streamflow Prediction Models
- Predict river flow levels  
- Combine climate, terrain, and upstream hydrology inputs  
- Provide interval forecasts + uncertainty  

### 2. 🚰 Reservoir Modeling
- Predict reservoir elevation  
- Integrate inflow/outflow + seasonal climate drivers  
- Provide confidence ranges  

### 3. 🌧️ Flash-Flood & Flood Risk Models
- Use DEM + rainfall-runoff ML models  
- Provide pixel-level flood scores  
- SALIENCY REQUIRED (terrain drivers)  
- Publish outputs as COG rasters + STAC Items  

### 4. 🌱 Soil-Moisture Models
- Combine DEM, soils, climate, and radar inputs  
- Provide soil-moisture anomaly predictions  
- MUST follow Data Contract v3 + CRS/Vertical Axis v11  

### 5. 🧬 Terrain–Hydrology Fusion Models
- Combine slope, curvature, flow accumulation, and DEM derivatives  
- Predict hydrologically conditioned behavior  
- Provide risk maps for hydrologic shifts  

### 6. 🧭 Focus Mode v3 Hydrology Reasoners
- Provide hydrology context windows  
- Combine STAC Items + graph links + temporal windows  
- Must be deterministic and CARE-compliant  

---

## 📡 STAC Integration (KFM-STAC v11)

Hydrology models MUST publish geospatial outputs as STAC Items:

Required fields:

- `kfm:hydro:model_name`  
- `kfm:hydro:model_version`  
- `kfm:hydro:method`  
- `kfm:hydro:severity` or classification  
- `kfm:input_items` (upstream STAC IDs)  
- CRS + vertical datum  
- Bounding geometry  
- Multihash checksums  
- Provenance: `prov:used`, `prov:wasGeneratedBy`, `prov:generatedAtTime`  

Outputs may include:

- COG risk rasters  
- GeoParquet tile surfaces  
- Local vectors (catchments, hotspots)  
- Story Node v3 hydrology narratives  

---

## 🧠 Explainability Requirements (XAI)

All hydrology models must provide:

- SHAP global attribution  
- Local attribution per region/segment  
- DEM driver maps (CAMs, saliency)  
- Integrated Gradients for deep terrain models  
- JSON-LD explainability bundles (`kfm:explainability:*`)  

Hydrology explanations MUST:

- Be interpretable (slope, rainfall, DEM drivers)  
- Respect CARE masking for sensitive landscape regions  
- Provide provenance for all driver variables  

---

## 🔐 FAIR+CARE Requirements

Hydrology models MUST:

- Document training datasets + licensing  
- Mask sensitive areas (H3 generalization)  
- Avoid speculative or causal claims  
- Provide CARE scope in Model Cards  
- Include governance policy IDs  

Any violation → **pipeline block**.

---

## 🧪 Testing Requirements

Models must pass:

- Seed-locked reproducibility  
- Golden-record comparison  
- Hydrology-specific drift detection  
- Explainability schema validation  
- STAC template validation  
- Vertical axis & CRS checks  
- CARE-compliance audits  

Failing any check → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                       |
|----------|------------|-------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade to v11.2.2; new templates, telemetry, emoji tree |
| v11.0.0  | 2025-11-22 | Initial hydrology model family specification                |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Models Index](../README.md) · [⚙️ Inference Layer](../../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

