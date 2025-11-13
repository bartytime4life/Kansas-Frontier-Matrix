---
title: "🎨 Kansas Frontier Matrix — Climate Symbol SVG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/svg/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Climate Symbol SVG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/svg/README.md`

**Purpose:**  
Define requirements and governance for the **canonical SVG climate symbol icons** used across Focus Mode, Story Nodes, legends, and STAC-linked visualizations.

<img alt="SVG Assets" src="https://img.shields.io/badge/Assets-SVG%20Icons-blue" />
<img alt="Vector" src="https://img.shields.io/badge/Format-Scalable%20Vector-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains the **master SVG icon set** for all climate-related symbols in the Kansas Frontier Matrix (KFM).  

These vector assets are:

- The **authoritative source** for all climate glyphs  
- Consumed by Focus Mode, Story Nodes, and MapLibre layers  
- Referenced by climate legend metadata (`climate-symbols.json`)  
- Exported to PNG for raster-only workflows  

Any visual change to a climate symbol **must** be made here first, then propagated to derivative formats (PNG, sprites, etc.).

---

### 🗂️ Directory Layout

    svg/
    |-- README.md                    # This document
    |-- temp_anomaly_cool.svg       # Cool temperature anomaly symbol
    |-- temp_anomaly_warm.svg       # Warm temperature anomaly symbol
    |-- precip_heavy.svg            # Heavy precipitation anomaly symbol
    |-- drought_severe.svg          # Severe drought symbol
    |-- flood_major.svg             # Major flood symbol
    |-- wind_high.svg               # High wind symbol
    |-- storm_severe.svg            # Severe storm symbol
    |-- index_pdsiextr.svg          # Extreme PDSI index symbol
    |
    └── ...                         # Any additional climate symbol SVGs

---

## 🧱 SVG Design & Technical Requirements

All climate SVG icons in this directory must follow these rules:

- **Coordinate system**
  - Use a square artboard (e.g., 32×32 or 64×64 units).
  - Center shapes within the artboard to avoid alignment drift.

- **Styling**
  - Use simple paths and shapes; avoid excessive complexity.
  - Prefer stroke + fill styling that preserves readability at small sizes.
  - Avoid embedded raster images or filters (shadows, blurs).

- **Color**
  - Colors must follow the climate symbol palette defined elsewhere in KFM.
  - Maintain consistent colors for categories (temperature, drought, flood, etc.).
  - Ensure sufficient contrast for use on both light and dark basemaps.

- **Accessibility**
  - Distinguish categories by both **shape and color**.
  - Avoid thin strokes that disappear at low resolution.
  - Symbols should remain recognizable at common UI sizes.

- **Metadata hygiene**
  - Strip editor-specific metadata (Inkscape, Illustrator junk tags).
  - Remove unnecessary `<title>` / `<desc>` if they conflict with KFM labels.

---

## 🔗 Integration With Metadata & Story Nodes

SVG filenames must match the IDs in climate symbol metadata:

- For each SVG file here, `climate-symbols.json` should include:
  - `id` equal to the base name (without extension) or a clear mapping.
  - `svg` pointing to the relative path from the metadata file.

Example (conceptual, shown as indented text):

    {
      "id": "flood_major",
      "category": "flood",
      "label": "Major Flood",
      "svg": "../svg/flood_major.svg",
      "severity": "severe"
    }

Story Nodes and Focus Mode reference these IDs, not raw filenames.  
Renderers use the metadata to resolve the correct SVG icon from this directory.

---

## 🧪 Validation & QA

SVG assets should be validated via:

- **Linting**
  - Check for well-formed SVG markup.
  - Ensure no broken references or embedded raster data.

- **Visual snapshots**
  - Generate sprite sheets or preview images for human review.
  - Compare against prior snapshots to detect unexpected changes.

- **Metadata linkage**
  - Confirm every symbol in `climate-symbols.json` resolves to an SVG file.
  - Confirm no orphan SVGs exist without a metadata entry, unless explicitly staged.

Suggested local helper (wrapped here as plain text):

    make test-legends-climate

This target should include SVG-specific checks as they are wired into the KFM CI system.

---

## 🕒 Version History

| Version  | Date       | Author        | Notes                                                  |
|----------|------------|---------------|--------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial SVG asset README aligned with memory rules.    |