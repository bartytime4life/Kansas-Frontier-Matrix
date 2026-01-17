# 🧩 Map Legend Patterns (Textures) — `web/assets/maps/legends/patterns/`

![asset](https://img.shields.io/badge/assets-legend%20patterns-0b7285?style=flat)
![format](https://img.shields.io/badge/prefer-SVG%20%2B%20PNG-1f6feb?style=flat)
![goal](https://img.shields.io/badge/goal-readable%20%26%20accessible-2f9e44?style=flat)

Tileable textures used for **map legend swatches** (and optionally polygon fill patterns) in the KFM web app.

> [!NOTE]
> KFM’s web UI includes **legends for map symbology**, and the map viewers integrate **MapLibre GL JS (2D)** and **CesiumJS (3D)** — these pattern assets help keep symbology consistent across layers and views.

---

## ✨ What belongs in this folder?

✅ **Seamless / tileable** textures intended to repeat cleanly (no visible seams)  
✅ Patterns that remain identifiable at **legend-swatch size** (tiny!)  
✅ Assets that support **category differentiation** when color alone isn’t enough (accessibility, overlays, print, etc.)  
✅ Patterns that are **distinct from each other** (avoid “nearly the same hatch at a slightly different angle”)

🚫 Don’t add random textures with unknown origin/licensing  
🚫 Don’t add patterns so dense they turn into moiré / visual noise at small sizes  
🚫 Don’t add “one-off” patterns unless a layer truly needs it

---

## 🗂️ Suggested structure

```text
web/assets/maps/legends/patterns/
├─ 📄 README.md                        # 📘 What these patterns are for, naming rules, and how to reference them
├─ 🟫🧷 hatch-diagonal-45.svg            # 🟫 Vector hatch (45°) for a11y/print-friendly overlays (preferred source)
├─ 🟫🖼️ hatch-diagonal-45.png            # 🟫 Raster fallback for engines that can’t use SVG patterns
├─ 🟫🧷 dots-4.svg                       # 🟫 Vector dot pattern (density “4”) for uncertainty/restricted/secondary fills
├─ 🟫🖼️ dots-4.png                       # 🟫 Raster fallback (match SVG visually; use for fast runtime)
├─ 🟫🧷 crosshatch.svg                    # 🟫 Vector crosshatch for “do-not-use / masked / disputed” style signals
├─ 🟫🖼️ crosshatch.png                    # 🟫 Raster fallback (use when SVG patterns aren’t supported)
└─ 🧾 _meta/                             # 🧾 Provenance + licensing + tags + recommended usage per pattern
   ├─ 🧾 hatch-diagonal-45.meta.json      # 🧾 Source/tooling, license, intended meanings (e.g., uncertainty)
   ├─ 🧾 dots-4.meta.json                 # 🧾 Same: provenance + semantic tags + constraints
   └─ 🧾 crosshatch.meta.json             # 🧾 Same: provenance + semantic tags + constraints
```

> [!TIP]
> Pair **SVG** (crisp in UI, theme-friendly) with **PNG** (widely compatible for WebGL sprite/pattern pipelines).

---

## 🧷 Naming conventions

Keep names **kebab-case**, descriptive, and stable:

- `hatch-diagonal-45`
- `hatch-horizontal`
- `crosshatch`
- `dots-4`
- `dots-8`
- `waves-light`

### Optional prefixes (recommended)
Use a simple prefix to make scanning the folder easy:

- `hatch-*` → line hatching / stripes  
- `dots-*` → dots / stippling  
- `grid-*` → grid / lattice  
- `terrain-*` → specialized textures (use sparingly)

---

## 🧾 Provenance + metadata (KFM-style “no mystery assets”)

KFM’s architecture treats provenance as first-class. Patterns are part of what “shows up in the UI,” so they should be traceable too.

### ✅ Add a sidecar metadata file

Create: `web/assets/maps/legends/patterns/_meta/<pattern-id>.meta.json`

Example:

```json
{
  "id": "hatch-diagonal-45",
  "title": "Diagonal hatch (45°)",
  "category": "hatch",
  "tile_px": { "width": 32, "height": 32 },
  "intended_use": ["legend", "fill-pattern"],
  "visual_notes": {
    "recommended_swatches_px": [16, 24, 32],
    "density": "medium",
    "orientation_deg": 45
  },
  "source": {
    "origin": "in-house",
    "author": "KFM contributors",
    "license": "TBD",
    "url": null
  },
  "accessibility": {
    "works_on_light_bg": true,
    "works_on_dark_bg": true,
    "notes": "Avoid using as the only differentiator; pair with labels/colors."
  }
}
```

> [!TIP]
> If you don’t know the license/source, **don’t commit the asset** until it’s documented.

---

## 🎨 Design rules (cartography-first ✅)

### 1) Keep the pattern set small + legible
Too many distinct textures quickly become hard to decode in a legend. A tight set of patterns usually wins.

- If a layer is quantized/classified, prefer **a small number of classes** so the legend remains readable.
- If you need more categories, consider **labels**, **color**, or **interactive filtering** instead of adding 15 new patterns.

### 2) Make patterns meaningfully different
Use differences that are obvious at small size:

- orientation (↗ vs ↘)
- spacing (dense vs sparse)
- geometry (dots vs stripes vs grid)
- stroke weight (light vs bold)

### 3) Prioritize contrast + identifiability
Patterns must be distinguishable from adjacent map layers and basemaps. If it disappears against imagery, it’s not doing its job.

---

## 🧪 QA checklist before merging a new pattern

**Swatch tests**
- [ ] Still recognizable at **16×16** and **24×24** swatches  
- [ ] Seamless repetition (no “tile edge” visible)  
- [ ] Looks acceptable on **light** and **dark** backgrounds  

**Map tests**
- [ ] Doesn’t shimmer/moiré during zoom/tilt  
- [ ] Doesn’t overpower labels or boundary lines  
- [ ] Distinct from existing patterns in this folder  

**Provenance**
- [ ] Metadata sidecar exists (`_meta/*.meta.json`)  
- [ ] License/source documented  
- [ ] Pattern ID is stable (no renames without a deprecation plan)

---

## 🧰 Usage patterns

### ✅ Legend swatch (CSS background)

```css
.legend-swatch {
  width: 18px;
  height: 18px;
  border-radius: 4px;
  border: 1px solid rgba(0,0,0,0.2);
  background-image: url("/assets/maps/legends/patterns/hatch-diagonal-45.svg");
  background-repeat: repeat;
  background-size: 16px 16px;
}
```

### ✅ MapLibre GL JS fill-pattern (concept)

If you’re using fill patterns in the style layer, patterns typically need to exist as **images** that the renderer can reference.

```js
// Pseudocode: load and register a pattern image, then reference by ID in a layer style.
map.loadImage("/assets/maps/legends/patterns/hatch-diagonal-45.png", (err, img) => {
  if (err) throw err;
  if (!map.hasImage("hatch-diagonal-45")) map.addImage("hatch-diagonal-45", img);
});

// Then in a fill layer:
{
  "id": "some-layer",
  "type": "fill",
  "source": "kfm-source",
  "paint": {
    "fill-pattern": "hatch-diagonal-45",
    "fill-opacity": 0.6
  }
}
```

> [!NOTE]
> If your pipeline uses sprites/atlas generation instead, keep the **basename stable** (`hatch-diagonal-45`) so the sprite ID stays consistent across builds.

---

## 🤝 Contribution workflow

1. Add the pattern asset(s): `*.svg` and/or `*.png`
2. Add metadata: `_meta/<pattern-id>.meta.json`
3. Validate visually with the QA checklist
4. If applicable: update any legend registry/index file used by the UI

---

## 📚 Design references (project-aligned)

- **KFM Technical Documentation**: web UI includes legends; MapLibre GL JS + Cesium integration; provenance-first “no mystery layers” approach  
- **Making Maps: A Visual Guide to Map Design for GIS**: classification/legend readability; textures/orientation for qualitative categories  
- **Cartographic principles**: contrast, distinct symbols, and clear relationships between symbol and data

---
