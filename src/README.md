---
title: "KFM src/ — Source Code Layout (README)"
path: "src/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:src:readme:v1.0.0"
semantic_document_id: "kfm-src-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:readme:v1.0.0"
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

# src/ — KFM Source Code Overview

## 📘 Overview

### Purpose

- Provide a **single, governed map** of what lives under `src/` and how it aligns to KFM’s layered architecture.
- Act as a **navigation + placement contract** so contributors put new code in the correct subsystem and do not break the API boundary.
- Keep the repo architecture **synced to the canonical flow**: ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode.

### Scope

| In Scope | Out of Scope |
|---|---|
| High-level `src/` layout, responsibilities, and contract boundaries | Repo-specific build commands, deployment procedures, and environment secrets |
| Placement rules for pipelines/graph/API code | Implementation details of any single pipeline |
| Cross-links to governance, contracts, and schemas | New policy creation (policy belongs under `docs/governance/`) |

### Audience

- Primary: KFM developers and maintainers
- Secondary: Data stewards, reviewers, and contributors orienting to KFM’s code layout

### Definitions

- Glossary: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: ETL, STAC, DCAT, PROV-O, Neo4j, API boundary, Story Nodes, Focus Mode, deterministic pipeline, idempotence, redaction, contract tests.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (v12) | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + invariants |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used by this README |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM Core | How to evolve REST/GraphQL contracts |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Provenance-first narrative structure |
| Schema registry | `schemas/` | Data/Platform | JSON Schemas for validation gates |
| Pipelines runbooks | `docs/pipelines/` | Data Eng | Human-facing “recipes” (code stays in `src/`) (**not confirmed in repo**) |
| Graph docs | `docs/graph/` | Graph Eng | Ontology/labels/edges, migrations (**not confirmed in repo**) |
| API contracts (canonical) | `src/server/contracts/` | API Eng | Contract-first boundary (OpenAPI/GraphQL) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Draft/published narratives consumed by UI |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] `src/` responsibilities + placement rules documented
- [ ] Canonical pipeline + API boundary invariants stated
- [ ] Expected `src/` tree provided (recommended structure allowed)
- [ ] Validation steps listed (placeholders allowed; mark “not confirmed in repo” where needed)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `src/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs, plus catalog + provenance outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (canonical evidence + lineage) |
| Graph import artifacts | `data/graph/` | CSV + Cypher outputs for Neo4j ingest (if used) |
| Documentation | `docs/` | Canonical governed docs (Master Guide, standards, runbooks, reports) |
| Schemas | `schemas/` | JSON Schemas for catalogs/contracts/story nodes/telemetry |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph | `src/graph/` | Ontology bindings, graph build, import fixtures |
| API boundary | `src/server/` | REST/GraphQL + redaction + access controls + query services |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts + assets |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Ops scripts and developer utilities |
| MCP | `mcp/` | Experiments, run manifests, model cards, SOPs |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**). Keep this README synchronized with the actual `src/` contents.

~~~text
📁 src/
├── 📄 README.md
├── 📁 pipelines/
│   ├── 📄 README.md                 # pipeline overview + conventions (recommended)
│   ├── 📁 etl/                      # orchestration + domain ETL entrypoints (optional)
│   ├── 📁 catalog/                  # STAC/DCAT/PROV builders (optional)
│   ├── 📁 domains/                  # per-domain packs (recommended)
│   │   └── 📁 <domain>/
│   │       ├── 📄 README.md
│   │       ├── 📁 ingest/           # source connectors (optional)
│   │       ├── 📁 transform/        # normalization/joins (optional)
│   │       └── 📁 export/           # writing processed + catalogs + graph export (optional)
│   └── 📁 shared/                   # shared utilities (recommended; keep stable and minimal)
├── 📁 graph/
│   ├── 📄 README.md                 # graph build + ontology conventions (recommended)
│   ├── 📁 ontology/                 # ontology bindings / schema mappings (recommended)
│   ├── 📁 ingest/                   # graph import builders (recommended)
│   ├── 📁 migrations/               # graph migrations/constraints (optional)
│   └── 📁 queries/                  # query library used by API (optional)
└── 📁 server/
    ├── 📄 README.md                 # API boundary overview (recommended)
    ├── 📁 contracts/
    │   ├── 📁 openapi/              # OpenAPI specs (optional)
    │   └── 📁 graphql/              # GraphQL SDL (optional)
    ├── 📁 app/                      # application entrypoint (implementation-defined)
    ├── 📁 services/                 # domain services + query services
    ├── 📁 middleware/               # auth, redaction, logging, rate limits
    └── 📁 adapters/                 # graph + catalog adapters (Neo4j, STAC readers, etc.)
~~~

> If you find `src/api/` or `src/map/` in the repo, treat them as **legacy drift** unless explicitly documented otherwise (**not confirmed in repo**). The target canonical homes are `src/server/` for the API boundary and `web/` for the UI.

---

## 🧭 Context

### Background

KFM is a governed geospatial + historical knowledge system designed around **evidence-first outputs** (catalog + provenance), a semantic **graph layer**, a strict **API boundary**, and an interactive **UI + narrative layer**.

### Assumptions

- `src/` contains **code**, not datasets.
- Data artifacts live under the `data/` hierarchy; governed documents live under `docs/`.
- Interfaces are contract-first: schemas and API contracts are treated as first-class repo artifacts.

### Constraints / invariants (non-negotiables)

- **Canonical order is preserved:** ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
- **API boundary is enforced:** the UI does **not** connect to Neo4j directly; all access routes through `src/server/` contracts and policy.
- **Contracts are canonical:** JSON Schemas under `schemas/`; API contracts under `src/server/contracts/`. Avoid “shadow copies” of schemas in code or UI.
- **No unsourced narrative:** Story Nodes / Focus Mode content must be provenance-linked to datasets/documents and pass validation gates.
- **Data outputs are not code:** derived datasets do not belong in `src/`; executable code does not belong in `docs/` or `data/`. Mixed “doc + script” files must be split.
- **Determinism + idempotence:** pipelines should be reproducible (stable IDs, pinned dependencies where applicable, fixed seeds, run manifests).
- **Single canonical home per subsystem:** duplicates must include explicit deprecation/migration notes (no “mystery duplicates”).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `src/` subtrees exist today vs target layout? | TBD | TBD |
| What are the canonical build/test commands per subsystem (Python/Node/etc.)? | TBD | TBD |
| Where do contract tests live today (and are they enforced in CI)? | TBD | TBD |
| What is the canonical glossary location and completeness? | TBD | TBD |

### Future extensions

- Per-domain “packs” that include: connectors → transforms → catalogs → graph export → tests.
- Stronger contract tooling (generated clients/types) to reduce contract duplication.
- Deterministic run “receipts” (PROV + checksums + artifact inventories) for all pipelines.

---

## 🗺️ Diagrams

### Canonical pipeline and `src/` responsibilities

~~~mermaid
flowchart LR
  A["ETL + Transforms<br/>src/pipelines"] --> B["Catalogs<br/>data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph Build + Ingest<br/>src/graph + data/graph"]
  C --> D["API Boundary<br/>src/server + contracts"]
  D --> E["UI<br/>web (React/Map)"]
  E --> F["Story Nodes<br/>docs/reports/story_nodes"]
  F --> G["Focus Mode<br/>provenance-linked only"]
~~~

### API boundary (UI never queries Neo4j directly)

~~~mermaid
sequenceDiagram
  participant UI as web (UI)
  participant API as src/server (API boundary)
  participant Graph as Neo4j / graph services
  UI->>API: Request (contracted)
  API->>Graph: Query (policy + redaction applied)
  Graph-->>API: Results + provenance refs
  API-->>UI: Contracted payload + provenance pointers
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Typical location | How `src/` uses it |
|---|---|---|
| Raw source files | `data/<domain>/raw/` | Read-only inputs for ETL |
| Work/intermediate artifacts | `data/<domain>/work/` | Cached intermediates (optional; deterministic preferred) |
| Processed datasets | `data/<domain>/processed/` | Outputs written by pipelines; inputs for graph export (as needed) |
| STAC/DCAT/PROV schemas | `schemas/` | Validation and contract enforcement |
| Governed docs/runbooks | `docs/` | Human guidance; no executable code |

### Outputs

| Output | Location | Producer |
|---|---|---|
| Processed datasets | `data/<domain>/processed/` | `src/pipelines/` |
| STAC catalogs | `data/stac/collections/` + `data/stac/items/` | `src/pipelines/` (catalog stage) |
| DCAT catalog | `data/catalog/dcat/` | `src/pipelines/` (catalog stage) |
| PROV bundles | `data/prov/` | `src/pipelines/` (run lineage stage) |
| Graph import artifacts (optional) | `data/graph/` | `src/pipelines/` export + `src/graph/` build |
| API responses (runtime) | N/A | `src/server/` |

> Rule: **Do not** check large derived datasets into `src/`. If a file is “an output,” it belongs under `data/` (or `releases/` for packaged artifacts, if adopted).

---

## 🌐 STAC, DCAT & PROV Alignment

### Responsibility map

| Layer | In `src/` | Must link to |
|---|---|---|
| STAC (evidence assets) | `src/pipelines/` | `data/stac/*` + stable IDs |
| DCAT (discovery metadata) | `src/pipelines/` | `data/catalog/dcat/*` datasets/distributions |
| PROV (lineage) | `src/pipelines/` | `data/prov/*` run/activity/entity IDs |
| Graph semantics | `src/graph/` | STAC item IDs, DCAT dataset IDs, PROV activity/run IDs |
| API contracts | `src/server/contracts/` | Provenance references in payloads (where applicable) |

### Minimum alignment expectations

- Pipeline outputs should be **valid** against schemas (where provided).
- Graph ingest should preserve stable identifiers and attach provenance pointers (e.g., `prov:wasDerivedFrom`, run IDs, dataset IDs).
- API payloads that drive UI narratives should include the **provenance refs needed for citation** in Story Nodes / Focus Mode.

---

## 🧱 Architecture

### `src/pipelines/` — ETL + transforms + catalogs

**Primary job:** turn raw sources into governed, validated evidence outputs:

- Write domain data to `data/<domain>/{raw,work,processed}/`
- Write catalogs to `data/stac/`, `data/catalog/dcat/`, and lineage to `data/prov/`
- Optionally export graph-import bundles to `data/graph/` (CSV/Cypher/etc.)

**Non-negotiables:**

- Deterministic behavior (stable IDs, pinned inputs, seeded randomness)
- Idempotent reruns (unchanged inputs → unchanged outputs)
- No secrets in configs committed to repo

### `src/graph/` — ontology + ingest + integrity

**Primary job:** build/ingest the semantic graph layer without breaking traceability:

- Import from `data/graph/` (if used) or directly from catalog artifacts (implementation-defined)
- Apply ontology bindings, constraints, and integrity checks
- Produce a graph that can answer API queries with provenance-backed semantics

**Non-negotiables:**

- Preserve references to STAC/DCAT/PROV identifiers
- Avoid UI concerns; this layer is not presentation logic

### `src/server/` — API boundary (contract-first)

**Primary job:** expose a safe, stable interface to KFM capabilities:

- Enforce access controls, redaction/generalization rules, and audit/logging
- Serve contracted payloads to `web/` (UI) and external clients
- Centralize query services; do not allow UI to couple directly to graph internals

**Non-negotiables:**

- Contracts live under `src/server/contracts/` (OpenAPI/GraphQL as chosen)
- Responses include provenance pointers where required for Story Nodes / Focus Mode
- Schema/contract changes require versioning + tests

---

## 🧠 Story Node & Focus Mode Integration

Even though Story Nodes live under `docs/`, `src/` must support narrative integrity:

- `src/server/` should provide endpoints that can return:
  - the data needed to render a story’s evidence layers
  - provenance references sufficient for citations
- Any AI/predictive outputs (if introduced) must be:
  - clearly labeled (prediction vs fact)
  - opt-in for UI display
  - bundled with uncertainty/confidence fields and provenance/derivation notes

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Markdown protocol checks for governed docs (where applicable)
- [ ] Schema validation (STAC/DCAT/PROV + contract schemas)
- [ ] Pipeline determinism/idempotence checks (golden outputs or checksum receipts)
- [ ] Graph integrity checks (constraints, required labels/edges, provenance pointers)
- [ ] API contract tests (OpenAPI/GraphQL lint + integration tests)
- [ ] Security scanning (secrets/PII) and sovereignty checks (if sensitive data introduced)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) validate schemas
# 2) run unit/integration tests
# 3) run contract tests
# 4) run doc lint
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| Schema validation results | CI | CI logs + artifacts |
| Pipeline run lineage | Pipelines/catalog | `data/prov/` + run manifests (if used) |
| Contract conformance | API tests | `tests/contract/` (recommended) |
| Graph integrity | Graph checks | CI logs + graph build artifacts |

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Schema changes affecting STAC/DCAT/PROV or public API payloads require governance review.
- Any new external data connector must document:
  - license/terms
  - sensitivity classification
  - provenance capture
- Any changes to redaction/generalization logic require explicit review and test coverage.

### CARE and sovereignty considerations

- Identify communities impacted by new datasets or new derived layers.
- If locations/records are sensitive, define protection rules and ensure they are enforced at the API boundary.

### AI usage constraints

- This document permits: structural extraction, summarization, translation, keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `src/` layout README (governed) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
