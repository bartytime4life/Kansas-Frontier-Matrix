# 🧩 Map Sprites Atlas (MapLibre Icons + Patterns)

![MapLibre GL JS](https://img.shields.io/badge/MapLibre-GL%20JS-blue)
![Style%20Spec](https://img.shields.io/badge/Style%20Spec-Sprite-lightgrey)
![HiDPI](https://img.shields.io/badge/HiDPI-@2x-success)

This folder contains the **sprite atlas** (🖼️ spritesheet + 🧾 index) used by the **2D map (MapLibre GL JS)** inside the KFM web UI.  
It powers **map symbols** (e.g., forts, trails, “sites of interest”) and optional **pattern fills/lines** (e.g., hatch fills) in a MapLibre style.

> ℹ️ **Note:** Sprites are a **MapLibre (2D)** concept. The **Cesium (3D)** viewer does not consume these sprite files.

---

## 🗂️ What lives here

A MapLibre/Mapbox-style sprite is always a **pair**:

- `*.png` → the packed atlas image (many icons in one file)
- `*.json` → the layout index mapping icon names → coordinates in the PNG

On high‑DPI devices, renderers look for **retina** variants:

- `*@2x.png`
- `*@2x.json`

### ✅ Typical structure (recommended convention)

> If your repo uses different filenames, keep the **same rules** (base name + `.png/.json` + optional `@2x`).

```text
web/src/assets/map/sprites/
├─ README.md
├─ kfm.png
├─ kfm.json
├─ kfm@2x.png
├─ kfm@2x.json
└─ src/                    # 👈 editable source icons (SVG)
   ├─ fort.svg
   ├─ trail.svg
   ├─ town.svg
   └─ …
```

---

## 🧠 How MapLibre loads sprites

In a style JSON, the root-level `sprite` property is a **base URL without an extension**.

Example:

```json
{
  "version": 8,
  "name": "KFM",
  "sprite": "/assets/map/sprites/kfm",
  "glyphs": "/assets/map/glyphs/{fontstack}/{range}.pbf",
  "sources": {},
  "layers": []
}
```

MapLibre will automatically request:

- `/assets/map/sprites/kfm.json`
- `/assets/map/sprites/kfm.png`
- and on retina devices:
  - `/assets/map/sprites/kfm@2x.json`
  - `/assets/map/sprites/kfm@2x.png`

---

## 🗺️ Using sprite icons in layers

Use the sprite icon name in `icon-image`:

```json
{
  "id": "sites-of-interest",
  "type": "symbol",
  "source": "some-source",
  "layout": {
    "icon-image": "fort",
    "icon-size": 1,
    "icon-allow-overlap": true
  }
}
```

✅ `icon-image` must match the **JSON key** in the sprite index (usually the SVG filename without `.svg`).

Sprites can also be referenced by patterns:

- `background-pattern`
- `fill-pattern`
- `line-pattern`
- `fill-extrusion-pattern`

---

## 🛠️ Updating / generating the sprite set

### Option A: `@mapbox/spritezero-cli` (recommended)

This is a well-known generator for Mapbox/MapLibre-compatible sprites.

1) Put/edit SVGs in `web/src/assets/map/sprites/src/`

2) Generate sprite outputs:

```bash
# from repo root (or wherever your package manager lives)
npm i -D @mapbox/spritezero-cli

# output base name: web/src/assets/map/sprites/kfm  (NO extension)
# input directory:  web/src/assets/map/sprites/src
npx spritezero --retina --unique \
  web/src/assets/map/sprites/kfm \
  web/src/assets/map/sprites/src
```

This produces:

- `kfm.png` + `kfm.json`
- `kfm@2x.png` + `kfm@2x.json`

### Option B: other generators

Any generator is fine **if** it produces MapLibre/Mapbox-compatible output pairs:

- `*.png` + `*.json`
- with matching icon names
- and correct `@2x` retina variants (if you need crisp icons on HiDPI)

---

## 🎨 Icon design rules (cartography + UI)

Keep icons readable at **12–18px** on a dense map:

- ✅ Prefer **simple silhouettes** (avoid tiny details)
- ✅ Use a consistent `viewBox` (common choice: `0 0 24 24`)
- ✅ Keep shapes inside the viewBox (no accidental clipping)
- ✅ Transparent background only
- ✅ Keep line weights consistent across the set
- ✅ One icon = one meaning (don’t reuse the same symbol for different concepts)

> 🧾 Licensing: only add icons you created, or icons with a compatible license. If you import third‑party SVGs, include attribution in the repo’s NOTICE/CREDITS.

---

## 🧪 Troubleshooting (fast checks)

### Icons aren’t showing
- Open DevTools → **Network**
- Confirm these requests return **200**:
  - `<sprite>.json` and `<sprite>.png`
  - `<sprite>@2x.json` and `<sprite>@2x.png` (on HiDPI)
- Ensure your style has a `sprite` property **without** `.png` / `.json`
- Confirm the style’s `icon-image` exactly matches the sprite JSON keys

### Icons are blurry
- Make sure the `@2x` assets exist and are reachable
- Avoid fractional scaling where possible; test at common zoom levels
- Ensure SVGs are aligned/clean (extra whitespace can cause odd rasterization)

### Icons are “wrong” after editing
- Clear cache / hard refresh
- Regenerate the sprite outputs (don’t hand-edit the generated PNG/JSON)

---

## 🔗 References (external)

- MapLibre style spec: Sprite → https://www.maplibre.org/maplibre-style-spec/sprite/
- Mapbox style spec: Sprite → https://docs.mapbox.com/style-spec/reference/sprite/
- `spritezero-cli` → https://github.com/mapbox/spritezero-cli
