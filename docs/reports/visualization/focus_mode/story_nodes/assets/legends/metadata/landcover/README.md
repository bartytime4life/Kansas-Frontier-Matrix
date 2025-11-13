---
title: "🌾 Kansas Frontier Matrix — Landcover Legend Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/landcover/README.md"
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

# 🌾 **Kansas Frontier Matrix — Landcover Legend Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/landcover/README.md`

**Purpose:**  
Serve as the authoritative root index for all **landcover symbol metadata**, governing ecosystem, vegetation, land-use, and ecological classification icons used in Focus Mode, Story Nodes, map legends, and STAC-published landcover datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Landcover-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory defines the canonical metadata structures for **all landcover symbols** used in the Kansas Frontier Matrix (KFM).  
Landcover symbols represent:

- Grassland classes  
- Prairie biotypes (tallgrass, mixed-grass, shortgrass)  
- Woodland & forest cover  
- Shrubland  
- Wetlands  
- Cropland & agricultural areas  
- Urban/built environments  
- Transitional ecological zones  

Metadata ensures:

- Consistent ecological semantics  
- FAIR+CARE ecological representation  
- Correct SVG/PNG linkage  
- Valid Story Node bindings  
- STAC-compliant publication  
- Harmonized ecological storytelling across Focus Mode + maps  

No landcover symbol is considered valid unless defined here.

---

### 🗂️ Directory Layout

    landcover/
    |-- README.md                               # This document (index)
    |-- landcover-symbols.json                  # Canonical symbol registry
    |-- landcover-symbols.stac.json             # STAC metadata for symbol assets
    |-- landcover-symbols-story-nodes.json      # Story Node usage bindings
    |
    └── examples/                               # Developer-ready metadata samples

---

### 🧱 Landcover Symbol Registry — `landcover-symbols.json`

Defines canonical fields:

- id  
- category (grassland, woodland, shrubland, cropland, wetland, built)  
- label  
- description  
- svg path  
- optional png path  
- emoji fallback  
- landcover_type (NLCD code or ecological classification)  
- cultural/ecological sensitivity (CARE labels)  
- variable mappings (optional)  

Example (indented):

    {
      "id": "woodland_icon",
      "category": "woodland",
      "label": "Woodland",
      "description": "Represents wooded landscape dominated by tree cover.",
      "svg": "../svg/woodland_icon.svg",
      "emoji": "🌲",
      "landcover_type": "NLCD_41",
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `landcover-symbols.stac.json`

Defines STAC Items for legend/symbol publication:

- `roles: ["legend", "symbol"]`  
- Asset descriptions  
- Category metadata  
- FAIR+CARE ecological fields  
- STAC Collection linkages  

Example (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-landcover-v1",
      "collection": "kfm-legends",
      "assets": {
        "prairie_tallgrass_svg": {
          "href": "../svg/prairie_tallgrass.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Tallgrass Prairie Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `landcover-symbols-story-nodes.json`

Controls landcover symbol behavior:

- Badge behavior  
- Header vs. timeline visibility  
- Narrative embedding rules (`{symbol:id}`)  
- Emoji fallback  
- Context classification  
- CARE ecological sensitivity  

Example (indented):

    {
      "wetland_icon": {
        "label": "Wetland",
        "badge": true,
        "emoji": "💧",
        "contexts": ["ecology", "hydrology", "habitat"],
        "display_rules": {
          "timeline": true,
          "header": true
        }
      }
    }

---

### 🧪 Validation & CI Requirements

All landcover metadata must pass:

- JSON schema validation  
- File existence checks (SVG/PNG)  
- STAC schema validation  
- Story Node binding checks  
- CARE sensitivity enforcement  
- Optional snapshot linkage  

Local validator:

    make test-legends-landcover

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                  |
|----------|------------|---------------|------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover legend metadata overview — fully memory compliant.   |
