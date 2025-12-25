---
title: "KFM Web UI — Test Area README"
path: "web/src/test/README.md"
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

doc_uuid: "urn:kfm:doc:web:src:test-readme:v1.0.0"
semantic_document_id: "kfm-web-src-test-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:test-readme:v1.0.0"
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

# KFM Web UI Test Area

> **Purpose (required):** Document how the **Web UI test area** under `web/src/test/` is structured and used to produce **deterministic, contract-aligned** UI tests that preserve KFM’s non-negotiables: **API-boundary access**, **provenance-first rendering**, and **FAIR+CARE governance posture**.

## 📘 Overview

### What this directory is for

`web/src/test/` is the **UI test harness area** for:

- test helpers and shared test utilities used by the Web UI,
- fixtures that simulate **API responses** and **Story Node** payloads,
- validation helpers that ensure UI code stays aligned with:
  - the API boundary (UI never reads the graph directly),
  - provenance-focused rendering expectations,
  - accessibility and deterministic behavior in CI.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI unit tests and UI integration tests that exercise rendering and user flows | ETL, catalog, graph ingest, or server-side tests |
| Test utilities, mocks, fixtures, and deterministic helpers | End-to-end tests in a dedicated E2E area *(not confirmed in repo)* |
| Contract-oriented UI checks (schema validation of UI registry / Story Node shapes) | Changing API contracts *(requires `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`)* |

### Audience

- Primary: Web UI contributors working under `web/`.
- Secondary: API / schema maintainers who want to verify UI contract alignment.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo)*

Terms used in this README:

- **API boundary**: UI accesses data **only** through server APIs (no direct Neo4j/graph access).
- **Contract test**: a test that fails when the UI shape expectations diverge from schemas/contracts.
- **Fixture**: a synthetic or redacted payload used for tests.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repo pipeline ordering | `README.md` | Maintainers | Canonical pipeline is non-negotiable |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical system/pipeline source of truth |
| v13 blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Draft readiness gates *(if adopted)* |
| Schemas | `schemas/` | Contracts owners | Used for validation *(not confirmed in repo)* |
| API server | `src/server/` | Backend owners | UI must go through contracted endpoints |
| UI registry config | `web/` | UI owners | Validate layer/config schemas *(where applicable)* |

### Definition of Done

- [ ] Tests in this area are deterministic (no live network, no clock drift, no random seeds).
- [ ] Any mocked data uses synthetic or redacted fixtures (no PII, no sensitive coordinates).
- [ ] UI tests assert API-boundary behavior (requests go to API client layer, not the graph).
- [ ] Where schemas exist, fixtures are validated against them.
- [ ] A11y checks are present for core UI surfaces *(tooling not confirmed in repo)*.
- [ ] Documentation changes preserve KFM Markdown protocol (front-matter + required sections).

## 🗂️ Directory Layout

### Where this document lives

- This README: `web/src/test/README.md`

### Related repository paths

- Web UI root: `web/`
- API boundary: `src/server/`
- Schemas registry: `schemas/` *(not confirmed in repo)*
- Repo-wide CI expectations: `.github/workflows/` *(not confirmed in repo)*

### Expected local structure

The exact contents of `web/src/test/` are repo-dependent, but the following structure is recommended:

~~~text
🌐 web/
└─ 🧩 src/
   └─ 🧪 test/
      ├─ README.md
      ├─ 🧰 helpers/           # render helpers, time/random determinism helpers (recommended)
      ├─ 🎭 mocks/             # API client mocks, mock servers (recommended)
      ├─ 🧪 fixtures/          # synthetic/redacted payload fixtures (recommended)
      └─ ⚙️ setup/             # test runner setup hooks (recommended)
~~~

> If your repo uses a different test layout (e.g., `__tests__/`, `test/`, or `tests/`), treat the above tree as a **recommended convention** and align to the existing structure.

## 🧭 Context

### How this fits into KFM’s pipeline

KFM’s canonical ordering is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

UI tests live at the **UI** stage and should treat upstream layers as **contracts**:

- the UI consumes **API responses**,
- API responses are derived from graph + catalogs,
- story nodes are rendered with provenance-first behavior.

### Boundary rule enforced by tests

UI tests must preserve the boundary:

- ✅ UI code may call an API client/service abstraction
- ❌ UI code must not call Neo4j/graph directly
- ❌ UI tests must not “cheat” by reading graph fixtures as if they are UI inputs

## 🗺️ Diagrams

### Pipeline placement

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV]
  B --> C[Graph]
  C --> D[API]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### UI test harness concept

~~~mermaid
flowchart TD
  T[Test Runner] --> U[UI Components / Map UI]
  U --> C[API Client Layer]
  C --> M[Mock Server / Mock Fetch]
  M --> F[Fixtures]
  F --> V[Schema Validators]
