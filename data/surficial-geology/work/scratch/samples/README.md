---
title: "🧪 Surficial Geology — Work — Scratch Samples"
path: "data/surficial-geology/work/scratch/samples/README.md"

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
    - "data/surficial-geology/work/scratch/samples/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:samples-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-samples-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:samples-readme:v0.1.0"

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

# 🧪 **Surficial Geology — Work — Scratch Samples**
`data/surficial-geology/work/scratch/samples/README.md`

**Purpose**  
Store **very small, disposable sample artifacts** used for local debugging and quick exploration, without creating dependencies for pipelines, catalogs, or provenance.

</div>

---

## 📘 Overview

This folder is for **scratch samples** created while iterating on Surficial Geology work.

Use `work/scratch/samples/` for:

- tiny extracts used to reproduce a bug quickly,
- minimal examples to test a transform locally,
- small representative snippets used to verify assumptions (field names, geometry types, encoding),
- short-lived samples used during QA exploration.

This folder is **non-authoritative**:

- nothing here may be required by ETL, catalogs, lineage, API, UI, or tests,
- samples may be replaced or deleted as work progresses,
- if a sample becomes important for reproducibility or review, it must be promoted to a governed location.

Do **not** place:

- raw source-of-record bytes (use `data/surficial-geology/raw/`),
- deterministic distributions (use `data/surficial-geology/outputs/`),
- catalog JSON (use `data/surficial-geology/stac/`),
- provenance/lineage artifacts (use `data/surficial-geology/lineage/`),
- run logs/config snapshots (use `mcp/runs/` or `mcp/experiments/`).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/                — Scratch workspace (non-authoritative)
└── 📁 samples/                                        — Scratch samples (this directory)
    ├── 📄 README.md                                   — This file
    ├── 📁 vectors/                                    — Optional: tiny vector samples (strictly limited)
    ├── 📁 rasters/                                    — Optional: tiny raster samples (strictly limited)
    ├── 📁 tables/                                     — Optional: tiny tabular samples (strictly limited)
    └── 📁 _archive/                                   — Optional: superseded samples kept minimal
~~~

Notes:

- Keep subfolders optional and minimal.
- Avoid accumulating “lots of little samples”; delete true throwaways rather than archiving everything.

---

## 🧭 Context

This folder lives in the workspace layer:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Hard boundary:

- scratch samples support iteration, but they are not part of deterministic or publishable surfaces

If the same sample is needed repeatedly (for example, as a formal fixture), it should be promoted into the repo’s governed testing/fixture location (if one exists) or into an appropriate governed data area.

---

## 📦 Data & Metadata

Guidelines for scratch samples:

- **Keep samples tiny** (minimal geometry, minimal rows, minimal extent).
- Prefer **portable formats** (e.g., small GeoJSON/CSV for quick inspection) when appropriate, but do not “convert” raw sources here as an authoritative step.
- Use **sortable naming**:
  - `YYYY-MM-DD__<topic>.<ext>`
  - `YYYY-MM-DD__run-<run_id>__<topic>.<ext>` (if tied to a run)
- Include a short sidecar note only when needed:
  - what the sample represents,
  - how it was produced (high level),
  - what it is intended to test.

Promotion guidance (when a sample matters):

- run-scoped, reproducibility evidence → `mcp/runs/<run_id>/`
- audit-grade lineage evidence or curated caveats → `data/surficial-geology/lineage/**`
- publishable derivatives → `data/surficial-geology/outputs/**`
- catalog-facing documentation → `data/surficial-geology/stac/notes/**` or `docs/**`

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If a sample must be cited as evidence in catalogs or provenance, it is in the wrong place—promote it first into a governed location.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on scratch samples.

If a sample reveals an end-user caveat (limitations, known issues, interpretation constraints), capture the caveat in governed notes:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- no secrets, tokens, credentials, or signed URLs
- no PII
- no restricted sensitive precision or discoverability guidance
- small footprint (avoid large binaries and large extracts)
- no new dependencies (pipelines/tests must not rely on this folder)

If CI enforces size or forbidden-pattern rules, keep samples compliant by design.

---

## ⚖ FAIR+CARE & Governance

Samples can accidentally increase risk by:

- exposing sensitive locations with unnecessary precision,
- copying restricted content into a new file without capturing rights correctly,
- leaking internal paths or operational details.

For this folder:

- keep samples minimal and generalized where necessary,
- do not copy provider contact details,
- do not make new licensing claims here (rights belong in governed source/license records).

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/scratch/samples/` README defining scope, non-dependency boundary, and promotion guidance. |

---

<div align="center">

🧪 **Surficial Geology — Work — Scratch Samples**  
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

