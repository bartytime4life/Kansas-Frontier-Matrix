---
title: "🎨 Kansas Frontier Matrix — Web Styles Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/README.md"
version: "v10.4.2"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-styles-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-styles"
fair_category: "F1-A1-I1"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Web Styles Architecture**  
`web/src/styles/README.md`

**Purpose:**  
Define the global styling system for the Kansas Frontier Matrix (KFM) web client, including design tokens,
themes, mixins, map styles, accessibility rules, and Focus Mode visuals. This keeps all frontend components
consistent, reproducible, FAIR+CARE-aligned, and Focus Mode–aware.

Documentation standard: MCP v6.3  
License: MIT  
FAIR+CARE status: Active / Enforced  

</div>

---

## 📚 Overview

The `web/src/styles` module is the **single source of truth** for styling in the KFM web application.

It standardizes:

- Design tokens (colors, spacing, typography, radii, shadows)  
- Light/dark themes and future variants  
- Shared mixins (buttons, layout primitives, Focus Mode effects)  
- MapLibre-specific styling (basemap and legend)  
- Accessibility guarantees (WCAG 2.1 AA)  
- Visual language for Story Nodes and Focus Mode

All style changes must pass CI linting and validation before merge.

---

## 🧩 Directory Layout

    web/src/styles/
    ├── tokens/                 # Design tokens: colors, spacing, typography, radii, shadows
    │   ├── color.tokens.js
    │   ├── spacing.tokens.js
    │   └── typography.tokens.js
    ├── themes/                 # Theme entrypoints (light, dark, future variants)
    │   ├── light.css
    │   └── dark.css
    ├── mixins/                 # Shared CSS utilities and component patterns
    │   ├── focus-mode.css
    │   ├── buttons.css
    │   └── layout.css
    ├── maps/                   # MapLibre-specific style modules
    │   ├── basemap.css
    │   └── legend.css
    └── index.css               # Master global stylesheet imported by React entrypoint

Any new global styling artifact must live under `web/src/styles/` and be referenced through `index.css` or
a theme entrypoint, not imported ad hoc from components.

---

## 🏗 Style System Architecture

KFM styling is layered:

1. **Tokens (`tokens/`)**  
   Implementation-agnostic values for color, spacing, typography, radii, and shadows.

2. **Themes (`themes/`)**  
   Map tokens to concrete CSS variables (e.g. `--kfm-bg`, `--kfm-text`, `--kfm-primary-strong`) per
   theme (light, dark, high-contrast, etc.).

3. **Mixins (`mixins/`)**  
   Reusable CSS utility classes and component patterns (buttons, layout shells, Focus Mode visuals).

4. **Map Styles (`maps/`)**  
   Styles targeted at MapLibre, using the same token set so the map matches the UI.

5. **Global Entry (`index.css`)**  
   Root stylesheet that imports themes, mixins, and any Tailwind layers; defines base element styles.

This architecture yields testable, modular, and themed styling with clear responsibilities.

---

## 🎨 Design Tokens (`tokens/`)

Tokens are plain JS modules plus CSS variable bindings. They are semantically named and theme-agnostic.

### Color Tokens (`color.tokens.js`)

Semantic prefixes:

- `kfm-primary-*` — primary UI actions and highlights  
- `kfm-secondary-*` — secondary actions and subtle accents  
- `kfm-neutral-*` — backgrounds, borders, base text  
- `kfm-status-*` — success/warn/error/info states  
- `kfm-map-*` — map land, water, boundaries, overlays  
- `kfm-focus-*` — Focus Mode halos, outlines, pulses  
- `kfm-care-*` — markers and overlays for CARE-sensitive entities  

Each token is documented with:

- Intended usage (e.g. “primary button fill”, “timeline active segment”)  
- Contrasts for light/dark themes  
- Any mapping to STAC/DCAT layer semantics (for map colors)

### Spacing Tokens (`spacing.tokens.js`)

A simple, consistent scale:

- `kfm-space-0` = 0px  
- `kfm-space-1` = 4px  
- `kfm-space-2` = 8px  
- `kfm-space-3` = 12px  
- `kfm-space-4` = 16px  
- …and so on

Used for paddings, margins, gutters, and icon+label spacing; no ad-hoc pixel values in components.

### Typography Tokens (`typography.tokens.js`)

Define:

- Font families: `kfm-font-sans`, `kfm-font-serif`, `kfm-font-mono`  
- Text styles: `kfm-text-xs`…`kfm-text-2xl` (font-size, line-height, weight)  
- Heading styles: `kfm-heading-sm`, `kfm-heading-md`, `kfm-heading-lg`  

Base narrative text should be at least 16px (`kfm-text-md`) in sidebars and story-node bodies.

---

## 🌗 Themes (`themes/`)

Themes resolve tokens into CSS variables.

Example pattern:

    :root[data-theme="light"] {
      --kfm-bg: #ffffff;
      --kfm-fg: #111827;
      --kfm-primary-strong: #2563eb;
      --kfm-primary-soft: #dbeafe;
      /* … */
    }

    :root[data-theme="dark"] {
      --kfm-bg: #020617;
      --kfm-fg: #e5e7eb;
      --kfm-primary-strong: #60a5fa;
      --kfm-primary-soft: #0b1120;
      /* … */
    }

Guidelines:

