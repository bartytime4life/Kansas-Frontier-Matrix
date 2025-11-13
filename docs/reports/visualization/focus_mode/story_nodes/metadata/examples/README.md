---
title: "🧩 Kansas Frontier Matrix — Story Node Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/metadata/examples/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reports-visualization-focusmode-storynode-examples-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Story Node Metadata Examples**
`docs/reports/visualization/focus_mode/story_nodes/metadata/examples/README.md`

**Purpose:**  
Provide **canonical, validated examples** of Story Node metadata used in Focus Mode.  
These serve as reference implementations for narrative authors, pipeline maintainers, and UI/3D visualization systems.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

These examples show:
- Minimum viable Story Node metadata  
- Full metadata variants with spatial, temporal, provenance, 2D/3D visualization, and CARE governance blocks  
- Correct formatting and fields required by the **v10 Story Node Schema**  
- FAIR+CARE aligned narrative metadata patterns  

All examples validate successfully via:
- `faircare-validate.yml`
- `stac-validate.yml`
- `docs-lint.yml`

---

## 🧩 Example 1 — Minimal Valid Story Node

```json
{
  "id": "storynode_heatwave_1956",
  "title": "The 1956 Kansas Heatwave",
  "summary": "A defining climate event that reshaped regional farming resilience.",
  "temporal": {
    "start": "1956-06-01T00:00:00Z",
    "end": "1956-09-01T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "provenance": {
    "datasets": ["noaa_temp_1900_2025"],
    "citations": ["NOAA Climate Records (1956)"]
  },
  "updated": "2025-11-12T14:12:00Z"
}
```

---

## 🧩 Example 2 — Full Spatial + Temporal + Provenance Metadata

```json
{
  "id": "storynode_flood_epoch_1935",
  "title": "The 1935 Flood Epoch Along the Republican River",
  "summary": "Historic flooding reshaped settlement, hydrology, and cultural migration routes.",
  "temporal": {
    "start": "1935-05-15T00:00:00Z",
    "end": "1935-06-30T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "spatial": {
    "bbox": [-100.92, 39.01, -96.45, 40.32],
    "crs": "EPSG:4326",
    "geometry": {
      "type": "Polygon",
      "coordinates": [[
        [-100.92, 39.10], [-98.4, 39.50],
        [-97.1, 39.20], [-96.45, 40.32],
        [-100.92, 39.10]
      ]]
    }
  },
  "provenance": {
    "datasets": [
      "usgs_streamflow_1900_2025",
      "fema_nfhl_floodzones_ks"
    ],
    "citations": [
      "USGS Streamflow Archive (1900–2025)",
      "FEMA NFHL Flood Hazard Zones"
    ],
    "lineage": "Hydrologic extent interpolated from monthly peak flow anomaly models."
  },
  "visualization": {
    "map_2d": "flood_extent_1935.png",
    "scene_3d": "republican_river_1935.glb",
    "overlay": "flood_depth_overlay.geojson"
  },
  "updated": "2025-11-12T14:17:00Z"
}
```

---

## 🧩 Example 3 — Cultural / Sensitive Sites With CARE Governance

```json
{
  "id": "storynode_indigenous_trade_route_epoch_pre1800",
  "title": "Pre-1800 Indigenous Trade Routes Across Northeast Kansas",
  "summary": "Generalized spatial narrative describing historic tribal mobility corridors.",
  "temporal": {
    "start": "1700-01-01T00:00:00Z",
    "end": "1800-01-01T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "spatial": {
    "bbox": [-96.55, 38.80, -94.60, 40.10],
    "crs": "EPSG:4326"
  },
  "provenance": {
    "datasets": ["khs_archival_trade_routes"],
    "citations": [
      "Kansas Historical Society (Trade Route Manuscripts)",
      "Ethnohistorical Archives, Prairie Band Potawatomi Nation"
    ],
    "lineage": "Spatial paths generalized with 10 km uncertainty buffer under CARE review."
  },
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council + Tribal Historic Preservation Office",
    "notes": "Sensitive spatial features generalized; direct site coordinates removed."
  },
  "visualization": {
    "map_2d": "generalized_trade_routes.png"
  },
  "updated": "2025-11-12T14:25:00Z"
}
```

---

## 🧩 Example 4 — Story Node With Entities (CIDOC CRM-Aligned)

```json
{
  "id": "storynode_railroad_expansion_1870s",
  "title": "Railroad Expansion Through Northern Kansas (1870s)",
  "summary": "Dramatic increases in rail access transformed migration, farming, and trade.",
  "temporal": {
    "start": "1870-01-01T00:00:00Z",
    "end": "1879-12-31T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "entities": [
    {
      "type": "Event",
      "name": "Union Pacific Railway Construction"
    },
    {
      "type": "Group",
      "name": "Settler Communities"
    },
    {
      "type": "EcologicalProcess",
      "name": "Tallgrass Prairie Fragmentation"
    }
  ],
  "provenance": {
    "datasets": ["kdot_railroad_historical", "nlcd_landcover_1850_2020"],
    "citations": ["KDOT Railway Archives", "USGS NLCD Historical Reconstructions"]
  },
  "visualization": {
    "map_2d": "railroad_growth_1870s.png",
    "overlay": "landcover_change.geojson"
  },
  "updated": "2025-11-12T14:33:00Z"
}
```

---

## 🧩 Example 5 — 3D Scene-Focused Story Node

```json
{
  "id": "storynode_pleistocene_waterways",
  "title": "Pleistocene Waterways Beneath Modern Kansas",
  "summary": "Subsurface 3D reconstruction of paleo-channels and buried valley systems.",
  "temporal": {
    "start": "-12000-01-01T00:00:00Z",
    "end": "-8000-01-01T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "visualization": {
    "scene_3d": "paleo_channels.glb"
  },
  "provenance": {
    "datasets": ["usgs_buried_valleys_ks", "lidar_multitemporal_relief"],
    "citations": ["USGS Paleochannel Research Program"]
  },
  "updated": "2025-11-12T14:41:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | KFM Focus Mode Team | Initial examples directory creation with full FAIR+CARE-compliant Story Node metadata models. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Story Node Metadata](../README.md) · [⬅ Story Node Index](../../README.md)

</div>

