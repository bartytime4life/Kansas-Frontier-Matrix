# 🗺️ Legend Previews (KFM Web UI)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-2ea44f)
![Web](https://img.shields.io/badge/Web-React%20SPA-61dafb)
![Maps](https://img.shields.io/badge/Maps-MapLibre%20%2B%20Cesium-3b82f6)
![Assets](https://img.shields.io/badge/Asset%20Type-Legend%20Preview-orange)

Static **thumbnail previews** of map legends used by the **KFM front-end** to keep the map understandable at a glance (layer catalog cards, dataset side panels, story node previews, etc.). 🧭✨  
These previews should **match the active symbology** defined by the map styles (e.g., MapLibre style JSON legend items), while staying readable in small UI containers.

---

## 📁 Where you are

```text
web/
└── assets/
    └── maps/
        └── legends/
            └── previews/   👈 (this folder)
                └── README.md
```

---

## 🧠 What belongs here

✅ **Final, production-ready preview assets**, optimized for the web:
- `*.svg` (preferred) 🧩
- `*.png` (allowed when raster gradients/text rendering are required) 🖼️

🚫 Please *don’t* put here:
- source design files (`.psd`, `.ai`, `.fig`, etc.)
- huge exports / uncompressed assets
- one-off screenshots that don’t reflect the real legend

> Tip: If you need a place for editable sources, consider a sibling folder like `web/assets/maps/legends/sources/` or a top-level `design/` area (depending on repo conventions).

---

## 🎯 Why previews exist (UX intent)

KFM’s web UI emphasizes clarity while users:
- toggle layers in a **layer list / catalog** 🧱
- explore data with **search + timeline** ⏳🔎
- interpret **map symbology via legends** 🗝️

Preview images help users quickly recognize:
- **what the layer represents**
- **how it’s encoded** (colors / symbols / classes)
- **units & meaning** (when space allows)

---

## 🧷 File naming conventions

Legend previews should be **discoverable + deterministic** so UI code can find them reliably.

### ✅ Recommended pattern

Use a **stable layer/dataset identifier** as the filename base (prefer lowercase + underscores):

```text
<layer_or_dataset_id>__legend-preview.<ext>
```

Examples:
```text
kfm_ks_landcover_2000_2020_v1__legend-preview.svg
kfm_ks_historic_boundaries_1870_v2__legend-preview.png
kfm_ks_precip_anomaly_monthly_v1__legend-preview.svg
```

### 🔁 Mapping from IDs (common approach)

If your canonical IDs contain dots (e.g. `kfm.ks.landcover.2000_2020.v1`), normalize to filenames like:

- replace `.` with `_`
- keep everything lowercase
- avoid spaces

```text
kfm.ks.landcover.2000_2020.v1
→ kfm_ks_landcover_2000_2020_v1__legend-preview.svg
```

> Keep preview names stable over time; when symbology changes, update the file **contents** rather than inventing new names—unless a version bump is intentional.

---

## 🧩 Format rules (keep previews crisp)

### ⭐ Prefer SVG
SVG is ideal for:
- discrete class legends (swatches + labels)
- symbol keys (points/lines/polygons)
- icons + patterns

✅ Suggested SVG best practices:
- keep a **transparent background**
- use **embedded text** (not outlines) when possible
- run through an optimizer (e.g., `svgo`) to reduce file size
- avoid tiny font sizes (aim for readable at thumbnail scale)

### 🖼️ Use PNG when needed
PNG works best for:
- smooth raster gradients
- complex blended shading
- “mini-ramp” legends where SVG becomes heavy

✅ Suggested PNG best practices:
- export with transparency when possible
- export at **2×** size for high-DPI displays (while keeping file weight sane)
- avoid JPG (compression artifacts ruin fine legend text)

---

## 🎨 Cartography & accessibility checklist

These previews should follow the same map design principles as the live legend:

- ✅ **colorblind-friendly palettes** (avoid red/green traps)
- ✅ intuitive color semantics when applicable (blue=water, etc.)
- ✅ consistent symbol meaning across layers
- ✅ show **units** where relevant (%, mm, °C, people/km², etc.)
- ✅ don’t rely on color alone (use patterns/labels when possible)
- ✅ maintain strong contrast and legibility at small sizes

---

## 🔄 Update workflow

Update a legend preview when:
- symbology changes (colors, classes, symbols, line widths, opacity)
- classification/bins change (breakpoints, categories)
- units/labels change
- the default variable for a multi-variable layer changes

### Suggested steps
1. **Confirm live symbology** (MapLibre style / layer config) 🧾  
2. Export/update the preview asset (SVG preferred) 🎯  
3. Optimize:
   - SVG → `svgo`
   - PNG → compression (lossless)  
4. Verify readability at thumbnail size 🔍  
5. Commit with a clear message:
   - `Update legend preview for <layer_id> (new bins + units)`
   - `Fix contrast + accessibility for <layer_id> legend preview`

---

## 🧪 QA quick checks (before merging)

- [ ] Filename matches naming rules
- [ ] Preview matches current map symbology
- [ ] Readable when displayed small (try ~300px wide)
- [ ] Units and class labels are correct
- [ ] Color/contrast is accessible
- [ ] File size is reasonable (avoid multi‑MB assets)

---

## 🖼️ Preview gallery (optional, but helpful)

Add rows as previews are added so contributors can visually confirm everything quickly.

| Preview | Layer / Dataset | Notes |
|---|---|---|
| _(add thumbnail)_ | `kfm_ks_example_layer_v1` | default symbology |

Example snippet:
```md
| ![](./kfm_ks_landcover_2000_2020_v1__legend-preview.svg) | `kfm_ks_landcover_2000_2020_v1` | Default classes |
```

---

## 🔗 Related

- 📚 If there’s a parent legends README: `../README.md`
- 🧭 If the style sources live elsewhere: link the style folder here (e.g. MapLibre style JSON directory)
- 🧱 Layer catalog / dataset metadata: wherever the canonical layer IDs are defined

---

## 🧾 Attribution & licensing

If a legend preview is derived from an external standard, basemap style, or third-party symbology:
- preserve required attribution
- confirm license compatibility
- document the source in commit messages (or a manifest if you maintain one)

👣 The goal is the same as the broader KFM ethos: *the “map behind the map” should be understandable and trustworthy.*