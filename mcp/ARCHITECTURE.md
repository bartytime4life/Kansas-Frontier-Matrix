---
title: "MCP Architecture"
path: "mcp/ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "Architecture"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:mcp:architecture:v1.0.0"
semantic_document_id: "kfm-mcp-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:mcp:architecture:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# MCP Architecture

## 📘 Overview

### Purpose
This document defines the architecture and governed practices for KFM’s **MCP space** (`mcp/`): where **experiments**, **model cards**, and **SOPs** live, and how MCP outputs are promoted into the canonical KFM pipeline (**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**).

It is intended to make MCP work reproducible, auditable, and safe to surface in Story Nodes / Focus Mode.

### Scope
| In Scope | Out of Scope |
|---|---|
| Documentation + artifact conventions for `mcp/` (experiments, model cards, SOPs) | Implementation details of any specific ML framework (e.g., MLflow, DVC) |
| How MCP artifacts reference datasets, catalogs, graph entities, and UI views | Running instructions for every pipeline (belongs in dedicated SOPs) |
| Promotion rules for moving “experimental” outputs into `data/processed` + catalogs | Governance policy text itself (lives under `docs/governance/`) |

### Audience
- Primary: Contributors running analysis/AI experiments and writing governed artifacts for KFM.
- Secondary: Maintainers reviewing promotions into catalog/graph/API/UI.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **MCP**: In-repo documentation and experiment space (experiments, model cards, SOPs) under `mcp/`.
  - **Experiment**: A planned investigation described in a governed experiment report.
  - **Run**: A single execution of an experiment (one parameterization + dataset version set).
  - **Promotion**: Moving an output from “experimental” to “product” by publishing through catalogs (STAC/DCAT/PROV) and graph/API.
  - **Evidence artifact**: A derived dataset, metric summary, or analytic output that can be referenced in Story Nodes.
  - **Provenance**: Traceability links back to sources and processing lineage (e.g., PROV records).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline order + invariants |
