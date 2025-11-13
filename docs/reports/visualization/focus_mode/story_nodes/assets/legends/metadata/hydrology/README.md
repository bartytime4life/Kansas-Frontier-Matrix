---
title: "💧 Kansas Frontier Matrix — Hydrology Legend Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/hydrology/README.md"
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

# 💧 **Kansas Frontier Matrix — Hydrology Legend Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/hydrology/README.md`

**Purpose:**  
Provide a unified index for all **hydrology symbol metadata** used in Focus Mode, Story Nodes, hazard layers, watershed overlays, and STAC-linked hydrologic datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Hydrology-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains the canonical machine-readable metadata for **all hydrologic symbols** used across the Kansas Frontier Matrix (KFM).

Hydrology symbols cover:

- Streamflow and discharge  
- Flood/high-water stage  
- Drought/low-flow indicators  
- Groundwater wells and aquifers  
- Watershed boundaries  
- Hydrologic infrastructure (dams, levees, diversions)  

The metadata here ensures:

- Semantic consistency across visualization layers  
- Proper linkage to SVG/PNG icon assets  
- STAC-compatible hydrologic symbol publishing  
- FAIR+CARE-compliant communication of water-related hazards  
- Reliability across Focus Mode + Story Nodes  

No hydrology symbol is valid unless defined here.

---

### 🗂️ Directory Layout

    hydrology/
    |-- README.md                                # This document
    |-- hydrology-symbols.json                   # Canonical symbol registry
    |-- hydrology-symbols.stac.json              # STAC metadata for SVG/PNG hydrology icons
    |-- hydrology-symbols-story-nodes.json       # Story Node usage + binding rules
    |
    └── examples/                                # Developer metadata examples

---

### 🧱 Hydrology Symbol Registry — `hydrology-symbols.json`

Defines core attributes for each hydrology symbol:

- id  
- category (drought, flood, flow, infrastructure, groundwater)  
- label  
- description  
- svg path  
- optional png path  
- emoji fallback  
- severity class (if applicable)  
- data_mapping  
  - variable (streamflow, gw_level, discharge…)  
  - unit (m³/s, ft³/s, ft, index)  
  - thresholds  

Example (indented):

    {
      "id": "gauge_station",
      "category": "streamflow",
      "label": "River Gauge Station",
      "description": "Monitoring point collecting river stage/discharge data.",
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

### 🧩 STAC Metadata — `hydrology-symbols.stac.json`

STAC metadata defines:

- Legend/symbol asset roles  
- Semantic category linking  
- Descriptive titles  
- FAIR+CARE lineage info  
- Dataset-level environmental metadata  

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

Controls hydrology symbol behavior in Story Nodes:

- Icon badge usage  
- Header vs. timeline placement  
- Emoji fallback  
- Topical contexts (hydrology, hazards, drought, watershed)  
- CARE cultural/environmental sensitivity  

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

### 🧪 Validation & CI Requirements

All hydrology metadata must pass:

- JSON schema validation  
- STAC schema validation  
- File existence checks  
- Story Node usage validation  
- CARE label enforcement  
- Optional snapshot linkage (in symbol test suite)  

Local validation command:

    make test-legends-hydrology

This validates:

- Metadata correctness  
- STAC integration  
- File paths  
- Story Node bindings  
- Snapshot consistency  

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                   |
|----------|------------|---------------|-------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology metadata overview — fully memory-rule compliant.      |
