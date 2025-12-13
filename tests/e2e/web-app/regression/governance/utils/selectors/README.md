---
title: "🎯 Kansas Frontier Matrix — Selector Utilities (Governance Regression E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/utils/selectors/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Utility Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-utils-selectors"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-utils-selectors-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:utils:selectors:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/utils/selectors/README.md"
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
  - "tests/e2e/web-app/regression/governance/utils/selectors/README.md@v11.2.6"
---

<div align="center">

# 🎯 **Selector Utilities (Governance Regression E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/utils/selectors/README.md`

**Purpose**  
Define the **canonical selector utility layer** for governance regression E2E suites.  
Selectors in this folder standardize *how tests locate UI surfaces* in a way that is:

- deterministic and stable across refactors,
- accessibility-aligned (roles, names, landmarks),
- governance-safe (no precision leakage, no brittle text scraping),
- consistent across specs, page objects, and leak checks.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Discipline-Stable%20Selectors-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Utilities](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

Selectors are a hidden source of E2E instability. This utility layer exists to ensure governance suites:

- use the same stable selector strategies everywhere,
- avoid brittle CSS chains and text-based scraping that drifts over time,
- prefer accessibility-first selection (roles and names),
- keep governance tests high-signal (fail for real regressions, not DOM churn).

### Selector priorities (normative order)

Governance regression E2E selectors SHOULD follow this priority order:

1. **`data-testid`** (preferred for stable, refactor-friendly hooks)
2. **ARIA role + accessible name** (preferred for A11y alignment and user-realistic flows)
3. **Landmarks and headings** (for navigation and WCAG regression checks)
4. **Stable attributes** (explicitly versioned, non-user-content attributes)
5. **CSS selectors** only as a last resort (never `nth-child`-based)

### Non-goals

This layer is not intended to:

- encode business logic in selectors,
- depend on localized UI copy (text changes are expected),
- parse and re-emit sensitive-like values (coordinates, geometry).

---

## 🗂️ Directory Layout

This folder typically contains selector builders and shared constants used by specs and page objects.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 utils/
                    ├── 📁 selectors/
                    │   ├── 📄 README.md                         — This guide
                    │   ├── 📄 by_testid.ts                      — data-testid selector helpers
                    │   ├── 📄 by_role.ts                        — ARIA role + name helpers
                    │   ├── 📄 by_label.ts                       — label-based helpers (forms)
                    │   ├── 📄 landmarks.ts                      — banner/nav/main/contentinfo helpers
                    │   ├── 📄 testids.ts                        — centralized test-id constants (optional)
                    │   ├── 📄 selectors_catalog.ts              — registry of common selectors (optional)
                    │   └── 📄 index.ts                          — public surface for imports
                    │
                    ├── 📁 navigation/                            — deterministic route + readiness helpers
                    ├── 📁 parsing/                               — safe parsing utilities
                    └── 📁 leak_checks/                           — governance leak checks
~~~

Notes:
- Names above represent the **canonical target layout**. Your repo may use different filenames or languages.
- Centralization here is intentional: governance suites should not reinvent selectors per spec.

---

## 🧭 Context

### Why selectors are a governance concern

Selectors can accidentally create governance failures when tests:

- scrape raw debug panes or hidden JSON blocks,
- rely on text that may contain precision-like fragments,
- “solve” flakiness by widening selectors until they match unintended content.

Selector utilities MUST be written to avoid encouraging these patterns.

### Stable selector guidance (recommended)

Selectors SHOULD:

- anchor to stable UI contracts:
  - `data-testid`
  - ARIA roles
  - landmark regions
- be scoped:
  - select inside a panel container instead of the whole document
- be explicit:
  - “which page/panel” is being targeted

Selectors SHOULD NOT:

- rely on layout positions (`nth-child`, deep `div > div > div` chains),
- depend on user-facing copy that can change due to:
  - localization
  - accessibility improvements
  - content governance revisions
- traverse into hidden debug payload dumps unless the surface is explicitly governed and redacted.

### Naming conventions (recommended)

- `data-testid` values SHOULD be:
  - kebab-case
  - namespaced by feature/surface
  - stable over refactors

Examples:
- `focus-mode-panel-context`
- `focus-mode-panel-timeline`
- `focus-mode-panel-map`
- `governance-badge-care-tier`
- `governance-flag-sovereignty`
- `provenance-panel`
- `provenance-chip-list`

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Spec or page object"] --> B["Selector utility (by_testid/by_role)"]
  B --> C["Scoped element handle"]
  C --> D["Assertion or interaction"]
  D --> E["Parsing and leak checks consume safe surfaces"]
~~~

Interpretation:
- Selector utilities sit between tests and the DOM, ensuring selection is stable, accessible, and governance-safe.

---

## 🧠 Story Node & Focus Mode Integration

Governance regression frequently targets narrative surfaces where selection must be strict and safe.

### Story Node v3 selector expectations

Selectors SHOULD support:

- title and narrative region selection via landmarks/headings
- provenance chip container selection by test ID
- “spacetime” container selection without scraping raw geometry

### Focus Mode v3 selector expectations

Selectors SHOULD support:

- locating the three panels deterministically:
  - Context
  - Timeline
  - Map
- locating governance indicators:
  - CARE tier badge
  - sovereignty flag icon
  - restricted-state banners
- locating provenance surfaces:
  - evidence chip lists
  - reference IDs/hashes

Selectors MUST NOT encourage:

- scraping map canvas internals for coordinates,
- extracting raw GeoJSON from hidden debug panes.

---

## 🧪 Validation & CI/CD

Selector utilities should be:

- unit tested when they include:
  - regex/name normalization
  - scoping logic
  - strict error messages for missing elements
- used consistently across governance suites (no ad-hoc selector drift)

Recommended enforcement:

- lint rule (project-local) that flags:
  - `nth-child` usage
  - deep CSS chains
  - direct text scraping outside explicit allowlisted helpers
- snapshots of selector catalogs (if used) to detect accidental churn.

---

## 📦 Data & Metadata

### Canonical helper shapes (examples)

A small, composable utility interface is recommended.

~~~ts
// by_testid.ts (illustrative)
export function byTestId(id: string): string {
  return `[data-testid="${id}"]`;
}
~~~

~~~ts
// by_role.ts (illustrative)
export type Role = "button" | "link" | "heading" | "textbox" | "dialog" | "main" | "navigation";

export function byRole(role: Role, name?: string): { role: Role; name?: string } {
  return { role, name };
}
~~~

### Selector catalog (optional)

If a selector registry is used, it SHOULD be minimal and stable:

~~~json
{
  "schema_version": "v11.2.6",
  "surfaces": {
    "focus_mode": {
      "panel_context": "focus-mode-panel-context",
      "panel_timeline": "focus-mode-panel-timeline",
      "panel_map": "focus-mode-panel-map"
    },
    "governance": {
      "care_tier_badge": "governance-badge-care-tier",
      "sovereignty_flag": "governance-flag-sovereignty"
    },
    "provenance": {
      "panel": "provenance-panel",
      "chip_list": "provenance-chip-list"
    }
  }
}
~~~

Catalogs MUST NOT include:
- real coordinate-like placeholders,
- real names, addresses, or sensitive references.

---

## 🌐 STAC, DCAT & PROV Alignment

Selector utilities are test-code artifacts:

- **DCAT**: selector catalogs (if emitted as artifacts) are `dcat:Distribution` (`mediaType: application/json`).
- **STAC**: if represented as a STAC item, use:
  - `geometry: null`
  - `properties.datetime` = run timestamp
- **PROV-O**:
  - selector catalogs and utilities are `prov:Entity`,
  - E2E runs that consume selectors are `prov:Activity`,
  - CI runners and maintainers are `prov:Agent`.

---

## 🧱 Architecture

Selectors are designed to compose with other governance utilities:

- **navigation/** establishes deterministic readiness and stable routes
- **selectors/** locates stable UI surfaces
- **parsing/** extracts safe structured signals
- **leak_checks/** enforces “no precision leak” invariants

Recommended pattern:

1. navigate with deterministic readiness
2. select stable elements via selector utilities
3. parse into safe structures
4. assert governance invariants and run leak checks

---

## ⚖ FAIR+CARE & Governance

Selectors influence what tests observe and what they may accidentally store.

Selector utilities MUST uphold:

- **Authority to Control**: do not normalize access to hidden precision surfaces.
- **Responsibility**: do not broaden selectors until they match unsafe content.
- **Ethics**: do not scrape or store user-identifying or sensitive-like fragments.

If a selector change enables unsafe scraping or precision leakage:

- treat as a governance regression,
- block merges affecting governed surfaces,
- fix selectors and/or the underlying UI contracts (prefer stable test IDs).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial selector utilities guide aligned to KFM‑MDP v11.2.6 (stable test IDs, accessibility-first selection, governance-safe scoping). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

