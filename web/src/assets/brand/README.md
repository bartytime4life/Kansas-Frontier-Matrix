<div align="center">

# 🧭 Kansas Frontier Matrix — Brand Assets

**Single-source-of-truth UI branding for the KFM web client**  
_Logos, icons, tokens, and visual rules that help our maps + stories stay consistent, readable, and trustworthy._

![scope](https://img.shields.io/badge/scope-web%2Fsrc%2Fassets%2Fbrand-0b7285?style=for-the-badge)
![type](https://img.shields.io/badge/type-brand%20assets-364fc7?style=for-the-badge)
![rules](https://img.shields.io/badge/rules-contract--first%20%26%20evidence--first-2f9e44?style=for-the-badge)

</div>

---

## 🎯 Purpose

This folder is the **canonical home** for KFM web-brand artifacts:
- ✅ **Marks** (logo / wordmark), **icons**, **favicons**, **badges**
- ✅ **Design tokens** (colors, typography, radii, shadows) used by the UI
- ✅ **Patterns / textures** that support cartographic accessibility and “dual encoding” (color + pattern)
- ✅ **Metadata & governance** so every shipped visual asset is attributable and safe to use

> 🧩 **Core idea:** In KFM, the UI is a *boundary* that must remain consistent and governed. Brand assets and tokens are treated like **contract artifacts**: versioned, reviewable, and reusable across the app.

---

## 🗂️ Recommended folder layout

> If some of these folders don’t exist yet, this README still defines the *target* structure and naming rules.

```text
web/src/assets/brand/
├── README.md
├── logos/                # KFM marks (SVG first)
│   ├── kfm-mark.svg
│   ├── kfm-wordmark.svg
│   └── kfm-lockup-horizontal.svg
├── icons/                # product + UI icons (SVG)
│   ├── ui/
│   └── domains/
├── favicons/             # favicon + PWA icons
├── patterns/             # hatching/textures for map layers + charts
├── tokens/               # design tokens (CSS vars + optional JSON)
│   ├── brand.css
│   ├── brand.tokens.json
│   └── README.md
└── meta/                 # provenance + licensing + manifest
    ├── brand.manifest.json
    ├── LICENSES.md
    └── SOURCES.md
```

---

## 🚀 Quick usage (React / TS)

### 1) Use a logo as an `<img>` (safe default ✅)

```tsx
import kfmMarkUrl from "@/assets/brand/logos/kfm-mark.svg";

export function HeaderBrand() {
  return (
    <img
      src={kfmMarkUrl}
      alt="Kansas Frontier Matrix"
      width={28}
      height={28}
      loading="eager"
      decoding="async"
    />
  );
}
```

### 2) Use an SVG *as a component* (if your toolchain supports it)

If your bundler supports SVGR (or an equivalent plugin), this gives better control for sizing and accessibility:

```tsx
import { ReactComponent as KfmMark } from "@/assets/brand/logos/kfm-mark.svg";

export function HeaderBrand() {
  return (
    <KfmMark role="img" aria-label="Kansas Frontier Matrix" />
  );
}
```

> ♿ Tip: If an SVG is **purely decorative**, set `aria-hidden="true"` and **omit** `aria-label`.

---

## 🎨 Design tokens (our “brand contract”)

KFM supports theming (ex: light/dark) through **design tokens** (typically CSS variables).  
**Never** hardcode one-off hex values in components for “brand colors” — always use tokens.

### Token naming rules ✅
- Prefix with `--kfm-`
- Prefer semantic names over raw color names  
  - ✅ `--kfm-color-bg`, `--kfm-color-fg`, `--kfm-color-accent`
  - ❌ `--kfm-teal`, `--kfm-blue2`

### Example: `tokens/brand.css`

```css
:root {
  /* Color (semantic) */
  --kfm-color-bg: #0b0f14;
  --kfm-color-surface: #101826;
  --kfm-color-fg: #f8fafc;
  --kfm-color-muted: #94a3b8;
  --kfm-color-accent: #2dd4bf;

  /* Type */
  --kfm-font-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, "Noto Sans", "Liberation Sans", sans-serif;
  --kfm-font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  /* Shape */
  --kfm-radius-sm: 8px;
  --kfm-radius-md: 12px;
  --kfm-radius-lg: 16px;
}

/* Optional: theme switching */
[data-theme="dark"] {
  --kfm-color-bg: #0b0f14;
  --kfm-color-surface: #101826;
  --kfm-color-fg: #f8fafc;
}

[data-theme="light"] {
  --kfm-color-bg: #ffffff;
  --kfm-color-surface: #f5f7fb;
  --kfm-color-fg: #0b0f14;
}
```

> 🧠 Treat tokens like APIs: changes to token meaning (not just value tweaks) are breaking changes.

---

## 🧭 Logo rules (do / don’t)

### ✅ Do
- Keep aspect ratio locked (no stretching)
- Prefer **SVG** for crisp scaling
- Maintain clear space around marks  
  - suggested: at least **0.5×** mark height as padding
- Use monochrome variants when overlaying complex imagery (maps, aerials, etc.)

### ❌ Don’t
- Don’t recolor the logo ad-hoc (make a named variant if needed)
- Don’t add drop shadows/glows unless it’s a documented variant
- Don’t place full-color marks on low-contrast map tiles

---

## 🧩 Iconography guidelines

We want icons that read well at small sizes, especially on map UIs.

**Recommended constraints**
- Design on a 24×24 grid (or 20×20) and export as SVG
- Use consistent stroke weights
- Round joins/caps for friendliness + legibility
- Avoid tiny negative spaces that disappear at 16px

**Naming**
- `icons/ui/<name>.svg` (generic UI)
- `icons/domains/<domain>-<name>.svg` (domain-specific concepts)

---

## 🗺️ Maps & data visualization styling

KFM is map-forward. Brand choices must **support interpretation**, not compete with it.

### 1) Dual encoding (color + pattern) ✅
When a meaning matters (especially “restricted / sensitive / confidence / access”), encode it in **more than one channel**:
- Color **and** hatching / texture
- Light/dark **and** line style
- Icon shape **and** label

> This improves accessibility (color vision deficiency) and improves comprehension at different zoom levels.

### 2) Scale-aware symbology
- At small scales (statewide): prioritize **simpler** styling, fewer classes, stronger contrast
- At large scales (street-level): allow more detail, but keep consistent token usage

### 3) Sensitive contexts
Some layers may be generalized, suppressed, or shown with warnings depending on governance rules.  
Brand elements must not “over-promise precision” (e.g., avoid crisp pinpoint glyphs for intentionally generalized locations).

---

## ♿ Accessibility requirements (non-negotiable)

### Text + UI contrast
- Target WCAG AA contrast for text (especially on basemap imagery).
- Always test contrast in **both** themes and over **map tiles**.

### No “color-only” meaning
If color is used to signal state (warning, restricted, active), add at least one of:
- Icon change
- Pattern fill
- Text label
- Border/shape change

### Alt text rules
- Logos used as identity: `alt="Kansas Frontier Matrix"`
- Decorative marks: `aria-hidden="true"` and empty `alt=""`

---

## 🧾 Provenance, licensing, and governance

Brand assets must be as traceable as other KFM artifacts.

### Every shipped asset MUST have:
- Source/creator (human or tool)
- License (or explicit permission)
- Modification notes (if altered)
- Intended usage + where it appears in the UI

### Recommended: `meta/brand.manifest.json`
A lightweight manifest helps prevent “mystery assets”:

```json
{
  "version": "0.1.0",
  "assets": [
    {
      "path": "logos/kfm-mark.svg",
      "type": "logo",
      "license": "Project-owned",
      "source": "KFM Design",
      "notes": "Primary mark. Use on headers and loading screens.",
      "a11y": { "defaultAlt": "Kansas Frontier Matrix" }
    }
  ]
}
```

> 🛡️ If an asset’s license is unclear, it does **not** ship.

---

## ✅ Adding or updating a brand asset (checklist)

**Before you commit**
- [ ] Asset is in the correct folder (`logos/`, `icons/`, `tokens/`, etc.)
- [ ] File name is kebab-case and prefixed where appropriate (`kfm-…`)
- [ ] SVGs are optimized (SVGO or equivalent) without breaking geometry
- [ ] Raster images are compressed (PNG/WebP) and sized appropriately
- [ ] Accessibility is handled (`alt`, `aria-label`, no color-only meaning)
- [ ] `meta/brand.manifest.json` updated
- [ ] License/source recorded in `meta/SOURCES.md` (and/or `LICENSES.md`)
- [ ] Visual smoke test in both themes + over map tiles

---

## 🧪 QA tips (fast wins)

- **Logos/icons:** Check at 16px, 20px, 24px, 32px
- **Maps:** Check readability over satellite + light vector basemap
- **Token changes:** Run a UI snapshot pass (header, sidebar, Focus Mode, map legend)

---

## 📚 References inside the KFM ecosystem

These are the “why” behind the “how” above (governance, contract boundaries, and map-forward UI design):
- 📘 KFM Master Guide (pipeline boundaries, contract-first, evidence-first)
- 🧭 KFM technical blueprints (UI theming, provenance, governance)
- 🗺️ Mapping / cartography references (legend strategy, multi-scale readability)
- 🌐 Web design references (typography hierarchy, backgrounds, usability)

---

## 🧷 TL;DR

- **This folder is the brand truth.**  
- **Tokens over hex.**  
- **Dual-encode meaning (color + pattern).**  
- **No unclear licensing.**  
- **Accessibility is part of the brand.** ✅
