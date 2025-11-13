---
title: "🖼️ Kansas Frontier Matrix — Event Symbol PNG Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/png/README.md"
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

# 🖼️ **Kansas Frontier Matrix — Event Symbol PNG Assets**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/events/png/README.md`

**Purpose:**  
Document and govern the **raster PNG event symbol assets** used when SVG rendering is unavailable or undesirable (legacy environments, print/export workflows, thumbnails).

<img alt="PNG Assets" src="https://img.shields.io/badge/Assets-Event%20PNG%20Icons-blue" />
<img alt="Resolution" src="https://img.shields.io/badge/Resolution-High%20DPI%20@2x-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />

</div>


---

## 📚 Overview

This directory holds **PNG fallbacks** for the event symbol icons defined under:

- `../svg/` (canonical vector sources)  
- `../metadata/` (event-symbol metadata)  

These PNGs are used for:

- Static map exports (PDF, PNG, TIFF)  
- Environments that do not fully support SVG  
- Thumbnail previews and sprite sheets  
- Embedding into raster-only report pipelines  

Key principles:

- SVGs remain the **authoritative source**  
- PNGs are **derived artifacts**  
- Naming, semantics, and severity must match the SVG set exactly  
- Any visual change begins at the SVG level and then is re-exported here  

---

### 🗂️ Directory Layout

    png/
    |-- README.md                      # This document
    |-- treaty_marker@2x.png           # Treaty / agreement symbol (raster)
    |-- conflict_event@2x.png          # Conflict / hostile event symbol
    |-- migration_path@2x.png          # Migration path event symbol
    |-- settlement_marker@2x.png       # Settlement / community founding
    |-- cultural_site@2x.png           # Cultural or ceremonial site marker
    |-- archaeological_discovery@2x.png# Archaeological discovery event
    |-- ceremony_marker@2x.png         # Ceremony / gathering event marker
    |-- exploration_route@2x.png       # Exploration route / expedition path
    |
    └── ...                            # Additional PNG variants as needed

---

### 🧱 PNG Asset Requirements

All event PNG icons must satisfy the following:

- Resolution  
  - Minimum high-DPI 2× assets (for example 64×64 px for a 32×32 logical icon)  
  - Square or consistent aspect ratio matching SVG artboard  

- Background  
  - Transparent (alpha channel)  
  - No baked-in map, halo, or background color unless explicitly required  

- Naming  
  - Base name mirrors SVG icon ID  
  - Suffix `@2x` (or similar) indicates DPI scaling  
  - Example:
    - `treaty_marker.svg` → `treaty_marker@2x.png`  

- Visual parity  
  - Same shape, color, and stroke as SVG source  
  - No unique “PNG-only” styling or effects  
  - If SVG is updated, PNG must be regenerated  

- Cultural & ethical safeguards  
  - No sensationalist imagery (especially for conflict or traumatic events)  
  - Respect Indigenous and local protocols when encoding ceremonial events  
  - Follow CARE labels defined in event metadata  

---

### 🔗 Linkage to Metadata & Legends

Each PNG file must be referenced indirectly via **metadata**, never hard-coded paths in application logic.

- The **event symbol registry** (`../metadata/event-symbols.json`) defines:
  - Canonical `id`  
  - SVG path  
  - Optional PNG path (or derivable naming convention)  

- The **STAC metadata** (`../metadata/event-symbols.stac.json`) may include:
  - PNG assets with roles such as `["thumbnail", "legend", "symbol"]`  

Example conceptual mapping (indented, not fenced):

    {
      "id": "treaty_marker",
      "category": "treaty",
      "label": "Treaty / Agreement",
      "svg": "../svg/treaty_marker.svg",
      "png": "../png/treaty_marker@2x.png"
    }

Renderers and export pipelines should resolve PNG paths from metadata, not from ad-hoc string concatenation.

---

### 🧪 Validation & QA

Event PNG assets should undergo the following checks:

- File existence for every symbol with a PNG reference  
- Transparent backgrounds (no unintended solid color)  
- Correct resolution and dimension expectations  
- Visual comparison against golden snapshot baselines under `../tests/snapshots/`  
- Synchronization with SVG updates (no outdated PNGs)  

Example CI behavior (indented):

    [OK] treaty_marker@2x.png exists and matches baseline
    [OK] conflict_event@2x.png exists and matches baseline
    [DIFF] exploration_route@2x.png deviates from baseline (review required)

Local validation is typically triggered through a higher-level target such as:

    make test-legends-events

which should include PNG-specific checks alongside metadata and SVG tests.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                      |
|----------|------------|---------------|------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial README for event PNG symbols, memory-compliant.    |