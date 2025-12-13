---
title: "🧾 Kansas Frontier Matrix — Focus Mode v3 API Mocks (E2E Regression) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/focus-mode/fixtures/api_mocks/README.md"

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
intent: "tests-e2e-web-app-regression-focus-mode-api-mocks"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-focus-mode-api-mocks-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:focus-mode:fixtures:api-mocks:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/focus-mode/fixtures/api_mocks/README.md"
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
  - "tests/e2e/web-app/regression/focus-mode/fixtures/api_mocks/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Focus Mode v3 API Mocks (E2E Regression) (v11 LTS)**
`tests/e2e/web-app/regression/focus-mode/fixtures/api_mocks/README.md`

**Purpose**  
Define the **canonical API mock payloads** used by Focus Mode v3 regression E2E tests.  
API mocks allow UI flows to be tested **without live services** while preserving **governance behavior**, **determinism**, and **sovereignty-safe** outputs.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/E2E-API%20Mocks-informational" />
<img src="https://img.shields.io/badge/Surface-Focus%20Mode%20v3-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Fixtures](../README.md) · [🧾 Scenario Registry](../scenario_registry.json) · [🧠 Focus Mode Specs](../../specs/README.md)

</div>

---

## 📘 Overview

This folder contains **synthetic, deterministic API response payloads** used for Focus Mode v3 regression testing.

API mocks are used when:
- the E2E runner intercepts network calls (Playwright route handlers / Cypress intercepts),
- the stack is running in “test mode” and requests are served from fixtures,
- tests must validate UI rendering and governance behavior without requiring:
  - Neo4j,
  - external catalogs,
  - full API stack availability.

API mocks MUST:
- match the expected **API DTO shape** for the route being mocked,
- remain **synthetic** and **non-identifying**,
- enforce governance-safe behaviors:
  - masking/generalization where required,
  - restricted states produce safe UI responses.

API mocks MUST NOT:
- include real dataset payloads,
- include real coordinates or plausible restricted site geometry,
- include secrets, tokens, or environment identifiers.

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 focus-mode/
                └── 📁 fixtures/
                    └── 📁 api_mocks/
                        ├── 📄 README.md                     — This guide
                        │
                        ├── 🧾 focus_mode_entity.json         — Mock for entity resolution endpoint
                        ├── 🧾 focus_mode_panels.json         — Mock for 3-panel payload (Context/Timeline/Map)
                        ├── 🧾 focus_mode_provenance.json     — Mock for evidence/provenance payload
                        ├── 🧾 focus_mode_governance.json     — Mock for CARE + sovereignty flags
                        └── 🧾 focus_mode_errors.json         — Mock error modes (restricted/redacted/not-found)
~~~

Notes:
- Filenames above are the **canonical targets**; align to your actual route map if it differs.
- If mocks are scenario-specific, store them under `api_mocks/<scenario_id>/...` and keep this README as the umbrella ruleset.

---

## 🧭 Context

### What “API mock” means in this folder
An API mock is a fixture payload that replaces an HTTP response in the test stack.

This enables deterministic tests by:
- eliminating dependency on network timing and external services,
- controlling response ordering and content,
- making governance and masking states explicit and repeatable.

### Determinism contract
API mocks MUST:
- be stable across runs,
- preserve stable ordering (arrays sorted where UI relies on order),
- use fixed timestamps or a deterministic clock injection pattern,
- avoid runtime-generated random identifiers unless seeded and recorded.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Spec selects scenario_id"] --> B["Runner installs route intercepts"]
  B --> C["UI triggers API request"]
  C --> D["Intercept responds from api_mocks/*.json"]
  D --> E["UI renders panels + governance badges"]
  E --> F["Assertions validate masking, provenance, and UX"]
~~~

Interpretation:
- API mocks are the controlled boundary that let the UI be tested like “real,” without using real data.

---

## 🧠 Story Node & Focus Mode Integration

API mocks may simulate:
- an entity opened from a Story Node link,
- a direct Focus Mode route (entity id in URL),
- provenance chips that open an evidence drawer.

When simulating Story Node integration:
- never embed full story node payloads here (keep them in `scenarios/`),
- ensure identifiers remain consistent across:
  - entity payload,
  - panel payload,
  - provenance payload,
  - governance payload.

---

## 🧪 Validation & CI/CD

API mocks are governed artifacts and must pass CI scans.

Minimum checks:
- ✅ valid JSON
- ✅ schema validation (if a mock schema exists for the endpoint DTO)
- ✅ secret scan + PII scan
- ✅ sovereignty-safety checks (no coordinate leakage patterns)

Recommended checks:
- enforce `Content-Type` assumptions in runner (`application/json`),
- ensure error mocks cover:
  - restricted state,
  - not-found,
  - backend validation error,
  - “governance blocked” response.

---

## 📦 Data & Metadata

### Recommended mock payload anatomy
Keep payloads minimal but sufficient for UI:
- IDs (synthetic)
- Labels (synthetic)
- Panel data (short)
- Governance flags (explicit)
- Evidence/provenance references (IDs/hashes only)

Avoid:
- large narrative bodies,
- full text documents,
- full geometry dumps,
- any sensitive-like location attributes.

### Example mock snippet (shape only; simplified)
~~~json
{
  "entity_id": "ent_synthetic_001",
  "title": "Synthetic Entity Title",
  "panels": {
    "context": { "bullets": ["Synthetic fact A", "Synthetic fact B"] },
    "timeline": { "events": [{ "when": "2020-01-01", "label": "Synthetic event" }] },
    "map": { "geometry": null, "h3": ["872830828ffffff"] }
  },
  "governance": {
    "care_tier": "Tier B",
    "sovereignty_flag": true,
    "masking": { "enabled": true, "method": "H3-R7" }
  },
  "provenance": {
    "experiment_ids": ["mcp/experiments/2025-11-05_AI-EXP-003.md"],
    "hashes": { "panel_payload_sha256": "<sha256>" }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O alignment (test interpretation)
- Each mocked response is a `prov:Entity` (test artifact).
- The interception + UI render path is represented by the test run `prov:Activity`.
- CI runner is a `prov:Agent`.

Mocks SHOULD contain only:
- stable IDs,
- hashes (placeholders allowed),
- reference anchors.

### STAC/DCAT alignment (optional)
These mocks are test artifacts, not datasets; do not treat them as publishable domain data.
If indexed in reports, label them clearly as:
- `kfm:TestFixture`
- `kfm:ApiMock`

---

## 🧱 Architecture

### How the runner should use these mocks (recommended)
- Map route patterns to fixture files.
- Choose fixtures by `scenario_id` to avoid cross-test coupling.
- Keep intercept logic centralized (in `tests/e2e/utils/...`) so specs stay readable.

Recommended runner behavior:
- default to mocks for `@smoke` and `@regression`,
- allow live stack mode only when explicitly enabled and governed.

---

## ⚖ FAIR+CARE & Governance

### Non-negotiable governance rules
API mocks MUST:
- never expose raw coordinates,
- represent sensitive states using:
  - masked H3 cells, or
  - redacted / restricted response patterns.

API mocks MUST validate:
- CARE tier presence when relevant,
- sovereignty flags when relevant,
- restricted-state behavior is safe and predictable.

### Escalation
If a mock payload risks policy violations:
- remove it immediately,
- quarantine affected tests,
- route review to FAIR+CARE Council and the relevant working group.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-13 | Initial Focus Mode v3 API mocks guide aligned to KFM-MDP v11.2.6 (deterministic, sovereignty-safe, governance-aware). |

<div align="center">

[🏛️ Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

