---
title: "🗂️🌐🌪️ KFM v11.2.2 — Hazard STAC Collections (Tornado 🌪️ · Hail 🧊 · Flood 🌊 · Fire-Weather 🔥 · Heat ☀️ · Winter ❄️ · FAIR+CARE 🛡️ · Sovereignty ⚖️)"
path: "docs/pipelines/ai/models/hazards/stac/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard AI Working Group 🌪️🧠 · FAIR+CARE Council 🛡️ · Sovereignty Review Board ⚖️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazard Models · STAC Collections 🗂️🌐🌪️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/hazard-stac-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-hazard-stac-v11.2.2.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Hazards-STAC-Collections"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-stac-collections"
  - "tornado-collection"
  - "hail-collection"
  - "flood-collection"
  - "fireweather-collection"
  - "heat-collection"
  - "winter-collection"
  - "faircare-governance"
  - "sovereignty-protection"
  - "hazard-driver-domains"
  - "hazard-stac-governance"

scope:
  domain: "pipelines/ai/models/hazards/stac/collections"
  applies_to:
    - "README.md"
    - "*.json"
    - "../items/*"
    - "../model-cards/*"
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
requires_governance_links-in-footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🗂️🌐🌪️ **Hazard STAC Collections — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/hazards/stac/collections/README.md`

**Purpose**  
Define the **STAC Collections** governing metadata for all Hazard AI domains:

🌪️ Tornado  
🧊 Hail  
🌊 Flood  
🔥 Fire-Weather  
☀️ Heat  
❄️ Winter  

Collections enforce **FAIR+CARE**, **sovereignty safety**, **XAI inheritance**, **STAC spec alignment**,  
and **cross-domain consistency** across hazard drivers.

</div>

---

## 🗂️📁🌐 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/hazards/stac/collections/
    📄 README.md
    📄 tornado.json
    📄 hail.json
    📄 flood.json
    📄 fireweather.json
    📄 heat.json
    📄 winter.json
```

---

## 🧬🌐🌪️ **Hazard Collections Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🗂️ Hazard STAC Collection] --> B[📄 Domain Definition Block]
    A --> C[🛡️ CARE And Sovereignty Metadata]
    A --> D[💡 XAI Inheritance Rules]
    A --> E[📜 PROV O Structure Requirements]
    A --> F[🔋 Energy And 🌍 Carbon Metadata]
    B --> G[📦 STAC Items For All Hazard Model Versions]
    G --> H[🎯 Downstream Consumers Focus Mode Hydrology Climate]
```

---

# 🔍 **Collection Definitions**

Each hazard type has its own STAC Collection MUST include:

---

## 🌪️ **1. Tornado Collection (tornado.json)**  
Defines metadata for:

- CAPE/CIN/SRH/shear/LLJ  
- Terrain influence on supercells  
- Climate-driver inheritance  
- CAM spatial generalization  
- FAIR+CARE masking for sovereignty regions  

---

## 🧊 **2. Hail Collection (hail.json)**  
Specifies:

- MUHAIL/hail-proxy variables  
- Storm-top temperature domain  
- Thermodynamic depth metadata  
- Dryline/upslope patterns  

---

## 🌊 **3. Flood Collection (flood.json)**  
Defines:

- Precip buckets (1h/3h/6h)  
- Runoff + soil moisture  
- Streamflow + basin metadata  
- Hydrology-driven hazard constraints  

---

## 🔥 **4. Fire-Weather Collection (fireweather.json)**  
Includes:

- Temp/humidity/wind/drought index  
- Fuel moisture metadata  
- CAM dryness hotspots  
- Sovereignty-sensitive fire-weather patterns  

---

## ☀️ **5. Heat Collection (heat.json)**  
Covers:

- Heat index metadata  
- Synoptic patterns (ridge, trough)  
- Dewpoint/temp gradient metadata  
- Environmental health-safety metadata  

---

## ❄️ **6. Winter Collection (winter.json)**  
Specifies:

- Snow-liquid ratio  
- Wind chill / thermal gradient metadata  
- CAM snowband relevance  
- Terrain influence metadata  

---

# 🛡️⚖️ **FAIR+CARE + Sovereignty Requirements**

All Collections MUST include:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Metadata generalized to protect sovereignty-sensitive hazard areas"]
  }
}
```

Protections include:

- Tribal territories  
- Cultural/ecological protected areas  
- Sensitive hydroclimate regions  
- Watersheds with restrictions  

---

# 🔋🌍 **Energy + Carbon Metadata**

Collections MUST define:

- Expected energy cost categories  
- gCO₂e emission expectations  
- Sustainability targets  
- Telemetry inheritance rules  

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- STAC compliance  
- Deterministic serialization  
- XAI inheritance consistency  
- Sovereignty masking correctness  
- FAIR+CARE metadata  
- Link references to Items  
- Cross-domain alignment  
- No sensitive-region leakage  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 Version History

| Version | Date       | Notes                                             |
|---------|------------|---------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard STAC Collections (MAX MODE)        |

---

<div align="center">

### 🔗 Footer  
[🌐 Back to Hazard STAC Root](../README.md) ·  
[📦 STAC Items](../items/README.md) ·  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

