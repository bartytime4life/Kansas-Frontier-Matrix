---
title: "🧭 KFM E2E Scenario — Focus Mode v3 Expected UI Baseline (fm_synth_001) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Scenario"
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

semantic_document_id: "kfm-tests-e2e-focus-mode-scenario-fm-synth-001-readme"
doc_uuid: "urn:kfm:tests:e2e:focus-mode:scenario:fm_synth_001:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Focus Mode v3 Expected UI Scenario — fm_synth_001 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/README.md`

**Purpose**  
Define the **scenario-scoped expected UI baseline** for Focus Mode v3 regression testing.  
`fm_synth_001` is a **synthetic, sovereignty-safe** scenario used to verify:
**(1) three-panel rendering**, **(2) governance surfaces**, **(3) provenance surfaces**, and **(4) no precision leakage**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Regression-informational" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__001-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Scenarios Index](../README.md) · [🧾 API Mocks](../../../api_mocks/README.md) · [📐 Focus Mode Specs](../../../../specs/README.md) · [🧭 Focus Mode Regression](../../../../README.md)

</div>

---

## 📘 Overview

### What `fm_synth_001` is
`fm_synth_001` is the **baseline governed scenario** for Focus Mode v3 regression.

It is designed to be:
- **Deterministic** (stable IDs, stable strings, stable panel structure)
- **Synthetic** (no real persons, no real sensitive locations, no restricted datasets)
- **Governance-forward** (masking + CARE tiers validated before content assertions)

### Primary claim (one-sentence)
When Focus Mode loads a synthetic entity, the UI renders **Context / Timeline / Map** consistently, displays the expected **CARE + sovereignty state**, and never exposes **raw precision** anywhere in the surface.

### What this scenario MUST catch
This scenario is intended to fail loudly on:
- missing governance overlays (CARE tier not visible, sovereignty state not visible)
- raw coordinate leakage (tooltips, debug panes, downloads, JSON viewers)
- missing provenance/evidence references when policy requires them
- broken panel structure (missing one of the three panels, wrong headings/landmarks)
- WCAG-critical regressions (keyboard traps, missing roles, heading structure collapse)

---

## 🗂️ Directory Layout

~~~text
📁 fm_synth_001/
├── 📄 README.md                      — This scenario guide (what/why/how)
├── 🧾 expected_panels.json            — Stable subset assertions for Context/Timeline/Map
├── 🧾 expected_governance.json        — CARE + sovereignty + masking expectations (policy invariants)
├── 🧾 expected_provenance.json        — Evidence chip + ref-prefix expectations
├── 🧾 expected_a11y.json              — WCAG-critical expectations for this scenario
├── 🧾 scenario_meta.json              — Optional: tags, viewport/theme matrix, runner options
└── 📁 snapshots/                      — Optional: visual baselines (last resort)
    ├── 🖼️ chromium_1280x720.png
    └── 🖼️ chromium_1280x720.dark.png
~~~

Directory policy:
- JSON baselines are the **source of truth** for assertions.
- `snapshots/` is optional and SHOULD NOT be used unless semantic assertions are insufficient.

---

## 🧭 Context

### Scenario inputs (high level)
This scenario expects that:
- API mocks for `scenario_id = "fm_synth_001"` are loaded by the runner.
- A deterministic “test mode” stack is used (fixed time and seeded IDs where applicable).
- The UI is run without requiring external networks.

### UI invariants targeted
`fm_synth_001` is written to validate:
- correct panel headings: **Context**, **Timeline**, **Map**
- governance display: CARE tier and sovereignty/masking state is visible
- provenance display: at least one evidence/provenance element appears
- coordinate safety: raw precision never appears in UI, tooltips, or downloads
- accessibility: landmarks and headings exist; primary controls are reachable by keyboard

### Non-goals (what this scenario intentionally does not test)
- performance benchmarking (handled elsewhere)
- deep map rendering correctness for complex layers (covered by additional scenarios)
- long-form narrative audits (covered by governance-focused narrative scenarios)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Runner loads API mocks for fm_synth_001"] --> B["Open Focus Mode entry route"]
  B --> C["Render panels: Context / Timeline / Map"]
  C --> D["Assert governance invariants (CARE + masking)"]
  D --> E["Assert provenance invariants (evidence refs)"]
  E --> F["Assert UI content subset + a11y invariants"]
