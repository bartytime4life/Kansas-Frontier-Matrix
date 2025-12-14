---
title: "🧾 Surficial Geology — Lineage Manifests"
path: "data/surficial-geology/lineage/manifests/README.md"

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
    - "data/surficial-geology/lineage/manifests/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage-manifests-readme:v0.1.0"
semantic_document_id: "surficial-geology-lineage-manifests-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage-manifests-readme:v0.1.0"

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

# 🧾 **Surficial Geology — Lineage Manifests**
`data/surficial-geology/lineage/manifests/README.md`

**Purpose**  
Define what belongs in `data/surficial-geology/lineage/manifests/`, how manifests are named and treated as immutable provenance artifacts, and how they support deterministic replays and traceable STAC/DCAT/PROV lineage.

</div>

---

## 📘 Overview

This directory contains **machine-readable, provenance-first manifest files** for the Surficial Geology domain. Manifests in this folder are intended to make builds:

- **Deterministic** (inputs + config → repeatable outputs)
- **Auditable** (checksums, tool versions, and file inventories are recorded)
- **Traceable** (connectable to STAC/DCAT and PROV summaries)

### What belongs here

- Run-level manifests capturing:
  - input references (source ids/URIs + checksums)
  - output inventories (paths + roles + checksums)
  - build configuration identifiers (config path, commit sha, parameters)
- Optional PROV summaries (or references to PROV artifacts stored elsewhere) that can be ingested into the graph.

### What does not belong here

- Raw data drops (store raw under `data/raw/` with proper source manifests).
- Ad-hoc notes, personal logs, screenshots, or workstation exports.
- Secrets, credentials, API tokens, or private endpoints (CI will scan and reject).

### Immutability rule

Manifests are **append-only** in practice:

- Do not “edit history” by changing an existing manifest unless correcting a clearly documented, non-semantic formatting issue.
- When something changes, generate a **new** manifest for the new run/version and link via catalogs/provenance.

---

## 🗂️ Directory Layout

~~~text
📁 manifests/                                         — Lineage manifests (this directory)
├── 📄 README.md                                      — This file (conventions + rules)
├── 🧾 checksums.sha256                               — Checksums for manifest artifacts (recommended)
├── 🧾 manifest.<run_id>.json                         — Run-level manifest (inputs → outputs)
├── 🧾 inputs.<run_id>.yaml                           — Input list (URIs/ids + checksums) (optional)
├── 🧾 artifacts.<run_id>.json                        — Output inventory (paths/roles/checksums) (optional)
└── 🧾 prov.<run_id>.json                             — PROV summary for the run (optional)
~~~

Notes:

- `<run_id>` should be globally unique and stable (e.g., timestamp + short git sha).
- File naming MUST remain deterministic (stable ordering, stable keys) to support reproducible diffs.

---

## 🧭 Context

This folder exists to support the KFM lineage contract:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

In practice:

- `manifests/` is the **evidence layer** for “what happened in a run.”
- `data/surficial-geology/lineage/indexes/` can store **derived indexes** built from these manifests (faster lookup, summaries, rollups).
- `data/surficial-geology/outputs/` stores the **actual produced artifacts** (tiles/vectors/metadata), which SHOULD be referenced by the manifests here.

---

## 📦 Data & Metadata

### Manifest expectations

Manifests SHOULD be structured so they can be validated and ingested. Typical fields include:

- `run_id`, `generated_at`, `commit_sha`
- `inputs[]`: `{id|uri, role, checksum_sha256, license|rights_ref}`
- `outputs[]`: `{path, role, media_type, size_bytes, checksum_sha256}`
- `config`: `{path, checksum_sha256, parameters}`

### Checksums

- Prefer SHA-256 everywhere.
- When a manifest references an artifact under `outputs/`, the referenced checksum MUST match the committed file.

### Naming conventions

- Use lowercase stems and predictable prefixes: `manifest.*`, `inputs.*`, `artifacts.*`, `prov.*`.
- Avoid spaces and “latest” pointers. If needed, generate a separate index file under `lineage/indexes/` rather than mutating manifests.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Output artifacts referenced in a manifest SHOULD also be referenced as STAC assets.
- A manifest (or PROV summary) MAY be linked from STAC as an auxiliary asset (e.g., role `metadata` or `provenance`) if your STAC profile supports it.

### DCAT

- Manifests can support DCAT by providing distribution-level details (format/media type, checksums, paths).
- License/rights in manifests MUST be sourced from authoritative records (source manifests and/or catalog metadata), not guessed.

### PROV

- A run that produced artifacts is a `prov:Activity`.
- Output files and manifests are `prov:Entity` objects:
  - outputs: `prov:wasGeneratedBy` → run activity
  - outputs: `prov:wasDerivedFrom` → inputs (and intermediate entities where recorded)
- Agents (scripts, CI, maintainers) SHOULD be represented as `prov:Agent` where applicable.

---

## 🧪 Validation & CI/CD

Minimum expectations for manifests committed here:

- **Schema validity**: JSON/YAML is well-formed and (when available) conforms to KFM lineage schemas.
- **Checksum integrity**:
  - `checksums.sha256` updated (if used)
  - manifest-referenced checksums match the actual files they describe
- **Path correctness**:
  - referenced artifact paths are repo-relative and stable
  - manifests do not reference local filesystem paths (e.g., `/Users/...`)
- **Governance scans**: no secrets, no PII, and no disallowed sensitive precision.

---

## ⚖ FAIR+CARE & Governance

Lineage artifacts are part of governance:

- Record license/rights constraints at the point of intake and carry them forward through outputs.
- If sovereignty or sensitivity flags apply, manifests MUST reflect:
  - generalization/redaction decisions
  - access restrictions (when applicable)
  - provenance continuity (no “mystery inputs”)

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `lineage/manifests/` README defining manifest purpose, immutability expectations, naming conventions, and STAC/DCAT/PROV alignment guidance. |

---

<div align="center">

🧾 **Surficial Geology — Lineage Manifests**  
KFM Data Layer · Provenance Manifests · Deterministic Lineage

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

