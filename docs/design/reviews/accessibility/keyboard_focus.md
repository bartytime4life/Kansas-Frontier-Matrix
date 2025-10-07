<div align="center">

# ⌨️ Kansas Frontier Matrix — Accessibility Audit: Keyboard & Focus  
`docs/design/reviews/accessibility/keyboard_focus.md`

**Objective:** Validate that **all interactive UI components** within the Kansas Frontier Matrix (Map, Timeline, AI Drawer, Panels) are fully operable via **keyboard navigation**, with visible, accessible focus indicators that meet WCAG 2.1 AA.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#checklist)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Purpose

Keyboard accessibility ensures that **all KFM functionality**—navigation, timeline scrubbing, layer toggles, AI interaction—is usable without a mouse or touch input.  
Every interactive element must be reachable, operable, and clearly identifiable by focus state.

This audit covers:
- **Keyboard-only navigation** (Tab, Shift + Tab, Enter, Space, Arrow keys)
- **Focus management** (logical order, retention, visibility)
- **Skip links** and **focus trapping** in modals/drawers
- **ARIA practices** for focusable roles (`role="button"`, `tabindex="0"`, etc.)

---

## 🧭 Scope

| UI Region | Expected Behavior | WCAG Ref |
|------------|------------------|-----------|
| **Header / Navigation** | Tab order: logo → search → help → login; Escape closes menus | 2.1.1 / 2.4.3 |
| **Timeline (Canvas)** | Arrow keys navigate events; Tab moves to active event label | 2.1.1 / 2.4.7 |
| **Map (MapLibre GL)** | Tab focuses toolbar → layer toggles → zoom controls → legend | 2.1.1 / 2.4.3 |
| **AI Assistant Drawer** | Focus trapped while open; Escape closes; Shift+Tab cycles back | 2.1.2 / 2.4.3 |
| **Detail Panel** | Keyboard accessible scroll + close button | 2.1.1 |
| **Global Skip Link** | “Skip to Main Content” appears on Tab from body start | 2.4.1 |

---

## 🧩 Checklist

| # | Test | Expected | Status |
|----|------|-----------|---------|
| 1 | **Tab order** follows DOM reading sequence | Natural left–right, top–down | ✅ |
| 2 | **Focus visible** on all interactive items | ≥ 3 px outline, ≥ 3:1 contrast | ✅ |
| 3 | **No hidden traps** (user can always tab out) | Modals restore focus correctly | ✅ |
| 4 | **Keyboard triggers functional** | Enter / Space activate buttons & toggles | ✅ |
| 5 | **ARIA roles & tabindex applied** | Non-native elements are announced | ✅ |
| 6 | **Focus retained after action** | Re-focus on source element after close | ⚙️ (under test) |
| 7 | **Escape key** closes drawers, modals | Immediate, no residual focus | ✅ |
| 8 | **MapLibre overlays** navigable | Focus ring visible, labels announced | ⚙️ (pending MapLibre upgrade) |
| 9 | **Timeline scrubber** operable | Arrow keys, PgUp/PgDn adjust position | ✅ |
| 10 | **Skip link** appears and functions | Visible at first tab press | ✅ |

---

## 🧠 Test Setup

| Tool / Env | Purpose |
|-------------|----------|
| **Chrome + DevTools Accessibility Tree** | Verify focus order and tab stops |
| **NVDA (Windows)** / **VoiceOver (macOS)** | Confirm announcement and region landmarks |
| **Axe DevTools** / **Pa11y CI** | Automated keyboard traps detection |
| **Storybook A11y Addon** | Component-level regression tests |
| **Keyboard Simulation** | Chrome extension: emulate key sequences |

---

## 🧩 Focus Order Flow (Web App Overview)

```mermaid
flowchart LR
  A["Header\n(Logo → Search → Lang → Help)"] --> B["Sidebar\n(Layer Toggles → Legend)"]
  B --> C["Map Controls\n(Zoom → Locate → Timeline Link)"]
  C --> D["Timeline Canvas\n(Events → Scrubber)"]
  D --> E["Detail Panel\n(Read more → Close)"]
  E --> F["AI Assistant Drawer\n(Input → Send → Close)"]
  F --> G["Footer / Docs Link"]
<!-- END OF MERMAID -->


⸻

🧩 Focus Styling Tokens

Variable	Purpose	Example
--kfm-focus-outline	Primary outline color	 #3BAFDA
--kfm-focus-width	Outline thickness	3px
--kfm-focus-offset	Offset from element edge	2px
--kfm-focus-transition	Animation timing	0.1s ease-out

Focus outlines must never be removed (outline: none;) without an accessible alternative (box-shadow, border, etc.).

⸻

🧩 Recommendations
	1.	✅ Ensure tabindex=“0” on custom map controls or legend items.
	2.	✅ Add focus-visible utility class for consistent outline rendering.
	3.	⚙️ Implement focus trap for AI Assistant modal if user switches context mid-conversation.
	4.	⚙️ Test focus behavior in Firefox + NVDA (MapLibre differs in keyboard handling).
	5.	🧩 Add unit tests under tests/accessibility/focus.test.js to simulate tab navigation and Escape key handling.

⸻

🧾 Provenance

Field	Value
Reviewer(s)	@accessibility-team / @design-lead
Review Date	{{ ISO8601_DATE }}
Component Versions	Navigation v0.3.2, Timeline v0.4.0, Map Controls v0.5.1
Commit Hash	{{ GIT_COMMIT }}
Audit Tool	Axe Core v4.10.0 / Pa11y v7
Result	✅ AA Compliant (minor MapLibre patch pending)


⸻

🪪 License

Released under Creative Commons CC-BY 4.0
© 2025 Kansas Frontier Matrix Design Collective

⸻



