---
title: "✅ Kansas Frontier Matrix — Metadata Validation Telemetry: Checks (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/checks/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/metadata-validation-checks-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/metadata-validation-checks-v11.2.6.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "telemetry-metadata-validation-checks"
  applies_to:
    - "docs/**"
    - "schemas/**"
    - "data/**"
    - ".github/workflows/docs-lint.yml"
    - ".github/workflows/schema-lint.yml"
    - ".github/workflows/stac-validate.yml"
    - ".github/workflows/faircare-validate.yml"
    - ".github/workflows/telemetry-export.yml"
    - "tools/**"
  non_goals:
    - "Defining badge rules (see docs/telemetry/metadata-validation/badges/README.md)"
    - "Defining footer rules (see docs/telemetry/metadata-validation/footers/* if present)"
    - "Replacing per-workflow specifications under docs/workflows/*"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Validation telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Metadata Validation Checks Telemetry v12"

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
  - "docs/telemetry/metadata-validation/checks/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metadata-validation:checks:v11.2.6"
semantic_document_id: "kfm-telemetry-metadata-validation-checks-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metadata-validation:checks:v11.2.6"
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
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/telemetry-export.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

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

# ✅ **Kansas Frontier Matrix — Metadata Validation Telemetry: Checks**
`docs/telemetry/metadata-validation/checks/README.md`

**Purpose**  
Define the **check taxonomy** and **telemetry semantics** for KFM metadata validation across docs, schemas, and catalogs.  
This standard ensures that validation outcomes are **portable, queryable, and governance-ready** (FAIR+CARE aligned) across CI workflows.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Metadata_Validation%3A_Checks-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. What this document standardizes

KFM runs many validations across the pipeline:

- Documentation linting (`docs-lint.yml`)
- Schema linting (`schema-lint.yml`)
- STAC/DCAT/PROV validation (`stac-validate.yml`)
- FAIR+CARE governance validation (`faircare-validate.yml`)
- Supply-chain and other governed checks

Each workflow produces reports, but governance requires **consistent, cross-workflow telemetry**.

This README defines:

- A **check ID namespace** (stable identifiers),
- A **result and severity model** (pass/warn/fail/skip),
- A minimal telemetry shape for check outcomes,
- A mapping approach for converting tool-specific results into KFM check events.

### 2. Guiding principles (normative)

Metadata validation checks MUST be:

- **Deterministic** for a given commit + config set.
- **Machine-joinable** across workflows (stable `check_id`, stable `doc_path` / `dataset_id` references).
- **Governance-safe**:
  - no secrets,
  - no PII,
  - no sensitive coordinates,
  - aggregated where appropriate.
- **Actionable**: failure events must include a short remediation hint or link to the authoritative spec.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 metadata-validation/
        ├── 📁 checks/
        │   └── 📄 README.md                                     # ← This standard (check taxonomy + telemetry semantics)
        ├── 📁 badges/
        │   └── 📄 README.md                                     # Badge-specific rules + telemetry
        ├── 📁 footers/                                          # Optional: footer telemetry/rules (if present)
        │   └── 📄 README.md
        └── 📄 README.md                                         # Optional: metadata-validation root index (if present)

📁 schemas/
└── 📁 telemetry/
    └── 🧾 metadata-validation-checks-v11.2.6.json               # Canonical schema for check telemetry

📁 reports/
└── 📁 self-validation/
    └── 📁 metadata-validation/
        └── 📁 checks/
            ├── 📄 check_results.json                            # Expanded check results (per target)
            ├── 📄 lint_summary.json                             # Canonical machine-readable summary
            └── 📄 summary.md                                    # Human-readable summary for PRs

📁 releases/
└── 📁 v11.2.6/
    └── 🧾 metadata-validation-checks-telemetry.json             # Aggregated check telemetry for the release

📁 tools/
└── 📁 validation/
    ├── ✅ emit_check_telemetry.py                               # Converts reports → telemetry events (recommended)
    └── ✅ normalize_check_ids.py                                # Ensures stable IDs across tools (recommended)
~~~

---

## 🧭 Context

### 1. Where checks sit in the KFM pipeline

Metadata validation checks span the full pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → Frontend → Story Nodes → Focus Mode

They exist to ensure that:

- catalogs are consistent and ingestible,
- governance metadata exists (license, provenance, CARE tags),
- downstream systems can trust contracts and schemas,
- changes remain auditable across releases.

### 2. Relationship to other telemetry streams

This telemetry stream is **check-centric** and intentionally generic.

Specialized telemetry lives elsewhere, for example:

- badges telemetry (badge parsing & ordering),
- front-matter validation telemetry,
- STAC/DCAT validation telemetry,
- AI training telemetry, etc.

The rule is:

- Specialized streams can exist,
- but they SHOULD still map to `check_id` events defined here for cross-dashboard continuity.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Workflow reports (lint/schema/STAC/FAIR+CARE)"] --> B["Normalize to check outcomes"]
  B --> C["Emit check telemetry (run + target events)"]
  C --> D["Merge into release telemetry snapshot"]
  D --> E["Governance dashboards + graph ingest"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Nodes

Check telemetry can create Story Nodes such as:

- `urn:kfm:story-node:telemetry:metadata-validation:checks:<run_id>`

Nodes can summarize:

- total checks run,
- failure counts by severity,
- recurring failure classes,
- most impacted directories/domains.

### 2. Focus Mode behavior (normative)

Focus Mode MAY:

- summarize check trends over time,
- show what checks gate a doc/dataset,
- link to summaries and authoritative specs.

Focus Mode MUST NOT:

- invent failures or “auto-fix” claims,
- reclassify severity without recorded evidence,
- disclose sensitive payloads that are not present in telemetry.

---

## 🧪 Validation & CI/CD

### 1. Check event model (normative)

Each check result MUST map to:

- `result`: one of
  - `pass`
  - `warn`
  - `fail`
  - `skip`
- `severity`: one of
  - `info`
  - `warning`
  - `error`
- `scope`: one of
  - `run` (applies to workflow run)
  - `document` (doc_path)
  - `dataset` (dataset_id)
  - `schema` (schema_id)
  - `artifact` (artifact_path)

A `fail` result MUST have `severity: error`.

### 2. Check ID namespace (normative)

`check_id` MUST follow:

~~~text
kfm.<domain>.<topic>.<rule>
~~~

Examples:

- `kfm.docs.frontmatter.required_fields`
- `kfm.docs.headings.approved_h2_registry`
- `kfm.docs.links.internal_resolves`
- `kfm.schemas.jsonschema.valid_schema`
- `kfm.schemas.shacl.constraints_pass`
- `kfm.catalogs.stac.items_validate`
- `kfm.catalogs.dcat.distributions_complete`
- `kfm.gov.faircare.care_tag_present`
- `kfm.gov.faircare.sovereignty_restrictions_applied`

### 3. Suggested gating policy

Each workflow defines its own gating, but the following is recommended:

- Any `severity: error` event:
  - fails protected-branch checks (unless explicitly waived).
- `warning` events:
  - allowed but surfaced in PR summaries and dashboards.

Waivers MUST be:

- explicit,
- time-bound,
- recorded in a governance artifact (not only in logs).

---

## 📦 Data & Metadata

### 1. Telemetry shapes

This stream supports:

1) **Run summary event** (`metadata_check_run`)
- one per workflow run, aggregated counters

2) **Target check event** (`metadata_check_target`)
- one per doc/schema/dataset artifact where a meaningful failure/warn occurred
- MAY emit pass events for strict auditing (configurable)

### 2. Minimum telemetry fields

Run summary SHOULD include:

- `workflow`
- `event_type`
- `run_id`
- `schema_version`
- `checks_total`
- `checks_failed`
- `checks_warned`
- `targets_checked` (docs/schemas/datasets as applicable)
- `workflow_duration_sec`
- `energy_wh`
- `carbon_gco2e`
- `timestamp`

Target event SHOULD include:

- `workflow`
- `event_type`
- `run_id`
- `schema_version`
- `check_id`
- `result`
- `severity`
- a target reference:
  - `doc_path` OR `dataset_id` OR `schema_id` OR `artifact_path`
- `message` (short)
- `spec_ref` (relative link to authoritative doc if available)
- `timestamp`

### 3. Example telemetry entries (schematic)

