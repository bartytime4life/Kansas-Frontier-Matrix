---
title: "🧪 Kansas Frontier Matrix — Testing & QA Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/README.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"
ttl_policy: "6-month review"
sunset_policy: "Superseded by next v12 test framework update"

status: "Active / Enforced"
doc_kind: "Testing Framework"
intent: "tests-framework-overview"
header_profile: "standard"
footer_profile: "standard"
machine_extractable: true

semantic_document_id: "kfm-doc-tests-readme"
doc_uuid: "urn:kfm:tests:readme:v11.0.0"
event_source_id: "ledger:tests/README.md"
immutability_status: "version-pinned"

classification: "Public Document"
sensitivity: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Ethical · Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../releases/v11.0.0/signature.sig"
attestation_ref: "../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"

data_contract_ref: "../docs/contracts/data-contract-v3.json"

telemetry_ref: "../releases/v11.0.0/tests-telemetry.json"
telemetry_schema: "../schemas/telemetry/tests-validation-v11.json"
validation_reports:
  - "../reports/fair/tests_summary.json"
  - "../reports/audit/ai_tests_ledger.json"
  - "../reports/self-validation/work-tests-validation.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "inject-secrets"
  - "inject-pii"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Testing & QA Framework (v11)**
`tests/README.md`

**Deterministic · Ethical · Sovereignty-Safe · Telemetry-Driven · Diamond⁹ Ω / Crown∞Ω**

The v11 Testing & QA Framework is the CI/CD guardian for the KFM monorepo. It validates correctness,
reproducibility, governance, accessibility, and semantic integrity across ETL, catalogs, graph ingestion,
API/UI, Story Nodes, and Focus Mode.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### What this framework guarantees
- ✅ unit → integration → end-to-end coverage with deterministic fixtures
- ✅ schema + contract validation (data contracts, payload shapes, telemetry shapes)
- ✅ sovereignty and CARE non-regression checks (no restricted coordinate leakage)
- ✅ narrative safety gates where narrative-capable systems are involved
- ✅ accessibility gates (WCAG 2.1 AA+; keyboard paths and structural checks)
- ✅ provenance expectations (references to PROV-O and OpenLineage artifacts)
- ✅ sustainability telemetry capture (energy/carbon/runtime where available)

### What this framework produces
Every test run SHOULD produce (where applicable):
- validation reports (JSON)
- provenance references (PROV-O/OpenLineage pointers)
- telemetry artifacts (energy/carbon/runtime)
- accessibility results (pass/fail gates)
- governance outcomes (CARE/sovereignty checks)

---

## 🗂️ Directory Layout

~~~text
tests/
├── 📄 README.md                      — 🧪 This framework overview (this file)
├── 📄 ARCHITECTURE.md                — 🧱 Optional deeper test architecture notes
│
├── 📁 unit/                          — 🧪 Pure deterministic tests (no network)
│   ├── 📁 pipelines/                 — ETL/AI/utils unit tests
│   ├── 📁 web/                       — UI component tests (headless)
│   ├── 📁 governance/                — CARE/masking atomic rule checks
│   └── 📁 utils/                     — Pure logic helpers, format validators
│
├── 📁 integration/                   — 🧩 Cross-component behavior tests
│   ├── 📁 stac/                      — STAC/DCAT linking and metadata checks
│   ├── 📁 storynodes/                — Story Node v3 payload and flow tests
│   ├── 📁 graph/                     — Neo4j constraints, idempotency, dedupe (if enabled)
│   ├── 📁 api/                       — API contract tests (schema, paging, error shapes)
│   └── 📁 telemetry/                 — Telemetry emission + aggregation validation
│
├── 📁 e2e/                           — 🧭 End-to-end user flows (browser-driven)
│   ├── 📁 web-app/                   — Navigation, a11y, keyboard paths
│   ├── 📁 governance/                — Ledger/provenance UI flows (where implemented)
│   └── 📁 dataset-workflows/         — Intake → validate → publish simulations
│
├── 📁 schemas/                       — 🧾 Schema test fixtures + assertions
│   ├── 📄 story-node.test.json
│   ├── 📄 stac-collection.test.json
│   └── 📄 telemetry.test.json
│
└── 📁 resources/                     — 🧰 Deterministic fixtures (sanitized)
    ├── 📁 sample_stac/
    ├── 📁 storynodes/
    ├── 📁 focus_payloads/
    └── 📁 pipelines/
~~~

---

## 🧭 Context

