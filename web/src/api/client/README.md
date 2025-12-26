---
title: "KFM Web API Client — Governance & Usage"
path: "web/src/api/client/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:api-client-readme:v1.0.0"
semantic_document_id: "kfm-web-api-client-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:api-client-readme:v1.0.0"
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

# KFM Web API Client (`web/src/api/client/`)

This directory is the **single, governed** home for the web app’s API-client code: request construction, auth hooks, error normalization, caching/deduping, and *provenance-preserving* response handling.

It exists to enforce a core KFM invariant:

- The UI (`web/`) reads **only** from contracted API endpoints and catalog endpoints — **never** from Neo4j directly.

---

## 📘 Overview

### Purpose

- Provide a consistent, testable, contract-aligned way for the KFM UI to call the API boundary (`src/server/`) without bypassing governance.
- Centralize cross-cutting concerns:
  - base URL + environment wiring
  - auth & redaction-safe headers
  - retries/backoff (where allowed)
  - response validation (where schemas exist)
  - consistent error shaping for UI components

### Scope

| In Scope | Out of Scope |
|---|---|
| HTTP client wrapper(s), endpoint helpers, request/response types, error normalization, caching/dedupe, telemetry hooks | Business/domain logic, graph queries, writing derived datasets, embedding “unsourced narrative”, defining API contracts |

### Audience

- Primary: frontend maintainers building map/timeline/Focus Mode UI features.
- Secondary: API maintainers validating that client usage matches contracts; governance reviewers spot-checking boundary compliance.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add/repair link if glossary lives elsewhere)*

Terms used here:

- **API boundary**: the contracted access layer (REST/GraphQL) that the UI uses for all graph/catalog content.
- **Contract artifact**: machine-validated schema/spec (OpenAPI/GraphQL/JSON Schema) treated as canonical.
- **Evidence references**: stable identifiers pointing back to STAC/DCAT/PROV artifacts.
- **Provenance-linked**: a UI view is “provenance-linked” if every factual element can be traced to evidence references (directly or via the API payload).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering and boundary rules |
| API contracts | `src/server/contracts/` | API | Contract-first source of truth |
| API implementation | `src/server/` | API | Enforces redaction/generalization |
| Schemas | `schemas/` | Platform | JSON Schemas for catalogs/story/ui/telemetry |
| UI app | `web/` | Frontend | Only consumes API + catalog endpoints |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Must remain provenance-linked |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Directory responsibilities + boundary invariants stated (no direct graph reads)
- [ ] Recommended structure documented (and marked “not confirmed in repo” where applicable)
- [ ] Validation steps listed and repeatable (or explicitly “not confirmed in repo”)
- [ ] Governance + CARE/sovereignty considerations stated (PII, sensitive locations, caching)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/api/client/README.md` (must match front-matter)

### Expected file tree for this sub-area

> This is the **recommended** structure. Some files/directories may not exist yet (**not confirmed in repo**).  
> Keep this README synchronized with what actually exists under `web/src/api/client/`.

~~~text
📁 web/
└── 📁 src/
    └── 📁 api/
        └── 📁 client/
            ├── 📄 README.md                      # This file (governance + usage)
            ├── 📄 index.ts                       # Public exports (recommended)
            ├── 📄 http.ts                        # fetch/transport wrapper (recommended)
            ├── 📄 errors.ts                      # normalized error model (recommended)
            ├── 📄 types.ts                       # shared client types (recommended)
            ├── 📁 middleware/                    # cross-cutting hooks (recommended)
            │   ├── 📄 auth.ts                    # auth token injection (recommended)
            │   ├── 📄 tracing.ts                 # request-id/provenance headers (recommended)
            │   └── 📄 retry.ts                   # retry/backoff policy (recommended)
            ├── 📁 endpoints/                     # endpoint-specific helpers (recommended)
            │   ├── 📄 focus.ts                   # Focus Mode bundles (example)
            │   ├── 📄 places.ts                  # Place lookup/search (example)
            │   └── 📄 catalog.ts                 # STAC/DCAT discovery (example)
            └── 📁 __tests__/                     # unit/contract-ish tests (recommended)
                └── 📄 client.test.ts             # request/response shaping (example)
~~~

---

## 🧭 Context

KFM’s canonical flow is contract-first and provenance-first:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This client exists so the UI consistently stays on the **UI→API** side of that boundary and does not drift into:
- direct graph access,
- ad hoc endpoint calls scattered across components,
- “stringly typed” error handling,
- or Focus Mode content assembled without provenance.

---

## 🗺️ Diagrams

### Web request boundary (what this client enforces)

~~~mermaid
flowchart LR
  UI[web UI components] --> C[web/src/api/client]
  C --> API[src/server API boundary]
  API --> G[Neo4j graph]
  API --> E[Evidence refs: STAC/DCAT/PROV]
  UI <-->|contracted payload| API
~~~

---

## 📦 Data & Metadata

### Inputs

- UI intent: “fetch place context”, “load layer items”, “render Focus Mode bundle”, etc.
- Runtime configuration: API base URL and (optional) auth token source.

### Outputs

- Contracted JSON responses (plus headers) returned to UI components in a normalized shape:
  - success payloads include **evidence/provenance references** when the endpoint is Focus Mode or “narrative-adjacent”
  - errors are normalized into a predictable error type (status, code, message, request_id)

---

## 🌐 STAC, DCAT & PROV Alignment (Client-side expectations)

The API boundary is the place where catalog/provenance references are stitched into responses. The client should:

- **Preserve** evidence identifiers coming back from the API (do not drop or rename them casually).
- **Avoid manufacturing** provenance: the client may add request correlation metadata, but it must not invent citations, dataset IDs, or event claims.
- Prefer APIs that return explicit references to:
  - STAC Items/Collections (e.g., `stac_item_ids`, `stac_collection_id`)
  - DCAT dataset IDs
  - PROV activity/run IDs (e.g., `prov_activity_id`, `run_id`)

> Field names vary by contract; treat the contract as canonical.

---

## 🧱 Architecture

### Public surface

Recommended pattern:

- `index.ts`: exports a small, stable surface (`createClient`, `getFocusBundle`, etc.).
- `http.ts`: owns `fetch` wiring (timeouts, headers, JSON parsing).
- `middleware/*`: pure functions that decorate request options (auth, tracing, retry).
- `endpoints/*`: endpoint-level helpers; these should stay “thin” and contract-aligned.

### Configuration

This directory should support a single way to define the API base URL.

Because build tooling varies, the exact env var name is **not confirmed in repo**. Recommended conventions:
- `VITE_KFM_API_BASE_URL` (Vite-style), or
- `NEXT_PUBLIC_KFM_API_BASE_URL` (Next.js-style)

Document the actual variable used by the repo once confirmed.

### Error model (recommended)

Normalize all request failures into a single shape so UI components can behave consistently.

~~~ts
type KfmApiError = {
  name: "KfmApiError";
  status: number;
  code?: string;
  message: string;
  request_id?: string;
  cause?: unknown;
};
~~~

### Retries & caching

Only retry when it is safe and allowed by the API contract (idempotent GETs; avoid retries on writes unless explicitly supported).

Recommended:
- Request de-duping for identical in-flight GETs (prevents UI thundering herds).
- Short TTL caching for “static-ish” lookups (layer registries, vocab lists), if permitted.
- Never cache sensitive payloads in long-lived storage without a documented policy.

---

## 🧠 Story Node & Focus Mode Integration

If an endpoint feeds Focus Mode, the client must treat provenance as first-class:

- Keep provenance refs attached to the UI state (don’t discard them during transformations).
- Don’t “improve” narrative text on the client side.
- If the UI renders citations, it should render citations that come from:
  - Story Nodes (`docs/reports/story_nodes/`) and/or
  - API payload references to evidence artifacts

Client responsibility is delivery + integrity, not authorship.

---

## 🧪 Validation & CI/CD

Commands depend on repo tooling (**not confirmed in repo**). At minimum, this directory should be covered by:

- unit tests for:
  - request URL construction
  - header injection (auth/tracing)
  - error normalization
- (optional) contract-ish tests that validate example responses against schema/types if those exist.

If CI includes a “forbidden dependency” gate, this directory is an ideal place to enforce:
- no Neo4j drivers imported,
- no direct Cypher strings,
- no graph credentials usage.

---

## ⚖ FAIR+CARE & Governance

- **Do not log secrets** (tokens, cookies) or raw sensitive payloads.
- Treat any location-like payload as potentially sensitive if the API marks it so.
- Respect redaction/generalization decisions made at the API boundary (do not attempt to reverse them).
- If caching is used, document:
  - what is cached,
  - where (memory/session/local storage),
  - TTL,
  - and data sensitivity constraints.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial governed README for `web/src/api/client/` | TBD |

---

## ⚖️ Footer

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Canonical pipeline + invariants: `docs/MASTER_GUIDE_v12.md`
- API contracts: `src/server/contracts/`
~~~


