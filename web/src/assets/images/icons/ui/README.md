# 🧩 UI Icons (KFM Web)

![assets](https://img.shields.io/badge/assets-ui%20icons-blue?style=flat)
![preferred](https://img.shields.io/badge/preferred-SVG-brightgreen?style=flat)
![theming](https://img.shields.io/badge/theme-currentColor-informational?style=flat)
![a11y](https://img.shields.io/badge/a11y-required-critical?style=flat)

Small, consistent, **theme-aware** UI icons used across the KFM React + TypeScript frontend (toolbars, buttons, panels, controls, status chips, etc.).  
This folder is intentionally **UI-only** — keep it clean, predictable, and easy to import. ✨

---

## 📍 Location

📂 `web/src/assets/images/icons/ui/`

---

## 🧭 What belongs here (and what does not)

✅ **Belongs here**
- Monochrome / single-color **UI control icons** (actions, navigation, status)
- Icons intended to inherit color from CSS (`currentColor`)
- SVGs designed to render cleanly at small sizes (16–24px)

🚫 **Does NOT belong here**
- Logos / brand marks (put those in a `logos/` or brand folder)
- Full illustrations, hero images, photography
- Complex map symbols that need multi-color styling (use a dedicated map-symbols folder)

> [!TIP]
> If you’re unsure: **UI icons = functional + small + minimal.**  
> Anything decorative or “art-y” probably belongs elsewhere.

---

## 🗂️ Suggested sibling layout (context)

```text
📦 web/
└─ 📂 src/
   └─ 📂 assets/
      └─ 📂 images/
         └─ 📂 icons/
            ├─ 📂 ui/        ✅ (you are here)
            ├─ 📂 map/       (optional, if the repo has map markers/symbols)
            └─ 📂 system/    (optional, if the repo has system-level assets)
```

---

## ✅ Icon standards (the contract)

### 1) Format

**Preferred:** `SVG`  
**Allowed (rare):** `PNG` (only if SVG is truly not viable)

### 2) Naming

**Rule:** `kebab-case.svg`  
**Avoid:** spaces, uppercase, vague names (`icon1.svg`, `thing.svg`), duplicates.

**Optional prefix pattern** (recommended for scale):
- `action-…` (create/delete/edit/share)
- `nav-…` (chevrons, arrows, hamburger)
- `status-…` (check, warning, error)
- `data-…` (layers, filters, search)
- `map-…` (if UI controls are map-related, but still UI)

Examples:
- `action-add.svg`
- `nav-chevron-left.svg`
- `status-warning.svg`
- `data-filter.svg`

### 3) Size + grid

- **Design on a 24×24 grid** (recommended)
- Keep geometry aligned to the pixel grid where possible
- Avoid ultra-thin details that vanish at 16px

### 4) Color + theming

**Use `currentColor`** so icons automatically match text color, themes, and states.

✅ Good:
- `stroke="currentColor"` and/or `fill="currentColor"`  
- Prefer strokes for outline icons; prefer fills for solid icons — but keep style consistent.

🚫 Avoid:
- Hard-coded colors like `fill="#000"` or `stroke="#123456"`  
- Inline styles that fight theming

### 5) SVG hygiene (recommended baseline)

Aim for SVGs like this:

```xml
<svg
  viewBox="0 0 24 24"
  xmlns="http://www.w3.org/2000/svg"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  aria-hidden="true"
  focusable="false"
>
  <path d="..." />
</svg>
```

> [!NOTE]
> Some icons may be **fill-based** instead of stroke-based. That’s fine — just keep them **consistent** within a given “family” and theme-aware.

---

## ♿ Accessibility rules (non-negotiable)

### Decorative icon (most common)
If the icon is purely decorative (icon inside a labeled button), hide it from screen readers:

- Icon: `aria-hidden="true"`
- Button/parent: has a readable label (`aria-label`, visible text, etc.)

### Meaningful icon
If an icon conveys meaning **by itself**, it must have an accessible name:
- Provide visible text **or**
- Provide `aria-label` / `title` strategy consistent with your icon rendering approach

> [!TIP]
> “Decorative by default” is usually the correct assumption for UI icons.

---

## ⚛️ Usage in React (common patterns)

Because bundlers differ (CRA / Vite / Webpack), this repo may support one or more import styles.

### Option A: Inline SVG component (preferred)
Pros: style with CSS, animate, control size easily, inherits `currentColor`.

```tsx
// Example (SVGR-style – your project may vary)
import { ReactComponent as SearchIcon } from "@/assets/images/icons/ui/data-search.svg";

export function SearchButton() {
  return (
    <button type="button" aria-label="Search">
      <SearchIcon aria-hidden="true" focusable="false" />
    </button>
  );
}
```

### Option B: URL import + <img> (fallback)
Pros: simplest if no SVGR pipeline exists.

```tsx
import searchUrl from "@/assets/images/icons/ui/data-search.svg";

export function SearchButton() {
  return (
    <button type="button" aria-label="Search">
      <img src={searchUrl} alt="" aria-hidden="true" />
    </button>
  );
}
```

### Option C: CSS background-image (use sparingly)
Use only when layout demands it (e.g., background decoration). Prefer inline SVG for UI controls.

---

## ➕ Adding a new icon (workflow)

1) **Name it well** ✅  
   Pick a clear, stable name (`action-export.svg`, not `export2.svg`).

2) **Export clean SVG** 🧼  
   From Figma/Illustrator/etc. Remove:
   - embedded rasters
   - editor metadata
   - unnecessary groups/transforms (when possible)

3) **Make it theme-friendly** 🎨  
   Replace hard-coded colors with `currentColor`.

4) **Optimize the SVG** ⚡  
   Use an optimizer (e.g., SVGO) or your project’s existing `npm` script if present.

5) **Sanity check at real sizes** 🔍  
   View at 16px and 24px (dark + light backgrounds).

6) **Provenance check** 🧾  
   If it’s from a third-party set, include attribution/license info (see below).

---

## 🧾 Provenance & licensing

Only commit icons we have the right to use.

If an icon comes from a third-party library:
- Add a note in a local provenance file (recommended): `SOURCES.md` (next to this README)
- Include the license text if required (recommended): `LICENSES/<source>.txt`
- Don’t mix incompatible licenses without tracking it

> [!IMPORTANT]
> “Found on the internet” is not a license. ✋

---

## ✅ PR checklist

- [ ] File is SVG (or justified exception)
- [ ] Name is `kebab-case` and descriptive
- [ ] Uses `currentColor` (no hard-coded colors)
- [ ] Has a clean `viewBox`
- [ ] Decorative icons are used with proper `aria-hidden`
- [ ] Optimized (no extra metadata / giant path bloat)
- [ ] License/provenance documented (if applicable)

---

## 🧠 FAQ

<details>
  <summary><strong>Why do we prefer SVG for UI icons?</strong></summary>

- Scales cleanly across DPIs (retina friendly)
- Usually smaller than multiple PNG sizes
- Easy to theme (`currentColor`)
- Easy to animate and style

</details>

<details>
  <summary><strong>When is PNG acceptable?</strong></summary>

Rarely. Use PNG only if:
- the asset is fundamentally raster (e.g., tiny texture, photoreal element)
- converting to SVG produces worse results or huge output

Even then: keep it small and optimized.

</details>
