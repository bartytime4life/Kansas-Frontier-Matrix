---
title: "🌦️ Kansas Frontier Matrix — Climate Symbol Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/climate/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climate Symbol Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/climate/README.md`

**Purpose:**  
Define, document, and govern the metadata schemas that control all **climate-related symbol assets** used in Focus Mode, Story Nodes, reports, interactive visualization, and STAC-linked climate datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Climate-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains all canonical **climate symbol metadata files** that govern:

- Temperature anomaly icons  
- Precipitation & moisture symbols  
- Drought severity icons  
- Flood / inundation symbols  
- Wind, storm, and severe weather markers  
- Composite climate indices (PDSI, SPI, heatwave duration…)  

These metadata structures define:

- Symbol IDs  
- Categories  
- Semantic domain  
- Data variable mappings  
- Severity thresholds  
- Story Node integration rules  
- STAC Item metadata  
- FAIR+CARE governance labels  
- Required ICON → METADATA → STAC linkage  

No climate symbol may be used anywhere in KFM unless it is defined here.

---

### 🗂️ Directory Layout

    climate/
    |-- README.md                                # This document
    |-- climate-symbols.json                     # Canonical climate symbol registry
    |-- climate-symbols.stac.json                # STAC Item metadata for climate symbols
    |-- climate-symbols-story-nodes.json         # Story Node binding + usage rules
    |
    └── examples/                                # Developer-ready metadata snippets

---

### 🧱 Climate Symbol Registry — `climate-symbols.json`

Defines:

- id  
- category (temperature, precipitation, drought, flood, storm, index)  
- label  
- description  
- svg path  
- png path (optional)  
- emoji fallback  
- severity (none / moderate / severe / extreme)  
- data_mapping  
  - variable (tas_anom, prcp, pdsiextr, spi…)  
  - unit (°C, mm, index)  
  - thresholds  
- CARE sensitivity  

Example (indented):

    {
      "id": "temp_anomaly_warm",
      "category": "temperature",
      "label": "Warm Temperature Anomaly",
      "description": "Positive deviation from long-term temperature baseline.",
      "svg": "../svg/temp_anomaly_warm.svg",
      "emoji": "🔥",
      "severity": "moderate",
      "data_mapping": {
        "variable": "tas_anom",
        "unit": "°C",
        "min": 1.0
      },
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `climate-symbols.stac.json`

Ensures that all climate symbols can be published under **STAC 1.0**, enabling external discoverability and standardized metadata inheritance.

Example (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-climate-v1",
      "collection": "kfm-legends",
      "assets": {
        "temp_anomaly_warm_svg": {
          "href": "../svg/temp_anomaly_warm.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Warm Temperature Anomaly Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `climate-symbols-story-nodes.json`

Defines:

- Badge visibility  
- Emoji usage fallback  
- Header/timeline placement  
- Recommended usage contexts  
- Narrative-embedding rules (`{symbol:id}`)  

Example (indented):

    {
      "drought_extreme": {
        "label": "Extreme Drought",
        "badge": true,
        "emoji": "🟥",
        "contexts": ["climatology", "hydrology"],
        "display_rules": {
          "timeline": true,
          "header": true
        }
      }
    }

---

### 🧪 Validation & CI Requirements

All climate metadata must pass:

- JSON Schema validation  
- STAC compliance checks  
- File existence checks (SVG/PNG path integrity)  
- Story Node usage validation  
- FAIR+CARE cultural sensitivity checks  
- Optional snapshot linkage in sibling directories  

Local validation (indented):

    make test-legends-climate

This executes:

- Metadata validation  
- STAC schema validation  
- Story Node binding consistency checks  
- Preview + snapshot regression (when enabled)

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                               |
|----------|------------|---------------|---------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial climate metadata overview, fully memory-rule compliant.     |