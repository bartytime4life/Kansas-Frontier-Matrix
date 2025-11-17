---
title: "🗺️ Kansas Frontier Matrix — Accessible Map Controls & Geospatial Interactions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/map-controls.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-map-controls-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-map-controls"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Moderate"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/map-controls.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-map-controls.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-map-controls-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-map-controls-v10.4.1"
semantic_document_id: "kfm-doc-a11y-map-controls"
event_source_id: "ledger:docs/accessibility/patterns/map-controls.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Document"
jurisdiction: "United States / Kansas"
role: "a11y-pattern-map-controls"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next map-controls standard update"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Accessible Map Controls & Geospatial Interactions**  
`docs/accessibility/patterns/map-controls.md`

**Purpose:**  
Define accessible interaction standards for **MapLibre, Cesium, Recharts, and other geospatial controls** within KFM’s map interfaces — ensuring compliance with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, **XAUR**, and **FAIR+CARE** principles governing cultural, environmental, and ethical data visualization.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Map controls are the primary interaction surface for KFM’s geospatial experiences, including:

- 2D MapLibre views  
- 3D Cesium scenes  
- Time-dynamic overlays and Focus Mode timelines  
- Feature selection, filtering, and consent-based overlays  

This pattern ensures that:

- All map controls are keyboard navigable  
- ARIA feedback is provided for changes in zoom, position, and layers  
- Sensitive layers (e.g., archaeological, tribal, refuge) respect FAIR+CARE consent models  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── map-controls.md                 # This file
    ├── media.md
    ├── navigation.md
    ├── network-infrastructure.md
    ├── notifications.md
    ├── minerals-energy.md
    ├── microbiology-ecosystem-health.md
    ├── parks-conservation.md
    ├── planetarium-3d.md
    ├── pollinators-ecosystem-services.md
    ├── prairie-restoration.md
    ├── rail-transit.md
    ├── soil-health.md
    ├── space-remote-sensing.md
    ├── system-controls.md
    ├── tables.md
    ├── telemetry-streams.md
    ├── testing-validation.md
    ├── tooltips.md
    ├── transportation-mobility.md
    ├── urban-planning.md
    ├── vehicle-logistics.md
    └── wildlife-tracking.md
```

---

## 🧩 Accessibility Standards

| Principle             | Description                                                | WCAG / Standard |
|-----------------------|------------------------------------------------------------|-----------------|
| Keyboard Access       | All controls accessible via Tab, Enter, and Space.        | WCAG 2.1.1      |
| Screen Reader Feedback| Live updates announce zoom, center, and active layers.     | WAI-ARIA 1.2    |
| Focus Management      | Focus indicators persist while panning/zooming.           | WCAG 2.4.7      |
| Motion Sensitivity    | Camera motion honors `prefers-reduced-motion`.            | WCAG 2.3.3      |
| Cultural Consent      | Restricted overlays masked unless consent toggled.        | FAIR+CARE       |
| Tooltip Alternatives  | ARIA labels describe all map icons and layer controls.    | WCAG 1.1.1      |

---

## 🧭 Example Implementation

~~~html
<div role="region" aria-label="Interactive Map Viewer">
  <div class="map-controls">
    <button
      class="zoom-in"
      aria-label="Zoom in"
      data-action="zoom-in"
    >
      +
    </button>
    <button
      class="zoom-out"
      aria-label="Zoom out"
      data-action="zoom-out"
    >
      −
    </button>
    <button
      class="toggle-layer"
      aria-pressed="false"
      aria-label="Toggle hydrology layer"
      data-layer="hydrology"
    >
      💧
    </button>
  </div>

  <div
    id="map-canvas"
    role="application"
    aria-roledescription="Interactive map"
    aria-live="polite"
  ></div>
</div>
~~~

### Implementation Notes

- `role="region"` with `aria-label` wraps the map experience.  
- `role="application"` on the canvas establishes an advanced navigation context for assistive tech.  
- `aria-pressed` communicates stateful layer toggles.  
- All map interactions should be mirrored by keyboard operations and ARIA feedback.  

---

## 🎨 Design Tokens

| Token                     | Description                              | Example Value |
|---------------------------|------------------------------------------|---------------|
| map.control.bg            | Background for buttons and panels        | #263238       |
| map.control.icon.color    | Icon color for controls                  | #FFFFFF       |
| map.focus.outline         | Focus ring color                         | #FFD54F       |
| map.layer.active.color    | Active layer toggle color                | #4CAF50       |
| map.layer.sensitive.mask  | Mask overlay color for restricted layers | #00000099     |

---

## ⚙️ Keyboard & ARIA Matrix

| Key / Attribute    | Action                                      | Notes                                               |
|--------------------|---------------------------------------------|-----------------------------------------------------|
| Tab                | Move between map controls                   | Logical traversal order required                    |
| Enter / Space      | Activate control (zoom, toggle layer)      | Must trigger both visual + ARIA feedback            |
| Arrow Keys         | Pan map (up, down, left, right)            | Should announce direction / region via `aria-live`  |
| `+` / `-`          | Zoom map                                   | Announce “Zoom level X” through a status region     |
| Esc                | Close tooltips, modals, or legends         | Return focus to the map canvas                      |
| aria-pressed       | Indicates toggle layer on/off state        | Boolean true/false maintained via JS                |
| aria-hidden        | Used to hide sensitive layers sans consent | Required on sensitive overlay containers            |

---

## 🧾 FAIR+CARE Ethical Controls

| Feature            | Implementation                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| Consent Toggles    | Overlays for cultural or sacred sites require explicit opt-in from consent UI. |
| Layer Audit Trails | Each layer toggle event logged with timestamp, user, and dataset ID.           |
| Opacity Control    | Sensitive overlays auto-fade to reduced opacity for contextual awareness.      |
| Legend Annotation  | Cultural and ecological data include ethical attribution in legends and notes. |

### Example Consent Switch

~~~html
<button
  class="consent-toggle"
  aria-pressed="false"
  aria-label="Enable cultural layer with consent"
>
  🪶 Cultural Data
</button>
~~~

---

## 🧪 Validation & Testing

| Tool           | Scope                                      | Output                                      |
|----------------|--------------------------------------------|---------------------------------------------|
| axe-core       | ARIA, roles, focus, and live-region checks | a11y_map_controls.json                      |
| Lighthouse CI  | Keyboard flow, focus states, performance   | lighthouse_map_controls.json                |
| jest-axe       | Component-level map control tests          | a11y_map_components.json                    |
| Manual Audit   | Keyboard + screen reader spatial traversal | FAIR+CARE QA logs                           |

Validation ensures:

- No control is inaccessible via keyboard alone.  
- Focus states remain visible during panning, zooming, or layer changes.  
- Live-region announcements remain concise and meaningful.  

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| Collective Benefit  | Maps reveal ecological and cultural patterns in ways that aid all communities. |
| Authority to Control| Communities and custodians determine when restricted layers become visible.    |
| Responsibility      | Layer and zoom interactions logged for governance and audit.                   |
| Ethics              | Map symbology and narrative labels vetted for cultural respect and context.    |

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                     |
|--------:|------------|------------------------|---------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council  | Upgraded to KFM-MDP v10.4.3; added extended metadata, consent semantics, and one-box-safe formatting. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Established accessible map control patterns, consent toggles, and FAIR+CARE layer governance.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to A11y Patterns Index](../README.md) · [Next → Charts](charts.md)

</div>