~~~

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

When UI tests involve story nodes:

- fixtures must represent **story node payloads** that the UI actually renders,
- story node fixtures should include provenance fields where expected,
- story node fixtures should link to evidence IDs where possible (STAC/DCAT/PROV identifiers).

### Focus Mode rule

UI tests that cover Focus Mode behavior should assert that:

- Focus Mode consumes **provenance-linked content** only,
- any predictive/AI-derived content (if present) is:
  - opt-in,
  - labeled as predictive,
  - accompanied by uncertainty/confidence metadata.

> If Focus Mode features are not yet implemented in the UI, keep this section as the **contract expectation** for when they are introduced.

## 🧪 Validation & CI/CD

### Minimum CI gates relevant to this directory

This area should be compatible with repo-wide baseline gates such as:

- Markdown protocol validation
- Schema validation (where schemas exist)
- API contract tests (UI ↔ API boundary)
- UI registry schema checks (where applicable)
- Security + sovereignty scanning gates (where applicable)
- Accessibility checks (where applicable)

> The exact workflow wiring (and scripts) is **not confirmed in repo**; align with `.github/workflows/` and the repo’s package scripts.

### Local reproduction

~~~bash
# NOTE: Commands below are placeholders; replace with repo-approved tooling.
# The intent is to provide a deterministic “same as CI” workflow for UI tests.

# cd web
# npm test
# npm run test:unit
# npm run test:integration
# npm run test:contracts
~~~

### Determinism checklist for UI tests

- Freeze time where relevant (avoid snapshot churn).
- Seed randomness where used (or remove randomness entirely).
- Never call real external services.
- Prefer fixtures checked into the repo (small + synthetic).
- Avoid brittle DOM selectors (prefer semantic roles / stable test IDs).

## 📦 Data & Metadata

### Fixture rules

Fixtures in UI tests should be:

- **synthetic by default**,
- **redacted/generalized** if derived from real sources,
- small and focused on the UI contract.

Do not store:

- API tokens or secrets,
- PII (names/emails/phone numbers),
- restricted/sensitive coordinates or geometries.

### Stable identifiers

Where IDs are required in fixtures:

- use stable, explicit IDs (e.g., `fixture:storynode:demo:001`),
- avoid IDs that imply real people/communities unless approved and properly governed.

## 🌐 STAC, DCAT & PROV Alignment

UI tests do not generate catalogs, but they **must** respect downstream expectations:

- provenance fields should round-trip through UI rendering where applicable,
- citations/sources panels (if present) should show **evidence identifiers**,
- “expert drill-down” should surface STAC IDs and PROV lineage where applicable.

If a UI surface claims to display provenance:

- test fixtures must include those fields,
- tests must assert they render correctly (and fail if missing).

## 🧱 Architecture

### Layering principle

UI tests should treat the UI as an **outer layer**:

- talk inward using simple structures (plain objects from API clients),
- talk outward through interfaces (API client abstractions),
- keep dependencies replaceable (mocks/fakes) to preserve determinism.

### WebGL and map rendering considerations

If map rendering is part of tests:

- prefer integration tests around UI logic (layer toggles, data bindings) over pixel-perfect rendering,
- be explicit about WebGL context behavior (context loss/recover) if you simulate it.

> Exact MapLibre/WebGL harness utilities are **not confirmed in repo**; keep tests resilient to headless renderer constraints.

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that touch any of the following should trigger **human review**:

- provenance rendering rules,
- redaction/generalization behavior,
- public-facing UI messaging related to sensitive topics,
- any new AI narrative behavior surfaced in the UI.

### CARE and sovereignty considerations

- Assume sensitive location handling is high-risk by default.
- Do not allow tests or fixtures to reconstruct restricted locations.
- Respect the sovereignty policy when using any real-world geographic references.

### AI usage constraints

- This README’s AI permissions are informational only.
- Do not use UI tests to “infer” sensitive locations from nearby measurements or proxies.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/test/` README scaffold | `<your-name>` |

---

<div align="center">

**📚 Governance Links**  
[Repo README](../../../README.md) ·  
[Docs Root](../../../docs/README.md) ·  
[Governance Charter](../../../docs/governance/ROOT_GOVERNANCE.md) ·  
[Ethics](../../../docs/governance/ETHICS.md) ·  
[Sovereignty](../../../docs/governance/SOVEREIGNTY.md)

**🔐 Compliance**  
FAIR+CARE · KFM‑MDP v11.2.6 · KFM‑STAC v11 · KFM‑DCAT v11 · KFM‑PROV v11

**End of Document**

</div>
