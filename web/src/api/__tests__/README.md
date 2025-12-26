---
title: "Web API Client — Tests (README)"
path: "web/src/api/__tests__/README.md"
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

doc_uuid: "urn:kfm:doc:web:src:api:tests:readme:v1.0.0"
semantic_document_id: "kfm-web-api-tests-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:api:tests:readme:v1.0.0"
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

# Web API Client — Tests

This directory contains tests for the **web UI’s API client layer** (`web/src/api/**`). These tests exist to keep the UI aligned with the **API boundary contracts**, enforce “no direct graph access,” and ensure response parsing remains stable as contracts evolve.

## 📘 Overview

### Purpose

- Provide a single, governed reference for how to write and maintain tests under `web/src/api/__tests__/`.
- Keep the UI’s API client behavior aligned to contract expectations (paths, parameters, error handling, and provenance/citation fields where applicable).
- Prevent architectural drift (e.g., accidental direct access to graph/database layers).

### Scope

| In Scope | Out of Scope |
|---|---|
| Unit/integration tests for request builders, query param serialization, headers/auth hooks, and response parsing in `web/src/api/**` | Backend API contract tests (server-side), Neo4j/graph tests, ETL/catalog validation |
| Deterministic tests using network mocks/fakes (no real network) | End-to-end browser/UI tests (Playwright/Cypress/etc. — not documented here) |
| Regression coverage for “Focus Mode / context bundle” fetching semantics (as implemented in this repo) | Story Node authoring rules (see `docs/templates/TEMPLATE__STORY_NODE_V3.md`) |

### Audience

- Primary: Web/UI contributors working in `web/`
- Secondary: API contributors reviewing client/server contract alignment; QA/release reviewers validating CI gates

### Definitions (link to glossary)

