---
title: "🗺️ Kansas Frontier Matrix — Map Styling Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/maps/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-styles-maps-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Specification"
intent: "web-styles-maps"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Variable (depends on layers)"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/styles/maps/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DefinedTermSet"
  owl_time: "TemporalEntity"
  geosparql: "N/A"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../schemas/json/web-styles-maps.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-styles-maps-shape.ttl"
doc_uuid: "urn:kfm:doc:web-styles-maps-v10.4.0"
semantic_document_id: "kfm-doc-web-styles-maps"
event_source_id: "ledger:web/src/styles/maps/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified visual semantics"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "specification"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon map-style system v11 update"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map Styling Specification**  
`web/src/styles/maps/README.md`

**Purpose:**  
Define the **map-specific styling layer** for the Kansas Frontier Matrix (KFM) Web Platform:  
how MapLibre and Cesium maps, overlays, legends, masking grids, and map UI components  
are visually rendered in a way that is **consistent**, **accessible**, and **FAIR+CARE-aware**.

</div>

---

## 📘 Overview

The `web/src/styles/maps/` directory contains **CSS and styling primitives specifically for map UIs**:

- MapLibre GL map canvas and interaction controls  
- Cesium 3D globe + terrain overlays  
- Map legends and layer keys  
- H3 masking cell visualizations  
- Sovereignty and CARE overlays  
- Map HUDs (cursor readouts, debug HUDs, etc.)  
- Map-specific A11y adaptations (focus rings, color ramps)  

These map styles sit **on top of** the design tokens and themes defined in:

- `web/src/styles/tokens/**`  
- `web/src/styles/themes/**`  
- `web/src/styles/mixins/**`  

Map styles must **never** introduce their own colors or spacing directly; they must use tokens + theme variables.

---

## 🧱 Directory Structure

> Filenames are illustrative; align them to your actual implementation paths.

~~~text
web/src/styles/maps/
├── maplibre.css          # Base MapLibre map, controls, popups, and overlays
├── cesium.css            # Cesium globe, timeline, and overlay styling
├── layers.css            # Layer-specific styling (boundaries, rivers, trails, etc.)
├── legends.css           # Legend layout, swatches, and labels
├── masking.css           # H3 grid + masking visualization for sensitive sites
└── hud.css               # Map HUD styling (cursor info, debug overlays, scale bar)
~~~

---

## 🧩 Module Responsibilities

---

### 🗺️ `maplibre.css` — MapLibre Core Styling

Defines styles for:

- Map canvas container and parent element  
- Navigation controls (zoom in/out, reset, compass)  
- Attribution + scale controls  
- Popups and info boxes  
- Click/hover feedback indicators  

Requirements:

- Must use theme variables for backgrounds, borders, and text  
- Must provide **visible focus states** for keyboard users on controls  
- Must ensure controls do not block critical map content (e.g., masked overlays, legends)  
- Must be legible in light/dark/high-contrast themes  

---

### 🌍 `cesium.css` — Cesium 3D Styling

Defines styles for:

- Cesium canvas container  
- 3D globe overlays (e.g., grid lines, bounding overlays)  
- Timeline + animation controls (if used)  
- Attribution area  

Constraints:

- Must not diminish legibility of 3D overlays (like sovereignty areas)  
- Must maintain accessible contrast for all textual overlays  
- Must coordinate with themes to keep UI visually coherent with 2D maps  

---

### 🧱 `layers.css` — Layer-Specific Styling

Defines styling for:

- Administrative boundaries  
- Rivers & hydrology lines  
- Trails, railways, roads  
- Historical overlays (treaty lines, forts, etc.)  
- Environmental overlays (e.g., drought indices, land cover)  

Rules:

- All colors must be derived from design tokens via theme variables  
- Must provide **visually distinct, yet accessible** line/area styling  
- Must not encode governance meaning (CARE, sovereignty) without the respective governance components  
- Must avoid saturated or confusing color ramps that could misrepresent risk/severity  

