---
title: "🌐🔡📦 KFM v11.2.2 — Embeddings STAC Catalog (Spatial 🗺️ · Climate 🌡️ · Hydrology 💧 · Hazard 🌪️ · Narrative 📚 · Fusion 🎯 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/models/embeddings/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Embeddings Working Group 🔡🧠 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Embeddings Models · STAC Catalog Root 🌐🔡📦"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/embeddings-stac-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-embeddings-stac-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Embedding Metadata)"
sensitivity: "Embeddings-STAC"
sensitivity_level: "High"
public_exposure_risk: "Medium"
immutability_status: "version-pinned"

semantic_intent:
  - "embedding-stac"
  - "embedding-collections"
  - "embedding-items"
  - "embedding-modelcards"
  - "embedding-provenance"
  - "embedding-telemetry"
  - "spatial-stac"
  - "climate-stac"
  - "hydrology-stac"
  - "hazard-stac"
  - "narrative-stac"
  - "fusion-stac"
  - "faircare-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/models/embeddings/stac"
  applies_to:
    - "README.md"
    - "collections/*"
    - "items/*"
    - "model-cards/*"
    - "provenance/*"
    - "telemetry/*"
    - "../mlops/*"
    - "../../inference/embeddings/*"
    - "../../../ai/inference/focus/*"

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

# 🌐🔡📦 **Embeddings STAC Catalog — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/embeddings/stac/README.md`

**Purpose**  
Define the **STAC Catalog system** for *all embedding models* in the Kansas Frontier Matrix, including:

🗺️ Spatial embeddings  
🌡️ Climate embeddings  
💧 Hydrology embeddings  
🌪️ Hazard embeddings  
📚 Narrative embeddings  
🎯 Focus Mode Fusion embeddings  
🔡 Vector index metadata (FAISS/HNSW)  
📜 PROV lineage  
💡 XAI metadata  
🔋 Energy + 🌍 Carbon sustainability telemetry  

This catalog ensures **discoverability**, **governance integrity**, **traceability**,  
**FAIR+CARE compliance**, and **sovereignty-safe metadata**.

</div>

---

## 📘🌐🔡 **Overview — Why an Embeddings STAC Catalog?**

Embedding models form the **semantic backbone** of KFM:

- Spatial context  
- Climate regime vectors  
- Hydrology regime fingerprints  
- Hazard-state signatures  
- StoryNode v3 narrative embeddings  
- Focus Mode fusion vectors  

STAC ensures:

- Deterministic metadata  
- Cross-domain linkage  
- FAIR+CARE enforcement  
- Provenance integrity  
- Governance-history traceability  
- Compatibility with StoryNodes + Focus Mode  
- Version-pinned embedding invariants  
- CI auditing  

---

## 🗂️📁🔡 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/embeddings/stac/
    📄 README.md                      # ← This file
    📁 collections/                   # STAC Collections for embedding families
        📄 spatial.json
        📄 climate.json
        📄 hydrology.json
        📄 hazard.json
        📄 narrative.json
        📄 fusion.json
    📁 items/                         # STAC Items for embedding model versions
        📄 embedding_spatial_v11.2.2.json
        📄 embedding_climate_v11.2.2.json
        📄 embedding_hydrology_v11.2.2.json
        📄 embedding_hazard_v11.2.2.json
        📄 embedding_narrative_v11.2.2.json
        📄 embedding_fusion_v11.2.2.json
    📁 model-cards/                   # Embedding model cards (XAI + metrics)
        📄 model-card_spatial_v11.2.2.json
        📄 model-card_climate_v11.2.2.json
    📁 provenance/                    # PROV-O metadata chains
        📄 prov_embedding_spatial_v11.2.2.json
        📄 prov_embedding_climate_v11.2.2.json
    📁 telemetry/                     # OTel + XAI + energy/carbon bundles
        📄 telemetry_spatial_v11.2.2.json
        📄 telemetry_climate_v11.2.2.json
