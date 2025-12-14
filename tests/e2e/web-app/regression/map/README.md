---
title: "🗺️ Kansas Frontier Matrix — Map Regression (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/map/README.md"

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
intent: "tests-e2e-web-app-regression-map"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-map-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:map:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/map/README.md"
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
  - "tests/e2e/web-app/regression/map/README.md@v11.2.6"
---

<div align="center">

# 🗺️ **Map Regression (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/map/README.md`

**Purpose**  
Define the **canonical E2E regression suite** for KFM’s **map experience** (MapLibre/Cesium as applicable):  
layer toggles, render stability, timeline/map coupling, performance budgets, and governance-safe behavior (no precision leaks).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Suite-Map%20Regression-blueviolet" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Web App Regression](../README.md) ·
[🧭 E2E Guide](../../../README.md) ·
[🧪 Tests Index](../../../../README.md)

</div>

---

## 📘 Overview

The map is a **high-risk regression surface** because failures can present as:
- blank tiles / missing layers,
- broken interactions (hover, click, filters, timeline coupling),
- nondeterministic rendering and flaky waits,
- accidental precision leakage via tooltips, debug panels, downloads, or URL state.

This folder defines how we validate map behavior end-to-end using:
- ✅ deterministic, synthetic fixtures,
- ✅ event-based waits (no “sleep-and-hope”),
- ✅ auditable artifacts (traces, screenshots, reports),
- ✅ governance guardrails (masking invariants; no precision leaks).

### What “map regression” covers in KFM

Map regression specs SHOULD include:
- layer enable/disable flows and persisted UI state,
- base map + overlay rendering expectations,
- timeline-driven filters reflected on the map,
- selection/hover tooltips and highlight behavior,
- map viewport changes (zoom/pan) with stable UI readiness,
- performance budgets (within reason for CI),
- sovereignty-safe rendering (masked/generalized states).

### Non-goals

- Map regression does not validate climate/hydrology scientific correctness.
- Map regression does not attempt to infer restricted locations.
- Map regression does not use real coordinates, real sites, or production data.

---

## 🗂️ Directory Layout

This directory is organized for **fixtures → specs → assertions → artifacts**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 map/
                ├── 📄 README.md                              — This guide (map regression suite)
                │
                ├── 📁 specs/                                 — E2E spec files (runner-specific)
                │   ├── 📄 map_smoke.spec.ts                  — Fast PR-gate scenarios
                │   ├── 📄 map_layers_regression.spec.ts      — Layer toggles, ordering, visibility
                │   ├── 📄 map_interactions.spec.ts           — Hover/click/select, tooltips, highlights
                │   ├── 📄 map_timeline_coupling.spec.ts      — Timeline filters reflected on map
                │   ├── 📄 map_viewport_persistence.spec.ts   — URL/state persistence (zoom/center/layers)
                │   └── 📄 map_governance_invariants.spec.ts  — Masking/no-precision invariants
                │
                ├── 📁 fixtures/                              — Synthetic inputs (non-sensitive)
                │   ├── 🧾 scenario_registry.json              — Scenario ID → bundle mapping
                │   ├── 📁 scenarios/                          — Scenario bundles (public/masked/restricted)
                │   ├── 📁 api_mocks/                          — Optional API stubs (if runner intercepts)
                │   ├── 📁 expected/                           — High-signal expected UI assertions
                │   ├── 📁 allowlists/                         — Safe placeholders only (no realistic coords)
                │   └── 📁 provenance/                         — IDs/hashes only; no full payload dumps
                │
                ├── 📁 assertions/                             — Reusable map assertions (high-signal)
                │   ├── 📄 assert_layers.ts
                │   ├── 📄 assert_map_ready.ts
                │   ├── 📄 assert_tooltips_safe.ts
                │   └── 📄 assert_no_precision_leak.ts
                │
                ├── 📁 utils/                                  — Navigation, selectors, waits, parsing
                │   ├── 📄 selectors.ts
                │   ├── 📄 waits.ts
                │   ├── 📄 navigation.ts
                │   ├── 📄 parsing.ts
                │   └── 📄 telemetry.ts
                │
                └── 📁 artifacts/                              — Map-specific artifact handling
                    ├── 📁 templates/                          — Report templates (redacted by default)
                    ├── 📁 snapshots/                          — Snapshot manifests (not raw dumps)
                    └── 📄 README.md
~~~

Notes:
- Filenames above are the **canonical target layout**.
- If the repo uses a different runner extension (e.g., `.cy.ts`, `.pw.ts`), preserve:
  - structure,
  - intent,
  - merge-blocking posture for `map_smoke` and governance invariants.

---

## 🧭 Context

### Determinism rules (map regressions must not “guess”)

Map regression specs MUST:
- use deterministic fixture bundles (stable IDs; stable ordering; stable timestamps),
- use event-based waits:
  - layer-ready indicators,
  - network-idle (when safe),
  - selector-visible state changes,
- avoid frame-perfect assumptions (GPU/browser differences exist),
- keep assertions **high-signal**:
  - “layer present and visible,” not “pixel-perfect render.”

### Governance rules (non-negotiable)

Map regression MUST assert:
- no raw coordinate precision appears in:
  - map tooltips,
  - side panels,
  - debug/JSON views,
  - downloads,
  - URL query/state where policy forbids it,
- masked scenarios remain masked across:
  - hover/select,
  - zoom/pan,
  - layer toggles,
  - route transitions.

### Tagging (recommended)

