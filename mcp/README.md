---
title: "MCP Workspace — Runs, Experiments, Model Cards & SOPs"
path: "mcp/README.md"
version: "v1.1.1"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:mcp:readme:v1.1.1"
semantic_document_id: "kfm-mcp-readme-v1.1.1"
event_source_id: "ledger:kfm:doc:mcp:readme:v1.1.1"
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

`mcp/` is the **documentation-first workspace** for experiments, model documentation, and repeatable procedures that support KFM’s evidence-first pipeline.

Use this directory to capture:

- **How** results were produced (methods, configs, run context)
- **What** was produced (outputs + metrics + links to canonical artifacts)
- **Why** the work matters (objectives, decisions, tradeoffs)
- **What can go wrong** (limitations, failure modes, governance constraints)

**Non-negotiable ordering (canonical pipeline):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

**Do not store canonical datasets or production code in `mcp/`.**  
Prefer “pointer, don’t duplicate”:

- Store **data** under `data/**` (raw/work/processed + STAC/DCAT/PROV outputs).
- Store **pipeline code** under `src/**`.
- Store **UI code** under `web/**`.
- Store **Story Nodes** under `docs/reports/story_nodes/**`.

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

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(if present; not confirmed in repo)*

- Terms used in this doc:
  - **MCP workspace**: the controlled, versioned “lab notebook” layer for experiments, run context, and model documentation.
  - **Run manifest**: a structured record of *one execution* (inputs, code ref, outputs, metrics, and provenance pointers).
  - **Experiment report**: a narrative + technical write-up that frames an objective, method, results, and limitations.
  - **Evidence artifact**: a downstream-consumable output surfaced via STAC/DCAT/PROV and then through APIs.
  - **Model card**: a structured description of intended use, training/eval data, performance, risks, and limitations.
  - **SOP**: a step-by-step repeatable process with prerequisites, procedure, expected outcomes, and troubleshooting notes.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | System map and non-negotiable ordering |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Required governed doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative artifacts must be provenance-linked |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Extends REST/GraphQL contracts at the boundary |
| STAC/DCAT/PROV profiles | `docs/standards/` | Data/catalog maintainers | Validate catalog + provenance compliance *(if present)* |
| v13 redesign blueprint (draft reference) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home” alignment *(if present)* |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done (for this document)

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

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Domain-staged raw/work/processed data; domain READMEs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (canonical evidence + lineage) |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import fixtures |
| Pipelines | `src/pipelines/` | Deterministic transforms and catalog builders |
| API boundary | `src/server/` | Contracts, redaction, access controls, query services |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Documentation | `docs/` | Governed designs, guides, standards, reports |
| Schemas | `schemas/` | JSON Schemas, telemetry schemas, contract validation |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Ops scripts and developer utilities |
| Releases | `releases/` | Release manifests, snapshots, bundles *(if present)* |

### Conventions

#### 1) “Pointer, don’t duplicate”

When `mcp/` needs to reference a dataset or evidence artifact, prefer:

- a **path pointer** into `data/**`, and/or
- a **catalog identifier** (STAC/DCAT), and/or
- a **provenance identifier** (PROV bundle / activity id), and/or
- a **graph entity id** (when applicable)

Avoid copying catalog payloads into `mcp/`. Keep one canonical home per subsystem.

#### 2) Stable IDs + file naming (recommended)

Use predictable file names to make audits and cross-links easy:

- **Run manifests:** `mcp/runs/run-YYYYMMDDTHHMMSSZ-<slug>.yml`  
- **Experiment reports:** `mcp/experiments/exp-YYYYMMDD-<slug>/README.md` *(or a single `.md` if small)*  
- **Model cards:** `mcp/model_cards/<model_id>__vX.Y.Z.md`  
- **SOPs:** `mcp/sops/sop-<slug>__vX.Y.Z.md`

When possible, reuse the same stable identifiers in:
- PROV activity IDs,
- STAC item IDs / collection IDs,
- DCAT dataset IDs,
- API references (endpoint + version).

#### 3) Recommended run manifest minimal fields (optional, but encouraged)

If you store run manifests as YAML/JSON, keep a minimal predictable shape:

~~~yaml
run_id: "run-YYYYMMDDTHHMMSSZ-<slug>"
run_kind: "etl|catalog|graph|evaluation|experiment|adhoc"
owners: ["<handle-or-role>"]
created_at: "YYYY-MM-DD"

code_ref:
  paths:
    - "src/pipelines/<...>"
  commit_sha: "<git-sha>"

command:
  - "TBD: exact invocation used to reproduce"

inputs:
  - kind: "dataset"
    path: "data/raw/<domain>/<...>"
    stac_item_id: "<optional>"

outputs:
  - kind: "evidence_artifact"
    path: "data/processed/<domain>/<...>"
  - kind: "prov_bundle"
    path: "data/prov/<...>"

catalog_refs:
  stac_item_ids: ["<optional>"]
  dcat_dataset_ids: ["<optional>"]

metrics:
  - name: "<metric_name>"
    value: 0

notes: "Short summary + known limitations"
~~~

If a formal schema is introduced later, prefer validating manifests against `schemas/**` and treat schema changes as governed.

---

## 🧭 Context

### Background

KFM is intentionally staged to keep the system **modular, testable, and auditable**. The canonical ordering is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

`mcp/` exists to ensure *experimentation and AI usage* remain transparent and reproducible—especially when experimental outputs become evidence products that influence downstream graph and narrative.

### Assumptions

