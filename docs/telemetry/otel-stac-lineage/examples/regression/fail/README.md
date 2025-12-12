---
title: "🚫 Kansas Frontier Matrix — OTel → STAC Lineage Regression Fixtures: FAIL Cases (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/examples/regression/fail/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/otel-stac-lineage-regression-fail-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/otel-stac-lineage-regression-fail-v11.2.6.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

scope:
  domain: "telemetry-otel-stac-lineage-regression-fail-fixtures"
  applies_to:
    - "docs/telemetry/otel-stac-lineage/examples/regression/fail/**"
    - "docs/telemetry/otel-stac-lineage/examples/regression/regression_manifest.json"
    - "docs/telemetry/otel-stac-lineage/validators/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Synthetic negative fixtures; no secrets; no private URLs; no sensitive coordinates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Regression FAIL Fixtures v12"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/otel-stac-lineage/examples/regression/fail/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:examples:regression:fail:v11.2.6"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-examples-regression-fail-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:otel-stac-lineage:examples:regression:fail:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
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

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🚫 **Kansas Frontier Matrix — Regression FAIL Fixtures (OTel → STAC Lineage)**
`docs/telemetry/otel-stac-lineage/examples/regression/fail/README.md`

**Purpose**  
This directory contains **intentionally invalid** telemetry fixtures that **MUST fail** OTel → STAC lineage validation.  
Use these fixtures to prevent validator drift, enforce governance constraints, and keep failure modes deterministic.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Regression-FAIL_Fixtures-red" />
<img src="https://img.shields.io/badge/Validators-Strict_Blocks-orange" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 otel-stac-lineage/
        └── 📁 examples/
            └── 📁 regression/
                ├── 📄 README.md                     — Regression fixtures overview (PASS/FAIL semantics)
                ├── 📄 regression_manifest.json       — Fixture index + expected outcome + rule ids
                ├── 📁 pass/                          — Known-good fixtures (MUST pass)
                │   └── 📄 README.md
                └── 📁 fail/                          — ← This folder (MUST fail)
                    ├── 📄 README.md                  — This file
                    ├── 📄 missing_trace_id.fail.json
                    ├── 📄 invalid_timestamp.fail.json
                    ├── 📄 forbidden_url.fail.json
                    ├── 📄 secret_like_token.fail.json
                    └── 📄 care_tag_sensitive.fail.json
~~~

---

## 📘 Overview

### What “FAIL fixture” means (normative)

A FAIL fixture is a JSON payload that:

- **MUST NOT** validate as acceptable OTel/KFM telemetry, and
- **MUST** yield at least one **blocking** rule violation (stable rule IDs), and
- **MUST** be safe to store in a public repo (synthetic, sanitized).

### Naming conventions

- Filenames MUST end with: `*.fail.json`
- Prefer single-fault fixtures:
  - one fixture → one primary rule failure
- If multi-fault is unavoidable:
  - document it in `../regression_manifest.json`

---

## 🧭 Context

### Why these exist

FAIL fixtures are the “hard edge” of KFM telemetry governance:

- they encode what we **reject**
- they keep validator behavior deterministic across versions
- they prevent accidental acceptance of:
  - malformed OTel identifiers
  - invalid time semantics
  - prohibited URLs or unsafe link patterns
  - secret-like strings
  - sensitive CARE-tagged payloads without governance overrides

### Fixture safety rules (normative)

FAIL fixtures MUST:

- use placeholder domains like `example.invalid` (preferred) or `example.com`
- use synthetic identifiers (never real trace IDs from production)
- never contain:
  - real tokens
  - real internal hostnames
  - real emails
  - real coordinates for sensitive sites

If the test is about “secret detection,” include *token-like shape* only:

~~~text
"token": "REDACTED_TOKEN_LIKE_STRING_FOR_TESTING_ONLY"
~~~

---

## 🧪 Validation & CI/CD

### How validators should treat this folder

CI SHOULD:

1. load `../regression_manifest.json`
2. run each fixture through the declared validators
3. assert:
   - `expect = fail`
   - `expect_rule_ids` are present in the output (exact string match)

### Determinism requirement (normative)

For every file in this folder:

- running validators multiple times MUST yield the same:
  - blocking vs non-blocking classification
  - rule IDs
  - pass/fail outcome

No validator is allowed to “randomly” classify or partially pass these fixtures.

---

## 📦 Data & Metadata

### Minimal recommended FAIL fixture shape

A FAIL fixture SHOULD still resemble a real event enough to exercise parsing:

~~~json
{
  "trace_id": "00000000000000000000000000000000",
  "span_id": "0000000000000000",
  "timestamp": "2025-12-12T00:00:00Z",
  "attributes": {
    "kfm.workflow": "telemetry-export",
    "kfm.run_id": "regression_fail_demo",
    "kfm.classification": "Public",
    "kfm.care_tag": "public"
  }
}
~~~

Then introduce the *one* intended failure (example: remove `trace_id`, break timestamp format, add forbidden URL, etc.).

### Recommended failure categories

| Category              | What breaks                         | Why it matters                         |
|----------------------|--------------------------------------|----------------------------------------|
| Missing required key | `trace_id`, `run_id`, etc.           | mapping + indexing can’t proceed       |
| Invalid formatting   | timestamp or ID shape/length         | prevents deterministic joins           |
| Prohibited content   | forbidden URL, secret-like patterns  | security + governance risk             |
| Policy breach        | invalid classification/CARE tag      | sovereignty + ethics enforcement       |

Keep rows short; keep IDs and paths in the manifest, not in tables.

---

## ⚖ FAIR+CARE & Governance

These fixtures are governance evidence.

When a FAIL rule changes intentionally:

- update the fixture(s)
- update `../regression_manifest.json` with new rule IDs
- record the change under **🕰️ Version History**
- ensure related validator/spec docs are updated (no silent drift)

Focus Mode / summarizers may summarize these fixtures, but MUST NOT “rewrite” them into passing payloads.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | Built from scratch: FAIL fixture rules, naming conventions, CI semantics, and governance safety constraints. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline (superseded by v11.2.6 structure and determinism rules). |

---

<div align="center">

🚫 **KFM — Regression FAIL Fixtures (v11.2.6)**  
Strict Validation · Governance-Safe Negatives · Deterministic Failures

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Regression Fixtures](../README.md) ·
[⬅ Examples](../../README.md) ·
[🧾 OTel Fixtures](../../otel/README.md) ·
[🧩 Mapping Examples](../../mapping/README.md) ·
[🧾 Specs](../../../specs/README.md) ·
[🧪 Validators](../../../validators/README.md) ·
[📦 Storage](../../../storage/README.md) ·
[🗺️ Diagrams](../../../diagrams/README.md) ·
[⚙ Workflows Index](../../../../../workflows/README.md) ·
[⚙ Telemetry Export Workflow](../../../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../../../README.md) ·
[📘 Markdown Protocol](../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

