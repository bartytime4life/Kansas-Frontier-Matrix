---
title: "🧪 Surficial Geology — Work — Scratch Samples — Tables"
path: "data/surficial-geology/work/scratch/samples/tables/README.md"

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
    - "data/surficial-geology/work/scratch/samples/tables/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:samples:tables-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-samples-tables-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:samples:tables-readme:v0.1.0"

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
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧪 **Surficial Geology — Work — Scratch Samples — Tables**
`data/surficial-geology/work/scratch/samples/tables/`

**Purpose**  
Store **very small, disposable tabular samples** used for local debugging and exploration, without creating dependencies for pipelines, catalogs, or provenance.

</div>

---

## 📘 Overview

This folder contains **scratch tabular samples** used while iterating on Surficial Geology work.

Use this folder for:

- tiny extracts to reproduce a bug quickly (parsing, typing, joins, lookups),
- minimal examples to test schema mapping logic locally,
- small “known-good” tables to sanity-check column names, encodings, null handling, and category codes.

This folder is **non-authoritative**:

- nothing here may be required by ETL, catalogs, lineage, API, UI, or tests,
- samples may be replaced or deleted at any time,
- if a sample becomes important for reproducibility or review, promote it to a governed location.

Do NOT store:

- raw source-of-record tables (use `data/surficial-geology/raw/**`),
- deterministic outputs or distributions (use `data/surficial-geology/outputs/**`),
- formal run evidence (use `mcp/runs/**`),
- lineage artifacts (use `data/surficial-geology/lineage/**`).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/samples/            — Scratch samples (non-authoritative)
└── 📁 tables/                                             — Tabular samples (this directory)
    ├── 📄 README.md                                       — This file
    ├── 🧾 <sample_name>.csv                               — Tiny sample table (preferred)
    ├── 🧾 <sample_name>.tsv                               — Tiny sample table (optional)
    ├── 🧾 <sample_name>.parquet                           — Tiny sample table (optional; keep very small)
    ├── 🧾 <sample_name>.json                              — Optional sidecar (intent + origin + constraints)
    └── 📁 _archive/                                       — Optional: superseded samples (keep minimal)
~~~

Notes:

- Prefer text formats (`.csv`, `.tsv`) for transparency unless binary formats are required to reproduce a bug.
- Keep the total footprint small; avoid “sample sprawl”.

---

## 🧭 Context

This directory sits in the **workspace/scratch** layer.

Hard boundaries:

- `data/surficial-geology/raw/**` is the source-of-record intake surface (immutable evidence).
- `data/surficial-geology/outputs/**` is the deterministic distribution surface.
- `data/surficial-geology/stac/**` is the catalog surface (machine-validated metadata).
- `data/surficial-geology/lineage/**` is the audit-grade provenance surface.
- `mcp/runs/**` is the reproducibility surface (run configs/logs/outputs).

Scratch samples are allowed only as **temporary aids** during development.

---

## 🗺️ Diagrams

Not used in this directory.

---

## 🧠 Story Node & Focus Mode Integration

This directory must not be used as evidence for Story Nodes or Focus Mode.

If a table sample reveals an interpretation caveat that matters beyond local debugging, record it in a governed location:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- passes secret scanning and PII scanning policies,
- remains small (no large extracts, no bulk copies),
- does not introduce dependencies (pipelines/tests must not rely on this folder),
- avoids mutable “latest” files intended to be overwritten repeatedly.

If a sample is needed for deterministic testing, promote it into the repo’s governed test/fixture strategy (if defined) with an explicit governance review.

---

## 📦 Data & Metadata

### Size and scope rules

- Keep samples tiny (minimal rows, minimal columns).
- Include only the columns required to reproduce the issue under investigation.
- Avoid embedding identifiers that could be sensitive or personal.

### Naming conventions

Recommended:

- `YYYY-MM-DD__<topic>__<short_slug>.csv`
- `YYYY-MM-DD__run-<run_id>__<short_slug>.csv` (only if helpful; still non-authoritative)

### Optional sidecar (`<sample_name>.json`)

If a sample needs context, store a small sidecar describing:

- intent (what it’s for),
- origin (high-level source path, not a copy of raw),
- constraints (what must remain true for the sample to be useful),
- disposal plan (delete after fix, or promote if it becomes a fixture).

### Rights and provenance hygiene

- Do not copy restricted or non-redistributable content into this folder.
- Do not create new “official” data statements here (no licensing claims; no canonical mappings).

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If a sample must be cited as evidence, promote it first to:

- `mcp/runs/<run_id>/` (run-scoped evidence), and/or
- `data/surficial-geology/lineage/notes/` (curated, governed narrative evidence)

---

## 🧱 Architecture

This folder is intentionally **non-authoritative** and **non-contractual**.

It exists to protect deterministic and governed surfaces from accidental contamination while supporting fast local iteration.

---

## ⚖ FAIR+CARE & Governance

Tabular samples can create harm if they:

- contain PII or contact information,
- embed sensitive location hints that increase discoverability,
- duplicate restricted content without clear rights.

Rules:

- minimize and generalize where necessary,
- never store secrets/tokens/credentials,
- if there is any uncertainty about safety or rights, do not commit the sample—record only the safe, governed lesson elsewhere.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `tables/` README defining scope, boundaries, and safe handling guidance for scratch tabular samples. |

---

<div align="center">

🧪 **Surficial Geology — Work — Scratch Samples — Tables**  
KFM Data Layer · Scratch Workspace · Governance-Aware

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

