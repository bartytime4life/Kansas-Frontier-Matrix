# 🖼️ Illustrations (Web UI)

![Assets](https://img.shields.io/badge/assets-illustrations-0b7285)
![Preferred](https://img.shields.io/badge/preferred-SVG-2f9e44)
![Policy](https://img.shields.io/badge/provenance-required-845ef7)

This folder contains **UI illustrations** used by the **KFM web client** (onboarding, empty states, gentle “how it works” visuals, and non-data decorative art).  
These assets are **not** authoritative data layers, map tiles, or GIS outputs—just interface visuals to improve clarity and usability. 🧭✨

---

## 📌 Folder intent

**Path:** `web/src/assets/images/illustrations/`

Use this folder for:
- ✅ onboarding / walkthrough visuals
- ✅ empty-states (no layers selected, no search results, etc.)
- ✅ friendly explanatory diagrams (high-level, *not* data claims)
- ✅ story-mode or timeline “chapter cover” art (if not a map output)
- ✅ placeholders for loading / “no content yet” panels

Avoid putting here:
- ❌ icons (tiny UI glyphs) → keep in an `icons/` folder (if/when present)
- ❌ photos / screenshots → store in a `photos/` or `screens/` folder (if/when present)
- ❌ generated map tiles / GIS renders → those belong with *data artifacts* (and must be source-traceable)
- ❌ anything that could be mistaken for **real** KFM evidence layers (e.g., “heatmaps” that look like data)

> [!IMPORTANT]
> KFM is an evidence-first platform. If an illustration visually implies a fact (boundaries, numbers, “this happened here”), it must either:
> 1) be generated from traceable data (and stored with data artifacts), **or**
> 2) be clearly presented as conceptual/illustrative (and **not** data).

---

## 🗂️ Recommended structure

```text
web/
  src/
    assets/
      images/
        illustrations/
          README.md
          (your .svg/.png/.jpg files live here)
          (optional) illustrations.manifest.yml
```

---

## 🧱 Format standards

### ✅ Preferred formats (in order)

| Format | Use for | Why | Notes |
|---|---|---|---|
| **SVG** | line art, diagrams, simple scenes, UI illustrations | crisp at any size, theme-friendly, small | optimize with SVGO; strip editor metadata |
| **PNG** | raster art needing transparency (alpha) | reliable transparency & sharp UI edges | keep sizes modest; avoid “raw export” bloat |
| **JPG/JPEG** | photos or complex raster scenes | great compression for photos | no transparency; avoid for UI line art |
| **WebP/AVIF** | heavy raster art, backgrounds | best compression | only if our build pipeline supports it consistently |

> [!TIP]
> If it can be drawn cleanly as vectors, **use SVG**. It scales better and usually ships smaller.

---

## 🧾 Naming conventions

Keep names predictable and searchable. Prefer **kebab-case**.

### Pattern
`<category>--<purpose>--<variant>[@2x].<ext>`

### Examples
- `empty--no-layers.svg`
- `empty--no-results.svg`
- `onboarding--step-01.svg`
- `onboarding--step-02.svg`
- `placeholder--map-panel.svg`
- `hero--kansas-frontier@2x.png`
- `illustration--focus-mode--dark.svg`

### Variants
- `--dark` / `--light` for theme-specific artwork
- `--hc` for high-contrast variant (if needed)
- `--es`, `--fr`, etc. for localized text baked into the image (**avoid** baked-in text when possible)

> [!NOTE]
> Avoid putting text inside illustrations. If you must, keep it minimal and consider localization impacts.

---

## 🎨 Theming rules (light/dark safe)

- Use **currentColor** and CSS variables in SVGs when possible
- Avoid “pure black” fills unless intentional (they can be harsh in dark mode)
- Ensure enough contrast against both light and dark backgrounds
- If an illustration relies heavily on background color, export **explicit variants**:
  - `...--light.svg`
  - `...--dark.svg`

---

## ♿ Accessibility rules

### Alt text
- **Informative illustration**: provide meaningful `alt`
- **Decorative only**: use empty alt (`alt=""`) and `aria-hidden="true"` if appropriate

> [!TIP]
> If a user needs the illustration to understand state (“No layers selected”), it’s **informative**, not decorative.

### Prefer semantic grouping
When an illustration is paired with a caption or explanation, use semantic structure:

- `<figure>` + `<figcaption>` (or your component equivalent)
- Keep text in actual UI labels, not baked into pixels

---

## ⚡ Performance budgets (practical defaults)

These are “keep us honest” targets (not hard law):

- **SVG**: aim for **< 150 KB**
- **PNG**: aim for **< 400 KB** (use `@2x` only when needed)
- **JPG/WebP**: aim for **< 500 KB** for UI usage

General rules:
- ✅ export at the *smallest* size that still looks good
- ✅ compress/optimize before committing
- ❌ don’t commit raw exports from design tools as-is

---

## 🧰 Optimization workflow

### SVG (recommended)
Checklist:
- remove hidden layers
- convert text to outlines (only if you must keep text inside SVG)
- simplify paths
- run SVGO

Example command (if `svgo` is available in the toolchain):
```bash
npx svgo -f web/src/assets/images/illustrations --multipass
```

### PNG/JPG
Checklist:
- export only the necessary resolution
- compress with a lossless/lossy optimizer (depending on use)
- validate quality at 100% and at typical UI size

---

## 🧬 Provenance & licensing (KFM-style “trust path”)

Every **non-trivial** illustration must be source-traceable:
- ✅ where it came from (designer, tool, link, or generated)
- ✅ license/rights (public domain, CC, purchased, internal)
- ✅ what was changed (colors, cropping, recomposition)
- ✅ which UI it supports (screen/component)

### ✅ Recommended: `illustrations.manifest.yml`
Create (or update) a manifest file alongside this README.

**Example entry:**
```yaml
- id: empty--no-layers
  file: empty--no-layers.svg
  title: "Empty state: no layers selected"
  purpose: "Shown when the map has no active layers"
  author: "KFM Team"
  source: "Internal"
  license: "Proprietary (KFM)"
  created: "2026-02-05"
  modified: []
  notes: "Decorative + informative; requires alt text"
```

> [!CAUTION]
> Do not add third‑party artwork unless we can **prove** we have rights to use it.  
> If in doubt, treat it as **not allowed** until confirmed.

### AI-generated illustrations
If you use generative tools:
- record **tool/model**, **prompt**, and **license terms**
- ensure it doesn’t include copyrighted logos/characters
- store that info in the manifest as `generated_with`, `prompt_summary`, etc.

---

## 🧩 Using illustrations in the web app (React-friendly)

### Import as an asset (common bundler behavior)
```tsx
import emptyNoLayers from "./empty--no-layers.svg";

export function EmptyStateNoLayers() {
  return (
    <figure>
      <img src={emptyNoLayers} alt="No map layers are selected." />
      <figcaption>Select a layer to begin exploring Kansas data.</figcaption>
    </figure>
  );
}
```

### Decorative usage
```tsx
<img src={someDecoration} alt="" aria-hidden="true" />
```

> [!TIP]
> If we use SVG-as-component tooling (SVGR, Vite plugins, etc.), prefer that approach for themeable SVGs.
> Keep the export consistent with the project’s current build setup.

---

## ✅ PR checklist

Before merging new/updated illustrations:

- [ ] Filename follows conventions (kebab-case + sensible suffixes)
- [ ] SVG/PNG/JPG is optimized (no raw export bloat)
- [ ] Works in light + dark theme (or has explicit variants)
- [ ] Has correct `alt` behavior (informative vs decorative)
- [ ] Doesn’t visually imply authoritative data (unless it is sourced data art)
- [ ] `illustrations.manifest.yml` updated (source + license + purpose)
- [ ] Used in at least one UI location (or is staged intentionally)

---

## 📚 References used for these conventions

These conventions align with:
- general web graphics best practices (vector vs bitmap, format choice, compression discipline)
- semantic HTML usage patterns for images/figures/captions
- KFM’s provenance-first “no source, no claim” philosophy

(See repo/project documentation and the design/dev references in the notes below.)