- Link: `docs/glossary.md` (if missing, treat as **not confirmed in repo** and add/repair the link)
- Terms used in this doc:
  - **API boundary:** the server layer (canonical root is `src/server/`) that mediates access to graph + catalogs and enforces redaction/generalization.
  - **Contracts:** versioned OpenAPI / GraphQL / JSON schema artifacts used to ensure producers and consumers evolve safely.
  - **Focus Mode / context bundle:** UI mode that requests a packaged payload for an entity/story (exact endpoint shape is repo-specific).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/api/__tests__/README.md` | Web team | Test rules + conventions |
| Web API client code | `web/src/api/**` | Web team | Centralized API I/O surface |
| API contracts | `src/server/contracts/**` | API team | Canonical contract artifacts (if adopted in this repo layout) |
| Master pipeline rules | `docs/MASTER_GUIDE_v12.md` | KFM core | Non-negotiable ordering + boundaries |
| v13 blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch team | Canonical roots + CI minimums |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches this file)
- [ ] Directory layout section contains an accurate, minimal tree for this sub-area
- [ ] Clear rules for: determinism, mocking, fixtures, and contract alignment
- [ ] Constraints/invariants explicitly state “no UI direct-to-graph reads”
- [ ] Validation steps are repeatable (commands may be placeholders if tooling isn’t finalized)
- [ ] Governance + CARE/sovereignty considerations cover test fixtures (no sensitive/PII)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/api/__tests__/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| API boundary | `src/server/` | Auth, redaction, contract-serving APIs |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL/contract artifacts (if present) |
| Graph | `src/graph/` | Ontology bindings + ingest logic (UI must not depend on this) |
| Schemas | `schemas/` | Schema registry (STAC/DCAT/PROV/story/ui/telemetry) |
| UI | `web/` | React + map clients (MapLibre/Cesium if present) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narratives consumed by UI |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 src/
    └── 📁 api/
        └── 📁 __tests__/
            ├── 📄 README.md
            ├── 📄 <api_module>.test.<ts|tsx>          # naming depends on test runner (not confirmed in repo)
            ├── 📁 fixtures/                           # optional; prefer synthetic fixtures
            └── 📁 helpers/                            # optional; shared mock builders
~~~

## 🧭 Context

### Background

KFM’s user-facing web app is intentionally “thin” in data authority: it **renders** content and context, but does not define truth. Truth is produced by upstream pipeline stages (ETL → catalogs → graph) and mediated through the **API boundary**.

API client tests are a key guardrail because they:
- keep the UI aligned with changing API contracts,
- prevent accidental bypass of governance/redaction at the API boundary,
- ensure “Focus Mode” and narrative views remain provenance-linked and stable.

### Assumptions

- The canonical pipeline ordering is preserved:
  - **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- The UI (`web/`) does **not** query Neo4j directly; graph access is mediated by `src/server/`.
- Contract artifacts exist (OpenAPI and/or GraphQL and/or schema definitions) and are treated as authoritative for payload shapes.

### Constraints / invariants

- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via the API boundary (`src/server/`).
- **Contracts are canonical:** API payload contracts must be versioned and validated (at minimum in CI for the server; client tests should not contradict them).
- **Determinism:** tests in this directory must not require real network calls, real API tokens, or real databases.
- **Fixtures are safe:** do not commit fixtures containing PII, restricted coordinates, or culturally sensitive details. Prefer synthetic, minimal objects.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the exact web test runner/tooling (Jest/Vitest/etc.) and which file suffix patterns does it collect? | TBD | TBD |
| What is the project-standard HTTP mocking approach (fetch mock, MSW, test server, etc.)? | TBD | TBD |
| Where is the canonical “API base URL” configured for the web app (env var name / runtime config)? | TBD | TBD |

### Future extensions

- Add contract-driven test generation (e.g., generate test vectors from `src/server/contracts/**`) — only after the contract format is finalized.
- Add “negative tests” for security drift (e.g., lint/test rule that blocks imports that indicate direct database access).
- Add CI gate that fails if any test fixture includes restricted coordinate precision (requires governance + tooling agreement).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR

  UI[UI<br/>web/] --> Client[API client<br/>web/src/api]
  Client --> API[API boundary<br/>src/server]
  API --> Graph[Graph<br/>Neo4j]
  API --> Catalogs[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  UI --> Story[Story Nodes<br/>docs/reports/story_nodes]
  Story --> Focus[Focus Mode<br/>provenance-linked only]

  subgraph Tests[This directory]
    T[API client tests<br/>web/src/api/__tests__]
  end

  T --> Client
~~~

### Optional: sequence diagram (Focus Mode fetch)

> This is an illustrative interaction. Exact endpoint names/params are **repo-specific**.

~~~mermaid
sequenceDiagram
  participant Test as Test
  participant Client as Web API Client
  participant Net as Network Mock
  participant API as API Boundary

  Test->>Client: getFocusContext(entityId, options)
  Client->>Net: HTTP GET /focus/{entityId}?<params>
  Net-->>Client: 200 OK (context bundle)
  Client-->>Test: parsed ContextBundle
  Note over Client,Test: Assert URL, params, headers, and parsing/error handling
~~~

## 🧠 Story Node & Focus Mode Integration

Even though these are “API client tests,” they directly protect Focus Mode integrity.

Test expectations (as applicable to implemented endpoints):
- The client preserves provenance-linked fields returned from the API (evidence IDs, references, audit flags, etc.).
- The client does not silently drop “redaction/generalization” notices that the API boundary may attach.
- If the system supports opt-in AI/predictive content, the client must treat it as **explicitly requested** and clearly separable from factual content (the UI should not display AI content by default).

Recommended test pattern:
- Prefer “contract-shaped minimal fixtures”:
  - include the smallest valid payload that still tests parsing behavior,
  - include at least one citation/provenance reference example where the UI depends on it.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Run the web unit/integration test suite that includes `web/src/api/__tests__/`.
- Run web lint + typecheck (to catch breaking changes in types and imports).
- Run secret scans (ensure no tokens appear in tests/fixtures).
- If contracts/types are generated: ensure generated outputs are stable and version-pinned (process documented elsewhere).

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# From repo root:

# 1) Install dependencies (package manager not confirmed in repo)
# npm install
# pnpm install
# yarn install

# 2) Run web tests (runner not confirmed in repo)
# npm test
# npm run test:web

# 3) (Recommended) Run typecheck + lint
# npm run typecheck
# npm run lint
~~~

### Telemetry signals (optional)

| Signal | Source | Where recorded |
|---|---|---|
| Web test suite result | CI | CI logs/artifacts |
| Contract drift detected | CI | contract test report (server-side) |
| Fixture policy violation | CI | security/PII scan output |

## 📦 Data & Metadata

### Fixtures policy

- Prefer **synthetic** test data.
- If you must include geometry/coordinates:
  - use generalized/dummy coordinates (avoid real sensitive sites),
  - keep precision low unless the contract requires it.
- If you include IDs that “look real,” ensure they are clearly fake/non-resolving (e.g., prefix with `test-`).

### What should never be committed here

- API keys, tokens, session cookies
- PII (names, personal addresses, emails) unless explicitly approved and minimized
- Restricted location coordinates or culturally sensitive location markers
- Large raw data dumps (belongs under `data/**` with governance, not under web tests)

## 🌐 STAC, DCAT & PROV Alignment

The web client may receive or reference STAC/DCAT/PROV identifiers via API responses. When relevant:
- Treat provenance IDs as **first-class**: preserve them through parsing and don’t “normalize away” critical identifiers.
- Avoid mutating provenance-linked payloads in-place; prefer immutable transforms so audit trails stay clear.
- If the client fetches catalogs directly (STAC/DCAT endpoints), ensure test fixtures align with the project’s schema expectations.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| `web/src/api/**` | Centralized HTTP requests + parsing for the UI | Calls API boundary + (optionally) catalog endpoints |
| `web/src/api/__tests__/**` | Regression protection for client behavior | Deterministic tests with network mocks |
| `src/server/contracts/**` | Contract sources for API payloads | Versioned artifacts validated in CI (server-side) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/**` | semver + contract tests |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | semver + validation |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | semver + changelog |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that could expand access to sensitive/restricted information (even via fixtures) require governance review (approval routing **not confirmed in repo** — follow `docs/governance/ROOT_GOVERNANCE.md`).
- Any change that risks bypassing the API boundary (direct graph access) must be treated as a blocking architecture violation.

### CARE / sovereignty considerations

- Treat fixtures as publishable artifacts: do not include culturally sensitive knowledge or restricted location details.
- Prefer aggregation/generalization and synthetic fixtures for any location-linked tests.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing (consistent with front-matter).
- Prohibited: generating new policy; inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/api/__tests__/README.md` scaffold | TBD |

---

### Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty policy: `docs/governance/SOVEREIGNTY.md`

