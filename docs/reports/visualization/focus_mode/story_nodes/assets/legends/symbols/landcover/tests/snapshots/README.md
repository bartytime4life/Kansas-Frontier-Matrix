---
title: "🖼️ Kansas Frontier Matrix — Landcover Symbol Snapshot Baselines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/tests/snapshots/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-landcover-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Landcover Symbol Snapshot Baselines**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/tests/snapshots/README.md`

**Purpose:**  
Store and govern the golden baseline images used for **visual regression testing** of landcover symbols across Focus Mode, Story Nodes, map legends, and raster export pipelines.

<img alt="Snapshots" src="https://img.shields.io/badge/Snapshots-Golden%20Masters-green" />
<img alt="Regression Testing" src="https://img.shields.io/badge/Testing-Visual%20Regression-orange" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains the **approved baseline snapshots** representing the expected visual appearance of every landcover icon used across the Kansas Frontier Matrix (KFM).

Snapshot baselines ensure:

- No unintended changes to icon geometry  
- Stability of category color palettes  
- Consistent stroke width and spacing  
- Accurate symbol reproduction in raster exports  
- High-fidelity ecological communication under FAIR+CARE  
- Transparent version-to-version tracking of landcover icon evolution  

These snapshots are used by the landcover legend test suite to detect pixel-level differences.

---

### 🗂️ Directory Layout

    snapshots/
    |-- README.md                        # This document
    |-- landcover-symbols.png            # Composite preview of all symbols
    |-- grassland_icon.png               # Baseline snapshot
    |-- woodland_icon.png                # Baseline snapshot
    |-- cropland_icon.png                # Baseline snapshot
    |-- wetland_icon.png                 # Baseline snapshot
    |-- shrubland_icon.png               # Baseline snapshot
    |-- urban_builtup.png                # Baseline snapshot
    |-- prairie_tallgrass.png            # Baseline snapshot
    |-- prairie_mixedgrass.png           # Baseline snapshot
    |
    └── ...                              # Additional snapshots as symbols expand

---

### 🧪 How Snapshot Testing Works

Snapshot testing compares:

1. The **current render** of each landcover icon (SVG/PNG)  
2. Against its **golden master baseline** stored here  

If there is *any* deviation, CI triggers a failure.

Snapshot comparison detects:

- Shape deformation  
- Subtle color drift  
- Stroke misalignment  
- Export pipeline artifacts  
- Missing/extra geometry  
- Improper scaling  

Example diff output (indented):

    [OK] grassland_icon.png matches baseline
    [DIFF] wetland_icon.png differs — manual inspection required

---

### 🎨 Updating Baseline Snapshots

Only update snapshots when:

- SVG icon artwork changes intentionally  
- Accessibility improvements are applied  
- Landcover color palette is updated  
- Ecological category semantics change  
- CARE-based adjustments require new iconography  

Approved workflow (indented):

    1. Update SVG asset(s) under svg/
    2. Run generate_previews.py to re-render snapshots
    3. Inspect all new snapshot images manually
    4. Replace old baselines with approved versions
    5. Commit SVG + metadata + snapshot updates together
    6. Record update in Version History

Never update snapshots automatically or without review.

---

### ⚖️ Governance & Ecological Sensitivity

Landcover symbols describe ecosystems and cultural landscapes.  
Snapshot stability ensures:

- Respectful, non-biased ecological representation  
- No implicit value judgment encoded visually  
- Reinforcement of FAIR+CARE practices  
- Steady ecological communication across the platform  

Snapshots also serve as a visual audit log for compliance review.

---

### 🧪 Running Snapshot Validation

Validation is performed through:

    make test-legends-landcover

This includes:

- Metadata validation  
- STAC checks  
- Story Node binding checks  
- Snapshot comparison  
- Preview generation  

All tests **must** pass before merge approval.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                          |
|----------|------------|---------------|----------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover snapshot baseline README, memory-compliant.  |