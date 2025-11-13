---
title: "🗺️ Kansas Frontier Matrix — Story Node Map Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reports-visualization-focusmode-storynode-assets-maps-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Story Node Map Assets Index**
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/README.md`

**Purpose:**  
Provide an authoritative, FAIR+CARE-aligned registry for **static maps, geospatial renderings, overlays, grid-aggregated surfaces, and derived thematic layers** used by Focus Mode Story Nodes.  
Ensures **traceability, dataset lineage, reproducibility, and sensitivity masking** for all map-based assets.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **2D map assets** referenced by Story Nodes, including:

- Basemaps  
- Archaeological overlays  
- Hydrological layers (flood extents, paleo-channels, recharge zones)  
- Climate anomaly surfaces  
- Landcover/NDVI transitions  
- Historical cartography reconstructions  
- Generalized / CARE-restricted spatial products

Every file stored here must also appear in the **Story Node Asset Index** at:

```
docs/reports/visualization/focus_mode/story_nodes/assets/metadata/assets_index.json
```

with complete provenance and CARE classification.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/maps/
├── README.md                      # This file
│
├── basemaps/
│   ├── kansas_relief_terrain.png
│   ├── kansas_hillshade_30m.png
│   └── stac.json
│
├── archaeological/
│   ├── settlement_density_1890.png
│   ├── generalized_sites_overlay.geojson
│   └── stac.json
│
├── hydrology/
│   ├── flood_extent_1993.png
│   ├── watershed_boundaries.png
│   └── stac.json
│
├── climate/
│   ├── drought_anomaly_map_1956.png
│   ├── precipitation_departure_1930s.png
│   └── stac.json
│
├── landcover/
│   ├── ndvi_change_2001_2021.png
│   ├── prairie_loss_density.png
│   └── stac.json
│
└── metadata/
    ├── map_assets_index.json      # Required per-asset listing
    └── provenance_records/
```

---

## 🧩 Metadata Requirements (per-asset)

Each map asset must include:

| Field | Description |
|-------|-------------|
| `id` | Unique asset ID |
| `path` | Relative file path |
| `type` | Must be `map` |
| `checksum` | SHA-256 hash |
| `provenance.datasets` | Source datasets |
| `provenance.methods` | Processing steps |
| `care.status` | `public` · `generalized` · `restricted` |
| `updated` | ISO timestamp |

---

## 🧾 Example Map Metadata Record

```json
{
  "id": "kansas_drought_1956_map_v10",
  "type": "map",
  "path": "climate/drought_anomaly_map_1956.png",
  "checksum": "sha256-ca1be0043afe12fd442cc89ebf93fd132f1ddfa8db31c3697eb9778b03aa093f",
  "provenance": {
    "datasets": ["noaa_pds_1950_2020", "usdm_archive"],
    "methods": [
      "30-year baseline anomaly calculation",
      "Raster reproject EPSG:4326",
      "Color ramp normalization"
    ]
  },
  "care": {
    "status": "public",
    "notes": "No sensitive site information."
  },
  "updated": "2025-11-12T15:40:00Z"
}
```

---

## 📐 Visualization Standards for Story Nodes

| Requirement | Rule |
|------------|------|
| **Format** | PNG, SVG, GeoJSON, TopoJSON |
| **Resolution** | Minimum 2048 px width for map surfaces |
| **Projection** | EPSG:4326 unless otherwise noted |
| **Metadata** | STAC item in sibling directory required |
| **CARE** | Archaeological/cultural features must be generalized ≥ 5 km |
| **Color Accessibility** | WCAG 2.1 AA compliant (contrast ≥ 4.5:1) |

---

## 🧠 FAIR+CARE Governance Alignment

| Principle | Implementation |
|----------|----------------|
| **Findable** | STAC metadata, indexed asset registries |
| **Accessible** | CC-BY licensing + public paths |
| **Interoperable** | Standard projections & open raster/vector formats |
| **Reusable** | Provenance, checksums, reproducible code |
| **CARE** | Spatial generalization for sensitive datasets |

---

## 🧭 Related Directories

- **Story Node Assets Root**  
  `../assets/README.md`

- **3D Views**  
  `../../3d_views/README.md`

- **Story Node Metadata**  
  `../../metadata/README.md`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Team | Initial map asset registry for Focus Mode Story Nodes. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  
[⬅ Back to Asset Index](../README.md)

</div>

