---
title: "KFM src — Source Code Layout README"
path: "src/README.md"
version: "v1.1.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:src:readme:v1.1.0"
semantic_document_id: "kfm-src-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:src:readme:v1.1.0"
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

# src — Source Code Layout

This README is the **governed placement contract** for what belongs under `src/` and how it maps to the KFM architecture. Its job is to keep code placement **deterministic**, boundaries **enforced**, and the system’s canonical pipeline **unchanged**.

## 📘 Overview

### Purpose

- Provide a **single, governed map** of what lives under `src/` and how it aligns to KFM’s layered architecture.
- Act as a **navigation and placement contract** so contributors put new code in the correct subsystem and do not break the API boundary.
- Keep the repo architecture synced to the canonical flow:

  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### TLDR placement

- **`src/pipelines/`**: ETL + transforms + catalog builders that produce governed artifacts under `data/` (processed datasets + STAC/DCAT/PROV).
- **`src/graph/`**: ontology bindings + graph ingest/build logic + integrity checks (Neo4j layer).
- **`src/server/`**: API boundary only (contract-first REST/GraphQL, policy + redaction + provenance-aware responses).
- Everything else belongs in its canonical root (`web/`, `docs/`, `schemas/`, `tests/`, `tools/`, `mcp/`, `data/`, `releases/`).

### Scope

| In Scope | Out of Scope |
|---|---|
| High-level `src/` layout, responsibilities, and contract boundaries | Repo-specific deployment/run commands and environment secrets |
| Placement rules for pipelines, graph, and API code | Deep implementation details of any single domain pipeline |
| Cross-links to governance, contracts, and schemas | Creating new policy text (policy belongs under `docs/governance/`) |

### Audience

- Primary: KFM developers and maintainers
- Secondary: reviewers and contributors orienting to KFM’s code layout

### Definitions

- Glossary: `docs/glossary.md` (**not confirmed in repo**)
- Terms used here: ETL, STAC, DCAT, PROV-O, Neo4j, API boundary, deterministic pipeline, idempotence, redaction, contract tests, Story Nodes, Focus Mode.

### Key artifacts this README depends on

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + system inventory + extension matrix |
| Redesign blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Canonical homes, “one home per subsystem,” drift control |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template applied here |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Required for public API evolution |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Provenance-first narrative structure |
| Schema registry | `schemas/` | Data/Platform | JSON Schemas for catalogs, story nodes, telemetry, contracts |

### Definition of done for this document

- [ ] Front-matter valid and `path` matches file location
- [ ] `src/` responsibilities + placement rules are explicit and actionable
- [ ] Canonical pipeline ordering and API boundary invariants are stated
- [ ] Expected `src/` tree is documented and clearly labeled “recommended”
- [ ] Contract surfaces are listed (`schemas/`, `src/server/contracts/`, ontology bindings)
- [ ] Validation gates are listed (schema, contract, security, provenance)
- [ ] Sovereignty and sensitivity rules are acknowledged and not weakened

### Quick placement guide

Use this table when deciding where to put new work.

| What you are adding or changing | Primary home in `src/` | Also update | Minimum gates |
|---|---|---|---|
| New connector or ETL transform | `src/pipelines/` | `data/**` outputs + `schemas/` if needed + domain docs | schema validation + idempotence checks |
| New catalog mapping or provenance emission | `src/pipelines/` | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV validation |
| New entity type or relationship | `src/graph/` | ontology bindings + ingest mappings + upstream pipeline export | graph integrity + provenance pointer checks |
| New API endpoint or field | `src/server/` | `src/server/contracts/` + contract tests + version notes | OpenAPI/GraphQL lint + contract tests |
| New UI feature or layer | **not `src/`** (`web/`) | API contract + UI layer registry | a11y + contract conformance |
| New Story Node type or narrative workflow | **not `src/`** (`docs/reports/story_nodes/`) | graph + API + UI as needed | story node schema + citation validation |
| New security or telemetry gate | varies | `.github/` workflows + `docs/security/` + telemetry schemas | secrets/PII scan + policy enforcement tests |

## 🗂️ Directory Layout

### This document

- `path`: `src/README.md` (must match front-matter)

### Canonical homes by stage

These are the canonical subsystem homes. Keep them single-homed and drift-free.

