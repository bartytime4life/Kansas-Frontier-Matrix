---
title: "🧪 Kansas Frontier Matrix — Test Platform Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/ARCHITECTURE.md"

version: "v11.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"
ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 test architecture upgrade"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-platform-architecture"

semantic_document_id: "kfm-doc-tests-architecture"
doc_uuid: "urn:kfm:doc:tests-architecture-v11.0.0"
event_source_id: "ledger:tests/ARCHITECTURE.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk · Inclusive · Ethical"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

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

telemetry_ref: "../releases/v11.0.0/tests-telemetry.json"
telemetry_schema: "../schemas/telemetry/tests-architecture-v11.json"

validation_reports:
  - "../reports/fair/tests_summary.json"
  - "../reports/audit/ai_tests_ledger.json"
  - "../reports/self-validation/work-tests-validation.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "tests/ARCHITECTURE.md@v10.0.0"
  - "tests/ARCHITECTURE.md@v10.3.2"
  - "tests/ARCHITECTURE.md@v10.4.0"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"
  - "inject-secrets"
  - "inject-pii"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Test Platform Architecture (v11 LTS)**
`tests/ARCHITECTURE.md`

**Deterministic · FAIR+CARE · Sovereignty-Safe · Telemetry-Aligned · Diamond⁹ Ω / Crown∞Ω**

This document defines the **test platform architecture** for the Kansas Frontier Matrix monorepo:
how tests are structured, how they run, what they validate, which gates block merges/releases, and how
the platform emits governance- and telemetry-ready artifacts for auditability.

</div>

---

## 📘 Overview

### What this architecture is responsible for
The v11 test platform architecture is the system-wide guardrail for:

- correctness (logic, schemas, contracts)
- reproducibility (deterministic fixtures, pinned config, seeded randomness)
- governance (FAIR+CARE and sovereignty constraints)
- narrative safety (for any narrative-capable surfaces)
- accessibility (WCAG 2.1 AA+)
- catalog integrity (STAC/DCAT link integrity)
- semantic integrity (schema and ontology alignment at boundaries)
- observability (telemetry shape + required fields; release-bundle readiness)

### What this architecture is not
- It is not the full list of tests (see `tests/README.md` for suite inventory).
- It does not define production infrastructure.
- It does not permit “best effort” safety: governance gates are hard blockers.

### Non-negotiables
- deterministic-by-default execution
- CI-gated for governance, sovereignty, and accessibility
- fixtures are sanitized and sovereignty-safe
- no secrets and no PII in test code, fixtures, or logs
- provenance references and telemetry are treated as first-class QA outputs

---

## 🗂️ Directory Layout

~~~text
📁 tests/
├── 📄 README.md                              — 🧪 Test framework overview and suite index
├── 📄 ARCHITECTURE.md                        — 🧱 This architecture document
│
├── 📁 unit/                                  — 🧪 Pure deterministic tests (no network)
│   ├── 📁 pipelines/                          — ETL helpers, transforms, contract utilities
│   ├── 📁 web/                                — UI component tests (headless)
│   ├── 📁 governance/                          — CARE + sovereignty atomics (masking, prohibitions)
│   └── 📁 utils/                               — Deterministic pure functions
│
├── 📁 integration/                           — 🧩 Cross-boundary tests (mocked services allowed)
│   ├── 📁 stac/                               — STAC Items/Collections validation and link integrity
│   ├── 📁 dcat/                               — DCAT mapping/required fields validation (if implemented)
│   ├── 📁 storynodes/                         — Story Node v3 schema, SHACL, ingestion readiness
│   ├── 📁 graph/                              — Neo4j constraints/idempotency/dedupe behavior (if enabled)
│   ├── 📁 api/                                — API contract tests (DTO schemas, error shapes, pagination)
│   ├── 📁 focus_mode/                         — Focus Mode payload and safety gates (if implemented)
│   └── 📁 telemetry/                          — Telemetry shape + aggregation validation
│
├── 📁 e2e/                                   — 🧭 End-to-end flows (browser driven)
│   ├── 📁 web-app/                            — Navigation, rendering, keyboard paths, a11y
│   ├── 📁 dataset-workflows/                  — Intake → validate → publish simulations
│   └── 📁 governance/                         — Ledger/provenance UI flows (if implemented)
│
├── 📁 schemas/                               — 🧾 Test fixtures and schema assertions
│   ├── 📄 story-node.test.json
│   ├── 📄 stac-collection.test.json
│   └── 📄 telemetry.test.json
│
└── 📁 resources/                             — 🧰 Deterministic sanitized fixtures
    ├── 📁 sample_stac/
    ├── 📁 storynodes/
    ├── 📁 focus_payloads/
    └── 📁 pipelines/
