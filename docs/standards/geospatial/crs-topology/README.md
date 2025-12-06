---
title: "📐 KFM v11.2.4 — CRS, Geometry & Topology Governance Standard"
path: "docs/standards/geospatial/crs-topology/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Spatial Governance Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x CRS/topology-contract compatible"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "geospatial-crs-topology"
  applies_to:
    - "ingest"
    - "etl"
    - "analysis"
    - "stac"
    - "dcat"
    - "graph"
    - "tiling"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask & zoom-governance rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/crs-topology-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/crs-topology/v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ttl_policy: "24 months"
sunset_policy: "Supersedes ad-hoc CRS/topology rules in v10.x stack"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "GeoSPARQL 1.1"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/architecture/map-stack-v10.4.md@v10.4.3"
  - "docs/standards/geospatial/crs-topology/README.md@v11.2.0"
  - "docs/standards/geospatial/crs-topology/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/crs-topology-standard-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/crs-topology-standard-v11.2.4-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:standards:crs-topology-v11.2.4"
semantic_document_id: "kfm-doc-crs-topology-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geospatial:crs-topology"

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
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true"
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_crs_rules_v10.4"
---

<div align="center">

# 📐 KFM v11.2.4 — CRS, Geometry & Topology Governance Standard  
Deterministic Coordinates · Clean Topology · GeoSPARQL / STAC / PROV-Aligned  

`docs/standards/geospatial/crs-topology/README.md`

**Purpose:**  
Define the **only approved rules** for Coordinate Reference Systems (CRS), geometry encoding, and topological relationships used in the Kansas Frontier Matrix (KFM). This standard ensures that every geometry in KFM — from raw ETL inputs to tiles, STAC/DCAT records, Neo4j graph objects, Story Nodes, and Focus Mode overlays — is **CRS-explicit**, **topologically valid**, and **provenance-traceable**, with behavior consistent across pipelines, catalogs, and frontends.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/geospatial/
├── 📂 geoprivacy-masking/
│   └── 📄 README.md                 # 🛡 Geoprivacy & masking standard
├── 📂 tiling-resolution/
│   ├── 📄 README.md                 # 🧩 Tiling & zoom governance
│   └── 📄 examples.md               # 📚 Tiling examples & profiles
└── 📂 crs-topology/
    └── 📄 README.md                 # 📐 This standard: CRS, geometry & topology
~~~

Related implementation & data locations (for reference):

~~~text
📂 src/
├── 📂 pipelines/
│   ├── 📂 ingest/
│   │   └── 📄 crs_normalization.py          # Enforce WGS84 storage, log CRS provenance
│   └── 📂 geometry/
│       ├── 📄 topology_cleaning.py          # Snap, fix, validate topology
│       └── 📄 reprojection_ops.py           # Deterministic CRS transforms
├── 📂 graph/
│   └── 📄 geometry_mapping.py               # Map CRS/topology into Neo4j & GeoSPARQL
└── 📂 api/
    └── 📂 geometry/
        └── 📄 validation_endpoints.py       # Optional geometry validation utilities

📂 schemas/
├── 📂 json/
│   └── 📄 crs-topology-standard-v11.2.4.schema.json
└── 📂 shacl/
    └── 📄 crs-topology-standard-v11.2.4-shape.ttl
~~~

Author rules:

- Any new CRS or topology-related guide must be placed under `docs/standards/geospatial/crs-topology/` and reference this file as canonical.  
- ETL and API configs must reference this standard where CRS or topology behavior is configured (e.g., comments or `kfm:crs_policy_ref`).

---

## 📘 Overview

KFM operates across multiple spatial scales and tools (ETL, STAC/DCAT catalogs, Neo4j, MapLibre/Cesium, Story Nodes). Without a **strict CRS and topology contract**, the system risks:

- Inconsistent coordinates between ETL, catalogs, graph, and tiles.  
- Topological errors (self-intersections, gaps, overlaps) that break analytics.  
- Ambiguous or undocumented reprojections that undercut reproducibility.  

This standard:

