---
title: "🧪 Kansas Frontier Matrix — Climate Symbol Legend Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/README.md"
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

# 🧪 **Kansas Frontier Matrix — Climate Symbol Legend Test Suite**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/climate/tests/README.md`

**Purpose:**  
Document the automated validation tests that guarantee correctness, consistency, and FAIR+CARE governance for all climate legend symbols and metadata.

<img alt="Test Suite" src="https://img.shields.io/badge/Tests-Validation%20Suite-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliance-gold" />
<img alt="CI" src="https://img.shields.io/badge/CI-Enforced-red" />

</div>


---

## 📚 Overview

This directory contains all automated tests related to:

- Climate symbol SVG/PNG assets  
- Metadata definitions  
- STAC legend/symbol entries  
- Story Node binding rules  
- Snapshot-based visual regression  

These tests ensure:

- Symbol naming consistency  
- File presence and integrity  
- Schema compliance  
- Visual stability across versions  
- No missing or extra assets  
- Full MCP-DL and FAIR+CARE alignment  

All tests must pass before any merge involving climate symbol assets.

---

### 🗂️ Directory Layout

    tests/
    |-- README.md                    # This document
    |-- snapshots/                   # Golden image snapshots for visual regression
    |-- validate_metadata.py         # Schema and file-path validation script
    |-- generate_previews.py         # Renders SVG/PNG previews for snapshot tests

---

### 🧱 Metadata Validation — `validate_metadata.py`

This script checks:

- All symbol IDs exist in metadata  
- All referenced SVG/PNG assets exist  
- No orphan icons without metadata  
- JSON Schema conformance  
- Category + severity consistency  
- Threshold and variable completeness  

Example output format (indented):

    [OK] climate-symbols.json schema validated
    [OK] 8 SVG assets found and linked
    [OK] 8 PNG assets found and linked
    [OK] STAC metadata validated
    [OK] Story Node bindings validated

---

### 🎨 Visual Regression Testing — `snapshots/`

The **snapshots** directory stores **golden master images** representing the expected appearance of each climate symbol.

`generate_previews.py` renders the current symbol set, then the tests compare:

- Colors  
- Strokes  
- Shapes  
- Proportions  
- Alignment  
- Icon padding  

Regression tests catch even small unintended changes.

Example (indented):

    [DIFF] flood_major.svg changed from baseline
    [OK] storm_severe.svg matches baseline

---

### 🖼️ Preview Generation — `generate_previews.py`

This helper script:

- Loads all SVG and PNG symbols  
- Rasterizes previews into a sprite sheet  
- Saves preview exports to assist visual QA  
- Supports both CLI and CI-driven runs  
- Uses deterministic settings for reproducibility

Typical invocation (indented):

    python generate_previews.py --all

---

### 🧪 Running the Full Suite

Local test helper:

    make test-legends-climate

This runs:

- Metadata validation  
- STAC validation  
- Story Node binding validation  
- Snapshot comparison  
- Preview generation  

CI will **block all merges** if any test fails.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                 |
|----------|------------|---------------|-------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial test suite README, fully memory-compliant.    |