- Contributors will store large artifacts (datasets, derived evidence) under `data/**`, not under `mcp/**`.
- `mcp/**` documents will link to canonical artifact identifiers (STAC/DCAT/PROV IDs, graph entity IDs, release manifests) wherever applicable.
- Not all subfolders may exist yet; this README defines the intended canonical structure.

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- **No UI direct-to-graph reads** (all graph access via the API boundary).
- **No unsourced narrative** in published Story Nodes or Focus Mode contexts.
- Do not store secrets, tokens, credentials, or private keys in `mcp/**`.
- Treat `mcp/**` as *public by default* unless governance explicitly marks an artifact restricted.
- Prefer deterministic, reproducible runs (stable IDs, logged inputs/outputs, captured parameters).

### “Extension Matrix” (how MCP work propagates)

Use this table to anticipate what else must change when MCP artifacts create new “evidence”:

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

  STAC --> GRAPH["src/graph/**"]
  DCAT --> GRAPH
  PROV --> GRAPH

  GRAPH --> API["src/server/**"]
  API --> UI["web/**"]
  UI --> SN["docs/reports/story_nodes/**"]
  SN --> FM["Focus Mode<br/>provenance-linked only"]
~~~

### Optional sequence diagram for Focus Mode contract boundary

~~~mermaid
sequenceDiagram
  participant UI as UI (web)
  participant API as API boundary
  participant Graph as Graph layer

  UI->>API: focusContext(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle (entities + evidence ids)
  API-->>UI: narrative context + citations + flags
~~~

---

## 📦 Data & Metadata

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
| Run manifest/log | YAML/JSON/Markdown | `mcp/runs/**` | recommended schema in `schemas/**` *(if adopted)* |
| Model card | Markdown (+ optional JSON) | `mcp/model_cards/**` | model card format (TBD) |
| SOP | Markdown | `mcp/sops/**` | SOP conventions (purpose, prereqs, steps, expected outcomes, troubleshooting) |

### Data lifecycle (required staging)

Canonical staging is:

- Raw snapshots: `data/raw/<domain>/...`
- Working intermediates: `data/work/<domain>/...`
- Published/derived outputs: `data/processed/<domain>/...`
- Catalog outputs:
  - STAC: `data/stac/**`
  - DCAT: `data/catalog/dcat/**`
  - PROV: `data/prov/**`

`mcp/` should generally **reference** these locations, not replace them.

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

### STAC

- When a run produces a new evidence product, ensure the *canonical artifact* is cataloged:
  - STAC Collections + Items under `data/stac/**`
- `mcp/**` should reference STAC IDs (not duplicate catalog content).

### DCAT

- For datasets/evidence products intended for publication or external interoperability:
  - DCAT dataset record under `data/catalog/dcat/**`
- `mcp/**` should capture attribution/license notes discovered during experimentation and link to the DCAT identifier.

### PROV-O

- Prefer every meaningful run to produce (or link to) a PROV activity bundle under `data/prov/**`.
- `mcp/runs/**` should contain pointers/IDs to PROV, rather than duplicating provenance payloads.

### Versioning

- Treat model cards, run manifests, and SOPs as versioned artifacts.
- When a model is updated, update its model card with a changelog entry and link to evaluation evidence.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| MCP workspace (`mcp/`) | Experiment record + model documentation + SOPs | Markdown docs + manifests + pointers |
| ETL / pipelines | Ingest + normalize | configs + deterministic transforms |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j ingest | import fixtures + API boundary |
| APIs | Serve contracts; enforce redaction | REST/GraphQL |
| UI | Map + narrative exploration | API calls |
| Story Nodes | Curated narrative | provenance-linked content |
| Focus Mode | Contextual synthesis | provenance-linked only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | semver + changelog |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | semver + changelog |
| API contracts | `src/server/**` | semver + contract tests |
| Schemas | `schemas/**` | semver + schema validation |
| MCP artifacts | `mcp/**` | version per artifact + provenance pointers |

### Extension points checklist (when MCP outputs become “evidence”)

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

## 🧩 Story Node & Focus Mode Integration

### How MCP artifacts become publishable narrative

Use `mcp/` to **incubate** and **validate** evidence before it becomes narrative:

1. Experiment or evaluation happens (documented in `mcp/experiments/**`)
2. Evidence products land in `data/processed/<domain>/`
3. Catalog artifacts updated: `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`
4. Graph ingest fixture updated (if new entities/relationships are introduced)
5. API contract surfaces evidence with citations
6. Story Nodes reference evidence IDs and are validated before publishing
7. Focus Mode renders provenance-linked context only

### Focus Mode guardrails

- Focus Mode should never “invent” evidence: all claims must map to an evidence identifier.
- If an MCP experiment suggests a narrative claim, it must be labeled as:
  - **fact** (directly supported by evidence id),
  - **inference** (supported but interpretive),
  - **hypothesis** (needs more evidence / not publishable).

### Minimal citation bundle (recommended)

When MCP work influences Story Nodes, include at least:

- STAC item/collection IDs (or file pointers)
- DCAT dataset identifiers (if applicable)
- PROV activity/bundle reference
- API endpoint or response contract reference (where evidence is surfaced)

---

## 🧪 Validation & CI/CD

### Validation steps

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
- Any AI-assisted experimental finding that could become narrative must be labeled as **fact / inference / hypothesis** and backed by evidence identifiers before publication.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.1 | 2025-12-28 | Tightened alignment to Universal template headings; corrected canonical data staging paths; added reproduction + telemetry table; expanded governance/CI gates | KFM maintainers |
| v1.1.0 | 2025-12-27 | Reworked to fully align with Universal template sections + Story/Focus integration + run-manifest conventions | KFM maintainers |
| v1.0.0 | 2025-12-22 | Initial `mcp/` README establishing structure and conventions | KFM maintainers |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- v13 Blueprint (draft reference): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(if present)*
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`
- Glossary: `docs/glossary.md` *(if present; not confirmed in repo)*
---
