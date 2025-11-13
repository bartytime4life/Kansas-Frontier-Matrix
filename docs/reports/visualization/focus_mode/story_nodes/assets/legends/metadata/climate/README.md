---
title: "🌦️ Kansas Frontier Matrix — Climate Legend Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/climate/README.md"
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

# 🌦️ **Kansas Frontier Matrix — Climate Legend Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/climate/README.md`

**Purpose:**  
Serve as the **root index** for all metadata governing climate-related symbols used in Focus Mode, Story Nodes, map legends, analytical overlays, and STAC-exported climate datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Climate-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory provides the **canonical metadata frameworks** for all climate symbol types used throughout the Kansas Frontier Matrix (KFM).  
These include:

- Temperature anomaly icons  
- Precipitation anomaly symbols  
- Snow/ice markers  
- Soil moisture–related glyphs  
- Drought severity indicators  
- Flood & inundation markers  
- Storm, wind, and severe-weather symbols  
- Climate index markers (SPI, PDSI, HWDI, etc.)  

Metadata here ensures:

- Correct climate symbol semantics  
- FAIR+CARE-compliant communication of climate conditions  
- Linkage to SVG/PNG assets  
- Accurate data variable mappings  
- STAC interoperability  
- Consistent symbol use across Focus Mode, Story Nodes, and map legends  

No climate symbol may be used without an entry in this metadata directory.

---

### 🗂️ Directory Layout

    climate/
    |-- README.md                                 # This document (index)
    |-- climate-symbols.json                      # Canonical climate metadata registry
    |-- climate-symbols.stac.json                 # STAC metadata for symbol assets
    |-- climate-symbols-story-nodes.json          # Story Node usage rules
    |
    └── examples/                                 # Developer-ready metadata examples

---

### 🧱 Climate Symbol Registry — `climate-symbols.json`

Each climate symbol definition includes:

- id  
- category (temperature, precipitation, drought, flood, storm, index…)  
- label  
- description  
- svg path  
- optional png path  
- emoji fallback  
- severity class  
- data_mapping:  
  - variable (tas_anom, prcp, spi…)  
  - unit (°C, mm, m³/s, index)  
  - thresholds (min/max)  
- CARE sensitivity tags  

Example (indented):

    {
      "id": "temp_anomaly_cool",
      "category": "temperature",
      "label": "Cool Temperature Anomaly",
      "description": "Negative anomaly relative to long-term temperature baseline.",
      "svg": "../svg/temp_anomaly_cool.svg",
      "emoji": "❄️",
      "severity": "moderate",
      "data_mapping": {
        "variable": "tas_anom",
        "unit": "°C",
        "max": -1.0
      },
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `climate-symbols.stac.json`

Defines STAC Items for publishable climate legend assets:

- Each SVG/PNG asset is assigned legend/symbol roles  
- Metadata includes variable, severity, and climate domain cues  
- Links back to the `kfm-legends` collection  
- FAIR+CARE metadata preserved  

Example (indented):

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

### 🧠 Story Node Bindings — `climate-symbols-story-nodes.json`

Controls climate symbol use inside Story Nodes:

- Header appearance  
- Timeline markers  
- Badge visibility  
- Fallback emoji usage  
- Contextual relevance (hazards, climatology, hydrology)  
- CARE cultural/environmental rules  

Example (indented):

    {
      "precip_heavy": {
        "label": "Heavy Precipitation",
        "badge": true,
        "emoji": "🌧️",
        "contexts": ["climatology", "hazards"],
        "display_rules": {
          "timeline": true,
          "header": true
        }
      }
    }

---

### 🧪 Validation & Compliance

All climate metadata must pass:

- JSON schema validation  
- STAC schema validation  
- SVG/PNG path checks  
- Story Node linkage validity  
- CARE label compliance  
- Optional snapshot linkage when used with visual test suites  

Local validator:

    make test-legends-climate

Ensures all metadata is complete, correct, and safe for merge.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                 |
|----------|------------|---------------|-----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial climate metadata overview, fully memory-rule compliant.       |
