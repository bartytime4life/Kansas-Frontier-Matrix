---
title: "KFM Web UI — Test Guide"
path: "web/src/test/README.md"
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

doc_uuid: "urn:kfm:doc:web:test-readme:v1.0.0"
semantic_document_id: "kfm-web-test-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:test-readme:v1.0.0"
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

# KFM Web UI Test Guide

## 📘 Overview

### Purpose

`web/src/test/` is the shared home for **web UI test utilities** (fixtures, factories, mocks, helpers) and the
rules we expect tests to follow.

This guide is written to keep tests aligned with KFM’s architectural boundaries:

- The web UI is a consumer of **API contracts**, not a direct consumer of the graph layer.
- Tests should reinforce “contract-first” behavior (types/shapes from the API layer are the source of truth).

### Scope

| In Scope | Out of Scope |
|---|---|
| Unit/integration test utilities for `web/` | ETL, catalog, graph, or server tests (see their subsystem homes) |
| Mocking APIs and map engine seams | Writing/defining API contracts themselves |
| Fixtures for Story Nodes / Focus Mode UI rendering | Publishing Story Nodes / narrative authoring standards |

### Audience

- Primary: Web UI developers working in `web/`
- Secondary: API/contract owners who need UI expectations for contract changes

### Definitions

- **Unit test:** Tests a single function/component with minimal dependencies.
- **Integration test:** Tests multiple modules/components together (often with mocked network).
- **E2E test:** Tests the running app via a browser automation tool.
- **Contract test:** Verifies request/response shapes match API contracts (OpenAPI/GraphQL/JSON Schema).
- **Focus Mode:** UI mode that surfaces provenance-linked narrative context.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + subsystem homes | `docs/MASTER_GUIDE_v12.md` | Maintainers | UI is downstream of API boundary |
| v13 UI/graph boundary invariant | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | “No UI direct-to-graph reads” |
| API contracts | `src/server/contracts/` | API owners | UI tests should follow these shapes |
| UI schemas (layer registry, etc.) | `schemas/ui/` | UI/Contracts owners | Use for registry validation tests |

### Definition of done

- [ ] New test utilities live under `web/src/test/` (not scattered ad-hoc)
- [ ] Tests are deterministic (no real network, stable time, stable random seed where applicable)
- [ ] API calls are mocked at the boundary (no Neo4j drivers or direct graph access in `web/`)
- [ ] Any new contract or schema assumptions are reflected in `src/server/contracts/` / `schemas/` (as applicable)
- [ ] CI checks pass (unit tests, typecheck/lint, and any configured a11y/registry/schema checks)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/test/README.md`

### Recommended structure inside `web/src/test/`

Create what you need, but prefer a predictable, reusable layout:

~~~text
📁 web/
└── 📁 src/
    └── 📁 test/
        ├── 📄 README.md
        ├── 📁 fixtures/          # small, stable JSON fixtures (API payloads, Story Nodes)
        ├── 📁 factories/         # builders for typed test objects
        ├── 📁 mocks/             # module mocks (map engine seams, browser APIs)
        ├── 📁 msw/               # request handlers for mocked API calls (if used)
        ├── 📁 utils/             # shared helpers (render wrappers, router/state setup)
        └── 📄 setupTests.*       # global test setup (matchers, polyfills)
~~~

## 🧭 Context

KFM’s system contract is a staged pipeline:

- ETL → STAC/DCAT/PROV → Graph → API boundary → UI → Story Nodes → Focus Mode

The UI lives at the **end** of the pipeline. It must not bypass the API boundary to query the graph layer.

In practice, that means:

- UI code (and UI tests) should interact with data via API responses, not via Neo4j drivers or raw graph queries.
- UI tests should “lock in” expected contract behavior so that contract changes are intentional and reviewed.

## 🧱 Architecture

### Test pyramid for the UI

1. **Unit tests**
   - Pure utilities (formatting, parsing, filtering)
   - Small components with mocked hooks/dependencies

2. **Integration tests**
   - Feature components with routing/state
   - Network mocked at the API boundary
   - Focus Mode render paths with realistic (but minimal) fixtures

3. **E2E tests**
   - Only for critical user journeys (map loads, layer toggles, Focus Mode entry)
   - Prefer running against a locally hosted API stub (or mocked server) for determinism

### Mocking guidance

- **API boundary mocking**
  - Prefer one consistent approach (e.g., request interception or a mock service worker) and keep handlers here.
  - Avoid “deep mocking” internal implementation details of components unless unavoidable.

- **Map engine seams**
  - Map engines are typically hard to run under JSDOM.
  - Keep map glue code thin and mock the map adapter at the boundary.
  - Test map-related logic at the “adapter interface” level (inputs → expected calls), not pixel-perfect rendering.

- **Time and randomness**
  - Freeze time for tests that depend on “now”.
  - Seed randomness (or inject PRNG) for any stochastic behavior.

## 📦 Data & Metadata

### Fixtures

- Keep fixtures **small and explicit**.
- Prefer fixtures that look like **API responses**, since that is what the UI consumes.
- Do not include real restricted coordinates or sensitive content in fixtures.

### “Provenance-like” test data

Where possible, fixtures should include:

- Stable identifiers (e.g., dataset IDs, story node IDs)
- Citation-like fields (so Focus Mode/citation UI paths are exercised)
- Minimal geometry (or generalized geometry) for map-facing tests

## 🌐 STAC, DCAT & PROV Alignment

Even though the UI does not build catalogs, it consumes catalog-derived content.

Testing recommendations:

- Don’t embed full catalogs in unit tests.
- Use small fixture slices that represent the **contracted** subset the UI expects.
- If a UI feature depends on schema validation (e.g., a layer registry), add a test that validates the sample config
  against the relevant schema under `schemas/`.

## 🧠 Story Node & Focus Mode Integration

When adding or updating Focus Mode UI behavior, tests should cover:

- Story Node text renders (including headings, citations/footnotes if present)
- Evidence/asset panels render safely (no untrusted HTML injection)
- “No unsourced narrative” UI affordances (warnings when citations are missing, where applicable)

## 🧪 Validation & CI/CD

### Local runs

Use the scripts defined for the web app (adjust to whatever is configured in `web/package.json`). Example:

~~~bash
cd web
# examples only — use the script names defined in this repo
npm run test
npm run test:watch
npm run lint
npm run typecheck
~~~

### CI expectations

CI commonly enforces (at minimum):

- Markdown protocol validation for markdown files
- Contract/schema validation (API + UI schemas)
- Unit/integration test execution
- Lint + typecheck
- Security/dependency scans

## ⚖ FAIR+CARE & Governance

Even tests can leak sensitive information if fixtures contain restricted content.

- Keep fixtures synthetic or generalized.
- If you must use real examples, ensure they comply with sovereignty/redaction rules and are approved for the
  repo’s `classification` level.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `web/src/test/` README scaffold | TBD |

