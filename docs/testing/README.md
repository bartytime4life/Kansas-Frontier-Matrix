---
title: "🧪 KFM — Testing Index (CI Profiles · Data/Graph/API/UI Gates)"
path: "docs/testing/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Council · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-testing-index"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "testing"
applies_to:
  - "docs/testing/**"
  - "tests/**"
  - "tools/validation/**"
  - ".github/workflows/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded by KFM-MDP v12"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../security/SECURITY.md"

ontology_alignment:
  prov_o: "prov:Plan"
  dcat: "dcat:Dataset"
  stac: "Item"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain: []

doc_uuid: "urn:kfm:doc:testing:index:v11.2.6"
semantic_document_id: "kfm-testing-index-v11.2.6"
event_source_id: "ledger:kfm:doc:testing:index:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
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

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
fencing_profile: "outer-backticks-inner-tildes-v1"
---

# 🧪 KFM — Testing Index

## 📘 Overview

**Purpose:** Provide a single, governed entry point for **how KFM tests work**, **where they live**, and **which CI gates apply** across the full pipeline (ETL → STAC/DCAT/PROV → Neo4j graph → APIs → Web UI → Story Nodes / Focus Mode).

**Audience:** Data Engineering, Reliability, Backend/API, Frontend/UI, Domain Curators, Governance Reviewers.

**Scope (what this index covers):**
- Deterministic test layers that protect **data contracts**, **catalog integrity**, **graph correctness**, **API stability**, and **UI accessibility**.
- Where test artifacts and provenance belong (so promotions are reviewable).

**Non‑Goals (explicit):**
- This index does **not** replace subsystem‑specific guides (each pipeline/module may have additional tests and runbooks).
- This index does **not** define new governance policy; it links to governed standards instead.

**Quick links (primary):**
- `tests/README.md` — cross‑cutting test suite overview
- `tests/ARCHITECTURE.md` — testing strategy & architecture
- `docs/testing/golden-record/README.md` — golden‑record (data invariants) guide
- `tools/validation/` — catalog + schema validators (STAC/DCAT/metadata)

## 🗂️ Directory Layout

~~~text
📂 <repo-root>/
├─ 📂 docs/
│  ├─ 📂 testing/
│  │  ├─ 📄 README.md — This testing index (governed, canonical entry point)
│  │  └─ 📂 golden-record/
│  │     └─ 📄 README.md — Golden-record data tests (schema/value invariants)
│  └─ 📂 standards/
│     ├─ 📂 governance/ — Charter + governance controls (enforced)
│     ├─ 📂 faircare/ — FAIR+CARE guidance (enforced)
│     └─ 📂 sovereignty/ — Indigenous data protection (enforced)
├─ 📂 tests/
│  ├─ 📄 README.md — Test suite overview (cross-cutting)
│  ├─ 📄 ARCHITECTURE.md — Testing strategy & architecture
│  └─ 📂 fixtures/ — Shared test fixtures and sample data
├─ 📂 tools/
│  ├─ 📂 validation/ — Data/metadata validators (STAC/DCAT/schema checks)
│  └─ 📂 ci/ — CI helper scripts (build/test automation helpers)
└─ 📂 .github/
   └─ 📂 workflows/ — CI workflows (linting, tests, audits, build/deploy)
~~~

## 🧭 Context

KFM runs “tests” at multiple layers. This index uses the following **common meanings**:

- **Code tests:** unit/integration tests that validate functions, services, and APIs.
- **Contract tests:** checks that **schemas and interfaces** stay stable (STAC, DCAT, PROV, API response shapes).
- **Data tests:** validation of **values** and **invariants** (including golden‑records and drift tolerances).
- **Governance tests:** enforcement of policy gates (no secrets, no obvious PII leakage, required metadata present, required governance links in docs).

**Pipeline alignment (contract-first):**
- ETL and derived artifacts must validate before catalog publish.
- STAC/DCAT/PROV are the “public contracts” for discoverability and reproducibility.
- The **frontend stays behind APIs** (no direct graph access from the UI); tests should preserve that boundary.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  PR[Pull Request / Change] --> L0[L0: Static Checks\nmarkdown-lint · schema-lint · secret-scan · pii-scan]
  L0 --> L1[L1: Unit & Integration Tests\nlanguage/tool specific]
  L1 --> L2[L2: Data/Metadata Contracts\nSTAC/DCAT/PROV validators]
  L2 --> L3[L3: Golden-Record Invariants\nschema + value invariants + tight tolerances]
  L3 --> L4[L4: Graph & API Contracts\nconstraints · query invariants · API response shape]
  L4 --> L5[L5: UI Quality Gates\na11y checks · lint · build]
  L5 --> PROMOTE[Promotion / Release Gate\nattestations + provenance artifacts]
~~~

## 🧠 Story Node & Focus Mode Integration

Testing is part of Story Node integrity:

- **Evidence-led narrative:** Story Nodes must remain anchored to cataloged data and provenance artifacts.
- **No hidden “magic”:** if an algorithm (or model) contributes to a Story Node, tests must ensure:
  - versioned identifiers (model/tool versions),
  - pinned configs (hashable),
  - provenance emits (OpenLineage + PROV where required),
  - sensitive data protection rules apply (aggregation/masking/generalization if mandated).

