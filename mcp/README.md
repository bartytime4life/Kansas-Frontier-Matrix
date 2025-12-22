---
title: "MCP — Model Cards & Prototypes"
path: "mcp/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:mcp:readme:v1.0.0"
semantic_document_id: "kfm-mcp-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:mcp:readme:v1.0.0"
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

# MCP Workspace

`mcp/` is the **documentation-first workspace** for experiments, model documentation, and repeatable procedures that support KFM’s evidence-first pipeline.

Use this directory to capture *how* results were produced (methods), *what* was produced (outputs + metrics), and *what the limitations are* (biases, known failure modes, governance constraints). Store **data outputs** under `data/**` and **code** under `src/**`; `mcp/**` is for the *research/ops record* of the work.

---

## 📘 Overview

### Purpose

- Provide a canonical home for:
  - **Experiment reports** (what was tried, why, results, and how to reproduce).
  - **Run manifests/logs** (what was executed, with input/output pointers).
  - **Model cards** (intended use, training data, limitations, evaluation, ethical considerations).
  - **SOPs** (repeatable procedures that keep work consistent across contributors).

### Scope

In scope:
- Documentation and metadata for AI/analysis workflows (including model evaluation and comparisons).
- Reproducibility artifacts that *point to* canonical data/catalog/provenance outputs.

Out of scope:
- Raw source data snapshots (belongs in `data/<domain>/raw/`).
- Processed datasets and derived evidence artifacts (belongs in `data/<domain>/processed/` and catalogs).
- API contracts (belongs at the API boundary), UI code, or graph migrations.

### Audience

- Contributors running AI or analytic workflows
- Maintainers performing governance/audit review
- Curators validating evidence before narrative publication

### Definition of done for this document

- [x] Front-matter complete and `path` matches file location
- [x] Directory responsibilities + placement rules documented
- [x] Expected `mcp/` tree provided
- [ ] Repo lint / markdown lint run (CI or local)
- [ ] Maintainer review

---

## 🗂 Directory Layout

### This document

