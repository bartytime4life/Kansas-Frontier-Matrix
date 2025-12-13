---
title: "🧭 Kansas Frontier Matrix — Focus Mode v3 Expected UI Scenarios (E2E Regression) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/README.md"

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
intent: "tests-e2e-web-app-regression-focus-mode-expected-ui-scenarios"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-focus-mode-expected-ui-scenarios-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:expected-ui:scenarios:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/README.md"
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

signature_ref: "../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/README.md@v11.2.6"
---

<div align="center">

# 🧭 **Focus Mode v3 Expected UI Scenarios (E2E Regression) (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/scenarios/README.md`

**Purpose**  
Define how to create and maintain **scenario-scoped expected UI baselines** for Focus Mode v3 regression testing.  
Scenarios are **deterministic, sovereignty-safe, synthetic** bundles that bind:
**API mocks** → **UI rendering** → **expected assertions**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Regression-informational" />
<img src="https://img.shields.io/badge/Surface-Focus%20Mode%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Expected UI](../README.md) · [🧾 API Mocks](../../api_mocks/README.md) · [📐 Specs](../../../specs/README.md)

</div>

---

## 📘 Overview

A **scenario** is the smallest complete unit of deterministic Focus Mode regression coverage.

Each scenario:
- has a stable `scenario_id`
- maps to one or more API mock bundles (fixtures)
- defines a set of **expected UI assertions** that must hold for:
  - Context panel
  - Timeline panel
  - Map panel
  - Governance surfaces (CARE + sovereignty)
  - Provenance surfaces (evidence chips, refs)
  - Accessibility invariants (headings/landmarks/labels)

Scenarios exist to keep regression tests:
- **auditable** (the expectation is explicit and reviewable)
- **stable** (minimize flake; normalize run-variant fields)
- **governance-safe** (no sensitive precision; no restricted narratives)
- **focused** (one scenario expresses one primary behavioral claim)

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
                        └── 📁 scenarios/
                            ├── 📄 README.md                     — This guide (scenario rules)
                            │
                            ├── 📁 fm_synth_001/                  — Scenario folder (stable ID)
                            │   ├── 🧾 expected_panels.json        — Context/Timeline/Map expectations
                            │   ├── 🧾 expected_governance.json    — CARE + sovereignty expectations
                            │   ├── 🧾 expected_provenance.json    — Evidence/provenance expectations
                            │   ├── 🧾 expected_a11y.json          — WCAG-critical UI expectations
                            │   ├── 🧾 scenario_meta.json          — Optional: scenario tags + UI profile
                            │   └── 📁 snapshots/                  — Optional: visual baselines (last resort)
                            │       ├── 🖼️ chromium_1280x720.png
                            │       └── 🖼️ chromium_1280x720.dark.png
                            │
                            ├── 📁 fm_synth_002/
                            │   └── 🧾 ...
                            │
                            └── 📁 fm_synth_003/
                                └── 🧾 ...
~~~

Naming policy:
- Scenario folders MUST be lowercase and filesystem-safe.
- Preferred pattern: `fm_synth_<nnn>` (example: `fm_synth_014`).
- Scenario IDs MUST be stable across time. Do not rename without a versioned migration.

---

## 🧭 Context

### Scenario design goals
A good scenario:
- covers one high-signal behavior (one “primary claim”)
- includes explicit governance expectations (masking/redaction rules)
- avoids brittle assertions (only assert what must be stable)
- is independent and idempotent (no cross-scenario state)

### Determinism requirements
Scenarios MUST:
- rely on synthetic fixture inputs only
- avoid time-based assumptions (inject deterministic time if needed)
- avoid unstable UI strings (or normalize them explicitly)
- avoid network calls as required dependencies (unless governance-whitelisted)

### Governance-first ordering
When writing expectations, validate in this order:
1. **Masking / restricted-state safety**
2. **CARE tier rendering and routing behavior**
3. **Provenance presence**
4. **Panel content (stable subset only)**
5. **Accessibility invariants**
6. **Visual snapshot diffs (only if necessary)**

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Pick scenario_id"] --> B["Load API mock bundle"]
  B --> C["Render Focus Mode panels"]
  C --> D["Normalize dynamic fields"]
  D --> E["Assert governance + provenance"]
  E --> F["Assert panels + a11y"]
~~~

Interpretation:
- Scenarios bind mocks to expected outputs and enforce governance invariants before content-level diffs.

---

## 🧠 Story Node & Focus Mode Integration

Scenarios SHOULD be chosen to cover:
- direct entity entry into Focus Mode
- panel-to-panel coherence:
  - Context claims ↔ Timeline ordering ↔ Map layer presence
- sovereignty-sensitive UI behaviors:
  - masking banners
  - restricted-state UI (redacted/blocked states)
  - “no raw coordinates” guarantees in tooltips and exports
