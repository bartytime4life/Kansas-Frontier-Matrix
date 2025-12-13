---
title: "🖥️ Kansas Frontier Matrix — E2E Web App Test Suites (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/README.md"

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
intent: "tests-e2e-web-app-guide"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/README.md"
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

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tests-e2e-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/README.md@v11.2.6"
---

<div align="center">

# 🖥️ **Kansas Frontier Matrix — E2E Web App Test Suites (v11 LTS)**
`tests/e2e/web-app/README.md`

**Purpose**  
Define the canonical E2E suites for the KFM Web App: navigation, map/timeline UX, Story Node and Focus Mode surfaces, governance overlays, accessibility flows, and deterministic PR-gate smoke coverage.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧭 E2E Guide](../README.md) ·
[🧰 Pages](../utils/pages/README.md) ·
[🧾 Assertions](../utils/assertions/README.md)

</div>

---

## 📘 Overview

The Web App E2E suites verify that the user-visible product remains:

- **functionally correct** (routes, rendering, interactions)
- **stable and deterministic** (no flaky sleeps; event-based readiness)
- **accessible** (keyboard-first, landmarks, roles)
- **governance-safe** (CARE tier and sovereignty masking behavior is enforced)
- **narrative-safe** (Story Node and Focus Mode surfaces never leak restricted precision)

These suites focus on the KFM Web UI surfaces and their API-driven behaviors, without requiring external networks or production data.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        ├── 📄 README.md                 — This guide (web app suites + runbook)
        │
        ├── 📁 smoke/                    — PR gate: minimal, deterministic, high-signal
        │   ├── 📄 app_boot.spec.ts       — app boots, shell renders, no console errors
        │   ├── 📄 map_smoke.spec.ts      — map renders, layer toggles respond
        │   ├── 📄 timeline_smoke.spec.ts — timeline loads, filters apply deterministically
        │   └── 📄 nav_smoke.spec.ts      — core routes reachable (no auth, no tokens)
        │
        ├── 📁 regression/               — broader UI coverage (allowed slower)
        │   ├── 📄 map_layers.spec.ts     — layer groups, legends, basemap changes
        │   ├── 📄 timeline_filters.spec.ts— multi-filter combos + reset behavior
        │   ├── 📄 search.spec.ts         — entity search, result navigation
        │   └── 📄 deep_links.spec.ts     — permalink + share link behavior
        │
        └── 📁 accessibility/            — WCAG-focused flows (keyboard, landmarks, reduced motion)
            ├── 📄 keyboard_nav.spec.ts   — tab order, focus visible, skip links
            ├── 📄 landmarks.spec.ts      — roles/regions present and coherent
            └── 📄 reduced_motion.spec.ts — reduced-motion support honored
~~~

---

## 🧭 Context

### Scope boundaries (what belongs here)
Web App suites belong here when they:
- drive browser interactions (Playwright/Cypress)
- validate UI state changes that depend on API responses
- validate accessibility and governance overlays at the UI layer

If a test is primarily about:
- schemas or contracts → `tests/schemas/` or integration suites
- API-only logic → integration or unit
- governance policy evaluation without UI → governance integration suites

### Determinism contract
Web App E2E MUST:
- use seeded synthetic fixtures
- use deterministic time (fixed clock or injectable provider)
- prefer state-based waits (selector visible, network idle, app-ready marker)
- avoid brittle image/pixel comparisons unless supported by stable hooks

### Selector contract
Use page objects and role-first selectors:
- prefer `role + name` and `label`
- allow `data-testid` for complex widgets (map canvas, timeline brush)

