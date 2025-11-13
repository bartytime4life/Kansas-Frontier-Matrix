---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/archaeological/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-archaeological-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeological Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/archaeological/examples/README.md`

**Purpose:**  
Provide fully memory-rule-compliant example metadata entries for archaeological symbols used in Focus Mode, Story Nodes, map legends, and STAC-integrated cultural heritage datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Archaeological%20Metadata-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Required-gold" />
<img alt="Developer Ready" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer-ready example snippets** demonstrating correct metadata formatting for:

- Archaeological symbol registry entries  
- STAC legend-symbol metadata  
- Story Node archaeological symbol bindings  

These examples follow:

- KFM Markdown Protocol (one fenced block)  
- No nested code-fences  
- JSON shown as indented examples  
- FAIR+CARE cultural protections  
- MCP-DL metadata discipline  
- GitHub-safe, stable formatting  

Use these examples as a template for creating or updating archaeological symbol metadata.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                            # This document
    |-- example-archaeological-symbol.json   # Example registry entry
    |-- example-stac.json                    # Example STAC-compatible symbol entry
    |-- example-storynode.json               # Example Story Node binding

---

### 🧱 Example — Archaeological Symbol Registry Entry

Example `archaeological-symbols.json` entry (indented):

    {
      "id": "archaeological_discovery",
      "category": "discovery",
      "label": "Archaeological Discovery",
      "description": "Location where material cultural remains were uncovered.",
      "svg": "../svg/archaeological_discovery.svg",
      "emoji": "🏺",
      "archaeological_type": "artifact_find",
      "cultural_sensitivity": "public"
    }

---

### 🧩 Example — STAC Legend Metadata

Example entry for `archaeological-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-archaeological-v1",
      "collection": "kfm-legends",
      "assets": {
        "burial_protected_svg": {
          "href": "../svg/burial_protected.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Protected Burial Area Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example for `archaeological-symbols-story-nodes.json`:

    {
      "burial_protected": {
        "label": "Protected Burial Area",
        "badge": true,
        "emoji": "⚱️",
        "contexts": ["archaeology", "cultural_history"],
        "display_rules": {
          "timeline": true,
          "header": false
        },
        "cultural_sensitivity": "restricted"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                           |
|----------|------------|---------------|---------------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial archaeological metadata examples README, full memory-rule compliance.   |
