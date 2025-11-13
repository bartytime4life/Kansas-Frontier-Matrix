---
title: "🎨 Kansas Frontier Matrix — Event Symbol SVG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/svg/README.md"
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

# 🎨 **Kansas Frontier Matrix — Event Symbol SVG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/svg/README.md`

**Purpose:**  
Define requirements, governance, and usage patterns for the **canonical SVG event symbol icons** used across Focus Mode, Story Nodes, legends, and STAC-linked historical/cultural datasets.

<img alt="SVG Assets" src="https://img.shields.io/badge/Assets-Event%20SVG%20Icons-blue" />
<img alt="Vector" src="https://img.shields.io/badge/Format-Scalable%20Vector-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory contains the **master SVG icon set** for all **event-related symbols** in the Kansas Frontier Matrix (KFM).  

These assets are:

- The **authoritative visual source** for event glyphs  
- Used by Focus Mode, Story Nodes, and MapLibre layers  
- Linked via event symbol metadata (`event-symbols.json`)  
- Exported to PNG for raster-only workflows (`../png/`)  

Any visual change to an event symbol **must be made here first**, then propagated to derivatives (PNGs, sprites, thumbnails).

---

### 🗂️ Directory Layout

    svg/
    |-- README.md                    # This document
    |-- treaty_marker.svg            # Treaty / agreement events
    |-- conflict_event.svg           # Conflicts, battles, hostile encounters
    |-- migration_path.svg           # Migration or movement paths
    |-- settlement_marker.svg        # Settlement / community formation
    |-- cultural_site.svg            # Cultural or ceremonial site
    |-- archaeological_discovery.svg # Archaeological discovery event
    |-- ceremony_marker.svg          # Ceremony / gathering event
    |-- exploration_route.svg        # Exploration / expedition route
    |
    └── ...                          # Additional event symbol SVGs

---

## 🎨 SVG Design & Technical Requirements

All event symbol SVGs must follow these rules to remain legible, accessible, and interoperable.

### 🧱 Artboard & Geometry

- Use a **square artboard** (for example 32×32 or 64×64 units).  
- Center the glyph to avoid offset issues in map symbol placement.  
- Maintain consistent padding so icons align well in legends and sprites.  

### 🎯 Shape & Category Encoding

- **Treaty / Agreement**  
  - Icon language: document, scroll, or seal motif.  
  - Neutral, non-triumphal representation.  

- **Conflict / Hostile Events**  
  - Shapes: angular or crossed forms, but **avoid weapons or gore**.  
  - Must stay neutral and non-sensational in line with FAIR+CARE.  

- **Migration / Movement**  
  - Shapes: arrows or path lines, suggesting motion or routes.  

- **Settlement / Community**  
  - Shapes: simple structures, clustered shapes, or grounded markers.  

- **Cultural / Ceremonial Sites**  
  - Shapes: circular or symmetric, suggesting gathering or focus.  

- **Archaeological Discoveries**  
  - Shapes: trowel-like, artifact silhouettes, or dig-symbol metaphors.  

Each category must be **recognizable by shape alone**, with color as a secondary reinforcement.

### 🌈 Color & Accessibility

- Colors must follow the **event palette** established for KFM (treaty, conflict, cultural, etc.).  
- Maintain **WCAG 2.1 AA contrast** against both light and dark basemaps.  
- Do not rely solely on color to differentiate categories; shape must also differ.  
- Avoid colors that imply moral judgment (for example, intense red only for “bad” events).

### 🧼 Markup & File Hygiene

- Remove editor-specific metadata and unused definitions (Inkscape, Illustrator, etc.).  
- Prefer simple `<path>`, `<rect>`, `<circle>`, `<polygon>` elements.  
- Avoid filters, embedded rasters, or heavy effects (blurs, drop shadows).  
- Keep file size small and markup clean for web performance.

---

## 🔗 Integration With Metadata & Story Nodes

SVG filenames must integrate cleanly with metadata and Story Node systems.

### 🧩 Linkage to `event-symbols.json`

The `event-symbols.json` file in `../metadata/` should reference these SVGs using stable IDs.

Conceptual example (shown as indented JSON-style text):

    {
      "id": "treaty_marker",
      "category": "treaty",
      "label": "Treaty / Agreement",
      "description": "Formal treaty or agreement event.",
      "svg": "../svg/treaty_marker.svg",
      "emoji": "📜",
      "event_type": "treaty"
    }

Applications should resolve SVG paths through metadata, **not** hard-coded filenames.

### 🧠 Story Node Usage

Story Nodes use the event symbol IDs rather than filenames directly.  

Example narrative text pattern:

    "In 1867, the {symbol:treaty_marker} Medicine Lodge Treaty reshaped relations on the plains."

The renderer:

- Replaces `{symbol:treaty_marker}` with the appropriate SVG or emoji.  
- Registers the symbol in the legend.  
- Records its usage in Focus Mode telemetry.

---

## 🧪 Validation & QA

SVG event icons should be covered by the climate/event legend test suite under `../tests/`.

Recommended checks:

- **SVG linting**  
  - Verify files are valid XML/SVG.  
  - Check for disallowed constructs (embedded raster, heavy filters).  

- **Metadata linkage**  
  - Ensure every symbol ID in metadata points to an existing SVG.  
  - Ensure no stray SVG files without metadata entries (unless explicitly staged).  

- **Visual snapshots**  
  - Preview sheets generated (for example via `generate_previews.py` from `../tests/`).  
  - Differences against snapshot baselines reviewed and approved before merge.  

Typical local workflow (shown as indented text):

    1. Edit or add SVG in svg/
    2. Update event-symbols.json metadata
    3. Run make test-legends-events
    4. Inspect preview/snapshot outputs
    5. Commit SVG + metadata + snapshots together

CI must block merges if SVG or metadata validation fails.

---

## 🕒 Version History

| Version  | Date       | Author        | Notes                                                     |
|----------|------------|---------------|-----------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial SVG event symbol asset README, memory-compliant.  |