---
title: "🧠 KFM v11.2.4 — AI Pipeline Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Full v10.x → v11.x compatibility"
status: "Active / Enforced"

doc_kind: "Pipeline Layer"
header_profile: "standard"
footer_profile: "standard"

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

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "AI (Medium-Risk)"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Reliability Board"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/ai-pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/ai-pipelines-v11.2.4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "PROV-O Core + KFM Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"

semantic_document_id: "kfm-ai-pipelines-v11.2.4"
doc_uuid: "urn:kfm:pipelines:ai:index:v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:ai:index:v11.2.4"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

semantic_intent:
  - "ai-pipelines"
  - "training"
  - "inference"
  - "explainability"
  - "focus-mode"
  - "story-nodes"
  - "agentic-schema-drift"
  - "governed-ml"

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

# 🧠 KFM v11.2.4 — AI Pipeline Layer  
`docs/pipelines/ai/README.md`

**Purpose:**  
Define the **AI/ML pipeline architecture** for the Kansas Frontier Matrix v11, including model training, inference services, Focus Mode engines, Story Node generation, explainability overlays, agentic schema-drift stewardship, and data-aligned semantic reasoning.  
This layer integrates tightly with **ETL**, **STAC/DCAT**, **Neo4j**, **API**, **MapLibre/Cesium**, **Story Nodes**, and **Focus Mode v3**.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/pipelines/ai/
├── 📄 README.md                      # 🧠 AI Pipeline Layer spec (this file)
│
├── 📂 models/                        # 🧬 Model families & model cards (metadata only)
│   ├── 📂 climate/
│   ├── 📂 hydrology/
│   ├── 📂 hazards/
│   ├── 📂 nlp/
│   ├── 📂 embeddings/
│   └── 📂 focus-mode/
│
├── 📂 training/                      # 🏋️ Training DAGs, configs & evaluation notes
│   ├── 📂 climate/
│   ├── 📂 hydrology/
│   ├── 📂 hazards/
│   ├── 📂 nlp/
│   └── 📂 embeddings/
│       └── 📂 focus-mode/
│
├── 📂 inference/                     # ⚡ Inference pipelines (batch + on-demand)
│   ├── 📂 climate/
│   ├── 📂 hydrology/
│   ├── 📂 hazards/
│   ├── 📂 embeddings/
│   └── 📂 focus/
│
├── 📂 explainability/                # 🔍 XAI pipelines (SHAP, saliency, IG, etc.)
│   ├── 📂 climate/
│   └── 📂 hydrology/
│
├── 📂 templates/                     # 📑 SOPs, configs, model-card templates
│   ├── 📂 model-cards/
│   ├── 📂 explainability/
│   ├── 📂 inference/
│   ├── 📂 story-nodes/
│   └── 📂 mlops/
│
└── 📂 agentic-schema-drift/          # 🤖 Agentic schema-drift steward
    ├── 📄 README.md                  # Implementation-layer index (governed agents)
    ├── 📂 src/                       # Agents, drift detectors, governance hooks
    ├── 📂 flows/                     # Prefect flows & LangGraph subgraphs
    ├── 📂 examples/                  # Synthetic drift events, patches, narratives
    ├── 📂 tests/                     # Determinism, governance, lineage tests
    └── 📂 telemetry/                 # Telemetry + PROV-O + OpenLineage specs
