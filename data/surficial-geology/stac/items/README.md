---
title: "🗺️ Surficial Geology — STAC Items"
path: "data/surficial-geology/stac/items/README.md"

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
    - "data/surficial-geology/stac/items/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:stac-items-readme:v0.1.0"
semantic_document_id: "surficial-geology-stac-items-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:stac-items-readme:v0.1.0"

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

# 🗺️ **Surficial Geology — STAC Items**
`data/surficial-geology/stac/items/README.md`

**Purpose**  
Define what belongs in `data/surficial-geology/stac/items/`, how Surficial Geology STAC Item JSON is named and validated, and how Items reference `outputs/` artifacts and lineage records.

</div>

---

## 📘 Overview

This directory contains **STAC Item** JSON documents for the Surficial Geology data domain.

A STAC Item is the **machine-readable discovery record** that describes a single spatiotemporal asset (or a tightly-scoped, versioned deliverable) with:

- a footprint (`geometry` / `bbox`)
- a temporal extent (`properties.datetime` or an interval)
- searchable metadata (`properties`)
- asset links (`assets.*.href`) to the actual files (vectors, tiles, schemas, etc.)

Treat everything under `stac/items/` as:

- **Derived**: Items are generated/maintained by deterministic pipeline logic and should remain reproducible.
- **Indexable**: Items are used by catalog tooling, graph ingestion, and API discovery/search.
- **Provenance-aware**: Items should be linkable to lineage artifacts under `data/surficial-geology/lineage/`.

### What belongs here

- STAC Item JSON files (`*.json`) that describe Surficial Geology deliverables.
- Optional integrity aids such as checksums/manifests if used by the pipeline.

### What does not belong here

- Actual data assets (GeoPackage, GeoJSON, MBTiles, etc.). Those belong under `data/surficial-geology/outputs/` and are referenced by `assets.*.href`.
- Raw sources (those belong under `data/surficial-geology/raw/`).
- Hand-edited “one-off” Items that cannot be regenerated.

---

## 🗂️ Directory Layout

~~~text
📁 items/                                           — STAC Item JSON (this directory)
├── 📄 README.md                                    — This file (conventions + validation rules)
├── 🧾 checksums.sha256                             — Optional: checksums for Item JSON files
├── 🧾 items.manifest.json                          — Optional: inventory of Item files + build params
├── 📄 surficial_geology_ks__<item_id>_v<ver>.json  — Example STAC Item (one per asset/deliverable)
└── 📁 shards/                                      — Optional: sharded layout for large item counts
    ├── 📁 00/                                      — Bucket (e.g., hash/prefix)
    │   └── 📄 <item_id>.json
    └── 📁 ff/
        └── 📄 <item_id>.json
~~~

Notes:

- `<item_id>` must be stable and unique within the Surficial Geology collection(s).
- `<ver>` is the dataset/deliverable version token selected by the pipeline config.
- Sharding is optional; use it only if the number of Item files becomes operationally inconvenient.

---

## 🧭 Context

These STAC Items are part of KFM’s catalog layer:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

In the Surficial Geology domain, a typical flow is:

1. Pipeline produces deliverables under `data/surficial-geology/outputs/`.
2. Pipeline emits/updates Collection JSON under `data/surficial-geology/stac/collections/`.
3. Pipeline emits/updates Item JSON here under `data/surficial-geology/stac/items/`.
4. Lineage summaries and/or run references are written under `data/surficial-geology/lineage/` and `mcp/runs/`.

---

## 📦 Data & Metadata

### Minimum STAC expectations (per Item)

Each Item JSON should include (at minimum, per STAC core):

- `type`: `Feature`
- `stac_version`
- `id`
- `geometry` + `bbox`
- `properties` (with `datetime` or an explicit interval)
- `links` (including a `collection` link)
- `assets` (each asset with `href`, and ideally `type` + `roles`)

### Assets should point to KFM outputs

- STAC Items should reference deliverables in `data/surficial-geology/outputs/` via `assets.*.href`.
- Prefer stable, versioned asset paths (e.g., filenames that include `_v<ver>`).
- When available, include integrity metadata (e.g., checksum fields) that correspond to the authoritative checksums/manifest stored alongside outputs.

### “Do not hand-edit” rule

If an Item is missing a field, has an incorrect footprint, or points to the wrong asset path, do not patch it manually. Fix the pipeline inputs/configuration so that regeneration produces the corrected Item deterministically.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Items in this directory should belong to one or more Collections defined under `../collections/`.
- Items should include a `links` entry with `rel: "collection"` pointing to the correct Collection JSON.

### DCAT

- STAC Items can be mapped to DCAT `dcat:Distribution` records (or distribution-like entities) for publication.
- License/rights must come from authoritative source manifests and governance policy—do not infer or guess.

### PROV

- The run that created/updated Items should be represented as a provenance activity.
- Lineage pointers should resolve to:
  - `data/surficial-geology/lineage/prov/` (PROV exports/summaries), and/or
  - `data/surficial-geology/lineage/openlineage/` (OpenLineage events/exports), and/or
  - `mcp/runs/` (run logs + config snapshots)

---

## 🧪 Validation & CI/CD

Minimum expectations for committed STAC Items:

- **JSON validity**: syntactically valid JSON and stable formatting rules (as configured).
- **STAC validity**: passes STAC schema/validator checks for the chosen STAC version/profile.
- **Link integrity**:
  - `links` include a valid `collection` reference
  - `assets.*.href` paths resolve to expected outputs (where CI is configured to check this)
- **Governance scans**: no secrets, no PII, and no disallowed precision when sensitivity/sovereignty flags apply.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `stac/items/` README defining STAC Item scope, naming/layout guidance, and linkage expectations to outputs + lineage. |

---

<div align="center">

🗺️ **Surficial Geology — STAC Items**  
KFM Data Layer · Catalog Metadata · Provenance-First

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

