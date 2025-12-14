---
title: "🧪 Kansas Frontier Matrix — E2E Web App Regression Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
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

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"
  - "citation-fabrication"

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
<img src="https://img.shields.io/badge/E2E-Regression-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App E2E Index](../README.md) ·
[🧭 E2E Guide](../../README.md) ·
[🏗 Test Architecture](../../../ARCHITECTURE.md)

</div>

---

## 📘 Overview

The regression suite is the “broad coverage” layer of KFM’s Web App E2E testing.

Regression E2E tests are expected to:
- 🧩 validate correctness across **multiple screens/states**
- 🧭 confirm key UX behaviors remain stable across releases
- 🧪 detect slow drift regressions missed by smoke tests
- 🛡️ verify governance is enforced in user-visible surfaces

Regression E2E tests are required to:
- ✅ run against **synthetic fixtures only**
- ✅ remain **deterministic** (seeded, stable time, stable selectors)
- ✅ produce **auditable artifacts** (report + traces + screenshots on failure)
- ✅ avoid external network dependencies (unless explicitly allowlisted by governance)

### In-scope behaviors (regression-grade)

- 🗺️ Map + timeline interactions across multiple actions (toggle layers, filter, revisit state)
- 🧠 Story Node v3 render + provenance chips + safe geometry precision
- 🧩 Focus Mode v3 panels (Context/Timeline/Map) + governance overlays
- 🧭 Search + navigation flows across routes and back/forward history
- 🧾 Publish-adjacent UX flows (preview modes, synthetic-only dataset workflows)

### Out-of-scope behaviors

- unit logic validation (belongs in `tests/unit/`)
- schema-only shape checks (belongs in `tests/schemas/`)
- pixel-perfect visual diffs unless the suite is explicitly designed for it
- performance benchmarking as a merge gate unless mandated by governance

### Suite boundaries (how regression differs)

- `@smoke`: minimal, merge-blocking, fastest, highest-signal
- `@regression`: broader coverage, scheduled and release-candidate friendly
- `@governance`: policy and masking assertions (merge-blocking when touching governed surfaces)

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            ├── 📄 README.md                           — This guide (suite intent + policies)
            │
            ├── 📁 navigation/                         — Multi-route flows (deep links, back/forward, reload)
            ├── 📁 map/                                — MapLibre/Cesium interactions (layers, tooltips, bounds)
            ├── 📁 timeline/                           — Timeline brushing, filters, temporal ordering
            ├── 📁 storynodes/                         — Story Node v3 regression flows
            ├── 📁 focus-mode/                         — Focus Mode v3 regression flows (panels + provenance)
            ├── 📁 governance/                         — CARE tier routing + sovereignty gating (UI-visible)
            │
            ├── 📁 fixtures/                           — Regression-specific synthetic fixtures (optional)
            └── 📁 specs/                              — Runner-native spec files (e.g., *.spec.ts / *.cy.ts)
~~~

Directory policy:
- Put runner-specific entrypoints under `specs/` unless your repo standard differs.
- Prefer fixture registries (scenario ID → bundle) over inline payloads.
- Regression tests must not depend on smoke ordering or cross-test side effects.

---

## 🧭 Context

### Determinism rules (non-negotiable)

Regression suites MUST:
- use a fixed seed (recorded in a run manifest),
- use deterministic time (injectable clock or fixed timestamps),
- avoid arbitrary sleeps; prefer event/state-based waits,
- isolate state (each test idempotent and independent).

Recommended pattern:
- one spec → one primary behavioral claim
- multi-assert flows are allowed only when inseparable and failure diagnosis remains clear

### Flake policy (strict, regression-aware)

- Newly flaky tests are quarantined behind `@nightly` until fixed.
- Retries are permitted only when:
  - the reason is recorded (run manifest + tracking issue)
  - determinism remains intact (no “sleep-and-hope”)
- Governance failures are not retryable by default.

### Tagging guidance

Use tags to control CI routing and artifacts:
- `@regression` — default for this suite
- `@nightly` — slow/high-volume
- `@governance` — CARE + sovereignty + leak checks
- `@a11y` — accessibility-specific regressions (otherwise use the a11y suite)

### Selector discipline

Regression tests SHOULD:
- rely on stable `data-testid` selectors,
- centralize selectors in shared utilities where possible,
- avoid brittle text matching for core routing and gating assertions.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Scheduled, RC, or manual trigger"] --> B["Boot deterministic test stack"]
  B --> C["Load synthetic fixture bundle"]
  C --> D["Run regression suites (@regression)"]
  D --> E["Capture artifacts (report, traces, screenshots)"]
  E --> F["Validate governance and telemetry shapes"]
  F --> G["Publish summaries and upload artifacts"]
~~~

Interpretation:
- Regression E2E is wide coverage + strong artifact capture.
- Governance and telemetry validation remains mandatory because failures are high-risk.

---

## 🧠 Story Node & Focus Mode Integration

Regression coverage must include narrative surfaces because they are the primary user-visible risk boundary.

