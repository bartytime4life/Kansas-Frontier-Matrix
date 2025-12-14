---
title: "📅 KFM — Remote Sensing Validation Daily Reports (YYYY Index)"
path: "docs/analyses/remote-sensing/validation/reports/daily/YYYY/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
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

intent: "remote-sensing-validation-daily-reports-year-index"
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

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:year-index:YYYY:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-daily-reports-YYYY"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/YYYY/README.md"
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

# 📅 **KFM — Remote Sensing Validation Daily Reports (YYYY)**
`docs/analyses/remote-sensing/validation/reports/daily/YYYY/README.md`

**Purpose**  
Year index and conventions for **daily** remote-sensing validation report artifacts produced by KFM.
This folder organizes daily rollups used for ops visibility, governance review, and release promotion evidence.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory holds **daily validation rollups** for a single calendar year.

Replace `YYYY` in the path with a real 4-digit year (e.g., `2025`, `2026`).

Daily rollups SHOULD:

- summarize per-day validation outcomes (`pass|warn|fail`) for governed algorithms,
- record deterministic support counts (items/tiles/pixels/time steps where applicable),
- include stable reason codes for non-pass outcomes,
- link to governed artifacts via references:
  - STAC Items for validation/report assets,
  - PROV-O bundles and/or OpenLineage event refs,
  - optional detailed report artifacts (stored as assets, not embedded here).

Daily rollups MUST remain governance-safe:

- no raw coordinates,
- no restricted identifiers or “how to locate” content,
- no signed URLs, secrets, or internal endpoints.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/daily/
└── 📁 YYYY/                                                   — One year of daily rollups (this directory)
    ├── 📄 README.md                                           — This year index (you are here)
    ├── 📁 01/                                                 — January
    │   ├── 📄 YYYY-01-01.summary.json                          — Daily summary (machine)
    │   ├── 📄 YYYY-01-01.summary.md                            — Daily summary (human, optional)
    │   └── 📄 YYYY-01-01.refs.json                             — STAC/DCAT/PROV refs (optional)
    ├── 📁 02/
    └── 📁 12/
~~~

Notes:

- Month folders keep directory sizes manageable.
- If a day has multiple products, keep the day as one “rollup” summary and link to per-product detail via STAC assets and provenance refs.

---

## 🧾 File naming conventions (enforced)

### Daily summary (recommended)

- Machine-readable: `YYYY-MM-DD.summary.json`
- Human-readable (optional): `YYYY-MM-DD.summary.md`

### Optional reference-only file

- `YYYY-MM-DD.refs.json`

Use references instead of embedding large tables:

- STAC Item ids/hrefs for daily outputs
- PROV bundle refs for lineage
- (Optional) OpenLineage run ids

---

## ✅ Minimum content for a daily summary

A daily summary SHOULD include:

- day identifier and UTC window,
- algorithm families executed,
- per-family outcomes:
  - `pass|warn|fail`,
  - key metric values (aggregated),
  - threshold results,
  - reason codes,
  - support counts,
- governance posture:
  - CARE gate status,
  - sovereignty gate status,
  - redaction summary counts (if any),
- references:
  - STAC Item ids for the day,
  - PROV bundle refs,
  - config snapshot refs/hashes,
  - input pack digests (as refs/hashes).

---

## 🎯 Determinism and comparability rules

Daily reports MUST be comparable across time:

- stable enumeration:
  - stable ordering for ids before hashing/aggregation,
- pinned configs:
  - thresholds, masks, sampling policies referenced via config snapshot digests,
- pinned sampling:
  - if sampling used, record:
    - `frame_hash_sha256`,
    - seed (or systematic rule),
    - selected count and candidate count,
- stable reason codes:
  - deterministic tie-breaking for multi-failure cases.

---

## 🛡️ FAIR+CARE and sovereignty posture

Daily reports must be safe by default:

- report only generalized spatial scope (region/coarse grid) when needed,
- do not disclose per-sample lists for restricted collections,
- if governance is unclear:
  - fail closed (per policy) and require review,
  - record `care_gate_status` and `sovereignty_gate` explicitly.

---

## 🧪 CI/CD expectations (recommended)

Daily report directories support CI checks such as:

- file naming conventions,
- schema validation for `*.summary.json` payloads (when schema exists),
- required field checks (outcome, reason codes, refs),
- governance leakage scans (no coordinates, no secrets),
- deterministic reproduction checks (when a sample manifest exists and can be regenerated).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed year-index template for daily remote-sensing validation reports; standardized layout, naming conventions, determinism rules, and governance posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />

[⬅ Daily Reports](../README.md) ·
[🧾 Reports Index](../../README.md) ·
[🧾 Per-Run Reports](../../per-run/README.md) ·
[🏷 Release Reports](../../releases/README.md) ·
[🧩 Methods](../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

