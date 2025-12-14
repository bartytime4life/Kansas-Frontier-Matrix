---
title: "🧪 Surficial Geology — Work — Scratch Samples — Rasters"
path: "data/surficial-geology/work/scratch/samples/rasters/README.md"

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
    - "data/surficial-geology/work/scratch/samples/rasters/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:samples:rasters-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-samples-rasters-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:samples-rasters-readme:v0.1.0"

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

# 🧪 **Surficial Geology — Work — Scratch Samples — Rasters**
`data/surficial-geology/work/scratch/samples/rasters/README.md`

**Purpose**  
Store **very small, disposable raster samples** used for local debugging and exploration, without creating dependencies for pipelines, catalogs, or provenance.

</div>

---

## 📘 Overview

This folder contains **scratch raster samples** for Surficial Geology work.

Use this folder for:

- minimal raster snippets to reproduce a bug (read/warp/translate),
- tiny “known-good” samples to validate a local transform step,
- small tiles/crops to sanity-check CRS, nodata, dtype, and georeferencing.

This folder is **non-authoritative**:

- nothing here may be required by ETL, validation gates, catalogs, lineage, API, UI, or tests,
- samples may be replaced or deleted at any time,
- if a sample becomes important for reproducibility, it must be promoted to a governed location.

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/samples/              — Scratch samples (non-authoritative)
└── 📁 rasters/                                              — Raster samples (this directory)
    ├── 📄 README.md                                         — This file
    ├── 🗺️ <sample_name>.tif                                 — Tiny GeoTIFF sample (preferred)
    ├── 🗺️ <sample_name>.vrt                                 — Optional VRT (do not reference external secrets)
    ├── 🧾 <sample_name>.json                                — Optional sidecar (intent + origin + constraints)
    └── 📁 _archive/                                         — Optional: superseded samples (keep minimal)
~~~

Notes:

- Keep samples tiny and few.
- Avoid large rasters, pyramids, or bulk intermediary outputs.

---

## 🧭 Context

This directory is part of the workspace layer:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Hard boundaries:

- source-of-record bytes live under `data/surficial-geology/raw/**`
- deterministic deliverables live under `data/surficial-geology/outputs/**`
- catalog metadata lives under `data/surficial-geology/stac/**`
- audit-grade lineage lives under `data/surficial-geology/lineage/**`
- reproducible run evidence lives under `mcp/runs/**`

If a raster sample is required to reproduce a run or validate a release, it belongs in run evidence or lineage—not here.

---

## 📦 Data & Metadata

### Size and scope rules

- Keep rasters **small** (minimal extent and minimal resolution).
- Prefer a **crop** over a resample, unless resampling is what you are testing.
- Avoid multi-GB imagery, full-state mosaics, or “convenience copies” of raw sources.

### Formats

Preferred:

- GeoTIFF (`.tif`) with explicit nodata and CRS
- Sidecar JSON for intent (optional)

Avoid:

- formats that depend on external credentials/paths,
- formats that are hard to inspect or that bloat the repo.

### Naming

Recommended:

- `YYYY-MM-DD__<topic>__<short_slug>.tif`
- `YYYY-MM-DD__run-<run_id>__<short_slug>.tif` (if tied to a specific run)

### Rights and provenance hygiene

- Do not copy restricted or non-redistributable imagery into this folder.
- If a sample is derived from a governed source, keep it minimal and do not remove context needed to assess whether it is safe to keep.

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If a raster sample must be cited by provenance or catalog records, promote it first to:

- `mcp/runs/<run_id>/` (run-scoped evidence), or
- `data/surficial-geology/lineage/notes/` (curated narrative evidence), or
- an approved governed data area for long-lived fixtures (if defined in-repo).

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on scratch raster samples.

If a raster sample reveals a caveat that affects interpretation or publication, record that caveat in governed notes:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for commits here:

- no secrets, tokens, credentials, or signed URLs (including inside VRTs or sidecars),
- no PII,
- no restricted sensitive precision beyond policy thresholds,
- small footprint (avoid large binaries and bulk samples),
- no new dependencies (pipelines/tests must not rely on this folder).

---

## ⚖ FAIR+CARE & Governance

Raster samples can increase risk by unintentionally disclosing precision or enabling inference when combined with other layers.

- Do not store sensitive-location rasters or “discoverability aids.”
- Default to minimal crops and generalized extents when policy requires it.
- If there is any uncertainty about rights or sensitivity, do not commit the sample; capture only the safe, governed lesson in lineage notes.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `rasters/` README defining scope, non-dependency rules, and safe handling guidance for scratch raster samples. |

---

<div align="center">

🧪 **Surficial Geology — Work — Scratch Samples — Rasters**  
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

