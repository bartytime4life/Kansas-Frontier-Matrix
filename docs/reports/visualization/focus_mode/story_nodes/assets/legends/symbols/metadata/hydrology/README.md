---
title: "💧 Kansas Frontier Matrix — Hydrology Symbol Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/hydrology/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Symbol Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/hydrology/README.md`

**Purpose:**  
Define the authoritative metadata schemas for all **hydrology symbols** used across Focus Mode, Story Nodes, MapLibre visualization layers, and STAC-aligned hydrologic datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Hydrology-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains canonical metadata definitions governing hydrology symbols representing:

- Streamflow, discharge, & peak flow events  
- River gauge stations  
- Flood-stage & inundation markers  
- Drought & low-flow indicators  
- Groundwater wells & aquifer markers  
- Hydrologic unit/watershed boundaries  
- Water infrastructure (dams, levees, diversions)  

These metadata files:

- Define symbol identity and semantics  
- Link symbols to hydrologic datasets  
- Map symbols to STAC Items for catalog publication  
- Drive Story Node symbol embedding rules  
- Enforce FAIR+CARE hydrologic communication ethics  
- Support Focus Mode hydrology overlays  

No hydrology symbol is permitted in KFM unless defined here.

---

### 🗂️ Directory Layout

    hydrology/
    |-- README.md                               # This document
    |-- hydrology-symbols.json                  # Canonical hydrology symbol registry
    |-- hydrology-symbols.stac.json             # STAC metadata for hydrologic symbols
    |-- hydrology-symbols-story-nodes.json      # Story Node usage bindings
    |
    └── examples/                               # Developer metadata examples

---

### 🧱 Hydrology Symbol Registry — `hydrology-symbols.json`

Defines canonical fields for each hydrology symbol:

- id  
- category (flood, drought, groundwater, discharge, infrastructure)  
- label  
- description  
- svg path  
- png fallback path (optional)  
- emoji fallback  
- severity (none/moderate/severe/extreme)  
- data_mapping  
  - variable (streamflow, gw_level, discharge, etc.)  
  - unit (m³/s, ft³/s, ft, index)  
  - thresholds  

Example (indented):

    {
      "id": "discharge_peak",
      "category": "streamflow",
      "label": "Peak Discharge",
      "description": "High-flow event exceeding expected discharge thresholds.",
      "svg": "../svg/discharge_peak.svg",
      "emoji": "💧",
      "severity": "severe",
      "data_mapping": {
        "variable": "streamflow",
        "unit": "m³/s",
        "threshold": "Q > Q95"
      }
    }

---

### 🧩 STAC Metadata — `hydrology-symbols.stac.json`

Defines STAC-compatible metadata for publishing symbol assets, ensuring:

- External discoverability  
- FAIR+CARE metadata inclusion  
- Standardized hydrologic lineage fields  
- Valid `roles: ["legend", "symbol"]`  

Example (indented):

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
          "title": "Flood Highwater Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `hydrology-symbols-story-nodes.json`

Controls how hydrology symbols behave inside Story Nodes:

- Badge visibility rules  
- Timeline placement  
- Header icon use  
- Recommended Focus Mode contexts  
- Emoji fallback usage  
- CARE sensitivity labels  
- Hydrologic domain tagging  

Example (indented):

    {
      "gauge_station": {
        "label": "River Gauge Station",
        "badge": true,
        "emoji": "📏",
        "contexts": ["hydrology", "monitoring"],
        "display_rules": {
          "timeline": true,
          "header": false
        }
      }
    }

---

### 🧪 Validation & CI

Hydrology metadata is validated using:

- JSON Schema checks  
- STAC schema validation  
- SVG/PNG file existence checks  
- Variable/unit consistency validation  
- Story Node binding tests  
- CARE-compliant hydrologic communication checks  
- Optional preview/snapshot linkage  

Local test command (shown indented):

    make test-legends-hydrology

This runs:

- Metadata validation  
- STAC validation  
- Story Node usage validation  
- Snapshot comparison (if enabled)  

All hydrology metadata must pass CI before merge approval.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                  |
|----------|------------|---------------|------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology metadata overview, fully memory-rule compliant.      |