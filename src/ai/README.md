---
title: "🧠 Kansas Frontier Matrix — AI Model Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ai/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-ai-models-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Subsystem-README"
intent: "ai-model-suite"
semantic_document_id: "kfm-ai-model-suite"
doc_uuid: "urn:kfm:ai:model-suite:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk / Public"
immutability_status: "version-pinned"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — AI Model Suite Overview**  
`src/ai/README.md`

**Purpose:**  
Define the complete architecture, governance, training lifecycle, telemetry, and interoperability specifications for the **Kansas Frontier Matrix v11 AI Model Suite**, including all multi-modal transformers, classifiers, and embedding systems.  
All models conform to **MCP-DL v6.3**, **FAIR+CARE**, **STAC/DCAT metadata**, and **KFM-MDP v11** documentation standards.

</div>

---

# 📘 Overview

The **AI Model Suite** powers all machine intelligence capabilities in **KFM v11**, including:

- Entity extraction & classification  
- Temporal-spatial-text alignment  
- Multi-modal embeddings  
- Narrative reasoning (Focus Mode v3)  
- AI-based validation, metadata enrichment, and Story Node generation  

These models operate within KFM’s unified system stack:

**data → ETL/AI pipelines → Neo4j Graph → API → React/MapLibre/Cesium → Story Nodes → Focus Mode v3**

Every model is:

- **Provenance-complete** (PROV-O lineage)
- **Deterministic** where applicable
- **Fully auditable**
- **ETHICS-bound** under FAIR+CARE
- **Energy + Carbon metered** (ISO 50001 / 14064)

---

# 🗂 Directory Layout

```text
src/ai/
│
├── README.md                            # This file
│
├── models/
│   ├── embeddings/                      # Text, graph, spatial embedding models
│   ├── classification/                  # Entity, spatial, document classifiers
│   └── focus_transformer_v3/            # Focus Mode v3 multi-modal reasoning engine
│
└── telemetry/
    ├── focus-telemetry.json             # Global AI telemetry bundle
    └── model-specific/                  # Model-level energy, drift, fairness logs
```

---

# 🧩 AI Model Categories

## 🧬 Embedding Models
- **Text embeddings** (BERT/RoBERTa)
- **Graph embeddings** (Node2Vec, GNNs)
- **Spatial embeddings** (ViT, CNN, raster encoders)
- **Hybrid embeddings** aligned to OWL-Time + GeoSPARQL

## 🧭 Classification Models
- **Named Entity Classification (NEC)**
- **Text classification (topics, genres, treaty types, risk labels)**
- **Spatial classification (landcover, hydrology, geology)**

## 🔮 Focus Transformer v3 (Multi-Modal)
Integrates:

- Time × Space × Text × Graph  
- Cross-modal attention  
- Embedded explainability (SHAP/LIME)  
- CARE-filtered narrative layers  
- Story Node v3 compliance  
- STAC-aware asset reasoning  

This model powers **Focus Mode v3**, the narrative engine that binds the knowledge graph and 3D timeline.

---

# ⚖️ Governance & Ethics

All AI components must comply with:

### 📜 FAIR+CARE  
- Cultural sensitivity filters  
- Authority-to-Control for tribal data  
- Ethical refusal for sensitive content  
- Reproducibility + transparency guarantees  

### 🧾 MCP-DL v6.3  
- Documentation-first  
- Schema-safe JSON/YAML artifacts  
- Experiment logs, SOPs, Model Cards  

### 🌍 Sustainability  
- ISO 50001: Energy reporting  
- ISO 14064: Carbon accounting  
- Telemetry emitted per inference + training job  

---

# ⚙️ Training, Evaluation, and Provenance

## 🚀 Training
- Declarative config files  
- Deterministic seeds  
- Hydra/Lightning orchestration  
- GPU/TPU/CPU uniformity profiles  

## 📊 Evaluation Metrics
- Accuracy, Precision, Recall, F1  
- Confusion matrices  
- FairCARE scoring  
- Drift indices  
- Explainability deltas  

## 🧬 Provenance (PROV-O)
Each model tracks:

- Input datasets  
- Preprocessing chain  
- Hyperparameters  
- Code commit SHA  
- Dependency tree (SBOM)  
- Telemetry bundle references  

---

# 🔐 Telemetry & Sustainability

Each model outputs:

- Energy (Wh)  
- Carbon (gCO₂e)  
- Model-drift metrics  
- Fairness tests  
- Bias indicators  
- Focus-mode narrative quality tests  

Telemetry is stored in:

```
src/ai/telemetry/
```

And referenced in STAC/DCAT metadata.

---

# 🧠 Example: Text Classification Config

```yaml
model:
  name: "bert-base-uncased"
  architecture: "transformer"
  num_labels: 6
  epochs: 5
  batch_size: 16
  learning_rate: 3e-5
  dropout_rate: 0.1

data:
  source: "../../../../data/processed/text_classification_corpus.json"
  validation_split: 0.1

telemetry:
  enable_energy_tracking: true
  telemetry_ref: "../../../telemetry/model-specific/text_classifier_energy.json"

ethics:
  reviewer: "@faircare-council"
  care_tag: "restricted"
  governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
```

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-ai` | Full v11 rebuild. Converted to MDP v11.0.0, added Focus v3, telemetry schema v11, ethics expansion, STAC/DCAT/PROV-O integration. |

---

<div align="center">

**Kansas Frontier Matrix — AI Systems v11**  
*Multi-Modal Intelligence × Ethical Governance × Semantically Linked Narratives*  

[Back to AI Subsystem](../README.md) ·  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
