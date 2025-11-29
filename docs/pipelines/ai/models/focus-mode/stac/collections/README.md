---
title: "🗂️🌐🎯 KFM v11.2.2 — Focus Mode STAC Collections (Context AI 🌐 · Geo 🧭 · Climate 🌡️ · Hydrology 💧 · Hazards 🌪️ · Narrative 📖 · Fusion 🔡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/models/focus-mode/stac/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Focus Mode Working Group 🎯🧠 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Focus Mode STAC · Collections Catalog 🗂️🎯"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/focusmode-stac-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-focusmode-stac-v11.2.2.json"
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
care_label: "Public · High-Risk (Contextual Intelligence Metadata)"
sensitivity: "FocusMode-STAC-Collections"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "focusmode-stac-collections"
  - "context-ai-collections"
  - "geo-awareness-collection"
  - "climate-context-collection"
  - "hydrology-context-collection"
  - "hazard-context-collection"
  - "narrative-collection"
  - "fusion-collection"
  - "faircare-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/models/focus-mode/stac/collections"
  applies_to:
    - "README.md"
    - "*.json"
    - "../items/*"
    - "../model-cards/*"
    - "../provenance/*"
    - "../telemetry/*"
    - "../../mlops/*"
    - "../../../inference/focus/*"
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

# 🗂️🌐🎯 **Focus Mode STAC Collections — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/focus-mode/stac/collections/README.md`

**Purpose**  
Define the **STAC Collections** that organize Focus Mode’s contextual intelligence metadata across:  

🧭 **Geo-awareness**  
🌡️ **Climate interpretation**  
💧 **Hydrology interpretation**  
🌪️ **Hazard interpretation**  
📖 **Narrative (Story Node v3)**  
🔡 **Fusion vectors (2048D)**  
🎯 **Complete Focus Mode AI stack**

Collections enforce **FAIR+CARE ethics**, **sovereignty protection**, **STAC-spec alignment**, and  
**cross-domain metadata governance**.

</div>

---

## 🗂️📁🌐 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/focus-mode/stac/collections/
    📄 README.md
    📄 focusmode.json
    📄 geo-awareness.json
    📄 climate.json
    📄 hydrology.json
    📄 hazards.json
    📄 narrative.json
    📄 fusion.json
```

---

## 🧬🌐🎯 **Focus Mode Collections Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🗂️ Focus Mode STAC Collection] --> B[📄 Domain Definition Block]
    A --> C[🛡️ CARE And Sovereignty Metadata]
    A --> D[💡 XAI Inheritance Rules]
    A --> E[📜 PROV O Structure Requirements]
    A --> F[🔋 Energy And 🌍 Carbon Metadata]
    B --> G[📦 STAC Items For All model Versions]
    G --> H[🎯 Downstream Use Focus Mode StoryNode Hazard Climate Hydro]
```

---

# 🔍 **Collection Definitions**

Each Focus Mode domain has its own STAC Collection.  
Below are the mandatory requirements for each.

---

## 🎯 **1. focusmode.json (Primary Collection)**  
Represents the **unified Focus Mode intelligence artifact**, integrating all domains.  
Must define:

- Purpose of Focus Mode  
- Fusion dimension  
- Supported domains  
- FAIR+CARE & sovereignty policy  
- XAI inheritance  
- Link relation templates  

---

## 🧭 **2. geo-awareness.json**  
Defines metadata for:

- H3 indices  
- Terrain  
- Landcover  
- Watersheds  
- Sovereignty-boundary masking  
- Spatial CAM inheritance  

---

## 🌡️ **3. climate.json**  
Defines metadata for climate-domain reasoning:

- Temperature, dewpoint, pressure  
- CAPE/CIN/LLJ/shear  
- Anomaly state metadata  
- Hazard coupling  
- Climate XAI inheritance  

---

## 💧 **4. hydrology.json**  
Includes metadata for hydrology context:

- Soil moisture  
- Runoff  
- Streamflow  
- Drought index  
- Hydrologic CAM inheritance  

---

## 🌪️🔥🌊❄️ **5. hazards.json**  
Domains:

- Tornado  
- Hail  
- Flood  
- Fire-weather  
- Winter-weather  
- Heat stress  

Includes:

- Hazard-driver attribution  
- Climate coupling metadata  
- Hazard suppression in sovereignty zones  

---

## 📖 **6. narrative.json (Story Node v3)**  
Defines:

- Narrative-domain metadata  
- Attention-map inheritance  
- Cultural-safety markers  
- Story Node semantic anchors  
- Sovereignty masking for narrative content  

---

## 🔡 **7. fusion.json**  
Defines the critical **2048D fusion embedding layer**, with fields for:

- Cross-domain mixing rules  
- Weight distribution  
- Drift baselines  
- XAI cross-domain vectors  
- Sovereignty-compliant fusion behavior  

---

# 🛡️⚖️ **FAIR+CARE + Sovereignty Requirements**

Every Collection MUST include:

```json
{
  "care": {
    "masking": "h3-focus-generalized",
    "scope": "public-generalized",
    "notes": [
      "Collection metadata generalized to protect sovereignty-sensitive contexts"
    ]
  }
}
```

Protections MUST cover:

- Tribal territories  
- Cultural features  
- Sensitive hydrological / ecological regions  
- Narrative content referencing cultural or historical material  

---

# 🔋🌍 **Energy + Carbon Metadata Requirements**

Each Collection MUST contain:

- Energy expectations  
- Sustainability constraints  
- gCO₂e tracking fields  
- Telemetry inheritance hooks  

Used for governance & carbon-budget auditing.

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- STAC v1.x compliance  
- Deterministic serialization  
- Fair+CARE metadata  
- Sovereignty masking  
- XAI inheritance rules  
- PROV structure  
- Valid linking to STAC Items  
- No sensitive-region leakage  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 **Version History**

| Version | Date       | Notes                                           |
|---------|------------|-------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Focus Mode STAC Collections (MAX MODE)  |

---

<div align="center">

### 🔗 Footer  
[🌐 Back to Focus Mode STAC Root](../README.md) ·  
[📦 STAC Items](../items/README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

