---
title: "Kansas Frontier Matrix — API Layer"
path: "src/api/README.md"
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

doc_uuid: "urn:kfm:doc:src:api:readme:v1.0.0"
semantic_document_id: "kfm-src-api-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:api:readme:v1.0.0"
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

# Kansas Frontier Matrix — API Layer

## 📘 Overview

### Purpose
- Define what belongs in `src/api/` and how the API layer participates in the KFM pipeline.
- Document the contract-first expectations for endpoints that expose graph/catalog-backed content to downstream consumers (UI, Story Nodes, Focus Mode).

### Scope
| In Scope | Out of Scope |
|---|---|
| API service code under `src/api/` | ETL pipelines (`src/pipelines/`) |
| Request routing, handlers/controllers, middleware | Graph ontology/migrations (`src/graph/`, `docs/graph/`) |
| Response shaping to match contracts (REST/GraphQL) | Frontend implementation (`web/` or repo-specific UI path) |
| Provenance packaging and sensitivity handling at the API boundary | Raw dataset storage (`data/raw/`) |

### Audience
- Primary: API/backend contributors maintaining the contracted access layer.
- Secondary: Graph contributors, UI contributors, Story Node authors, data stewards.

### Definitions
- **Contract**: The documented REST/GraphQL interface (OpenAPI/GraphQL schema) that clients rely on.
- **Contract tests**: Automated tests asserting the implementation matches the contract and remains backward compatible.
- **Provenance refs**: Stable identifiers linking API outputs back to STAC/DCAT/PROV artifacts.
- **Redaction/generalization**: Rules that omit or coarsen sensitive fields/locations before public output.
- **Focus Mode**: A narrative UX mode that must only consume provenance-linked content.
- Link to glossary: `docs/glossary.md` (not confirmed in repo)

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + subsystem contracts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | Use for endpoint changes |
| Graph model docs | `docs/graph/` | TBD | Labels, relationships, constraints |
| Schemas | `schemas/` | TBD | STAC/DCAT/telemetry/API schemas |
| Tests | `tests/` | TBD | Contract + integration tests |
| Governance policies | `docs/governance/` | TBD | Ethics, sovereignty, approvals |

### Definition of done
- [ ] Front-matter complete and valid
- [ ] Purpose/scope clearly describes what belongs in `src/api/`
- [ ] Links to canonical contracts/templates are present
- [ ] Contract-testing expectations are stated (backward compat or version bump)
- [ ] Sensitivity/redaction expectations are stated
- [ ] Validation steps are listed and repeatable
- [ ] Open questions and “not confirmed in repo” assumptions are captured (if any)

## 🗂️ Directory Layout

