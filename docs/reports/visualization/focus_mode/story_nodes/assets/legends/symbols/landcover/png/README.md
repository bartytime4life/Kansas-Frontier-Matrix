---
title: "🖼️ Kansas Frontier Matrix — Landcover Symbol PNG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/png/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Landcover Symbol PNG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/png/README.md`

**Purpose:**  
Document the raster-based PNG assets derived from canonical Landcover SVG icons, used for static exports, backward compatibility, thumbnails, and non-SVG pipelines.

<img alt="PNG Icons" src="https://img.shields.io/badge/Assets-Landcover%20PNG%20Icons-green" />
<img alt="Resolution" src="https://img.shields.io/badge/High%20DPI-@2x-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains **PNG derivatives** of landcover symbol SVGs.  
These files support:

- Static visualization exports (PNG, PDF, TIFF)  
- Systems that lack SVG rendering support  
- Quick-loading thumbnails or sprite sheets  
- Backup formats in offline or lightweight environments  

PNG icons must **always** be regenerated from the SVG masters in:

- `../svg/`  
- And referenced through metadata in `../metadata/`

The PNG set must always mirror:

- Naming  
- Color  
- Geometry  
- Semantic meaning  

No “PNG-only” variants or stylistic deviations are permitted.

---

### 🗂️ Directory Layout

    png/
    |-- README.md                        # This document
    |-- grassland_icon@2x.png            # Grassland landcover
    |-- woodland_icon@2x.png             # Woodland / forest
    |-- cropland_icon@2x.png             # Cropland/agricultural land
    |-- wetland_icon@2x.png              # Wetlands
    |-- shrubland_icon@2x.png            # Shrubland / savanna-shrub
    |-- urban_builtup@2x.png             # Built environment
    |-- prairie_tallgrass@2x.png         # Tallgrass prairie
    |-- prairie_mixedgrass@2x.png        # Mixed-grass prairie
    |
    └── ...                              # Additional landcover PNGs

---

### 🧱 PNG Asset Requirements

PNG assets must follow these rules:

- **Resolution**  
  - Minimum high DPI (2× scaling)  
  - Example: 64×64 px PNG for a 32×32 rendered symbol  

- **Background**  
  - Transparent alpha layer (no opaque background)  

- **Naming**  
  - Matches SVG filename + `@2x` suffix  
  - Example:  
        grassland_icon.svg → grassland_icon@2x.png  

- **Visual Consistency**  
  - Identical geometry and colors to SVG source  
  - No artifacts from raster export  
  - No stylistic differences between SVG and PNG  

- **Ethical + Ecological Neutrality**  
  - No “good/bad” vegetation imagery  
  - Avoid degradation icons unless explicitly an ecological state indicator  
  - Align with FAIR+CARE ecological representation rules  

---

### 🔗 Metadata Linkage & Usage

Landcover symbol metadata files define how PNGs are referenced:

- `landcover-symbols.json`  
- `landcover-symbols.stac.json`  
- `landcover-symbols-story-nodes.json`  

Example mapping (indented):

    {
      "id": "prairie_tallgrass",
      "category": "grassland",
      "label": "Tallgrass Prairie",
      "svg": "../svg/prairie_tallgrass.svg",
      "png": "../png/prairie_tallgrass@2x.png",
      "emoji": "🌾"
    }

Renderers and pipelines should always resolve PNG paths indirectly via metadata.

---

### 🧪 Validation & QA

PNG asset checks validate:

- File existence and alignment with metadata  
- Correct transparent background  
- Pixel-perfect match to snapshot baselines (in `../tests/snapshots/`)  
- Correct naming conventions  
- Regeneration from current SVGs (no stale PNGs)  

Example CI result (indented):

    [OK] grassland_icon@2x.png matches baseline  
    [DIFF] wetland_icon@2x.png differs — review required  

Local validation:

    make test-legends-landcover

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                          |
|----------|------------|---------------|----------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover PNG symbol README, memory-rule compliant.    |