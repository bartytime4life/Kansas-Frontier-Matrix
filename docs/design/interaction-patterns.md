<div align="center">

# 🧩 Kansas Frontier Matrix — Interaction Patterns  
`docs/design/interaction-patterns.md`

**Mission:** Define consistent, accessible, and reproducible **interaction behaviors**  
across all Kansas Frontier Matrix (KFM) components — ensuring that time, space,  
and story remain synchronized through every user action.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Design Standards](https://img.shields.io/badge/Design-Human%20Centered-orange)](README.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](README.md)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🎯 Purpose

Interaction patterns define **how users move through the Frontier Matrix experience** —  
how they explore data, trigger actions, and perceive feedback.  
Each pattern unites technical reproducibility with emotional clarity, allowing  
Kansas history to unfold intuitively through map, timeline, and AI-driven storytelling.

All interactions must:
- Meet **WCAG 2.1 AA** accessibility.
- Use **consistent keyboard and touch gestures**.
- Provide **instant, visible feedback** for every user action.
- Remain fully **reproducible and documented** per MCP.

---

## 🧭 System Overview — Interaction Architecture

```mermaid
flowchart TD
    A["Timeline\n(Canvas / D3)"] -->|Scroll / Zoom / Select| B["Map\n(MapLibre GL)"]
    B -->|Click / Hover / Focus| C["Detail Panel\n(Events · Docs · AI Summaries)"]
    C -->|Back / Close| B
    B -->|Filter / Toggle| D["Legend & Layer Controls"]
    D -->|Update / Sync| A
    A -->|Time Context| E["AI Assistant\n(Narrative Context Engine)"]
````

<!-- END OF MERMAID -->

**Interaction Cycle Summary**

1. User scrolls or zooms on the **Timeline** → updates visible map layers.
2. Clicking an item on the **Map** → opens corresponding **Detail Panel**.
3. **Layer Controls** synchronize between timeline filters and map overlays.
4. The **AI Assistant** observes the current state and can narrate context dynamically.

---

## 🗺️ Map Interactions (MapLibre GL)

| Action             | Description                 | Feedback / Behavior                                    |
| :----------------- | :-------------------------- | :----------------------------------------------------- |
| **Hover**          | Focus on marker or polygon. | Tooltip appears after 300 ms; highlighted outline.     |
| **Click / Tap**    | Select feature.             | Opens side Detail Panel with related entities.         |
| **Shift + Drag**   | Box zoom.                   | Smooth zoom animation; resets on `ESC`.                |
| **Scroll / Pinch** | Zoom in/out.                | Accelerated zoom with easing; accessible ARIA updates. |
| **Keyboard**       | `↑ ↓ ← →` pan, `+ –` zoom.  | Live region announces new map bounds.                  |
| **Layer Toggle**   | Enable/disable overlays.    | Immediate update; visual toggle changes state color.   |

### Map Design Rules

* Default cursor: `grab`; on hover: `pointer`.
* Maintain focus ring on selected feature (2 px accent outline).
* Ensure reduced motion compliance: disable inertia if `prefers-reduced-motion`.
* Tooltip text limited to 120 characters; include `aria-describedby`.

---

## 🕰️ Timeline Interactions

| Action                  | Description                             | Visual Response                                   |
| :---------------------- | :-------------------------------------- | :------------------------------------------------ |
| **Scroll / Drag**       | Navigate through time (horizontal pan). | Smooth scroll; inertia easing.                    |
| **Zoom (Ctrl + wheel)** | Adjust time granularity.                | Tick density recalculates dynamically.            |
| **Click Event Marker**  | Select specific year or event.          | Marker expands; triggers map filter + AI summary. |
| **Keyboard**            | `← →` move through events.              | Current marker outline updates; map syncs.        |
| **Hover Tooltip**       | Display event title/date.               | Appears with fade-in delay 200 ms.                |

```mermaid
sequenceDiagram
    participant User
    participant Timeline
    participant Map
    participant DetailPanel
    User->>Timeline: Scrolls to 1867
    Timeline->>Map: Show layers where year ≤ 1867
    Map->>User: Highlight “Medicine Lodge Treaty”
    User->>Map: Click marker
    Map->>DetailPanel: Load event summary + links
    DetailPanel->>User: Display AI narrative
```

<!-- END OF MERMAID -->

---

## 🧠 AI Assistant Interactions

| Trigger               | Behavior                                             | Example                                         |
| :-------------------- | :--------------------------------------------------- | :---------------------------------------------- |
| **User Question**     | `POST /ask` API query → generates contextual answer. | “Show me treaties near the Arkansas River.”     |
| **Passive Context**   | Updates summary when user changes map/timeline.      | Displays “5 treaties active between 1850–1870.” |
| **Highlight Command** | AI highlights matching map features.                 | Outline polygons with confidence > 0.9.         |
| **Narrative Mode**    | Sequential storytelling view.                        | AI narrates events as timeline autoplays.       |

**Design Notes**

* Assistant opens in a right-side drawer (non-modal).
* Keyboard focus returns to last element on close.
* Voice output (optional) via Web Speech API.

---

## 🧾 Legend & Layer Controls

| Interaction       | Description                         | Feedback                                      |
| :---------------- | :---------------------------------- | :-------------------------------------------- |
| **Toggle**        | Enables/disables dataset layer.     | Checkbox → accent color when active.          |
| **Hover Label**   | Shows dataset metadata tooltip.     | Delay 150 ms; fade animation.                 |
| **Shift + Click** | Solo mode (hide all others).        | Deactivates other layers; announces via ARIA. |
| **Keyboard**      | Arrow keys navigate; Enter toggles. | Visual focus ring on current layer.           |

---

## ♿ Accessibility & Keyboard Shortcuts

| Shortcut            | Action                           | Notes                                    |
| :------------------ | :------------------------------- | :--------------------------------------- |
| `Tab / Shift + Tab` | Move between controls            | Visible focus outline required           |
| `Enter / Space`     | Activate selected element        | Buttons, toggles, links                  |
| `Esc`               | Close modals, tooltips, AI panel | Must always return focus                 |
| `Alt + T`           | Focus timeline                   | Adds `.focus-visible` class              |
| `Alt + M`           | Focus map                        | Announces “Map focused” to screen reader |
| `Alt + A`           | Open AI assistant                | Non-modal toggle                         |

All shortcuts documented under `/web/src/utils/hotkeys.ts` and displayed in the Help Menu (`?` icon).

---

## 📱 Responsive Interaction Rules

| Device                   | Behavior                                      | Adjustment                    |
| :----------------------- | :-------------------------------------------- | :---------------------------- |
| **Desktop (≥ 1280 px)**  | Timeline visible; hover + keyboard supported. | Full dual-pane layout.        |
| **Tablet (768–1279 px)** | Timeline collapsible; tap events open modal.  | Replace hover with focus tap. |
| **Mobile (< 768 px)**    | Map full-screen; timeline as bottom sheet.    | Swipe up/down reveals panel.  |

Touch gestures replace hover actions on small devices.

---

## 🔄 Feedback & Animation Patterns

| Type                | Duration | Easing      | Description                     |
| :------------------ | :------- | :---------- | :------------------------------ |
| **Hover Highlight** | 150 ms   | ease-in-out | Marker glow or polygon tint.    |
| **Panel Slide In**  | 250 ms   | ease-out    | Detail panel reveal.            |
| **Timeline Scroll** | 300 ms   | ease-in-out | Smooth horizontal animation.    |
| **Tooltip Fade**    | 120 ms   | ease-in     | Soft transparency effect.       |
| **Reduced Motion**  | 0 ms     | none        | Honor `prefers-reduced-motion`. |

---

## 🧪 Interaction Testing Checklist

| Test                 | Tool / Method             | Expected Result                |
| :------------------- | :------------------------ | :----------------------------- |
| Map hover / click    | Manual & Playwright tests | Correct tooltip & panel sync   |
| Timeline scroll sync | Playwright E2E            | Layers update accurately       |
| Keyboard focus flow  | Axe / NVDA                | Sequential, visible focus      |
| AI assistant Q&A     | Cypress API mock          | Correct narrative output       |
| Layer toggles        | Jest + DOM test           | Proper map visibility toggle   |
| Reduced motion       | Browser setting           | Animations disabled gracefully |

---

## 🧩 Implementation Notes

* Define all interaction constants in `/web/src/config/interactions.ts`.
* Document every new pattern with a short GIF or Mermaid diagram in this directory.
* Never rely solely on color for state changes — use icons, patterns, or text labels.
* Interaction code must emit accessibility events (e.g., `aria-live="polite"`).
* Each new pattern requires a brief **Design Review** entry in `/docs/design/reviews/`.

---

<div align="center">

### 🕹️ “Interactivity is empathy in motion — it turns data into discovery.”

**— Kansas Frontier Matrix Design Team**

</div>
