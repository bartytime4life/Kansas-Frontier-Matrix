---
title: "📜 Kansas Frontier Matrix — Event Symbol Legend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Event Symbol Legend Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/README.md`

**Purpose:**  
Define the canonical visual symbol system for **historical, cultural, political, and archaeological events** used in Focus Mode Story Nodes, map legends, timelines, and narrative overlays across the KFM system.

<img alt="Legend Type" src="https://img.shields.io/badge/Legend-Symbols%20·%20Events-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Verified-gold" />
<img alt="Schema" src="https://img.shields.io/badge/Metadata-STAC%201.0%20Aligned-purple" />
<img alt="License" src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

</div>


---

## 📚 Overview

Event symbols provide a consistent, FAIR+CARE-aligned iconography describing major **historic, cultural, and human-driven events** within the Kansas Frontier Matrix (KFM).  

They support:

- Story Node event classification  
- Focus Mode contextual event overlays  
- Timeline event markers  
- MapLibre map symbol layers  
- STAC-linked event legend definitions  
- Accessible visual representation of cultural + historical data  

Event symbols must be:

- Shape-distinct across categories  
- Color-consistent with event classes  
- Meaningful without exaggeration or harm  
- Reproducible, versioned, and validated  
- Respectful of Indigenous data sovereignty and cultural sensitivity  

---

### 🗂️ Directory Layout

    events/
    |-- README.md                        # This document
    |
    |-- svg/                             # Master vector icons for event symbols
    |   |-- treaty_marker.svg
    |   |-- conflict_event.svg
    |   |-- migration_path.svg
    |   |-- settlement_marker.svg
    |   |-- cultural_site.svg
    |   |-- archaeological_discovery.svg
    |   |-- ceremony_marker.svg
    |   |-- exploration_route.svg
    |
    |-- png/                             # Raster fallback versions
    |   |-- treaty_marker@2x.png
    |   |-- conflict_event@2x.png
    |   |-- migration_path@2x.png
    |   |-- settlement_marker@2x.png
    |   |-- cultural_site@2x.png
    |   |-- archaeological_discovery@2x.png
    |   |-- ceremony_marker@2x.png
    |   |-- exploration_route@2x.png
    |
    |-- metadata/                        # Machine-readable metadata definitions
    |   |-- event-symbols.json
    |   |-- event-symbols.stac.json
    |   |-- event-symbols-story-nodes.json
    |
    └── tests/                           # Validation + visual regression tests
        |-- snapshots/
        |-- validate_metadata.py
        |-- generate_previews.py

---

### 🧱 Event Symbol Categories & Semantics

Event symbols represent narrative categories used across KFM’s Story Node system.  
Each symbol has:

- A **semantic ID**  
- A **glyph** (SVG)  
- A **category** (treaty, conflict, migration…)  
- **Severity or significance class** (if applicable)  
- **Data linkage** (event type, time, ontology link)  
- **Usage rules** for Story Nodes + Focus Mode  

### Treaty & Agreement Events  
Used for formal negotiations, agreements, and treaties.

Colors: neutral blues and teals  
Shape language: documents, ribbons, seals  

Example (indented JSON-style for readability):

    {
      "id": "treaty_marker",
      "category": "treaty",
      "label": "Treaty / Agreement",
      "svg": "svg/treaty_marker.svg"
    }

### Migration & Movement Events  
Represents population movement, trade routes, relocation paths, etc.

Colors: earthy oranges  
Shapes: arrows, path-line glyphs  

### Conflict & Hostile Events  
Represents battles, confrontations, and violent events.

Colors: reserved caution palette  
Shapes: angular, but **non-sensational** (FAIR+CARE rule)  

### Settlement & Community Formation  
Founding of towns, homesteads, missions, fort sites, etc.

Colors: greens / browns  
Shapes: simple structure or pin glyph  

### Cultural & Ceremonial Events  
Ceremonies, gatherings, festivals, religious or cultural markers.

Colors: purples and warm tones  
Shapes: symmetric, circle-based  

### Archaeological & Discovery Events  
Dig sites, artifact finds, historic material discovery.

Colors: stone/earth neutrals  
Shapes: trowel, collection bag, artifact silhouette  

---

### 🎨 Cartographic & Accessibility Rules

- Distinct shapes per event category  
- Pair shape + color + label (no color-only meaning)  
- WCAG 2.1 AA contrast minimum  
- Icons readable at:
  - 32×32 px interactive  
  - 16 pt print export  
- Avoid harmful / sensational imagery  
- Event severity (if used) must be stylistic (size, stroke), not fear-based  
- Cultural respect rules:
  - Indigenous ceremonial events use neutral respectful glyphs  
  - No depiction of sacred objects without approval  
  - Follow CARE + Local Protocols for event representation  

---

### 🧩 Story Node Integration

Event symbols appear in Story Nodes via the same lightweight syntax used for other legends:

    "In 1854, the {symbol:treaty_marker} Kansas–Nebraska Act reshaped the territorial boundaries..."

Renderer responsibilities:

- Auto-replace `{symbol:event_id}` with SVG/emoji  
- Add the symbol to the map legend  
- Maintain event category coloring  
- Log symbol usage in Focus Mode telemetry  

---

### 🧱 Metadata Requirements

Event symbol metadata is defined in:

- `event-symbols.json`  
- `event-symbols.stac.json`  
- `event-symbols-story-nodes.json`  

Metadata fields include:

- `id`, `category`, `label`, `description`  
- `svg`, `emoji` fallback  
- `event_type` mappings  
- `temporal_precision`  
- `cultural_sensitivity` flags  
- `CARE_label` tags (public / restricted / sensitive)  

Example metadata snippet:

    {
      "id": "migration_path",
      "category": "migration",
      "label": "Migration Path",
      "svg": "svg/migration_path.svg",
      "emoji": "➡️",
      "event_type": "population_movement",
      "temporal_precision": "range"
    }

---

### 🧪 Validation & CI

Validation includes:

- Metadata schema checks  
- Required-field enforcement  
- SVG/PNG file existence  
- STAC Item correctness  
- Snapshot comparison  
- CARE label enforcement  
- Telemetry link validation  

Local test runner:

    make test-legends-events

---

### 🕒 Version History

| Version | Date       | Author        | Notes                                                   |
|---------|------------|---------------|---------------------------------------------------------|
| v10.2.3 | 2025-11-13 | KFM Docs AI   | Initial event symbol legend README, memory-compliant.   |