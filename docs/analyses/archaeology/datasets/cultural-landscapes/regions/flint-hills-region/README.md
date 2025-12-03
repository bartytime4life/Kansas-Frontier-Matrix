---
title: "🗺️ KFM v11.2.3 — Flint Hills Eco-Cultural Landscape Region (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/README.md"
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
intent: "cultural-landscape-region-flint-hills"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **KFM — Flint Hills Eco-Cultural Landscape Region**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/README.md`

**Purpose:**  
Define the **Flint Hills Eco-Cultural Landscape Region** dataset within the Kansas Frontier Matrix (KFM).  
This region provides a **generalized eco-cultural landscape** used for:

- Settlement pattern and interaction analysis in a tallgrass prairie context  
- Story Node narratives centered on the Flint Hills escarpment and prairie corridor  
- Focus Mode v2/v3 interpretive overlays and explainability chips  
- MapLibre & Cesium regional polygons with governed zoom behavior  
- Eco-cultural modeling of lithic provisioning, subsistence, and mobility  
- Integration of archaeological, environmental, and historical evidence  

This document specifies the **data layout**, **metadata profile**, **provenance expectations**, and **governance rules** unique to the Flint Hills region while remaining aligned with the global cultural landscape region standard.

</div>

---

## 📘 Conceptual Overview

The **Flint Hills Eco-Cultural Landscape Region** represents a **generalized eco-cultural zone** characterized by:

- Tallgrass prairie and dissected uplands  
- Widespread chert-bearing formations and lithic raw material sources  
- Strong connections between topography, soils, grasslands, and cultural use  
- Long-term continuity of grazing, hunting, and movement corridors

Key conceptual properties:

- **Eco-cultural**: defined by combined ecological and cultural signatures rather than strict political or administrative boundaries.  
- **Lithic-linked**: the distribution of chert and related stone resources is a major organizing factor in cultural activity.  
- **Multi-phase**: used as an analytic unit across multiple cultural phases (e.g., Woodland, Late Prehistoric, Protohistoric), expressed via OWL-Time.  
- **Sensitivity-aware**: boundaries are generalized; **no site-level or resource-precise geometry** is exposed in public datasets.

The Flint Hills region provides a **meso-scale scaffold** that connects:

- Site clusters and survey blocks (internally)  
- Lithic sources, soils, eco-regions, and hydrology layers  
- Narrative structures about movement, land use, and resource provisioning.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/
├── 📄 README.md                                # This file (Flint Hills region dataset standard)
│
├── 📁 data/                                    # Region geometries and derivatives
│   ├── 🌐 geojson/                             # Generalized polygons (EPSG:4326) for public use
│   │   ├── flint-hills-region.v1.geojson
│   │   └── flint-hills-region.v1-topology-simplified.geojson
│   └── 🔷 h3/                                  # H3 mosaic representations (for zoom- or sensitivity-aware views)
│       └── flint-hills-region-h3-r6.v1.geojson
│
├── 🗂️ stac/                                   # STAC Items & Collections for the Flint Hills region
│   ├── collection-flint-hills-region-v1.json
│   └── item-flint-hills-region-v1.json
│
├── 🧾 metadata/                                # DCAT, JSON-LD, narrative/context metadata
│   ├── dcat-flint-hills-region-v1.jsonld
│   └── context-flint-hills-region-v1.md
│
└── 🧬 provenance/                              # Optional region-local pointers; canonical logs live in ../provenance/
    └── flint-hills-region-v1.prov-ref.json
~~~

**Directory contract:**

- Canonical **provenance logs** for the Flint Hills region reside in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `flint-hills-region-v1.json`), with this directory optionally containing lightweight references.  
- `data/` geometries must be **derived from internal, more detailed sources**, but **only generalized outputs** are stored here.  
- STAC and metadata files must remain synchronized with:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md`.

---

## 🌄 Region Definition (Flint Hills Eco-Cultural Region)

The Flint Hills Eco-Cultural Landscape Region must define:

| Element                   | Requirement |
|---------------------------|------------|
| **Region Name**          | `"Flint Hills Eco-Cultural Landscape Region"` (or equivalent human-readable label) |
| **Region Identifier**    | Slug: `flint-hills-region` (used in STAC IDs, files, and graph nodes) |
| **Region Kind**          | `"eco-cultural"` (may include `"upland-escarpment"` or similar ontology tags) |
| **Temporal Span**        | OWL-Time intervals for relevant cultural phases (e.g., Woodland, Late Prehistoric, Protohistoric) |
| **Spatial Representation** | Generalized polygons and optional H3 mosaics characterizing the Flint Hills eco-cultural zone (CRS = EPSG:4326) |
| **Environmental Context** | Tallgrass prairie, chert-bearing formations, soils, slope/relief, hydrology context |
| **Cultural Connections** | Settlement clustering, land-use patterns, lithic provisioning, mobility corridors, and interaction networks |
| **Sources**              | Archaeological syntheses, geological and geomorphological mapping, paleoenvironmental and historical sources |
| **Sensitivity Classification** | CARE-compliant (`generalized` or `restricted-generalized`) with documented visibility rules |

