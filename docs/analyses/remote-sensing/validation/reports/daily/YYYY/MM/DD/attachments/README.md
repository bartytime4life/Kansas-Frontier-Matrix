---
title: "📎 KFM — Daily Validation Attachments (Notes · Evidence Pointers · Governance-Safe Addenda)"
path: "docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/attachments/README.md"

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

intent: "remote-sensing-validation-daily-report-attachments"
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

governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:attachments:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-daily-attachments"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/attachments/README.md"
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

# 📎 **KFM — Daily Validation Attachments**
`docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/attachments/README.md`

**Purpose**  
This folder holds **small, governance-safe addenda** for a single day’s validation bundle:
operator notes, review annotations, and **pointers** to governed evidence artifacts (STAC/PROV), without embedding sensitive or bulky outputs.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Attachments are for **human-facing context** that is helpful in day-to-day operations and governance review, while keeping the core artifacts:

- **machine summaries** in the day bundle,
- **manifests and provenance** in their dedicated folders,
- **large evidence artifacts** stored as governed assets referenced by STAC and PROV.

This is an **in-repo** directory. Treat it as public-facing unless explicitly restricted by repository policy.

---

## ✅ What belongs here

Use this folder for small, governance-safe files such as:

- short operator notes explaining anomalies (e.g., upstream outage, scheduled downtime),
- review notes describing why an outcome is `warn` instead of `fail`,
- redaction notes describing what was withheld and why (no sensitive detail),
- “next actions” for follow-up investigation tickets,
- accessibility notes for any human summaries.

Recommended attachment files (optional):

- `notes.md` — brief human notes for the day
- `review.md` — reviewer comments and sign-off notes
- `redaction.md` — redaction summary (counts + reason codes only)
- `exceptions.md` — approved exceptions with policy reference (no secret content)
- `links.md` — stable pointers (repo paths, STAC ids, PROV ids) only

---

## ⛔ What must NOT be committed here

Do NOT store any of the following in this folder:

- raw imagery, tiles, rasters, large tables, or any “data payload” outputs,
- precise coordinates, site-level location details, or “how to locate” content,
- restricted identifiers from gated datasets (unless explicitly generalized and approved),
- signed URLs, tokens, credentials, internal endpoints, or secrets of any kind,
- PII or personal operational notes that identify individuals beyond role (avoid names),
- bulky provenance bundles (store as governed artifacts; reference by id/path instead).

If you need to preserve evidence:

- store it in governed artifact storage and link via **STAC assets** and **PROV Entities**,
- or store only a **digest + stable id** here.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/attachments/
├── 📄 README.md                                               — This policy/index
├── 📄 notes.md                                                — Optional: brief operator notes (small)
├── 📄 review.md                                               — Optional: governance/reviewer notes (small)
├── 📄 redaction.md                                            — Optional: redaction rationale (counts only)
├── 📄 exceptions.md                                           — Optional: approved exception record (no secrets)
└── 📄 links.md                                                — Optional: stable pointers (ids/paths/digests)
~~~

---

## 🛡️ Governance and CARE posture (enforced)

Attachments MUST obey the same governance posture as the day’s inputs.

Rules:

- if any input is restricted or uncertain:
  - do not include per-sample details,
  - do not include precise spatial/temporal slices that allow inference,
  - use generalized scope language (region/coarse grid),
  - reference the governed artifacts (STAC/PROV) instead of copying content.
- if governance is unclear:
  - fail closed in the main summary (per policy),
  - keep notes here high-level and policy-referential.

---

## 🔗 Linking pattern (preferred)

When referencing evidence, prefer stable references:

- STAC Item ids: `urn:kfm:...`
- PROV Entity/Activity ids: `urn:kfm:...`
- repo paths: `data/stac/...`, `data/dcat/...`, `data/.../prov/...`
- digests: `sha256:<...>`

Avoid external links unless they are stable, public, and approved.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed attachments policy for daily validation bundles; defined allowed content, prohibited content, and governance-safe linking patterns. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Day Bundle](../README.md) ·
[⬅ Month Index](../../README.md) ·
[⬅ Year Index](../../../README.md) ·
[🧾 Daily Reports](../../../../README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

