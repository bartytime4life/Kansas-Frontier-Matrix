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
- Accessible visualizations (MapLibre, D3, Recharts, Cesium)  
- Focus Mode interaction & consent patterns  
- Mobile & reduced-motion adaptations  

---

## 🗂️ Directory Layout

```
docs/accessibility/patterns/
├── README.md                 # This file
├── alerts.md                 # Live regions, role="alert"/"status", toasts
├── buttons.md                # Accessible buttons and toggle patterns
├── charts.md                 # Accessible charts and data visualizations
├── dialogs.md                # Modal, alertdialog, drawer interactions
├── forms.md                  # Input controls and validation messaging
├── map-controls.md           # Accessible geospatial & map widgets
├── media.md                  # Video, audio, captions, transcripts
├── navigation.md             # Menus, breadcrumbs, skip-links
└── tables.md                 # Semantic tables & ARIA grids
```

---

## ♿ Pattern Foundations

| Category | Principle | Description |
|---|---|---|
| **Keyboard Operability** | All components usable with keyboard-only navigation. | Supports Tab, Shift+Tab, Enter, Space, Arrow keys, Esc. |
| **Screen Reader Support** | Semantic markup and ARIA roles announce structure and state. | Follows WAI-ARIA 1.2 Authoring Practices. |
| **Focus Management** | Predictable focus order and visible focus rings (≥3:1 contrast). | Logical DOM order; focus trap for modals; return focus on close. |
| **Motion Sensitivity** | Respects user’s `prefers-reduced-motion` settings. | Animations disabled or simplified automatically. |
| **Cultural Sensitivity** | Text, iconography, and visuals avoid bias/harm; consent surfaced. | FAIR+CARE-aligned content validation. |

---

## 🧭 Global Accessibility Tokens

These design tokens unify a11y behavior across UI components (see `../../design/tokens/accessibility-tokens.md`).

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

### 🔘 Buttons & Toggles (`buttons.md`)
- **Role:** `role="button"` with `tabindex="0"` if not native.  
- **Interaction:** `Enter` and `Space` trigger action.  
- **ARIA:** `aria-pressed="true|false"` for toggles.  
- **Guidelines:** Use clear, verb-led labels (e.g., “Save data”).

### 💬 Dialogs & Modals (`dialogs.md`)
- **Role:** `role="dialog"` or `role="alertdialog"`.  
- **Focus Trap:** Contain tab order in dialog; restore focus to opener on close.  
- **ARIA:** `aria-labelledby` for title; `aria-describedby` for content.

### 🚨 Alerts & Live Regions (`alerts.md`)
- **Polite vs. Assertive:** Use `role="status"` (polite) for non-urgent; `role="alert"` (assertive) for urgent.  
- **Toasts:** Dismissible, `Esc` closable; do not steal focus.  
- **Fair Tone:** Avoid alarmist copy; provide actionable next steps.

### 🗺️ Map Controls (`map-controls.md`)
- **Keyboard Access:** Arrow keys pan; `+/-` zoom; Tab cycles controls.  
- **Live Regions:** Announce zoom level, active layers (`aria-live="polite"`).  
- **Consent:** Cultural overlays require visible consent flags.

### 📈 Charts & Visualizations (`charts.md`)
- **Structure:** `role="figure"` + labels; data table alt or CSV.  
- **Keyboarding:** Arrow keys move focus among data points; `Esc` exits.  
- **Color Independence:** Distinguish series via shape/patterns; maintain contrast.

### 📝 Forms & Inputs (`forms.md`)
- **Labels:** Visible `<label for="…">` or `aria-label`; never rely on placeholder.  
- **Errors:** `aria-invalid`, `aria-describedby`, and polite live feedback.  
- **Consent:** FAIR+CARE checkbox for data use and cultural governance.

### 🧭 Navigation (`navigation.md`)
- **Landmarks:** `<header>`, `<nav>`, `<main>`, `<footer>`; skip-to-content links.  
- **Menus:** Keyboard operable; `aria-current="page"` for breadcrumbs.

### 📊 Tables & Grids (`tables.md`)
- **Semantics:** `<table>`, `<thead>`, `<tbody>`, `<th scope="…">`.  
- **Grids:** `role="grid"` with `aria-sort`, roving tabindex for large datasets.

### 🎥 Media & Time-Based Content (`media.md`)
- **Captions & Transcripts:** Required for all AV content.  
- **Controls:** Fully keyboard operable; no auto-play; visible focus.

---

## ⚙️ Validation & CI Automation

| Workflow | Validation Target | Artifact |
|---|---|---|
| `accessibility_scan.yml` | Axe/Lighthouse checks (roles, labels, headings) | `reports/self-validation/web/a11y_summary.json` |
| `storybook-a11y.yml` | Component snapshots and jest-axe tests | `reports/ui/a11y_component_audits.json` |
| `color-contrast.yml` | Token contrast thresholds | `reports/ui/color-contrast.json` |
| `faircare-visual-audit.yml` | Ethical tone & consent metadata checks | `reports/faircare-visual-validation.json` |

---

## ⚖️ FAIR+CARE Integration for UI Patterns

| Care Principle | Application in UI |
|---|---|
| **Collective Benefit** | Patterns tested by diverse user groups and assistive tech users. |
| **Authority to Control** | Cultural/Indigenous symbols used only with consent and attribution. |
| **Responsibility** | Components versioned with a11y regression tests and telemetry. |
| **Ethics** | Dialogs, alerts, and narratives avoid exploitative or traumatic content. |

---

## 🧠 References & Tools

- [WAI-ARIA Authoring Practices 1.2](https://www.w3.org/TR/wai-aria-practices/)  
- [Deque axe-core](https://www.deque.com/axe/)  
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)  
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)  
- [FAIR+CARE Framework](../../standards/faircare.md)

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | A11y & FAIR+CARE Council | Updated directory layout and pattern index; added alerts, media, and tables coverage; aligned with FAIR+CARE, WCAG 2.1 AA, and CI pipelines. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[Back to Accessibility Index](../README.md) · [A11y Checklists](../checklists/README.md)

</div>