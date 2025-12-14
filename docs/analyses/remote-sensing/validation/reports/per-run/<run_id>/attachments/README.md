---
title: "📎 KFM — Per-Run Validation Attachments (Notes · Review Addenda · Evidence Pointers)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/attachments/README.md"

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

intent: "remote-sensing-validation-per-run-attachments"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:attachments:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-attachments-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/attachments/README.md"
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

# 📎 **KFM — Per‑Run Validation Attachments**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/attachments/README.md`

**Purpose**  
This folder stores **small, governance-safe addenda** for a single validation run (`<run_id>`):
operator notes, reviewer annotations, and pointers to governed evidence artifacts—without embedding sensitive data or large payloads.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Per-Run" src="https://img.shields.io/badge/Reports-Per--Run-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Attachments are optional, human-facing context for a single run bundle.

Use this folder to capture:

- brief explanations of anomalies,
- reviewer notes for governance decisions,
- redaction explanations using counts + reason codes only,
- follow-up action items linked to tickets/PRs (no secrets).

This directory is in-repo and should be treated as public-facing by default.

---

## ✅ What belongs here

Recommended attachment files (optional):

- `notes.md` — brief operator notes (small)
- `review.md` — governance/reviewer notes and sign-offs (small)
- `redaction.md` — redaction rationale (counts + reason codes only)
- `exceptions.md` — approved exceptions with policy references (no secrets)
- `links.md` — stable pointers (repo paths, STAC ids, PROV ids, digests)

---

## ⛔ What must NOT be committed here

Do NOT store any of the following:

- raw imagery, tiles, rasters, large tables, or any “data payload” outputs,
- per-sample lists (especially when restricted inputs exist),
- precise coordinates, site-level identifiers, or “how to locate” content,
- signed URLs, tokens, credentials, internal endpoints, secrets,
- PII or personal notes beyond role-level attribution.

If you need to preserve evidence:

- store it as a governed artifact and link via STAC assets and PROV entities,
- store only digests and stable ids here.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/attachments/
├── 📄 README.md                                               — This policy/index
├── 📄 notes.md                                                — Optional: brief operator notes
├── 📄 review.md                                               — Optional: reviewer annotations and sign-offs
├── 📄 redaction.md                                            — Optional: redaction rationale (counts only)
├── 📄 exceptions.md                                           — Optional: approved exception record (no secrets)
└── 📄 links.md                                                — Optional: stable pointers (ids/paths/digests)
~~~

---

## 🛡️ Governance posture (enforced)

Attachments MUST obey the same governance posture as the run’s inputs.

Rules:

- if any input is restricted or governance is unclear:
  - do not include per-sample details,
  - keep spatial scope generalized (region/coarse grid),
  - reference governed artifacts instead of copying details.
- if governance is unclear:
  - the run summary should fail closed per policy,
  - notes here should remain high-level and policy-referential.

---

## 🔗 Linking pattern (preferred)

When referencing evidence:

- STAC Item ids: `urn:kfm:...`
- PROV Entity/Activity ids: `urn:kfm:...`
- repo paths: `data/stac/...`, `data/dcat/...`, `data/.../prov/...`
- digests: `sha256:<...>`

Avoid external links unless they are stable, public, and approved by governance posture.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed per-run attachments policy; defined allowed content, prohibited content, and governance-safe linking patterns. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Run Bundle](../README.md) ·
[🧾 Manifests](../manifests/README.md) ·
[🧬 Provenance](../provenance/README.md) ·
[🧾 Per-Run Reports](../../README.md) ·
[🧩 Methods](../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

