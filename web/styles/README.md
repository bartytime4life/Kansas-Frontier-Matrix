# `web/styles/` — Viewer Styles & Themes

This folder contains **styling assets** for the Kansas Frontier Matrix web viewer.  
It defines the **look and feel** of maps, overlays, and UI components.

---

## Design Goals

- **Consistency**: Shared colors, symbols, and fonts across layers and timelines.
- **Modularity**: Stylesheets and JSON definitions can be swapped or overridden.
- **Declarative**: Viewer code (`web/app.js`) reads styles from here (or from `web/config/legend.json`).
- **Extensible**: Add new categories (e.g. trails, treaties, hydrology) without editing core code.

---

## Directory Layout

```

web/styles/
├── base.css          # Global CSS resets and variables
├── map.css           # MapLibre-specific styling (controls, sidebar, legend)
├── theme-light.css   # Light theme overrides
├── theme-dark.css    # Dark theme overrides
├── icons/            # SVG/PNG icons for map symbols
└── README.md         # This file

````

---

## How It Works

- **Base CSS** defines color palette variables and shared layout.
- **Map CSS** styles the map container, sidebar, timeline slider, and popups.
- **Theme files** provide overrides (light/dark/high-contrast).
- **Icons** are referenced in `web/config/legend.json` and bound to layers.

---

## Example: Adding a New Symbol

1. Place an SVG/PNG icon in `web/styles/icons/` (e.g. `treaty.svg`).
2. Add a symbol style to `web/config/legend.json`:

```json
"treaties": { "icon": "web/styles/icons/treaty.svg", "fillColor": "#FFCA3A" }
````

3. Reference the symbol in your layer config (`web/data/*.json`).

---

## Guidelines

* Use **relative paths** (e.g., `web/styles/icons/...`) so GitHub Pages deployment works.
* Keep palettes accessible: ensure sufficient contrast for color-blind users.
* Test both light and dark themes.
* Document any new icons or color tokens in this README.

---

✅ **Mission-grade principle**: The `styles/` folder is the **single source of truth** for UI styling — keeping Kansas’s historical map layers visually coherent and accessible.

```
