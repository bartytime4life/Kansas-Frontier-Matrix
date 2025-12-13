---
title: "🧪 Kansas Frontier Matrix — E2E Web App Regression Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/README.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

provenance_chain:
  - "tests/e2e/web-app/regression/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — E2E Web App Regression Suite (v11 LTS)**
`tests/e2e/web-app/regression/README.md`

**Purpose**  
Define the canonical **regression-grade** end-to-end (E2E) suite for the KFM Web App.  
Regression E2E tests validate **multi-step UI flows**, **map/timeline coherence**, and **governance-safe narrative surfaces** under deterministic, synthetic fixtures.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Regressions-informational" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App E2E Index](../README.md) · [🧭 E2E Guide](../../README.md) · [🏗 Test Architecture](../../../ARCHITECTURE.md)

</div>

---

## 📘 Overview

The regression suite is the “broad coverage” layer of KFM’s Web App E2E testing.

Regression E2E tests SHOULD:
- validate correctness across **multiple screens/states**
- confirm that key UI features remain stable across releases
- detect “slow drift” regressions missed by smoke tests
- verify governance is enforced in user-visible surfaces

Regression E2E tests MUST:
- run against **synthetic fixtures only**
- remain **deterministic** (seeded, stable time, stable selectors)
- produce auditable artifacts (report + traces + screenshots on failure)
- avoid external network dependencies (unless explicitly whitelisted)

### In-scope behaviors (regression-grade)
- map + timeline interactions across multiple actions (toggle layers, filter, revisit state)
- Story Node v3 render + provenance chips + safe geometry precision
- Focus Mode v3 panels (Context/Timeline/Map) + governance overlays
- search/navigation flows across routes and back/forward history
- “dataset preview” and other publish-adjacent UX flows (synthetic-only)

### Out-of-scope behaviors
- unit logic validation (belongs in `tests/unit/`)
- schema-only shape tests (belongs in `tests/schemas/`)
- pixel-perfect visual diffs unless the suite is explicitly designed for it
- performance benchmarking as a gating requirement (track separately unless mandated)

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            ├── 📄 README.md                           — This guide
            │
            ├── 📁 navigation/                         — Multi-route flows (deep links, back/forward, reload)
            ├── 📁 map/                                — MapLibre/Cesium interactions (layers, tooltips, bounds)
            ├── 📁 timeline/                           — Timeline brushing, filters, temporal ordering
            ├── 📁 storynodes/                         — Story Node v3 regression flows
            ├── 📁 focus-mode/                         — Focus Mode v3 regression flows
            ├── 📁 governance/                         — CARE tier routing + sovereignty gating (UI-visible)
            │
            ├── 📁 fixtures/                           — Regression-only synthetic fixtures (if needed)
            └── 📁 specs/                              — Runner-native spec files (e.g., *.spec.ts / *.cy.ts)
~~~

Directory policy:
- Put runner-specific files under `specs/` unless the repo standard differs.
- If a fixture exists here, it must remain synthetic and should be referenced from an ID/versioned bundle.
- Regression tests must not depend on smoke test ordering or side effects.

---

## 🧭 Context

### Determinism rules
Regression suites MUST:
- use a fixed seed (recorded in run manifest)
- use deterministic time (injectable clock or fixed timestamps)
- avoid arbitrary sleeps; prefer event/state-based waits
- isolate state (no cross-test coupling)

Recommended pattern:
- one test → one primary behavioral claim
- small number of “multi-assert” tests is allowed only when the flow is inseparable and the failure signal remains clear

### Flake policy (strict, regression-aware)
- Any newly flaky regression test is quarantined behind `@nightly` until fixed.
- Retries are permitted only when:
  - the retry reason is recorded (manifest field or tracking issue)
  - the test remains deterministic
- Governance failures are not retryable by default.

### Tagging guidance
Use tags to manage CI routing:
- `@regression` — default for this suite
- `@nightly` — slow or high-volume scenarios
- `@governance` — CARE + sovereignty gates and redaction assertions
- `@a11y` — if a regression test is specifically accessibility-related (otherwise use the a11y suite)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Scheduled or manual trigger"] --> B["Boot deterministic test stack"]
  B --> C["Load synthetic fixture bundle"]
  C --> D["Run regression suites (@regression)"]
  D --> E["Write report + junit + traces"]
  E --> F["Validate governance + telemetry shapes"]
  F --> G["Publish artifacts and summaries"]
