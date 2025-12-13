---
title: "🧾 Kansas Frontier Matrix — E2E Assertions (Policy · A11y · Telemetry) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/utils/assertions/README.md"

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
intent: "tests-e2e-assertions-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-assertions-readme"
doc_uuid: "urn:kfm:tests:e2e:assertions:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/utils/assertions/README.md"
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
  - "tests/e2e/utils/assertions/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — E2E Assertions (Policy · A11y · Telemetry) (v11 LTS)**
`tests/e2e/utils/assertions/README.md`

**Purpose**  
Define the canonical E2E assertion layer for KFM: reusable, deterministic checks that enforce governance, sovereignty safety, accessibility (WCAG), and telemetry/provenance expectations across end-to-end tests.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧭 E2E Guide](../../README.md) ·
[🧰 E2E Utils](../README.md) ·
[🧱 Fixtures](../../../fixtures/README.md)

</div>

---

## 📘 Overview

The assertions layer exists to keep E2E tests:

- **high-signal** (failures point to a specific policy/UX regression)
- **deterministic** (no sleep-based “fixes” and no flaky timing expectations)
- **governance-enforcing** (sovereignty masking, CARE routing, prohibited outputs)
- **accessible by construction** (role-first selectors and WCAG checks)
- **auditable** (assertions map cleanly to CI gates and telemetry artifacts)

### Assertion categories (normative)
1. **Governance assertions**
   - sovereignty-safe masking/generalization checks
   - restricted output handling (redacted/masked/blocked)
   - prohibited output checks (coordinate leaks, unsafe narrative forms)

2. **Accessibility assertions**
   - keyboard navigation flows
   - landmark/heading sanity checks
   - critical WCAG regressions (role/name/label failures)

3. **Telemetry assertions**
   - required telemetry payload shape present for E2E runs
   - run manifest present and consistent
   - governance-related failure classifications recorded (when supported)

### What an assertion is (KFM definition)
An assertion is a reusable test helper that validates one concrete, user-visible or policy-visible claim. It must be safe to run repeatedly and must not depend on external networks or non-deterministic clocks.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 utils/
        └── 📁 assertions/
            ├── 📄 README.md                      — This guide (assertion patterns + contracts)
            ├── 📄 governance.assert.ts           — Sovereignty masking + CARE routing + prohibited outputs
            ├── 📄 a11y.assert.ts                 — WCAG critical checks + keyboard flows
            └── 📄 telemetry.assert.ts            — Run manifest + telemetry shape checks
~~~

---

## 🧭 Context

### Determinism contract (non-negotiable)
Assertions MUST:
- prefer event/state checks over time-based sleeps
- be idempotent and safe to rerun
- avoid cross-test shared state
- avoid dependence on wall-clock time unless a fixed clock is injected

Assertions MUST NOT:
- introduce retries by default (retries are a suite-level decision)
- log raw payloads that might include secrets or sensitive fields
- assert on brittle UI details (CSS classnames, pixel-perfect layout)

### Sovereignty safety contract (non-negotiable)
Assertions MUST:
- never embed real or plausible sensitive coordinates
- never validate that raw precise geometry is displayed for restricted content
- include positive checks for masked/generalized behavior where required
- treat any coordinate precision leak as a CI-blocking governance failure

