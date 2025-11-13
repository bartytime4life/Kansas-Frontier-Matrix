---
title: "🗂️ Kansas Frontier Matrix — Map Asset Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/examples/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reports-visualization-focusmode-mapassets-metadata-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Map Asset Metadata Examples**
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/metadata/examples/README.md`

**Purpose:**  
Provide **fully compliant metadata examples** for Focus Mode map assets, aligning with **STAC 1.0**, **DCAT 3.0**, **CIDOC CRM**, **ISO 19115**, and the KFM **FAIR+CARE Data Governance Framework**.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **canonical examples** of metadata blocks used by:
- Story Node map layers  
- Focus Mode overlays  
- Basemaps, elevation models, archaeological generalizations  
- Hydrology, climate, landcover, hazards, and treaty layers  
- 2D/3D map assets (GeoTIFF, PMTiles, CZML, GLB)

Each example illustrates:
- Required fields (ID, title, checksum, provenance)
- STAC/DCAT interoperability
- FAIR+CARE ethical metadata (CARE blocks)
- Dataset lineage & commit references
- Temporal & spatial precision rules
- Compatibility with KFM v10.2 visualization engine

---

## 🧩 Example 1 — Hydrology: Flood Extent Raster (GeoTIFF)

```json
{
  "id": "kfm_flood_extent_1993_upper_kansas_v10",
  "title": "Historic Flood Extent — Kansas River Basin (1993)",
  "description": "GeoTIFF flood extent raster derived from USGS and FEMA NFHL datasets.",
  "domain": "hydrology",
  "projection": "EPSG:4326",
  "spatial_extent": [-98.5, 38.5, -94.5, 40.5],
  "temporal_extent": { "start": "1993-07-01", "end": "1993-07-31" },
  "format": "GeoTIFF",
  "checksum_sha256": "sha256-3af92b41f0e1bb6d9dd...",
  "provenance": {
    "upstream": ["USGS NWIS", "FEMA NFHL"],
    "processing": "Water classification via thresholding + DEM correction",
    "workflow": "hydrology_flood_pipeline_v3",
    "commit_sha": "<commit-hash>"
  },
  "care": {
    "status": "public",
    "statement": "No sensitive cultural sites involved.",
    "reviewer": "FAIR+CARE Hydrology Board",
    "date_reviewed": "2025-11-12"
  },
  "stac_extensions": ["proj", "raster", "checksum", "version"],
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🧩 Example 2 — Archaeology: Generalized Site Density (1 km grid)

```json
{
  "id": "kfm_archaeology_density_generalized_km1_v10",
  "title": "Generalized Archaeological Site Density (1 km)",
  "description": "Generalized raster representing archaeological site density across NE Kansas.",
  "domain": "archaeology",
  "projection": "EPSG:4326",
  "spatial_extent": [-102.05, 37.0, -94.6, 40.0],
  "format": "GeoTIFF",
  "checksum_sha256": "sha256-81df22c710f1cdaa992...",
  "provenance": {
    "upstream": ["Kansas Historical Society"],
    "processing": "Aggregated to 1x1 km grid; sensitive coordinates masked",
    "workflow": "archaeology_generalization_v4",
    "commit_sha": "<commit-hash>"
  },
  "care": {
    "status": "generalized",
    "statement": "Spatial precision reduced to protect sensitive cultural heritage locations.",
    "reviewer": "Prairie Band Potawatomi Nation",
    "date_reviewed": "2025-11-11"
  },
  "stac_extensions": ["proj", "raster", "checksum", "version"],
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🧩 Example 3 — Climate: Annual Precipitation PMTiles Layer

```json
{
  "id": "kfm_climate_precip_tiles_1980_2020_v10",
  "title": "Kansas Annual Precipitation (1980–2020) — PMTiles",
  "description": "Vector-tiles representation of precipitation anomalies for Focus Mode visual analytics.",
  "domain": "climate",
  "format": "PMTiles",
  "projection": "EPSG:3857",
  "spatial_extent": [-11354500, 4450000, -10540000, 5020000],
  "temporal_extent": { "start": "1980-01-01", "end": "2020-12-31" },
  "checksum_sha256": "sha256-aa44fdc3e12fe89ab31...",
  "provenance": {
    "upstream": ["NOAA NCEI", "CPC"],
    "processing": "Zonal aggregation + tile generation",
    "workflow": "climate_precip_pipeline_v5",
    "commit_sha": "<commit-hash>"
  },
  "care": {
    "status": "public",
    "statement": "Dataset contains no cultural sensitivity risks.",
    "reviewer": "FAIR+CARE Climate Council",
    "date_reviewed": "2025-11-11"
  },
  "stac_extensions": ["vector", "checksum", "version"],
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🧩 Example 4 — 3D Scene Layer (GLB) for Focus Mode

```json
{
  "id": "kfm_3d_prairie_reconstruction_1850_v10",
  "title": "3D Prairie Landscape Reconstruction (circa 1850)",
  "description": "GLB model representing a historically accurate prairie environment for Focus Mode 3D contextual storytelling.",
  "domain": "landcover",
  "format": "GLB",
  "checksum_sha256": "sha256-7b0cda9319a12fee8d3...",
  "provenance": {
    "upstream": ["USGS DEM", "NLCD 1850 Reconstruction"],
    "processing": "LOD decimation + PBR texturing",
    "workflow": "3d_prairie_pipeline_v2",
    "commit_sha": "<commit-hash>"
  },
  "care": {
    "status": "public",
    "statement": "No sensitive ecological or cultural zones depicted.",
    "reviewer": "FAIR+CARE Land Systems Council",
    "date_reviewed": "2025-11-12"
  },
  "updated": "2025-11-12T18:00:00Z"
}
```

---

## 🧭 How to Use These Examples

- Use as templates for new Story Node map layers  
- Validate against STAC/DCAT schemas before committing  
- Include in pipeline-generated validation previews  
- Ensure all examples conform to **markdown_rules.md** and **data-contracts.md**

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Board | Added complete cross-domain metadata examples for map assets under STAC/DCAT/CARE alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Map Asset Metadata](../README.md)

</div>