1. Defines **canonical KFM CRS policies** (storage, analytics, tiling, 3D/vertical).  
2. Establishes **geometry validity and orientation rules** (rings, multipart, precision).  
3. Governs **topology operations** (snapping, overlay, adjacency) and tolerances.  
4. Binds CRS & topology behavior to **STAC/DCAT/GeoSPARQL/PROV** metadata.  
5. Provides a contract for **Story Nodes and Focus Mode** so spatial reasoning is correct and reproducible.

All KFM geometry-handling code, configs, and datasets must conform to this standard unless an exception is explicitly documented and approved.

---

## 🧭 Context

This standard sits in the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

Within this pipeline:

- **CRS** determines how geometries are interpreted and transformed.  
- **Topology** controls the relationships between geometries (touching, overlapping, containing, disjoint).  
- **GeoSPARQL & KFM-OP v11** require **CRS-aware spatial predicates** and consistent geometry semantics.  

Key constraints from related standards:

- Geometries exposed via STAC/DCAT must be in **WGS84** (GeoJSON, STAC).  
- Tiles use Web Mercator-compatible tile matrices and respect zoom governance.  
- Geoprivacy & sovereignty rules require certain operations to be done **on a specific CRS representation** and logged with PROV.

This document is therefore a **foundational contract** for all spatial operations across KFM.

---

## 🧱 Architecture

### 1. Canonical CRS policy

**Storage & catalogs (authoritative):**

- All geometries stored in STAC/DCAT and the core KFM geometry store must use:

  - **CRS:** EPSG:4326 (WGS84, lon/lat).  
  - **Axis order:** `[longitude, latitude]` in GeoJSON / STAC.  

- Any ingest from other CRSs must:

  - Declare source CRS explicitly (e.g., EPSG:xxxx).  
  - Perform reprojection into EPSG:4326 using deterministic parameters.  
  - Record the transform in PROV (`prov:used` source CRS, `prov:wasGeneratedBy` reprojection activity).

**Web maps & tiling:**

- All public-facing tile services must use:

  - **Display CRS:** EPSG:3857-equivalent (Web Mercator) or officially supported Web-tiling CRS.  
  - Tile coordinates (x, y, z) consistent with MapLibre/Cesium defaults.

- Reprojection between EPSG:4326 and EPSG:3857 must be:

  - Implemented once in shared libraries (`reprojection_ops.py`).  
  - Logged with PROV for reproducibility if used in batch workflows.

**3D & vertical:**

- When 3D or elevation is required:

  - Prefer EPSG:4979 (WGS84 3D) for lat/lon + ellipsoidal height.  
  - Vertical datums (e.g., NAVD88) must be recorded in metadata (`kfm:vertical_datum`).  
  - 3D/vertical use is **optional but must be explicit**; no implicit assumptions.

### 2. Geometry encoding rules

For all GeoJSON / STAC geometries:

- **Allowed geometry types:**
  - `Point`, `MultiPoint`  
  - `LineString`, `MultiLineString`  
  - `Polygon`, `MultiPolygon`  
  - `GeometryCollection` (discouraged; use only when necessary).  

- **Rings orientation:**
  - Exterior rings: **counter-clockwise** (CCW) in coordinate order.  
  - Interior rings (holes): **clockwise** (CW).  

- **Precision:**
  - Storage precision: up to 7 decimal places (~1 cm).  
  - For public/tiling outputs: rounding to 5–6 decimal places is recommended; geoprivacy rules take precedence.

- **No mixed-CRS objects:**
  - Each geometry must be associated with a single CRS (EPSG:4326 authoritative).  
  - Mixed-CRS collections must be normalized by reprojection before storage.

### 3. Topology validity rules

KFM requires all stored geometries to be **topologically valid** under OGC rules:

- Polygons must not self-intersect.  
- Polygons/lines must not have duplicate consecutive vertices (except where required by ring closure).  
- Multi-geometries should not have overlapping parts unless explicitly modeled (e.g., overlapping MultiPolygon).  

**Topological cleaning pipeline (conceptual):**

1. Snap vertices to a defined tolerance (e.g., 1e-8 degrees) when merging datasets.  
2. Remove spikes, slivers, and zero-area polygons.  
3. Enforce ring orientation.  
4. Run validity checks (e.g., GEOS `IsValid` or equivalent).  
5. Log all modifications in PROV (original vs cleaned geometry references).

