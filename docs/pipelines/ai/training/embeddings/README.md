---
title: "🧠 KFM v11.2.2 — Embedding Model Training Pipelines (Text · Geo · Hybrid · Semantic Search)"
path: "docs/pipelines/ai/training/embeddings/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · AI Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Training Pipeline"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-training-embeddings-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-training-embeddings-v11.2.2.json"
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
sensitivity: "Embedding-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "embedding-training"
  - "nlp-embeddings"
  - "geo-embeddings"
  - "hybrid-embeddings"
  - "semantic-search"
  - "provenance"
  - "faircare-governance"
  - "xai-training"

scope:
  domain: "ai-training-embeddings"
  applies_to:
    - "training-configs"
    - "training-dags"
    - "evaluation-bundles"
    - "model-cards"
    - "embedding-xai"
    - "provenance"
    - "dataset-governance"
    - "energy-carbon-telemetry"
    - "drift-handling"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🧠 **KFM v11.2.2 — Embedding Model Training Pipelines**  
`docs/pipelines/ai/training/embeddings/README.md`

**Purpose:**  
Define deterministic, provenance-rich, FAIR+CARE-governed training pipelines for **text**, **geospatial**, and **hybrid embeddings** used across semantic search, Focus Mode v3, Story Node v3 evidence fusion, and multi-domain AI reasoning in the Kansas Frontier Matrix.

</div>

---

## 📘 Overview

Embedding training pipelines generate:

- Text embeddings (NER, OCR, classification, semantic search)  
- Geo-embeddings (place-aware vectors)  
- Hybrid embeddings (text × geo × climate × terrain)  
- Focus Mode v3 semantic windows  
- Story Node v3 relevance drivers  
- Explainability vectors (global & local attribution)  
- Evaluation bundles (retrieval metrics, drift baselines)  
- Model Cards (v11.2.2)  
- PROV-O lineage + OpenLineage training spans  
- Sustainability telemetry (energy/carbon v2)

All pipelines:

- MUST use **STAC v11** datasets  
- MUST be deterministic, seed-locked  
- MUST comply with **FAIR+CARE**  
- MUST provide XAI outputs (feature drivers, attribution vectors)  
- MUST include dataset licensing + Data Contract v3 validation  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/embeddings/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 training-config.yaml                    # Hyperparams, tokenizer, seed, STAC sources
    ├── 📄 dag.md                                  # DAG overview (Airflow / LangGraph)
    ├── 📄 evaluation-metrics.md                   # Metrics + regression tests
    │
    ├── 📁 datasets/                               # STAC-linked dataset manifests
    │   ├── 📄 stac-inputs.json
    │   └── 📄 dataset-license-notes.md
    │
    ├── 📁 explainability/                         # Train-time XAI outputs
    │   ├── 📄 embedding-attribution.json
    │   ├── 📄 attention-weights.json
    │   └── 📄 projection-umap.png
    │
    ├── 📁 evaluation/                             # Evaluation bundles
    │   ├── 📄 metrics.json
    │   ├── 📄 similarity-tests.md
    │   └── 📄 regression-tests.json
    │
    └── 📁 provenance/                             # Training provenance bundles
        ├── 📄 prov-trace.jsonld
        └── 📄 lineage-facets.json

---

## 🧬 Embedding Training Categories

### 1. 📝 Text Embedding Training
Used for:

- Semantic search  
- Story Node grounding  
- Focus Mode reasoning  
- Entity resolution  

Outputs MUST include:

- Deterministic vectors  
- Vocabulary provenance  
- Explainability (attention & attribution)  

---

### 2. 🗺️ Geo-Embedding Training
Used for:

- Place-to-place similarity  
- Environmental/terrain semantic mapping  
- Archaeology / hydrology / climate fusion  

MUST:

- Include CRS metadata  
- Apply H3 generalization for sensitive areas  
- Produce spatial explainability overlays  

---

### 3. 🔀 Hybrid Embedding Training
Combines:

- Text × Geo × Climate × Terrain × Hydrology  

MUST:

- Log fusion weights  
- Emit XAI factor-blend vectors  
- Provide multi-modal evaluation bundles  

---

### 4. 🧭 Focus Mode v3 Embedding Core
Powers:

- Semantic window expansion  
- Relevance ranking  
- Evidence fusion  
- Story Node narrative justification  

MUST:

- Provide narrative-safe embeddings  
- Enforce CARE masking  
- Provide JSON-LD XAI driver summaries  

---

## ⚙️ Training Requirements (v11.2.2)

### Determinism
Training MUST:

- Lock seeds  
- Freeze tokenizer + vocab  
- Version-lock STAC datasets  
- Freeze environment fingerprint  

### Explainability Requirements  
Training MUST output:

- Global driver vectors  
- Local attribution vectors  
- PCA/UMAP projections  
- Attention/gradient maps (if transformer-based)  
- JSON-LD XAI bundles  

### Evaluation Standards  
Evaluation bundles MUST include:

- Retrieval metrics (recall@k, MRR, nDCG)  
- Embedding drift detection  
- Golden-record test sets  
- Confidence bounds  
- Sensitivity to CARE-masked content  

### Provenance & Lineage  
Training MUST provide:

- PROV-O lineage (JSON-LD)  
- OpenLineage run/task spans  
- Model version fingerprint  
- Dataset checksums  

### FAIR+CARE Enforcement  
Embedding training MUST:

- Mask restricted cultural terms  
- Apply H3 generalization for sensitive geospatial embeddings  
- Avoid speculative similarity inference  
- Include CARE scope in model metadata  
- Track dataset licenses (Data Contract v3)  

### Energy/Carbon Telemetry  
Training MUST record:

- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  
- Training runtime footprint  

---

## 📡 STAC Publishing (Training Outputs)

Training MUST publish:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- Training dataset STAC IDs  
- XAI bundle references  
- Evaluation bundle references  
- CRS + vertical axis (if spatial)  
- Checksums (multihash)  
- Provenance blocks  

Outputs can include:

- Embedding projection assets (COGs or vectors)  
- XAI bundles  
- Evaluation bundles  
- Embedding metadata for downstream pipelines  

---

## 🧪 Testing Requirements

Embedding training pipelines MUST pass:

- Seed-locked reproducibility  
- Embedding drift tests  
- Evaluation regression tests  
- CARE-sensitive vocabulary masking tests  
- XAI drift tests  
- STAC/DCAT validation  
- Energy/Carbon telemetry validation  
- Provenance schema validation  

All failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                       |
|----------|------------|-------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade; XAI templates, STAC metadata, governance pass |
| v11.0.0  | 2025-11-22 | Initial embedding training specification                    |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Training Index](../README.md) · [🧠 Embedding Models](../../models/embeddings/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
