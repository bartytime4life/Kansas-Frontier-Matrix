---
title: "♿ Kansas Frontier Matrix — E2E Accessibility Test Suites (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/accessibility/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-accessibility-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-accessibility-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:accessibility:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/accessibility/README.md"
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

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/tests-e2e-v11.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

provenance_chain:
  - "tests/e2e/web-app/accessibility/README.md@v11.2.6"
---

<div align="center">

# ♿ **Kansas Frontier Matrix — E2E Accessibility Test Suites (v11 LTS)**
`tests/e2e/web-app/accessibility/README.md`

**Purpose**  
Define the canonical E2E accessibility suites for the KFM Web App, ensuring the UI remains **WCAG 2.1 AA+ aligned**, **keyboard-first**, **screen-reader navigable**, and **governance-safe** across Story Nodes, Focus Mode, maps, timelines, and dataset workflows.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧭 E2E Guide](../../README.md) ·
[🖥️ Web App Suites](../README.md) ·
[🧰 Pages](../../utils/pages/README.md) ·
[🧾 Assertions](../../utils/assertions/README.md)

</div>

---

## 📘 Overview

Accessibility E2E suites validate that KFM’s user-facing experience is usable for:

- keyboard-only users
- screen-reader users
- users requiring reduced motion
- users relying on consistent headings, landmarks, and focus indicators
- users interacting with complex spatial + temporal UI (MapLibre/Cesium + timeline)

These suites are **merge-blocking** for critical failures because accessibility is a governance requirement, not an optional enhancement.

The accessibility suites MUST remain:
- deterministic
- sovereignty-safe (no sensitive coordinate leakage via tooltips, debug panels, or downloads)
- fixture-driven (synthetic, non-identifying)

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 accessibility/
            ├── 📄 README.md                   — This guide (a11y suites + runbook)
            │
            ├── 📄 keyboard_navigation.spec.ts  — tab order, focus visible, skip links
            ├── 📄 landmarks_and_headings.spec.ts — landmark/heading structure and order
            ├── 📄 screen_reader_basics.spec.ts — roles/names/labels for critical controls
            ├── 📄 reduced_motion.spec.ts       — reduced-motion behaviors honored
            ├── 📄 color_contrast_smoke.spec.ts — contrast checks where measurable and stable
            │
            └── 📁 artifacts/                   — optional local-only outputs (CI writes to reports/)
                ├── 🧾 axe-results.json
                ├── 🧾 a11y-summary.json
                └── 🧾 screenshots/
~~~

Directory policy:
- Keep accessibility tests scoped to **high-signal** behaviors (landmarks, roles, keyboard, motion).
- Avoid brittle assertions that depend on pixel-perfect rendering.
- Prefer role/name/label semantics over DOM structure.

---

## 🧭 Context

### What “accessibility E2E” means in KFM
An accessibility E2E test is any browser test that asserts one or more of:
- keyboard navigation correctness
- semantic structure correctness (headings/landmarks/roles/names)
- reduced-motion support
- focus management in complex UI (map/timeline overlays, modals, drawers)
- safe handling of error/empty states (clear messages, focus moved appropriately)

### Determinism and stability rules
Accessibility suites MUST:
- avoid time-based sleeps
- use event/state readiness checks (e.g., app-ready markers, stable selectors)
- isolate test state (idempotent tests; no inter-test coupling)
- avoid non-deterministic snapshots (especially for maps)