- `@smoke` — minimal PR gate
- `@regression` — broader suite
- `@map` — map-only subset
- `@governance` — masking/no-precision invariants
- `@a11y` — keyboard navigation and landmark behavior for map UI controls

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Boot test stack (UI/API in test mode)"]
  B --> C["Load map scenario bundle (fixtures)"]
  C --> D["Navigate to map route"]
  D --> E["Wait for map readiness (event-based)"]
  E --> F["Interact (layers/hover/select/timeline)"]
  F --> G["Assert map invariants + UI expectations"]
  G --> H["Run leak checks (tooltips/panels/downloads)"]
  H --> I["Write artifacts + telemetry summary"]
~~~

Interpretation:
- Map regression runs are fixture-driven and governance-aware: we validate behavior and prevent precision leaks before CI can allow merges.

---

## 🧠 Story Node & Focus Mode Integration

Map behavior is coupled to narrative and entity surfaces in KFM.

### Story Node v3 map expectations

Map regression SHOULD validate (where applicable):
- Story Node map jumps land on correct (synthetic) geometry extent,
- masked Story Node geometry remains masked (no raw precision),
- provenance chips remain present without expanding into payload dumps.

### Focus Mode v3 map expectations

Map regression SHOULD validate:
- focus overlays (highlights, pins, extents) remain governance-safe,
- tooltips remain policy-safe (IDs/hashes/titles; no raw coordinates),
- switching panels does not reset map governance state.

---

## 🧪 Validation & CI/CD

### CI posture (recommended)

- `map_smoke` SHOULD be merge-blocking.
- `map_governance_invariants` SHOULD be merge-blocking for governed surfaces.

### Local run intent

~~~bash
# Example intent (replace with repo scripts)
make test-stack-up
make e2e-map-smoke
make e2e-map-regression
make test-stack-down
~~~

### Flake policy

- Map specs MUST not rely on arbitrary sleeps.
- If a map spec flakes:
  - fix readiness signals/waits,
  - reduce over-precise assertions,
  - avoid “pixel-perfect” checks unless explicitly required and stable.

---

## 📦 Data & Metadata

### Scenario registry (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "map_public": {
      "bundle": "scenarios/map_public.json",
      "expected": "expected/map_public_expected.json",
      "tags": ["@regression", "@map"]
    },
    "map_masked": {
      "bundle": "scenarios/map_masked.json",
      "expected": "expected/map_masked_expected.json",
      "tags": ["@regression", "@map", "@governance"]
    },
    "map_restricted": {
      "bundle": "scenarios/map_restricted.json",
      "expected": "expected/map_restricted_expected.json",
      "tags": ["@regression", "@map", "@governance"]
    }
  }
}
~~~

### “Expected” files (what belongs there)

Expected files MUST contain only high-signal assertions:
- layer IDs visible/invisible,
- expected counts (features rendered, markers present),
- governance flags visible,
- raw precision visibility flags (always false in masked/restricted).

~~~json
{
  "scenario_id": "map_masked",
  "expect": {
    "map_ready": true,
    "layers_visible": ["base", "context"],
    "layers_hidden": ["raw_geometry_layer"],
    "tooltips_safe": true,
    "raw_coordinates_visible": false,
    "sovereignty_flag_visible": true
  }
}
~~~

### Artifact guidance (safe by default)

Artifacts MUST NOT include full payload dumps.
Artifacts SHOULD include:
- traces/videos (runner-supported),
- screenshots for failures,
- redacted summaries (rule IDs, selectors, counts).

---

## 🌐 STAC, DCAT & PROV Alignment

Map regression outputs are test artifacts (not real datasets):

- **DCAT**: reports may be treated as `dcat:Distribution` (`mediaType: application/json`).
- **STAC**: if represented as STAC items:
  - `geometry: null`
  - `properties.datetime` set to run timestamp
  - assets: `report.json`, `run-manifest.json`, `trace.zip`
- **PROV-O**:
  - each map regression run is a `prov:Activity`,
  - fixtures are `prov:Entity`,
  - CI runner is a `prov:Agent`.

---

## 🧱 Architecture

### Recommended spec composition (thin specs, shared helpers)

Specs SHOULD:
1. choose `scenario_id`,
2. load registry + bundle + expected,
3. navigate using shared navigation helpers,
4. wait for map readiness using shared waits,
5. assert map invariants with shared assertions,
6. run leak checks for tooltips/panels/download paths,
7. write artifacts + telemetry.

### Anti-patterns (avoid)

- pixel-perfect checks without stable GPU normalization,
- sleeping for map load rather than waiting for readiness signals,
- allowing tooltips to print raw geometry fragments (even for synthetic),
- allowlisting any string that resembles real coordinates.

---

## ⚖ FAIR+CARE & Governance

Map regression protects high-impact constraints:

- **Authority to Control**: prevents accidental precision leakage.
- **Responsibility & Ethics**: ensures public-facing map UX cannot reveal restricted detail.
- **Collective Benefit**: preserves safe, trustworthy geospatial narratives.

If map regression detects a governance failure:
- treat as merge-blocking for governed surfaces,
- fix the underlying UI/API behavior,
- do not weaken leak checks or expand allowlists as a shortcut,
- escalate to the relevant working group and FAIR+CARE Council when policy impact is unclear.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial map regression E2E guide aligned to KFM‑MDP v11.2.6 (fixture-driven, deterministic waits, governance-safe tooltips, merge-blocking invariants). |

<div align="center">

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

