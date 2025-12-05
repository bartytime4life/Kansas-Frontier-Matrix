---
title: "🗺️ KFM v11.2.4 — Geospatial Standards Index"
path: "docs/standards/geospatial/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Spatial & Sovereignty Board"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Standards Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "geospatial"
  applies_to:
    - "ingest"
    - "etl"
    - "analysis"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/geospatial-standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/geospatial-standards-v1.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:standards:geospatial-index-v11.2.4"
semantic_document_id: "kfm-doc-geospatial-standards-index-v11.2.4"
event_source_id: "ledger:kfm:doc:standards:geospatial"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🗺️ KFM v11.2.4 — Geospatial Standards Index  
`docs/standards/geospatial/README.md`

**Purpose:**  
Provide the canonical index for KFM geospatial standards — including geoprivacy, masking, tiling, coordinate systems, and spatial semantics — so all ETL, graph, API, Story Node, and Focus Mode behavior is deterministic, catalog-aligned, and sovereignty-respecting.

</div>

---

## 📘 Overview

KFM’s geospatial stack spans:

- Raw and processed spatial datasets (points, lines, polygons, rasters).  
- STAC/DCAT catalogs for discoverability and licensing.  
- Neo4j graph representations of places, events, and spatial relationships.  
- MapLibre/Cesium frontends for 2D/3D visualization.  
- Story Nodes and Focus Mode for narrative overlays on space-time.  

This index:

- Locates geospatial standards under `docs/standards/geospatial/`.  
- Defines how geospatial standards interact with KFM’s pipeline and ontologies.  
- Points to **Geoprivacy & Masking** and future geospatial standards (tiling, CRS, topologies).  
- Establishes governance and CI hooks that geospatial standards must respect.  

All new geospatial standards **must** link back to this index in their front-matter and follow KFM-MDP v11.2.4.

---

## 🗂️ Directory Layout

```text
📂 docs/standards/geospatial/
├── 📄 README.md                           # 🗺️ Geospatial Standards Index (this file)
├── 📂 geoprivacy-masking/                 # 🛡️ Geoprivacy & cultural-safety masking
│   ├── 📄 README.md                       # 🛡️ Geospatial Privacy & Cultural-Safety Masking Standard
│   ├── 📂 examples/
│   │   └── 📄 validation-tests.md         # 🧪 Example unit/integration test patterns
│   └── 📂 schemas/
│       └── 📄 geoprivacy-masking-v1.json  # 📦 JSON Schema for masking metadata blocks
├── 📂 tiling-resolution/                  # 🧱 (Reserved) Tiling schemes & level-of-detail policies
│   └── 📄 README.md                       # 🧱 Tiling & LOD standard (to be created)
└── 📂 crs-topology/                       # 🌐 (Reserved) CRS, projections, topology & snapping rules
    └── 📄 README.md                       # 🌐 CRS & topology standard (to be created)
```

Author rules:

- Every subdirectory under `docs/standards/geospatial/` **must** contain a `README.md` describing its scope, affected modules, and links to schemas/examples.  
- New geospatial standards must be added to this tree, with clear emojis and concise comments, and their `README.md` files must link back to this index.  

---

## 🧭 Context

KFM’s geospatial standards apply across the entire pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

Within this context:

- **Geoprivacy & masking**  
  - Ensures sensitive and sacred sites are never exposed as raw coordinates.  
  - Provides deterministic donut masking, linked to sovereignty decisions and geoethical metadata.  

- **Tiling & resolution (reserved)**  
  - Will standardize spatial resolutions, zoom levels, and level-of-detail policies for tiles and overlays.  

- **CRS & topology (reserved)**  
  - Will define canonical CRS usage (e.g., EPSG codes), reprojection rules, and topology/ snapping behaviors.  

Geospatial standards must:

- Be compatible with KFM’s ontology protocol (KFM-OP), including place/event modeling and GeoSPARQL alignment.  
- Integrate with the **Geoethical Reflection Layer** for Story Nodes, particularly where mapping reveals or abstracts sensitive sites.  
- Support Focus Mode’s need for stable spatial references and predictable generalization.

---

## 🧱 Architecture

From an architecture standpoint, geospatial standards sit above and constrain:

- `src/pipelines/*` — ingest and ETL (masking, CRS normalization, tiling prep).  
- `src/graph/*` — spatial node/relationship modeling and stored geometries.  
- `src/api/*` — geospatial endpoints, filters, and bounding-box queries.  
- `src/web/*` — MapLibre/Cesium layers, selection tools, and overlays.  

### 1. Module boundaries

Typical module boundaries influenced by this index:

- `src/pipelines/geospatial/`  
  - Implement masking, H3 indexing, tiling preparation, and CRS normalization according to standards here.  

- `src/graph/spatial/`  
  - Define labels and relationships such as `:Place`, `:Region`, `:Boundary`, and connections to masked geometries.  

- `src/api/geospatial/`  
  - Expose bounding-box queries, tile endpoints, geosearch, and sensitivity-aware access.  

- `src/web/map/` & `src/web/cesium/`  
  - Render masked locations, generalized regions, and H3 grids.  
  - Respect zoom-dependent visibility rules and access labels.  

Any new geospatial capability (e.g., corridor masking, river network generalization) must identify:

- A standard under `docs/standards/geospatial/...`.  
- A clear mapping from requirements → ETL → graph → API → frontend.

---

## 📦 Data & Metadata

Geospatial standards define how spatial datasets and layers are **described**, **masked**, and **cataloged**.

Key expectations for all geospatial data in KFM:

- **Explicit geoprivacy metadata**  
  - Sensitivity labels (`public`, `community`, `sensitive`, `sacred`).  
  - Masking method, radius bounds, and seed strategy (as defined in the Geoprivacy & Masking Standard).  

- **STAC/DCAT-consistent fields**  
  - STAC Item properties for geometry, bounding box, and geoethical/geo-privacy metadata.  
  - DCAT Dataset fields for access rights, license, and spatial coverage.  

- **Graph-mappable semantics**  
  - Places, regions, and boundaries modeled as nodes/relations that can be surfaced in Story Nodes and Focus Mode.  

The **Geoprivacy & Cultural-Safety Masking Standard** provides required JSON keys (e.g., `kfm:privacy_method`, `kfm:sensitivity_label`, `kfm:masking_run_id`) and PROV references; this index treats that document as the authoritative source for masking-specific metadata.

---

## 🌐 STAC, DCAT & PROV Alignment

All geospatial standards under this index must be STAC/DCAT/PROV-aligned:

- **STAC**
  - Collections and Items for spatial datasets must:
    - Record geometry and bounding boxes according to the tiling / CRS standards.  
    - Include privacy and geoethical properties when masking or sovereignty restrictions apply.  

- **DCAT**
  - DCAT Datasets must:
    - Use `dct:spatial` and `dct:coverage` for spatial extents.  
    - Map access rights and geoprivacy labels into `dct:accessRights`, `dct:rights`.  

- **PROV-O**
  - ETL activities (masking, tiling, reprojection) must:
    - Represent masking jobs as `prov:Activity`.  
    - Link original and masked geometries as `prov:Entity` with `prov:used` and `prov:wasGeneratedBy`.  

This index does **not** redefine those standards; it requires that any geospatial standard:

- Explicitly state its STAC/DCAT/PROV mappings.  
- Reuse KFM profiles (KFM-STAC, KFM-DCAT, KFM-PROV) instead of inventing new fields without schema updates.

---

## 🧠 Story Node & Focus Mode Integration

Geospatial standards directly shape how Story Nodes and Focus Mode operate:

- **Story Nodes**
  - Spatial extents must follow CRS, masking, and tiling conventions defined under this index.  
  - Geoethical metadata (`kfm_geoethics`) must respect geoprivacy rules, especially for `sensitive` and `sacred` labels.  
  - Frontend components (Story Node maps) must not override or sharpen generalized geometries.  

- **Focus Mode**
  - Focus Mode overlays (map, 3D, timeline) must:
    - Use masked geometries and access labels from STAC/DCAT/graph, not derive their own.  
    - Honoring H3-based generalization and zoom-level constraints.  
  - Graph-local views must be aware of spatial sensitivity (e.g., not clustering sacred nodes into compact centroids).  

New Story Node or Focus Mode features that manipulate or filter spatial context must:

