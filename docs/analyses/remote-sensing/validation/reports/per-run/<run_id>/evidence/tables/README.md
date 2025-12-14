---
title: "📋 KFM — Per-Run Validation Evidence Tables (Aggregated · Deterministic · Governance-Safe)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/tables/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Policy"
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

intent: "remote-sensing-validation-per-run-evidence-tables"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
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

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:evidence:tables:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-evidence-tables-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/tables/README.md"
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
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 📋 **KFM — Per‑Run Validation Evidence Tables**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/tables/README.md`

**Purpose**  
This folder stores **small, aggregated tables** for a single validation run (`<run_id>`).
Tables must remain **deterministic** and **governance-safe**, supporting review and release promotion without leaking sensitive content.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Tables" src="https://img.shields.io/badge/Evidence-Tables-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Tables in this folder are **review exhibits** that provide compact numeric support for validation outcomes.

They SHOULD answer:

- What metrics were computed and what are their aggregate values?
- Which thresholds were evaluated and what was the outcome?
- What is the support (counts/coverage) behind the metrics?
- If there are strata (classes/regions/time buckets), what are the aggregated results per stratum?

Tables MUST be:

- **aggregated** (no raw/pixel-level dumps),
- **small** (review-friendly),
- **deterministic** (stable sort + stable rounding),
- **governance-safe** (no restricted identifiers; no sensitive coordinates).

---

## 🗂️ Directory Layout (expected)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/tables/
├── 📄 README.md                               — This policy/index
├── 📋 metrics_rollup.csv                      — Example: aggregate metrics (overall + p50/p90/p99)
├── 📋 thresholds_eval.csv                     — Example: threshold checks (metric, threshold, pass/fail)
├── 📋 support_counts.csv                      — Example: counts/coverage (tiles/items/time steps)
├── 📋 per_class_metrics.csv                   — Example: classification aggregates (no per-sample rows)
├── 📋 per_region_metrics.csv                  — Example: generalized region aggregates (policy-safe only)
└── 📋 drift_delta_summary.csv                 — Example: release delta aggregates (counts + deltas)
~~~

Notes:

- Filenames are illustrative. Only include what you produce.
- Any file included here SHOULD be registered in `../evidence_index.json` with a sha256 digest.

---

## ✅ Allowed table formats

Preferred:

- `CSV` (`.csv`) — small, diff-friendly, and broadly readable
- `Parquet` (`.parquet`) — acceptable for slightly larger aggregated tables (keep small)
- `JSON` (`.json`) — acceptable for nested aggregates (keep stable ordering)

Avoid:

- Excel formats in this directory,
- huge tables (store as governed assets elsewhere and reference by digest).

---

## 🏷️ Naming conventions (recommended)

Use `snake_case` and keep names stable across runs.

Recommended patterns:

- `metrics_rollup.csv`
- `thresholds_eval.csv`
- `support_counts.csv`
- `per_class_metrics.csv`
- `per_region_metrics.csv`
- `drift_delta_summary.csv`

Avoid embedding:

- coordinates,
- restricted ids,
- ephemeral timestamps beyond run window naming if needed.

---

## 🎯 Determinism requirements (non-negotiable)

Tables SHOULD be reproducible:

- stable sort order:
  - sort by primary key columns (e.g., `metric_name`, `class`, `region_id`) deterministically,
- stable numeric formatting:
  - explicitly define rounding (e.g., 6 decimals) and apply consistently,
- stable null handling:
  - define and document whether nulls are omitted, retained, or filled,
- stable schema:
  - do not reorder columns across runs without governance review.

If the producing pipeline uses sampling:

- tables MUST include sampling metadata (seed or systematic rule id) either in:
  - a header row (CSV comment style) **if allowed by tooling**, or
  - a companion manifest referenced from `../evidence_index.json`.

---

## 🛡️ Governance and leakage rules (mandatory)

Do NOT include in any table:

- raw coordinates,
- tile ids or per-sample identifiers when restricted inputs exist,
- site-level or restricted identifiers,
- signed URLs, secrets, internal endpoints.

For spatial breakdowns:

- use generalized scopes only (region bins or H3 generalized cells),
- enforce minimum group sizes before publishing per-group metrics (policy-defined),
- prefer counts and aggregates rather than listing entities.

---

## 🔗 Registration in the evidence index

Every table SHOULD be referenced from:

- `../evidence_index.json`

Each entry SHOULD include:

- `evidence_id`
- relative path (e.g., `tables/metrics_rollup.csv`)
- `sha256`
- producing `algorithm_ids`
- a short caption
- governance posture summary if relevant

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- table files are optional, but if present:
  - every table is listed in `../evidence_index.json`,
  - sha256 digests match,
  - size limits are respected,
  - leakage scans pass (no coords, no secrets, no signed URLs),
  - stable schema rules (column set and order) for gate tables.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for per-run evidence tables; defined allowed formats, naming conventions, determinism controls, and governance-safe aggregation posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Tables" src="https://img.shields.io/badge/Evidence-Tables-blue" />

[⬅ Evidence](../README.md) ·
[🧾 Evidence Index](../evidence_index.json) ·
[📊 Plots](../plots/README.md) ·
[🏃 Run Bundle](../../README.md) ·
[🧾 Manifests](../../manifests/README.md) ·
[🧬 Provenance](../../provenance/README.md) ·
[📎 Attachments](../../attachments/README.md) ·
[🧾 Per-Run Reports](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🧩 Methods](../../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

