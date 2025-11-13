---
title: "🎨 Kansas Frontier Matrix — Landcover Symbol SVG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/svg/README.md"
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

# 🎨 **Kansas Frontier Matrix — Landcover Symbol SVG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/svg/README.md`

**Purpose:**  
Define the canonical vector icon set representing landcover classes for Focus Mode, Story Nodes, ecological overlays, timelines, and all map legend layers across the Kansas Frontier Matrix (KFM).

<img alt="SVG Icons" src="https://img.shields.io/badge/Assets-Landcover%20SVG%20Icons-green" />
<img alt="Vector Format" src="https://img.shields.io/badge/Format-Scalable%20Vector-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains the **master SVG icons** for all landcover-related symbols used in KFM.

These icons are the authoritative source for:

- Focus Mode landcover overlays  
- Story Node landcover badges  
- Timeline ecological state indicators  
- Map legend symbols  
- PNG rasterization pipelines  
- STAC-based legend metadata distribution  

All landcover symbols **must** originate from these SVGs.  
Raster/PNG or snapshot versions are derived from these icons only.

---

### 🗂️ Directory Layout

    svg/
    |-- README.md                        # This document
    |-- grassland_icon.svg               # General grassland
    |-- woodland_icon.svg                # Woodland / forest
    |-- cropland_icon.svg                # Agriculture / cropland
    |-- wetland_icon.svg                 # Wetlands
    |-- shrubland_icon.svg               # Shrubland / savanna-shrub
    |-- urban_builtup.svg                # Urban/built environment
    |-- prairie_tallgrass.svg            # Tallgrass prairie
    |-- prairie_mixedgrass.svg           # Mixed-grass prairie
    |
    └── ...                               # Additional landcover SVG icons

---

## 🎨 SVG Design Requirements

SVGs must follow strict visual, ecological, and metadata rules to ensure consistent, accessible, FAIR+CARE-compliant representation of landcover categories.

### 🧱 Artboard Standards

- Square artboard (32×32 or 64×64 units recommended).  
- Consistent internal padding across the landcover icon set.  
- Centered glyphs for consistent map-marker alignment.  

### 🌿 Category Shape Language

**Grassland & Prairie**  
Shapes: blade clusters, tufts, prairie silhouettes  
Colors: natural greens/yellows

**Woodland / Forest**  
Shapes: canopy silhouettes, tree crowns  
Colors: deep/mid greens

**Shrubland**  
Shapes: rounded shrub clusters  
Colors: muted greens, olives

**Cropland / Agriculture**  
Shapes: row patterns, tilled textures  
Colors: earthy browns/beiges

**Wetlands**  
Shapes: cattail/marsh elements with water indicators  
Colors: blue-teal/green hybrids

**Urban & Infrastructure**  
Shapes: block/rectilinear forms  
Colors: grays, neutrals

### 🌈 Color & Accessibility

- Landcover palette must remain consistent and contrast-friendly.  
- No “good/bad ecology” symbolism (FAIR+CARE rule).  
- Must pass **WCAG 2.1 AA** contrast checks.  
- Icons must remain recognizable in monochrome and reduced contrast environments.

### 🧼 SVG Markup Hygiene

- Remove editor metadata (Inkscape/Illustrator tags).  
- Avoid filters, masks, raster-embedded objects.  
- Use clean `<path>`, `<circle>`, `<polygon>`, `<rect>` elements.  
- Keep file size minimal for web performance and mobile rendering.

---

## 🔗 Metadata Integration

SVG filenames correspond directly to entries in:

- `../metadata/landcover-symbols.json`  
- `../metadata/landcover-symbols.stac.json`  
- `../metadata/landcover-symbols-story-nodes.json`  

Example (indented for readability):

    {
      "id": "woodland_icon",
      "category": "woodland",
      "label": "Woodland",
      "svg": "../svg/woodland_icon.svg",
      "emoji": "🌲",
      "landcover_type": "NLCD_41"
    }

Story Nodes and Focus Mode **do not** reference filenames directly — they use metadata keys that resolve to these SVG assets.

---

## 🧪 Validation & Quality Assurance

All landcover SVGs are validated through the legend test suite.

Validation includes:

- **XML/SVG linting**  
- **Asset linkage tests** (metadata → file existence)  
- **Visual regression** using snapshot baselines  
- **STAC metadata validation**  
- **CARE/ecological neutrality** checks  

Workflow (indented):

    1. Add or modify SVG in svg/
    2. Update metadata registry entries
    3. Run `make test-legends-landcover`
    4. Confirm previews & snapshots match expectations
    5. Commit SVG + metadata + snapshot updates together

Any SVG failing tests must be fixed before merging.

---

## 🕒 Version History

| Version  | Date       | Author        | Notes                                                               |
|----------|------------|---------------|---------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover SVG asset README, fully memory-rule compliant.    |