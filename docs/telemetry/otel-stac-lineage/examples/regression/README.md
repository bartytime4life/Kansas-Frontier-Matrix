---
title: "🧨 Kansas Frontier Matrix — OTel → STAC Lineage: Regression Fixtures (PASS/FAIL) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/examples/regression/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/otel-stac-lineage-regression-examples-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/otel-stac-lineage-regression-examples-v11.2.6.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "telemetry-otel-stac-lineage-regression-fixtures"
  applies_to:
    - "docs/telemetry/otel-stac-lineage/examples/regression/**"
    - "docs/telemetry/otel-stac-lineage/validators/**"
    - "docs/telemetry/otel-stac-lineage/specs/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Synthetic validator fixtures; no secrets; no private URLs"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by OTel Regression Fixtures v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/otel-stac-lineage/examples/regression/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:examples:regression:v11.2.6"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-examples-regression-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:otel-stac-lineage:examples:regression:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧨 **Kansas Frontier Matrix — OTel → STAC Lineage: Regression Fixtures (PASS/FAIL)**
`docs/telemetry/otel-stac-lineage/examples/regression/README.md`

**Purpose**  
Provide **validator regression fixtures** (known-good and known-bad) for the OTel → STAC/DCAT/PROV lineage pipeline.  
These fixtures lock in: required fields, attribute conventions, prohibited content rules, and strict failure semantics.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Examples-Regression_Fixtures-success" />
<img src="https://img.shields.io/badge/Validators-PASS%2FFAIL_Strict-orange" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 otel-stac-lineage/
        └── 📁 examples/
            ├── 📄 README.md                         — Examples index (conventions + pointers)
            ├── 📁 otel/                             — Raw OTel-shaped fixtures (inputs)
            ├── 📁 mapping/                          — Expected mapped outputs (STAC/DCAT/PROV)
            └── 📁 regression/                       — ← This folder (validator PASS/FAIL cases)
                ├── 📄 README.md                     — This file
                ├── 📁 pass/                         — Fixtures that MUST validate successfully
                │   ├── 📄 span_end_minimal.pass.json
                │   ├── 📄 log_event_minimal.pass.json
                │   └── 📄 bundle_minimal.pass.json
                ├── 📁 fail/                         — Fixtures that MUST fail validation
                │   ├── 📄 missing_trace_id.fail.json
                │   ├── 📄 invalid_timestamp.fail.json
                │   ├── 📄 forbidden_url.fail.json
                │   ├── 📄 secret_like_token.fail.json
                │   └── 📄 care_tag_sensitive.fail.json
                └── 📄 regression_manifest.json       — Index: fixture → expected outcome → rule id
~~~

**Directory rule (normative):**  
Regression fixtures MUST be segregated into `pass/` and `fail/` directories, and each fixture MUST be referenced by `regression_manifest.json`.

---

## 📘 Overview

Regression fixtures exist to prevent validator “drift.”

They answer:

- If we change validators/specs, did we accidentally accept something we used to reject?
- Did we become too strict and reject previously accepted valid telemetry?
- Did we break mapping assumptions that downstream STAC/DCAT/PROV outputs rely on?

These fixtures are intended for:

- unit tests for validator functions
- CI smoke tests for docs/telemetry changes
- governance review evidence when rules evolve

---

## 🧭 Context

### 1. What is being tested

Typical validator rules these fixtures cover:

- OTel identifiers:
  - `trace_id`, `span_id` shape/length (strict)
  - cross-field consistency (parent span relationships)
- Timestamps:
  - UTC ISO-8601 format
  - start <= end semantics
- Required KFM attributes:
  - `kfm.workflow`, `kfm.run_id`, `kfm.classification`, `kfm.care_tag`
- Prohibited content:
  - URLs in disallowed namespaces
  - secret-like strings (token formats)
  - raw PII fields
  - sensitive coordinates or sensitive tags without overrides
- Mapping prerequisites:
  - required fields that STAC/DCAT/PROV mapping depends on

### 2. Sanitization policy

Even FAIL fixtures must remain governance-safe:

- include the *shape* of a secret/token, but not a real token
- include placeholders for URLs (e.g., `https://example.invalid/…`) if demonstrating forbidden URL logic
- never embed real internal hostnames, emails, or production repo URLs

---

## 🗺️ Diagrams

### Where regression fixtures sit

~~~mermaid
flowchart LR
  FIX["Regression fixtures (pass/fail)"] --> VAL["Validators"]
  VAL --> RES["PASS / FAIL results"]
  RES --> CI["CI gate"]
  CI --> SPEC["Spec stability (no drift)"]
