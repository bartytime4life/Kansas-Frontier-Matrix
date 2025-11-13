---
title: "🏺 Kansas Frontier Matrix — Archaeological Legend Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/archaeological/examples/README.md"
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

# 🏺 **Kansas Frontier Matrix — Archaeological Legend Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/archaeological/examples/README.md`

**Purpose:**  
Provide fully memory-rule–compliant metadata examples for archaeological legend symbols used in Story Nodes, Focus Mode visualization, map legends, and STAC-exported heritage datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Archaeology-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Required-gold" />
<img alt="Dev Ready" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer-ready** example snippets demonstrating the correct structure of:

- Archaeological symbol registry metadata  
- STAC symbol asset metadata  
- Story Node binding definitions  

All examples follow stored memory rules:

- **One fenced block**
- **No nested code blocks**
- **Indented JSON examples only**  
- **Correct heading hierarchy (## > ###)**  
- **Directory layout always under `###`**  
- **Spacing after `</div>` preserved**  
- **FAIR+CARE cultural respect maintained**

Use these examples when creating or modifying archaeological symbol metadata entries.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                            # This document
    |-- example-archaeological-symbol.json   # Example registry entry
    |-- example-stac.json                    # Example STAC metadata
    |-- example-storynode.json               # Example Story Node binding

---

### 🧱 Example — Archaeological Symbol Registry Entry

Valid template for `archaeological-symbols.json`:

    {
      "id": "cultural_site",
      "category": "cultural_site",
      "label": "Cultural Site",
      "description": "Location representing a significant cultural or historic site.",
      "svg": "../svg/cultural_site.svg",
      "emoji": "🏛️",
      "archaeological_type": "cultural_feature",
      "cultural_sensitivity": "review"
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
        "archaeological_discovery_svg": {
          "href": "../svg/archaeological_discovery.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Archaeological Discovery Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example entry from `archaeological-symbols-story-nodes.json`:

    {
      "archaeological_discovery": {
        "label": "Archaeological Discovery",
        "badge": true,
        "emoji": "🏺",
        "contexts": ["archaeology", "history"],
        "display_rules": {
          "timeline": true,
          "header": false
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                 |
|----------|------------|---------------|-----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial archaeological metadata examples README, fully memory-compliant. |
