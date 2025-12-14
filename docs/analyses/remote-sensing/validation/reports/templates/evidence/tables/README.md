---
title: "📋 KFM — Remote Sensing Validation Evidence Table Templates (Metrics · Thresholds · Reason Codes)"
path: "docs/analyses/remote-sensing/validation/reports/templates/evidence/tables/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Template Pack"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "rs-validation-evidence-table-templates"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:templates:evidence:tables:v11.2.6"
semantic_document_id: "kfm-rs-validation-evidence-tables-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/templates/evidence/tables/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 📋 **KFM — Remote Sensing Validation Evidence Table Templates**
`docs/analyses/remote-sensing/validation/reports/templates/evidence/tables/README.md`

**Purpose**  
Define governed conventions for **evidence tables** embedded in remote-sensing validation reports (per-run, daily, release), emphasizing **stable ordering**, **deterministic rounding**, and **governance-safe aggregation**.

<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="Evidence Tables" src="https://img.shields.io/badge/Evidence-Tables-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Evidence tables are **machine-friendly and reviewer-friendly** artifacts used to summarize validation outcomes.

They are used to:

- report aggregate metrics and thresholds (pass/warn/fail),
- enumerate reason codes for failures,
- provide stable, auditable summaries for CI gates,
- support release promotion review without disclosing sensitive details.

This directory defines:

- table categories (what types are acceptable),
- stable sorting and rounding rules,
- recommended schemas/columns,
- governance posture (no per-sample leakage; no restricted identifiers).

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/templates/           — Report template pack (governed)
└── 📁 evidence/                                                      — Evidence template family (indexes + media)
    ├── 📁 tables/                                                    — Evidence table conventions (this directory)
    │   └── 📄 README.md                                              — This document
    ├── 📁 maps/                                                      — Evidence map conventions (high-risk; redaction rules)
    ├── 📁 plots/                                                     — Evidence plot conventions (deterministic bins/axes)
    └── 📁 indexes/                                                   — Evidence index templates (bind evidence to digests)
~~~

---

## 🧩 Table categories (recommended)

### 1) Metric summary tables (aggregate)

Use for continuous or categorical validation outputs:

- per dataset + algorithm aggregate metrics (RMSE/MAE/bias; precision/recall/F1),
- per region/tile-cohort aggregates (governance-safe scopes only),
- per time window aggregates (daily/weekly).

Minimum fields (recommended):

- `dataset_id`
- `algorithm_id`
- `scope_id` (region/cohort identifier; avoid sensitive ids)
- `time_start_utc`, `time_end_utc`
- `metric_name`, `metric_value`, `metric_unit`
- `rounding_policy`
- `created_utc`

### 2) Threshold gate tables (policy outcomes)

Use for CI and promotion decisions:

- thresholds applied,
- pass/warn/fail outcome,
- reason codes.

Minimum fields (recommended):

- `dataset_id`
- `algorithm_id`
- `gate_id`
- `threshold_name`, `threshold_value`, `comparison` (`<=`, `>=`)
- `observed_value`
- `outcome` (`pass|warn|fail`)
- `reason_codes` (pipe-delimited or JSON array; stable order)

### 3) Drift delta tables (release-to-release)

Use to compare a new release against baseline:

- counts changed (items/assets/tiles),
- metric deltas and percent deltas (aggregate),
- significance flags (if used, explain method and determinism).

Minimum fields (recommended):

- `baseline_version`, `target_version`
- `dataset_id`, `algorithm_id`
- `delta_name` (`rmse_delta`, `item_count_delta`, etc.)
- `delta_value`, `delta_unit`
- `delta_percent` (optional)
- `outcome` and `reason_codes`

### 4) Missingness and coverage tables

Use for operational health:

- expected vs delivered tiles/items,
- missingness fraction,
- coverage cohort counts.

Minimum fields (recommended):

- `dataset_id`
- `time_window`
- `expected_count`, `observed_count`, `missing_count`, `missing_fraction`
- `outcome` and `reason_codes`

---

## 🧷 File formats (recommended)

Preferred:

- `CSV` for small, review-grade tables (diff-friendly)
- `Parquet` for larger machine outputs (with a small CSV summary alongside)

Rules:

- If you publish Parquet, include a small CSV/MD summary for human review.
- Avoid Excel formats in governed report trees unless a specific workflow requires it.

---

## 🎯 Determinism requirements (non-negotiable)

Evidence tables MUST be reproducible:

- stable row ordering before write,
- stable string normalization (ids, scope labels),
- deterministic aggregation (explicit group keys),
- deterministic rounding policy (documented and applied consistently),
- stable serialization (CSV delimiter, quote behavior, newline convention).

### Stable sorting (required)

Use this recommended stable sort key order (when fields exist):

1. `dataset_id`
2. `algorithm_id`
3. `scope_id`
4. `time_start_utc`
5. `metric_name` (or `threshold_name` / `delta_name`)
6. `created_utc` (if needed; avoid when it breaks determinism)

If there are ties, define a final deterministic tiebreaker (`row_id` or `evidence_id`).

### Rounding policy (required)

Every table MUST declare:

- precision (e.g., 3 decimals),
- rounding mode (e.g., round-half-away-from-zero or round-half-to-even),
- any unit normalization rules.

Record this in:

- table caption (evidence index), and/or
- a `rounding_policy` column.

---

## 🛡️ Governance posture (mandatory)

Evidence tables MUST remain governance-safe:

- do not include precise coordinates,
- do not include restricted site ids,
- do not include per-sample or per-pixel record dumps in public report trees,
- avoid unique identifiers that enable re-identification.

If a detailed table is required for internal review:

- store it in a controlled location,
- publish only an aggregated summary table here,
- record the redaction decision in the evidence index and provenance.

---

## ♿ Accessibility requirements (WCAG-aligned)

For tables included in Markdown:

- include a short textual summary above the table,
- keep column names descriptive,
- avoid overly wide tables; link to CSV when needed.

For CSV artifacts:

- ensure headers are present,
- use consistent units and explicit encoding (UTF-8).

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- stable sorting (lint check),
- presence of required columns for gate tables,
- no forbidden patterns (coordinates, signed URLs, secrets),
- matching sha256 digests in the evidence index JSON.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed conventions for evidence tables (determinism, sorting/rounding policies, acceptable table categories, and governance-safe aggregation rules). |

---

<div align="center">

📋 **KFM — Remote Sensing Validation Evidence Table Templates**  
Stable Summaries · Deterministic Ordering · Governance-Safe Evidence

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📡 Validation](../../../../README.md) ·  
[🧾 Reports](../../../README.md) ·  
[🧩 Templates](../../README.md) ·  
[🧾 Evidence Templates](../README.md) ·  
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