### This document
- `path`: `src/api/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/catalog outputs by domain |
| Documentation | `docs/` | Canonical governed docs, contracts, governance |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Graph | `src/graph/` | Neo4j graph build + ontology bindings |
| API service | `src/api/` | This directory: API implementation (repo-specific) |
| API service | `src/server/` | Canonical API location per Master Guide v12 (verify/reconcile) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/telemetry/API) |
| Tests | `tests/` | Contract + integration tests |
| UI | `web/` | React + map clients (repo-specific path may differ) |

### Expected file tree for this sub-area
~~~text
📁 src/api/
├── 📄 README.md
├── 📁 contracts/
│   ├── 📄 openapi.<ext>                 # not confirmed in repo
│   └── 📄 graphql_schema.<ext>          # not confirmed in repo
├── 📁 routes/
│   └── 📄 <routes-and-endpoints>        # not confirmed in repo
├── 📁 handlers/
│   └── 📄 <request-handlers>            # not confirmed in repo
├── 📁 services/
│   └── 📄 <domain-services>             # not confirmed in repo
├── 📁 adapters/
│   ├── 📁 graph/
│   │   └── 📄 <neo4j-adapters>          # not confirmed in repo
│   └── 📁 catalogs/
│       └── 📄 <stac-dcat-prov-adapters> # not confirmed in repo
└── 📁 middleware/
    ├── 📄 auth.<ext>                    # not confirmed in repo
    └── 📄 redaction.<ext>               # not confirmed in repo
~~~

### Content ownership
- Code ownership: TBD
- Contract ownership: TBD
- Reviewers: TBD

### On-call and incident info
- Not confirmed in repo

## 🧭 Context

### Background
KFM’s API layer provides the **contracted access layer** between the graph/catalog layer and downstream consumers (UI and narrative experiences). This directory documents the expected responsibilities and boundaries of that API layer.

### Assumptions
- API responses are contract-shaped (OpenAPI and/or GraphQL) and covered by tests.
- API responses can include provenance references (STAC/DCAT/PROV IDs) when data originates from governed artifacts.
- Sensitive fields are redacted/generalized at the API boundary before public exposure.

### Constraints and invariants
- Preserve the canonical pipeline ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Backward compatibility must be maintained, or a version bump/deprecation path must be defined.
- No secrets/credentials in-repo; configs must be injected via approved mechanisms.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Is the runtime API implemented in `src/api/` or `src/server/` in this repo? | TBD | TBD |
| Where do OpenAPI/GraphQL contract files live in this repo? | TBD | TBD |
| What framework/runtime is used (FastAPI, Flask, Node, etc.)? | TBD | TBD |
| What is the standard error envelope and request-id behavior? | TBD | TBD |
| What is the redaction/generalization policy for sensitive locations? | TBD | TBD |

### Future extensions
- Add new endpoints that return provenance-linked context bundles for Focus Mode.
- Add structured “evidence artifacts” endpoints aligned to STAC assets.
- Add telemetry hooks aligned with `schemas/telemetry/`.

## 🗺️ Diagrams

### System and dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Layer]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as UI
  participant API as API
  participant Graph as Graph
  UI->>API: Request (contracted)
  API->>Graph: Query (apply redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>UI: Response (contracted payload + refs)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Client requests | HTTP/JSON | UI, tools, other clients | Contract schema + request validation |
| Entity identifiers | string/UUID | UI/Story/Focus | Existence + authorization checks |
| Query constraints | params/body | UI/clients | Range limits, pagination, allowlists |

### Outputs
| Output | Format | Delivery | Contract / Schema |
|---|---|---|---|
| Contracted API responses | JSON | HTTP | OpenAPI/GraphQL contract |
| Geo features | GeoJSON-like JSON | HTTP | Contract + geometry validation rules |
| Provenance references | IDs/URIs | Embedded in payload | PROV/STAC/DCAT mappings (as applicable) |

### Sensitivity and redaction
- Identify any fields requiring generalization or omission for public outputs.
- If returning location-bearing data, document:
  - whether coordinates are precise vs generalized
  - what authorization gates exist
  - whether audit/logging is required
- If sensitive behavior exists, it must be documented in the endpoint contract extension docs.

### Quality signals
- Schema validity (request/response)
- Geometry validity and bounds checks
- Completeness checks (required fields present)
- Provenance completeness (refs present when required)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- When API responses surface catalog-backed assets, include stable STAC identifiers:
  - STAC Collection IDs
  - STAC Item IDs
- Prefer returning identifiers over duplicating full STAC JSON unless the endpoint is explicitly “catalog API”.

### DCAT
- When responses represent or aggregate datasets, include DCAT dataset identifiers and license/publisher metadata as appropriate.

### PROV-O
- When returning derived/curated information, include provenance pointers:
  - `prov:wasDerivedFrom` references
  - `prov:wasGeneratedBy` activity/run identifiers
- Avoid “source-less” narrative: provenance pointers are first-class.

### Versioning
- If an endpoint changes shape, document compatibility and versioning expectations.
- Link predecessor/successor where applicable and mirror lineage in the graph when relevant.

## 🧱 Architecture

### Component boundaries
- **Routes/handlers**: Map endpoints to application logic.
- **Services**: Domain logic for assembling responses from graph/catalog sources.
- **Adapters**: Integration with Neo4j and catalog stores; isolate query implementations.
- **Middleware**: Auth, rate limiting, redaction/generalization, request-id, logging.

### Key interfaces
- REST: OpenAPI specification and integration tests
- GraphQL: Schema lint and resolver tests
- Graph boundary: no direct UI access; all graph access occurs through API code and governed adapters

### Error handling strategy
- Use a consistent error envelope (not confirmed in repo).
- Include a request identifier for traceability (not confirmed in repo).
- Prefer explicit error codes over free-form strings.

### Performance and scaling
- Enforce pagination and bounded queries by default.
- Prefer server-side filtering and indexed graph queries.
- Consider caching for high-traffic read endpoints where it does not violate freshness requirements.

### Extension points checklist
- [ ] Add/modify endpoint
- [ ] Create a contract change doc using `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- [ ] Update OpenAPI/GraphQL schema artifacts
- [ ] Add/extend contract tests
- [ ] Verify sensitivity/redaction behavior
- [ ] Add telemetry events where applicable
- [ ] Update UI layer registry or client usage docs if needed

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode should call API endpoints that return provenance-linked context bundles.
- Any predictive or model-derived content must be opt-in and include uncertainty/confidence metadata.

### Provenance-linked narrative rule
- If an endpoint feeds Focus Mode, it must return:
  - provenance references for every major claim (or a reference bundle that can be resolved)
  - any redaction/generalization flags applied

### Optional structured controls
~~~yaml
focus_mode:
  include_provenance: true
  include_predictions: false
  max_hops: 2
  redaction_level: "public"
~~~

## 🧪 Validation and CI/CD

### Minimum validations
- [ ] Markdown protocol validation for governed docs
- [ ] JSON schema validation (STAC/DCAT/telemetry as applicable)
- [ ] Graph integrity tests (where API changes depend on graph semantics)
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] Security scanning gates (where applicable)

### How to run validations locally
~~~bash
# Not confirmed in repo: replace placeholders with repo-standard commands

# Run unit tests
<repo_test_command>

# Run API contract tests
<repo_contract_test_command>

# Run doc lint / markdown protocol validation
<repo_docs_lint_command>
~~~

### Telemetry signals
| Signal | Type | Why it matters |
|---|---|---|
| request_count | counter | Traffic baseline |
| request_latency_p95 | histogram | Performance regression detection |
| error_rate | gauge | Contract/infra issues |
| redaction_applied_count | counter | Safety posture visibility |
| provenance_missing_count | counter | Governance regression detection |

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- New public-facing endpoints
- New sensitive fields/layers or location precision changes
- New AI narrative behaviors or “Focus Mode” output paths
- New external data sources or license changes

### Sovereignty safety
- Document redaction/generalization rules for any restricted locations.
- Flag any culturally sensitive content handling for human review.

### Ethical use notes
- Avoid presenting derived/predictive output as fact.
- Ensure every factual claim can be traced to a governed source reference.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `src/api` README scaffold aligned to KFM doc protocol | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
