---
title: "🌦️ Kansas Frontier Matrix — Climate Legend Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/climate/examples/README.md"
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

# 🌦️ **Kansas Frontier Matrix — Climate Legend Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/climate/examples/README.md`

**Purpose:**  
Provide fully compliant, developer-ready climate metadata examples for symbol registry entries, STAC lexicon structures, and Story Node bindings.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Climate%20Metadata-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer Ready" src="https://img.shields.io/badge/Developer-Ready-teal" />

</div>


---

## 📚 Overview

This directory contains **reference example snippets** demonstrating the correct formatting of:

- Climate symbol registry entries  
- STAC legend/symbol declarations  
- Story Node climate symbol bindings  

All examples:

- Use **one single fenced block**  
- Use **indented JSON** (never nested code blocks)  
- Follow heading hierarchy: `##` → `###`  
- Place directory layout under `###`  
- Maintain FAIR+CARE cultural and environmental communication standards  
- Follow MCP-DL v6.3 metadata discipline  

Use these templates when adding or updating climate-related symbol metadata.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                          # This document
    |-- example-climate-symbol.json        # Example symbol registry entry
    |-- example-stac.json                  # Example STAC item
    |-- example-storynode.json             # Example Story Node binding

---

### 🧱 Example — Climate Symbol Registry Entry

    {
      "id": "heat_extreme",
      "category": "temperature",
      "label": "Extreme Heat",
      "description": "Temperature well above climatological norms.",
      "svg": "../svg/heat_extreme.svg",
      "emoji": "🔥",
      "severity": "extreme",
      "data_mapping": {
        "variable": "tas_anom",
        "unit": "°C",
        "min": 4
      },
      "cultural_sensitivity": "public"
    }

---

### 🧩 Example — STAC Legend Metadata

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
          "title": "Extreme Heat Symbol"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

    {
      "precip_heavy": {
        "label": "Heavy Precipitation",
        "badge": true,
        "emoji": "🌧️",
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

| Version  | Date       | Author        | Notes                                                                    |
|----------|------------|---------------|--------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial climate metadata examples README — fully memory-rule compliant.  |
