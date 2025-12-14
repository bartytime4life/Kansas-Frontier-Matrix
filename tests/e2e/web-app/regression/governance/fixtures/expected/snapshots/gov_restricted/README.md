---
title: "⛔ Kansas Frontier Matrix — Expected UI Snapshots (gov_restricted) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_restricted/README.md"

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
intent: "tests-e2e-web-app-regression-governance-expected-snapshots-gov-restricted"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-expected-snapshots-gov-restricted-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:expected:snapshots:gov-restricted:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_restricted/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_restricted/README.md@v11.2.6"
---

<div align="center">

# ⛔ **Expected UI Snapshots — gov_restricted (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_restricted/README.md`

**Purpose**  
Define the **canonical expected snapshot baselines** for the `gov_restricted` governance regression scenario.  
These snapshots confirm that the UI correctly enters **restricted mode** (blocked/redacted) while remaining **precision-safe** and **accessible**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Expected%20Snapshots-blueviolet" />
<img src="https://img.shields.io/badge/Scenario-gov__restricted-orange" />
<img src="https://img.shields.io/badge/Policy-Restricted%20Mode-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Snapshots Index](../README.md) ·
[⬅️ Expected Fixtures](../../README.md) ·
[⬅️ Governance Regression](../../../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

`gov_restricted` is the “must-block” governance scenario. It exists to ensure that when the application is required to withhold content:

- ✅ the UI visibly communicates **restriction** (clear banner/modal/state),
- ✅ the user cannot access disallowed material via:
  - panels,
  - tooltips,
  - downloads,
  - “details/JSON” views,
  - console-exposed debug information,
- ✅ provenance surfaces remain **minimal and safe** (IDs/hashes/links only),
- ✅ precision safety remains intact:
  - no coordinate-like strings,
  - no geometry payload dumps,
  - no high-precision bboxes.

### What `gov_restricted` must prove

This scenario MUST prove three invariants simultaneously:

1. **Restricted UX correctness**  
   The correct “blocked/redacted” UI is shown in all relevant surfaces.

2. **No bypass**  
   Route changes, panel switching, and deep links do not reveal restricted content.

3. **No precision leak**  
   Restricted-state failures do not result in raw payload dumps that include sensitive precision.

---

## 🗂️ Directory Layout

This folder contains baseline snapshot artifacts for the `gov_restricted` expected UI state.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 expected/
                        └── 📁 snapshots/
                            └── 📁 gov_restricted/
                                ├── 📄 README.md                               — This guide (rules + invariants)
                                │
                                ├── 🧾 snapshot_manifest.json                   — Snapshot index (files + hashes + viewport)
                                │
                                ├── 📄 gov_restricted__chromium__desktop.png    — Baseline: restricted banner/state visible
                                ├── 📄 gov_restricted__chromium__mobile.png     — Baseline: restricted banner/state visible
                                │
                                ├── 📄 gov_restricted__blocked_modal.png        — Baseline: blocked modal (if used)
                                ├── 📄 gov_restricted__redaction_panel.png      — Baseline: redaction details (safe summary)
                                └── 📄 gov_restricted__map_tooltip.png          — Baseline: tooltip shows withheld, no precision
~~~

Notes:
- Filenames above are the **canonical target layout**.
- Your runner may store additional snapshots (e.g., per-browser), but this folder MUST retain a small set of **high-signal baselines**.

---

## 🧭 Context

### Snapshot intent (what should be visible)

`gov_restricted` snapshots SHOULD clearly show:

- **Restricted state indicators**
  - blocked banner, restricted badge, or modal (as implemented),
  - a user-safe explanation that content is withheld (no “debug” detail).
- **Safe provenance**
  - stable IDs/hashes may be shown,
  - no expanded payload dumps,
  - no raw dataset content.
- **No-leak posture**
  - no coordinate-like strings,
  - no geometry dumps,
  - no verbose error stacks rendered in UI.

### Snapshot intent (what must NOT be visible)

Snapshots MUST NOT show:

- any raw coordinate pairs,
- any raw GeoJSON/WKT-like geometry,
- any “internal” unrestricted text that the restricted scenario is meant to block,
- any secrets/tokens/credentials.

### Determinism requirements

To keep snapshots stable across CI:

- Use fixed viewports (desktop + mobile).
- Wait for the “restricted state ready” UI condition (event-based).
- Avoid capturing transient spinners or toasts.
- Prefer capturing one stable restricted view per surface (main, modal, tooltip).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load gov_restricted fixtures"] --> B["Navigate to governed surface"]
  B --> C["Trigger restricted policy state"]
  C --> D["Wait for restricted UI to stabilize"]
  D --> E["Capture snapshots (main and key surfaces)"]
  E --> F["Compare against expected baselines"]
  F -->|match| G["Pass"]
  F -->|diff| H["Fail and write redacted diff artifacts"]
~~~

Interpretation:
- `gov_restricted` snapshots are intentionally minimal and governance-centered: they validate “blocked correctly” and “nothing leaks.”

---

## 🧠 Story Node & Focus Mode Integration

When `gov_restricted` includes narrative surfaces:

- Story Node routes MUST show the restricted state without rendering withheld narrative bodies.
- Focus Mode panels MUST:
  - show a restricted state for the relevant panel(s),
  - preserve safe provenance references (IDs/hashes),
  - prevent precision leakage in map tooltips and “details” panes.

Minimum integration invariants:
- restricted state persists across panel switching (Context/Timeline/Map),
- restricted state persists across route transitions and refresh,
- no “copy/export/download” paths bypass restriction.

---

## 🧪 Validation & CI/CD

### CI expectations

- `gov_restricted` snapshot comparisons SHOULD be merge-blocking.
- Any diff that changes the restricted UX MUST be treated as governance-impacting.
- Diff artifacts MUST be safe:
  - do not attach raw payload dumps,
  - do not include screenshots of any restricted content (only the blocked UI itself).

### Updating baselines (controlled)

Baseline updates MUST:
- be tied to an intentional restricted UX change,
- preserve the restricted-state invariants,
- be reviewed as governance-sensitive.

Example workflow intent (tooling may differ):

~~~bash
make test-stack-up
make e2e-governance:update-snapshots SCENARIO=gov_restricted
make e2e-governance
make test-stack-down
~~~

---

## 📦 Data & Metadata

### snapshot_manifest.json (recommended minimal shape)

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_restricted",
  "browser_matrix": ["chromium"],
  "viewports": ["desktop", "mobile"],
  "snapshots": [
    { "file": "gov_restricted__chromium__desktop.png", "surface": "main", "sha256": "<sha256>" },
    { "file": "gov_restricted__blocked_modal.png", "surface": "blocked_modal", "sha256": "<sha256>" },
    { "file": "gov_restricted__map_tooltip.png", "surface": "map_tooltip", "sha256": "<sha256>" }
  ],
  "invariants": {
    "restricted_banner_visible": true,
    "blocked_modal_visible": true,
    "raw_coordinates_visible": false,
    "geometry_dump_visible": false,
    "provenance_payload_dump_visible": false
  }
}
~~~

### Content safety rule (snapshot hygiene)

Expected snapshots MUST use placeholders where text might otherwise expose details:

- `CONTENT_WITHHELD`
- `RESTRICTED_BY_POLICY`
- `GEOMETRY_REDACTED`
- `COORDINATES_WITHHELD`

Snapshots should validate *presence of restriction*, not the withheld content.

---

## 🌐 STAC, DCAT & PROV Alignment

These snapshots are **test artifacts** (not real datasets):

- **DCAT**: snapshot outputs can be treated as `dcat:Distribution` artifacts (`mediaType: image/png`).
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

`gov_restricted` snapshots exist to enforce non-negotiable constraints:

- **Authority to Control**: restricted content stays withheld.
- **Responsibility & Ethics**: blocked states must not “accidentally reveal” through debug surfaces.
- **Collective Benefit**: consistent restriction UX avoids harm and builds trust.

If a snapshot diff indicates:
- missing restricted indicators, or
- a bypass path revealing content, or
- precision leakage via UI/debug panels,

treat it as a governance regression and block merges affecting governed surfaces.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial `gov_restricted` expected snapshot baselines guide aligned to KFM‑MDP v11.2.6 (restricted UX correctness, no bypass, no precision leak). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

