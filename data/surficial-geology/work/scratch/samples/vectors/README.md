---
title: "🧪 Surficial Geology — Work — Scratch Samples — Vectors"
path: "data/surficial-geology/work/scratch/samples/vectors/README.md"

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
    - "data/surficial-geology/work/scratch/samples/vectors/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:samples:vectors-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-samples-vectors-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:samples:vectors-readme:v0.1.0"

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

# 🧪 **Surficial Geology — Work — Scratch Samples — Vectors**
`data/surficial-geology/work/scratch/samples/vectors/README.md`

**Purpose**  
Store **very small, disposable vector samples** used for local debugging and exploration, without creating dependencies for pipelines, catalogs, or provenance.

</div>

---

## 📘 Overview

This folder contains **scratch vector samples** used while iterating on Surficial Geology work.

Use this folder for:

- tiny extracts to reproduce a bug quickly (read/write, CRS, topology, attribute typing),
- minimal examples to test joins, dissolve rules, clipping, and geometry validation locally,
- small “known-good” samples to sanity-check field names, codes, and geometry types.

This folder is **non-authoritative**:

- nothing here may be required by ETL, catalogs, lineage, API, UI, or tests,
- samples may be replaced or deleted at any time,
- if a sample becomes important for reproducibility or review, promote it to a governed location.

Do NOT store:

- raw source-of-record bytes (use `data/surficial-geology/raw/**`),
- deterministic distributions (use `data/surficial-geology/outputs/**`),
- catalog metadata (use `data/surficial-geology/stac/**`),
- provenance artifacts (use `data/surficial-geology/lineage/**`),
- run logs/config snapshots (use `mcp/runs/**` or `mcp/experiments/**`).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/samples/              — Scratch samples (non-authoritative)
└── 📁 vectors/                                              — Vector samples (this directory)
    ├── 📄 README.md                                         — This file
    ├── 🧾 <sample_name>.geojson                             — Tiny GeoJSON sample (preferred for inspection)
    ├── 🧾 <sample_name>.gpkg                                — Tiny GeoPackage sample (optional; keep very small)
    ├── 🧾 <sample_name>.fgb                                 — Tiny FlatGeobuf sample (optional)
    ├── 🧾 <sample_name>.json                                — Optional sidecar (intent + origin + constraints)
    └── 📁 _archive/                                         — Optional: superseded samples (keep minimal)
~~~

Notes:

- Prefer transparent formats (`.geojson`) unless you specifically need a binary format to reproduce a bug.
- Keep the total footprint small; avoid “sample sprawl.”

---

## 🧭 Context

This directory sits in the workspace/scratch layer.

Hard boundaries:

- source-of-record intake lives under `data/surficial-geology/raw/**` (immutable evidence),
- deterministic deliverables live under `data/surficial-geology/outputs/**`,
- catalog metadata lives under `data/surficial-geology/stac/**`,
- audit-grade lineage lives under `data/surficial-geology/lineage/**`,
- reproducible run evidence lives under `mcp/runs/**`.

Scratch samples are allowed only as **temporary aids** during development.

---

## 📦 Data & Metadata

### Size and scope rules

- Keep samples **tiny** (minimal features, minimal extent).
- Include only the attributes required to reproduce the issue under investigation.
- Prefer cropping/subsetting over format conversion unless conversion is what you are testing.
- Avoid copying full layers, full counties, or statewide extracts into this folder.

### Naming

Recommended:

- `YYYY-MM-DD__<topic>__<short_slug>.geojson`
- `YYYY-MM-DD__run-<run_id>__<short_slug>.geojson` (if tied to a specific run)

### Optional sidecar (`<sample_name>.json`)

If a sample needs context, store a small sidecar describing:

- intent (what the sample is for),
- origin (high-level source path or run id; do not paste credentials/URLs),
- constraints (what must remain true for the sample to be useful),
- disposal plan (delete after fix, or promote if it becomes a fixture).

### Rights and provenance hygiene

- Do not copy restricted or non-redistributable content into this folder.
- Do not embed licensing claims here; rights belong in governed source/license records.

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`),
- DCAT dataset/distribution records,
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`).

If a sample must be cited as evidence, promote it first to:

- `mcp/runs/<run_id>/` (run-scoped evidence), and/or
- `data/surficial-geology/lineage/notes/` (curated, governed narrative evidence), and/or
- an approved governed fixtures/test location (if defined in-repo).

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on scratch vector samples.

If a sample reveals an end-user caveat (limitations, known issues, interpretation constraints), record that caveat in governed notes:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`,
- catalog caveats → `data/surficial-geology/stac/notes/`.

---

## 🧪 Validation & CI/CD

Minimum expectations for commits here:

- no secrets, tokens, credentials, or signed URLs (including inside sidecars),
- no PII,
- no restricted sensitive precision or discoverability guidance,
- small footprint (avoid large binaries and bulk extracts),
- no new dependencies (pipelines/tests must not rely on this folder).

If a vector sample becomes part of a deterministic test strategy, move it into the repo’s governed test/fixture location (if defined) with an explicit governance review.

---

## ⚖ FAIR+CARE & Governance

Vector samples can increase risk by disclosing precision or enabling inference when combined with other layers.

- Do not store sensitive-location vectors or “discoverability aids.”
- Default to minimal features and generalized extents when policy requires it.
- If there is any uncertainty about rights or sensitivity, do not commit the sample; record only the safe, governed lesson in lineage notes.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `vectors/` README defining scope, non-dependency rules, and safe handling guidance for scratch vector samples. |

---

<div align="center">

🧪 **Surficial Geology — Work — Scratch Samples — Vectors**  
KFM Data Layer · Scratch Workspace · Governance-Aware

[📘 Docs Root](../../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

