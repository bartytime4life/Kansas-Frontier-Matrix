---
title: "🧭 KFM v11.2.2 — Focus Mode v3 Reasoning Models (Semantic Engine · Evidence Fusion · Narrative Alignment)"
path: "docs/pipelines/ai/models/focus-mode/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Narrative Oversight Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Family"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-models-focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-models-focus-v11.2.2.json"
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
sensitivity: "Narrative-Reasoning"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "focus-mode"
  - "semantic-reasoning"
  - "cross-domain-fusion"
  - "narrative-ai"
  - "explainability"
  - "care-governance"

scope:
  domain: "ai-models-focus-mode"
  applies_to:
    - "semantic-reasoners"
    - "narrative-builders"
    - "evidence-fusion"
    - "jsonld-story-nodes"
    - "embedding-integration"
    - "ontology-alignment"
    - "provenance"

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

# 🧭 **KFM v11.2.2 — Focus Mode v3 Reasoning Models**  
`docs/pipelines/ai/models/focus-mode/README.md`

**Purpose:**  
Define and govern the **semantic reasoning models** that power Focus Mode v3 — the AI subsystem that fuses STAC metadata, Neo4j graph knowledge, embeddings, explainability vectors, and narrative policies into consistent and FAIR+CARE-aligned insights for users.

</div>

---

## 📘 Overview

Focus Mode v3 is the **semantic orchestration layer** of KFM.  
Its models generate:

- Entity-centered reasoning windows  
- Story Node v3 narratives  
- Cross-domain evidence fusion  
- Provenance-anchored explanations  
- CARE-safe, non-speculative contextual information  
- Timeline + map filtering guidance  
- Multi-hop graph reasoning  
- Spatially masked or abstracted outputs when required  

These models do **not** hallucinate.  
They strictly follow:

- **Source-grounded evidence**  
- **STAC lineage**  
- **Graph links** (Neo4j, CIDOC-CRM)  
- **FAIR+CARE constraints**  
- **Deterministic inference**  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/models/focus-mode/
    ├── 📄 README.md                             # This file
    │
    ├── 📄 model-card.jsonld                     # Model Card v11.2.2 (semantic reasoner)
    ├── 📄 training-metadata.json                # Hyperparams, datasets, seeds, ontology refs
    ├── 📄 narrative-evaluation.md               # Accuracy/validity tests for narrative generation
    ├── 📄 explainability.json                   # Evidence-fusion explainability bundle
    │
    ├── 📁 examples/                             # Example Focus Mode outputs
    │   ├── 📄 focus-snapshot.json               # Example Focus summary (JSON-LD)
    │   ├── 📄 evidence-trace.json               # Provenance chain sample
    │   └── 📄 narrative-window.md               # Narrative example for audits
    │
    ├── 📁 stac/                                 # STAC templates for semantic products
    │   ├── 📄 focus-mode-item.json              # STAC item (semantic output)
    │   └── 📄 assets-template.json              # Assets for narrative/explainability
    │
    └── 📁 mlops/                                # Inference deployment + governance configs
        ├── 📄 inference-config.yaml
        ├── 📄 narrative-governance.md
        └── 📄 drift-monitoring.md

---

## 🧬 Model Types (Focus Mode v3)

### 1. 🧩 Semantic Reasoner  
The core engine that:

- Synthesizes graph, STAC, embeddings, and XAI  
- Performs multi-hop reasoning  
- Enforces ethical constraints, masking, and CARE labels  
- Outputs deterministic semantic windows  

### 2. 🛰 Evidence Fusion Model  
Combines:

- Climate / hydrology indicators  
- Soil/terrain relationships  
- Archaeology data (masked as required)  
- Event timelines (hazards, historical events)  
- Text/NLP evidence from primary sources  

Produces:

- Evidence chains  
- JSON-LD justification vectors  
- Story Node evidence entries  

### 3. 📝 Narrative Builder Model  
Generates the Story Node v3 narrative body:

- Strictly non-speculative  
- Fully provenance-backed  
- Optional multi-language expansions  
- CARE-masked where necessary  
- Integration with Focus Mode’s timeline/map context  

### 4. 🧭 Query Expansion & Relevance Model  
Provides:

- Semantic search and relevance scoring  
- Similarity scoring (embedding-fusion)  
- Deduplication / canonicalization of entities  
- Multi-source evidence prioritization  

---

## 📡 STAC Integration (KFM-STAC v11)

Semantic outputs are registered as:

- STAC Items (`focus-mode:*`)  
- JSON-LD narrative assets  
- Provenance maps (`prov:*`)  

Required fields:

- `kfm:focus:entity_id`  
- `kfm:focus:model_name`  
- `kfm:focus:model_version`  
- `kfm:focus:evidence`  
- `kfm:explainability:*`  
- `kfm:input_items` (array of STAC IDs)  
- Spatial masking metadata (if applicable)  
- CARE labels (`care:*`)  

Outputs must include **multihash checksums**, CRS metadata, bounding geometry (if spatial), and Story Node IDs.

---

## 🧠 Explainability Requirements (XAI)

Focus Mode models must provide:

- Evidence ranking vectors  
- Attention weights or SHAP drivers  
- Source-to-narrative mapping  
- Per-sentence provenance  
- CARE-compliant spatial abstraction  
- JSON-LD explainability bundles  

Explainability outputs feed:

- Story Nodes  
- Focus summaries  
- Audit dashboards  
- Reliability logs  

---

## 🔐 FAIR+CARE Requirements

Focus Mode v3 **must**:

- Mask sensitive locations with **H3 generalization**  
- Never infer tribal identity or sensitive cultural info  
- Only emit narratives grounded in **actual data**  
- Include CARE labels in all outputs  
- Include provenance trace IDs for auditability  
- Document all model training dependencies and data sources  

Any unclear or insufficient provenance → **block inference**.

---

## 🧪 Testing Requirements

All Focus Mode models must pass:

- Narrative validity tests  
- Evidence-chain consistency tests  
- Seed-locked reproducibility  
- Story Node v3 schema validation  
- XAI bundle schema tests  
- FAIR+CARE governance checks  
- Drift tests (embedding + narrative alignment)  
- Golden-record tests  

Failing any check → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                        |
|----------|------------|--------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full upgrade; XAI + STAC templates; governance refinements   |
| v11.0.0  | 2025-11-22 | Initial Focus Mode model family definition                   |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Models Index](../README.md) · [🧠 AI Pipeline Layer](../../README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

