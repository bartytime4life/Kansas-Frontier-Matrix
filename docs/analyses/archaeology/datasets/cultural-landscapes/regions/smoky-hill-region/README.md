---
title: "🗺️ KFM v11.2.3 — Smoky Hill Cultural Drainage Region (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Dataset"
intent: "cultural-landscape-region-smoky-hill"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **KFM — Smoky Hill Cultural Drainage Region**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/README.md`

**Purpose:**  
Define the **Smoky Hill Cultural Drainage Region** dataset within the Kansas Frontier Matrix (KFM).  
This region provides a **generalized fluvial cultural landscape** used for:

- Multi-phase settlement and interaction analysis along the Smoky Hill system  
- Story Node narratives centered on the Smoky Hill drainage corridor  
- Focus Mode v2/v3 interpretive overlays and explainability chips  
- MapLibre & Cesium regional polygons with governed zoom behavior  
- Modeling of riverine movement, exchange, and landscape use  
- Integration of archaeological, geomorphological, and environmental evidence  

This document specifies the **data layout**, **metadata profile**, **provenance expectations**, and **governance rules** unique to the Smoky Hill region while remaining aligned with the global cultural landscape region standard.

</div>

---

## 📘 Conceptual Overview

The **Smoky Hill Cultural Drainage Region** represents a **generalized fluvial landscape** focused on:

- The Smoky Hill River and key tributaries within the KFM scope  
- Valley and adjacent upland systems that structure movement and settlement  
- Long-term patterns of riverine subsistence, travel, and exchange  
- Fluvial landforms (terraces, floodplains, bluffs) tied to cultural activity  

Key conceptual properties:

- **Cultural drainage corridor**: the river and its valley function as a connective axis across cultural phases.  
- **Multi-phase**: spans multiple cultural periods (e.g., Woodland, Late Prehistoric, Protohistoric), represented via OWL-Time.  
- **Geomorphically grounded**: region geometry is derived from basin-scale hydrology, valley morphology, and adjacent eco-regions, then generalized.  
- **Sensitivity-aware**: boundaries are generalized; **no site-level or feature-precise geometry** is exposed publicly.

The Smoky Hill region acts as a **meso-scale scaffold** linking:

- Internal site clusters and survey records  
- Hydrology, soils, terrain, and eco-regions  
- Story Nodes about riverine mobility, interaction, and landscape change.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/
├── 📄 README.md                                # This file (Smoky Hill region dataset standard)
│
├── 📁 data/                                    # Region geometries and derivative products
│   ├── 🌐 geojson/                             # Generalized polygons (EPSG:4326) for public use
│   │   ├── smoky-hill-region.v1.geojson
│   │   └── smoky-hill-region.v1-topology-simplified.geojson
│   └── 🔷 h3/                                  # H3 mosaic representations (for sensitivity-aware views)
│       └── smoky-hill-region-h3-r6.v1.geojson
│
├── 🗂️ stac/                                   # STAC Items & Collections for this region
│   ├── collection-smoky-hill-region-v1.json
│   └── item-smoky-hill-region-v1.json
│
├── 🧾 metadata/                                # DCAT, JSON-LD, narrative/context metadata
│   ├── dcat-smoky-hill-region-v1.jsonld
│   └── context-smoky-hill-region-v1.md
│
└── 🧬 provenance/                              # Optional region-local pointers; canonical logs live in ../provenance/
    └── smoky-hill-region-v1.prov-ref.json
~~~

**Directory contract:**

- Canonical **provenance logs** for the Smoky Hill region live in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `smoky-hill-region-v1.json`), with this directory optionally containing thin reference files.  
- `data/` geometries must be **derived from more detailed internal sources**, but **only generalized outputs** are stored here.  
- `stac/` and `metadata/` must remain synchronized with:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md` and the region metadata registry.

---

## 🌄 Region Definition (Smoky Hill Cultural Drainage Region)

The Smoky Hill Cultural Drainage Region must define:

| Element                   | Requirement |
|---------------------------|------------|
| **Region Name**          | `"Smoky Hill Cultural Drainage Region"` (or equivalent human-readable label) |
| **Region Identifier**    | Slug: `smoky-hill-region` (used in STAC IDs, files, and graph nodes) |
| **Region Kind**          | `"drainage"` and optionally `"eco-cultural"` |
| **Temporal Span**        | OWL-Time intervals covering relevant cultural phases (e.g., Woodland, Late Prehistoric, Protohistoric) |
| **Spatial Representation** | Generalized polygons and optional H3 mosaics describing the Smoky Hill corridor (CRS = EPSG:4326) |
| **Environmental Context** | Fluvial system (channel, floodplain, terraces), adjacent uplands, soils, and eco-regions |
| **Cultural Connections** | Settlement clustering, movement routes, interaction networks, subsistence regimes tied to the drainage |
| **Sources**              | Archaeological syntheses, geomorphological mapping, hydrological models, historical cartography, and environmental proxies |
| **Sensitivity Classification** | CARE-compliant (`generalized` or `restricted-generalized`) with documented visibility rules |

