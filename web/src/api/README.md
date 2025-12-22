---
title: "KFM Web — API Client Layer (web/src/api)"
path: "web/src/api/README.md"
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

doc_uuid: "urn:kfm:doc:web:api:readme:v1.0.0"
semantic_document_id: "kfm-web-api-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:api:readme:v1.0.0"
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

# KFM Web API Client Layer

## 📘 Overview

### Purpose

This directory is the **frontend API client boundary** for Kansas Frontier Matrix (KFM). It defines how the React/Map UI calls KFM backend services **without** bypassing the API layer.

This README governs:

- **Where** API-call code lives (`web/src/api/`).
- **How** requests are made (one transport + consistent auth + consistent error handling).
- **What must be preserved** across the boundary (IDs, provenance references, redaction expectations).

### Scope

| In Scope | Out of Scope |
|---|---|
| Frontend HTTP client utilities (fetch wrappers, headers, auth token injection) | Defining backend endpoints (belongs under `src/server/` + docs) |
| Request/response typing strategy (manual types or generated types) | Direct graph access (UI never queries Neo4j directly) |
| Error normalization + retry/backoff guidelines | ETL, catalog building, graph ingest |
| Contract-sync workflow (how frontend stays aligned with backend contracts) | Writing Story Nodes (belongs under `docs/reports/.../story_nodes/`) |

### Audience

- **Primary:** Frontend engineers working in `web/`.
- **Secondary:** Backend/API engineers (contract evolution), QA/validation reviewers, governance reviewers (safety/redaction boundary).

### Definitions

- **API boundary:** The server contract layer (REST/GraphQL) that mediates all access to catalogs/graph/data products.
- **Contract artifact:** A machine-validated API schema (e.g., OpenAPI JSON, GraphQL SDL) published by the server.
- **Provenance reference:** A stable ID or pointer to evidence (e.g., STAC item ID, DCAT dataset ID, PROV activity ID, source document/record ID).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants (ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode). |
| API contracts | `src/server/` + docs | API Team | Source of truth for endpoint shapes and redaction rules. |
| Data schemas | `schemas/` | DataOps | JSON Schema for STAC/DCAT/PROV and other governed artifacts. |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story Team | Requires provenance-linked narrative. |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] This README describes the **single, canonical** frontend API boundary (no duplicate “mystery clients” elsewhere in `web/`).
- [ ] No secrets, tokens, or environment-specific URLs are committed in examples.
- [ ] Validation steps are listed (even if commands are placeholders).

## 🗂️ Directory Layout

### This document

