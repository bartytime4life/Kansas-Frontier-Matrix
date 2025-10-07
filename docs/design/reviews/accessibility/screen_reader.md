<div align="center">

# 🗣 Kansas Frontier Matrix — Accessibility Audit: Screen Reader  
`docs/design/reviews/accessibility/screen_reader.md`

**Goal:** Guarantee that every component of the Kansas Frontier Matrix web UI is fully perceivable and navigable using screen-reader technologies (NVDA, JAWS, VoiceOver, Orca).  
Accessibility is a first-class citizen of the Master Coder Protocol (MCP): if it’s not accessible, it’s not reproducible.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#summary-results)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY-4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Purpose

This audit validates the **semantic correctness**, **ARIA roles**, and **screen-reader readability** of the KFM user interface—across all views (MapLibre map, Timeline Canvas, AI Assistant, and Detail Panels).  
It ensures that every interactive region has an accessible name, role, and state.

---

## 🧭 Scope

| Region | Description | Assistive Features Tested |
|---------|--------------|---------------------------|
| **Header & Navigation** | Branding, global search, language toggle, help menu | ARIA landmarks (`role="banner"`, `nav`); skip links |
| **Timeline Canvas** | Chronological event visualization | Accessible name for range input; keyboard focus announcements |
| **Map View (MapLibre)** | Map overlays and markers | `aria-label`, `aria-describedby` on controls and popups |
| **Layer Controls** | Toggles, legends, opacity sliders | Live updates to `aria-pressed` and dynamic labels |
| **AI Assistant Panel** | Chat region + history | `aria-live="polite"` for responses; focus management |
| **Detail Panel** | Event/Entity details | Headings hierarchy + `role="region"` for segmentation |

---

## 🧩 Checklist (WCAG 2.1 AA + ARIA 1.2)

| # | Requirement | Status | Notes |
|----|--------------|--------|-------|
| 1 | Landmarks used (`header`, `nav`, `main`, `footer`) | ✅ | Verified by NVDA |
| 2 | Every interactive element has an accessible name | ✅ | Buttons, toggles labeled via `aria-label` |
| 3 | Dynamic content updates via `aria-live` or `role="status"` | ✅ | AI responses and alerts correctly announced |
| 4 | Headings follow a logical hierarchy (`h1`–`h4`) | ✅ | Confirmed with VoiceOver rotor |
| 5 | Focused elements announced with role + name | ✅ | Timeline and map controls tested |
| 6 | No redundant announcements (e.g., duplicate alt text) | ✅ | Cleaned up nested labels |
| 7 | Modal focus trap preserves screen-reader context | ⚙️ | Works, but needs retest post React update |
| 8 | MapLibre controls exposed to accessibility tree | ⚙️ | Pending upstream MapLibre patch |
| 9 | Timeline Canvas has accessible summary description | ✅ | `aria-label="Historical timeline of Kansas events"` |
| 10 | SVG icons have descriptive `title` or `aria-hidden="true"` | ✅ | Passed audit |

---

## 🧠 Tools & Environment

| Tool | Purpose | Result |
|------|----------|--------|
| **NVDA 2023.3 (Windows)** | Primary navigation audit | ✅ Pass |
| **JAWS 2024** | Landmarks + forms test | ✅ Pass |
| **VoiceOver (macOS 14)** | Semantic region order | ✅ Pass |
| **Chrome DevTools Accessibility Tree** | DOM structure validation | ✅ Pass |
| **Axe Core CLI v4.10** | Automated ARIA/role check | ✅ Pass |
| **Lighthouse CI** | Accessibility score ≥ 90 | ✅ Pass |

---

## 🗂️ Audit Steps

1. Launch site with screen-reader enabled.  
2. Verify **landmarks and regions** are announced in correct order.  
3. Tab through all interactive elements—ensure descriptive labels and focus order.  
4. Trigger AI Assistant responses; verify live announcements.  
5. Open Detail Panel; confirm heading levels and label hierarchy.  
6. Switch map layers and observe announcements of state changes.  
7. Record issues and retest after fixes.

---

## 📊 Summary Results

| Section | Status | Notes |
|----------|--------|-------|
| Header & Navigation | ✅ | Fully compliant |
| Map View | ⚙️ | MapLibre missing role on zoom buttons (pending PR) |
| Timeline Canvas | ✅ | Focus + announcements OK |
| Detail Panel | ✅ | Proper heading structure |
| AI Assistant | ✅ | `aria-live` polite region verified |
| Layer Controls | ✅ | Dynamic state labels added |
| Global Skip Links | ✅ | Confirmed visible on Tab start |

---

## 🧩 Screen-Reader Focus Flow

```mermaid
flowchart TD
  A["Header\n(role='banner')"] --> B["Navigation\n(role='navigation')"]
  B --> C["Main Content\n(role='main')"]
  C --> D["Timeline Canvas\naria-label='Kansas Events Timeline'"]
  D --> E["Map View\naria-label='Interactive Map of Kansas'"]
  E --> F["Detail Panel\n(role='region' aria-labelledby='entity-title')"]
  F --> G["AI Assistant Drawer\n(role='complementary')"]
  G --> H["Footer\n(role='contentinfo')"]
<!-- END OF MERMAID -->


⸻

🪶 Recommendations
	1.	✅ Add aria-current="page" to active navigation items.
	2.	✅ Use aria-describedby for map marker popups referencing contextual text.
	3.	⚙️ Investigate custom ARIA roles for MapLibre controls to ensure compatibility.
	4.	⚙️ Retest modal focus trap post React 18 upgrade.
	5.	🧩 Integrate screen-reader regression tests in CI (Pa11y + NVDA automation).

⸻

🧾 Provenance

Field	Value
Reviewer(s)	@accessibility-team / @design-lead
Review Date	{{ ISO8601_DATE }}
Components Audited	Navigation v0.3.2 · Timeline v0.4.0 · Map Controls v0.5.1 · AI Assistant v0.3.0
Commit Hash	{{ GIT_COMMIT }}
Result	✅ AA Compliant (MapLibre enhancement pending)


⸻

🪪 License

Released under Creative Commons CC-BY 4.0
© 2025 Kansas Frontier Matrix Design Collective

⸻



