# 🧩 UI Textures (web/src/assets/textures/ui)

![KFM](https://img.shields.io/badge/KFM-UI%20Textures-1f6feb?style=flat-square)
![Asset%20Type](https://img.shields.io/badge/Asset-Bitmap%20Textures-2ea043?style=flat-square)
![Formats](https://img.shields.io/badge/Formats-.png%20%7C%20.webp-8957e5?style=flat-square)
![HiDPI](https://img.shields.io/badge/HiDPI-%40x%20support-f97316?style=flat-square)

> 🎨 **Purpose:** This folder contains **bitmap textures** used by the **KFM React/Map UI** (MapLibre/Cesium UI chrome, panels, overlays, separators, noise/grain, sliders/knobs, etc.).  
> 🧭 **Goal:** Keep the UI crisp, performant, and consistent—while respecting KFM’s **governance + provenance-first** workflow (even for “just assets”). 🧾✨

---

## ✅ What belongs here

Use this folder for **repeatable or decorative bitmap textures** that help the UI feel tactile and readable:

- 🌫️ **Noise / grain overlays** (subtle texture for panels, modals, Focus Mode sidebar)
- 🧱 **Seamless patterns** (backgrounds, subtle fills)
- 🧩 **UI chrome textures** (borders, dividers, frames, bevels, masks)
- 🎚️ **Slider/timeline textures** (ticks, handles, scrubber grip textures)
- 🖱️ **Cursor/drag affordance bitmaps** (if not done via CSS/SVG)
- 🧷 **Small UI “chips”** that are texture-based (not icons)

---

## 🚫 What does NOT belong here

Keep this folder clean by pushing other assets to their rightful homes:

- 🧷 **SVG icons** (buttons, tool icons, map controls) → place in an `icons/` area (vector-first)
- 🗺️ **Map tiles / basemap art / raster datasets** → data + map pipelines (not UI textures)
- 🧑‍🎨 **Large illustrations / photos** → `images/` (not textures)
- 📦 **Third-party libraries’ assets** → vendor folder + license record

---

## 🗂️ Suggested organization

If you need structure beyond a flat folder, create subfolders *as the set grows*:

```text
web/src/assets/textures/ui/
├── README.md
├── noise/            # grain, film noise, subtle overlays
├── patterns/         # seamless repeating patterns
├── overlays/         # gradients, vignettes, scanlines (use carefully)
├── controls/         # sliders, knobs, timeline handles (texture-based)
├── frames/           # borders, panels, dividers, masks
└── atlases/          # optional: packed sprite/texture atlases + manifest
```

> 🧠 Tip: Prefer *fewer*, *reusable* textures over a lot of one-off bitmaps.

---

## 📛 Naming conventions

Consistency matters because these assets will be imported throughout the UI.

### Required rules
- ✅ **kebab-case**
- ✅ Include **role** and **size** when it matters
- ✅ Include **scale** if you export multiple densities

### Recommended filename patterns
- `noise-256.webp`
- `noise-512@2x.webp`
- `panel-grain-soft-512.webp`
- `divider-dash-2x8.png`
- `timeline-handle-grip-24@2x.png`
- `pattern-topo-subtle-512.webp`

### Scale suffixes
- `@1x`, `@2x` (and only `@3x` if absolutely necessary)
- If you only ship one, default to `@2x` quality and let the UI downscale.

---

## 🧪 Texture sizing & GPU friendliness

These are *UI textures*, but many may still be used in WebGL contexts (or heavily repeated in CSS).

- 🧊 **Prefer power-of-two** sizes for repeatable textures and anything likely to touch WebGL:
  - `128`, `256`, `512`, `1024`
- 🧷 For “pixel-snapped” UI bits (dividers, grips), use exact pixel sizes:
  - Example: `divider-2x8.png`
- 🪟 Avoid massive textures. If you need a “big background,” it should probably be:
  - a seamless pattern
  - a gradient in CSS
  - or generated procedurally

---

## 🖼️ Format guidelines

### Preferred
- ✅ **WebP (lossless)** for most textures (best size/quality balance)
- ✅ **PNG** when:
  - you need pixel-perfect edges and exact alpha behavior
  - a pipeline/tool can’t output WebP cleanly for that asset

### Avoid
- ❌ JPEG (no alpha, compression artifacts)
- ❌ Uncompressed TIFF/BMP/etc.

### Alpha edges (important!)
To prevent “halo” artifacts around transparency:
- keep edges clean
- export with proper alpha
- consider a 1–2px “alpha dilation” if the texture will be scaled/filtered

---

## 🌗 Theme readiness (light/dark)

KFM UI often needs to work in multiple lighting contexts (map backgrounds change too).

**Preferred approach**
- 🩶 Use **neutral grayscale + alpha** textures
- 🎛️ Tint via CSS / shader / canvas when possible

**If you must ship variants**
- Add `-dark` / `-light` suffixes:
  - `panel-grain-512-dark.webp`
  - `panel-grain-512-light.webp`

---

## 🧾 Provenance & licensing rules (non-negotiable)

Even UI assets can introduce licensing risk. KFM is provenance-first.

### ✅ If you create the texture yourself
- You’re good—no external provenance needed.
- Still keep it consistent with the naming + sizing rules.

### ✅ If you use or derive from a third-party texture
Add a **source record** (recommended: one per folder or per bundle):

Create/append one of:
- `SOURCES.md` (human readable ✅)
- `SOURCES.yml` / `SOURCES.json` (machine readable ✅)

**Suggested record template**
```md
- asset: noise/noise-512.webp
  source: "Author / Site Name"
  url: "https://example.com/original-texture-pack"
  license: "CC-BY 4.0"
  retrieved: "YYYY-MM-DD"
  changes: "Converted to lossless WebP, adjusted levels, made seamless"
```

> 🧠 Reminder: if we can’t verify the license, we can’t ship the texture.

---

## 🧩 Using textures in the React UI

### Import in TypeScript (bundler-friendly)
```ts
import panelGrain from "@/assets/textures/ui/noise/noise-512.webp";

// Example: apply as inline style
const style = {
  backgroundImage: `url(${panelGrain})`,
};
```

### CSS usage (with HiDPI)
```css
.kfm-panel {
  background-image: image-set(
    url("./noise/noise-256.webp") 1x,
    url("./noise/noise-512.webp") 2x
  );
  background-repeat: repeat;
  background-size: 256px 256px;
}
```

> ✅ If you rely on relative CSS paths, keep them stable and avoid deep cross-folder imports.

---

## 🗺️ When used in map UI components

Textures may be used to:
- improve readability of overlays on busy basemaps (subtle panel grain)
- emphasize controls (timeline grip)
- make Focus Mode UI feel “paper + archive” rather than sterile

**Rule of thumb:** textures should support comprehension—never distract.

---

## 🧯 Performance checklist

Before committing new textures:

- ✅ The file is **as small as possible** for its job  
- ✅ The texture is **seamless** if it repeats  
- ✅ The texture looks correct in:
  - light UI + dark map
  - dark UI + bright basemap
- ✅ No visible “alpha halos” at common scales  
- ✅ No redundant near-duplicates (reuse > remix)

---

## 🧰 Optional: atlas workflow (only if needed)

If the UI starts importing many small textures (e.g., grips, caps, tiny repeated elements), consider:
- packing them into an **atlas** to reduce requests + improve runtime efficiency
- storing:
  - `atlases/ui-atlas.webp`
  - `atlases/ui-atlas.json` (sprite rects, names, sizes)

> Only do this when there’s a measurable benefit—clarity first.

---

## 🧑‍💻 Contributing quick checklist

- [ ] File named correctly (kebab-case, meaningful)
- [ ] WebP/PNG chosen intentionally
- [ ] HiDPI considered (`@2x` or image-set)
- [ ] Source/license recorded if third-party
- [ ] No UI regressions (dark/light + map background variability)
- [ ] Asset is reusable (or justified as one-off)

---

### ✨ North Star

KFM is a **governed, evidence-first** system. UI textures are part of the experience—but they still must be:
- consistent ✅
- performant ✅
- license-safe ✅
- maintainable ✅

🧭 If you’re unsure where an asset belongs, document it and ask: “Will this help future contributors understand why it exists?”
