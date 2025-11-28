---
title: "🌡️🔍 KFM v11.2.2 — Climate Explainability Pipelines (SHAP · IG · CAMs · Attribution Maps)"
path: "docs/pipelines/ai/explainability/climate/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Pipeline Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-explainability"
  - "xai"
  - "shap"
  - "integrated-gradients"
  - "cams"
  - "saliency"
  - "narrative-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "ai-explainability-climate"
  applies_to:
    - "xai-global"
    - "xai-local"
    - "xai-visualizations"
    - "shap"
    - "cams"
    - "saliency"
    - "prov-xai"
    - "stac-xai"
    - "story-node-xai"
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

# 🌡️🔍 **KFM v11.2.2 — Climate Explainability Pipelines**  
`docs/pipelines/ai/explainability/climate/README.md`

**Purpose:**  
Define the **explainability (XAI) layer** for all **Climate AI models**, producing governed and interpretable outputs using SHAP, Integrated Gradients, CAMs/saliency maps, and JSON-LD-based explainability bundles that feed:  

- STAC v11 Items  
- Story Node v3 narratives  
- Focus Mode v3 evidence overlays  
- Governance & audit workflows  

</div>

---

## 📘 Overview

Climate explainability pipelines generate structured, FAIR+CARE-aligned explanations for:

- Downscaling models  
- Bias-correction models  
- Seasonal/annual forecast models  
- Anomaly-detection models  
- Climate–hydrology–terrain fusion models  

Explainability outputs generated here must be:

- Deterministic  
- Reproducible  
- JSON-LD-structured  
- STAC-compliant  
- Safe for CARE-restricted datasets  
- Usable by Story Node v3 & Focus Mode v3  

This directory defines the spec for generating:

- **SHAP global importance vectors**  
- **SHAP local explanations**  
- **Integrated Gradients (IG) maps**  
- **CAM/saliency overlays**  
- **Spatial attribution rasters**  
- **Feature driver JSON-LD bundles**  
- **XAI → narrative mappings**  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/
    ├── 📄 README.md                               # This file
    │
    ├── 📁 shap/                                   # SHAP global & local attribution
    │   ├── 📄 global.json
    │   ├── 📄 local.json
    │   └── 📄 driver-summary.md
    │
    ├── 📁 integrated-gradients/                   # IG gradient attribution
    │   ├── 📄 ig-global.json
    │   └── 📄 ig-samples.json
    │
    ├── 📁 cams/                                   # CAMs / saliency overlays (imagery)
    │   ├── 📄 cam-maps.md
    │   └── 📄 saliency-driver.json
    │
    ├── 📁 spatial-attribution/                    # Raster/tiling-based spatial XAI
    │   ├── 📄 attribution.tif
    │   └── 📄 spatial-drivers.json
    │
    └── 📁 jsonld/                                 # XAI JSON-LD bundles
        ├── 📄 xai-global.jsonld
        ├── 📄 xai-local.jsonld
        └── 📄 xai-driver-summary.jsonld

---

## 🔍 Explainability Components

### 1. 🟥 SHAP Global Attribution
Required for:

- Downscaling  
- Forecasting  
- Bias-correction  
- Anomaly models  

Outputs:

- Feature-level global importance  
- Ranked climate driver vectors  
- JSON-LD entries suitable for STAC + Story Nodes  

### 2. 🟦 SHAP Local Attribution
Used for:

- Instance-level predictions  
- Probabilistic forecasts  
- Anomaly explanations  

Outputs include:

- Local contribution vectors  
- Contextual explanations  
- CARE-masked drivers where appropriate  

---

### 3. 🟩 Integrated Gradients (IG)

Used primarily for:

- Deep learning models  
- Terrain-aware climate fusion models  
- Spatially complex features  

Must generate:

- Gradient-based attribution  
- Structured IG JSON  
- Domain-interpretable driver descriptions  

---

### 4. 🟨 CAMs / Saliency Maps

Used in:

- CNN-based downscaling  
- Remote-sensing climate predictors  

Outputs:

- Pixel-importance / driver-heatmaps  
- CARE masking for sensitive geospatial zones  
- Optional conversion to GeoTIFF or COG  

---

### 5. 🟪 Spatial Attribution Maps

For gridded model outputs:

- Slope, aspect, surface roughness  
- Climate anomaly predictors  
- Downscaled bias-corrected layers  

Outputs include:

- Raster-based attribution TIFFs  
- GeoParquet driver tiles  
- Multihash checksums for STAC integration  

---

### 6. 🧭 XAI → Story Node v3 & Focus Mode v3 Integration

All climate explainability must produce:

- Narrative-ready **driver summaries**  
- Spatial attribution clues  
- JSON-LD provenance links  

Focus Mode v3 uses these for:

- Climate-context windows  
- Trend explanations  
- Driver-based map overlays  

Story Node v3 uses these for:

- Evidence blocks  
- Time-bounded context  
- Model-version provenance  

---

## 📡 STAC Integration (KFM-STAC v11)

Climate XAI outputs must generate valid STAC assets:

Required fields:

- `kfm:explainability:method`  
- `kfm:explainability:global`  
- `kfm:explainability:local`  
- `kfm:explainability:spatial`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS + bounding geometry  
- Asset checksums (multihash)  

---

## 🧾 PROV-O Lineage Requirements

Each explainability product must include:

- `prov:wasGeneratedBy` (model + run)  
- `prov:used` (input datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (pipeline + model identity)  

Outputs are consumed by:

- AI lineage dashboards  
- Focus Mode v3  
- Story Node v3  

---

## 🔐 FAIR+CARE Requirements

Climate XAI outputs must:

- Mask culturally sensitive regions (H3 generalization)  
- Remove drivers tied to restricted community-level features  
- Include CARE-scope metadata  
- Provide dataset license transparency  
- Never imply tribal identity or culturally sensitive interpretations  

---

## 🧪 Testing Requirements

All climate explainability pipelines must pass:

- Deterministic output comparison  
- JSON-LD schema validation  
- STAC validation (items + assets)  
- Raster CRS/vertical-axis checks  
- CARE governance tests  
- Drift detection baselines for SHAP/IG  

PRs failing any requirement → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Explainability Layer; aligned with XAI templates |
---

<div align="center">

### 🔗 Footer  
[⬅ Back to Explainability Index](../README.md) · [🧠 AI Pipeline Layer](../../README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

