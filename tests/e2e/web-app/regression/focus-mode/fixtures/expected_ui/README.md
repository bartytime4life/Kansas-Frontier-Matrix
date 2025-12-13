---
title: "🧩 Kansas Frontier Matrix — Focus Mode v3 Expected UI Baselines (E2E Regression) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Fixtures Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-focus-mode-expected-ui"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-focus-mode-expected-ui-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:fixtures:expected-ui:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/README.md@v11.2.6"
---

<div align="center">

# 🧩 **Focus Mode v3 Expected UI Baselines (E2E Regression) (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/README.md`

**Purpose**  
Define the **canonical “expected UI” baselines** for Focus Mode v3 regression tests.  
These fixtures capture **what the UI is allowed to show** (and what it must *not* show) using **deterministic, sovereignty-safe, synthetic** examples.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Expected_UI-informational" />
<img src="https://img.shields.io/badge/Surface-Focus%20Mode%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Fixtures](../README.md) · [🧾 API Mocks](../api_mocks/README.md) · [🧠 Focus Mode Specs](../../specs/README.md)

</div>

---

## 📘 Overview

This folder contains **golden expectations** for Focus Mode v3 UI rendering in regression suites.

Expected UI baselines are used to assert:
- **Panel rendering correctness** (Context / Timeline / Map)
- **Provenance visibility rules** (IDs, hashes, references present when required)
- **Governance behavior** (CARE tier labels, sovereignty flags, restricted/redacted behaviors)
- **Accessibility invariants** (headings/landmarks present, key text accessible)
- **Non-disclosure invariants** (no raw sensitive precision, no restricted coordinate leakage)

Expected UI baselines MUST:
- remain **synthetic** and **non-identifying**
- remain **stable** across machines and CI
- avoid dynamic tokens (timestamps, random IDs, build IDs) unless normalized or explicitly ignored
- express governance expectations explicitly (what should be masked/redacted)

Expected UI baselines MUST NOT:
- include real names, real individuals, or restricted archival text
- include raw coordinates or plausible “real site” geometry
- include secrets or environment identifiers
- encode policy exceptions or “temporary bypasses”

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 fixtures/
                    └── 📁 expected_ui/
                        ├── 📄 README.md                         — This guide
                        │
                        ├── 📁 scenarios/                         — Scenario-scoped expected UI baselines
                        │   ├── 📁 fm_synth_001/                   — One deterministic scenario (synthetic)
                        │   │   ├── 🧾 expected_panels.json        — Expected Context/Timeline/Map content (structured)
                        │   │   ├── 🧾 expected_governance.json    — Expected CARE + sovereignty surfaces
                        │   │   ├── 🧾 expected_provenance.json    — Expected evidence chip/link presence
                        │   │   ├── 🧾 expected_a11y.json          — Expected headings/landmarks/labels
                        │   │   └── 📁 snapshots/                  — Optional visual baselines (golden images)
                        │   │       ├── 🖼️ chromium_1280x720.png
                        │   │       └── 🖼️ chromium_1280x720.dark.png
                        │   └── 📁 fm_synth_002/
                        │       └── 🧾 ...
                        │
                        ├── 🧾 ignore_fields.json                 — Normalization rules (fields to ignore or sanitize)
                        └── 🧾 schema_map.json                     — Route/surface → expected file mapping (optional)
~~~

Notes:
- The structure above is the **canonical target layout**. If your repo uses a different naming scheme, keep the same intent and document it here.
- Prefer **structured expectations** (`.json`) over pixel diffs where possible.
- Visual snapshots are permitted only when the surface cannot be asserted reliably via semantics.

---

## 🧭 Context

### Why “Expected UI” exists
Focus Mode surfaces are governance-sensitive. A small UI change can:
- hide provenance,
- expose restricted precision,
- change CARE tier display,
- introduce accidental speculative phrasing,
- break accessibility patterns.

Expected UI fixtures make those constraints **testable** and **auditable**.

### Baseline types
Use the lightest baseline that proves the rule:

1. **Structured panel expectations** (preferred)
   - titles, bullet lists, labels, chips, counts, and key strings
   - stable ordering rules
   - explicit “MUST NOT appear” patterns

2. **Governance expectations** (required where applicable)
   - CARE tier label
   - sovereignty flag presence/absence
   - masking method label (e.g., H3 generalization)
   - restricted/redacted UI state expectations

3. **A11y expectations** (recommended)
   - landmark + heading presence
   - key aria-labels for controls
   - focus order invariants (high-level, not brittle)

4. **Visual snapshots** (last resort)
   - only when semantic assertions cannot cover regressions
   - must be deterministic: viewport, DPR, theme, fonts, reduced-motion

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load api_mocks for scenario"]
  B --> C["Render Focus Mode UI"]
  C --> D["Load expected_ui baselines for scenario"]
  D --> E["Normalize dynamic fields"]
  E --> F["Assert panels, governance, provenance, a11y"]
~~~

