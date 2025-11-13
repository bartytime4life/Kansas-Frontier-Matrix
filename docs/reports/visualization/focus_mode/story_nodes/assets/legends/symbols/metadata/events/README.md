---
title: "📜 Kansas Frontier Matrix — Event Symbol Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/events/README.md"
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

# 📜 **Kansas Frontier Matrix — Event Symbol Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/events/README.md`

**Purpose:**  
Define the machine-readable metadata for **historical, cultural, political, social, and archaeological event symbols** used across Focus Mode, Story Nodes, map legends, and STAC-linked event datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Events-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains authoritative metadata definitions for **event symbols**, ensuring consistent classification and ethically responsible representation of:

- Treaties & political agreements  
- Migrations & population movements  
- Conflicts & confrontations  
- Cultural gatherings & ceremonies  
- Exploration routes & expeditions  
- Settlement formation  
- Archaeological discoveries  
- Historic infrastructure events  

Event metadata governs:

- Symbol IDs  
- Categories & semantic domains  
- Cultural sensitivity & CARE labels  
- Story Node usage rules  
- STAC Item asset definitions  
- Legend placement & meaning  
- Narrative-injection (`{symbol:id}`) behavior  

No event symbol may appear anywhere in KFM without being defined in these metadata files.

---

### 🗂️ Directory Layout

    events/
    |-- README.md                                # This document
    |-- event-symbols.json                       # Canonical event symbol registry
    |-- event-symbols.stac.json                  # STAC metadata for legend/symbol assets
    |-- event-symbols-story-nodes.json           # Story Node usage & binding rules
    |
    └── examples/                                # Developer-ready metadata examples

---

### 🧱 Event Symbol Registry — `event-symbols.json`

Defines per-symbol canonical metadata:

- id  
- category (treaty, conflict, migration, ceremony, archaeological, etc.)  
- label  
- description  
- svg path  
- optional png path  
- emoji fallback  
- event_type (ontology-linked classification)  
- temporal_precision (day, month, year, approx, uncertain)  
- cultural_sensitivity (public / restricted / sacred)  
- CARE compliance flags  

Example (indented):

    {
      "id": "treaty_marker",
      "category": "treaty",
      "label": "Treaty / Agreement",
      "description": "Formal treaty or agreement event.",
      "svg": "../svg/treaty_marker.svg",
      "emoji": "📜",
      "event_type": "treaty",
      "temporal_precision": "day",
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `event-symbols.stac.json`

Enables external cataloging through STAC 1.0.

STAC metadata defines:

- Item structure  
- Asset declarations  
- Legend/symbol roles  
- Metadata lineage  
- CARE-compliant context fields  

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
          "title": "Migration Path Symbol"
        }
      }
    }

---

### 🧠 Story Node Bindings — `event-symbols-story-nodes.json`

Controls how event symbols appear inside Story Nodes:

- header badge  
- timeline marker  
- narrative-level symbolic embeds  
- emoji fallbacks  
- event-type specific contexts  
- CARE-based visibility rules  

Example (indented):

    {
      "conflict_event": {
        "label": "Conflict Event",
        "badge": true,
        "emoji": "⚔️",
        "contexts": ["history", "political"],
        "cultural_sensitivity": "review"
      }
    }

---

### 🧪 Validation & CI

All event metadata undergoes:

- JSON schema validation  
- STAC schema compliance  
- SVG/PNG asset existence checks  
- Story Node linkage validation  
- CARE label compliance audits  
- Optional snapshot linkage checks  

Local test runner (indented):

    make test-legends-events

CI will block merges if any metadata is missing, invalid, or culturally noncompliant.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                |
|----------|------------|---------------|----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial event metadata overview, fully memory-rule compliant.        |