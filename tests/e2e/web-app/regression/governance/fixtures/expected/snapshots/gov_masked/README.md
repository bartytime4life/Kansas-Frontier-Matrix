---
title: "🖼️ Kansas Frontier Matrix — Expected UI Snapshots (gov_masked) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_masked/README.md"

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
intent: "tests-e2e-web-app-regression-governance-expected-snapshots-gov-masked"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-governance-expected-snapshots-gov-masked-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:expected:snapshots:gov-masked:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_masked/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_masked/README.md@v11.2.6"
---

<div align="center">

# 🖼️ **Expected UI Snapshots — gov_masked (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/expected/snapshots/gov_masked/README.md`

**Purpose**  
Define the **canonical expected snapshot baselines** for the `gov_masked` governance regression scenario.  
These snapshots exist to confirm that **masking, redaction, and “no precision leak” invariants** are user-visible, stable, and CI-enforced.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Expected%20Snapshots-blueviolet" />
<img src="https://img.shields.io/badge/Scenario-gov__masked-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Precision%20Leak-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Snapshots Index](../README.md) ·
[⬅️ Expected Fixtures](../../README.md) ·
[⬅️ Governance Regression](../../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

The `gov_masked` scenario is designed to validate that governed surfaces:

- ✅ display **masked/generalized** location context instead of raw precision,
- ✅ keep “details” / debug panes safe (no raw coordinate or geometry dumps),
- ✅ preserve governance signals (CARE tier badges, sovereignty flags, masking indicators),
- ✅ remain deterministic across CI runs.

Snapshots in this folder are **expected outputs** (baselines). They are compared against actual UI renders to detect:

- regressions in masking UX (e.g., a “masked” badge disappears),
- regressions that reintroduce precision leakage (even accidentally),
- regressions in governance labeling (CARE tier mismatches),
- regressions in redaction behavior for restricted/controlled data states.

### Non-negotiable constraints

Snapshots MUST:
- be created from **synthetic fixtures** (non-identifying; non-sensitive),
- avoid capturing or embedding any raw coordinate precision,
- remain deterministic (stable viewport, stable font rendering settings where possible).

Snapshots MUST NOT:
- include any real site imagery, real addresses, or realistic sensitive coordinates,
- include secrets, tokens, or restricted payload dumps,
- require external network access to reproduce.

---

## 🗂️ Directory Layout

This folder contains baseline snapshot artifacts for the `gov_masked` expected state.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 expected/
                        └── 📁 snapshots/
                            └── 📁 gov_masked/
                                ├── 📄 README.md                         — This guide (rules + invariants)
                                │
                                ├── 🧾 snapshot_manifest.json             — Snapshot index (files + hashes + viewport)
                                │
                                ├── 📄 gov_masked__chromium__desktop.png  — Baseline: desktop render (masked indicators visible)
                                ├── 📄 gov_masked__chromium__mobile.png   — Baseline: mobile render (masked indicators visible)
                                │
                                ├── 📄 gov_masked__details_panel.png      — Baseline: details/debug UI (no raw precision)
                                └── 📄 gov_masked__map_tooltip.png        — Baseline: tooltip state (no raw coordinates)
~~~

Notes:
- Filenames above represent the **canonical target layout** for `gov_masked`.
- If your runner uses a different naming convention, keep the intent stable:
  - scenario ID present,
  - browser/viewport encoded,
  - feature surface encoded (map tooltip, details panel, etc.).

---

## 🧭 Context

### What these snapshots are asserting

Snapshots in `gov_masked/` SHOULD provide evidence of these high-signal UI invariants:

- **Masking indicator visible**
  - “masked/generalized” labels are present where policy requires them.
- **No precision leakage**
  - no coordinate-like pairs appear in tooltips, panels, or detail views.
  - no GeoJSON/WKT-like “geometry dumps” appear in UI.
- **Governance badges present**
  - CARE tier badge is visible and matches the scenario fixture.
  - sovereignty flags are visible when the fixture indicates they should be.
- **Safe “details” experience**
  - any JSON/diagnostic UI shows IDs/hashes or redacted placeholders only.

### Determinism expectations

To keep snapshots stable across CI:

- Use fixed viewports (e.g., a single “desktop” and “mobile” profile).
- Use event-based waits before capture (panel ready, map idle, fonts loaded).
- Avoid capturing animated states (transitions, spinners, loading skeletons).

### Naming conventions (recommended)

Use consistent, scan-friendly filenames:

- `gov_masked__<browser>__<viewport>.png`
- `gov_masked__<surface>.png`

Avoid:
- spaces in filenames,
- timestamps inside filenames,
- machine-specific paths inside filenames.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load gov_masked fixtures"] --> B["Navigate to governed surface"]
  B --> C["Wait for stable UI state"]
  C --> D["Capture snapshot(s)"]
  D --> E["Compare to expected baselines"]
  E -->|match| F["Pass"]
  E -->|diff| G["Fail + write redacted diff artifacts"]
~~~

Interpretation:
- `gov_masked` snapshots are a deterministic assertion layer. They fail fast on masking regressions.

---

## 🧪 Validation & CI/CD

### Expected behavior in CI

- `gov_masked` baseline comparisons SHOULD be merge-blocking for governance regression suites.
- Snapshot diffs SHOULD produce artifacts that are safe to store:
  - do not upload raw dumps,
  - prefer redacted diffs and bounded screenshots.

### Updating snapshots (strict policy)

Snapshot updates MUST:
- be tied to an intentional UX change or policy change,
- be reviewed like a governance-sensitive change,
- avoid “mass update” unless a deterministic rendering change is confirmed.

Recommended workflow (example intent; tool specifics may differ):

~~~bash
# Example pattern:
# 1) Run the scenario locally in deterministic test mode
# 2) Update snapshots intentionally
# 3) Validate governance leak checks still pass

make test-stack-up
make e2e-governance:update-snapshots SCENARIO=gov_masked
make e2e-governance
make test-stack-down
~~~

### Flake handling (do not weaken baselines)

If snapshots are flaky:
- fix waits and deterministic rendering controls,
- reduce snapshot surface area to high-signal UI regions,
- do not relax governance assertions to “make it green.”

---

## 📦 Data & Metadata

### snapshot_manifest.json (recommended minimal shape)

This manifest exists to keep snapshot sets auditable and machine-indexable.

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_masked",
  "browser_matrix": ["chromium"],
  "viewports": ["desktop", "mobile"],
  "snapshots": [
    {
      "file": "gov_masked__chromium__desktop.png",
      "surface": "main",
      "sha256": "<sha256>"
    },
    {
      "file": "gov_masked__map_tooltip.png",
      "surface": "map_tooltip",
      "sha256": "<sha256>"
    }
  ],
  "invariants": {
    "raw_coordinates_visible": false,
    "masked_indicator_required": true,
    "care_badge_required": true
  }
}
~~~

### What must never be in expected snapshots

Expected snapshots MUST NOT contain:
- numeric coordinate-like strings rendered in the UI,
- full debug payload dumps visible on-screen,
- realistic imagery of sensitive locations.

If you need to show “location-like” content, use placeholders:
- `H3_CELL_REDACTED`
- `COORDINATES_WITHHELD`
- `MASKED_GEOMETRY`

---

## ⚖ FAIR+CARE & Governance

`gov_masked` snapshots are governance-sensitive because they validate user-visible policy behavior.

These baselines exist to enforce:
- **Authority to Control**: masking stays applied and visible.
- **Responsibility**: the UI cannot “accidentally” leak precision.
- **Ethics**: fixtures and text remain synthetic and non-identifying.

If a snapshot diff indicates precision leakage:
- treat it as **stop-ship** for governed surfaces,
- fix UI/API behavior rather than weakening the baseline.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial `gov_masked` expected snapshot baselines guide aligned to KFM‑MDP v11.2.6 (deterministic, sovereignty-safe, governance-enforced). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