- Theme is switched via `data-theme="light|dark|..."` on `<html>` or `<body>`.  
- Components must only reference CSS variables, not raw hex values.  
- Any new theme must define the full base variable set (`--kfm-bg`, `--kfm-fg`, `--kfm-primary-*`,
  `--kfm-neutral-*`, etc.) and be contrast-tested.

---

## 🧱 Mixins & Utilities (`mixins/`)

### Buttons (`mixins/buttons.css`)

Provides canonical button classes:

- `.kfm-btn-primary`  
- `.kfm-btn-secondary`  
- `.kfm-btn-ghost`  
- `.kfm-btn-icon`

Each defines:

- Background/border/text colors via CSS variables  
- Hover / active / focus-visible states  
- Disabled state (reduced opacity, no pointer events)  

Components should use or extend these button classes rather than redefining their own.

### Layout (`mixins/layout.css`)

Defines core layout primitives:

- `.kfm-shell` — app shell container (header + main + sidebar layouts)  
- `.kfm-sidebar` — side panels (Focus Mode, filters, story nodes)  
- `.kfm-main` — primary map/timeline content area  

Layout utilities must:

- Keep timeline and map visible and synchronized  
- Support responsive breakpoints (mobile ↔ desktop)  
- Avoid overlapping critical map regions (focus halos, legends)

### Focus Mode (`mixins/focus-mode.css`)

Focus Mode visuals:

- `.kfm-focus-ring` — keyboard focus outline for components  
- `.kfm-focus-halo` — subtle glow around focused entities (cards, markers, timeline items)  
- `.kfm-focus-related` — lighter emphasis for related nodes  
- `.kfm-focus-ai-explanation` — container for AI-generated summaries or insights  

Animations must respect `prefers-reduced-motion`.

---

## 🗺 Map Styles (`maps/`)

Map styles align MapLibre with UI tokens to avoid visual dissonance.

### Basemap (`maps/basemap.css`)

Controls:

- Land/water colors via `--kfm-map-land`, `--kfm-map-water`  
- Boundary colors (counties, reservations, treaty areas)  
- Road and rail hues  
- Label contrast and legibility in both themes

### Legend (`maps/legend.css`)

Legend styling:

- `.kfm-legend` — container  
- `.kfm-legend-item` — row for a single symbol plus label  
- `.kfm-legend-swatch` — symbol sample  

Legends should:

- Be keyboard navigable  
- Use consistent spacing and typography tokens  
- Display source metadata when appropriate (dataset name, temporal extent, license icon)

---

## 🧠 Story Nodes & Focus Mode Integration

Story Nodes represent narrative units with spacetime grounding.

Styling must:

- Render story nodes as cards with:

  - Title using `kfm-heading-md`  
  - Summary text (`kfm-text-sm` or `kfm-text-md`)  
  - Time range and place labels as a metadata row  
  - Relations as chip-style tags

- Use `.kfm-focus-halo` and `.kfm-focus-ring` when a story node is the active Focus entity  
- Clearly separate:

  - Archival quotes (blockquote styling)  
  - AI summaries (`.kfm-focus-ai-explanation`, distinct background and icon)  

Screen readers distinguish AI-generated content vs primary sources through component ARIA attributes;
styles cannot rely solely on color.

---

## ♿ Accessibility & FAIR+CARE Styling

Accessibility constraints:

- Minimum contrast ratio 4.5:1 in both light and dark themes for body text  
- Focus outlines must be visible independent of color perception (width and pattern)  
- `prefers-reduced-motion: reduce` disables non-essential animations (Focus pulses become static)  
- Interactive targets (buttons, toggles) aim for at least 44×44 px

FAIR+CARE considerations:

- CARE-sensitive entities (e.g., sacred sites) are styled non-sensationally:

  - Neutral color palettes  
  - Optional blur/generalization overlays when zoomed in too far  
  - Clear textual notices in the UI about any redaction or generalization  

- H3-generalized geometries are rendered as soft regions, not pinpoint icons.

---

## 🧪 Validation & CI

Style hygiene is enforced via:

- Stylelint on all files under `web/src/styles/`  
- Token schema validation against `tokens.schema.json`  
- Map style validation against the MapLibre style schema (for any generated JSON)  
- Optional visual regression tests for key components (buttons, Focus Mode states, story node cards)

Any failure blocks merges until fixed.

---

## 📦 Usage Guidelines for Developers

1. Do not hard-code hex colors, font sizes, or spacing in components. Use tokens and CSS variables.  
2. When creating a new component:

   - Use existing button/layout mixins if possible  
   - For new patterns, implement them under `mixins/` and reference them from components  
   - Confirm accessibility (contrast, focus, motion) before shipping

3. When adding a new theme:

   - Copy from an existing theme as a base  
   - Define the complete base variable set  
   - Run contrast checks and manual smoke tests in both map and story-node contexts

4. When changing tokens:

   - Consider downstream effects on map layers, legends, Focus Mode, and accessibility  
   - Coordinate with design/UX and data viz maintainers if colors encode particular semantics.

---

## 🕰 Version History

| Version | Date       | Author / Maintainer | Summary                                                                 |
|--------|------------|---------------------|-------------------------------------------------------------------------|
| v10.4.2| 2025-11-15 | Lead Programmer     | Removed badge-style markup, stabilized header formatting                |
| v10.4.1| 2025-11-15 | Lead Programmer     | Rebuilt README into single-box format; tightened layout and usage       |
| v10.4.0| 2025-11-14 | Lead Programmer     | Initial creation of styles architecture doc and directory layout        |

---