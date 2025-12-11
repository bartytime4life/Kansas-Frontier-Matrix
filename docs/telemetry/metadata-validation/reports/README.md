---
title: "📊 Kansas Frontier Matrix — Metadata Validation Telemetry: Reports (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/reports/README.md"

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

telemetry_ref: "../../../../releases/v11.2.6/metadata-validation-reports-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/metadata-validation-reports-v11.2.6.json"
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
  - "mermaid-timeline-v1"

scope:
  domain: "telemetry-metadata-validation-reports"
  applies_to:
    - "reports/**"
    - "reports/self-validation/**"
    - "reports/faircare/**"
    - "docs/telemetry/metadata-validation/**"
    - ".github/workflows/docs-lint.yml"
    - ".github/workflows/schema-lint.yml"
    - ".github/workflows/stac-validate.yml"
    - ".github/workflows/faircare-validate.yml"
    - ".github/workflows/telemetry-export.yml"
    - "scripts/emit_telemetry.py"
    - "scripts/merge_telemetry.py"
    - "tools/**"
    - "schemas/telemetry/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Validation reports and telemetry; low-risk when summarized and redacted"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Metadata Validation Telemetry Reports v12"

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
  - "docs/telemetry/metadata-validation/reports/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metadata-validation:reports:v11.2.6"
semantic_document_id: "kfm-telemetry-metadata-validation-reports-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metadata-validation:reports:v11.2.6"
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
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
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

# 📊 **Kansas Frontier Matrix — Metadata Validation Telemetry: Reports**
`docs/telemetry/metadata-validation/reports/README.md`

**Purpose**  
Define the **canonical report artifacts** emitted by metadata validation workflows (docs, schemas, catalogs, FAIR+CARE),  
and how those reports are normalized into **governance-ready telemetry** for release snapshots, dashboards, and graph ingestion.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Metadata_Validation%3A_Reports-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. What counts as a “report” in metadata validation

A **metadata validation report** is a machine-readable artifact that records:

- **what was validated** (targets, paths, IDs),
- **which rules were applied** (stable `check_id`s),
- **what happened** (pass/fail, severity, counts),
- **why** (reason codes/messages, safely redacted),
- **how to reproduce** (workflow, config refs, commit SHA).

Reports are distinct from telemetry:

- **Reports** contain detailed per-target results (or a canonical summary of those results).
- **Telemetry** is the normalized event stream derived from reports and merged into release snapshots.

### 2. Why this layer exists

This reports standard exists so that:

- Different validators can write different raw outputs, but still produce:
  - a stable summary,
  - stable check IDs,
  - a consistent governance trail.
- Governance systems can query:
  - “What failed?”,
  - “Which rule?”,
  - “Which workflow run?”,
  without parsing tool-native logs.

### 3. Normative constraints

Metadata validation reports MUST:

- be safe to publish under the document’s classification and governance constraints,
- avoid embedding secrets, tokens, or raw PII,
- avoid leaking restricted or culturally sensitive coordinates or feature identifiers,
- be deterministic for a given commit + config + inputs (no random ordering or unstable IDs).

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 metadata-validation/
        ├── 📁 badges/
        │   └── 📄 README.md                           — Badge rules + badge telemetry semantics
        ├── 📁 checks/
        │   └── 📄 README.md                           — Check taxonomy + check_id registry
        ├── 📁 ci/
        │   └── 📄 README.md                           — CI integration + merge contract
        └── 📁 reports/
            └── 📄 README.md                           — ← This document (report artifact contract)

📁 reports/
└── 📁 self-validation/
    ├── 📁 docs/
    │   ├── 📄 lint_summary.json                       — Canonical docs lint summary (machine-readable)
    │   └── 📄 summary.md                              — Human summary (optional)
    ├── 📁 schemas/
    │   ├── 📄 lint_summary.json                       — Canonical schema lint summary
    │   └── 📄 summary.md                              — Human summary (optional)
    ├── 📁 stac/
    │   ├── 📄 stac_summary.json                       — Canonical STAC/DCAT/PROV validation summary
    │   └── 📄 summary.md                              — Human summary (optional)
    └── 📁 metadata-validation/
        └── 📁 reports/
            ├── 📄 reports_index.json                  — Optional: cross-workflow report index (single run)
            └── 📄 summary.md                          — Optional: PR-friendly roll-up summary

📁 reports/
└── 📁 faircare/
    ├── 📄 faircare_summary.json                       — FAIR+CARE audit summary (machine-readable)
    ├── 📄 pii_scan.json                               — PII/sensitivity scan findings (redacted)
    └── 📄 provenance_trace.json                       — Lineage/provenance trace (PROV-friendly)

