---
title: "🪨 Surficial Geology — Outputs"
path: "data/surficial-geology/outputs/README.md"

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
    - "data/surficial-geology/outputs/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:outputs-readme:v0.1.0"
semantic_document_id: "surficial-geology-outputs-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:outputs-readme:v0.1.0"

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

# 🪨 **Surficial Geology — Outputs**
`data/surficial-geology/outputs/README.md`

**Purpose**  
Document what belongs in `data/surficial-geology/outputs/`, how artifacts are named and versioned, and how outputs are linked into STAC/DCAT/PROV for the KFM pipeline.

</div>

---

## 📘 Overview

This directory holds **generated, versioned deliverables** for the Surficial Geology data domain. Treat everything under `outputs/` as:

- **Derived** (never the authoritative source of truth)
- **Reproducible** (re-creatable from tracked inputs + config)
- **Referenceable** (linked as assets from STAC/DCAT and as entities in PROV)

### What belongs here

- Canonical export formats used by downstream systems (API, web map, analysis).
- Sidecar metadata that describes the exports (schemas, checksums).
- Optional “distribution” artifacts (tiles, simplified derivatives) when generated deterministically.

### What does not belong here

- Raw source drops (place those under `data/raw/` with a source manifest).
- Temporary caches, scratch work, or workstation-specific exports.
- Manually edited shapefiles/GeoJSON “fixes” (fix the pipeline instead).

---

## 🗂️ Directory Layout

~~~text
📁 outputs/                                     — Generated deliverables (this directory)
├── 📄 README.md                                — This file (conventions + regeneration rules)
├── 🧾 checksums.sha256                         — SHA-256 checksums for committed artifacts
├── 📁 vectors/                                 — Vector deliverables (if produced)
│   ├── 📄 surficial_geology_ks_v<ver>.gpkg      — Canonical GeoPackage export
│   ├── 📄 surficial_geology_ks_v<ver>.geojson   — Interchange GeoJSON (often simplified)
│   └── 📄 surficial_geology_ks_v<ver>.parquet   — Analytics-friendly columnar export (optional)
├── 📁 tiles/                                   — Web tiling artifacts (optional)
│   └── 📄 surficial_geology_ks_v<ver>.mbtiles   — Vector tileset for map clients
└── 📁 metadata/                                — Sidecar metadata (machine-readable)
    ├── 🧾 attributes.schema.json                — Field dictionary + types + constraints
    ├── 🧾 export.manifest.json                  — File list + sizes + checksums + build params
    └── 🧾 prov.run.json                         — PROV summary for the build that produced outputs
~~~

Notes:

- `<ver>` is the dataset output version (e.g., `v2025.12.14` or `v0.3.0`), chosen by the pipeline config.
- Keep the tree “boring”: stable names, stable ordering, and no ad-hoc folders.

---

## 🧭 Context

These artifacts sit in the KFM pipeline at the “distribution” edge:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

In practice, `outputs/` exists so that:

- **Catalogs** can point to durable, versioned files.
- **Graph ingestion** can treat each deliverable as a typed entity with provenance.
- **UI layers** (MapLibre/Cesium) can consume optimized distributions (e.g., tiles).

---

## 📦 Data & Metadata

### Naming and versioning

- Use lowercase, underscore-separated file stems: `surficial_geology_ks_*`.
- Every generated file name MUST include a version token: `_v<ver>`.
- Prefer emitting a **single canonical “best”** export per format per version.

### Format expectations

Keep exports deterministic and interoperable:

- Vector: GeoPackage (`.gpkg`) preferred for canonical; GeoJSON for interchange; Parquet for analytics.
- Tiles: `.mbtiles` only if reproducibly generated and schema-stable.
- Always embed or record CRS/axis order explicitly (format-native where possible; otherwise in sidecars).

### Sidecar metadata (required when artifacts are committed)

- `checksums.sha256` must include every committed deliverable in this folder (and subfolders).
- `attributes.schema.json` must define:
  - column/field names
  - types
  - allowed values (where constrained)
  - required/optional flags
- `export.manifest.json` should capture:
  - build config identifiers
  - source manifest identifiers (checksums or ids)
  - tool versions (where relevant)
  - output file inventory (paths, sizes, checksums)

### “Do not hand-edit” rule

If an artifact is wrong, do not patch it in-place. Update inputs/config/code so the deterministic build produces the corrected artifact and regenerates checksums + provenance.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- `outputs/` files are referenced as STAC assets.
- STAC records should live under `data/stac/` (collection + items) and point to the outputs as `assets.*.href`.
- Each asset should include:
  - `type` (media type)
  - `roles` (e.g., `data`, `metadata`, `tile`, `schema`)
  - `checksum:sha256` when available

### DCAT

- The Surficial Geology dataset is represented as a DCAT `dcat:Dataset`.
- Each file in `outputs/` corresponds to a DCAT `dcat:Distribution` with `dct:format` / `mediaType`.
- License/rights for the dataset MUST be taken from the authoritative source manifest and/or catalog record (do not guess).

### PROV

- Each build that produces artifacts here is a `prov:Activity`.
- Each output file is a `prov:Entity` with:
  - `prov:wasGeneratedBy` → the build activity
  - `prov:wasDerivedFrom` → raw inputs (and intermediate entities where recorded)
- Build logs/config snapshots should be stored under `mcp/runs/` and referenced from `prov.run.json`.

---

## 🧪 Validation & CI/CD

Minimum expectations for committed outputs:

- **Checksums**: `checksums.sha256` updated and matches file contents.
- **Schema stability**: `attributes.schema.json` updated for any field changes.
- **Geometry sanity** (when vector):
  - valid geometries
  - consistent CRS
  - bounded to expected spatial extent
- **Catalog integrity**:
  - STAC/DCAT records (when present) reference the exact output paths
  - PROV summary references the producing run and inputs
- **Governance scans**: no secrets, no PII, and no disallowed sensitive precision.

---

## ⚖ FAIR+CARE & Governance

Even “public” geospatial layers can create harm when combined with other data. When preparing outputs:

- Prefer aggregation/generalization where outputs could enable sensitive inference.
- If sovereignty or sensitivity flags apply, record the decision in:
  - catalog metadata (STAC/DCAT)
  - provenance (PROV)
  - this directory’s manifests

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `outputs/` README defining artifact conventions, sidecar metadata expectations, and STAC/DCAT/PROV linkage guidance. |

---

<div align="center">

🪨 **Surficial Geology — Outputs**  
KFM Data Layer · Deterministic Artifacts · Provenance-First

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

