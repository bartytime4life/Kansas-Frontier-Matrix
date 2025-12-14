---
title: "✅ Kansas Frontier Matrix — Governance Expected Baselines (E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/expected/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-expected"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-expected-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:expected:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/expected/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/expected/README.md@v11.2.6"
---

<div align="center">

# ✅ **Governance Expected Baselines (E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/expected/README.md`

**Purpose**  
Define the **canonical “expected baseline” fixtures** used by governance E2E regression suites to assert:
- correct governance UI states (CARE tier labels, sovereignty badges, restriction banners),
- correct masking/redaction behavior (no sensitive precision leakage),
- stable provenance surfaces (IDs/hashes only; no payload dumps),

using **synthetic, deterministic, sovereignty-safe** expected outputs.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Fixtures-Expected%20Baselines-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Sensitive%20Precision-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Fixtures](../README.md) ·
[⬅️ Governance Regression](../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **expected baselines** (“goldens”) used by governance regression tests.

Expected baselines exist to:
- ✅ reduce flaky assertions by centralizing “what should be true” for a scenario,
- ✅ keep governance tests **high-signal** (policy-critical fields only),
- ✅ enforce **no-leak invariants** (precision never appears in governed surfaces),
- ✅ provide an auditable spec surface for reviewers (diffable JSON, minimal content).

Expected baselines MUST be:
- **Synthetic** (non-identifying; no real places, no real people, no restricted knowledge).
- **Deterministic** (stable IDs; stable ordering; stable timestamps where used).
- **Minimal** (assertions only; avoid duplicating full API payloads or UI dumps).
- **Policy-safe** (no geometry payloads; no lat/long-like values; no realistic bboxes).

Expected baselines MUST NOT:
- include screenshots that require OCR to validate correctness,
- embed raw or plausible sensitive-like coordinates,
- “bless” unsafe UI output by allowlisting it here.

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
                        ├── 📄 README.md                         — This guide (expected baseline rules)
                        │
                        ├── 🧾 expected_registry.json             — Scenario ID → expected file mapping
                        │
                        ├── 📁 cases/                             — One file per scenario expected baseline
                        │   ├── 🧾 gov_public_expected.json        — Fully public, no masking required
                        │   ├── 🧾 gov_masked_expected.json        — Masking required; no precision permitted
                        │   └── 🧾 gov_restricted_expected.json    — Restricted/blocked UX expectations
                        │
                        └── 📁 snapshots/                          — Optional structured “UI snapshot” JSON (not images)
                            ├── 🧾 gov_public_snapshot.json
                            ├── 🧾 gov_masked_snapshot.json
                            └── 🧾 gov_restricted_snapshot.json
~~~

Notes:
- This is the **canonical target layout** for expected baselines.
- If your runner uses different filenames, keep a stable mapping in `expected_registry.json`.

---

## 🧭 Context

### What belongs in an “expected baseline”

Expected baselines SHOULD contain:
- expected governance labels (CARE tier, sovereignty flag presence),
- expected restriction state (allowed/masked/redacted/blocked),
- expected provenance references (IDs/hashes only),
- expected UI invariants (no-precision-leak boolean flags, banner presence, chip counts).

Expected baselines SHOULD NOT contain:
- full narrative bodies (use short synthetic strings and/or reference IDs),
- full API payload copies (that belongs in `api_mocks/`),
- raw DOM dumps (prefer structured, targeted expectations).

### “High-signal” governance invariants

Governance regression tests MUST be able to assert these invariants from expected baselines:

- **No sensitive precision appears** in governed UI surfaces:
  - no coordinate pairs,
  - no high-precision bboxes,
  - no GeoJSON/WKT-like geometry strings.
- **CARE tier** is visible and matches the scenario.
- **Sovereignty** indicator is visible when required.
- **Restricted** state produces safe UX (redacted, masked, or blocked).
- **Provenance** shows IDs/hashes only (no payload dumps).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load api_mocks and scenario bundle"]
  B --> C["Render governed UI surface"]
  C --> D["Load expected baseline (expected/cases)"]
  D --> E["Run assertions from expected baseline"]
  E --> F["Run leak checks (no precision)"]
  F --> G["Write artifacts and telemetry"]
~~~

Interpretation:
- Expected baselines define “what must be true,” while leak checks ensure “what must never appear.”

---

## 🧠 Story Node & Focus Mode Integration

Expected baselines may cover governance behavior across:
- Story Node routes that expose governance badges or provenance chips,
- Focus Mode panels that render governed content and evidence surfaces.

Minimum integration expectations:
- governance status persists across navigation,
- restriction banners persist after panel switching,
- provenance surfaces remain non-empty without exposing full content.

---

## 🧪 Validation & CI/CD

Expected baselines MUST pass:
- ✅ JSON parse validation
- ✅ schema validation (if a fixture schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ leak-safety scan (no coordinate-like patterns)

Recommended lint rules for `expected/`:
- forbid geometry-bearing keys unless set to `null`:
  - `geometry`, `coordinates`, `bbox`, `wkt`, `geojson`
- enforce stable ordering for assertion arrays
- enforce `schema_version: "v11.2.6"` (or via registry)

---

## 📦 Data & Metadata

### Registry shape (recommended)

~~~json
{
  "schema_version": "v11.2.6",
  "expected_cases": {
    "gov_public": {
      "expected": "cases/gov_public_expected.json",
      "snapshot": "snapshots/gov_public_snapshot.json",
      "tags": ["@regression", "@governance"]
    },
    "gov_masked": {
      "expected": "cases/gov_masked_expected.json",
      "snapshot": "snapshots/gov_masked_snapshot.json",
      "tags": ["@regression", "@governance"]
    },
    "gov_restricted": {
      "expected": "cases/gov_restricted_expected.json",
      "snapshot": "snapshots/gov_restricted_snapshot.json",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Expected baseline shape (recommended)

Keep this minimal and auditable.

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_masked",
  "expect": {
    "care_tier": "Tier B",
    "sovereignty_flag_visible": true,
    "restriction_mode": "masked",
    "restriction_banner_visible": true,

    "provenance": {
      "has_ids": true,
      "allows_payload_dump": false
    },

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

### Snapshot JSON (optional, structured)

If you need a “snapshot,” keep it structured and safe (no full dumps).

~~~json
{
  "schema_version": "v11.2.6",
  "scenario_id": "gov_restricted",
  "snapshot": {
    "page": "GovernanceOverlay",
    "visible_panels": ["governance"],
    "visible_badges": ["CARE", "SOVEREIGNTY"],
    "visible_banners": ["RESTRICTED"],
    "redaction_markers_present": true
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Expected baselines are test fixtures, not real datasets:

- **DCAT**: expected JSON files may be treated as test artifact distributions (`mediaType: application/json`).
- **STAC**: if indexed, represent as non-spatial STAC items:
  - `geometry: null`
  - `properties.datetime` = E2E run time (not fixture content)
- **PROV-O**:
  - expected files are `prov:Entity`,
  - an E2E run is `prov:Activity`,
  - CI runner is `prov:Agent`.

---

## 🧱 Architecture

### Recommended usage pattern

Governance specs SHOULD:
1. select `scenario_id`,
2. load `api_mocks` + scenario bundle,
3. render the UI state,
4. load the expected baseline from this folder,
5. apply shared assertion helpers,
6. run leak checks as a separate enforcement layer,
7. emit artifacts + telemetry.

This prevents:
- scattered hardcoded expectations,
- brittle assertion logic across multiple specs,
- silently weakening governance posture.

---

## ⚖ FAIR+CARE & Governance

Expected baselines are governance artifacts. They must uphold:

- **Authority to Control**: never encode precision that could enable inference.
- **Responsibility**: keep baselines minimal and auditable.
- **Ethics**: avoid harmful framing, even in synthetic labels and messages.
- **Collective Benefit**: ensure the system remains safe and respectful by default.

If an expected baseline is found to include unsafe content:
- remove it immediately,
- fix the underlying mock/scenario that produced the unsafe output,
- re-run governance suites and leak checks before merging.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance expected baselines guide aligned to KFM‑MDP v11.2.6 (minimal assertions, deterministic registry, no-leak invariants). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

