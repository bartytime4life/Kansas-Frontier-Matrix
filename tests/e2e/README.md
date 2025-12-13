---
title: "🧭 Kansas Frontier Matrix — End-to-End (E2E) Tests (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-guide"

semantic_document_id: "kfm-tests-e2e-readme"
doc_uuid: "urn:kfm:tests:e2e:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/README.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_transform_permissions:
  - "summarize"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "citation-fabrication"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — End-to-End (E2E) Tests (v11 LTS)**
`tests/e2e/README.md`

**Purpose**  
Define the canonical E2E test suite for Kansas Frontier Matrix (KFM) v11:  
UI + API + governance + narrative flows validated end-to-end using deterministic, sovereignty-safe, synthetic data and CI-enforced gates.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 Tests Index](../README.md) ·
[🧱 Test Architecture](../ARCHITECTURE.md) ·
[🧱 Fixtures](../fixtures/README.md) ·
[🏛️ Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

E2E tests are the system-level trust harness for KFM. They validate that:

- 🧩 user-facing workflows behave correctly (navigation, rendering, interactions)
- 🔒 governance controls are enforced (FAIR+CARE, sovereignty masking, prohibited outputs)
- 🧠 narrative surfaces remain grounded and safe (Story Nodes, Focus Mode panels)
- 🗺️ spatial and temporal UX is coherent (map layers, timeline interactions, query filters)
- 📊 telemetry and provenance are emitted in expected shapes (test run artifacts, energy/carbon summaries)

### Definition
An E2E test is any test that crosses at least two boundaries in one run:

- UI ↔ API
- UI ↔ graph-backed behavior (via API)
- UI ↔ governance overlays / provenance views
- dataset workflow ↔ validation ↔ publish gating
- narrative surface ↔ masking / ethics / citation rules

### Non-goals
E2E tests must not rely on:
- real individuals, real sensitive locations, production tokens, or restricted datasets
- external networks as a required dependency (unless explicitly whitelisted and mocked)
- non-deterministic clocks, random seeds, or arbitrary sleep-based timing

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    ├── 📄 README.md                       — This guide (rules + runbook)
    │
    ├── 📁 web-app/                        — Browser-driven UI flows
    │   ├── 📁 smoke/                      — Fast PR gate scenarios (minimal, high-signal)
    │   ├── 📁 regression/                 — Broader UI behavior coverage
    │   └── 📁 accessibility/              — WCAG flows (keyboard, landmarks, reduced motion)
    │
    ├── 📁 dataset-workflows/              — Intake → validate → publish flows (synthetic)
    │   ├── 📁 ingest-validate/            — Contract + schema gates
    │   └── 📁 publish-preview/            — Preview modes + publish gating
    │
    ├── 📁 governance/                     — Ledger/provenance surfaces + masking enforcement
    │   ├── 📁 care/                       — CARE classification and routing
    │   └── 📁 sovereignty/                — Masking + restricted-output assertions
    │
    ├── 📁 storynodes/                     — Story Node v3 UI flows (rendering + provenance chips)
    ├── 📁 focus-mode/                     — Focus Mode v3 flows (Context/Timeline/Map panels)
    │
    ├── 📁 resources/                      — E2E-only deterministic fixtures (synthetic, non-sensitive)
    └── 📁 utils/                          — Page objects, selectors, stable helpers, wait strategies
~~~

---

## 🧭 Context

### Determinism rules
E2E tests MUST:
- use stable deterministic fixtures (no live random generation unless seeded and recorded)
- use deterministic time where possible (fixed clock / injectable time provider)
- prefer event-based waits over sleeps (state change, selector visible, network idle)
- avoid cross-test coupling (each test is isolated and idempotent)

### Sovereignty and ethics rules
E2E tests MUST:
- never embed or assert raw sensitive coordinates (or plausible real-site geometry)
- validate that restricted outputs remain masked/generalized at required H3 resolutions
- avoid narratives implying genealogy, sacred-site inference, or culturally harmful framing
- use synthetic examples that simulate governance states without enabling real-world harm

### Tagging policy
Use tags to control CI behavior:
- `@smoke` — PR gate, fastest, deterministic
- `@regression` — broader coverage, allowed to take longer
- `@governance` — CARE + sovereignty gating
- `@a11y` — accessibility flows
- `@nightly` — slow or high-volume suites

---

## 📦 Data & Metadata

### Fixture source of truth
E2E tests MUST use synthetic fixtures from:
- `tests/fixtures/` (global synthetic assets)
- `tests/e2e/resources/` (E2E-specific synthetic assets)

No production data. No sensitive coordinates. No identifying text.

### Required E2E artifacts
Every E2E run MUST produce:
- machine-readable report (JUnit and/or JSON)
- screenshots for failures
- trace or video artifact (where supported)
- deterministic run manifest (seed, environment hash, suite tags)

Recommended artifact locations:
~~~text
reports/
└── e2e/
    ├── junit.xml
    ├── report.json
    ├── traces/
    ├── screenshots/
    └── run-manifest.json
~~~

### Run manifest (recommended minimum)
~~~json
{
  "run_id": "e2e_2025-12-13_001",
  "suite_tags": ["@smoke", "@governance"],
  "browser_matrix": ["chromium"],
  "seed": 112233,
  "env_hash": "<sha256>",
  "artifacts": {
    "report": "reports/e2e/report.json",
    "junit": "reports/e2e/junit.xml",
    "traces_dir": "reports/e2e/traces/"
  }
}
~~~

### Telemetry requirements
E2E should contribute to repo-level telemetry:
- runtime duration
- failures by category
- a11y counts (violations, regressions)
- energy/carbon where available

Aggregation target:
~~~text
releases/<version>/tests-e2e-telemetry.json
~~~

---

## 🧱 Architecture

### E2E platform components
E2E testing is composed of:
- runner (suite execution, quarantine rules, artifact capture)
- stack bootstrap (UI/API in deterministic test mode)
- synthetic fixture loader (known states, non-sensitive inputs)
- governance gate (masking and policy enforcement is testable and visible)
- telemetry sink (validates and aggregates run summaries)

### Flake policy
- flaky tests are quarantined behind `@nightly` until fixed
- retries are allowed only with a recorded reason and an issue reference
- governance-related failures are not retryable by default

### Diagrams
~~~mermaid
flowchart TD
  A["Trigger"] --> B["Boot deterministic test stack"]
  B --> C["Load synthetic fixtures"]
  C --> D["Run suites"]
  D --> E["Collect artifacts"]
  E --> F["Validate governance and telemetry"]
  F --> G["CI gate decision"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Node v3 E2E expectations
E2E tests SHOULD validate:
- rendering of Story Node v3 fields (title, narrative body, spacetime, relations)
- provenance chips/evidence links present and non-empty
- spatial geometry is rendered only at permitted precision (masked/generalized if required)
- timeline respects OWL-Time intervals (start/end, ordering, granularity)

### Focus Mode v3 E2E expectations
E2E tests SHOULD validate:
- three-panel behavior (Context/Timeline/Map) with consistent entity grounding
- claims surfaced are attributable to an entity/dataset/experiment/model-card reference
- governance overlays trigger correctly (CARE tier visible; sovereignty flags visible)
- restricted material is withheld, redacted, or generalized

---

## 🧪 Validation & CI/CD

### Where E2E runs in CI
E2E is merge-blocking for `@smoke` (and optionally `@governance`).

Common CI stages:
1. unit tests
2. schema tests
3. integration tests
4. E2E smoke
5. accessibility
6. governance validation
7. telemetry validation

### Local runbook
Use repo scripts (preferred) and keep them stable.

~~~bash
make test-stack-up
make e2e-smoke
make test-stack-down
~~~

If using Playwright/Cypress scripts, ensure the intent exists:
- `e2e:smoke`
- `e2e:regression`
- `e2e:a11y`
- `e2e:governance`

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC / DCAT (optional representations)
- This document may be treated as documentation metadata (DCAT-style dataset record).
- E2E reports may be treated as distributions (JSON, JUnit XML).
- E2E outputs may be represented as non-spatial STAC Items:
  - `geometry: null`
  - `properties.datetime` set to run timestamp
  - assets include report, junit, traces, screenshots

### PROV-O alignment (what E2E produces)
- an E2E run is a `prov:Activity`
- fixtures/configs/built artifacts are `prov:Entity`
- CI and maintainers are `prov:Agent`

Minimal fragment example:
~~~json
{
  "prov:entity": {
    "e2e_report": { "prov:label": "E2E report JSON", "prov:type": "kfm:TestArtifact" }
  },
  "prov:activity": {
    "e2e_run": { "prov:label": "E2E run", "prov:type": "kfm:TestRun" }
  }
}
~~~

---

## ⚖ FAIR+CARE & Governance

E2E suites MUST block merges if they detect:
- sensitive precision leakage (coordinates, geometry dumps, tooltips, downloads)
- CARE routing failures (Tier A/B/C logic mismatched)
- narrative safety failures in governed surfaces
- provenance UI missing required references (IDs/hashes/links)
- accessibility regressions (WCAG-critical failures)

Escalation rule:
- governance-related failures are stop-ship for merges that affect governed outputs
- route to FAIR+CARE Council and the relevant working group for review
- record the failure in the audit ledger where applicable

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Aligned to KFM-MDP v11.2.6 (approved H2 registry, tilde fences, Mermaid-safe labels, governed metadata and footer). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
