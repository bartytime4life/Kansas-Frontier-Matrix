---
title: "💧 Kansas Frontier Matrix — Hydrology Legend Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/hydrology/examples/README.md"
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

# 💧 **Kansas Frontier Matrix — Hydrology Legend Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/hydrology/examples/README.md`

**Purpose:**  
Provide fully memory-rule–compliant example metadata entries for **hydrology-related legend symbols** used in Focus Mode, Story Nodes, map legends, and STAC-published hydrologic datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Hydrology%20Metadata-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer Ready" src="https://img.shields.io/badge/Developer-Ready-teal" />

</div>


---

## 📚 Overview

This directory contains **developer-ready reference examples** showing proper formatting for:

- Hydrology symbol registry entries  
- STAC legend/symbol assets  
- Story Node hydrology bindings  

All examples follow the stored KFM Markdown Protocol:

- One fenced block  
- Correct heading hierarchy (`##` → `###`)  
- Directory layout at `###`  
- Indented JSON examples (NO nested fences)  
- FAIR+CARE compliance  
- MCP-DL metadata discipline  

Use these templates when adding or modifying hydrologic symbol metadata.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                           # This document
    |-- example-hydrology-symbol.json       # Example registry entry
    |-- example-stac.json                   # Example STAC metadata
    |-- example-storynode.json              # Example Story Node bindings

---

### 🧱 Example — Hydrology Symbol Registry Entry

Example entry for `hydrology-symbols.json`:

    {
      "id": "drought_lowflow",
      "category": "drought",
      "label": "Low Flow / Hydrologic Drought",
      "description": "Indicator of unusually low stream discharge or hydrologic drought conditions.",
      "svg": "../svg/drought_lowflow.svg",
      "emoji": "🟫",
      "severity": "severe",
      "data_mapping": {
        "variable": "streamflow",
        "unit": "m³/s",
        "threshold": "Q < Q10"
      },
      "cultural_sensitivity": "public"
    }

---

### 🧩 Example — STAC Legend Metadata

Example snippet for `hydrology-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-hydrology-v1",
      "collection": "kfm-legends",
      "assets": {
        "drought_lowflow_svg": {
          "href": "../svg/drought_lowflow.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Low Flow Hydrologic Drought Icon"
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
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                    |
|----------|------------|---------------|--------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology legend metadata examples — fully memory-rule compliant. |
