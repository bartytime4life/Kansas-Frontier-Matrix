---
title: "🌾 Kansas Frontier Matrix — Landcover Symbol Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/landcover/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Landcover Symbol Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/landcover/README.md`

**Purpose:**  
Define the canonical metadata governing all **landcover symbol assets** used in Focus Mode, Story Nodes, map legends, ecological overlays, and STAC-aligned landcover datasets within the Kansas Frontier Matrix (KFM).

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Landcover-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains the **authoritative metadata definitions** that control the behavior, classification, and semantic meaning of **landcover symbols** used throughout the Kansas Frontier Matrix.

Landcover symbols describe:

- Vegetation classes (grassland, prairie, woodland, shrubland)  
- Agricultural land use classes  
- Wetland types  
- Urban/built environments  
- Ecological biotypes and transitions  

Metadata in this directory ensures:

- Consistent representation across maps, timelines, and Story Nodes  
- FAIR+CARE ecological neutrality  
- Stable symbology for historical and ecological analysis  
- Correct linkage to SVG/PNG assets  
- STAC-compliant external cataloging  
- Reproducible rendering within Focus Mode  

No landcover symbol may appear in any KFM layer unless defined here.

---

### 🗂️ Directory Layout

    landcover/
    |-- README.md                               # This document
    |-- landcover-symbols.json                  # Canonical landcover symbol registry
    |-- landcover-symbols.stac.json             # STAC metadata for landcover icons
    |-- landcover-symbols-story-nodes.json      # Story Node usage + binding rules
    |
    └── examples/                               # Developer metadata examples

---

### 🧱 Landcover Symbol Registry — `landcover-symbols.json`

Defines the canonical fields for each landcover symbol:

- id  
- category (grassland, woodland, shrubland, cropland, wetland, built)  
- label  
- description  
- svg path  
- optional png path  
- emoji fallback  
- landcover_type (ecological class or NLCD code)  
- cultural/ecological sensitivity (CARE labels)  
- variable mappings (if applicable)  

Example (indented):

    {
      "id": "prairie_tallgrass",
      "category": "grassland",
      "label": "Tallgrass Prairie",
      "description": "Native tallgrass prairie ecosystem.",
      "svg": "../svg/prairie_tallgrass.svg",
      "emoji": "🌾",
      "landcover_type": "NLCD_71",
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `landcover-symbols.stac.json`

Defines how landcover symbols are represented in **STAC Items**, enabling:

- External discoverability  
- Dataset lineage  
- Legend/symbol asset classification  
- FAIR+CARE metadata propagation  

Example STAC snippet (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-landcover-v1",
      "collection": "kfm-legends",
      "assets": {
        "woodland_icon_svg": {
          "href": "../svg/woodland_icon.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Woodland Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `landcover-symbols-story-nodes.json`

Defines how landcover symbols are used inside Story Nodes:

- Badge visibility  
- Header/timeline placement rules  
- Recommended narrative contexts  
- Emoji fallbacks  
- CARE visibility restrictions  
- Display rules per ecological category  

Example (indented):

    {
      "grassland_icon": {
        "label": "Grassland",
        "badge": true,
        "emoji": "🌾",
        "contexts": ["ecology", "vegetation", "habitat"],
        "display_rules": {
          "timeline": true,
          "header": false
        }
      }
    }

---

### 🧪 Validation & CI Requirements

All landcover metadata must pass:

- JSON schema validation  
- File-path existence checks (SVG/PNG)  
- STAC schema conformance  
- Story Node binding validation  
- CARE/ecological neutrality checks  
- Optional snapshot linkage  

Local validation:

    make test-legends-landcover

This runs:

- Metadata validation  
- STAC validation  
- Story Node checks  
- Snapshot comparisons (if enabled)

Metadata must pass CI before merge approval.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                |
|----------|------------|---------------|----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover metadata overview, fully memory-rule compliant.     |