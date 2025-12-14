```markdown
---
title: "🧪 Kansas Frontier Matrix — Governance API Mocks (E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/api_mocks/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-api-mocks"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-api-mocks-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:api-mocks:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/api_mocks/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/api_mocks/README.md@v11.2.6"
---

<div align="center">

# 🧪 **Governance API Mocks (E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/api_mocks/README.md`

**Purpose**  
Define the **canonical API mock fixtures** used by governance regression E2E suites to provide:
- deterministic UI/API behavior (no external dependencies),
- governance-state simulation (CARE tiers, sovereignty flags, restricted routing),
- safe-by-construction payloads (synthetic, non-identifying, precision-safe).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Type-API%20Mocks-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Sensitive%20Precision-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Fixtures](../README.md) ·
[🕵️ Leak Checks](../../utils/leak_checks/README.md) ·
[🧭 E2E Guide](../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic API response stubs** used by governance E2E regression tests.

API mocks exist to:

- ✅ make tests **deterministic** (stable inputs, stable ordering, stable timestamps),
- ✅ remove reliance on **live networks** and external services,
- ✅ simulate governance decision paths **without** using real people, real places, or restricted knowledge,
- ✅ enable high-signal assertions for:
  - restricted/masked/blocked UI states,
  - provenance and evidence surfaces (IDs/hashes only),
  - policy enforcement in edge cases.

**Non-goals**
- API mocks are not an integration test of real backend behavior.
- API mocks are not a complete replica of production payloads.
- API mocks are not allowed to include any sensitive or realistic coordinate precision.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 api_mocks/
                        ├── 📄 README.md                         — This guide (rules + patterns)
                        │
                        ├── 🧾 mock_registry.json                 — Endpoint key → mock file mapping
                        │
                        ├── 📁 endpoints/                         — Canonical endpoint-shaped stubs (synthetic)
                        │   ├── 🧾 governance_status.json          — Governance status summary (safe fields only)
                        │   ├── 🧾 care_classification.json        — CARE tier + routing behavior (synthetic)
                        │   ├── 🧾 sovereignty_flags.json          — Sovereignty flags + masking mode (synthetic)
                        │   ├── 🧾 provenance_refs.json            — IDs/hashes only (no payload dumps)
                        │   └── 🧾 narrative_surface.json          — Minimal narrative fields (short, synthetic)
                        │
                        ├── 📁 scenarios/                          — Scenario bundles (optional)
                        │   ├── 🧾 governance_public_ok.json        — Public-safe path
                        │   ├── 🧾 governance_masked_required.json  — Masked/generalized path
                        │   └── 🧾 governance_restricted_block.json — Restricted/blocked path
                        │
                        └── 📁 schemas/                             — Optional: fixture schemas for validation
                            └── 🧾 api_mock.schema.json
~~~

Notes:
- The filenames above are a **canonical target layout**. Adjust names to match your runner (Playwright/Cypress/MSW), but keep:
  - a registry,
  - endpoint mocks,
  - optional scenario bundles,
  - optional schemas.

---

## 🧭 Context

### Where these mocks are used (common patterns)

Governance regression tests typically use one of these approaches:

- **Network interception** (recommended):
  - intercept `/api/**` requests,
  - fulfill with JSON from `api_mocks/`,
  - keep deterministic ordering and stable IDs.

- **In-memory mock server**:
  - start a local mock server in test mode,
  - serve scenario-selected responses from this folder.

### Mock design rules (determinism + safety)

API mocks MUST:

- be **synthetic** and **non-identifying**,
- use stable IDs (string keys, or pinned UUIDs),
- avoid non-deterministic fields (no “now” timestamps unless injected),
- omit or null out geometry fields by default,
- never include realistic coordinate precision.

API mocks SHOULD:

- include only fields needed for the UI under test,
- use short strings for narrative fields (functional, not story-like),
- separate “provenance refs” (IDs/hashes) from “display content.”

### Interaction with leak checks

Leak checks treat API mocks as **input sources** that must not cause precision leakage.

If a mock introduces a precision-like token:
- it will (and should) fail `@governance` suites,
- do not bypass via allowlists unless the token is an explicit placeholder.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["E2E test selects scenario"] --> B["Load mock_registry.json"]
  B --> C["Intercept API route (runner)"]
  C --> D["Fulfill with api_mocks JSON"]
  D --> E["UI renders governance state"]
  E --> F["Leak checks scan UI surfaces"]
  F --> G["Assertions validate routing and masking"]
~~~

Interpretation:
- API mocks are a controlled input layer that makes governance regressions reproducible and policy-safe.

---

## 🧪 Validation & CI/CD

API mock fixtures MUST pass:

- ✅ JSON parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance fixture lint checks
- ✅ schema validation (if `schemas/api_mock.schema.json` is present)

Recommended CI checks for this folder:

- forbid fields that look like:
  - raw lat/long pairs,
  - bboxes with numeric precision,
  - GeoJSON/WKT geometry dumps,
- enforce stable ordering (formatter in CI),
- enforce minimal schema version tagging (`schema_version: v11.2.6`).

---

## 📦 Data & Metadata

### Registry file (recommended minimal shape)

The registry maps a stable key (endpoint or logical name) to a mock file.

~~~json
{
  "schema_version": "v11.2.6",
  "mocks": {
    "GET:/api/governance/status": "endpoints/governance_status.json",
    "GET:/api/governance/care": "endpoints/care_classification.json",
    "GET:/api/governance/sovereignty": "endpoints/sovereignty_flags.json",
    "GET:/api/provenance/refs": "endpoints/provenance_refs.json"
  }
}
~~~

### Endpoint mock (example: governance status)

This is intentionally minimal and precision-safe.

~~~json
{
  "schema_version": "v11.2.6",
  "request": {
    "method": "GET",
    "path": "/api/governance/status"
  },
  "response": {
    "http_status": 200,
    "body": {
      "mode": "governed",
      "care_tier": "Tier B",
      "sovereignty": {
        "flagged": true,
        "masking_required": true,
        "masking_level": "H3_REDACTED"
      },
      "restrictions": {
        "blocked": false,
        "redacted": true
      }
    }
  }
}
~~~

### Provenance refs (IDs/hashes only)

Do not dump documents or full payloads.

~~~json
{
  "schema_version": "v11.2.6",
  "provenance_refs": {
    "dataset_ids": ["stac:synthetic/dataset_001"],
    "experiment_ids": ["mcp/experiments/SYNTH-EXP-001.md"],
    "model_card_paths": ["mcp/model_cards/synthetic_model_v1.md"],
    "hashes": {
      "bundle_sha256": "<sha256>"
    }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

API mocks are test fixtures (not real datasets):

- **DCAT**: mock files are test distributions (`mediaType: application/json`).
- **STAC**: if represented for indexing, use `geometry: null` and attach JSON assets.
- **PROV-O**:
  - each mock file is a `prov:Entity`,
  - an E2E run is a `prov:Activity`,
  - CI runner + maintainers are `prov:Agent`.

Keep all mappings synthetic and non-sensitive.

---

## 🧱 Architecture

### Recommended layering

Keep mocks layered so the suite remains maintainable:

- `endpoints/` holds “single responsibility” endpoint-shaped stubs,
- `scenarios/` composes endpoint mocks into an overall story for a test,
- shared assertions should consume **scenario IDs**, not raw payloads.

### Anti-patterns (avoid)

- storing full production payload dumps as “mocks,”
- embedding real-ish coordinate patterns “because it’s just a test,”
- coupling tests to unstable UI strings instead of governance flags and IDs,
- letting mocks drift without a registry and schema version tags.

---

## ⚖ FAIR+CARE & Governance

API mocks must uphold the same governance posture as production:

- **Authority to Control**: never include precision leakage that could enable inference.
- **Responsibility**: keep mocks minimal, auditable, and deterministic.
- **Ethics**: avoid harmful framing, genealogy implications, or culturally sensitive details.
- **Collective Benefit**: ensure governance features are consistently testable and safe.

If an API mock is found to violate policy:
- remove it immediately,
- invalidate dependent scenarios until corrected,
- route review per governance process.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance API mocks guide aligned to KFM‑MDP v11.2.6 (deterministic interception patterns, precision-safe stubs, CI validation expectations). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
```
