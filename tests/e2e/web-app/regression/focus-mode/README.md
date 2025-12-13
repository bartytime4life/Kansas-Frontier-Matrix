---
title: "🧠 Kansas Frontier Matrix — Web App Regression E2E (Focus Mode v3) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/README.md"

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
intent: "tests-e2e-web-app-regression-focus-mode"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-focus-mode-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/README.md"
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

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/focus-mode/README.md@v11.2.6"
---

<div align="center">

# 🧠 **Web App Regression E2E — Focus Mode v3 (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/README.md`

**Purpose**  
Define the canonical **regression E2E suite** for **Focus Mode v3** in the KFM Web App.  
These tests validate the **Context · Timeline · Map** panels end-to-end using **deterministic**, **sovereignty-safe**, **synthetic** fixtures and **merge-blocking** CI gates.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Regression-informational" />
<img src="https://img.shields.io/badge/Focus%20Mode-v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Regression Suite](../README.md) · [🧭 E2E Guide](../../../README.md) · [🧱 Regression Fixtures](../fixtures/README.md)

</div>

---

## 📘 Overview

Focus Mode v3 is a governed narrative surface. Regression E2E tests exist to ensure that:
- the **3-panel UX** stays coherent across releases,
- provenance and governance UI stays visible and correct,
- sovereignty masking and CARE routing cannot regress silently.

### What these tests cover
This suite SHOULD validate end-to-end behaviors such as:
- ✅ Focus Mode opens for a synthetic entity and renders all three panels.
- ✅ Panel-to-panel consistency (Context ↔ Timeline ↔ Map refer to the same grounded entity).
- ✅ Map interactions update deterministically (layer toggles, feature hover, selection state).
- ✅ Timeline interactions update deterministically (brushing, range filters, ordering).
- ✅ Governance overlays render correctly (CARE tier labels, sovereignty flags).
- ✅ Restricted scenarios are handled safely (redaction/masking, no raw precision leaks).
- ✅ Provenance UI surfaces are non-empty and stable (IDs/hashes/links present).

### What these tests must not do
This suite MUST NOT:
- rely on production credentials, production tokens, or restricted datasets,
- include real individuals, real sensitive locations, or plausible restricted geometries,
- use flaky timing patterns (arbitrary sleeps) as a primary synchronization mechanism.

### Boundary definition (E2E)
A Focus Mode regression E2E test is any test that crosses at least **two** boundaries in one run:
- Web UI ↔ API responses
- UI ↔ governed overlays (CARE/sovereignty/provenance)
- UI ↔ graph-backed entity resolution (via API)
- UI ↔ map/timeline state transitions

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                ├── 📄 README.md                           — This guide
                │
                ├── 📁 specs/                              — Focus Mode regression specs
                │   ├── 📄 focus_mode_open.spec.ts          — Open Focus Mode + baseline panel assertions
                │   ├── 📄 focus_mode_timeline.spec.ts      — Timeline interactions (deterministic)
                │   ├── 📄 focus_mode_map.spec.ts           — Map interactions (deterministic)
                │   ├── 📄 focus_mode_governance.spec.ts    — CARE + sovereignty overlays + restricted states
                │   └── 📄 focus_mode_provenance.spec.ts    — Provenance chips, IDs/hashes visible
                │
                ├── 📁 fixtures/                            — Focus Mode-specific fixture pointers (optional)
                │   └── 📄 fixtures.ref.json                — Maps scenario IDs → regression fixture bundle IDs
                │
                └── 📁 snapshots/                           — Optional stable snapshots (if used by runner)
                    └── 📄 README.md                        — Snapshot policy (if present)
~~~

Notes:
- Filenames are canonical examples; keep the intent stable even if the exact runner differs.
- All fixtures referenced here MUST be sourced from synthetic bundles under:
  - `tests/e2e/web-app/regression/fixtures/`
  - and/or `tests/fixtures/` (shared synthetic layer)

---

## 🧭 Context

### Determinism rules (non-negotiable)
These tests MUST:
- run on synthetic fixture IDs with stable timestamps,
- prefer event-based waits (state change, selector visible, network idle) over time-based sleeps,
- avoid cross-test coupling (each test is isolated and idempotent),
- use deterministic selectors and page objects (avoid brittle DOM traversal).

Recommended patterns:
- wait for a panel “ready” state (explicit UI signal),
- wait for a specific request/response pair (if the runner supports it),
- validate stable identifiers, not cosmetic strings where possible.

### Sovereignty + ethics rules (non-negotiable)
These tests MUST:
- never assert raw sensitive coordinates in UI (tooltips, JSON viewers, downloads),
- validate masking/generalization behavior where required,
- treat restricted scenarios as “safe UX paths” (redacted/masked/blocked),
- avoid synthetic narratives that imply genealogy, sacred-site inference, or harmful framing.

### Regression scope guidance
Use regression Focus Mode tests for:
- stable UX contracts (panel presence, navigation, error states),
- governance contract enforcement (CARE tier shows; sovereignty flags show),
- provenance surface integrity (IDs/hashes exist).

