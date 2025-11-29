---
title: "📦🔡🌐 KFM v11.2.2 — Embeddings STAC Items (Per-Version Metadata · XAI 💡 · PROV 📜 · FAIR+CARE 🛡️ · Sovereignty ⚖️)"
path: "docs/pipelines/ai/models/embeddings/stac/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Embeddings Working Group 🔡🧠 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Embeddings STAC · Items Catalog 📦🔡"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/embeddings-stac-items-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-embeddings-stac-items-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

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
care_label: "Public · High-Risk (Embedding STAC Items)"
sensitivity: "Embeddings-STAC-Items"
sensitivity_level: "High"
public_exposure_risk: "Medium"
immutability_status: "version-pinned"

semantic_intent:
  - "embedding-stac-items"
  - "embedding-versioning"
  - "embedding-assets"
  - "xai-stac"
  - "provenance-stac"
  - "telemetry-stac"
  - "faircare-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/models/embeddings/stac/items"
  applies_to:
    - "README.md"
    - "embedding_*_v*.json"
    - "../collections/*"
    - "../model-cards/*"
    - "../provenance/*"
    - "../telemetry/*"
    - "../../mlops/*"
    - "../../../inference/embeddings/*"
    - "../../../../ai/inference/focus/*"

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

# 📦🔡🌐 **Embeddings STAC Items — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/embeddings/stac/items/README.md`

**Purpose**  
Define the **STAC Items** representing every version of every embedding model  
(spatial, climate, hydrology, hazard, narrative, fusion) in the Kansas Frontier Matrix.  
Each STAC Item captures:

🔡 **Embedding vectors**  
💡 **XAI explainability metadata**  
📜 **PROV lineage**  
🔋 **Energy/Carbon telemetry**  
🛡️ **FAIR+CARE + sovereignty protections**  
📄 **Model-card linkage**  
📦 **Immutable model registry assets**

</div>

---

## 📘📦🔡 **Overview — What Is An Embedding STAC Item?**

A STAC Item describes one embedding model version, including:

- Model domain (spatial/climate/hydro/hazard/narrative/fusion)  
- Dimensionality  
- Seed (deterministic)  
- XAI artifacts  
- Telemetry  
- PROV  
- CARE + sovereignty metadata  
- STAC asset listings  
- Model-card linkage  
- Drift/stability indicators  

These Items ensure deterministic, governed, sovereignty-safe embedding releases.

---

## 🗂️📁📦 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/embeddings/stac/items/
    📄 README.md
    📄 embedding_spatial_v11.2.2.json
    📄 embedding_climate_v11.2.2.json
    📄 embedding_hydrology_v11.2.2.json
    📄 embedding_hazard_v11.2.2.json
    📄 embedding_narrative_v11.2.2.json
    📄 embedding_fusion_v11.2.2.json
    📄 item_template.json
```

---

## 🧬🌐📦 **Embedding STAC Item Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🔡 Embedding Model Weights] --> B[💡 XAI Metadata]
    A --> C[📜 PROV O Lineage]
    A --> D[📊 Metrics And Stability]
    A --> E[🔋 Energy And 🌍 Carbon Telemetry]
    A --> F[🛡️ CARE And Sovereignty Metadata]
    B --> G[🌐 Build Embedding STAC Item]
    C --> G
    D --> G
    E --> G
    F --> G
    G --> H[📦 Publish To Embeddings STAC Catalog]
```

---

## 📄🔡🧠 **Required STAC Item Fields**

### 1️⃣ **Core STAC Fields**

```json
{
  "type": "Feature",
  "id": "embedding_spatial_v11_2_2",
  "stac_version": "1.0.0",
  "collection": "embeddings-spatial"
}
```

### 2️⃣ **Model Properties**

- `model:domain`  
- `model:dimension`  
- `model:architecture`  
- `model:seed`  
- `model:family` (spatial/climate/hydro/hazard/narrative/fusion)

### 3️⃣ **Assets Block**

Every STAC Item MUST include:

```json
{
  "assets": {
    "weights": {"href": "embedding_model.pt"},
    "xai": {"href": "xai/"},
    "telemetry": {"href": "telemetry/"},
    "provenance": {"href": "prov_embedding.json"},
    "model-card": {"href": "../model-cards/model-card_spatial_v11.2.2.json"},
    "metrics": {"href": "embedding_metrics.json"}
  }
}
```

### 4️⃣ **CARE + Sovereignty Metadata**

```json
{
  "care": {
    "masking": "h3-embedding-generalized",
    "scope": "public-generalized",
    "notes": ["Embedding generalized in sovereignty-sensitive regions"]
  }
}
```

### 5️⃣ **Drift + Stability Fields**

```json
{
  "stability": {
    "drift_centroid": 0.002,
    "drift_cosine": 0.004,
    "cluster_shift": 0.001
  }
}
```

### 6️⃣ **Energy + Carbon Telemetry**

```json
{
  "energy": {"wh": 3.12},
  "carbon": {"gco2e": 0.29}
}
```

### 7️⃣ **STAC Relations**

```
"links": [
  {"rel": "collection", "href": "../collections/spatial.json"},
  {"rel": "model-card", "href": "../model-cards/model-card_spatial_v11.2.2.json"}
]
```

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- Deterministic STAC item structure  
- Schema correctness  
- FAIR+CARE + sovereignty enforcement  
- Telemetry presence  
- XAI metadata correctness  
- PROV lineage integrity  
- STAC → model-card → provenance linkage  
- No leakage of sensitive-region vectors  
- Reproducibility across runs  

Failure → ❌ CI BLOCK.

---

## 🕰️📜 **Version History**

| Version | Date       | Notes                                             |
|---------|------------|---------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Embeddings STAC Items Catalog (MAX MODE)  |

---

<div align="center">

### 🔗 Footer  
[🔡 Back to Embeddings STAC Catalog](../README.md) ·  
[📄 Model Cards](../model-cards/README.md) ·  
[🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

