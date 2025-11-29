---
title: "🌐📦🌪️ KFM v11.2.2 — Hazard Models STAC Catalog (Tornado 🌪️ · Hail 🧊 · Flood 🌊 · Fire-Weather 🔥 · Heat ☀️ · Winter ❄️ · FAIR+CARE 🛡️ · Sovereignty ⚖️ · XAI 💡 · PROV 📜)"
path: "docs/pipelines/ai/models/hazards/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard AI Working Group 🌪️🧠 · FAIR+CARE Council 🛡️ · Sovereignty Review Board ⚖️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazard Models · STAC Catalog Root 🌐🌪️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/hazard-stac-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-hazard-stac-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
hazard_policy: "../../../../standards/hazards/HAZARD-MODELING-GUIDE.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Hazard Metadata)"
sensitivity: "Hazards-STAC"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-stac"
  - "tornado-stac"
  - "hail-stac"
  - "flood-stac"
  - "fireweather-stac"
  - "heat-stac"
  - "winter-stac"
  - "xai-stac"
  - "prov-stac"
  - "faircare-governance"
  - "sovereignty-protection"
  - "hazard-model-registry"
  - "hazard-item-catalog"

scope:
  domain: "pipelines/ai/models/hazards/stac"
  applies_to:
    - "README.md"
    - "collections/*"
    - "items/*"
    - "model-cards/*"
    - "provenance/*"
    - "telemetry/*"
    - "../mlops/*"
    - "../../inference/hazards/*"
    - "../../models/climate/*"
    - "../../models/hydrology/*"
    - "../../models/embeddings/*"

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

# 🌐📦🌪️ **Hazard Models STAC Catalog — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/hazards/stac/README.md`

**Purpose**  
Define the **STAC Catalog** governing metadata for all Hazard AI models:

🌪️ Tornado  
🧊 Hail  
🌊 Flood  
🔥 Fire-Weather  
☀️ Heat  
❄️ Winter  

The catalog enforces **FAIR+CARE ethics**, **sovereignty protection**,  
**STAC v1.x compliance**, **XAI linkage**, **PROV lineage**,  
**telemetry governance**, and **model registry discoverability**.

</div>

---

## 🗂️📁🌪️ **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/hazards/stac/
    📄 README.md
    📁 collections/
        📄 tornado.json
        📄 hail.json
        📄 flood.json
        📄 fireweather.json
        📄 heat.json
        📄 winter.json
    📁 items/
        📄 hazard_tornado_v11.2.2.json
        📄 hazard_hail_v11.2.2.json
        📄 hazard_flood_v11.2.2.json
        📄 hazard_fireweather_v11.2.2.json
        📄 hazard_heat_v11.2.2.json
        📄 hazard_winter_v11.2.2.json
        📄 item_template.json
    📁 model-cards/
        📄 hazardcard_tornado_v11.2.2.json
        📄 hazardcard_hail_v11.2.2.json
        📄 hazardcard_flood_v11.2.2.json
        📄 hazardcard_fireweather_v11.2.2.json
        📄 hazardcard_heat_v11.2.2.json
        📄 hazardcard_winter_v11.2.2.json
        📄 hazardcard_template.json
    📁 provenance/
        📄 prov_hazard_tornado_v11.2.2.json
        📄 prov_hazard_template.json
    📁 telemetry/
        📄 telemetry_hazard_tornado_v11.2.2.json
        📄 telemetry_template.json
```

---

## 🧬🌐🌪️ **Hazard STAC Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌐 Hazard STAC Collection] --> B[📦 Hazard STAC Items Per Version]
    B --> C[📄 Model Cards Metrics XAI]
    B --> D[📜 PROV O Lineage Chains]
    B --> E[🛡️ CARE And Sovereignty Metadata]
    B --> F[🔋 Energy And 🌍 Carbon Sustainability]
    C --> G[🎯 Downstream Pipelines Focus Mode StoryNode Hydrology Climate]
```

---

# 🔍 **STAC Components**

---

## 🗂️ **1. STAC Collections (Domain-Level)**

Each hazard type MUST have its own Collection:

- `tornado.json`  
- `hail.json`  
- `flood.json`  
- `fireweather.json`  
- `heat.json`  
- `winter.json`  

Each MUST define:

- Hazard domain  
- Spatial + temporal extents  
- Climate + hydrology driver metadata  
- FAIR+CARE + sovereignty metadata  
- Links to STAC Items  

Example:

```json
{
  "type": "Collection",
  "id": "hazard_tornado",
  "description": "Tornado hazard models for KFM v11"
}
```

---

## 📦 **2. STAC Items (Per Version)**

Required fields:

```json
{
  "type": "Feature",
  "id": "hazard_tornado_v11_2_2",
  "collection": "hazard_tornado",
  "stac_version": "1.0.0",
  "properties": {
    "hazard:type": "tornado",
    "hazard:version": "v11.2.2",
    "model:seed": 42,
    "care:masking": "h3-hazard-generalized"
  }
}
```

Required assets:

- weights  
- xai  
- telemetry  
- provenance  
- model-card  
- metrics  
- drift baselines  

---

## 📄 **3. Model Cards**

Each hazard model card MUST include:

- Training metadata  
- Hazard metrics  
- Climate/hydro coupling  
- XAI explainability  
- Stability metrics  
- CARE metadata  
- Sovereignty rules  
- Energy + carbon telemetry  
- STAC references  
- PROV lineage  

---

## 📜 **4. PROV-O Lineage**

Must document:

- Training activity  
- Upstream STAC items used  
- Embedding models used  
- Preprocessing & masking steps  
- XAI lineage  
- Telemetry lineage  

---

## 💡 **5. XAI Requirements**

Hazard models MUST document:

- Climate→hazard attribution  
- Hydrology→hazard attribution  
- Spatial CAM overlays  
- Hazard-driver scores  
- Narrative attribution (if part of Focus Mode)  
- XAI seed-lock + provenance  

---

## 🔋🌍 **6. Energy + Carbon Sustainability**

Every hazard STAC item MUST include:

- watt-hours used  
- gCO₂e emissions  
- FLOPs  
- hardware profiles  
- sustainability constraints  

---

## 🛡️⚖️ **7. FAIR+CARE + Sovereignty Metadata**

All hazard metadata MUST include:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Metadata generalized to protect sovereignty-sensitive hazard regions"]
  }
}
```

Protections include:

- Tribal lands  
- Sensitive water features  
- Cultural regions  
- Any region requiring hazard-signal suppression  

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- STAC schema correctness  
- XAI completeness  
- PROV lineage  
- CARE metadata  
- Sovereignty-safe metadata  
- Telemetry completeness  
- Drift baseline correctness  
- Climate/hydrology driver metadata  
- Consistent outputs across builds  
- No sensitive-region leakage  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 Version History

| Version | Date       | Notes                                     |
|---------|------------|-------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard STAC Catalog (MAX MODE)     |

---

<div align="center">

### 🔗 Footer  
[🌪️ Back to Hazard Models](../README.md) ·  
[📦 STAC Items](./items/README.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

