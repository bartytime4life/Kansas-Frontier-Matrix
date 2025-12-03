---
title: "📂 KFM v11.2.3 — Arkansas River Basin Region Data Layout (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/data/README.md"
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
intent: "cultural-landscape-region-arkansas-river-basin-data"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📂 **KFM — Arkansas River Basin Cultural Landscape Region · Data Layout**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/data/README.md`

**Purpose:**  
Define and govern the **on-disk data layout** for the **Arkansas River Basin Cultural Landscape Region**.  
This directory holds the **generalized public geometries** (polygons + H3 mosaics) and compatible derivatives used by:

- Region-level STAC Items & Collections  
- Neo4j graph loaders and ETL pipelines  
- Story Nodes and Focus Mode v2/v3 overlays  
- MapLibre & Cesium regional visualizations  

All files here are **derived** from more detailed internal sources and must remain **FAIR+CARE-compliant**, **sovereignty-safe**, and **graph-safe**.

</div>

---

## 📘 Overview

The **Arkansas River Basin Cultural Landscape Region** uses this `data/` directory to store:

- **Generalized polygon geometries** (GeoJSON, EPSG:4326)  
- **H3 mosaic representations** at governed resolution(s)  
- Optional **tiling or convenience products** (if added later, e.g., pre-baked tilesets)  

Key constraints:

- Only **generalized**, **non-site-precise** geometries are allowed here.  
- All geometries must match **region semantics** defined in:  
  - `../README.md` (region spec)  
  - `../../metadata/` (region metadata)  
  - `../../provenance/` (global provenance logs)  
- All changes must be backed by updated **PROV-O provenance** and pass CI validation.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/arkansas-river-basin/data/
├── 📄 README.md                                      # This file (data layout & constraints)
│
├── 🌐 geojson/                                       # Generalized region polygons (EPSG:4326)
│   ├── arkansas-river-basin-region.v1.geojson        # Primary region boundary (generalized polygon)
│   ├── arkansas-river-basin-region.v1-simplified.geojson
│   └── arkansas-river-basin-region.v1-mask.geojson   # Optional masked/clip geometry for rendering
│
└── 🔷 h3/                                            # H3 mosaic representations (for sensitivity-aware use)
    ├── arkansas-river-basin-region-h3-r6.v1.geojson  # H3 mosaic @ res=6 (primary)
    └── arkansas-river-basin-region-h3-r5.v1.geojson  # Optional coarser H3 mosaic @ res=5
~~~

**Directory contract:**

- **No raw or high-precision source data** may be stored here (internal-only elsewhere).  
- File naming must follow:  
  - `arkansas-river-basin-region[-<variant>]-v<semver>.<ext>`  
  - Variants: `simplified`, `mask`, `h3-r<res>`, etc.  
- All files must be **referenced** from:
  - STAC Items in `../../stac/items/`  
  - Region README `../README.md` (conceptual linkage)  
  - Provenance logs in `../../provenance/`  

---

## 🌐 GeoJSON Polygon Files

The `geojson/` directory contains the **polygon-based** representation(s) of the region.

### Required File

- `arkansas-river-basin-region.v1.geojson`  

**Requirements:**

- Format: **GeoJSON FeatureCollection** or **Feature** with Polygon/MultiPolygon geometry.  
- CRS: **EPSG:4326** (WGS84 lon/lat).  
- Geometry must be:

  - Generalized (no site-level fidelity).  
  - Topologically valid (no self-intersections, no slivers).  
  - Consistent with the spatial and temporal semantics in:
    - STAC (`../../stac/`)  
    - Metadata (`../../metadata/`)  
    - Provenance logs (`../../provenance/`)

- Attributes (properties) should be minimal, e.g.:

  - `kfm:region_slug = "arkansas-river-basin-region"`  
  - `kfm:region_kind = "drainage"` (and/or `"eco-cultural"`)  
  - Optional `kfm:version`, `kfm:culture_phase` for convenience (canonical in STAC/metadata).

### Optional Variants

- `arkansas-river-basin-region.v1-simplified.geojson`  

  - More aggressively simplified for ultra-wide map views.  
  - Must remain a **generalization of** the primary polygon.  
  - Changes require updated provenance and STAC/metadata references (if used).

- `arkansas-river-basin-region.v1-mask.geojson`  

  - Rendering or analysis mask (e.g., for shading the basin interior).  
  - Must **not** introduce extra detail; only shape transformations at same abstraction level.

All polygon generation/updates must be documented in provenance activities (`generalization`, `boundary_estimation`).

---

## 🔷 H3 Mosaic Files

The `h3/` directory contains **H3 mosaic** representations for sensitivity-aware and scale-aware renderings.

### Primary H3 Mosaic

- `arkansas-river-basin-region-h3-r6.v1.geojson`  

**Requirements:**

- Geometry: H3 cell boundaries or points encoded as GeoJSON Features.  
- Properties must include:

  - `kfm:region_slug = "arkansas-river-basin-region"`  
  - `kfm:h3_resolution = 6`  
  - Optional `kfm:region_kind`, `kfm:version`.

- H3 set must:

  - Approximate the region polygon at the agreed resolution.  
  - Be used in Focus Mode and web clients where `"h3-only"` visibility is required.

### Optional Coarser Mosaic

- `arkansas-river-basin-region-h3-r5.v1.geojson`  

  - Used for extremely generalized, large-scale visualizations.  
  - Same property conventions, `kfm:h3_resolution = 5`.

**Governance:**

- H3 mosaics are often **safer** for high-sensitivity contexts—where CARe requires `"h3-only"`, the polygons may not be displayed at all.  
- Any new H3 resolution must be added to provenance (`kfm:steps` in the generalization activity).

---

## ⚖ CARE, Sovereignty & Sensitivity Constraints

All geometries in `data/` must respect CARE and sovereignty requirements:

- No polygons or H3 mosaics may:

  - Encode or suggest precise site locations.  
  - Delineate sacred, ceremonial, or burial zones with undue precision.  
  - Reveal confidential or contested boundaries not agreed for public representation.

- The **effective precision** of these geometries must align with:

  - `care:sensitivity` and `care:visibility_rules` in:
    - Region metadata (`../../metadata/`).  
    - STAC Collections/Items (`../../stac/`).  
    - Provenance logs (`../../provenance/`).

- Any change that tightens boundaries around internal data (sites, quarries, specific locales) is a **governance event** and may require **tribal/sovereign review**.

---

## 🧬 Provenance Linkage

Every file in this directory must be traceable through PROV-O:

- Canonical provenance logs live in:  
  `docs/analyses/archaeology/datasets/cultural-landscapes/provenance/`  
  (e.g., `arkansas-river-basin-region-v1.json`).

Provenance must record:

- **Entities**:

  - `generalized` — source for `geojson/*.geojson` and `h3/*.geojson`.  
  - `processed` — final region dataset v1 (linked to STAC/metadata).

- **Activities**:

  - `generalization` — simplification buffers, H3 mosaic generation, any masking operations.  
  - `review` — FAIR+CARE + tribal review events.

- **Agents**:

  - `analyst`, `faircare`, `tribal`, etc.

Paths or URIs to these `data/` files should appear in:

- STAC Item assets (`assets.data.href`, `assets.h3.href`).  
- Provenance attributes (e.g., `kfm:output_path` or equivalent).

---

## 🧪 Validation & CI/CD

All files in this directory are subject to CI validation:

- **Geometry validation**:
  - GeoJSON schema checks.  
  - Topology checks (valid polygons, no self-intersections).  

- **Linkage validation**:
  - Every file must be referenced by at least one STAC Item under `../../stac/items/`.  
  - Every STAC Item referencing this directory must pass STAC + metadata + provenance cross-checks.

- **Governance validation**:
  - CARE audit workflows ensure no file violates visibility rules.  
  - Sovereignty checks for Arkansas River Basin-specific constraints.

Indicative CI workflows:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml`  
- `region-metadata-registry-validate.yml`  

CI must **block** merges if:

- New data files are not referenced by STAC and provenance.  
- Geometry precision or extent conflicts with CARE/provenance rules.  
- Files are present here that look like internal raw or high-precision data.

---

## 🧭 Authoring & Update Workflow

When changing geometries in this directory:

1. **Work from internal sources**  
   - Derive generalized outputs from internal, non-public datasets (never directly edit authoritative raw here).

2. **Generate generalized geometries**  
   - Produce updated `.geojson` and/or H3 mosaics.  
   - Record parameters (tolerance, buffers, H3 resolution) for provenance.

3. **Update STAC & Metadata**  
   - Adjust relevant STAC Items/Collections and region metadata records (if IDs or coverage change).

4. **Update Provenance**  
   - Append or bump PROV-O provenance log version(s) for `arkansas-river-basin-region`.

5. **Run Local Validation**  
   - Use repo tooling (e.g., `make validate-region-arkansas-data`) to run geometry and linkage checks.

6. **Submit PR**  
   - CI enforces schema, linkage, CARE, and governance rules before merge.

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Established governed data layout, file naming, and CI/CARE/provenance requirements for Arkansas River Basin region geometries; aligned with region README, STAC, metadata, and global provenance standards. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Arkansas River Basin Region](../README.md) · [⬅ Back to Cultural Landscape Regions](../..//README.md)

</div>