---

### 📊 `legends.css` — Legend Layout & Styling

Defines legend styling for:

- Map legends with color ramps and patterns  
- Layer symbolization preview items  
- H3 masking and sovereignty indications  
- Legend titles and descriptive text  

Requirements:

- Layout must remain readable on small viewports  
- Swatches must be WCAG AA-compliant in all themes  
- Text must clearly describe any CARE/masking semantics  
- Must work with A11y helpers to provide SR-only descriptions where necessary  

---

### 🧊 `masking.css` — H3 & Masking Visuals

Defines:

- Visualization for H3 cell grids (hexes or equivalent shapes)  
- Styles for masked or generalized regions  
- Visual representation of sovereignty-protected or culturally sensitive zones  

Governance constraints:

- Masking visuals **must clearly indicate** that exact locations are generalized  
- Masked layers must visually differ from “normal” unmasked layers  
- Masking must not be subtle, ambiguous, or easily confused with other overlays  
- Any style changes here must not **reduce the clarity** of masking as an ethical safeguard  

---

### 🧭 `hud.css` — Map HUD Styling

Defines UI for:

- Cursor HUD (coarse coordinate/region readout)  
- Debug/diagnostic overlays (if enabled in dev)  
- Layer status HUDs (used in dev features or advanced views)  

Constraints:

- HUD must not interfere with accessibility or essential controls  
- Text must be legible and theme-aware  
- HUD positioning must avoid blocking essential map content (e.g., sovereignty boundaries, warnings)  

---

## ♿ Accessibility Requirements

Map-specific styles must:

- Ensure all map controls have clear focus outlines (when combined with mixins)  
- Maintain adequate contrast for all labels and overlays  
- Respect reduced-motion for interactions:
  - No purely decorative transitions or animations on map/HUD  
- Work well with:
  - Large text mode  
  - High-contrast theme  
  - Screen readers (for necessary textual overlays)  

Any map styling change must not degrade:

- The ability to see CARE labels, warnings, and masked areas  
- The readability of key map UI under different themes  

---

## 🔐 FAIR+CARE & Governance Constraints

Map styles are deeply connected to governance:

- Sovereignty-related overlays must remain visually prioritized and recognizable  
- Masked grids must **not** resemble non-sensitive layers; they must be obviously distinct  
- CARE-coded overlays must use consistent color semantics as defined by tokens/themes  
- Styles may **not** hide or mute serious warnings or governance indication in any theme  

If a new map style would hide or confuse:

- CARE labels  
- SovereigntyNotice  
- MaskingIndicator  

…it is **not allowed** and must be redesigned before merge.

---

## 📈 Telemetry & Observability

Map styles themselves do not send telemetry, but they influence:

- User behavior (what gets clicked / interacted with)  
- A11y event rates (keyboard vs mouse usage)  
- Potential misclicks if visual design is confusing  

When making significant map styling changes, observability dashboards should be monitored for:

- Changes in map interaction patterns  
- A11y usage metrics  
- Governance-related user flows (e.g., less/more interaction with sovereignty layers)

---

## 🧪 Testing Requirements

Suggested tests:

- **Visual regression tests** of key map views:
  - Masked vs unmasked overlays  
  - Legend readability  
  - Map controls focus outlines  

- **A11y checks:**
  - Contrast ratios for map labels and controls  
  - Focus visibility on controls  
  - Visibility of CARE/masking visuals in all themes  

- **Theming tests:**
  - Map UI under light/dark/high-contrast themes  
  - Legends & overlays in theme combinations  

Failures in any of the above should be treated as CI-blocking for map-related PRs.

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Introduced map styling spec; aligned maplibre/cesium/legends/masking with tokens & themes |
| v10.3.2 | 2025-11-14 | Hardened CARE/sovereignty overlay styling in maps                      |
| v10.3.1 | 2025-11-13 | Initial map-specific styles for MapLibre and base legends             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