📁 schemas/
└── 📁 telemetry/
    ├── 🧾 metadata-validation-reports-v11.2.6.json     — Telemetry schema derived from reports
    ├── 🧾 metadata-validation-checks-v11.2.6.json      — Check-level telemetry schema
    └── 🧾 metadata-validation-ci-v11.2.6.json          — CI integration telemetry schema

📁 releases/
└── 📁 v11.2.6/
    ├── 🧾 metadata-validation-reports-telemetry.json   — Release-pinned telemetry derived from reports
    ├── 🧾 metadata-validation-checks-telemetry.json    — Release-pinned check events (optional)
    ├── 🧾 metadata-validation-ci-telemetry.json        — Release-pinned CI merge evidence (optional)
    └── 📦 manifest.zip                                 — Release manifest (hashes, refs, attestations)
~~~

---

## 🧭 Context

### 1. Where reports come from

Reports are produced by governed validation workflows, typically:

- `docs-lint.yml` → `reports/self-validation/docs/lint_summary.json`
- `schema-lint.yml` → `reports/self-validation/schemas/lint_summary.json`
- `stac-validate.yml` → `reports/self-validation/stac/stac_summary.json`
- `faircare-validate.yml` → `reports/faircare/faircare_summary.json` (and related artifacts)

This directory documents the *report contract* for metadata validation, regardless of which workflow produced the report.

### 2. How reports become telemetry

Telemetry emission is a deterministic transformation:

- canonical summary report(s)
  → normalized telemetry events
  → merged release snapshot(s)

This layer must remain stable across releases to support governance trend analysis.

---

## 🗺️ Diagrams

### 1. Report → Telemetry pipeline

~~~mermaid
flowchart LR
  A["Workflow validation runs"] --> B["Tool-native outputs"]
  B --> C["Canonical summary report"]
  C --> D["Telemetry emitted from summary"]
  D --> E["Release snapshot updated"]
  E --> F["Dashboards / catalogs / graph ingest"]
~~~

### 2. Timeline: single PR validation cycle

~~~mermaid
timeline
  title Metadata Validation Reports — CI Lifecycle
  section PR
    T0 : PR opened or updated
    T1 : Validation workflows run and write reports
  section Normalization
    T2 : Canonical summaries produced
    T3 : Telemetry emitted from summaries
  section Governance
    T4 : Telemetry merged into release snapshot
    T5 : Dashboards and governance review consume evidence
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Report-derived Story Nodes

Reports can produce Story Nodes like:

- `urn:kfm:story-node:telemetry:metadata-validation:reports:<run_id>`

Recommended Story Node fields to summarize:

- totals by severity (`errors`, `warnings`, `info`),
- top failing `check_id`s,
- affected paths or collections (without leaking restricted details),
- links to canonical summary artifacts.

### 2. Focus Mode behavior (normative)

Focus Mode MAY:

- summarize report outcomes across workflows (docs/schema/stac/faircare),
- surface remediation links by `check_id`,
- show trends across releases.

Focus Mode MUST NOT:

- embed sensitive report payloads,
- “fix” results or reclassify severities,
- infer compliance where no report evidence exists.

---

## 🧪 Validation & CI/CD

### 1. Canonical report types (normative)

A workflow that participates in metadata validation reporting MUST emit at least one of:

- **Canonical summary JSON**  
  - filename pattern: `*_summary.json` or `lint_summary.json`
  - location: under `reports/self-validation/**` or `reports/<workflow-family>/**`

Optionally, it MAY emit:

- **Human summary Markdown** (`summary.md`) for PR readability
- **Detailed per-target JSON** (tool-specific) as long as:
  - it is redacted,
  - it does not replace canonical summary requirements.

### 2. Required fields for canonical summary JSON (normative)

A canonical summary JSON MUST include:

- `report_kind` (e.g., `docs_lint`, `schema_lint`, `stac_validate`, `faircare_validate`)
- `workflow` (workflow name / identifier)
- `run_id`
- `commit_sha`
- `schema_version` (e.g., `v11.2.6`)
- `status` (`pass` | `fail` | `partial`)
- `counts` (at minimum: total checked + totals by severity)
- `violations[]` (zero or more, with stable `check_id` references)

It SHOULD include:

- `started_at`, `ended_at`
- `duration_sec`
- `inputs` (paths, dataset refs, config refs)
- `artifacts` (paths written by the workflow)
- `checksums` (optional: sha256 for canonical outputs)

### 3. Stable check IDs (normative)

Every `violations[]` element MUST reference a stable `check_id` defined in:

- `docs/telemetry/metadata-validation/checks/README.md`

If a tool does not provide stable IDs, the workflow SHOULD normalize tool-native rule IDs into the KFM registry before writing the canonical summary.

---

## 📦 Data & Metadata

### 1. Example canonical summary (schematic)

