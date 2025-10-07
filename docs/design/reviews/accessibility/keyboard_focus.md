<div align="center">

# ⌨️ Kansas Frontier Matrix — Accessibility Audit: Keyboard & Focus  
`docs/design/reviews/accessibility/keyboard_focus.md`

**Objective:** Validate that **all interactive UI components** within the Kansas Frontier Matrix (Map, Timeline, AI Drawer, Panels)  
are fully operable via **keyboard navigation**, with visible focus indicators meeting **WCAG 2.1 AA**.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#🧩-checklist)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../LICENSE)

</div>

---

## 🎯 Purpose

Keyboard accessibility ensures that **all KFM functionality**—navigation, timeline scrubbing, layer toggles, and AI interactions—  
is usable without a mouse or touch input. Every focusable element must be **reachable, operable, and visible**.  

Audit scope includes:
- Keyboard-only navigation (`Tab`, `Shift+Tab`, `Enter`, `Space`, `Arrow` keys)
- Logical focus management and order
- Skip links and modal/drawer focus traps
- Proper ARIA roles and `tabindex` usage for custom elements

---

## 🧭 Scope

| UI Region | Expected Behavior | WCAG Ref |
|------------|------------------|-----------|
| **Header / Navigation** | Tab order: logo → search → help → login; `Esc` closes menus | 2.1.1 / 2.4.3 |
| **Timeline (Canvas)** | Arrow keys navigate events; Tab jumps to active label | 2.1.1 / 2.4.7 |
| **Map (MapLibre GL)** | Tab cycles toolbar → layer toggles → zoom controls → legend | 2.1.1 / 2.4.3 |
| **AI Assistant Drawer** | Focus trapped while open; `Esc` closes; `Shift+Tab` cycles back | 2.1.2 / 2.4.3 |
| **Detail Panel** | Scroll and close button keyboard-accessible | 2.1.1 |
| **Global Skip Link** | “Skip to Main Content” visible on first Tab press | 2.4.1 |

---

## 🧩 Checklist

| # | Test | Expected | Status |
|:--:|------|-----------|:-------:|
| 1 | Tab order follows DOM sequence | Left→right, top→down | ✅ |
| 2 | Focus visible on all interactive items | ≥ 3 px outline · ≥ 3:1 contrast | ✅ |
| 3 | No focus traps | Modals restore focus correctly | ✅ |
| 4 | Keyboard triggers functional | Enter/Space activate controls | ✅ |
| 5 | ARIA roles & `tabindex` applied | Non-native controls announced | ✅ |
| 6 | Focus retained after action | Returns to origin after close | ⚙️ Testing |
| 7 | `Esc` closes drawers/modals | Immediate · no residual focus | ✅ |
| 8 | MapLibre overlays navigable | Focus ring visible · labels read | ⚙️ Pending |
| 9 | Timeline scrubber operable | Arrow/Pg keys adjust position | ✅ |
| 10 | Skip link appears and works | First tab press shows link | ✅ |

---

## 🧠 Test Setup

| Tool / Env | Purpose |
|-------------|----------|
| Chrome + DevTools A11y Tree | Validate focus order and tab stops |
| NVDA / VoiceOver | Check announcements & landmarks |
| Axe DevTools / Pa11y CI | Detect keyboard traps |
| Storybook A11y Addon | Component-level tests |
| Keyboard Simulation Ext | Replay key sequences |

---

## 🧩 Focus Order Flow (Web App Overview)

```mermaid
flowchart LR
  A["Header\nLogo → Search → Lang → Help"] --> B["Sidebar\nLayer Toggles → Legend"]
  B --> C["Map Controls\nZoom → Locate → Timeline Link"]
  C --> D["Timeline Canvas\nEvents → Scrubber"]
  D --> E["Detail Panel\nRead More → Close"]
  E --> F["AI Assistant Drawer\nInput → Send → Close"]
  F --> G["Footer\nDocs Link"]

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

## 🧩 Focus Styling Tokens

| Variable                 | Purpose                  | Example         |
| ------------------------ | ------------------------ | --------------- |
| `--kfm-focus-outline`    | Primary outline color    | `#3BAFDA`       |
| `--kfm-focus-width`      | Outline thickness        | `3px`           |
| `--kfm-focus-offset`     | Offset from element edge | `2px`           |
| `--kfm-focus-transition` | Animation timing         | `0.1s ease-out` |

> Focus outlines must never be removed (`outline: none`) without a visible alternative (e.g. `box-shadow`).

---

## 🧩 Recommendations

1. ✅ Ensure `tabindex="0"` on custom map controls and legends.
2. ✅ Apply `.focus-visible` utility for consistent outline styles.
3. ⚙️ Implement focus trap for AI Assistant drawer during context switches.
4. ⚙️ Test MapLibre behavior in Firefox + NVDA (enhanced keyboard support).
5. 🧩 Add unit tests (`tests/accessibility/focus.test.js`) to simulate Tab + Esc navigation.

---

## ⚙️ Continuous Integration (Focus QA)

```yaml
# .github/workflows/a11y_keyboard_focus.yml
on:
  pull_request:
    paths:
      - "web/src/components/**"
      - "docs/design/reviews/accessibility/keyboard_focus.md"
jobs:
  focus:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install a11y tools
        run: npm i -g axe-core-cli pa11y-ci
      - name: Run keyboard focus audit
        run: pa11y-ci --config .pa11yci.focus.json > focus-report.json
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: focus-audit-report
          path: focus-report.json
```

---

## 🧾 Provenance

| Field           | Value                                            |
| --------------- | ------------------------------------------------ |
| **Reviewer(s)** | @accessibility-team / @design-lead               |
| **Review Date** | `2025-10-07`                                     |
| **Components**  | Navigation v0.3.2 · Timeline v0.4.0 · Map v0.5.1 |
| **Commit Hash** | `{{ GIT_COMMIT }}`                               |
| **Audit Tool**  | Axe Core v4.10 · Pa11y v7                        |
| **Result**      | ✅ AA Compliant (minor MapLibre patch pending)    |

---

## 🪪 License

Released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Design Collective

---

<div align="center">

### ⌨️ Kansas Frontier Matrix — Keyboard Navigation by Design

**Accessible · Predictable · Reproducible**

</div>
