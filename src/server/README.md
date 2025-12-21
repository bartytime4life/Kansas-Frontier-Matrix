---
title: "KFM Server (API Boundary) — src/server"
path: "src/server/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:src-server:readme:v1.0.0"
semantic_document_id: "kfm-src-server-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src-server:readme:v1.0.0"
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

# KFM Server (API Boundary) — src/server

## 📘 Overview

### Purpose
This directory defines the **KFM API boundary**: the only approved interface between upstream system layers (catalogs + graph) and downstream consumers (UI, Story Nodes, external clients). It enforces contracts, provenance linking, redaction rules, and auditability.

### Scope

| In Scope | Out of Scope |
|---|---|
| REST endpoints and OpenAPI contract surfaces | UI components and map rendering |
| Optional GraphQL schema/resolvers (contracted) | Direct Neo4j access from the frontend |
| Redaction/sensitivity gates for Focus Mode | ETL transforms and catalog generation |
| Provenance attachment rules (STAC/DCAT/PROV IDs) | Narrative authoring (Story Nodes live in `docs/`) |

### Audience
- Primary: API engineers, graph/query engineers, contract/test maintainers
- Secondary: UI developers, curators, governance reviewers, external integrators

### Definitions (link to glossary)
- Link: `../../docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc: API boundary, contract, redaction, provenance bundle, Focus Mode, Story Node

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `../../docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| API contracts | `src/server/**` | API Maintainers | OpenAPI + (optional) GraphQL |
| Graph constraints | `../graph/constraints/` | Graph Maintainers | API must respect graph constraints |
| Schema library | `../../schemas/` | Schema Maintainers | JSON Schema validation |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] “API boundary” rule stated and unambiguous
- [ ] Contract locations + expected layout documented
- [ ] Validation expectations listed (contract tests, schema validation, security checks)
- [ ] Provenance + redaction requirements described clearly

## 🗂️ Directory Layout