| Governed doc templates | `docs/templates/` | Maintainers | Universal doc, story node, API contract templates |
| MCP experiments | `mcp/experiments/` | Contributors | Experiment plans + reports |
| MCP run logs/artifacts | `mcp/runs/` | Contributors | Repeatable run manifests + outputs (non-product) |
| MCP model cards | `mcp/model_cards/` | Contributors | Model documentation |
| MCP SOPs | `mcp/sops/` | Contributors | Step-by-step repeatable procedures |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Maintainers | Only for promoted outputs |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] MCP responsibilities and boundaries are clear (what belongs in `mcp/` vs `data/`)
- [ ] Promotion workflow is described (experimental → catalog/graph/API/UI)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `mcp/ARCHITECTURE.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| MCP root | `mcp/` | Experiment docs, model cards, SOPs, run artifacts |
| ETL pipelines | `src/pipelines/` | Code that creates derived artifacts for cataloging/graph ingest |
| STAC outputs | `data/stac/` | Promoted geospatial assets indexed via STAC |
| DCAT outputs | `data/catalog/dcat/` | Promoted dataset + distribution metadata |
| PROV outputs | `data/prov/` | Lineage records for promoted artifacts |
| Graph ingest + ontology | `src/graph/` | Neo4j ingest and schema/ontology glue |
| API layer | `src/api/` | Contracts + endpoints serving the UI |
| UI | `src/web/` | React + MapLibre UI (does not query graph directly) |
| Story nodes | `docs/story_nodes/` | Governed narratives (if present) |

### Expected file tree for this sub-area
~~~text
📁 mcp/
├── 📄 ARCHITECTURE.md
├── 📁 experiments/
│   ├── 📄 README.md
│   └── 📁 exp_<experiment_id>/
│       ├── 📄 EXPERIMENT.md
│       └── 📁 runs/
│           └── 📁 run_<run_id>/
│               ├── 📄 RUN_MANIFEST.yml
│               ├── 📄 METRICS.json
│               └── 📁 artifacts/
├── 📁 model_cards/
│   └── 📄 <model_id>.md
└── 📁 sops/
    └── 📄 <sop_name>.md
~~~

> Note: the exact substructure under `mcp/` is governed by this document; if existing repo structure differs, update this doc or add a migration plan.

## 🧭 Context

### Background
KFM’s architecture is modular and contract-driven: ETL produces standardized catalogs (STAC/DCAT/PROV), which feed the Neo4j knowledge graph, which is accessed only through APIs, which power the React/MapLibre UI, story nodes, and Focus Mode.

The `mcp/` area provides a safe, auditable place to develop and evaluate experimental analyses and AI components (e.g., model prototypes, narrative drafts) without directly changing core datasets or public-facing outputs.

### Goals
- Make experimental work reproducible (same inputs + same code → same outputs).
- Keep experimental outputs from leaking into Story/Focus without provenance and review.
- Provide a clear path to promote validated results into catalogs/graph/API/UI.

### Non-goals
- Defining a specific ML framework or deployment topology (separate docs).
- Replacing the canonical catalog/graph/API pipeline with an experiment tracker.

### Architectural invariants
- **Canonical pipeline order is preserved**: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary**: UI never reads Neo4j directly; all graph access occurs via the API layer.
- **No hallucinated/unsourced narrative**: Story Nodes and Focus Mode content must be evidence-led and provenance-backed; AI-generated or AI-inferred content must be clearly labeled and opt-in.
- **Separation of concerns**: Derived datasets intended for use by the platform belong under `data/processed/` and catalogs; MCP stores run artifacts and documentation, plus pointers to promoted outputs.

## 🗺️ Diagrams

### System / dataflow diagram (MCP in context)
~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines/] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>Neo4j]
  C --> D[API Layer<br/>src/api/]
  D --> E[UI<br/>React + MapLibre]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph MCP[mcp/<br/>Experiments • Model Cards • SOPs]
    M1[Experiment Reports]
    M2[Run Artifacts]
    M3[Model Cards]
    M4[SOPs]
  end

  M1 -->|validated outputs promoted via ETL| A
  M2 -->|links to artifacts + metrics| M1
  M3 -->|document model behavior + limits| D
  M4 -->|defines repeatable procedures| A
~~~

### Promotion sequence (experimental → product)
~~~mermaid
sequenceDiagram
  participant Contributor
  participant MCP as mcp/ (experiment docs + run artifacts)
  participant ETL as ETL (src/pipelines/)
  participant Catalog as STAC/DCAT/PROV (data/*)
  participant Graph as Neo4j Graph
  participant API as API Layer
  participant UI as UI / Story / Focus

  Contributor->>MCP: Write / update experiment report
  Contributor->>ETL: Run pipeline with declared inputs + params
  ETL-->>MCP: Emit run artifacts (logs, metrics, summaries)
  ETL->>Catalog: (If promoted) Write STAC/DCAT/PROV outputs
  Catalog->>Graph: (If promoted) Graph ingest references catalogs
  Graph->>API: Query results (with provenance refs)
  API->>UI: Contracted payloads (with provenance + uncertainty)
~~~

## 📦 Data & Metadata

### MCP inputs (what must be referenced)
At minimum, each MCP experiment/run SHOULD record:
- Dataset identifiers and versions (e.g., STAC item/collection IDs, DCAT dataset IDs, or stable dataset paths).
- Code provenance (commit SHA, branch/tag, or release ID).
- Configuration / parameters (including random seeds if applicable).
- Execution context (runtime environment summary).

### MCP outputs (what may be produced)
- Experiment report updates (interpretation, limitations, next steps).
- Run manifests and metrics summaries.
- Draft narrative elements or evidence summaries (NOT directly user-facing until promoted).
- Prototype model artifacts (if applicable), documented via model cards.

### Promotion criteria (high level)
A candidate output may be promoted when:
- It is reproducible from declared inputs.
- It has complete lineage and metadata (PROV + catalog entries as applicable).
- It passes required validation checks (see Validation section).
- It passes governance review if sensitive or public-facing.

## 🌐 STAC / DCAT / PROV alignment

### When to use which
- **STAC**: for geospatial assets / layers (rasters, vectors, tiles, map derivatives) that the UI or external tools will index and discover.
- **DCAT**: for dataset-level cataloging (what the dataset is, who publishes it, distributions, licenses).
- **PROV**: for transformation lineage (how raw inputs were processed into outputs; who/what/when).

### Linking MCP → catalogs
MCP artifacts SHOULD link to the IDs of promoted assets/datasets/lineage:
- `stac_item_id` / `stac_collection_id` (if geospatial outputs)
- `dcat_dataset_id` (if dataset published)
- `prov_activity_id` / `prov_entity_id` (for lineage)

## 🧱 Architecture

### Responsibilities (what MCP owns)
- Governed documentation of experiments, assumptions, limitations, and results.
- Run-level traceability for experimental work (inputs → config → outputs).
- Model cards for any ML/NLP components used to produce evidence or drafts.
- SOPs that make recurring procedures repeatable and reviewable.

### Responsibilities (what MCP does NOT own)
- Serving data directly to the UI (that is the API layer’s job).
- Long-term storage of promoted datasets (use `data/processed/` + catalogs instead).
- Defining or bypassing governance rules for sensitive data.

### Promotion workflow (recommended)
1. **Experiment**: Author/update an experiment report under `mcp/experiments/`.
2. **Run**: Record a run manifest + metrics under `mcp/runs/` (or `mcp/experiments/.../runs/`).
3. **Validate**: Run schema checks (STAC/DCAT/PROV where relevant) and QA checks.
4. **Promote**: If the output is intended for platform use, publish it under `data/processed/` and register in STAC/DCAT/PROV.
5. **Ingest**: Update graph ingest to reference the cataloged outputs (not the MCP run folder).
6. **Surface**: UI/Story/Focus consumes through the API layer with provenance links.

## 🔌 Interfaces / Contracts

### Document templates
- Default governed docs: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Nodes / Focus narratives: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API changes: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### Contract boundary reminders
- MCP outputs intended for UI MUST be accessible via API contracts.
- Graph structure changes MUST be reflected in ontology + ingest + API contracts (no UI-side schema guessing).

## 🧠 Story Node & Focus Mode Integration

### Evidence-first rule
Story Nodes and Focus Mode MUST only present narrative content that is provenance-backed. If any AI-generated or AI-inferred content is included, it MUST:
- be explicitly labeled as AI-generated/inferred
- include uncertainty/confidence metadata
- be opt-in (not forced on the user)

### Referencing MCP artifacts from stories
- Story Nodes SHOULD reference MCP run IDs and/or experiment IDs as **supporting evidence**, but MUST ultimately link to the promoted dataset/document IDs exposed via catalogs/graph/API.

## 📜 Governance

### Sensitivity and sovereignty
- If an experiment touches sensitive data (e.g., culturally restricted sites, private locations, protected ecological resources), it requires governance review before promotion.
- Follow `docs/governance/*` for classifications, redaction/generalization requirements, and approval workflows.

### Review triggers (examples)
- New dataset ingestion
- New AI-driven narrative generation
- New public API surface area
- Any change that alters sensitivity classification or redaction behavior

## ✅ Validation

### Minimum validation steps for MCP artifacts
- [ ] Markdown front-matter validation (keys, types, required fields)
- [ ] Link integrity checks (no broken internal links)
- [ ] If promoting outputs: STAC validation + collection/item integrity checks
- [ ] If promoting outputs: DCAT validation (shape/schema)
- [ ] If promoting outputs: PROV validation (activity/entity/agent linkage)
- [ ] Reproducibility check: inputs + code ref + config captured
- [ ] Governance check when sensitive/public-facing

## 📎 Appendix

### A. Minimal run manifest (example)
~~~yaml
run_id: "run_YYYYMMDD_hhmmss_<shortid>"
experiment_id: "exp_<experiment_id>"
created_at: "YYYY-MM-DD"
code:
  commit_sha: "<git-sha>"
inputs:
  datasets:
    - id: "<dataset-id-or-path>"
parameters:
  seed: 1234
outputs:
  artifacts_path: "mcp/runs/<run_id>/artifacts/"
notes: "TBD"
~~~

### B. Not confirmed in repo
The following are intentionally left as TBD until confirmed/standardized:
- Exact experiment/run naming conventions and ID registry approach
- Whether `mcp/runs/` vs per-experiment `runs/` is the preferred canonical layout
- Any automated promotion tooling or CI gates beyond basic lint/schema checks
- A formal schema for run manifests and metrics files (JSON Schema/YAML spec)