---
title: "🧬 Surficial Geology — Lineage Indexes"
path: "data/surficial-geology/lineage/indexes/README.md"

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
    - "data/surficial-geology/lineage/indexes/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage-indexes-readme:v0.1.0"
semantic_document_id: "surficial-geology-lineage-indexes-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage-indexes-readme:v0.1.0"

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

# 🧬 **Surficial Geology — Lineage Indexes**
`data/surficial-geology/lineage/indexes/README.md`

**Purpose**  
Define what belongs in `data/surficial-geology/lineage/indexes/`, how index artifacts are named/versioned, and how these indexes support deterministic provenance and catalog integrity (STAC/DCAT/PROV).

</div>

---

## 📘 Overview

This directory holds **machine-generated index artifacts** that accelerate common lineage and audit lookups for the Surficial Geology domain.

Treat everything under `lineage/indexes/` as:

- **Derived** (rebuildable from tracked inputs + recorded provenance)
- **Deterministic** (stable outputs from the same inputs/config/tool versions)
- **Query-oriented** (optimized for “what produced this?” and “what depends on this?” lookups)

These indexes are intended to **speed up validation, ingestion, and provenance traversal**. They do **not** replace full provenance capture (PROV) or authoritative catalog metadata (STAC/DCAT).

### What belongs here

- Versioned index files that summarize lineage relationships (runs, entities, derivations).
- Inventory manifests for the index set (schemas, checksums, build parameters).
- Checksums for committed index artifacts.

### What does not belong here

- Hand-edited corrections (fix the pipeline/config; regenerate instead).
- Raw source data, ad-hoc exports, or workstation-specific caches.
- Sensitive details that should not be public (secrets, PII, restricted locations, protected cultural knowledge).

---

## 🗂️ Directory Layout

~~~text
📁 indexes/                                         — Derived lineage lookup indexes (this directory)
├── 📄 README.md                                    — This file (conventions + regeneration rules)
├── 🧾 checksums.sha256                             — SHA-256 checksums for committed index artifacts
├── 🧾 indexes.manifest_v<ver>.json                  — Inventory + schema versions + build parameters
├── 🧾 runs_index_v<ver>.json                        — Run-level summary (run ids, times, config hashes)
├── 🧾 entities_index_v<ver>.jsonl                   — Entity lookup (urn/id → path, checksum, type)
├── 📄 assets_index_v<ver>.parquet                   — STAC/DCAT asset/distribution mapping (optional)
└── 📄 lineage_edges_index_v<ver>.parquet            — Derivation edges for traversal (optional)
~~~

Notes:

- `<ver>` is the **dataset output version** (e.g., `v2025.12.14` or `v0.3.0`) chosen by the producing pipeline.
- Index sets MAY be partial (e.g., only `runs_index_*` + `entities_index_*`) depending on what the pipeline emits.
- Prefer simple, stable filenames and stable ordering to keep diffs readable and regeneration verifiable.

---

## 🧭 Context

These artifacts sit in the KFM pipeline between lineage capture and downstream consumers:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

In practice, `lineage/indexes/` exists so that:

- **Validators** can quickly confirm that expected lineage links exist (and match checksums).
- **Graph ingestion** can resolve file paths and entity ids without scanning full provenance bundles.
- **Audit workflows** can answer “what run produced this output?” and “what inputs contributed?” efficiently.

---

## 📦 Data & Metadata

### Naming and versioning

- Use lowercase, underscore-separated file stems: `*_index_*`.
- Every committed index file MUST include a version token: `_v<ver>`.
- Prefer emitting **one canonical index per type per version** (avoid duplicates with slightly different scopes).

### Determinism expectations

To remain reproducible, indexes SHOULD be written with deterministic conventions:

- Stable sort order (by stable id / path / checksum — pick one and keep it consistent).
- Newline-terminated JSON/JSONL.
- No ephemeral fields unless strictly necessary (avoid machine hostname, wall-clock durations, random ids).
- If timestamps are required, prefer run start/end timestamps that are already part of recorded run metadata.

### Sidecar metadata (required when artifacts are committed)

- `checksums.sha256` must include every committed artifact in this directory.
- `indexes.manifest_v<ver>.json` should capture:
  - index file inventory (paths, sizes, checksums)
  - schema versions / profile ids (where applicable)
  - producing run identifier(s)
  - references to the producing run log/config snapshot under `mcp/runs/` (when available)

### “Do not hand-edit” rule

If an index is wrong, do not patch it in-place. Update inputs/config/code so the deterministic build produces corrected indexes and regenerates checksums + manifests.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Index files MAY be referenced as STAC assets when they are useful for traceability.
- If referenced, treat them as **metadata assets** (not primary data), and ensure `checksum:sha256` is present when available.
- STAC records should live under `data/stac/` and reference committed index artifacts by exact relative path.

### DCAT

- Index artifacts are typically **internal distributions** used for system integrity and audit.
- If published as a distribution, ensure the dataset’s license/rights are inherited from the authoritative source record and that formats/media types are explicit.

### PROV

- Each index file is a `prov:Entity`.
- The activity that produces the index set is a `prov:Activity`.
- The index entities MUST link:
  - `prov:wasGeneratedBy` → the index-build activity
  - `prov:wasDerivedFrom` → the provenance sources/captured entities they summarize (and/or the run record)

---

## 🧪 Validation & CI/CD

Minimum expectations for committed lineage indexes:

- **Checksums**: `checksums.sha256` updated and matches file contents.
- **Schema stability**: manifests validate and track schema/profile versions.
- **Referential integrity** (when applicable):
  - entity ids map to real paths and/or known catalog ids
  - checksums in indexes match the referenced artifacts
- **Determinism**: rerunning the same build produces byte-identical outputs (or documented, justified exceptions).
- **Governance scans**: no secrets, no PII, and no disallowed sensitive precision.

---

## ⚖ FAIR+CARE & Governance

Indexes can unintentionally amplify risk by making cross-joins and lookups easy.

When generating lineage indexes:

- Prefer **stable identifiers** (URNs, dataset ids, checksums) over embedding sensitive coordinates.
- If sovereignty or sensitivity flags apply, ensure masking/generalization is applied before publication.
- Record any governance-driven transformations in the producing run record and provenance.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `lineage/indexes/` README defining index artifact conventions, determinism expectations, and STAC/DCAT/PROV alignment guidance. |

---

<div align="center">

🧬 **Surficial Geology — Lineage Indexes**  
KFM Data Layer · Provenance-First · Deterministic Index Artifacts

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