### This document
- `path`: `src/server/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Pipelines | `../pipelines/` | ETL + catalog builders (upstream) |
| Graph | `../graph/` | Neo4j build, ontology bindings, constraints |
| Schemas | `../../schemas/` | JSON Schemas used by contracts + UI registries |
| Web UI | `../../web/` | React/Map clients (downstream) |
| Story Nodes | `../../docs/reports/story_nodes/` | Narrative artifacts with citations *(not confirmed in repo)* |
| Catalog outputs | `../../data/stac/`, `../../data/catalog/dcat/`, `../../data/prov/` | STAC/DCAT/PROV artifacts *(not confirmed in repo)* |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 server/
    ├── 📄 README.md
    ├── 📁 contracts/                  # OpenAPI/GraphQL source-of-truth (recommended)
    │   ├── 📁 openapi/                # OpenAPI YAML/JSON (recommended)
    │   └── 📁 graphql/                # GraphQL SDL (optional)
    ├── 📁 api/                        # Route handlers (REST)
    ├── 📁 middleware/                 # Authn/authz, logging, correlation IDs, rate limits
    ├── 📁 services/                   # Use-cases: query orchestration, provenance join
    ├── 📁 adapters/                   # Graph driver, catalog reader, cache clients
    ├── 📁 domain/                     # Domain models + invariants (no transport types)
    ├── 📁 policy/                     # Redaction + sovereignty + sensitivity rules
    ├── 📁 telemetry/                  # Metrics/tracing/logging helpers
    ├── 📁 config/                     # Typed config + env parsing (no secrets committed)
    └── 📁 tests/                      # Contract tests + integration tests
~~~

## 🧭 Context

### Background
KFM’s pipeline is intentionally layered. The API exists to:
- prevent downstream components from bypassing governance (no direct graph reads by UI),
- provide **stable, versioned contracts** (OpenAPI/GraphQL),
- attach **provenance identifiers** to every response,
- enforce **redaction and sensitivity controls**, especially for Focus Mode.

### Assumptions
- OpenAPI exists (or will exist) as the canonical REST contract surface.
- GraphQL may exist as an additional contract surface for subgraph-shaped client needs.
- Authn/authz and redaction policies are required before any “restricted” datasets can be served.
- Governance docs referenced in front-matter are authoritative, but some may be **not confirmed in repo**.

### Constraints / invariants
- Canonical pipeline ordering is preserved:
  - ETL → STAC/DCAT/PROV → Graph → **APIs** → UI → Story Nodes → Focus Mode
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- API responses must be contract-valid and must include provenance references when used in Focus Mode contexts.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical auth mechanism (OIDC/OAuth2 vs API keys for internal use)? | KFM Core | TBD |
| Where is the single source-of-truth for OpenAPI (YAML vs generated)? | API Maintainers | TBD |
| What is the minimum “Focus Bundle” response schema for Focus Mode? | API + UI | TBD |

### Future extensions
- STAC API-compatible search endpoints (if adopted).
- “Evidence bundles” for Focus Mode (graph subgraph + STAC/DCAT/PROV IDs + audit flags).
- Signed response metadata for published releases (requires human review).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC / DCAT / PROV — data outputs"]
  B --> C["Neo4j Graph — src/graph"]
  C --> D["API Boundary — src/server"]
  D --> E["Web UI — web"]
  E --> F["Story Nodes — docs"]
  F --> G["Focus Mode — provenance-linked"]
~~~

### Optional: sequence diagram (Focus Mode context fetch)
~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph Store
  UI->>API: GET /focus/{entity_id}?time=...
  API->>Graph: Query subgraph + provenance refs
  Graph-->>API: Nodes/edges + record identifiers
  API-->>UI: Focus bundle (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Graph query results | Records / subgraph | Graph adapter | Constraint checks + pagination limits |
| Catalog lookups | STAC/DCAT/PROV | `data/**` readers | JSON schema validation |
| Access context | auth claims | middleware | policy allowlist + RBAC |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| REST responses | JSON | `src/server/api/**` | OpenAPI schema |
| GraphQL responses (optional) | JSON | `src/server/graphql/**` | GraphQL SDL + typed resolvers |
| Audit signals | headers / fields | middleware | schema + logging rules |
| Provenance references | IDs + links | service layer | required in Focus Mode contexts |

### Sensitivity & redaction
- The API must support redaction/generalization rules for:
  - sensitive locations,
  - culturally sensitive content,
  - restricted datasets requiring governance approval.
- If governance policy files are missing, treat these rules as **not confirmed in repo** and block restricted releases until reviewed.

### Quality signals
- Contract validation (OpenAPI/GraphQL).
- Pagination + rate limit defaults (prevent accidental graph dumps).
- Provenance completeness: responses include dataset/asset IDs where applicable.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Responses referencing assets should include STAC Item IDs (and Collection IDs where relevant).
- API may provide “asset resolver” endpoints (ID → asset URL + metadata) if needed.

### DCAT
- Dataset-level endpoints should include DCAT dataset identifiers (stable semantic IDs).
- License information should be propagated from DCAT metadata into response metadata.

### PROV-O
- Responses used in Focus Mode should include:
  - `prov:wasDerivedFrom` identifiers (source assets/records),
  - `prov:wasGeneratedBy` identifiers (pipeline run/activity IDs),
  - optional confidence/uncertainty fields for predictive outputs.

### Versioning
- When contracts change, bump contract versions and add contract tests.
- When datasets change, ensure successor/predecessor metadata is reflected and references remain resolvable.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Catalog readers | Resolve STAC/DCAT/PROV IDs | file readers + schema validation |
| Graph adapters | Query graph store safely | parameterized queries via services |
| Service layer | Orchestrate use-cases + join provenance | pure functions + typed models |
| Policy layer | Redaction + sovereignty gating | allow/deny + transform rules |
| API layer | Present contracts | REST/GraphQL |
| Telemetry | Observability | logs + metrics + traces |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `../../schemas/` | Semver + changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| UI registries | `../../web/**` | Schema-validated |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode consumes a **focus bundle** produced by the API boundary:
  - graph context (entities + relationships),
  - evidence references (STAC/DCAT/PROV IDs),
  - redaction and audit flags,
  - optional curated story node references.

### Provenance-linked narrative rule
- Every claim rendered in Focus Mode must trace to a dataset / record / asset ID.
- If an endpoint cannot provide provenance identifiers, it must not be eligible for Focus Mode rendering.

### Optional structured controls
~~~yaml
focus_layers:
  - "base_map"
  - "kfm_assets"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) where referenced
- [ ] Graph integrity checks (as part of graph pipeline CI)
- [ ] API contract tests (OpenAPI + GraphQL, if present)
- [ ] Security and sovereignty checks (policy gating, as applicable)

### Reproduction
~~~bash
# Placeholders — commands are not confirmed in repo.
# Validate API contracts
# make api-contract-test

# Run API unit/integration tests
# make test-server
~~~

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `src/server/README.md` scaffold | TBD |

---

## 🔗 Navigation
- ⬅️ Back to `src/README.md`
- 📘 Master Guide: `../../docs/MASTER_GUIDE_v12.md`
- 🛡️ Governance Charter: `../../docs/governance/ROOT_GOVERNANCE.md` *(not confirmed in repo)*
