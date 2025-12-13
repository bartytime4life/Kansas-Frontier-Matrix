---
title: "🖼️ KFM E2E Artifacts — Visual Snapshots (fm_synth_001) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/snapshots/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Artifacts Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-snapshots-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-focus-mode-fm-synth-001-snapshots-readme"
doc_uuid: "urn:kfm:tests:e2e:focus-mode:scenario:fm_synth_001:snapshots:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/snapshots/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/snapshots/README.md@v11.2.6"
---

<div align="center">

# 🖼️ **Visual Snapshots — fm_synth_001 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/fm_synth_001/snapshots/README.md`

**Purpose**  
Define how **visual snapshot baselines** are stored and governed for the `fm_synth_001` Focus Mode v3 E2E regression scenario.  
Snapshots are **optional, last‑resort artifacts** used only when semantic expectations (JSON baselines) cannot catch a regression.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Visual%20Baselines-informational" />
<img src="https://img.shields.io/badge/Scenario-fm__synth__001-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Scenario README](../README.md) · [📚 Scenarios Index](../../README.md) · [🧾 Expected UI Root](../..//README.md)

</div>

---

## 📘 Overview

### What snapshots are
Snapshots are **static images** captured from deterministic E2E runs that represent an **approved UI baseline** for a specific:
- scenario (`fm_synth_001`)
- browser profile (e.g., `chromium`)
- viewport profile (e.g., `1280x720`)
- theme mode (e.g., `light` / `dark`)

Snapshots exist to detect **visual regressions** that might not be detectable via:
- panel text subsets
- DOM/ARIA semantic assertions
- governance overlay assertions

### What snapshots are not
Snapshots MUST NOT be treated as the source of truth for governance.
Governance assertions MUST remain **semantic and explicit** (see `expected_governance.json`) and must not depend on pixel-only checks.

### When snapshots are allowed
Snapshots are allowed only when at least one of these is true:
- The regression is purely visual (spacing/layout/alignment) but semantically stable.
- A map or timeline rendering change cannot be validated reliably with selectors alone.
- A high-value UI surface (e.g., panel framing) needs a last-resort “screen truth” check.

---

## 🗂️ Directory Layout

~~~text
📁 snapshots/
├── 📄 README.md                       — This guide
├── 🖼️ chromium_1280x720.png            — Light-mode baseline (preferred default)
└── 🖼️ chromium_1280x720.dark.png       — Dark-mode baseline (only if supported by runner)
~~~

Naming rules (required):
- `<browser>_<width>x<height>.png`
- `<browser>_<width>x<height>.dark.png` (theme-qualified)
- Use lowercase, underscores, and ASCII only in filenames.

---

## 🧭 Context

### Determinism requirements (non-negotiable)
Snapshot generation MUST:
- run in deterministic “test mode”
- use synthetic, non-identifying fixtures only
- use fixed viewport sizes (no “maximize window” baselines)
- avoid time-dependent UI (inject a fixed clock where applicable)
- disable animations where possible (or enforce reduced-motion)

### Sovereignty & safety requirements (non-negotiable)
Snapshots MUST NOT contain:
- raw coordinate displays (tooltips, debug panes, JSON viewers)
- any plausible sensitive site geometry or precision
- real people or identifying text
- restricted material (Tier A) content

If a snapshot capture reveals unsafe precision or restricted text:
- delete the artifact
- fix the underlying UI behavior
- re-run the scenario with governance assertions enabled

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Run fm_synth_001 with synthetic fixtures"] --> B["Assert governance and provenance (semantic)"]
  B --> C["Assert panel expectations (JSON)"]
  C --> D["If needed, capture snapshot image"]
  D --> E["Compare to baseline and report diffs"]
~~~

Interpretation:
- Snapshot comparisons occur only after semantic safety gates pass.
- Snapshot diffs are used to confirm visual stability, not policy correctness.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 surfaces that may justify snapshots
Snapshots are most useful when validating:
- three-panel layout integrity (Context / Timeline / Map)
- map canvas presence (not blank)
- overlay layout (CARE tier label placement, sovereignty banner presence)
- critical UI framing (headers, tabs, toolbars)

### Governance-first rule
Even when snapshots exist, tests MUST still assert:
- CARE tier visibility (semantic)
- sovereignty/masking state visibility (semantic)
- absence of raw precision (semantic; string/regex/DOM-based)

---

## 🧪 Validation & CI/CD

### CI usage policy
- Snapshot tests SHOULD run under `@regression`.
- Snapshot tests MUST NOT be `@smoke` unless the flake rate is effectively zero.

### Flake policy (strict)
Snapshot comparisons can become flaky due to rendering variance.
To prevent that:
- prefer semantic assertions first
- keep the snapshot area minimal (capture only the relevant region if supported)
- standardize fonts, DPR, and GPU settings in CI runners where possible
- quarantine unstable snapshots behind `@nightly` until stabilized

### Failure behavior
When a snapshot diff is detected:
- CI MUST attach a diff artifact (expected vs actual vs diff)
- the PR must explicitly justify baseline updates

---

## 📦 Data & Metadata

### What to commit
Commit only:
- baseline images that are stable across CI
- the smallest set of baselines needed (avoid explosion of browser matrices)

Recommended minimal baseline set for `fm_synth_001`:
- `chromium_1280x720.png`
- optional: `chromium_1280x720.dark.png`

### What not to commit
Do not commit:
- videos unless policy explicitly requires them
- raw traces that might contain URLs/tokens (sanitize first)
- images containing debug-only panels that expose internal state not intended for public docs

### Baseline update procedure (recommended)
When intentionally updating UI:
1. Update semantic expectations first (`expected_*.json`).
2. Run the scenario locally in deterministic mode.
3. Generate new snapshots.
4. Review for safety (no precision leakage, no sensitive content).
5. Replace baselines and document “why” in the PR.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O mapping (conceptual)
- Snapshot image files are `prov:Entity` (kfm:TestArtifact).
- The E2E run is `prov:Activity` (kfm:TestRun).
- The runner and maintainers are `prov:Agent`.

Snapshots SHOULD be referenced by:
- run manifest (`reports/e2e/run-manifest.json`)
- test reports (JSON/JUnit)
- E2E telemetry aggregation (`tests-e2e-telemetry.json`)

---

## 🧱 Architecture

### Recommended snapshot comparator behavior
Recommended (not normative):
- capture deterministic screenshots at stable checkpoints
- compare with a pixel-diff tool using a conservative threshold
- emit:
  - `expected.png`
  - `actual.png`
  - `diff.png`
  - a JSON summary (percent difference, bounding boxes)

Keep the comparator outputs as **CI artifacts**, not committed baselines.

---

## ⚖ FAIR+CARE & Governance

### Governance invariants for snapshot baselines
Before committing or updating snapshots, reviewers MUST confirm:
- No raw coordinates or precision surfaces are visible
- CARE and sovereignty UI is present only as allowed by policy
- The fixture content remains synthetic and non-identifying

If there is any uncertainty:
- treat as a governance escalation and route through the FAIR+CARE process

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial snapshot governance + naming guide for `fm_synth_001` Focus Mode v3 E2E regression scenario. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

