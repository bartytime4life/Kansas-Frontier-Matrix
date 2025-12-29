---
title: "MCP Workspace — Runs, Experiments, Model Cards & SOPs"
path: "mcp/README.md"
version: "v1.1.2"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:mcp:readme:v1.1.2"
semantic_document_id: "kfm-mcp-readme-v1.1.2"
event_source_id: "ledger:kfm:doc:mcp:readme:v1.1.2"
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

# MCP Workspace — Runs, Experiments, Model Cards & SOPs

## 📘 Overview

### Purpose

`mcp/` is the **documentation-first workspace** for experiments, model documentation, and repeatable procedures (SOPs) that support KFM’s evidence-first, contract-first pipeline.

Use this directory to capture:

- **How** results were produced (methods, configs, run context, environments)
- **What** was produced (outputs + metrics + links to canonical artifacts)
- **Why** the work matters (objectives, decisions, tradeoffs)
- **What can go wrong** (limitations, failure modes, governance constraints)

**Non-negotiable ordering (canonical pipeline):**  
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

Expanded view (for catalog + lineage boundary artifacts):

- ETL → **STAC** (Collections + Items) → **DCAT** (dataset records) → **PROV** (run/activity bundles)  
- → Neo4j graph → APIs → UI → Story Nodes → Focus Mode

**Do not store canonical datasets or production code in `mcp/`.**  
Prefer “pointer, don’t duplicate”:

- Store **data** under `data/**` (raw/work/processed + STAC/DCAT/PROV outputs).
- Store **pipeline code** under `src/**`.
- Store **UI code** under `web/**`.
- Store **Story Nodes** under `docs/reports/story_nodes/**`.

### Quickstart

When starting new work that might affect downstream evidence:

1. Create a **run manifest** under `mcp/runs/` (even for “small” runs).
2. Put the write-up under `mcp/experiments/**` (or update an existing experiment report).
3. Save any evidence outputs under `data/processed/<domain>/...` (never under `mcp/`).
4. Update catalogs as applicable:
   - STAC under `data/stac/**`
   - DCAT under `data/catalog/dcat/**`
   - PROV under `data/prov/**`
5. If the work influences narrative:
   - Link evidence IDs into a Story Node (`docs/reports/story_nodes/**`)
   - Ensure Focus Mode only consumes provenance-linked content
6. Run validation gates (Markdown + schemas + link checks + contract tests as applicable).

### Scope

| In Scope | Out of Scope |
|---|---|
| Experiment reports (questions, methods, results, limitations) | Raw source data snapshots (belongs in `data/raw/<domain>/`) |
| Run manifests/logs that **point to** canonical artifacts | Canonical processed datasets (belongs in `data/processed/<domain>/`) |
| Model cards for models used by KFM | Graph migrations / ontology changes (belongs in `src/graph/**` + governed docs) |
| SOPs for recurring workflows | API contracts (belongs in `src/server/**` + contract templates) |
| Prototyping notes and evaluation summaries | UI implementations (belongs in `web/**`) |

### Audience

- Primary: contributors running AI/analytics workflows and generating evidence products
- Secondary: maintainers performing governance/audit review; curators validating evidence before narrative publication

### Definitions

- Link: `docs/glossary.md` *(if present; otherwise: not confirmed in repo)*

Terms used in this doc:

- **MCP workspace**: the controlled, versioned “lab notebook” layer for experiments, run context, and model documentation.
- **Run manifest**: a structured record of *one execution* (inputs, code ref, outputs, metrics, and provenance pointers).
- **Experiment report**: a narrative + technical write-up that frames an objective, method, results, and limitations.
- **Evidence artifact**: a downstream-consumable output surfaced via STAC/DCAT/PROV and then through APIs.
- **Model card**: a structured description of intended use, training/eval data, performance, risks, and limitations.
- **SOP**: a step-by-step repeatable process with prerequisites, procedure, expected outcomes, and troubleshooting notes.
- **Contract-first**: schemas + API contracts are first-class artifacts; breaking changes require versioning + compatibility tests.
- **Deterministic pipeline**: idempotent, config-driven transforms with logged inputs/outputs and stable IDs.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | System map and non-negotiable ordering |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Required governed doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative artifacts must be provenance-linked |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Extends REST/GraphQL contracts at the boundary |
| JSON schema roots (STAC/DCAT/PROV/story/ui/telemetry) | `schemas/**` | Schema maintainers | Schema validation for machine-validated artifacts *(if present)* |
| Standards (profiles + repo rules) | `docs/standards/**` | Maintainers | STAC/DCAT/PROV profiles; markdown/repo standards *(if present)* |
| v13 blueprint docs (draft references) | `docs/architecture/**` | Architecture | Future alignment docs *(if present)* |

