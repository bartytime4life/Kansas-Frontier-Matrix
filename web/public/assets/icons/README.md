<div align="center">

# 🧭 Kansas Frontier Matrix — **Public Icons**  
`web/public/assets/icons/`

**Vector Icons · UI Symbols · Thematic Graphics**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../../docs/design/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Public Icons (web/public/assets/icons/)"
version: "v1.4.0"
last_updated: "2025-10-14"
owners: ["@kfm-design", "@kfm-web"]
tags: ["icons","svg","ui","design-system","accessibility","mcp"]
license: "MIT"
semantic_alignment:
  - WCAG 2.1 AA
  - W3C SVG 2.0
  - MCP-DL v6.2 Design Provenance
---
````

---

## 🧭 Overview

The `web/public/assets/icons/` directory contains the **official vector icon set** used across the Kansas Frontier Matrix (KFM) web interface.
These icons are employed in navigation, map controls, modals, timeline tools, and accessibility components — providing visual clarity and consistency across the entire application.

Each icon follows the **KFM Design System** specifications and is exported directly from Figma as **optimized SVGs**.
Icons are **responsive, accessible**, and adapt to **theme changes** (light/dark) through CSS variable bindings.

> **Purpose:** unify all visual language — one symbol system, shared across time, data, and terrain.

---

## 🧱 Directory Structure

```text
web/public/assets/icons/
├── ai-bot.svg            # AI Assistant symbol
├── map-marker.svg        # Map location pin
├── timeline.svg          # Timeline navigation icon
├── filter.svg            # Filter / Layer control icon
├── info.svg              # Info / help modal icon
├── settings.svg          # App configuration icon
├── search.svg            # Header search magnifier
├── keyboard.svg          # Keyboard shortcut icon
├── contrast.svg          # Theme/contrast switcher
└── README.md             # This documentation file
```

---

## 🎨 Design Specifications

| Attribute         | Specification                                       |
| :---------------- | :-------------------------------------------------- |
| **Canvas Size**   | `24×24px` (standardized viewBox across UI)          |
| **Stroke Width**  | `1.5px` (scalable for crispness)                    |
| **Fill**          | `none` — stroke-based for theme inheritance         |
| **Color Tokens**  | `var(--kfm-color-accent)` / `var(--kfm-color-text)` |
| **Export Format** | Optimized SVG (via `svgo --multipass`)              |
| **Usage Context** | Inline `<svg>` or `<img>` in React components       |

Example Icon Template:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  stroke="var(--kfm-color-accent)" fill="none" stroke-width="1.5">
  <circle cx="12" cy="12" r="9" />
</svg>
```

> All SVGs reference **CSS variables** for color to ensure automatic adaptation between light/dark modes.

---

## 🧩 Icon Usage by Component

| Icon             | Used In                        | Purpose                                        |
| :--------------- | :----------------------------- | :--------------------------------------------- |
| `ai-bot.svg`     | AIAssistant                    | AI Assistant avatar / chat header              |
| `map-marker.svg` | MapView                        | Geographic markers on the interactive map      |
| `timeline.svg`   | TimelineView                   | Temporal navigation and toolbar controls       |
| `filter.svg`     | LayerControls / Sidebar        | Activates layer filters & overlays             |
| `info.svg`       | Modals / DetailPanel           | Opens contextual help or metadata modals       |
| `settings.svg`   | Header / SettingsModal         | Accesses configuration and theme options       |
| `search.svg`     | Header                         | Global search input magnifier                  |
| `keyboard.svg`   | AccessibilityModal / HelpModal | Displays shortcut reference                    |
| `contrast.svg`   | ThemeToggle                    | Switches between contrast or light/dark themes |

---

## 🧠 Design & Development Workflow

1. **Design** — Icons are created or refined in Figma (`docs/design/mockups/icons/`) using the shared 24×24px grid.
2. **Export** — Exported as **SVG (Outline Text)** with `viewBox="0 0 24 24"`.
3. **Optimize** — Compressed in CI via `svgo --multipass` (removes redundant metadata).
4. **Accessibility Review** — Verified for contrast and screen-reader roles.
5. **Integration** — Imported inline in React components or referenced by `<img src>` tags.
6. **Validation** — CI runs lint checks for correct viewBox, title/aria attributes, and absence of raster data.

---

## ♿ Accessibility Guidelines

* **Decorative icons:** Must include `role="presentation"` or empty `alt=""` attributes when rendered as `<img>`.
* **Informative icons:** Use `aria-label`, `<title>`, or `aria-describedby` to provide contextual meaning.
* **Minimum Size:** 16×16px for buttons, 20×20px recommended for legibility.
* **Contrast Ratio:** Must maintain **≥ 4.5:1** contrast with background.
* **Scalability:** Icons scale via CSS `em` units to support browser zoom and accessibility settings.
* **Focus Visibility:** Interactive icons inherit focus ring styles from the global accessibility theme.

---

## 🧩 Example Integration

```tsx
import React from "react";
import "./styles.scss";

