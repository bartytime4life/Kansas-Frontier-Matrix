---
title: "🌾 Kansas Frontier Matrix — Landcover Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/metadata/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Landcover Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/metadata/examples/README.md`

**Purpose:**  
Provide fully compliant metadata examples for landcover symbol definitions used in Focus Mode, Story Nodes, STAC metadata, and map legend integrations.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Landcover%20Metadata-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Required-gold" />
<img alt="DevReady" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer-ready example snippets** for constructing valid landcover symbol metadata.

Examples demonstrate correct formatting for:

- `landcover-symbols.json` entries  
- `landcover-symbols.stac.json` STAC definitions  
- `landcover-symbols-story-nodes.json` bindings  

All examples:

- Follow the stored Markdown Protocol  
- Maintain a single fenced block  
- Use indentation for JSON examples (no nested backticks)  
- Respect KFM legend semantics  
- Comply with FAIR+CARE ecological neutrality  
- Reflect STAC alignment requirements  

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                      # This document
    |-- example-landcover-symbol.json  # Example registry entry
    |-- example-stac.json              # Example STAC metadata
    |-- example-storynode.json         # Example Story Node binding

---

### 🧱 Example — Landcover Symbol Registry Entry

Example snippet for `landcover-symbols.json` (indented):

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

### 🧩 Example — STAC Legend Asset

Example snippet for `landcover-symbols.stac.json`:

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

### 🧠 Example — Story Node Symbol Binding

Example snippet for `landcover-symbols-story-nodes.json`:

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

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                 |
|----------|------------|---------------|-----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover metadata examples README, fully memory compliant.    |