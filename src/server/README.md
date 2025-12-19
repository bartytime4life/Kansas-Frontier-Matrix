---
title: "src/server — API Layer README"
path: "src/server/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:src:server:readme:v1.0.0"
semantic_document_id: "kfm-src-server-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:server:readme:v1.0.0"
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

# src/server — API Layer

## 📘 Overview

### Purpose
`src/server/` implements KFM’s **API layer**: the contracted interface that serves data, narrative bundles, and provenance references to client applications.

This layer is responsible for:
- Enforcing the **API boundary** (clients do not read Neo4j directly).
- Returning **contracted payloads** (REST and/or GraphQL; exact implementation is not confirmed in repo).
- Applying **authorization + redaction/generalization** rules when data may be sensitive.
- Preserving **provenance-first behavior** by linking responses back to STAC/DCAT/PROV identifiers when applicable.

### Scope

| In Scope | Out of Scope |
|---|---|
| API endpoints + resolvers | ETL ingestion logic |
| Contract schemas + validation glue | STAC/DCAT/PROV catalog generation |
| Graph access via an API-owned adapter/client | Graph ontology/label design (lives under `src/graph/` + `docs/graph/`) |
| AuthN/AuthZ enforcement for API routes | Frontend rendering/UX (lives under `web/`) |
| Response redaction/generalization + audit hooks | Story Node authoring (lives under `docs/reports/.../story_nodes/`) |