export const MapMarkerIcon: React.FC = () => (
  <img src="/assets/icons/map-marker.svg" alt="Map Marker" width="20" height="20" />
);

// Inline SVG alternative for theming:
export const AIIcon: React.FC = () => (
  <svg viewBox="0 0 24 24" stroke="var(--kfm-color-accent)" fill="none" strokeWidth="1.5">
    <path d="M8 12h8m-4-4v8" />
  </svg>
);
```

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                               |
| :--------------- | :------------------------------------------------------------------------ |
| **Inputs**       | Figma/Illustrator exports, design tokens                                  |
| **Outputs**      | Optimized SVGs with consistent metadata                                   |
| **Dependencies** | SVGO, Framer Motion (animated icons), TailwindCSS                         |
| **Integrity**    | CI validates accessibility, viewBox, checksum, and color token compliance |
| **Metadata**     | Each SVG includes comments for license, author, and export source         |

Example Embedded Metadata:

```xml
<!-- Kansas Frontier Matrix Icon: ai-bot.svg
     Source: docs/design/mockups/icons/ai-bot.fig
     License: MIT | Author: KFM Design Team -->
```

---

## 🧪 Validation & Testing

| Test               | Description                                                | Tool                 |
| :----------------- | :--------------------------------------------------------- | :------------------- |
| **SVG Lint**       | Checks for raster data, invalid paths, or missing metadata | SVGO CLI             |
| **Accessibility**  | Verifies roles, labels, and color contrast                 | axe-core             |
| **Integrity**      | Confirms SHA256 checksum for each icon                     | Node hash pipeline   |
| **Theming**        | Renders in light/dark mode snapshots                       | Jest + RTL           |
| **Responsiveness** | Ensures crisp scaling at 1×–4× zoom                        | Cypress visual tests |

> **Coverage Target:** ≥ **95%** asset compliance across accessibility and rendering audits.

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                                |
| :------------------ | :------------------------------------------------------------ |
| Documentation-first | Each icon family documented in Design System                  |
| Provenance          | Embedded metadata linking to source Figma file                |
| Accessibility       | WCAG 2.1 AA compliance tested via CI                          |
| Reproducibility     | Deterministic SVG builds + hash validation                    |
| Open Standards      | SVG 2.0 + CSS variable theming                                |
| Inclusivity         | Legibility validated at multiple resolutions & contrast modes |

---

## 🔗 Related Documentation

* **Public Assets Overview** — `web/public/assets/README.md`
* **Design Mockups (Icons)** — `docs/design/mockups/icons/`
* **Accessibility Guidelines** — `docs/design/reviews/accessibility/`
* **Web UI Architecture** — `web/ARCHITECTURE.md`

---

## 📜 License

All **Kansas Frontier Matrix icons** are distributed under the **MIT License**,
and derivative works retain attribution per CC-BY 4.0 or other open licenses.

© 2025 Kansas Frontier Matrix — created under **MCP-DL v6.2** for **transparent**, **reproducible**, and **accessible** iconography.

> *“Icons are the compass of discovery — guiding each interaction across Kansas’s digital frontier.”*

```
```
