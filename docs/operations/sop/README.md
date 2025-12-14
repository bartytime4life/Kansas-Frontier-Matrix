---
title: "🧰 KFM — Operations SOP Index (Runbooks · Daily Checks · Rollback Guides)"
path: "docs/operations/sop/README.md"

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

intent: "operations-sop-index"
audience:
  - "Reliability Engineering"
  - "Data Engineering"
  - "Catalog Engineering"
  - "On-Call Responders"
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

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:ops:sop:index:v11.2.6"
semantic_document_id: "kfm-ops-sop-index"
event_source_id: "ledger:docs/operations/sop/README.md"
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

# 🧰 **KFM — Operations SOP Index**
`docs/operations/sop/README.md`

**Purpose**  
Index for day‑to‑day **Standard Operating Procedures (SOPs)** used to keep KFM reliable:
scheduling, releases, catalog SemVer, SLO/alerts, incident response, and rollback.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

SOPs are **operator-facing** documents designed to be:

- **fast to execute** under pressure,
- **deterministic** (clear steps, bounded choices),
- **governance-aware** (FAIR+CARE, sovereignty labels, provenance expectations),
- **operationally testable** (validate via CI linting and runbook smoke checks where applicable).

SOPs complement:

- patterns (`docs/patterns/**`) for repeatable engineering designs,
- standards (`docs/standards/**`) for governance rules,
- CI/CD docs (`docs/ci/**`) for automation behavior.

---

## 🗂️ Directory Layout

~~~text
📁 docs/operations/                                   — Operations documentation root
└── 📁 sop/                                           — Standard Operating Procedures (this directory)
    ├── 📄 README.md                                  — SOP index (this file)
    └── 📄 automation-stability-onepager.md            — Schedulers, SemVer in STAC/DCAT, SLO tiers, rollback
~~~

---

## 🧭 SOP Index

| SOP | When to use | Primary owner | Review cycle |
|---|---|---|---|
| [`automation-stability-onepager.md`](automation-stability-onepager.md) | Daily automation stability: schedulers, STAC/DCAT SemVer enforcement, SLO/alerts, rollback | Reliability Council | Quarterly |

> Add SOPs here as they land. Keep titles short and execution-focused.

---

## ✅ SOP conventions (governed)

### 1) Structure (required)

Each SOP MUST include:

- a single H1 at top (this file uses the index format),
- concise numbered sections (operators should find the step they need in <30 seconds),
- deterministic “if/then” criteria for paging, ticketing, rollback, and escalations,
- a version history block.

### 2) Operations posture (required)

SOPs MUST:

- fail closed when governance posture is unclear (deny or aggregate rather than leak),
- avoid embedding secrets, signed URLs, or internal-only endpoints,
- prefer references to stable repo paths over environment-specific instructions.

### 3) Governance expectations (required)

When a SOP interacts with:

- catalogs (STAC/DCAT),
- provenance (PROV/OpenLineage),
- sensitive data labels,

…it MUST mention:

- where governance labels are enforced,
- what gets emitted (artifacts, manifests, references),
- what the operator is allowed to override (and how overrides are recorded).

---

## 🧪 Validation & CI/CD (recommended)

CI checks SHOULD include:

- `markdown-lint` for KFM‑MDP v11.2.6 formatting and fence style (`~~~`),
- link checks (relative paths resolve),
- optional “runbook smoke checks” for command snippets (if included).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial SOP index; added automation stability one-pager. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Docs Index](../../README.md) ·
[🏗 Data Architecture](../../architecture/data/README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