~~~

Interpretation:
- Regression suites are designed for wide coverage and strong artifact capture.
- Governance and telemetry validation remains mandatory because failures are high-risk.

---

## 🧠 Story Node & Focus Mode Integration

Regression E2E coverage must include narrative surfaces because they are the primary user-facing risk boundary.

### Story Node v3 regression expectations
Regression tests SHOULD validate:
- rendering of core Story Node fields (title, narrative, spacetime, relations)
- provenance chips are visible and populated with non-empty references
- sensitive geometry remains masked/generalized (no raw precision in UI)
- timeline panel respects OWL-Time semantics (ordering and interval display)

### Focus Mode v3 regression expectations
Regression tests SHOULD validate:
- three-panel coherence (Context/Timeline/Map stays aligned to the same entity)
- governance overlays remain visible where required (CARE tier, sovereignty flags)
- restricted states produce safe UI behavior (redacted/masked/blocked)
- UI does not surface speculative language when policy forbids it

---

## 🧪 Validation & CI/CD

### Where regression runs
Regression E2E suites are typically executed:
- on scheduled workflows (nightly/weekly)
- on release candidate pipelines
- on-demand for high-risk UI changes

PR merge blocking is usually reserved for `@smoke` (and optionally `@governance`), but regression results remain governed and auditable.

### Required regression artifacts
Every regression run MUST produce:
- machine-readable report (JSON and/or JUnit)
- screenshots for failures
- trace/video artifacts (if supported by runner)
- a deterministic run manifest (seed, env hash, suite tags)

Recommended locations:
~~~text
📁 reports/
└── 📁 e2e/
    └── 📁 web-app/
        ├── 🧾 junit.xml
        ├── 🧾 report.json
        ├── 🧾 run-manifest.json
        ├── 📁 traces/
        └── 📁 screenshots/
~~~

---

## 📦 Data & Metadata

### Fixture source of truth
Regression tests MUST use synthetic fixtures from:
- `tests/fixtures/` (shared synthetic assets)
- `tests/e2e/resources/` (E2E synthetic assets)
- `tests/e2e/web-app/resources/` (Web App-specific synthetic assets)

If a regression test needs additional fixtures:
- add them as synthetic assets
- document them in the nearest governed fixture README
- version the fixture bundle ID used by the suite

### Run manifest requirements
Regression runs SHOULD write:
- `suite_tags` including `@regression`
- `seed`
- `env_hash`
- `fixture_bundle_id`
- artifact paths

Do not store raw payload dumps in manifests.

---

## 🌐 STAC, DCAT & PROV Alignment

Regression E2E outputs may be represented as:
- `prov:Activity` (the run)
- `prov:Entity` (report, junit, traces, screenshots)
- `prov:Agent` (CI runner, maintainers)

Where supported:
- OpenLineage facets may record run IDs, input fixture bundle IDs, and output artifact references.
- DCAT alignment can treat reports as `dcat:Distribution` artifacts (mediaType JSON/XML).

Governance-safe rule:
- provenance references must be identifiers and hashes, not raw content.

---

## 🧱 Architecture

### Recommended implementation pattern
Regression suites SHOULD use:
- page objects in `tests/e2e/utils/pages/`
- stable selectors and assertions in `tests/e2e/utils/assertions/`
- deterministic wait helpers (event/state-based)
- explicit test IDs for synthetic entities (Story Nodes, Focus Mode entities)

Design goal:
- tests remain readable, debuggable, and resistant to UI timing variance.

---

## ⚖ FAIR+CARE & Governance

Regression suites MUST block unsafe behavior from becoming release-normal.

Minimum governance assertions for regression:
- no sensitive precision leakage (tooltips, downloads, debug views, JSON overlays)
- CARE tier routing behaves as expected for synthetic Tier A/B/C fixtures
- sovereignty masking holds at required generalization levels
- narrative safety holds (no disallowed speculative claims in governed surfaces)
- provenance surfaces remain present and non-empty (IDs/hashes/links)

If a governance-related regression test fails:
- treat as stop-ship for affected governed surfaces
- route to the relevant working group and FAIR+CARE Council per policy

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Web App regression E2E guide aligned to KFM-MDP v11.2.6 (deterministic, synthetic, governed, artifact-first). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

