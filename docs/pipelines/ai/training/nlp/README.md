---
title: "📝 KFM v11.2.2 — NLP Model Training Pipelines (NER · OCR · Text Classification · Geoparsing · Embeddings)"
path: "docs/pipelines/ai/training/nlp/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · NLP Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Training Pipeline"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-training-nlp-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-training-nlp-v11.2.2.json"
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
sensitivity: "NLP-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "nlp-training"
  - "ner-training"
  - "ocr-training"
  - "geoparsing-training"
  - "embeddings-training"
  - "text-classification"
  - "provenance"
  - "faircare-governance"

scope:
  domain: "ai-training-nlp"
  applies_to:
    - "training-configs"
    - "training-dags"
    - "evaluation-bundles"
    - "model-cards"
    - "nlp-xai"
    - "provenance"
    - "dataset-governance"
    - "energy-carbon-telemetry"

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

# 📝 **KFM v11.2.2 — NLP Training Pipelines**  
`docs/pipelines/ai/training/nlp/README.md`

**Purpose:**  
Define deterministic, reproducible NLP training pipelines powering **NER**, **OCR**, **text classification**, **geoparsing**, and **embedding models**.  
All pipelines follow **FAIR+CARE**, **STAC v11**, **PROV-O**, **Data Contract v3**, and must emit **Model Cards**, **XAI bundles**, **Evaluation reports**, and **Energy/Carbon telemetry**.

</div>

---

## 📘 Overview

The NLP training subsystem produces models for:

- Named Entity Recognition (NER)
- Geoparsing & geotemporal extraction
- OCR-to-Text normalization
- Text classification (hazards, hydrology, archaeology, climate)
- Document embeddings
- Narrative reasoning (Focus Mode v3)
- Story Node v3 text grounding

Training pipelines:

- Are fully deterministic (seed + environment lock)
- Consume validated STAC datasets only
- Produce complete Model Cards v11.2.2
- Emit PROV-O training lineage + OpenLineage spans
- Generate explainability bundles (XAI)
- Pass FAIR+CARE + Data Contract v3 validation
- Emit energy/carbon telemetry (sustainability compliance)

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/nlp/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 training-config.yaml                     # Hyperparams, dataset sources, seeds
    ├── 📄 dag.md                                   # DAG overview (Airflow / LangGraph)
    ├── 📄 evaluation-metrics.md                    # Metrics + regression structure
    │
    ├── 📁 datasets/                                # STAC-linked dataset manifests
    │   ├── 📄 stac-inputs.json
    │   └── 📄 dataset-license-notes.md
    │
    ├── 📁 explainability/                          # Train-time XAI outputs
    │   ├── 📄 attention-maps.json
    │   ├── 📄 token-attribution.json
    │   └── 📄 xai-summary.json
    │
    ├── 📁 evaluation/                              # Evaluation bundles from training
    │   ├── 📄 metrics.json
    │   ├── 📄 skill-scores.md
    │   └── 📄 regression-tests.json
    │
    └── 📁 provenance/                              # Training provenance bundles
        ├── 📄 prov-trace.jsonld
        └── 📄 lineage-facets.json

---

## 🧬 NLP Training Categories

### 1. 🔍 NER Training
Extracts:

- Places  
- People  
- Events  
- Organizations  
- Tribal Nations (CARE-masked)  
- Historic references  
- Temporal expressions  

MUST:

- Align with CIDOC-CRM entity classes  
- Emit provenance per extracted token  
- Enforce CARE masking for sensitive identity terms  

---

### 2. 🌐 Geoparsing & Geotemporal Training

Models use:

- GNIS-aligned gazetteers  
- STAC geospatial datasets  
- Textual sources (OCR, archives, KHS docs)

Outputs MUST include:

- Spatial grounding (H3 generalized when needed)  
- Temporal intervals (OWL-Time `ProperInterval`)  
- Provenance for each mapping  

---

### 3. 📄 OCR Training

OCR models MUST:

- Normalize historical fonts and noisy scans  
- Produce token-level confidence  
- Emit provenance per OCR segment  
- Mask culturally sensitive text fragments  

---

### 4. 🧭 Focus Mode v3 Narrative Training

Models MUST:

- Generate deterministic narrative windows  
- Respect CARE masking & narrative constraints  
- Map extracted entities to Neo4j graph nodes  
- Provide provenance for every sentence/claim  
- Include XAI → narrative drivers  

---

### 5. 🧠 Embedding Training (Text)

Models MUST:

- Produce deterministic embedding vectors  
- Document training datasets & licenses  
- Provide PCA/UMAP projections (XAI)  
- Include drift baselines for inference  

---

## ⚙️ Training Requirements (v11.2.2)

### Deterministic Training
MUST include:

- Seed locking  
- Hyperparameter locking  
- Fixed environment fingerprint  
- STAC dataset version locking  
- Reproducible tokenizer configs  

### Explainability (Training-Time XAI)
Training MUST output:

- Attention maps  
- Token-level attribution  
- Global/local importance factors  
- JSON-LD XAI summaries  

### Evaluation Standards
Evaluation bundles MUST contain:

- Precision/Recall/F1 (for NER/classification)  
- OCR word accuracy  
- Geoparsing accuracy + spatial error radius  
- Text classification metrics  
- Drift testing baseline  
- Golden-record comparison  

### Provenance & Lineage
Training MUST emit:

- PROV-O graph  
- OpenLineage task/event spans  
- Model version fingerprint  
- Dataset fingerprints (checksums)  

### FAIR+CARE Enforcement
Training MUST:

- Mask sensitive identities  
- Abstract culturally restricted content  
- Respect sovereignty + Indigenous data policies  
- Include CARE-scope fields in Model Cards  
- Validate dataset licenses (Data Contract v3)  

---

## 📡 STAC Publishing of Training Outputs

Training outputs MUST be published to STAC with:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- Training input STAC IDs  
- Explainability references  
- Evaluation bundle references  
- CRS / bounding geometry (if spatial)  
- Multi-hash checksums  
- PROV-O lineage fields  

---

## 🧪 Testing Requirements

NLP training pipelines MUST pass:

- Seed-locked determinism  
- NER/POS regression tests  
- OCR accuracy checks  
- Geoparsing spatial accuracy tests  
- FAIR+CARE compliance tests  
- XAI drift stability tests  
- STAC + DCAT validation  
- Carbon/Energy telemetry validation  

Any failure → **CI-blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                      |
|----------|------------|------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full uplift to v11.2.2; XAI & governance templates added  |
| v11.0.0  | 2025-11-22 | Initial NLP training specification                         |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Training Index](../README.md) · [📝 NLP Models](../../models/nlp/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

