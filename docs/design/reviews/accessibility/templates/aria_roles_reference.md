<div align="center">

# 🧭 Kansas Frontier Matrix — ARIA Roles & Landmark Reference  
`docs/design/reviews/accessibility/templates/aria_roles_reference.md`

**Purpose:** Define consistent **ARIA roles, landmarks, and live-region usage** across the  
Kansas Frontier Matrix (KFM) interface — ensuring semantic accessibility in **React**,  
**MapLibre**, and **HTML5 Canvas** components following the **Master Coder Protocol (MCP)**.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](../wcag_checklist.md)  
[![ARIA Spec](https://img.shields.io/badge/WAI--ARIA-1.2-blue)](https://www.w3.org/TR/wai-aria-1.2/)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🎯 Objective

KFM adheres to **semantic HTML + WAI-ARIA 1.2** to ensure that maps, timelines, and AI panels are fully perceivable  
and operable by assistive technologies (screen readers, braille devices, and speech input).  
This document establishes **canonical ARIA usage patterns** and serves as a shared reference for developers and auditors.

---

## 🗺️ Landmark Roles (Page Structure)

| Region | HTML Element | ARIA Role | Description / Usage |
|---------|---------------|------------|----------------------|
| **Header** | `<header>` | `banner` | Top-level navigation region containing logo, global search, language selector. |
| **Navigation** | `<nav>` | `navigation` | Global menu; label with `aria-label="Primary Navigation"`. |
| **Main Content** | `<main>` | `main` | Central content of the app. Only one per page. |
| **Sidebar / Layers** | `<aside>` | `complementary` | Contextual filters or map layer toggles. |
| **Timeline Canvas** | `<section>` | `region` | Must have `aria-labelledby="timeline-title"`. |
| **AI Assistant Drawer** | `<section>` | `complementary` | Focus-trapped drawer; `aria-label="AI Assistant"`. |
| **Footer** | `<footer>` | `contentinfo` | Global footer with metadata and links. |

---

## 🔘 Widget & Control Roles

| Control Type | Element | ARIA Role / Attribute | Notes |
|---------------|----------|------------------------|-------|
| Button | `<button>` | `button` | Prefer native; if custom, add `role="button"` + keyboard handlers. |
| Toggle Button | `<div>` / `<span>` | `button` + `aria-pressed="true/false"` | For map layer toggles. |
| Checkbox | `<input type="checkbox">` | `checkbox` | For visibility toggles. |
| Radio Group | `<input type="radio">` | `radio` + parent `radiogroup` | For basemap/theme selection. |
| Slider | `<input type="range">` | `slider` + `aria-valuenow` | For timeline scrubber. |
| Link | `<a>` | `link` | Must have meaningful text. |
| Tooltip | `<div>` | `tooltip` + `aria-describedby` | Trigger element must own tooltip ID. |
| Dialog | `<div>` | `dialog` + `aria-modal="true"` | For AI Assistant or detail modals. |
| Search | `<input>` | `searchbox` | Enclose within `<form role="search">`. |
| Menu | `<ul>` / `<li>` | `menu` / `menuitem` | Used for context or layer menus. |
| Progress | `<progress>` | `progressbar` | Data loading indicators. |

---

## 📢 Live Regions (Dynamic Updates)

| Use Case | ARIA Property | Value | Notes |
|-----------|----------------|--------|-------|
| AI Assistant Responses | `aria-live` | `polite` | Announces generated replies non-intrusively. |
| System Alerts | `aria-live` | `assertive` | Interrupts to report urgent messages. |
| Timeline Updates | `role="status"` | — | Announces temporal range changes. |
| Map Loading | `aria-busy="true"` → `false` | — | Toggle while data is rendering. |
| Search Autocomplete | `aria-autocomplete` + `aria-expanded` | list | For global search input. |

---

## 🧭 MapLibre / Canvas Accessibility

| Element | Implementation | ARIA Strategy |
|----------|----------------|----------------|
| **Map Toolbar** | `<div role="toolbar">` | Group zoom, locate, and layer buttons; all focusable via `tabindex="0"`. |
| **Map Marker Popups** | `<div role="dialog">` | Provide `aria-labelledby` (title) + `aria-describedby` (body). |
| **Timeline Canvas** | `<canvas>` wrapped in `<div role="region">` | Include textual equivalent via `aria-label`. |
| **Map View** | `<div role="application">` | Use sparingly; only one per app. |
| **Dynamic Layers** | `<g role="group">` (SVG overlay) | Label with `aria-labelledby` for dataset name. |

---

## 🧠 ARIA States & Properties Reference

| Property | Description | Example Usage |
|-----------|--------------|----------------|
| `aria-expanded` | Indicates toggle state | Collapsible menus or drawers |
| `aria-controls` | Links control to target ID | Header menu → dropdown |
| `aria-pressed` | Indicates pressed toggle | Map layer toggles |
| `aria-current` | Marks current item | Active navigation item |
| `aria-describedby` | Associates with helper text | Tooltip reference |
| `aria-labelledby` | Associates with visible label | Section header → content |
| `aria-hidden="true"` | Hides element from AT | Decorative icons |
| `tabindex="0"` | Adds element to keyboard order | Custom controls |
| `role="status"` | Announces dynamic updates | Live region for map state |

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

  style A fill:#E6EFFF,stroke:#0074D9,stroke-width:2px
  style B fill:#F8F8FF,stroke:#6C63FF,stroke-width:1.5px
  style C fill:#FFFDE7,stroke:#FBC02D,stroke-width:1.5px
  style D fill:#E3F2FD,stroke:#1976D2,stroke-width:1.5px
  style E fill:#E8F5E9,stroke:#2E7D32,stroke-width:1.5px
  style F fill:#FFF3C4,stroke:#FFB700,stroke-width:2px
  style G fill:#FFF9C4,stroke:#F57F17,stroke-width:1.5px

  %% END OF MERMAID
````

---

## ⚙️ Continuous Integration (ARIA Validation)

```yaml
# .github/workflows/a11y_aria_validate.yml
on:
  pull_request:
    paths:
      - "web/src/**/*.tsx"
      - "docs/design/reviews/accessibility/templates/aria_roles_reference.md"
jobs:
  aria:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install accessibility tools
        run: npm i -g axe-core-cli
      - name: Run ARIA validation
        run: axe --url http://localhost:3000 --tags=aria
```

> **Note:** All ARIA validations must pass with **0 critical violations** before merge approval.
> Include resulting reports in PR artifacts for audit traceability.

---

## 🧾 Provenance Metadata Example

```yaml
review_id: "aria_roles_ref_v1"
reviewed_by: ["@accessibility-team"]
commit: "{{ GIT_COMMIT }}"
wcag_level: "AA"
aria_version: "1.2"
conformance: "Pass"
notes: "Landmarks and roles verified for React + MapLibre components"
```

---

## 🪪 License

Released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Design Collective

---

<div align="center">

### 🧭 Kansas Frontier Matrix — Semantic Accessibility Framework

**Structured · Auditable · Inclusive**

</div>
