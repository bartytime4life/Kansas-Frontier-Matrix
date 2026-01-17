# 🧩 KFM Map Sprite Icons

> **Source-of-truth icons** used to generate the **KFM map sprite** consumed by the web map (MapLibre GL JS) + surrounding UI.

📍 **You are here:** `web/assets/maps/sprites/kfm/src/icons/`

---

## 🎯 What this folder is for

KFM’s web UI includes a **layer catalog**, **legends**, **popups**, and other map-centric components — icons help users scan categories fast and keep multi-layer maps understandable. This directory is the canonical place to store **source icons** that get compiled into a **sprite sheet** for fast map rendering.

---

## 🗂️ Expected layout

We keep **editable source icons** here, and a build step generates sprite artifacts (often `sprite.json`, `sprite.png`, `sprite@2x.png`) somewhere under `web/assets/maps/sprites/kfm/`.

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 sprites/
        📁 kfm/
          📁 src/
            📁 icons/            ✅ (this folder)
              📄 README.md
              🖼️ *.svg / *.png   (source icons)
          📦 (generated sprite artifacts live nearby; do not hand-edit)
```

> ✅ Rule of thumb: **edit icons only in `src/icons/`** — treat generated sprites as build outputs.

---

## 🧭 Naming conventions

Keep names stable because styles reference them directly.

- ✅ **lower_case_with_underscores** (no spaces, no CamelCase)
- ✅ Prefer **semantic prefixes** to keep things searchable:
  - `ui_*` → buttons/tooling
  - `layer_*` → dataset/theme categories
  - `poi_*` → points-of-interest symbols
  - `story_*` → narrative / story node needs
- ✅ Be explicit: `layer_historical`, `poi_school`, `ui_search`, etc.
- ❌ Avoid renaming unless necessary (it breaks `icon-image` references)

---

## 🎨 Icon design guidelines (practical + map-friendly)

### Recommended source format
- **SVG preferred** ✅ (crisp at any scale)
- PNG only when we need **true multi-color raster art** or a specific pixel look.

### Visual consistency
- Use a **consistent stroke weight** across the set
- Keep shapes readable at small sizes (icons often render tiny on maps)
- Avoid ultra-thin details that disappear when scaled down

### “Tintable” icons (optional but useful)
If the map style tints icons dynamically, keep the artwork:
- single-color
- no gradients
- minimal opacity tricks

> If you’re unsure whether an icon must be tintable, default to **simple monochrome SVG** first.

---

## ➕ Adding a new icon

### 1) Create the icon (SVG preferred)
- Save as `lower_case_with_underscores.svg`
- Keep the design simple and legible

### 2) Optimize it 🧼
Use whatever the repo standard is (common options are SVGO / build-time optimizers).
- Goal: predictable output + smaller files

### 3) Track license + attribution 🧾
KFM is strict about transparency and reuse. If your icon comes from an external library (even if “free”):
- record the **source**
- record the **license**
- record any **required attribution**

> Suggested pattern: maintain an `ATTRIBUTION.md` or `icons.attribution.yml` in this folder.

### 4) Rebuild the sprite 🏗️
This repo should have a script to regenerate sprite assets.
- Search your root `package.json` for scripts containing: `sprite`, `sprites`, `icon`, or `assets`
- Run the relevant build command (examples you might see):
  - `npm run sprites:kfm`
  - `pnpm sprites:kfm`
  - `yarn sprites:kfm`

### 5) Sanity check ✅
- Verify the generated sprite artifacts changed as expected
- Load the app and confirm:
  - the icon appears in the **layer list / legend** (if applicable)
  - the icon renders on the map
  - no blurry output at typical zoom levels

---

## 🧪 Using an icon in a MapLibre style

Most map styles reference sprite icons by **name** (without file extension).

```json
{
  "id": "poi-school",
  "type": "symbol",
  "source": "pois",
  "layout": {
    "icon-image": "poi_school",
    "icon-size": 1,
    "icon-allow-overlap": true
  }
}
```

> Tip: If the icon doesn’t show up, it’s usually one of: name mismatch, sprite not rebuilt, or browser cache.

---

## 🧩 Definition of Done (DoD) checklist

- [ ] Icon filename follows `lower_case_with_underscores`
- [ ] Icon is readable at small sizes
- [ ] Icon matches stroke/weight style of existing set
- [ ] Sprite build completes cleanly
- [ ] Map renders icon correctly (no clipping, no blur)
- [ ] Attribution captured (if sourced externally)

---

## 🧯 Troubleshooting

### Icon is missing
- Confirm the **exact** `icon-image` name matches the sprite key
- Confirm the sprite build ran and outputs updated
- Hard refresh / clear cache (sprites are aggressively cached)

### Icon is blurry
- Ensure the sprite pipeline produces a high-DPI (`@2x`) variant
- Avoid raster-only icons unless necessary

### Icon is clipped
- Your SVG viewBox / bounds may be too tight
- Add padding inside the SVG canvas and re-export

---

## 📚 Useful icon sources (if we must import external symbols)

If we choose to pull from established cartography icon sets, keep licensing clean and track attribution.

```text
- Mapbox “Maki” icon set
- OpenStreetMap / OSM icon sets
- OSGeo map symbol references
- Open-SVG-Map-Icons / public-domain style collections
```

---

## 🤝 Contribution mindset

KFM icons are part of the project’s clarity + trust layer:
- they improve navigation through datasets and stories
- they must remain consistent, readable, and properly attributed

When in doubt: **opt for simple, legible, and well-documented.**