Avoid loading regression with:
- long-running data generation,
- high-volume randomized fuzz tests (move to nightly/scheduled suites).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Boot deterministic test stack"] --> B["Load synthetic Focus Mode fixtures"]
  B --> C["Open Focus Mode for test entity"]
  C --> D["Assert panels: Context, Timeline, Map"]
  D --> E["Exercise interactions: timeline and map"]
  E --> F["Assert governance overlays: CARE + sovereignty"]
  F --> G["Assert provenance surfaces: IDs/hashes/links"]
  G --> H["Write artifacts and telemetry"]
~~~

Interpretation:
- The regression suite is intentionally “high-signal”: open, interact, confirm governance/provenance, capture artifacts.

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode often coexists with Story Node surfaces in navigation and evidence display.

### Required integration expectations
Regression E2E tests SHOULD confirm:
- Focus Mode references are grounded (entity ID displayed or implicitly traceable),
- any “evidence” UI element routes to a safe, non-empty provenance surface,
- when Focus Mode is entered from a Story Node view, the entity remains consistent.

### Minimum governance assertions for Focus Mode
Regression E2E tests MUST assert at least:
- masked scenarios never show raw precision in any UI surface,
- restricted scenarios render a safe UI outcome (blocked/redacted/masked),
- governance indicators remain visible and correct (CARE tier + sovereignty flags where applicable).

---

## 🧪 Validation & CI/CD

### CI expectations
- Focus Mode regression tests are typically tagged as `@regression`.
- Any governance-focused Focus Mode tests SHOULD also be tagged `@governance`.
- If a minimal Focus Mode path is required for merge confidence, a small subset MAY be tagged `@smoke`.

### Flake policy
- Flaky Focus Mode tests are quarantined (e.g., `@nightly`) until fixed.
- Governance failures are not “retry-to-green” by default; treat as merge-blocking.

### Required artifacts
Each failing run MUST produce audit-friendly artifacts:
- screenshot(s) on failure,
- trace/video (if supported by runner),
- machine-readable report (JUnit/JSON),
- a run manifest (suite tags, seed, env hash).

Recommended destination (pattern):
~~~text
📁 reports/
└── 📁 e2e/
    ├── 🧾 junit.xml
    ├── 🧾 report.json
    ├── 📁 traces/
    └── 📁 screenshots/
~~~

---

## 📦 Data & Metadata

### Fixture sources
Focus Mode regression tests MUST source data from:
- `tests/e2e/web-app/regression/fixtures/` (regression fixture bundles)
- `tests/fixtures/` (shared synthetic assets)

No production data. No restricted datasets. No real coordinates.

### Minimal scenario set (recommended)
Maintain these baseline scenarios to prevent governance regressions:
- `focus_safe` — fully renderable Focus Mode payload (non-sensitive)
- `focus_masked` — masked/generalized geometry scenario (sovereignty-safe)
- `focus_restricted` — restricted/redacted scenario (blocked path)

### Telemetry expectations
Focus Mode regression runs SHOULD contribute to:
- runtime duration,
- failure counts by category (UI, governance, a11y),
- (where available) energy/carbon estimates at the suite level.

Aggregation target:
~~~text
releases/<version>/tests-e2e-telemetry.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (what this suite produces)
- A regression run is a `prov:Activity`.
- Synthetic fixtures and build artifacts are `prov:Entity`.
- CI runners and maintainers are `prov:Agent`.

### DCAT alignment (optional but supported)
- Regression reports can be treated as `dcat:Distribution` artifacts for auditability.
- Documentation (this README) may be treated as a documentation dataset if indexed.

Governance rule:
- alignment records should reference **IDs and hashes**, not sensitive-like payload dumps.

---

## 🧱 Architecture

### Recommended E2E design pattern
- Use page objects from `tests/e2e/utils/pages/` for Focus Mode entry and stable selectors.
- Use shared assertions from `tests/e2e/utils/assertions/` for governance/provenance checks.
- Keep each spec focused:
  - open → assert panels
  - timeline → assert deterministic filtering
  - map → assert deterministic rendering/selection
  - governance → assert masked/restricted behaviors
  - provenance → assert evidence surfaces are present

### Assertion strategy (high signal)
Prefer assertions that survive UI refactors:
- stable data-testids / roles / landmarks,
- stable entity IDs,
- governance badges/labels,
- presence of provenance references.

Avoid assertions tied to:
- pixel-perfect layout,
- fragile DOM structure,
- long narrative text blocks.

---

## ⚖ FAIR+CARE & Governance

### Merge-blocking conditions
Focus Mode regression MUST block merges if it detects:
- sensitive precision leakage in any UI surface (tooltips, JSON viewers, downloads),
- missing governance indicators where required (CARE/sovereignty),
- restricted content being displayed instead of withheld/masked,
- provenance UI becoming empty or severed from IDs/hashes.

### Escalation routing (policy)
If a governance-related Focus Mode regression fails:
- treat as a stop-ship for PRs touching governed outputs,
- route to the relevant working group and FAIR+CARE Council per governance process.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode v3 regression E2E guide aligned to KFM-MDP v11.2.6 (deterministic, synthetic, sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

