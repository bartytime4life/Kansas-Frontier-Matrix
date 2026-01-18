# 🧩 UI Icons — Samples

![asset:icons](https://img.shields.io/badge/asset-icons-blue)
![scope:samples](https://img.shields.io/badge/scope-samples-6f42c1)
![format:svg-first](https://img.shields.io/badge/format-SVG%20first-2ea44f)
![a11y](https://img.shields.io/badge/a11y-considerations-important-orange)

This folder contains **sample UI icon assets** for the KFM web frontend (prototypes, demos, and reference patterns).

KFM’s frontend structure explicitly calls out `assets/` for **static assets like icons/images** and emphasizes a **responsive + accessible** web app UI.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📁 Folder position (context)

```text
🌐 web/
  🧰 assets/
    🧪 samples/
      🎛️ ui/
        🧩 icons/
          ✅ README.md   ← you are here
          (optional) 🗂️ sprite.svg / defs.svg
          (optional) 🧾 ATTRIBUTION.md
          (optional) 🧷 icon-manifest.json
```

> 💡 **Why keep samples here?**  
> Samples are great for experimentation without forcing production decisions too early (build pipeline, bundler, icon component API, etc.).  

---

## ✅ What “good” looks like

### 🎯 Goals
- **Clarity:** icons communicate an action/state at a glance 🧠
- **Consistency:** coherent stroke, corner radius, perspective, and visual weight 🎛️
- **Accessibility:** icons support assistive tech (or are explicitly decorative) ♿
- **Provenance-first:** each asset is traceable to a source + license 🧾

KFM emphasizes “provenance-first” principles where **citations and metadata are first-class**, and nothing is a black box.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧱 Recommended formats

### ⭐ SVG (preferred)
Why:
- Resolution independent (crisp on retina + zoom)
- Easy theming via CSS (e.g., `currentColor`)
- Can be delivered as a **sprite** for reuse

### 🖼️ PNG (fallback / special cases)
Use when:
- The icon is truly raster (photographic, scanned texture)
- You need pixel-perfect legacy support

---

## 🧩 Using icons in the web UI (patterns)

### Option A — SVG sprite (inline) ✅
Define symbols once (often at the top of the document), then reuse them with `<use>`:

```html
<!-- somewhere once per page -->
<svg style="display:none" aria-hidden="true">
  <symbol id="icon-zoom-in" viewBox="0 0 24 24">
    <path d="..." />
  </symbol>
</svg>

<!-- anywhere -->
<svg class="kfm-icon" aria-hidden="true">
  <use xlink:href="#icon-zoom-in"></use>
</svg>
```

This approach is a common way to reuse SVG symbols via `<use>` and size them with CSS.  [oai_citation:2‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

### Option B — SVG sprite (external file, cached) 🚀
You can keep symbols in an external `defs.svg`/`sprite.svg` and reference them:

```html
<svg class="kfm-icon" aria-hidden="true">
  <use xlink:href="defs.svg#icon-zoom-in"></use>
</svg>
```

This can improve caching (the browser can cache the sprite like other assets).  [oai_citation:3‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

> ⚠️ Note: Some older browsers historically had issues referencing external SVG symbols; if legacy support matters, consider a polyfill strategy.  [oai_citation:4‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

---

### Option C — Inline SVG per icon (simple + explicit)
```html
<svg class="kfm-icon" viewBox="0 0 24 24" role="img" aria-label="Zoom in">
  <title>Zoom in</title>
  <path d="..." />
</svg>
```

---

## 🎨 Styling & theming

### Default “icon class”
```css
.kfm-icon {
  width: 1.25rem;
  height: 1.25rem;
  display: inline-block;
}
```

### Color: use `currentColor` for easy theming 🎨
For single-color icons, letting the icon inherit text color keeps them consistent across themes.

For two-tone effects, you can combine `fill` + `currentColor` patterns (where one path uses `currentColor`).  [oai_citation:5‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## ♿ Accessibility checklist (A11y)

### Decide: decorative vs meaningful
- **Decorative icon:**  
  - add `aria-hidden="true"` and no label/title needed
- **Meaningful icon (communicates content):**  
  - provide an accessible name (`aria-label`, `<title>`, etc.)

SVGs can include `<title>` and `<desc>` tags that help describe the graphic for accessibility.  [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

### Prefer semantic HTML first
If an icon triggers an action, wrap it with a real control:
- ✅ `<button>` for actions
- ✅ `<a>` for navigation

ARIA exists to improve accessibility for dynamic/custom widgets, but semantic elements are still the best baseline.  [oai_citation:7‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

---

## 🏷️ Naming conventions (keep it boring 😌)

### File names
- `kebab-case.svg`
- recommended prefix if needed: `kfm-` or `ui-`

Examples:
- `zoom-in.svg`
- `layer-visible.svg`
- `timeline-play.svg`
- `search.svg`

### Symbol IDs (sprite)
- `icon-<name>` (kebab-case)
- keep stable once published (treat as API)

Examples:
- `icon-zoom-in`
- `icon-layer-visible`

---

## ➕ Adding a new icon (contributor flow)

- [ ] **Name**: `kebab-case` and action-oriented (e.g., `layer-add`, not `plus2`)
- [ ] **ViewBox**: consistent (commonly `0 0 24 24` for UI glyphs)
- [ ] **No hard-coded colors** unless the icon truly requires it  
- [ ] **Accessibility decision**: decorative vs meaningful
- [ ] **Provenance**: record source + license (see below)

---

## 🧾 Provenance & licensing (non-negotiable)

KFM explicitly treats licensing rigorously to avoid conflicts and to foster collaboration.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**If you add/import icons:**
- ✅ record **source URL / author / license**
- ✅ keep an `ATTRIBUTION.md` (or similar) alongside the set
- ✅ avoid “mystery icons” with unclear terms

Suggested minimal attribution entry:
```md
- icon: `layer-visible.svg`
  source: Example Icon Set
  license: CC BY 4.0
  changes: resized to 24x24, removed hard-coded fills
```

---

## 🗺️ Note on map symbols vs UI icons

This directory is for **UI icons** (buttons, controls, panels).  
For **map symbology** (POIs, cartographic markers), consider dedicated map symbol sets—but validate licensing and styling fit.

A curated list of mapping icon libraries (e.g., Mapbox Maki and others) is discussed in the project’s geospatial references.  [oai_citation:9‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)

---

<details>
  <summary>📚 Sources & rationale (project files)</summary>

- KFM frontend structure includes `assets/` for icons/images + responsive/accessibility emphasis. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM “provenance-first” principle: sources + metadata are first-class. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM licensing discipline to prevent conflicts and build trust. [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- SVG `<use>` pattern for reusable symbols + CSS sizing guidance. [oai_citation:13‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- `currentColor` theming concept + reusable icon styling ideas. [oai_citation:14‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- External SVG sprite reference can be cached by the browser; legacy caveats noted. [oai_citation:15‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- SVG `<title>` / `<desc>` for accessibility notes + SVG structuring concepts. [oai_citation:16‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- ARIA purpose + “use semantic elements where possible” guidance. [oai_citation:17‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)  
- Mapping icon library list (for map markers/symbol sets). [oai_citation:18‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)

</details>
