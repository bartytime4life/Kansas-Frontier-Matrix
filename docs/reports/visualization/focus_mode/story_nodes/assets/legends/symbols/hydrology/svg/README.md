---
title: "🎨 Kansas Frontier Matrix — Hydrology Symbol SVG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/svg/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Hydrology Symbol SVG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/svg/README.md`

**Purpose:**  
Define and govern the canonical vector (SVG) icon set used to represent hydrologic features, hazards, and infrastructure across Focus Mode, Story Nodes, and KFM map legends.

<img alt="SVG Assets" src="https://img.shields.io/badge/Assets-Hydrology%20SVG%20Icons-blue" />
<img alt="Vector Format" src="https://img.shields.io/badge/Format-Scalable%20Vector-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains the **master hydrology SVG icon set**, which forms the basis of:

- Focus Mode hydrology overlays  
- Story Node hydrology badges and indicators  
- Map legend symbols  
- PNG raster export generation  
- STAC legend/symbol metadata  

These SVGs are the **authoritative source** for hydrologic symbology.  
All updates must occur here before propagating to PNG or snapshot variants.

---

### 🗂️ Directory Layout

    svg/
    |-- README.md                        # This document
    |-- well_marker.svg                   # Groundwater well icon
    |-- flood_highwater.svg               # Flood stage symbol
    |-- drought_lowflow.svg               # Hydrologic drought marker
    |-- gauge_station.svg                 # River gauge station
    |-- watershed_outline.svg             # Watershed boundary glyph
    |-- dam_structure.svg                 # Dam location symbol
    |-- levee_marker.svg                  # Levee or floodwall symbol
    |-- discharge_peak.svg                # Peak discharge indicator
    |
    └── ...                               # Additional hydrology SVGs

---

## 🎨 SVG Design Requirements

Hydrology SVGs must follow these technical and aesthetic rules:

### 🧱 Artboard Standards

- Square artboard (32×32 or 64×64 units recommended).  
- Centralized geometry for consistent map placement.  
- Uniform padding so icons align across symbols.

### 🎯 Category Shape Language

- **Groundwater Wells** — vertical shaft + cap or casing element.  
- **Flood Indicators** — multi-wave forms indicating stage or overflow.  
- **Drought/Low Flow** — downward droplet or cracked-water metaphors.  
- **Streamflow/Gauge** — arrow-flow forms, gauges, or measurement glyphs.  
- **Infrastructure** — dam silhouettes, levee segments, intake/diversion markers.  
- **Watersheds** — contour-outline or basin crest motif.

### 🌈 Color & Visibility

- Hydrology colors follow the **blue–teal–aqua** KFM palette.  
- Drought- and low-flow symbols use **amber–brown** tones.  
- Infrastructure uses **gray** styles.  
- All icons must maintain **WCAG 2.1 AA contrast** on light/dark maps.  
- Shapes must be identifiable even in monochrome rendering.

### 🧼 SVG Markup Hygiene

- Use simple `<path>`, `<circle>`, `<polyline>`, etc.  
- Strip all Inkscape/Illustrator metadata.  
- Remove unnecessary `defs`, filters, embedded rasters.  
- Keep markup minimal for performance.

---

### 🔗 Metadata Integration

SVG assets are referenced in the metadata registry at:

- `../metadata/hydrology-symbols.json`  
- `../metadata/hydrology-symbols.stac.json`  
- `../metadata/hydrology-symbols-story-nodes.json`

Example linking (indented):

    {
      "id": "flood_highwater",
      "label": "Flood Highwater",
      "svg": "../svg/flood_highwater.svg",
      "emoji": "🌊",
      "category": "flood"
    }

Story Nodes and Focus Mode never reference raw filenames —  
they always resolve icons via metadata keys.

---

### 🧪 Validation & QA

Hydrology SVGs undergo several automated QC processes:

- **SVG Linting** — validates XML/SVG structure  
- **Metadata Linkage Checks** — ensures all SVGs are referenced  
- **Snapshot Visual Regression** — compares preview renderings with baselines  
- **STAC Compliance Tests** — ensures correct asset typing and roles  

Example workflow (indented):

    1. Update or add SVG  
    2. Update metadata registry  
    3. Run make test-legends-hydrology  
    4. Verify previews and snapshots  
    5. Commit SVG + metadata + snapshot updates  

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                         |
|----------|------------|---------------|---------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology SVG asset README, fully memory-compliant.   |