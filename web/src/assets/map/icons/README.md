# 🗺️ Map Icons

`path: web/src/assets/map/icons` · `preferred: SVG` · `targets: MapLibre + Cesium` · `policy: No Source, No Ship`

This folder contains **icon assets** used by the **Kansas Frontier Matrix (KFM)** web map experience — from **markers + pins** to **legend/layer symbols** and **map UI controls**.

> 🧠 Why this matters: icons are “micro-UX.” If they’re inconsistent, unlabeled, or unlicensed… the map feels unreliable.

---

## ✅ Quick rules (read this first)

- [ ] **SVG-first** (only use raster when SVG is a bad fit)
- [ ] **Family-prefixed filenames** so icons are easy to find (e.g., `marker-…`, `layer-…`, `ui-…`)
- [ ] **Kebab-case only** (no spaces, no caps)
- [ ] **Theme-friendly** SVGs: prefer `currentColor` for `fill`/`stroke`
- [ ] **No mystery icons**: every icon must have a **source + license** recorded (see “Provenance”)
- [ ] **Optimize** before commit (SVGO or equivalent)
- [ ] **No scripts / external refs** inside SVGs (security + portability)

---

## 📁 Recommended folder layout

If this folder is currently flat, that’s okay — but this is the target structure as the icon set grows:

```text
web/src/assets/map/icons/
├── 📄 README.md
├── 📄 icons.manifest.json              # (recommended) provenance + metadata index
├── 📁 markers/                         # point symbols used on the map
│   ├── marker-trailhead.svg
│   ├── marker-town.svg
│   └── marker-site.svg
├── 📁 layers/                          # legend icons for dataset/layer toggles
│   ├── layer-hydrology.svg
│   ├── layer-transport.svg
│   └── layer-boundaries.svg
├── 📁 ui/                              # buttons, controls, tool icons
│   ├── ui-layers.svg
│   ├── ui-legend.svg
│   └── ui-info.svg
└── 📁 status/                          # loading, warning, success, etc.
    ├── status-loading.svg
    ├── status-warning.svg
    └── status-ok.svg
```

---

## 🏷️ Naming convention

We use **“families”** (prefix groups) so you can locate icons instantly and keep the codebase readable.

### ✅ File naming pattern

```text
<family>-<meaning>(-<variant>)(-<size>).<ext>
```

### Families

| Prefix | What it’s for | Example filenames |
|---|---|---|
| `marker-` | Point markers placed on the map | `marker-trailhead.svg` |
| `layer-` | Legend / LayerControl symbols | `layer-historic-trails.svg` |
| `ui-` | UI icons (buttons/controls) | `ui-search.svg` |
| `status-` | Status indicators | `status-warning.svg` |

### Variants

Use **suffix tokens** when the icon meaning is the same but the state differs:

- `-active` / `-inactive`
- `-dark` / `-light` (rare; prefer `currentColor`)
- `-filled` / `-outline`

✅ Example: `ui-layers-active.svg`

---

## 🧩 Formats & when to use them

### ✅ Preferred: SVG
Use SVG for:
- crisp rendering at any zoom
- theming (via `currentColor`)
- smaller payload for simple shapes

### 🟨 Allowed: PNG / WebP (when SVG is not a good fit)
Use raster only for:
- highly detailed imagery
- textured / photo-like symbols
- icons that require pixel-perfect raster art

If you add raster icons, keep them **small** and consider **multiple densities** if the map renders them at fixed pixel sizes.

---

## 🎛️ SVG style guide (KFM-friendly)

### ViewBox + sizing
- Prefer `viewBox="0 0 24 24"` (or `16 16` if the set is intentionally small)
- Avoid hardcoding `width`/`height` unless needed — let the consumer size it

### Color + theming
- Prefer:
  - `fill="currentColor"` for solid icons
  - `stroke="currentColor"` for outline icons
- Avoid baked-in colors unless the icon is inherently semantic (rare)

### Clean geometry
- Keep strokes consistent (e.g., 1.5–2.0)
- Avoid tiny details that disappear at small sizes (12–16px)

### ❌ Forbidden inside SVGs
- `<script>` tags
- external references (remote images, fonts)
- `foreignObject`
- hidden metadata that bloats size

---

## 🧾 Provenance & licensing (No Source, No Ship)

Icons often come from:
- internal design work
- open icon sets
- purchased/stock sources
- vendor/partner assets

To keep KFM legally clean and provenance-first:

### ✅ Add/maintain `icons.manifest.json` (recommended)

Example schema:

