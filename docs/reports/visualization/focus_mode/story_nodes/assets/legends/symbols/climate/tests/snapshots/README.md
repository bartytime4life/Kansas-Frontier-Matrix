---
title: "🖼️ Kansas Frontier Matrix — Climate Symbol Snapshot Baselines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/snapshots/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-climate-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Climate Symbol Snapshot Baselines**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/snapshots/README.md`

**Purpose:**  
Document the golden baseline snapshots used for visual regression testing of climate symbol icons (SVG/PNG). These baselines ensure visual consistency across versions, rendering engines, and export pipelines.

<img alt="Snapshots" src="https://img.shields.io/badge/Snapshots-Golden%20Masters-blue" />
<img alt="Visual Regression" src="https://img.shields.io/badge/Testing-Visual%20Regression-orange" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory stores **golden master images** representing the approved visual appearance of all climate symbols.

Snapshot testing guarantees:

- Icon geometry stability  
- Correct color palettes  
- Proper stroke thickness  
- No unintended visual drift  
- Valid export integrity (SVG → PNG)  
- Consistency across browsers and renderer engines  

Whenever an icon is updated, the expected snapshot **must** be updated after human review and approval.

---

### 🗂️ Directory Layout

    snapshots/
    |-- README.md                    # This document
    |-- climate-symbols.png          # Golden master sprite sheet for all symbols
    |-- temp_anomaly_cool.png        # Individual baseline snapshot
    |-- temp_anomaly_warm.png        # Individual baseline snapshot
    |-- precip_heavy.png             # Individual baseline snapshot
    |-- drought_severe.png           # Individual baseline snapshot
    |-- flood_major.png              # Individual baseline snapshot
    |-- wind_high.png                # Individual baseline snapshot
    |-- storm_severe.png             # Individual baseline snapshot
    |-- index_pdsiextr.png           # Individual baseline snapshot
    |
    └── ...                          # Additional snapshots as symbols expand

---

### 🧪 How Snapshots Are Used

Visual regression tests compare **current renderings** of each symbol against these stored snapshots.

Matching rules check for:

- Pixel-level exact match  
- Alpha transparency correctness  
- Stroke and fill consistency  
- Identical bounding box alignment  

Example expected behavior (indented):

    [OK] drought_severe.png matches baseline
    [DIFF] flood_major.png deviates from baseline (Δ detected)

A diff triggers CI failure until reviewed and approved.

---

### 🎨 Regenerating Snapshots

Snapshots are regenerated using the preview generator script in the tests directory.

Typical workflow (shown as indented instructions):

    1. Update SVG icon in the svg/ directory
    2. Run generate_previews.py to produce updated PNG previews
    3. Validate new images visually
    4. Replace old snapshots only if approved
    5. Commit updated snapshots alongside the SVG update

Snapshots must never drift unintentionally.

---

### ⚖️ Governance & Compliance

All snapshot updates must:

- Undergo visual review  
- Pass FAIR+CARE compliance checks  
- Maintain semantic meaning of symbols  
- Preserve accessibility (contrast, clarity)

Snapshots serve as audit-proof evidence of correct icon evolution.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                        |
|----------|------------|---------------|--------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial snapshot README, fully compliant with memory rules.  |