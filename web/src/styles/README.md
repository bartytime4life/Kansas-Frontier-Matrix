# 🎨 KFM Web Styles (`web/src/styles`)

![CSS3](https://img.shields.io/badge/CSS3-ready-blue) ![Responsive](https://img.shields.io/badge/Responsive-mobile--first-success) ![A11y](https://img.shields.io/badge/Accessibility-key-important) ![Design Tokens](https://img.shields.io/badge/Design%20Tokens-CSS%20Variables-informational)

> [!NOTE]
> This folder houses the **global styling primitives** (tokens, themes, resets, utilities) that power the **Kansas Frontier Matrix (KFM)** frontend UI — built for an interface that stays **intuitive, responsive, and informative** across maps, charts, dashboards, and mobile.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## 🧭 What this folder is for

KFM’s frontend is a React SPA with interactive mapping + data visualization, and it relies on **CSS3 (Flexbox/Grid) + media queries** to keep layouts responsive (e.g., mobile layout changes when width is under a breakpoint like ~768px).  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

This `styles/` directory is the “single source of truth” for:

- 🎛️ **Design tokens** (spacing, typography, color, elevation, z-index, motion)
- 🌓 **Theming** (light/dark + high-contrast options)
- 🧼 **Resets + base styles** (cross-browser sanity)
- 🧰 **Utilities** (small reusable helpers when CSS Modules aren’t ideal)
- 🗺️ **Visualization styling conventions** (legends, tooltips, overlays, panels)

> [!TIP]
> Keep *component-specific styling* as close to the component as possible (CSS Modules or scoped styles), and keep *system primitives* here. KFM’s code structure explicitly calls out `styles/` for global CSS or CSS module definitions.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## 🗂️ Suggested layout

> [!IMPORTANT]
> Your repo may not have every file below yet — treat this as the **recommended contract** for how `web/src/styles` should evolve.

```text
📁 web/
  📁 src/
    📁 styles/
      📄 README.md               ← you are here ✅
      📄 index.css               ← single import point (app entry)
      📄 reset.css               ← baseline reset / normalize
      📄 tokens.css              ← raw tokens (scales)
      📄 theme.light.css         ← semantic tokens (light)
      📄 theme.dark.css          ← semantic tokens (dark)
      📄 globals.css             ← base element styles (body, links, etc.)
      📄 utilities.css           ← tiny helpers (opt-in)
      📁 viz/
        📄 map.css               ← map + layer UI styling conventions
        📄 charts.css            ← chart containers + tooltips
        📄 legend.css            ← legend blocks, ramps, labels
      📁 components/
        📄 buttons.module.css    ← shared UI primitives if not using a UI kit
        📄 panels.module.css
        📄 forms.module.css
```

---

## 🔌 How styles are consumed (React)

### ✅ One global entry import
Import **one** file at the app entry (e.g., `src/main.tsx`, `src/index.tsx`, or `src/App.tsx`) so ordering stays consistent:

```ts
import "@/styles/index.css";
```

### ✅ Component scope by default (CSS Modules)
For component-specific styling, prefer co-located modules:

```tsx
import styles from "./MapView.module.css";

export function MapView() {
  return <div className={styles.container}>...</div>;
}
```

> [!NOTE]
> KFM’s frontend is designed around reusable components (MapView, Sidebar, TimelineSlider, ChartPanel), so CSS Modules help keep map/chart complexity from bleeding into global scope.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## 🧬 CSS layering strategy (recommended)

If you want predictable CSS cascade in a complex app (maps + charts + panels), you can adopt **cascade layers**:

```css
/* index.css */
@layer reset, tokens, theme, base, components, utilities, overrides;

@import "./reset.css" layer(reset);
@import "./tokens.css" layer(tokens);
@import "./theme.light.css" layer(theme); /* or theme.dark.css */
@import "./globals.css" layer(base);
@import "./utilities.css" layer(utilities);
```

> [!WARNING]
> `@import` can increase HTTP requests and impact load speed if misused. Use sparingly and rely on your bundler whenever possible.  [oai_citation:4‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## 🧱 Design tokens

### 🎛️ Raw tokens vs semantic tokens
**Raw tokens** define consistent scales (spacing steps, font sizes, radii).  
**Semantic tokens** map those scales to meaning (surface, text, border, accent).

#### `tokens.css` (raw scales)
```css
:root {
  /* 🧷 Spacing (4px baseline grid) */
  --kfm-space-0: 0;
  --kfm-space-1: 0.25rem; /* 4px */
  --kfm-space-2: 0.5rem;  /* 8px */
  --kfm-space-3: 0.75rem; /* 12px */
  --kfm-space-4: 1rem;    /* 16px */
  --kfm-space-6: 1.5rem;  /* 24px */
  --kfm-space-8: 2rem;    /* 32px */

  /* 🔤 Typography */
  --kfm-font-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, "Noto Sans", "Liberation Sans", sans-serif;
  --kfm-font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  --kfm-text-0: 0.875rem; /* 14px */
  --kfm-text-1: 1rem;     /* 16px */
  --kfm-text-2: 1.125rem; /* 18px */
  --kfm-text-3: 1.25rem;  /* 20px */

  /* 🧊 Radius */
  --kfm-radius-1: 0.25rem;
  --kfm-radius-2: 0.5rem;
  --kfm-radius-3: 0.75rem;

  /* 🧭 Z-index (keep map + panels sane) */
  --kfm-z-map: 1;
  --kfm-z-overlay: 10;
  --kfm-z-panel: 20;
  --kfm-z-modal: 100;
  --kfm-z-toast: 200;

  /* 🎞️ Motion */
  --kfm-ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --kfm-dur-fast: 120ms;
  --kfm-dur-base: 180ms;
  --kfm-dur-slow: 260ms;
}
```

#### `theme.light.css` (semantic mapping)
```css
:root[data-theme="light"] {
  --kfm-surface: #ffffff;
  --kfm-surface-2: #f7f7f9;
  --kfm-text: #111827;
  --kfm-text-muted: #4b5563;
  --kfm-border: #e5e7eb;

  --kfm-accent: #2563eb;
  --kfm-accent-contrast: #ffffff;

  --kfm-focus: #2563eb;
}
```

#### `theme.dark.css`
```css
:root[data-theme="dark"] {
  --kfm-surface: #0b1220;
  --kfm-surface-2: #111a2e;
  --kfm-text: #e5e7eb;
  --kfm-text-muted: #9ca3af;
  --kfm-border: #24324a;

  --kfm-accent: #60a5fa;
  --kfm-accent-contrast: #0b1220;

  --kfm-focus: #93c5fd;
}
```

> [!TIP]
> For map layers (NDVI, soil moisture, rainfall), define **named ramps** as tokens (e.g., `--kfm-ramp-ndvi-0..n`) so legends, overlays, and charts stay consistent. KFM explicitly prioritizes intuitive styling and accessibility (including colorblind-friendly choices).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## 📱 Responsive design rules

KFM’s UI is expected to be fully responsive and to adapt layouts (side-by-side vs stacked, swipeable panels, etc.) using **Flexbox/Grid + media queries**.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

### ✅ Breakpoints
KFM documentation gives an example breakpoint behavior at **~768px** for switching to mobile layout.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

Recommended baseline breakpoints:

```css
/* Mobile-first: base styles first */

@media (min-width: 48rem) { /* 768px */
  /* tablet+ */
}

@media (min-width: 64rem) { /* 1024px */
  /* desktop */
}

@media (min-width: 80rem) { /* 1280px */
  /* large desktop */
}
```

### ✅ Prefer em/rem for MQs when appropriate
Media queries can be specified in pixels **or** em/rem units. Example: `800px` can be expressed as `50em` (800/16) for a font-relative breakpoint.  [oai_citation:8‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

```css
/* 800px ≈ 50em when 1em = 16px */
@media (min-width: 50em) {
  .layout { display: grid; }
}
```

---

## ♿ Accessibility & UX essentials

KFM’s frontend emphasizes accessibility and cross-browser behavior (semantic elements, labels, ARIA where needed, and color choices that are colorblind-friendly).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

### ✅ Focus rings that don’t disappear
```css
:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 3px solid var(--kfm-focus);
  outline-offset: 2px;
}
```

### ✅ Reduced motion support (maps + charts can be intense)
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 1ms !important;
    transition-duration: 1ms !important;
    scroll-behavior: auto !important;
  }
}
```

### ✅ Color + shape (not just color)
For legends and status indicators, pair:
- 🎨 color ramps
- 🔣 labels (text)
- ▦ patterns / icons when possible (e.g., dashed vs solid outlines)

> [!NOTE]
> This matters especially in KFM because users compare geospatial layers and trends; clarity and trust are core UX requirements.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## 🗺️ Maps, layers, legends, and overlays

KFM’s UI includes interactive mapping (2D/3D) and a layer-toggling workflow, so the visual system must stay coherent across:
- Map tiles / vector overlays
- Sidebar toggles + legend
- Timeline slider states
- Popups/tooltips
- Dashboard mini-panels  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

### 🎛️ Suggested “viz primitives”
Put these in `styles/viz/*` so MapView/Cesium/Leaflet/Mapbox components share a consistent look.

```css
/* viz/legend.css */
.kfmLegend {
  background: color-mix(in oklab, var(--kfm-surface) 92%, transparent);
  border: 1px solid var(--kfm-border);
  border-radius: var(--kfm-radius-2);
  padding: var(--kfm-space-3);
  box-shadow: 0 6px 24px rgba(0,0,0,0.12);
}

.kfmLegend__title {
  font-weight: 700;
  font-size: var(--kfm-text-2);
  margin-bottom: var(--kfm-space-2);
}

.kfmLegend__row {
  display: flex;
  align-items: center;
  gap: var(--kfm-space-2);
  margin: 0 0 var(--kfm-space-1) 0;
}

.kfmLegend__swatch {
  inline-size: 1rem;
  block-size: 1rem;
  border-radius: 0.2rem;
  border: 1px solid var(--kfm-border);
}
```

### 🧠 Keep “meaning” in tokens, not in components
Instead of:
- `background: #00ff00; /* NDVI good */`

Prefer:
- `background: var(--kfm-ramp-ndvi-high);`

This makes it easier to:
- tune palettes for accessibility
- keep charts and legends consistent
- share ramps between 2D/3D modes  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## 🧰 Naming conventions & best practices

### ✅ Naming
Pick one and keep it consistent:

- **CSS Modules:** `camelCase` for local classes (recommended)
  - `container`, `panelHeader`, `legendRow`
- **Global/Viz primitives:** `kfmPrefix__block--modifier` (BEM-ish)
  - `.kfmLegend`, `.kfmLegend__row`, `.kfmLegend--compact`

### ✅ Rules of thumb
- 🧊 Use tokens: `var(--kfm-*)` for spacing, colors, radii, durations.
- 🧱 Prefer layout with Flexbox/Grid (KFM explicitly expects this).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)
- 🧼 Keep global selectors minimal (avoid `div { ... }`).
- 🧵 Avoid `!important` (unless you’re writing a small “override” layer for a 3rd-party widget).
- 🧪 Test at breakpoints + common browsers (Chrome/Firefox/Safari/Edge + mobile).  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)

---

## ✅ Style PR checklist

- [ ] Uses tokens (`--kfm-*`) instead of hard-coded magic numbers where practical 🎯  
- [ ] Works at mobile breakpoint (≈768px) + desktop layout 📱💻  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)  
- [ ] Keyboard focus is visible (`:focus-visible`) ⌨️  
- [ ] Motion respects `prefers-reduced-motion` 🎞️  
- [ ] Legend / overlays remain readable on map backgrounds 🗺️  
- [ ] No global leakage (CSS Modules for component styling) 🧩  

---

## 📚 References (project source material)

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation & Markdown Guide.gdoc](file-service://file-XGC3Vf2AfbA2JWvTvmHNGF)  
- Responsive Web Design with HTML5 and CSS3 (media queries, px vs em/rem guidance, @import considerations)  [oai_citation:18‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  

---