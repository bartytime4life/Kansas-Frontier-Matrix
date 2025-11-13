---
title: "🖼️ Kansas Frontier Matrix — Story Node Asset Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-storynode-assets-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Story Node Asset Index**
`docs/reports/visualization/focus_mode/story_nodes/assets/README.md`

**Purpose:**  
Centralized index of **images, overlays, 3D scenes, legends, and supporting visual materials** referenced by Focus Mode Story Nodes.  
Ensures **provenance, reproducibility, and FAIR+CARE visualization ethics** for all narrative-linked assets.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

All visual and spatial materials used by Story Nodes must be:
- Traceable to datasets and commit versions  
- Stored in structured, metadata-enriched directories  
- Compatible with 2D/3D rendering standards (PNG, SVG, GeoJSON, GLB, CZML)  
- Accompanied by **CARE-sensitive** masking where required  
- Referenced by Story Node metadata via reproducible file paths  

This directory acts as the canonical registry for everything a Story Node displays.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/
├── README.md                          # This file
│
├── maps/                              # 2D static and thematic maps
│   ├── example_map.png
│   └── example_overlay.geojson
│
├── legends/                           # Colorbars, symbols, UI legends
│   ├── colorbars/
│   └── symbols/
│
├── overlays/                          # Feature overlays (GeoJSON, TopoJSON)
│   └── landcover_transition.geojson
│
├── scenes_3d/                         # Cesium/GLTF/GLB/CZML models
│   ├── prairie_reconstruction.glb
│   └── paleo_channels.czml
│
├── thumbnails/                        # Preview images for Story Node browsing
│   └── storynode_heatwave_1956.webp
│
└── metadata/                          # Asset lineage, checksums, STAC/DCAT metadata
    ├── assets_index.json
    └── provenance_records/
```

---

## 🧩 Asset Metadata Requirements

Every asset referenced by a Story Node **must** include a metadata entry in  
`assets/metadata/assets_index.json`.

Required fields:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier for the asset |
| `type` | `map` · `overlay` · `3d_scene` · `legend` · `thumbnail` |
| `path` | Relative file path within this directory |
| `checksum` | SHA-256 for integrity |
| `provenance.datasets` | Source dataset IDs |
| `provenance.citations` | Bibliographic/cultural references |
| `care.status` | Ethical classification: `public` · `generalized` · `restricted` |
| `updated` | ISO timestamp |

---

## 🧾 Example Asset Metadata Record

```json
{
  "id": "paleo_channels_scene_v10",
  "type": "3d_scene",
  "path": "scenes_3d/paleo_channels.glb",
  "checksum": "sha256-93ab4eaf91c32b0df99a2d3811cf5a9ce1b2337e9c1a0bdf5e1d27fb43f5bb08",
  "provenance": {
    "datasets": ["usgs_buried_valleys_ks", "lidar_multitemporal_relief"],
    "citations": ["USGS Paleochannel Reconstruction Program"]
  },
  "care": {
    "status": "public",
    "notes": "No culturally sensitive information."
  },
  "updated": "2025-11-12T14:55:00Z"
}
```

---

## 🧠 FAIR+CARE Alignment

| Category | Implementation |
|----------|----------------|
| **Findable** | All assets indexed in `assets_index.json` with STAC-ready metadata |
| **Accessible** | Public CC-BY licensing unless CARE-restricted |
| **Interoperable** | Use of standard formats: PNG/SVG/GeoJSON/GLB/CZML |
| **Reusable** | Checksums + provenance guarantee reproducibility |
| **CARE** | Generalization required for archaeological / sacred sites |

---

## 🧭 Workflow Integration

Assets are validated through:

| Workflow | Validation |
|---------|------------|
| `docs-lint.yml` | Markdown structure + file path verification |
| `stac-validate.yml` | STAC/DCAT metadata for spatial assets |
| `faircare-validate.yml` | CARE-sensitive content review |
| `telemetry-export.yml` | Sustainability & traceability logging |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.2.0 | 2025-11-12 | KFM Focus Mode Team | Initial asset registry creation with metadata and FAIR+CARE rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Story Node Index](../../README.md) ·  
[⬅ Metadata Directory](../metadata/README.md)

</div>

