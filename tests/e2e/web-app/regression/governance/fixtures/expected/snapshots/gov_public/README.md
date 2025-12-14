---
title: "🖼️ Kansas Frontier Matrix — Expected UI Snapshots (gov_public) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_public/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Snapshots Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-expected-snapshots-gov-public"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-expected-snapshots-gov-public-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:expected:snapshots:gov-public:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_public/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_public/README.md@v11.2.6"
---

<div align="center">

# 🖼️ **Expected UI Snapshots — gov_public (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_public/README.md`

**Purpose**  
Define the **canonical expected snapshot baselines** for the `gov_public` governance regression scenario.  
These snapshots confirm that **public-facing governed UI** is usable, correctly labeled, and still **precision-safe** (no coordinate/geometry leaks).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Expected%20Snapshots-blueviolet" />
<img src="https://img.shields.io/badge/Scenario-gov__public-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Precision%20Leak-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Snapshots Index](../README.md) ·
[⬅️ Expected Fixtures](../../README.md) ·
[⬅️ Governance Regression](../../../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

`gov_public` is the “public-safe” governance scenario. It is intended to validate that:

- ✅ governance indicators render correctly (public/low-risk posture is visible to the user),
- ✅ the UI is not unnecessarily blocked or over-redacted for this scenario,
- ✅ provenance surfaces remain present (IDs/hashes/links) without dumping raw payloads,
- ✅ precision safety remains intact:
  - no high-precision coordinate-like strings,
  - no geometry dumps in tooltips, panels, or debug views.

### What `gov_public` is *not*

- It is not a “show everything” mode.
- It does not relax sovereignty protections.
- It does not permit raw coordinates or raw geometry payloads in the UI.

Even in public scenarios, KFM’s safety posture remains **mask-safe by default**.

---

## 🗂️ Directory Layout

This folder contains baseline snapshot artifacts for the `gov_public` expected UI state.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 expected/
                        └── 📁 snapshots/
                            └── 📁 gov_public/
                                ├── 📄 README.md                         — This guide (rules + invariants)
                                │
                                ├── 🧾 snapshot_manifest.json             — Snapshot index (files + hashes + viewport)
                                │
                                ├── 📄 gov_public__chromium__desktop.png  — Baseline: desktop render (public posture visible)
                                ├── 📄 gov_public__chromium__mobile.png   — Baseline: mobile render (public posture visible)
                                │
                                ├── 📄 gov_public__details_panel.png      — Baseline: details/debug UI (IDs/hashes only)
                                └── 📄 gov_public__map_tooltip.png        — Baseline: tooltip state (no raw precision)
~~~

Notes:
- Filenames above are the **canonical target layout**.
- If your runner uses a different naming convention, preserve:
  - scenario ID (`gov_public`),
  - browser + viewport,
  - surface name (`map_tooltip`, `details_panel`, etc.).

---

## 🧭 Context

### Snapshot intent (high-signal assertions)

Snapshots in `gov_public/` SHOULD clearly show:

- **Public posture indicators**
  - public/low-risk messaging or badges (as defined by UI),
  - CARE tier badge (when present in this scenario) is consistent with fixture expectations.
- **Usable governed UX**
  - surfaces load and render without “restricted/blocked” banners (unless the scenario intentionally includes a partial restriction).
- **Precision safety**
  - no coordinate-like pairs (especially high precision),
  - no `GeoJSON`/`WKT`-like geometry dumps visible in UI text.
- **Provenance surfaces remain present**
  - evidence/provenance chips show stable references (IDs/hashes/links),
  - expansions do not reveal raw payload dumps.

### Determinism requirements

To keep `gov_public` snapshots stable across CI:

- Use fixed viewports (one desktop, one mobile).
- Use event-based readiness waits (no arbitrary sleeps).
- Avoid capturing transient loading states (spinners, skeletons, animations).
- Capture “high-signal” surfaces only (main view, tooltip, details panel).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load gov_public fixtures"] --> B["Navigate to governed surface"]
  B --> C["Wait for stable UI state"]
  C --> D["Capture snapshots"]
  D --> E["Compare against expected baselines"]
  E -->|match| F["Pass"]
  E -->|diff| G["Fail + write redacted diff artifacts"]
~~~

Interpretation:
- `gov_public` snapshots exist to detect governance UI regressions without introducing sensitive data into the test suite.

---

## 🧠 Story Node & Focus Mode Integration

When `gov_public` includes navigation across narrative surfaces:

- Story Node routes SHOULD preserve governance posture.
- Focus Mode panels SHOULD render:
  - Context / Timeline / Map consistently,
  - provenance references as IDs/hashes (not raw dumps),
  - no precision leak in tooltips or “details” panes.

Minimum integration invariants:
- governance badges remain consistent across route transitions,
- “public posture” does not disable safety checks,
- no precision appears during panel switching.

---

## 🧪 Validation & CI/CD

### CI expectations

- `gov_public` snapshot comparisons SHOULD be merge-blocking for governance regression suites.
- Snapshot diffs SHOULD:
  - be uploaded as artifacts,
  - be redacted/safe (no raw dumps in reports),
  - include stable metadata (scenario, browser, viewport).

### Updating baselines (controlled)

Baseline updates MUST:
- be tied to an intentional UI change (or deterministic rendering changes),
- be reviewed as governance-impacting changes,
- keep precision-safety and provenance constraints intact.

Example workflow intent (tooling may differ):

~~~bash
make test-stack-up
make e2e-governance:update-snapshots SCENARIO=gov_public
make e2e-governance
make test-stack-down
~~~

---

## 📦 Data & Metadata

### snapshot_manifest.json (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_public",
  "browser_matrix": ["chromium"],
  "viewports": ["desktop", "mobile"],
  "snapshots": [
    { "file": "gov_public__chromium__desktop.png", "surface": "main", "sha256": "<sha256>" },
    { "file": "gov_public__map_tooltip.png", "surface": "map_tooltip", "sha256": "<sha256>" }
  ],
  "invariants": {
    "raw_coordinates_visible": false,
    "geometry_dump_visible": false,
    "public_posture_visible": true,
    "restricted_banner_visible": false
  }
}
~~~

### Content safety rule (snapshot hygiene)

Expected snapshots MUST NOT contain:
- raw coordinate strings,
- raw geometry payload text,
- secrets/tokens,
- identifying text.

If location-like information is needed, use placeholders:
- `COORDINATES_WITHHELD`
- `GEOMETRY_REDACTED`
- `H3_CELL_REDACTED`

---

## 🌐 STAC, DCAT & PROV Alignment

These snapshot artifacts are **test outputs** (not real datasets):

- **DCAT**: snapshot outputs can be treated as `dcat:Distribution` artifacts (e.g., `mediaType: image/png`).
- **STAC**: if represented as STAC items:
  - `geometry: null`
  - `properties.datetime` set to run timestamp
  - assets: snapshots + manifest
- **PROV-O**:
  - snapshot generation is a `prov:Activity`,
  - fixtures/manifests are `prov:Entity`,
  - CI and maintainers are `prov:Agent`.

---

## ⚖ FAIR+CARE & Governance

`gov_public` snapshots enforce two simultaneous obligations:

- **Usability**: public-safe content should render clearly (no accidental “blocked” state).
- **Safety**: public-safe does not mean precision-safe is optional.

If a snapshot diff indicates:
- precision leakage, or
- a governance label mismatch, or
- provenance surfaces dumping raw payloads,

treat it as a governance regression and block merges affecting governed surfaces.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial `gov_public` expected snapshot baselines guide aligned to KFM‑MDP v11.2.6 (public-safe UX, governance-correct, precision-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

