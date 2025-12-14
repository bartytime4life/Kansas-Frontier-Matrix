---
title: "🪨 Surficial Geology — Raw Source: <source_id>"
path: "data/surficial-geology/raw/<source_id>/README.md"

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
    - "data/surficial-geology/raw/<source_id>/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw-<source_id>-readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-<source_id>-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw-<source_id>-readme:v0.1.0"

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

# 🪨 **Surficial Geology — Raw Source: `<source_id>`**
`data/surficial-geology/raw/<source_id>/README.md`

**Purpose**  
Describe the authoritative raw source drop for `<source_id>`: what files belong here, how they are verified (checksums), and how this source is referenced by `data/sources/<source_id>.json` and downstream STAC/DCAT/PROV lineage.

</div>

---

## 📘 Overview

This directory contains the **closest-to-upstream, unmodified** files for a single Surficial Geology source, identified by `<source_id>`.

Treat everything here as:

- **Authoritative raw evidence** for ingestion and reproducibility
- **Immutable** (do not edit file contents in-place)
- **Verifiable** (every file has a recorded checksum)
- **Rights-governed** (license and access constraints must be explicit)

### Source summary (fill in)

- **Source ID:** `<source_id>`
- **Publisher / Owner:** `<publisher>`
- **Upstream landing page / API:** `<source_uri>`
- **License / Rights:** `<license_or_rights_statement>`
- **Retrieval date:** `<YYYY-MM-DD>`
- **Upstream version (if any):** `<vX / date / revision id>`
- **Native format(s):** `<zip / gdb / shp / tif / pdf / csv / etc.>`
- **Notes:** `<known quirks, join keys, encoding, etc.>`

### What belongs here

- Files downloaded from the publisher (exact bytes where possible).
- Publisher-provided documentation (readme, metadata, field definitions).
- License/citation text when redistribution is permitted.
- Integrity records (checksums) for every committed file.

### What does not belong here

- “Fixed” or manually edited copies of the dataset.
- Reprojected/simplified/cleaned derivatives (those go under `data/surficial-geology/outputs/` and/or `data/processed/` depending on the pipeline contract).
- Cache files, scratch outputs, or workstation exports.

---

## 🗂️ Directory Layout

~~~text
📁 raw/<source_id>/                              — Raw source drop (this directory)
├── 📄 README.md                                 — This file (what this source is + rules)
├── 🧾 checksums.sha256                          — SHA-256 checksums for all committed raw files
├── 📁 original/                                 — Original files exactly as retrieved (preferred)
│   ├── 📄 <upstream_filename_1>                 — e.g., .zip / .gdb / .shp bundle / .tif / .pdf
│   └── 📄 <upstream_filename_2>
├── 📁 metadata/                                 — Provider metadata snapshots (recommended)
│   ├── 📄 upstream_readme.txt                   — Any upstream readme / release notes
│   ├── 🧾 upstream_metadata.json                — If provided by publisher (JSON/XML/etc.)
│   └── 📄 field_definitions.*                   — PDFs/CSVs describing attributes, if provided
├── 📁 license/                                  — Rights & citation artifacts (if redistributable)
│   ├── 📄 LICENSE.txt                           — Publisher license text (or terms-of-use excerpt)
│   └── 📄 CITATION.*                            — Citation guidance (if available)
└── 📁 notes/                                    — Curation notes (text only; NO data edits)
    └── 📄 curator_notes.md                      — Known issues, assumptions, ingestion caveats
~~~

Notes:

- Keep upstream filenames whenever possible.
- If the upstream is an archive (`.zip`), prefer storing **the archive** in `original/` as the “byte-identical” reference. If extraction is required for tooling, document it in `notes/` and ensure lineage captures the extraction step.

---

## 🧭 Context

This folder is the **source-intake** edge for the Surficial Geology domain:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

In practice, `raw/<source_id>/` exists so that:

- ETL runs can be **replayed** against the exact same inputs.
- The project can **audit** what was used (bytes + license).
- PROV lineage can point back to durable, checksummed evidence.

The authoritative “source contract” for this intake SHOULD live at:

- `data/sources/<source_id>.json`

That manifest is where we record: `source_uri`, license/rights, retrieval date, checksums, and any access restrictions.

---

## 📦 Data & Metadata

### Integrity and immutability

- Never modify raw files in-place.
- If you discover corruption or a bad download:
  - re-fetch from upstream,
  - update `checksums.sha256`,
  - update `data/sources/<source_id>.json` (retrieval date, checksum set, notes).

### Naming conventions

- Prefer **upstream names** inside `original/`.
- Avoid renaming unless upstream names are unsafe for cross-platform use; if renaming is unavoidable:
  - document the mapping in `notes/curator_notes.md`,
  - keep a copy of the original archive/filename where license permits.

### Checksums

- `checksums.sha256` should include every committed file under this directory (including `license/` and `metadata/` when present).
- If large files are stored via Git LFS / DVC (if configured in-repo), checksums still apply to the canonical stored bytes.

### Rights and redistribution

- Do not assume a dataset is open. Capture license/terms in:
  - `data/sources/<source_id>.json` (authoritative), and
  - `license/` (local copy) if redistribution is permitted.

If rights are unclear or restrictive, store only what is allowed and document the restriction. When in doubt, prefer a **manifest-only** approach over committing restricted content.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Raw sources may be linked as STAC assets when license permits and when it improves traceability. Typical patterns:

- Processed STAC Items reference outputs as `data` assets and may reference raw inputs as `source`/`evidence` assets.
- STAC records live under `data/stac/` (collection + items).

### DCAT

- The dataset is represented as a DCAT `dcat:Dataset`.
- Raw files may appear as `dcat:Distribution` entries when they are redistributable and stable.

### PROV

- Each raw file is a `prov:Entity`.
- An ingestion/download step is a `prov:Activity` that:
  - `prov:used` → upstream source URI (as an entity) and any auth-free access metadata
  - `prov:generated` / `prov:wasGeneratedBy` → the raw file entities (downloaded artifacts)
- Any transformation (unzip, reprojection, attribute cleanup) must be a separate activity and must not overwrite raw.

---

## 🧪 Validation & CI/CD

Minimum expectations for committed raw sources:

- **Checksums**: `checksums.sha256` exists and matches file contents.
- **Source contract**: `data/sources/<source_id>.json` exists (or is added alongside this source) and includes license + retrieval facts.
- **Governance scans**: no secrets, no PII, and no disallowed sensitive precision.
- **Reproducibility**: ingestion scripts/configs should be able to re-derive downstream artifacts from these raw inputs.

---

## ⚖ FAIR+CARE & Governance

Even “public” geospatial layers can create harm when combined with other data.

- Respect sovereignty policies and masking/generalization requirements when creating downstream derivatives.
- Ensure rights and access constraints are explicit and queryable (catalog + provenance).
- If a source includes any sensitive context, record mitigation decisions in:
  - the source contract (`data/sources/<source_id>.json`)
  - lineage (PROV)
  - any downstream catalog records (STAC/DCAT)

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial per-source raw README template for `<source_id>`: immutability rules, integrity checks, and STAC/DCAT/PROV linkage guidance. |

---

<div align="center">

🪨 **Surficial Geology — Raw Source: `<source_id>`**  
KFM Data Layer · Source-of-Record · Provenance-First

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

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

