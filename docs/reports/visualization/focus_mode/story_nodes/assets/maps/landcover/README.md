---
title: "🌿 Kansas Frontier Matrix — Landcover Basemap Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/landcover/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-focusmode-landcover-basemaps-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Landcover Basemap Assets Index**  
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/landcover/README.md`

**Purpose:**  
Define and index all **landcover basemap assets** used in Focus Mode Story Nodes, including vegetation, canopy cover, land-use change, ecological zones, and soil/permeability surfaces.  
All assets follow **FAIR+CARE**, **STAC 1.0**, **ISO 19115**, and **DCAT 3.0** metadata conventions.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Landcover basemaps support ecological and historical storytelling, including:
- Vegetation distribution across eras  
- NDVI and seasonal greenness composites  
- Fire history and burn scar mapping  
- Land-use transitions (e.g., prairie → agriculture)  
- Soil/terrain permeability for hydrology–landcover integration  
- Carbon storage and biomass estimates  
- Ecological zones relevant to archaeology and settlement analysis  

These basemaps serve as **foundational overlays** for Focus Mode environmental context, 3D scenes, and Story Nodes.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/maps/landcover/
├── README.md
├── landcover_classification_nlcd_2021.tif
├── ndvi_composite_2025_summer.png
├── canopy_cover_trend_2000_2025.svg
├── landuse_change_2001_2021.geojson
├── soil_permeability_surface.tif
└── stac.json
```

---

## 🧩 Required Metadata Fields (Landcover Basemaps)

| Field | Description |
|-------|-------------|
| `id` | Landcover asset identifier |
| `type` | `"landcover_basemap"` |
| `checksum_sha256` | SHA-256 integrity verification |
| `projection` | Typically `EPSG:4326` |
| `landcover_domain` | `"vegetation"`, `"ndvi"`, `"canopy"`, `"soil"`, `"landuse_change"` |
| `temporal_extent` | Time period represented |
| `care.status` | Public / generalized / restricted |
| `generalization.method` | Smoothing or generalization applied |
| `provenance` | NLCD, MODIS, VIIRS, ESA CCI, USGS | 
| `updated` | ISO timestamp |
| `stac_extensions` | `proj`, `raster`, `version`, `checksum` |

---

## 🌱 Example Metadata Record (Landcover Classification)

```json
{
  "id": "kfm_landcover_nlcd_2021_v10",
  "type": "landcover_basemap",
  "path": "landcover_classification_nlcd_2021.tif",
  "checksum_sha256": "sha256-12ff7c09ef2d455d901e0ab2c53d9b944f01b5d1aa7c77dfb87c1a55c229abcd",
  "projection": "EPSG:4326",
  "landcover_domain": "vegetation",
  "temporal_extent": "2021",
  "care": {
    "status": "public",
    "reason": "Landcover surfaces derived from publicly licensed NLCD sources.",
    "authority": "FAIR+CARE Land Systems Review Board"
  },
  "generalization": {
    "method": "categorical smoothing",
    "window": "3x3 majority filter"
  },
  "provenance": {
    "datasets": ["USGS NLCD", "Copernicus Global Land Service"],
    "agreements": []
  },
  "updated": "2025-11-12T17:21:00Z",
  "stac_extensions": ["proj", "raster", "checksum", "version"]
}
```

---

## 🌳 Supported Landcover Product Types

| Category | Description | Format |
|----------|-------------|--------|
| **NLCD / CLC Classification** | Landcover types (forest, agriculture, prairie, wetlands) | GeoTIFF |
| **NDVI Composites** | Seasonal greenness indices for ecological timing | PNG, TIFF |
| **Canopy Cover Trends** | Long-term canopy change metrics | SVG, PNG |
| **Land-Use Change Matrix** | Crosswalk of major transitions | GeoJSON |
| **Soil / Permeability Surfaces** | Soil type & infiltration capacity | TIFF |
| **Biomass / Carbon Density Surfaces** | Ecological carbon storage estimates | TIFF |

---

## 🌍 FAIR+CARE Alignment (Landcover)

| Principle | Implementation |
|----------|----------------|
| **Collective Benefit** | Landcover data supports ecological restoration and public education |
| **Authority to Control** | No culturally sensitive locations included; no high-risk archaeological sites |
| **Responsibility** | NDVI and vegetation maps generalized to avoid precise backyard vegetation in rural parcels |
| **Ethics** | All maps reviewed by FAIR+CARE Ecological & Cultural Board |

---

## 🧭 STAC Collection Requirements

Each folder must include a `stac.json` containing:
- STAC 1.0.0 metadata  
- `proj`, `raster`, `checksum`, `version` extensions  
- Climate–landcover cross references  
- `"kfm:landcover_domain"`  
- `"kfm:care_tag"`  
- `"kfm:generalization_method"`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Ecological Visualization Board | Initial landcover basemap index; includes NLCD, NDVI, canopy, soil layers with FAIR+CARE alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Map Assets](../README.md)

</div>