~~~

---

## 🧭 Context

### KFM pipeline coverage map
The test platform is designed to gate the KFM pipeline end-to-end:

ETL → catalogs (STAC/DCAT/PROV) → graph ingestion → API → UI → Story Nodes → Focus Mode

Coverage is enforced through layered suites:
- unit: pure correctness and rule enforcement
- integration: boundary contracts and link integrity
- e2e: user-critical flows and publish gates

### Determinism model
Determinism is achieved via:
- pinned fixtures in `tests/resources/**`
- fixed seeds for randomness (where used)
- pinned time windows (no “today” time math in tests)
- strict schema-driven validation (avoid brittle string snapshots)
- hermetic runs for unit tests; mocked services for integration; controlled environments for e2e

### Environment matrix (expected)
Tests are designed to support these execution contexts:
- local developer runs (fast unit + targeted integration)
- CI runners (full gate set)
- release validation runs (same as CI with release packaging checks)

This architecture assumes containerization is available for service dependencies when needed (e.g., graph/database), but does not require it for unit suites.

---

## 🧱 Architecture

### Layer responsibilities and gates
**1) Unit layer**
- pure logic and deterministic helpers
- governance atomics (masking rules, prohibited output detectors)
- contract utility validation

Gate class: correctness and safety primitives

**2) Schema and contract layer**
- JSON Schema validity for Story Nodes, telemetry, DTOs, catalog items
- SHACL validation where used (Story Node v3 shapes)
- contract mapping validation (KFM-PDC referenced fields)

Gate class: schema correctness and drift prevention

**3) Integration layer**
- STAC/DCAT link integrity (collections, items, assets, required metadata)
- graph idempotency and merge behavior (when enabled)
- API contract validation (paging, error shapes, DTOs)
- telemetry aggregation correctness (required fields, types, invariants)

Gate class: boundary correctness and interoperability

**4) Accessibility layer**
- keyboard-only path checks
- landmark and heading structure checks
- reduced-motion mode checks
- color contrast checks (where automated tests exist)

Gate class: user safety and compliance

**5) End-to-end layer**
- user workflows: intake → validate → publish
- Focus Mode navigation flows (where implemented)
- provenance overlay behavior (where implemented)
- governance UI flows (where implemented)

Gate class: whole-system behavior

**6) Governance and sovereignty layer**
- coordinate leakage scanners (raw lat/long, tight bboxes)
- H3 masking/generalization enforcement tests
- narrative safety checks for narrative-capable models/surfaces
- license and rights checks (no restricted content in fixtures)

Gate class: ethics and sovereignty enforcement

**7) Telemetry and sustainability layer**
- telemetry schema validation
- required field presence validation
- regression checks on runtime/energy/carbon where tracked
- report bundling checks for release artifacts

Gate class: observability and auditability

---

## 🗺️ Diagrams

### Test layer flow
~~~mermaid
flowchart TD
  A["Unit"] --> B["Schema and contract"]
  B --> C["Integration"]
  C --> D["Accessibility"]
  D --> E["E2E"]
  E --> F["Governance and sovereignty"]
  F --> G["Telemetry verification"]
~~~

