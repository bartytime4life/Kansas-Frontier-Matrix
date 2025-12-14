---
title: "🕰️ Kansas Frontier Matrix — Timeline Regression (Web App E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/timeline/README.md"

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
intent: "tests-e2e-web-app-regression-timeline"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-timeline-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:timeline:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/timeline/README.md"
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
  - "tests/e2e/web-app/regression/timeline/README.md@v11.2.6"
---

<div align="center">

# 🕰️ **Timeline Regression (Web App E2E) (v11 LTS)**
`tests/e2e/web-app/regression/timeline/README.md`

**Purpose**  
Define the **canonical regression coverage** for the KFM web app **timeline surface**:  
filters, brushing/zoom, ordering, OWL-Time rendering rules, and cross-surface synchronization (Map, Story Nodes, Focus Mode) using **synthetic**, **deterministic**, **governance-safe** fixtures.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Suite-Web%20App%20Regression-blueviolet" />
<img src="https://img.shields.io/badge/Surface-Timeline-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App Regression](../README.md) ·
[🧭 E2E Guide](../../../README.md) ·
[🧪 Tests Index](../../../../README.md)

</div>

---

## 📘 Overview

Timeline regressions protect the **temporal integrity** of user-visible experiences in KFM.

This suite validates that:
- 🧭 **Temporal filtering** is deterministic and stable (same inputs → same results).
- 🧩 **Cross-surface sync** works: timeline actions update map layers and lists predictably.
- 🕰️ **OWL-Time constraints** are respected (instant/interval; start/end; ordering).
- 🧾 **Provenance surfaces** remain stable and non-empty (IDs/hashes only).
- 🛡️ **Governance invariants** are preserved (masked/restricted content stays masked/restricted).
- ♿ **Accessibility** is maintained (keyboard navigation, landmarks, focus order).

### Out of scope (non-goals)

Timeline regression tests are not responsible for:
- validating scientific correctness of the underlying data,
- verifying production data recency,
- reconstructing missing temporal facts.

---

## 🗂️ Directory Layout

This folder is organized for **spec discoverability**, **fixture-driven determinism**, and **auditable expected outputs**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 timeline/
                ├── 📄 README.md                                  — This guide
                │
                ├── 📁 specs/                                     — Runner entrypoints
                │   ├── 📄 timeline_smoke.spec.ts                 — Minimal merge-blocking timeline smoke
                │   ├── 📄 timeline_regression.spec.ts            — Brushing/zoom/filter regressions
                │   └── 📄 timeline_governance.spec.ts            — Masking/restriction + leak checks
                │
                ├── 📁 fixtures/                                  — Synthetic deterministic fixtures
                │   ├── 🧾 scenario_registry.json                  — Scenario ID → bundle mapping
                │   ├── 📁 scenarios/                              — Scenario bundles
                │   │   ├── 🧾 tl_public.json                       — Public-safe timeline scenario
                │   │   ├── 🧾 tl_masked.json                       — Masked/generalized scenario
                │   │   └── 🧾 tl_restricted.json                   — Restricted scenario (blocked/redacted UX)
                │   ├── 📁 api_mocks/                              — Optional endpoint stubs (if interception is used)
                │   ├── 📁 expected_ui/                            — High-signal UI assertions (counts, flags, ordering)
                │   └── 📁 provenance/                             — Provenance fragments (IDs/hashes only)
                │
                ├── 📁 utils/                                     — Timeline helpers (selectors, waits, assertions)
                └── 📁 artifacts/                                 — Local templates (no sensitive dumps)
~~~

Notes:
- Filenames above represent the **canonical target layout**. Adapt extensions/language to your runner while preserving structure and intent.
- This suite is expected to reuse common E2E utilities (waits/selectors/leak checks) via shared imports.

---

## 🧭 Context

### Determinism rules (timeline is not allowed to “guess”)

Timeline E2E tests MUST:
- use stable IDs and stable ordering in fixture arrays,
- avoid non-deterministic “now” timestamps (inject a deterministic clock if needed),
- prefer event-based waits (render-ready state) over arbitrary sleeps,
- isolate tests: a test must not depend on prior test state.

Recommended ready markers:
- timeline root: `data-testid=timeline`
- brush/viewport: `data-testid=timeline-viewport`
- list panel (if present): `data-testid=timeline-list`
- filters panel: `data-testid=timeline-filters`

### OWL-Time expectations (UI-level)

Regression assertions SHOULD validate:
- instants vs intervals render correctly (e.g., single date label vs start–end),
- ordering is stable given equal timestamps (secondary stable key),
- granularity displays are consistent (year/month/day) for the scenario,
- time zone presentation is stable for deterministic fixtures (prefer UTC).

### Governance invariants (timeline-level)

