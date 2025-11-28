---
title: "🧠 KFM v11.2.2 — Embedding Model Family (Text · Geo · Hybrid · Semantic Search · Focus Mode)"
path: "docs/pipelines/ai/models/embeddings/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · AI Working Group"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Family"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-models-embeddings-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-models-embeddings-v11.2.2.json"
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
sensitivity: "Embedding-Model"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "embedding-models"
  - "semantic-search"
  - "geo-embeddings"
  - "nlp-embeddings"
  - "graph-embeddings"
  - "focus-mode-embedding-core"

scope:
  domain: "ai-models-embeddings"
  applies_to:
    - "model-cards"
    - "training-metadata"
    - "evaluation-bundles"
    - "embeddings"
    - "provenance"
    - "explainability"
    - "search"
    - "focus-mode"
    - "graph-integration"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🧠 **KFM v11.2.2 — Embedding Model Family**  
`docs/pipelines/ai/models/embeddings/README.md`

**Purpose:**  
Define and govern all **text, geospatial, hybrid, and graph-aligned embedding models** used for semantic search, entity similarity, Focus Mode v3 reasoning, Story Node v3 evidence matching, and cross-domain AI fusion in the Kansas Frontier Matrix.

</div>

---

## 📘 Overview

Embedding models provide the **semantic backbone** of KFM.  
They power:

- Text similarity & entity retrieval  
- Geo-semantic similarity (place-aware embedding spaces)  
- Climate/hydrology/terrain hybrid embeddings  
- Vector search for the knowledge graph  
- Story Node evidence matching  
- Focus Mode semantic expansion  
- AI agent reasoning context windows  

All embedding models here MUST:

- Include **Model Card v11.2.2**  
- Provide **training metadata**, **eval bundle**, **explainability**, and **energy/carbon telemetry**  
- Support **FAIR+CARE** masking for sensitive terms/locations  
- Publish **PROV-O lineage** + **STAC metadata** when embeddings produce spatial assets  
- Maintain deterministic embedding vectors for reproducibility  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/embeddings/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 model-card.jsonld                          # Model Card v11.2.2
    ├── 📄 training-metadata.json                     # Hyperparams, seeds, provenance
    ├── 📄 evaluation-report.md                       # Semantic retrieval metrics + drift tests
    ├── 📄 explainability.json                        # Attribution vectors, PCA/UMAP projections
    │
    ├── 📁 examples/                                  # XAI examples, visualizations
    │   ├── 📄 semantic-map.png
    │   ├── 📄 similarity-query.json
    │   ├── 📄 embedding-distribution.png
    │   └── 📄 attribute-drivers.json
    │
    ├── 📁 stac/                                      # STAC templates for spatial embeddings
    │   ├── 📄 embedding-item.json                    # STAC item template when embeddings → geospatial outputs
    │   └── 📄 assets-template.json                   # Asset examples (COG, GeoParquet, etc.)
    │
    └── 📁 mlops/                                     # Deployment, monitoring, drift detection
        ├── 📄 inference-config.yaml
        ├── 📄 drift-monitoring.md
        └── 📄 retrieval-policy.md

---

## 🧬 Embedding Model Types

### 1. 📝 Text Embeddings (NLP)
Used for:

- Semantic search  
- Entity extraction enhancement  
- Document clustering  
- Story Node textual grounding  
- Focus Mode context retrieval  

Requirements:

- Sentence-transformer-compatible or equivalent  
- CARE masking for cultural/Indigenous terms  
- Training metadata with complete dataset licenses  

---

### 2. 🗺️ Geo-Embeddings
Used for:

- Spatial similarity  
- Place-to-place semantic comparisons  
- Archaeology / hydrology / terrain fusion embeddings  
- “Environmental affordance” layer embeddings  

Requirements:

- Must store CRS + bounding box  
- Must produce explainability overlays (e.g., feature relevance maps)  
- Story Node v3 integration required  

---

### 3. 🔀 Hybrid Embeddings (Text × Geo × Climate)
Used for:

- Multi-modal semantic reasoning  
- Deep environmental context models  
- Climate + terrain + soils + hydrology latent spaces  
- Cross-domain inference fusion  

Requirements:

- Explicit multi-source PROV-O lineage  
- Training metadata must identify all upstream STAC Collections  
- Evaluation must include **drift tests across modalities**  

---

### 4. 🧭 Focus Mode v3 Embeddings
Used for:

- Semantic window expansion  
- Narrative entity resolution  
- AI reasoning chain construction  
- Deduplication & similarity scoring  
- Evidence scoring for Story Nodes  

Requirements:

- CARE masking built-in  
- Deterministic embedding vectors  
- Explainability vectors (driver terms + spatial drivers)  

---

## 📡 STAC Integration (KFM-STAC v11)

Embedding models produce STAC metadata when:

- Embeddings create **spatial layers** (e.g., similarity heatmaps, cluster rasters)  
- Embeddings are used in a geospatial ML pipeline  
- Embeddings are used in hydrology/climate/terrain fusion  

Required STAC fields:

- `kfm:embedding:model_name`  
- `kfm:embedding:model_version`  
- `kfm:embedding:method`  
- `kfm:embedding:dimensionality`  
- `kfm:explainability:*`  
- Complete PROV-O relations  

---

## 🧠 Explainability Requirements

Embedding models must produce:

- Global attribution vectors (SHAP / transformer attention)  
- Local attribution vectors for a query  
- PCA/UMAP projections  
- Density maps (if geospatial)  
- JSON-LD XAI structure for Story Nodes + Focus Mode  

---

## 🔐 FAIR+CARE Requirements

Embedding pipelines MUST:

- Mask culturally sensitive or restricted terms  
- Apply H3 generalization for any spatially sensitive output  
- Include explicit CARE scope in Model Cards  
- Avoid inference of tribal identity or related protected classes  
- Document training dataset licenses + ethical constraints  

---

## 🧪 Testing Requirements

All embedding models MUST pass:

- Reproducibility tests (same input → same vector)  
- Drift tests (vector distributions stable across releases)  
- Evaluation regression tests  
- Explainability consistency tests  
- Governance (FAIR+CARE) compliance tests  
- Training metadata + Model Card schema validation  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                         |
|----------|------------|---------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full v11.2.2 uplift; STAC templates; XAI enforcement; emoji tree |
| v11.0.0  | 2025-11-20 | Initial embedding model specification                        |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Models Index](../README.md) · [⚙️ Inference Layer](../../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