---

## 📦 Metadata Profile (Smoky Hill Region)

### ✔ STAC Item / Collection

The STAC representation for this region must include:

- `id`  
  - Example: `"kfm-arch-lands-smoky-hill-region-v1"`  
- `bbox`  
  - Generalized bounding box of the Smoky Hill region (no site-level precision).  
- `geometry`  
  - Polygon/MultiPolygon for the generalized region; CRS = EPSG:4326.  
- `properties` (selected fields):  
  - `kfm:region_slug = "smoky-hill-region"`  
  - `kfm:region_kind = "drainage"` (and optionally `"eco-cultural"`)  
  - `kfm:culture_phase`: array of cultural phase labels (e.g., `["Woodland", "Late Prehistoric", "Protohistoric"]`)  
  - `kfm:temporal_coverage`: OWL-Time-compatible temporal representation  
  - `kfm:fluvial_context`: optional descriptor (e.g., `"Smoky Hill corridor; multi-terrace valley system"`)  
  - `care:sensitivity`: `"generalized"` or `"restricted-generalized"`  
  - `care:visibility_rules`: `"polygon-generalized"`, `"h3-only"`, or governed combinations  
  - `kfm:provenance`: reference to PROV-O provenance record under `../provenance/`  
- `assets`:  
  - `data`: link(s) into `data/geojson/` and/or `data/h3/` inside this directory.

### ✔ DCAT & Context Metadata

Under `metadata/`, DCAT/JSON-LD records must specify:

- `dct:title`: `"Smoky Hill Cultural Drainage Region"`  
- `dct:description`: region purpose, derivation, and fluvial/cultural context.  
- `dct:temporal`: temporal coverage matching STAC and provenance.  
- `dct:license`: `CC-BY 4.0` (or stricter per governance).  
- `dcat:keyword`:  
  - Examples: `"Smoky Hill"`, `"cultural drainage"`, `"fluvial landscape"`, `"valley corridor"`, `"protohistoric"`.

The context markdown (`context-smoky-hill-region-v1.md`) should:

- Provide human-readable narrative of the drainage logic.  
- Summarize fluvial geomorphology, ecology, and cultural evidence.  
- Document generalization and CARE decision-making.

---

## ⚖ CARE & Sovereignty Requirements

The Smoky Hill region must comply with global CARE rules, with specific requirements:

- `care:sensitivity` reflects the combined risk of exposing sensitive archaeological patterns along the drainage:
  - `"generalized"` is acceptable for appropriately abstracted polygons.  
  - `"restricted-generalized"` may be required if risks persist after generalization.  
- `care:review` must record the governance path:
  - `"faircare"`  
  - `"tribal"` (where sovereign review is relevant)  
  - `"faircare+tribal"` for shared or multi-community contexts.  
- `care:notes` must:
  - Explain how hydrology, geomorphology, and cultural information were generalized.  
  - Document any segments intentionally excluded or suppressed.  
- `care:visibility_rules` must:
  - Govern zoom-dependent visibility in web clients.  
  - Prevent inference of site-level or highly sensitive features from public geometries.

**Forbidden for this public dataset:**

- Geometries enabling reverse-engineering of precise site clusters or sensitive localities along the drainage.  
- Public mapping of confidential or contested cultural boundaries that are not approved for dissemination.

---

## 🧬 Provenance Requirements

The Smoky Hill region must have at least one PROV-O provenance log under:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `smoky-hill-region-v1.json`)

Expected content in the provenance log:

- **Entities (`prov:Entity`)**:
  - `raw`: detailed hydrology, geomorphology, internal artifact distributions, and survey data.  
  - `generalized`: Smoky Hill generalized region polygon/H3 mosaic used in public datasets.  
  - `processed`: final Smoky Hill region dataset v1 linked to STAC/metadata.

- **Activities (`prov:Activity`)**:
  - `generalization`: creation of generalized polygons and H3 mosaics from internal datasets.  
  - `boundary_estimation`: determination of upstream/downstream extents and lateral valley limits.  
  - `review`: FAIR+CARE and (if applicable) tribal review.

