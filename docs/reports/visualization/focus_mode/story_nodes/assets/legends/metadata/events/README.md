---
title: "📜 Kansas Frontier Matrix — Event Legend Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/events/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Event Legend Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/events/README.md`

**Purpose:**  
Provide the authoritative metadata index for all **event-related symbols** used across Focus Mode, Story Nodes, map legends, and STAC-linked historical/cultural datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Events-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains the **canonical metadata definitions** governing all *event symbols*, used to represent:

- Treaties & agreements  
- Cultural gatherings & ceremonies  
- Conflicts & confrontations  
- Migration & movement routes  
- Historic settlements  
- Archaeological discoveries  
- Political or territorial changes  
- Exploration routes and expeditions  

Metadata defined here ensures:

- Consistent symbolic meaning  
- FAIR+CARE cultural sensitivity  
- Clean SVG/PNG linkage  
- Story Node integration consistency  
- STAC metadata interoperability  
- Semantic harmonization across all visualization layers  

No event symbol may appear within KFM unless its metadata is defined here.

---

### 🗂️ Directory Layout

    events/
    |-- README.md                               # This document (index)
    |-- event-symbols.json                      # Canonical event metadata registry
    |-- event-symbols.stac.json                 # STAC-linked metadata
    |-- event-symbols-story-nodes.json          # Story Node usage + binding rules
    |
    └── examples/                               # Developer metadata examples

---

### 🧱 Event Symbol Registry — `event-symbols.json`

Defines per-symbol fields, including:

- id  
- category (treaty, conflict, migration, ceremony, archaeology…)  
- label  
- description  
- svg  
- optional png  
- emoji fallback  
- event_type classification  
- temporal_precision  
- cultural_sensitivity (public/restricted/sacred)  
- CARE metadata mapping  

Example (indented):

    {
      "id": "ceremony_marker",
      "category": "ceremony",
      "label": "Ceremonial Event",
      "description": "Represents a cultural gathering, ritual, or traditional event.",
      "svg": "../svg/ceremony_marker.svg",
      "emoji": "🕊️",
      "event_type": "ceremony",
      "temporal_precision": "day",
      "cultural_sensitivity": "review"
    }

---

### 🧩 STAC Metadata — `event-symbols.stac.json`

Defines STAC Items/Assets for symbol publishing, ensuring:

- External discoverability  
- Cultural/ethical lineage  
- FAIR+CARE fields  
- Roles such as `legend` and `symbol`  
- Synchronization with registry entries  

Example (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-events-v1",
      "collection": "kfm-legends",
      "assets": {
        "migration_path_svg": {
          "href": "../svg/migration_path.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Migration Path Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `event-symbols-story-nodes.json`

Controls how event symbols are used within Story Nodes:

- Whether the symbol appears in the header or timeline  
- Badge behavior  
- Contextual categorization  
- Emoji fallback  
- CARE restrictions for sensitive event types  
- Domain-specific placement rules  

Example (indented):

    {
      "treaty_marker": {
        "label": "Treaty / Agreement",
        "badge": true,
        "emoji": "📜",
        "contexts": ["history", "culture", "political"],
        "display_rules": {
          "timeline": true,
          "header": true
        },
        "cultural_sensitivity": "public"
      }
    }

---

### 🧪 Validation & Compliance

All event metadata must pass:

- JSON Schema checks  
- STAC validation  
- File-existence checks (SVG/PNG)  
- Story Node linkage validation  
- CARE cultural sensitivity compliance  
- Optional snapshot linkage, depending on test configuration  

Local validator:

    make test-legends-events

The CI workflow blocks merge until all checks pass.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                      |
|----------|------------|---------------|----------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial event metadata overview — fully memory-rule compliant.             |