---

## 📦 Metadata Profile (Flint Hills Region)

### ✔ STAC Item / Collection

The STAC representation for this region must include:

- `id`  
  - Example: `"kfm-arch-lands-flint-hills-region-v1"`  
- `bbox`  
  - Generalized bounding box of the Flint Hills region.  
- `geometry`  
  - Polygon/MultiPolygon describing the generalized region (no site-level precision), CRS = EPSG:4326.  
- `properties` (selected fields):  
  - `kfm:region_slug = "flint-hills-region"`  
  - `kfm:region_kind = "eco-cultural"`  
  - `kfm:culture_phase`: array of cultural phase labels (e.g., `["Woodland", "Late Prehistoric", "Protohistoric"]`)  
  - `kfm:temporal_coverage`: OWL-Time-compatible temporal representation  
  - `kfm:lithic_context`: optional field summarizing lithic provisioning relevance (e.g., `"chert-rich upland zone"`)  
  - `care:sensitivity`: `"generalized"` or `"restricted-generalized"`  
  - `care:visibility_rules`: `"polygon-generalized"`, `"h3-only"`, or governed combinations  
  - `kfm:provenance`: reference to PROV-O provenance record under `../provenance/`  
- `assets`:  
  - `data`: link(s) into `data/geojson/` and/or `data/h3/` within this directory.

### ✔ DCAT & Context Metadata

Under `metadata/`, DCAT/JSON-LD records must specify:

- `dct:title`: `"Flint Hills Eco-Cultural Landscape Region"`  
- `dct:description`: region purpose, derivation, and eco-cultural context.  
- `dct:temporal`: temporal coverage consistent with STAC and provenance.  
- `dct:license`: `CC-BY 4.0` (or stricter if required by governance).  
- `dcat:keyword`:  
  - Examples: `"Flint Hills"`, `"eco-cultural region"`, `"tallgrass prairie"`, `"chert"`, `"upland escarpment"`.

The context markdown (`context-flint-hills-region-v1.md`) can include:

- Human-readable narrative of eco-cultural logic.  
- Diagrams schematizing relationships between geology, ecology, and cultural use.  
- Explicit descriptions of the generalization and CARE decision-making process.

---

## ⚖ CARE & Sovereignty Requirements

The Flint Hills region must follow all global CARE rules, with specific expectations:

- `care:sensitivity` must reflect the **aggregated risk** of exposing lithic resources, site clusters, or culturally significant patterns:
  - `"generalized"` is acceptable for appropriately abstracted polygons.  
  - `"restricted-generalized"` may be required if risk remains after generalization.
- `care:review` should record the review path, such as:
  - `"faircare"`  
  - `"tribal"` (where sovereign input is relevant)  
  - `"faircare+tribal"` for shared or multi-community contexts.
- `care:notes` must:
  - Explain how geomorphic, ecological, and cultural information were generalized.  
  - Describe any exclusions or suppressed subregions for cultural or sovereignty reasons.
- `care:visibility_rules` must:
  - Govern zoom behaviors in web clients (e.g., polygon only at regional zoom, H3 at coarser or alternative zooms).  
  - Prevent users from inferring site-level precision or resource exactness.

**Forbidden for this public dataset:**

- Geometries that can be reasonably used to reverse-engineer precise lithic quarry locations or sensitive sites.  
- Any mapping of confidential or contested cultural boundaries that have not been approved for public display.

---

## 🧬 Provenance Requirements

The Flint Hills region must have at least one PROV-O provenance log under:

- `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `flint-hills-region-v1.json`)

Expected content in the provenance log:

- **Entities (`prov:Entity`)**:
  - `raw`: internal eco-region, geology, survey, and site-based evidence.  
  - `generalized`: Flint Hills generalized region polygon/H3 mosaic used in public datasets.  
  - `processed`: final published Flint Hills region dataset v1 tied to STAC/metadata.

- **Activities (`prov:Activity`)**:
  - `generalization`: polygon simplification, buffering, clipping, and H3 generation steps.  
  - `boundary_estimation`: decisions about where the eco-cultural region starts/ends.  
  - `review`: FAIR+CARE and (if applicable) tribal review of the region representation.

- **Agents (`prov:Agent`)**:
  - `analyst`: GIS/archaeology analyst responsible for the dataset.  
  - `faircare`: FAIR+CARE governance group.  
  - `tribal`: relevant sovereign reviewers (where engaged).

- **CARE fields**:
  - `care:sensitivity`, `care:notes`, and `care:visibility_rules` aligned with this README.  

The local file `provenance/flint-hills-region-v1.prov-ref.json` may:

- Provide a resolvable pointer to the canonical provenance JSON-LD.  
- Offer a summary useful for UI components and tooling.

---

## 🧭 Spatial Specifications

- CRS: **EPSG:4326** for all public geometries stored here.  
- Generalization must:
  - Use documented algorithms (e.g., Douglas–Peucker simplification) with parameters recorded in provenance.  
  - Produce valid, topologically sound polygons (no self-intersections, no slivers).  
  - Avoid “hugging” any internal dataset so tightly that it suggests site-level detail.

- The Flint Hills region geometry should:

  - Represent an eco-cultural band, not a hyper-precise geologic line.  
  - Reflect combined interpretations of geology, vegetation, and cultural evidence.  
  - Be representable as both polygons and H3 mosaics for different zoom levels and sensitivity controls.

---

## 🕰️ Temporal Specifications

- Temporal coverage must capture:

  - The range of cultural phases for which the Flint Hills region is treated as a meaningful analytic unit in KFM.  

- OWL-Time representations should:

  - Use intervals (`time:Interval`) with `time:hasBeginning` / `time:hasEnd` when possible.  
  - Include mappings to KFM’s internal cultural phase ontology (`kfm:culture_phase`).

- Temporal uncertainty:

  - Where phase boundaries or dates are uncertain, encode ranges or uncertainty notes.  
  - Maintain consistency between STAC, DCAT, and provenance records.

---

## 🧪 Validation & CI/CD

The Flint Hills region dataset must pass all applicable validations before publication:

- **Schema validation**
  - Region metadata profile (KFM archaeology region schema).  
  - CARE schema for sensitivity and review fields.  
  - DCAT and STAC schemas.

- **Provenance validation**
  - PROV-O JSON-LD compliance.  
  - Consistent `kfm:provenance` references between this dataset, STAC, and provenance logs.  
  - CARE fields in provenance aligned with region metadata.

- **Generalization validation**
  - Polygon and H3 generalizations meet abstraction requirements.  
  - No geometry violates sovereignty or confidentiality expectations.

### Indicative CI Workflows

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  

CI must **block**:

- Any update that modifies geometry or temporal coverage without updated provenance.  
- Any change that weakens CARE protections or alters visibility rules without governance approval.  
- Any inconsistency between this README, STAC, metadata, and provenance documents.

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From this dataset, KFM graph loaders create:

- **Nodes**
  - `CulturalRegion { slug: "flint-hills-region" }`  
  - `EcoRegion` (tallgrass prairie / related eco-units)  
  - `GeologicUnit` (chert-bearing formations; generalized)  
  - `CulturalPhase` (Woodland, Late Prehistoric, Protohistoric, etc.)  
  - `ProvenanceRecord`

- **Relationships**
  - `ASSOCIATED_WITH` (region ↔ eco-regions, geologic units, hydrology units).  
  - `OCCURRED_DURING` (region ↔ cultural phases/intervals).  
  - `HAS_PROVENANCE` (region ↔ provenance record).  
  - `HAS_SENSITIVITY` (region ↔ sensitivity classification).  
  - `HAS_LITHIC_CONTEXT` (region ↔ lithic-related concepts, where modeled).

### Story Nodes

Story Nodes using the Flint Hills region should:

- Reference the region slug (`flint-hills-region`) and/or STAC ID.  
- Provide narratives about:

  - Eco-cultural dynamics of the tallgrass prairie.  
  - Lithic provisioning and its impact on regional networks.  
  - Changes in land use across cultural phases.

- Use provenance to:

  - Expose reasoning and evidence behind the region definition.  
  - Communicate limitations and generalization choices.  
  - Surface CARE and sovereignty context where relevant.

### Focus Mode v2/v3

Focus Mode behaviors for this region include:

- Region-aware overlays that:

  - Show eco-cultural summaries in map panels.  
  - Render provenance and CARE badges as chips.  
  - Enforce zoom-dependent visibility rules (e.g., polygon vs H3).

- Model constraints to:

  - Prevent inference of site-level lithic sources from the public region geometry.  
  - Respect uncertainty and multi-phase nature in textual or visual explanations.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed dataset spec, layout, and CI/CARE/provenance requirements for Flint Hills Eco-Cultural Region; aligned with KFM-MDP v11.2.2 and global region standard. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Regions](../README.md) · [⬅ Back to Cultural Landscapes](../../README.md)

</div>