```

---

## 🧬🌐📦 **Embeddings STAC Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌐 Embeddings STAC Collection] --> B[📦 STAC Items (Per Domain + Version)]
    B --> C[💡 XAI Assets (Importance · CAM · Attention)]
    B --> D[📜 PROV-O Lineage]
    B --> E[🛡️ CARE + Sovereignty Metadata]
    B --> F[🔋 Energy + 🌍 Carbon Sustainability]
    B --> G[📄 Model Cards]
    G --> H[🎯 Downstream Pipelines (Focus Mode · StoryNodes · Hazard/Hydro AI)]
```

---

## 🗂️📦🌡️ **STAC Collections (Domains)**

Each embedding domain has its own **STAC Collection**:

- `spatial.json`  
- `climate.json`  
- `hydrology.json`  
- `hazard.json`  
- `narrative.json`  
- `fusion.json`  

Each Collection MUST define:

- `id`, `title`, `description`  
- Spatial/temporal extent  
- Domain variables  
- Embedding dimension invariants  
- FAIR+CARE metadata  
- Sovereignty protection rules  
- XAI inheritance rules  
- STAC → Item linking  

---

## 📦🔡🧠 **STAC Items (Per Model Version)**

Each embedding model version MUST include:

```json
{
  "type": "Feature",
  "id": "embedding_spatial_v11_2_2",
  "stac_version": "1.0.0",
  "properties": {
    "model:domain": "spatial",
    "model:dimension": 512,
    "model:seed": 42
  }
}
```

Required assets:

- `weights`  
- `xai`  
- `telemetry`  
- `provenance`  
- `model-card`  
- `metrics`  

---

## 📄🧠💡 **Embedding Model Cards**

Model cards MUST include:

- Training metadata  
- Hyperparameters  
- Embedding dimension  
- Metrics (norm, PCA stability, cluster coherence)  
- XAI attribution  
- CAM/attention maps (if applicable)  
- FAIR+CARE blocks  
- Sovereignty notes  
- Energy/Carbon telemetry  

---

## 📜🧬🌐 **Provenance (PROV-O)**

Every embedding model MUST provide a PROV chain:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:training:embedding_spatial_v11_2_2",
    "used": [
      "urn:kfm:data:terrain_item",
      "urn:kfm:data:landcover_item"
    ],
    "agent": "urn:kfm:service:embedding-training-engine"
  }
}
```

---

## 💡🔍🔡 **XAI Requirements for Embeddings STAC**

STAC Items MUST reference XAI assets:

- Cross-domain importance vectors  
- CAM overlays (spatial embeddings)  
- Attention maps (transformer embeddings)  
- XAI provenance  

---

## 🔋🌍📊 **Energy + Carbon Sustainability Requirements**

Telemetry MUST include:

- Wh  
- gCO₂e  
- FLOPs  
- GPU/CPU usage  
- Cumulative model carbon impact  

These MUST be included in the STAC Item.

---

## 🛡️⚖️🧭 **FAIR+CARE + Sovereignty Requirements**

All embedding STAC metadata MUST include:

```json
{
  "care": {
    "masking": "h3-embedding-generalized",
    "scope": "public-generalized",
    "notes": ["Embedding metadata generalized inside sovereignty-protected regions"]
  }
}
```

Sovereignty rules MUST ensure:

- No culturally unsafe narrative embeddings  
- No hyperlocal hazard/climate vectors in tribal regions  
- No sensitive environmental signature leakage  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- STAC schema correctness  
- Deterministic STAC Item creation  
- XAI asset presence  
- PROV lineage correctness  
- FAIR+CARE compliance  
- Sovereignty masking  
- Telemetry completeness  
- No sensitive-region leakage  
- Reproducibility of metadata  

Failure → ❌ CI BLOCK.

---

## 🕰️📜 **Version History**

| Version | Date       | Notes                                         |
|---------|------------|-----------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Embeddings STAC Catalog (MAX MODE)    |

---

<div align="center">

### 🔗 Footer  
[🔡 Back to Embeddings Models](../README.md) ·  
[📦 Collections](./collections/README.md) ·  
[📜 Provenance](./provenance/README.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

