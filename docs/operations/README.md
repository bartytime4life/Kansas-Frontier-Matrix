---
title: "🛠️ KFM — Operations (SOPs · Runbooks · Reliability · Rollback)"
path: "docs/operations/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
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

intent: "operations-index"
audience:
  - "Reliability Engineering"
  - "On-Call Responders"
  - "Data Engineering"
  - "Catalog Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Reliability Council · FAIR+CARE Council"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:operations:index:v11.2.6"
semantic_document_id: "kfm-operations-index"
event_source_id: "ledger:docs/operations/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🛠️ **KFM — Operations**
`docs/operations/README.md`

**Purpose**  
Operator-facing documentation for keeping KFM stable day-to-day:
SOPs, reliability conventions, alerting posture, catalog safety, and rollback procedures.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

Operations docs are designed to be:

- **fast**: runnable under pressure (on-call friendly),
- **deterministic**: unambiguous steps and thresholds,
- **governed**: FAIR+CARE and sovereignty controls respected by default,
- **auditable**: changes and rollbacks are evidence-led (STAC/DCAT/PROV, checksums, attestations).

This directory complements:

- engineering patterns: `docs/patterns/**`
- governance standards: `docs/standards/**`
- CI/CD automation: `docs/ci/**`

---

## 🗂️ Directory Layout

~~~text
📁 docs/operations/                                   — Operations docs (this directory)
├── 📄 README.md                                      — This index
└── 📁 sop/                                           — Standard Operating Procedures (SOPs)
    ├── 📄 README.md                                  — SOP index
    └── 📄 automation-stability-onepager.md            — Schedulers, SemVer in STAC/DCAT, SLO tiers, rollback
~~~

---

## 🧭 Quick links

- SOP index: [`docs/operations/sop/README.md`](sop/README.md)
- Automation stability one‑pager: [`docs/operations/sop/automation-stability-onepager.md`](sop/automation-stability-onepager.md)

---

## 🧰 What belongs in Operations

Include documents that answer:

- “What do I do right now?” (page, incident, rollback, degrade, re-run)
- “What is the stable posture?” (SLOs, alert tiers, schedulers, run cadence)
- “What must be true before promotion?” (SemVer, STAC/DCAT validity, provenance complete)
- “How do we prevent regressions?” (CI gates, dashboards, postmortems)

Exclude:

- new architecture proposals (place those under `docs/architecture/**` or `docs/patterns/**`)
- one-off notes without run criteria (convert into a SOP or a runbook)

---

## ✅ SOP expectations (governed)

SOPs MUST:

- define **explicit triggers** (thresholds, time windows, and job criticality),
- define **safe degradations** (fail closed, skip noncritical, preserve lineage),
- preserve catalog correctness:
  - no byte mutation of published artifacts,
  - rollback via pointers (`replacedBy`, `previousVersion`) and republish catalogs,
- record lineage and outcomes:
  - emit PROV/OpenLineage artifacts where applicable,
  - store checksums/attestations for promoted bundles.

---

## 🧪 Validation & CI/CD

Recommended checks for operations docs:

- `markdown-lint` (KFM-MDP v11.2.6 structure + `~~~` fences)
- link checks (relative paths resolve)
- optional “runbook smoke checks” for command snippets (if/when SOPs include executable commands)

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial operations index; linked SOP directory and automation stability one‑pager. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧰 SOP Index](sop/README.md) ·
[🏗 Data Architecture](../architecture/data/README.md) ·
[🏛️ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

