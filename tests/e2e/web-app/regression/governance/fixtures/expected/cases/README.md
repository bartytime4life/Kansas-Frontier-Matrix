---
title: "📌 Kansas Frontier Matrix — Governance Expected Cases (E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/expected/cases/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Fixtures Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-fixtures-expected-cases"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-expected-cases-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:expected:cases:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/expected/cases/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/expected/cases/README.md@v11.2.6"
---

<div align="center">

# 📌 **Governance Expected Cases (E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/expected/cases/README.md`

**Purpose**  
Define the **canonical per-scenario expected baseline files** used by governance E2E regression suites.  
Each file in this folder encodes **minimal, high-signal, policy-safe assertions** (counts, flags, labels, modes) for a single scenario—without embedding payload dumps or sensitive precision.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Fixtures-Expected%20Cases-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Sensitive%20Precision-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Expected Baselines](../README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[🧭 E2E Guide](../../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **one expected baseline per governance scenario**.

Expected cases exist to:
- ✅ keep governance assertions **consistent** across specs,
- ✅ keep diffs reviewable (small JSON files; no UI dumps),
- ✅ enforce **no-leak invariants** by construction (expected files must never contain sensitive-like precision),
- ✅ enable shared assertion helpers to consume a stable shape.

Expected cases MUST:
- remain **synthetic** and **non-identifying**,
- remain **minimal** (assertions only),
- remain **deterministic** (stable IDs and ordering),
- remain **safe** (no geometry payloads, no coordinate-like values, no realistic bboxes).

Expected cases MUST NOT:
- copy raw API responses,
- embed full provenance payloads (IDs/hashes only belong elsewhere),
- include lat/long-like pairs, GeoJSON fragments, WKT, or high-precision bbox values.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 expected/
                        └── 📁 cases/
                            ├── 📄 README.md                      — This guide
                            │
                            ├── 🧾 gov_public_expected.json        — Public scenario expectations (no masking required)
                            ├── 🧾 gov_masked_expected.json        — Masking scenario expectations (no precision visible)
                            ├── 🧾 gov_restricted_expected.json    — Restricted scenario expectations (blocked/redacted UX)
                            │
                            └── 🧾 ...                             — Additional scenario expected baselines (one file per scenario)
~~~

Naming convention (recommended):
- `gov_<scenario_id>_expected.json`

---

## 🧭 Context

### “Expected case” scope boundaries

Expected cases SHOULD describe:
- governance labels and modes:
  - `care_tier`
  - `restriction_mode` (e.g., `allowed | masked | redacted | blocked`)
  - sovereignty badge visibility (boolean)
- no-leak invariants:
  - `raw_coordinates_visible: false`
  - `raw_geometry_visible: false`
  - `high_precision_bbox_visible: false`
- small UI invariants:
  - required banner presence
  - minimum chip/badge counts
  - panel readiness flags (if applicable)

Expected cases SHOULD NOT describe:
- exact UI phrasing beyond stable labels (avoid brittle text matches),
- pixel-perfect layouts (use screenshot artifacts elsewhere),
- full navigation sequences (that belongs in specs / page objects).

### Determinism contract

Expected cases SHOULD be stable over time:
- avoid timestamps unless required; prefer fixed values when used,
- avoid random IDs unless they are pinned and reused,
- ensure arrays are ordered deterministically.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Spec selects scenario_id"] --> B["Load expected case JSON"]
  B --> C["Render governed UI state"]
  C --> D["Run shared governance assertions"]
  D --> E["Run leak checks (separate layer)"]
  E --> F["Write artifacts + telemetry"]
~~~

Interpretation:
- Expected cases define **what must be true**; leak checks independently enforce **what must never appear**.

---

## 🧠 Story Node & Focus Mode Integration

Some governance scenarios originate in narrative surfaces (Story Nodes and Focus Mode).

Expected cases MAY include expectations for:
- governance badges within narrative panels,
- provenance chip presence (ID-only),
- restriction states that persist across panel switching.

Expected cases MUST NOT:
- include narrative bodies,
- include coordinate-bearing “spacetime” fields,
- include full provenance JSON.

---

## 🧪 Validation & CI/CD

Expected cases MUST pass:
- ✅ JSON parse validation
- ✅ schema validation (when a fixture schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak-safety scan (no coordinate-like patterns; no geometry-bearing keys unless explicitly null)

Recommended lint rules for expected cases:
- forbid keys: `coordinates`, `geometry`, `wkt`, `geojson`, `bbox` unless set to `null`,
- forbid numeric patterns that resemble high-precision lat/long pairs,
- enforce `schema_version: "v11.2.6"`.

---

## 📦 Data & Metadata

### Minimal expected case schema (recommended)

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_masked",
  "expect": {
    "care_tier": "Tier B",
    "sovereignty_flag_visible": true,
    "restriction_mode": "masked",
    "restriction_banner_visible": true,
    "no_leak_invariants": {
      "raw_coordinates_visible": false,
      "raw_geometry_visible": false,
      "high_precision_bbox_visible": false
    },
    "ui_counts": {
      "governance_badge_min": 1,
      "provenance_chip_min": 1
    }
  }
}
~~~

Guidance:
- keep counts as **minimums** when possible (reduces brittleness),
- prefer booleans over string comparisons for UI text,
- keep `scenario_id` aligned with the scenario registry used by the suite.

---

## 🌐 STAC, DCAT & PROV Alignment

Expected cases are test fixtures, not production datasets:

- **DCAT**: expected case JSON files can be treated as test artifact distributions (`mediaType: application/json`).
- **STAC**: if indexed, represent as non-spatial items:
  - `geometry: null`
  - `properties.datetime` derived from the run (not fixture content)
- **PROV-O**:
  - expected case files are `prov:Entity`,
  - the E2E run is a `prov:Activity`,
  - CI runner is a `prov:Agent`.

---

## 🧱 Architecture

### How expected cases should be consumed

Specs SHOULD:
1. load a scenario bundle (fixtures/scenarios or api_mocks),
2. render the UI state,
3. load the expected case from this folder,
4. pass it into a shared assertion helper,
5. run leak checks as a separate enforcement step.

This prevents:
- scattered hard-coded expectations,
- accidentally “blessing” unsafe output,
- duplicating governance logic across specs.

---

## ⚖ FAIR+CARE & Governance

Expected cases are governance-critical artifacts.

They must uphold:
- **Authority to Control**: no precision-bearing content that could enable inference.
- **Responsibility**: minimal, auditable, diff-friendly assertions.
- **Ethics**: safe synthetic text only; avoid harmful framing even in placeholders.
- **Collective Benefit**: consistent enforcement of safe behavior across governed surfaces.

If an expected case violates policy:
- delete or correct it immediately,
- fix the underlying scenario/mock/spec that produced the unsafe output,
- re-run governance suites and leak checks before merging.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial expected-cases guide aligned to KFM‑MDP v11.2.6 (one file per scenario; minimal, deterministic, policy-safe baselines). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