### Determinism rules for tests
A test suite is deterministic when it:
- avoids network calls unless explicitly isolated + mocked
- uses pinned fixtures and pinned time ranges
- uses fixed seeds wherever randomness exists
- validates outputs via schemas/checksums rather than brittle string matching

### Fixture safety rules
Fixtures under `tests/resources/**` MUST be:
- sanitized (no PII)
- sovereignty-safe (no restricted coordinates)
- rights-safe (no restricted datasets)
- stable and reproducible (no live dependencies)

---

## 🧱 Architecture

### Test pyramid
- **Unit:** fast, pure logic, no network
- **Integration:** boundary checks (schemas, catalogs, graph merges, API shapes)
- **E2E:** user-critical flows (a11y, navigation, publish gates)

### Governance-first test design
When changes could affect sovereignty, heritage masking, or narrative claims:
- required non-regression tests MUST exist
- failures MUST block CI (no warning-only mode)

---

## 🗺️ Diagrams

### CI workflow
~~~mermaid
flowchart TD
  A["CI trigger"] --> B["Unit tests"]
  B --> C["Schema and contract validation"]
  C --> D["Integration tests"]
  D --> E["Accessibility tests (WCAG 2.1 AA+)"]
  E --> F["E2E tests"]
  F --> G["Governance and CARE validation"]
  G --> H["Telemetry and sustainability verification"]
  H --> I["Publish reports and release telemetry"]
~~~

---

## 🧪 Validation & CI/CD

### Merge blockers
A merge MUST be blocked if any of the following fail:
- schema/contract validation
- sovereignty masking regression checks
- narrative safety checks where applicable
- accessibility regressions (WCAG 2.1 AA+)
- secret scan or PII scan flags
- telemetry/provenance structural failures

### QA artifacts
| Artifact | Description | Format |
|---|---|---|
| `pytest.log` | execution log | text |
| `coverage.json` | coverage summary | JSON |
| `checksums.json` | lineage checks | JSON |
| `fairstatus.json` | FAIR+CARE summary | JSON |
| `tests-telemetry.json` | energy/carbon/runtime | JSON |
| `metadata.json` | governance/provenance refs | JSON |

### Local run order
Local runs SHOULD follow CI order:
- unit tests
- schema/contract validation
- integration tests
- accessibility checks
- end-to-end tests (where supported)

---

## 🌐 STAC, DCAT & PROV Alignment

### Catalog validation scope
Integration tests SHOULD validate:
- STAC Items/Collections for derived spatial outputs
- DCAT-compatible dataset metadata presence for publishable bundles
- link integrity among:
  - derived outputs
  - STAC assets
  - DCAT records
  - provenance references

### Provenance expectations
Test runs SHOULD validate that pipeline outputs include:
- PROV-O references (Activity/Entity/Agent identifiers)
- OpenLineage references (job/run identifiers and dataset linkages)
- stable identifiers that can be traced across CI, releases, and governance ledgers

---

## 🧠 Story Node & Focus Mode Integration

### Story Node v3 tests
Story Node tests SHOULD verify:
- schema validity (JSON Schema and any SHACL checks used)
- provenance references present and non-empty
- masking rules enforced for sensitive geographies
- narrative claims bounded by evidence links (where applicable)

### Focus Mode v3 tests
Focus Mode tests SHOULD verify:
- context/timeline/map panels render consistently
- provenance overlays do not expose restricted content
- UI remains accessible (keyboard paths, reduced motion, readable headings)

---

## ⚖ FAIR+CARE & Governance

### Security and privacy
Tests MUST NOT:
- emit PII
- use production tokens
- access restricted datasets
- leak sovereignty-protected coordinates or restricted knowledge
- store sensitive intermediate data in fixtures or committed logs

### Governance report routing
Reports listed under `validation_reports` are the canonical audit pointers for:
- CARE decisions
- a11y conformance
- ethical flags
- semantic violations
- telemetry anomalies

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-12-13 | Upgraded to KFM-MDP v11.2.6 structure (tilde fences, Mermaid-safe labels, normalized headings, governed metadata). |
| v11.0.0 | 2025-11-24 | Initial v11 QA framework: sovereignty rules, telemetry v11, Story Node v3 + Focus Mode v3 testing. |
| v10.3.1 | 2025-11-13 | Pre-v11 structure; STAC/DCAT bridge; explainability testing. |
| v10.0.0 | 2025-11-10 | Initial QA framework for v10. |
| v9.7.0 | 2025-11-05 | Earlier telemetry + ethics testing layer. |

<div align="center">

[🏛️ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
