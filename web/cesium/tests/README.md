---
title: "KFM Web — Cesium Tests"
path: "web/cesium/tests/README.md"
version: "v0.1.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:cesium:tests:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-tests-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:tests:readme:v0.1.0"
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

# KFM Web — Cesium Tests

Directory: `web/cesium/tests/`

## 📘 Overview

### Purpose
- Define how Cesium-specific UI code is tested in a way that is:
  - deterministic and CI-friendly,
  - architecture-synced to KFM’s **API boundary** rule,
  - provenance-aware for Focus Mode and Story Node rendering,
  - safe with respect to sensitivity, sovereignty, and restricted location precision.

### Scope

| In Scope | Out of Scope |
|---|---|
| Unit tests for Cesium adapters, layer parsing, and Focus Mode map sync | Server/API contract authoring (lives under `src/server/`) |
| Integration tests for Cesium viewer wiring and layer toggles | ETL/cat/graph pipelines (lives under `src/pipelines/`, `src/graph/`) |
| UI contract and provenance expectations for “focus bundles” | Full repo-wide CI workflow definition (lives under `.github/`) |
| Guidance for mocks, fixtures, and safe test data | Real-world sensitive datasets or restricted precision fixtures |

### Audience
- Primary: UI engineers working on Cesium integration.
- Secondary: API engineers validating contracts; governance reviewers validating safety posture of test fixtures.

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this document:
  - **Adapter**: Cesium rendering module responsible for attach/update/detach lifecycle.
  - **Mock viewer**: a lightweight stand-in for Cesium viewer objects used for unit tests.
  - **Focus bundle**: contracted API payload consumed by Focus Mode and map clients.
  - **Golden test**: snapshot or reference output used to detect regressions.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Cesium overview | `web/cesium/README.md` | UI | High-level Cesium integration rules |
| Adapters | `web/cesium/adapters/README.md` | UI | Adapter lifecycle conventions |
| Layer registries | `web/cesium/layers/` | UI | Descriptor inputs for adapters |
| UI schemas | `schemas/ui/` | Schemas/UI | Registry validation (not confirmed in repo) |
| API boundary | `src/server/` | API | Focus bundles and layer metadata |

### Definition of done
- [ ] Front-matter is complete and `path` matches `web/cesium/tests/README.md`
- [ ] Adapter lifecycle is covered by tests (attach/update/detach)
- [ ] Layer registry parsing and schema validation is tested or enforced in CI (where schemas exist)
- [ ] Focus Mode interactions preserve provenance and do not render uncited claims as fact
- [ ] Tests do not require secrets or private endpoints
- [ ] Fixtures do not increase sensitive location precision and contain no PII

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/tests/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Cesium code | `web/cesium/` | Cesium integration and adapters |
| Cesium tests | `web/cesium/tests/` | This directory |
| Layer registries | `web/cesium/layers/` | Declarative layer configs |
| Web app source | `web/src/` | UI features and Focus Mode UX |
| API contracts | `src/server/contracts/` | Contract tests and schemas |
| UI schemas | `schemas/ui/` | Registry schemas (not confirmed in repo) |

### Expected file tree
> This is a recommended shape. Update it to match the actual repo.

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 tests/
        ├── 📄 README.md
        ├── 📁 unit/                      # adapter and parsing tests
        ├── 📁 integration/               # viewer wiring and runtime interaction tests
        ├── 📁 e2e/                       # optional: end-to-end smoke tests for 3D mode
        ├── 📁 fixtures/                  # non-sensitive fixtures only
        ├── 📁 mocks/                     # Cesium viewer/primitives mocks
        └── 📁 helpers/                   # test utilities
~~~

## 🧭 Context

### Background
Cesium introduces WebGL and GPU resource lifecycles, which can be difficult to test directly in CI. KFM’s strategy is to:
- test pure logic (parsing, validation, state transitions) with unit tests,
- test adapter lifecycle correctness with mocked viewer objects,
- run minimal smoke/integration tests for wiring and interactions,
- keep all fixtures public-safe and provenance-aware.

### Assumptions
- The UI consumes data through contracted APIs and does not query Neo4j directly.
- Tests should not depend on network access to external endpoints unless explicitly allowed and sandboxed.
- Cesium objects require deterministic teardown; tests should assert detach cleans up handles.

### Constraints and invariants
Non-negotiables:
- **No direct graph access**: tests must not introduce client-side graph connections.
- **No secrets**: tests must not require Cesium Ion tokens, API keys, or private endpoints.
- **Safety posture**: fixtures must not include restricted location precision, PII, or culturally sensitive content.
- **Provenance UX**: tests must protect the rule that Focus Mode displays provenance-linked content.

### Test strategy
Recommended layers of testing:
1) **Unit tests**
   - registry parsing and validation behavior,
   - adapter attach/update/detach behavior with mocked Cesium objects,
   - citation/provenance UI helpers (as applicable).

2) **Integration tests**
   - minimal viewer boot and shutdown,
   - toggling a layer on/off and ensuring no leaks,
   - switching 2D/3D modes without losing state (if supported).

