---
title: "⚡🔍 KFM v11.2.2 — Hazard Explainability Pipelines (Wildfire · Tornado · Wind/Hail · Flood · Multi-Hazard XAI)"
path: "docs/pipelines/ai/explainability/hazard/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Pipeline Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
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
  - "hazard-explainability"
  - "xai"
  - "shap"
  - "integrated-gradients"
  - "cams"
  - "saliency"
  - "spatial-attribution"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "ai-explainability-hazard"
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

# ⚡🔍 **KFM v11.2.2 — Hazard Explainability Pipelines**  
`docs/pipelines/ai/explainability/hazard/README.md`

**Purpose:**  
Define the **explainability (XAI) layer** for **Hazard AI models**, producing deterministic and governed SHAP, IG, CAM/saliency, and spatial attribution outputs for:

- Wildfire  
- Tornado  
- Hail / Wind  
- Severe Weather  
- Flood / Flash Flood  
- Multi-hazard fusion pipelines  

XAI outputs produced here feed:

- **STAC v11 Items**  
- **Story Node v3 hazard narratives**  
- **Focus Mode v3 hazard reasoning**  
- **Governance, auditing, & safety systems**  

</div>

---

## 📘 Overview

Hazard explainability pipelines generate structured attribution for:

- Tornado/wind/hail severity models  
- Wildfire probability & spread models  
- Flood & flash-flood ML models  
- Drought / heatwave hazard predictors  
- Multi-hazard fusion models (climate × hydrology × terrain × vegetation)  

Outputs MUST be:

- Deterministic and reproducible  
- JSON-LD structured  
- STAC-compliant  
- FAIR+CARE safe (masked spatially & semantically)  
- Provenance-rich (PROV-O)  

This directory defines specs for:

- **Global SHAP attribution**  
- **Local SHAP attribution**  
- **Integrated Gradients (IG)**  
- **CAM/saliency maps for spatial CNNs**  
- **GeoTIFF/GeoParquet spatial attribution**  
- **Narrative-ready driver summaries**  
- **XAI JSON-LD evidence bundles**  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/
    ├── 📄 README.md                                  # This file
    │
    ├── 📁 shap/                                      # Global & local SHAP
    │   ├── 📄 global.json
    │   ├── 📄 local.json
    │   └── 📄 hazard-driver-summary.md
    │
    ├── 📁 integrated-gradients/                      # IG gradient attribution
    │   ├── 📄 ig-global.json
    │   └── 📄 ig-samples.json
    │
    ├── 📁 cams/                                      # CAM / saliency overlays
    │   ├── 📄 cam-maps.md
    │   └── 📄 saliency-driver.json
    │
    ├── 📁 spatial-attribution/                       # Spatial/raster XAI
    │   ├── 📄 attribution.tif
    │   └── 📄 spatial-drivers.json
    │
    └── 📁 jsonld/                                    # XAI JSON-LD bundles
        ├── 📄 xai-global.jsonld
        ├── 📄 xai-local.jsonld
        └── 📄 xai-driver-summary.jsonld

---

## 🔍 Explainability Components

### 1. 🟥 SHAP Global Attribution
Used for:

- Multi-hazard fusion  
- Severe weather prediction  
- Wildfire risk scoring  
- Flood/flash flood predictors  

Outputs:

- Feature importance rankings  
- Hazard-driver summaries  
- JSON-LD global attribution bundles  

---

### 2. 🟦 SHAP Local Attribution
Used for:

- Single-event hazard likelihood  
- Localized wildfire/wind/flood scoring  
- Short-term anomaly predictions  

Properties:

- Uncertainty-aware  
- CARE-masked  
- Fully traceable  

---

### 3. 🟩 Integrated Gradients (IG)

For deep-learning hazard models:

- CNN-based radar models  
- Terrain-aware fusion networks  
- Spatially complex predictors  

Outputs:

- Gradient-based attribution  
- JSON-formatted IG bundles  
- Interpretations of hazard-relevant variables  

---

### 4. 🟨 CAMs / Saliency Maps

Used especially for:

- Radar-based tornado/hail prediction  
- Wildfire spread CNNs  
- Flood-mapping convolutional models  

Outputs:

- Pixel-importance maps  
- GeoTIFF overlays  
- CARE-safe spatial abstraction  

---

### 5. 🟪 Spatial Attribution Maps

For gridded hazard outputs:

- Flood probability  
- Wildfire spread tiles  
- Drought index attribution  
- Storm pathway maps  

Outputs:

- Spatial driver rasters  
- GeoParquet / COG attribution assets  
- STAC v11 metadata compatible  

---

### 6. 🧭 XAI → Story Node v3 & Focus Mode v3 Integration

Hazard explainability pipelines MUST produce:

- Narrative-ready hazard driver summaries  
- Spatial attribution for Focus Mode v3 overlays  
- Time-sequenced hazard relevance maps  
- JSON-LD provenance chains  

Used for:

- Story Node hazard narratives  
- Hazard reasoning in Focus Mode v3  
- Multi-domain evidence fusion  

---

## 📡 STAC Integration (KFM-STAC v11)

Hazard XAI outputs MUST include:

- `kfm:explainability:method`  
- `kfm:explainability:global`  
- `kfm:explainability:local`  
- `kfm:explainability:spatial`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS + bounding box  
- Asset checksums (`checksum:multihash`)  
- Vertical datum (if applicable)  

---

## 🧾 PROV-O Lineage Requirements

Each explainability job MUST output:

- `prov:wasGeneratedBy` (model & pipeline identifiers)  
- `prov:used` (STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (training/inference agent identity)  

Used by:

- Governance dashboards  
- Story Node v3  
- Focus Mode v3 hazard evidence sequences  

---

## 🔐 FAIR+CARE Requirements

Hazard explainability MUST:

- Mask culturally sensitive regions  
- Apply H3 generalization for sensitive geospatial areas  
- Respect sovereignty flags in datasets  
- Avoid speculative hazard–cultural associations  
- Include CARE-scope metadata  
- Remove drivers tied to restricted environmental or cultural indicators  

---

## 🧪 Testing Requirements

Pipelines MUST pass:

- Deterministic output tests  
- JSON-LD schema validation  
- STAC validation  
- CRS/vertical checks  
- CARE governance tests  
- Drift detection (SHAP/IG/CAMs)  
- Hazard-specific spatial integrity tests  

Failing tests → **blocked from merge**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                            |
|----------|------------|------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard XAI layer (aligned with climate & hydrology XAI) |
---

<div align="center">

### 🔗 Footer  
[⬅ Back to Explainability Index](../README.md) · [⚡ Hazard Models](../../models/hazards/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

