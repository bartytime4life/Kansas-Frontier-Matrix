---
title: "KFM — GraphQL Server Module (src/server/graphql)"
path: "src/server/graphql/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:src:server:graphql:readme:v1.0.0"
semantic_document_id: "kfm-src-server-graphql-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:server:graphql:readme:v1.0.0"
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

# KFM — GraphQL Server Module

## 📘 Overview

### Purpose
This module documents (and should govern) the GraphQL surface area of the KFM API layer under `src/server/graphql/`.
It exists to ensure GraphQL remains a **contracted API boundary** between clients (UI/tools) and backends (graph/catalog/services), and to keep provenance + sensitivity behavior explicit and testable.

### Scope
| In Scope | Out of Scope |
|---|---|
| GraphQL schema organization, resolver patterns, context construction, authorization hooks, provenance-linking conventions, validation/testing expectations | ETL ingestion, STAC/DCAT/PROV generation, graph migrations/constraints, UI implementation details, “policy text” beyond existing governance docs |

### Audience
- Primary: Backend/API engineers working in `src/server/` and `src/server/graphql/`
- Secondary: Graph engineers (`src/graph/`), pipeline engineers (`src/pipelines/`), frontend engineers (`web/`) who consume GraphQL contracts

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **API boundary**: UI consumers must not query Neo4j directly; all access is via API contracts.
  - **Provenance refs**: identifiers (STAC/DCAT/PROV) included in responses so clients can render evidence/audit.
  - **Focus bundle**: an API payload optimized for Focus Mode (narrative + entities + citations + map hints). (**not confirmed in repo**)

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| GraphQL schema entrypoint | `src/server/graphql/` | API | Exact filename(s) **not confirmed in repo** |
| Resolver implementation(s) | `src/server/graphql/` | API | Prefer small resolvers + shared services/dataloaders |
| API contract governance | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API + Governance | Use when changing public GraphQL contract |
| System invariants | `docs/MASTER_GUIDE_v12.md` | Architecture | Canonical pipeline + “no direct graph access from UI” |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `src/server/graphql/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Server (API layer) | `src/server/` | REST/GraphQL servers, auth middleware, contract tests |
| GraphQL (this area) | `src/server/graphql/` | Schema + resolvers + GraphQL-specific utilities |
| Graph access layer | `src/graph/` | Graph build/ontology bindings (UI must not read this directly) |
| Pipelines | `src/pipelines/` | ETL + catalog generation + graph build pipelines |
| Schemas | `schemas/` | JSON schemas, telemetry schemas, contract fixtures |
| Frontend | `web/` | React + MapLibre/Cesium clients consuming API contracts |

### Expected file tree for this sub-area
(**not confirmed in repo** — this is the recommended minimum shape)

~~~text
📁 src/
└── 📁 server/
    └── 📁 graphql/
        ├── 📄 README.md
        ├── 📄 schema.graphql              # or schema.ts (not confirmed)
        ├── 📁 resolvers/                  # field resolvers (not confirmed)
        │   ├── 📄 index.ts                # resolver map (not confirmed)
        │   └── 📄 *.resolver.ts           # per-domain resolvers (not confirmed)
        ├── 📁 types/                      # GraphQL type helpers (not confirmed)
        ├── 📁 directives/                 # auth/provenance directives (not confirmed)
        ├── 📁 dataloaders/                # batching + caching (not confirmed)
        ├── 📁 services/                   # backend adapters (Neo4j/catalog) (not confirmed)
        └── 📁 __tests__/                  # contract/integration tests (not confirmed)
~~~

## 🧭 Context

### Background
KFM’s architecture is pipeline-driven and explicitly separates concerns:
ETL → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.

GraphQL (when used) lives in the **API layer**, enforcing:
- a stable **contract** for clients
- provenance-first payloads (evidence and audit references)
- sensitivity-aware access (authorization + redaction/generalization)

### Assumptions
- A GraphQL service exists or is planned under `src/server/graphql/`. (**not confirmed in repo**)
- The UI consumes graph data through API contracts, not direct database connectivity.
- Provenance is required in Focus Mode contexts.

### Constraints / invariants
- The canonical pipeline ordering is preserved: ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Any predictive/AI-derived fields must be opt-in and carry uncertainty/confidence metadata. (**not confirmed in repo**; treat as requirement for future work if introduced)

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which GraphQL server/runtime is used (Apollo, Yoga, Mercurius, etc.)? | API | TBD |
| How auth is implemented (OIDC/OAuth2, API keys, RBAC)? | Security + API | TBD |
| What the canonical “Focus bundle” GraphQL query shape is | API + UI | TBD |
| What provenance fields are required in every response | Governance + API | TBD |

### Future extensions
- Extension point A: add domain-specific GraphQL modules (e.g., `Place`, `Event`, `Document`) without breaking contract semantics
- Extension point B: add “provenance directive” helpers so every resolver can attach evidence refs consistently (**not confirmed in repo**)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Layer]
  D --> E[GraphQL Server]
  E --> F[React/Map UI]
  F --> G[Story Nodes]
  G --> H[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant GQL as GraphQL API
  participant SVC as Backend Services
  participant Graph as Neo4j Graph
  UI->>GQL: FocusQuery(entity_id, options)
  GQL->>SVC: authorize + build resolver context
  SVC->>Graph: fetch subgraph + provenance refs
  Graph-->>SVC: nodes/edges + evidence IDs
  SVC-->>GQL: normalized payload
  GQL-->>UI: contracted response (data + provenance + audit flags)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| GraphQL operation | GraphQL query/mutation | Client | Schema validation + query complexity limits (**not confirmed in repo**) |
| Auth context | headers/token | Client | AuthN/AuthZ middleware |
| Graph + catalog data | service calls | Neo4j + catalog stores | Backend data validation + redaction rules |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| GraphQL response | JSON | over HTTP | GraphQL schema (typed) |
| Provenance references | IDs/URLs | embedded in response | STAC/DCAT/PROV identifier rules (governed) |
| Audit flags | JSON fields | embedded in response | “Audit panel expectations” (**not confirmed in repo**) |

### Sensitivity & redaction
- If a field can reveal sensitive locations or culturally sensitive information:
  - enforce authorization checks at resolver/service layer
  - generalize or omit restricted fields for public outputs
  - log access decisions in telemetry (without leaking restricted data)
- This README does not define new policy; it must defer to governed docs referenced by `governance_ref`, `ethics_ref`, and `sovereignty_policy`.

### Quality signals
- Schema-level validation (types, non-null where appropriate)
- Resolver-level guardrails (rate limits, query depth/complexity, pagination)
- Deterministic response shapes for the same request inputs (where practical)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If GraphQL returns geospatial/time assets, responses should include:
  - STAC Collection IDs and Item IDs (or resolvable references)
  - asset URLs/paths with appropriate access controls

### DCAT
- For dataset-level responses, include:
  - dataset identifier(s)
  - license and publisher references as appropriate

### PROV-O
- For derived/curated outputs (e.g., story nodes, extracted entities), include:
  - `prov:wasDerivedFrom` (source IDs)
  - `prov:wasGeneratedBy` (pipeline run/activity ID)
- Field naming is **not confirmed in repo**; adopt a consistent convention and document it in API contract docs when implemented.

### Versioning
- GraphQL schema changes that affect clients should follow semver + deprecation policy (**not confirmed in repo**) and must be documented via an API Contract Extension doc.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Schema | Type system + operations | GraphQL SDL / code-first equivalent |
| Resolvers | Map fields to backend services | Resolver map |
| Context | Auth + request-scoped state | Request lifecycle |
| Data loaders | Batch/cache backend calls | Dataloader pattern (recommended) |
| Backend services | Neo4j + catalog adapters | Internal service API |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| GraphQL schema | `src/server/graphql/` | Changes require contract review + tests |
| Contract change doc | `docs/` via template | Use `TEMPLATE__API_CONTRACT_EXTENSION.md` |
| JSON schemas | `schemas/` | Semver + changelog |

### Extension points checklist (for future work)
- [ ] Add a new GraphQL type/module without breaking existing clients
- [ ] Add provenance refs to new fields by default
- [ ] Add auth/redaction directives where needed
- [ ] Add contract tests for any new query/mutation
- [ ] Add telemetry signals for error rates and sensitive-field denials

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- GraphQL should support retrieving narrative + evidence for a focusable entity (Place/Event/Person/Document).
- Responses should include citations/evidence identifiers to render in UI audit panels.

### Provenance-linked narrative rule
Every user-visible claim in Focus Mode must trace to a dataset / record / asset ID (STAC/DCAT/PROV or source document identifiers).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] GraphQL schema validation / lint (tooling **not confirmed in repo**)
- [ ] Resolver unit tests (if present)
- [ ] API integration tests (GraphQL endpoint)
- [ ] Contract tests for public operations (queries/mutations used by UI)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Commands are not confirmed in repo — replace with the project’s actual scripts.
# Example intent only:
# 1) lint GraphQL schema
# 2) run server tests
# 3) run contract tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Query latency | GraphQL server | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed in repo**) |
| Auth denials | Auth middleware | telemetry logs |
| Resolver error rate | GraphQL server | telemetry logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- GraphQL contract changes: API + governance review (and security review if auth/redaction changes)
- New sensitive fields: sovereignty/ethics review as required by referenced governance docs

### CARE / sovereignty considerations
- Do not expose sensitive locations or culturally restricted information in public GraphQL responses.
- Prefer generalized geometry and redacted attributes where required.

### AI usage constraints
- The GraphQL layer must not generate unsourced narrative.
- Any AI-derived fields must be explicitly labeled, provenance-linked, and opt-in.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README scaffold for `src/server/graphql/` | TBD |

---
Footer refs:
- Architecture baseline: `docs/MASTER_GUIDE_v12.md`
- API contract change process: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

