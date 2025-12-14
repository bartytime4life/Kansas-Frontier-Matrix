---
title: "🧾 Kansas Frontier Matrix — Governance API Mock Endpoints (E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/api_mocks/endpoints/README.md"

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
intent: "tests-e2e-web-app-regression-governance-fixtures-api-mocks-endpoints"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-fixtures-api-mocks-endpoints-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:api-mocks:endpoints:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/api_mocks/endpoints/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/api_mocks/endpoints/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Governance API Mock Endpoints (E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/api_mocks/endpoints/README.md`

**Purpose**  
Define the **endpoint-shaped API mock fixtures** used by governance E2E regression suites to simulate:
- CARE tier routing,
- sovereignty flags + masking modes,
- restricted/blocked states,
- provenance reference surfaces (IDs/hashes only),

using **synthetic, deterministic, precision-safe** payloads.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Type-Endpoint%20Mocks-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-No%20Sensitive%20Precision-red" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ API Mocks](../README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **endpoint-shaped stubs**. Each file should look like “one API response” the UI expects, but in a governed, minimized form.

Endpoint mocks exist to:

- ✅ keep governance suites **deterministic** (no backend dependency),
- ✅ provide stable fixtures for **interception** (Playwright/Cypress/MSW),
- ✅ simulate **policy-critical states** without real-world harm:
  - masked vs. unmasked presentation modes,
  - restricted/blocked flows,
  - provenance surfaces that remain non-empty,
- ✅ enable strict “no-leak” scanning (precision patterns must not appear).

**Non-goals**
- These mocks are not a full clone of production DTOs.
- These mocks must not contain realistic coordinates, real people, or restricted cultural information.
- These mocks should not grow into a parallel backend implementation.

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
                        ├── 📄 README.md                         — API mock layer overview
                        ├── 🧾 mock_registry.json                 — Endpoint key → file mapping
                        │
                        └── 📁 endpoints/
                            ├── 📄 README.md                      — This guide (endpoint mock conventions)
                            │
                            ├── 🧾 governance_status.json          — Governed status summary (safe fields)
                            ├── 🧾 care_classification.json        — CARE tier + routing behavior
                            ├── 🧾 sovereignty_flags.json          — Sovereignty flags + masking mode
                            ├── 🧾 provenance_refs.json            — IDs/hashes only (no payload dumps)
                            ├── 🧾 narrative_surface.json          — Minimal narrative fields (synthetic)
                            └── 🧾 errors_restricted_block.json    — Restricted-state error (safe UX)
~~~

Notes:
- File names SHOULD be stable and descriptive.
- If your runner requires different names, keep a stable mapping in `mock_registry.json`.

---

## 🧭 Context

### Endpoint mock contract (what “endpoint-shaped” means)

Each endpoint mock SHOULD define:

- **request identity** (method + path),
- **response identity** (HTTP status),
- **body** (minimal fields needed by the UI),
- optional **headers** (only when required for routing/UI behavior),
- **schema_version** so fixtures remain compatible across refactors.

### Safety constraints (non-negotiable)

Endpoint mocks MUST NOT include:

- coordinate-like pairs (lat/long patterns),
- high-precision bboxes,
- GeoJSON/WKT geometry dumps,
- realistic site names tied to restricted knowledge,
- any PII, secrets, or production tokens.

If an endpoint mock needs to represent “location exists”:
- prefer `geometry: null`,
- prefer generalized placeholders (e.g., `H3_REDACTED`),
- let UI show masking badges rather than raw numbers.

### Determinism constraints (non-negotiable)

Endpoint mocks MUST:

- use stable IDs (string keys or pinned UUIDs),
- use stable ordering for arrays,
- avoid runtime-generated timestamps unless injected by a deterministic clock in the runner.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Runner intercepts request"] --> B["Resolve endpoint key (registry)"]
  B --> C["Load endpoints/*.json"]
  C --> D["Fulfill network route"]
  D --> E["UI renders governed state"]
  E --> F["Leak checks + assertions"]
~~~

Interpretation:
- The endpoint mocks are a deterministic input layer that enables stable governance regression coverage.

---

## 🧠 Story Node & Focus Mode Integration

Endpoint mocks MAY be used to drive:

- governance overlays visible from **Story Node v3** views,
- governed content panels in **Focus Mode v3**.

Minimum integration invariants:
- governance badges remain consistent across navigation,
- restricted/blocked states persist across panel switching,
- provenance surfaces render as **IDs/hashes only** (no expanded payload dumps).

---

## 🧪 Validation & CI/CD

Endpoint mocks MUST pass:

- ✅ JSON parse validation
- ✅ secret scan
- ✅ PII scan (best-effort)
- ✅ governance fixture lint rules
- ✅ leak-check compatibility (no precision patterns)

Recommended fixture lint rules for this folder:
- forbid keys commonly used for geometry payloads unless explicitly null:
  - `coordinates`, `geometry`, `bbox`, `wkt`, `geojson`
- forbid numeric patterns resembling lat/long or bboxes
- require `schema_version: v11.2.6` in each file (or enforce via registry)

---

## 📦 Data & Metadata

### Canonical endpoint mock shape (recommended)

~~~json
{
  "schema_version": "v11.2.6",
  "request": {
    "method": "GET",
    "path": "/api/governance/status"
  },
  "response": {
    "http_status": 200,
    "headers": {
      "content-type": "application/json"
    },
    "body": {
      "mode": "governed",
      "restrictions": {
        "blocked": false,
        "redacted": true
      }
    }
  }
}
~~~

### Restricted-state error mock (recommended)

Use safe messaging and stable codes (no raw payload dumps).

~~~json
{
  "schema_version": "v11.2.6",
  "request": {
    "method": "GET",
    "path": "/api/focus-mode/entity"
  },
  "response": {
    "http_status": 403,
    "body": {
      "error_code": "GOV_RESTRICTED",
      "ui_safe_message": "This content is restricted under governance policy.",
      "care_tier": "Tier A",
      "sovereignty_flagged": true
    }
  }
}
~~~

### Provenance refs mock (IDs/hashes only)

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

These endpoint mocks are test fixtures, not real datasets:

- **DCAT**: treat files as test artifact distributions (`mediaType: application/json`).
- **STAC**: if indexed, use non-spatial STAC items:
  - `geometry: null`
  - timestamp from the E2E run (not fixture content)
- **PROV-O**:
  - fixture files are `prov:Entity`,
  - an E2E execution is `prov:Activity`,
  - CI runner is `prov:Agent`.

---

## 🧱 Architecture

### Recommended composition pattern

- Keep endpoint mocks minimal and “single responsibility.”
- Use scenario bundles (outside this folder) to compose multiple endpoints into a full UI state.
- Keep assertions in test code, not in endpoint mocks.

This prevents:
- brittle UI coupling,
- duplication,
- “fixture bloat.”

---

## ⚖ FAIR+CARE & Governance

Endpoint mocks must uphold the same posture as governed production outputs:

- **Authority to Control**: never encode precision that could enable inference.
- **Responsibility**: minimize content and keep it auditable.
- **Ethics**: avoid harmful framing and avoid restricted knowledge simulation.
- **Collective Benefit**: ensure governance behavior is consistently testable.

If a mock violates policy:
- remove it immediately,
- update `mock_registry.json`,
- re-run governance suites and leak checks before merging.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial endpoint mocks guide aligned to KFM‑MDP v11.2.6 (endpoint-shaped stubs, determinism constraints, precision-safe governance simulation). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

