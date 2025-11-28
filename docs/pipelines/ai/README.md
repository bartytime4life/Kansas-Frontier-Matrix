---
title: "🧠 KFM v11.2.2 — AI Pipeline Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/ai-pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/ai-pipelines-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Pipeline Layer"
semantic_document_id: "kfm-ai-pipelines-v11.2.2"
doc_uuid: "urn:kfm:pipelines:ai:index:v11.2.2"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "AI (Medium-Risk)"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "ai-pipelines"
  - "training"
  - "inference"
  - "explainability"
  - "focus-mode"
  - "story-nodes"
  - "agentic-schema-drift"
  - "governed-ml"

scope:
  domain: "pipelines/ai"
  applies_to:
    - "ai-training"
    - "ai-inference"
    - "ai-models"
    - "ai-explainability"
    - "ai-templates"
    - "focus-mode-v3"
    - "story-node-v3"
    - "agentic-schema-drift"

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

# 🧠 **KFM v11.2.2 — AI Pipeline Layer**  
`docs/pipelines/ai/README.md`

**Purpose:**  
Define the **AI/ML pipeline architecture** for the Kansas Frontier Matrix v11, including model training, inference services, Focus Mode engines, Story Node generation, explainability overlays, agentic schema-drift stewardship, and data-aligned semantic reasoning.  
This layer integrates tightly with **ETL**, **STAC**, **Neo4j**, **API**, **MapLibre/Cesium**, and **Focus Mode v3**.

</div>

---

## 📘 Overview

The **AI Pipeline Layer** is the intelligent processing engine that transforms raw and normalized historical, environmental, archaeological, hydrological, and climate data into **high-level semantic outputs** used by KFM, including:

- Entity extraction & linking  
- Geoparsing & geotemporal alignment  
- Climate / hydrology / wildfire / hazard predictions  
- AI-assisted data cleaning & quality checks  
- Generative summaries (strictly data-grounded)  
- Story Node v3 narrative production  
- Focus Mode v3 contextual reasoning  
- Explainability overlays (e.g., SHAP, feature maps)  
- Autonomous pattern detection / anomaly identification  
- **Agentic schema drift detection and governed remediation (self-healing ETL controls)**  

All AI pipelines strictly enforce:

- **FAIR+CARE**  
- **Data Contract v3**  
- **Vertical Axis v11**  
- **CRS v11**  
- **STAC/DCAT v11**  
- **PROV-O lineage**  
- **MCP-DL v6.3 (documentation-first)**  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/
    ├── 📄 README.md                         # This file (AI Pipeline Layer spec, v11.2.2)
    │
    ├── 📁 models/                           # Model families + model cards
    │   ├── 📁 climate/
    │   ├── 📁 hydrology/
    │   ├── 📁 hazards/
    │   ├── 📁 nlp/
    │   ├── 📁 embeddings/
    │   └── 📁 focus-mode/
    │
    ├── 📁 training/                         # Training DAGs + configs
    │   ├── 📁 climate/
    │   ├── 📁 hydrology/
    │   ├── 📁 hazards/
    │   ├── 📁 nlp/
    │   └── 📁 embeddings/
    │       └── 📁 focus-mode/
    │
    ├── 📁 inference/                        # Inference pipelines, batch + on-demand
    │   ├── 📁 climate/
    │   ├── 📁 hydrology/
    │   ├── 📁 hazards/
    │   ├── 📁 embeddings/
    │   └── 📁 focus/
    │
    ├── 📁 explainability/                   # XAI pipelines (SHAP, saliency, IG, etc.)
    │   ├── 📁 climate/
    │   └── 📁 hydrology/
    │
    ├── 📁 templates/                        # SOPs, training configs, model metadata templates
    │   ├── 📁 model-cards/
    │   ├── 📁 explainability/
    │   ├── 📁 inference/
    │   ├── 📁 story-nodes/
    │   └── 📁 mlops/
    │
    └── 📁 agentic-schema-drift/             # Agentic schema-drift steward (Pydantic AI + Prefect + LangGraph)
        ├── 📄 README.md                     # Implementation-layer index
        ├── 📁 src/                          # Steward agents, drift detectors, governance hooks
        ├── 📁 flows/                        # Prefect durable flows + LangGraph subgraphs
        ├── 📁 examples/                     # Synthetic drift events, patches, evaluations, narratives
        ├── 📁 tests/                        # Determinism + governance + lineage test suite
        └── 📁 telemetry/                    # Telemetry + PROV-O + OpenLineage specs

*(Model checkpoints themselves are not stored in the repo; only metadata, cards, and configs.)*

---

## 🤖 AI Pipeline Types (KFM v11)

### 1. 🔍 Entity Extraction Pipelines

Extract place names, dates, people, events from unstructured text:

- spaCy / Transformer-based models  
- Geoparsing aligned to GNIS, KFM STAC Collections, and KFM place registries  
- Links to Neo4j (CIDOC-CRM entities)  
- Story Node term extraction and tagging  

---

### 2. 🌐 Geospatial AI Pipelines

- Land-use change detection  
- Remote-sensing classification  
- Bathymetry / DEM-derived features  
- Hydrological and erosion risk estimation  

Outputs always include:

- CRS & vertical datum  
- STAC Items for geospatial outputs  
- Graph entities for downstream interpretation  

---

### 3. 🌡 Climate AI Pipelines

- Downscaling and bias correction  
- Seasonal anomaly detection  
- Future climate projections (e.g., CMIP-like, Daymet-derived)  
- Explainable forecasting (SHAP, attribution charts)  

