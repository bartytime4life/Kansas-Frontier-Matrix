---
title: "🧪 KFM E2E — Focus Mode Regression Scenario: fm_synth_003 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_003/README.md"

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
intent: "tests-e2e-focus-mode-regression-scenario-fm-synth-003"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-focus-mode-regression-scenario-fm-synth-003"
doc_uuid: "urn:kfm:tests:e2e:web-app:focus-mode:scenario:fm_synth_003:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_003/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_003/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Focus Mode Regression Scenario — fm_synth_003 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/fm_synth_003/README.md`

**Purpose**  
Define the **sovereignty-aware synthetic regression scenario** for Focus Mode v3 E2E testing.  
`fm_synth_003` validates that **masking/generalization UI invariants** hold across panels and that **no raw precision** leaks via tooltips, JSON views, or downloads when a synthetic “restricted geometry” state is enabled.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__003-blueviolet" />
<img src="https://img.shields.io/badge/Sovereignty-Masking%20Assertions-orange" />
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
`fm_synth_003` is a regression scenario designed to verify **sovereignty-safe rendering** under an explicitly simulated, synthetic “restricted geometry” context.

It exists to catch regressions where:
- the Map panel renders geometry at **higher-than-allowed precision**
- tooltips/popovers expose **raw coordinates** or precise bounding boxes
- “view JSON” / debug drawers expose forbidden geometry fields
- export/download actions provide unmasked geometry or identifiers
- governance overlays fail to communicate restricted state

### What this scenario MUST validate
This scenario is expected to validate:

- ✅ **Sovereignty flags** (or equivalent restriction indicators) render when enabled by fixtures.
- ✅ **Masked geometry** renders in the Map panel as generalized (e.g., H3-cell style or coarse polygon), never as raw precision.
- ✅ **No coordinate leakage** via:
  - map tooltips
  - details drawers
  - copied JSON
  - share links
  - downloads
- ✅ **Cross-panel consistency**:
  - Context/Timeline/Map remain consistent with the same entity selection
  - restricted state messaging is consistent across panels

### What this scenario MUST NOT do
- Include real-world restricted geometry, sacred sites, or plausible “real location” coordinates.
- Test by “hiding” precision only in the UI while leaving it accessible via debug/exports.
- Depend on external networks or live governance services.

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
                        └── 📁 fm_synth_003/
                            ├── 📄 README.md              — This document (sovereignty-safe scenario contract)
                            ├── 🧾 scenario.json           — Scenario manifest (masking flags + expected invariants)
                            └── 🧾 bindings.json           — Fixture bindings (api_mocks / expected_ui / provenance refs)
~~~

---

## 🧭 Context

### Determinism contract
To keep `fm_synth_003` stable:
- restricted/masked behavior is driven by **fixture flags**, not environment heuristics
- time is fixed (or injected) to avoid nondeterministic ordering in Timeline
- assertions prefer stable UI states (selectors + network-idle + deterministic mocks)

### Sovereignty-safe test posture
This scenario simulates restricted content without using restricted content:
- geometry is synthetic and intentionally non-identifying
- masking is treated as a **first-class UI invariant**, not a best-effort behavior
- the test must actively probe likely leakage vectors (tooltip, export, JSON view)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario.json (masking-on)"] --> B["Install API mocks + provenance fixtures"]
  B --> C["Navigate to Focus Mode route"]
  C --> D["Render panels + governance overlays"]
  D --> E["Assert masked geometry rendering"]
  E --> F["Probe leakage surfaces (tooltip/json/export)"]
  F --> G["Capture artifacts + emit telemetry"]
~~~

**Interpretation**  
This scenario forces a sovereignty-aware state and then verifies that every user-visible and semi-visible surface remains safe.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode expectations (masking-aware)
When routed with `fm_synth_003`:
- the Map panel must display only generalized geometry
- contextual summaries must avoid implying precision
- provenance and governance indicators must remain visible (even if details are withheld)

### Minimum narrative safety expectation
Even in synthetic scenarios:
- UI text must remain neutral and non-identifying
- no speculative phrasing implying real-world sensitive location inference
- restricted state is communicated clearly without revealing restricted details

---

## 🧪 Validation & CI/CD

### Recommended tags
This scenario is typically appropriate for:
- `@regression`
- `@governance`

It should remain deterministic and fast enough to run on CI schedules that include governance regression gates.

### Required assertions (minimum)
Specs selecting `fm_synth_003` SHOULD assert:

- governance overlay is visible when `governance_overlay: "on"`
- sovereignty/restriction indicator is visible when `simulate_restricted_geometry: true`
- map geometry is rendered as masked/generalized:
  - no raw coordinate strings
  - no high-precision bbox values
- tooltip and details drawer do not expose coordinates
- export/download surfaces are blocked or return masked payloads
- no console errors

### Flake policy
- Sovereignty regressions are **not retryable by default**.
- Any nondeterminism must be corrected by stabilizing fixtures, selectors, or waits (never by adding sleeps).

---

## 📦 Data & Metadata

### scenario.json (required)
Expected to define:
- `scenario_id`: `fm_synth_003`
- a Focus Mode route using a synthetic entity id
- explicit masking flags
- expectations around what must be withheld/masked

Example shape:

~~~json
{
  "scenario_id": "fm_synth_003",
  "route": "/focus-mode?entity=kfm:entity:synth:place:003",
  "mode": {
    "deterministic_time": "2025-01-01T00:00:00Z",
    "governance_enforced": true,
    "governance_overlay": "on",
    "simulate_restricted_geometry": true,
    "expected_masking_profile": "h3-generalized",
    "network_blocked": true
  },
  "seed": 334455,
  "expectations": {
    "panels": ["context", "timeline", "map"],
    "care_tier_visible": true,
    "sovereignty_indicator_visible": true,
    "masked_geometry_required": true,
    "raw_coordinates_forbidden": true,
    "export_blocked_or_masked": true,
    "provenance_chips_expected": true
  }
}
~~~

### bindings.json (required)
Binds this scenario to synthetic fixture roots:

~~~json
{
  "api_mocks_ref": "../../api_mocks/fm_synth_003/",
  "expected_ui_ref": "../../expected_ui/scenarios/fm_synth_003/",
  "provenance_ref": "../../provenance/",
  "notes": "Sovereignty masking regression scenario. Synthetic-only. Probes tooltip/JSON/export leakage vectors."
}
~~~

### Artifact expectations
Runs using this scenario SHOULD produce:
- report + junit (where configured)
- traces/screenshots on failure
- run manifest capturing `scenario_id`, suite tags, and masking flags

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O expectations (test-level)
- `prov:Activity`: this scenario’s E2E run
- `prov:Entity`: scenario.json, bindings.json, mock payloads, reports, traces
- `prov:Agent`: CI runner / test harness

### OpenLineage expectations (optional)
If emitted:
- include masking flags as run facets (synthetic)
- include fixture directories as inputs
- include reports/traces as outputs

---

## ⚖ FAIR+CARE & Governance

### Ethical fixture rules
Fixtures MUST:
- remain synthetic and non-identifying
- avoid plausible reproduction of restricted knowledge
- keep restricted behavior driven by explicit test flags

### Sovereignty rule
This scenario enforces a hard invariant:

- **No raw precision** may appear in any surfaced UI pathway when restricted geometry is enabled.

Failures should be treated as merge-blocking for governed outputs.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Added `fm_synth_003` sovereignty-safe Focus Mode regression scenario documentation aligned to KFM‑MDP v11.2.6. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

