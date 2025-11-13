---
title: "🖼️ Kansas Frontier Matrix — Event Symbol Snapshot Baselines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/tests/snapshots/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-event-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Event Symbol Snapshot Baselines**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/tests/snapshots/README.md`

**Purpose:**  
Provide the golden master baseline images used for **visual regression testing** of event symbol icons, ensuring consistent rendering across Focus Mode, Story Nodes, map legends, and KFM visualization layers.

<img alt="Snapshots" src="https://img.shields.io/badge/Snapshots-Golden%20Masters-blue" />
<img alt="Regression Testing" src="https://img.shields.io/badge/Testing-Visual%20Regression-orange" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

The **snapshot baseline images** stored in this directory represent the *approved visual appearance* of all event symbols across the Kansas Frontier Matrix (KFM).  
They ensure that:

- SVG/PNG event symbols remain visually stable  
- No unintentional design drift occurs  
- Stroke widths, colors, shapes, and proportions remain correct  
- Rendering engines (MapLibre, Pipeline Rasterizer, Browser) are consistent  
- Updates to symbol artwork require deliberate human review  

Snapshots are used by the event legend test suite to detect differences between current and expected output.

---

### 🗂️ Directory Layout

    snapshots/
    |-- README.md                       # This document
    |-- event-symbols.png               # Composite sprite-sheet baseline
    |-- treaty_marker.png               # Baseline snapshot
    |-- conflict_event.png              # Baseline snapshot
    |-- migration_path.png              # Baseline snapshot
    |-- settlement_marker.png           # Baseline snapshot
    |-- cultural_site.png               # Baseline snapshot
    |-- archaeological_discovery.png    # Baseline snapshot
    |-- ceremony_marker.png             # Baseline snapshot
    |-- exploration_route.png           # Baseline snapshot
    |
    └── ...                             # Additional event symbol snapshots

---

### 🧪 How Snapshot Testing Works

During CI or local validation:

1. The test suite renders **current** SVG/PNG icons into a preview sheet.
2. Each generated icon is compared pixel-by-pixel against the matching snapshot.
3. Differences trigger a **test failure** unless intentionally approved.

Snapshot testing detects:

- Color changes  
- Stroke thickness changes  
- Shape inconsistencies  
- Alignment or padding drift  
- Export/rendering anomalies  

Example CI output (indented):

    [OK] treaty_marker.png matches baseline  
    [DIFF] conflict_event.png deviates from baseline (review needed)

If a symbol is intentionally updated, the snapshot must be regenerated and committed after approval.

---

### 🎨 Updating Snapshot Baselines

Snapshots must only be updated when:

- The SVG source was intentionally redesigned  
- A symbol was corrected for accessibility  
- A category palette was changed  
- CARE/cultural adjustments were approved  
- Rendering pipeline updates require new outputs  

Approved workflow (indented):

    1. Update SVG icon
    2. Run generate_previews.py
    3. Inspect new renders visually
    4. Replace old snapshots with new ones
    5. Commit SVG + snapshot changes together
    6. Document update in Version History

Snapshots **should never** drift unintentionally.

---

### ⚖️ Governance & Cultural Sensitivity

Event symbols often represent:

- Treaties  
- Conflicts  
- Migrations  
- Sacred or ceremonial events  
- Archaeological contexts  

Thus snapshot integrity is critical for:

- Respectful representation  
- Non-sensational visual language  
- Ensuring clean, consistent symbology that aligns with FAIR+CARE  
- Maintaining transparency in symbol evolution  

Snapshots serve as part of the audit trail for symbol correctness.

---

### 🧪 Running Snapshot Validation

The snapshot tests run automatically through the event legend test suite:

    make test-legends-events

This includes:

- Metadata validation  
- STAC validation  
- Story Node binding checks  
- Snapshot regression comparison  
- Visual preview generation  

All snapshot tests must pass before merge.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                         |
|----------|------------|---------------|---------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial snapshot baseline README, fully memory-compliant.     |