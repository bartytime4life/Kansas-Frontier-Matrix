---
title: "🌾 Kansas Frontier Matrix — Landcover Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/landcover/examples/README.md"
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

# 🌾 **Kansas Frontier Matrix — Landcover Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/landcover/examples/README.md`

**Purpose:**  
Provide ready-to-use, memory-rule-compliant examples for developers creating new **landcover symbol metadata** aligned with Story Nodes, Focus Mode overlays, and STAC record structures.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Landcover%20Metadata-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer reference examples** showing the correct structure for:

- Landcover symbol registry entries  
- STAC legend/symbol assets  
- Story Node binding specifications  

These examples follow:

- Stored KFM Markdown rules  
- One-box / one-fence output  
- Indented (not fenced) code examples  
- FAIR+CARE ecological neutrality requirements  
- MCP-DL v6.3 metadata discipline  
- GitHub-stable formatting  

Use these examples as templates when adding or modifying landcover symbols.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                         # This document
    |-- example-landcover-symbol.json     # Example registry entry
    |-- example-stac.json                 # Example STAC metadata
    |-- example-storynode.json            # Example Story Node binding

---

### 🧱 Example — Landcover Symbol Registry Entry

Example snippet for `landcover-symbols.json`:

    {
      "id": "shrubland_icon",
      "category": "shrubland",
      "label": "Shrubland",
      "description": "Woody shrub-dominated vegetation class.",
      "svg": "../svg/shrubland_icon.svg",
      "emoji": "🌿",
      "landcover_type": "NLCD_52",
      "cultural_sensitivity": "public"
    }

---

### 🧩 Example — STAC Legend Metadata

For use in `landcover-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-landcover-v1",
      "collection": "kfm-legends",
      "assets": {
        "shrubland_icon_svg": {
          "href": "../svg/shrubland_icon.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Shrubland Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

For use in `landcover-symbols-story-nodes.json`:

    {
      "wetland_icon": {
        "label": "Wetland",
        "badge": true,
        "emoji": "💧",
        "contexts": ["ecology", "wetlands", "habitat"],
        "display_rules": {
          "timeline": true,
          "header": true
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                  |
|----------|------------|---------------|------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover metadata examples README, fully memory-compliant.     |
