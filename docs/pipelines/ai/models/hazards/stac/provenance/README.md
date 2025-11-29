---
title: "📜🌪️🌐 KFM v11.2.2 — Hazard STAC Provenance Catalog (PROV-O 🧬 · Hazard Lineage 🌪️ · Climate/Hydro Coupling 🌡️💧 · XAI 💡 · FAIR+CARE 🛡️ · Sovereignty ⚖️)"
path: "docs/pipelines/ai/models/hazards/stac/provenance/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard AI Working Group 🌪️🧠 · FAIR+CARE Council 🛡️ · Sovereignty Review Board ⚖️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazard Models · STAC Provenance Catalog 📜🌪️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/hazard-stac-provenance.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/ai-hazard-stac-provenance-v11.2.2.json"
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
care_label: "Public · High-Risk (Hazard Lineage Metadata)"
sensitivity: "Hazards-STAC-Provenance"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-provenance"
  - "hazard-provenance-chains"
  - "stac-lineage"
  - "prov-o-hazards"
  - "xai-provenance"
  - "telemetry-provenance"
  - "climate-hazard-lineage"
  - "hydro-hazard-lineage"
  - "sovereignty-protection"
  - "faircare-governance"

scope:
  domain: "pipelines/ai/models/hazards/stac/provenance"
  applies_to:
    - "README.md"
    - "prov_hazard_*.json"
    - "../items/*"
    - "../model-cards/*"
    - "../collections/*"
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

# 📜🌪️🌐 **Hazard STAC Provenance Catalog — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/hazards/stac/provenance/README.md`

**Purpose**  
Define the **complete PROV-O lineage system** for all Hazard AI models:  
🌪️ Tornado • 🧊 Hail • 🌊 Flood • 🔥 Fire-Weather • ☀️ Heat • ❄️ Winter  

This catalog ensures every hazard model version includes **transparent**, **deterministic**,  
**FAIR+CARE aligned**, **sovereignty-safe**, **STAC-compliant**, **XAI-linked** provenance.

</div>

---

## 🗂️📁📜 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/hazards/stac/provenance/
    📄 README.md
    📄 prov_hazard_tornado_v11.2.2.json
    📄 prov_hazard_hail_v11.2.2.json
    📄 prov_hazard_flood_v11.2.2.json
    📄 prov_hazard_fireweather_v11.2.2.json
    📄 prov_hazard_heat_v11.2.2.json
    📄 prov_hazard_winter_v11.2.2.json
    📄 prov_hazard_template.json
```

---

## 🧬📜🌪️ **Hazard Provenance Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📦 Hazard STAC Item] --> B[📜 PROV O Activity Block]
    B --> C[🧬 Upstream Inputs Climate Hydrology Spatial Event Data]
    C --> D[⚙️ Transformations Training Preprocess Masking]
    D --> E[💡 XAI Provenance Attribution CAM Attention]
    E --> F[📡 Telemetry Provenance Energy Carbon OTel]
    F --> G[🛡️ CARE And Sovereignty Metadata]
    G --> H[🌐 Final Hazard STAC Item With Provenance]
```

---

# 🔍 **Required PROV-O Components**

---

## 1️⃣ **prov:wasGeneratedBy**

Tracks training activity:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:training:hazard_tornado_v11_2_2"
  }
}
```

---

## 2️⃣ **prov:used**

Lists every upstream resource used in training + inference:

```json
{
  "prov": {
    "used": [
      "urn:kfm:data:climate_item",
      "urn:kfm:data:hydrology_item",
      "urn:kfm:data:terrain_item",
      "urn:kfm:data:event_hail_v11",
      "urn:kfm:model:embedding_climate_v11_2_2",
      "urn:kfm:model:embedding_spatial_v11_2_2",
      "urn:kfm:model:embedding_hydrology_v11_2_2",
      "urn:kfm:model:embedding_hazard_v11_2_2",
      "urn:kfm:preprocess:sovereignty_mask_v3"
    ]
  }
}
```

Must be deterministic ordering.

---

## 3️⃣ **prov:wasAssociatedWith**

Indicates the training agent:

```json
{
  "prov": {
    "agent": "urn:kfm:service:hazard-training-engine"
  }
}
```

---

## 4️⃣ **Deterministic Seed Declaration**

Stored in STAC `"properties.model:seed"`.

---

# 🔍 **XAI Provenance Requirements**

Hazard models MUST include XAI provenance:

```json
{
  "xai:prov": {
    "wasGeneratedBy": "urn:kfm:activity:xai:hazard_v11_2_2",
    "used": [
      "hazard_model.pt",
      "normalization_params.json"
    ],
    "agent": "urn:kfm:service:hazard-xai-engine"
  }
}
```

This ensures environmental drivers → hazard logic → attribution remain traceable.

---

# 🔍 **Telemetry Provenance**

Telemetry MUST include:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:telemetry:hazard_inference_v11_2_2",
    "used": [
      "hazard_tornado_v11_2_2.json",
      "embedding_climate_v11_2_2.json"
    ],
    "agent": "urn:kfm:service:hazard-telemetry-engine"
  }
}
```

---

# 🛡️⚖️ **FAIR+CARE + Sovereignty Provenance Requirements**

Each provenance file MUST include:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Sovereignty-safe hazard model applied in STAC lineage"]
  }
}
```

---

# 📦📜🧾 **Provenance Templates**

Template JSON MUST be provided for all hazard domains.

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- PROV-O schema correctness  
- Deterministic ordering  
- STAC linkage correctness  
- XAI provenance  
- Telemetry lineage  
- CARE + sovereignty metadata  
- No sensitive-region leakage  
- Reproducible provenance  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 Version History

| Version | Date       | Notes                                                 |
|---------|------------|-------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard STAC Provenance Catalog (MAX MODE)     |

---

<div align="center">

### 🔗 Footer  
[🌐 Back to Hazard STAC Root](../README.md) ·  
[📄 Model Cards](../model-cards/README.md) ·  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