~~~

---

## 🧪 Validation & CI/CD

### 1. How CI should use these fixtures

A typical validator test runner SHOULD:

1. Load `regression_manifest.json`
2. For each fixture:
   - run the validator(s) listed in the manifest
   - assert:
     - PASS fixtures validate with no blocking errors
     - FAIL fixtures produce the expected rule failure IDs
3. Emit a summary artifact in CI:
   - counts
   - failures
   - diff vs previous run (optional)

### 2. Required outcome semantics (normative)

- `pass/*` MUST pass:
  - no schema errors
  - no prohibited content hits
  - all required KFM keys present
- `fail/*` MUST fail:
  - at least one blocking rule hit
  - error classification is deterministic and stable

### 3. Suggested test profiles

- `schema-lint` (if fixtures declare `$schema` or are validated against JSON Schema)
- `metadata-check` (required keys, enumerations, and IDs)
- `footer-check` (for docs only)
- validator regression runner (project-local)

---

## 📦 Data & Metadata

### 1. regression_manifest.json (recommended shape)

`regression_manifest.json` SHOULD be small and explicit:

~~~json
{
  "schema_version": "v11.2.6",
  "kind": "otel_regression_manifest",
  "fixtures": [
    {
      "id": "missing_trace_id",
      "path": "./fail/missing_trace_id.fail.json",
      "expect": "fail",
      "validators": ["otel-basic", "kfm-required-attrs"],
      "expect_rule_ids": ["OTEL_TRACE_ID_REQUIRED"],
      "notes": "Trace ID missing should always fail."
    },
    {
      "id": "span_end_minimal",
      "path": "./pass/span_end_minimal.pass.json",
      "expect": "pass",
      "validators": ["otel-basic", "kfm-required-attrs"],
      "notes": "Minimal valid end-of-span payload."
    }
  ]
}
~~~

**Rule IDs** SHOULD be stable strings (not error-message text) so governance dashboards can track trendlines.

### 2. PASS fixture minimal principles

PASS fixtures SHOULD:

- include only what is required to be valid
- prefer deterministic placeholder IDs
- avoid optional fields unless the test is about those optional fields

### 3. FAIL fixture minimal principles

FAIL fixtures SHOULD:

- break exactly one rule when feasible (single-fault fixtures)
- when multi-fault is required, document it in the manifest

---

## 🌐 STAC, DCAT & PROV Alignment

Regression fixtures protect the mapping layer indirectly:

- if a validator change breaks required fields for mapping,
  mapping fixtures in `examples/mapping/` should fail too

This folder is therefore an upstream guardrail for:

- STAC item creation (run/event → item properties/assets)
- DCAT distribution creation (report URLs/media types/checksums)
- PROV graph export (activity/entity/agent completeness)

---

## 🧱 Architecture

This directory is intentionally boring and predictable:

- `pass/` and `fail/` folders
- one manifest that is the authoritative index
- deterministic filenames and IDs
- a small, stable set of validator rule identifiers

This makes it safe to:

- audit changes in PRs
- run diffs across versions
- generate dashboards from counts and rule IDs

---

## ⚖ FAIR+CARE & Governance

Regression fixtures embody governance constraints:

- they demonstrate “what we reject”
- they define “minimum acceptable telemetry”
- they make validator evolution reviewable

When a rule is intentionally changed:

- update the relevant fixtures and the manifest
- record the change in `🕰️ Version History` below
- ensure mapping examples and validator docs remain consistent

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | `@kfm-telemetry` | Built from scratch: PASS/FAIL directory convention, regression manifest pattern, and normative CI semantics. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline guidance (superseded by v11.2.6 rewrite).               |

---

<div align="center">

🧨 **KFM — OTel → STAC Lineage: Regression Fixtures (v11.2.6)**  
Deterministic Validation · No Drift · Governance-Safe Test Data

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Examples](../README.md) ·
[⬅ OTel STAC Lineage Telemetry](../../README.md) ·
[🧾 OTel Fixtures](../otel/README.md) ·
[🧩 Mapping Examples](../mapping/README.md) ·
[🧾 Specs](../../specs/README.md) ·
[🧪 Validators](../../validators/README.md) ·
[📦 Storage](../../storage/README.md) ·
[🗺️ Diagrams](../../diagrams/README.md) ·
[⚙ Workflows Index](../../../../workflows/README.md) ·
[⚙ Telemetry Export Workflow](../../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