3) **End-to-end smoke tests**
   - open app, enable 3D mode, enter/exit Focus Mode, toggle a known non-sensitive layer.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which test runner and framework is used for `web/` | UI | TBD |
| Are headless WebGL runs supported in CI for integration tests | UI | TBD |
| Where contract fixture schemas live for Focus bundles | UI + API | TBD |

### Future extensions
- Add leak detection checks (handles destroyed) for adapters.
- Add performance regression checks for 3D mode initialization and layer toggles.
- Add schema-driven fixture generation for focus bundles (if a schema exists).

## 🗺️ Diagrams

### Test pyramid for Cesium
~~~mermaid
flowchart TB
  U["Unit tests: parsing + adapters with mocks"] --> I["Integration tests: viewer wiring + toggles"]
  I --> E["E2E smoke: 3D toggle + Focus Mode flows"]
~~~

### Adapter lifecycle assertion
~~~mermaid
sequenceDiagram
  participant T as Test
  participant A as Adapter
  participant V as Mock Viewer

  T->>A: attach(ctx, input)
  A->>V: create primitives
  T->>A: update(ctx, patch)
  A->>V: update primitives
  T->>A: detach(ctx)
  A->>V: destroy primitives
  T-->>T: assert no leaked handles
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Notes |
|---|---|---|---|
| Registry fixtures | JSON | `web/cesium/layers/` or test fixtures | Must be public-safe |
| Focus bundle fixtures | JSON | `web/cesium/tests/fixtures/` | Must include provenance fields used by UI |
| Mock Cesium objects | TS/JS | `web/cesium/tests/mocks/` | Keep lightweight and deterministic |

### Outputs

| Output | Format | Path | Notes |
|---|---|---|---|
| Test reports | runner-specific | CI artifacts | Do not include PII |
| Coverage metrics | runner-specific | CI artifacts | Optional |

### Sensitivity and redaction
- Fixtures must never contain precise restricted coordinates or sensitive site names under restriction.
- If a fixture represents an entity, use generalized coordinates and clearly mark as synthetic.
- Ensure fixtures do not embed EXIF/GPS metadata in images (if any fixtures include images).

## 🌐 STAC, DCAT & PROV Alignment

Tests should protect provenance behavior by validating that:
- focus bundle fixtures include evidence identifiers used by the UI audit panel,
- UI components render citations and sources as inspectable elements,
- missing provenance triggers warnings rather than silent acceptance.

This directory does not author catalog outputs; it only validates UI handling of evidence identifiers delivered via APIs.

## 🧱 Architecture

### What tests should cover
- Adapter correctness:
  - attach allocates expected primitives,
  - detach cleans up all resources,
  - update is idempotent where possible.

- Contract consumption:
  - focus bundles and layer metadata are parsed defensively,
  - required fields for provenance display are present (or UI degrades safely).

- State transitions:
  - 2D/3D toggles preserve active layer IDs and Focus Mode selection (if supported).

### What tests should not do
- Do not call Neo4j directly.
- Do not hardcode internal hostnames or private endpoints.
- Do not require secrets to run locally or in CI.

## 🧠 Story Node & Focus Mode Integration

### Focus Mode expectations to test
- Entering Focus Mode requests a contracted payload through the API client.
- Narrative rendering shows citations and sources as an audit affordance.
- Layer hints from Story Nodes do not enable layers that are not present in registries, and do not bypass gating.

Illustrative fixture pattern:
~~~yaml
focus_layers:
  - "kfm-example-layer"
focus_time: "1854-01-01/1854-12-31"
focus_center: [-98.0000, 38.0000]
~~~

### AI-related behavior
If the UI supports opt-in predictive content:
- tests should assert it is clearly labeled,
- tests should assert it is opt-in,
- tests should assert provenance or uncertainty metadata is present.

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Unit tests run without network access
- [ ] Integration tests avoid requiring GPU-specific features unless CI explicitly supports it
- [ ] No secrets in fixtures or environment requirements
- [ ] Registry schema validation runs if `schemas/ui/` exists
- [ ] Markdown and link checks run if governed doc linting is enabled

### Local reproduction
~~~bash
# Placeholders — replace with repo-approved commands from web tooling.

# run unit tests
# <tool> test

# run integration tests
# <tool> test:integration

# run e2e smoke tests
# <tool> test:e2e

# validate registries if schema exists
# <tool> validate --schema schemas/ui/<registry-schema>.json web/cesium/layers/*.json
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
Governance review required when tests:
- add fixtures that resemble real sensitive locations,
- add fixtures derived from restricted sources,
- change how provenance or redaction behavior is validated.

### CARE and sovereignty considerations
- Keep fixtures synthetic and generalized.
- Ensure tests do not create “how-to” pathways for discovering restricted locations or knowledge.

### AI usage constraints
- Tests must not introduce speculative narrative as if factual.
- Tests must not infer sensitive locations or attempt to “fill in” redacted information.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-24 | Initial Cesium tests README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`