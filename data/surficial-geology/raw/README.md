---
title: "🪨 Surficial Geology — Raw"
path: "data/surficial-geology/raw/README.md"

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
    - "data/surficial-geology/raw/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw-readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw-readme:v0.1.0"

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

# 🪨 **Surficial Geology — Raw**
`data/surficial-geology/raw/README.md`

**Purpose**  
Define what belongs in `data/surficial-geology/raw/`, how raw source drops are organized and integrity-checked, and how raw inputs are referenced by manifests and provenance for deterministic reprocessing.

</div>

---

## 📘 Overview

This directory stores **raw, source-of-record inputs** for the Surficial Geology domain.

Treat everything under `raw/` as:

- **Immutable**: once a snapshot is accepted, do not edit or “fix” files in place.
- **Reproducible**: the pipeline must be able to re-run from these bytes + configs.
- **Auditable**: every snapshot must have traceable origin, rights, and checksums.

### What belongs here

- Vendor/provider source drops (archives, geodatabases, rasters, PDFs, etc.) **as received**.
- Deterministic unpacked copies (optional) **only if** the original drop is preserved.
- Snapshot-local integrity files (e.g., SHA-256 checksum lists) and lightweight pointers to manifests.

### What does not belong here

- Processed/normalized datasets (those go in `data/surficial-geology/outputs/`).
- Scratch work, caches, or work-in-progress artifacts (those belong in `data/surficial-geology/work/`).
- Hand-edited “corrections” to source data (correct via deterministic transforms in the pipeline).

---

## 🗂️ Directory Layout

~~~text
📁 raw/                                             — Raw source inputs for this domain (this directory)
├── 📄 README.md                                    — This file (rules + organization)
├── 📁 <source_id>/                                 — One upstream source (stable identifier)
│   ├── 📁 <snapshot_id>/                            — Immutable snapshot (date/version-based)
│   │   ├── 📄 manifest.ref.json                     — Pointer to authoritative manifest id + metadata
│   │   ├── 🧾 checksums.sha256                      — SHA-256 checksums for files in this snapshot
│   │   ├── 📁 original/                             — Vendor drop preserved as-received
│   │   │   └── 📄 <vendor_filename>.<ext>           — e.g., zip/gdb/tif/pdf/etc.
│   │   └── 📁 expanded/                             — Optional deterministic unpack (no edits)
│   │       └── 📄 <expanded_files...>               — Extracted files (keep structure stable)
│   └── 📄 README.md                                 — Optional per-source notes (must follow KFM-MDP)
└── 📁 <source_id_2>/                                — Additional sources as needed
~~~

Notes:

- `<source_id>` should be stable and machine-friendly (lowercase, hyphenated), and should match the id used in manifests under `data/surficial-geology/lineage/manifests/`.
- `<snapshot_id>` should be deterministic and unique (e.g., `YYYY-MM-DD`, `v<ver>`, or `YYYY-MM-DD__<shorthash>`). Choose one convention and keep it consistent across sources.

---

## 🧭 Context

`raw/` is the first durable landing zone for the Surficial Geology domain’s data lifecycle:

Raw intake → deterministic transforms → outputs → catalogs (STAC/DCAT) → provenance (PROV/OpenLineage) → graph → API → UI → Story Nodes / Focus Mode

In practice, `raw/` exists so that:

- The system can **replay** processing deterministically without re-downloading.
- Every output can be traced back to **exact source bytes**.
- Rights/sensitivity decisions can be enforced from the start (not retroactively).

---

## 📦 Data & Metadata

### Snapshot rules (immutability)

- Do not edit raw files after placement.
- If a source is wrong or updated, create a **new snapshot** under a new `<snapshot_id>`.
- Prefer keeping the original packaging (e.g., `.zip`) even if you also unpack to `expanded/`.

### Required sidecars (per snapshot)

Each `<source_id>/<snapshot_id>/` MUST include:

- `checksums.sha256`
  - Must include hashes for every file that is part of the snapshot (including the preserved original archive if present).
- `manifest.ref.json`
  - Minimal pointer to the authoritative manifest record stored under `data/surficial-geology/lineage/manifests/`.
  - Should include at least: manifest id, retrieval date, upstream URI, and license/rights pointer (do not guess).

### Naming guidance

- Use stable folder names; avoid spaces.
- Avoid renaming vendor filenames inside `original/` unless absolutely required for compatibility.
- If renaming is necessary, record the mapping in the authoritative manifest and provenance.

### Rights and licensing

- The **README license** is CC-BY 4.0 (documentation).
- The **data license** for raw snapshots varies by upstream source and must be recorded in the authoritative source manifest.
- Never assume “open” without confirming and recording the rights metadata.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Raw assets may be referenced by STAC **for internal lineage**, but are not necessarily exposed as public “distribution” assets.
- If raw files are referenced as STAC assets, ensure roles clearly indicate “source” and that any access constraints are represented in metadata.

### DCAT

- DCAT distributions typically point to **outputs** intended for consumption.
- Raw snapshots should be treated as **provenance inputs** and may be captured as internal distributions only when appropriate under governance.

### PROV

- Each raw snapshot is a `prov:Entity` (source entity) and should be linked into the provenance chain:
  - outputs `prov:wasDerivedFrom` raw entities
  - processing activities `prov:used` raw entities
- Retrieval and acceptance of raw inputs should be captured as a distinct activity (even if it is “download + verify”).

---

## 🧪 Validation & CI/CD

Minimum expectations for accepted raw snapshots:

- **Integrity**:
  - `checksums.sha256` present and correct.
- **Traceability**:
  - `manifest.ref.json` present and points to a real manifest under `data/surficial-geology/lineage/manifests/`.
- **Governance**:
  - passes secret-scan and pii-scan expectations (even if “unlikely” for this domain).
- **Reproducibility**:
  - snapshot id is stable and not overwritten by subsequent drops.

If a snapshot fails validation, it should not be used by the pipeline until corrected via a new snapshot + updated manifests.

---

## ⚖ FAIR+CARE & Governance

Even geology-focused layers can create harm when combined with other datasets. When landing raw data:

- Respect any upstream access constraints (license, terms, embargoes).
- If any sovereignty flags apply (e.g., culturally sensitive places inferred from geology layers when combined with other sources), document:
  - the risk assessment,
  - any mitigation (masking/generalization),
  - and any restrictions on downstream publication.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `raw/` README defining snapshot conventions, checksum + manifest pointer requirements, and provenance alignment guidance. |

---

<div align="center">

🪨 **Surficial Geology — Raw**  
KFM Data Layer · Immutable Inputs · Reproducible Processing

[📘 Docs Root](../../../docs/README.md) ·
[📂 Standards Index](../../../docs/standards/README.md) ·
[📄 Templates Index](../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

