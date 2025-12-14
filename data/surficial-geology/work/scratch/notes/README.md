---
title: "📝 Surficial Geology — Work — Scratch Notes"
path: "data/surficial-geology/work/scratch/notes/README.md"

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
    - "data/surficial-geology/work/scratch/notes/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:notes-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-notes-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:notes-readme:v0.1.0"

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

# 📝 **Surficial Geology — Work — Scratch Notes**
`data/surficial-geology/work/scratch/notes/README.md`

**Purpose**  
Provide a governed place for **small, disposable, human-authored notes** created during exploration and debugging, without turning them into authoritative lineage, catalog metadata, or pipeline dependencies.

</div>

---

## 📘 Overview

This folder is for **scratch notes** produced while working on Surficial Geology data and tooling.

Use `work/scratch/notes/` for:

- quick investigation notes (what you tried, what you observed),
- planning notes before encoding decisions into deterministic configs/code,
- short debugging notes (why a step failed locally, what fixed it),
- “working hypotheses” that are clearly labeled and not presented as facts.

This folder is **non-authoritative**:

- nothing here may be required by ETL, catalogs, lineage, API, UI, or tests,
- notes may be overwritten or deleted as work progresses,
- if a note becomes important for governance, reproducibility, or publication, it must be promoted to a governed location.

Do not use this folder for:

- raw intake documentation (use `data/surficial-geology/raw/**` READMEs and manifests),
- audit-grade lineage or curation decisions (use `data/surficial-geology/lineage/notes/**`),
- catalog behavior decisions meant for consumers (use `data/surficial-geology/stac/notes/**`),
- run-by-run reproducibility evidence (use `mcp/runs/**`).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/                  — Scratch workspace (non-authoritative)
└── 📁 notes/                                            — Scratch notes (this directory)
    ├── 📄 README.md                                     — This file (scope + rules)
    ├── 📄 YYYY-MM-DD__<topic>.md                        — Scratch note (small; disposable)
    ├── 📄 YYYY-MM-DD__run-<run_id>__<topic>.md          — Scratch note tied to a run (optional)
    └── 📁 _archive/                                     — Optional: superseded notes kept minimal
        └── 📄 README.md                                 — Archive rules (if used)
~~~

Notes:

- Prefer one topic per file.
- Prefer sortable filenames (`YYYY-MM-DD__...`).
- Keep this directory small; promote important notes instead of accumulating a long scratch history.

---

## 🧭 Context

This folder lives in the workspace layer:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Scratch notes exist to support iteration while preserving strict boundaries:

- `raw/` stays immutable and source-of-record
- `outputs/` stay deterministic and versioned
- `stac/` stays machine-validated and consumer-facing
- `lineage/` stays audit-grade and provenance-first
- `mcp/runs/` stays reproducibility-first (config snapshots + logs)

---

## 📦 Data & Metadata

### Non-dependency rule

No production process may rely on files in `work/scratch/notes/`.

If a note defines a rule that must hold (example: “we dissolve polygons by UNIT_ID”), that rule must be implemented in deterministic config/code and validated by the pipeline. The scratch note may remain as context, but it is not the rule itself.

### Recommended note template

Inside each scratch note, separate:

- **Facts (observed / sourced)**: what you measured or what the source states
- **Interpretation**: how you think it should be handled
- **Next actions**: what to implement or validate
- **Promotion target**: where the final, governed record will live

Example structure:

~~~text
Facts:
- …

Interpretation:
- …

Next actions:
- …

Promotion target:
- …
~~~

### Promotion guidance

If a scratch note becomes important:

- governance/curation decisions and caveats → `data/surficial-geology/lineage/notes/`
- catalog decisions and consumer-visible guidance → `data/surficial-geology/stac/notes/`
- run reproducibility evidence (inputs/config/logs) → `mcp/runs/<run_id>/`
- publishable documentation (stable, maintained) → appropriate `docs/**` or domain README under `data/surficial-geology/**`

---

## 🌐 STAC, DCAT & PROV Alignment

This directory should not be referenced by governed metadata systems:

- **STAC**: Collections/Items must not link to `work/scratch/notes/`.
- **DCAT**: distributions must not point to scratch notes.
- **PROV/OpenLineage**: scratch notes are not provenance evidence; use `mcp/runs/**` and `data/surficial-geology/lineage/**`.

If a note must be referenced by STAC/DCAT/PROV, promote it first into a governed notes location.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on scratch notes as evidence.

Scratch notes may be summarized for internal navigation, but narrative outputs must be evidence-led and must rely on:

- governed lineage artifacts (`data/surficial-geology/lineage/**`),
- governed catalogs (`data/surficial-geology/stac/**`),
- governed documentation (`docs/**`),
- and published outputs (`data/surficial-geology/outputs/**`).

Do not write scratch notes as if they are publishable findings.

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- no secrets (tokens, credentials, signed URLs),
- no PII (personal emails/phones/names in contact blocks),
- no restricted sensitive precision or discoverability guidance,
- small footprint (no large pasted logs or dataset dumps),
- no new dependencies (CI/builds must not rely on these notes).

---

## ⚖ FAIR+CARE & Governance

Scratch notes can accidentally leak sensitive details or create harmful inference pathways.

- Do not include restricted coordinates or instructions that increase discoverability of sensitive sites.
- Do not copy provider contact details from upstream metadata.
- Keep licensing/rights claims out of scratch notes; those belong in governed source/license records.

When a governance-relevant decision is made, record it in the governed lineage system and implement enforcement in deterministic pipelines and catalogs.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/scratch/notes/` README defining scope, non-dependency rules, promotion targets, and governance boundaries. |

---

<div align="center">

📝 **Surficial Geology — Work — Scratch Notes**  
KFM Data Layer · Scratch Workspace · Governance-Aware

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