- Reference relevant geospatial standards in their front-matter.  
- Demonstrate, via tests, that they do not violate masking or sovereignty rules.

---

## 🧪 Validation & CI/CD

Geospatial standards carry specific CI/CD expectations, which should be implemented in `.github/workflows/kfm-ci.yml` (or derivative workflows):

- **Schema validation**
  - JSON Schemas under `docs/standards/geospatial/*/schemas/*.json` must be validated during CI.  

- **Geoprivacy tests**
  - Masking behavior (distance bounds, determinism, anti-triangulation) must be tested as defined in the Geoprivacy & Masking Standard.  

- **Geometry & CRS checks (future standards)**
  - Validate CRS usage, reprojection correctness, and geometry validity (no self-intersections, degenerate polygons).  

- **Catalog sync**
  - Verify that STAC/DCAT records for spatial datasets carry required geoprivacy, access, and spatial metadata fields.  

- **Frontend integration tests**
  - Map/3D-related tests must confirm that masked / generalized geometries are used and that sacred/sensitive layers obey zoom and access constraints.  

Any addition to `docs/standards/geospatial/` must include:

- At least one CI test category referencing the new standard.  
- A clear mapping from standard → test implementation path.

---

## ⚖ FAIR+CARE & Governance

Geospatial standards are a primary enforcement surface for FAIR+CARE and Indigenous data sovereignty:

- **FAIR**
  - *Findable*: spatial datasets and their masking/geoethics metadata are cataloged and queryable.  
  - *Accessible*: spatial information is available at controlled resolutions, with clear access rights.  
  - *Interoperable*: uses shared vocabularies (STAC, DCAT, PROV, GeoSPARQL).  
  - *Reusable*: datasets include sufficient metadata and masking to prevent harmful reuse.  

- **CARE & sovereignty**
  - *Collective benefit*: geospatial standards favor community-beneficial uses over extractive behaviors.  
  - *Authority to control*: Indigenous and local governance determines sensitivity labels, masking radii, and allowed resolutions.  
  - *Responsibility*: masking, CRS, and tiling choices must be justified, documented, and audited.  
  - *Ethics*: geospatial decisions explicitly consider risks of re-identification, site looting, and cultural harm.  

Governance expectations:

- Geospatial standards are subject to review by:
  - FAIR+CARE Council.  
  - Tribal Sovereignty Board (where Indigenous datasets and sites are involved).  
  - KFM Governance maintainers.  
- Any deviation from these standards must be:
  - Explicitly documented in a standards exception doc.  
  - Reviewed and approved before implementation.

### 📚 Reference Standards & Resources (Footer)

- [FAIR Principles](https://www.go-fair.org/fair-principles/)  
- [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care)  
- [CIDOC-CRM](https://www.cidoc-crm.org/) · [PROV-O](https://www.w3.org/TR/prov-o/) · [GeoSPARQL](https://www.ogc.org/standard/geosparql/)  
- [KFM Governance Framework](../governance/ROOT-GOVERNANCE.md)  
- [KFM Markdown Authoring Protocol — KFM-MDP v11.2.4](../kfm_markdown_protocol_v11.2.4.md)  
- [Geospatial Privacy & Cultural-Safety Masking Standard](./geoprivacy-masking/README.md)  
- [Geoethical Reflection Layer for Story Nodes](../../frontend/story-nodes/geoethical-reflection/README.md)  

These links form the **canonical footer** for geospatial standards; reuse and extend as necessary while keeping governance links intact.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                                          |
|--------:|------------|-------------------|------------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial KFM-MDP v11.2.4–aligned Geospatial Standards Index; anchors geoprivacy & future specs. |

Future revisions must:

- Add new geospatial standards as subdirectories with READMEs and schemas.  
- Update references to masking, tiling, CRS, and topology standards as they are created or revised.  
- Keep governance and FAIR+CARE references synchronized with KFM-wide standards.

---

<div align="center">

🗺️ **KFM v11.2.4 — Geospatial Standards Index**  
Scientific Insight · FAIR+CARE Ethics · Sovereignty-First Geospatial Design  

[📘 Docs Root](../../..) · [📂 Standards Index](../README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>