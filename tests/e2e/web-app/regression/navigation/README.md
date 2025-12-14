---
title: "🧭 Kansas Frontier Matrix — Navigation Regression (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/navigation/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-navigation"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-navigation-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:navigation:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/navigation/README.md"
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
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

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
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/web-app/regression/navigation/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Navigation Regression (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/navigation/README.md`

**Purpose**  
Define the **canonical E2E regression suite** for KFM web-app navigation:  
routing, deep-links, state persistence, guarded routes, error boundaries, and safe back/forward behavior across governed surfaces.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Suite-Navigation%20Regression-blueviolet" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App Regression](../README.md) ·
[🧭 E2E Guide](../../../README.md) ·
[🧪 Tests Index](../../../../README.md)

</div>

---

## 📘 Overview

Navigation is a **system-wide coupling surface**: it connects map state, timeline state, Story Nodes, Focus Mode panels, governance overlays, and provenance views.

Navigation regressions tend to manifest as:
- broken deep links,
- state loss on refresh,
- infinite redirects or unexpected route guards,
- incorrect breadcrumbs or title updates,
- unsafe URL state (leaking forbidden precision or restricted identifiers),
- “back/forward” restoring an inconsistent governance state.

This suite validates navigation behavior end-to-end using:
- ✅ deterministic synthetic fixtures,
- ✅ event-based waits (not sleeps),
- ✅ auditable artifacts (trace + redacted reports),
- ✅ governance-safe URL and UI checks.

### What this suite covers

Navigation regression SHOULD validate:
- app shell boot + initial route stability,
- deep links to core surfaces (Map, Story Node, Focus Mode),
- route guards and safe fallbacks (404, permission-denied, restricted),
- query-param handling (filters, tabs, panel state),
- back/forward + refresh semantics,
- URL safety invariants (no raw precision, no restricted payload dumps).

### Non-goals

- This suite does not validate scientific content correctness.
- This suite does not validate full map rendering (covered in `map/`).
- This suite does not validate accessibility flows (covered in `accessibility/`), but MUST not break a11y-critical navigation patterns.

---

## 🗂️ Directory Layout

This directory is organized for **specs + fixtures + shared navigation helpers + artifacts**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 navigation/
                ├── 📄 README.md                              — This guide (navigation regression suite)
                │
                ├── 📁 specs/                                 — E2E spec files (runner-specific)
                │   ├── 📄 nav_smoke.spec.ts                  — Merge-blocking minimal scenarios
                │   ├── 📄 nav_deeplinks.spec.ts              — Deep-link coverage (routes + params)
                │   ├── 📄 nav_state_persistence.spec.ts      — Refresh/back-forward restores state
                │   ├── 📄 nav_route_guards.spec.ts           — Restricted/blocked/safe responses
                │   ├── 📄 nav_error_boundaries.spec.ts       — 404/500-like safe routes
                │   └── 📄 nav_governance_url_safety.spec.ts  — URL safety (no precision leaks)
                │
                ├── 📁 fixtures/                              — Synthetic navigation scenarios
                │   ├── 🧾 scenario_registry.json              — Scenario ID → bundle mapping
                │   ├── 📁 scenarios/                          — Route + state bundles
                │   ├── 📁 expected/                           — High-signal expected UI outcomes
                │   ├── 📁 allowlists/                         — Safe placeholders only
                │   └── 📁 provenance/                         — IDs/hashes only; no payload dumps
                │
                ├── 📁 utils/                                  — Shared navigation helpers
                │   ├── 📄 routes.ts                           — Canonical route builders
                │   ├── 📄 navigation.ts                       — Navigate + assert ready
                │   ├── 📄 waits.ts                            — Event-based readiness checks
                │   ├── 📄 selectors.ts                        — Stable selectors (data-testid)
                │   └── 📄 parsing.ts                          — URL/state parsing helpers
                │
                └── 📁 artifacts/                              — Navigation suite artifacts
                    ├── 📁 templates/                          — Redacted report templates
                    ├── 📁 snapshots/                          — Snapshot manifests (not raw dumps)
                    └── 📄 README.md
~~~

Notes:
- Filenames above are the **canonical target layout**.
- If your repo uses different runner conventions, preserve:
  - deterministic fixture registry,
  - a merge-blocking smoke spec,
  - governance URL safety spec.

---

## 🧭 Context

### Determinism rules (navigation must not “guess”)

Specs MUST:
- avoid relying on nondeterministic redirects,
- use stable navigation helpers that wait for route readiness,
- avoid timing-based assumptions for async route hydration.

Recommended readiness cues:
- route-specific `data-testid` root marker,
- spinner disappearance with bounded wait,
- network-idle only when safe and controlled.

### Governance rules (URL safety is mandatory)

Navigation specs MUST assert:
- no raw coordinate precision appears in:
  - the URL path,
  - query params,
  - hash fragments,
  - copied share links rendered by the UI (if present),
- restricted routes produce safe results:
  - blocked screen or masked view,
  - no leakage via “details” panels or logs.

### Tags (recommended)

- `@smoke` — PR gate (fast, deterministic)
- `@regression` — broader coverage
- `@governance` — route guards + URL safety
- `@a11y` — only where navigation assertions are explicitly tied to keyboard or focus behavior

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Pick scenario_id"] --> B["Build route (routes.ts)"]
  B --> C["Navigate (navigation.ts)"]
  C --> D["Wait for route-ready marker (waits.ts)"]
  D --> E["Assert expected UI (expected/*.json)"]
  E --> F["Assert URL safety (no precision leaks)"]
  F --> G["Write artifacts + telemetry summary"]
~~~

Interpretation:
- Navigation regression is fixture-driven: we validate routes, restore behavior, and governance-safe URL/UI outcomes before CI can merge.

---

## 🧠 Story Node & Focus Mode Integration

Navigation regressions are most likely at **cross-surface transitions**.

### Story Node route expectations

Navigation specs SHOULD validate:
- deep link to a Story Node renders safely,
- provenance chips present without payload expansion,
- route transitions preserve governance banners.

### Focus Mode route expectations

Navigation specs SHOULD validate:
- opening Focus Mode via:
  - direct deep-link,
  - from Story Node,
  - from map selection,
  results in consistent panel state and safe governance overlays.

### Minimum invariants across transitions

- “back” returns to the previous surface without losing policy state,
- restricted states remain restricted after back/forward,
- no precision leaks via URL state when toggling views.

---

## 🧪 Validation & CI/CD

### CI posture (recommended)

- `nav_smoke` SHOULD be merge-blocking.
- `nav_route_guards` and `nav_governance_url_safety` SHOULD be merge-blocking for governed surfaces.

### Local run intent

~~~bash
# Example intent (replace with repo scripts)
make test-stack-up
make e2e-nav-smoke
make e2e-nav-regression
make test-stack-down
~~~

### Flake policy

- No arbitrary sleeps.
- If a test flakes:
  - improve route readiness markers,
  - strengthen deterministic fixture setup,
  - simplify assertions to high-signal states (not micro-timings).

---

## 📦 Data & Metadata

### Scenario registry (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "nav_public_deeplink": {
      "bundle": "scenarios/nav_public_deeplink.json",
      "expected": "expected/nav_public_deeplink_expected.json",
      "tags": ["@smoke"]
    },
    "nav_masked_route": {
      "bundle": "scenarios/nav_masked_route.json",
      "expected": "expected/nav_masked_route_expected.json",
      "tags": ["@regression", "@governance"]
    },
    "nav_restricted_route": {
      "bundle": "scenarios/nav_restricted_route.json",
      "expected": "expected/nav_restricted_route_expected.json",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Expected UI (high-signal only)

~~~json
{
  "scenario_id": "nav_restricted_route",
  "expect": {
    "route_ready": true,
    "status_view": "restricted",
    "raw_coordinates_visible": false,
    "details_payload_visible": false,
    "governance_banner_visible": true
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Navigation regression outputs are test artifacts:

- **DCAT**: reports may be `dcat:Distribution` (`mediaType: application/json`).
- **STAC**: if represented as STAC items:
  - `geometry: null`
  - `properties.datetime` as run timestamp
- **PROV-O**:
  - navigation run is `prov:Activity`,
  - fixtures are `prov:Entity`,
  - CI runner is `prov:Agent`.

---

## 🧱 Architecture

### Recommended navigation helper pattern

A canonical navigation helper SHOULD:
- build route deterministically,
- navigate,
- wait for route readiness,
- return a typed page object (or stable handle) for further assertions.

Anti-patterns:
- waiting for “some element” without scoping to the route,
- relying on global network-idle across the entire app,
- storing raw payloads in artifacts as “debugging help.”

---

## ⚖ FAIR+CARE & Governance

Navigation regression protects critical constraints:

- **Authority to Control**: prevents unsafe deep links from bypassing masking.
- **Responsibility & Ethics**: ensures restricted routes remain restricted.
- **Collective Benefit**: supports safe public UX without accidental exposure.

If a navigation regression detects a governance failure:
- treat as merge-blocking for governed surfaces,
- fix routing/state handling, do not relax allowlists,
- route uncertain cases to the working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial navigation regression E2E guide aligned to KFM‑MDP v11.2.6 (deep-links, guards, persistence, URL safety, deterministic waits). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

