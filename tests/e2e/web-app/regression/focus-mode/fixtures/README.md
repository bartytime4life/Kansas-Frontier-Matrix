---
title: "🧩 Kansas Frontier Matrix — Focus Mode v3 Regression Fixtures (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/README.md"

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
intent: "tests-e2e-web-app-regression-focus-mode-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-focus-mode-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/README.md"
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

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧩 **Focus Mode v3 Regression Fixtures (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/README.md`

**Purpose**  
Define the **canonical synthetic fixture set** used by **Focus Mode v3 regression E2E** tests.  
Fixtures in this folder simulate **known UI + governance states** without using real individuals, real sites, or restricted data.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-Fixtures-informational" />
<img src="https://img.shields.io/badge/Surface-Focus%20Mode%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Focus Mode Regression](../README.md) ·
[🧾 Spec Rules](../specs/README.md) ·
[🧭 E2E Guide](../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic, deterministic fixtures** used to drive Focus Mode v3 regression scenarios.

Fixtures here exist to:
- 🧠 Provide stable **Context · Timeline · Map** inputs for regression specs.
- 🛡️ Simulate governance conditions (CARE tiers, sovereignty flags, restricted states) safely.
- 🧾 Provide stable **provenance/evidence surfaces** (IDs, hashes, references) without full payload dumps.
- 🧪 Enable regression tests to assert **masking invariants** and “no-leak” requirements.

Fixtures here MUST be:
- **Synthetic** (non-identifying; non-realistic for restricted knowledge).
- **Deterministic** (stable IDs; stable ordering; stable timestamps where possible).
- **Sovereignty-safe** (no raw sensitive-like geometry; no plausible site coordinates).

Fixtures here MUST NOT:
- include real people, real addresses, real place coordinates, or restricted cultural information,
- include production tokens, credentials, or secrets,
- rely on live network access as a required dependency.

---

## 🗂️ Directory Layout

This folder is organized for **scenario discovery**, **runner-friendly loading**, and **clear governance intent**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 fixtures/
                    ├── 📄 README.md                                  — This guide (rules + governance intent)
                    ├── 🧾 scenario_registry.json                      — Scenario ID → bundle mapping (source of truth)
                    │
                    ├── 📁 api_mocks/                                  — API interception stubs (optional; synthetic)
                    │   ├── 📄 README.md                                — API mock conventions + schema notes
                    │   └── 📁 fm_synth_00x/                            — Per-scenario mock bundles (recommended)
                    │       └── 🧾 *.json                               — Endpoint-shaped responses (synthetic)
                    │
                    ├── 📁 expected_ui/                                 — High-signal expected UI assertions (no payload dumps)
                    │   ├── 📄 README.md                                — What belongs in expected UI fixtures
                    │   └── 📁 scenarios/
                    │       ├── 📄 README.md                            — Scenarios index (expected UI layer)
                    │       ├── 📁 fm_synth_001/
                    │       │   ├── 📄 README.md                        — Expected UI contract for fm_synth_001
                    │       │   └── 📁 snapshots/
                    │       │       └── 📄 README.md                    — Snapshot rules (only sanitized UI render outputs)
                    │       ├── 📁 fm_synth_002/
                    │       │   ├── 📄 README.md
                    │       │   └── 📁 snapshots/
                    │       │       └── 📄 README.md
                    │       └── 📁 fm_synth_003/
                    │           ├── 📄 README.md
                    │           └── 📁 snapshots/
                    │               └── 📄 README.md
                    │
                    ├── 📁 provenance/                                  — Provenance fixtures (IDs/hashes only; synthetic)
                    │   ├── 📄 README.md                                — Provenance fixture rules (no full dumps)
                    │   ├── 📁 governance/
                    │   │   └── 📄 README.md                            — CARE tiers, sovereignty flags, restriction routing
                    │   ├── 📁 mappings/
                    │   │   └── 📄 README.md                            — ID mapping glue (entity↔dataset↔experiment↔modelcard)
                    │   ├── 📁 openlineage/
                    │   │   └── 📄 README.md                            — OpenLineage v2.5 synthetic facets + shapes
                    │   └── 📁 prov_o/
                    │       └── 📄 README.md                            — PROV-O fragments (Activity/Entity/Agent; IDs only)
                    │
                    └── 📁 scenarios/                                   — Scenario manifests (route + flags + invariants)
                        ├── 📄 README.md                                — Scenario bundle conventions (this layer)
                        ├── 📁 fm_synth_001/
                        │   └── 📄 README.md                            — Scenario definition + invariants
                        ├── 📁 fm_synth_002/
                        │   └── 📄 README.md
                        └── 📁 fm_synth_003/
                            └── 📄 README.md
~~~

Notes:
- Use `📁` for directories, `📄` for Markdown, and `🧾` for JSON/YAML artifacts.
- If a fixture file is not Markdown, prefer **machine-friendly** formats (`🧾 .json`) and keep payloads minimal.

---

## 🧭 Context

### Fixture design principles (high-signal over high-volume)
Fixtures SHOULD:
- be small enough to debug from a diff,
- contain just enough data to render panels and trigger governance logic,
- avoid long narrative bodies (prefer short synthetic strings + reference IDs),
- preserve deterministic ordering (arrays sorted; stable keys).

Fixtures SHOULD NOT:
- mirror real historical events in detail,
- embed plausible restricted knowledge even as “fake data,”
- include full external documents (use short synthetic excerpts only).

### IDs and timestamps (determinism contract)
Use stable deterministic identifiers:
- `scenario_id`: stable string key (e.g., `fm_synth_003`)
- `entity_id`: stable synthetic ID (UUID allowed if pinned)
- `seed`: numeric seed (only if a generator is used; stored in the scenario manifest)

Timestamps:
- Use fixed timestamps where possible (e.g., `2020-01-01T00:00:00Z`).
- If “now” is required, it MUST be injected by a deterministic clock provider in the runner.

### Geometry safety rules (fixture-level)
Fixtures MUST NOT contain:
- raw latitude/longitude coordinate pairs intended to represent plausible real locations,
- high-resolution bounding boxes that look like real places,
- sensitive-like geometry payloads (full polygons/lines) unless clearly synthetic and explicitly validated as safe.

Prefer:
- `geometry: null`, or
- generalized representations (e.g., “masked” placeholders) that contain no real precision.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load scenario_registry.json"] --> B["Select scenario_id"]
  B --> C["Load scenario manifest (scenarios/<id>/...)"]
  C --> D["Optionally install api_mocks/<id>/..."]
  D --> E["Render Focus Mode panels (Context/Timeline/Map)"]
  E --> F["Assert expected_ui/scenarios/<id>/..."]
  F --> G["Assert provenance fragments (IDs/hashes only)"]
  G --> H["Write artifacts + telemetry (test run)"]
~~~

Interpretation:
- The fixture stack is a deterministic input layer that enables regression specs to assert UI behavior and governance invariants without exposing real data.

---

## 🧠 Story Node & Focus Mode Integration

Fixtures MAY represent:
- an entity opened directly in Focus Mode, or
- an entity reached from a Story Node route transition.

When fixtures simulate Story Node linkage:
- use synthetic Story Node IDs,
- keep relationships shallow and deterministic,
- ensure governance flags are preserved across navigation.

Minimum integration invariants:
- entity identity remains stable across panel interactions,
- provenance surfaces remain non-empty (IDs/hashes),
- restricted state remains restricted across route transitions and UI exports.

---

## 🧪 Validation & CI/CD

Fixtures are CI-scanned and CI-validated.

Fixtures MUST pass:
- ✅ JSON parse validation (where applicable)
- ✅ schema validation (when a fixture schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ sovereignty safety checks (no coordinate leakage patterns)

Recommended fixture lint rules:
- enforce stable formatting and ordering in JSON (formatter in CI),
- forbid coordinate-like key pairs unless explicitly null/generalized,
- forbid full geometry dumps in “expected_ui” fixtures,
- verify every `scenario_id` referenced in `scenario_registry.json` has:
  - a scenario manifest,
  - an expected UI contract,
  - a provenance fragment bundle reference.

---

## 📦 Data & Metadata

### scenario_registry.json (canonical shape)
The registry maps scenario IDs to fixture bundle roots.

Example (simplified):
~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "fm_synth_001": {
      "scenario_ref": "scenarios/fm_synth_001/",
      "expected_ui_ref": "expected_ui/scenarios/fm_synth_001/",
      "api_mocks_ref": "api_mocks/fm_synth_001/",
      "provenance_ref": "provenance/",
      "tags": ["@regression"]
    },
    "fm_synth_002": {
      "scenario_ref": "scenarios/fm_synth_002/",
      "expected_ui_ref": "expected_ui/scenarios/fm_synth_002/",
      "api_mocks_ref": "api_mocks/fm_synth_002/",
      "provenance_ref": "provenance/",
      "tags": ["@regression", "@governance"]
    },
    "fm_synth_003": {
      "scenario_ref": "scenarios/fm_synth_003/",
      "expected_ui_ref": "expected_ui/scenarios/fm_synth_003/",
      "api_mocks_ref": "api_mocks/fm_synth_003/",
      "provenance_ref": "provenance/",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Scenario manifests (what belongs there)
Scenario manifests SHOULD declare:
- `scenario_id`
- deterministic route (or navigation recipe)
- fixed time (or injected time config)
- governance flags (CARE tier, sovereignty visibility, restricted geometry simulation)
- invariants (e.g., “raw coordinates forbidden”, “export blocked or masked”)

### Expected UI fixtures (what belongs there)
Expected UI fixtures MUST remain **high-signal and minimal**, such as:
- required panel presence flags,
- expected counts (chips, timeline entries),
- required governance badges (CARE tier visible, sovereignty indicator visible),
- restricted-state UI expectations (masked/redacted/blocked),
- explicit “no raw coordinates” assertions.

Expected UI fixtures MUST NOT:
- include full API payload dumps,
- include full geometry payloads,
- include copied internal debug JSON that contains raw precision.

### Provenance fixtures (IDs/hashes only)
Provenance fixtures SHOULD include only:
- dataset IDs / STAC/DCAT IDs (synthetic IDs allowed),
- experiment IDs / model card IDs (synthetic references allowed),
- hashes/checksums (placeholders allowed until pinned),
- governance routing metadata (Tier, allowed/blocked/masked state).

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (fixture interpretation)
- Scenario manifests and expected UI files are `prov:Entity` artifacts.
- An E2E run is a `prov:Activity`.
- CI runner and maintainers are `prov:Agent`.

### OpenLineage alignment (synthetic test runs)
If OpenLineage events are emitted during E2E:
- include scenario_id and suite tags as run facets,
- include fixture bundle refs as inputs,
- include reports/traces/screenshots as outputs.

### STAC/DCAT alignment (optional)
If fixtures are indexed as documentation/test datasets:
- represent them as non-spatial resources (`geometry: null`),
- treat outputs as test artifacts (not real datasets),
- keep any “coverage” synthetic and non-identifying.

---

## 🧱 Architecture

### How fixtures are used by specs (recommended pattern)
Specs SHOULD:
1. select a `scenario_id`,
2. load `scenario_registry.json`,
3. load the scenario manifest + expected UI + provenance fragments,
4. drive UI interactions using page objects,
5. apply shared assertions using expected UI contracts.

This avoids:
- hardcoding payloads in test logic,
- duplicating scenario selection logic,
- fragile assertions scattered across specs.

---

## ⚖ FAIR+CARE & Governance

### Sovereignty and masking rules (non-negotiable)
Fixtures MUST:
- never encode raw sensitive-like coordinates,
- simulate masked states without revealing precision,
- ensure restricted-state fixtures produce safe UI behaviors:
  - redacted, masked, or blocked.

### Ethical fixture language rules
Synthetic text MUST:
- avoid colonial framing and culturally harmful phrasing,
- avoid implying genealogy or sacred knowledge,
- remain minimal and purely functional for testing.

### Escalation
If a fixture violates policy:
- remove it immediately,
- quarantine any dependent specs until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Expanded and normalized fixture architecture to match KFM‑MDP v11.2.6 (emoji directory layout, scenario bundles, expected UI snapshots, provenance subpackages). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
