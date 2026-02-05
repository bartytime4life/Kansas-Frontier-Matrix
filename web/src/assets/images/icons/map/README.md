# 🗺️ Map Icons (KFM)

![Domain](https://img.shields.io/badge/Domain-Maps-2ea44f)
![Assets](https://img.shields.io/badge/Assets-SVG%20%7C%20PNG-informational)
![Frontend](https://img.shields.io/badge/Web-React%20%2B%20TypeScript-blue)
![Mapping](https://img.shields.io/badge/Map-MapLibre%20%2F%20Cesium-orange)

📍 **Path:** `web/src/assets/images/icons/map/`  
🎯 **Purpose:** Map-specific icon assets used across the Maps UI (layer toggles, tools, markers, legends, and map-view affordances).

---

## ✨ What belongs in this folder?

These icons support the **Maps domain UI** — especially components like:

- 🧭 Map controls (zoom, home, compass, locate, reset view)
- 🧩 Layer/overlay UI (layer list, visibility, filter, legend)
- 🗂️ Dataset / category affordances (trails, hydrology, boundaries, etc.)
- 📌 Marker/POI assets (pins, waypoints, story nodes)
- 🫧 Clusters / density indicators (if not generated dynamically)
- ⏱️ Time + story map interactions (timeline play/pause, scrub, link-to-story)

> ✅ **Rule of thumb:** If an icon is *only* relevant to map UX or map symbology, it goes here.  
> If it’s global (settings, profile, generic close button), it belongs in the shared icon set instead.

---

## ✅ Quick rules (keep it clean + consistent)

- 🧩 **Prefer SVG** for UI icons (crisp at all sizes, easy theming).
- 🎨 **Use `currentColor`** in SVG whenever possible so icons inherit theme colors (including dark mode).
- 🧱 **Stick to a standard grid** (typically `24×24` for UI icons).
- 🧠 **Don’t rely on color alone** to convey meaning — use shape + labels/tooltips where needed.
- 🧼 **Optimize before commit** (strip editor metadata, compress paths).
- 📦 **Keep icons stylistically consistent** (stroke weight, corner radius, fill style).

---

## 🗂️ Suggested organization

If this folder starts getting busy, consider subfolders like:

```text
📦 web/src/assets/images/icons/map
├─ 📄 README.md                👈 you are here
├─ 🧭 controls/                (zoom, compass, home, locate…)
├─ 🧩 layers/                  (layer list, legend, visibility…)
├─ 📌 markers/                 (pins, POIs, story nodes…)
├─ 🫧 clusters/                (cluster badges, density icons…)
└─ 🧪 experimental/            (WIP icons — keep out of prod UI)
```

> 💡 If you add folders, keep naming stable and **don’t move icons casually** (imports break).

---

## 🏷️ Naming conventions

Use **kebab-case**, keep names descriptive, and avoid “generic” labels.

| Type | Pattern | Examples |
|---|---|---|
| UI control | `control-<action>.svg` | `control-locate.svg`, `control-compass.svg` |
| Layer UI | `layer-<concept>.svg` | `layer-traffic.svg`, `layer-boundaries.svg` |
| Marker/POI | `marker-<thing>.svg/png` | `marker-trailhead.svg`, `marker-water-well.png` |
| State variant | `-active` / `-disabled` (rare) | `control-locate-active.svg` |

✅ **Prefer CSS-based states** (hover/active/disabled) instead of duplicating files.  
⚠️ Only create variants if geometry meaningfully changes (not just color).

---

## 🎨 Style guide (Map-domain friendly)

### UI icons (buttons, toggles, panels)
- 📐 **Grid:** 24×24 (or 20×20 if tight)
- 🖊️ **Stroke:** consistent thickness (e.g., 1.5–2px)
- 🎛️ **Color:** `currentColor` (no hard-coded fills unless intentional)
- 🧽 **No embedded raster** inside SVG (keep it vector)

### Map symbols (MapLibre / “icon-image” style use)
- 🎯 Prefer **single-color silhouettes** (works well for tinting & SDF workflows)
- 📏 Export at **multiple pixel sizes** only when necessary (e.g., 1× and 2×)
- 🧾 Avoid tiny details that disappear when zoomed out

### Cluster visuals
- ✅ Prefer **dynamic clustering styles** (circles + counts) when possible
- If you must ship a static cluster icon:
  - 🔢 Ensure the number remains readable
  - 🫧 Keep strong contrast against basemap
  - 🧱 Consider multiple sizes (`cluster-sm`, `cluster-md`, `cluster-lg`)

---

## 🧩 Using icons in React (common patterns)

> Your build setup determines whether SVG imports become URLs or React components. Use the approach supported by the project config.

### Option A: Import as a URL (always works)
```tsx
import layersIconUrl from "@/assets/images/icons/map/layer-layers.svg";

export function LayersButton() {
  return (
    <button type="button" aria-label="Layers">
      <img src={layersIconUrl} alt="" width={20} height={20} />
    </button>
  );
}
```

### Option B: Import as a React component (if SVGR is enabled)
```tsx
import { ReactComponent as LayersIcon } from "@/assets/images/icons/map/layer-layers.svg";

export function LayersButton() {
  return (
    <button type="button" aria-label="Layers">
      <LayersIcon aria-hidden="true" focusable="false" />
    </button>
  );
}
```

✅ **Accessibility tip:**  
- If the icon is decorative, use `alt=""` (for `<img>`) or `aria-hidden="true"` (for SVG components).  
- If it communicates meaning, pair it with `aria-label`, visible text, or a tooltip.

---

## 🗺️ Using icons in MapLibre (symbols / images)

If a map layer needs an icon, the safest approach is usually to **load an image and register it**:

```ts
import markerUrl from "@/assets/images/icons/map/marker-trailhead.png";

map.loadImage(markerUrl, (error, image) => {
  if (error || !image) return;

  // "sdf: true" enables tinting via icon-color (best with monochrome icons)
  if (!map.hasImage("marker-trailhead")) {
    map.addImage("marker-trailhead", image, { sdf: true });
  }
});
```

Then reference it in your style/layer via the corresponding icon id.

---

## ➕ Adding a new icon (workflow)

1. 🎨 **Design/export** (SVG preferred)
   - Use a 24×24 grid (UI icons) unless you have a reason not to.
   - Convert text to paths if present (avoid font issues).
2. 🧼 **Optimize**
   - Remove hidden layers, editor metadata, unused defs.
   - Keep paths clean and minimal.
3. 🏷️ **Name correctly**
   - Kebab-case, descriptive, stable.
4. 🧪 **Test**
   - Light + dark theme
   - 100% / 125% / 150% zoom
   - On-map readability (if used as a marker/symbol)
5. 📌 **Document**
   - If sourced externally, record the **license + attribution** (see below).

---

## ⚖️ Licensing & attribution

🛑 **Do not add third‑party icons** unless their license is compatible with this repo.

If you import icons from external packs:
- ✅ Prefer **open + permissive** sources
- 🧾 Record source + license (recommended: `SOURCES.md` alongside this README or at `/docs/licenses/`)

> 💡 Tip: even permissive icon sets often require attribution — track it once, clearly, and forever.

---

## 🔍 PR checklist (icons)

- [ ] File name follows conventions
- [ ] SVG uses `currentColor` (or intentional fixed color)
- [ ] Icon looks correct in light/dark mode
- [ ] No style drift (stroke weight, corners, fill rules)
- [ ] Optimized size (no huge SVGs)
- [ ] License/attribution recorded (if external)

---

## 🧭 Related areas

- 📁 `web/src/components/` — Map UI components (MapViewer, LayerControl, Timeline, etc.)
- 🗺️ Map rendering: **MapLibre (2D)** and **Cesium (3D)** integrations
- 🎛️ Global theming: domain accent colors (Maps typically “green-ish”) + shared component styling

---
