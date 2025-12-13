---
title: "🖼️ KFM E2E — Snapshot Baselines (fm_synth_003) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/snapshots/README.md"

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
intent: "tests-e2e-snapshot-baselines"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-snapshots-fm-synth-003"
doc_uuid: "urn:kfm:tests:e2e:snapshots:focus-mode:fm_synth_003:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/snapshots/README.md"
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

signature_ref: "../../../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E snapshot framework update"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/snapshots/README.md@v11.2.6"
---

<div align="center">

# 🖼️ **Snapshot Baselines — fm_synth_003 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_003/snapshots/README.md`

**Purpose**  
Define the **snapshot policy** and **baseline storage rules** for `fm_synth_003`.  
Snapshots are **optional secondary evidence** used to detect UI regressions that are hard to express semantically, while remaining **deterministic**, **synthetic**, and **sovereignty-safe**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Snapshots-blueviolet" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__003-informational" />
<img src="https://img.shields.io/badge/Sovereignty-Safe-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Scenario README](../README.md) ·
[🧾 Scenarios Index](../../README.md) ·
[🧪 Focus Mode Specs](../../../../../specs/README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

### What snapshots are (KFM definition)
A **snapshot** is a deterministic, non-sensitive baseline artifact intended to help catch regressions in:
- layout or panel composition,
- presence/visibility of governance UI elements (badges, chips, overlays),
- stable map/timeline rendering states (in masked/generalized mode),
- accessibility-critical UI affordances that are visually inspectable.

Snapshots are **not the source of truth**.

**Source of truth order**
1. ✅ `expected_*.json` semantic baselines (required)
2. ✅ explicit assertion logic (required)
3. 🖼️ snapshots (optional, secondary)

### What snapshots must never contain
Snapshots MUST NOT include:
- raw coordinates or precise geometry readouts (tooltips, debug panels, downloads)
- any real or plausible sensitive-site depiction
- real persons, identifying text, or PII
- secrets (tokens, keys, internal URLs that embed credentials)

### When snapshots are allowed
Snapshots are allowed when they add signal beyond semantic assertions, for example:
- verifying that a CARE badge is visible in the correct region of the UI,
- ensuring map panel chrome renders and does not “collapse” under CSS changes,
- confirming a masked/generalized state is clearly indicated in the map UI,
- capturing deterministic empty/error states for restricted outputs.

---

## 🗂️ Directory Layout

~~~text
📁 snapshots/
├── 📄 README.md                         — Snapshot policy and update rules (this file)
│
├── 🧾 snapshot_manifest.json            — Required if snapshots exist (names, hashes, intent)
├── 🧾 snapshot_allowlist.json           — Optional: file patterns allowed in this folder
│
├── 🖼️ fm_synth_003__context__base.png   — Optional: Context panel snapshot (synthetic)
├── 🖼️ fm_synth_003__timeline__base.png  — Optional: Timeline panel snapshot (synthetic)
├── 🖼️ fm_synth_003__map__masked.png     — Optional: Map panel snapshot (masked/generalized)
│
└── 🧾 checksums.sha256                  — Optional: detached checksums for offline verification
~~~

Policy:
- If any `*.png` (or other snapshot files) exist, `snapshot_manifest.json` MUST exist.
- Keep snapshot counts small. Prefer “high-signal” snapshots only.

---

## 🧭 Context

### Determinism guardrails (required)
Snapshots MUST be produced under a deterministic configuration:
- animations disabled (UI and map)
- stable viewport and device profile
- fixed scenario seed (declared in `scenario_manifest.json`)
- stable theme selection (if theme affects pixel output)
- stable font loading strategy (avoid late-loading layout shifts)

### Map-specific guardrails (required)
When capturing Map panel snapshots:
- ensure the map is in a **masked/generalized** state when the scenario expects masking
- disable coordinate readouts and dev overlays
- avoid capturing hover tooltips
- avoid capturing downloadable JSON panels that could include geometry

### Accessibility note
Snapshots are not a substitute for A11y checks.
If snapshots are ever embedded into docs (rare), they MUST include:
- meaningful alt text
- a short caption describing what the snapshot verifies

---

## 🧪 Validation & CI/CD

### Snapshot comparison policy (strict)
- Snapshots are compared only when:
  - the suite tag includes `@regression` or `@nightly`, and
  - a scenario explicitly opts into snapshot checking.
- Governance-related regressions are **not** “diff-accepted” by default.
- Any snapshot update requires semantic baseline review first.

### Flake policy (snapshot-specific)
Snapshots are sensitive to flake. If flake is detected:
- move the snapshot check behind `@nightly`, or
- replace with semantic assertions, or
- stabilize the render (fonts/animations/map timing), then re-enable.

### Quarantine rule
A flaky snapshot MUST NOT be run in `@smoke` gating.

---

## 📦 Data & Metadata

### snapshot_manifest.json (required when snapshots exist)
The manifest binds every snapshot to:
- a purpose,
- a deterministic capture configuration,
- a checksum,
- and the expected governance safety constraints.

Example (shape only):
~~~json
{
  "scenario_id": "fm_synth_003",
  "snapshot_version": "v11.2.6",
  "capture_profile": {
    "viewport": { "width": 1280, "height": 720 },
    "theme": "default",
    "animations_disabled": true
  },
  "safety_constraints": {
    "synthetic_only": true,
    "no_raw_coordinates": true,
    "masked_map_required": true
  },
  "snapshots": [
    {
      "file": "fm_synth_003__context__base.png",
      "intent": "Verify Context panel chrome + governance badge visibility",
      "sha256": "<sha256>"
    },
    {
      "file": "fm_synth_003__map__masked.png",
      "intent": "Verify Map panel renders masked/generalized state with indicator visible",
      "sha256": "<sha256>"
    }
  ]
}
~~~

### Naming convention (recommended)
Use stable, grep-friendly names:

- `fm_synth_003__<panel>__<state>__<viewport>.png`

Where:
- `<panel>`: `context` | `timeline` | `map`
- `<state>`: `base` | `masked` | `restricted` | `empty` (keep vocabulary small)
- `<viewport>`: `1280x720` (optional if already fixed in manifest)

---

## ⚖ FAIR+CARE & Governance

### Sovereignty-safe snapshot requirements (non-negotiable)
Any snapshot workflow MUST guarantee:
- no sensitive coordinate precision is visible anywhere in the captured UI
- masked/generalized state is used when required
- the scenario remains synthetic and non-identifying

### Governance escalation
If a snapshot reveals a potential policy failure (even synthetic):
- treat as a **stop-ship** for governed UI merges
- route to FAIR+CARE Council + the responsible working group
- record the failure according to the project audit policy

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial snapshot policy for `fm_synth_003` (secondary validation; deterministic; sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

