---
title: "🧩 Kansas Frontier Matrix — Map Asset Metadata Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/field_definitions.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
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

# 🧩 **Kansas Frontier Matrix — Map Asset Metadata Field Definitions**
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/field_definitions.md`

**Purpose:**  
Provide **authoritative definitions** for every metadata field associated with Focus Mode map assets, ensuring interoperability across **STAC 1.0**, **DCAT 3.0**, **CIDOC CRM**, **GeoJSON**, and **FAIR+CARE** governance.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

These field definitions support:
- Story Node map asset metadata
- Focus Mode dynamic overlays
- 2D/3D map layers (basemaps, hydrology, climate, archaeology, landcover, treaties)
- Temporal layers and elevation surfaces
- STAC/DCAT interoperability
- FAIR+CARE ethical governance of sensitive spatial information

All fields must be validated via:
- `stac-validate.yml`
- `faircare-validate.yml`
- `docs-lint.yml`
- `telemetry-export.yml`

---

## 🧱 Field Definitions (KFM v10.2)

### **Core Identification Fields**

| Field | Type | Description | Required | Example |
|-------|------|-------------|----------|---------|
| `id` | string | Globally unique identifier for the map asset | ✅ | `"kfm_climate_precip_1980_2020_v10"` |
| `title` | string | Human-readable name | ✅ | `"Kansas Annual Precipitation (1980–2020)"` |
| `description` | string | Summary of the dataset, visualization, or map product | ✅ | `"Derived from NOAA NCEI and CPC sources"` |
| `domain` | string (enum) | `archaeology`, `hydrology`, `climate`, `landcover`, `treaties`, `hazards`, etc. | ✅ | `"hydrology"` |

---

### **Spatial Metadata Fields**

| Field | Type | Description | Required | Example |
|-------|------|-------------|----------|---------|
| `projection` | string | EPSG code or CRS (e.g., EPSG:4326) | ✅ | `"EPSG:4326"` |
| `spatial_extent` | array[number] | BBox `[W, S, E, N]` | ⚙️ | `[-102.05, 37.0, -94.6, 40.0]` |
| `geo:geometry` | object | Optional GeoJSON geometry | — | `{ "type":"Polygon", ... }` |

---

### **Temporal Metadata Fields**

| Field | Type | Description | Required | Example |
|-------|------|-------------|----------|---------|
| `temporal_extent.start` | string (ISO 8601) | Beginning of dataset or map layer | ⚙️ | `"1950-01-01"` |
| `temporal_extent.end` | string (ISO 8601) | End of dataset or map layer | ⚙️ | `"2020-12-31"` |
| `period` | string | Named period or era, if no precise dates | — | `"Late Holocene"` |

---

### **File & Asset Metadata**

| Field | Type | Description | Required | Example |
|-------|------|-------------|----------|---------|
| `format` | string | File type (`GeoTIFF`, `PNG`, `SVG`, `PMTiles`, `CZML`, `GLB`) | ⚙️ | `"GeoTIFF"` |
| `checksum_sha256` | string | SHA-256 hash for integrity | ✅ | `"sha256-8baf7c..."` |
| `stac_extensions` | array[string] | STAC extensions used | ⚙️ | `["proj", "raster", "checksum", "version"]` |
| `asset_role` | string | `data`, `visualization`, `thumbnail`, `legend` | — | `"data"` |

---

### **Provenance & Lineage Fields**

| Field | Type | Description | Required | Example |
|-------|------|-------------|----------|---------|
| `provenance.upstream` | array[string] | Source datasets | ⚙️ | `["NOAA NCEI", "USGS NLCD"]` |
| `provenance.processing` | string | Summary of transformations applied | — | `"GDAL warp + reprojection to EPSG:3857"` |
| `provenance.commit_sha` | string | Git commit of producing workflow | ⚙️ | `"<commit-hash>"` |
| `provenance.workflow` | string | Name of pipeline used | — | `"hydrology_flood_pipeline_v3"` |

---

### **FAIR+CARE Governance Fields**

| Field | Type | Description | Required | Example |
|-------|------|-------------|----------|---------|
| `care.status` | enum | `public`, `generalized`, `restricted` | ⚙️ | `"generalized"` |
| `care.statement` | string | Justification & ethical handling guidance | — | `"Spatial precision reduced to protect cultural sites"` |
| `care.reviewer` | string | FAIR+CARE Council / Tribal Authority | ⚙️ | `"Prairie Band Potawatomi Nation"` |
| `care.date_reviewed` | string (ISO 8601) | Review date | — | `"2025-11-12"` |

---

### **Interoperability Fields (STAC/DCAT/CIDOC)**

| Field | Maps To | Notes |
|-------|---------|--------|
| `dcat:theme` | DCAT thematic category | Required for catalogs |
| `dct:spatial` | DCAT spatial field | Must map from `spatial_extent` |
| `dct:temporal` | DCAT temporal coverage | Use `temporal_extent` |
| `crm:E53_Place` | CIDOC location class | Used for archaeology & heritage | 
| `crm:E52_Time-Span` | CIDOC temporal class | Required for historical periods |

---

## 🧾 Example — Full Metadata Block

```json
{
  "id": "kfm_archaeology_generalized_sites_v10",
  "title": "Generalized Archaeological Site Density",
  "description": "1 km aggregated density raster of sensitive archaeological sites.",
  "domain": "archaeology",
  "projection": "EPSG:4326",
  "spatial_extent": [-102.05, 37.0, -94.6, 40.0],
  "temporal_extent": { "start": "1850-01-01", "end": "1900-01-01" },
  "format": "GeoTIFF",
  "checksum_sha256": "sha256-7fa912...",
  "provenance": {
    "upstream": ["Kansas Historical Society", "USGS"],
    "processing": "Generalization to 1 km grid; spatial masking applied",
    "commit_sha": "<commit-hash>",
    "workflow": "archaeology_generalization_v4"
  },
  "care": {
    "status": "generalized",
    "statement": "Coordinates reduced to protect Indigenous cultural sites",
    "reviewer": "FAIR+CARE Council",
    "date_reviewed": "2025-11-12"
  },
  "stac_extensions": ["proj", "raster", "checksum", "version"],
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Board | Introduced complete field definitions for map asset metadata; fully aligned with STAC/DCAT/CARE/KFM v10.2. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Map Asset Metadata](README.md)

</div>

