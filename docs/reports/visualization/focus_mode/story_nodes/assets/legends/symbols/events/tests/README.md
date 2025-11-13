---
title: "🧪 Kansas Frontier Matrix — Event Symbol Legend Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/tests/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Event Symbol Legend Test Suite**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/tests/README.md`

**Purpose:**  
Document the automated **test suite** that validates event symbol assets, metadata, STAC integration, and Story Node bindings for Focus Mode and KFM visualizations.

<img alt="Test Suite" src="https://img.shields.io/badge/Tests-Event%20Legend%20Suite-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold" />
<img alt="CI" src="https://img.shields.io/badge/CI-Merge%20Blocking-red" />

</div>


---

## 📚 Overview

This directory contains all tests that ensure **event symbol legends** are:

- Correctly defined in metadata  
- Properly linked to SVG and PNG assets  
- In compliance with STAC and Story Node schemas  
- Visually stable across icon updates  
- Respectful of FAIR+CARE and cultural sensitivity requirements  

These tests protect against:

- Missing or orphaned icons  
- Broken metadata references  
- Schema drift  
- Unintended visual changes to event symbols  
- Inconsistent use of event categories and CARE labels  

All tests in this directory must pass before any merge that touches event symbol assets or metadata.

---

### 🗂️ Directory Layout

    tests/
    |-- README.md                    # This document
    |-- snapshots/                   # Golden master images for visual regression
    |-- validate_metadata.py         # Metadata + linkage validation script
    |-- generate_previews.py         # Renders preview sheets for snapshot tests

---

### 🧱 Metadata Validation — `validate_metadata.py`

This script validates:

- `event-symbols.json` structure and schema  
- `event-symbols.stac.json` STAC compliance  
- `event-symbols-story-nodes.json` Story Node binding rules  
- Existence of all referenced SVG and PNG assets  
- No orphan assets without a corresponding metadata entry  

Typical checks (illustrative output):

    [OK] event-symbols.json schema validated
    [OK] 8 SVG assets found and linked
    [OK] 8 PNG assets found and linked
    [OK] STAC metadata valid
    [OK] Story Node bindings consistent

If any symbol is missing, duplicated, or mis-linked, the script must fail and return a non-zero exit code to CI.

---

### 🎨 Visual Regression — `snapshots/`

The `snapshots/` directory stores **golden baseline images** representing the expected appearance of event symbols.

Visual tests compare current renders against these baselines to detect:

- Color changes  
- Stroke thickness differences  
- Shape or geometry drift  
- Alignment and padding changes  

Sample diff-style output:

    [OK] treaty_marker.png matches baseline
    [DIFF] conflict_event.png deviates from baseline (review required)

Any meaningful change must be explicitly reviewed, the snapshot updated, and the change documented in commit messages and version history.

---

### 🖼️ Preview Generation — `generate_previews.py`

This helper script renders **preview sheets** from the SVG/PNG assets to aid human review.

Responsibilities:

- Load all event SVG (and optionally PNG) icons  
- Render them into a sprite sheet or grid layout  
- Save outputs for snapshot comparison and manual inspection  
- Provide deterministic sizing and padding for consistent comparisons  

Example usage pattern:

    python generate_previews.py --all

The script should be wired into the main event legend test target so it runs automatically in CI when assets change.

---

### 🧪 Running the Event Legend Test Suite

All event legend validations should be runnable via a single, high-level Make target (or equivalent task runner).

Example local invocation:

    make test-legends-events

This target is expected to run, at minimum:

- `validate_metadata.py`  
- STAC metadata validation (if separate)  
- Story Node binding checks  
- Preview generation and snapshot comparison  

CI must be configured so that **any failure** in these checks blocks merge operations affecting:

- `svg/` event icons  
- `png/` event icons  
- `metadata/` event symbol definitions  
- `tests/` baselines and scripts  

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                         |
|----------|------------|---------------|---------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial event legend test suite README, memory-compliant.     |