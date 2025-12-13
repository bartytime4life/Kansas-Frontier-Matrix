---
title: "🧪 KFM E2E — Expected UI Scenario (fm_synth_003) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/README.md"

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
intent: "tests-e2e-expected-ui-scenario"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-expected-ui-scenario-fm-synth-003"
doc_uuid: "urn:kfm:tests:e2e:expected-ui:scenario:focus-mode:fm_synth_003:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/README.md"
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

signature_ref: "../../../../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 expected-ui scenario framework update"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Expected UI Scenario — fm_synth_003 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/README.md`

**Purpose**  
Define the **canonical expected-ui baselines** for the Focus Mode v3 regression scenario `fm_synth_003`.  
This scenario is **synthetic**, **deterministic**, and **sovereignty-safe**, and is designed to validate **governance-visible UI behavior** (CARE labels, masking indicators, provenance chips) across the 3-panel Focus Mode surface.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Expected_UI-blueviolet" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__003-informational" />
<img src="https://img.shields.io/badge/Sovereignty-Safe-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Scenarios Index](../README.md) ·
[🧾 Expected UI Root](../../README.md) ·
[🧪 Focus Mode Regression](../../../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

### Scenario intent (high-signal)
`fm_synth_003` is a **governance-forward** Focus Mode scenario. It exists to catch regressions where:
- governance states are computed correctly but **not surfaced** correctly in UI,
- masking/precision rules hold in data but **leak through UI affordances** (tooltips, debug panels, downloads),
- provenance exists but **UI chips or evidence links** go missing,
- A11y regressions occur in key policy surfaces (CARE badge, sovereignty flag, provenance chip lists).

### What this scenario must validate
This scenario MUST be able to assert (via `expected_*.json`) that:

- **Context panel**
  - displays the expected entity label/title (synthetic)
  - shows CARE tier label(s) and any sovereignty indicators required by policy
  - renders provenance/evidence chips in a stable, non-empty way (IDs/hashes allowed; no secrets)

- **Timeline panel**
  - shows time bounds consistently (no dependence on system clock)
  - respects ordering and granularity rules (OWL-Time aligned behavior in UI)
  - does not surface restricted precision through hover details

- **Map panel**
  - renders a stable “masked/generalized” representation when required
  - never displays raw coordinates or high-precision geometry
  - shows correct layer toggle behavior for the scenario state

### What this scenario must NOT include
- real persons, real places, real sensitive locations
- any plausible archaeological/sacred-site geometry
- production tokens, secrets, or network dependencies
- “debug coordinate readouts” as part of expected UI

---

## 🗂️ Directory Layout

~~~text
📁 fm_synth_003/
├── 📄 README.md                              — This document (scenario intent + baseline rules)
│
├── 🧾 scenario_manifest.json                 — Deterministic inputs (seed, viewport, routes, flags)
│
├── 🧾 expected_context_panel.json            — Stable assertions for Context panel (no speculation)
├── 🧾 expected_timeline_panel.json           — Stable assertions for Timeline panel
├── 🧾 expected_map_panel.json                — Stable assertions for Map panel (masking-safe)
│
├── 🧾 expected_governance.json               — CARE + sovereignty + masking expectations
├── 🧾 expected_provenance.json               — Evidence chips (IDs/hashes/links) + visibility rules
├── 🧾 expected_a11y.json                     — Accessibility assertions (roles, landmarks, keyboard)
│
└── 📁 🖼️ snapshots/                          — Optional visual baselines (secondary to semantic)
    └── 📄 README.md                          — Snapshot policy + filenames + update rules
~~~

Directory policy:
- `expected_*.json` files are the **primary** source of truth.
- `snapshots/` is **optional** and MUST remain minimal.

---

## 🧭 Context

### Determinism contract
`fm_synth_003` assets MUST be authored so tests can run deterministically:
- fixed viewport(s) declared in `scenario_manifest.json`
- fixed scenario IDs and entity IDs (synthetic)
- no dependence on runtime clocks, time zones, or “today” behavior
- event-based waits only (UI-ready markers, stable selectors)

### Sovereignty + ethics contract
All scenario baselines MUST:
- assert that restricted precision is **not present** in any user-visible surface
- simulate sovereignty/masking states using **synthetic** content only
- avoid culturally harmful phrasing even in test strings
- remain compatible with H3-masking expectations (masking resolution is a declared expectation, not raw geometry)

### Snapshot contract (if used)
If snapshots exist for `fm_synth_003`, they MUST:
- never contain tooltips or overlays that could reveal precision
- capture only safe surfaces (panel chrome, badges, masked map state)
- be treated as secondary validation (semantic baselines come first)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario_manifest.json"] --> B["Boot deterministic test stack"]
  B --> C["Open Focus Mode route (fm_synth_003)"]
  C --> D["Assert semantic baselines (expected_*.json)"]
  D --> E["Optional: compare snapshots"]
  E --> F["Emit artifacts + telemetry + governance signals"]
~~~

Interpretation:
- Baseline JSON assertions are required.
- Snapshots are optional and must never replace governance validation.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 panels covered by this scenario
`fm_synth_003` is expected to exercise all three Focus Mode panels:

- **Context**
  - governance badges (CARE tier, sovereignty indicator)
  - provenance chips (visible + non-empty)
  - stable entity identity (synthetic id/title)

- **Timeline**
  - stable date rendering and ordering
  - safe truncation (no hidden coordinate or debug leaks)

- **Map**
  - masked/generalized display when required
  - no coordinate readouts in UI, tooltips, or downloads
  - stable camera state (no inertial drift)

### Narrative safety boundary
This scenario is not a narrative generator test.
If narrative text appears in UI, it MUST:
- remain factual and synthetic
- avoid speculation
- avoid genealogy inference
- avoid restricted cultural inference

---

## 🧪 Validation & CI/CD

### CI tagging expectations
This scenario SHOULD run under:
- `@regression` (expected-ui baselines)
- `@governance` (policy-visible UI assertions)
- `@a11y` (minimum critical A11y checks)

This scenario MUST NOT be promoted to `@smoke` unless:
- it is consistently deterministic,
- flake rate is near zero,
- it adds high-signal coverage that cannot be achieved elsewhere.

### Update workflow (strict)
When updating `fm_synth_003`:
1. Update the semantic baseline(s) (`expected_*.json`) first.
2. Update the spec assertions next (in `.../specs/`).
3. Update snapshots last (if they exist), with a clear reason.

Governance-related diffs are **not retryable by default** in CI.

---

## 📦 Data & Metadata

### scenario_manifest.json (required)
`scenario_manifest.json` SHOULD declare:
- `scenario_id`: `"fm_synth_003"`
- `seed`: deterministic seed used by the scenario
- `route`: Focus Mode navigation entry point
- `viewport`: width/height (and optionally device profile)
- `governance_mode`: flags that enable policy surfaces for testing
- `fixtures`: references to API mocks or local synthetic fixtures

Example (shape only):
~~~json
{
  "scenario_id": "fm_synth_003",
  "seed": 112233,
  "route": "/focus-mode?scenario=fm_synth_003",
  "viewport": { "width": 1280, "height": 720 },
  "governance_mode": { "enable_overlays": true, "strict_masking": true },
  "fixtures": {
    "api_mocks_ref": "../api_mocks/fm_synth_003.json",
    "expected_ui_ref": "./expected_governance.json"
  }
}
~~~

### expected_governance.json (required)
This file MUST express governance expectations without encoding sensitive data.

Example (shape only):
~~~json
{
  "scenario_id": "fm_synth_003",
  "care": { "tier": "B", "label": "Public · Low-Risk" },
  "sovereignty": { "flags_visible": true, "restricted_precision_blocked": true },
  "masking": { "required": true, "h3_min_resolution": 7 },
  "ui_constraints": {
    "no_raw_coordinates": true,
    "no_geometry_debug_views": true
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O mapping (conceptual)
- Scenario execution is a `prov:Activity` (kfm:TestRun).
- Baseline JSON files are `prov:Entity` (kfm:ExpectedUIBaseline).
- CI runner and maintainers are `prov:Agent`.

### Artifact classification
All scenario artifacts are **non-spatial documentation/test artifacts**:
- no geometry exports
- no coordinate assertions
- no real-world location semantics

---

## 🧱 Architecture

### Separation of responsibilities
- **Specs** define *what* to test (flows and assertions).
- **Pages** define *how* to interact with UI (selectors and actions).
- **Assertions** define *how* to verify outcomes (semantic checks, governance checks).
- **Expected UI baselines** define *what “correct” means* for a scenario (this folder).

`fm_synth_003` is authored to keep correctness anchored in:
- stable JSON baselines (`expected_*.json`)
- minimal, stable selectors (no fragile DOM dependence)
- explicit governance checks (not implied behavior)

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable gates (scenario-level)
This scenario MUST fail if it detects:
- any raw coordinate leakage in UI
- masking indicators missing when required
- CARE tier label missing or incorrect
- provenance chips missing or empty when required
- accessibility regressions in policy surfaces (labels, roles, keyboard access)

### Escalation routing
If a governance-related expectation fails:
- treat as **stop-ship** for merges affecting governed outputs
- route to FAIR+CARE Council + relevant working group
- record the failure in the governance/audit ledger per project policy

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial expected-ui scenario guide for `fm_synth_003` (Focus Mode regression; governance-forward; deterministic). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

