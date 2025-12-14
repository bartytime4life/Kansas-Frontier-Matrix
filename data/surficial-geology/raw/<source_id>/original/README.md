---
title: "🪨 Surficial Geology — Raw — <source_id> — Original"
path: "data/surficial-geology/raw/<source_id>/original/README.md"

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
    - "data/surficial-geology/raw/<source_id>/original/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw:<source_id>:original-readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-<source_id>-original-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw:<source_id>:original-readme:v0.1.0"

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

# 🪨 **Surficial Geology — Raw — <source_id> — Original**
`data/surficial-geology/raw/<source_id>/original/README.md`

**Purpose**  
Preserve the **bytes-as-received** upstream source drop for `<source_id>` (no edits, no renames), so every downstream transformation can be reproduced and audited from an immutable raw baseline.

</div>

---

## 📘 Overview

This directory is the **authoritative raw payload** for this source: what was downloaded, received, or otherwise acquired from the upstream provider.

Treat everything under `original/` as:

- **Immutable**: do not modify contents in-place
- **Evidence-grade**: filenames and structure should match upstream delivery
- **Reproducibility anchor**: all derived products should trace back here via manifests + provenance

### What belongs here

- Upstream-delivered archives and files exactly as received (e.g., `.zip`, `.7z`, `.tar.gz`, `.gdb.zip`, `.tif`, `.shp` bundles, vendor PDFs).
- Vendor-provided directory structure (keep intact).
- Optional integrity artifacts that describe the originals without changing them (e.g., `checksums.sha256`).

### What does not belong here

- Converted formats (GeoPackage exports, reprojected rasters, simplified vectors) — those go under `data/surficial-geology/outputs/` or `data/processed/` per pipeline conventions.
- Manual “fixes” to source data — fix via deterministic ETL, not by patching raw inputs.
- Scratch or temporary extraction work folders — keep that under run workspaces (e.g., `mcp/runs/<run_id>/...`) unless policy explicitly requires otherwise.

Related folders (same `<source_id>` scope):

- License context: `../license/README.md`
- Source metadata: `../metadata/README.md`
- Curation notes: `../notes/README.md`

---

## 🗂️ Directory Layout

~~~text
📁 original/                                     — Bytes-as-received upstream payload (this directory)
├── 📄 README.md                                  — This file (immutability + handling rules)
├── 🧾 checksums.sha256                           — (Recommended) SHA-256 checksums for originals
├── 📄 <upstream_filename_1>                      — As delivered (do not rename)
├── 📄 <upstream_filename_2>                      — As delivered (do not rename)
└── 📁 <upstream_folder_if_any>/                  — If upstream delivered a folder, keep structure intact
    └── 📄 <upstream_file_n>                      — As delivered
~~~

Notes:

- Prefer keeping the upstream packaging (e.g., keep the original `.zip` if that is how it was delivered).
- If extraction is required for processing, do it deterministically in the pipeline workspace; do not “organize” extracted files into this folder unless the upstream delivery itself was extracted.

---

## 🧭 Context

In the KFM pipeline, `original/` sits at the **ingest boundary**:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

This folder exists so that:

- **Lineage is defensible**: every derivative can point to a stable raw entity.
- **Audits are possible**: reviewers can verify transformations against originals.
- **Re-ingestion is deterministic**: pipelines can re-run from identical raw bytes.

---

## 📦 Data & Metadata

### Integrity expectations

- If any files in `original/` are added/updated/removed, update integrity tracking:
  - Prefer `checksums.sha256` in this folder (or ensure the authoritative manifest elsewhere is updated).
- Keep upstream filenames intact. If the pipeline needs canonical names, handle mapping in config/manifests—not by renaming originals.

### Recommended checksum format

- Use SHA-256 checksums, one line per file.
- Include relative paths when subfolders exist so validation is unambiguous.

Example line format (illustrative):

~~~text
<sha256>  <relative/path/to/file>
~~~

### Where “descriptive” metadata should live

- Put upstream metadata documents and parsed metadata sidecars under `../metadata/`.
- Put license texts, rights statements, and attribution requirements under `../license/`.
- Put human curation notes and data-quality observations under `../notes/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Originals are typically referenced indirectly (via processed artifacts), but may be modeled as STAC assets when policy allows.
- If included as assets, mark them clearly as **source/original** and provide checksums when available.

### DCAT

- The upstream dataset corresponds to a DCAT `dcat:Dataset`.
- Files in `original/` may be represented as upstream distributions or source evidence, but **license/rights must come from authoritative source documentation** (do not infer).

### PROV

- Each file in `original/` is a `prov:Entity` (raw source entity).
- Any ingestion/extraction/conversion step is a `prov:Activity` that:
  - `prov:used` → raw entities from `original/`
  - `prov:generated` → derived entities (processed/outputs)
- Run identifiers and config snapshots should be stored with the run artifacts (e.g., `mcp/runs/<run_id>/...`) and referenced from provenance summaries.

---

## 🧪 Validation & CI/CD

Minimum expectations when committing/updating raw originals:

- **Checksum integrity**: checksums present and match (or manifests updated where authoritative).
- **No secrets / no PII**: repository scans must pass.
- **No silent edits**: replace-by-new-download only; record retrieval date and rationale in manifests/notes as applicable.
- **Governance compliance**: if any content could trigger masking/generalization policies downstream, ensure it is flagged in metadata and provenance.

---

## ⚖ FAIR+CARE & Governance

Even where sensitivity is “low,” governance still applies:

- Do not add precision-enhancing annotations to raw files.
- Do not combine or repackage raw inputs in ways that obscure provenance.
- If a source introduces restrictions or attribution requirements, capture them in `../license/` and ensure downstream catalogs reflect them.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `original/` README defining immutability rules, integrity expectations, and linkage guidance for STAC/DCAT/PROV. |

---

<div align="center">

🪨 **Surficial Geology — Raw — <source_id> — Original**  
KFM Data Layer · Bytes-as-Received · Provenance-First

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

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

