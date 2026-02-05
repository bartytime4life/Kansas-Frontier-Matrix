# 📍 Map Marker Icons (Pins & Point Symbols)

![Path](https://img.shields.io/badge/path-web%2Fsrc%2Fassets%2Fmap%2Ficons%2Fmarkers-1f6feb)
![Assets](https://img.shields.io/badge/assets-marker%20icons-2ea44f)
![Format](https://img.shields.io/badge/prefer-SVG%20source%20%E2%86%92%20PNG%20runtime-6f42c1)
![Maps](https://img.shields.io/badge/maps-2D%20%2B%203D-ff8c00)

> One marker = one meaning. ✅  
> Keep point symbology consistent, lightweight, and correctly anchored across the KFM web map experience.

---

## 🧭 What lives here?

This folder is the **single source of truth** for **map marker icons** used by the web frontend:

- 📌 “Pin” style markers (bottom-tip anchored)
- 🔘 Point symbols / dots (center anchored)
- 🧩 Category markers (POI / story / event / alert / etc.)
- 🎯 State variants (default / hover / selected / disabled)

📂 Location: `web/src/assets/map/icons/markers/`

> [!IMPORTANT]
> If an icon is used on the map as a *point feature*, it belongs here.  
> If it’s a general UI icon (buttons, menus), it belongs in the general UI icon set — not here.

---

## ⚡ TL;DR Rules

- ✅ Keep **consistent sizing** and **visual weight**
- ✅ Use **kebab-case**
- ✅ Use `--state` suffixes for variants
- ✅ Prefer **SVG as editable source**, export **PNG** for runtime safety (WebGL + billboards)
- ✅ For dense data: **cluster / aggregate** instead of spamming pins 🌪️

---

## 🗂️ Folder contract

```text
📦 web/src/assets/map/icons/markers
├─ 📄 README.md
├─ 🧩 poi-pin--default.svg
├─ 🧩 poi-pin--selected.svg
├─ 🖼️ poi-pin--default.png
├─ 🖼️ poi-pin--default@2x.png
└─ ...
```

> The exact filenames will vary — the contract is the **pattern** + **consistency**.

---

## 🏷️ Naming conventions

### ✅ Pattern

**`<category>-<name>--<state>.<ext>`**

- `category` (optional but recommended): `poi`, `event`, `story`, `alert`, `user`, `resource`, etc.
- `name`: short and specific (`courthouse`, `battle-site`, `trailhead`)
- `state`: UI/interaction state (see below)
- `ext`: `svg` (source) and/or `png` (runtime)

### Examples

- `poi-courthouse--default.svg`
- `poi-courthouse--selected.svg`
- `poi-courthouse--default.png`
- `poi-courthouse--default@2x.png`

### ✅ Allowed states (recommended set)

- `--default`
- `--hover` (or `--focus`)
- `--selected`
- `--disabled` (or `--muted`)
- `--warning` / `--error` (only if it’s *semantic*, not decorative)

---

## 📐 Sizing & anchoring

### Default size targets

- 🎯 **24–32 px** on-screen is the standard “map pin” size.
- Bigger icons should be **rare** and **meaningful** (e.g., “you are here”, critical alert).

### Anchor rules

- 📌 **Pin/teardrop markers:** anchor = **bottom-center** (the tip)
- 🔘 **Dot markers:** anchor = **center**
- 🏁 **Flags/offset shapes:** document any intentional offset in the PR

> [!NOTE]
> If the anchor is wrong, the map lies. Even if the icon looks “fine.”

---

## 🎨 Design & accessibility guidelines

### Visual clarity (map-first)

- Keep detail low; markers must be readable at a glance.
- Avoid tiny text inside markers (it becomes noise).
- Prefer clear silhouettes + simple glyphs.

### Contrast & theming

- Ensure visibility on:
  - 🌞 light basemaps
  - 🌙 dark basemaps
  - 🗺️ imagery / satellite

### Don’t rely on color alone

Use **shape** or **glyph differences** to separate categories. Color is a *bonus*, not the only channel.

---

## 🧬 Recommended asset pipeline

```mermaid
flowchart LR
  Figma[Figma / Illustrator 🎨] --> SVG[SVG (editable source) 🧩]
  SVG --> Export[Export step 🔁]
  Export --> PNG1[PNG @1x 🖼️]
  Export --> PNG2[PNG @2x 🖼️]
  PNG1 --> Register[Register / Load in map 🧠]
  PNG2 --> Register
  Register --> MapLibre[MapLibre GL JS (2D) 🗺️]
  Register --> Cesium[CesiumJS (3D) 🌍]
```

---

## 🧩 Usage patterns

### 2D: MapLibre GL JS (symbol layers)

Best for **lots of points** (fast + GPU-friendly).

```ts
import maplibregl from "maplibre-gl";
import poiPinUrl from "@/assets/map/icons/markers/poi-pin--default.png"; // bundler resolves asset url

map.loadImage(poiPinUrl, (err, image) => {
  if (err || !image) throw err;

  if (!map.hasImage("poi-pin--default")) {
    map.addImage("poi-pin--default", image, {
      // If you're loading an @2x image, set pixelRatio: 2
      pixelRatio: 2,
      // If using SDF icons for runtime tinting, set sdf: true (and keep the icon monochrome)
      // sdf: true,
    });
  }
});

map.addLayer({
  id: "poi-layer",
  type: "symbol",
  source: "pois",
  layout: {
    "icon-image": "poi-pin--default",
    "icon-anchor": "bottom",
    "icon-allow-overlap": true,
    "icon-size": 1,
  },
});
```

### 2D: MapLibre GL JS (DOM markers)

Best for **small sets** or heavy interactivity (dragging, custom DOM, tooltips).

```ts
const el = document.createElement("div");
el.className = "kfm-marker";
el.style.width = "32px";
el.style.height = "32px";
el.style.backgroundImage = `url(${poiPinUrl})`;
el.style.backgroundSize = "contain";

new maplibregl.Marker({ element: el, anchor: "bottom" })
  .setLngLat([lng, lat])
  .addTo(map);
```

### 3D: CesiumJS (billboards)

```ts
import * as Cesium from "cesium";
import poiPinUrl from "@/assets/map/icons/markers/poi-pin--default.png";

viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(lng, lat),
  billboard: {
    image: poiPinUrl,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
    heightReference: Cesium.HeightReference.CLAMP_TO_GROUND,
    scale: 1,
  },
});
```

---

## 🧠 Density control: clustering & aggregation

> [!NOTE]
> If you can’t count the pins, the user can’t reason about them.

For dense point layers:

- ✅ cluster points (GeoJSON source clustering + circle/text layers)
- ✅ use heatmaps / density layers where appropriate
- ✅ show pins primarily for: **filtered**, **selected**, or **highlighted** sets

---

## ➕ Adding a new marker (checklist)

### 1) Create & export

- [ ] Create SVG source (clean paths, no external refs)
- [ ] Export PNG @1x and @2x (transparent background)
- [ ] Confirm anchor is correct (tip centered / dot centered)

### 2) Optimize

- [ ] SVGO for SVG
- [ ] pngquant (or equivalent) for PNG
- [ ] Keep file sizes lean (don’t ship 200KB pins)

### 3) Wire up

- [ ] Register in map loader / sprite / registry (wherever the app loads marker images)
- [ ] Verify in both 2D and 3D (if applicable)
- [ ] Screenshot before/after in PR

---

## 🧪 QA & troubleshooting

<details>
<summary><strong>Marker looks blurry</strong> 🫧</summary>

- You might be scaling up a low-res PNG.
- Export an `@2x` version and set `pixelRatio: 2` when registering the image.
</details>

<details>
<summary><strong>Marker is offset / “floating”</strong> 🎈</summary>

- Confirm anchor:
  - Pin: bottom-center
  - Dot: center
- Ensure the exported canvas matches the intended “tip” position.
</details>

<details>
<summary><strong>Marker doesn’t render</strong> 🫥</summary>

- Make sure the image is registered before the layer references it.
- Confirm the import resolves to a URL (check devtools Network).
</details>

---

## 🧾 Notes

- Keep markers **semantic**: symbols should communicate category/meaning, not decoration.
- Keep the set **cohesive**: same stroke style, same corner radius family, same visual weight.

✅ If it’s consistent, it’s learnable.  
✅ If it’s learnable, it’s fast.  
✅ If it’s fast, users trust it. 🎯
