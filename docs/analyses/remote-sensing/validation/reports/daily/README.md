---
title: "📅 KFM — Remote Sensing Daily Validation Reports (Index · Naming · Rollups)"
path: "docs/analyses/remote-sensing/validation/reports/daily/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index"
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

intent: "remote-sensing-validation-daily-index"
audience:
  - "Remote Sensing Engineering"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"
  - "Science QA Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-reports-daily-index"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📅 **KFM — Remote Sensing Daily Validation Reports**
`docs/analyses/remote-sensing/validation/reports/daily/README.md`

**Purpose**  
Index and conventions for **daily** remote-sensing validation rollups:
what to write, how to name it, what to link, and what must be redacted under FAIR+CARE policy.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

Daily validation reports provide a lightweight, operator-friendly summary of:

- what ran (pipelines, datasets, AOIs),
- what passed or failed (key checks),
- what drifted compared to prior days (counts and threshold deltas),
- where the governed artifacts are (STAC/DCAT/PROV references).

Daily reports are not the source of truth for data products; they are a human-facing index into governed artifacts.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/          — Reports root
└── 📁 daily/                                               — Daily rollups (this directory)
    ├── 📄 README.md                                        — This index
    └── 📁 YYYY/                                            — Year partition
        └── 📁 MM/                                          — Month partition
            └── 📁 DD/                                      — Day partition
                ├── 📄 summary.md                           — Human-readable daily summary (recommended)
                ├── 🧾 metrics.json                         — Small machine-readable summary (recommended)
                └── 🧾 links.json                           — STAC/DCAT/PROV refs (recommended)
~~~

> If you do not want a deep directory tree, you may store daily bundles as `YYYY-MM-DD/`,
> but keep a deterministic naming convention and update this README accordingly.

---

## 🧾 Daily bundle contract (recommended)

A daily bundle SHOULD include:

### 1) `summary.md` (human-facing)

Minimum sections:

- date and coverage window (UTC)
- pipelines/datasets included
- pass/fail overview
- top failures (with normalized reason codes)
- links to provenance and catalogs

### 2) `metrics.json` (machine-facing, small)

Recommended fields:

- `date_utc`
- `pipelines_total`
- `pipelines_failed`
- `datasets_checked`
- `checks_pass_ratio`
- `freshness_p95_seconds` (if applicable)
- `drift_flags_total`
- `care_gate_status` (`allow|redact|deny`)
- `redaction_summary` (counts + reason codes only)

### 3) `links.json` (references only)

Recommended fields:

- `stac_items` (array of hrefs/paths to STAC Items or Collections)
- `dcat_datasets` (array of hrefs/paths)
- `prov_bundles` (array of hrefs/paths)
- `run_ids` (array of stable run ids)
- `config_snapshots` (array of `mcp/runs/**/config.snapshot.json` paths)

---

## 🧭 Naming conventions

Use deterministic, sortable naming:

- directory partitioning: `daily/YYYY/MM/DD/`
- filenames: `summary.md`, `metrics.json`, `links.json`

If an additional artifact is included, prefix by type:

- `drift.delta.json`
- `qa.table.csv`
- `screenshots/` (only if safe and required)

---

## 🛡️ FAIR+CARE and sovereignty posture

Daily reports MUST be safe to publish in-repo:

- no raw restricted coordinates,
- no “how to find” sensitive sites,
- no internal endpoints or signed URLs,
- no full imagery samples unless policy explicitly allows.

If a daily report touches governed or sensitive datasets:

- set `care_gate_status` to `redact` or `deny` (as applicable),
- include only aggregated counts and generalized region indicators,
- link to restricted artifacts only via governed, access-controlled paths (no public URLs).

---

## 🧪 CI/CD alignment

Daily report generation SHOULD align with automated gates:

- STAC/DCAT schema validation results (summary only here; link to the machine report)
- asset integrity outcomes (checksums, expected asset presence)
- spatiotemporal sanity outcomes (bbox/time-window sanity in generalized form)
- drift thresholds (counts and metric deltas vs previous days)

When CI fails, the daily bundle SHOULD contain:

- failing check id/name
- expected vs observed values (safe)
- pointers to run logs and provenance

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial daily reports index; defined bundle contract, naming, and FAIR+CARE posture. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Reports](../README.md) ·
[📡 Validation](../../README.md) ·
[📡 Remote Sensing Analyses](../../../README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

