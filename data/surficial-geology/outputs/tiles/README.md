---
title: "🗺️ Surficial Geology — Tiles"
path: "data/surficial-geology/outputs/tiles/README.md"

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
    - "data/surficial-geology/outputs/tiles/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:outputs-tiles-readme:v0.1.0"
semantic_document_id: "surficial-geology-outputs-tiles-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:outputs-tiles-readme:v0.1.0"

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

# 🗺️ **Surficial Geology — Tiles**
`data/surficial-geology/outputs/tiles/README.md`

**Purpose**  
Define what belongs in `outputs/tiles/`, how tile artifacts are named/versioned, how they are served for map clients, and how tiles are linked to `outputs/metadata/` plus STAC/DCAT/PROV.

</div>

---

## 📘 Overview

This directory holds **web-map tiling distributions** for Surficial Geology outputs (typically vector tiles packaged as `.mbtiles`). Tile artifacts are:

- **Derived** from canonical vector outputs (e.g., `outputs/vectors/`)
- **Deterministic** (re-creatable from tracked inputs + build config)
- **Distribution-oriented** (optimized for map rendering, not editing)

Related docs:

- `../README.md` — output directory conventions
- `../metadata/README.md` — sidecar manifests, schemas, PROV summaries (when present)

---

## 🗂️ Directory Layout

~~~text
📁 tiles/                                        — Tiling distributions (this directory)
├── 📄 README.md                                 — This file (tile conventions + serving notes)
├── 📄 surficial_geology_ks_v<ver>.mbtiles        — Vector tileset package (preferred distribution)
├── 📄 surficial_geology_ks_v<ver>.tilejson       — TileJSON descriptor (optional, if emitted)
└── 📄 surficial_geology_ks_v<ver>.style.json     — Style fragment/source hints (optional)
~~~

Notes:

- `<ver>` is the dataset output version token chosen by the deterministic pipeline (match `outputs/` conventions).
- Keep naming stable and boring. Avoid ad-hoc subfolders unless the pipeline contract requires it.

---

## 🧭 Context

Tiles sit at the “map delivery” edge of KFM’s pipeline:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

This folder exists so the frontend (MapLibre/Cesium) and downstream services can use **fast, cached, versioned** distributions, while still retaining strong provenance back to canonical sources.

---

## 📦 Data & Metadata

### What a tile artifact represents

A committed tileset (e.g., `.mbtiles`) MUST be traceable back to:

- the canonical vector export version it was built from
- the tile build parameters (zoom bounds, simplification, layer name, attribute allowlist)
- the exact toolchain versions (where relevant)

Those details should be recorded in sidecar metadata under `../metadata/` (for example `export.manifest.json` and `prov.run.json` if used in this dataset).

### Naming and versioning

- File stems should be lowercase with underscores: `surficial_geology_ks_*`
- Include `_v<ver>` in every artifact name.
- Emit one authoritative tileset per output version (avoid multiple competing mbtiles for the same version).

### Tile scheme expectations (when vector tiles)

- Tile addressing: XYZ / z-x-y
- Projection: Web Mercator (EPSG:3857) for map client compatibility
- Vector tile encoding: MVT / PBF inside the tileset (MBTiles `format` typically `pbf`)

### MBTiles metadata expectations

If `.mbtiles` is committed, it SHOULD contain coherent metadata (at minimum):

- `minzoom`, `maxzoom`
- `bounds` (lon/lat WGS84 bounds, per MBTiles conventions)
- `center` (optional but recommended)
- `name`, `description` (human-facing)

Any additional tile-layer schema expectations should be cross-referenced to `../metadata/attributes.schema.json` (when present) to keep tiles aligned with canonical field definitions.

### Serving tiles (important)

Most browser map clients do not read `.mbtiles` directly. `.mbtiles` typically needs:

- a tile server that can expose `/tiles/{z}/{x}/{y}.pbf` (or equivalent), or
- a deterministic export to a static Z/X/Y directory or archive (only if the pipeline defines it)

Serving details (endpoints, caching, headers) belong in the API/ops layer docs, but the build should record enough information to reproduce the served result.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Tiles should be referenced as STAC assets from the Surficial Geology STAC Items/Collections.
- Asset recommendations:
  - `roles`: include `tile` (and `data` where appropriate)
  - `type`: reflect the container/encoding (tileset packages vs JSON descriptors)
  - `checksum:sha256`: include when checksums are tracked

### DCAT

- Each committed tile artifact corresponds to a `dcat:Distribution` for the Surficial Geology dataset.
- The distribution should carry:
  - `mediaType` (or equivalent)
  - access URL / download URL (as governed by deployment)
  - license/rights inherited from the authoritative dataset record (do not guess)

### PROV

- The tile build is a `prov:Activity`.
- The `.mbtiles` output is a `prov:Entity` that:
  - `prov:wasGeneratedBy` the tile build activity
  - `prov:wasDerivedFrom` the canonical vector export (and any intermediate derivations, if recorded)

---

## 🧪 Validation & CI/CD

Minimum expectations before committing or publishing tiles:

- **Determinism**: build parameters and tool versions recorded (manifest or provenance summary).
- **Spatial sanity**:
  - bounds match expected coverage
  - tiles render in the expected area and do not appear shifted (projection/axis issues)
- **Schema sanity**:
  - vector tile layer name(s) stable across versions
  - attribute fields match the declared schema/allowlist (when enforced)
- **Integrity**:
  - checksums updated (if `checksums.sha256` is used for this dataset’s outputs)
  - STAC/DCAT references point to the correct versioned artifact paths

Governance scans MUST pass: no secrets, no PII, and no disallowed sensitive precision.

---

## ⚖ FAIR+CARE & Governance

Tile outputs can amplify risk because they are easy to consume at scale.

When building tiles:

- prefer generalization/simplification appropriate to the highest published zoom
- enforce a maximum zoom ceiling when higher precision could increase harm
- if sovereignty/sensitivity flags apply, document the decision in metadata + provenance and ensure published distributions respect those constraints

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `tiles/` README defining tile artifact conventions, serving expectations, and STAC/DCAT/PROV linkage guidance. |

---

<div align="center">

🗺️ **Surficial Geology — Tiles**  
KFM Data Layer · Map Distributions · Provenance-First

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

