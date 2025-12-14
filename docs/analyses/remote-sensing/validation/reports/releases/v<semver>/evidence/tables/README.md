---
title: "📋 KFM — Release Validation Evidence Tables (v<semver>) · Aggregated · Deterministic · Governance-Safe"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/tables/README.md"

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

intent: "remote-sensing-validation-release-evidence-tables"
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

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:evidence:tables:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-evidence-tables-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/tables/README.md"
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

# 📋 **KFM — Release Validation Evidence Tables**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/tables/README.md`

**Purpose**  
This folder contains **small, aggregated tables** that support promotion decisions for **v<semver>**.
Tables here MUST remain **deterministic where feasible** and **governance-safe** for in-repo review.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Evidence Tables" src="https://img.shields.io/badge/Evidence-Tables-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Release evidence tables are curated, review-friendly exhibits that SHOULD help reviewers quickly verify:

- metric rollups and distribution summaries (overall + percentiles),
- threshold gate evaluations (pass/warn/fail, distance-to-threshold),
- drift/delta summaries vs baseline release (aggregate),
- support/coverage counts that justify the reported metrics.

Tables in this folder MUST NOT become a raw data channel. Keep them small, aggregated, and safe.

---

## 🗂️ Directory Layout (expected)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/tables/
├── 📄 README.md                                  — This policy/index
├── 📋 metrics_rollup.csv                          — Example: aggregate metrics (overall + p50/p90/p99)
├── 📋 thresholds_eval.csv                         — Example: threshold checks (metric, threshold, pass/fail)
├── 📋 support_counts.csv                          — Example: counts/coverage (items/tiles/timesteps)
├── 📋 drift_delta_summary.csv                     — Example: drift vs baseline (aggregate)
├── 📋 per_class_metrics.csv                       — Example: classification metrics by class (aggregate)
└── 📋 per_region_metrics.csv                      — Example: generalized region aggregates (policy-safe only)
~~~

Notes:

- Filenames are illustrative. Include only what the release produces.
- Every table SHOULD be registered in `../release_evidence_index.json` with a sha256 digest.

---

## ✅ Allowed table formats

Preferred:

- `CSV` (`.csv`) — diff-friendly and broadly readable

Allowed with care:

- `Parquet` (`.parquet`) — only for slightly larger *aggregated* tables
- `JSON` (`.json`) — for nested aggregates (keep stable key ordering)

Avoid:

- spreadsheets (`.xlsx`) in this directory,
- huge tables (store as governed assets and reference by stable id + digest).

---

## 🏷️ Naming conventions (recommended)

Use `snake_case` and keep names stable across releases.

Recommended patterns:

- `metrics_rollup.csv`
- `thresholds_eval.csv`
- `support_counts.csv`
- `drift_delta_summary.csv`
- `per_class_metrics.csv`
- `per_region_metrics.csv`

Avoid embedding:

- coordinates,
- restricted dataset identifiers,
- internal infrastructure paths,
- per-sample row keys when restricted inputs exist.

---

## 🎯 Determinism requirements (non-negotiable)

Tables SHOULD be reproducible from the same inputs + config snapshot:

- stable sort order:
  - sort by deterministic keys (e.g., `metric_name`, `class`, `region_id`) before writing,
- stable schema:
  - column names and column order remain stable across releases unless governed,
- stable numeric formatting:
  - explicit rounding policy (example: 6 decimals) and consistent application,
- stable null handling:
  - document whether null rows are omitted, retained, or filled.

If sampling is used anywhere upstream:

- tables MUST record sampling metadata either:
  - as explicit columns (recommended), or
  - as manifest metadata referenced from the release report.

Recommended sampling metadata fields:

- `sampling_mode` (`full|fixed_set|random|stratified|systematic`)
- `seed` (if applicable)
- `sample_size_total`
- `strata_key` and `sample_size_by_stratum` (if applicable)

---

## 🛡️ Governance and leakage rules (mandatory)

Tables can leak sensitive content via identifiers, small groups, or overly-specific breakdowns.

Rules:

- Do NOT include:
  - precise coordinates,
  - site identifiers,
  - per-sample tile ids or per-item lists when restricted inputs exist,
  - signed URLs, secrets, internal endpoints.
- For subgroup breakdowns (class, region, time bucket):
  - enforce minimum group sizes (policy-defined),
  - suppress low-support groups when they risk re-identification,
  - note suppression as counts and reason codes (no “what/where” detail).
- If governance status is unclear:
  - fail closed per policy and restrict output to high-level aggregates.

---

## ♿ Accessibility requirements (WCAG-aligned)

Every table artifact SHOULD have a caption available via:

- `../release_evidence_index.md` (human index), and/or
- `../release_evidence_index.json` (`caption` fields)

Captions SHOULD include:

- what metrics are included,
- aggregation scope (release-wide; baseline comparison if applicable),
- support basis (counts and sampling posture),
- threshold interpretation guidance where relevant.

---

## 🔗 Registration (release evidence index)

Every table SHOULD be registered in:

- `../release_evidence_index.json`

Each entry SHOULD include:

- `evidence_id`
- relative path (e.g., `tables/metrics_rollup.csv`)
- `sha256`
- producing `algorithm_ids`
- a short caption (human-readable; governance-safe)

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- if tables exist:
  - each table is listed in `../release_evidence_index.json`,
  - sha256 digests match,
  - size limits are respected,
  - leakage scans pass (no coordinates, no secrets, no signed URLs),
  - schema stability checks for gate-critical tables (`metrics_rollup`, `thresholds_eval`).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release evidence tables; defined allowed formats, naming conventions, determinism controls, governance-safe aggregation rules, and evidence index registration requirements. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Tables" src="https://img.shields.io/badge/Evidence-Tables-blue" />

[⬅ Evidence](../README.md) ·
[🧾 Evidence Index](../release_evidence_index.md) ·
[🧾 Evidence Index JSON](../release_evidence_index.json) ·
[📈 Plots](../plots/README.md) ·
[🗺️ Maps](../maps/README.md) ·
[🏷 Release Report](../../README.md) ·
[🏷 Releases Index](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🏃 Per-Run Reports](../../../../per-run/README.md) ·
[📅 Daily Reports](../../../../daily/README.md) ·
[🧩 Methods](../../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

