# 🧩 Icons — Source Library (KFM Web)

![Scope](https://img.shields.io/badge/scope-web-blue)
![Type](https://img.shields.io/badge/type-static%20assets-5c6bc0)
![Format](https://img.shields.io/badge/format-SVG-orange)
![Policy](https://img.shields.io/badge/policy-no%20mystery%20assets-success)

Welcome to `web/assets/media/_sources/icons/` — the **canonical, editable source-of-truth** for icons used across the Kansas Frontier Matrix (KFM) web UI. 🎛️🗺️  
This folder is intentionally “source-y”: it’s where we keep clean, human-editable originals (typically SVG) **with traceability + licensing baked in**.

> 🧭 KFM is provenance-first. Icons are part of the UI’s “truth surface,” so they must be trackable just like data layers.

---

## 📌 What goes here vs. what doesn’t

✅ **Put here**
- `*.svg` source icons (UI controls, map controls, layer/category symbols, story affordances)
- Third-party icon packs **only if** they’re license-compatible and properly attributed
- Per-icon metadata (recommended) to prevent “mystery icons” (see below)

🚫 **Don’t put here**
- Random screenshots, raster exports, or “temporary” icons that won’t be attributed
- Auto-generated sprite sheets (those should live in a generated/build output folder)
- Brand assets that have restricted usage (unless we’ve explicitly documented permission)

---

## 🗂️ Suggested folder layout (scales well)

> If these folders don’t exist yet, create them as needed — the goal is predictable organization.

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 🧾 _sources/
         └─ 🧷 icons/
            ├─ 🎛️ ui/                # Buttons/menus/controls source SVGs (human-edited masters)
            ├─ 🗺️ map/               # Map markers, layer-type icons, legend symbols (source set)
            ├─ 📚 story/              # Narrative affordances + Focus Mode UI icon sources
            ├─ 🏷️ logos/             # KFM-only logo sources (avoid third-party marks; keep tightly governed)
            ├─ 📦 third_party/        # Imported icon packs (one folder per pack; preserve license files)
            ├─ 🧾 _meta/              # Shared metadata + attribution indexes for all icon sources
            └─ ✅📄 README.md          # You are here 📌 Conventions, licensing, and how sources become generated sprites
```

---

## 🎨 Design & SVG rules (the “house style”)

### 1) Prefer SVG (almost always)
- Scales cleanly across desktop/tablet/mobile without pixelation
- Keeps icons crisp for map UI, legends, and dense control panels

### 2) ViewBox is mandatory
Every icon **must** have a `viewBox` so it scales predictably:
- ✅ `viewBox="0 0 24 24"` (preferred for most UI icons)
- ✅ `viewBox="0 0 16 16"` (tight UI, small controls)
- ✅ Map markers can vary, but should be normalized and documented

### 3) Keep icons styleable
Best practice is to let CSS control color:
- Use `fill="currentColor"` and/or `stroke="currentColor"`
- Avoid hard-coded fills except for **brand marks** (and keep those isolated in `logos/`)

### 4) Keep geometry clean
- Avoid hidden layers, editor artifacts, and unnecessary `<g>` nesting
- No embedded rasters in SVG (e.g., `<image href="...png">`) unless explicitly justified

---

## ♿ Accessibility expectations

Icons often appear in controls. Don’t make the UI guess.

### If the icon is **decorative**
- Add `aria-hidden="true"` to the `<svg>` wrapper in the UI component
- Ensure there is a readable label elsewhere (button text, `aria-label`, tooltip)

### If the icon conveys **meaning**
- Provide accessible labeling in the UI component:
  - `aria-label="Search"` on the `<button>`
  - Or include a `<title>` inside the SVG when inlined

---

## ⚡ Performance & delivery patterns

You’ll typically see one of these approaches in web UIs:

### Pattern A — Inline SVG (max flexibility)
✅ Pros: easy to style + animate + manipulate  
⚠️ Cons: repeated markup can bloat pages if not componentized

```html
<button class="IconButton" aria-label="Layers">
  <svg viewBox="0 0 24 24" aria-hidden="true">
    <path d="..." fill="currentColor"></path>
  </svg>
</button>
```

### Pattern B — SVG Symbol Sprite (best caching + reuse)
✅ Pros: cached once, reused everywhere; keeps markup minimal  
⚠️ Cons: requires a build step or a static sprite file

```html
<svg class="Icon" aria-hidden="true">
  <use href="/assets/icons/sprite.svg#icon-layers"></use>
</svg>
```

> 🧪 If you’re supporting very old browsers, document any polyfills in the web app setup (and keep them optional).

---

## 🧾 Provenance & licensing (non-negotiable)

**Every icon must be traceable to:**
1) **Origin** (made in-house vs. imported)  
2) **License** (what we’re allowed to do)  
3) **Attribution requirements** (if any)  
4) **Modifications** (what we changed)

### Recommended: per-icon metadata sidecar
For each icon, add a matching metadata file:

```text
ui/
├─ search.svg
└─ search.icon.json
```

Example `search.icon.json`:

```json
{
  "id": "ui/search",
  "name": "Search",
  "tags": ["ui", "magnifier", "lookup"],
  "source_kind": "in_house",
  "source_url": null,
  "license": "Project-License",
  "author": "KFM",
  "modified": false,
  "notes": "Standard search icon for top nav + focus mode."
}
```

### Third-party icons
If you add a third-party pack, keep it isolated:

```text
third_party/
└─ maki/
   ├─ LICENSE
   ├─ README.source.md
   └─ *.svg
```

And ensure `_meta/ATTRIBUTION.md` (or equivalent) is updated.

---

## ➕ Adding a new icon (workflow)

1. **Pick the right home**
   - UI control? → `ui/`
   - Map symbol or legend? → `map/`
   - Story / Focus Mode UI? → `story/`

2. **Normalize**
   - Add/verify `viewBox`
   - Remove editor namespaces and junk
   - Convert fills/strokes to `currentColor` when appropriate

3. **Optimize**
   - Run SVGO (or equivalent) to reduce size without changing appearance  
   - Keep the optimized SVG readable if possible (don’t over-minify during early design)

4. **Add metadata**
   - Create `*.icon.json` and fill out provenance + licensing
   - If imported, include license text + attribution requirements

5. **Verify in UI**
   - Check alignment at typical icon sizes: 16 / 20 / 24
   - Validate contrast + meaning in both light/dark backgrounds (if applicable)

---

## ✅ Definition of Done (DoD) for icons

- [ ] SVG has a `viewBox`
- [ ] Uses `currentColor` where appropriate (not hard-coded fill/stroke)
- [ ] No embedded rasters (unless documented)
- [ ] Optimized (SVGO or equivalent)
- [ ] Provenance captured (`*.icon.json` or pack-level docs)
- [ ] License compatible + attribution requirements recorded
- [ ] Tested in the UI at common sizes

---

## 🔎 Quick glossary

- **_sources/** → editable originals, preserved for maintainability ✍️  
- **sprite** → a combined SVG file with many `<symbol>` definitions 🧺  
- **currentColor** → CSS-driven coloring for SVG paths 🎨  

---

## 🧭 Related (recommended) docs to add later

- `web/assets/README.md` (how the web app serves assets)
- `docs/design/iconography.md` (style rules, grid, stroke weights)
- `web/components/Icon/` (single source of truth component for icons)

---
