---
title: "🧪 KFM E2E — Focus Mode Regression Scenario: fm_synth_002 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_002/README.md"

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
intent: "tests-e2e-focus-mode-regression-scenario-fm-synth-002"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-focus-mode-regression-scenario-fm-synth-002"
doc_uuid: "urn:kfm:tests:e2e:web-app:focus-mode:scenario:fm_synth_002:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_002/README.md"
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

signature_ref: "../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 Focus Mode regression scenario update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_002/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Focus Mode Regression Scenario — fm_synth_002 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_002/README.md`

**Purpose**  
Define the **governance-visible synthetic regression scenario** for Focus Mode v3 E2E testing.  
`fm_synth_002` verifies that CARE labels, governance overlays, and safe UI fallbacks render correctly under controlled “policy-present” conditions.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__002-blueviolet" />
<img src="https://img.shields.io/badge/Governance-Overlay%20Coverage-orange" />
<img src="https://img.shields.io/badge/Fixtures-Synthetic%20Only-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Scenarios Index](../README.md) ·
[🧩 API Mocks](../../api_mocks/README.md) ·
[🧾 Expected UI](../../expected_ui/README.md) ·
[🧬 Provenance](../../provenance/README.md) ·
[🧪 Specs](../../../specs/README.md)

</div>

---

## 📘 Overview

### What this scenario is for
`fm_synth_002` is a regression scenario that emphasizes **governance surfaces** and **policy-driven UI behavior** while remaining fully synthetic.

It exists to catch regressions in:
- CARE tier rendering and routing
- Governance overlay UI (badges, banners, chips)
- Provenance visibility under “governance-on” mode
- Safe fallbacks when a panel has restricted/withheld content (without any real sensitive data)

### What this scenario MUST validate
This scenario is expected to validate:

- **Governance overlay appears** and is stable (no missing badges/labels).
- **CARE tier label(s)** render with consistent formatting.
- **Restricted-state UI fallback** renders safely (redacted/withheld messaging) *when invoked by synthetic flags*.
- **No leakage**: no raw precision, no identifying text, no policy bypass.

### What this scenario MUST NOT do
- Include real restricted datasets or real-world sensitive geometry.
- Assert exact sensitive coordinates (ever).
- Depend on external networks or live services.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 fixtures/
                    └── 📁 scenarios/
                        └── 📁 fm_synth_002/
                            ├── 📄 README.md              — This document (scenario contract + governance invariants)
                            ├── 🧾 scenario.json           — Scenario manifest (governance-on flags + expected behaviors)
                            └── 🧾 bindings.json           — Fixture bindings (api_mocks / expected_ui / provenance refs)
~~~

---

## 🧭 Context

### Determinism contract
To keep `fm_synth_002` stable:
- policy state is simulated via fixture flags (not by contacting governance services),
- time is fixed (or injected) so ordering is deterministic,
- assertions target visible UI state, not transient animation timing.

### Governance posture
This scenario simulates a “policy-present” environment:
- governance overlays are **expected**,
- redaction/withhold UI **may** be exercised via synthetic configuration,
- any “restricted” state must be represented as **synthetic** (not derived from real content).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario.json (governance-on)"] --> B["Install API mocks + provenance fixtures"]
  B --> C["Navigate to Focus Mode route"]
  C --> D["Render panels + overlays"]
  D --> E["Assert CARE tier + governance UI"]
  E --> F["Assert safe fallback when restricted flag is set"]
  F --> G["Capture artifacts + emit telemetry"]
~~~

**Interpretation**  
This scenario checks that governed UI elements render reliably and that restricted-mode responses are safe and consistent.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode expectations (governance-visible)
When routed with this scenario:
- Context/Timeline/Map panels should render as usual unless a synthetic restriction flag is enabled.
- Governance overlays should render without layout shift regressions.
- Provenance references should remain present (even if content is withheld).

### Minimum narrative safety expectation
If synthetic “withheld” content is displayed:
- the UI must not reveal hidden content in tooltips, JSON views, or download links,
- text must remain neutral and non-identifying.

---

## 🧪 Validation & CI/CD

### Recommended tags
This scenario is typically appropriate for:
- `@regression`
- `@governance`

It can be promoted to `@smoke` only if it remains fast and stable.

### Required assertions (minimum)
Specs selecting `fm_synth_002` SHOULD assert:

- governance overlay is visible,
- CARE tier label(s) are visible and match expected tier values from fixtures,
- provenance chip(s) render and are non-empty,
- restricted/withheld UI state (if activated) shows a safe message and blocks access to raw data,
- no console errors.

### Flake policy
- Governance regressions are **not retryable by default**.
- Any intermittent failures must be fixed by improving determinism (selectors, fixtures, waits).

---

## 📦 Data & Metadata

### scenario.json (required)
Expected to define:
- `scenario_id`: `fm_synth_002`
- `route`: Focus Mode route under test
- governance flags that trigger overlay rendering
- optional “restricted simulation” mode

Example shape:

~~~json
{
  "scenario_id": "fm_synth_002",
  "route": "/focus-mode?entity=kfm:entity:synth:event:002",
  "mode": {
    "deterministic_time": "2025-01-01T00:00:00Z",
    "governance_enforced": true,
    "governance_overlay": "on",
    "simulate_withheld_panel": true,
    "network_blocked": true
  },
  "seed": 223344,
  "expectations": {
    "panels": ["context", "timeline", "map"],
    "care_tier_visible": true,
    "sovereignty_redaction_expected": false,
    "restricted_ui_fallback_expected": true,
    "provenance_chips_expected": true
  }
}
~~~

### bindings.json (required)
Binds this scenario to synthetic fixtures:

~~~json
{
  "api_mocks_ref": "../../api_mocks/fm_synth_002/",
  "expected_ui_ref": "../../expected_ui/scenarios/fm_synth_002/",
  "provenance_ref": "../../provenance/",
  "notes": "Governance-visible regression scenario. Synthetic. Uses withheld-panel simulation flags."
}
~~~

### Artifact expectations
Runs using this scenario SHOULD produce:
- report + junit (where configured)
- traces/screenshots on failure
- run manifest capturing `scenario_id`, suite tags, and governance flags

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O expectations (test-level)
- `prov:Activity`: this scenario’s E2E run
- `prov:Entity`: scenario manifest, bindings, mocks, reports
- `prov:Agent`: CI runner / test harness

### OpenLineage expectations (optional)
If emitted:
- include fixture refs as “inputs”
- include reports/traces as “outputs”
- include governance flag facets as “run facets” (synthetic)

---

## ⚖ FAIR+CARE & Governance

### Ethical fixture rules
Fixtures MUST:
- remain synthetic and non-identifying,
- avoid plausible reproduction of restricted knowledge,
- simulate governance states via flags, not real content.

### Sovereignty rule
This scenario does not require sovereignty masking content, but it MUST still ensure:
- no UI path exposes raw precision fields,
- “restricted” behaviors remain safe and non-bypassable.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Added `fm_synth_002` governance-visible Focus Mode regression scenario documentation aligned to KFM‑MDP v11.2.6. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

