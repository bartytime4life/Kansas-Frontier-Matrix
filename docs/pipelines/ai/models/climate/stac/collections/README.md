---
title: "🗂️🌡️🌐 KFM v11.2.2 — Climate STAC Collections (Downscaling 📉 · Drivers ⚡ · Bias-Correction 📏 · Anomalies 📉 · MLOps 🚀 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/models/climate/stac/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Data Working Group 🌡️📊 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Climate STAC · Collections Catalog 🗂️🌡️"

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/climate-stac-collections-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-climate-stac-collections-v11.2.2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Climate Aggregates)"
sensitivity: "Climate-STAC-Collections"
sensitivity_level: "High"
public_exposure_risk: "Medium"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-stac-collections"
  - "collection-definition"
  - "climate-model-grouping"
  - "downscaling-collection"
  - "driver-model-collection"
  - "biascorr-collection"
  - "anomaly-collection"
  - "mlops-collection"
  - "faircare-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/models/climate/stac/collections"
  applies_to:
    - "README.md"
    - "*.json"
    - "../items/*"
    - "../model-cards/*"
    - "../../mlops/*"
    - "../../../inference/climate/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🗂️🌡️🌐 **Climate STAC Collections — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/climate/stac/collections/README.md`

**Purpose**  
Define the **STAC Collections** for Climate AI model families:  
📉 Downscaling,  
⚡ Climate drivers,  
📏 Bias-correction models,  
📉 Anomaly models,  
🚀 Climate MLOps metadata,  
📦 XAI + PROV lineage bundles,  
🛡️ FAIR+CARE & sovereignty protections.

Collections serve as **governed namespaces** grouping all Climate AI STAC Items.

</div>

---

## 📘🗂️🌡️ **Overview — What Are Climate STAC Collections?**

Climate STAC Collections describe **categories of climate model artifacts**, including:

- Model family identity  
- Spatial/temporal extent  
- Domain variables  
- Governance metadata  
- Care + sovereignty rules  
- Links to STAC Items  
- Lineage (PROV) and sustainability metadata  
- XAI metadata inheritance rules  

Collections allow downstream systems—Focus Mode, Story Nodes, hazards, hydrology, climate inference—to query **groups** of models deterministically.

---

## 🗂️📁🌐 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/climate/stac/collections/
    📄 README.md                         # ← This file
    📄 downscaling.json                  # STAC collection for all downscalers
    📄 drivers.json                      # STAC collection for CAPE/CIN/shear/LLJ models
    📄 bias-correction.json              # STAC collection for bias correction models
    📄 anomalies.json                    # STAC collection for anomaly models
    📄 mlops.json                        # STAC collection for training/validation/deployment metadata
```

---

## 🧬🌐🗂️ **STAC Collections Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📘 Climate STAC Collection] --> B[📦 Climate STAC Items]
    A --> C[💡 XAI Requirements]
    A --> D[📜 PROV Lineage Rules]
    A --> E[🛡️ CARE + Sovereignty Metadata]
    A --> F[🔋 Energy + 🌍 Carbon Metadata]
    B --> G[🌡️ Downstream Workflows (Hazard Hydrology Focus Mode)]
```

---

## 📦📘🌡️ **Collection Definition Requirements**

Each Collection MUST include:

### ✔ Core fields

```json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "climate-downscaling",
  "description": "KFM Climate Downscaling Models (U-Net, Transformer, Hybrid)"
}
```

### ✔ Spatial + temporal extent  
- Must represent entire Kansas bounding box  
- Must include temporal extent of model training data  

### ✔ Keywords  
e.g. `"downscaling"`, `"climate-drivers"`, `"bias-correction"`, `"anomalies"`, `"mlops"`

### ✔ License  
`"MIT"` for model metadata (unless otherwise governed)

### ✔ Governance + ethics links  
- FAIR+CARE  
- Sovereignty rules  
- Governance approvals  
- Data contract  

### ✔ CARE block  
```json
{
  "care": {
    "masking": "h3-climate-generalized",
    "scope": "public-generalized",
    "notes": ["Collection metadata generalized to protect sovereignty-sensitive climate domains"]
  }
}
```

### ✔ Links to Items  
All Items for this Collection MUST connect back via `"collection"` link.

---

## 📉📦🌡️ **Downscaling Collection Requirements**

Models include:

- U-Net  
- Transformer downscaler  
- Hybrid physics-ML models  
- Climate refinement networks  

Fields MUST include:

- Vertical axis metadata  
- CRS  
- Raw/stage inputs  
- Training era  
- Bias correction linkages  

---

## ⚡📦🌡️ **Driver Model Collection Requirements**

Driver families:

- CAPE  
- CIN  
- Shear (0–1 km, 0–3 km, 0–6 km)  
- LLJ  
- Storm-relative helicity  
- Lapse rates  

Collections MUST store:

- Physics definition references  
- XAI driver validity  
- Hazard coupling metadata  

---

## 📏📦🌡️ **Bias-Correction Collection Requirements**

Bias-correction collections MUST describe:

- Normalization methodology  
- Correction function  
- Physical consistency requirements  

---

## 📉📦🌡️ **Anomaly Model Collection Requirements**

Anomaly models MUST include:

- Baseline datasets  
- Deviation definition  
- XAI anomaly explainability  
- Governance warnings for anomaly-sensitive regions  

---

## 🚀📦🌡️ **MLOps Collection Requirements**

Includes:

- Training metadata collections  
- Deployment MLOps metadata  
- Model-card storage  
- Telemetry logs (energy/carbon/OTel)  
- Drift/bias audit logs  
- Reproducibility requirements  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- Collection schema validity  
- STAC 1.x compliance  
- CARE metadata correctness  
- Sovereignty masking applied  
- Deterministic generation  
- XAI & PROV completeness  
- Links to Items valid  
- No sensitive-region leakage  
- Sustainability metadata present  

Failure → ❌ CI BLOCK.

---

## 🕰️📜 **Version History**

| Version | Date       | Notes                                      |
|---------|------------|--------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Climate STAC Collections Catalog    |

---

<div align="center">

### 🔗 Footer  
[🌡️ Back to Climate STAC Catalog](../README.md) ·  
[📦 STAC Items](../items/README.md) ·  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

