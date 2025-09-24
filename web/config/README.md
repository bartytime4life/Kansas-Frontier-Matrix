# `web/config/` — Kansas-Frontier-Matrix Viewer Configuration

This directory contains **JSON configuration files** used by the **Kansas-Frontier-Matrix** web viewer (`web/app.js`).  
They define how the MapLibre map, sidebar, and timeline should behave, and what data layers are loaded.

---

## 📂 Files

### [`viewer.json`](./viewer.json)
Primary configuration file for the web app.

- Defines **title, subtitle, center, zoom**, and **layer list**.
- Layers can be of type:
  - `raster` → tiled raster sources (e.g., OSM, DEMs, hillshade)
  - `image` → single image overlays with explicit `coordinates`
  - `geojson` → vector features from GeoJSON files
  - `vector` → vector tile sources
- Each layer supports:
  - `id` (unique string)
  - `title` (display name)
  - `url` / `tiles` (source location)
  - `start` / `end` (time bounds for filtering)
  - `opacity`, `visible`, `category`, `attribution`
  - optional `paint` blocks for per-type styling

### [`layers.json`](./layers.json)
Alternate layers-only config.  
If `viewer.json` or `app.config.json` are not found, `app.js` falls back to this file.  
Use this for **quick testing** when you only want to declare layer definitions.

### [`time_config.json`](./time_config.json)
Optional **timeline configuration overrides**.

- `time.min` / `time.max` — global slider range
- `time.step` — granularity of the slider (years)
- `time.defaultYear` — initial position of the slider
- `time.loop` — whether autoplay wraps around
- `time.fps` — autoplay frames per second
- `presets[]` — named ranges (e.g., “Dust Bowl 1930–1940”)

If present, these settings are merged into `viewer.json`.

### [`app.config.json`](./app.config.json)
Optional **top-level config**.  
If present, this is loaded first and can combine **viewer + time + defaults** in one file.

---

## 🔄 Load Priority

When the app starts (`web/app.js`), configs are loaded in this order:

1. `./config/app.config.json`
2. `./config/viewer.json`
3. `./config/layers.json`
4. `./layers.json` (legacy root)

If [`time_config.json`](./time_config.json) exists, its values override the `time` block in whichever base config is loaded.

---

## 🧩 Example Layer Entry

```json
{
  "id": "usgs_topo_1894",
  "title": "USGS Topographic (Larned, 1894)",
  "type": "image",
  "url": "./data/overlays/usgs_topo_larned_1894.tif",
  "coordinates": [
    [-100.1, 38.6],
    [-98.8, 38.6],
    [-98.8, 37.9],
    [-100.1, 37.9]
  ],
  "start": 1894,
  "end": 1894,
  "opacity": 0.7,
  "category": "Historic Maps",
  "attribution": "USGS Historical Topo Map Collection"
}

