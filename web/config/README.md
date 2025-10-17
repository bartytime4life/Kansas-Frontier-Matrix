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

## 🧭 Overview

`web/public/assets/icons/` contains KFM’s **official vector icon set** used across Header, Map, Timeline, Modals, Sidebar, and Accessibility UIs.  
Icons are exported from Figma as **optimized SVGs**, adapt to **light/dark** themes via CSS variables, and meet **WCAG 2.1 AA** legibility.

> One symbol system—coherent across time, data, and terrain.

---

## 🧱 Directory Structure

```text
web/public/assets/icons/
├── ai-bot.svg            # AI Assistant
├── map-marker.svg        # Map pin
├── timeline.svg          # Timeline tools
├── filter.svg            # Filter / layers
├── info.svg              # Info / help
├── settings.svg          # Settings
├── search.svg            # Search magnifier
├── keyboard.svg          # Keyboard shortcuts
├── contrast.svg          # Contrast/theme switch
└── README.md
```

---

## 🎨 Design Specifications

| Attribute       | Spec                                                                           |
| :-------------- | :----------------------------------------------------------------------------- |
| **ViewBox**     | `0 0 24 24` (consistent canvas)                                                |
| **Stroke**      | `1.5px` (scalable)                                                             |
| **Fill**        | `none` (stroke-driven for token theming)                                       |
| **Tokens**      | `stroke="var(--kfm-color-accent)"` or `var(--kfm-color-text)`                  |
| **Export**      | `svgo --multipass`                                                             |
| **Usage**       | Inline `<svg>` (preferred) or `<img src="/assets/icons/*.svg" alt="...">`      |

**Template**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
     stroke="var(--kfm-color-accent)" fill="none" stroke-width="1.5"
     role="img" aria-label="Example icon">
  <circle cx="12" cy="12" r="9"/>
</svg>
```

---

## 🧩 Icon Usage by Component

| Icon             | Component(s)                   | Purpose                                      |
| :--------------- | :----------------------------- | :------------------------------------------- |
| `ai-bot.svg`     | AIAssistant                    | Chat header/avatar                            |
| `map-marker.svg` | MapView                        | Geomarkers, selections                        |
| `timeline.svg`   | TimelineView                   | Temporal tools & controls                     |
| `filter.svg`     | LayerControls, Sidebar         | Toggle filters & overlay groups               |
| `info.svg`       | Modals, DetailPanel            | Help/about/citation info                      |
| `settings.svg`   | Header, SettingsModal          | App preferences                               |
| `search.svg`     | Header                         | Global search                                 |
| `keyboard.svg`   | Accessibility/Help modals      | Shortcut guide                                |
| `contrast.svg`   | ThemeToggle                    | Contrast or light/dark switching              |

---

## ♿ Accessibility Guidelines

- **Decorative:** `role="presentation"` or `alt=""` when purely visual.  
- **Informative:** include `<title>` or `aria-label`.  
- **Min size:** 16×16px (buttons), 20×20px recommended.  
- **Contrast:** ≥ **4.5:1** against background (validated in CI).  
- **Focus:** interactive icons inherit global focus rings via tokens.

---

## 🧠 Design → Dev Workflow

1. **Design** in Figma (`docs/design/mockups/icons/`) on a 24×24 grid.  
2. **Export** SVG with paths outlined; keep `viewBox="0 0 24 24"`.  
3. **Optimize** in CI using `svgo --multipass`.  
4. **Validate a11y** (roles/labels, contrast) via **axe-core**.  
5. **Integrate** inline or via `<img>`; tokens drive color.  
6. **Hash & record** checksum; embed source/license comment header.

**Embedded metadata example:**
```xml
<!-- KFM Icon: keyboard.svg | Source: docs/design/mockups/icons | License: MIT | Author: KFM Design -->
```

---

## 🧪 Validation & Testing

| Test              | Goal                                          | Tooling             |
| :---------------- | :-------------------------------------------- | :------------------ |
| SVG lint          | No raster, proper viewBox, clean paths        | SVGO CLI            |
| Accessibility     | Roles/labels; contrast                        | axe-core            |
| Integrity         | SHA-256 checksum per file                     | Node hash pipeline  |
| Theming snapshots | Light/dark renders                            | Jest + RTL          |
| Scaling           | Crisp at 1×–4× zoom                           | Cypress visuals     |

**Compliance target:** ≥ **95%** across asset checks.

---

## 🧾 Provenance & Integrity

| Artifact   | Description                                                        |
| :--------- | :----------------------------------------------------------------- |
| Inputs     | Figma exports, KFM tokens                                          |
| Outputs    | Optimized SVGs with consistent metadata                            |
| Dependencies | SVGO, TailwindCSS (layout), Framer Motion (animated variants)   |
| Integrity  | CI validates checksum, viewBox, a11y metadata, token usage         |

---

## 🧠 MCP Compliance Checklist

| Principle           | Implementation                                      |
| :------------------ | :-------------------------------------------------- |
| Documentation-first | Icon families documented here & in the Design guide |
| Provenance          | Embedded source/license metadata in SVG             |
| Accessibility       | WCAG 2.1 AA checks in CI                            |
| Reproducibility     | Deterministic optimization + hashing                |
| Open Standards      | SVG 2.0 + CSS variables                             |

---

## 🔗 Related Documentation

- **Public Images** — `web/public/assets/images/README.md`  
- **Design Mockups (Icons)** — `docs/design/mockups/icons/`  
- **Accessibility Reviews** — `docs/design/reviews/accessibility/`  
- **Web Architecture** — `web/ARCHITECTURE.md`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.6.0` |
| **Codename** | *Themeable SVG & A11y Compliance Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-design · @kfm-web |
| **License** | MIT (icons) |
| **Alignment** | WCAG 2.1 AA · SVG 2.0 · MCP-DL v6.2 |
| **Maturity** | Stable / Production |

---

## 📜 License

All Kansas Frontier Matrix icons are **MIT**; derivatives may include attribution if sourced from compatible open sets (e.g., CC-BY 4.0).  
© 2025 Kansas Frontier Matrix — **MCP-DL v6.2** compliant iconography for a consistent, accessible UI.
