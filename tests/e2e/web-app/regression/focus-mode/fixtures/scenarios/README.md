---
title: "🧪 KFM E2E — Focus Mode Regression Scenarios Fixtures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-focus-mode-regression-scenarios-fixtures"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11.0"

semantic_document_id: "kfm-tests-e2e-focus-mode-regression-scenarios-fixtures"
doc_uuid: "urn:kfm:tests:e2e:web-app:focus-mode:fixtures:scenarios:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/README.md"
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
sunset_policy: "Superseded upon next v12 Focus Mode regression scenario framework update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Focus Mode Regression — Scenario Fixtures (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/scenarios/README.md`

**Purpose**  
Define the **canonical scenario fixture format** used by Focus Mode regression E2E tests.  
Scenarios provide a deterministic, sovereignty-safe way to bind: API mocks → expected UI → provenance overlays → governance outcomes.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Regression-informational" />
<img src="https://img.shields.io/badge/Focus%20Mode-v3-blueviolet" />
<img src="https://img.shields.io/badge/Fixtures-Synthetic%20Only-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Focus Mode Fixtures](../README.md) ·
[🧾 Expected UI](../expected_ui/README.md) ·
[🧩 API Mocks](../api_mocks/README.md) ·
[🧬 Provenance](../provenance/README.md) ·
[🧪 Specs](../../specs/README.md)

</div>

---

## 📘 Overview

### What a “scenario” means in this folder
A **scenario** is a deterministic test bundle that describes:

- **What the UI loads** (route, entity IDs, query params)
- **What the API returns** (synthetic responses and errors)
- **What the UI must show** (expected panels, chips, labels, redactions)
- **What governance must enforce** (CARE tier visibility, sovereignty masking, restricted output behavior)
- **What provenance must render** (OpenLineage/PROV‑O links surfaced safely)

Scenarios exist so regression tests can be:
- stable across machines,
- stable across time,
- and safe across governance boundaries.

