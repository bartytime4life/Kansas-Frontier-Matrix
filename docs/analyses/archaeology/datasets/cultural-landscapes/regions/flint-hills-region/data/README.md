---
title: "📂 KFM v11.2.3 — Flint Hills Eco-Cultural Region Data Layout (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/data/README.md"
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
intent: "cultural-landscape-region-flint-hills-data"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📂 **KFM — Flint Hills Eco-Cultural Landscape Region · Data Layout**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/data/README.md`

**Purpose:**  
Define and govern the **on-disk data layout** for the **Flint Hills Eco-Cultural Landscape Region**.  
This directory holds the **generalized public geometries** (polygons + H3 mosaics) and compatible derivatives used by:

- Flint Hills region STAC Collections & Items  
- Neo4j graph loaders and ETL pipelines  
- Story Nodes and Focus Mode v2/v3 overlays  
- MapLibre & Cesium eco-cultural regional visualizations  

All files here are **derived** from more detailed internal sources and must remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **graph-safe**.

</div>

---

## 📘 Overview

The **Flint Hills Eco-Cultural Landscape Region** uses this `data/` directory to store:

- **Generalized polygon geometries** (GeoJSON, EPSG:4326) describing the tallgrass / chert-rich eco-cultural band  
- **H3 mosaic representations** at governed resolution(s) for sensitivity-aware rendering  
- Optional **tiling or convenience products** if introduced later (e.g., pre-baked tilesets or masks)  

Key constraints:

- Only **generalized**, **non-site-precise** geometries are allowed here.  
- All geometries must match the **region semantics** defined in:  
  - `../README.md` (Flint Hills region spec)  
  - `../../metadata/` (region metadata registry)  
  - `../../provenance/` (global cultural landscape provenance logs)  
- Any change to these geometries must be captured in **PROV-O provenance** and must pass CI validation.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/flint-hills-region/data/
├── 📄 README.md                                    # This file (data layout & constraints)
│
├── 🌐 geojson/                                     # Generalized eco-cultural region polygons (EPSG:4326)
│   ├── flint-hills-region.v1.geojson              # Primary eco-cultural region boundary (generalized polygon)
│   ├── flint-hills-region.v1-simplified.geojson   # More aggressively simplified outline (for small-scale maps)
│   └── flint-hills-region.v1-mask.geojson         # Optional mask/clip geometry for rendering the eco-cultural band
│
└── 🔷 h3/                                          # H3 mosaic representations (for sensitivity-aware use)
    ├── flint-hills-region-h3-r6.v1.geojson        # H3 mosaic @ res=6 (primary)
    └── flint-hills-region-h3-r5.v1.geojson        # Optional coarser H3 mosaic @ res=5
~~~

**Directory contract:**

- **No raw or high-precision source data** (e.g., site coordinates, quarry outlines) may be stored here.  
- File naming must follow:  
  - `flint-hills-region[-<variant>]-v<semver>.<ext>`  
  - Variants: `simplified`, `mask`, `h3-r<res>`, etc.  
- All files must be **referenced** from:
  - STAC Items in `../../stac/items/`  
  - Region README `../README.md` (conceptual linkage)  
  - Provenance logs in `../../provenance/`  

---

## 🌐 GeoJSON Polygon Files

The `geojson/` directory contains the **polygon-based eco-cultural representation(s)** of the Flint Hills region.

### Required File

- `flint-hills-region.v1.geojson`  

**Requirements:**

- Format: **GeoJSON FeatureCollection** or single **Feature** with Polygon/MultiPolygon geometry.  
- CRS: **EPSG:4326** (WGS84 lon/lat).  
- Geometry must be:

  - Generalized (no site-level precision; no quarry/site outlines encoded).  
  - Topologically valid (no self-intersections, no slivers, no dangling artifacts).  
  - Consistent with the spatial and temporal semantics defined in:
    - STAC (`../../stac/`)  
    - Metadata (`../../metadata/`)  
    - Provenance logs (`../../provenance/`)

- Recommended minimal properties:

  - `kfm:region_slug = "flint-hills-region"`  
  - `kfm:region_kind = "eco-cultural"`  
  - Optional convenience fields:
    - `kfm:version = "v1"`  
    - `kfm:culture_phase` (canonical in STAC/metadata, mirrored here only if useful).

### Optional Variants

- `flint-hills-region.v1-simplified.geojson`  

  - More aggressively simplified for **very small-scale** map usage.  
  - Must remain a **generalization of** the primary polygon (no additional detail).  
  - If used in STAC Items, changes require updated provenance and metadata references.

- `flint-hills-region.v1-mask.geojson`  

  - Rendering or analysis mask (e.g., to shade or highlight the eco-cultural band).  
  - Must not encode additional sensitive detail; only shape transformations at equivalent abstraction level.

All polygon generation/updates must be documented in provenance activities (e.g., `generalization`, `boundary_estimation`).

---

## 🔷 H3 Mosaic Files

The `h3/` directory contains **H3 mosaic** representations used for sensitivity-aware and scale-aware renderings.

### Primary H3 Mosaic

- `flint-hills-region-h3-r6.v1.geojson`  

**Requirements:**

- Geometry: H3 cells represented as GeoJSON Features (cell polygons or centroids).  
- Properties must include:

  - `kfm:region_slug = "flint-hills-region"`  
  - `kfm:h3_resolution = 6`  
  - Optional:
    - `kfm:region_kind = "eco-cultural"`  
    - `kfm:version = "v1"`

- H3 cell set must:

  - Approximate the eco-cultural region polygon at the agreed resolution.  
  - Be the primary representation when CARE visibility policies call for `"h3-only"` displays.

### Optional Coarser Mosaic

- `flint-hills-region-h3-r5.v1.geojson`  

  - Used for extremely generalized, cross-state/region views.  
  - Same property conventions (`kfm:h3_resolution = 5`).

**Governance:**

- H3 mosaics are often **safer** for high-sensitivity eco-cultural contexts—where CARE sets `"h3-only"`, polygon overlays may be suppressed entirely in public UIs.  
- Any new H3 resolution must be added as a separate asset and recorded in provenance (e.g., `kfm:steps` in the generalization activity).

---

## ⚖ CARE, Sovereignty & Sensitivity Constraints

All geometries in `data/` must respect CARE and sovereignty requirements, especially around:

- Eco-cultural zones tied to lithic resources (chert)  
- Sensitive settlement pattern inferences  
- Traditional land-use and culturally important places

Constraints:

- No polygons or H3 mosaics may:

  - Encode or allow recovery of precise site locations, quarries, or sacred sites.  
  - Delineate confidential or disputed boundaries without explicit governance approval.  
  - Encode “near exact” boundaries that reveal internal confidential maps.

- The **effective precision** (polygon edges, H3 resolution) must align with:

  - `care:sensitivity` and `care:visibility_rules` in:
    - Region metadata (`../../metadata/`).  
    - STAC Collections/Items (`../../stac/`).  
    - Provenance logs (`../../provenance/`).

- Any change tightening geometries around internal data (site clusters, quarries, sensitive locales) is a **governance event** and may require **tribal/sovereign review**.

---

## 🧬 Provenance Linkage

Every file in this directory must be traceable via PROV-O:

- Canonical provenance logs for the Flint Hills region live in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `flint-hills-region-v1.json`).

Provenance must record:

- **Entities (`prov:Entity`)**:

  - `generalized` — source entity representing these generalized geometries.  
  - `processed` — final Flint Hills region dataset v1 (linked to STAC & metadata).

- **Activities (`prov:Activity`)**:

  - `generalization` — polygon simplification, clipping, buffers, H3 derivation.  
  - `boundary_estimation` — eco-cultural boundary decisions (tallgrass extent, lithic zones).  
  - `review` — FAIR+CARE and (where applicable) tribal review.

- **Agents (`prov:Agent`)**:

  - `analyst` — dataset engineer / GIS specialist.  
  - `faircare` — FAIR+CARE Council.  
  - `tribal` — relevant sovereign reviewers (where involved).

Paths/URIs to the data files should appear in:

- STAC Item assets (`assets.data.href`, `assets.h3.href`).  
- Provenance attributes (e.g., `kfm:output_path` or equivalent).

---

## 🧪 Validation & CI/CD

All files in this directory are subject to CI validation:

### Geometry Validation

- GeoJSON schema checks:
  - Valid GeoJSON types, coordinates, and required fields.  
- Topology checks:
  - Valid polygons (no self-intersections, holes consistent, etc.).  
- H3 validation (where applicable):
  - Resolution and index integrity (e.g., consistent `kfm:h3_resolution`).

### Linkage Validation

- Every data file must be referenced by at least one STAC Item under `../../stac/items/`.  
- Every STAC Item referencing `../data/` must pass STAC + metadata + provenance cross-checks.

### Governance Validation

- CARE audit workflows must ensure:

  - No data file violates `care:visibility_rules`.  
  - No regressions in `care:sensitivity` or `care:review` behavior.

Indicative CI workflows:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

CI must **block** merges if:

- New or modified data files are not referenced in STAC / provenance.  
- Geometry precision conflicts with CARE/provenance rules.  
- Files appear to be raw/high-precision source data instead of governed generalizations.

---

## 🧭 Authoring & Update Workflow

When updating geometries in this directory:

1. **Work from Internal Sources**  
   - Derive generalized outputs from internal, non-public datasets.  
   - Never treat `data/` as the editing source for authoritative raw data.

2. **Generate Generalized Geometries**  
   - Produce updated `.geojson` and H3 mosaics.  
   - Capture all parameters (simplification tolerance, buffers, H3 resolution, masks) for PROV-O.

3. **Update STAC & Metadata**  
   - Adjust relevant STAC Items/Collections (`../../stac/`) and region metadata (`../../metadata/`) if IDs, coverage, or assets change.

4. **Update Provenance**  
   - Append or bump PROV-O provenance log version(s) for `flint-hills-region`.  
   - Ensure CARE fields and governance notes are up to date.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-flint-hills-data`) to run geometry, linkage, and CARE checks.

6. **Submit PR & Address Feedback**  
   - CI enforces schema, linkage, and FAIR+CARE rules.  
   - Governance reviewers sign off on eco-cultural and sovereignty implications.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed data layout, file naming, and CI/CARE/provenance requirements for Flint Hills Eco-Cultural Region geometries; aligned with region README, STAC, metadata, and global provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Flint Hills Eco-Cultural Region](../README.md) · [⬅ Back to Cultural Landscape Regions](../..//README.md)

</div>