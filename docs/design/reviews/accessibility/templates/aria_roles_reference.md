<div align="center">

# 🧭 Kansas Frontier Matrix — ARIA Roles & Landmark Reference  
`docs/design/reviews/accessibility/templates/aria_roles_reference.md`

**Purpose:** Provide a definitive guide for applying **ARIA roles, landmarks, and live regions** across the Kansas Frontier Matrix (KFM) web interface — ensuring consistent, semantic accessibility across React, MapLibre, and HTML5 Canvas components.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](../wcag_checklist.md)
[![ARIA Spec](https://img.shields.io/badge/WAI--ARIA-1.2-blue)](https://www.w3.org/TR/wai-aria-1.2/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🎯 Purpose

Kansas Frontier Matrix uses **semantic HTML + WAI-ARIA 1.2** to make maps, timelines, and AI interfaces perceivable by assistive technologies (screen readers, braille displays, speech input).  
This reference standardizes which **roles, properties, and landmarks** are used and how they map to KFM UI components.

---

## 🗺️ Landmark Roles (Page Structure)

| Region | HTML Element | ARIA Role | Description / Usage |
|---------|----------------|------------|---------------------|
| Site Header | `<header>` | `banner` | Top-level navigation area; contains logo, global search, and language selector. |
| Global Navigation | `<nav>` | `navigation` | Main navigation links or menus; must be labeled (`aria-label="Primary Navigation"`). |
| Main Content | `<main>` | `main` | Primary content region of the page. |
| Sidebar / Layer Controls | `<aside>` | `complementary` | Contextual sidebar for filters or map layer toggles. |
| Timeline Canvas Container | `<section>` | `region` | Identified via `aria-labelledby="timeline-title"`. |
| AI Assistant Drawer | `<section>` | `complementary` | Interactive chat area with focus trap; `aria-label="AI Assistant"`. |
| Footer | `<footer>` | `contentinfo` | Global footer with project metadata and links. |

---

## 🔘 Widget & Control Roles

| Control Type | HTML Element | ARIA Role / Property | Notes |
|---------------|--------------|----------------------|-------|
| Button | `<button>` | `button` | Use native element unless custom. |
| Toggle Button | `<div>` / `<span>` | `button` + `aria-pressed="true/false"` | For map layer toggles. |
| Checkbox | `<input type="checkbox">` | `checkbox` | Use in layer visibility or legend toggles. |
| Radio Group | `<input type="radio">` | `radio` + `role="radiogroup"` | Used for mode selections (e.g., basemap themes). |
| Slider / Range | `<input type="range">` | `slider` | For timeline scrubbing; include `aria-valuenow`, `aria-valuemin`, `aria-valuemax`. |
| Link | `<a>` | `link` | Must have descriptive link text. |
| Tooltip | `<div>` | `tooltip` | Use with `aria-describedby` for trigger element. |
| Dialog / Modal | `<div>` | `dialog` + `aria-modal="true"` | For AI Assistant drawer or detail modals. |
| Search Field | `<input>` | `searchbox` | Use with `role="search"` in parent container. |
| Menu / Dropdown | `<ul>` / `<li>` | `menu`, `menuitem` | For header and layer context menus. |
| Progress | `<progress>` | `progressbar` | Use for loading indicators (data fetch). |

---

## 📢 Live Regions (Dynamic Updates)

| Use Case | ARIA Property | Value | Notes |
|-----------|----------------|--------|-------|
| AI Assistant Response | `aria-live` | `polite` | Announces generated replies without interrupting user. |
| System Notifications | `aria-live` | `assertive` | For urgent events (errors, warnings). |
| Timeline Updates | `role="status"` | — | Announce time change when user scrubs timeline. |
| Map Loading State | `aria-busy="true"` | until map renders | Must toggle to false when ready. |
| Search Suggestions | `aria-autocomplete="list"` | with `aria-expanded` and `aria-owns` | For global search input. |

---

## 🧩 MapLibre / Canvas Accessibility

| Element | Implementation | ARIA Strategy |
|----------|----------------|----------------|
| Map Toolbar | `<div role="toolbar">` | Group zoom, locate, layer buttons; ensure `tabindex="0"` |
| Map Marker Popups | `<div role="dialog">` | Provide `aria-labelledby` for title and `aria-describedby` for content. |
| Canvas Timeline | `<canvas>` + `<div role="region">` | Provide textual description via `aria-label` or `aria-describedby`. |
| Map View | `<div role="application">` | Avoid nested `application` roles; limit to one per page. |
| Dynamic Layers | `<g role="group">` (SVG overlay) | Label via `aria-labelledby`. |

---

## 🧠 ARIA States & Properties Reference

| Property | Description | Usage Example |
|-----------|--------------|----------------|
| `aria-expanded` | Indicates toggle state of collapsible UI. | Used for layer menus or accordions. |
| `aria-controls` | Identifies the element controlled by trigger. | Header menu → dropdown list. |
| `aria-pressed` | Toggle button pressed state. | Map layer on/off buttons. |
| `aria-current` | Marks current item in a set. | Active page or selected timeline event. |
| `aria-describedby` | Associates contextual help text. | Tooltips, map legends. |
| `aria-labelledby` | Names an element via visible label. | Section headers → content regions. |
| `aria-hidden="true"` | Hides decorative elements from AT. | Background icons, purely visual SVGs. |
| `tabindex="0"` | Adds element to keyboard order. | Custom controls. |

---

## 🪶 Example Layout (ARIA Landmark Map)

```mermaid
flowchart TD
  A["<header role='banner'>\nGlobal Navigation"] --> B["<main role='main'>\nPrimary Content"]
  B --> C["<section role='region'>\nTimeline Canvas"]
  B --> D["<section role='application'>\nMapLibre Map View"]
  D --> E["<aside role='complementary'>\nLayer Controls"]
  B --> F["<section role='complementary'>\nAI Assistant Drawer"]
  B --> G["<footer role='contentinfo'>\nMetadata & License"]
<!-- END OF MERMAID -->


⸻

🧾 Provenance Metadata Example

review_id: "aria_roles_ref_v1"
reviewed_by: ["@accessibility-team"]
commit: "{{ GIT_COMMIT }}"
wcag_level: "AA"
aria_version: "1.2"
conformance: "Pass"
notes: "Landmarks and roles reviewed for MapLibre and Timeline UI"


⸻

🪪 License

Released under Creative Commons CC-BY 4.0
© 2025 Kansas Frontier Matrix Design Collective

⸻



