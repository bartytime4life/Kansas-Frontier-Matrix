---
title: "🧾 Kansas Frontier Matrix — Web App Regression Specs (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/specs/README.md"

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
intent: "tests-e2e-web-app-regression-specs"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-specs-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:specs:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/specs/README.md"
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
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/web-app/regression/specs/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Web App Regression Specs (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/specs/README.md`

**Purpose**  
Define the **canonical regression spec entrypoints** for KFM’s web-app E2E suite.  
This folder hosts **runner-facing spec files** that orchestrate feature regressions (navigation, map, Focus Mode, governance) using **synthetic fixtures**, **deterministic waits**, and **governance-safe assertions**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Suite-Web%20App%20Regression-blueviolet" />
<img src="https://img.shields.io/badge/Mode-E2E%20Specs-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App Regression](../README.md) ·
[🧭 E2E Guide](../../../README.md) ·
[🧪 Tests Index](../../../../README.md)

</div>

---

## 📘 Overview

This directory contains **E2E spec files** that are designed to be:

- ✅ **merge-friendly** (high-signal failures; minimal noise),
- ✅ **runner-compatible** (Playwright/Cypress/or equivalent patterns),
- ✅ **fixture-driven** (scenario registries, expected UI, provenance fragments),
- ✅ **governance-safe** (no precision leaks; restricted-state invariants enforced),
- ✅ **deterministic** (event-based waits, stable selectors, stable clocks where supported).

### What belongs in `specs/`

Specs in this folder SHOULD:
- orchestrate cross-feature “regression” runs (smoke vs full),
- call into feature suites (navigation/map/focus-mode/governance) where appropriate,
- enforce consistent tagging conventions (e.g., `@smoke`, `@regression`, `@governance`, `@a11y`),
- produce auditable artifacts (report + trace + redacted summaries),
- ensure governance leak checks execute when required.

Specs in this folder SHOULD NOT:
- embed large payload fixtures inline (use `fixtures/` folders),
- hardcode secrets, tokens, or production URLs,
- use timing sleeps as correctness gates.

---

## 🗂️ Directory Layout

This folder is structured for **CI parallelism** and **stable discoverability**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            ├── 📄 README.md                                  — Regression suite overview
            │
            ├── 📁 navigation/                                — Navigation regressions (deep-links, guards, state restore)
            ├── 📁 map/                                       — Map regressions (layers, interactions, budgets)
            ├── 📁 focus-mode/                                — Focus Mode regressions (Context/Timeline/Map panels)
            ├── 📁 governance/                                — Governance regressions (masking, CARE routing, leak checks)
            │
            └── 📁 specs/
                ├── 📄 README.md                              — This guide (spec conventions + entrypoints)
                │
                ├── 📄 regression_smoke.spec.ts               — Merge-blocking minimal cross-feature regression
                ├── 📄 regression_full.spec.ts                — Broader cross-feature regression coverage
                ├── 📄 regression_governance.spec.ts          — Governance-only cross-feature run (masking/leak checks)
                ├── 📄 regression_a11y_smoke.spec.ts          — Minimal navigation-linked a11y smoke (if used)
                │
                └── 🧾 spec_registry.json                      — Optional: spec ID → tags → inclusion policy
~~~

Notes:
- Filenames are a **canonical target layout**; adapt extensions to your runner.
- If `spec_registry.json` is present, it MUST remain deterministic and safe to publish.

---

## 🧭 Context

### Spec design principles (high-signal)

A regression spec SHOULD:
- assert one primary outcome per scenario (avoid “kitchen sink” tests),
- fail with actionable diagnostics (route, selector, rule ID),
- avoid brittle CSS selectors (prefer `data-testid`),
- prefer “ready markers” to global network-idle.

### Determinism requirements

Specs MUST:
- avoid nondeterministic clocks unless the stack provides a deterministic test clock,
- avoid random data generation unless seeded AND recorded in run manifests,
- avoid “sleep-and-hope” timing.

Recommended event-based waits:
- route-ready markers (page root `data-testid`),
- panel-ready markers (Focus Mode: context/timeline/map ready flags),
- overlay-ready markers (governance banner/CARE tier visible),
- bounded retry loops only when supported by the runner and tracked.

### Tagging and CI intent (recommended)

- `@smoke` — fastest set, merge-blocking
- `@regression` — broader coverage
- `@governance` — CARE/sovereignty/leak checks
- `@a11y` — only when the spec explicitly validates accessibility behavior

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["CI selects spec entrypoint"] --> B["Boot deterministic test stack"]
  B --> C["Load synthetic fixtures and registries"]
  C --> D["Execute spec (feature suites + shared utilities)"]
  D --> E["Run governance leak checks where required"]
  E --> F["Collect artifacts (report, traces, screenshots)"]
  F --> G["Write telemetry summary"]
  G --> H["CI gates: pass or block"]
~~~

Interpretation:
- Specs are orchestration points: they run feature regressions, enforce governance utilities, and produce auditable outputs.

---

## 🧠 Story Node & Focus Mode Integration

Regression specs SHOULD include at least one scenario that crosses narrative surfaces, because policy failures become user-visible there.

Minimum recommended narrative coverage:
- open a Story Node route (synthetic),
- transition into Focus Mode,
- verify provenance chips are non-empty (IDs/hashes only),
- verify restricted/masked states persist across navigation.

If narrative coverage is handled exclusively in `focus-mode/specs/`, then cross-feature entrypoints SHOULD still:
- include one “routing into Focus Mode” smoke scenario, or
- explicitly delegate to the Focus Mode smoke spec in the feature suite.

---

## 🧪 Validation & CI/CD

### Merge-blocking expectations

At minimum, CI SHOULD treat these as merge-blocking:
- `regression_smoke.spec.*`
- `regression_governance.spec.*` (when PR touches governed surfaces)

### Required artifacts (per spec run)

Each spec run MUST produce:
- machine-readable report (JUnit/JSON),
- traces or videos where supported,
- screenshots for failures,
- a run manifest with tags, env hash, and seed(s).

Recommended artifact directory:
~~~text
reports/
└── e2e/
    ├── junit.xml
    ├── report.json
    ├── traces/
    ├── screenshots/
    └── run-manifest.json
~~~

### Flake policy

- Flaky tests are quarantined behind scheduled runs until fixed.
- Governance failures are not retryable by default.
- If a spec fails intermittently, improve waits/readiness markers rather than adding sleeps.

---

## 📦 Data & Metadata

### Optional spec registry (recommended shape)

If `spec_registry.json` exists, it SHOULD define inclusion and tagging policy without encoding sensitive content.

~~~json
{
  "schema_version": "v11.2.6",
  "specs": {
    "regression_smoke": {
      "file": "regression_smoke.spec.ts",
      "tags": ["@smoke"],
      "ci_policy": "merge_blocking"
    },
    "regression_governance": {
      "file": "regression_governance.spec.ts",
      "tags": ["@regression", "@governance"],
      "ci_policy": "merge_blocking_for_governed_surfaces"
    }
  }
}
~~~

### Run manifest expectations (spec output)

Specs SHOULD write or contribute to a run manifest containing:
- `run_id`, `job_id`
- spec name and tags
- environment hash
- browser/device matrix (if applicable)
- seed(s)
- artifact paths

---

## 🌐 STAC, DCAT & PROV Alignment

Spec execution produces test artifacts (not scientific datasets):

- **DCAT**: reports can be treated as `dcat:Distribution` artifacts (`mediaType: application/json`).
- **STAC**: if represented as STAC items:
  - `geometry: null`
  - `properties.datetime` set to run timestamp
- **PROV-O**:
  - spec run is `prov:Activity`,
  - fixtures/configs are `prov:Entity`,
  - CI runner and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Recommended spec architecture (composition-first)

Specs SHOULD:
- delegate UI interactions to page objects,
- delegate stable waits to shared wait utilities,
- delegate policy checks to governance utilities (e.g., leak checks),
- consume fixture registries rather than embedding payloads.

Anti-patterns:
- one spec file importing unrelated fixtures ad hoc,
- duplicating selectors across suites,
- printing raw network payloads to console for debugging.

---

## ⚖ FAIR+CARE & Governance

Regression specs exist to ensure:
- governance controls remain enforceable under real navigation and state transitions,
- no precision leaks are introduced by UI refactors,
- restricted or masked states remain stable across back/forward/refresh.

If a regression spec detects a governance failure:
- block merges affecting governed surfaces,
- fix the underlying behavior,
- do not weaken allowlists as a shortcut.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial regression specs entrypoint guide aligned to KFM‑MDP v11.2.6 (deterministic orchestration, artifact requirements, governance-safe tagging). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

