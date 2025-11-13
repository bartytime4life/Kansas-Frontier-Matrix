---
title: "📜 Kansas Frontier Matrix — Event Legend Metadata Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/events/examples/README.md"
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

# 📜 **Kansas Frontier Matrix — Event Legend Metadata Examples**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/events/examples/README.md`

**Purpose:**  
Provide fully memory-rule–compliant example metadata templates for defining event symbols used across Focus Mode, Story Nodes, legends, and STAC-published historical/cultural datasets.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Event%20Metadata-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Developer Ready" src="https://img.shields.io/badge/Developer-Ready-blue" />

</div>


---

## 📚 Overview

This directory contains **developer-ready** examples showing correct metadata structure for:

- Event symbol registry definitions  
- STAC Item/asset declarations  
- Story Node usage bindings  

All examples follow:

- KFM Markdown Protocol  
- One fenced block  
- No nested code fences (JSON is indented only)  
- Heading hierarchy: `##` → `###`  
- FAIR+CARE cultural sensitivity rules  
- MCP-DL metadata discipline  

Use these templates to build new event metadata entries cleanly and consistently.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                         # This document
    |-- example-event-symbol.json         # Example registry entry
    |-- example-stac.json                 # Example STAC metadata
    |-- example-storynode.json            # Example Story Node binding

---

### 🧱 Example — Event Symbol Registry Entry

Example structure for `event-symbols.json`:

    {
      "id": "treaty_marker",
      "category": "treaty",
      "label": "Treaty / Agreement",
      "description": "Formal treaty or governmental agreement.",
      "svg": "../svg/treaty_marker.svg",
      "emoji": "📜",
      "event_type": "treaty",
      "temporal_precision": "day",
      "cultural_sensitivity": "public"
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
        "conflict_event_svg": {
          "href": "../svg/conflict_event.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Conflict Event Icon"
        }
      }
    }

---

### 🧠 Example — Story Node Symbol Binding

Example from `event-symbols-story-nodes.json`:

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

| Version  | Date       | Author        | Notes                                                                    |
|----------|------------|---------------|--------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial event metadata examples README — fully memory-rule compliant.    |