- `path`: `web/src/api/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed data; STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Ontology bindings, graph build tooling |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Schemas | `schemas/` | JSON schemas (validation contracts) |
| **Backend APIs** | `src/server/` | REST/GraphQL services + contract artifacts |
| Frontend | `web/` | React + map UI, including this API client boundary |

### Expected file tree for this sub-area

> The non-README entries below are **recommended** structure (not confirmed in repo). Keep it minimal unless/until the code exists.

~~~text
📁 web/
└── 📁 src/
    └── 📁 api/
        ├── 📄 README.md
        ├── 📄 index.ts                 # public exports (recommended)
        ├── 📄 transport.ts             # fetch wrapper (recommended)
        ├── 📄 auth.ts                  # token wiring (recommended)
        ├── 📄 errors.ts                # normalized error types (recommended)
        ├── 📁 endpoints/               # endpoint modules by domain (recommended)
        │   └── 📄 focus.ts             # Focus Mode fetches (example name; not confirmed)
        ├── 📁 contracts/               # contract snapshots or generated types (recommended)
        │   └── 📄 openapi.json         # if checked-in (not confirmed)
        └── 📁 __tests__/               # client/contract tests (recommended)
            └── 📄 transport.test.ts
~~~

## 🧭 Context

### Background

KFM’s UI must consume many evidence-backed data products (catalog metadata, graph-derived context bundles, Story Node artifacts). A centralized `web/src/api/` layer prevents:

- duplicated request logic (headers/auth/error handling scattered across UI components),
- accidental direct coupling to implementation details (graph queries, storage paths),
- loss of provenance identifiers needed for citations, audits, and Focus Mode.

### Assumptions

- The backend publishes **versioned** API contracts (format and location not confirmed in repo).
- The UI has an environment-specific **API base URL** injected at build/runtime (specific env var naming not confirmed in repo).
- Redaction/sensitivity enforcement occurs **server-side**; the UI treats missing/redacted fields as expected.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **UI never reads Neo4j directly.** All graph access is mediated by `src/server/` APIs.
- Client code must not log secrets (tokens) or attempt to “reconstruct” redacted fields.
- Inputs that cross the boundary (query params, filters) must be treated as untrusted and sanitized/encoded appropriately.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| REST, GraphQL, or both for UI consumption? | TBD | TBD |
| Contract strategy: generated client from OpenAPI/GraphQL vs hand-written wrappers? | TBD | TBD |
| Caching strategy in UI (library + invalidation rules)? | TBD | TBD |
| Standard error envelope for all endpoints? | TBD | TBD |

### Future extensions

- Add a codegen pipeline that generates TypeScript types from API contracts (if adopted).
- Add contract tests that verify frontend assumptions against the published API schema.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  UI[React / Map UI] --> C[web/src/api (client boundary)]
  C --> API[src/server (REST/GraphQL APIs)]
  API --> CAT[STAC/DCAT/PROV catalogs]
  API --> G[Neo4j graph]
  API --> SN[Story Nodes store / renderer]
  UI --> FM[Focus Mode UI]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (Focus Mode)
  participant Client as web/src/api
  participant API as src/server
  participant Graph as Neo4j (server-side only)

  UI->>Client: getFocusBundle(entity_id, options)
  Client->>API: GET /focus?entity_id=...
  API->>Graph: fetch subgraph + evidence refs
  Graph-->>API: context bundle
  API-->>Client: focus bundle + provenance references
  Client-->>UI: typed data + normalized errors
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API base URL | string | build/runtime config | must be a valid URL |
| Auth credentials | bearer token / session | auth provider | never logged; injected via headers |
| Request params | query/body | UI state | encode/sanitize; type-check |
| Responses | JSON (sometimes GeoJSON/STAC/DCAT/PROV JSON) | `src/server/` | validate shape via types/guards (strategy not confirmed) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Typed UI data | TS types | `web/src/api/*` | derived from API contract |
| Normalized errors | typed error objects | `web/src/api/errors.*` (recommended) | consistent envelope across endpoints |
| Provenance IDs | strings/objects | returned with domain payloads | must be preserved for citation rendering |

### Sensitivity & redaction

- Treat redaction as **normal**: null/missing fields must not break rendering.
- Do not add client-only workarounds that leak/guess sensitive locations or identities.
- Do not store tokens in local logs or analytics events.

### Quality signals

- Request success rate / error rate per endpoint (telemetry location not confirmed in repo).
- Presence of provenance references for any “claim-like” UI element (e.g., a narrative sentence, an entity summary).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- If the API returns STAC Collections/Items directly, the client should:
  - preserve `id`, `links`, and asset identifiers as-is,
  - avoid rewriting `href` unless explicitly required by contract,
  - treat broken links as a server/data issue (surface gracefully in UI).

### DCAT

- If the API returns DCAT datasets, the client should render:
  - license and attribution fields when present,
  - publisher/contact fields when present (subject to redaction rules).

### PROV-O

- If the API returns provenance bundles or provenance pointers:
  - preserve `prov:wasDerivedFrom`, `prov:wasGeneratedBy`, and activity/agent IDs,
  - keep provenance pointers attached to the UI objects they justify (so citations remain stable).

### Versioning

- The client should assume the API is **contract-first**:
  - breaking changes require a contract version bump (server-side),
  - frontend updates should be tied to that contract change (tests recommended).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| `transport` | HTTP request wrapper (timeouts, headers, JSON parsing) | `request(method, path, opts)` |
| `auth` | attach credentials to requests | `getAuthHeaders()` |
| `endpoints/*` | domain-oriented API calls | `getX()`, `searchY()` |
| `errors` | normalize server/network errors | `ApiError` / `ProblemDetails` (names not confirmed) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API schema | `src/server/` + docs | semver + contract tests |
| STAC/DCAT/PROV schemas | `schemas/` | profile version bumps as needed |
| UI consumption boundary | `web/src/api/` | must track server contract version |

### Extension points checklist

- [ ] Add new endpoint module under `web/src/api/endpoints/`
- [ ] Add/extend types (generated or manual)
- [ ] Add tests (mock transport + contract expectations)
- [ ] Ensure provenance references remain attached to returned objects
- [ ] Update UI callers to use the centralized API boundary (no ad-hoc `fetch()` in components)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode screens should fetch a **single focus bundle** (entity + context + evidence pointers) through `web/src/api/`.
- UI components must render citations/attribution using provenance references provided by the API (not invented client-side).

### Provenance-linked narrative rule

- Any narrative text rendered in the UI that implies a claim should be accompanied by a provenance reference:
  - dataset ID (DCAT),
  - item/asset ID (STAC),
  - activity/agent reference (PROV),
  - or source document/record identifier.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter keys present; no forbidden fields)
- [ ] Type-check frontend API layer (TypeScript)
- [ ] Contract alignment checks (client assumptions vs server schema)
- [ ] Unit tests for transport/auth/error normalization
- [ ] Security checks: no secrets in repo; safe logging

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) lint + type-check the web app
# (e.g., npm/pnpm/yarn — not confirmed in repo)
# <package-manager> -C web run lint
# <package-manager> -C web run typecheck

# 2) run tests
# <package-manager> -C web test

# 3) docs lint (if configured)
# <package-manager> run docs:lint
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| API latency p95 | browser + server | `docs/telemetry/` + `schemas/telemetry/` (not confirmed) |
| API error rate | transport | same |
| Missing provenance refs | UI assertion | same |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to authentication handling, request logging, or anything that could affect redaction/sensitivity should be flagged **requires human review**.
- Changes that alter how provenance is displayed or stored should be reviewed for compliance with Story Node and Focus Mode rules.

### CARE / sovereignty considerations

- If an endpoint returns culturally sensitive or community-sensitive materials, the UI must respect server-provided redaction/generalization.
- Do not add client-side “enhancements” that increase specificity of protected locations or identities.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for frontend API client boundary | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

