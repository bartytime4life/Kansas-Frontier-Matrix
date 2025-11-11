---
title: "🧩 Kansas Frontier Matrix — Accessible UI Patterns & Components (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-patterns-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Accessible UI Patterns & Components**
`docs/accessibility/patterns/README.md`

**Purpose:**  
Define inclusive UI patterns for **Kansas Frontier Matrix (KFM)** components — ensuring consistent **keyboard operability**, **screen reader support**, and **WCAG 2.1 AA** compliance across the web application and embedded data visualization environments.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

Accessible UI patterns form the **foundation of user equity** in the Kansas Frontier Matrix interface.  
These reusable patterns ensure that components — from **buttons** and **dialogs** to **interactive maps** — meet high standards for usability, responsiveness, and cultural inclusivity.  
Each pattern includes **ARIA semantics**, **keyboard interaction rules**, **focus management**, and **inclusive design guidance** to align with FAIR+CARE principles.

**Coverage Areas**
- Universal keyboard & screen reader interactions  
- Component-level ARIA & labeling  
- Accessible visualizations (MapLibre, D3, Cesium)  
- Focus Mode interaction and consent patterns  
- Mobile & reduced-motion adaptations  

---

## 🗂️ Directory Layout

```
docs/accessibility/patterns/
├── README.md              # This file
├── buttons.md             # Accessible buttons and toggle patterns
├── dialogs.md             # Modal, alert, and drawer interactions
├── map-controls.md        # Accessible geospatial & map widgets
├── charts.md              # Accessible charts and data visualizations
├── navigation.md          # Menus, breadcrumbs, and skip-links
└── forms.md               # Input controls and validation messaging
```

---

## ♿ Pattern Foundations

| Category | Principle | Description |
|---|---|---|
| **Keyboard Operability** | All components usable with keyboard-only navigation. | Supports Tab, Shift+Tab, Enter, Space, Arrow keys, Esc. |
| **Screen Reader Support** | Semantic markup and ARIA roles announce structure and state. | Follows WAI-ARIA 1.2 Authoring Practices. |
| **Focus Management** | Predictable focus order and visible focus rings (≥3:1 contrast). | Uses logical DOM order and focus trapping for modals. |
| **Motion Sensitivity** | Respects user’s `prefers-reduced-motion` settings. | Animations disabled or simplified automatically. |
| **Cultural Sensitivity** | Text and iconography avoid bias or harmful symbolism. | FAIR+CARE-aligned content validation. |

---

## 🧭 Global Accessibility Tokens

These design tokens unify a11y behavior across UI components.

| Token | Type | Description |
|---|---|---|
| `a11y.focus.color` | Color | Focus indicator color (≥3:1 contrast) |
| `a11y.outline.width` | Spacing | 3px default outline width |
| `aria.expanded` | State | Used in menus and accordions |
| `aria.selected` | State | Identifies active or focused items |
| `aria.modal` | Boolean | True for dialogs and focus-trapped content |
| `a11y.skiplinks.enabled` | Boolean | Activates skip-navigation links |

---

## 🧩 Component Pattern Summaries

### 🔘 Buttons & Toggles
- **Role:** `role="button"` with `tabindex="0"`.  
- **Interaction:** `Enter` and `Space` trigger action.  
- **ARIA:** Use `aria-pressed="true|false"` for toggles.  
- **Guidelines:** Always label buttons clearly with verbs (e.g., “Save Data”).  

### 💬 Dialogs & Modals
- **Role:** `role="dialog"` or `role="alertdialog"`.  
- **Focus Trap:** Use `focus-trap` utility to contain tab order.  
- **Escape Handling:** `Esc` closes modal; return focus to invoking element.  
- **ARIA:** Label with `aria-labelledby` and describe via `aria-describedby`.  

### 🗺️ Map Controls
- **Keyboard Access:** Arrow keys for panning; `+`/`-` or `=`/`_` for zooming.  
- **Live Regions:** Announce zoom level or active layer (`aria-live="polite"`).  
- **ARIA Roles:** `role="application"` with `aria-label="Interactive map"`.  
- **Layer List:** Treated as checkbox group with `aria-checked` and keyboard toggles.  

### 📊 Charts & Visualizations
- **Alt Representation:** Provide tabular summaries below each chart.  
- **ARIA:** Use `aria-roledescription="chart"` and `aria-label="Population by decade"`.  
- **Focus Management:** Navigable data points or annotations for keyboard users.  
- **Motion:** Avoid flashing elements (>3 Hz) to meet WCAG 2.3.1.  

### 📑 Navigation Menus
- **ARIA Roles:** `menubar`, `menuitem`, `menuitemcheckbox`, `menuitemradio`.  
- **Keyboard Shortcuts:** Left/Right arrows to move between items.  
- **Skip Links:** Provide skip-to-content and skip-to-map shortcuts at top of page.  
- **Active State:** Use `aria-current="page"` and `aria-expanded` for nested menus.  

### 📝 Forms & Inputs
- **Labels:** Use `<label for="input-id">` or `aria-label`.  
- **Error Feedback:** Provide descriptive text linked by `aria-describedby`.  
- **Color Independence:** Do not rely on color alone to show error states.  
- **Focus Return:** On validation error, move focus to first invalid field.  

---

## ⚙️ Validation & CI Automation

| Workflow | Validation Target | Artifact |
|---|---|---|
| `accessibility_scan.yml` | Component and page-level checks via axe-core | `reports/self-validation/web/a11y_summary.json` |
| `storybook-a11y.yml` | Storybook + Jest a11y snapshot testing | `reports/ui/a11y_component_audits.json` |
| `color-contrast.yml` | Validates design tokens for WCAG compliance | `reports/ui/color-contrast.json` |

---

## ⚖️ FAIR+CARE Integration for UI Patterns

| Care Principle | Application in UI |
|---|---|
| **Collective Benefit** | UI patterns tested by diverse user groups and screen-reader users. |
| **Authority to Control** | Cultural or Indigenous symbols used with proper consent and attribution. |
| **Responsibility** | Components versioned with accessibility regression tests. |
| **Ethics** | Dialogs and narrative outputs avoid exploitative or traumatic content. |

---

## 🧠 References & Tools

- [WAI-ARIA Authoring Practices 1.2](https://www.w3.org/TR/wai-aria-practices/)
- [Deque axe-core](https://www.deque.com/axe/)
- [WCAG 2.1 Checklist](https://www.w3.org/WAI/WCAG21/quickref/)
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)
- [FAIR+CARE Framework](../../standards/faircare.md)

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | A11y & FAIR+CARE Council | Created comprehensive accessible UI pattern library with ARIA specs, CI validation links, and component guidelines. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[Back to Accessibility Index](../README.md) · [Design Tokens](../../design/tokens/accessibility-tokens.md)

</div>
