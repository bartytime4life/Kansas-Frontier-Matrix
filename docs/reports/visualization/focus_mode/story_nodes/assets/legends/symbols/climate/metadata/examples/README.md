---
title: "🧩 Kansas Frontier Matrix — Climate Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/metadata/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Climate Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/metadata/examples/README.md`

**Purpose:**  
Provide ready-to-use sample metadata snippets for developers configuring climate symbols across Focus Mode, Story Nodes, and STAC metadata layers.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Ready-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

</div>


---

## 📚 Overview

This folder contains **developer-ready examples** demonstrating correct formats for:

- Climate symbol registry entries (`climate-symbols.json`)
- STAC symbol metadata (`climate-symbols.stac.json`)
- Story Node binding examples (`climate-symbols-story-nodes.json`)

All examples follow:

- FAIR+CARE governance  
- MCP-DL v6.3 formatting  
- The KFM standardized metadata format  
- **Indent-only code examples** (no nested fenced blocks)  
- Neutral, non-stigmatizing symbol semantics  

These samples serve as templates for adding new climate symbols.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                # This document
    |-- example-symbol.json      # Example climate symbol registry entry
    |-- example-stac.json        # Example STAC asset declaration
    |-- example-storynode.json   # Example Story Node symbol binding

---

### 🧱 Example — Climate Symbol Registry Entry

Example structure for `climate-symbols.json`:

    {
      "id": "heat_extreme",
      "category": "temperature",
      "label": "Extreme Heat",
      "description": "High-temperature event exceeding threshold.",
      "svg": "../svg/heat_extreme.svg",
      "emoji": "🔥",
      "severity": "extreme",
      "data_mapping": {
        "variable": "tas_anom",
        "unit": "°C",
        "min": 4
      }
    }

---

### 🧩 Example — STAC Legend Asset

Example structure for `climate-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-climate-v1",
      "collection": "kfm-legends",
      "assets": {
        "heat_extreme_svg": {
          "href": "../svg/heat_extreme.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Extreme Heat Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example structure for `climate-symbols-story-nodes.json`:

    {
      "heat_extreme": {
        "label": "Extreme Heat",
        "badge": true,
        "emoji": "🔥",
        "contexts": ["climatology", "hazards"],
        "description": "Heatwave conditions of extreme severity."
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                               |
|----------|------------|---------------|-----------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial examples README using full memory rules.    |