Timeline regressions MUST ensure:
- masked content remains masked in timeline tooltips and details panes,
- restricted scenarios remain blocked/redacted (no “hover to leak”),
- no raw coordinate patterns appear via timeline-linked content.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario_registry.json"] --> B["Select scenario_id"]
  B --> C["Open route with timeline surface"]
  C --> D["Wait for timeline ready markers"]
  D --> E["Interact (filter, brush, zoom)"]
  E --> F["Assert ordering + counts + labels"]
  F --> G["Assert governance invariants (no-leak)"]
  G --> H["Write artifacts + telemetry"]
~~~

Interpretation:
- Timeline regressions are interaction-driven and must validate both UX correctness and governance safety.

---

## 🧠 Story Node & Focus Mode Integration

Timeline interactions are often the “glue” between Story Nodes and Focus Mode.

Regression coverage SHOULD include:
- selecting a timeline entry navigates to the expected Story Node route,
- timeline changes update Focus Mode panels deterministically (Context/Timeline/Map remain coherent),
- provenance chips remain present and safe (IDs/hashes only),
- masked/restricted state does not change due to navigation.

Minimum integration invariants:
- entity identity is stable across transitions,
- time filters persist (or reset) according to policy, deterministically,
- restricted material remains withheld across surfaces.

---

## 🧪 Validation & CI/CD

### Merge-blocking guidance (recommended)

- `timeline_smoke` is merge-blocking for web-app changes.
- Governance-tagged timeline specs are merge-blocking for any change affecting:
  - timeline tooltip/details rendering,
  - provenance panels,
  - masking/restriction behaviors.

### Required artifacts

Every run MUST emit:
- report (JUnit/JSON),
- screenshots on failure,
- trace/video where supported,
- run manifest with scenario IDs and tags.

Recommended path:
~~~text
reports/
└── e2e/
    ├── junit.xml
    ├── report.json
    ├── traces/
    ├── screenshots/
    └── run-manifest.json
~~~

### Flake policy

- Do not add sleeps to stabilize rendering.
- Prefer explicit “ready” markers and deterministic animation settings (reduced motion).
- Governance failures are not retryable by default.

---

## 📦 Data & Metadata

### Scenario registry (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "tl_public": {
      "bundle": "scenarios/tl_public.json",
      "expected": "expected_ui/tl_public_expected.json",
      "provenance": "provenance/tl_public_prov.json",
      "tags": ["@smoke", "@regression"]
    },
    "tl_masked": {
      "bundle": "scenarios/tl_masked.json",
      "expected": "expected_ui/tl_masked_expected.json",
      "provenance": "provenance/tl_masked_prov.json",
      "tags": ["@regression", "@governance"]
    },
    "tl_restricted": {
      "bundle": "scenarios/tl_restricted.json",
      "expected": "expected_ui/tl_restricted_expected.json",
      "provenance": "provenance/tl_restricted_prov.json",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Expected UI contents (timeline-specific)

Expected UI files SHOULD include:
- counts of rendered entries for a filter range,
- expected first/last labels (stable ordering),
- brush/viewport expected domain values (synthetic),
- governance badge visibility expectations,
- forbidden surface expectations (no raw coordinates; no geometry dumps).

### Provenance fragments

Provenance fragments SHOULD include only:
- synthetic dataset IDs / experiment IDs / model card IDs (if surfaced),
- stable hash placeholders,
- governance mode indicators (masked/restricted).

Do NOT include full payloads or raw geometry.

---

## 🌐 STAC, DCAT & PROV Alignment

Timeline regression artifacts are test outputs:

- **DCAT**: reports/traces are `dcat:Distribution` artifacts (`mediaType` per file type).
- **STAC**: if represented, use non-spatial STAC items:
  - `geometry: null`
  - `properties.datetime` as run timestamp
  - assets include report, junit, traces, screenshots
- **PROV-O**:
  - timeline regression run is `prov:Activity`,
  - fixtures/expected/provenance fragments are `prov:Entity`,
  - CI runners are `prov:Agent`.

---

## 🧱 Architecture

### Recommended regression design pattern

Specs SHOULD:
- select `scenario_id`,
- load registry → bundle → expected assertions,
- use stable selectors and page objects,
- centralize waits (timeline ready markers),
- centralize leak checks (shared governance utilities).

Anti-patterns:
- asserting pixel-perfect rendering (prefer semantic assertions),
- embedding large fixture JSON in specs,
- relying on time sleeps or race-prone animation timing.

---

## ⚖ FAIR+CARE & Governance

Timeline regressions protect:

- **Collective Benefit**: ensures public timeline interactions remain reliable and safe.
- **Authority to Control**: prevents precision leakage via tooltips/details.
- **Responsibility & Ethics**: blocks restricted-state bypasses and unsafe debug output.

If a governance-related timeline regression fails:
- block merges affecting governed surfaces,
- fix underlying UI or data shaping,
- do not expand allowlists without review.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial timeline regression guide aligned to KFM‑MDP v11.2.6 (deterministic fixtures, OWL-Time UX invariants, governance-safe assertions). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

