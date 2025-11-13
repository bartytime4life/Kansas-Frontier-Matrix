---
title: "🧩 Kansas Frontier Matrix — Focus Mode Story Nodes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-storynodes-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Focus Mode Story Nodes**
`docs/reports/visualization/focus_mode/story_nodes/README.md`

**Purpose:**  
Define and index all **Story Nodes** used by Kansas Frontier Matrix (KFM) Focus Mode to provide **narrative-linked spatial, temporal, and cultural context**.  
Story Nodes serve as the **atomic narrative units** within Focus Mode, powering explainable timelines, AI-assisted synthesis, immersive 3D scenes, and contextual overlays.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

**Story Nodes** unify narrative, spatial geometry, temporal intervals, provenance, and CARE-governed cultural metadata into a single structured unit.  
They act as **explainable links** between datasets, scenes, maps, timeline frames, and AI-generated insights across Focus Mode.

Each Story Node:
- Represents one narrative insight or historical moment  
- Links to **STAC/DCAT/CIDOC CRM** metadata  
- Includes spatial footprint (vector/mesh/extent)  
- Includes temporal coverage (instant or interval via OWL-Time)  
- Includes provenance, citations, and source datasets  
- Carries **CARE sensitivity flags** and masking rules  
- Links directly to 2D/3D visualizations and overlays  
- Is machine-parseable for AI summarization and explainability  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/
├── README.md                          # This file
├── examples/                          # Example Story Node JSON/LD files
│   ├── settlement_transition_1856.json
│   ├── treaty_boundary_shift_1861.json
│   ├── drought_epoch_1890.json
│   └── hydrology_change_1930s.json
├── metadata/                          # Validation schemas & provenance linkage
│   ├── storynode-schema-v10.json
│   ├── ontology-mapping.json
│   └── lineage-examples.json
├── assets/                            # Images & scene references for nodes
│   ├── preview_settlement.png
│   ├── preview_treaty_shift.png
│   └── preview_drought.png
└── stac/                              # Derived STAC/DCAT compatible node info
    ├── storynodes_collection.json
    └── items/
        ├── settlement_transition_1856.json
        ├── treaty_boundary_shift_1861.json
        └── drought_epoch_1890.json
```

---

## 🧬 Story Node Structure (v10 Reference)

```json
{
  "id": "storynode_settlement_transition_1856",
  "type": "StoryNode",
  "title": "Settlement Expansion & Ecotone Shift (1856)",
  "description": "Describes the ecological and cultural transitions during early settlement expansion in eastern Kansas.",
  "temporal": {
    "start": "1856-01-01T00:00:00Z",
    "end": "1856-12-31T23:59:59Z",
    "ontology": "OWL-Time"
  },
  "spatial": {
    "bbox": [-96.55, 38.89, -95.02, 39.41],
    "geometry": "geojson/polygon"
  },
  "provenance": {
    "datasets": [
      "kfm_landcover_ecotones_v10",
      "kfm_settlement_traces_v10",
      "kfm_historic_plats_v10",
      "kfm_hydrology_surfaces_v10"
    ],
    "citations": [
      "Kansas State Historical Society Records",
      "USGS Historical Topographic Archive"
    ]
  },
  "care": {
    "status": "approved",
    "sensitivity": "low",
    "reviewer": "FAIR+CARE Council"
  },
  "links": {
    "map_2d": "settlement_ecotone_1856.png",
    "scene_3d": "story_context_scenes/prairie_crossroads.glb",
    "timeline_frame": "frame_1856.png"
  },
  "updated": "2025-11-12T11:50:00Z"
}
```

---

## 🧩 How Story Nodes Integrate Focus Mode

| Component | Mapping |
|----------|---------|
| **Timeline** | Nodes provide labeled intervals & temporal context |
| **3D Scenes** | Nodes link directly to GLB/Cesium reconstructions |
| **Overlays** | Node spatial geometry informs raster/vector overlays |
| **AI Assistant** | Nodes act as explainable reference units for answers |
| **Story Mode** | Nodes are narrative chapters for user-guided tours |

---

## 🗺️ Story Node Categories

| Category | Description |
|----------|-------------|
| **Hydrology Nodes** | Flood epochs, drought cycles, watershed shifts |
| **Archaeology Nodes** | Settlement density changes, cultural landscapes |
| **Ecology Nodes** | Prairie transitions, fire regimes, habitat corridors |
| **Historical Nodes** | Treaty changes, migration periods, land-use epochs |
| **Geology Nodes** | Stratigraphic controls, terrace development |

---

## ⚖️ FAIR+CARE Narrative Ethics

| Principle | Implementation |
|----------|----------------|
| **Collective Benefit** | Nodes illuminate Kansas history and ecology without exposing sensitive data |
| **Authority to Control** | Tribal partners define which storylines require review |
| **Responsibility** | Provenance + citations + lineage trace for each node |
| **Ethics** | No precise site disclosure; context-only spatial footprints |

---

## 🧮 Example Telemetry Entry

```json
{
  "storynode_batch_id": "storynodes_v10",
  "nodes_validated": 41,
  "energy_joules": 13.6,
  "carbon_gCO2e": 0.0055,
  "faircare_status": "Pass",
  "timestamp": "2025-11-12T11:56:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Focus Mode Team | Initial index for Story Nodes, metadata models, and visualization linkage. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Focus Mode Visualization](../README.md) · [⬅ Back to 3D Views](../3d_views/README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

