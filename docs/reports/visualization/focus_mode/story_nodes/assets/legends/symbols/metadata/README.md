---
title: "📘 Kansas Frontier Matrix — Symbol Metadata Directory Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focus-symbols-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Symbol Metadata Directory Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/README.md`

**Purpose:**  
Provide a unified reference for **all symbol metadata directories** used across climate, hydrology, landcover, event, and archaeological symbol systems for Focus Mode Story Nodes and KFM visualization layers.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Symbol%20Registry-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="Compliance" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory acts as the **root index** for all symbol metadata files that govern:

- Focus Mode Story Node symbols  
- Map legend icon metadata  
- STAC asset declarations  
- Category/classification mappings  
- Cultural + ecological safeguards (FAIR+CARE)  
- Visualization consistency across the entire Kansas Frontier Matrix  

All metadata follows:

- KFM Markdown Protocol rules  
- MCP-DL v6.3 strictness  
- Indented JSON examples (no nested fences)  
- Ethical symbol representation standards  
- One-box formatting for GitHub compatibility  

Every symbol in KFM **must** have:

1. An SVG source  
2. Optional PNG derivative  
3. A metadata registry entry  
4. STAC item definition  
5. Story Node usage bindings  
6. Snapshot tests validating visual stability  

---

### 🗂️ Directory Layout

    metadata/
    |-- README.md                                     # This document (directory index)
    |
    |-- climate/                                      # Climate symbol metadata
    |   |-- climate-symbols.json
    |   |-- climate-symbols.stac.json
    |   |-- climate-symbols-story-nodes.json
    |   └── examples/
    |
    |-- hydrology/                                    # Hydrology symbol metadata
    |   |-- hydrology-symbols.json
    |   |-- hydrology-symbols.stac.json
    |   |-- hydrology-symbols-story-nodes.json
    |   └── examples/
    |
    |-- landcover/                                    # Landcover & ecological symbols
    |   |-- landcover-symbols.json
    |   |-- landcover-symbols.stac.json
    |   |-- landcover-symbols-story-nodes.json
    |   └── examples/
    |
    |-- events/                                       # Historical / cultural event symbols
    |   |-- event-symbols.json
    |   |-- event-symbols.stac.json
    |   |-- event-symbols-story-nodes.json
    |   └── examples/
    |
    └── archaeological/                               # Archaeological symbol metadata
        |-- archaeological-symbols.json
        |-- archaeological-symbols.stac.json
        |-- archaeological-symbols-story-nodes.json
        └── examples/

---

### 🧱 Metadata Structure Requirements

Regardless of category, all symbol metadata files MUST define:

- **id** — canonical key  
- **category** — classification (climate, hydrology, landcover, event, etc.)  
- **label** — human-readable name  
- **description** — semantic meaning  
- **svg** — relative path to SVG icon  
- **png** — optional PNG fallback path  
- **emoji** — fallback text glyph  
- **severity or type** — if applicable  
- **data_mapping** (variable, units, thresholds) for scientific symbology  
- **CARE labels** for cultural/ecological sensitivity  
- **storynode rules** for placement and visibility  

Example template (indented, no fenced blocks):

    {
      "id": "<symbol_id>",
      "category": "<domain>",
      "label": "<Human Name>",
      "description": "<Meaning>",
      "svg": "../svg/<symbol_id>.svg",
      "png": "../png/<symbol_id>@2x.png",
      "emoji": "<emoji>",
      "severity": "none",
      "data_mapping": {
        "variable": "<var>",
        "unit": "<unit>",
        "threshold": "<value>"
      },
      "cultural_sensitivity": "public"
    }

---

### 🔗 STAC Integration Requirements

All STAC metadata files (`*-symbols.stac.json`) must:

- Use `roles: ["legend", "symbol"]` for icon assets  
- Provide descriptive titles  
- Link back to KFM collections (e.g., `kfm-legends`)  
- Include FAIR+CARE lineage fields  
- Maintain one-to-one correspondence with registry entries  

Example STAC snippet (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "<legend-id>",
      "collection": "kfm-legends",
      "assets": {
        "<symbol_id>_svg": {
          "href": "../svg/<symbol_id>.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"]
        }
      }
    }

---

### 🧠 Story Node Binding Requirements

Story Node binding metadata controls:

- Badges  
- Header icons  
- Timeline icons  
- Context-sensitive usage  
- Emoji fallback  
- CARE-based visibility restrictions  

Example binding snippet (indented):

    {
      "<symbol_id>": {
        "label": "<Human Name>",
        "badge": true,
        "emoji": "<emoji>",
        "contexts": ["ecology", "history", "climate"],
        "display_rules": {
          "timeline": true,
          "header": false
        }
      }
    }

---

### 🧪 Validation & Testing Requirements

All symbol metadata directories must pass:

- JSON Schema checks  
- STAC schema validation  
- Story Node linkage validation  
- Asset existence validation (SVG/PNG)  
- Snapshot image comparison  
- CARE label compliance checks  

Local test runner (indented):

    make test-legends-all

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                |
|----------|------------|---------------|----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial metadata root index, fully memory-rule compliant.            |