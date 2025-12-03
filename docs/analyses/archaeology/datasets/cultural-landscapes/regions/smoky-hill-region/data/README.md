---
title: "📂 KFM v11.2.3 — Smoky Hill Cultural Drainage Region Data Layout (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with v11.2.3 cultural-landscape-region data-contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Region Data Layout"
intent: "cultural-landscape-region-smoky-hill-data"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📂 **KFM — Smoky Hill Cultural Drainage Region · Data Layout**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/README.md`

**Purpose:**  
Define and govern the **on-disk data layout** for the **Smoky Hill Cultural Drainage Region**.  
This directory holds the **generalized public geometries** (polygons + H3 mosaics) and compatible derivatives used by:

- Smoky Hill region STAC Collections & Items  
- Neo4j graph loaders and ETL pipelines  
- Story Nodes and Focus Mode v2/v3 overlays  
- MapLibre & Cesium drainage-scale visualizations  

All files here are **derived** from more detailed internal sources and must remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **graph-safe**.

</div>

---

## 📘 Overview

The **Smoky Hill Cultural Drainage Region** uses this `data/` directory to store:

- **Generalized polygon geometries** (GeoJSON, EPSG:4326) describing the Smoky Hill river corridor and adjacent valley/upland context  
- **H3 mosaic representations** at governed resolution(s) for sensitivity-aware rendering  
- Optional **tiling or convenience products** if introduced later (e.g., pre-baked tilesets or masks)  

Key constraints:

- Only **generalized**, **non-site-precise** geometries are allowed here.  
- All geometries must match the **region semantics** defined in:  
  - `../README.md` (Smoky Hill region spec)  
  - `../metadata/` (region metadata registry)  
  - `../provenance/` and global `../../../../provenance/` (canonical provenance logs)  
- Any change to these geometries must be captured in **PROV-O provenance** and must pass CI validation.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/smoky-hill-region/data/
├── 📄 README.md                                    # This file (data layout & constraints)
│
├── 🌐 geojson/                                     # Generalized drainage-region polygons (EPSG:4326)
│   ├── smoky-hill-region.v1.geojson               # Primary drainage region boundary (generalized polygon)
│   └── smoky-hill-region.v1-topology-simplified.geojson
│       # Topology-safe simplified outline for small-scale maps
│
└── 🔷 h3/                                          # H3 mosaic representations (for sensitivity-aware use)
    ├── smoky-hill-region-h3-r6.v1.geojson         # H3 mosaic @ res=6 (primary)
    └── smoky-hill-region-h3-r5.v1.geojson         # Optional coarser H3 mosaic @ res=5
~~~

**Directory contract:**

- **No raw or high-precision source data** (e.g., site coordinates, detailed terrace edges) may be stored here.  
- File naming must follow:  
  - `smoky-hill-region[-<variant>]-v<semver>.<ext>`  
  - Variants: `topology-simplified`, `mask`, `h3-r<res>`, etc.  
- All files must be **referenced** from:
  - STAC Items in `../../stac/items/`  
  - Region README `../README.md` (conceptual linkage)  
  - Provenance logs in `../../../../provenance/` and local `../provenance/`

---

## 🌐 GeoJSON Polygon Files

The `geojson/` directory contains the **polygon-based** representation(s) of the Smoky Hill cultural drainage region.

### Required File

- `smoky-hill-region.v1.geojson`  

**Requirements:**

- Format: **GeoJSON FeatureCollection** or single **Feature** with Polygon/MultiPolygon geometry.  
- CRS: **EPSG:4326** (WGS84 lon/lat).  
- Geometry must be:

  - Generalized (no site-level precision; no direct encoding of site clusters or sensitive locales).  
  - Topologically valid (no self-intersections, slivers, or invalid rings).  
  - Consistent with the spatial semantics defined in:
    - STAC (`../../stac/`)  
    - Region metadata (`../metadata/`)  
    - Provenance logs (`../provenance/` and `../../../../provenance/`)

- Recommended minimal properties:

  - `kfm:region_slug = "smoky-hill-region"`  
  - `kfm:region_kind = "drainage"` (and optionally `"eco-cultural"`)  
  - Optional convenience fields:
    - `kfm:version = "v1"`  
    - `kfm:culture_phase` (canonical in STAC/metadata, mirrored here only for convenience).

### Optional Variant

- `smoky-hill-region.v1-topology-simplified.geojson`  

  - A more aggressively simplified, **topology-safe** outline for **very small-scale** / overview maps.  
  - Must remain a **generalization of** the primary polygon (never more detailed).  
  - May drop minor bends or micro-features but must preserve the recognizable Smoky Hill corridor shape.  
  - If used in STAC Items, changes require updated provenance and metadata references.

Possible future addition (if needed):

- `smoky-hill-region.v1-mask.geojson`  

  - Rendering or analysis mask (e.g., valley interior shading).  
  - Must not introduce extra detail; only shape transformations at equivalent abstraction level.  
  - Any buffering or transformation must be documented in provenance.

All polygon generation/updates must be documented in provenance activities (e.g., `generalization`, `boundary_estimation`).

---

## 🔷 H3 Mosaic Files

The `h3/` directory contains **H3 mosaic** representations for sensitivity-aware and scale-aware renderings.

### Primary H3 Mosaic

- `smoky-hill-region-h3-r6.v1.geojson`  

**Requirements:**

- Geometry: H3 cells represented as GeoJSON Features (cell polygons or centroids).  
- Properties must include:

  - `kfm:region_slug = "smoky-hill-region"`  
  - `kfm:h3_resolution = 6`  
  - Optional:
    - `kfm:region_kind = "drainage"` (and/or `"eco-cultural"`)  
    - `kfm:version = "v1"`

- H3 cell set must:

  - Approximate the drainage-region polygon at the agreed resolution.  
  - Be used in Focus Mode and web clients where `"h3-only"` visibility is required.

### Optional Coarser Mosaic

- `smoky-hill-region-h3-r5.v1.geojson`  

  - Used for extremely generalized, large-scale visualizations.  
  - Same property conventions, `kfm:h3_resolution = 5`.

**Governance:**

- H3 mosaics are often **safer** for high-sensitivity corridors—where CARE requires `"h3-only"`, polygon overlays may not be used in certain UIs.  
- Any new H3 resolution must be added as a separate asset and recorded in provenance (e.g., in `kfm:steps` of the generalization activity).

---

## ⚖ CARE, Sovereignty & Sensitivity Constraints

All geometries in `data/` must respect CARE and sovereignty requirements for the Smoky Hill drainage corridor:

- **Forbidden** in this directory:

  - Geometries allowing reverse-engineering of precise site clusters or sensitive locales along the drainage.  
  - Encoded boundaries that are not approved for public representation.  
  - Nearly exact copies of internal confidential drainage or settlement maps.

- The **effective precision** (polygon edges, H3 resolution) must align with:

  - `care:sensitivity` and `care:visibility_rules` in:
    - Region metadata (`../metadata/`).  
    - STAC Collections/Items (`../../stac/`).  
    - Provenance logs (`../provenance/` and `../../../../provenance/`).

Examples:

- `"polygon-generalized"` → polygons may be shown at appropriate regional zoom levels.  
- `"h3-only"` → polygons may still exist here for internal use, but UIs must render only H3 mosaics in those modes.

Any change that tightens geometries around internal data (e.g., site clusters along the valley) is a **governance event** and may require **tribal/sovereign review**.

---

## 🧬 Provenance Linkage

Every file in this directory must be traceable via PROV-O:

- Canonical provenance logs for Smoky Hill live in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `smoky-hill-region-v1.json`).

Provenance must record:

- **Entities (`prov:Entity`)**:

  - `generalized` — drainage-region generalized polygons / H3 mosaics corresponding to these files.  
  - `processed` — final Smoky Hill region dataset v1 (linked to STAC & metadata).

- **Activities (`prov:Activity`)**:

  - `generalization` — polygon simplification, drainage envelope derivation, H3 generation.  
  - `boundary_estimation` — decisions about upstream/downstream extents and lateral valley boundaries.  
  - `review` — FAIR+CARE and (where applicable) tribal review.

- **Agents (`prov:Agent`)**:

  - `analyst` — dataset engineer / GIS specialist.  
  - `faircare` — FAIR+CARE Council.  
  - `tribal` — relevant sovereign reviewers (where engaged).

Paths/URIs to the data files should appear in:

- STAC Item assets (`assets.data.href`, `assets.h3.href`).  
- Provenance attributes (e.g., `kfm:output_path` or equivalent).

---

## 🧪 Validation & CI/CD

All files in this directory are subject to CI validation:

### Geometry & Schema Checks

- GeoJSON schema validation:
  - Proper Feature/FeatureCollection structure.  
  - Valid coordinate ranges and geometry types.

- Topology checks:
  - Valid polygons (no self-intersections, ring ordering OK).  

- H3 checks (for mosaics):
  - Valid H3 indices (if encoded).  
  - All features at declared `kfm:h3_resolution`.

### Linkage Validation

- Every data file must be referenced by at least one STAC Item under `../../stac/items/`.  
- Every STAC Item referencing this directory must pass STAC + metadata + provenance cross-checks.

### Governance & CARE Validation

- CARE fields in metadata and provenance must be compatible with the level of abstraction in these geometries.  
- CI must **block** merges if:

  - New or modified data files are not referenced in STAC and provenance.  
  - Geometry precision or extents conflict with CARE/provenance rules.  
  - Files appear to be raw or high-precision internal data rather than governed generalizations.

Indicative CI workflows:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

---

## 🧭 Authoring & Update Workflow

When updating geometries in this directory:

1. **Work from internal, non-public sources**  
   - Derive generalized outputs from internal hydrology, geomorphology, and archaeological data.  
   - Never treat these public GeoJSON/H3 files as authoritative raw data.

2. **Generate generalized geometries**  
   - Produce updated `.geojson` polygons and H3 mosaics.  
   - Capture all parameters (simplification tolerance, drainage envelopes, H3 resolution) for PROV-O (`kfm:steps`).

3. **Update STAC & Metadata**  
   - Adjust relevant STAC Items/Collections (`../../stac/`) and region metadata (`../metadata/`) if IDs, coverage, or assets change.

4. **Update Provenance**  
   - Append or bump PROV-O provenance log version(s) for `smoky-hill-region`.  
   - Ensure CARE fields and governance notes are current.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-smoky-hill-data`) to run geometry, STAC, and CARE checks.

6. **Submit PR & Address Feedback**  
   - CI enforces schema, linkage, and FAIR+CARE rules.  
   - Governance reviewers sign off on drainage-corridor and sovereignty implications.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed data layout, file naming, and CI/CARE/provenance requirements for Smoky Hill Cultural Drainage Region geometries; aligned with region README, STAC, metadata, and global provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Smoky Hill Cultural Drainage Region](../README.md) · [⬅ Back to Cultural Landscape Regions](../..//README.md)

</div>