Topological errors found in ingest must not be silently ignored; they must be:

- Corrected and logged, or  
- Rejected with an error and flagged for manual review.

### 4. Topology and the Neo4j / GeoSPARQL graph

In the KFM Neo4j graph:

- Geometries are represented in EPSG:4326 (or a single chosen CRS per layer, with mapping metadata).  
- Topological relationships must use:

  - GeoSPARQL-compatible predicates: `sfWithin`, `sfContains`, `sfOverlaps`, `sfTouches`, `sfDisjoint`, etc.  
  - Deterministic tolerance parameters (snap distance, equality tolerance) defined in config and referenced by this standard.

- Example mapping:

  - A **County** node with `geom` property (Polygon) and `crs = "EPSG:4326"`.  
  - A **Site** node with Point geometry.  
  - Relationship `(:Site)-[:LOCATED_IN]->(:County)` must be supported by a GeoSPARQL `sfWithin` test under configured tolerance.

Any derived topology (e.g., adjacency graphs of counties, connectivity graphs of rivers) must be:

- Computed with deterministic CRS and tolerance settings.  
- Stored with provenance indicating CRS, tolerance, and algorithm/version.

---

## 🗺️ Diagrams

### 1. CRS & topology pipeline

~~~mermaid
flowchart LR
    A[Raw Data\nvarious CRS] --> B[CRS Detection & Validation]
    B --> C[Deterministic Reprojection\n→ EPSG:4326 storage]
    C --> D[Topology Cleaning & Validation]
    D --> E[STAC/DCAT Geometries]
    D --> F[Neo4j / GeoSPARQL Graph]
    E --> G[Tiling & APIs\n(EPSG:3857 display)]
    F --> H[Story Nodes & Focus Mode]
~~~

---

## 📦 Data & Metadata

### 1. Required CRS metadata fields

Where applicable (STAC/DCAT/graph configs):

- `kfm:storage_crs` — canonical CRS for the dataset (e.g., `"EPSG:4326"`).  
- `kfm:display_crs` — CRS used in UI/tiles (e.g., `"EPSG:3857"`).  
- `kfm:source_crs` — original CRS(es) for ingested data (if not EPSG:4326).  
- `kfm:crs_transform_ref` — reference to transform configuration / PROV bundle.  
- `kfm:vertical_datum` — if vertical coordinates present (e.g., `"NAVD88"`).

Example:

~~~json
{
  "kfm:storage_crs": "EPSG:4326",
  "kfm:display_crs": "EPSG:3857",
  "kfm:source_crs": ["EPSG:26914"],
  "kfm:crs_transform_ref": "prov/crs_reprojection_run_2025-12-06.jsonld"
}
~~~

### 2. Topology metadata fields

Optional but recommended:

- `kfm:topology_clean_profile` — ID of cleaning rules (snap tolerance, min area).  
- `kfm:topology_validated` — boolean; indicates geometry has passed validity checks.  
- `kfm:topology_version` — version of topology rules applied (e.g., `"v11.2.4"`).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- All STAC Items must use GeoJSON geometries in EPSG:4326.  
- CRS metadata is implicit in STAC, but KFM-specific fields (`kfm:storage_crs`, `kfm:display_crs`) may be added for clarity.  
- Topology-related information (e.g., adjacency to counties) is typically modeled in the graph, not STAC, but references may be included as `kfm:*` fields.

### DCAT

- DCAT datasets should:

  - Use `dct:spatial` and geometry encodings consistent with WGS84.  
  - Include CRS metadata in custom extensions (`kfm:storage_crs`, etc.).  
  - Reference this CRS/topology standard via `dct:conformsTo`.

### PROV

- CRS and topology operations must be encoded as:

  - `prov:Activity` — reprojection run, topology cleaning run.  
  - `prov:Entity` — original geometry, transformed geometry.  
  - `prov:used` — source CRS definition, initial geometry dataset.  
  - `prov:wasGeneratedBy` — link to reprojection/cleaning activity.

Example conceptual snippet:

~~~json
{
  "@id": "urn:kfm:activity:crs-reprojection:2025-12-06",
  "@type": "prov:Activity",
  "prov:used": [
    "urn:kfm:dataset:raw:soils_epsg26914",
    "urn:ogc:def:crs:EPSG::26914"
  ],
  "prov:generated": [
    "urn:kfm:dataset:processed:soils_epsg4326"
  ]
}
~~~