### Story Node v3 regression expectations

Regression tests SHOULD validate:
- rendering of core Story Node fields (title, narrative, spacetime, relations)
- provenance chips are visible and populated with non-empty references
- sensitive geometry remains masked/generalized (no raw precision in UI)
- timeline panel respects OWL-Time semantics (ordering and interval display)

### Focus Mode v3 regression expectations

Regression tests SHOULD validate:
- three-panel coherence (Context/Timeline/Map aligned to the same entity)
- governance overlays remain visible where required (CARE tier, sovereignty flags)
- restricted states produce safe UI behavior (redacted/masked/blocked)
- governed surfaces do not show disallowed speculative language

### Minimum cross-surface invariants

- entity identity remains stable across route transitions
- governance posture does not weaken due to navigation (masked stays masked; restricted stays restricted)
- provenance surfaces are present (IDs/hashes/links) without dumping raw payloads

---

## 🧪 Validation & CI/CD

### When regression runs

Regression suites are typically executed:
- on scheduled workflows (nightly/weekly),
- on release-candidate pipelines,
- on-demand for high-risk UI or governance changes.

Merge-blocking is usually reserved for `@smoke` (and optionally `@governance`), but regression runs remain governed and auditable.

### Required regression artifacts

Every regression run MUST produce:
- machine-readable report (JSON and/or JUnit)
- screenshots for failures
- trace/video artifacts (if supported by runner)
- a deterministic run manifest (seed, env hash, suite tags, fixture bundle ID)

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

### Governance gating (regression)

If a regression test is tagged `@governance`, it MUST:
- run leak checks (precision/geometry/prohibited-output patterns),
- assert masking invariants,
- assert restricted-state behavior does not degrade.

---

## 📦 Data & Metadata

### Fixture source of truth

Regression tests MUST use synthetic fixtures from:
- `tests/fixtures/` (shared synthetic assets)
- `tests/e2e/resources/` (E2E synthetic assets)
- `tests/e2e/web-app/resources/` (Web App synthetic assets)

If a regression test needs additional fixtures:
- add synthetic assets only,
- document them in the nearest governed fixtures README,
- reference them via a scenario registry (ID → bundle).

### Run manifest requirements

Regression runs SHOULD write:
- `suite_tags` including `@regression`
- `seed`
- `env_hash`
- `fixture_bundle_id`
- `browser_matrix`
- artifact paths

Do not store raw payload dumps in manifests.

Example (simplified):
~~~json
{
  "run_id": "web_app_regression_2025-12-14_001",
  "suite_tags": ["@regression"],
  "browser_matrix": ["chromium"],
  "seed": 112233,
  "env_hash": "<sha256>",
  "fixture_bundle_id": "kfm_web_app_regression_synth_v11_2_6",
  "artifacts": {
    "report": "reports/e2e/web-app/report.json",
    "junit": "reports/e2e/web-app/junit.xml",
    "traces_dir": "reports/e2e/web-app/traces/"
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Regression E2E outputs may be represented as:
- `prov:Activity` (the run)
- `prov:Entity` (report, junit, traces, screenshots)
- `prov:Agent` (CI runner, maintainers)

Where supported:
- OpenLineage facets may record run IDs, fixture bundle IDs, and output artifact references.
- DCAT alignment can treat reports as `dcat:Distribution` artifacts (`mediaType` JSON/XML).

Governance-safe rule:
- provenance references must be identifiers and hashes, not raw content.

---

## 🧱 Architecture

### Recommended implementation pattern

Regression suites SHOULD use:
- page objects in `tests/e2e/utils/pages/`
- shared assertions in `tests/e2e/utils/assertions/`
- deterministic wait helpers (event/state-based)
- shared governance utilities for leak checks and redaction-safe reporting

Design goal:
- tests remain readable, debuggable, and resistant to UI timing variance.

### Anti-patterns (avoid)

- embedding large fixture JSON directly in spec files
- asserting pixel coordinates or layout exactness without a dedicated visual suite
- using time-based sleeps instead of readiness markers
- logging full API payloads to CI output or artifacts without redaction

---

## ⚖ FAIR+CARE & Governance

Regression suites must prevent unsafe behavior from becoming release-normal.

Minimum governance assertions for regression:
- no sensitive precision leakage (tooltips, downloads, debug views, JSON overlays)
- CARE tier routing behaves as expected for synthetic Tier A/B/C fixtures
- sovereignty masking holds at required generalization levels
- narrative safety holds (no disallowed speculative claims in governed surfaces)
- provenance surfaces remain present and non-empty (IDs/hashes/links)

If a governance-related regression test fails:
- treat as stop-ship for affected governed surfaces,
- route to the relevant working group and FAIR+CARE Council per policy,
- fix the underlying UI/API behavior (do not weaken rules as a shortcut).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Expanded and normalized Web App regression E2E guide; corrected relative paths; clarified determinism, artifacts, governance gating, and fixture/run-manifest expectations under KFM‑MDP v11.2.6. |

<div align="center">

[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