```json
[
  {
    "file": "markers/marker-trailhead.svg",
    "title": "Trailhead marker",
    "family": "marker",
    "tags": ["trails", "recreation", "poi"],
    "source": "internal",
    "author": "KFM",
    "license": "Proprietary",
    "modified": "2026-02-05",
    "notes": "Designed for small-size legibility; currentColor compatible."
  }
]
```

### Third-party icon sets
If you bring in a third-party set (or a subset):
- record the **license name**
- record the **upstream source**
- keep any required **attribution text** close to the assets (or in a central `THIRD_PARTY_NOTICES` area)

---

## 🧑‍💻 Using icons in the app

Because KFM is a React + TypeScript web app with a map viewer, icons get used in a few different ways:

### 1) React UI icons (buttons/controls)

**If your build supports SVG-as-component (SVGR / CRA-style):**

```tsx
import { ReactComponent as LayersIcon } from "@/assets/map/icons/ui/ui-layers.svg";

export function LayersButton() {
  return (
    <button aria-label="Layers">
      <LayersIcon />
    </button>
  );
}
```

**If SVGs import as URLs in your build:**

```tsx
import layersIconUrl from "@/assets/map/icons/ui/ui-layers.svg";

export function LayersButton() {
  return (
    <button aria-label="Layers">
      <img src={layersIconUrl} alt="" />
    </button>
  );
}
```

✅ Accessibility note: if the icon is purely decorative, use `alt=""` and provide the label on the button.

---

### 2) MapLibre icons (markers, symbol layers)

A common pattern is:
1. import/get the icon URL
2. load it into the MapLibre runtime
3. `addImage(...)`
4. reference it by name in style layers (or marker rendering)

```ts
import trailheadIconUrl from "@/assets/map/icons/markers/marker-trailhead.svg";

function registerMapIcons(map: any) {
  map.loadImage(trailheadIconUrl, (err: unknown, image: any) => {
    if (err) throw err;

    // "marker-trailhead" is the key you will reference in your style layers
    map.addImage("marker-trailhead", image, { sdf: true });
  });
}
```

💡 Tip: if you use `sdf: true`, design the SVG to be **monochrome**, because SDF icons are typically tinted at render time.

---

### 3) Cesium icons (3D billboards)

Cesium commonly uses an image URL for billboards:

```ts
import siteIconUrl from "@/assets/map/icons/markers/marker-site.svg";

// Example usage (pseudo-code, depends on how Cesium is wired in this repo)
viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(lon, lat),
  billboard: {
    image: siteIconUrl,
    width: 24,
    height: 24,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM
  }
});
```

---

## ➕ Add a new icon (workflow)

1. **Pick the family** (`marker-`, `layer-`, `ui-`, `status-`)
2. Create/export as **SVG**
3. Ensure the SVG follows the style guide:
   - correct `viewBox`
   - uses `currentColor`
   - no embedded scripts/external refs
4. **Optimize** the SVG (SVGO or equivalent)
5. Place the file into the correct folder
6. Update `icons.manifest.json` (if present)
7. Use it in code + verify on:
   - light + dark backgrounds
   - small sizes (12–16px)
   - 2D (MapLibre) and/or 3D (Cesium) where applicable

---

## 🧯 Troubleshooting

<details>
  <summary><strong>Icon doesn’t show on the map</strong></summary>

- Confirm the icon was registered via `addImage(...)` before the layer references it  
- Confirm the layer uses the correct icon key (e.g., `"marker-trailhead"`)  
- Confirm the icon is in the final build output (path/import works)

</details>

<details>
  <summary><strong>Icon renders but looks “blurry”</strong></summary>

- Prefer SVG for markers wherever possible  
- If raster is required, consider multiple densities or correct pixel sizing  
- Avoid scaling tiny complex shapes down too far

</details>

<details>
  <summary><strong>Icon color won’t theme</strong></summary>

- Replace fixed fills/strokes (e.g., `#000`) with `currentColor`  
- Avoid inline styles that override your CSS/theming layer

</details>

---

## 🔐 Security note

SVGs are XML and can contain unexpected content. Keep icons safe by:
- stripping scripts and foreign objects
- avoiding external references
- using a trusted optimizer/sanitizer in the pipeline

---

## 🧪 PR checklist

- [ ] filename follows the naming convention
- [ ] icon is optimized
- [ ] icon is legible at small sizes
- [ ] icon source + license recorded (manifest or equivalent)
- [ ] map/UI integration verified (2D/3D as applicable)

---

## 🧭 Philosophy

KFM is a provenance-first system:  
**icons are part of the story** — so treat them like data: curated, traceable, and consistent. ✨
