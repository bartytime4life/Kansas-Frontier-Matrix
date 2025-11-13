---
title: "🌦️ Kansas Frontier Matrix — Climate Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/climate/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climate Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/climate/examples/README.md`

**Purpose:**  
Provide fully compliant, developer-ready example metadata entries for **climate symbols** used in Focus Mode, Story Nodes, map legends, and STAC-published climate datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Climate%20Metadata-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer" src="https://img.shields.io/badge/Developer-Ready-teal" />

</div>


---

## 📚 Overview

This directory contains **reference examples** demonstrating correct formatting for:

- Climate symbol registry entries  
- STAC legend/symbol entries  
- Story Node climate symbol bindings  

These examples follow:

- Stored KFM Markdown Protocol  
- Single fenced-block requirement  
- Indented JSON examples (NO nested backticks)  
- FAIR+CARE climate communication ethics  
- MCP-DL v6.3 metadata discipline  
- GitHub-stable formatting  

Use these examples as direct templates when adding or updating climate symbol metadata in the system.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                         # This document
    |-- example-climate-symbol.json       # Example core registry entry
    |-- example-stac.json                 # Example STAC Item snippet
    |-- example-storynode.json            # Example Story Node binding snippet

---

### 🧱 Example — Climate Symbol Registry Entry

Example entry for `climate-symbols.json`:

    {
      "id": "precip_heavy",
      "category": "precipitation",
      "label": "Heavy Precipitation",
      "description": "Significant positive precipitation anomaly relative to seasonal norms.",
      "svg": "../svg/precip_heavy.svg",
      "emoji": "🌧️",
      "severity": "severe",
      "data_mapping": {
        "variable": "prcp",
        "unit": "mm",
        "min": 50
      },
      "cultural_sensitivity": "public"
    }

---

### 🧩 Example — STAC Legend Metadata

Example snippet for `climate-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-climate-v1",
      "collection": "kfm-legends",
      "assets": {
        "precip_heavy_svg": {
          "href": "../svg/precip_heavy.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Heavy Precipitation Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Climate Symbol Binding

Example for `climate-symbols-story-nodes.json`:

    {
      "heat_extreme": {
        "label": "Extreme Heat",
        "badge": true,
        "emoji": "🔥",
        "contexts": ["climatology", "hazards"],
        "display_rules": {
          "timeline": true,
          "header": true
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                   |
|----------|------------|---------------|-------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial climate metadata examples README, fully memory-rule compliant.  |
