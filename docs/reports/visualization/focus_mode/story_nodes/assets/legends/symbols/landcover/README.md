---
title: "🌾 Kansas Frontier Matrix — Landcover Symbol Legend Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Landcover Symbol Legend Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/README.md`

**Purpose:**  
Define the official KFM landcover symbol system for Focus Mode, Story Nodes, timelines, and map legend overlays, covering vegetation, land use, biome structure, and ecological transitions.

<img alt="Legend Type" src="https://img.shields.io/badge/Legend-Symbols%20·%20Landcover-green" />
<img alt="Ecosystems" src="https://img.shields.io/badge/Domain-Landcover%20%2F%20Ecology-forestgreen" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

Landcover symbols represent persistent or historical **vegetation, land use, surface cover, and ecological structures**.  
They enable:

- Focus Mode ecosystem overlays  
- Story Node landcover classification badges  
- Timelines showing ecological shifts  
- MapLibre landcover symbol layers  
- STAC-linked landcover metadata  
- Ecological/habitat storytelling in Kansas Frontier studies  

Landcover symbols include:

- Grassland types  
- Woodland & forest extent  
- Cropland vs. rangeland  
- Wetland categories  
- Shrubland  
- Built environment markers  
- Prairie vs. tallgrass vs. mixed-grass distinctions  

Landcover legends must be:

- Shape- and color-distinguishable  
- Ecologically neutral (FAIR+CARE)  
- Accessible and non-biased  
- Consistent across reports and timelines  

---

### 🗂️ Directory Layout

    landcover/
    |-- README.md                        # This document
    |
    |-- svg/                             # Canonical landcover SVG icons
    |   |-- grassland_icon.svg
    |   |-- woodland_icon.svg
    |   |-- cropland_icon.svg
    |   |-- wetland_icon.svg
    |   |-- shrubland_icon.svg
    |   |-- urban_builtup.svg
    |   |-- prairie_tallgrass.svg
    |   |-- prairie_mixedgrass.svg
    |
    |-- png/                             # Raster fallbacks
    |   |-- grassland_icon@2x.png
    |   |-- woodland_icon@2x.png
    |   |-- cropland_icon@2x.png
    |   |-- wetland_icon@2x.png
    |   |-- shrubland_icon@2x.png
    |   |-- urban_builtup@2x.png
    |   |-- prairie_tallgrass@2x.png
    |   |-- prairie_mixedgrass@2x.png
    |
    |-- metadata/                        # Machine-readable symbol definitions
    |   |-- landcover-symbols.json
    |   |-- landcover-symbols.stac.json
    |   |-- landcover-symbols-story-nodes.json
    |
    └── tests/                           # Validation + visual regression
        |-- snapshots/
        |-- validate_metadata.py
        |-- generate_previews.py

---

### 🌾 Landcover Symbol Categories & Semantics

Each symbol defines:

- A semantic ID  
- Ecological category  
- SVG glyph  
- Color family  
- Usage rules  
- Optional severity/degree (e.g., canopy closure)  
- Data/variable mapping for STAC and analysis  

### **Grasslands**

Kansas prairie types:

- `grassland_general`  
- `prairie_tallgrass`  
- `prairie_mixedgrass`  
- `prairie_shortgrass`  

Shapes: blade clusters, tufted silhouettes  
Colors: warm or natural greens, yellows  

### **Woodlands & Forest**

- `woodland_icon`  
- `forest_deciduous`  
- `riparian_forest`  

Shapes: tree canopy profiles  
Colors: deeper greens  

### **Shrublands**

- `shrubland_icon`  
- `savanna_shrub`  

Shapes: rounded/bushy forms  
Colors: mid-greens, olive  

### **Cropland & Agriculture**

- `cropland_icon`  
- `rowcrop`  
- `irrigated_field`  

Shapes: structured rows, tilled patterns  
Colors: browns, yellows  

### **Wetlands**

- `wetland_icon`  
- `marsh`  
- `fen_bog`  
- `riparian_wetland`  

Shapes: marsh grass + water shapes  
Colors: teal/blue-green  

### **Urban & Built Environment**

- `urban_builtup`  
- `infrastructure_cluster`  
- `settlement_unit`  

Shapes: blocky, grid-suggestive  
Colors: grays  

---

### 🎨 Cartographic & Accessibility Rules

- Must be readable at:
  - **32×32 px** interactive scale  
  - **16 pt** print scale  
- Use **shape + color** for redundancy  
- Follow ecological neutrality—no symbolic judgment  
- WCAG 2.1 AA contrast minimum  
- No iconographic bias toward “healthy/unhealthy” ecosystems  
- Respect Indigenous ecological knowledge (CARE-aligned)  

---

### 🧩 Story Node Integration

Symbols appear in Story Node narratives via:

    "The region transitioned from {symbol:grassland_icon} tallgrass prairie to cropland by 1890."

Renderer functions:

- Replace `{symbol:id}` with SVG/emoji  
- Register symbols in the map legend  
- Log symbol usage in Focus Mode telemetry  

---

### 🧱 Metadata Requirements

Metadata is defined in:

- `landcover-symbols.json`  
- `landcover-symbols.stac.json`  
- `landcover-symbols-story-nodes.json`  

Metadata fields include:

- id  
- category  
- label  
- description  
- svg path  
- emoji fallback  
- landcover_type  
- optional variable mapping  
- CARE sensitivity  

Example (indented):

    {
      "id": "grassland_icon",
      "category": "grassland",
      "label": "General Grassland",
      "svg": "../svg/grassland_icon.svg",
      "emoji": "🌾",
      "landcover_type": "prg_general"
    }

---

### 🧪 Validation & CI

Checks include:

- JSON schema validation  
- Existence of SVG/PNG assets  
- STAC metadata checks  
- Story Node binding consistency  
- Snapshot visual regression  

Run locally:

    make test-legends-landcover

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                       |
|----------|------------|---------------|-------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover legend README, fully memory-compliant.    |