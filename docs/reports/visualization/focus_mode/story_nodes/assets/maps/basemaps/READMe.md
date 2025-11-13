---
title: "🗺️ Kansas Frontier Matrix — Story Node Basemap Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/basemaps/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-focusmode-basemaps-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Story Node Basemap Assets Index**  
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/basemaps/README.md`

**Purpose:**  
Provide a FAIR+CARE-aligned index for **basemap raster and vector layers** used by Focus Mode Story Nodes.  
These basemaps supply **contextual terrain, elevation, relief, hydrology, boundaries**, and **reference cartography** for KFM’s interactive narrative visualizations.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Basemaps under this directory serve as the **foundational cartographic layers** on which Story Node overlays are rendered.  
All basemaps must include **STAC metadata**, **checksum verification**, and **CARE sensitivity classification**.

This includes:

- Terrain relief & shaded relief  
- Hillshades (30m, 10m, 1m depending on region)  
- Vector boundaries (counties, rivers, watersheds)  
- Historical reference cartography  
- Neutral-tone accessibility-compliant base layers  
- Generalized basemaps for sensitive cultural areas  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/maps/basemaps/
├── README.md                      # This file
├── kansas_relief_terrain.png
├── kansas_hillshade_30m.png
├── kansas_boundary_reference.svg
├── neutral_gray_basemap.png
└── stac.json                      # STAC item for all assets
```

---

## 🧩 Metadata Requirements (per basemap)

| Field | Description |
|-------|-------------|
| `id` | Unique asset identifier |
| `path` | Relative file path |
| `type` | Must be `"basemap"` |
| `checksum_sha256` | Required integrity hash |
| `projection` | Default: EPSG:4326 |
| `provenance.datasets` | Source DEMs / boundaries / raster products |
| `provenance.methods` | Processing steps (e.g., hillshade generation) |
| `care.status` | `public` · `generalized` · `restricted` |
| `updated` | ISO timestamp |

---

## 🧾 Example Basemap Metadata Record

```json
{
  "id": "kansas_hillshade_30m_v10",
  "type": "basemap",
  "path": "kansas_hillshade_30m.png",
  "checksum_sha256": "sha256-eab1820fa03a992c7df1b0f9094db37df29055aafce6b4f07aaa5d35c6e4192c",
  "projection": "EPSG:4326",
  "provenance": {
    "datasets": ["usgs_ned_30m"],
    "methods": [
      "DEM reprojection",
      "Hillshade generation (315° azimuth, 35° altitude)",
      "Contrast normalization"
    ]
  },
  "care": {
    "status": "public",
    "notes": "No sensitive archaeological features embedded."
  },
  "updated": "2025-11-12T16:05:00Z"
}
```

---

## 🎨 Basemap Design Standards

| Requirement | Rule |
|------------|------|
| **Projection** | All basemaps must be EPSG:4326 unless purpose-specific |
| **Resolution** | Minimum width 2048 px |
| **Color Accessibility** | WCAG 2.1 AA contrast-safe palettes |
| **Neutral Variant** | Required for overlays to avoid ambiguity |
| **STAC Metadata** | `stac.json` required for every basemap folder |
| **CARE Masking** | Must generalize cultural features ≥ 5 km when present |

---

## 🧠 FAIR+CARE Alignment

| Principle | Implementation |
|----------|----------------|
| **Findable** | STAC items + asset index |
| **Accessible** | CC-BY maps, documented lineage |
| **Interoperable** | PNG/SVG/GeoJSON & standard projections |
| **Reusable** | Provenance included; reproducible processing |
| **CARE** | Sensitive features removed or masked |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Team | Initial basemap asset registry created for Focus Mode Story Nodes. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  
[⬅ Back to Map Assets](../README.md)

</div>

