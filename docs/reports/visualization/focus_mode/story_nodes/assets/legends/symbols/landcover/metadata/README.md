---
title: "🌾 Kansas Frontier Matrix — Landcover Symbol Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/metadata/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Landcover Symbol Metadata Specification**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/metadata/README.md`

**Purpose:**  
Define the authoritative machine-readable metadata for all landcover symbols used in Focus Mode, Story Nodes, map legends, ecological overlays, and STAC-linked datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Landcover-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-brightgreen" />

</div>


---

## 📚 Overview

This directory defines the **canonical metadata structures** for all landcover symbol icons used throughout the Kansas Frontier Matrix (KFM).

These metadata files control symbol usage in:

- Focus Mode ecological overlays  
- Story Node landcover badges  
- Timeline landcover transitions  
- Map legends across all visualization layers  
- STAC Item & Collection publishing  
- FAIR+CARE–aligned ecological communication  

Landcover metadata covers:

- Vegetation classes (grassland, woodland, shrubland)  
- Agricultural land use  
- Wetlands  
- Built environments  
- Prairie biotype distinctions  

Any landcover symbol must be registered here before use.

---

### 🗂️ Directory Layout

    metadata/
    |-- README.md                           # This document
    |-- landcover-symbols.json              # Canonical landcover symbol registry
    |-- landcover-symbols.stac.json         # STAC definitions for landcover symbols
    |-- landcover-symbols-story-nodes.json  # Story Node usage and binding rules
    |
    └── examples/                           # Developer metadata samples

---

### 🧱 Landcover Symbol Registry — `landcover-symbols.json`

This file defines each symbol’s:

- id  
- category (grassland, woodland, shrubland, cropland, wetland, built)  
- label  
- description  
- svg reference  
- emoji fallback  
- landcover_type (ecological code, e.g., NLCD class)  
- cultural/ecological sensitivity flags (CARE)  
- variable mappings (if applicable)  

Example (indented):

    {
      "id": "grassland_icon",
      "category": "grassland",
      "label": "General Grassland",
      "description": "Represents natural or semi-natural grassland ecosystems.",
      "svg": "../svg/grassland_icon.svg",
      "emoji": "🌾",
      "landcover_type": "NLCD_71",
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `landcover-symbols.stac.json`

This file defines how each symbol is exposed via STAC for external cataloging and dataset indexing.

Features include:

- STAC Item metadata  
- Asset declarations for SVG/PNG versions  
- Category tagging  
- FAIR+CARE lineage fields  
- Legend classification metadata  

Example (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-landcover-v1",
      "collection": "kfm-legends",
      "assets": {
        "grassland_icon_svg": {
          "href": "../svg/grassland_icon.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Grassland Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `landcover-symbols-story-nodes.json`

This file controls how landcover symbols behave inside Story Nodes:

- Whether symbols appear as badges  
- Header/timeline placement  
- Label formatting  
- Recommended narrative contexts (ecology, vegetation, land use, restoration)  
- Emoji fallbacks  
- Display rules  

Example (indented):

    {
      "woodland_icon": {
        "label": "Woodland",
        "badge": true,
        "emoji": "🌲",
        "contexts": ["ecology", "habitat", "vegetation"],
        "display_rules": {
          "timeline": true,
          "header": false
        }
      }
    }

---

### 🧪 Validation & CI

Hydrology metadata undergoes:

- JSON Schema validation  
- File path integrity checks  
- STAC validation  
- Story Node usage rule validation  
- CARE label compliance checks  
- Optional snapshot linkage checks (if tied to icon previews)  

Local test runner (indented):

    make test-legends-landcover

All landcover metadata must pass validation to be merged.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                           |
|----------|------------|---------------|-----------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover metadata README, fully memory-rule compliant. |