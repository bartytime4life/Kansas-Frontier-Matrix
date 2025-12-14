---
title: "🧾 Kansas Frontier Matrix — API Mock Schemas (Governance E2E Fixtures) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/fixtures/api_mocks/schemas/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Schema Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-fixtures-api-mocks-schemas"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-api-mocks-schemas-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:fixtures:api-mocks:schemas:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/fixtures/api_mocks/schemas/README.md"
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
  - "tests/e2e/web-app/regression/governance/fixtures/api_mocks/schemas/README.md@v11.2.6"
---

<div align="center">

# 🧾 **API Mock Schemas (Governance E2E Fixtures) (v11 LTS)**
`tests/e2e/web-app/regression/governance/fixtures/api_mocks/schemas/README.md`

**Purpose**  
Define the **canonical schema layer** for Governance E2E **API mock fixtures**.  
Schemas in this folder ensure mock responses are:
- **deterministic** (stable shapes),
- **governance-safe** (no sensitive precision fields),
- **CI-validated** (schema-lint + secret/PII scans),
- **compatible** with regression specs and shared assertions.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Layer-API%20Mocks%20Schemas-orange" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ API Mocks](../README.md) ·
[⬅️ Governance Fixtures](../../README.md) ·
[🧭 E2E Guide](../../../../../../README.md)

</div>

---

## 📘 Overview

This folder contains **schemas used to validate API mock fixtures** that drive governance regression scenarios.

Why this exists:
- Mock responses are high leverage: if their shape drifts, E2E tests can become flaky or meaningless.
- Governance regressions must be **detectable** without relying on real data.
- The schema layer enforces a minimal “contract” for:
  - endpoint payload shape,
  - governance flags and badges,
  - safe provenance references (IDs/hashes),
  - explicit prohibition of sensitive-precision fields.

### Normative rules (MUST)

Schemas in this folder MUST enforce:

- **No secrets / no PII** in mock payloads.
- **No sensitive precision** fields (no realistic coordinates, no raw GeoJSON/WKT dumps).
- **Stable, testable governance fields** (e.g., restricted/masked states are explicit).
- **Deterministic identity** (scenario/entity IDs are stable strings; ordering is stable where relevant).

Schemas in this folder MUST NOT:
- encode real-world coordinates as “examples,”
- allow open-ended “anything goes” objects for governed surfaces unless narrowly scoped,
- require external network lookups to validate.

---

## 🗂️ Directory Layout

This folder is designed to be discoverable and CI-friendly.

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                └── 📁 fixtures/
                    └── 📁 api_mocks/
                        └── 📁 schemas/
                            ├── 📄 README.md                          — This guide (schema contract + rules)
                            │
                            ├── 🧾 schema_registry.json                — Optional: schema ID → file mapping
                            │
                            ├── 🧾 common.schema.json                  — Shared types (IDs, timestamps, redaction markers)
                            ├── 🧾 governance_envelope.schema.json      — Required governance wrapper (care/sovereignty/restricted)
                            ├── 🧾 provenance_refs.schema.json          — IDs/hashes-only provenance references
                            │
                            ├── 🧾 endpoint_storynode.schema.json       — Mock shape for Story Node endpoints (if used in governance suites)
                            ├── 🧾 endpoint_focusmode.schema.json       — Mock shape for Focus Mode endpoints (if used in governance suites)
                            └── 🧾 endpoint_errors.schema.json          — Mock error payload contract (redacted, safe, deterministic)
~~~

Notes:
- Filenames above are the **canonical target layout** for this folder.
- If the repo uses different names, preserve the intent:
  - **common** types,
  - **governance envelope**,
  - **provenance refs**,
  - **endpoint-specific** schemas.

---

## 🧭 Context

### What “API mock schemas” protect

These schemas primarily protect:
- regression reliability (fixtures remain compatible with page objects and assertions),
- governance posture (fixtures cannot “accidentally” contain leak-like content),
- safe reporting (fixtures validate without requiring payload dumps).

### What belongs in mock payloads (safe-by-design)

Mock payloads SHOULD:
- include governance flags explicitly (`restricted`, `masking_required`, `care_tier`),
- include provenance references as **IDs/hashes only**,
- include UI-driving fields only (minimal required to render).

