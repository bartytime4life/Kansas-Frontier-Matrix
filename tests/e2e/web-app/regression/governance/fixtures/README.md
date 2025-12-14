---
title: "🧱 Kansas Frontier Matrix — Governance Regression Fixtures (E2E) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/README.md@v11.2.6"
---

<div align="center">

# 🧱 **Governance Regression Fixtures (E2E) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/README.md`

**Purpose**  
Define the **canonical synthetic fixture set** used by governance regression E2E suites to validate:
- CARE tier routing and UI badges,
- sovereignty masking invariants,
- restricted-state behavior (redacted/masked/blocked),
- “no leak” guarantees for governed surfaces.

These fixtures are **synthetic**, **deterministic**, and **sovereignty-safe** by construction.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Type-Fixtures-informational" />
<img src="https://img.shields.io/badge/Surface-Governance%20Regression-blueviolet" />
<img src="https://img.shields.io/badge/Policy-Synthetic%20Only-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Regression](../README.md) ·
[🧰 Governance Utils](../utils/README.md) ·
[🧭 E2E Guide](../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic, deterministic fixtures** for governance regression tests.

Fixtures here exist to:

- 🛡️ simulate governance states safely (CARE tiers, sovereignty flags, restricted access),
- 🧪 drive E2E assertions without embedding real individuals, real addresses, or real sensitive sites,
- 🧾 provide stable provenance identifiers (IDs/hashes only; no full payload dumps),
- 🕵️ support leak checks by providing known-safe placeholders and known-block patterns.

Fixtures in this folder MUST be:

- **Synthetic**: no real people, no real site coordinates, no restricted cultural content.
- **Deterministic**: stable IDs, stable ordering, stable timestamps (where required).
- **Redacted-by-construction**: placeholders over “fake but plausible” precision.

Fixtures in this folder MUST NOT:

- include coordinate-like values (even if “fake”),
- include raw geometry payloads (GeoJSON/WKT) or `"coordinates"` dumps,
- include production tokens, secrets, credentials, or environment-specific URLs,
- require external network access as a dependency.

---

## 🗂️ Directory Layout

This layout favors **scenario discovery**, **runner-friendly loading**, and **governance intent clarity**.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                ├── 📄 README.md                               — Governance regression overview
                │
                ├── 📁 fixtures/
                │   ├── 📄 README.md                           — This guide
                │   ├── 🧾 fixture_manifest.json               — Optional: file list + checksums
                │   ├── 🧾 scenario_registry.json              — Scenario ID → bundle mapping
                │   │
                │   ├── 📁 scenarios/                          — Scenario bundles (synthetic governance states)
                │   │   ├── 🧾 care_tier_a_restricted.json      — Restricted state simulation (redacted/blocked UX)
                │   │   ├── 🧾 care_tier_b_masked.json          — Masking/generalization simulation (H3-safe)
                │   │   └── 🧾 care_tier_c_public.json          — Fully public scenario (no restrictions)
                │   │
                │   ├── 📁 api_mocks/                          — Optional API stubs (if network interception is used)
                │   │   ├── 🧾 governance_badges.json
                │   │   ├── 🧾 sovereignty_flags.json
                │   │   └── 🧾 provenance_surface.json
                │   │
                │   ├── 📁 expected/                           — High-signal expected outcomes (counts, flags, badges)
                │   │   ├── 🧾 expected_public.json
                │   │   ├── 🧾 expected_masked.json
                │   │   └── 🧾 expected_restricted.json
                │   │
                │   ├── 📁 allowlists/                         — Safe placeholders only (never realistic examples)
                │   │   └── 🧾 safe_placeholders.json
                │   │
                │   └── 📁 provenance/                         — IDs/hashes only; no payload dumps
                │       ├── 🧾 prov_refs_public.json
                │       ├── 🧾 prov_refs_masked.json
                │       └── 🧾 prov_refs_restricted.json
                │
                └── 📁 utils/
                    ├── 📄 README.md
                    └── 📁 leak_checks/
                        └── 📄 README.md
~~~

Notes:
- Filenames above represent the **canonical target layout** for governance fixtures.
- If your implementation uses different naming or file extensions, preserve the **structure and intent**.

---

## 🧭 Context

### Fixture design principles (governance-first)

Fixtures SHOULD:

- use short functional strings (avoid long narratives),
- prefer deterministic identifiers over text bodies,
- simulate policy states with explicit flags (e.g., `masked`, `restricted`, `care_tier`),
- keep diffs small (reviewable, auditable).

Fixtures SHOULD NOT:

- reproduce plausible restricted knowledge “just for testing,”
- embed realistic coordinates or bboxes,
- include full network payloads.

### Determinism contract

Use stable identifiers in fixtures:

- `scenario_id`: stable string key (e.g., `care_tier_b_masked`)
- `entity_id`: stable synthetic ID (UUID allowed if pinned)
- `run_seed`: numeric seed (only if generation is required)

Time handling:

- prefer fixed timestamps (e.g., `2020-01-01T00:00:00Z`)
- if “now” is required, it MUST be injected by the test runner (deterministic clock), not encoded ad hoc.

### Redaction contract (mandatory placeholders)

If the tests need to validate “no leak,” use placeholders:

- `COORDINATE_REDACTED`
- `BBOX_REDACTED`
- `GEOMETRY_REDACTED`
- `H3_CELL_REDACTED`
- `PAYLOAD_REDACTED`
- `HASH_SHA256_REDACTED`

Placeholders MUST be non-realistic and non-reconstructible.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Select scenario_id"] --> B["Load scenario bundle"]
  B --> C["Optional API interception (api_mocks)"]
  C --> D["Render governed UI surfaces"]
  D --> E["Assert badges and routing (expected)"]
  E --> F["Run leak checks (block on precision)"]
  F --> G["Write artifacts and telemetry"]
~~~

Interpretation:
- Fixtures supply deterministic inputs; governance utilities enforce invariants; CI blocks unsafe changes.

---

## 🧪 Validation & CI/CD

Governance fixtures are CI-validated.

Fixtures MUST pass:

- ✅ parse validation (JSON/YAML)
- ✅ schema validation (when fixture schemas exist)
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ sovereignty safety checks (no precision-like patterns)

Recommended fixture lint rules:

- stable key ordering (formatter enforced in CI),
- forbid `"coordinates"` keys unless value is `null` or a `...REDACTED...` placeholder,
- forbid lat/long-like patterns anywhere in fixture strings,
- forbid large embedded payload blobs (prefer summaries + hashes).

If a fixture violates policy:

- remove it immediately,
- quarantine dependent tests until corrected,
- route review to the relevant working group and FAIR+CARE Council.

---

## 📦 Data & Metadata

### Scenario registry (canonical shape)

Scenario registry maps scenario IDs to bundle + expected + provenance fragments.

~~~json
{
  "schema_version": "v11.2.6",
  "scenarios": {
    "care_tier_c_public": {
      "bundle": "scenarios/care_tier_c_public.json",
      "expected": "expected/expected_public.json",
      "provenance": "provenance/prov_refs_public.json",
      "tags": ["@regression"]
    },
    "care_tier_b_masked": {
      "bundle": "scenarios/care_tier_b_masked.json",
      "expected": "expected/expected_masked.json",
      "provenance": "provenance/prov_refs_masked.json",
      "tags": ["@regression", "@governance"]
    },
    "care_tier_a_restricted": {
      "bundle": "scenarios/care_tier_a_restricted.json",
      "expected": "expected/expected_restricted.json",
      "provenance": "provenance/prov_refs_restricted.json",
      "tags": ["@regression", "@governance"]
    }
  }
}
~~~

### Expected files (what belongs here)

Expected files MUST contain only **high-signal assertions**, such as:

- expected CARE tier label,
- whether sovereignty flag is visible,
- whether restricted-state UI is redacted/masked/blocked,
- minimum evidence/provenance chip counts,
- explicit assertion that raw precision is not visible.

~~~json
{
  "scenario_id": "care_tier_b_masked",
  "expect": {
    "care_tier": "Tier B",
    "sovereignty_flag_visible": true,
    "restricted_state": "masked",
    "raw_precision_visible": false,
    "evidence_chip_min_count": 1
  }
}
~~~

### Provenance fragments (IDs/hashes only)

Provenance fragments SHOULD include only:

- stable identifiers (dataset IDs, experiment IDs, model card IDs),
- hashes (sha256 placeholders allowed),
- reference anchors.

Do not include full payloads.

---

## 🌐 STAC, DCAT & PROV Alignment

Governance fixtures are **test data artifacts**, not real datasets.

- **DCAT**: fixture bundles can be treated as test distributions (`mediaType: application/json`).
- **STAC**: if represented as a STAC item, use `geometry: null` and attach assets (bundle, expected, provenance).
- **PROV-O**:
  - scenario bundles are `prov:Entity`,
  - an E2E run is a `prov:Activity`,
  - CI runner and maintainers are `prov:Agent`.

All representations must remain synthetic and safe to publish.

---

## ⚖ FAIR+CARE & Governance

Fixtures must uphold non-negotiable constraints:

- **Authority to Control**: do not include precision that could enable inference.
- **Responsibility**: validate masking and restricted-state invariants against regressions.
- **Ethics**: avoid harmful framing, even in synthetic test strings.
- **Collective Benefit**: keep governed surfaces consistently safe for all users.

If you need additional test coverage:
- add a new scenario with placeholders (not plausible “fake” data),
- add expected assertions and provenance IDs/hashes,
- update the scenario registry.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance regression fixtures guide aligned to KFM‑MDP v11.2.6 (synthetic-only, deterministic, leak-safe). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

