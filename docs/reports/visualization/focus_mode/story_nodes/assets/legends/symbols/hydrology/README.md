---
title: "💧 Kansas Frontier Matrix — Hydrology Symbol Legend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Hydrology Symbol Legend Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/README.md`

**Purpose:**  
Define the canonical hydrology symbol system for Focus Mode, Story Nodes, map legends, and STAC-linked hydrologic datasets across the Kansas Frontier Matrix (KFM).

<img alt="Legend Type" src="https://img.shields.io/badge/Legend-Symbols%20·%20Hydrology-blue" />
<img alt="Hydrology" src="https://img.shields.io/badge/Domain-Hydrology%20%2F%20Water%20Systems-teal" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Verified-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

Hydrology symbols represent **water-related processes, conditions, hazards, and infrastructure** across KFM, supporting:

- Focus Mode river- and watershed-specific overlays  
- Story Node badges for hydrologic events  
- Timeline hydrology indicators  
- MapLibre hydrology symbol layers  
- STAC-aligned hydrologic metadata publishing  
- FAIR+CARE-compliant environmental communication  

Hydrology symbols include:

- Streamflow, discharge, and gauge readings  
- Drought and low-flow markers  
- Flood stage, inundation markers, and stream peak events  
- Groundwater wells and aquifer indicators  
- Watershed boundaries and hydrologic units  
- Water infrastructure (dams, levees, diversions)  

Symbols must be:

- Shape-distinct  
- Color-consistent  
- Accessible  
- Respectful, neutral, non-alarmist  
- Tightly governed under metadata + STAC standards  

---

### 🗂️ Directory Layout

    hydrology/
    |-- README.md                        # This document
    |
    |-- svg/                             # Canonical hydrology SVG icons
    |   |-- well_marker.svg
    |   |-- flood_highwater.svg
    |   |-- drought_lowflow.svg
    |   |-- gauge_station.svg
    |   |-- watershed_outline.svg
    |   |-- dam_structure.svg
    |   |-- levee_marker.svg
    |   |-- discharge_peak.svg
    |
    |-- png/                             # Raster fallback versions
    |   |-- well_marker@2x.png
    |   |-- flood_highwater@2x.png
    |   |-- drought_lowflow@2x.png
    |   |-- gauge_station@2x.png
    |   |-- watershed_outline@2x.png
    |   |-- dam_structure@2x.png
    |   |-- levee_marker@2x.png
    |   |-- discharge_peak@2x.png
    |
    |-- metadata/                        # Machine-readable metadata definitions
    |   |-- hydrology-symbols.json
    |   |-- hydrology-symbols.stac.json
    |   |-- hydrology-symbols-story-nodes.json
    |
    └── tests/                           # Validation + visual regression tests
        |-- snapshots/
        |-- validate_metadata.py
        |-- generate_previews.py

---

### 💧 Hydrology Symbol Categories & Semantics

Each symbol has defined:

- A **semantic ID**  
- A category (e.g., discharge, flood, drought, groundwater)  
- A glyph (SVG icon)  
- Severity or stage (if applicable)  
- Data mapping (variable, units, thresholds)  
- Story Node usage rules  

### **Streamflow & Discharge Symbols**

Represent real-time or historical streamflow.

- **`discharge_peak`** — Peak discharge events  
- **`gauge_station`** — River gauge locations  
- **`flow_normal`** — Baseline or normalized flow  

Color palette: blues, teals  
Shape language: wave, arrows, flow lines  

### **Drought & Low Water**

- **`drought_lowflow`** — Critically low stream discharge  
- **`water_deficit`** — Combined hydrologic drought indicators  

Color palette: brown, amber  
Shapes: v-shaped low-flow glyphs or cracked-water icons  

### **Flood & Inundation**

- **`flood_highwater`** — Flood stage indicator  
- **`inundation_area`** — Flooded polygon centroid symbol  

Color palette: deep blues  
Shapes: stacked wave glyphs  

### **Groundwater & Aquifers**

- **`well_marker`** — Groundwater well  
- **`aquifer_indicator`** — Aquifer zone marker  

Color palette: turquoise  
Shapes: well profiles, droplet-down arrows  

### **Infrastructure**

- **`dam_structure`** — Dam location  
- **`levee_marker`** — Levee structure marker  
- **`diversion_point`** — Water diversion/canal intake  

Colors: muted grays  
Shapes: structural icon silhouettes  

---

### 🎨 Cartographic & Accessibility Rules

Symbols must remain readable at:

- **32×32 px interactive** map scale  
- **16 pt in print**  

Accessibility:

- Shape + color = required redundancy  
- WCAG 2.1 AA contrast minimum  
- Avoid misleading disaster-themed imagery (FAIR+CARE requirement)  

---

### 🧩 Story Node Integration

Hydrology symbols appear via:

    "Record flooding occurred at the {symbol:flood_highwater} Neosho River gauge..."

Renderer responsibilities:

- Replace `{symbol:...}` with SVG/emoji fallback  
- Add symbol to legend automatically  
- Maintain consistent coloring  
- Log symbol usage for Focus Mode explainability  

---

### 🧱 Metadata Requirements

Hydrology symbol metadata is defined under:

- `hydrology-symbols.json`  
- `hydrology-symbols.stac.json`  
- `hydrology-symbols-story-nodes.json`  

Metadata fields:

- id  
- category  
- label  
- description  
- svg  
- emoji  
- severity level  
- variable + units + thresholds  
- CARE-level tags  

Example metadata entry (indented):

    {
      "id": "flood_highwater",
      "category": "flood",
      "label": "High Water / Flood Stage",
      "svg": "../svg/flood_highwater.svg",
      "emoji": "🌊",
      "severity": "severe",
      "data_mapping": {
        "variable": "streamflow",
        "unit": "m³/s",
        "threshold": "Q > Q100"
      }
    }

---

### 🧪 Validation & CI

Tests enforce:

- Schema validation  
- STAC correctness  
- All SVG/PNG files exist  
- Snapshot visual consistency  
- No orphaned or unreferenced symbols  

Run locally:

    make test-legends-hydrology

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                     |
|----------|------------|---------------|-----------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology symbol legend, fully memory-compliant.  |