Mock payloads SHOULD NOT:
- include free-form dumps of upstream records,
- embed coordinates or geometry beyond policy-safe placeholders,
- include large narratives (use short synthetic text only).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Load api_mocks/*.json"] --> B["Validate against schemas"]
  B -->|pass| C["Run E2E scenario"]
  B -->|fail| D["Block merge and report schema errors"]
~~~

Interpretation:
- The schema layer is a **front gate**: it blocks drift before E2E spends time booting browsers.

---

## 🧪 Validation & CI/CD

### Required CI checks (recommended minimum)

- `schema-lint` for JSON Schema validity
- fixture validation (each `api_mocks/**/*.json` validates against the correct schema)
- `secret-scan` and `pii-scan` (best-effort)
- governance leak checks (separate layer) SHOULD still run even if schemas pass

### Local validation pattern (example)

~~~bash
# Example intent (tooling may differ):
# - Validate schemas themselves
# - Validate fixture payloads against endpoint schemas

make test:schemas
make test:e2e-fixtures-validate
~~~

### Failure policy

A schema validation failure is:
- **merge-blocking** for governed suites,
- **not retryable** by default (it is deterministic).

---

## 📦 Data & Metadata

### schema_registry.json (optional but recommended)

If multiple endpoints exist, a registry prevents ambiguity and avoids hardcoding mapping in test code.

~~~json
{
  "schema_version": "v11.2.6",
  "schemas": {
    "common": "common.schema.json",
    "governance_envelope": "governance_envelope.schema.json",
    "provenance_refs": "provenance_refs.schema.json",
    "endpoints": {
      "GET:/api/governance/storynode": "endpoint_storynode.schema.json",
      "GET:/api/governance/focusmode": "endpoint_focusmode.schema.json",
      "ERROR:default": "endpoint_errors.schema.json"
    }
  }
}
~~~

### Governance envelope (recommended minimal contract)

This schema is the “must be present” wrapper for governed UI surfaces.

~~~json
{
  "$id": "kfm://schemas/governance_envelope.schema.json",
  "type": "object",
  "required": ["governance"],
  "properties": {
    "governance": {
      "type": "object",
      "required": ["care_tier", "restricted", "masking_required"],
      "properties": {
        "care_tier": { "type": "string", "enum": ["Tier A", "Tier B", "Tier C"] },
        "restricted": { "type": "boolean" },
        "masking_required": { "type": "boolean" },
        "sovereignty_flag": { "type": "boolean" }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": true
}
~~~

### Prohibited precision fields (recommended approach)

Schemas SHOULD explicitly disallow common leakage keys on governed payloads. Typical examples include:

- `coordinates`
- `geometry`
- `bbox`
- `lat`, `lng`, `lon`, `longitude`, `latitude`

Implementation options:
- denylist via `not` + `required` patterns (for strict payloads),
- structured “redacted placeholder only” for fields that must exist in UI models.

Example snippet (illustrative):

~~~json
{
  "not": {
    "anyOf": [
      { "required": ["coordinates"] },
      { "required": ["geometry"] },
      { "required": ["bbox"] },
      { "required": ["lat"] },
      { "required": ["lng"] },
      { "required": ["lon"] },
      { "required": ["latitude"] },
      { "required": ["longitude"] }
    ]
  }
}
~~~

---

## 🧱 Architecture

### How schemas connect to fixtures and tests (recommended)

- Endpoint mocks live in: `../endpoints/` (or equivalent)
- Schemas live in: `./`
- Specs:
  - select a scenario,
  - load endpoint mocks,
  - validate mocks against schemas (preflight),
  - run UI steps and assertions.

This separation prevents:
- fixtures silently drifting,
- specs compensating for invalid payload shapes,
- governance regressions being hidden by “loose mocks.”

---

## ⚖ FAIR+CARE & Governance

These schemas enforce governance-by-construction:

- **Authority to Control**: prevents fixture-level introduction of precision that would enable harmful inference.
- **Responsibility**: ensures governed UI flows always include explicit governance context fields.
- **Ethics**: ensures test text remains synthetic and non-identifying.
- **Collective Benefit**: enables robust QA without access to restricted datasets.

If a schema change expands what mocks can contain:
- treat it as a governance posture change,
- require careful review (same seriousness as code changes in governed surfaces).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial API mock schema guide for Governance E2E fixtures; standardized governance envelope + provenance refs; reinforced no-precision and no-secrets constraints. |

<div align="center">

[🏛️ Governance Charter](../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

