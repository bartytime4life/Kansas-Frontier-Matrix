---
title: "💧 Kansas Frontier Matrix — Hydrology Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/metadata/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/metadata/examples/README.md`

**Purpose:**  
Provide fully formatted metadata examples for developers defining hydrology symbols within Focus Mode, Story Nodes, and STAC-based hydrologic datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Hydrology%20Metadata-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

</div>


---

## 📚 Overview

This folder contains **developer-ready** examples demonstrating proper metadata formatting for:

- Hydrology symbol registry entries  
- STAC legend/symbol assets  
- Story Node hydrology symbol bindings  

All examples strictly follow:

- Stored KFM Markdown Protocol  
- MCP-DL v6.3 rules  
- FAIR+CARE ethical guidelines  
- Indented examples (no nested code blocks)  
- GitHub-stable, one-block formatting  

Use these examples when adding or revising hydrology symbols.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                    # This document
    |-- example-hydrology-symbol.json
    |-- example-stac.json
    |-- example-storynode.json

---

### 🧱 Example — Hydrology Symbol Registry Entry

Example snippet for `hydrology-symbols.json`:

    {
      "id": "gauge_station",
      "category": "streamflow",
      "label": "River Gauge Station",
      "description": "Monitors river stage and discharge at fixed locations.",
      "svg": "../svg/gauge_station.svg",
      "emoji": "📏",
      "severity": "none",
      "data_mapping": {
        "variable": "streamflow",
        "unit": "m³/s",
        "thresholds": {
          "low": 10,
          "high": 300
        }
      }
    }

---

### 🧩 Example — STAC Legend Asset

Example snippet for `hydrology-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-hydrology-v1",
      "collection": "kfm-legends",
      "assets": {
        "gauge_station_svg": {
          "href": "../svg/gauge_station.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Gauge Station Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Defines Story Node usage for hydrology symbols.

Example snippet for `hydrology-symbols-story-nodes.json`:

    {
      "drought_lowflow": {
        "label": "Low Flow / Hydrologic Drought",
        "badge": true,
        "emoji": "🟫",
        "contexts": ["hydrology", "hazards", "drought"],
        "display_rules": {
          "timeline": true,
          "header": true
        }
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                           |
|----------|------------|---------------|-----------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology metadata examples README, memory-compliant.   |