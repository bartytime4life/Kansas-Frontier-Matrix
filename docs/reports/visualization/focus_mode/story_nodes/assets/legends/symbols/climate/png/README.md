---
title: "🖼️ Kansas Frontier Matrix — Climate Symbol PNG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/png/README.md"
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

# 🖼️ **Kansas Frontier Matrix — Climate Symbol PNG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/png/README.md`

**Purpose:**  
Document and govern the raster-format climate symbol assets used when SVG is unavailable (legacy browsers, print workflows, offline export pipelines).

<img alt="PNG Assets" src="https://img.shields.io/badge/Assets-PNG%20Icons-blue" />
<img alt="Resolution" src="https://img.shields.io/badge/Resolution-2x%20High%20DPI-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

The PNG folder stores **raster renderings of climate symbol icons**, primarily used for:

- Static exports (PDF, PNG, TIFF)
- Systems without SVG rendering capability  
- Mobile fallbacks  
- Offline map generation  
- Embedded report workflows

These PNG assets mirror the **SVG master icons** found in `../svg/` and must maintain:

- identical naming  
- identical semantics  
- identical severity variants  
- equal conceptual meaning  

PNG assets are **not authoritative**; they are derivatives.  
All corrections must first be made to the SVG sources.

---

### 🗂️ Directory Layout

    png/
    |-- README.md                    # This document
    |-- temp_anomaly_cool@2x.png     # Raster icon: cool temperature anomaly
    |-- temp_anomaly_warm@2x.png     # Raster icon: warm temperature anomaly
    |-- precip_heavy@2x.png          # Raster icon: heavy precipitation anomaly
    |-- drought_severe@2x.png        # Raster icon: severe drought indicator
    |-- flood_major@2x.png           # Raster icon: major flood indicator
    |-- wind_high@2x.png             # Raster icon: high wind conditions
    |-- storm_severe@2x.png          # Raster icon: severe storm indicator
    |-- index_pdsiextr@2x.png        # Raster icon: extreme PDSI index
    |
    └── ...                          # Any additional raster variants

---

### 🧱 Asset Requirements

PNG icons must follow these constraints:

- **Resolution:**  
  - Minimum 2× scale (high DPI)
  - Recommended size: 64×64 px or larger
- **Background:**  
  - Transparent (`.png` with alpha)
- **Naming:**  
  - Must match SVG name + `@2x` suffix  
  - Example: `drought_severe.svg` → `drought_severe@2x.png`
- **Color + Shape Parity:**  
  - Must match SVG colors, stroke widths, shapes
- **No semantic drift:**  
  - PNG cannot introduce unique variants or new styling

All PNG assets should be **exported directly from the canonical SVG files** to ensure consistency.

---

### 🧪 Validation & QA

PNG asset QA checks include:

- Correct filenames  
- Correct resolution  
- Correct transparency (no solid background)  
- Pixel-perfect comparison to baseline snapshot images  
- Matching STAC asset registration (if used)

Local validation helper:

    make test-legends-climate

This runs:

- Metadata validation  
- Snapshot comparison  
- File integrity checks

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                |
|----------|------------|---------------|------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial PNG asset README, fully memory-compliant.    |