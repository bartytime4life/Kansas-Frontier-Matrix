---
title: "🌾 Kansas Frontier Matrix — Landcover Legend Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/landcover/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Landcover Legend Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/landcover/examples/README.md`

**Purpose:**  
Provide fully compliant templates for constructing **landcover symbol metadata** used across Focus Mode, Story Nodes, map legends, and STAC-integrated ecological datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Landcover%20Metadata-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer Ready" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer-ready reference examples** showing correct formatting for:

- Landcover symbol registry entries  
- STAC legend & symbol asset metadata  
- Story Node landcover symbol bindings  

All examples follow stored memory rules:

- **One fenced block**
- **Indented JSON examples only**  
- **Correct heading hierarchy (## → ###)**  
- **Directory layout at `###`**  
- **No nested code fences**  
- **FAIR+CARE compliant ecological representation**  

Use these templates when adding or updating landcover symbol metadata.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                         # This document
    |-- example-landcover-symbol.json     # Example registry entry
    |-- example-stac.json                 # Example STAC metadata entry
    |-- example-storynode.json            # Example Story Node symbol binding

---

### 🧱 Example — Landcover Symbol Registry Entry

Example entry for `landcover-symbols.json`:

    {
      "id": "prairie_mixedgrass",
      "category": "grassland",
      "label": "Mixed-Grass Prairie",
      "description": "Prairie ecosystem characterized by a blend of tallgrass and shortgrass species.",
      "svg": "../svg/prairie_mixedgrass.svg",
      "emoji": "🌾",
      "landcover_type": "NLCD_71",
      "cultural_sensitivity": "public"
    }

---

### 🧩 Example — STAC Legend Metadata

Example for `landcover-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-landcover-v1",
      "collection": "kfm-legends",
      "assets": {
        "prairie_mixedgrass_svg": {
          "href": "../svg/prairie_mixedgrass.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Mixed-Grass Prairie Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example entry for `landcover-symbols-story-nodes.json`:

    {
      "grassland_icon": {
        "label": "Grassland",
        "badge": true,
        "emoji": "🌾",
        "contexts": ["ecology", "vegetation", "habitat"],
        "display_rules": {
          "timeline": true,
          "header": false
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                     |
|----------|------------|---------------|---------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover legend metadata examples — fully memory-rule compliant. |