Never rely on:
- CSS classes
- deep DOM paths
- hard-coded pixel offsets

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Web App smoke suite (@smoke)"] --> B["App boot + shell ready"]
  B --> C["Map/timeline ready checks"]
  C --> D["Core interactions (toggle, filter, navigate)"]
  D --> E["Governance + a11y assertions"]
  E --> F["Artifacts + telemetry"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Web App suites must include governed narrative surfaces because they are user-visible policy boundaries.

### Web app responsibilities for narrative surfaces
The web app E2E suites SHOULD verify:
- Story Node route renders and shows provenance chips
- Focus Mode panels render consistently (Context/Timeline/Map)
- Governance overlays appear when expected (CARE tier, sovereignty flag)
- Restricted precision never appears in:
  - tooltips
  - JSON debug panels
  - downloads
  - copy-to-clipboard surfaces

Recommended coupling:
- Use `storynode.page.ts` and `focusmode.page.ts` page objects
- Use governance-safe assertions from `tests/e2e/utils/assertions/`

---

## 🧪 Validation & CI/CD

### Required suite tags
Web App E2E tests MUST use tags:
- `@smoke` for PR gate tests
- `@regression` for broader coverage
- `@a11y` for accessibility flows
- `@governance` when asserting CARE/sovereignty behavior

### Merge-blocking policy
- `@smoke` is merge-blocking
- `@a11y` is merge-blocking for critical violations
- `@governance` failures are stop-ship by default

### Runbook pattern
Use repo scripts as the source of truth. The commands below are a canonical pattern.

~~~bash
# Example canonical pattern (repo-defined targets may differ)
make test-stack-up
make e2e-web-smoke
make test-stack-down
~~~

### Artifact requirements
Each run MUST produce:
- machine-readable report (JUnit/JSON)
- screenshots on failure
- trace/video when supported
- run manifest (suite tags, seed, env hash)

Recommended output location:
~~~text
reports/
└── e2e/
    ├── web-app/
    │   ├── junit.xml
    │   ├── report.json
    │   ├── traces/
    │   └── screenshots/
    └── run-manifest.json
~~~

---

## 📦 Data & Metadata

### Synthetic data requirements
Web App E2E tests MUST:
- rely on synthetic Story Nodes, Places, Events, Datasets
- avoid real-world identifiers, names, or plausible sensitive coordinates
- validate masking behavior through safe UI signals (badges, “masked” labels)

### Environment flags
The web app should run E2E in a deterministic mode, typically enabling:
- fixed time provider
- synthetic fixture loader
- telemetry sinks enabled (test-mode)
- debug surfaces sanitized (no restricted payload dumps)

If these flags exist, document them in the stack bootstrap docs (not in this file unless present in repo).

---

## 🌐 STAC, DCAT & PROV Alignment

Web App suites may validate the existence of catalog and provenance surfaces without parsing raw catalog JSON.

Allowed checks:
- provenance chips present and non-empty
- dataset reference links present for Story Node evidence
- governance labels visible

Not allowed:
- scraping full STAC/DCAT payloads from UI unless explicitly sanitized and fixtures-only

---

## 🧱 Architecture

### Test design patterns
Recommended patterns for Web App E2E:
- page objects for each surface (app/map/timeline/storynode/focusmode)
- “one test, one primary claim” (high-signal failures)
- minimal reliance on multi-step state when not needed
- stable IDs for synthetic fixtures (repeatable deep-links)

### Common flows covered by suites
- App boot and route readiness
- Map layer toggles and legend interactions
- Timeline brush / range filters / reset behavior
- Search and navigation to entities
- Story Node rendering + provenance chips
- Focus Mode panel switching + governance overlays
- Accessibility flows (keyboard navigation, landmarks)

---

## ⚖ FAIR+CARE & Governance

### Mandatory governance assertions for Web App suites
Web App E2E MUST block merges when it detects:
- sensitive precision leakage (coordinates/geometry/tooltip)
- sovereignty badge missing when required
- CARE tier routing failures
- restricted content not redacted/masked/blocked as policy requires
- governed narrative surfaces emitting disallowed language patterns (where policies prohibit it)

### Escalation workflow
When a governance-tagged test fails:
- treat as stop-ship for merges affecting governed outputs
- route to FAIR+CARE Council and the relevant working group
- record the failure in the audit ledger (per repo policy)

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Web App E2E guide aligned to KFM-MDP v11.2.6 (smoke/regression/a11y structure, determinism and governance enforcement). |

<div align="center">

[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

