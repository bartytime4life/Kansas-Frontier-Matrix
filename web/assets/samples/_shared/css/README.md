# 🎨 `web/assets/samples/_shared/css/` — Shared CSS for KFM Samples

This folder contains **shared, reusable CSS** for the **static sample pages** under `web/assets/samples/`.  
Goal: keep samples **consistent, readable, and provenance-friendly** without dragging a full framework into every demo.

> ✅ Samples should be **easy to copy**, **easy to audit**, and **safe to evolve**.

---

## 🧭 Table of Contents

- [What belongs here](#-what-belongs-here)
- [Design principles](#-design-principles)
- [Recommended file layout](#-recommended-file-layout)
- [How to use in a sample page](#-how-to-use-in-a-sample-page)
- [CSS “contracts”](#-css-contracts)
- [Tokens & theming](#-tokens--theming)
- [Components & utilities](#-components--utilities)
- [Responsive rules](#-responsive-rules)
- [Accessibility & motion](#-accessibility--motion)
- [Performance notes](#-performance-notes)
- [Contribution checklist](#-contribution-checklist)
- [References](#-references)

---

## 📦 What belongs here

**✅ Yes**
- Minimal **reset / base** styles that make samples render consistently
- Shared **design tokens** (CSS Custom Properties)
- Shared **utilities** (spacing, layout helpers, visually-hidden, etc.)
- Tiny sample-friendly **components** (badges, panels, tooltips, legends)
- Styles for **trust UI cues** (source badges, “AI-suggested” labels, restricted-data styling)

**🚫 No**
- App-specific React styling (belongs in the main `web/` app styling system)
- One-off tweaks for a single sample (keep those near the sample)
- Huge CSS frameworks (samples should teach, not hide complexity)

---

## 🧠 Design principles

These samples follow KFM’s broader **contract-first / provenance-first / evidence-first** philosophy.

### 1) 🔎 No “mystery styles”
If a selector exists, it should have a **reason** and a **home**:
- “one thing, one place” (tokens defined once; utilities defined once)
- avoid copy-pasting “just for this sample” into shared files

### 2) 🧾 Trust cues are first-class UI
KFM’s UI is expected to surface provenance and governance concepts (e.g., **source**, **license**, **AI-generated**, **restricted**).  
Shared CSS should include patterns that make these cues:
- visually consistent ✅
- hard to miss ✅
- accessible ✅

### 3) 🧱 Small, layered, predictable
Prefer:
- simple selectors (`.kfm-card`, `.kfm-badge`)  
- shallow cascade  
- `@layer` for ordering (optional but recommended)

### 4) 🧑‍🤝‍🧑 Human-centered defaults
Make it comfortable to read and use:
- sane typography defaults
- consistent spacing scale
- accessible focus states
- motion respects user preference

---

## 🗂️ Recommended file layout

> This is a **suggested** structure. If the folder already has files, keep names consistent and evolve toward this shape.

```text
web/assets/samples/_shared/css/
├─ 📄 README.md                          # 👈 you are here 📌 How sample CSS is structured, naming, and layering order
├─ 🎛️📄 tokens.css                       # 🎛️ Design tokens: CSS vars for colors/spacing/typography (samples-only)
├─ 🧱🧼📄 base.css                        # 🧱 Reset + base element defaults (type, links, focus rings, forms)
├─ 🧩📐📄 layout.css                      # 🧩 Layout helpers: containers, grids, stacks, clusters (minimal)
├─ 🧰📄 components.css                   # 🧰 Reusable sample components: cards, badges, panels, callouts
├─ 🧪🧰📄 utilities.css                   # 🧪 Utility helpers (.u-*): spacing, display, visually-hidden, etc.
└─ 🧵📄 samples.css                      # 🧵 Optional entry point that imports/layers the above in order
```

---

## 🔌 How to use in a sample page

### Option A: Link individual files (simple & explicit)
Use relative paths from the sample HTML file:

```html
<link rel="stylesheet" href="../_shared/css/tokens.css">
<link rel="stylesheet" href="../_shared/css/base.css">
<link rel="stylesheet" href="../_shared/css/layout.css">
<link rel="stylesheet" href="../_shared/css/components.css">
<link rel="stylesheet" href="../_shared/css/utilities.css">
```

### Option B: Link a single entry stylesheet (cleanest)
If you maintain a `samples.css` entry point:

```html
<link rel="stylesheet" href="../_shared/css/samples.css">
```

If you use `@layer`, your entry point can define load order:

```css
/* samples.css */
@layer tokens, base, layout, components, utilities;

@import url("./tokens.css") layer(tokens);
@import url("./base.css") layer(base);
@import url("./layout.css") layer(layout);
@import url("./components.css") layer(components);
@import url("./utilities.css") layer(utilities);
```

> ⚠️ Note: `@import` can slow rendering in some contexts. Prefer multiple `<link>` tags if you want maximal simplicity/perf.

---

## 📜 CSS contracts

In KFM, “contracts” are treated as first-class boundaries.  
For sample CSS, our **contract** is:

- **Tokens** (CSS Custom Properties) ✅  
- **Public class API** (component + utility class names) ✅  
- **Behavioral conventions** (how states and themes are expressed) ✅  

### Contract rules
- Changing a token name or a public class name is a **breaking change**
- Additive changes are preferred (new token, new class, new variant)
- If you must break: provide a short migration note in this README

### Suggested “contract header” (per shared file)
```css
/*
  KFM Samples Shared CSS — Contract Header
  Layer: components
  Public API: .kfm-card, .kfm-badge, .kfm-pill, .kfm-panel
  Version: 0.1.0 (bump on breaking changes)
*/
```

---

## 🎛️ Tokens & theming

### Token naming
- Prefix tokens with `--kfm-`
- Group by domain: `--kfm-color-*`, `--kfm-space-*`, `--kfm-font-*`, `--kfm-radius-*`

Example:

```css
:root {
  /* Colors */
  --kfm-color-bg: #0b0f14;
  --kfm-color-fg: #e7eef8;
  --kfm-color-muted: #a7b4c6;

  /* Accents */
  --kfm-color-accent: #4da3ff;

  /* Spacing scale */
  --kfm-space-1: 0.25rem;
  --kfm-space-2: 0.5rem;
  --kfm-space-3: 0.75rem;
  --kfm-space-4: 1rem;

  /* Radius */
  --kfm-radius-2: 0.5rem;

  /* Typography */
  --kfm-font-body: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  --kfm-font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
}
```

### Theme switching
Prefer a **data attribute** on the root element:

```html
<html data-theme="dark">
```

```css
:root[data-theme="light"] {
  --kfm-color-bg: #ffffff;
  --kfm-color-fg: #0b0f14;
}
```

---

## 🧰 Components & utilities

### Naming conventions
- Components: `.kfm-*`
- Utilities: `.u-*`
- State: prefer attributes or modifiers:
  - `.kfm-badge--ai`
  - `[data-state="loading"]`
  - `[aria-busy="true"]`

### Trust cues (recommended shared patterns)

KFM’s UI standards emphasize provenance and governance. Samples should have a consistent visual language for:

- **Source-backed** content
- **AI-suggested** content
- **Restricted / redacted** content

Example HTML:

```html
<div class="kfm-card">
  <div class="kfm-card__header">
    <span class="kfm-badge kfm-badge--source">Source: STAC</span>
    <span class="kfm-badge kfm-badge--ai">AI-suggested</span>
    <span class="kfm-badge kfm-badge--restricted">Restricted</span>
  </div>
  <p class="kfm-card__body">
    This panel demonstrates provenance-linked UI cues.
  </p>
</div>
```

Example CSS:

```css
.kfm-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  font: 600 0.75rem/1 var(--kfm-font-body);
  border: 1px solid color-mix(in oklab, var(--kfm-color-fg) 20%, transparent);
}

.kfm-badge--source { }
.kfm-badge--ai { }
.kfm-badge--restricted { }
```

> Tip: keep badge variants mostly token-driven (so themes work “for free”).

### Utilities (minimal set)
Recommended utilities for samples:
- `.u-sr-only` (screen-reader-only)
- `.u-stack` (vertical spacing)
- `.u-row` / `.u-col` (simple flex helpers)
- `.u-wrap` (wrap long words/URLs)
- `.u-mono` (code-ish text)
- `.u-shadow` (subtle elevation)

---

## 📱 Responsive rules

### Mobile-first default
Start with the small layout, then add breakpoints for larger viewports.

### Breakpoints as tokens
Avoid hardcoding breakpoints all over:

```css
:root {
  --kfm-bp-sm: 40rem;  /* ~640px */
  --kfm-bp-md: 60rem;  /* ~960px */
  --kfm-bp-lg: 80rem;  /* ~1280px */
}
```

Use:

```css
@media (min-width: var(--kfm-bp-md)) {
  .kfm-card { /* enhancements */ }
}
```

### Fluid type (optional but nice)
```css
.kfm-title {
  font-size: clamp(1.1rem, 2vw + 0.75rem, 1.75rem);
}
```

---

## ♿ Accessibility & motion

### Focus styles are not optional
If you restyle focus, keep it visible:

```css
:where(a, button, input, select, textarea):focus-visible {
  outline: 2px solid var(--kfm-color-accent);
  outline-offset: 2px;
}
```

### Reduced motion support
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Color contrast
- Don’t rely on color alone for meaning (add icons/labels/patterns)
- “Restricted” UI should be obvious even in grayscale

---

## ⚡ Performance notes

Samples are small, but we still want good habits:

- ✅ Prefer fewer CSS files when publishing (but keep dev files readable)
- ✅ Avoid expensive selectors (`div > div > div ...`), keep specificity low
- ✅ Keep animations subtle and limited (especially on map UIs)
- ✅ Avoid reflow-heavy transitions (prefer opacity/transform)

---

## ✅ Contribution checklist

When you change anything in `_shared/css/`:

- [ ] Did you update **tokens** instead of hardcoding a new color/spacing?
- [ ] Did you keep the **public class API** stable?
- [ ] Did you avoid adding sample-specific hacks to shared files?
- [ ] Did you test in at least:
  - [ ] a narrow viewport
  - [ ] a wide viewport
  - [ ] keyboard navigation (Tab/Shift+Tab)
  - [ ] reduced motion mode
- [ ] If you introduced a new shared component, did you add a tiny snippet/example here?

---

## 📚 References

These project docs influenced the “contract-first / provenance-first” stance and how UI should communicate trust:

- Kansas Frontier Matrix — Comprehensive Technical Documentation (PDF)  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Kansas Frontier Matrix — Master Guide v13 (Draft)  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- KFM — Open-Source Geospatial Historical Mapping Hub Design (PDF)  [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  
- Responsive Web Design with HTML5 and CSS3 (PDF)  [oai_citation:3‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- Introduction to Digital Humanism (PDF)  [oai_citation:4‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  

---

## 🏷️ Optional: “real” GitHub badges (copy/paste)

> If you want badges at the top of this README, here are examples.  
> (Kept in a code block so URLs don’t clutter the page.)

```md
![CSS](https://img.shields.io/badge/CSS-Shared%20Samples-blue)
![Responsive](https://img.shields.io/badge/Responsive-Mobile--first-success)
![A11y](https://img.shields.io/badge/A11y-Focus%20%2B%20Reduced%20Motion-informational)
![Provenance-first](https://img.shields.io/badge/KFM-Provenance--first-purple)
```
