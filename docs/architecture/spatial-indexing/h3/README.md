---
title: "🧭 Kansas Frontier Matrix — H3 Spatial Indexing & Hex-Based Joins"
path: "docs/architecture/spatial-indexing/h3/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Spatial Systems Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture Standard"
intent: "spatial-indexing-h3"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Spatial Systems Board"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:architecture:spatial-indexing:h3:v11.2.6"
semantic_document_id: "kfm-architecture-spatial-indexing-h3-v11.2.6"
event_source_id: "ledger:kfm:doc:architecture:spatial-indexing:h3:v11.2.6"
doc_integrity_checksum: "<sha256>"

commit_sha: "<latest-commit-hash>"
provenance_chain:
  - "docs/architecture/spatial-indexing/h3/README.md@v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

scope:
  domain: "spatial-architecture"
  applies_to:
    - "data/**/raw/**"
    - "data/**/processed/**"
    - "data/**/stac/**"
    - "src/etl/**"
    - "docs/story-nodes/**"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — H3 Spatial Indexing & Hex-Based Joins**
`docs/architecture/spatial-indexing/h3/README.md`

**Purpose**  
Define the **canonical, enforceable use of H3 hexagonal indexing** across KFM for deterministic,
multi-resolution spatial joins and aggregation—while preserving authoritative geometry and provenance.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. What H3 is used for in KFM

This standard defines the canonical use of **Uber H3** as a **deterministic spatial key** across the
Kansas Frontier Matrix (KFM) to enable:

- fast joins between **point observations** and **polygonal boundaries**
- geometry-free rollups for **analytics**, **map rendering**, and **Story Nodes**
- stable multi-resolution aggregation via **parent/child** relationships
- consistent spatial semantics across **ETL → catalogs → graph → API → UI**

H3 is treated as a **first-class spatial identifier**, not a visualization convenience.

### 2. What H3 is not

- H3 does **not** replace authoritative source geometry.
- H3-derived joins are **approximate** and must be labeled as such when used for interpretation.
- H3 cell membership must not be interpreted as “regulatory alignment” or “ground truth authority.”

### 3. Normative rules

1. **CRS rule (MUST)**  
   All H3 computations MUST be performed from coordinates in **WGS84 lat/lon** (EPSG:4326).

2. **Determinism rule (MUST)**  
   H3 library versions, resolution policies, and join modes MUST be config-driven, version-pinned,
   and reproducible.

3. **Non-destructive rule (MUST)**  
   H3 indices are derived fields. Raw geometries and source identifiers MUST remain preserved and
   traceable.

4. **Resolution governance rule (MUST)**  
   Every dataset using H3 MUST declare the resolution(s) used and the purpose of each resolution.

---

## 🗂️ Directory Layout

Recommended placement for H3 policies, utilities, schemas, and index artifacts:

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                                — Documentation layer
│   ├── 📁 architecture/                                    — Architecture standards (ETL → graph → API → UI)
│   │   ├── 📁 spatial-indexing/
│   │   │   ├── 📁 h3/
│   │   │   │   ├── 📄 README.md                            — ← This standard
│   │   │   │   └── 📄 resolutions.md                       — Resolution policy and rationale (if split out)
│   │   │   └── 📄 README.md                                — Spatial indexing index (domain entrypoint)
│   │   └── 📄 README.md                                    — Architecture index
│   └── 📁 standards/                                       — Governance, FAIR+CARE, sovereignty
│       ├── 📁 governance/
│       │   └── 📄 ROOT-GOVERNANCE.md
│       ├── 📁 faircare/
│       │   └── 📄 FAIRCARE-GUIDE.md
│       └── 📁 sovereignty/
│           └── 📄 INDIGENOUS-DATA-PROTECTION.md
├── 📁 src/
│   └── 📁 etl/
│       └── 📁 spatial/
│           └── 📁 h3/                                      — H3 derivation + join utilities (deterministic)
├── 📁 schemas/
│   ├── 📁 json/                                            — Machine validation for H3 artifacts
│   └── 📁 shacl/                                           — Graph constraints for H3Cell nodes (if used)
└── 📁 data/
    ├── 📁 processed/                                       — Derived, replayable products
    │   └── 📁 spatial_index/
    │       └── 📁 h3/                                      — Hex-key tables (by AOI/resolution)
    └── 📁 stac/                                            — STAC Collections/Items for published artifacts
        └── 📁 spatial_index/
            └── 📁 h3/
