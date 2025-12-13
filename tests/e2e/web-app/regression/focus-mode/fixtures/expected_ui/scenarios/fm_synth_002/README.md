---
title: "🧭 KFM E2E Scenario — Focus Mode v3 Expected UI (fm_synth_002) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Scenario Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-focus-mode-expected-ui-scenario"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-focus-mode-expected-ui-fm-synth-002"
doc_uuid: "urn:kfm:tests:e2e:focus-mode:expected-ui:scenario:fm_synth_002:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/README.md"
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

signature_ref: "../../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Focus Mode v3 — Expected UI Scenario (fm_synth_002) (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/README.md`

**Purpose**  
Define the **canonical expected UI baselines** for the `fm_synth_002` Focus Mode v3 regression scenario.  
This scenario validates **Context · Timeline · Map** panel behavior, governance overlays, provenance surfaces, and masking rules using **synthetic, sovereignty-safe fixtures**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Expected%20UI%20Baselines-informational" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__002-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Scenarios Index](../README.md) ·
[🧾 Expected UI Root](../../README.md) ·
[🧪 Focus Mode Regression](../../../../README.md)

</div>

---

## 📘 Overview

### Scenario intent
`fm_synth_002` is a deterministic Focus Mode v3 regression scenario designed to catch:
- panel-layout regressions (Context/Timeline/Map arrangement and state transitions)
- data-to-UI grounding regressions (entity context shown without missing references)
- governance overlay regressions (CARE tier display, sovereignty masking indicators)
- provenance surface regressions (IDs, hashes, evidence chips present and non-empty)
- unsafe precision regressions (raw coordinate leakage, overly precise geometry disclosure)

### What makes `fm_synth_002` different from `fm_synth_001`
This scenario SHOULD focus on at least one *distinct* failure class to avoid redundant coverage, for example:
- a different governance tier routing state (Tier B vs Tier C)
- a different entity cluster type (place-dominant vs event-dominant)
- a different map interaction path (layer toggle, timeline brush → map filter)
- a different provenance composition (experiment reference + model card reference present)

Keep the scenario’s purpose narrow: one scenario should detect one primary class of regression reliably.

### What this directory contains
This directory binds together:
- a scenario manifest (what state to load)
- expected UI baselines (what must be shown)
- governance expectations (what must be masked/redacted)
- optional visual snapshots (only if semantic baselines are insufficient)

### What this scenario must never contain
- any real individuals, real addresses, or identifying text
- any plausible sensitive site geometry, raw coordinates, or raw precision tooltips
- any production tokens, live endpoints, or required external network dependencies
- any “creative” narrative content (the scenario is policy + UX validation, not fiction)

---

## 🗂️ Directory Layout

~~~text
📁 fm_synth_002/
├── 📄 README.md                                  — This guide (scenario intent + rules)
│
├── 🧾 scenario_manifest.json                      — Scenario loader inputs (routes, fixtures, toggles)
├── 🧾 expected_context_panel.json                 — Expected Context panel content (subset, deterministic)
├── 🧾 expected_timeline_panel.json                — Expected Timeline panel events + OWL-Time assertions
├── 🧾 expected_map_panel.json                     — Expected Map panel state (layers, overlays, precision rules)
│
├── 🧾 expected_governance.json                    — CARE + sovereignty expectations (masking, tier, routing)
├── 🧾 expected_provenance.json                    — Provenance expectations (IDs/hashes/links present)
│
├── 🧾 expected_a11y.json                          — Accessibility expectations (landmarks, headings, focus order)
├── 🧾 expected_telemetry_facets.json              — Expected test telemetry facets emitted for this scenario
│
└── 📁 snapshots/                                 — Optional visual baselines (use only when necessary)
    ├── 📄 README.md                               — Snapshot governance + naming rules
    └── 🖼️ <optional baseline pngs>                — Minimal stable baseline set only
~~~

Policy notes:
- `expected_*.json` files define **semantic baselines** and are preferred over screenshots.
- If snapshots exist, they MUST be subordinate to semantic gates (governance/provenance/a11y).

---

## 🧭 Context

### Determinism contract
All `fm_synth_002` runs MUST:
- use seeded, synthetic fixtures (seed recorded in run manifest)
- run with a deterministic clock (fixed time provider where available)
- avoid arbitrary sleeps; prefer event/state-based waits
- remain idempotent (reruns do not depend on prior state)

### Governance contract
The scenario MUST explicitly define:
- the intended CARE tier state (and what the UI must show)
- the intended sovereignty masking state (and what the UI must not show)
- expected redactions (where restricted material must be withheld)

