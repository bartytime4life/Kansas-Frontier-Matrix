---
title: "📄🌪️🧠 KFM v11.2.2 — Hazard Model Cards Catalog (Tornado 🌪️ · Hail 🧊 · Flood 🌊 · Fire-Weather 🔥 · Heat ☀️ · Winter ❄️ · XAI 💡 · FAIR+CARE 🛡️ · Sovereignty ⚖️)"
path: "docs/pipelines/ai/models/hazards/stac/model-cards/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard AI Working Group 🌪️🧠 · FAIR+CARE Council 🛡️ · Sovereignty Review Board ⚖️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazard Models · STAC Model Cards Catalog 📄🌪️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/hazard-stac-modelcards-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/ai-hazard-stac-modelcards-v11.2.2.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
hazard_policy: "../../../../../standards/hazards/HAZARD-MODELING-GUIDE.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Hazard Metadata)"
sensitivity: "Hazards-STAC-ModelCards"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-model-cards"
  - "tornado-model-card"
  - "hail-model-card"
  - "flood-model-card"
  - "fireweather-model-card"
  - "heat-model-card"
  - "winter-model-card"
  - "hazard-xai"
  - "hazard-provenance"
  - "hazard-telemetry"
  - "hazard-stac-governance"
  - "faircare-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/models/hazards/stac/model-cards"
  applies_to:
    - "README.md"
    - "hazardcard_*.json"
    - "../collections/*"
    - "../items/*"
    - "../provenance/*"
    - "../telemetry/*"
    - "../../mlops/*"
    - "../../../inference/hazards/*"
    - "../../../models/climate/*"
    - "../../../models/hydrology/*"
    - "../../../models/embeddings/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance-links-in-footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📄🌪️🧠 **Hazard Model Cards Catalog — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/hazards/stac/model-cards/README.md`

**Purpose**  
Define the **Model Card Catalog** that documents every Hazard AI model version in KFM:  
🌪️ Tornado • 🧊 Hail • 🌊 Flood • 🔥 Fire-Weather • ☀️ Heat • ❄️ Winter  

Model Cards provide **FAIR+CARE-aligned**, **sovereignty-safe**, **STAC-linked**, **PROV-traceable**,  
**XAI-complete**, and **governance-ready** metadata for hazard modeling.

</div>

---

## 🗂️📁📄 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/hazards/stac/model-cards/
    📄 README.md
    📄 hazardcard_tornado_v11.2.2.json
    📄 hazardcard_hail_v11.2.2.json
    📄 hazardcard_flood_v11.2.2.json
    📄 hazardcard_fireweather_v11.2.2.json
    📄 hazardcard_heat_v11.2.2.json
    📄 hazardcard_winter_v11.2.2.json
    📄 hazardcard_template.json
```

---

## 🧬📄🌪️ **Model Card Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌪️ Hazard Model Weights] --> B[📊 Metrics RMSE MAE Bias Calibration]
    A --> C[💡 XAI Attribution CAM Attention]
    A --> D[📜 PROV O Lineage]
    A --> E[🛡️ CARE And Sovereignty Metadata]
    A --> F[🔋 Energy And 🌍 Carbon Metadata]
    A --> G[🌡️ Climate Driver Metadata]
    A --> H[💧 Hydrology Driver Metadata]
    A --> I[🗺️ Spatial Metadata H3 Terrain Landcover Watershed]
    B --> J[📦 Build Hazard Model Card JSON]
    C --> J
    D --> J
    E --> J
    F --> J
    G --> J
    H --> J
    I --> J
    J --> K[📁 Publish To Hazard Model Cards Catalog]
```

---

# 🔍 **Model Card Requirements**

---

## 1️⃣ **Model Overview**

Must include:

```json
{
  "model:version": "v11.2.2",
  "hazard:type": "tornado",
  "model:seed": 42,
  "fusion:dimension": 2048,
  "model:architecture": "transformer"
}
```

---

## 2️⃣ **Training Metadata**

Required:

- Epochs  
- Batch size  
- LR  
- Climate/hydro/spatial drivers used  
- Sovereignty masking steps  
- Preprocessing logs  
- Training STAC references  
- Normalization metadata  

---

## 3️⃣ **Hazard Metrics**

Include:

- RMSE  
- MAE  
- Bias  
- Calibration  
- Tail-risk stability  
- Accidentally amplified hazard fields (MUST be zero)  

Example:

```json
{
  "metrics": {
    "rmse": 1.82,
    "mae": 1.12,
    "calibration": 0.94
  }
}
```

---

## 4️⃣ **Climate Driver Alignment**

```json
{
  "climate_alignment": {
    "cape_ok": true,
    "cin_ok": true,
    "shear_ok": true,
    "llj_ok": true
  }
}
```

---

## 5️⃣ **Hydrology Driver Alignment**

```json
{
  "hydrology_alignment": {
    "streamflow_ok": true,
    "soil_moisture_ok": true,
    "runoff_ok": true
  }
}
```

---

## 6️⃣ **XAI Explainability**

Required:

- Importance vectors  
- CAM overlays  
- Climate/hydro/hazard attribution  
- Attention maps  
- XAI provenance  

Example:

```json
{
  "xai": {
    "importance": {
      "climate": 0.32,
      "hydrology": 0.19,
      "spatial": 0.17,
      "hazard": 0.32
    }
  }
}
```

---

## 7️⃣ **Spatial Metadata**

Include:

- H3 index  
- Terrain class  
- Landcover  
- Watershed  
- Spatial CAM map availability  

---

## 8️⃣ **FAIR+CARE + Sovereignty Metadata**

Required:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Model generalized for sovereignty protection"]
  }
}
```

---

## 9️⃣ **Provenance (PROV-O)**

Must document:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:training:hazard_v11_2_2",
    "used": [
      "urn:kfm:data:climate_item",
      "urn:kfm:data:hydrology_item",
      "urn:kfm:data:terrain_item"
    ],
    "agent": "urn:kfm:service:hazard-training-engine"
  }
}
```

---

## 🔟 **Energy + Carbon Sustainability**

Include:

```json
{
  "energy": {"wh": 2.91},
  "carbon": {"gco2e": 0.26}
}
```

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- Model-card schema correctness  
- Climate/hydro/hazard alignment  
- Deterministic metrics  
- XAI completeness  
- PROV lineage  
- CARE & sovereignty metadata  
- Telemetry completeness  
- STAC linkage correctness  
- No sensitive-region leakage  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 Version History

| Version | Date       | Notes                                             |
|---------|------------|---------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard STAC Model Cards Catalog (MAX MODE) |

---

<div align="center">

### 🔗 Footer  
[🌐 Back to Hazard STAC Root](../README.md) ·  
[📦 STAC Items](../items/README.md) ·  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