---

### 4. 💧 Hydrology AI Pipelines

- Streamflow prediction  
- Reservoir level modeling  
- Sediment flux estimation  
- Scenario modeling for drought / flood risk  

---

### 5. ⚡ Hazard & Wildfire AI Pipelines

- Tornado/hail/wind risk modeling  
- FEMA/NWS event severity prediction  
- Wildfire probability and spread analysis  
- Hazard clustering + anomaly alerts  

---

### 6. 🧭 Focus Mode v3 (Semantic Core)

The AI reasoning engine powering Focus Mode:

- Multi-hop graph reasoning  
- STAC + graph + narrative fusion  
- Entity context windows  
- Multi-source evidence scoring  
- CARE-restricted mask enforcement  
- Automatic map/timeline filtering and highlighting  

---

### 7. 📘 Story Node v3 Generation

AI-assisted narrative generation **bounded by KFM data**:

- Structured JSON-LD output compliant with Story Node schema  
- Geo + time alignment  
- Provenance recorded for all statements  
- Abstraction & CARE-compliant masking for sensitive content  
- Optional multi-language variants  

---

### 8. 🤖 Agentic Schema-Drift & Reliability Pipelines

Agentic reliability patterns that:

- Detect schema drift across STAC/DCAT/Neo4j/tabular sources  
- Propose schema & ETL patches via Pydantic AI agents  
- Validate patches in shadow environments with LangGraph + tests  
- Promote safe patches via Prefect durable flows  
- Emit telemetry, PROV-O lineage, and Story Node v3 narratives describing schema evolution  

See:  
`docs/pipelines/ai/agentic-schema-drift/README.md` and subdirectories.

---

## 🧬 Data & Metadata Requirements

All AI pipelines MUST:

- Consume only **validated** data from `data/processed/` or `data/stac/`  
- Produce outputs with:

  - **CRS v11** fields  
  - **vertical:* metadata** where applicable  
  - Domain extensions (e.g., `hydro:*`, `climate:*`, `hazard:*` properties)  
  - **PROV-O lineage** (who/what/when)  
  - **DCAT** dataset mappings  
  - **Machine-extractable JSON-LD** for knowledge graph integration  

---

## ⚙️ AI Training DAG Requirements

Training DAGs (YAML- or config-driven) MUST:

- Lock random seeds for full reproducibility  
- Load training/eval datasets via STAC Collections (not ad-hoc paths)  
- Log full hyperparameters and configuration versions  
- Produce:

  - Model Card v11  
  - Training lineage (OpenLineage spans)  
  - Evaluation artifact bundle  
  - Fairness and CARE audits  

No training pipeline is considered **production-ready** without these artifacts.

---

## 🎛 Inference Pipelines (Batch + Realtime)

KFM v11 supports:

- **Realtime inference** (API / streaming)  
- **Batch inference** (nightly or scheduled DAGs)  

Inference pipelines MUST:

- Be fully deterministic for the same inputs + seed  
- Produce **STAC Items** for all geospatial outputs  
- Generate graph-safe entities for Neo4j (CIDOC-CRM + KFM ontologies)  
- Emit OTel + OpenLineage telemetry for every run  

---

## 🧠 Explainability Requirements

Explainability is **mandatory** for all predictive AI:

- Use SHAP, LIME, Integrated Gradients, or domain-specific XAI methods  
- Store explainability outputs as part of metadata:

  - e.g., `kfm:explainability:*` fields in STAC Items  
  - Story Nodes should optionally reference important drivers  

- Ensure that XAI outputs for CARE-sensitive entities are masked, aggregated, or removed as required.  

---

## 🔍 FAIR+CARE Requirements

All AI Pipelines MUST:

- Document training datasets, licenses, and restrictions (Model Card)  
- Redact/abstract CARE-protected data and locations  
- Include governance citations (`governance_ref`, policy IDs) in metadata where applicable  
- Support traceability of every AI inference via PROV-O and telemetry  
- Avoid speculation on tribal identity, sacred sites, or sensitive archaeology  
- Use H3 generalization and masking rules when operating on Indigenous or heritage datasets  

---

## 📊 Telemetry & Observability

Telemetry and observability for AI pipelines include:

- Energy and carbon metrics (linked to `energy_schema` and `carbon_schema`)  
- Model latency, throughput, error stats  
- Input dataset versions and checksums  
- STAC lineage and graph-write counts  
- Drift detection and alert signals  

Logged periodically (e.g., nightly) to:

- `releases/v11.2.2/ai-pipelines-telemetry.json` (see `telemetry_ref` in front-matter)

---

## 🧪 Testing Requirements

All AI pipelines MUST have:

- Unit tests for core logic  
- Integration tests for DAG orchestration  
- Golden-record comparison tests  
- Deterministic regression tests (outputs stable under same inputs + seed)  
- Governance rule tests (CARE, FAIR, vertical axis, CRS, STAC/DCAT contracts)  

Pull requests failing any of the above are **blocked** from merging.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                       |
|----------|------------|-----------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; added agentic-schema-drift layout + semantics |
| v11.0.0  | 2025-11-22 | Initial AI Pipeline Layer specification for KFM v11                         |

---

<div align="center">

### 🔗 Footer  

[⬅ Back to Pipelines Index](../README.md) · [🏛 Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [🔐 FAIR+CARE](../../standards/faircare/FAIRCARE-GUIDE.md)

</div>