If a governance rule changes upstream, update:
1) `expected_governance.json` first, then
2) panel baselines, and only then
3) snapshots (if any)

### Accessibility contract
This scenario MUST include accessibility expectations suitable for E2E validation, including:
- stable heading structure
- keyboard focus order on primary controls
- visible focus states in reduced-motion mode
- landmark presence for major UI regions
- no “governance-only” content that is inaccessible to assistive tech

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario_manifest.json"] --> B["Boot deterministic test stack"]
  B --> C["Inject synthetic fixtures"]
  C --> D["Navigate to Focus Mode view"]
  D --> E["Assert governance expectations (expected_governance.json)"]
  E --> F["Assert panel expectations (expected_*_panel.json)"]
  F --> G["Assert provenance surfaces (expected_provenance.json)"]
  G --> H["Assert accessibility expectations (expected_a11y.json)"]
  H --> I["Validate telemetry facets (expected_telemetry_facets.json)"]
~~~

Interpretation:
- Governance checks are evaluated before panel assertions.
- Telemetry validation is last, after the UI is confirmed safe and stable.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 minimum coverage
`fm_synth_002` MUST exercise:
- Context panel: at least one entity grounding reference (graph/dataset/experiment/model card ID)
- Timeline panel: at least one interval alignment check (OWL-Time start/end present and ordered)
- Map panel: at least one masking/precision rule check (no raw precision surfaces)

### Story Node adjacency
If this scenario touches Story Node-linked UI:
- it MUST validate that provenance chips are present
- it MUST validate that restricted material is withheld or generalized
- it MUST avoid asserting “creative narrative” text (assert structure + citations instead)

---

## 🧪 Validation & CI/CD

### Tagging recommendations
- `@regression` (default)
- `@governance` (required when tier/masking is involved)
- `@a11y` (required if this scenario is the coverage anchor for keyboard/landmarks)

Avoid tagging as `@smoke` unless:
- it is stable across CI runners
- it has near-zero flake rate
- it executes quickly and deterministically

### Baseline update rules
A baseline update is allowed only when:
- UI behavior changes intentionally
- governance rules are still satisfied
- the change is explained in the PR (what changed and why)

Baseline update order:
1. `expected_governance.json`
2. `expected_*_panel.json`
3. `expected_provenance.json`
4. `expected_a11y.json`
5. optional snapshots (last)

---

## 📦 Data & Metadata

### scenario_manifest.json expectations
The scenario manifest SHOULD declare:
- route(s) and initial UI entrypoint
- fixture bundle(s) to load (synthetic)
- feature flags (if required for deterministic mode)
- viewport profile(s) used for this scenario
- governance mode toggles (test-only, never production)

Example shape (illustrative):
~~~json
{
  "scenario_id": "fm_synth_002",
  "entry_route": "/focus-mode?entity=fm_synth_002_entity",
  "fixtures": ["focus_mode_synth_bundle_002"],
  "viewport": "1280x720",
  "governance_mode": "enabled",
  "clock_mode": "fixed"
}
~~~

### expected_* baselines policy
Expected baselines SHOULD:
- assert stable, high-signal invariants
- avoid brittle pixel-perfect or full-text assertions
- use safe subsets (IDs, labels, presence of sections, ordering rules)

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O mapping (conceptual)
- the scenario run is a `prov:Activity` (kfm:TestRun)
- expected baselines are `prov:Entity` (kfm:TestBaseline)
- generated reports are `prov:Entity` (kfm:TestArtifact)
- CI runner and maintainers are `prov:Agent`

### DCAT mapping (optional but compatible)
- scenario baselines may be represented as `dcat:Dataset` (documentation/test data)
- run artifacts may be represented as `dcat:Distribution` (report JSON, traces)

This mapping should remain non-spatial and non-sensitive.

---

## 🧱 Architecture

### Expected UI baseline strategy
This scenario is designed to prefer:
1) semantic baselines (`expected_*.json`) and explicit assertions
2) artifact trace review for failures
3) snapshots only when semantic checks cannot detect the regression

This keeps CI stable and reduces flake risk while preserving governance enforcement.

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable invariants
This scenario MUST block merges if it detects:
- any coordinate/precision leakage in UI surfaces
- CARE tier mismatch (UI vs expected routing)
- sovereignty masking not applied when expected
- provenance chips missing required references (IDs/hashes/links)
- restricted UI states incorrectly exposed

### Fixture ethics rule
Fixtures MUST remain:
- synthetic
- non-identifying
- non-harmful
- free of colonial framing or culturally harmful test text

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial `fm_synth_002` expected UI scenario guide (Focus Mode v3 regression baselines; governance-first). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

