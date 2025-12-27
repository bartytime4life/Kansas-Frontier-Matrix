---
title: "KFM Tests — E2E (End-to-End) README"
path: "tests/e2e/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:tests:e2e:readme:v1.0.0"
semantic_document_id: "kfm-tests-e2e-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tests:e2e:readme:v1.0.0"
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

# KFM Tests — E2E (End-to-End) README

## 📘 Overview

### Purpose

- Define **end-to-end (E2E)** testing conventions for Kansas Frontier Matrix (KFM).
- Make E2E tests **deterministic, reviewable, and CI-friendly**.
- Align E2E tests to the canonical system flow:
  - **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| Cross-subsystem flows (“vertical slices”) across API + UI + narrative rendering | Choosing a specific E2E framework/tooling *(not confirmed in repo)* |
| E2E fixtures (synthetic), environment contracts, and artifact handling | Load/performance testing (use a dedicated perf harness) |
| Validation of provenance-linked narrative + Focus Mode behaviors | Replacing governance/security policy text |

### Audience

- **Primary:** KFM contributors implementing pipelines, graph ingest, API endpoints, or UI features.
- **Secondary:** CI maintainers and governance reviewers validating release readiness.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **E2E test**, **fixture**, **deterministic run**, **idempotence**, **contract test**, **redaction/generalization**, **provenance**, **Story Node**, **Focus Mode**.

### Key artifacts (what this doc points to)