~~~


---

## 🧭 Context

### 1. Where H3 sits in the KFM pipeline

H3 indexing is applied **after geometry normalization** and **before graph/API consumption**:

- **ETL**: compute H3 keys as derived attributes (points, polygons, and aggregates)
- **Catalogs**: publish H3-indexed tables as STAC assets / DCAT distributions
- **Graph**: use H3 cells as joinable spatial identifiers (optional node model)
- **API/UI**: serve aggregated hex layers without heavy client-side geometry processing
- **Story Nodes / Focus Mode**: drive narrative overlays from cataloged, provenance-backed assets

### 2. Primary use cases

- point → polygon joins (e.g., sensors to counties, census tracts, watershed units)
- dense observation rollups (e.g., daily PM2.5 aggregates by cell)
- performance-first queries (H3 key joins vs repeated polygon intersections)
- privacy-aware generalization (use coarser resolutions to avoid exposing sensitive point locations)

---

## 🧱 Architecture

### 1. Canonical H3 key conventions

KFM uses a stable, explicit naming convention for H3 keys:

- `h3_index` — H3 cell ID as a lowercase string
- `h3_res` — integer resolution (0–15)
- `h3_rXX` — optional explicit resolution columns when storing multi-res keys  
  Example: `h3_r06`, `h3_r08`, `h3_r10`

When multi-resolution is stored, parent/child derivations MUST be reproducible (no cached lookup-only
behavior without a pinned source).

### 2. Ingestion patterns

#### Point observations (lat/lon)

- Compute `h3_index` at the declared resolution using WGS84 coordinates.
- Store source geometry or coordinates separately.
- Store both:
  - the chosen analysis resolution key (e.g., `h3_r08`)
  - and, when required, a parent key for rollups (e.g., `h3_r06`)

#### Polygon datasets (boundaries / coverage)

For polygons, H3 must be represented explicitly as a **set of cells** (polyfill) at the join resolution:

- `polygon_id` (stable dataset identifier)
- `h3_res`
- `h3_index` (repeated, one row per cell) OR a compacted representation stored as an asset

**Rule:** Polygon-to-H3 conversions MUST declare the polyfill mode (interior-only vs boundary-inclusive)
and how holes are treated.

### 3. Canonical join patterns (hex-based joins)

#### Pattern A — Point ↔ Polygon (membership join)

1. Point: derive `point.h3_index` at join resolution.
2. Polygon: precompute `polygon_cells(h3_index)` via polyfill.
3. Join: `point.h3_index = polygon_cells.h3_index`.

This is the canonical “geometry-free” join and is preferred for large volumes.

#### Pattern B — Point ↔ Polygon (validation join)

When high-stakes accuracy is required, validate H3-based membership with a geometry operation:

- H3 join proposes the candidate polygon(s)
- a final geometry predicate confirms membership (e.g., within)

This pattern is recommended for regulated or compliance-aligned analyses.

#### Pattern C — Aggregation by H3

For time-series observations:

- group by `(date, h3_index)` and aggregate numeric fields
- retain observation counts and completeness metrics per cell

---

## 📦 Data & Metadata

### 1. Minimum schema for H3-keyed tables

All H3-keyed tabular artifacts MUST include:

- `h3_index` (string)
- `h3_res` (integer)
- `time_*` fields when temporal (e.g., `date` or `datetime`)
- `source_id` / `dataset_id` (stable identifier for provenance join)
- `aggregation_method` when aggregated
- `quality_flags` and/or `completeness` metrics when derived

### 2. Integrity and replay

- Derived H3 artifacts MUST be reproducible from declared inputs and configs.
- Store a manifest/metadata sidecar for checksums and run identifiers (location per domain standard).

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

