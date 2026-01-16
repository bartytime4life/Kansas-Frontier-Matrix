# 🗺️ Basemap Styles (MapLibre)  
![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-2ea44f) ![Cesium](https://img.shields.io/badge/CesiumJS-3D-4c7bd9) ![Vector%20Tiles](https://img.shields.io/badge/Vector%20Tiles-MVT-6f42c1) ![Provenance](https://img.shields.io/badge/Provenance-First-ff7a18)

Basemaps are the **context layer** for the KFM web map experience. This folder contains **MapLibre style JSON** (and optional supporting assets) used as the **base layer** under KFM’s thematic & historical overlays. 🧭

> [!NOTE]
> A basemap should be “quiet” 🎛️ — it should help users orient themselves (roads, rivers, labels) *without competing* with KFM overlays (historic layers, analytics, stories).

---

## 🧭 Quick Links
- [📦 What lives here](#-what-lives-here)
- [🧩 Basemap vs overlays](#-basemap-vs-overlays)
- [🎨 Cartographic rules of thumb](#-cartographic-rules-of-thumb)
- [🧾 Provenance & attribution](#-provenance--attribution)
- [🧱 Basemap pack format](#-basemap-pack-format)
- [🔌 How the app uses basemaps](#-how-the-app-uses-basemaps)
- [⚡ Performance notes](#-performance-notes)
- [✅ QA checklist](#-qa-checklist)
- [🤝 Add a new basemap](#-add-a-new-basemap)

---

## 📦 What lives here

### ✅ Expected contents
- **MapLibre style JSON** (Mapbox Style Spec v8 compatible)
  - e.g. `*.json`, `*.style.json`, or `<basemap-id>/style.json` (pick one convention and stick to it)
- Optional “basemap pack” folders containing:
  - `meta.json` (provenance + licensing + display name)
  - `preview.png` (small screenshot for a basemap picker UI)
  - sprites/fonts references (usually shared elsewhere, but per-basemap is allowed)

### 🗂️ Suggested folder layout
```text
web/assets/maps/styles/
└─ basemaps/ 🗺️
   ├─ README.md
   ├─ <basemap-id>/               # ✅ recommended (keeps things tidy)
   │  ├─ style.json               # MapLibre style
   │  ├─ meta.json                # provenance + attribution + license
   │  └─ preview.png              # optional: used by basemap picker
   └─ <basemap-id-2>/
      ├─ style.json
      ├─ meta.json
      └─ preview.png
```

> [!TIP]
> Keeping each basemap in its own folder makes it easy to ship a “basemap as a unit” 📦 (style + metadata + preview).

---

## 🧩 Basemap vs overlays

| Layer type | Purpose | Examples | “Visual volume” 🔊 |
|---|---|---|---|
| **Basemap** | Orientation & place context | roads, water, labels, terrain tint | Low (quiet) |
| **Overlay** | KFM storytelling & analysis | historic boundaries, sensor layers, events, models | High (loud) |

✅ If a layer needs a legend, timeline behavior, or provenance popover… it probably belongs in **overlays**, not basemaps.

---

## 🎨 Cartographic rules of thumb

Basemaps should help overlays *win* visually:

- **Muted background** 🌫️  
  Avoid high-saturation fills and thick strokes.
- **Reserve strong color for meaning** 🎯  
  Strong color belongs to overlays / alerts / selections, not the base.
- **Label discipline** 🔤  
  Labels must be legible but not dense/noisy at small scales.
- **Consistent hierarchy** 🧱  
  Roads > hydro > boundaries > landuse (generally), but adapt to Kansas/KFM needs.

> [!NOTE]
> If users “see the basemap first,” the basemap is too loud.

---

## 🧾 Provenance & attribution

KFM is provenance-first 🧾✨ — basemaps are **not exempt**.

### ✅ Requirements
Every basemap MUST ship with:
- **Attribution HTML** (what must be shown in the UI)
- **License + usage constraints**
- **Provider/source reference**
- **Tile endpoint info** (or how it is resolved)

> [!WARNING]
> Don’t commit API keys into `style.json`.  
> If a provider requires keys, route it through configuration (env vars, server-side proxy, runtime config JSON, etc.).

---

## 🧱 Basemap pack format

A “basemap pack” is a folder containing `style.json` + `meta.json`.

### 📄 `meta.json` (recommended fields)
Use simple fields that the UI can show directly:

```json
{
  "id": "kfm-light",
  "name": "KFM Light",
  "type": "vector",
  "provider": "…",
  "license": "…",
  "attributionHtml": "…",
  "tileEndpoint": "…",
  "notes": "What this basemap is good for (and what it isn’t)."
}
```

### 🧩 `style.json` (minimum expectations)
At minimum:
- `version`
- `sources`
- `layers`
- `glyphs` / `sprite` **if** the style uses labels/icons

<details>
<summary><strong>Example style skeleton (click to expand)</strong> 🧱</summary>

```json
{
  "version": 8,
  "name": "KFM Light",
  "glyphs": "/assets/maps/fonts/{fontstack}/{range}.pbf",
  "sprite": "/assets/maps/sprites/kfm",
  "sources": {
    "basemap": {
      "type": "vector",
      "tiles": ["https://YOUR_TILE_ENDPOINT/{z}/{x}/{y}.pbf"],
      "attribution": "…"
    }
  },
  "layers": [],
  "metadata": {
    "kfm:id": "kfm-light",
    "kfm:attributionHtml": "…",
    "kfm:license": "…"
  }
}
```
</details>

---

## 🔌 How the app uses basemaps

Typical behavior:
1. The 2D viewer loads **one** basemap style at a time 🗺️
2. KFM then layers **overlays** on top (vector tiles, GeoJSON, rasters, etc.) 🧩
3. If the UI switches to **3D mode**, Cesium may handle imagery/terrain separately 🌍

> [!TIP]
> Keep basemap styles “clean” (no KFM overlays baked in). Overlays should be added via application logic so they can be toggled, time-filtered, cited, and audited.

---

## ⚡ Performance notes

- Prefer **vector tiles** for rich basemaps (fast zoom/pan, styling flexibility). 🧠  
- Keep layer counts reasonable; huge style graphs can slow down mid-tier devices. 📉  
- Sprites: avoid massive sprite sheets; split if needed. 🧩  
- If self-hosting tiles, use CDN caching where possible. 🚀

---

## ✅ QA checklist

Before merging any basemap changes:

- [ ] `style.json` loads in the app (no console errors)
- [ ] Attribution is visible and correct (and legally compliant)
- [ ] Basemap is readable in **light/dark** UI contexts (if applicable)
- [ ] Overlays still pop (basemap isn’t competing)
- [ ] Label density feels right at multiple zoom levels
- [ ] Network requests are sane (no spammy tile retries)

---

## 🤝 Add a new basemap

1. Create a new folder: `basemaps/<basemap-id>/` 📁  
2. Add:
   - `style.json`
   - `meta.json`
   - (optional) `preview.png`
3. Register the basemap in the **basemap picker/registry** wherever the UI lists options 🧭  
4. Run the [QA checklist](#-qa-checklist) ✅  
5. Ensure provenance/attribution data can be surfaced in the UI 🧾

---

### 🧷 Nearby folders (FYI)
- `web/viewers/` 🧭 — map viewer logic (2D/3D)
- `web/assets/maps/styles/overlays/` 🧩 — overlay styles (if present)
- `web/assets/maps/sprites/` 🎛️ — shared sprites (if present)
- `web/assets/maps/fonts/` 🔤 — glyph PBFs (if present)