---
title: "🧩 Kansas Frontier Matrix — Climate Symbol Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/metadata/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Climate Symbol Metadata Specification**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/metadata/README.md`

**Purpose:**  
Define the canonical machine-readable metadata structures powering climate symbols in Focus Mode, Story Nodes, STAC assets, and analytical workflows.

<img alt="MCP Docs" src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img alt="Metadata Schema" src="https://img.shields.io/badge/Metadata-Climate%20Symbols-purple" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img alt="STAC Linked" src="https://img.shields.io/badge/STAC-1.0%20Aligned-teal" />

</div>


---

## 📚 Overview

This directory contains the **authoritative metadata** that governs all climate symbols used across the Kansas Frontier Matrix (KFM).  
These files define:

- Canonical symbol IDs  
- Variable mappings (tas_anom, prcp, spi, pdsiextr, etc.)  
- Severity thresholds  
- STAC asset declarations  
- Story Node usage rules  
- FAIR+CARE lineage and governance  

No symbol may appear in the UI, Focus Mode, Story Nodes, or reports unless it is defined here.

---

### 🗂️ Directory Layout

    metadata/
    |-- README.md                        # This document
    |-- climate-symbols.json             # Primary climate symbol registry
    |-- climate-symbols.stac.json        # STAC metadata for symbol/legend assets
    |-- climate-symbols-story-nodes.json # Story Node usage bindings
    |
    └── examples/                        # Developer metadata examples

---

### 🧱 Climate Symbol Registry (`climate-symbols.json`)

Defines:

- id  
- category  
- label  
- description  
- svg (relative path)  
- emoji fallback  
- severity  
- data_mapping  
  - variable  
  - unit  
  - min/max thresholds  

Example entry (INDENTED, not fenced):

    {
      "id": "drought_extreme",
      "category": "drought",
      "label": "Extreme Drought",
      "description": "USDM D4 or equivalent PDSI threshold.",
      "svg": "../svg/drought_extreme.svg",
      "emoji": "🟥",
      "severity": "extreme",
      "data_mapping": {
        "variable": "pdsiextr",
        "unit": "index",
        "min": -6
      }
    }

---

### 🧩 STAC Metadata (`climate-symbols.stac.json`)

Defines how climate symbols are published as STAC Items.

Example:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-climate-v1",
      "collection": "kfm-legends",
      "assets": {
        "flood_major_svg": {
          "href": "../svg/flood_major.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Major Flood Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings (`climate-symbols-story-nodes.json`)

Defines how symbols appear inside Story Nodes:

- badge placement  
- emoji fallback  
- recommended discipline contexts  
- label strings  

Example:

    {
      "drought_extreme": {
        "label": "Extreme Drought",
        "badge": true,
        "emoji": "🟥",
        "contexts": ["hydrology", "climatology"]
      }
    }

---

### 🧪 Validation & CI

This directory is validated through:

- JSON Schema  
- STAC schema conformance  
- File path verification  
- Visual snapshot regression  

Local helper:

    make test-legends-climate

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                              |
|----------|------------|---------------|----------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Fully memory-compliant metadata README.            |