> Paths reflect canonical placement. Some may not exist yet in the current repo snapshot (**not confirmed in repo**).

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Test taxonomy + shared conventions | `tests/README.md` | KFM Core | Defines unit/integration/contract/e2e split |
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Architecture contract + sequencing |
| v13 target architecture (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Canonical paths, subsystem boundaries |
| API contracts | `src/server/contracts/` | API Eng | E2E should align to versioned contracts |
| Schemas (STAC/DCAT/PROV/story nodes/telemetry) | `schemas/` | Data/Platform | E2E fixtures should validate where applicable |
| Provenance bundles | `data/prov/` | Data Eng | E2E may assert presence/shape of provenance pointers |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `path` matches file location
- [ ] Directory layout + “where things go” is explicit
- [ ] Run steps are repeatable (or explicitly marked “not confirmed in repo”)
- [ ] Determinism + flakiness controls documented
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tests/e2e/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| E2E tests | `tests/e2e/` | Browser/API flows spanning multiple subsystems |
| Shared test utilities | `tests/helpers/` | Common assertions, stubs, deterministic helpers *(recommended)* |
| Synthetic fixtures | `tests/fixtures/` | Small, synthetic fixture datasets only *(recommended)* |
| Schemas | `schemas/` | Validation profiles for catalogs, story nodes, telemetry |
| API boundary | `src/server/` *(v13 target)* | Redaction, access controls, query services |
| UI | `web/` | React/Map UI and story rendering |
| Provenance | `data/prov/` | Run provenance bundles / pointers |
| CI workflows | `.github/workflows/` | CI gates; may run E2E optionally |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 tests/
├── 📄 README.md
├── 📁 e2e/
│   ├── 📄 README.md
│   ├── 📁 specs/                 # E2E specs/scenarios (recommended)
│   ├── 📁 fixtures/              # E2E-specific fixtures (recommended)
│   ├── 📁 helpers/               # E2E helpers: selectors, waits, API clients (recommended)
│   ├── 📁 snapshots/             # visual snapshots (if used; recommended)
│   └── 📁 artifacts/             # local outputs (screenshots/traces/videos); should be gitignored
└── 📁 fixtures/                  # shared synthetic fixtures (recommended)
~~~

## 🧭 Context

### Background

KFM is intentionally **pipeline-ordered** and **contract-driven**:

- Catalog artifacts (STAC/DCAT/PROV) serve as durable, auditable evidence.
- The graph (Neo4j) is accessed via an **API boundary** that enforces redaction/generalization.
- The UI (map + narrative) consumes data **through APIs/contracts**, and published narrative must be **provenance-linked**.

E2E tests are the place we validate that a “vertical slice” still works when all parts are wired together.

### Assumptions

- The system flow is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The **UI does not connect to Neo4j directly**; API mediates access and enforces governance rules.
- E2E tests are designed to be **deterministic** and **repeatable**.

### Constraints / invariants

- **No production data** in E2E fixtures.
- **No hidden network I/O:** external calls should be stubbed, recorded, or blocked.
- **Deterministic inputs/outputs:** fixed seeds, pinned time, stable fixtures, stable selectors.
- **Governance-safe artifacts:** screenshots/logs must not leak restricted coordinates, sensitive locations, or secrets.

### When to add an E2E test (vs. other test types)

Use E2E tests when you need to prove a **cross-subsystem contract** holds, such as:

- A new API endpoint + UI feature + story rendering all agree on identifiers and fields.
- Redaction/generalization rules are enforced end-to-end.
- Story Nodes / Focus Mode surfaces **only evidence-linked claims**.

Prefer **unit/integration/contract** tests for:
- Field-level validation, schema edge cases, or endpoint correctness in isolation.
- High-cardinality permutations (E2E should remain small and strategic).

## 🗺️ Diagrams

### System / dataflow diagram (E2E perspective)

~~~mermaid
flowchart LR
  A[Small Synthetic Fixtures] --> B[Catalog + Provenance Fixtures]
  B --> C[Graph Fixture Import]
  C --> D[API Boundary]
  D --> E[UI (Map + Narrative)]
  E --> F[Story Nodes]
  E --> G[Focus Mode]

  H[E2E Runner] --> D
  H --> E
~~~

### Sequence diagram (UI path)

~~~mermaid
sequenceDiagram
  participant T as E2E Runner
  participant U as Web UI
  participant A as API Boundary
  participant G as Graph Store
  participant P as Provenance/Catalog Artifacts

  T->>U: open page / story node / focus mode
  U->>A: request data (contracted endpoint)
  A->>G: query graph (server-side only)
  A->>P: (optional) resolve provenance pointers / catalog refs
  A-->>U: redacted + contract-shaped response
  U-->>T: rendered map/narrative with citations
~~~

## 📦 Data & Metadata

### Fixture rules (E2E)

E2E fixtures should be:

- **Small** (fast to load in CI)
- **Synthetic** (no real personal data; no restricted coordinates)
- **Stable** (identifiers do not change; deterministic ordering)
- **Documented** (each fixture folder includes a brief README)

Recommended fixture contents (adapt to repo reality):

- Minimal dataset records with stable IDs (e.g., `Place`, `Event`, `Document`, `Organization`).
- Optional STAC/DCAT/PROV artifacts that validate against `schemas/` (if the repo runs catalog validation in CI).
- A minimal “story node” example that references evidence IDs rather than free-form claims.

### Environment variables & secrets

- E2E tests must not require real credentials.
- If environment variables are needed (ports, base URLs), provide:
  - `.env.example`-style documentation *(not confirmed in repo)*
  - CI-safe defaults (e.g., loopback only)

## 🌐 STAC, DCAT & PROV Alignment

If E2E uses catalog/provenance fixtures, tests should validate:

- Fixtures align with current schema expectations under `schemas/`.
- Any “evidence” referenced by Story Nodes or Focus Mode corresponds to:
  - a stable dataset/document ID, and
  - a provenance pointer (or catalog identifier) when applicable.

Recommended “E2E assertions” (high-level):

- [ ] The API returns stable IDs and contract-shaped fields.
- [ ] Provenance pointers (if included) resolve to artifacts under `data/prov/` and/or catalog roots.
- [ ] The UI displays citations/provenance affordances where required (Story Nodes / Focus Mode).

## 🧱 Architecture

### Components under test (typical E2E slice)

| Component | Responsibility | Typical E2E assertion |
|---|---|---|
| Graph | Stores entities + relations | Seed/import succeeded; queries return expected stable IDs |
| API boundary | Serves contract-shaped data; enforces redaction | Responses match contracts; restricted fields are removed/generalized |
| UI | Renders map layers + narrative | UI renders deterministically with stable selectors |
| Story Nodes | Curated narrative artifacts | Facts displayed map to cited evidence IDs |
| Focus Mode | Contextual synthesis | Output is provenance-linked; no “unsourced narrative” |

### Test topology patterns

> Choose the pattern that matches how the repo is actually wired. Tooling below is illustrative (**not confirmed in repo**).

1) **API-only E2E (service-level smoke)**
- Start graph + API server with fixture seed.
- Run HTTP scenarios against API endpoints.
- Pros: faster, less flaky.
- Cons: doesn’t validate UI rendering.