H3-derived products SHOULD be published as STAC Items with:

- stable `id` that encodes AOI + resolution + temporal coverage (when applicable)
- `properties` capturing:
  - `kfm:h3_res`
  - `kfm:h3_join_mode`
  - `kfm:spatial_aoi_id`
- `assets` including:
  - the H3-keyed table (e.g., Parquet/CSV)
  - a metadata/manifest artifact (checksums + schema refs)
  - a provenance artifact (PROV JSON/TTL/JSON-LD as used in KFM)

### 2. DCAT

DCAT mirroring SHOULD express:

- the H3 product as a `dcat:Dataset`
- each file/table as a `dcat:Distribution`
- a clear statement that H3 is a **derived indexing layer**, not the authoritative geometry

### 3. PROV-O

Every published H3 artifact MUST be linkable to provenance:

- `prov:Entity` — raw source geometry / raw observations / derived H3 table
- `prov:Activity` — CRS normalization / H3 derivation / aggregation / publish
- `prov:Agent` — KFM pipeline runner + referenced governance plans

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Raw geometry or point observations"] --> B["Normalize CRS to WGS84"]
  B --> C["Derive H3 keys at configured resolution"]
  C --> D["Hex-keyed join tables and aggregates"]
  D --> E["Publish STAC assets and DCAT records"]
  E --> F["Ingest to graph and API layer"]
  F --> G["Render map layers and Story Nodes"]
~~~

Explanation: H3 indexing is a deterministic **derived layer** that enables fast joins and rollups
while preserving source geometry and catalog/provenance links.

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node usage

Story Nodes SHOULD reference cataloged H3-indexed artifacts rather than ad-hoc aggregations.

Typical narrative layers supported by this standard:

- “hotspot” comparisons by place and time (hex-aggregated)
- rural vs urban contrasts using a consistent cell resolution
- long-run trends visualized as resolution-stable grids

### 2. Focus Mode constraints

Focus Mode MAY summarize this document and extract schema/metadata, but MUST NOT invent
governance status, provenance, or architectural capabilities beyond what is declared.

---

## 🧪 Validation & CI/CD

Minimum checks that MUST pass for this document and any H3-indexed artifacts:

| Check | What it validates |
|---|---|
| `markdown-lint` | Approved H2s, ordering, and heading structure |
| `schema-lint` | YAML front-matter schema compliance |
| `diagram-check` | Mermaid parse + allowed diagram profiles |
| `footer-check` | Governance links present and ordered |
| `accessibility-check` | Heading order, list semantics, basic a11y |
| `secret-scan` | No credentials/tokens |
| `pii-scan` | No obvious PII leakage |
| `provenance-check` | Version history coherence + provenance linkage expectations |

H3-specific validation requirements (data-plane):

- H3 indices must be parseable and match declared `h3_res`
- CRS normalization must be recorded (WGS84 requirement)
- Join mode must be declared (membership-only vs validated)

---

## ⚖ FAIR+CARE & Governance

### 1. Authority and interpretation

- High sensor density does not imply authority.
- H3 aggregation should be treated as a **computational convenience**, not as a new “boundary” with
  inherent meaning.

### 2. Safety, privacy, and sovereignty

- Sensitive overlays and Indigenous community data require governance review and may require
  coarser resolution publication or masking.
- Do not publish H3 layers that enable re-identification of individuals or sensitive locations.

### 3. Governance accountability

- Changes to resolution defaults, join modes, or publishing rules require review by the Spatial Systems
  Board and FAIR+CARE Council as defined in the governance references.

---

## 🕰️ Version History

| Version | Date | Change |
|---|---:|---|
| v11.2.6 | 2025-12-12 | Re-structured to KFM-MDP ordering; formalized join patterns, metadata rules, and governance footer. |

---

<div align="center">

🧭 **Kansas Frontier Matrix — H3 Spatial Indexing & Hex-Based Joins**  
Designed for Longevity · Governed for Integrity

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📘 Docs Root](../../../README.md) ·
[🏗️ Architecture Index](../../README.md) ·
[🗺️ Spatial Indexing Index](../README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6

</div>