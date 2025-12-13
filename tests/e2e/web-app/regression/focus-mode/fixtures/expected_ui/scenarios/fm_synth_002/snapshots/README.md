---
title: "🖼️ KFM E2E — Snapshot Baselines (fm_synth_002) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/snapshots/README.md"

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
intent: "tests-e2e-snapshot-baselines-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-snapshots-fm-synth-002"
doc_uuid: "urn:kfm:tests:e2e:snapshots:focus-mode:fm_synth_002:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/snapshots/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/snapshots/README.md@v11.2.6"
---

<div align="center">

# 🖼️ **E2E Snapshot Baselines — fm_synth_002 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_002/snapshots/README.md`

**Purpose**  
Define **snapshot governance rules** for the `fm_synth_002` Focus Mode v3 regression scenario.  
Snapshots are **optional**, **subordinate to semantic baselines**, and MUST remain **sovereignty-safe**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Snapshots-informational" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__002-blueviolet" />
<img src="https://img.shields.io/badge/Governance-Strict-orange" />

[⬅️ Scenario Guide](../README.md) ·
[🧾 Expected UI Root](../../README.md) ·
[🧪 Focus Mode Regression](../../../../README.md)

</div>

---

## 📘 Overview

### Snapshot role (strictly secondary)
Snapshots exist only to detect regressions that are difficult to capture with purely semantic assertions, such as:
- layout breakage that still passes text-based checks
- visual rendering failures (blank map canvas, missing panel chrome)
- catastrophic CSS regressions (panels overlap, controls off-screen)
- iconography regressions that are policy-significant (masking badge disappears)

Snapshots MUST NOT be used as the primary source of truth for:
- governance enforcement
- provenance correctness
- masking/precision logic
- accessibility correctness

Those are enforced via the semantic baselines:
- `expected_governance.json`
- `expected_provenance.json`
- `expected_a11y.json`
- `expected_*_panel.json`

### When to add a snapshot
Add a snapshot only when ALL are true:
- the regression is user-visible and meaningful
- the regression is not reliably detectable via semantic checks
- the snapshot can be made stable (viewport, fonts, animations, time)

### When to remove a snapshot
Remove snapshots when:
- a semantic assertion becomes sufficient (preferred)
- the snapshot becomes flaky due to expected UI variability
- the UI changes frequently and the snapshot creates noise

---

## 🗂️ Directory Layout

~~~text
📁 snapshots/
├── 📄 README.md                           — This policy + runbook
│
├── 🖼️ fm_synth_002_context_panel.png       — Optional: Context panel baseline
├── 🖼️ fm_synth_002_timeline_panel.png      — Optional: Timeline panel baseline
├── 🖼️ fm_synth_002_map_panel.png           — Optional: Map panel baseline
│
└── 🖼️ fm_synth_002_full_view.png           — Optional: 3-panel full layout baseline
~~~

Notes:
- Keep the snapshot set minimal.
- Prefer panel-level captures over full-page captures unless the regression is layout-wide.

---

## 🧭 Context

### Determinism requirements (non-negotiable)
All snapshots MUST be captured with:
- a fixed viewport (declare it in scenario manifest)
- a fixed clock (or time-free UI)
- reduced motion enabled (or animations disabled)
- stable fonts and rendering settings (CI standard)
- stable map state (camera fixed; no inertial movement)

### Sovereignty + masking requirements (non-negotiable)
Snapshots MUST:
- contain only synthetic, non-sensitive content
- never show raw coordinates, raw geometry dumps, or “debug” JSON surfaces
- never include plausible real-world site locations or identifying text
- avoid capturing tooltips/popovers that could expose precision or internal data

If a snapshot would capture a precision-bearing tooltip or coordinate readout:
- do not take that snapshot
- replace with semantic assertions that validate the tooltip is not shown

### Accessibility requirements
Snapshots MUST NOT replace accessibility testing.
If a visual regression impacts accessibility:
- create or update `expected_a11y.json` assertions
- add an `@a11y` scenario check in specs

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Run scenario (deterministic)"] --> B["Assert governance + provenance (semantic)"]
  B --> C["Capture snapshots (optional)"]
  C --> D["Compare against baselines"]
  D -->|match| E["Pass"]
  D -->|diff| F["Review diff + confirm policy safe"]
~~~

Interpretation:
- semantic checks run before any snapshot capture/comparison.
- diffs require review; governance failures are not “snapshot-reviewable”.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode snapshot boundaries
Allowed snapshot surfaces:
- panel chrome (headers, tabs, layout)
- masked indicator badges (if any)
- high-level map rendering state (no raw precision readouts)

Disallowed snapshot surfaces:
- debug JSON viewers
- download dialogs that expose raw geometry
- coordinate inspector overlays
- provenance internals beyond stable UI chips

---

## 🧪 Validation & CI/CD

### Snapshot execution policy
- Snapshots SHOULD run under `@nightly` if they are sensitive to rendering differences.
- Snapshots MAY run under `@regression` only when stability is proven.
- Snapshots MUST NOT be merge-blocking unless flake rate is near zero.

### Snapshot update process (strict)
A snapshot baseline update requires:
- an intentional UI change explanation
- confirmation that governance and masking remain compliant
- confirmation that semantic baselines still pass (or were updated correctly)

Update order:
1. semantic baselines (`expected_*.json`)
2. assertions/specs
3. snapshots (last)

---

## 📦 Data & Metadata

### Naming convention
Snapshot filenames MUST:
- include the scenario id (`fm_synth_002`)
- include the surface name (`context_panel`, `map_panel`, `full_view`)
- use lowercase with underscores
- avoid timestamps in filenames

Examples:
- `fm_synth_002_context_panel.png`
- `fm_synth_002_full_view.png`

### Storage and artifacts
During CI runs, store comparison outputs under:
~~~text
reports/
└── e2e/
    ├── snapshots/
    │   ├── fm_synth_002/
    │   │   ├── expected/
    │   │   ├── actual/
    │   │   └── diff/
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O mapping (conceptual)
- baseline snapshots are `prov:Entity` (kfm:TestBaselineSnapshot)
- snapshot capture is a `prov:Activity` (kfm:TestArtifactCapture)
- CI runner is a `prov:Agent`

Snapshots MUST be treated as non-spatial test artifacts:
- no geometry export
- no coordinate assertions
- no real-world location semantics

---

## 🧱 Architecture

### Why snapshots are minimized
Snapshots are inherently sensitive to:
- browser rendering differences
- GPU differences in CI
- font and antialiasing changes
- map tile rasterization differences

Therefore:
- semantic baselines are the default
- snapshots are the last resort for high-value visual regressions

---

## ⚖ FAIR+CARE & Governance

### Snapshot governance gates
Snapshots MUST be rejected if they:
- reveal precision-bearing content
- include plausible sensitive locations
- capture restricted UI states improperly exposed
- include identifying text or quasi-identifiers

If a snapshot diff suggests a governance regression:
- treat as stop-ship
- investigate through semantic assertions and policy rules first

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial snapshot policy for `fm_synth_002` (snapshots are optional, secondary, and sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

