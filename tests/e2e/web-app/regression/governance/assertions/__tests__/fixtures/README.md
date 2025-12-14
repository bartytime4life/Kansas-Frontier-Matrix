---
title: "🧩 Kansas Frontier Matrix — Governance Assertion Fixtures (Unit Tests) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/assertions/__tests__/fixtures/README.md"

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
intent: "tests-e2e-web-app-regression-governance-assertions-unit-test-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-assertions-unit-test-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:assertions:unit-tests:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/assertions/__tests__/fixtures/README.md"
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
  - "tests/e2e/web-app/regression/governance/assertions/__tests__/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧩 **Governance Assertion Fixtures (Unit Tests) (v11 LTS)**
`tests/e2e/web-app/regression/governance/assertions/__tests__/fixtures/README.md`

**Purpose**  
Define the **canonical synthetic fixture set** used by unit tests for governance assertions.  
These fixtures provide **safe, deterministic inputs** (UI text samples, redacted payload summaries, expected results) that validate **CARE routing**, **sovereignty masking**, and **no-leak invariants**—without embedding real people, real sites, or restricted knowledge.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Type-Fixtures-informational" />
<img src="https://img.shields.io/badge/Surface-Governance%20Assertions-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Synthetic%20Only-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Unit Tests](../README.md) ·
[📸 Snapshots](../snapshots/README.md) ·
[⬅️ Assertions](../../README.md) ·
[⬅️ Governance Regression](../../../README.md)

</div>

---

## 📘 Overview

This folder holds **fixture inputs** for governance assertion unit tests, typically used to validate:

- 🪪 **CARE tier display and routing** (Tier A/B/C behavior and labels).
- 🪶 **Sovereignty flags and masking** (generalized/blocked states remain safe).
- 🧾 **Provenance surfacing** (IDs/hashes present, no full payload dumps).
- 🕵️ **Leak-prevention primitives** (coordinate-like strings, bbox-like patterns, geometry-like fragments are not exposed).
- 🧰 **Normalization behavior** (stable ordering, stable error payload shape).

Fixtures MUST be:

- ✅ **synthetic** (non-identifying; non-realistic for restricted knowledge),
- ✅ **deterministic** (stable IDs, stable ordering, stable timestamps where used),
- ✅ **redacted-by-construction** (no raw precision, no payload dumps),
- ✅ **small and reviewable** (diff-friendly).

Fixtures MUST NOT include:

- coordinate-like values (even “fake but plausible”),
- GeoJSON/WKT payloads or `"coordinates"` dumps,
- real names, addresses, phone numbers, emails,
- tokens, secrets, credentials, or production URLs.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 assertions/
                    └── 📁 __tests__/
                        └── 📁 fixtures/
                            ├── 📄 README.md                           — This guide (fixture rules + safety contract)
                            │
                            ├── 🧾 fixture_manifest.json                 — Optional: fixture index + checksums
                            │
                            ├── 📁 cases/                                — Canonical “case” inputs for assertion tests
                            │   ├── 🧾 care_tier_cases.json               — CARE tier label + routing scenarios
                            │   ├── 🧾 sovereignty_masking_cases.json     — Masked/restricted state scenarios
                            │   ├── 🧾 provenance_surface_cases.json      — Evidence/provenance ID presence scenarios
                            │   └── 🧾 leak_pattern_cases.json            — Synthetic “should block / should pass” strings
                            │
                            ├── 📁 inputs/                               — Pre-normalized input bundles
                            │   ├── 🧾 ui_text_samples.json               — DOM-visible text samples (redacted)
                            │   ├── 🧾 console_samples.json               — Console message samples (redacted)
                            │   └── 🧾 network_summary_samples.json       — Response summaries (no raw payloads)
                            │
                            ├── 📁 expected/                             — Expected structured outputs (stable + safe)
                            │   ├── 🧾 expected_results.json              — Per-case expected result summaries
                            │   └── 🧾 expected_rule_ids.json             — Allowed rule IDs and severity expectations
                            │
                            └── 📁 allowlists/                           — Safe placeholders only (no realistic examples)
                                └── 🧾 safe_placeholders.json            — Approved placeholder tokens for tests
~~~

Notes:
- Filenames represent a **canonical target layout**. If your repo uses different names, preserve the structure and intent.
- Keep fixtures **close to the tests** that consume them, and keep them **small enough to review in a diff**.

---

## 🧭 Context

### Fixture design principles

Fixtures SHOULD:

