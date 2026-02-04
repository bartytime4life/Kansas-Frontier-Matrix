# 🎨 `web/public/styles/` — KFM UI Styling Guide

![CSS](https://img.shields.io/badge/CSS-Modern-blue)
![Design System](https://img.shields.io/badge/Design-System-Tokens%20%2B%20Components-7a5cff)
![Accessibility](https://img.shields.io/badge/A11y-Keyboard%20%2B%20Contrast-success)

This folder is the **visual grammar** of Kansas Frontier Matrix (KFM): the styles that make maps, timelines, stories, and Focus Mode feel like one cohesive product—while staying *evidence-first*. KFM’s mission emphasizes that every layer and AI answer should remain traceable to sources (“the map behind the map”).  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> **Design north star 🧭:** styling should *clarify provenance*, not distract from it—KFM’s platform is explicitly built for transparency and trust.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📚 Table of Contents
- [🌱 What belongs here?](#-what-belongs-here)
- [🧱 Styling architecture (layers)](#-styling-architecture-layers)
- [🧩 Conventions](#-conventions)
- [🎛️ Design tokens](#️-design-tokens)
- [🗺️ Map UI styling (MapLibre / Cesium)](#️-map-ui-styling-maplibre--cesium)
- [🕰️ Timeline + scrollytelling](#️-timeline--scrollytelling)
- [🤖 Focus Mode UI](#-focus-mode-ui)
- [♿ Accessibility & motion](#-accessibility--motion)
- [⚡ Performance rules](#-performance-rules)
- [✅ “Add a style” checklist](#-add-a-style-checklist)

---

## 🌱 What belongs here?

**✅ This folder is for:**
- **Global tokens** (CSS variables): colors, spacing, typography, radii, elevation
- **Base styles**: normalize/reset, typography defaults, links, tables
- **Component styles** shared across the UI (buttons, chips, panels, drawers)
- **Map UI** polish: controls, overlays, legends, scale bar, coordinate readouts
- **Timeline** slider visuals + story “scrollytelling” transitions

**🚫 This folder is *not* for:**
- One-off inline styles sprinkled throughout React components
- Styling that encodes meaning *only by color* (use icons/labels too)
- “Demo CSS” that won’t survive production (remember: web design is constraint-driven)  [oai_citation:2‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

> KFM’s architecture enforces a “truth path” (Raw ➜ Processed ➜ Catalog ➜ DB ➜ API ➜ UI/AI). The UI should mirror that discipline: **no confusing visuals that imply certainty without provenance**.  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧱 Styling architecture (layers)

A healthy CSS system reads like a pipeline:

```text
🎨 styles/
  00-tokens/        → design tokens (CSS variables)
  10-base/          → reset + typography + page defaults
  20-layout/        → grid, containers, spacing utilities
  30-components/    → UI components (buttons, panels, chips)
  40-views/         → page/view composition (map shell, story shell)
  90-overrides/     → vendor overrides (MapLibre/Cesium), last resort
```

Why? Because **clarity beats cleverness**—selectors are simply “which elements get which properties/values.”  [oai_citation:4‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

> If you don’t have this exact folder tree yet, that’s fine—use it as the *target shape* for future refactors.

---

## 🧩 Conventions

### 🏷️ Naming
Use one of these consistently:

- **CUBE-ish** (recommended): `c-` components, `u-` utilities, `is-` states  
  - `c-panel`, `c-chip`, `u-stack`, `is-active`
- **BEM** (acceptable): `panel__header--compact`

### 🎯 Selector hygiene
- Prefer **single-class selectors** (`.c-button`) over deep nesting
- Avoid styling by tag (`button {}`) unless inside a scoped base layer
- Don’t bind styles to DOM shape (fragile), bind to **intent**

### 🧠 State styling
Use attributes/classes that encode state, not layout hacks:
- `[data-state="open"]`, `.is-loading`, `[aria-expanded="true"]`

---

## 🎛️ Design tokens

Tokens are the “single source of truth” for visuals—just like KFM’s data should be a “single source of truth.”  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Suggested token categories
- **Color**: `--color-bg`, `--color-fg`, `--color-accent`, `--color-danger`
- **Typography**: `--font-sans`, `--font-mono`, `--fs-0..--fs-6`, `--lh-body`
- **Spacing**: `--space-1..--space-8`
- **Radii**: `--radius-1..--radius-4`
- **Elevation**: `--shadow-1..--shadow-4`
- **Z-index**: `--z-map`, `--z-panel`, `--z-modal`, `--z-toast`

### Example: `00-tokens/tokens.css`
```css
:root {
  /* Color */
  --color-bg: #0b0f14;
  --color-surface: #121826;
  --color-fg: #e8eef7;
  --color-muted: #a7b3c7;
  --color-accent: #6ae4ff;
  --color-danger: #ff5a7a;

  /* Typography */
  --font-sans: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  /* Scale */
  --fs-0: 0.875rem;
  --fs-1: 1rem;
  --fs-2: 1.125rem;
  --fs-3: 1.25rem;
  --fs-4: 1.5rem;

  /* Line-height (respect typographic craft) */
  --lh-body: 1.55;
}
```

### Typography reminder 📝
Good typography is a core part of “graphic design craft applied to the web.”  [oai_citation:6‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)  
Practical note: **add more leading (line-height) than you think** for body text.  [oai_citation:7‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

---

## 🗺️ Map UI styling (MapLibre / Cesium)

KFM’s front-end is map-centric and explicitly expects **MapLibre GL JS (2D)** and **CesiumJS (3D)** in the UI stack.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧭 Classical navigation aids (yes, in CSS too)
The UI may include a **scale bar**, **north arrow**, and **grid overlays** / coordinate displays. Make sure these are:
- legible on satellite + dark basemaps
- responsive (don’t cover important map controls)
- keyboard accessible where interactive

This direction is explicitly described as a UI goal.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Vendor override policy
- Put MapLibre/Cesium overrides in `90-overrides/` only
- Prefer **CSS variables** or documented configuration first
- Keep overrides minimal and commented

---

## 🕰️ Timeline + scrollytelling

KFM’s UI includes a timeline slider and scroll-linked story playback (“scrollytelling”).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Timeline styling rules
- Slider must be **thumb-friendly** on touch screens
- Current year/date must be readable at a glance
- Provide **focus styles** (outline/box-shadow) for keyboard users
- Respect `prefers-reduced-motion` for animated scrubbing

### Story-map sync cues
When scroll triggers a map jump:
- show a small “now viewing: YEAR” toast
- optionally highlight the related story paragraph
- keep transitions fast and non-nauseating

---

## 🤖 Focus Mode UI

Focus Mode is a front-end chat interface inside a **React/TypeScript app** that calls backend endpoints rather than directly calling the model.  [oai_citation:11‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Styling requirements
- Make **citations** obvious and tappable (chips/footnotes)
- Use a consistent “evidence” pattern:
  - `Answer` (primary)
  - `Why/How` (secondary)
  - `Sources` (always visible or one click away)

This aligns with KFM’s evidence-first posture and “map behind the map” promise.  [oai_citation:12‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ♿ Accessibility & motion

### Minimum accessibility bar
- Visible focus rings (don’t remove outlines)
- Contrast safe text for map overlays (dark basemaps are tricky)
- Don’t encode meaning by color alone (icons + labels)
- Use ARIA states to drive styling (`[aria-expanded="true"]`)

### Motion safety
```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; }
}
```

---

## ⚡ Performance rules

KFM is a data-heavy map app; CSS needs to be boringly fast:

- **Avoid** expensive selectors (`.a .b .c > :nth-child(2)`)
- Prefer transforms for animations (`transform`, `opacity`)
- Keep CSS size tight—**“just because you can doesn’t mean you should.”**  [oai_citation:13‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)
- Ensure map overlays don’t trigger layout thrash (no frequent `top/left` animations)

---

## ✅ “Add a style” checklist

When adding or changing styles:

- [ ] Does it reuse **tokens** instead of hard-coded values?
- [ ] Does it work in **light + dark** (or at least degrade gracefully)?
- [ ] Keyboard: can I tab to it and see focus?
- [ ] Map: does it avoid covering core controls at common breakpoints?
- [ ] Motion: does it respect `prefers-reduced-motion`?
- [ ] Is the selector stable (class/attribute) rather than DOM-shape based?
- [ ] Did we accidentally hide provenance/citation UI?

---

## 📦 Where these styles are typically loaded

Many web apps keep browser-served assets under `public/` (e.g., `index.html` and stylesheets live there).  [oai_citation:14‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
If your KFM web package follows that shape, ensure the import order matches the layering approach above (tokens ➜ base ➜ components ➜ views ➜ overrides).

---

## 🔗 Related docs (project context)
- Evidence-first mission & “map behind the map” philosophy  [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Map + API + tile consumption patterns (Map clients consume shared tile URLs)  [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Timeline + scrollytelling behavior expectations  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- MapLibre/Cesium usage in the front-end stack  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---