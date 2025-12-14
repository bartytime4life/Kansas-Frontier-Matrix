---
title: "🗓️ KFM — Remote Sensing Validation Daily Reports (YYYY-MM Index)"
path: "docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/README.md"

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

intent: "remote-sensing-validation-daily-reports-month-index"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:month-index:YYYY-MM:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-daily-reports-YYYY-MM"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/README.md"
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

# 🗓️ **KFM — Remote Sensing Validation Daily Reports (YYYY‑MM)**
`docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/README.md`

**Purpose**  
Month index and conventions for **daily** validation rollups for KFM remote-sensing outputs.
This directory organizes daily summaries for a given month and links to governed evidence artifacts (STAC/PROV).

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory is the **month index** for daily validation rollups.

Replace placeholders:

- `YYYY` = 4-digit year (e.g., `2025`)
- `MM` = 2-digit month (e.g., `01`, `12`)

Daily rollups in this folder:

- summarize per-day outcomes (`pass|warn|fail`) across governed algorithms,
- record stable support counts and deterministic reason codes,
- link to provenance bundles and catalog artifacts (STAC/DCAT/PROV),
- remain safe for publication (no sensitive leakage).

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/
├── 📄 README.md                                              — This month index (you are here)
├── 📄 YYYY-MM-01.summary.json                                 — Daily summary (machine)
├── 📄 YYYY-MM-01.summary.md                                   — Daily summary (human, optional)
├── 📄 YYYY-MM-01.refs.json                                    — STAC/DCAT/PROV refs (optional)
├── 📄 YYYY-MM-02.summary.json
├── 📄 YYYY-MM-02.summary.md
├── 📄 YYYY-MM-02.refs.json
└── …
~~~

Notes:

- Keep one summary per day. If multiple products run, aggregate and reference detailed artifacts via STAC assets.
- If a day does not run (scheduled downtime), record a summary with an explicit reason code (e.g., `SCHEDULED_DOWNTIME`) and `outcome = "warn"` (or policy-defined).

---

## ✅ Minimum daily summary contents (recommended)

Each `YYYY-MM-DD.summary.json` SHOULD include:

- day and UTC window,
- algorithm families executed,
- outcomes and reason codes,
- key aggregate metrics and threshold results,
- support counts (items/tiles/pixels/time steps),
- sampling metadata (if sampling used):
  - frame hash, seed/systematic rule, selected vs candidate counts,
- governance posture:
  - CARE gate status, sovereignty gate status, redaction summary,
- references:
  - STAC ids/hrefs,
  - PROV bundle refs,
  - config snapshot refs/digests,
  - input pack refs/digests.

---

## 🎯 Determinism rules (enforced posture)

Daily summaries MUST be comparable across time:

- stable ordering for ids and arrays before hashing or aggregation,
- pinned configs and thresholds referenced by digest,
- deterministic selection when sampling is used,
- deterministic reason code selection and ordering.

---

## 🛡️ FAIR+CARE and sovereignty posture

Daily reports MUST not embed:

- raw coordinates,
- restricted site identifiers,
- signed URLs, secrets, internal endpoints.

When restricted inputs exist:

- aggregate only (region/coarse grid),
- set explicit `care_gate_status` and `sovereignty_gate`,
- include redaction counts and reason codes,
- store detailed traces only as governed artifacts referenced by STAC/PROV.

---

## 🧪 CI/CD expectations (recommended)

Month-level validation can include:

- naming convention checks (`YYYY-MM-DD.*`),
- schema validation for `*.summary.json`,
- required field presence,
- leakage scans (coords/secrets),
- reproducibility checks (if manifests are regenerable in CI).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed month-index template for daily remote-sensing validation reports; standardized naming, minimum content, determinism rules, and governance-safe publication posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />

[⬅ Year Index](../README.md) ·
[🧾 Daily Reports](../../README.md) ·
[🧾 Reports Index](../../../README.md) ·
[🧾 Per-Run Reports](../../../per-run/README.md) ·
[🏷 Release Reports](../../../releases/README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