### What accessibility suites MUST NOT do
- rely on external network calls as a required dependency
- use production accounts, tokens, or datasets
- embed real or plausible sensitive coordinates
- scrape raw debug payloads that could bypass masking rules

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Start web app in test mode"] --> B["Load synthetic fixtures"]
  B --> C["Run keyboard and landmark suites"]
  C --> D["Run reduced-motion suite"]
  D --> E["Run screen-reader semantics suite"]
  E --> F["Collect reports and artifacts"]
  F --> G["Enforce CI gates: a11y pass or block"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Accessibility coverage MUST include governed narrative surfaces because they are central to KFM’s user experience.

### Story Node v3 accessibility expectations
Accessibility E2E suites SHOULD validate:
- a single, clear H1 on Story Node pages
- meaningful heading structure for narrative sections
- provenance chips are reachable by keyboard and labeled
- link text is descriptive (no “click here” patterns)
- any “masked / restricted” indicators are readable and announced to assistive tech

### Focus Mode v3 accessibility expectations
Accessibility E2E suites SHOULD validate:
- panel switching is keyboard-operable
- focus is not trapped incorrectly when panels open/close
- panel headers are announced correctly (role + name)
- timeline interactions provide accessible alternatives (where supported by UI)
- governance overlays are readable and labeled (CARE tier + sovereignty flags)

---

## 🧪 Validation & CI/CD

### Required tagging
Accessibility suites MUST be tagged:
- `@a11y` for accessibility gating
- `@smoke` only for the smallest subset that must always run on PRs

### Merge-blocking policy
- WCAG-critical failures are merge-blocking
- focus-trap regressions are merge-blocking
- missing landmark structure in primary routes is merge-blocking
- violations that risk governance safety (e.g., masked state not communicated) are merge-blocking

### Local runbook pattern
Use repo-defined targets or scripts. Keep commands stable and documented in CI configs.

~~~bash
# Example canonical pattern (repo-defined targets may differ)
make test-stack-up
make e2e-web-a11y
make test-stack-down
~~~

### Required artifacts
Each accessibility run MUST produce machine-readable outputs.

Recommended output location:
~~~text
reports/
└── e2e/
    └── web-app/
        └── accessibility/
            ├── junit.xml
            ├── a11y-report.json
            ├── axe-results.json
            ├── screenshots/
            └── traces/
~~~

---

## 📦 Data & Metadata

### Fixture requirements
Accessibility E2E suites MUST use:
- synthetic entities (Story Nodes, Places, Events, Datasets)
- sanitized narrative snippets (non-identifying, culturally neutral)
- masked geometry states for testing sovereignty behavior (no raw precision)

### Accessibility result metadata
Accessibility suites SHOULD emit:
- counts by violation category (critical/serious/moderate/minor)
- affected route IDs
- selector/role context for failures
- run manifest references (suite tags, env hash, seed)

---

## 🌐 STAC, DCAT & PROV Alignment

Accessibility tests may validate that provenance and dataset links are **present and operable** without requiring parsing full catalog payloads.

Allowed checks:
- provenance/evidence link elements are reachable and labeled
- governance metadata surfaces are readable and announced

Not allowed:
- extracting full catalog payloads through UI unless fixtures-only and explicitly sanitized

---

## 🧱 Architecture

### Recommended test design pattern
- Use page objects for primary routes and complex surfaces
- Use role-first selectors and accessible names
- Validate focus management explicitly:
  - on navigation
  - on modal open/close
  - on panel switching
- Prefer “semantic assertions” over “visual assertions”

### Common a11y failure patterns to catch early
- missing skip link or non-functional skip link
- focus hidden behind overlays
- incorrect landmark structure (no main, multiple main, missing nav label)
- buttons without accessible names
- headings used for styling rather than structure
- reduced-motion preferences ignored in transitions

---

## ⚖ FAIR+CARE & Governance

Accessibility is a governance requirement in KFM.

Accessibility E2E MUST also protect policy constraints by ensuring:
- masked/restricted states are communicated accessibly (not color-only)
- sovereignty-related warnings are readable and announced
- no debug UI exposes sensitive precision, including in copy-to-clipboard features
- culturally sensitive content is not introduced via fixtures or test strings

If an accessibility defect intersects governance safety:
- treat as stop-ship for merges impacting governed outputs
- route to FAIR+CARE Council and the relevant working group

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial accessibility E2E guide aligned to KFM-MDP v11.2.6 (keyboard, landmarks, reduced motion, narrative surface coverage). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

