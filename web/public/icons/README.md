# 🧩 Icons (`web/public/icons`)

![Static Assets](https://img.shields.io/badge/type-static%20assets-blue)
![Formats](https://img.shields.io/badge/formats-svg%20%7C%20png%20%7C%20ico-informational)
![Public](https://img.shields.io/badge/visibility-public-important)
![URL](https://img.shields.io/badge/served%20as-/icons%2F*-success)

This folder contains **publicly served** icon assets for the web app UI (controls, map markers/symbols, app/favicons, and other small interface glyphs). Because these files live under `public/`, they are directly accessible by URL at:

- `/<...>` → `/icons/<...>` ✅

> [!IMPORTANT]
> Anything placed here is **public** by default. Do **not** put secrets, private imagery, or restricted assets in this directory.

---

## 🧭 Table of contents

- [What belongs here](#-what-belongs-here)
- [Recommended folder layout](#-recommended-folder-layout)
- [Naming conventions](#-naming-conventions)
- [Format & design rules](#-format--design-rules)
  - [SVG rules](#svg-rules)
  - [PNG/ICO rules](#pngico-rules)
- [Provenance & licensing](#-provenance--licensing)
- [Optimization](#-optimization)
- [How to use icons](#-how-to-use-icons)
  - [In HTML](#in-html)
  - [In CSS](#in-css)
  - [In React](#in-react)
  - [In MapLibre](#in-maplibre)
  - [In Cesium](#in-cesium)
- [Add / update an icon](#-add--update-an-icon)
- [Troubleshooting](#-troubleshooting)

---

## 📦 What belongs here

Typical icon categories (use what exists in this repo; add categories only when needed):

- 🧭 **UI icons** (buttons, panels, navigation, toolbars)
- 🗺️ **Map symbols** (markers, pins, POI glyphs, legend symbols)
- 📱 **App icons** (PWA icons, apple-touch icons, favicons)
- 🧪 **Experimental** icons (only if clearly separated and labeled)

---

## 🗂️ Recommended folder layout

Your repo may already have a layout—**keep it consistent**. If you’re creating or normalizing structure, this is a strong baseline:

```text
web/public/icons/
├─ README.md
├─ ui/                      # general UI icons (SVG preferred)
│  ├─ zoom-in.svg
│  ├─ zoom-out.svg
│  └─ layers.svg
├─ map/                     # map markers / legend symbols (SVG/PNG as needed)
│  ├─ marker-default.svg
│  ├─ marker-default@2x.png
│  └─ legend/
│     └─ boundary-dashed.svg
├─ app/                     # PWA + platform icons (PNG/ICO)
│  ├─ favicon.ico
│  ├─ icon-192.png
│  ├─ icon-512.png
│  └─ apple-touch-icon.png
└─ third-party/             # ONLY if license + attribution are tracked
   └─ <library-name>/
      ├─ LICENSE.txt
      └─ <icons...>
```

> [!NOTE]
> If you add a new top-level folder under `icons/`, update this README with a 1–2 line description of what it stores ✅

---

## 🏷️ Naming conventions

Keep names predictable and “grep-able”:

- ✅ **kebab-case** filenames: `zoom-in.svg`, `marker-county-seat.svg`
- ✅ **no spaces**, no camelCase, no unicode in filenames
- ✅ **semantic names**, not visual descriptions  
  - Prefer: `layers.svg`, `print.svg`, `marker-trailhead.svg`  
  - Avoid: `blue-icon.svg`, `icon2.svg`, `final-final.svg`
- ✅ Optional **variants** via suffix:
  - `*-filled.svg`, `*-outline.svg`
  - `*@2x.png` for retina PNGs (only if truly needed)

**Don’t** encode size in the name for SVGs. SVGs scale naturally:
- ✅ `layers.svg`
- ❌ `layers-24px.svg`

---

## 🎨 Format & design rules

### SVG rules

SVG is the default for UI symbols and many map symbols because it scales cleanly.

**Requirements (✅):**
- Must include a `viewBox`
- Prefer **single-color** icons driven by `currentColor` when used in UI contexts
- Avoid embedded fonts (convert text to paths if unavoidable)
- Avoid filters/blur/shadows unless absolutely required (they bloat files and vary by renderer)
- Keep icons visually aligned to a **common grid** (typically 24×24 or 20×20)

**Recommended style (for UI):**
- Stroke-based icons with consistent stroke width (e.g., 1.5–2) and rounded caps/joins
- Minimal detail (icons should read at small sizes)

> [!TIP]
> If an icon needs multiple colors, prefer a dedicated PNG *only when necessary* (e.g., brand marks), and document the reason.

---

### PNG/ICO rules

PNG/ICO is primarily for **app/platform icons** and **pixel-perfect map sprites**.

**Use PNG/ICO when:**
- You need a favicon / browser icon
- A map engine requires raster images for sprites (or you’re generating a sprite sheet)
- You need exact pixel hinting (rare for modern UI)

**Recommended sizes (common baseline):**
- `icon-192.png` (PWA)
- `icon-512.png` (PWA)
- `apple-touch-icon.png` (commonly 180×180)
- `favicon.ico` (multi-size ICO)

---

## 🧾 Provenance & licensing

Icons are “small,” but licensing risk is “big.” Follow the same rigor as data assets:

- ✅ **Every non-trivial icon must be attributable** (source, author, license)
- ✅ Prefer **original** icons created for this project, or icons with **clear permissive licensing**
- ✅ If importing from a library, store it under `third-party/<library>/` and preserve license text

### Suggested metadata file (recommended)

Create (or keep) a lightweight manifest like:

- `web/public/icons/icons.manifest.json`

Example structure:

```json
[
  {
    "id": "ui.layers",
    "path": "ui/layers.svg",
    "source": "internal",
    "author": "KFM contributors",
    "license": "Project-License",
    "notes": "Single-color UI icon; uses currentColor."
  },
  {
    "id": "map.marker.default",
    "path": "map/marker-default.svg",
    "source": "third-party:<library>",
    "author": "<upstream author>",
    "license": "<upstream license>",
    "upstream": "<link or citation>",
    "notes": "Modified for KFM stroke width + simplified geometry."
  }
]
```

> [!IMPORTANT]
> If an icon has **no provenance**, it’s considered **not shippable** 🚫

---

## ⚙️ Optimization

Keep icons fast to load—especially in map-heavy UIs.

### SVG optimization (SVGO)

If your toolchain includes SVGO:

```bash
npx svgo -f web/public/icons -r
```

### PNG optimization

If you use `imagemin` or similar tooling, ensure outputs remain visually correct:

```bash
npx imagemin "web/public/icons/**/*.png" --out-dir="web/public/icons"
```

> [!NOTE]
> Always sanity-check map markers after optimization (some PNG optimizers can change gamma/metadata in surprising ways).

---

## 🧰 How to use icons

### In HTML

```html
<img src="/icons/ui/layers.svg" alt="Layers" width="24" height="24" />
```

### In CSS

Using SVG as a mask (great for theming via `currentColor`):

```css
.icon {
  width: 1em;
  height: 1em;
  mask: url("/icons/ui/layers.svg") no-repeat center / contain;
  background-color: currentColor;
}
```

### In React

Because these live in `public/`, you can reference them by absolute path:

```tsx
export function LayersButtonIcon() {
  return <img src="/icons/ui/layers.svg" alt="" aria-hidden="true" />;
}
```

Accessibility note:
- Use `alt=""` + `aria-hidden="true"` when the icon is purely decorative.
- If the icon conveys meaning, give it an accessible name (or label the button).

---

### In MapLibre

Two common patterns:

#### 1) Register a runtime image (often easiest)

> Some MapLibre/Mapbox GL setups prefer PNG for `addImage`. If SVG doesn’t render reliably in your pipeline, convert to PNG or use sprites.

```js
map.loadImage("/icons/map/marker-default@2x.png", (err, img) => {
  if (err) throw err;
  map.addImage("marker-default", img);

  map.addLayer({
    id: "poi",
    type: "symbol",
    source: "poi",
    layout: {
      "icon-image": "marker-default",
      "icon-size": 0.5,
      "icon-allow-overlap": true
    }
  });
});
```

#### 2) Sprite workflow (best for large sets)

If you have many map symbols, consider generating a sprite sheet (`sprite.png` + `sprite.json`) and referencing icons by name in the map style.

---

### In Cesium

Billboard markers (PNG commonly used):

```js
viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(lon, lat),
  billboard: {
    image: "/icons/map/marker-default@2x.png",
    width: 32,
    height: 32,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM
  }
});
```

---

## ➕ Add / update an icon

Quick checklist ✅

1. **Pick the right folder**
   - UI control? → `icons/ui/`
   - Map marker/symbol? → `icons/map/`
   - App/browser icon? → `icons/app/`
2. **Name it well** (kebab-case, semantic)
3. **Optimize it** (SVGO / PNG optimizer)
4. **Verify contrast + legibility** at small sizes (16–24px)
5. **Add provenance**
   - Update `icons.manifest.json` (recommended)
   - If third-party, store license text under `third-party/<lib>/`
6. **Test in context**
   - UI: check hover/focus states
   - Map: check overlap, scale, and zoom behavior

<details>
  <summary>✅ “Done” definition (click)</summary>

- Loads quickly (small file size)
- Looks correct on light/dark backgrounds (or is themeable)
- Has provenance + license recorded
- Doesn’t break layout when scaled
- Is accessible (decorative vs meaningful handled correctly)

</details>

---

## 🧯 Troubleshooting

- **Icon 404s**
  - Confirm path is `/icons/...` (not `/public/icons/...`)
- **Icon doesn’t update**
  - Hard refresh (browser cache) or bump asset hash if you’re caching aggressively
- **Map marker looks blurry**
  - Use `@2x` PNGs for raster markers and scale down via code
- **SVG color won’t change**
  - Ensure SVG uses `fill="currentColor"` / `stroke="currentColor"` and isn’t hard-coded

---

🧠 *Keep it consistent. Keep it documented. Keep it attributable.*