- **Agents (`prov:Agent`)**:
  - `analyst`: GIS/archaeology analyst responsible for dataset creation.  
  - `faircare`: FAIR+CARE governance group.  
  - `tribal`: relevant sovereign reviewers (where engaged).

- **CARE fields**:
  - `care:sensitivity`, `care:notes`, and `care:visibility_rules` must align with this README.

The local file `provenance/smoky-hill-region-v1.prov-ref.json` may:

- Provide a resolvable pointer to canonical provenance JSON-LD.  
- Offer a compact summary for UIs and tooling (non-authoritative).

---

## 🧭 Spatial Specifications

- CRS: **EPSG:4326** for all public geometries in this directory.  
- Generalization must:

  - Use documented algorithms (e.g., Douglas–Peucker simplification, buffered valley envelopes) with parameters recorded in provenance.  
  - Produce valid, topologically correct polygons (no self-intersections).  
  - Avoid hugging fluvial or site distributions so tightly that it implies hidden, precise datasets.

- The Smoky Hill region geometry should:

  - Capture the main drainage corridor and relevant valley/upland context.  
  - Reflect an **analytic unit**, not a cadastral or political boundary.  
  - Exist as both polygons and H3 mosaics to support multi-scale and sensitivity-aware visualizations.

---

## 🕰️ Temporal Specifications

- Temporal coverage must represent:

  - The span of cultural phases for which the Smoky Hill drainage functions as a meaningful analytical region in KFM.

- OWL-Time representations should:

  - Use `time:Interval` with `time:hasBeginning` and `time:hasEnd` when possible.  
  - Include mappings to KFM’s cultural-phase ontology (`kfm:culture_phase`).

- Temporal uncertainty must be:

  - Represented via ranges, fuzzy bounds, or explicit notes, where needed.  
  - Consistent across STAC, DCAT, and provenance records.

---

## 🧪 Validation & CI/CD

The Smoky Hill region dataset must pass all relevant validations before publication:

- **Schema validation**
  - Region metadata schema (KFM archaeology region profile).  
  - CARE schema for sensitivity, review, and visibility fields.  
  - DCAT and STAC schema validation.

- **Provenance validation**
  - PROV-O JSON-LD structure and linkage.  
  - Consistent `kfm:provenance` references among this README, STAC, metadata, and provenance logs.  

- **Generalization validation**
  - Polygon/H3 generalizations meet abstraction requirements.  
  - No geometry violates sovereignty or confidentiality rules.

### Indicative CI Workflows

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  

CI must **block**:

- Any geometry or temporal changes without updated provenance.  
- Any weakening of CARE protections or alteration of visibility rules without governance approval.  
- Any inconsistency between this README, STAC, metadata, and provenance artifacts.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From this dataset, KFM graph loaders create:

- **Nodes**
  - `CulturalRegion { slug: "smoky-hill-region" }`  
  - `HydrologicalUnit` (Smoky Hill sub-basin units, generalized)  
  - `CulturalPhase` nodes tied to the archaeology ontology  
  - `ProvenanceRecord` nodes from canonical provenance logs  

- **Relationships**
  - `ASSOCIATED_WITH` (region ↔ hydrological units, eco-regions, geomorphic units).  
  - `OCCURRED_DURING` (region ↔ cultural phases/intervals).  
  - `HAS_PROVENANCE` (region ↔ provenance record).  
  - `HAS_SENSITIVITY` (region ↔ sensitivity classification).

### Story Nodes

Story Nodes using the Smoky Hill region should:

- Reference the region slug (`smoky-hill-region`) and/or STAC ID.  
- Anchor narratives about:

  - Riverine corridors of movement and exchange.  
  - Shifts in settlement and land use along the Smoky Hill system.  
  - Environmental and hydrological changes impacting cultural patterns.

- Use provenance to:

  - Explain evidence and uncertainties behind the region definition.  
  - Surface review status (FAIR+CARE, tribal) and CARE context.

### Focus Mode v2/v3

Focus Mode behavior for this region includes:

- Region-aware overlays that:

  - Show fluvial and cultural summaries in map panels.  
  - Render provenance and CARE badges as chips.  
  - Enforce zoom-dependent behavior (polygon vs H3, hide vs show) per `care:visibility_rules`.

- Model constraints that:

  - Prevent Focus Mode from presenting speculative, overly precise boundaries or claims not grounded in provenance.  
  - Respect multi-phase nature and uncertainty in textual and visual explanations.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed dataset spec, layout, and CI/CARE/provenance requirements for Smoky Hill Cultural Drainage Region; aligned with KFM-MDP v11.2.2 and global region standard. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Regions](../README.md) · [⬅ Back to Cultural Landscapes](../../README.md)

</div>