### Audience
- Primary: Backend/API developers
- Secondary: Graph/pipeline developers integrating new capabilities; frontend developers consuming contracts

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo; add if missing)*
- Terms used in this doc: API boundary, contract, provenance, redaction/generalization, Focus Mode bundle

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| System pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering + subsystem locations |
| API contract change template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM maintainers | Use for any endpoint/schema changes |
| Schemas (payload validation) | `schemas/` | KFM maintainers | Exact schema files not confirmed in repo |
| Tests (contract + integration) | `tests/` | KFM maintainers | Exact test layout not confirmed in repo |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `src/server/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Graph | `src/graph/` | Neo4j graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalog build + graph build |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narrative artifacts |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |

### Expected file tree for this sub-area
*(Illustrative only — actual layout is not confirmed in repo.)*

~~~text
📁 src/
└── 📁 server/
    ├── 📄 README.md
    ├── 📁 contracts/                 # not confirmed in repo
    │   ├── 📁 openapi/               # not confirmed in repo
    │   └── 📁 graphql/               # not confirmed in repo
    ├── 📁 routes/                    # not confirmed in repo
    ├── 📁 middleware/                # not confirmed in repo
    ├── 📁 services/                  # not confirmed in repo
    │   ├── 📁 graph/                 # not confirmed in repo (Neo4j access adapters)
    │   ├── 📁 catalog/               # not confirmed in repo (STAC/DCAT/PROV helpers)
    │   └── 📁 provenance/            # not confirmed in repo
    ├── 📁 auth/                      # not confirmed in repo
    ├── 📁 telemetry/                 # not confirmed in repo
    └── 📁 config/                    # not confirmed in repo
~~~

## 🧭 Context

### Background
KFM’s canonical architecture routes all client access through a contracted API layer to keep the system loosely coupled, enforce governance, and ensure provenance is first-class.

### Assumptions
- The API layer is the only supported path for UI or external consumers to access graph-backed context.
- REST and/or GraphQL may be supported; exact protocol(s) and framework choices are **not confirmed in repo**.

### Constraints / invariants
- **Pipeline ordering is preserved:** ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
- **No direct graph dependency from the frontend.**
- Every narrative or “Focus Mode” payload must remain **provenance-linked**.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical API protocol surface (REST, GraphQL, both)? | TBD | TBD |
| Where are OpenAPI / GraphQL schemas stored (file paths)? | TBD | TBD |
| What is the auth mechanism (OIDC/OAuth2/RBAC), and where is it configured? | TBD | TBD |
| How are sensitivity rules expressed and tested (policy-as-code vs. hardcoded)? | TBD | TBD |

### Future extensions
- Add endpoints that serve “evidence products” (as assets) with explicit STAC + PROV references.
- Add contract-level toggles for opt-in predictive outputs (with uncertainty/confidence fields).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Neo4j Graph] --> B[API Layer: src/server/]
  B --> C[React/Map UI: web/]
  B --> D[External Clients]
  B --> E[Story Nodes + Focus Mode consumers]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API (src/server)
  participant Graph as Neo4j Graph
  UI->>API: Request (focus query / entity context)
  API->>Graph: Query (with redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>UI: Contracted payload (data + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Graph query parameters | JSON / query args | UI + other clients | Request schema + type checks |
| Graph results | records/rows | Neo4j | Server-side shape validation |
| Catalog references | IDs/URIs | STAC/DCAT/PROV outputs | ID format + resolvability checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| API response payloads | JSON | served by API | OpenAPI/GraphQL schema (not confirmed in repo) |
| Provenance references | IDs/links | included in payloads | Required fields per contract |

### Sensitivity & redaction
- If responses can expose sensitive information, the API must:
  - enforce authorization,
  - generalize/redact protected fields,
  - record auditable decision signals (what was withheld and why, without leaking the withheld content).

### Quality signals
- Completeness (required fields present)
- Provenance completeness (references resolve)
- Geometry validity (if returning geospatial features)
- Deterministic response shape for the same request (excluding time-dependent fields)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- The API should return **STAC Item IDs** for any spatial/temporal assets referenced in responses.
- Where applicable, include links to related Collection IDs.

### DCAT
- Where a response represents a dataset (or slice of one), include the **DCAT dataset identifier** (or a stable equivalent mapping).

### PROV-O
- Include provenance hooks:
  - `prov:wasDerivedFrom`: source identifiers (assets/records)
  - `prov:wasGeneratedBy`: pipeline activity/run identifier (if the data was produced by a run)

### Versioning
- Where contract payloads include versioned entities, include predecessor/successor identifiers when applicable.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| API runtime | Serve contracted responses | REST/GraphQL (exact not confirmed in repo) |
| Auth layer | AuthN/AuthZ + role gating | Middleware/hooks |
| Graph adapter | Query graph + map results | Internal service interface |
| Catalog adapter | Resolve STAC/DCAT/PROV refs | Internal service interface |
| Redaction layer | Apply sensitivity rules | Response shaping |
| Telemetry | Emit audit + reliability signals | Schema-validated events |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API change spec | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Use for change review + tests |
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + `docs/` | Contract tests required |

### Extension points checklist (for future work)
- [ ] Add endpoint(s) with explicit provenance fields
- [ ] Add/extend schema(s) under `schemas/`
- [ ] Add contract tests under `tests/`
- [ ] Add redaction/generalization rules + regression tests
- [ ] Add telemetry signals + schema version bump (if applicable)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode requests should be satisfied with a **provenance-linked context bundle**.
- Any predictive/AI-assisted content must be explicitly marked and carry uncertainty/confidence metadata (if supported).

### Provenance-linked narrative rule
- Every claim in any narrative payload must trace to a dataset / record / asset ID.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (where applicable)
- [ ] Schema validation (OpenAPI/GraphQL + JSON Schema)
- [ ] Graph integration tests (query + mapping)
- [ ] API contract tests (backward compatibility)
- [ ] Security + sovereignty scanning gates (as applicable)

### Reproduction
~~~bash
# Placeholders — replace with repo-specific commands (not confirmed in repo).
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Access decisions (allow/deny) | API auth layer | `docs/telemetry/` + `schemas/telemetry/` (paths not confirmed in repo) |
| Redaction applied | Response shaping | same as above |
| Contract test coverage | CI | test reports |

## ⚖ FAIR+CARE & Governance

### Review gates
- Endpoint changes that expose new fields or new data sources may require governance review.
- Any changes that touch sensitive content require explicit review and testing of redaction/generalization behavior.

### CARE / sovereignty considerations
- Follow sovereignty policy for any culturally sensitive locations/content.
- Prefer generalization over disclosure when uncertainty exists.

### AI usage constraints
- No “generate policy” behavior from AI tooling.
- No inferring sensitive locations for public outputs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `src/server` README scaffold | TBD |