---

## 🧪 Validation & CI/CD

KFM CI must include CRS/topology checks as part of:

- Ingest tests.  
- Catalog validation.  
- Graph topology tests.

Minimum checks:

1. **CRS declaration check:**

   - No dataset can be ingested without a declared source CRS.  
   - Reprojection to EPSG:4326 must be configured and logged.

2. **Geometry validity check:**

   - Use a geometry library (e.g., GEOS) to assert `IsValid` on all geometries after cleaning.  
   - Reject or flag invalid geometries; do not silently accept.

3. **Topology consistency tests:**

   - For key datasets (counties, HUCs, etc.), enforce:
     - No overlaps beyond a defined tolerance (unless intended).  
     - Coverage completeness (e.g., counties cover Kansas extent with no gaps beyond tolerance).  

4. **Graph predicate tests:**

   - Sample Neo4j graph relationships and confirm they match spatial predicates (e.g., `LOCATED_IN` matches `sfWithin`).

5. **CI wiring:**

   - Tests should live under `tests/geospatial/test_crs_topology.py` (or similar).  
   - `.github/workflows/kfm-ci.yml` must run these tests for any change touching geometry logic or data.

---

## 🧠 Story Node & Focus Mode Integration

CRS/topology correctness is critical for narrative integrity:

- Story Nodes referencing places must assume:

  - EPSG:4326 lat/lon coordinates.  
  - Topological assertions (e.g., “within Sedgwick County”, “along the Arkansas River”) that match the graph and geometry.

Focus Mode:

- Must transform map interactions (clicks, extents) consistently between:

  - Display CRS (Web Mercator) and storage CRS (EPSG:4326).  
  - 2D maps and 3D/vertical views when used.

If CRS or topology are misconfigured, Story Nodes may point to the wrong place or misstate relationships; this standard exists to prevent that.

---

## ⚖ FAIR+CARE & Governance

This standard supports FAIR+CARE by:

- **FAIR**
  - *Findable*: geometry and CRS metadata enable spatial search and filtering.  
  - *Accessible*: consistent CRS across catalogs makes it easy to reuse and visualize datasets.  
  - *Interoperable*: alignment with GeoSPARQL, STAC, DCAT, and PROV ensures compatibility with external tools.  
  - *Reusable*: well-defined CRS and topology rules prevent subtle bugs in downstream analyses.

- **CARE & sovereignty**
  - Accurate CRS and topology are essential when respecting Tribal boundaries, cultural landscapes, and sacred regions.  
  - Misaligned CRS can misplace or distort boundaries, undermining sovereign decision-making.  
  - Governance bodies must be able to trust that spatial relationships reflect reality within known tolerances.

Any change to:

- Canonical storage CRS,  
- Acceptable reprojection pipelines, or  
- Topology tolerances for culturally sensitive boundaries

is a **governance change**, not only a technical decision, and requires formal review and documentation.

---

## 🕰️ Version History

| Version    | Date       | Status            | Notes                                                                                                 |
|-----------:|------------|-------------------|-------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Active / Enforced | Current CRS/topology governance standard; codifies EPSG:4326 storage, EPSG:3857 display, and topology rules. |
| v11.2.2    | 2025-11-28 | Superseded        | Added topology cleaning guidance and graph alignment; incomplete CI integration.                      |
| v11.2.0    | 2025-11-20 | Superseded        | Initial v11 CRS policy draft; lacked explicit topology and GeoSPARQL alignment.                      |
| v10.4.3    | 2023-10-03 | Legacy            | Pre-KFM CRS usage; ad-hoc reprojection and topology checks.                                          |

---

<div align="center">

📐 **KFM v11.2.4 — CRS, Geometry & Topology Governance Standard**  
Deterministic Coordinates · Clean Topology · FAIR+CARE Sovereignty  

[📘 Docs Root](../../../..) · [📂 Geospatial Standards](../README.md) · [🧩 Tiling Standard](../tiling-resolution/README.md) · [🛡 Geoprivacy Masking](../geoprivacy-masking/README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>

