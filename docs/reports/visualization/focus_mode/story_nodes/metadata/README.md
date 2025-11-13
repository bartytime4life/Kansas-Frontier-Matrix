---
title: "🧬 Kansas Frontier Matrix — Story Node Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-storynode-metadata-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Story Node Metadata Specification**
`docs/reports/visualization/focus_mode/story_nodes/metadata/README.md`

**Purpose:**  
Define the **metadata schema, ontology alignment, and validation rules** for Story Nodes used in Kansas Frontier Matrix (KFM) Focus Mode.  
Ensures every Story Node is **FAIR+CARE compliant**, **STAC/DCAT interoperable**, **CIDOC CRM aligned**, and **visually reproducible** across KFM’s 2D/3D visualization systems.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Story Nodes are **atomic narrative units** that power Focus Mode’s time-aligned, map-synchronized storytelling engine.  
Each Story Node combines:

- 🗺 Spatial extent (geometry, bbox, CRS)  
- ⏳ Temporal semantics (intervals, instants, epochs)  
- 🧠 Narrative metadata (summary, entities, storyline roles)  
- 🧩 Provenance & lineage (datasets, transformations, citations)  
- ⚖️ FAIR+CARE governance metadata (authority, ethics, sensitivity)  
- 🖼 Visualization links (2D maps, 3D scenes, overlays, legends)

This document defines the complete **metadata model** for constructing, validating, and publishing Story Nodes.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/metadata/
├── README.md                     # This file
├── schema_v10.json               # JSON Schema definition for Story Nodes
├── ontology_map.jsonld           # CIDOC CRM, OWL-Time & DCAT mappings
├── field_definitions.md          # Human-readable schema explanations
└── examples/                     # Minimal & full Story Node metadata examples
```

---

## 🧱 Core Metadata Fields

| Field | Type | Required | Description |
|-------|-------|----------|-------------|
| `id` | string | ✅ | Unique Story Node identifier (`storynode_*`). |
| `title` | string | ✅ | Human-readable narrative title. |
| `summary` | string | ✅ | Short description used in Focus Mode cards. |
| `temporal` | object | ✅ | Time interval/instant + ontology reference. |
| `spatial` | object | ⚙️ | GeoJSON geometry or bounding box. |
| `entities` | array | ⚙️ | People, events, organizations. |
| `provenance` | object | ✅ | Data lineage, dataset IDs, citations. |
| `visualization` | object | ⚙️ | References to 2D/3D assets. |
| `care` | object | ⚙️ | Ethical sensitivity classification. |
| `updated` | string | ✅ | ISO timestamp. |

---

## 🧩 Minimum Valid Story Node Example

```json
{
  "id": "storynode_flood_epoch_1935",
  "title": "Great Plains Flood Epoch of 1935",
  "summary": "A hydrological inflection point that reshaped Kansas river systems.",
  "temporal": {
    "start": "1935-01-01T00:00:00Z",
    "end": "1935-12-31T23:59:59Z",
    "ontology": "OWL-Time"
  },
  "provenance": {
    "datasets": ["usgs_streamflow_1900_1950", "kfm_climate_reanalysis_v10"],
    "citations": ["USGS Water-Supply Papers (1936)", "Kansas Flood Archives"]
  },
  "updated": "2025-11-12T13:20:00Z"
}
```

---

## 🧮 Full Story Node (Complete Metadata)

```json
{
  "id": "storynode_prairie_restoration_1870s",
  "title": "Prairie Restoration Patterns of the 1870s",
  "summary": "Ecological shifts in tallgrass prairie landscapes during the 1870s.",
  "temporal": {
    "start": "1870-01-01T00:00:00Z",
    "end": "1879-12-31T23:59:59Z",
    "ontology": "OWL-Time"
  },
  "spatial": {
    "geometry": "geojson/polygon",
    "bbox": [-101.5, 37.0, -94.6, 40.0],
    "crs": "EPSG:4326"
  },
  "entities": [
    { "type": "Group", "name": "Homesteaders of Central Kansas" },
    { "type": "EcologicalProcess", "name": "Tallgrass Expansion" }
  ],
  "provenance": {
    "datasets": [
      "nlcd_landcover_1870_1900",
      "kfm_climate_reconstruction_v10"
    ],
    "citations": [
      "Kansas State Historical Society Journals",
      "USDA Prairie Survey Records"
    ],
    "lineage": "Derived from normalized NLCD epoch data; spatial smoothing applied."
  },
  "visualization": {
    "map_2d": "prairie_1870s.png",
    "scene_3d": "prairie_reconstruction_1870s.glb",
    "overlay": "density_changes_1870s.svg"
  },
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Visualization Board",
    "notes": "No cultural site data involved."
  },
  "updated": "2025-11-12T13:24:00Z"
}
```

---

## 🧠 Ontology Mapping (CIDOC / OWL-Time / DCAT)

| Story Node Field | Ontology Mapping |
|-------------------|------------------|
| `temporal.start` / `end` | `time:Instant`, `time:Interval` |
| `entities.*` | `crm:E21_Person`, `crm:E7_Activity`, etc. |
| `provenance.citations` | `dct:source` |
| `provenance.datasets` | `dcat:Dataset` references |
| `visualization.*` | `dcat:Distribution` |
| `care.status` | CARE Principles extensions |

---

## ⚙️ Validation Rules

Story Nodes must pass:

- **Schema Validation** → `schema_v10.json`
- **FAIR+CARE Audit** → `faircare-validate.yml`
- **STAC/DCAT Compliance** → `stac-validate.yml`
- **Telemetry Logging** → `telemetry-export.yml`

CI rejects Story Nodes missing:

- Temporal fields  
- Provenance datasets  
- Summary text  
- Updated timestamp  
- CARE block for context-sensitive narratives  

---

## 🧮 Telemetry Record Example

```json
{
  "validation": "storynode_metadata_batch_v10",
  "validated": 42,
  "failures": 0,
  "energy_joules": 13.8,
  "carbon_gCO2e": 0.0056,
  "timestamp": "2025-11-12T13:30:00Z",
  "status": "Pass"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Focus Mode Team | Initial Story Node metadata specification with FAIR+CARE, CIDOC/OWL-Time alignment, and validation rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Story Nodes](../README.md) · [⬅ Back to Visualization Index](../../../README.md)

</div>