2) **Full UI E2E (browser + API)**
- Start graph + API + UI.
- Drive browser to validate UX flows + provenance visibility.
- Pros: validates “real” user path.
- Cons: slower; requires stable selectors and careful timing.

### Interfaces / contracts

- E2E should treat **contracts as authoritative**.
- If contracts are versioned (OpenAPI/GraphQL), E2E should fail when:
  - UI depends on an undocumented field, or
  - API breaks a documented response shape.

## 🧠 Story Node & Focus Mode Integration

### Provenance-linked narrative rule (E2E)

E2E tests must protect the KFM invariant:

- **Published narratives must not be unsourced.**
- **Focus Mode surfaces provenance-linked content only.**

Recommended E2E scenarios:

- **Story Node rendering**
  - Load a known Story Node fixture.
  - Assert that each displayed factual claim is associated with an evidence/citation affordance (ID/link).
  - Assert that broken/unknown evidence IDs are surfaced as errors (not silently ignored).

- **Focus Mode behavior**
  - Open Focus Mode on a bounded context (layer/time/area).
  - Assert the UI displays provenance links/pointers for surfaced claims/cards.
  - Assert the UI shows a redaction/generalization notice when applicable.

- **Redaction/generalization enforcement**
  - Use a fixture that includes at least one “restricted” field/geometry.
  - Assert restricted details are not present in API response payloads.
  - Assert UI does not render restricted details (including in screenshots/artifacts).

## 🧪 Validation & CI/CD

### Minimum CI gates (E2E-specific)

E2E tests are typically **optional** gates unless the repo explicitly requires them. The general principle:

- If the E2E root exists and CI is configured to run it: **strict** validation.
- If required dependencies/configs are absent in a given environment: **skip deterministically** (no flaky partial runs).

Recommended E2E-related CI gates:

- [ ] E2E specs compile/parse (syntax + lint where applicable)
- [ ] E2E run completes on fixtures (no external network)
- [ ] Artifacts generated (screenshots/logs) are sanitized and do not leak secrets/sensitive locations
- [ ] Contract checks pass (if contracts are present and wired to E2E)

### Reproduction (local)

~~~bash
# Example placeholders — replace with repo-specific commands/scripts (not confirmed in repo)

# 1) Start dependencies (graph + api + ui)
# <TBD: docker compose up / dev scripts / make targets>

# 2) Seed fixtures
# <TBD: load tests/e2e/fixtures into graph + catalogs>

# 3) Run E2E
# <TBD: e2e runner invocation>

# 4) Collect artifacts (screenshots/traces/logs)
# <TBD: output path conventions + sanitation rules>
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| E2E run ID | CI / local runner | CI logs + artifacts |
| Fixture version/hash | E2E harness | test report metadata |
| Flake retries | E2E runner | test report |
| Artifact refs (sanitized) | E2E runner | CI artifacts (private) |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when E2E changes introduce:

- New fixtures containing sensitive/restricted information.
- New test flows that could expose restricted coordinates via screenshots, logs, traces, or videos.
- Any automation that attempts to infer sensitive locations or produce policy text.

### CARE / sovereignty considerations

- Treat E2E artifacts (screenshots, traces, logs) as potential leakage vectors.
- If fixtures include locations, prefer:
  - synthetic coordinates, or
  - coarse generalized geometry consistent with sovereignty policy.
- Do not publish raw E2E artifacts publicly when they could expose restricted content.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `tests/e2e/README.md` scaffold aligned to Master Guide v12 + test conventions | TBD |

---

Footer refs:

- Tests root: `tests/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
