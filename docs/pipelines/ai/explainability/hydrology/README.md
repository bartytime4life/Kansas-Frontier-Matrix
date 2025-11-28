---
title: "💧🔍 KFM v11.2.2 — Hydrology Explainability Pipelines (SHAP · IG · CAMs · Spatial Attribution)"
path: "docs/pipelines/ai/explainability/hydrology/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Pipeline Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/hydrology-explainability-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-explainability-hydrology-v11.2.2.json"
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
  - "hydrology-explainability"
  - "xai"
  - "shap"
  - "integrated-gradients"
  - "cams"
  - "saliency"
  - "spatial-attribution"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "ai-explainability-hydrology"
  applies_to:
    - "xai-global"
    - "xai-local"
    - "xai-spatial"
    - "shap"
    - "ig"
    - "cams"
    - "saliency"
    - "prov-xai"
    - "stac-xai"
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

# 💧🔍 **KFM v11.2.2 — Hydrology Explainability Pipelines**  
`docs/pipelines/ai/explainability/hydrology/README.md`

**Purpose:**  
Define the **explainability (XAI) layer** for **Hydrology AI models**, producing deterministic, FAIR+CARE-aligned SHAP, IG, CAM/saliency, and spatial attribution outputs for:

- STAC v11 Items  
- Story Node v3 hydrology narratives  
- Focus Mode v3 hydrology reasoning  
- Governance and audit layers  

</div>

---

## 📘 Overview

Hydrology explainability pipelines generate structured attribution for:

- Streamflow prediction models  
- Reservoir elevation models  
- Flood & flash-flood models  
- Soil-moisture anomaly predictors  
- Terrain–hydrology fusion models  

The outputs generated here are:

- Deterministic & reproducible  
- JSON-LD structured  
- Governed (FAIR+CARE)  
- Provenance-rich (PROV-O)  
- STAC-compatible  
- Usable by Story Node v3 & Focus Mode v3 hydrology context windows  

This directory defines the spec for:

- **Global importance vectors (SHAP)**  
- **Local explanations (SHAP local)**  
- **Integrated Gradients (IG)**  
- **CAM/saliency maps**  
- **Spatial attribution rasters**  
- **Driver explanations for narratives**  
- **JSON-LD explainability bundles**  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hydrology/
    ├── 📄 README.md                                  # This file
    │
    ├── 📁 shap/                                      # SHAP global/local attribution
    │   ├── 📄 global.json
    │   ├── 📄 local.json
    │   └── 📄 hydrology-driver-summary.md
    │
    ├── 📁 integrated-gradients/                      # IG gradient attribution
    │   ├── 📄 ig-global.json
    │   └── 📄 ig-samples.json
    │
    ├── 📁 cams/                                      # CAM / saliency overlays
    │   ├── 📄 cam-maps.md
    │   └── 📄 saliency-driver.json
    │
    ├── 📁 spatial-attribution/                       # Raster/tiling spatial explainability
    │   ├── 📄 attribution.tif
    │   └── 📄 spatial-drivers.json
    │
    └── 📁 jsonld/                                    # JSON-LD explainability bundles
        ├── 📄 xai-global.jsonld
        ├── 📄 xai-local.jsonld
        └── 📄 xai-driver-summary.jsonld

---

## 🔍 Explainability Components

### 1. 🟥 SHAP Global Attribution
Applies to:

- Streamflow  
- Reservoir  
- Terrain-hydrology fusion  
- Drought/soil-moisture  

Outputs:

- Feature importance vectors  
- Ranked hydrological drivers  
- JSON-LD XAI summaries for STAC + Story Nodes  

---

### 2. 🟦 SHAP Local Attribution
Used for:

- Localized flow predictions  
- Per-catchment anomaly detection  
- Event-based hydrology forecasts  

Drivers must:

- Include uncertainty  
- Be masked for CARE-sensitive locations  
- Provide provenance  

---

### 3. 🟩 Integrated Gradients (IG)

Applicable for:

- Deep learning models with DEM/terrain inputs  
- Hybrid climate–hydrology–terrain fusion pipelines  

Outputs:

- Gradient-based attribution  
- Interpretable vertical & topographic drivers  
- JSON-formatted IG bundles  

---

### 4. 🟨 CAMs / Saliency Maps

For:

- CNN-based flood prediction  
- Remote-sensing hydrology models  

Outputs:

- Spatial pixel-importance maps  
- TIFF overlays (H3 masked where needed)  
- CARE-safe abstractions for narratives  

---

### 5. 🟪 Spatial Attribution Maps

For gridded hydrology outputs:

- Flow accumulation  
- Flood probability  
- Soil moisture anomalies  
- Terrain-derived features  

Outputs:

- GeoTIFF attribution rasters  
- GeoParquet attribution tiles  
- Full STAC v11 asset metadata  

---

### 6. 🧭 XAI → Story Node v3 & Focus Mode v3 Integration

Hydrology XAI pipelines must generate:

- Driver summaries for narratives  
- Spatial attribution inputs for Focus Mode v3  
- Time-series explainability  
- PROV-linked evidence chains  

Use cases:

- Hydrology contextual windows  
- Flood event narratives  
- Soil moisture anomaly stories  
- Basin-level reasoning  

---

## 📡 STAC Integration (KFM-STAC v11)

Hydrology XAI outputs MUST embed:

- `kfm:explainability:method`  
- `kfm:explainability:global`  
- `kfm:explainability:local`  
- `kfm:explainability:spatial`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS + bounding box  
- Vertical datum if applicable  
- Asset checksums (multihash)  

---

## 🧾 PROV-O Lineage Requirements

Required fields:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (STAC input datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (training/inference identity)  

Used by:

- Hydrology Story Node v3  
- Focus Mode v3 hydrology chains  
- Governance dashboards  

---

## 🔐 FAIR+CARE Requirements

Hydrology XAI pipelines MUST:

- Mask culturally sensitive floodplains or archaeological-adjacent hydrology  
- Apply H3 generalization to spatial attribution  
- Respect sovereignty metadata from datasets  
- Document dataset licenses  
- Avoid speculative hydrological inference tied to cultural identity  
- Include CARE scope in JSON-LD bundles  

---

## 🧪 Testing Requirements

Pipelines must pass:

- Deterministic output comparison  
- JSON-LD validation  
- STAC validation  
- CRS/vertical datum checks  
- CARE governance tests  
- SHAP/IG drift detection  
- Raster integrity checks  

Failing tests → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                             |
|----------|------------|-------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Hydrology explainability layer aligned with climate/XAI templates |
---

<div align="center">

### 🔗 Footer  
[⬅ Back to Explainability Index](../README.md) · [🧠 AI Pipeline Layer](../../README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