~~~json
{
  "schema_version": "v11.2.6",
  "report_kind": "docs_lint",
  "workflow": "docs-lint",
  "run_id": "docs-lint_2025-12-11T18:02:11Z",
  "commit_sha": "<latest-commit-hash>",
  "status": "fail",
  "counts": {
    "targets_checked": 286,
    "errors": 2,
    "warnings": 9,
    "info": 0
  },
  "violations": [
    {
      "check_id": "MDP.H2.REGISTRY",
      "severity": "error",
      "target_path": "docs/telemetry/metadata-validation/reports/README.md",
      "message": "Disallowed H2 heading detected (must match approved registry).",
      "rule_ref": "docs/telemetry/metadata-validation/checks/README.md#mdp-h2-registry"
    }
  ],
  "artifacts": [
    "reports/self-validation/docs/markdownlint.txt",
    "reports/self-validation/docs/lint_summary.json",
    "reports/self-validation/docs/summary.md"
  ],
  "timestamp": "2025-12-11T18:02:11Z"
}
~~~

### 2. Redaction and safety requirements (normative)

Canonical summaries MUST NOT include:

- raw secrets or detected token strings,
- full PII payloads,
- restricted coordinates or sensitive cultural site identifiers,
- unbounded stack traces that could embed environment details.

When a violation needs to reference sensitive material:

- record the `check_id`,
- record a redacted message,
- optionally record a safe pointer to an internal artifact location (policy-controlled),
- do not embed the sensitive string or coordinate.

### 3. Report hashing (recommended)

For integrity and governance traceability, canonical report files SHOULD include:

- `doc_integrity_checksum` in their own front-matter (when the report is Markdown),
- or a `checksums` object in summary JSON,
- and be included in release manifests and attestation references where applicable.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT modeling

Reports can be modeled as a DCAT dataset series:

- `dcat:Dataset`
  - “KFM Metadata Validation Reports”
- `dcat:Distribution`
  - `lint_summary.json`, `stac_summary.json`, `faircare_summary.json`
  - `mediaType`: `application/json`
  - `spdx:checksum`: sha256

### 2. STAC modeling (optional)

- Collection: `kfm-ci-metadata-validation`
- Items: one per `run_id`
- Assets:
  - canonical summaries,
  - human summaries (optional),
  - telemetry event files (optional)
- `geometry: null` (non-spatial)

### 3. PROV-O modeling

- Activity:
  - `ex:MetadataValidationRun_<run_id>` (`prov:Activity`)
- Used:
  - repo snapshot at `commit_sha`,
  - config refs,
  - dataset refs (when applicable)
- Generated:
  - canonical summary report(s),
  - telemetry event file(s)
- Agent:
  - CI runner (`prov:SoftwareAgent`)

This provides a complete lineage chain from commit → validation run → report → telemetry → release snapshot.

---

## 🧱 Architecture

### 1. Separation of concerns

- Validators and linters write tool-native outputs.
- Workflow summarizers create canonical summaries.
- Telemetry emitters transform summaries into normalized telemetry.
- Merge step appends telemetry to release snapshots.

This separation prevents “report drift” and keeps governance evidence stable.

### 2. Determinism and ordering

To prevent telemetry/report drift:

- canonical summary JSON MUST sort:
  - violations by (`severity`, `check_id`, `target_path`) or another deterministic key,
  - artifacts list lexicographically.
- telemetry emission MUST be deterministic for the same inputs.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

- **Findable**: stable locations (`reports/**`, `releases/**`) and stable IDs (`run_id`, `check_id`)
- **Accessible**: summaries are readable and exportable; raw details may be policy-restricted
- **Interoperable**: schemas govern shape; mapping to DCAT/STAC/PROV is defined
- **Reusable**: release-pinned snapshots allow longitudinal analysis

### 2. CARE / Sovereignty safety

Even “technical” reports can leak sensitive context. This standard therefore enforces:

- redaction-first reporting,
- safe pointer patterns rather than embedding sensitive strings,
- sovereignty policy compliance for any geo/cultural content implicated in metadata validation.

---

## 🕰️ Version History

| Version   | Date       | Author       | Summary                                                                 |
|----------:|-----------:|--------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`  | Built from scratch: canonical report artifact contract for metadata validation; defined required fields, redaction rules, deterministic ordering, and DCAT/STAC/PROV alignment. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`  | Prior baseline guidance (superseded by v11.2.6 rewrite).                |

---

<div align="center">

📊 **KFM — Metadata Validation Telemetry: Reports (v11.2.6)**  
Canonical Summaries · Deterministic Evidence · Governance-Ready Telemetry

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Metadata Validation Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[✅ Checks](../checks/README.md) ·
[🏷 Badges](../badges/README.md) ·
[🏗 CI Integration](../ci/README.md) ·
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