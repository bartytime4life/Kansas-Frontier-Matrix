---
title: "📜 Kansas Frontier Matrix — Event Symbol Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/events/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Event Symbol Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/events/examples/README.md`

**Purpose:**  
Provide fully compliant metadata examples for building *event symbol* definitions in Focus Mode, Story Nodes, map legends, and STAC-aligned cultural/historical datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Event%20Metadata-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer-ready** example snippets demonstrating valid metadata formats for:

- Event symbol registry entries  
- STAC legend/symbol metadata  
- Story Node event symbol bindings  

All examples:

- Follow stored KFM Markdown Protocol  
- Use indented JSON samples (no nested code fences)  
- Maintain FAIR+CARE principles for cultural and historical representation  
- Support MCP-DL v6.3 metadata discipline  
- Are GitHub-stable and memory-rule compliant  

Use these examples as templates when adding or modifying event symbol metadata.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                       # This document
    |-- example-event-symbol.json       # Example event registry entry
    |-- example-stac.json               # Example STAC symbol metadata
    |-- example-storynode.json          # Example Story Node event binding

---

### 🧱 Example — Event Symbol Registry Entry

Example metadata for `event-symbols.json`:

    {
      "id": "conflict_event",
      "category": "conflict",
      "label": "Conflict Event",
      "description": "Represents a recorded confrontation, battle, or hostile encounter.",
      "svg": "../svg/conflict_event.svg",
      "emoji": "⚔️",
      "event_type": "battle",
      "temporal_precision": "day",
      "cultural_sensitivity": "review"
    }

---

### 🧩 Example — STAC Legend Metadata

Example entry for `event-symbols.stac.json`:

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-events-v1",
      "collection": "kfm-legends",
      "assets": {
        "treaty_marker_svg": {
          "href": "../svg/treaty_marker.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Treaty / Agreement Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example for `event-symbols-story-nodes.json`:

    {
      "migration_path": {
        "label": "Migration Path",
        "badge": true,
        "emoji": "➡️",
        "contexts": ["history", "movement", "culture"],
        "display_rules": {
          "timeline": true,
          "header": false
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                             |
|----------|------------|---------------|-------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial event metadata examples README, fully memory compliant.    |