### Accessibility contract
Assertions SHOULD:
- use role-based selectors and visible text checks
- verify keyboard-only operation for critical flows
- fail with actionable messages (what was missing, where, and why it matters)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Test executes a workflow"] --> B["Call shared assertion"]
  B --> C["Assertion checks UI state"]
  C --> D["Assertion checks policy gates"]
  D --> E["Assertion records artifacts on failure"]
  E --> F["CI gate passes or blocks"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Assertions must support narrative surfaces because policy failures often surface here first.

### Story Node v3 assertion expectations
Assertions SHOULD cover:
- provenance chips/evidence references are present and non-empty
- restricted content renders as redacted/masked/blocked (as applicable)
- no raw coordinate precision appears in:
  - page text
  - tooltips
  - debug panels
  - exported JSON views (if exposed by UI)

### Focus Mode v3 assertion expectations
Assertions SHOULD cover:
- three-panel consistency (Context/Timeline/Map do not contradict each other)
- governance overlays appear when required (CARE tier, sovereignty flags)
- any restricted state yields a safe UI response (no leakage)

---

## 🧪 Validation & CI/CD

### Where assertions are used
- `@smoke` suites use only the most stable assertions (merge-blocking)
- `@governance` suites exercise sovereignty and CARE enforcement assertions
- `@a11y` suites use accessibility assertions
- `@nightly` may include slower, broader checks (kept out of PR gates)

### Failure classification (recommended)
Assertions should classify failures into one of:
- `governance:sovereignty-leak`
- `governance:care-routing`
- `governance:prohibited-output`
- `a11y:wcag-critical`
- `telemetry:shape-mismatch`
- `telemetry:missing-artifacts`

Where supported, write the classification into the E2E run manifest or report metadata.

### Flake policy
Assertions MUST NOT “paper over” flakiness.
- If a state is legitimately async, provide a deterministic wait helper.
- If the UI has no reliable readiness signal, add one to the app (preferred) rather than sleeping.

---

## 📦 Data & Metadata

### Inputs allowed to assertions
Assertions may accept:
- a page object handle
- a root element locator
- a small, sanitized expected-value struct (IDs, flags, tiers)
- a fixture identifier (synthetic only)

Assertions must not accept:
- real-world person names (unless explicitly public-domain and vetted)
- plausible real coordinates or site-like geometries
- secrets, tokens, or raw API keys

### Recommended assertion output on failure
- an actionable error message (what failed, where)
- a screenshot name using deterministic conventions (suite + test + timestamp)
- a trace capture trigger (where supported)
- a short, sanitized snippet of relevant UI text (no payload dumps)

Example (pattern only):
~~~ts
throw new Error([
  "governance:sovereignty-leak",
  "Expected masked geometry in tooltip, but detected a coordinate-like pattern.",
  "Location: Focus Mode map tooltip"
].join(" | "));
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Assertions may verify the presence of provenance references (IDs, hashes, links) without attempting to interpret or fabricate catalog metadata.

Recommended checks for governed surfaces:
- evidence/provenance IDs present (non-empty)
- experiment/model card references present when AI surfaces are shown
- run manifest reference present for E2E execution artifacts

Assertions must not:
- fabricate STAC/DCAT IDs
- invent PROV entities/activities that were not emitted
- interpret sovereignty status beyond what the UI and API expose in test mode

---

## 🧱 Architecture

### Assertion module contract (recommended)
Each assertion module should expose:
- small, composable functions (one primary claim per function)
- clear error messages and stable failure codes
- optional helpers to scan UI-visible text for prohibited patterns

### Prohibited-pattern scanning (recommended)
For sovereignty leak defense, include scanners that detect:
- coordinate-like patterns (lat/lon, UTM-like strings)
- high-precision decimals beyond allowed thresholds
- raw GeoJSON dumps in UI surfaces when policy forbids them

Pattern scanning must be conservative:
- it must avoid false positives on innocuous numbers
- it must be configurable per test context (e.g., a “public, non-sensitive geometry allowed” fixture)

---

## ⚖ FAIR+CARE & Governance

### Minimum governance gate (required)
Assertion coverage must be sufficient to block merges when:
- a sensitive precision leak is detected
- CARE routing is inconsistent with the UI state
- a restricted state fails to redact/mask/block content

### Ethical text in fixtures and assertions
All strings used by assertions (and fixtures they reference) must:
- remain synthetic and non-identifying
- avoid culturally harmful framing
- avoid speculative narrative forms in governed surfaces

### Escalation rule (recommended)
If an assertion fails with a governance failure classification:
- treat as stop-ship for affected PRs that touch governed surfaces
- route to the relevant working group plus FAIR+CARE Council review where applicable

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial E2E assertions guide aligned to KFM-MDP v11.2.6 (governance, a11y, telemetry assertions; deterministic contracts; sovereignty-safe rules). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