### Definition of done

- [x] Front-matter complete and `path` matches file location
- [x] Directory responsibilities + placement rules documented
- [x] Expected `mcp/` structure provided
- [x] Validation steps listed and repeatable
- [x] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Repo markdown lint / link checks executed (CI or local)
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `mcp/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows, security policies, automation |
| Data | `data/` | Domain-staged raw/work/processed + catalog outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (canonical evidence + lineage) |
| Documentation | `docs/` | Governed designs, guides, standards, reports |
| Templates | `docs/templates/` | Governed doc templates |
| Architecture | `docs/architecture/` | System design docs, blueprints, ADRs |
| Graph | `src/graph/` | Ontology bindings, graph build, ingest scripts, constraints |
| Pipelines | `src/pipelines/` | Deterministic transforms and catalog builders |
| API boundary | `src/server/` | Contracts, redaction, access controls, query services |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Schemas | `schemas/` | JSON Schemas, telemetry schemas, contract validation |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Ops scripts and developer utilities |
| Releases | `releases/` | Release manifests, snapshots, bundles *(if present)* |

### Expected file tree for this sub-area

~~~text
📁 mcp/
├── 📄 README.md
├── 📁 runs/
│   └── (run manifests, run logs, pointers to canonical outputs)
├── 📁 experiments/
│   └── (experiment reports + optional prototype notebooks used for analysis)
├── 📁 model_cards/
│   └── (model cards for any AI/ML model used by KFM workflows)
└── 📁 sops/
    └── (standard operating procedures for recurring workflows)
~~~

> Note: If prototype code becomes part of the production pipeline, move it into `src/` and link to it from `mcp/` rather than duplicating it.

---

## 🧭 Context

### Background

KFM is intentionally staged to keep the system **modular, testable, and auditable**. The canonical ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

`mcp/` exists to ensure experimentation and AI usage remain transparent and reproducible—especially when experimental outputs become evidence products that influence the graph and narrative.

### Assumptions

- Contributors store large artifacts (datasets, derived evidence) under `data/**`, not under `mcp/**`.
- `mcp/**` documents link to canonical artifact identifiers (STAC/DCAT/PROV IDs, graph entity IDs, releases) wherever applicable.
- Not all subfolders may exist yet; this README defines the intended canonical structure.

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes → Focus Mode**
- **No UI direct-to-graph reads** (all graph access via the API boundary).
- **No unsourced narrative** in published Story Nodes or Focus Mode contexts.
- Do not store secrets, tokens, credentials, or private keys in `mcp/**`.
- Treat `mcp/**` as public by default unless governance explicitly marks an artifact restricted.
- Prefer deterministic, reproducible runs (stable IDs, logged inputs/outputs, captured parameters).
- Any layout/structure change to staging paths or subsystem homes is a governed change (do not “mix layouts”).

### “Extension matrix”

Use this table to anticipate what else must change when MCP artifacts create new evidence:

| Extension | Data | Catalog | Graph | API | UI | Story/Focus | Telemetry |
|---|---|---|---|---|---|---|---|
| New dataset | ✓ | ✓ | optional | optional | optional | optional | optional |
| New analysis product (evidence artifact) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| New narrative node type | optional | optional | ✓ | ✓ | ✓ | ✓ | ✓ |
| New security/governance gate | — | — | — | — | — | — | ✓ |

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize a governed `run_manifest` schema (YAML/JSON) for `mcp/runs/`? | TBD | TBD |
| Do we add an experiment report template under `mcp/experiments/`? | TBD | TBD |
| Do we adopt a formal model card format (HF-style + KFM extensions)? | TBD | TBD |

### Future extensions

- Automated linking from `mcp/runs/**` → PROV bundles in `data/prov/**`
- CI checks: every model card must reference evaluation evidence
- Optional metrics tracking (e.g., entity extraction accuracy over time)

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  MCP["mcp/<br/>runs + experiments + model cards + SOPs"] -->|docs + pointers| DATA["data/<br/>raw/work/processed"]
  DATA --> STAC["data/stac/**"]
  DATA --> DCAT["data/catalog/dcat/**"]
  DATA --> PROV["data/prov/**"]

  STAC --> GRAPH["src/graph/** (Neo4j ingest)"]
  DCAT --> GRAPH
  PROV --> GRAPH

  GRAPH --> API["src/server/** (API boundary)"]
  API --> UI["web/** (React/Map UI)"]
  UI --> SN["docs/reports/story_nodes/**"]
  SN --> FM["Focus Mode<br/>provenance-linked only"]
~~~

### Optional sequence diagram for Focus Mode contract boundary

~~~mermaid
sequenceDiagram
  participant UI as UI (web)
  participant API as API boundary
  participant Graph as Graph layer (Neo4j)

  UI->>API: focusContext(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle (entities + evidence ids)
  API-->>UI: narrative context + citations + flags
~~~

---

## 📦 Data & Metadata

### Data lifecycle

Canonical staging is:

- Raw snapshots: `data/raw/<domain>/...`
- Working intermediates: `data/work/<domain>/...`
- Published/derived outputs: `data/processed/<domain>/...`
- Catalog outputs:
  - STAC: `data/stac/**`
  - DCAT: `data/catalog/dcat/**`
  - PROV: `data/prov/**`

`mcp/` should generally reference these locations, not replace them.

### Domain expansion pattern

When adding a new domain, prefer:

- Data: `data/raw/<domain>/`, `data/work/<domain>/`, `data/processed/<domain>/`
- Domain notes/runbooks: `data/<domain>/README.md` *(if present; choose one canonical home and link)*

If a different structure is introduced (e.g., domain-first under `data/<domain>/raw`), treat it as a governed change and update docs consistently.

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Evidence products (processed data) | files (varies) | `data/processed/<domain>/` | domain validators + schema checks |
| STAC/DCAT/PROV artifacts | JSON / JSON-LD (varies) | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | schema validation in `schemas/**` *(if present)* |
| Graph entity identifiers | strings | API/Graph outputs | contract tests (API) |
| Prior model versions + eval outputs | refs/pointers | releases or `data/**` | reproducibility checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Experiment report | Markdown | `mcp/experiments/**` | Universal doc conventions + governed headings |
| Run manifest/log | YAML/JSON/Markdown | `mcp/runs/**` | schema in `schemas/**` *(if adopted)* |
| Model card | Markdown (+ optional JSON) | `mcp/model_cards/**` | model card format (TBD) |
| SOP | Markdown | `mcp/sops/**` | SOP conventions (purpose, prereqs, steps, expected outcomes, troubleshooting) |

### Sensitivity & redaction

- Do not publish exact coordinates or culturally sensitive locations in `mcp/**` unless governance explicitly allows it.
- If an experiment touches protected data, restrict outputs at the canonical data layer and ensure `mcp/**` only stores redacted pointers.

### Quality signals

- Every experiment report includes:
  - a clear question/objective,
  - inputs and environment assumptions,
  - linkable output pointers,
  - known limitations and failure modes.
- Every model card links to evaluation evidence and states intended use + non-use.
- No orphan references (paths or IDs that do not resolve).

---

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

When a run produces a new dataset or evidence artifact intended to travel downstream:

- **STAC**: create/update Collections + Items under `data/stac/**`
- **DCAT**: create/update dataset records under `data/catalog/dcat/**` *(if publication/discovery is intended)*
- **PROV**: create/update a run/activity bundle under `data/prov/**`

`mcp/**` should reference IDs/pointers, not duplicate catalog payloads.

### Versioning expectations

- New versions link predecessor/successor (at least via PROV and/or catalog metadata).
- If the graph mirrors dataset/version lineage, graph nodes should reference catalog/provenance IDs.
- When a model is updated, update its model card with a changelog entry and link to evaluation evidence.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| MCP workspace (`mcp/`) | Experiment record + model documentation + SOPs | Markdown docs + manifests + pointers |
| ETL / pipelines | Ingest + normalize | configs + deterministic transforms |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j ingest + semantics | import fixtures + API boundary |
| APIs | Serve contracts; enforce redaction | REST/GraphQL |
| UI | Map + narrative exploration | API calls |
| Story Nodes | Curated narrative | provenance-linked content |
| Focus Mode | Contextual synthesis | provenance-linked only |

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | semver + changelog |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | semver + changelog |
| API contracts | `src/server/**` | semver + contract tests |
| Schemas | `schemas/**` | semver + schema validation |
| MCP artifacts | `mcp/**` | version per artifact + provenance pointers |

### Extension points checklist

- [ ] Evidence artifact saved under `data/processed/<domain>/...`
- [ ] STAC item/collection created or updated (`data/stac/**`)
- [ ] DCAT dataset updated *(if applicable)* (`data/catalog/dcat/**`)
- [ ] PROV bundle created or updated (`data/prov/**`)
- [ ] Graph ingest updated *(if applicable)* (`src/graph/**`)
- [ ] API contract / endpoint updated *(if applicable)* (`src/server/**`)
- [ ] UI surfaced via API (no direct graph reads) *(if applicable)* (`web/**`)
- [ ] Story Node references evidence IDs *(if applicable)* (`docs/reports/story_nodes/**`)
- [ ] Governance review completed *(if required)*

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Story Nodes must carry provenance annotations and connect to graph entities.
- Published narrative must separate:
  - **fact** (supported by evidence IDs),
  - **inference** (supported but interpretive),
  - **hypothesis** (needs more evidence; not publishable as fact).

### How MCP artifacts become publishable narrative

Use `mcp/` to incubate and validate evidence before it becomes narrative:

1. Experiment or evaluation happens (documented in `mcp/experiments/**`)
2. Evidence products land in `data/processed/<domain>/`
3. Catalog artifacts updated: `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`
4. Graph ingest fixture updated (if new entities/relationships are introduced)
5. API contract surfaces evidence with citations
6. Story Nodes reference evidence IDs and are validated before publishing
7. Focus Mode renders provenance-linked context only

### Focus Mode rule

- Focus Mode should never invent evidence: all claims must map to an evidence identifier.
- Any predictive content must be opt-in and carry uncertainty/confidence metadata.

### Minimal citation bundle

When MCP work influences Story Nodes, include at least:

- STAC item/collection IDs (or file pointers)
- DCAT dataset identifiers (if applicable)
- PROV activity/bundle reference
- API endpoint or response contract reference (where evidence is surfaced)

---

## 🧪 Validation & CI/CD

### Minimum CI gates

Recommended minimum gates (CI or local):

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation (if applicable):
  - STAC/DCAT/PROV
  - story node schemas *(if present)*
  - telemetry schemas *(if present)*
  - UI layer registry schemas *(if present)*
- Graph integrity tests *(if applicable)* (constraints, expected labels/edges)
- API contract tests *(if applicable)* (OpenAPI/GraphQL schema + resolver tests)
- Security + sovereignty scanning gates *(as applicable)*:
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)
- Release hygiene *(if applicable / used in repo)*:
  - SBOM generation
  - provenance attestations (e.g., SLSA)

### Reproduction

For any run that could influence downstream evidence, the run manifest should record the exact `command` and `code_ref` needed to reproduce.

~~~bash
# Example (placeholder): reproduce a run from its manifest.
# 1) Checkout the recorded commit
git checkout <git-sha>

# 2) Execute the recorded command(s)
# (copy/paste from: mcp/runs/<run_id>.yml -> command)
TBD

# 3) Validate produced artifacts (schemas + link checks)
TBD
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` (dataset_id, sensitivity, classification) | catalog/governance | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |
| `redaction_applied` (method, fields_removed, geometry_generalization) | API/catalog | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |
| `promotion_blocked` (reason, scan_results_ref) | CI/publishing gate | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |
| `catalog_published` (scope, counts, validation_status) | catalog pipeline | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |
| `focus_mode_redaction_notice_shown` (layer_id, redaction_method) | UI | `docs/telemetry/` + `schemas/telemetry/` *(if present)* |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Flag for human review when MCP work includes:

- culturally sensitive knowledge or locations
- protected personal data
- new model behavior that affects narrative generation
- any change that alters redaction or provenance rules at the API boundary
- new sensitive layers or sovereignty-obligated content
- new external data sources (license/provenance review)
- new public-facing endpoints or layer interactions that could reveal sensitive locations
- any classification/sensitivity change or publication derived from restricted inputs

### CARE / sovereignty considerations

- Redaction/generalization must be documented and enforced:
  - in datasets (`data/processed/**`),
  - in catalogs (STAC/DCAT),
  - in API responses (redaction policies),
  - and in UI rendering (CARE gating).
- No output may be less restricted than any upstream input in its lineage.

### AI usage constraints

- AI may assist only within the allowed transforms in front-matter (`ai_transform_permissions`).
- AI must not:
  - generate governance/policy content, or
  - infer sensitive locations.
- Any AI-assisted experimental finding that could become narrative must be labeled as fact / inference / hypothesis and backed by evidence identifiers before publication.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.2 | 2025-12-29 | Aligned wording and section order to Universal template; clarified canonical pipeline phrasing; added Quickstart + subsystem contracts; tightened domain staging notes | KFM maintainers |
| v1.1.1 | 2025-12-28 | Tightened alignment to Universal template headings; corrected canonical data staging paths; added reproduction + telemetry table; expanded governance/CI gates | KFM maintainers |
| v1.1.0 | 2025-12-27 | Reworked to fully align with Universal template sections + Story/Focus integration + run-manifest conventions | KFM maintainers |
| v1.0.0 | 2025-12-22 | Initial `mcp/` README establishing structure and conventions | KFM maintainers |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`
- Glossary: `docs/glossary.md` *(if present; not confirmed in repo)*
---