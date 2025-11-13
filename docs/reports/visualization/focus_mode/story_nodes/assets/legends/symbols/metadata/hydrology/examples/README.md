---
title: "💧 Kansas Frontier Matrix — Hydrology Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/hydrology/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/hydrology/examples/README.md`

**Purpose:**  
Provide fully compliant, developer-ready hydrology symbol metadata examples for usage in Focus Mode, Story Nodes, map legends, and STAC-published hydrologic datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Hydrology%20Metadata-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer" src="https://img.shields.io/badge/Developer-Ready-teal" />

</div>


---

## 📚 Overview

This directory provides **reference examples** demonstrating proper construction of:

- Hydrology symbol registry entries  
- STAC symbol asset metadata  
- Story Node hydrology symbol bindings  

All examples strictly follow:

- KFM Markdown Protocol (single fenced block, correct heading levels)  
- Indented JSON examples (no fenced code blocks inside the main fence)  
- FAIR+CARE hydrologic communication standards  
- MCP-DL metadata discipline  
- GitHub-stable formatting  

Use these examples to guide the creation or refinement of hydrology symbol metadata files.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                          # This document
    |-- example-hydrology-symbol.json      # Example registry entry
    |-- example-stac.json                  # Example STAC entry
    |-- example-storynode.json             # Example Story Node binding

---

### 🧱 Example — Hydrology Symbol Registry Entry

Example structure for `hydrology-symbols.json`:

    {
      "id": "flood_highwater",
      "category": "flood",
      "label": "High Water / Flood Stage",
      "description": "Indicates river stage exceeding bankfull or established flood threshold.",
      "svg": "../svg/flood_highwater.svg",
      "emoji": "🌊",
      "severity": "severe",
      "data_mapping": {
        "variable": "streamflow",
        "unit": "m³/s",
        "threshold": "Q > Q100"
      }
    }

---

### 🧩 Example — STAC Legend Metadata

Example entry for `hydrology-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-hydrology-v1",
      "collection": "kfm-legends",
      "assets": {
        "flood_highwater_svg": {
          "href": "../svg/flood_highwater.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "High Water Marker"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example entry for `hydrology-symbols-story-nodes.json`:

    {
      "well_marker": {
        "label": "Groundwater Well",
        "badge": true,
        "emoji": "💧",
        "contexts": ["hydrology", "groundwater", "monitoring"],
        "display_rules": {
          "timeline": true,
          "header": false
        }
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                    |
|----------|------------|---------------|--------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology metadata examples README, fully memory-rule compliant. |
