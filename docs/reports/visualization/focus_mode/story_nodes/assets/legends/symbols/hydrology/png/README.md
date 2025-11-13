---
title: "🖼️ Kansas Frontier Matrix — Hydrology Symbol PNG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/png/README.md"
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

# 🖼️ **Kansas Frontier Matrix — Hydrology Symbol PNG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/png/README.md`

**Purpose:**  
Define, govern, and validate the rasterized PNG versions of all hydrology symbols used across Focus Mode, Story Nodes, map legends, and export workflows.

<img alt="PNG Assets" src="https://img.shields.io/badge/Assets-Hydrology%20PNG%20Icons-blue" />
<img alt="Resolution" src="https://img.shields.io/badge/High%20DPI-@2x-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

The PNG assets in this directory are **rasterized derivatives** of the authoritative hydrology SVG symbols in:

- `../svg/` (master icons)  
- `../metadata/` (symbol definitions)

These PNGs exist for:

- Static hydrology map exports (PDF, PNG, TIFF)
- Device fallback where SVG rendering is limited
- Thumbnail displays or sprite sheets
- Automation workflows requiring pixel-based imagery  

**SVGs remain the canonical source**.  
PNG files must match SVG design exactly and be regenerated whenever the SVGs change.

---

### 🗂️ Directory Layout

    png/
    |-- README.md                      # This document
    |-- well_marker@2x.png             # Groundwater well
    |-- flood_highwater@2x.png         # Flood stage indicator
    |-- drought_lowflow@2x.png         # Hydrologic drought / low flow
    |-- gauge_station@2x.png           # Stream gauge station
    |-- watershed_outline@2x.png       # Watershed boundary marker
    |-- dam_structure@2x.png           # Dam infrastructure
    |-- levee_marker@2x.png            # Levee structure marker
    |-- discharge_peak@2x.png          # Peak discharge indicator
    |
    └── ...                            # Additional hydrology PNG assets

---

### 🧱 PNG Asset Requirements

All PNG hydrology icons must meet the following:

- **Resolution**
  - Minimum 2× high DPI (example: 64×64 px for 32×32 px logical size)
  - Square or SVG-matching aspect ratio

- **Background**
  - Fully transparent (alpha channel)
  - No embedded shadows, glows, or non-neutral backgrounds

- **Naming Convention**
  - Must mirror SVG filename + `@2x` suffix  
    Example:  
      - SVG → `well_marker.svg`  
      - PNG → `well_marker@2x.png`

- **Visual Parity**
  - Shapes, strokes, and colors must be visually identical to SVG originals
  - No raster-only embellishments or effects
  - Any SVG update **requires** PNG regeneration

- **Ethical & Cultural Requirements**
  - No alarmist hazard imagery  
  - Respectful representation of water infrastructure and hydrologic risk
  - Compliance with FAIR+CARE labeling from metadata

---

### 🔗 Metadata Linkage

PNG icons must be referenced through **metadata**, not hard-coded paths in UI or pipelines.

Hydrology symbol metadata (`../metadata/hydrology-symbols.json`) may include:

    {
      "id": "well_marker",
      "category": "groundwater",
      "label": "Groundwater Well",
      "svg": "../svg/well_marker.svg",
      "png": "../png/well_marker@2x.png",
      "emoji": "💧"
    }

STAC metadata (`../metadata/hydrology-symbols.stac.json`) may optionally include PNG files under:

- roles: `["thumbnail", "legend", "symbol"]`  
- type: `image/png`

---

### 🧪 Validation & QA

PNG asset checks must verify:

- File existence for all required PNGs  
- Resolution compliance with 2× export rules  
- Transparent background (no unintended solid fills)
- Pixel-level match with snapshot baselines
- Synchronization with corresponding SVG assets  

Snapshot tests under `../tests/snapshots/` ensure no visual drift occurs.

Example CI output:

    [OK] gauge_station@2x.png matches baseline
    [DIFF] discharge_peak@2x.png deviates — review needed

Local validation helper:

    make test-legends-hydrology

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                           |
|----------|------------|---------------|-----------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology PNG symbol README, memory-rule compliant.    |