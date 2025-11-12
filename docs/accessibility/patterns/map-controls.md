---
title: "🗺️ Kansas Frontier Matrix — Accessible Map Controls & Geospatial Interactions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/map-controls.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-map-controls-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Accessible Map Controls & Geospatial Interactions**
`docs/accessibility/patterns/map-controls.md`

**Purpose:**  
Define accessible interaction standards for **MapLibre, Cesium, and Recharts map controls** within KFM’s geospatial interfaces — ensuring compliance with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **FAIR+CARE** principles governing cultural, environmental, and ethical data visualization.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Map controls provide primary spatial interaction in the **Kansas Frontier Matrix (KFM)** platform.  
Accessible map interaction ensures **keyboard navigability**, **ARIA feedback**, and **ethical control over sensitive layers** (e.g., archaeological sites, tribal data).

**Control Types**
- Pan, zoom, and rotation controls  
- Layer toggle and legend visibility  
- Temporal scrubbers for Focus Mode  
- Feature popups, tooltips, and consent overlays  

---

## 🧩 Accessibility Standards

| Principle | Description | WCAG / Standard |
|------------|--------------|-----------------|
| **Keyboard Access** | All controls accessible via `Tab`, `Enter`, and `Space`. | WCAG 2.1.1 |
| **Screen Reader Feedback** | Live updates announce zoom levels and active layers. | WAI-ARIA 1.2 |
| **Focus Management** | Focus indicators persist across map movements. | WCAG 2.4.7 |
| **Motion Sensitivity** | Honor `prefers-reduced-motion` for camera animations. | WCAG 2.3.3 |
| **Cultural Consent** | Restricted overlays masked until consent toggled. | FAIR+CARE |
| **Tooltip Alternatives** | ARIA labels describe all map icons and layer controls. | WCAG 1.1.1 |

---

## 🧭 Example Implementation

```html
<div role="region" aria-label="Interactive Map Viewer">
  <div class="map-controls">
    <button
      class="zoom-in"
      aria-label="Zoom in"
      data-action="zoom-in"
    >+</button>
    <button
      class="zoom-out"
      aria-label="Zoom out"
      data-action="zoom-out"
    >−</button>
    <button
      class="toggle-layer"
      aria-pressed="false"
      aria-label="Toggle hydrology layer"
      data-layer="hydrology"
    >💧</button>
  </div>

  <div
    id="map-canvas"
    role="application"
    aria-roledescription="Interactive map"
    aria-live="polite"
  ></div>
</div>
```

**Implementation Notes**
- The map container must use `role="application"` to enable assistive navigation context.  
- Buttons use `aria-label` and `aria-pressed` for dynamic layer toggles.  
- Focus outlines remain visible during panning and zooming.  
- Live announcements reflect map changes (`aria-live="polite"`).  

---

## 🎨 Design Tokens

| Token | Description | Example |
|--------|-------------|---------|
| `map.control.bg` | Background for buttons and panels | `#263238` |
| `map.control.icon.color` | Icon color | `#FFFFFF` |
| `map.focus.outline` | Focus ring for active control | `#FFD54F` |
| `map.layer.active.color` | Active layer toggle color | `#4CAF50` |
| `map.layer.sensitive.mask` | Mask overlay color for restricted data | `#00000099` |

---

## ⚙️ Keyboard & ARIA Matrix

| Key | Action | Notes |
|------|--------|-------|
| `Tab` | Move between map controls | Logical traversal order |
| `Enter` / `Space` | Activate control (zoom, toggle layer) | Always trigger visual feedback |
| `Arrow Keys` | Pan map (up, down, left, right) | Maintain ARIA live announcements |
| `+` / `-` | Zoom map | Announce “Zoom level X” via `aria-live` |
| `Esc` | Close tooltips, modals, or legends | Return focus to map canvas |
| `aria-pressed` | Reflects toggle state for active layers | Boolean true/false |
| `aria-hidden` | Masks sensitive layers without consent | Enforced for cultural sites |

---

## 🧾 FAIR+CARE Ethical Controls

| Feature | Implementation |
|----------|----------------|
| **Consent Toggles** | Map overlays for cultural or sacred sites require explicit opt-in. |
| **Layer Audit Trails** | Each layer change event logged with timestamp and user ID. |
| **Opacity Control** | Sensitive overlays auto-fade to 40% opacity. |
| **Legend Annotation** | Cultural and ecological data include ethical attribution. |

Example Consent Switch:
```html
<button
  class="consent-toggle"
  aria-pressed="false"
  aria-label="Enable cultural layer with consent"
>
  🪶 Cultural Data
</button>
```

---

## 🧪 Validation & Testing

| Tool | Scope | Output |
|-------|--------|--------|
| **axe-core** | ARIA / focus / live region validation | `reports/self-validation/web/a11y_map_controls.json` |
| **Lighthouse CI** | Keyboard flow and focus states | `reports/ui/lighthouse_map_controls.json` |
| **jest-axe** | React/MapLibre component tests | `reports/ui/a11y_map_components.json` |
| **Manual Audit** | Keyboard + screen reader geospatial traversal | FAIR+CARE QA log |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Maps reveal shared ecological and cultural insights ethically. |
| **Authority to Control** | Users determine consent visibility of restricted overlays. |
| **Responsibility** | Layer and zoom telemetry logged for transparency. |
| **Ethics** | Map symbols and legends validated for cultural respect. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Established accessible map control patterns, consent toggles, and FAIR+CARE layer governance. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to A11y Patterns Index](README.md) · [Next → Charts](charts.md)

</div>