- focus on **high-signal assertions** (what must be true to remain safe),
- include only **the minimum fields** required for the assertion under test,
- use **stable deterministic ordering** (sorted arrays; stable object keys),
- prefer **IDs and placeholders** over long strings.

Fixtures SHOULD NOT:

- mimic real historical events with plausible detail,
- embed long narratives (use short functional strings),
- contain “example lat/long values” for convenience.

### Deterministic identifiers (recommended)

Use stable identifiers within fixtures:

- `case_id`: deterministic string (e.g., `care_tier_b_badge_visible`)
- `scenario_id`: deterministic string (e.g., `masked_required`)
- `rule_id`: deterministic string (e.g., `geojson_coordinates_key`)

If the test requires timestamps:
- prefer fixed timestamps (e.g., `2020-01-01T00:00:00Z`),
- do not use runtime `Date.now()` values inside fixtures.

### Redaction contract (mandatory)

If fixtures include snippets that resemble sensitive content, they MUST be explicitly redacted using placeholders:

- `COORDINATE_REDACTED`
- `BBOX_REDACTED`
- `GEOMETRY_REDACTED`
- `H3_CELL_REDACTED`
- `PAYLOAD_REDACTED`
- `HASH_SHA256_REDACTED`

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load fixture cases"] --> B["Run assertion helper"]
  B --> C["Normalize (order, whitespace, volatile fields)"]
  C --> D["Apply allowlists and redaction checks"]
  D --> E["Compare to expected results / rule IDs"]
  E --> F["Pass or fail (safe diagnostics only)"]
~~~

Interpretation:
- Fixtures are the stable input layer that makes governance assertion tests deterministic and safe to review.

---

## 🧪 Validation & CI/CD

Fixtures are CI-scanned and CI-validated.

Fixtures MUST pass:
- ✅ JSON parse validation (or YAML parse validation if used)
- ✅ schema validation (when a fixture schema exists)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance safety checks (no precision-leak patterns)

### Review rules for fixture changes

Treat fixture edits as governance-sensitive:

- changes MUST be diff-reviewable,
- avoid adding volume; prefer adding targeted cases,
- do not add “convenience examples” that resemble real data.

If a fixture violates policy:
- remove it immediately,
- quarantine dependent tests until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 📦 Data & Metadata

### Case file model (recommended)

A case file SHOULD store an array of cases with a stable shape:

~~~json
{
  "schema_version": "v11.2.6",
  "cases": [
    {
      "case_id": "care_tier_b_badge_visible",
      "input": {
        "ui_text": ["CARE Tier: Tier B", "SOVEREIGNTY_FLAG_VISIBLE"],
        "page": "FocusMode",
        "selectors": ["data-testid=care-badge"]
      },
      "expect": {
        "pass": true,
        "rule_ids_triggered": [],
        "care_tier": "Tier B"
      },
      "tags": ["@governance", "@unit"]
    }
  ]
}
~~~

### Allowlist model (safe placeholders only)

Allowlists MUST contain placeholders only—no realistic coordinate examples.

~~~json
{
  "schema_version": "v11.2.6",
  "placeholders": [
    "COORDINATE_REDACTED",
    "BBOX_REDACTED",
    "GEOMETRY_REDACTED",
    "H3_CELL_REDACTED",
    "HASH_SHA256_REDACTED",
    "PAYLOAD_REDACTED"
  ]
}
~~~

### Fixture manifest (optional but recommended)

If you maintain a manifest, keep it checksum-only:

~~~json
{
  "schema_version": "v11.2.6",
  "fixtures": [
    { "file": "cases/care_tier_cases.json", "sha256": "<sha256>" },
    { "file": "cases/sovereignty_masking_cases.json", "sha256": "<sha256>" }
  ]
}
~~~

---

## ⚖ FAIR+CARE & Governance

Fixtures exist to uphold non-negotiable constraints:

- **Authority to Control**: fixtures must not encode precision or restricted inference material.
- **Responsibility**: tests must validate safe behavior even during refactors.
- **Ethics**: synthetic text must avoid harmful framing and avoid implying genealogy/sacred knowledge.
- **Collective Benefit**: deterministic governance tests prevent regressions that could cause public harm.

If you need a fixture that *resembles* restricted content to test redaction:
- represent it only as placeholders (`…REDACTED…`),
- never store the raw form (even if “fake”).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance assertion fixtures guide aligned to KFM‑MDP v11.2.6 (synthetic-only, deterministic inputs, strict redaction contract). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

