---
title: "🧾 Kansas Frontier Matrix — Web App Regression E2E Specs (Focus Mode v3) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/specs/README.md"

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
intent: "tests-e2e-web-app-regression-focus-mode-specs"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-focus-mode-specs-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:specs:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/specs/README.md"
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

signature_ref: "../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/focus-mode/specs/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Web App Regression E2E Specs — Focus Mode v3 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/specs/README.md`

**Purpose**  
Define how **spec files** in this folder are structured, named, tagged, and governed for **Focus Mode v3 regression E2E** coverage.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Regression-informational" />
<img src="https://img.shields.io/badge/Surface-Focus%20Mode%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Focus Mode Regression](../README.md) · [🧱 Regression Fixtures](../../fixtures/README.md) · [🧭 E2E Guide](../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **regression-grade E2E spec files** for **Focus Mode v3** in the KFM Web App.

These specs exist to prevent regressions in:
- **3-panel behavior** (Context · Timeline · Map),
- **governance surfaces** (CARE tier, sovereignty flags, restricted-state handling),
- **provenance surfaces** (IDs/hashes/evidence links),
- **deterministic UX contracts** (map/timeline state changes, filtering, navigation),
- **accessibility-critical Focus Mode flows** (when covered by regression rather than the dedicated a11y suite).

### What belongs in `specs/`
Specs in this directory SHOULD:
- open Focus Mode for a known synthetic entity/scenario,
- exercise a small set of deterministic interactions,
- assert high-signal outcomes (governance + provenance + panel coherence),
- produce actionable diagnostics when they fail.

Specs in this directory SHOULD NOT:
- generate large datasets at runtime,
- depend on external networks as a required dependency,
- use “sleep-and-hope” timing as a synchronization strategy,
- assert on raw sensitive-like geometry (even if synthetic).

### Naming convention (canonical)
Use a stable, descriptive spec filename:
- `focus_mode_open.spec.<ext>`
- `focus_mode_map.spec.<ext>`
- `focus_mode_timeline.spec.<ext>`
- `focus_mode_governance.spec.<ext>`
- `focus_mode_provenance.spec.<ext>`

Where `<ext>` is defined by your runner (commonly `ts`/`js`).

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 specs/
                    ├── 📄 README.md                         — This document (spec rules + patterns)
                    │
                    ├── 📄 focus_mode_open.spec.ts            — Opens Focus Mode + baseline panel assertions
                    ├── 📄 focus_mode_map.spec.ts             — Map interactions (toggle, hover/select, masking)
                    ├── 📄 focus_mode_timeline.spec.ts        — Timeline interactions (range, ordering, filters)
                    ├── 📄 focus_mode_governance.spec.ts      — CARE + sovereignty flags + restricted state UX
                    └── 📄 focus_mode_provenance.spec.ts      — Evidence/provenance chips and reference integrity
~~~

Directory policy:
- Keep specs **small** and **high-signal**.
- One spec file should represent one primary axis of behavior (open/map/timeline/governance/provenance).
- Prefer adding a new spec file over making a single spec “do everything.”

---

## 🧭 Context

### Determinism requirements (hard rules)
Specs MUST:
- use deterministic fixture scenario IDs (no live random entity creation),
- use deterministic time (fixed clock / injectable time provider) where available,
- wait on **events/state** (selector visible, request resolved, panel ready) instead of arbitrary sleeps,
- avoid cross-test coupling (each spec can run in isolation and be re-run safely).

Recommended waiting strategies:
- “Panel ready” signals (explicit UI markers for Context/Timeline/Map readiness),
- network completion for known endpoints (request/response assertions if supported),
- stable state assertions (URL, active entity ID, rendered evidence count).

### Tagging strategy (controls CI)
Tags MUST be used to control CI scope and enforcement:
- `@regression` — default tag for this folder.
- `@governance` — required for tests asserting CARE/sovereignty behavior.
- `@a11y` — only if a regression spec is explicitly accessibility-focused.
- `@nightly` — only for slow or high-volume scenarios (avoid by default).

### Selector and UX stability
Specs SHOULD rely on:
- stable roles/landmarks (a11y-first),
- stable `data-testid` attributes when provided,
- page objects from `tests/e2e/utils/pages/`,
- shared assertions from `tests/e2e/utils/assertions/`.