```

> **Note:** Model checkpoints themselves are **not** stored in the repo; only metadata, model cards, configs, and evaluation summaries live under `docs/` and `src/`.

---

## 📘 Overview

The **AI Pipeline Layer** is the intelligent processing engine that transforms raw and normalized historical, environmental, archaeological, hydrological, and climate data into **high-level semantic outputs** used throughout KFM, including:

- Entity extraction and linking.  
- Geoparsing and geotemporal alignment.  
- Climate / hydrology / hazard predictions.  
- AI-assisted data cleaning and quality checks.  
- Generative summaries (strictly data-grounded and provenance-linked).  
- Story Node v3 narrative production and updates.  
- Focus Mode v3 contextual reasoning.  
- Explainability overlays (e.g., SHAP, saliency maps, attribution profiles).  
- Autonomous pattern detection and anomaly identification.  
- **Agentic schema-drift detection and governed remediation** (self-healing ETL controls).

All AI pipelines must adhere to:

- **FAIR+CARE** governance.  
- **Data Contract v3** and KFM-PDC v11.  
- **CRS v11** and vertical-axis conventions.  
- **STAC/DCAT v11** metadata profiles.  
- **PROV-O** lineage and **OpenLineage** runtime events.  
- **MCP-DL v6.3** documentation-first practices.

---

## 🧭 Context

In the KFM stack:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → AI Pipeline Layer → API → Frontend → Story Nodes & Focus Mode

The AI layer:

- **Consumes** validated, ontologically-aligned data from `data/processed/` and `data/stac/`.  
- **Produces** model outputs, semantic annotations, and narratives that are:
  - Typed against KFM ontologies.  
  - Versioned and provenance-linked.  
  - Governed by FAIR+CARE and sovereignty policies.  

It is tightly coupled to:

- **Core pipeline architecture** (`docs/pipelines/core/README.md` and queue-architecture standard).  
- **Lineage standards** (`docs/standards/lineage/openlineage-integration.md`).  
- **Geoprivacy and geoethics standards** (for masking and sensitive-site protections).  
- **Frontend standards** (Story Nodes, Focus Mode, geoethical reflection layer).

---

## 🧱 Architecture

### 1. AI pipeline classes

AI pipelines are grouped into several governed classes:

#### 1.1 🔍 Entity extraction pipelines

- Extract places, dates, people, events from unstructured text.  
- Use spaCy / Transformer-based models and domain-specific rules.  
- Geoparse entities against:
  - GNIS and KFM place registries.  
  - STAC Collections for spatial context.  
- Emit:
  - Neo4j entities (CIDOC-CRM + KFM-OP v11).  
  - Story Node term tags and references.

#### 1.2 🌐 Geospatial AI pipelines

- Land-use change detection and classification.  
- Remote-sensing–derived features (e.g., vegetation indices, water extent).  
- DEM-derived features and terrain metrics.  
- Hydrological and erosion risk estimation.  

Outputs must include:

- CRS and vertical datum.  
- STAC Items for geospatial outputs.  
- Graph entities for downstream exploration.

#### 1.3 🌡 Climate AI pipelines

- Downscaling and bias correction.  
- Seasonal anomaly detection.  
- Scenario and projection modeling.  
- Explainable forecasting (e.g., SHAP analyses).

#### 1.4 💧 Hydrology AI pipelines

- Streamflow prediction.  
- Reservoir and aquifer level modeling.  
- Sediment and nutrient flux estimation.  
- Scenario modeling for drought/flood risk.

#### 1.5 ⚡ Hazard & wildfire AI pipelines

- Tornado/hail/wind risk modeling.  
- FEMA/NWS event severity prediction.  
- Wildfire probability and spread modeling.  
- Hazard clustering and anomaly alerts.

#### 1.6 🧭 Focus Mode v3 semantic core

The reasoning engine powering Focus Mode:

- Multi-hop graph reasoning over Neo4j.  
- STAC + graph + narrative fusion.  
- Entity context windows and evidence scoring.  
- CARE-constrained masking and access enforcement.  
- Automatic map/timeline filters and highlights.

#### 1.7 📘 Story Node v3 generation

AI-assisted narrative generation **bounded by KFM data**:

- Structured JSON/JSON-LD output compliant with Story Node schema.  
- Geo- and time-aligned segments.  
- Explicit provenance for all statements (linking to sources and pipeline runs).  
- CARE-compliant abstraction/masking for sensitive content.  
- Optional multi-language variants, where governance allows.

#### 1.8 🤖 Agentic schema-drift & reliability pipelines

Agentic reliability patterns that:

- Detect schema drift across STAC/DCAT/Neo4j/tabular sources.  
- Propose schema and ETL patches via governed AI agents.  
- Validate patches in shadow environments (LangGraph + tests).  
- Promote safe patches via durable workflows.  
- Emit telemetry, OpenLineage, and PROV-O describing schema evolution.

See `docs/pipelines/ai/agentic-schema-drift/README.md` for details.

### 2. Training vs inference flows

- **Training flows** (config-driven DAGs):
  - Lock random seeds.  
  - Use STAC Collections or DCAT catalogs as dataset entry points.  
  - Log hyperparameters and config versions.  
  - Produce:
    - Model Card v11.  
    - Training lineage (OpenLineage events).  
    - Evaluation bundles and fairness/CARE audits.

- **Inference flows** (batch and realtime):
  - Deterministic for same inputs + seed.  
  - Emit STAC Items and graph entities for outputs.  
  - Generate OpenLineage events per run.  
  - Respect governance flags (e.g., disallow restricted outputs).

---

## 📦 Data & Metadata

AI pipelines MUST:

- Consume only **validated** data from:
  - `data/processed/`  
  - `data/stac/`  
  - Graph layers that pass governance checks.  

- Produce outputs with:

  - **CRS v11** and vertical metadata where applicable.  
  - Domain-specific property namespaces (`hydro:*`, `climate:*`, `hazard:*`, etc.).  
  - **PROV-O** lineage (entities, activities, agents).  
  - **DCAT** dataset mappings and identifiers.  
  - **Machine-extractable JSON-LD** for knowledge graph ingestion.  
  - Checksums and version identifiers aligned with data contracts.

### Training DAG metadata

Training DAGs must record:

- Dataset versions (STAC Collection IDs / DCAT dataset IDs).  
- Model artifact digests (e.g., `sha256:...`).  
- Hyperparameter and config hashes.  
- Evaluation metrics and fairness/CARE summaries.

### Explainability metadata

Explainability outputs (SHAP, LIME, IG, etc.) must:

- Be stored as structured artifacts (e.g., JSON, NetCDF, or images referenced by STAC).  
- Be referenced via `kfm:explainability:*` fields in metadata where applicable.  
- Respect CARE and geoprivacy rules (no leaking sensitive patterns).

---

## 🌐 STAC, DCAT & PROV Alignment

AI pipelines must align with KFM metadata and provenance profiles:

- **STAC**
  - Use Collections for model outputs (e.g., gridded predictions, feature maps).  
  - Treat model outputs as assets with media types, checksums, and roles.  
  - Embed AI-related metadata (model ID, feature description, explainability references) in `properties` or extensions.

- **DCAT**
  - Register AI-generated datasets as `dcat:Dataset` with:
    - `dct:title`, `dct:description`, `dct:license`, `dct:creator`.  
    - Links to distributions (raw predictions, summaries, derived products).  
    - Versioning that references model and training data versions.

- **PROV-O**
  - Represent:
    - Training runs as `prov:Activity`.  
    - Datasets and models as `prov:Entity`.  
    - Pipelines, orchestrators, and maintainers as `prov:Agent`.  
  - Use `prov:wasGeneratedBy`, `prov:used`, and `prov:wasDerivedFrom` to trace:
    - Models from training data.  
    - Predictions from models + inputs.  

- **OpenLineage**
  - Capture runtime job/run/dataset events for training and inference; must be convertible to PROV-O bundles in alignment with lineage standards.

---

## 🧪 Validation & CI/CD

AI pipelines must integrate tightly with CI/CD and validation:

### 1. Testing requirements

- **Unit tests** for core model-wrapping logic and feature preprocessing.  
- **Integration tests** for DAG orchestration, config loading, and artifact generation.  
- **Golden-record tests** ensuring outputs remain stable for fixed seeds and inputs.  
- **Deterministic regression tests** for critical paths.  
- **Governance rule tests**:
  - CARE, FAIR, CRS, STAC/DCAT contracts.  
  - Sovereignty-policy checks where datasets involve Indigenous or heritage content.

### 2. CI/CD hooks

Representative checks:

- Schema validation for AI pipeline configs.  
- OpenLineage presence and structure (lineage audit).  
- Energy and carbon telemetry compliance.  
- Security checks for model-serving dependencies.  

CI **must** block:

- Pipelines missing required metadata or lineage.  
- Non-deterministic behavior where determinism is required.  
- Violations of geoprivacy, sovereignty, or CARE rules.

### 3. Telemetry & observability

Telemetry for AI pipelines includes:

- Energy and carbon metrics (as per `energy_schema` and `carbon_schema`).  
- Latency, throughput, error rates.  
- Dataset and model version identifiers.  
- Drift detection metrics and alert flags.  

Aggregated telemetry for this layer is recorded at:

- `releases/v11.2.4/ai-pipelines-telemetry.json` (see `telemetry_ref`).

---

## 🧠 Story Node & Focus Mode Integration

AI pipelines are central to **Story Nodes** and **Focus Mode**:

- Story Nodes:
  - May use AI-generated summaries and contextual narratives.  
  - Must always reference underlying datasets, models, and lineage.  
  - Use AI pipelines for term extraction, entity linking, and narrative assembly.

- Focus Mode:
  - Uses AI reasoning engines to fuse STAC, graph, and narrative context.  
  - Relies on AI-generated overlays (e.g., explanation cards, “why this feature matters”).  
  - Enforces AI transform permissions:
    - Allowed: summarization, highlighting, a11y adaptations.  
    - Prohibited: speculative invention of datasets or events.

AI-driven narrative content remains **derived** from factual data and documents; normative meaning and governance remain anchored in KFM standards and ontologies.

---

## ⚖ FAIR+CARE & Governance

AI pipelines must operationalize FAIR+CARE:

- **FAIR**
  - Training and inference datasets must be identifiable, cataloged, and licensed.  
  - Model outputs must be discoverable and interoperable via STAC/DCAT.  
  - Provenance (OpenLineage + PROV-O) must allow independent verification.

- **CARE**
  - Training data usage must respect community rights and expectations.  
  - Models must not:
    - Infer sensitive attributes (e.g., tribal identity) without explicit governance.  
    - Expose locations or patterns of protected sites.  
  - AI decisions impacting sensitive topics must be reviewable and explainable.  

Governance hooks:

- Governance references (e.g., `governance_ref`, `ethics_ref`, `sovereignty_policy`) are **normative**.  
- AI-related incidents (e.g., bias findings, drift affecting sovereignty-sensitive content) must:
  - Be recorded via lineage and telemetry.  
  - Trigger governance review and potential model retraining or rollback.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                                  |
|--------:|------------|-------------------|----------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Updated to KFM-MDP v11.2.4; aligned directory layout; integrated queue, lineage, and validation standards. |
| v11.2.2 | 2025-11-28 | Superseded        | Added agentic-schema-drift architecture; expanded AI pipeline classes and telemetry.   |
| v11.0.0 | 2025-11-22 | Superseded        | Initial AI Pipeline Layer specification for KFM v11.                                   |

---

<div align="center">

🧠 **KFM v11.2.4 — AI Pipeline Layer**  
Governed AI · Deterministic Pipelines · FAIR+CARE-Aligned Semantic Intelligence  

<br/>

[📘 Docs Root](../..) · [🛠 Pipelines Index](../README.md) · [🧬 Lineage Standard](../../standards/lineage/openlineage-integration.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [🔐 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md)

</div>