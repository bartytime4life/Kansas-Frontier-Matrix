---
title: "✅ Surficial Geology — Work — Scratch Checks"
path: "data/surficial-geology/work/scratch/checks/README.md"

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
    - "data/surficial-geology/work/scratch/checks/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:checks-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-checks-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:checks-readme:v0.1.0"

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

# ✅ **Surficial Geology — Work — Scratch Checks**
`data/surficial-geology/work/scratch/checks/README.md`

**Purpose**  
Store **small, throwaway check outputs** produced during ad-hoc exploration (counts, bounds, schema quickviews, validity probes) without creating dependencies for pipelines, catalogs, or provenance.

</div>

---

## 📘 Overview

This folder is for **scratch check outputs** created while debugging or exploring Surficial Geology artifacts.

Use this directory for quick, local checks such as:

- feature/row counts by layer or attribute
- bbox/extent sanity checks
- geometry validity spot-checks
- projection/CRS detection results
- attribute field presence/type quickviews
- tiny diffs that help confirm “what changed”

This directory is **non-authoritative**:

- nothing here may be required by ETL, validation gates, catalogs, lineage, API, UI, or tests
- outputs here are disposable and may be deleted or replaced at any time
- if a check result matters long-term, it must be promoted to a governed location

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/                 — Scratch workspace (non-authoritative)
└── 📁 checks/                                          — Scratch check outputs (this directory)
    ├── 📄 README.md                                    — This file
    ├── 📁 counts/                                      — Counts, histograms, tallies (small)
    ├── 📁 extents/                                     — Bounds/extent snapshots (small)
    ├── 📁 schema/                                      — Field lists/type probes (small)
    ├── 📁 validity/                                    — Geometry validity probes (small)
    └── 📁 diffs/                                       — Tiny diffs used for debugging (small)
~~~

Notes:

- Subfolders are optional; keep the structure boring and minimal.
- Do not commit large extracts or bulk intermediate datasets here.

---

## 🧭 Context

This folder lives in the workspace layer:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Hard boundary:

- scratch checks support iteration, but they are not part of deterministic production surfaces

If the same check should run every time, encode it as deterministic validation tooling and store results as run artifacts.

---

## 📦 Data & Metadata

Guidelines for scratch checks:

- Keep files **small** and **review-friendly** (prefer `.md`, `.json`, `.csv`, `.txt`).
- Prefer sortable names:
  - `YYYY-MM-DD__<topic>.<ext>`
  - `YYYY-MM-DD__run-<run_id>__<topic>.<ext>` (when tied to a specific run)
- Prefer repo-safe references (paths, ids) over pasting large logs or large tables.

Promotion guidance (when a check output becomes important):

- reproducible run evidence (logs/config/check outputs) → `mcp/runs/<run_id>/`
- audit-grade lineage evidence or curated findings → `data/surficial-geology/lineage/**`
- review-grade QA summaries (still non-authoritative, but more structured) → `data/surficial-geology/work/qa/**`

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If a scratch check must be cited in provenance or catalog documentation, it is in the wrong place—promote it first.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on scratch checks.

If a scratch check reveals an end-user caveat (limitations, known issues, interpretation constraints), capture it in governed notes:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for committed scratch checks:

- no secrets, tokens, credentials, or signed URLs
- no PII
- no restricted sensitive precision or discoverability guidance
- small footprint (avoid large binaries and large extracts)
- no new dependencies (pipelines/tests must not rely on these files)

---

## ⚖ FAIR+CARE & Governance

Scratch artifacts can leak sensitive operational details.

- Do not include restricted coordinates or guidance that increases discoverability of sensitive locations.
- Do not copy provider contact information from upstream metadata into check outputs.
- Keep rights/licensing claims out of scratch outputs; licensing belongs in governed source records.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/scratch/checks/` README defining scope, non-dependency boundary, and promotion guidance. |

---

<div align="center">

✅ **Surficial Geology — Work — Scratch Checks**  
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

