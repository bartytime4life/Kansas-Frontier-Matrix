---
title: "🗂️ Kansas Frontier Matrix — Flood Visualization Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Hydrology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-metadata-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Flood Visualization Metadata Index**
`docs/reports/visualization/hydrology/flood/metadata/README.md`

**Purpose:**  
Define the **metadata structure, provenance linkage, and validation requirements** for all flood visualization artifacts in KFM.  
Ensures that every PNG, SVG, MP4, or GeoJSON flood visualization is **traceable, reproducible, ethically validated**, and registered in **STac/DCAT** catalogs with FAIR+CARE governance.

![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This folder contains all **metadata JSON files** corresponding to hydrological flood visualizations such as:
- Flood extent static maps  
- Temporal inundation animations  
- Flood frequency heatmaps  
- Basin/tributary overlays  
- 3D hydrology visual captures  

Each metadata file conforms to KFM’s **Visualization Metadata Contract v10**, aligning with:
- **STAC 1.0**
- **DCAT 3.0**
- **ISO 19115 (Geospatial metadata)**
- **FAIR+CARE hydrology ethics**

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/metadata/
├── README.md                           # This file
├── flood_extent_map.json               # Metadata for static flood extent visualization
├── flood_animation.json                # Metadata for temporal flood animation
└── flood_frequency_heatmap.json        # Metadata for multi-year flood recurrence heatmap
```

---

## 🧾 Required Metadata Schema (Summary)

| Field | Description | Required |
|-------|-------------|----------|
| `id` | Unique visualization identifier | ✅ |
| `title` | Human-readable visualization title | ✅ |
| `description` | Summary of what the visualization depicts | ✅ |
| `source_datasets` | List of KFM processed hydrology datasets used | ✅ |
| `projection` | CRS (must be `EPSG:4326`) | ✅ |
| `license` | SPDX/CC identifier (`CC-BY-4.0`) | ✅ |
| `care_review` | Ethical status of hydrology visualization | ✅ |
| `created` | ISO8601 creation timestamp | ✅ |
| `commit_sha` | Hash of generating workflow | ✅ |
| `stac_item` | Optional link to STAC Item (if published) | ⚙️ |
| `bounding_box` | Spatial extent (minX,minY,maxX,maxY) | ⚙️ |
| `temporal_extent` | Time range visualized | ⚙️ |
| `alt_text` | Human-readable accessible description | ⚙️ |
| `telemetry_ref` | Reference to telemetry log | ⚙️ |

---

## 🧠 Metadata Example (Flood Extent)

```json
{
  "id": "kfm_flood_extent_2025_v10",
  "title": "Kansas Flood Extent Map — April 2025",
  "description": "Static flood extent visualization created from processed hydrology datasets representing high-flow conditions in April 2025.",
  "source_datasets": [
    "hydro_flow_anomalies_v10",
    "watershed_boundaries_v10"
  ],
  "projection": "EPSG:4326",
  "license": "CC-BY-4.0",
  "care_review": {
    "status": "approved",
    "reviewer": "FAIR+CARE Hydrology Ethics Council",
    "notes": "Infrastructure details generalized for safety."
  },
  "created": "2025-11-12T09:20:00Z",
  "commit_sha": "<workflow-commit-sha>",
  "bounding_box": [-102.05, 37.00, -94.60, 40.00],
  "temporal_extent": ["2025-04-01", "2025-04-30"],
  "alt_text": "A shaded flood extent overlay map showing inundated regions across Kansas during April 2025.",
  "stac_item": "stac://hydrology/flood/kfm_flood_extent_2025_v10",
  "telemetry_ref": "releases/v10.2.0/focus-telemetry.json"
}
```

---

## ⚙️ FAIR+CARE Hydrological Compliance

| Principle | Application to Flood Visualizations |
|-----------|-------------------------------------|
| **Collective Benefit** | Supports flood preparedness & hazard research |
| **Authority to Control** | Sensitive hydrology layers reviewed for responsible public display |
| **Responsibility** | Visualizations must not expose critical infrastructure |
| **Ethics** | Review ensures no misuse potential for vulnerable communities |

---

## 🧪 Validation Workflows

| Workflow | Purpose |
|----------|----------|
| `stac-validate.yml` | Validates STAC metadata for visualizations |
| `faircare-validate.yml` | Ensures hydrological and cultural ethics |
| `visualization-validate.yml` | Confirms CRS, bounding box, metadata fields |
| `telemetry-export.yml` | Logs metadata generation & governance |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Council | Created comprehensive metadata index and contract alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Visualization](../README.md) · [Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