Specs SHOULD avoid:
- deep DOM traversal selectors,
- fragile CSS selectors tied to layout,
- exact string matches on long narrative bodies (prefer IDs, chip counts, and presence assertions).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Start spec"] --> B["Boot deterministic test stack"]
  B --> C["Load synthetic fixtures"]
  C --> D["Open Focus Mode for scenario ID"]
  D --> E["Assert panels: Context, Timeline, Map"]
  E --> F["Exercise interactions: map and timeline"]
  F --> G["Assert governance and provenance surfaces"]
  G --> H["Write artifacts and telemetry"]
  H --> I["Exit spec"]
~~~

Interpretation:
- Each spec is a deterministic workflow: open → verify → interact → assert governance/provenance → capture artifacts.

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode regression specs SHOULD validate cross-surface integrity when applicable:
- entering Focus Mode from a Story Node route preserves the entity context,
- evidence/provenance surfaces remain consistent across navigation,
- timeline/map interactions do not desynchronize from Context facts.

Minimum integration assertions (recommended):
- entity identity remains stable across panel interactions,
- provenance/evidence chips never become empty for governed entities,
- restricted/masked states remain safe across route transitions.

---

## 🧪 Validation & CI/CD

### CI placement
Typical CI ordering (conceptual):
1. unit
2. schema
3. integration
4. **e2e regression**
5. accessibility (suite)
6. governance validation
7. telemetry validation

### Required artifacts for failures
Each failing spec MUST produce:
- screenshot(s),
- trace/video (if supported),
- machine-readable report entry (JUnit/JSON),
- run manifest fields (tags, seed, env hash).

Recommended report layout:
~~~text
📁 reports/
└── 📁 e2e/
    ├── 🧾 report.json
    ├── 🧾 junit.xml
    ├── 📁 screenshots/
    └── 📁 traces/
~~~

### Flake policy (strict)
- Flaky specs are quarantined to `@nightly` until fixed.
- Governance-related failures are not “retry-to-green” by default.

---

## 📦 Data & Metadata

### Fixture usage rules
Specs MUST source scenario state from synthetic fixtures:
- `tests/e2e/web-app/regression/fixtures/`
- `tests/fixtures/`

Specs MUST NOT:
- request production-only endpoints,
- embed sensitive-like geometry payloads,
- include identifying text in fixtures or assertions.

### Scenario IDs (recommended pattern)
Use stable, descriptive scenario IDs (examples):
- `focus_safe`
- `focus_masked`
- `focus_restricted`

Store scenario mappings in the regression fixtures registry (if used) rather than hardcoding complex payloads in specs.

### Run manifest (recommended fields)
Specs SHOULD contribute to a deterministic run manifest:
- `run_id`, `suite_tags`
- `scenario_ids_exercised`
- `browser_matrix`
- `seed`
- `env_hash`
- `artifact_paths`

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment
- A spec execution maps to a `prov:Activity`.
- Fixtures and built assets map to `prov:Entity`.
- CI runner and maintainers map to `prov:Agent`.

Governance rule:
- provenance references should be **IDs/hashes**, not full payload dumps.

### DCAT alignment (optional)
- E2E reports may be indexed as `dcat:Distribution` artifacts for auditability.
- This README may be indexed as documentation metadata if the repo catalogs docs.

---

## 🧱 Architecture

### Recommended spec structure (high-signal)
A canonical Focus Mode spec typically follows:
1. bootstrap stack (test mode)
2. load fixture scenario
3. open Focus Mode
4. assert panel readiness
5. perform 1–3 deterministic interactions
6. assert governance/provenance surfaces
7. capture artifacts on failure

### Reuse policy
Specs SHOULD:
- reuse page objects (`tests/e2e/utils/pages/`),
- reuse assertions (`tests/e2e/utils/assertions/`),
- reuse deterministic waits (`tests/e2e/utils/`).

Specs SHOULD NOT:
- re-implement low-level waiting logic in every file,
- introduce unique selector strategies per spec unless necessary.

---

## ⚖ FAIR+CARE & Governance

### Merge-blocking conditions
These specs MUST block merges if they detect:
- sensitive precision leakage (tooltips, JSON viewers, downloads),
- missing or incorrect CARE tier/sovereignty indicator behavior where required,
- restricted content shown instead of masked/redacted/blocked,
- provenance surfaces becoming empty or severed from required references.

### Escalation routing
If a governance-related spec fails:
- treat as a stop-ship for governed surfaces,
- route to the relevant working group and FAIR+CARE Council per governance policy.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial spec authoring guide for Focus Mode v3 regression E2E specs (deterministic, sovereignty-safe, governance-aware). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