### CI gating flow
~~~mermaid
flowchart TD
  A["CI trigger"] --> B["Run unit suites"]
  B --> C["Validate schemas and contracts"]
  C --> D["Run integration suites"]
  D --> E["Run accessibility gates"]
  E --> F["Run end-to-end suites"]
  F --> G["Run governance checks"]
  G --> H["Validate telemetry and reports"]
  H --> I["Publish CI artifacts and release telemetry"]
~~~

---

## 📦 Data & Metadata

### Fixtures and goldens
Fixtures MUST:
- be sanitized (no PII)
- be sovereignty-safe (no restricted coordinates)
- be rights-safe (no restricted datasets)
- be deterministic (no “live” dependencies)

Recommended fixture strategy:
- “golden” JSON fixtures for Story Node v3 payloads
- “golden” STAC Item/Collection fixtures with minimal required fields
- synthetic time-series fixtures for hydrology/climate tests
- synthetic graph neighborhood fixtures for Focus Mode payload tests

### Naming conventions for tests
Recommended (not enforced here unless CI checks exist):
- unit tests: `test_*.py` / `*.test.ts`
- integration tests: `it_*.py` / `*.spec.ts`
- e2e: `*.e2e.ts` / `*.spec.ts` under `tests/e2e/**`

### QA artifact outputs (expected)
The platform expects outputs (paths may vary by runner):
- logs (text)
- reports (JSON)
- checksums (JSON)
- telemetry (JSON)
- governance summaries (JSON)

Canonical report pointers (as referenced in front matter):
- `../reports/fair/tests_summary.json`
- `../reports/audit/ai_tests_ledger.json`
- `../reports/self-validation/work-tests-validation.json`

---

## 🧪 Validation & CI/CD

### Merge blockers (normative)
CI MUST block merges if any fail:
- schema and contract validation
- sovereignty masking regression checks
- coordinate leakage checks
- narrative safety checks (when narrative-capable systems are involved)
- accessibility checks (WCAG 2.1 AA+ gate)
- secret scan or PII scan flags
- telemetry schema validation failures
- provenance reference failures where required by policy

### Test execution order (normative)
1. unit
2. schema and contract validation
3. integration
4. accessibility
5. e2e
6. governance and sovereignty
7. telemetry verification and report publication

### Local run guidance (architecture-level)
Local runs should mirror CI order, but can be scoped:
- unit first, always
- schema/contract checks before integration
- e2e only when UI flows or publish gates are changed

Example command shapes (implementation-specific):
~~~text
python -m pytest tests/unit
python -m pytest tests/integration
python -m pytest tests/e2e
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### Catalog validation
Integration tests should verify:
- STAC Collections and Items meet required fields
- asset links resolve to expected paths or fixtures
- DCAT-required fields are present where DCAT records exist
- catalog-to-provenance linkouts are present where policy requires

### Provenance validation
Where pipeline policy requires provenance:
- tests should verify the presence of PROV-O bundle references
- tests should verify OpenLineage reference presence (job and run identifiers)
- tests should verify checksums exist for derived outputs (where required)

---

## ⚖ FAIR+CARE & Governance

### Security and privacy rules
Tests must never:
- use production credentials
- emit PII
- fetch restricted datasets
- leak sovereignty-protected coordinates or knowledge
- store sensitive intermediate data in committed fixtures/logs

### Sovereignty safe rules
- enforce masking/generalization requirements in fixtures and outputs
- block any regression that allows raw sensitive coordinates through
- require governance routing for Tier A conditions (where encoded by policy)

### Accessibility rules
A11y regressions are merge blockers.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-12-13 | Updated and aligned to KFM-MDP v11.2.6 (tilde fences, approved H2 registry, Mermaid ASCII-safe labels, expanded platform responsibilities and gating model). |
| v11.0.0 | 2025-11-24 | Initial v11 architecture: sovereignty, accessibility, telemetry v11, and platform-wide test coverage. |
| v10.4.0 | 2025-11-15 | Prior architecture: Focus and Story Node integration hardening. |
| v10.3.2 | 2025-11-14 | Hardened schema and telemetry testing. |
| v10.0.0 | 2025-11-10 | Initial platform-wide test architecture. |

<div align="center">

[🏛️ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
