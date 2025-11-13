---
title: "🧪 Kansas Frontier Matrix — Hydrology Symbol Legend Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/tests/README.md"
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

# 🧪 **Kansas Frontier Matrix — Hydrology Symbol Legend Test Suite**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/hydrology/tests/README.md`

**Purpose:**  
Document all automated test routines for hydrology symbol metadata, SVG/PNG assets, STAC integration, and visual baseline validation.

<img alt="Test Suite" src="https://img.shields.io/badge/Tests-Hydrology%20Legend%20Suite-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold" />
<img alt="CI" src="https://img.shields.io/badge/CI-Merge%20Blocking-red" />

</div>


---

## 📚 Overview

This directory provides the **validation suite** ensuring that all hydrology symbol assets meet KFM’s strict standards for:

- Metadata correctness  
- SVG and PNG asset consistency  
- STAC-compliant legend publication  
- Visual regression stability  
- Accessibility and FAIR+CARE compliance  

These tests run automatically in CI and must pass before any merge that modifies hydrology legend content.

---

### 🗂️ Directory Layout

    tests/
    |-- README.md                    # This document
    |-- snapshots/                   # Golden baseline images for visual regression tests
    |-- validate_metadata.py         # Schema + linkage validator
    |-- generate_previews.py         # Preview generator for snapshot comparison

---

### 🧱 Metadata Validation — `validate_metadata.py`

Validates:

- Schema correctness for:
  - `hydrology-symbols.json`
  - `hydrology-symbols.stac.json`
  - `hydrology-symbols-story-nodes.json`
- Existence and correctness of all referenced assets  
- No orphan SVG/PNG files  
- Category, severity, and variable/unit consistency  

Sample output (indented):

    [OK] hydrology-symbols.json schema validated
    [OK] 8 SVG assets found and matched
    [OK] 8 PNG assets linked correctly
    [OK] STAC metadata valid
    [OK] Story Node bindings verified

---

### 🎨 Visual Regression — `snapshots/`

Hydrology symbols undergo snapshot comparison using rendered preview sheets.

Tests validate:

- Color fidelity  
- Stroke width  
- Shape geometry  
- Centering / padding alignment  
- No visual drift compared to golden snapshots  

Example diff output:

    [DIFF] flood_highwater.png differs from baseline — review required

Snapshot tests prevent unnoticed hydrology icon changes from entering production.

---

### 🖼️ Preview Generation — `generate_previews.py`

This tool builds preview images for manual and automated validation.

Responsibilities:

- Load all hydrology SVG assets  
- Optionally include PNG derivatives  
- Generate unified sprite sheets for review  
- Produce deterministic, consistent renders  

Example invocation (indented):

    python generate_previews.py --all

---

### 🧪 Running the Hydrology Legend Test Suite

The full test suite runs under a single Make target:

    make test-legends-hydrology

This executes, in order:

1. Metadata validation  
2. STAC metadata checks  
3. Story Node binding tests  
4. Preview generation  
5. Snapshot comparison  

All results must be green before merge.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                          |
|----------|------------|---------------|----------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial hydrology legend test suite README, memory-compliant.  |