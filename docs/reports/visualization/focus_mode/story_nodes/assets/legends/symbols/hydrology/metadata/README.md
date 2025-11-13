---
title: "💧 Kansas Frontier Matrix — Hydrology Symbol Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/metadata/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Symbol Metadata Specification**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/metadata/README.md`

**Purpose:**  
Define and govern the authoritative machine-readable metadata for all hydrology symbols used within Focus Mode, Story Nodes, map legends, and STAC-linked hydrologic datasets.

<img alt="Hydrology Metadata" src="https://img.shields.io/badge/Metadata-Hydrology-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Schema" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

</div>


---

## 📚 Overview

This directory contains all **canonical metadata files** defining hydrology-related symbols used across the Kansas Frontier Matrix (KFM).  
These metadata structures ensure:

- Consistent hydrologic glyph usage  
- Data-linked variables (streamflow, discharge, groundwater levels, etc.)  
- Severity thresholds and hydrologic classifications  
- FAIR+CARE-aligned representation of water processes and hazards  
- Accurate STAC integration for external cataloging  
- Validated, reproducible symbol usage across Focus Mode and Story Nodes  

No hydrology symbol may be used anywhere unless defined here.

---

### 🗂️ Directory Layout

    metadata/
    |-- README.md                           # This document
    |-- hydrology-symbols.json              # Canonical hydrology symbol registry
    |-- hydrology-symbols.stac.json         # STAC item definitions for symbols
    |-- hydrology-symbols-story-nodes.json  # Story Node symbol usage bindings
    |
    └── examples/                           # Developer sample metadata snippets

---

### 🧱 Hydrology Symbol Registry — `hydrology-symbols.json`

This file defines the **primary metadata** for each hydrology symbol:

- id  
- category (streamflow, flood, drought, groundwater, infrastructure)  
- label  
- description  
- svg (reference path)  
- emoji (fallback)  
- severity (none / moderate / severe / extreme)  
- data_mapping:  
  - variable (e.g., streamflow, discharge, gw_level)  
  - unit (m³/s, ft³/s, ft, index)  
  - thresholds  

Example (indented):

    {
      "id": "well_marker",
      "category": "groundwater",
      "label": "Groundwater Well",
      "description": "Monitoring location for groundwater depth or aquifer levels.",
      "svg": "../svg/well_marker.svg",
      "emoji": "💧",
      "severity": "none",
      "data_mapping": {
        "variable": "gw_level",
        "unit": "ft",
        "thresholds": {
          "low": 10,
          "critical": 5
        }
      }
    }

---

### 🧩 STAC Metadata — `hydrology-symbols.stac.json`

This file defines how hydrology symbols are represented as **STAC Items** or **assets**, ensuring:

- External discoverability  
- Data lineage tracking  
- Standards-based hydrologic metadata distribution  
- Proper `roles: ["legend", "symbol"]` classification  

Example event snippet (indented):

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
          "title": "Flood High Water Marker"
        }
      }
    }

---

### 🧠 Story Node Bindings — `hydrology-symbols-story-nodes.json`

Controls how hydrology symbols appear within:

- Story Node summaries  
- Timelines  
- Event focus views  
- Spatial overlays in map layers  

Key fields include:

- `label`  
- `badge` (true/false)  
- `emoji` fallback  
- recommended `contexts` (flood history, groundwater trends, drought record)  
- `display_rules`  

Example (indented):

    {
      "flood_highwater": {
        "label": "Flood Highwater",
        "badge": true,
        "emoji": "🌊",
        "contexts": ["hydrology", "hazards"],
        "display_rules": {
          "timeline": true,
          "header": true
        }
      }
    }

---

### 🧪 Validation & CI

Validation includes:

- JSON Schema conformance  
- File path existence checks for referenced SVG/PNG icons  
- Required-field enforcement  
- STAC validity  
- Snapshot matching (visual regression)  
- Hydrology variable/unit consistency checks  

Local validation command (shown as plain text):

    make test-legends-hydrology

This command runs:

- Metadata schema validation  
- Story Node binding checks  
- STAC integrity checks  
- Preview + snapshot regression tests  

All hydrology metadata MUST pass before merge approval.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                         |
|----------|------------|---------------|---------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology metadata README, fully memory-compliant.    |