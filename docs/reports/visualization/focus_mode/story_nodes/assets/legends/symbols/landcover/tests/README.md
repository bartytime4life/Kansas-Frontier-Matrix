---
title: "🧪 Kansas Frontier Matrix — Landcover Symbol Legend Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/tests/README.md"
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

# 🧪 **Kansas Frontier Matrix — Landcover Symbol Legend Test Suite**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/landcover/tests/README.md`

**Purpose:**  
Provide full documentation for the automated testing system that validates all **landcover symbol assets, metadata, STAC mappings, and visual snapshot baselines** used by Focus Mode and Story Nodes.

<img alt="Test Suite" src="https://img.shields.io/badge/Tests-Landcover%20Legend%20Suite-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold" />
<img alt="CI" src="https://img.shields.io/badge/CI-Merge%20Blocking-red" />

</div>


---

## 📚 Overview

This test suite ensures:

- All landcover symbol metadata is accurate and complete  
- SVG and PNG icons match metadata definitions  
- STAC Item & asset metadata is valid  
- No symbols drift visually  
- All assets remain compliant with ecological neutrality and FAIR+CARE principles  
- Story Node bindings reference real, existing icons  
- No orphan icons exist without metadata  

All tests must pass before merge approval.

---

### 🗂️ Directory Layout

    tests/
    |-- README.md                    # This document
    |-- snapshots/                   # Golden baseline images for regression tests
    |-- validate_metadata.py         # Schema + linkage validator
    |-- generate_previews.py         # Renderer for preview/snapshot comparisons

---

### 🧱 Metadata Validation — `validate_metadata.py`

This script validates:

- landcover-symbols.json  
- landcover-symbols.stac.json  
- landcover-symbols-story-nodes.json  
- Existence of all SVG/PNG files referenced  
- No stray/unreferenced files  
- Correct “category”, “label”, and “landcover_type” fields  
- Valid CARE labels  
- Semantic consistency across landcover groups  

Sample output (indented):

    [OK] landcover-symbols.json schema validated
    [OK] 8 SVG icons linked
    [OK] 8 PNG icons linked
    [OK] STAC metadata validated
    [OK] Story Node bindings validated

---

### 🎨 Visual Regression — `snapshots/`

Snapshot comparison ensures icons remain visually stable.

The system tests for:

- Color shifts  
- Shape deformation  
- Incorrect stroke widths  
- Alignment/padding drift  
- Basemap visibility issues  

Example output:

    [OK] grassland_icon.png matches baseline
    [DIFF] prairie_tallgrass.png differs — review required

Snapshots protect ecological communication consistency.

---

### 🖼️ Preview Generation — `generate_previews.py`

This helper tool:

- Loads all SVG landcover icons  
- Generates uniform preview sheets  
- Produces PNG outputs for snapshot comparison  
- Ensures deterministic rendering  

Example invocation (indented):

    python generate_previews.py --all

---

### 🧪 Running the Complete Landcover Test Suite

One command runs everything:

    make test-legends-landcover

This includes:

1. Metadata validation  
2. STAC validation  
3. Story Node binding checks  
4. Preview generation  
5. Snapshot comparison  

Any failure blocks merge operations.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                         |
|----------|------------|---------------|---------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial landcover test suite README, fully memory-compliant.  |