### Non-negotiable constraints
Scenario fixtures MUST:
- be synthetic and non-identifying,
- avoid any plausible sensitive coordinates or restricted site geometries,
- be deterministic (pinned IDs, pinned timestamps where used),
- be runnable without external network dependencies (unless explicitly approved elsewhere).

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                ├── 📁 specs/                                         — E2E specs that select scenarios
                └── 📁 fixtures/                                      — All Focus Mode regression fixtures
                    ├── 📁 api_mocks/                                 — Synthetic API responses used per scenario
                    ├── 📁 expected_ui/                               — Expected UI states and snapshot baselines
                    │   └── 📁 scenarios/                             — Expected UI by scenario ID (fm_synth_###)
                    ├── 📁 provenance/                                — Provenance overlays (OpenLineage/PROV‑O/governance)
                    └── 📁 scenarios/                                 — ← This folder (scenario manifests + wiring)
                        ├── 📄 README.md                              — This guide
                        ├── 📁 fm_synth_001/                           — Scenario bundle (example)
                        │   ├── 🧾 scenario.json                       — Scenario manifest (route + bindings)
                        │   ├── 🧾 bindings.json                       — Links to api_mocks / expected_ui / provenance
                        │   └── 📄 README.md                           — Scenario notes and invariants
                        ├── 📁 fm_synth_002/
                        │   ├── 🧾 scenario.json
                        │   ├── 🧾 bindings.json
                        │   └── 📄 README.md
                        └── 📁 fm_synth_003/
                            ├── 🧾 scenario.json
                            ├── 🧾 bindings.json
                            └── 📄 README.md
~~~

**Directory policy**
- Scenario IDs MUST be stable and **never reused** for a materially different scenario.
- A scenario folder MUST be self-contained enough to understand without reading specs.
- Expected UI snapshots live under `../expected_ui/scenarios/<scenario_id>/`.

---

## 🧭 Context

### Scenario ID rules
Scenario directories MUST use this format:

- `fm_synth_001`
- `fm_synth_002`
- `fm_synth_003`

Rules:
- Use **lowercase**, **underscores**, and a **zero-padded** numeric suffix.
- `synth` indicates the scenario is synthetic and governance-safe by design.
- IDs must remain stable across releases; do not rename without a provenance chain update.

### Determinism rules
Scenarios MUST:
- use pinned IDs for entities and datasets (synthetic URNs encouraged),
- pin time inputs if time affects UI ordering,
- avoid “sleep-and-hope” waits in specs (use state/event-based waits),
- avoid test coupling (scenario runs must be idempotent).

### Governance rules (Focus Mode regression)
Scenarios MUST be able to validate that:
- CARE tier labels render correctly,
- sovereignty/redaction states are enforced in UI,
- no restricted precision appears in tooltips, debug panels, exports, or JSON views,
- provenance is visible but safe (no leaking hidden details via provenance).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Spec selects scenario_id"] --> B["Load scenario.json and bindings.json"]
  B --> C["Boot app in deterministic test mode"]
  C --> D["Install API mocks for scenario"]
  D --> E["Navigate to route and render panels"]
  E --> F["Assert expected UI and governance behavior"]
  F --> G["Capture artifacts and telemetry"]
~~~

**Interpretation**  
The scenario manifest wires together the test stack: route + mocks + expected UI + governance/provenance checks.

---

## 🧪 Validation & CI/CD

### What CI expects from scenario fixtures
Scenario fixture changes SHOULD trigger:
- regression suite execution for Focus Mode specs that reference the scenario,
- snapshot comparisons (when snapshots are part of the scenario),
- governance assertions (masking and redaction),
- provenance assertions (chips/panels present, safe fields only).

### Change control rules
If you change:
- `scenario.json` → update scenario README with what changed and why.
- `bindings.json` → ensure referenced fixture paths exist and are stable.
- expected UI snapshots → ensure the spec is deterministic; do not “bless flakes”.

### Flake policy (strict)
- Scenarios that cause flaky UI behavior must be fixed, or quarantined behind a slower tag outside PR gates.
- Governance failures are never “retry-to-green” by default.

---

## 📦 Data & Metadata

### Scenario manifest: `scenario.json`
A scenario MUST define:
- `scenario_id` (matches directory name)
- `route` (relative path the UI will navigate to)
- `mode` flags (governance/test mode toggles)
- `seed` (if any randomness exists; prefer none)
- `expectations` summary (what this scenario is proving)

Example:

~~~json
{
  "scenario_id": "fm_synth_001",
  "route": "/focus-mode?entity=kfm:entity:synth:place:001",
  "mode": {
    "deterministic_time": "2025-01-01T00:00:00Z",
    "governance_enforced": true,
    "network_blocked": true
  },
  "seed": 112233,
  "expectations": {
    "panels": ["context", "timeline", "map"],
    "care_tier_visible": true,
    "sovereignty_redaction_expected": false,
    "provenance_chips_expected": true
  }
}
~~~

### Scenario bindings: `bindings.json`
Bindings connect the scenario to fixture sources:

~~~json
{
  "api_mocks_ref": "../../api_mocks/fm_synth_001/",
  "expected_ui_ref": "../../expected_ui/scenarios/fm_synth_001/",
  "provenance_ref": "../../provenance/",
  "notes": "Synthetic baseline scenario; non-sensitive."
}
~~~

### Required files per scenario folder
Each scenario folder MUST contain:
- `scenario.json`
- `bindings.json`
- `README.md`

Optional files (only if the repo uses them):
- `selectors.json` (stable selectors specific to scenario)
- `expected_events.json` (expected telemetry/provenance events)
- `constraints.json` (assertions that must hold across browsers)

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O and OpenLineage (scenario intent)
Scenarios SHOULD be capable of exercising provenance surfaces by referencing:
- synthetic OpenLineage runs (job/run IDs),
- synthetic PROV‑O entities/activities/agents,
- governance overlay states (tier, redaction mode).

### DCAT/STAC (optional representation)
Scenario artifacts may be represented as:
- `dcat:Distribution` for `scenario.json` and reports (mediaType `application/json`)
- non-spatial STAC Items for scenario runs (geometry null, assets for reports/traces)

Scenarios MUST not require external catalog access in order to run.

---

## ⚖ FAIR+CARE & Governance

### Ethical fixture requirements
Scenario text and labels MUST:
- avoid colonial framing or culturally harmful phrasing (even synthetically),
- avoid plausible restricted knowledge reconstruction,
- avoid real person names or identifying details.

### Sovereignty guardrails
Scenario fixtures MUST NOT:
- embed real coordinates,
- embed plausible sacred-site geometry,
- assert precision behavior that would violate masking policies.

If a scenario is intended to validate masking/redaction:
- it must validate *the presence of masking*, not the underlying precise value.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode regression scenario fixture guide aligned to KFM‑MDP v11.2.6; standardized scenario IDs, manifest/bindings structure, and governance-safe expectations. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