Recommended Story Node test focus:
- “No narrative without lineage”: every surfaced statistic/claim must be traceable to a dataset/entity lineage chain.
- “No sensitive precision leakage”: fixtures and example outputs must respect sovereignty and sensitivity rules.

## 🧪 Validation & CI/CD

Minimum CI profiles for governed docs and testing artifacts include:
- `markdown-lint`, `schema-lint`, `metadata-check`, `diagram-check`
- `footer-check` (governance links present + footer ordering)
- `provenance-check` (version history coherence + provenance artifacts where required)
- `secret-scan`, `pii-scan`
- `accessibility-check` for documentation and UI‑adjacent docs where relevant

Recommended local workflows (project-dependent; verify per subsystem README):
~~~bash
# Run the cross-cutting test suite (if Make targets are provided)
make test

# Python-based suites (typical)
pytest -q

# Validate catalogs / metadata contracts (tooling may vary; prefer deterministic validators)
python -m tools.validation.stac_validate --help
~~~

CI expectations for determinism:
- Fixed seeds where stochasticity exists (and record the seed).
- Stable ordering (sorted keys/rows) prior to hashing or emitting artifacts.
- Pin validator versions (STAC/DCAT/PROV validators) for reproducible pass/fail behavior.

## 📦 Data & Metadata

Testing produces artifacts that reviewers need to trust and reproduce. Recommended artifact handling:

- **Ephemeral CI artifacts:** JUnit/coverage logs can remain CI artifacts unless they gate promotions.
- **Promotion-relevant artifacts:** store deterministic summaries in the governed provenance locations:
  - `mcp/runs/<run-id>/` for run logs and auditables (CI-friendly)
  - `releases/<version>/` for release-pinned attestations, SBOMs, and manifests

Recommended test artifact types:
- `qa/<run-id>.summary.json` — machine-readable summary
- `qa/<run-id>.report.md` — human-readable explanation
- `provenance/<run-id>.openlineage.json` — minimal lineage event
- `provenance/<run-id>.prov.jsonld` — PROV-O JSON-LD (when required)

## 🌐 STAC, DCAT & PROV Alignment

**STAC (testing outputs):**
- QA outputs can be attached as STAC assets (role `qa`) to the affected Items/Collections.

Example (attach QA summary + provenance as assets):
~~~json
{
  "assets": {
    "qa_summary": {
      "href": "qa/2025-12-16T120000Z.summary.json",
      "type": "application/json",
      "roles": ["qa"],
      "title": "QA Summary (Golden-Record + Contract Gates)"
    },
    "provenance": {
      "href": "provenance/2025-12-16T120000Z.prov.jsonld",
      "type": "application/ld+json",
      "roles": ["provenance"],
      "title": "PROV-O JSON-LD (Test/Validation Lineage)"
    }
  }
}
~~~

**DCAT (testing outputs):**
- Treat test reports as `dcat:Distribution` of a documentation dataset when they are part of the governed release evidence.

**PROV-O / OpenLineage (testing runs):**
- Model each test run as an `Activity` that:
  - `used` inputs/configs,
  - `generated` QA reports,
  - is attributed to CI agents and maintainers.

## 🧱 Architecture

A practical testing architecture for KFM:

- **Spec-driven invariants** (for data): YAML/JSON specs define required fields, tolerances, and expected keys.
- **Executable harness**: test runner loads specs + fixtures deterministically and emits:
  - pass/fail,
  - a minimal diff,
  - lineage artifacts for auditability.
- **Contract validators**: schema and catalog validators run before promotions.
- **Promotion gates**: CI requires clean results for stable/governed paths.

Recommended “what to test” map (keep contracts intact):
- **ETL stage:** schema + value checks on intermediate outputs.
- **Catalog stage (STAC/DCAT/PROV):** validators + required field enforcement.
- **Graph stage:** constraint checks + query invariants (behind APIs).
- **API stage:** contract tests against OpenAPI/GraphQL shapes.
- **UI stage:** build/lint/a11y; ensure UI does not bypass API contracts.

## ⚖ FAIR+CARE & Governance

Testing must align with FAIR+CARE and sovereignty requirements:

- **Fixtures:** must be public-safe (or redacted/aggregated/synthetic), and must not leak sensitive locations or personal data.
- **Governance gates are real gates:** do not “waive” provenance, license, or sensitivity checks without explicit governance approval.
- **Reviewer ergonomics:** prefer small, targeted tests (golden records, contract assertions) over giant logs.

If a test requires restricted fixtures:
- store them outside the public repo (per sovereignty policy),
- use hashed placeholders in-repo,
- validate via secure CI context approved by governance.

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v11.2.6 | 2025-12-16 | Initial `docs/testing/` index published; defines test layers, repo locations, and governed footer | <name/handle> |

---

<div align="center">

**🧪 Testing · KFM v11.2.6**  
Deterministic Pipelines · Contract-First Validation · FAIR+CARE Governance

[📘 Docs Root](../README.md) ·
[🏗️ Data Architecture](../architecture/README.md) ·
[🧪 Testing Index](./README.md) ·
[✅ Golden-Record Tests](./golden-record/README.md) ·
[🧪 Test Suite](../../tests/README.md) ·
[⚙️ CI Workflows](../../.github/workflows/) ·
[🏛️ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🔐 Security](../security/SECURITY.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>