~~~

Interpretation:
- This scenario is governance-first: policy invariants are asserted before content diffs.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 expectations
This scenario SHOULD validate:
- **Context panel**
  - required headings/labels exist
  - prohibited strings are absent (e.g., raw `Lat:` / `Lon:` patterns)
- **Timeline panel**
  - stable ordering of synthetic events (only assert stable labels, not volatile timestamps)
- **Map panel**
  - masking banner appears when expected
  - no raw coordinate display in tooltips, debug overlays, or exports

### Story Node touchpoints (optional)
If the scenario navigates through Story Node UI:
- the Story Node content must remain synthetic
- any geometry must be masked/generalized where required
- the test must assert that “evidence/provenance chips” remain visible and non-empty

---

## 🧪 Validation & CI/CD

### Recommended tags
`fm_synth_001` is typically run with:
- `@regression`
- `@governance`

It MAY be promoted to `@smoke` only if:
- runtime is consistently low
- flake rate is effectively zero
- assertions remain stable across runner environments

### What changes require reruns
Changes to any of the following MUST trigger this scenario:
- Focus Mode UI layout
- governance overlays (CARE/sovereignty UI components)
- provenance chip logic or formatting
- tooltip/download rendering logic
- masking/generalization logic or display rules

### Flake policy
- No “sleep-and-hope” waits are allowed.
- Use event/state-driven waits only (selector visible, response complete, panel ready).

---

## 📦 Data & Metadata

### Baseline files (required)
These files MUST exist and be kept in sync:
- `expected_panels.json`
- `expected_governance.json`
- `expected_provenance.json`
- `expected_a11y.json`

### Editing rules (to keep baselines stable)
When updating expected JSON:
- prefer `must_include` and `must_exclude` lists over full-text snapshots
- never assert run-variant timestamps unless time is fully injected and fixed
- normalize known volatile tokens in the runner, not in the baseline
- keep governance assertions explicit (do not “normalize away” policy signals)

### Safety rules (non-negotiable)
Baselines MUST NOT include:
- raw coordinates (even synthetic ones that look plausible)
- text implying sacred-site inference, genealogy, or culturally harmful framing
- secrets, tokens, or internal URLs

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O guidance (conceptual)
- The scenario baseline files are `prov:Entity` (kfm:TestFixture).
- The regression execution is `prov:Activity` (kfm:TestRun).
- CI runner and maintainers are `prov:Agent`.

Example (simplified; illustrative only):
~~~json
{
  "prov:entity": {
    "fm_synth_001_expected_panels": {
      "prov:label": "fm_synth_001 expected_panels.json",
      "prov:type": "kfm:TestFixture"
    }
  },
  "prov:activity": {
    "fm_synth_001_run": {
      "prov:label": "Focus Mode E2E scenario run fm_synth_001",
      "prov:type": "kfm:TestRun"
    }
  }
}
~~~

---

## 🧱 Architecture

### Runner contract (recommended)
A typical runner should:
- locate scenario folder by `scenario_id`
- load API mocks for the same `scenario_id`
- execute governance-first assertions:
  1) masking / restricted state
  2) CARE tier
  3) provenance visibility
  4) panel subset assertions
  5) a11y invariants
- write artifacts under `reports/e2e/` (report + trace + screenshots on failure)

---

## ⚖ FAIR+CARE & Governance

### Governance invariants this scenario must enforce
- Masking/generalization is visible and consistent with policy.
- No sensitive precision can be surfaced anywhere in the UI.
- CARE tier display and routing behaviors must match expectations.
- Provenance references must not be empty when required.

### Fixture ethics rules
This scenario must remain:
- **synthetic**
- **non-identifying**
- **non-harmful in phrasing**
- **safe to publish in a public repo**

If governance assertions fail:
- treat as merge-blocking for any PR affecting governed outputs

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial scenario README for `fm_synth_001` (Focus Mode v3 baseline regression; governance-first; sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

