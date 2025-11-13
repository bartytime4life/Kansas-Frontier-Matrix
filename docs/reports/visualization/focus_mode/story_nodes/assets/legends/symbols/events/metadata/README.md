---
title: "📜 Kansas Frontier Matrix — Event Symbol Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/metadata/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Event Symbol Metadata Specification**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/metadata/README.md`

**Purpose:**  
Define the canonical machine-readable metadata governing **event symbols** used across Focus Mode, Story Nodes, map legends, and STAC-aligned historical/cultural datasets in the Kansas Frontier Matrix.

<img alt="Event Metadata" src="https://img.shields.io/badge/Metadata-Events-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Schema" src="https://img.shields.io/badge/Schema-STAC%201.0%20Aligned-purple" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

</div>


---

## 📚 Overview

This directory contains the **authoritative metadata definitions** for all *event-related* symbols used inside the Kansas Frontier Matrix (KFM).  
The metadata here ensures:

- Consistent symbol use across Focus Mode & Story Nodes  
- Correct cultural/historical semantics  
- Alignment with FAIR+CARE principles  
- Accurate mappings to historical event categories  
- STAC compliance for external cataloging  
- Reproducible rendering across maps, timelines, and narratives  

Any event symbol not defined in this directory must **not** be used anywhere in KFM.

---

### 🗂️ Directory Layout

    metadata/
    |-- README.md                        # This document
    |-- event-symbols.json               # Canonical event symbol registry
    |-- event-symbols.stac.json          # STAC definitions for event symbols
    |-- event-symbols-story-nodes.json   # Story Node usage rules and bindings
    |
    └── examples/                        # Developer example snippets

---

### 🧱 Event Symbol Registry — `event-symbols.json`

This file defines the canonical fields for each event symbol:

- `id` — unique symbol identifier  
- `category` — treaty, conflict, migration, settlement, cultural, archaeological  
- `label` — display name  
- `description` — narrative meaning  
- `svg` — SVG icon location  
- `emoji` — accessible fallback  
- `cultural_sensitivity` — flags for CARE compliance  
- `event_type` — mapping to KFM historical ontology  
- `temporal_precision` — point, range, approximate, uncertain  

Example entry (indented):

    {
      "id": "treaty_marker",
      "category": "treaty",
      "label": "Treaty / Agreement",
      "description": "Formal treaty or agreement event.",
      "svg": "../svg/treaty_marker.svg",
      "emoji": "📜",
      "event_type": "treaty",
      "temporal_precision": "day",
      "cultural_sensitivity": "review"
    }

---

### 🧩 STAC Metadata — `event-symbols.stac.json`

This file registers event symbols as **STAC Items** or **STAC assets**, ensuring:

- Interoperability with external catalogs  
- FAIR-aligned dataset linking  
- Reproducible metadata lineage  
- Proper `roles: ["legend", "symbol"]` assignment  

Example structure (indented):

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

### 🧠 Story Node Bindings — `event-symbols-story-nodes.json`

This metadata controls how event symbols appear within Story Nodes:

- Whether symbols appear in the **header**, **timeline**, or **context cards**  
- Recommended usage domains (history, archaeology, cultural studies)  
- Fallback emoji usage  
- Sensitivity flags (CARE, community restrictions)  
- Narrative labeling conventions  

Example snippet (indented):

    {
      "migration_path": {
        "label": "Migration Path",
        "emoji": "➡️",
        "badge": true,
        "contexts": ["history", "culture", "movement"],
        "cultural_sensitivity": "public"
      }
    }

---

### 🧪 Validation & CI

Validation rules include:

- Conformance to schema  
- Required fields present  
- All referenced SVG files exist  
- STAC metadata validity  
- CARE label warnings if missing  
- No orphan metadata entries  

Local validation command (shown as indented text):

    make test-legends-events

This runs:

- Metadata schema validation  
- STAC asset validation  
- Snapshot linkage checks  
- Contextual CARE rule validation  

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                     |
|----------|------------|---------------|-----------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial event metadata README following memory rules.     |