~~~json
{
  "workflow": "docs-lint",
  "event_type": "metadata_check_run",
  "run_id": "docs-lint_2025-12-11T20-05-00Z",
  "schema_version": "v11.2.6",
  "checks_total": 42,
  "checks_failed": 1,
  "checks_warned": 3,
  "targets_checked": 312,
  "workflow_duration_sec": 55,
  "energy_wh": 2.1,
  "carbon_gco2e": 0.0008,
  "timestamp": "2025-12-11T20:05:55Z"
}
~~~

~~~json
{
  "workflow": "docs-lint",
  "event_type": "metadata_check_target",
  "run_id": "docs-lint_2025-12-11T20-05-00Z",
  "schema_version": "v11.2.6",
  "check_id": "kfm.docs.frontmatter.required_fields",
  "result": "fail",
  "severity": "error",
  "doc_path": "docs/telemetry/metadata-validation/checks/README.md",
  "message": "Missing required front-matter keys: governance_ref, license.",
  "spec_ref": "docs/standards/kfm_markdown_protocol_v11.2.6.md",
  "timestamp": "2025-12-11T20:05:12Z"
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Model this telemetry stream as a DCAT Dataset:

- `dct:title`: "KFM Metadata Validation Telemetry — Checks"
- Distributions:
  - release telemetry JSON (`metadata-validation-checks-telemetry.json`)
  - per-run summaries (`lint_summary.json`, `summary.md`)
  - expanded results (`check_results.json`)

### 2. STAC

Optional pattern:

- Collection: `kfm-ci-metadata-validation`
- Item per run: `metadata-validation-checks-<run_id>`
- Assets: telemetry JSON and summary outputs (`geometry: null`).

### 3. PROV-O

- Activity: `ex:MetadataValidationRun_<run_id>`
- Used: repo state at commit SHA, configs, referenced schemas
- Generated: check outputs and telemetry snapshot
- Agents: CI bot / runner as `prov:SoftwareAgent`.

---

## 🧱 Architecture

### 1. Normalization pipeline

Metadata validation checks are normalized from heterogeneous sources:

- markdownlint, link checkers
- JSON Schema validators
- SHACL engines
- STAC/DCAT validators
- FAIR+CARE auditors

Each produces a tool-native report, then KFM emits:

- a canonical **summary JSON**,
- a canonical **check telemetry stream**.

### 2. Determinism

Determinism requires:

- tool versions pinned,
- configs versioned,
- stable ordering for emitted check events.

If a tool uses probabilistic sampling, it MUST:

- declare its seed,
- log sampling parameters,
- mark affected checks with a `sampling: true` flag (schema permitting).

---

## ⚖ FAIR+CARE & Governance

Check telemetry is governance evidence and must be:

- **FAIR**:
  - findable (stable IDs, stable paths),
  - accessible (where policy allows),
  - interoperable (standard schema),
  - reusable (versioned, provenance-linked).
- **CARE**:
  - protects community interests by enforcing safe metadata,
  - respects authority to control (sovereignty flags),
  - avoids leaking sensitive content in telemetry.

Where checks identify sensitive materials, telemetry SHOULD:

- record only counts and categories,
- provide links to internal reports rather than embedding content.

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                 |
|----------:|-----------:|---------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`   | Built from scratch: check ID taxonomy, event model, telemetry shapes, and governance-safe normalization guidance. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`   | Prior baseline guidance (superseded by v11.2.6 rewrite).                |

---

<div align="center">

✅ **KFM — Metadata Validation Telemetry: Checks (v11.2.6)**  
Stable Check IDs · Portable Validation Results · Governance-Ready Telemetry

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Checks-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Metadata Validation Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[🏷 Badges Telemetry](../badges/README.md) ·
[⚙ Workflows Index](../../../workflows/README.md) ·
[🧪 Docs Lint Workflow](../../../workflows/docs-lint.yml.md) ·
[🧩 Schema Lint Workflow](../../../workflows/schema-lint.yml.md) ·
[🗺 STAC Validate Workflow](../../../workflows/stac-validate.yml.md) ·
[⚖ FAIR+CARE Validate Workflow](../../../workflows/faircare-validate.yml.md) ·
[⚙ Telemetry Export Workflow](../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../README.md) ·
[📘 Markdown Protocol](../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω  

</div>