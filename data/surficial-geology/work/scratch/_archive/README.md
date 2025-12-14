---
title: "🗃️ Surficial Geology — Work — Scratch Archive"
path: "data/surficial-geology/work/scratch/_archive/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/work/scratch/_archive/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:archive-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-archive-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:archive-readme:v0.1.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-relationship-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🗃️ **Surficial Geology — Work — Scratch Archive**
`data/surficial-geology/work/scratch/_archive/README.md`

**Purpose**  
Store **superseded scratch artifacts** (notes, tiny experiments, short-lived helper outputs) for minimal auditability, while keeping active scratch work in `data/surficial-geology/work/scratch/`.

</div>

---

## 📘 Overview

This directory is the **archive** for the Surficial Geology scratch workspace.

Use `_archive/` to retain **small** scratch artifacts that are no longer active but are useful to keep for:

- understanding why an approach was abandoned,
- preserving a small exploratory note that influenced a deterministic change,
- retaining a minimal breadcrumb trail while keeping `scratch/` uncluttered.

This archive is still **non-authoritative**:

- nothing here may be required by pipelines, catalogs, lineage, API, UI, or tests,
- nothing here should be treated as a distribution or provenance record,
- if something becomes important long-term, it must be promoted to a governed location.

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/            — Scratch workspace (non-authoritative)
├── 📄 README.md                                   — Scratch rules and boundaries
└── 📁 _archive/                                   — Superseded scratch artifacts (this directory)
    ├── 📄 README.md                               — This file
    └── 📄 YYYY-MM-DD__<short_slug>.<ext>          — Archived scratch item(s) (small; keep minimal)
~~~

Recommended conventions:

- Prefer sortable filenames: `YYYY-MM-DD__<short_slug>.<ext>`
- If an archived file relates to a run or change, include the token:
  - `YYYY-MM-DD__run-<run_id>__<short_slug>.<ext>`
  - `YYYY-MM-DD__pr-<num>__<short_slug>.<ext>` (if you track PR numbers)
- Keep the archive small; delete true trash rather than “archiving everything.”

---

## 🧭 Context

`work/scratch/_archive/` exists to prevent scratch clutter while preserving minimal context around iterative work.

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Hard boundary:

- scratch (and scratch archive) is **not** part of deterministic or publishable surfaces.

---

## 📦 Data & Metadata

Rules for archived scratch artifacts:

- **Non-dependency**: no production code, ETL, validation, catalog generation, or tests may depend on this folder.
- **Small + readable**: prefer text files and tiny outputs; avoid large binaries and dataset extracts.
- **No secrets / no PII**: never store tokens, credentials, signed URLs, personal emails, phone numbers, or similar.
- **No sensitive precision**: do not store restricted coordinates or discoverability guidance.
- **Promote if important**: if an artifact is needed for reproducibility or governance, move it to:
  - run evidence: `mcp/runs/<run_id>/`
  - lineage notes/manifests: `data/surficial-geology/lineage/**`
  - publishable outputs: `data/surficial-geology/outputs/**`
  - catalogs: `data/surficial-geology/stac/**`

---

## 🌐 STAC, DCAT & PROV Alignment

This folder should not be referenced by catalogs or provenance:

- **STAC**: Items/Collections must not point to `_archive/`.
- **DCAT**: distributions must not point to `_archive/`.
- **PROV/OpenLineage**: do not treat `_archive/` as an entity store; use `mcp/runs/**` and `data/surficial-geology/lineage/**` for evidence.

If a scratch artifact must be cited, it is in the wrong place—promote it.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on this folder.

If an archived scratch note contains an end-user caveat that remains relevant:

- move the caveat into governed notes:
  - `data/surficial-geology/lineage/notes/` (dataset/run caveats), and/or
  - `data/surficial-geology/stac/notes/` (catalog caveats)

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- passes secret scanning and PII scanning expectations,
- remains small and non-essential,
- does not introduce “latest” files intended to be overwritten repeatedly,
- does not cause repo bloat.

If CI enforces size or forbidden-pattern rules, keep `_archive/` compliant by design.

---

## ⚖ FAIR+CARE & Governance

Archived scratch artifacts can still leak sensitive operational details.

- Do not archive restricted precision locations, sensitive inference guidance, or provider contact PII.
- If a file is found to violate governance, remove it and record the reason in a governed note location (not in scratch).

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial scratch archive README defining purpose, layout, non-dependency rules, and promotion boundaries. |

---

<div align="center">

🗃️ **Surficial Geology — Work — Scratch Archive**  
KFM Data Layer · Scratch Archive · Governance-Aware

[📘 Docs Root](../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

