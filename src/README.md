---
title: "KFM src — Source Code Layout README"
path: "src/README.md"
version: "v1.3.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:src:readme:v1.3.0"
semantic_document_id: "kfm-src-readme-v1.3.0"
event_source_id: "ledger:kfm:doc:src:readme:v1.3.0"
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

This README is the **governed placement contract** for what belongs under `src/` and how it maps to the KFM architecture. It exists to keep code placement **deterministic**, subsystem boundaries **enforced**, and the system’s canonical pipeline **unchanged**:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

## 📘 Overview

### Purpose

- Provide a **single, governed map** of what lives under `src/` and how it aligns to KFM’s layered architecture.
- Act as a **navigation + placement contract** so contributors put new code in the correct subsystem and do not break the API boundary.
- Encode **one canonical home per subsystem** (no duplicates) and keep the repo synced to the canonical pipeline ordering.

### Authority and precedence

- **Primary authority:** `docs/MASTER_GUIDE_v12.md` (repo-level source of truth for canonical ordering + canonical homes).
- **Directional draft (if adopted):** `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (documents drift patterns and a target layout; not binding unless adopted).

If this README conflicts with the Master Guide, the Master Guide wins.

### TL;DR placement

- **`src/pipelines/`**: ETL + transforms + catalog builders that produce governed artifacts under `data/` (processed datasets + STAC/DCAT/PROV).
- **`src/graph/`**: ontology bindings + graph ingest/build logic + integrity checks (Neo4j layer).
- **`src/server/`**: API boundary only (contract-first REST/GraphQL, policy + redaction + provenance-aware responses).
- Everything else belongs in its canonical root (`web/`, `docs/`, `schemas/`, `tests/`, `tools/`, `mcp/`, `data/`, `releases/`).

### Scope

| In Scope | Out of Scope |
|---|---|
| `src/` layout, responsibilities, and contract boundaries | Repo-specific deployment/run commands, infrastructure provisioning, environment secrets |
| Placement rules for pipelines, graph, and API code | Deep implementation details of any single domain pipeline |
| Drift-detection guidance + migration targets | Creating new policy text (policy belongs under `docs/governance/`) |

### Audience

- Primary: KFM developers and maintainers
- Secondary: reviewers and contributors orienting to KFM’s code layout

### Definitions

- Glossary: `docs/glossary.md` *(recommended; not confirmed in repo)*
- Terms used here: ETL, STAC, DCAT, PROV-O, Neo4j, API boundary, deterministic pipeline, idempotence, redaction, contract tests, Story Nodes, Focus Mode.

### Key artifacts this README depends on

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Repo-level source of truth for canonical ordering + canonical homes |
| Redesign blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Draft drift fixes + one-canonical-home enforcement |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template applied here |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Required for public API evolution |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Provenance-first narrative structure |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | not confirmed in repo |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | Architecture | not confirmed in repo |
| Schema registry | `schemas/` | Data/Platform | JSON Schemas for catalogs, story nodes, telemetry, contracts |

### Definition of done for this document

- [ ] Front-matter valid and `path` matches file location
- [ ] `src/` responsibilities + placement rules are explicit and actionable
- [ ] Canonical pipeline ordering and API boundary invariants are stated
- [ ] Expected `src/` tree is documented and clearly labeled “recommended”
- [ ] Contract surfaces are listed (`schemas/`, `src/server/contracts/`, ontology bindings)
- [ ] Drift rules reflect Master Guide v12; v13 blueprint drift patterns included as guidance
- [ ] Validation gates are listed (schema, link checks, contract, security, provenance)
- [ ] Sovereignty and sensitivity rules are acknowledged and not weakened

### Quick placement guide

Use this table when deciding where to put new work.

| What you are adding or changing | Primary home in `src/` | Also update | Minimum gates |
|---|---|---|---|
| New connector or ETL transform | `src/pipelines/` | `data/**` outputs + `schemas/` if needed + domain runbook under `docs/` | schema validation + idempotence checks |
| New catalog mapping or provenance emission | `src/pipelines/` | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV validation |
| New entity type or relationship | `src/graph/` | ontology bindings + ingest mappings + upstream pipeline export | graph integrity + provenance pointer checks |
| New API endpoint or field | `src/server/` | `src/server/contracts/` + contract tests + version notes | OpenAPI/GraphQL lint + contract tests |
| New UI feature or map layer | **not `src/`** (`web/`) | API contract + UI layer registry | a11y + contract conformance |
| New Story Node type or narrative workflow | **not `src/`** (`docs/reports/story_nodes/`) | graph + API + UI as needed | story node schema + citation validation |
| New security or telemetry gate | varies | `.github/` workflows + `docs/security/` + telemetry schemas | secrets/PII scan + policy enforcement tests |

## 🗂️ Directory Layout

### This document

- `path`: `src/README.md` (must match front-matter)

### Canonical homes by stage

These are the canonical subsystem homes. Keep them single-homed and drift-free.

| Stage | Canonical home | Primary artifacts |
|---|---|---|
| ETL / pipelines | `src/pipelines/` | deterministic transforms, run manifests/receipts, outputs in `data/**` |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections, DCAT datasets, PROV bundles |
| Graph | `src/graph/` + `data/graph/` *(if used)* | ontology-governed ingest + import fixtures/CSVs |
| API boundary | `src/server/` | OpenAPI/GraphQL contracts, redaction, query services |
| UI | `web/` | map layers, Focus Mode UX, citation rendering |
| Story Nodes | `docs/reports/story_nodes/` | templates, draft, published, assets |
| Experiments and run logs | `mcp/runs/` + `mcp/experiments/` | manifests, experiments, model cards, SOPs |
| Schemas | `schemas/` | JSON Schemas, validation contracts |
| Tests | `tests/` | unit, integration, contract, schema validation |
| Utilities | `tools/` | dev scripts, validators, repo hygiene |
| Releases | `releases/` | signed bundles, SBOMs, release manifests |

### Repo top-levels (expected)

This is the **repo-wide layout context** that `src/` must integrate with (see Master Guide v12). Treat this as an “expected” tree: validate if present; create intentionally if missing; do not create alternative roots.

~~~text
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md
├── 📁 data/
│   └── 📁 <domain>/
└── 📁 reports/
    └── 📁 story_nodes/                    # pattern; draft/published split if defined

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 story_nodes/
├── 📁 ui/
└── 📁 telemetry/

📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/

📁 web/
📁 tests/
📁 tools/
📁 releases/
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/` | raw/work/processed datasets, plus published catalog + provenance outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | evidence artifacts consumed downstream |
| Graph import artifacts | `data/graph/` | CSV/Cypher exports for Neo4j ingest (if used) |
| Documentation | `docs/` | governed docs (guides, standards, runbooks, reports) |
| Schemas | `schemas/` | validation contracts (catalogs, story nodes, telemetry, API schemas) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph | `src/graph/` | ontology bindings, graph build, ingest fixtures |
| API boundary | `src/server/` | REST/GraphQL implementation + contracts + policy |
| UI | `web/` | React/MapLibre UI, Focus Mode UX, layer registry |
| Story Nodes | `docs/reports/story_nodes/` | narrative artifacts + assets |
| Tests | `tests/` | unit/integration/contract/schema tests |
| Tools | `tools/` | utilities, validators, hygiene scripts |
| MCP | `mcp/runs/` + `mcp/experiments/` | experiments, run manifests, model cards, SOPs |
| Security | `.github/` + `docs/security/` | security standards and workflows *(docs path not confirmed)* |

### Expected file tree for this sub-area

This is a **recommended** internal structure for `src/`. Some directories may not exist yet. Keep this README synchronized with actual `src/` contents.

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
│   │       ├── 📁 export/                 # processed + graph export (optional)
│   │       └── 📁 tests/                  # pipeline-focused tests/fixtures (optional)
│   └── 📁 shared/                         # shared pipeline utilities (stable + minimal)
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

### Dependency direction rules

These rules enforce the canonical pipeline ordering:

- `src/pipelines/`:
  - **May** depend on: its own shared utilities; schema definitions; pure libraries.
  - **Must not** depend on: `src/graph/`, `src/server/`, `web/`.
  - **May write** to: `data/**` (raw/work/processed + catalogs + provenance).
- `src/graph/`:
  - **May** depend on: ontology bindings; schema definitions; readers for governed artifacts (catalog/prov/processed).
  - **Must not** depend on: `src/server/`, `web/`.
- `src/server/`:
  - **May** depend on: graph query services; readers for governed artifacts (STAC/DCAT/PROV); schemas/contracts.
  - **Must not** depend on: `src/pipelines/` (the server consumes *artifacts*, not pipeline code).
  - **Must not write** to: `data/**` as part of normal request handling (API is a boundary/serving layer).

Rule (API boundary): `web/` must not query Neo4j (or any datastore) directly. All access is mediated through contracted APIs in `src/server/`.

### File-type correctness

Do not mix governed Markdown and runnable scripts in the same file.

- If a pipeline recipe needs YAML front-matter and Markdown narrative, it belongs under `docs/` (typically `docs/data/<domain>/` or a repo-defined equivalent).
- If it is runnable code, it belongs under `src/` (typically `src/pipelines/...`).
- If you find a `.py`/`.js` file containing YAML front-matter + Markdown, split it into:
  - a Markdown recipe under `docs/`, and
  - a runnable script/module under `src/`.

### Legacy drift and migration notes

Do **not** create alternative subsystem roots under `src/` such as `src/api/`, `src/map/`, `src/ui/`, or `src/neo4j/`.

If you encounter such directories, treat them as **legacy drift** and:
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
- `docs/` contains **governed documents**, templates, runbooks, and reports.
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
- **CI gates are expected:** schema validation, link/reference checks, contract tests, secret and PII scans, and sensitive-location leakage checks.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `src/` subtrees exist today vs target layout? | TBD | TBD |
| Which data staging convention is canonical in this repo (v12 vs v13 target): `data/raw/<domain>/...` vs `data/<domain>/raw/...`? | TBD | TBD |
| Where do domain recipes/runbooks live: `docs/data/<domain>/` or another governed root? | TBD | TBD |
| Where do contract tests live and are they enforced in CI? | TBD | TBD |

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
| Raw source files | varies | `data/raw/<domain>/` *(v12 pattern; see Master Guide)* | domain QA + license/sensitivity checks |
| Intermediate artifacts | varies | `data/work/<domain>/` *(optional)* | determinism preferred |
| Schemas | JSON Schema | `schemas/` | schema validation in CI |
| Governed docs and runbooks | Markdown | `docs/` | doc lint + template validation |

### Outputs

| Output | Format | Path | Contract or schema |
|---|---|---|---|
| Processed datasets | CSV/Parquet/GeoJSON/etc. | `data/processed/<domain>/` | domain schema or constraints |
| STAC catalogs | JSON | `data/stac/collections/` + `data/stac/items/` | KFM-STAC profile |
| DCAT catalog | JSON-LD/RDF | `data/catalog/dcat/` | KFM-DCAT profile |
| PROV bundles | JSON/Turtle/etc. | `data/prov/` | KFM-PROV profile |
| Graph ingest artifacts | CSV/Cypher/etc. | `data/graph/` | graph ingest constraints |
| API contracts | OpenAPI/GraphQL SDL | `src/server/contracts/` | contract lint + versioning |
| API responses | JSON | runtime | contract tests |

### Sensitivity & redaction

Even though `src/` is code-only, it contains the enforcement logic that controls what can be exposed downstream:

- Redaction/generalization and classification propagation should be implemented and tested in `src/server/` (middleware/services).
- Pipelines and graph ingest must preserve sensitivity metadata and provenance pointers so the server can enforce policy consistently.

### Quality signals

- Deterministic behavior (stable IDs, pinned dependencies/config, idempotent reruns).
- Contract conformance: API responses, schemas, and catalogs validate in CI.
- Link/reference checks for governed docs and contracts remain green.

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

### Interfaces and contracts

These are the “hard edges” that keep subsystems decoupled:

- `schemas/`: JSON Schema validation contracts (data, catalogs, story nodes, telemetry)
- `src/server/contracts/`: OpenAPI and GraphQL contract sources of truth
- `src/graph/ontology/`: ontology bindings and ingest mappings
- `docs/templates/`: governed templates that shape documents and validation rules

### Extension points checklist (for future work)

Use this list as a “vertical slice” sanity check when adding a domain or evidence product.

- [ ] Data: domain staging exists under the canonical `data/` pattern (v12 or adopted v13 layout)
- [ ] STAC: new collection + item(s) produced and schema-validated
- [ ] DCAT: dataset/distribution metadata produced (if required)
- [ ] PROV: activity + agent identifiers recorded and linked to outputs
- [ ] Graph: labels/relations mapped; ingest fixtures updated; provenance pointers preserved
- [ ] APIs: contract updated + versioned; contract tests added/updated
- [ ] UI: layer registry entry + access rules; a11y checks pass
- [ ] Story Nodes / Focus Mode: provenance references sufficient for citations; no unsourced narrative
- [ ] Telemetry (if applicable): signals recorded and schema version bumped

## 🧠 Story Node & Focus Mode Integration

Even though Story Nodes live under `docs/`, `src/` must support narrative integrity.

- `src/server/` should expose endpoints that return:
  - data needed to render evidence layers, and
  - provenance references sufficient for citation rendering.
- Evidence artifacts (including AI/analysis outputs) are treated like datasets:
  - generated under `data/processed/<domain>/...`,
  - cataloged (STAC/DCAT) and traced (PROV),
  - optionally linked into the graph with explicit provenance,
  - exposed only via APIs that implement redaction and classification rules.
- If predictive or AI-derived outputs are introduced, they must be:
  - clearly labeled as not-fact,
  - opt-in for UI display,
  - bundled with uncertainty fields and derivation notes.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks for governed docs
- [ ] Link + reference checks (internal links resolve; “not confirmed in repo” used where appropriate)
- [ ] Schema validation for STAC/DCAT/PROV artifacts
- [ ] Pipeline determinism and idempotence checks
- [ ] Graph integrity checks (constraints + provenance pointers)
- [ ] API contract tests (OpenAPI/GraphQL lint + integration tests)
- [ ] Security scans (secrets/PII) and sensitive-location leakage checks
- [ ] Accessibility checks for UI changes (WCAG targets)
- [ ] (Recommended) repo drift checks: ensure no duplicate subsystem homes are introduced

### Reproduction

~~~bash
# Placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) validate schemas
# 2) run unit/integration tests
# 3) run contract tests
# 4) run doc lint + link check
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Link + schema validation results | CI | CI logs + artifacts |
| Catalog publish lineage | pipelines | `data/prov/` + run receipts |
| Contract conformance | API tests | `tests/**` (recommended) |
| Graph integrity | graph checks | CI logs + ingest reports |
| Promotion blocked / policy violations | CI / publish step | CI logs + governance events |

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
| v1.3.0 | 2025-12-28 | Synced `src/` README more tightly to Master Guide v12 “repo top-levels” expectations; clarified precedence rules (v12 authoritative, v13 directional); strengthened dependency direction rules; added extension checklist and drift gate guidance | TBD |
| v1.2.0 | 2025-12-28 | Synced `src/` contract to Master Guide v12 + v13 drift rules; clarified dependency direction, file-type correctness, and CI link checks; added sensitivity/quality signals | TBD |
| v1.1.0 | 2025-12-27 | Reworked `src/` README to align with v12 inventory + extension matrix and v13 canonical homes | TBD |
| v1.0.0 | 2025-12-26 | Initial `src/` layout README (governed) | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Templates: `docs/templates/`
- Schemas: `schemas/`