| Stage | Canonical home | Primary artifacts |
|---|---|---|
| ETL and pipelines | `src/pipelines/` | deterministic transforms, catalog builders, run receipts |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections, DCAT datasets, PROV bundles |
| Graph | `src/graph/` + optional `data/graph/` | ontology-governed ingest, import fixtures |
| API boundary | `src/server/` | OpenAPI/GraphQL contracts, policy + redaction, query services |
| UI | `web/` | map layers, Focus Mode UX, citation rendering |
| Story Nodes | `docs/reports/story_nodes/` | draft/published narratives + assets |
| Experiments and run logs | `mcp/` | manifests, experiments, model cards, SOPs |
| Schemas | `schemas/` | JSON Schemas, validation contracts |
| Tests | `tests/` | unit, integration, contract, schema validation |
| Utilities | `tools/` | dev scripts, validators, repo hygiene |
| Releases | `releases/` | signed bundles, SBOMs, release manifests |

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/` | raw, work, processed datasets, plus published catalog + provenance outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | evidence artifacts consumed downstream |
| Graph import artifacts | `data/graph/` | CSV/Cypher exports for Neo4j ingest if used |
| Documentation | `docs/` | governed docs (guides, standards, runbooks, reports) |
| Schemas | `schemas/` | validation contracts (catalogs, story nodes, telemetry, API schemas) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph | `src/graph/` | ontology bindings, graph build, ingest fixtures |
| API boundary | `src/server/` | REST/GraphQL implementation + contracts + policy |
| UI | `web/` | React/MapLibre UI, Focus Mode UX, layer registry |
| Story Nodes | `docs/reports/story_nodes/` | narrative artifacts + assets |
| Tests | `tests/` | unit/integration/contract/schema tests |
| Tools | `tools/` | utilities, validators, hygiene scripts |
| MCP | `mcp/` | experiments, run manifests, model cards, SOPs |
| Security | `.github/` + `docs/security/` | security standards and workflows |

### Expected file tree for this sub-area

This is a **recommended** structure. Some directories may not exist yet. Keep this README synchronized with the actual `src/` contents.

~~~text
📁 src/
├── 📄 README.md
├── 📁 pipelines/
│   ├── 📄 README.md
│   ├── 📁 domains/
│   │   └── 📁 <domain>/
│   │       ├── 📄 README.md
│   │       ├── 📁 ingest/                 # source connectors
│   │       ├── 📁 transform/              # normalization/joins/QA
│   │       ├── 📁 catalog/                # STAC/DCAT/PROV builders
│   │       └── 📁 export/                 # processed + graph export (optional)
│   └── 📁 shared/                         # shared utilities (keep stable and minimal)
├── 📁 graph/
│   ├── 📄 README.md
│   ├── 📁 ontology/                       # ontology bindings / schema mappings
│   ├── 📁 ingest/                         # ingest builders / fixtures
│   ├── 📁 migrations/                     # constraints / migrations (optional)
│   └── 📁 queries/                        # query library used by API (optional)
└── 📁 server/
    ├── 📄 README.md
    ├── 📁 contracts/
    │   ├── 📁 openapi/                    # OpenAPI specs (optional)
    │   └── 📁 graphql/                    # GraphQL SDL (optional)
    ├── 📁 app/                            # application entrypoint (implementation-defined)
    ├── 📁 services/                       # domain services + query services
    ├── 📁 middleware/                     # auth, redaction, logging, rate limits
    └── 📁 adapters/                       # graph + catalog adapters (Neo4j, STAC readers, etc.)
~~~

### Legacy drift and migration notes

- Do **not** create alternative subsystem roots under `src/` such as `src/api/`, `src/ui/`, `src/map/`, or `src/neo4j/`.
- If you encounter such directories in the repo, treat them as **legacy drift** and:
  1) document deprecation intent,
  2) migrate functionality into the canonical home,
  3) keep a compatibility shim only if required by contract tests,
  4) delete only after removal is governed and validated.

## 🧭 Context

### Background

KFM is a governed geospatial and historical knowledge system designed around **evidence-first outputs** (catalog + provenance), a semantic **graph layer**, a strict **API boundary**, and an interactive **UI + narrative layer**.

### Assumptions

- `src/` contains **code**, not datasets.
- `data/` contains **artifacts and outputs** (raw/work/processed + catalogs + provenance).
- `docs/` contains **governed documents**, templates, and runbooks.
- `schemas/` contains **validation contracts** used across pipeline, graph, API, UI, and Story Node validation.

### Constraints and invariants

These are non-negotiable and should be treated as architecture contracts:

- **Canonical pipeline ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.
- **API boundary is enforced:** the UI must not query Neo4j (or any datastore) directly.
- **One canonical home per subsystem:** no “mystery duplicates” for pipelines, graph, server, UI, or story nodes.
- **Contracts are first-class:** schemas live in `schemas/`; API contracts live in `src/server/contracts/`. Avoid shadow copies.
- **Evidence-first narrative:** Story Nodes and Focus Mode must not contain unsourced claims. If interpretive, label as inference or hypothesis.
- **Determinism and idempotence:** pipelines should produce reproducible outputs (stable IDs, pinned inputs where applicable, fixed seeds).
- **Classification monotonicity:** outputs must not become less restrictive than their inputs. Redaction and generalization must be applied consistently across data, catalogs, API, and UI.
- **CI gates are expected:** schema validation, contract tests, secret and PII scans, and sensitive-location leakage checks.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `src/` subtrees exist today vs target layout? | TBD | TBD |
| What are the canonical build and test commands per subsystem? | TBD | TBD |
| Where do contract tests live and are they enforced in CI? | TBD | TBD |
| Are STAC and PROV profile docs complete or still placeholders? | TBD | TBD |

### Future extensions

- A vertical slice for one domain: dataset → STAC/DCAT/PROV → graph ingest fixture → API endpoint → UI layer → published Story Node.
- Domain packs with a consistent structure: connectors → transforms → catalogs → graph export → tests → docs.
- Stronger contract tooling: generated clients/types, schema-driven validation, and standardized run receipts.

## 🗺️ Diagrams

### Canonical pipeline and `src` responsibilities

~~~mermaid
flowchart LR
  A["ETL + Transforms<br/>src/pipelines"] --> B["Catalogs<br/>data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph Ingest + Integrity<br/>src/graph (+ optional data/graph)"]
  C --> D["API Boundary<br/>src/server + contracts"]
  D --> E["UI<br/>web"]
  E --> F["Story Nodes<br/>docs/reports/story_nodes"]
  F --> G["Focus Mode<br/>evidence-first only"]
~~~

### API boundary and Neo4j access

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

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw source files | varies | `data/**/raw/` | domain QA + license/sensitivity checks |
| Intermediate artifacts | varies | `data/**/work/` | optional; determinism preferred |
| Schemas | JSON Schema | `schemas/` | schema validation in CI |
| Governed docs and runbooks | Markdown | `docs/` | doc lint + template validation |

### Outputs

| Output | Format | Path | Contract or schema |
|---|---|---|---|
| Processed datasets | CSV/Parquet/GeoJSON/etc. | `data/**/processed/` | domain schema or constraints |
| STAC catalogs | JSON | `data/stac/` | KFM-STAC profile |
| DCAT catalog | JSON-LD/RDF | `data/catalog/dcat/` | KFM-DCAT profile |
| PROV bundles | JSON/Turtle/etc. | `data/prov/` | KFM-PROV profile |
| Graph ingest artifacts | CSV/Cypher/etc. | `data/graph/` | graph ingest constraints |
| API contracts | OpenAPI/GraphQL SDL | `src/server/contracts/` | contract lint + versioning |
| API responses | JSON | runtime | contract tests |

Rule: **outputs do not belong in `src/`**. If a file is an artifact (data, catalog, provenance), it belongs under `data/` (or `releases/` for packaged outputs).

## 🌐 STAC, DCAT & PROV Alignment

### Responsibility map

| Layer | Lives in | Must link to |
|---|---|---|
| STAC | `src/pipelines/` | `data/stac/*` + stable IDs + asset checksums |
| DCAT | `src/pipelines/` | `data/catalog/dcat/*` dataset/distribution metadata |
| PROV | `src/pipelines/` | `data/prov/*` activity/entity/agent/run IDs |
| Graph semantics | `src/graph/` | STAC item IDs, DCAT dataset IDs, PROV activity/run IDs |
| API contracts | `src/server/contracts/` | provenance references in payloads where required |

### Minimum alignment expectations

- Pipeline outputs validate against schemas where provided.
- Each dataset generation step emits a PROV activity record with inputs and outputs linked.
- Graph ingest preserves stable identifiers and stores provenance pointers.
- API payloads include the provenance references required to render citations in UI and Story Nodes.

## 🧱 Architecture

### Components and responsibilities

| Component | Responsibility | Interface | Must not do |
|---|---|---|---|
| `src/pipelines/` | ETL, transforms, catalogs, run receipts | writes artifacts under `data/**` | serve UI payloads directly |
| `src/graph/` | ontology bindings, ingest fixtures, integrity checks | graph ingest inputs + query surface for server | contain UI presentation logic |
| `src/server/` | contract-first API boundary with redaction | OpenAPI/GraphQL contracts | allow UI to couple directly to Neo4j |

### `src/pipelines` responsibilities

Primary job: turn raw sources into governed, validated evidence outputs.

- Read: `data/**/raw/` (and optionally `data/**/work/`)
- Write: `data/**/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`
- Optional: export graph ingest bundles to `data/graph/`

Non-negotiables:

- deterministic behavior (stable IDs, pinned inputs where applicable)
- idempotent reruns (unchanged inputs → unchanged outputs)
- no secrets in committed configs

### `src/graph` responsibilities

Primary job: build or ingest the semantic graph without breaking traceability.

- Apply ontology bindings, constraints, and integrity checks
- Preserve references to STAC/DCAT/PROV identifiers
- Provide a queryable semantic layer for the API boundary

Non-negotiables:

- never weaken classification or provenance requirements
- no UI concerns and no direct coupling to presentation formats

### `src/server` responsibilities

Primary job: expose a safe, stable interface to KFM capabilities.

- Enforce access control, redaction and generalization rules, audit logging
- Serve contracted payloads to the UI and external clients
- Centralize query services and provenance pointers for citations

Non-negotiables:

- contracts live under `src/server/contracts/`
- changes require versioning discipline and contract tests
- do not bypass governance checks with “quick fixes” in the UI

### Interfaces and contracts

These are the “hard edges” that keep subsystems decoupled:

- `schemas/`: JSON Schema validation contracts (data, catalogs, story nodes, telemetry)
- `src/server/contracts/`: OpenAPI and GraphQL contract sources of truth
- `src/graph/ontology/`: ontology bindings and ingest mappings
- `docs/templates/`: governed templates that shape documents and validation rules

## 🧠 Story Node & Focus Mode Integration

Even though Story Nodes live under `docs/`, `src/` must support narrative integrity.

- `src/server/` should expose endpoints that return:
  - data needed to render evidence layers,
  - provenance references sufficient for citation rendering.
- If predictive or AI-derived outputs are introduced, they must be:
  - clearly labeled as not-fact,
  - opt-in for UI display,
  - bundled with uncertainty fields and derivation notes.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks for governed docs
- [ ] Schema validation for STAC/DCAT/PROV artifacts
- [ ] Pipeline determinism and idempotence checks
- [ ] Graph integrity checks (constraints + provenance pointers)
- [ ] API contract tests (OpenAPI/GraphQL lint + integration tests)
- [ ] Security scans (secrets/PII) and sensitive-location leakage checks
- [ ] Accessibility checks for UI changes (WCAG targets)

### Reproduction

~~~bash
# Placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) validate schemas
# 2) run unit/integration tests
# 3) run contract tests
# 4) run doc lint
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Schema validation results | CI | CI logs + artifacts |
| Catalog publish lineage | pipelines | `data/prov/` + run receipts |
| Contract conformance | API tests | `tests/**` (recommended) |
| Promotion blocked | CI / publish step | CI logs + governance events |
| Graph integrity | graph checks | CI logs + ingest reports |

## ⚖ FAIR+CARE & Governance

### Review gates

- Schema changes affecting STAC/DCAT/PROV or public API payloads require governance review.
- New external data connectors must document:
  - license and terms
  - sensitivity classification
  - provenance capture
- Redaction and generalization logic changes require explicit review and tests.

### CARE and sovereignty considerations

- Identify communities impacted by new datasets or derived layers.
- For sensitive locations or restricted cultural content:
  - encode protection rules upstream,
  - enforce again at API boundary,
  - ensure UI does not leak precision or metadata via tooltips, exports, or logs.

### AI usage constraints

- This document permits: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.0 | 2025-12-27 | Reworked `src/` README to align with v12 inventory + extension matrix and v13 canonical homes | TBD |
| v1.0.0 | 2025-12-26 | Initial `src/` layout README (governed) | TBD |

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Templates: `docs/templates/`
- Schemas: `schemas/`
---
