---
title: "📜 Kansas Frontier Matrix — Event Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/metadata/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Event Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/metadata/examples/README.md`

**Purpose:**  
Provide fully compliant example metadata snippets for developers creating or extending **event symbol metadata** for Focus Mode, Story Nodes, and STAC-exported datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Event%20Metadata-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Required-gold" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

</div>


---

## 📚 Overview

This directory includes **developer-ready metadata examples** showing the correct structure for:

- Event symbol registry entries  
- STAC symbol metadata  
- Story Node event symbol bindings  

All examples follow:

- Stored KFM Markdown Memory Rules  
- MCP-DL v6.3 compliance  
- FAIR+CARE cultural sensitivity principles  
- Strict indentation (no nested code fences)  
- GitHub-stable formatting  
- One-block markdown rules  

Use these examples as templates when adding new *historical*, *cultural*, *political*, or *archaeological* event symbols.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                    # This document
    |-- example-event-symbol.json    # Example event registry entry
    |-- example-stac.json            # Example STAC metadata entry
    |-- example-storynode.json       # Example Story Node symbol binding

---

### 🧱 Example — Event Symbol Registry Entry

Shows correct formatting for `event-symbols.json`.

    {
      "id": "ceremony_marker",
      "category": "ceremony",
      "label": "Ceremonial Event",
      "description": "A ceremonial or cultural gathering of significance.",
      "svg": "../svg/ceremony_marker.svg",
      "emoji": "🕊️",
      "cultural_sensitivity": "review",
      "event_type": "ceremony",
      "temporal_precision": "day"
    }

---

### 🧩 Example — STAC Legend Asset

Illustrates how event symbols appear in the STAC metadata file.

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-events-v1",
      "collection": "kfm-legends",
      "assets": {
        "ceremony_marker_svg": {
          "href": "../svg/ceremony_marker.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Ceremonial Event Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Event Symbol Binding

Defines how a symbol integrates into Story Node rendering.

    {
      "ceremony_marker": {
        "label": "Ceremonial Event",
        "badge": true,
        "emoji": "🕊️",
        "contexts": ["culture", "community"],
        "cultural_sensitivity": "review"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                       |
|----------|------------|---------------|-------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial examples README, fully memory-rule compliant.       |