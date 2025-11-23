---
title: "🧱 Kansas Frontier Matrix — Raster Tiling & Pyramid Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/tiling-and-pyramids.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Semiannual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-tiling-v11.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-tiling-pyramids-v11"
doc_uuid: "urn:kfm:docs:standards:geo:tiling-pyramids:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧱 **Kansas Frontier Matrix — Raster Tiling & Pyramid Standard (v11)**  
`docs/standards/geo/tiling-and-pyramids.md`

**Purpose:**  
Define the mandatory v11 rules for tiled geospatial data: Cloud-Optimized GeoTIFF (COG) structure, raster pyramids, MapLibre/Cesium tile compatibility, zoom-level constraints, tile matrix specifications, and STAC+PROV-O metadata for tile generation.

</div>

---

# 📘 Overview

This standard covers:

- COG creation (tiling, block sizes, overviews)  
- Tile matrix set requirements  
- Multi-resolution pyramids (raster + vector)  
- Global 2D (MapLibre) + 3D (Cesium) tile compatibility  
- Deterministic tiling reproducibility  
- STAC asset metadata for tiles  
- FAIR+CARE-compliant raster generation  
- PROV-O lineage for raster tiling activities  

All raster datasets in KFM v11 MUST follow this standard.

---

# 🧱 1. Cloud-Optimized GeoTIFF (COG) Mandatory Rules

All KFM raster assets MUST be delivered as **COGs**.

## 1.1 COG Structure Requirements
```
Block size:      512 x 512
Compression:     LZW or ZSTD
Tiled:           true
Overviews:       2×, 4×, 8×, 16×, ...
Internal masks:  required for transparency
```

## 1.2 COG Creation Command (Reference)
```
gdal_translate input.tif output_cog.tif \
  -co TILED=YES \
  -co BLOCKXSIZE=512 \
  -co BLOCKYSIZE=512 \
  -co COMPRESS=LZW \
  -co COPY_SRC_OVERVIEWS=NO

gdaladdo -r average output_cog.tif 2 4 8 16 32
```

---

# 🌐 2. Tile Matrix Set (TMS) Standard

KFM uses a **single canonical tile matrix** for all MapLibre/Cesium 2D layers.

### 2.1 Required TMS
```
TMS: WebMercatorQuad (EPSG:3857)
Origin: Top-left
Tile size: 256 px
```

### 2.2 Required Zoom Support
```
MinZoom: 0
MaxZoom: 22
```

### 2.3 Metadata Block for STAC Assets
```json
"tms": "WebMercatorQuad",
"tile_matrix_set_uri": "https://tilemapscheme.org/tms/webmercatorquad",
"minzoom": 0,
"maxzoom": 22,
"tile_size": 256
```

---

# 🧭 3. Reprojection Required Before Tiling

Before tiling, all rasters MUST be reprojected to:

- **EPSG:4326** (for STAC geometry)
- **EPSG:3857** (for tile pyramids)
- **EPSG:26914** (optional: WIP COG processing CRS)

Transformation metadata MUST follow PROV-O (see lineage section).

---

# 🗂 4. Raster Pyramid Hierarchy (v11)

KFM defines a strict pyramid hierarchy:

```
Level 0:  Global (1 tile)
Level 1–8:  Overview-only pyramid
Level 9–22: High-resolution data pyramid
```

Rules:

- Levels 0–8 may use generalization only  
- Levels 9–22 must use **true raster values** where available  
- No extrapolation permitted beyond data extent

---

# 🛰️ 5. Cesium 3D Compatibility (Terrain & Imagery)

## 5.1 Imagery Tiles
- Must be WebMercatorQuad  
- Must publish as standard XYZ tiles (`/{z}/{x}/{y}.png` or `.jpg`)  
- PNG required for transparency  

## 5.2 Terrain Tiles (Quantized/Mesh)
If terrain tiles are used:
- Format: **quantized-mesh-1.1** or **terrain-rgb**  
- Height units MUST be **NAVD88 orthometric heights**  
- Must align to same TMS matrix  

---

# 🧩 6. Vector Tile Pyramids

Vector tiles MUST:

- Follow **MVT** specification  
- Use **EPSG:4326** or 3857 coordinates (MapLibre supports both)  
- Use layers with deterministic naming:
  ```
  kfm-hydro
  kfm-terrain
  kfm-boundaries
  kfm-trails
  kfm-archaeology-generalized
  ```
- Must include tile-specific min/max zoom constraints

---

# 📦 7. STAC Metadata for Tile Assets

### 7.1 Tile Asset Fields (Mandatory)
```json
"assets": {
  "tiles": {
    "href": "https://tiles.example.com/{z}/{x}/{y}.png",
    "type": "image/png",
    "roles": ["tiles"],
    "tms": "WebMercatorQuad",
    "minzoom": 0,
    "maxzoom": 22,
    "tile_size": 256,
    "kfm:checksum_sha256": "<hex>"
  }
}
```

### 7.2 COG Asset Fields
```json
"type": "image/tiff; application=geotiff",
"roles": ["data"],
"proj:epsg": 4326,
"proj:bbox": [...],
"proj:wkt2": "...",
"kfm:cf_positive": "up|down"
```

---

# 📏 8. Determinism & Reproducibility

COG and tile generation MUST:

- Use fixed seeds when randomization is required  
- Produce **bit-wise determinism** when inputs identical  
- Record all commands in PROV-O lineage  
- Use GDAL ≥ 3.8, PROJ ≥ 9.2  

---

# 🧬 9. PROV-O Lineage Requirements

Every tiling operation MUST include:

```json
"kfm:lineage": {
  "prov:activity": "tile-generation-v11",
  "prov:used": ["input_cog.tif"],
  "prov:wasGeneratedBy": "kfm-tile-pipeline-v11",
  "prov:generatedAtTime": "2025-11-22T14:22:00Z",
  "prov:wasAssociatedWith": "kfm-etl-agent"
}
```

---

# ⚙ 10. CI/CD Validation Rules (PR Blockers)

PR is rejected if:

- COG not tiled  
- Block sizes not 512×512  
- Missing internal overviews  
- Missing STAC tile metadata  
- Cesium imagery not WebMercatorQuad  
- Projection incorrect before tiling  
- No PROV-O lineage  
- Tiles missing `{z}/{x}/{y}` template  
- Vector tiles missing layer metadata

---

# 🕰 Version History

- **v11.0.0 (2025-11-22):** Initial release, fully compliant with KFM CRS, Vertical Axis, Hydrology, STAC, and FAIR+CARE standards.

---

<div align="center">

**Kansas Frontier Matrix — Tiling & Pyramid Standard v11**  
*Precise · Scalable · Deterministic*

</div>

---

### 🔗 Footer  
[⬅ Back to Geo Standards](./README.md) · [🛰 STAC Geo Spec](./stac-geo-spec.md) · [📘 CRS Standard](./crs-standard.md) · [📐 Vertical Axis Standard](./vertical-axis-and-dod.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