- `path`: `mcp/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed domain data; catalog outputs by stage |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (canonical evidence + lineage) |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import fixtures |
| Pipelines | `src/pipelines/` | Deterministic transforms and catalog builders |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(if legacy)* | Contracts, redaction, access controls, query services |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Documentation | `docs/` | Governed designs, guides, reports, standards |
| MCP | `mcp/` | Experiments, model cards, SOPs (this area) |
| Schemas | `schemas/` | JSON Schemas, telemetry schemas, contract validation |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Ops scripts and developer utilities |

### Expected file tree for this sub-area

~~~text
📁 mcp/
├── 📄 README.md
├── 📁 runs/
│   └── (run manifests, run logs, pointers to outputs)
├── 📁 experiments/
│   └── (experiment reports, notebooks/scripts used for analysis)
├── 📁 model_cards/
│   └── (model cards for any AI model used by KFM)
└── 📁 sops/
    └── (standard operating procedures for recurring workflows)
~~~

---

## 🧭 Context

### Background

KFM’s pipeline is intentionally staged (ETL → catalogs → graph → API → UI → narratives) to keep the system modular, testable, and auditable. `mcp/` exists to make *experimentation and AI usage* transparent and reproducible—especially when AI outputs become “evidence products” that influence downstream graph and narrative.

### Assumptions

- Contributors will store large artifacts (datasets, derived evidence) under `data/**`, not under `mcp/**`.
- `mcp/**` documents must link to canonical artifact identifiers (STAC/DCAT/PROV IDs, graph entity IDs, or release manifests) wherever applicable.
- Not all subfolders may exist yet; this README defines the intended canonical structure.

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- No UI direct-to-graph reads (all graph access via API boundary).
- No unsourced narrative in published Story Nodes; `mcp/` artifacts should *help prevent* unsourced claims by keeping evidence traceable.
- Do not store secrets, tokens, or credentials in `mcp/**`.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize a `run_manifest` schema (YAML/JSON) for `mcp/runs/`? | TBD | TBD |
| Do we add an experiment report template under `mcp/experiments/`? | TBD | TBD |
| Do we adopt a formal model card format (e.g., HF-style + KFM extensions)? | TBD | TBD |

### Future extensions

- Automated linking from `mcp/runs/**` → PROV bundles in `data/prov/**`
- CI checks ensuring every model card references evaluation evidence
- Optional metrics tracking (e.g., entity extraction accuracy over time)

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  MCP[mcp/<br/>experiments + model cards + SOPs] -->|documents + pointers| D[data/<domain>/processed]
  D --> C1[data/stac/**]
  D --> C2[data/catalog/dcat/**]
  D --> C3[data/prov/**]
  C1 --> G[src/graph]
  C2 --> G
  C3 --> G
  G --> API[src/server or src/api]
  API --> UI[web/]
  UI --> SN[docs/reports/story_nodes]
  SN --> FM[Focus Mode<br/>provenance-linked only]
~~~

### Optional: sequence diagram (Focus Mode contract boundary)

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
| Evidence products (processed data) | files (varies) | `data/<domain>/processed/` | domain validators + schema checks |
| STAC/DCAT/PROV artifacts | JSON / JSON-LD (varies) | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | schema validation in `schemas/**` (if present) |
| Graph entity identifiers | strings | API/Graph outputs | contract tests (API) |
| Prior model versions + eval outputs | refs/pointers | releases or `data/**` | reproducibility checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Experiment report | Markdown | `mcp/experiments/**` | Universal doc template conventions |
| Run manifest/log | YAML/JSON/Markdown | `mcp/runs/**` | (recommended) schema in `schemas/telemetry/**` |
| Model card | Markdown (+ optional JSON) | `mcp/model_cards/**` | model card format (TBD) |
| SOP | Markdown | `mcp/sops/**` | SOP structure conventions |

### Sensitivity & redaction

- Do not publish exact coordinates or culturally sensitive locations in `mcp/**` unless governance explicitly allows it.
- Treat `mcp/**` as potentially public by default (see front-matter). If a doc must be restricted, mark it and follow the repository’s publishing rules.

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

- When an experiment/run produces a new evidence product, ensure the *canonical artifact* is cataloged:
  - STAC Collection + Items under `data/stac/**`
- `mcp/**` should reference STAC IDs (not duplicate the catalog content).

### DCAT

- For datasets/evidence products intended for publication or external interoperability:
  - DCAT dataset record under `data/catalog/dcat/**`
- `mcp/**` should reference DCAT identifiers and capture any license/attribution notes discovered during experimentation.

### PROV-O

- Prefer every meaningful run to produce (or link to) a PROV activity bundle under `data/prov/**`.
- `mcp/runs/**` should contain pointers/IDs to PROV, rather than duplicating provenance payloads.

### Versioning

- Treat model cards, run manifests, and SOPs as versioned artifacts.
- When a model is updated, update its model card with a changelog-style entry and link to evaluation evidence.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| MCP workspace (`mcp/`) | Experiment record + model documentation + SOPs | Markdown docs + manifests + pointers |
| ETL | Ingest + normalize | configs + run logs |
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
| API contracts | `src/server/contracts/**` (or legacy) | semver + contract tests |
| Schemas | `schemas/**` | semver + schema validation |
| MCP artifacts | `mcp/**` | version per artifact + provenance pointers |

---

## ⚙️ Validation & CI/CD

### Validation steps (recommended)

- Markdown protocol check (front-matter, required sections)
- Secrets scan (no tokens/keys)
- Link/reference checks (no orphan file pointers)
- If model card updated: ensure evaluation evidence is linked
- If experiment produces evidence: ensure STAC/DCAT/PROV updates exist in canonical locations

### CI expectations (if configured)

- Markdown protocol validation
- Schema validation (STAC/DCAT/PROV/story nodes/telemetry if present)
- API contract tests (if API boundary exists)
- Security and sovereignty scanning gates (if configured)

---

## ⚖ FAIR+CARE & Governance

- Keep `mcp/**` evidence-first:
  - clearly label *fact vs inference vs hypothesis* in experiment reports.
- If an experiment or model concerns:
  - culturally sensitive knowledge,
  - restricted locations,
  - protected personal data,
  - or high-impact narrative generation,
  then it requires governance review before downstream publication.

---

## 🧾 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `mcp/` README establishing structure and conventions | (you) |

---

### Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`
