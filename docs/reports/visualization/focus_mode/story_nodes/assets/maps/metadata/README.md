---
title: "🧩 Kansas Frontier Matrix — Map Asset Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-focusmode-mapassets-metadata-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Map Asset Metadata Specification**  
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/README.md`

**Purpose:**  
Define the **metadata schema**, **FAIR+CARE governance fields**, and **STAC/DCAT interoperability rules** for all map assets used in Focus Mode Story Nodes (basemaps, overlays, temporal layers, 3D tiles, and contextual environmental surfaces).

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This specification standardizes metadata for all Focus Mode map assets, ensuring:
- **Interoperability** across STAC 1.0, DCAT 3.0, CIDOC CRM, GeoJSON, and OWL-Time  
- **Ethical governance** of culturally sensitive or restricted data (CARE Principles)  
- **Reproducibility** via checksums, provenance, and versioned workflows  
- **Accessibility** with clear licensing, lineage, and FAIR metadata blocks  

Assets covered include:
- Basemaps (terrain, hydrology, landcover, climate, archaeological)
- Overlays (events, hazards, correlations, ecological zones)
- 3D Views (Cesium scenes, elevation meshes, prairie reconstructions)
- Story Node contextual layers (treaty polygons, timelines, settlement footprints)

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/
├── README.md
├── field_definitions.md
├── examples/
│   ├── stac_item_example.json
│   ├── dcat_distribution_example.json
│   └── care_metadata_example.json
└── schemas/
    ├── mapasset-schema-v10.json
    └── care-extension-v3.json
```

---

## 🧱 Required Metadata Fields (KFM v10)

| Field | Description | Required |
|-------|-------------|----------|
| `id` | Unique identifier for the map asset | ✅ |
| `type` | `basemap` · `overlay` · `3d_scene` · `temporal_layer` | ✅ |
| `title` | Human-readable name | ✅ |
| `description` | Summary of what the asset represents | ✅ |
| `domain` | `archaeology` · `climate` · `hydrology` · `landcover` · `treaties` · etc. | ✅ |
| `projection` | CRS (EPSG code) | ✅ |
| `temporal_extent` | Start/end times or eras | ⚙️ |
| `spatial_extent` | Bounding box `[W,S,E,N]` | ⚙️ |
| `checksum_sha256` | Integrity verification | ✅ |
| `format` | GeoTIFF, COG, PNG, SVG, PMTiles, CZML, GLB | ⚙️ |
| `license` | SPDX/CC identifier | ✅ |
| `provenance` | Upstream datasets + processing lineage | ✅ |
| `care` | Cultural/ethical review block | ⚙️ |
| `stac_extensions` | proj, raster, version, checksum, etc. | ⚙️ |
| `updated` | Timestamp | ✅ |

---

## 🧠 CARE Metadata Requirements

CARE governs sensitive archaeological, Indigenous, or ecological content.  
Every map asset must include:

```json
"care": {
  "status": "public | generalized | restricted",
  "statement": "Explanation of restrictions or ethical review",
  "reviewer": "FAIR+CARE Council or Tribal Authority",
  "date_reviewed": "2025-11-12",
  "notes": "Generalized to 5 km to protect sensitive cultural landscape."
}
```

### CARE Status Definitions

| CARE Status | Meaning | Enforcement |
|-------------|----------|-------------|
| **Public** | No ethical restrictions | Published openly |
| **Generalized** | Spatial/temporal precision reduced | Must follow generalization rules |
| **Restricted** | Sensitive content requires approval | Requires MOU + Council sign-off |

---

## 🧬 Example STAC Item (Map Asset)

```json
{
  "id": "kfm_hydro_floodextent_1993_v10",
  "type": "Feature",
  "stac_version": "1.0.0",
  "properties": {
    "title": "1993 Flood Extent — Kansas",
    "description": "Spatial flood footprint derived from USGS & NOAA datasets.",
    "kfm:domain": "hydrology",
    "kfm:care_status": "public",
    "kfm:generalization": "none",
    "datetime": "1993-07-20T00:00:00Z"
  },
  "bbox": [-102.05, 37.0, -94.6, 40.0],
  "assets": {
    "map": {
      "href": "../hydrology/flood/flood_1993_extent.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  },
  "stac_extensions": ["proj", "raster", "checksum", "version"]
}
```

---

## 📚 Provenance & Lineage Requirements (KFM v10)

Each metadata entry must include:

- **Upstream datasets** (NOAA, USGS, NLCD, DASC, ESA, etc.)  
- **Processing tools** (GDAL, PyTorch, PDAL, Rasterio)  
- **Workflow commit SHA**  
- **STAC/DCAT linkages**  
- **Checksum validation** entries in governance ledger  
- **Generalization method** if applicable (buffering, rounding, aggregation)  

---

## 🧭 Cross-Standard Mapping Table

| KFM Field | STAC Field | DCAT Field | CIDOC CRM | Notes |
|-----------|-------------|-------------|------------|-------|
| `id` | `id` | `dct:identifier` | `E42 Identifier` | — |
| `title` | `properties.title` | `dct:title` | `E35 Title` | — |
| `domain` | `kfm:domain` | `dcat:theme` | — | — |
| `temporal_extent` | `properties.datetime` | `dct:temporal` | `E52 Time-Span` | Supports ranges |
| `spatial_extent` | `bbox` | `dct:spatial` | `E53 Place` | — |
| `care.status` | `kfm:care_status` | `kfm:care_status` | — | Required for sensitive layers |
| `checksum_sha256` | `checksum:multihash` | — | — | SHA-256 only |

---

## 🧩 Generalization Policy Summary

| Technique | Applies To | Requirement |
|-----------|-------------|------------|
| Coordinate rounding | Archaeology / Sensitive ecology | ≥ 2 decimals removed |
| Spatial buffering | Sacred sites / burial grounds | ≥ 5 km |
| Temporal smoothing | Historic events | Replace exact dates with eras |
| Data suppression | Extreme sensitivity | Remove geometry, provide abstract centroid |

---

## 🧮 Validation Workflows

| Workflow | Validates |
|----------|-----------|
| `stac-validate.yml` | STAC schema, links, assets |
| `faircare-validate.yml` | CARE status, ethical governance |
| `docs-lint.yml` | Documentation compliance |
| `telemetry-export.yml` | Sustainability + governance metrics |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | KFM FAIR+CARE Visualization Board | Initial metadata specification for Focus Mode map assets; includes STAC/DCAT/CARE alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Map Assets](../README.md)

</div>

