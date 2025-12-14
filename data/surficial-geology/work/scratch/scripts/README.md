---
title: "🧪 Surficial Geology — Work — Scratch Scripts"
path: "data/surficial-geology/work/scratch/scripts/README.md"

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
    - "data/surficial-geology/work/scratch/scripts/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:scripts-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-scripts-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:scripts-readme:v0.1.0"

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

# 🧪 **Surficial Geology — Work — Scratch Scripts**
`data/surficial-geology/work/scratch/scripts/README.md`

**Purpose**  
Store **one-off / exploratory helper scripts** used during local iteration and debugging, without creating dependencies for ETL, catalogs, lineage, API, UI, or tests.

</div>

---

## 📘 Overview

This folder is for **scratch scripts** created while working on Surficial Geology data and tooling.

Use `work/scratch/scripts/` for:

- quick local helpers (inspect a file, print schema, compute counts, sample rows/features),
- short-lived debugging scripts (reproduce an error in isolation),
- exploratory conversions used only to learn something (not to publish),
- prototype code that may later be promoted into governed tooling.

This folder is **non-authoritative**:

- scripts here MUST NOT be required by deterministic pipelines,
- CI MUST NOT depend on these scripts to pass,
- scripts may be replaced or deleted as work evolves.

Do not use this folder for:

- production ETL steps (place deterministic tools in `tools/` or `src/` as appropriate),
- reproducible run evidence (place run configs/logs under `mcp/runs/`),
- publishing surfaces (outputs, STAC, lineage).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/                 — Scratch workspace (non-authoritative)
└── 📁 scripts/                                         — Scratch scripts (this directory)
    ├── 📄 README.md                                    — This file
    ├── 🧾 YYYY-MM-DD__<topic>.<ext>                    — One-off script (preferred naming)
    ├── 🧾 YYYY-MM-DD__run-<run_id>__<topic>.<ext>      — Script tied to a run (optional)
    ├── 📁 _archive/                                    — Optional: superseded scripts (keep minimal)
    └── 📄 NOTES.md                                     — Optional: brief scratch notes (keep short)
~~~

Recommended script extensions:

- `.py` (Python)
- `.sh` (shell)
- `.js` (Node)
- `.ipynb` only if absolutely necessary (prefer plain scripts for diffability)

---

## 🧭 Context

This directory exists to support fast iteration while protecting governed surfaces:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Hard boundaries:

- source-of-record bytes live in `data/surficial-geology/raw/**`
- deterministic deliverables live in `data/surficial-geology/outputs/**`
- catalog metadata lives in `data/surficial-geology/stac/**`
- audit-grade lineage lives in `data/surficial-geology/lineage/**`
- reproducible run artifacts live in `mcp/runs/**`

Scratch scripts are allowed only as **temporary aids** and must not become hidden dependencies.

---

## 📦 Data & Metadata

### Non-dependency rule

No production system may rely on scripts in this folder, including:

- ingestion/ETL execution
- STAC/DCAT generation
- provenance generation
- graph ingestion
- API runtime
- frontend build/runtime
- tests/CI gates

If a script becomes important, promote it into a governed location and wire it in explicitly.

### Promotion guidance

Promote scratch scripts when they become stable and reusable:

- deterministic tooling (CLI utilities, converters, validators) → `tools/`
- library code used by pipelines → `src/`
- schemas/specs for validation → `schemas/`
- tests and fixtures → `tests/` (and governed fixture paths, if defined)
- run-specific evidence and exact command context → `mcp/runs/<run_id>/` (as run notes/logs, not as core tooling)

When promoting, ensure the promoted tool is:

- deterministic (config-driven where applicable),
- replayable,
- documented with a minimal runbook,
- covered by tests where appropriate.

### Script hygiene

- No secrets, tokens, or credentials (hard fail).
- No PII (personal emails/phones; do not copy upstream contact blocks).
- Avoid absolute workstation paths; prefer repo-relative paths.
- Keep outputs out of this folder unless they are tiny scratch artifacts; publishable artifacts must go to governed outputs.

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If a script is required to explain provenance (“how it was generated”), capture that in:

- `mcp/runs/<run_id>/` (config snapshot + run notes), and/or
- `data/surficial-geology/lineage/notes/` (governed narrative of decisions)

Do not point catalogs/provenance at scratch scripts.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on scratch scripts.

If a script reveals an interpretation caveat or a limitation that should be user-visible:

- record it in governed notes (`data/surficial-geology/lineage/notes/` and/or `data/surficial-geology/stac/notes/`)
- implement enforcement in deterministic pipelines and catalog rules (do not rely on a scratch script)

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- passes secret scanning and PII scanning expectations,
- remains small and non-essential,
- does not introduce a required dependency for CI, ETL, or validation,
- does not write large outputs into the repo.

If a script becomes part of a formal validation step, it must be promoted to governed tooling and added to CI explicitly.

---

## ⚖ FAIR+CARE & Governance

Scratch scripts can accidentally leak sensitive information through:

- embedded credentials,
- hard-coded endpoints or signed URLs,
- printed/exported restricted coordinates at disallowed precision,
- copied upstream contact blocks (PII).

Rules:

- keep scripts minimal and local-use oriented,
- never commit secrets/PII,
- default to generalization when sovereignty/sensitivity constraints might apply,
- promote governance-relevant logic into deterministic pipelines with review.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/scratch/scripts/` README defining scope, non-dependency rules, hygiene requirements, and promotion boundaries. |

---

<div align="center">

🧪 **Surficial Geology — Work — Scratch Scripts**  
KFM Data Layer · Scratch Workspace · Governance-Aware

[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

