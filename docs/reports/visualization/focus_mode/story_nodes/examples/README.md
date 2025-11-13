---
title: "🧩 Kansas Frontier Matrix — Story Node Examples Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/examples/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-storynode-examples-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Story Node Examples Index**
`docs/reports/visualization/focus_mode/story_nodes/examples/README.md`

**Purpose:**  
Provide curated examples of **Story Node JSON/JSON-LD records** used in Focus Mode.  
These examples demonstrate correct structure, FAIR+CARE alignment, provenance linkage, temporal modeling, and visualization bindings for **narrative-driven spatial analysis**.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory provides **reference-quality Story Node examples** for developers, analysts, and Focus Mode integrators.  
Each example demonstrates:

- Correct **metadata** fields from the official Story Node schema  
- Alignment with **STAC/DCAT** geospatial metadata  
- **CIDOC CRM** and **OWL-Time** mappings  
- Proper **CARE** sensitivity annotation  
- Linkage to **2D/3D visualization assets**  
- Provenance, citations, and dataset lineage  
- Deployment-ready structure for ingestion in Focus Mode

Examples here are validated nightly by CI via:

- `storynode-schema-v10.json`
- `faircare-validate.yml`
- `stac-validate.yml`
- `telemetry-export.yml`

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/examples/
├── README.md                           # This file
├── settlement_transition_1856.json     # Example Story Node: Archaeology/Ecology
├── treaty_boundary_shift_1861.json     # Example Story Node: Historical/Political
├── drought_epoch_1890.json             # Example Story Node: Climate/Hydrology
├── hydrology_change_1930s.json         # Example Story Node: Watershed/Hydrology
└── wildfire_regime_shift_1870s.json    # Example Story Node: Ecology/Fire History
```

---

## 🧬 Example Summary Table

| File | Theme | Spatial Type | Temporal Type | CARE Status |
|------|--------|---------------|----------------|--------------|
| `settlement_transition_1856.json` | Archaeology/Ecology | Polygon | Interval | Approved |
| `treaty_boundary_shift_1861.json` | Historical/Legal | Polygon/Lines | Instant | Approved |
| `drought_epoch_1890.json` | Climate/Hydrology | Raster/Extent | Interval | Approved |
| `hydrology_change_1930s.json` | Watershed/Hydrology | Basin Polygons | Multi-Interval | Approved |
| `wildfire_regime_shift_1870s.json` | Ecology/Fire | Region Mask | Decadal Range | Approved |

---

## 🧩 Mini Example (Structure Reference)

```json
{
  "id": "storynode_treaty_boundary_shift_1861",
  "type": "StoryNode",
  "title": "Treaty Boundary Shift of 1861",
  "description": "Illustrates the legal and territorial changes resulting from the 1861 treaty modifications affecting northeastern Kansas.",
  "temporal": {
    "start": "1861-01-01T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "spatial": {
    "geometry": "geojson/polygon",
    "bbox": [-96.55, 38.89, -95.02, 39.41]
  },
  "provenance": {
    "datasets": [
      "kfm_treaty_boundaries_v10",
      "kfm_settlement_patterns_v10"
    ],
    "citations": [
      "Kappler’s Indian Affairs: Laws and Treaties",
      "Kansas Historical Society Archives"
    ]
  },
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council"
  },
  "links": {
    "map_2d": "treaty_shift_1861.png",
    "scene_3d": "story_context_scenes/treaty_shift_1861.glb"
  },
  "updated": "2025-11-12T12:00:00Z"
}
```

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|----------|----------------|
| **Collective Benefit** | Enhances public understanding of Kansas history without exposing sensitive data |
| **Authority to Control** | Story Nodes involving cultural or archaeological materials flagged for review |
| **Responsibility** | Includes citations, provenance graphs, and audit trails |
| **Ethics** | Spatial generalization applied when cultural sites are involved |

---

## 🧮 Telemetry Example (Batch Validation)

```json
{
  "batch": "storynode_examples_v10",
  "validated": 5,
  "energy_joules": 13.7,
  "carbon_gCO2e": 0.0056,
  "status": "Pass",
  "timestamp": "2025-11-12T12:02:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Focus Mode Team | Initial Story Node examples index with FAIR+CARE/ontology alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Story Nodes](../README.md) · [⬅ Back to Visualization Index](../../../README.md)

</div>

