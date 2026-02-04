# 🎨 KFM Styles System (`web/src/styles`)

![scope](https://img.shields.io/badge/scope-web%2Fsrc%2Fstyles-blue)
![approach](https://img.shields.io/badge/approach-design%20tokens%20%2B%20themes%20%2B%20CSS%20Modules-success)
![ui](https://img.shields.io/badge/ui-map--first%20%2B%20provenance--first-purple)
![status](https://img.shields.io/badge/status-living%20document-orange)

Welcome to the **global styling hub** for the Kansas Frontier Matrix (KFM) web app.  
This folder is where we keep **design tokens**, **themes**, and **global/Vendor styles** that must be shared across the UI.

> ✅ Goal: a UI that looks consistent, stays maintainable as the app grows, and keeps *trust & evidence* readable (citations, audit panels, provenance cues).

---

## 🧭 Quick links

- [What belongs in this folder](#-what-belongs-in-this-folder)
- [Recommended folder layout](#-recommended-folder-layout)
- [Styling rules of the road](#-styling-rules-of-the-road)
- [Theming](#-theming)
- [Design tokens](#-design-tokens)
- [CSS Modules & component styles](#-css-modules--component-styles)
- [Map UI & vendor overrides](#-map-ui--vendor-overrides)
- [Citations & audit UI](#-citations--audit-ui)
- [Accessibility & motion](#-accessibility--motion)
- [Contributing checklist](#-contributing-checklist)

---

## 📦 What belongs in this folder

### ✅ Put these here
- **Global tokens** (colors, spacing, typography, radii, shadows, z-index, motion)
- **Theme definitions** (light/dark + domain accents like Maps/AI/History/etc.)
- **Global base styles** (reset, typography baseline, app shell layout helpers)
- **Cross-cutting utilities** that are truly global (rare)
- **Vendor overrides** (MapLibre/Cesium control styling, third-party widgets)

### ❌ Don’t put these here
- Component-specific styling that only one component uses  
  → Keep that next to the component as a CSS Module (e.g., `Button.module.css`).

---

## 🗂 Recommended folder layout

> This is the *intended* structure for long-term sanity. If the repo differs, update this tree so it reflects reality.

```text
📁 web/
  📁 src/
    📁 styles/
      📄 README.md                👈 you are here
      📄 index.css                🌍 single import entry for global styles
      📄 reset.css                🧼 minimal reset / normalize-ish rules
      📄 tokens.css               🎛️ CSS custom properties (design tokens)
      📄 themes.css               🌓 light/dark + domain accents
      📄 globals.css              🧱 typography, base elements, app shell defaults
      📄 utilities.css            🧰 tiny set of global helpers (keep small!)
      📁 vendor/
        📄 maplibre-overrides.css 🗺️ MapLibre control + popup adjustments
        📄 cesium-overrides.css   🌎 Cesium UI adjustments
```

---

## 🧱 Styling rules of the road

### 1) Token-first (single source of truth)
If you catch yourself repeating a value (color/spacing/radius) in multiple places:  
**promote it to a token** and reuse it.

### 2) Local-by-default
Component styles should be **scoped** (CSS Modules). Globals are a special case.

### 3) Global CSS is *expensive*
Every global selector is a future collision risk. Keep global selectors:
- **predictable**
- **shallow**
- **prefixed**
- **rare**

### 4) Map-first layout
The map is the canvas; UI panels sit above it.
- overlays must stay readable over bright/dark imagery
- controls must be finger-friendly (touch targets) and keyboard-friendly
- z-index should be governed, not improvised

---

## 🎭 Theming

KFM supports:
- **Base theme**: light/dark
- **Domain accents**: Maps / AI / History / Ecology / Weather (and future domains)

### Theme toggles (recommended)
Apply theme and domain state as attributes on a single top-level element:

```html
<body data-theme="dark" data-domain="maps">
  <!-- app -->
</body>
```

### Theme variables (recommended)
Use CSS variables so components don’t care *which* theme they’re in:

```css
/* themes.css */
:root {
  --kfm-accent: var(--kfm-accent-maps);
  --kfm-bg: #ffffff;
  --kfm-fg: #111111;
}

[data-theme="dark"] {
  --kfm-bg: #0b0d12;
  --kfm-fg: #eef2ff;
}

[data-domain="maps"]   { --kfm-accent: var(--kfm-accent-maps); }
[data-domain="ai"]     { --kfm-accent: var(--kfm-accent-ai); }
[data-domain="history"]{ --kfm-accent: var(--kfm-accent-history); }
[data-domain="ecology"]{ --kfm-accent: var(--kfm-accent-ecology); }
[data-domain="weather"]{ --kfm-accent: var(--kfm-accent-weather); }
```

> 💡 The key idea: **components read `--kfm-accent`** (not “Maps green” directly).  
> That keeps the design system consistent while still giving each domain identity.

---

## 🎛 Design tokens

All tokens should live in `tokens.css` as CSS custom properties.

### Naming convention
Use a stable prefix and consistent categories:

- `--kfm-color-*`
- `--kfm-space-*`
- `--kfm-font-*`
- `--kfm-radius-*`
- `--kfm-shadow-*`
- `--kfm-z-*`
- `--kfm-motion-*`

Example:

```css
/* tokens.css */
:root {
  /* 🎨 Color */
  --kfm-color-bg: #ffffff;
  --kfm-color-fg: #111111;
  --kfm-color-muted: #6b7280;

  /* 🧩 Domain accents */
  --kfm-accent-maps:   #1f7a3f;
  --kfm-accent-ai:     #2563eb;
  --kfm-accent-history:#92400e;
  --kfm-accent-ecology:#6b8e23;
  --kfm-accent-weather:#0ea5e9;

  /* 📐 Spacing */
  --kfm-space-1: 4px;
  --kfm-space-2: 8px;
  --kfm-space-3: 12px;
  --kfm-space-4: 16px;

  /* 🔤 Typography */
  --kfm-font-sans: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  --kfm-font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;

  /* 🧊 Radius */
  --kfm-radius-1: 6px;
  --kfm-radius-2: 10px;

  /* 🧱 Elevation / shadows */
  --kfm-shadow-1: 0 1px 2px rgba(0,0,0,0.10);
  --kfm-shadow-2: 0 6px 18px rgba(0,0,0,0.18);

  /* 🧷 Layering */
  --kfm-z-map: 0;
  --kfm-z-overlay: 10;
  --kfm-z-panel: 20;
  --kfm-z-modal: 40;
  --kfm-z-toast: 50;

  /* 🌀 Motion */
  --kfm-motion-fast: 120ms;
  --kfm-motion-med:  180ms;
}
```

---

## 🧩 CSS Modules & component styles

### Recommended practice
- Global styles here: `web/src/styles/*`
- Component styles live next to their components:

```text
📁 web/src/components/
  📁 Button/
    📄 Button.tsx
    📄 Button.module.css
```

### Example: a button using tokens + CSS Modules
```css
/* Button.module.css */
.root {
  font: 600 14px/1 var(--kfm-font-sans);
  padding: var(--kfm-space-2) var(--kfm-space-3);
  border-radius: var(--kfm-radius-1);
  border: 1px solid color-mix(in srgb, var(--kfm-accent), transparent 65%);
  background: color-mix(in srgb, var(--kfm-accent), transparent 85%);
  color: var(--kfm-fg);
}

.root:focus-visible {
  outline: 3px solid color-mix(in srgb, var(--kfm-accent), transparent 40%);
  outline-offset: 2px;
}
```

```tsx
// Button.tsx
import styles from "./Button.module.css";

export function Button(props: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return <button {...props} className={styles.root} />;
}
```

---

## 🗺 Map UI & vendor overrides

KFM’s UI is map-centric, and the map stack often brings its own DOM + default styling.  
We keep vendor overrides here so they’re easy to locate and audit.

### Vendor CSS rules
- Put MapLibre/Cesium overrides in `styles/vendor/*`
- Prefer **targeted** selectors (avoid `*` or broad global rules)
- Never depend on brittle DOM structure unless unavoidable
- Keep overrides commented with *why* they exist

```css
/* vendor/maplibre-overrides.css */
/* Adjust map controls to match KFM panels and improve touch targets */
.maplibregl-ctrl-group button {
  min-width: 36px;
  min-height: 36px;
  border-radius: var(--kfm-radius-1);
}
```

> 🧠 Tip: If you’re using CSS Modules elsewhere, treat vendor overrides as the exception:
> vendor libraries usually require global selectors.

---

## 🔎 Citations & audit UI

KFM is **provenance-first**: users should be able to *see* and *verify* sources.

That means we style:
- citation chips / footnote markers
- “open source” links
- audit panels / drawers that show retrieved snippets & provenance details
- “confidence / caveat” callouts (when applicable)

### Recommended global classes (prefixed)
These classes are global because they often appear in rendered markdown/AI output:

```css
/* globals.css (or a dedicated citations.css) */
.kfm-citation {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 0 8px;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, var(--kfm-accent), transparent 60%);
  background: color-mix(in srgb, var(--kfm-accent), transparent 88%);
  font: 600 12px/20px var(--kfm-font-sans);
}

.kfm-citation a {
  color: inherit;
  text-decoration: none;
}

.kfm-citation a:hover {
  text-decoration: underline;
}
```

### Audit panel styling notes
- Use a **drawer** pattern (right side) or **bottom sheet** on small screens
- Show snippet text in a readable mono/sans pairing
- Provide obvious affordances: close button, copy snippet, open source link
- Don’t over-style: credibility comes from clarity, not decoration

---

## ♿ Accessibility & motion

### Focus states
Never remove focus outlines unless replacing them with something better.

### Reduced motion
Always respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 1ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Contrast
- UI overlays must remain legible over satellite imagery and bright basemaps
- Use scrims/backplates behind text-heavy panels

---

## ✅ Contributing checklist

Before you commit style changes:

- [ ] Did I reuse tokens instead of inventing new one-off values?
- [ ] Is this style truly global? If not, move it to a CSS Module.
- [ ] Are vendor overrides isolated under `styles/vendor/`?
- [ ] Did I check light + dark themes?
- [ ] Did I check at least one narrow viewport?
- [ ] Did I verify keyboard focus and hover/focus-visible behavior?
- [ ] Did I keep selectors shallow and avoid accidental global collisions?

---

## 🧪 Nice-to-have upgrades (future)

- 🧷 Add Stylelint + a small ruleset (especially for globals)
- 🧫 Add visual regression checks for key UI panels (map controls, citations, audit drawer)
- 🧰 Convert `utilities.css` to a *tiny* curated set (or remove it if it grows wild)

---

💬 If you’re unsure where a style should go: **default to CSS Modules next to the component** — and only promote to `web/src/styles` when multiple parts of the app truly share the rule.