- provenance “evidence chips”:
  - at least one reference visible where policy requires it
  - stable prefixes (e.g., `mcp/experiments/`, `mcp/model_cards/`) when applicable

If a scenario references Story Node surfaces indirectly (navigation):
- keep Story Node data synthetic and non-identifying
- avoid narrative content that could imply restricted knowledge

---

## 🧪 Validation & CI/CD

Scenario fixture changes are governance-sensitive.

Minimum validations (recommended):
- JSON parse and schema checks (if schemas exist)
- secret/PII scan
- coordinate-pattern scan (to prevent accidental precision leakage)
- deterministic-run checks (no run-variant tokens committed)
- review-gated snapshot updates (human approval required)

CI behavior guidance:
- any changes under `expected_ui/scenarios/**` SHOULD trigger:
  - Focus Mode regression suite
  - governance E2E suite (if present)
  - accessibility checks relevant to the surfaces under test

---

## 📦 Data & Metadata

### Required files per scenario
Each scenario folder MUST include:
- `expected_panels.json`
- `expected_governance.json`
- `expected_provenance.json`
- `expected_a11y.json`

Optional but recommended:
- `scenario_meta.json` (tags, UI profile, dependencies)
- `snapshots/` (only if semantic checks are insufficient)

### Suggested baseline shapes

#### expected_panels.json (stable subset assertions)
~~~json
{
  "scenario_id": "fm_synth_001",
  "panels": {
    "context": { "must_include": ["Synthetic fact A"], "must_exclude": ["Lat:", "Lon:"] },
    "timeline": { "event_labels_in_order": ["Synthetic event 1", "Synthetic event 2"] },
    "map": { "must_show_masking_banner": true, "must_not_render_raw_coordinates": true }
  }
}
~~~

#### expected_governance.json (policy invariants)
~~~json
{
  "scenario_id": "fm_synth_001",
  "care_tier": "Tier B",
  "sovereignty_flag": true,
  "masking": { "enabled": true, "method": "H3-R7" },
  "restricted_state": { "expected": false, "ui_behavior": "n/a" }
}
~~~

#### expected_provenance.json (evidence visibility)
~~~json
{
  "scenario_id": "fm_synth_001",
  "must_have_chip_count_at_least": 1,
  "must_include_ref_prefixes": ["mcp/experiments/", "mcp/model_cards/"],
  "must_not_include": ["internal://", "file:///"]
}
~~~

#### expected_a11y.json (critical accessibility invariants)
~~~json
{
  "scenario_id": "fm_synth_001",
  "must_have_landmarks": ["main", "navigation"],
  "must_have_headings": ["Focus Mode", "Context", "Timeline", "Map"],
  "must_have_controls": [
    { "name": "Toggle layers", "role": "button" }
  ]
}
~~~

### Normalization guidance
Normalization rules SHOULD live in the parent folder:
- `tests/e2e/web-app/regression/focus-mode/fixtures/expected_ui/ignore_fields.json`

Normalization must:
- remove run-variant fields (timestamps, internal IDs)
- preserve governance signals (masking, tier labels, restricted-state behavior)
- never normalize away coordinate leakage detection

---

## 🌐 STAC, DCAT & PROV Alignment

Scenario fixtures are test assets.

Mapping guidance:
- Scenario folder contents are `prov:Entity` (kfm:TestFixture)
- A regression run is `prov:Activity` (kfm:TestRun)
- The runner/CI system is `prov:Agent`

If scenarios are indexed into a test catalog:
- mark `geometry: null` for any STAC representation
- avoid exporting scenario content to public catalogs if it includes governance test triggers

---

## 🧱 Architecture

Recommended loading pattern:
- `scenario_id` is the key.
- The runner loads:
  1) API mocks for `scenario_id`
  2) expected UI baselines for `scenario_id`
  3) normalization rules (shared)
- Assertions are executed in a governance-first sequence.

Recommended tagging:
- store tags in `scenario_meta.json`:
  - `["@regression", "@governance"]` etc.
- keep test tags and scenario tags consistent but not coupled.

---

## ⚖ FAIR+CARE & Governance

Scenario fixtures MUST:
- remain synthetic and non-identifying
- avoid plausible reproduction of restricted knowledge
- avoid colonial framing or culturally harmful phrasing (even as “dummy” text)
- avoid raw coordinate disclosure in any expected baseline

Scenarios MUST explicitly test:
- masking application (when scenario indicates it)
- restricted-state UI behavior (when scenario indicates it)
- provenance visibility rules (when policy requires it)

Governance failures are stop-ship signals for merges affecting governed outputs.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode expected UI scenario guide (deterministic, governance-first, sovereignty-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

