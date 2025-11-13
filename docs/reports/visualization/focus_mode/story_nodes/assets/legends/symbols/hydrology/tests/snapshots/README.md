---
title: "🖼️ Kansas Frontier Matrix — Hydrology Symbol Snapshot Baselines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/tests/snapshots/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-hydrology-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Hydrology Symbol Snapshot Baselines**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/tests/snapshots/README.md`

**Purpose:**  
Store and govern the golden master baseline images used for **visual regression testing** of hydrology symbols across Focus Mode, Story Nodes, map legends, and rasterized export workflows.

<img alt="Snapshots" src="https://img.shields.io/badge/Snapshots-Golden%20Masters-blue" />
<img alt="Regression Testing" src="https://img.shields.io/badge/Testing-Visual%20Regression-orange" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains the **approved baseline snapshot images** representing the correct visual form of all hydrology legend symbols.

Snapshot testing ensures that:

- Hydrology icon shapes remain unchanged  
- Color palettes and stroke widths remain stable  
- No unintended artistic drifts occur  
- Export + rendering pipelines behave consistently across environments  
- Any updates to hydrologic symbol design receive explicit human approval  

Snapshots are tightly governed under FAIR+CARE, especially for representing flood hazards and drought states ethically.

---

### 🗂️ Directory Layout

    snapshots/
    |-- README.md                     # This document
    |-- hydrology-symbols.png         # Composite preview of all hydrology icons
    |-- well_marker.png               # Groundwater well baseline
    |-- flood_highwater.png           # Flood stage symbol baseline
    |-- drought_lowflow.png           # Hydrologic drought baseline
    |-- gauge_station.png             # Gauge station baseline
    |-- watershed_outline.png         # Watershed boundary baseline
    |-- dam_structure.png             # Dam infrastructure baseline
    |-- levee_marker.png              # Levee structure baseline
    |-- discharge_peak.png            # Peak discharge baseline
    |
    └── ...                           # Additional snapshots as symbols expand

---

### 🧪 How Snapshot Testing Works

Snapshot comparisons occur during CI and local validation:

1. Current hydrology icons (SVG/PNG) are rendered into previews.  
2. Each generated symbol is compared pixel-by-pixel against its stored baseline.  
3. A diff report highlights *any* deviation.  
4. CI blocks merge until:
   - the new design is reviewed,  
   - approved,  
   - and baseline snapshots updated accordingly.  

Example diff output (indented):

    [OK] well_marker.png matches baseline  
    [DIFF] flood_highwater.png differs — manual review required  

Snapshot tests catch:

- Accidental design edits  
- SVG rendering differences between toolchains  
- Color or stroke drift  
- Incorrect export sizes  

---

### 🎨 Updating Snapshot Baselines

Snapshots should be updated **only** when:

- The SVG symbol is intentionally redesigned  
- Accessibility or visibility improvements are made  
- Color palette or severity adjustments are approved  
- FAIR+CARE review mandates a new symbolic representation  

Approved workflow (indented):

    1. Update the SVG in svg/
    2. Regenerate previews with generate_previews.py
    3. Validate renders visually
    4. Replace old snapshots with approved new ones
    5. Commit SVG + snapshot updates together
    6. Document changes in Version History

Snapshots **must never be updated casually**.

---

### ⚖️ Governance & Sensitivity

Hydrology symbols represent **environmental hazards**, **water resources**, and **infrastructure**.  
Therefore, snapshot baselines are part of:

- Ethical hazard representation  
- Environmental justice communication  
- Stewardship of sensitive hydrologic data  
- Public transparency in symbol evolution  

All updates must meet FAIR+CARE criteria, especially when representing drought, inundation zones, or water insecurity.

---

### 🧪 Running Snapshot Validation

Snapshot testing runs through the main hydrology legend test suite:

    make test-legends-hydrology

This includes:

- Metadata validation  
- STAC schema checks  
- Story Node linkage validation  
- Preview sheet generation  
- Pixel-level snapshot comparison  

All hydrology symbol updates must pass before merge approval.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                        |
|----------|------------|---------------|--------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology snapshot baseline README, memory-compliant.|