Interpretation:
- Expected UI fixtures are paired with API mocks and compared after normalization.

---

## 🧠 Story Node & Focus Mode Integration

Expected UI baselines MUST cover at least:
- direct Focus Mode entry (entity route),
- Story Node → Focus Mode navigation (if regression suite includes it),
- provenance chip behavior (open/expand or link visibility),
- masking behavior when scenario simulates sensitive contexts.

When a scenario simulates “masked” content:
- UI may show generalized geography indicators (e.g., H3 cell IDs or masked extents),
- UI must NOT show raw coordinates in:
  - tooltips
  - debug JSON viewers
  - exports/download previews
  - query string fragments

---

## 🧪 Validation & CI/CD

Expected UI fixtures are merge-sensitive and must pass:
- JSON validity checks
- secret scan / PII scan
- governance-safety scan (no coordinate-like patterns where prohibited)
- schema checks (if expectation schema is defined)

Recommended CI behavior:
- update to `expected_ui/` should trigger regression suite runs for Focus Mode
- snapshot updates (images) should be review-gated (human approval required)

Flake policy:
- expected UI assertions must be deterministic
- if UI strings vary by locale/time, either:
  - normalize them, or
  - assert the stable subset only

---

## 📦 Data & Metadata

### Scenario folder contract
Each scenario folder under `expected_ui/scenarios/<scenario_id>/` SHOULD include:

- `expected_panels.json`
  - expected content for Context / Timeline / Map panels
- `expected_governance.json`
  - expected CARE tier label, sovereignty flags, redaction behavior
- `expected_provenance.json`
  - expected provenance chips/references visible
- `expected_a11y.json`
  - expected headings/landmarks/labels and critical accessible text
- `snapshots/` (optional)
  - golden screenshots for deterministic visual diffs

### Suggested JSON shape (baseline-friendly)
~~~json
{
  "scenario_id": "fm_synth_001",
  "ui_profile": {
    "theme": "light",
    "viewport": { "width": 1280, "height": 720 },
    "browser": "chromium"
  },
  "panels": {
    "context": {
      "must_include": ["Synthetic fact A", "Synthetic fact B"],
      "must_exclude": ["Lat:", "Lon:", "°", "NAD83"]
    },
    "timeline": {
      "event_labels_in_order": ["Synthetic event 1", "Synthetic event 2"]
    },
    "map": {
      "must_show_masking_banner": true,
      "must_not_render_raw_coordinates": true
    }
  },
  "governance": {
    "care_tier": "Tier B",
    "sovereignty_flag": true,
    "masking": { "enabled": true, "method": "H3-R7" }
  },
  "provenance": {
    "must_have_chip_count_at_least": 1,
    "must_include_refs_prefixes": ["mcp/experiments/", "mcp/model_cards/"]
  },
  "a11y": {
    "must_have_landmarks": ["main", "navigation"],
    "must_have_headings": ["Focus Mode", "Context", "Timeline", "Map"]
  }
}
~~~

### Normalization rules (ignore_fields.json)
Normalization MUST remove or ignore values that change per-run:
- timestamps
- run IDs
- telemetry counters
- randomized internal DOM IDs

Keep normalization conservative:
- never normalize away a governance violation
- never normalize away coordinate leakage
- never normalize away provenance absence

---

## 🌐 STAC, DCAT & PROV Alignment

Expected UI fixtures are **test artifacts**, not domain datasets.

Mapping guidance:
- treat `expected_ui` files as `prov:Entity` (kfm:TestFixture)
- treat an E2E run as `prov:Activity` (kfm:TestRun)
- treat the CI job/runner as `prov:Agent`

If your test reporting catalogs artifacts:
- mark them as `kfm:TestArtifact`
- keep `geometry: null` for any STAC representation
- ensure no sensitive content is indexed externally

---

## 🧱 Architecture

### Recommended assertion strategy (ordered)
1. Assert governance invariants (masking/redaction first)
2. Assert provenance visibility (chips/refs)
3. Assert panel content (stable text subset, stable ordering)
4. Assert a11y invariants (landmarks/headings)
5. Use visual diffs only if 1–4 cannot capture the regression

### Visual snapshot guardrails
If you must snapshot:
- pin viewport size and DPR
- pin theme (light/dark) explicitly
- prefer map mocks or deterministic tiles (no live basemaps)
- disable animations/reduced-motion where possible
- avoid flakey elements (spinners, time-based banners)

---

## ⚖ FAIR+CARE & Governance

Expected UI fixtures MUST enforce:
- no sensitive precision leakage
- correct CARE tier display and routing behavior
- sovereignty masking surfaces (when scenario flags it)
- safe restricted-state UX (redacted/blocked/not-found patterns)

If an expected baseline would require the UI to show prohibited content:
- the baseline is invalid and must be replaced
- route review to the relevant working group and FAIR+CARE Council

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial expected UI baselines guide for Focus Mode v3 regression fixtures (deterministic, governance-aware, sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

