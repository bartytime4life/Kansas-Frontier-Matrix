---
title: "🧪 Surficial Geology — Work — Scratch"
path: "data/surficial-geology/work/scratch/README.md"

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
    - "data/surficial-geology/work/scratch/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch-readme:v0.1.0"

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

# 🧪 **Surficial Geology — Work — Scratch**
`data/surficial-geology/work/scratch/README.md`

**Purpose**  
Provide a governed place for **throwaway / exploratory** artifacts (quick checks, prototypes, temporary notes) that must **not** become dependencies for raw intake, deterministic outputs, catalogs, or lineage.

</div>

---

## 📘 Overview

This folder is a **scratchpad workspace** for Surficial Geology work.

Use `work/scratch/` for:

- quick experiments and ad-hoc exploration,
- small temporary outputs from local debugging,
- short notes used to plan a change before it is encoded as deterministic config/code,
- small, disposable QA snippets that do not warrant a formal run artifact.

Do **not** use `work/scratch/` for:

- authoritative raw source bytes (`data/surficial-geology/raw/`),
- deterministic deliverables (`data/surficial-geology/outputs/`),
- catalogs (`data/surficial-geology/stac/`),
- lineage/provenance (`data/surficial-geology/lineage/`),
- run logs/config snapshots (`mcp/runs/` or `mcp/experiments/`).

Everything in `scratch/` is **non-authoritative** and should be treated as **temporary** by default.

---

## 🗂️ Directory Layout

~~~text
📁 work/scratch/                                    — Scratch workspace (this directory)
├── 📄 README.md                                     — This file (rules + boundaries)
├── 📁 notes/                                        — Small planning notes, short writeups
├── 📁 scripts/                                      — One-off helper scripts (do not become pipeline deps)
├── 📁 checks/                                       — Tiny check outputs (counts, bounds, schema quickviews)
├── 📁 samples/                                      — Very small samples for debugging (strictly limited)
├── 📁 tmp/                                          — Short-lived intermediates (prefer to keep empty)
└── 📁 _archive/                                     — Optional: superseded scratch notes (keep minimal)
~~~

Notes:

- Keep the structure boring and predictable.
- Avoid committing large binaries or large dataset extracts here.

---

## 🧭 Context

This directory exists to keep exploratory work from contaminating governed surfaces:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

The scratch area supports iteration while preserving:

- immutability of raw inputs,
- determinism of outputs,
- machine-validation of catalogs,
- audit-grade lineage.

---

## 📦 Data & Metadata

### Non-dependency rule

No pipeline step, API, UI, or catalog generation should rely on files in `work/scratch/`.

If anything in `scratch/` becomes required to reproduce results, **promote it** to the correct governed location:

- deterministic configs/code → `src/`, `tools/`, `schemas/`, `tests/` (as appropriate)
- reproducible run evidence → `mcp/runs/<run_id>/`
- provenance artifacts → `data/surficial-geology/lineage/**`
- publishable outputs → `data/surficial-geology/outputs/**`

### Keep it small

- Prefer text, small tables, and short reports.
- Avoid large binaries, full dataset copies, and repeated intermediate artifacts.
- If you must keep a sample, keep it minimal and document what it represents.

### Hygiene

- No secrets, tokens, credentials, signed URLs.
- No PII (names/emails/phones).
- No restricted sensitive precision or discoverability guidance.

---

## 🌐 STAC, DCAT & PROV Alignment

`work/scratch/` is **not** a publication surface and should not be referenced by:

- STAC Collections/Items,
- DCAT dataset/distribution records,
- PROV/OpenLineage artifacts.

If a scratch artifact needs to be referenced for auditability:

1. move it to `mcp/runs/` (run evidence) or `data/surficial-geology/lineage/notes/` (curated narrative context),
2. reference it from provenance/catalogn as appropriate.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on `work/scratch/`.

If scratch findings introduce an end-user caveat (limitations, known issues), capture them in governed notes:

- `data/surficial-geology/lineage/notes/` (run/dataset caveats), and/or
- `data/surficial-geology/stac/notes/` (catalog-specific caveats).

---

## 🧪 Validation & CI/CD

Minimum expectations for commits under `work/scratch/`:

- passes secret scanning and PII scanning expectations,
- remains small and non-essential (repo builds/tests do not depend on it),
- avoids large binaries and large extracts,
- avoids mutable “latest” outputs intended to be overwritten repeatedly.

If a scratch artifact represents a formal acceptance gate, encode it as deterministic validation tooling and store results as run artifacts instead.

---

## ⚖ FAIR+CARE & Governance

Scratch content can unintentionally leak sensitive operational details.

- Do not include restricted precision locations or sensitive inference guidance.
- Do not include provider contact PII copied from metadata.
- Do not include internal endpoints or access details.

When in doubt, generalize or omit, and record governed decisions in lineage notes/manifests instead.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/scratch/` README defining scratch scope, non-dependency rules, and promotion guidance. |

---

<div align="center">

🧪 **Surficial Geology — Work — Scratch**  
KFM Data Layer · Scratch Workspace · Governance-Aware

[📘 Docs Root](../../../../docs/README.md) ·
[📂 Standards Index](../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

