---
title: "🧭 KFM v11.2.2 — Focus Mode v3 Training Pipelines (Semantic Reasoning · Narrative AI · Evidence Fusion)"
path: "docs/pipelines/ai/training/focus-mode/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Narrative Oversight Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Training Pipeline"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-training-focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-training-focus-v11.2.2.json"
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
sensitivity: "Narrative-Training"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "focus-mode-training"
  - "semantic-reasoning"
  - "narrative-ai"
  - "evidence-fusion"
  - "story-node-training"
  - "xai-training"
  - "provenance"
  - "faircare-governance"

scope:
  domain: "ai-training-focus-mode"
  applies_to:
    - "training-configs"
    - "semantic-reasoner-training"
    - "narrative-builder-training"
    - "evidence-fusion"
    - "story-node-v3"
    - "xai"
    - "provenance"
    - "drift-handling"
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

# 🧭 **KFM v11.2.2 — Focus Mode v3 Training Pipelines**  
`docs/pipelines/ai/training/focus-mode/README.md`

**Purpose:**  
Define the deterministic, provenance-rich training pipelines for **Focus Mode v3 AI models**, including semantic reasoners, narrative builders, and evidence fusion engines.  
Training enforces strict **FAIR+CARE**, **STAC v11**, **PROV-O**, and **Indigenous data sovereignty** constraints, producing models that generate safe, grounded, audit-ready narratives.

</div>

---

## 📘 Overview

Focus Mode v3 training pipelines build models that:

- Synthesize multi-domain data (climate, hydrology, soils, DEM, hazards, archaeology)  
- Produce **semantic reasoning windows**  
- Generate **Story Node v3 narratives**  
- Fuse evidence across STAC, Neo4j, embeddings, and XAI  
- Enforce ethical constraints (CARE masking, cultural sovereignty rules)  
- Guarantee deterministic outputs, no hallucination, no speculation  
- Provide full train-time explainability bundles  
- Emit complete Model Cards v11.2.2  
- Record PROV-O lineage + OpenLineage job spans  
- Track Energy/Carbon v2 telemetry  

These pipelines form the core of KFM’s contextual AI reasoning layer.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/training/focus-mode/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 training-config.yaml                    # Hyperparams, dataset sources, seeds, ontology refs
    ├── 📄 dag.md                                  # Airflow/LangGraph DAG specification
    ├── 📄 evaluation-metrics.md                   # Narrative validity, evidence accuracy, drift tests
    │
    ├── 📁 datasets/                               # STAC-linked dataset manifests
    │   ├── 📄 stac-inputs.json
    │   └── 📄 dataset-license-notes.md
    │
    ├── 📁 explainability/                         # Train-time XAI outputs
    │   ├── 📄 evidence-drivers.json
    │   ├── 📄 attribution-map.json
    │   └── 📄 narrative-saliency.png
    │
    ├── 📁 evaluation/                             # Evaluation bundles
    │   ├── 📄 narrative-validity.json
    │   ├── 📄 evidence-consistency.md
    │   └── 📄 regression-tests.json
    │
    └── 📁 provenance/                             # Training provenance bundles
        ├── 📄 prov-trace.jsonld
        └── 📄 lineage-facets.json

---

## 🧬 Focus Mode v3 Training Categories

### 1. 🧩 Semantic Reasoner Training  
Models must:

- Fuse multi-domain features (climate/hydro/terrain/soils/event data)  
- Generate deterministic semantic windows  
- Align to CIDOC-CRM classes  
- Output context-aware entity relationships  
- Provide XAI drivers (importance vectors, contribution paths)

### 2. 📝 Narrative Builder Training  
Models must:

- Produce Story Node v3 narrative body  
- Enforce *no speculation, no identity inference*  
- Honor CARE masking + sovereignty policies  
- Generate per-sentence provenance links  
- Produce narrative validity metrics  

### 3. 🔗 Evidence Fusion Training  
Models must:

- Combine STAC inputs, graph relationships, text evidence, spatial drivers  
- Produce JSON-LD evidence chains  
- Provide relevance weights & confidence  
- Emit explainability bundles for each fused claim  

### 4. 🧠 Focus-Embeddings Training  
Provides embeddings controlling:

- Narrative relevance  
- Similarity matching  
- Evidence weighting  
- Deduplication and canonicalization of entities  

Must include drift baselines for inference.

---

## ⚙️ Training Requirements (v11.2.2)

### Determinism  
- Seeds locked  
- Hyperparameters versioned  
- Dataset STAC IDs + checksums required  
- Tokenizer/config frozen  
- Environment fingerprint logged  

### Explainability (Train-Time XAI)  
Training MUST output:

- Global evidence drivers  
- Local attribution vectors  
- Narrative saliency maps  
- Spatial/temporal relevance drivers  
- JSON-LD XAI summaries (`kfm:explainability:*`)  

### Evaluation Requirements  
Evaluation bundles MUST include:

- Narrative validity metrics  
- Evidence-chain consistency tests  
- Golden-record comparisons  
- Drift detection (embedding + narrative)  
- CARE masking validation  

### Provenance & Lineage  
Training MUST generate:

- PROV-O JSON-LD (`prov:*`)  
- OpenLineage spans  
- Model version fingerprints  
- Dataset fingerprints (multihash)  
- Training graph of semantic/narrative components  

### FAIR+CARE Enforcement  
Training MUST:

- Mask culturally sensitive or sovereign material  
- Abstract rather than reveal sensitive details  
- Apply H3 generalization for spatial content  
- Record CARE scope in Model Card  
- Follow sovereignty flags from data catalog  

### Energy/Carbon Telemetry  
Required:

- `energy.kwh_estimate`  
- `carbon.gco2e_estimate`  
- Runtime footprint summary  

---

## 📡 STAC Publishing (Training Outputs)

Training outputs MUST include:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- Training input STAC IDs  
- Narrative/XAI bundle references  
- Evaluation bundle references  
- CRS (if spatial)  
- Multihash checksums  
- Full PROV-O lineage  

Outputs include:

- Narrative driver maps  
- Evidence chains  
- Embedding vectors  
- Evaluation bundles  

---

## 🧪 Testing Requirements

Pipelines MUST pass:

- Seed-locked reproducibility  
- Narrative validity tests  
- Evidence-chain consistency  
- XAI drift tests  
- Evaluation regression tests  
- CARE & sovereignty compliance tests  
- STAC & DCAT validation  
- Energy/Carbon telemetry validation  

Failure → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade; governance, telemetry, XAI, STAC templates integrated |
| v11.0.0  | 2025-11-22 | Initial Focus Mode v3 training specification                         |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Training Index](../README.md) · [🧭 Focus Mode Models](../../models/focus-mode/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

