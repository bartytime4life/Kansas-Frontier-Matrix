# Kansas-Frontier-Matrix — Web Developer Guide

This guide is for **contributors and maintainers** working on the `web/` viewer.  
It explains how configs, code, and UI connect, and how to extend or debug them.

---

## Config Loading

Order of preference:

1. `./app.config.json` (primary)  
2. `./config/app.config.json` (fallback)  
3. `./layers.json` (legacy)  

Configs define:
- Basemap/terrain rasters (`url`)
- GeoJSON overlays (`path`)
- Temporal windows (`time.start`, `time.end`)
- Legend info (`legend[]`)

---

## How `index.html` / `app.js` Works

1. **Load config** → fetch JSON, normalize `layers[]`.  
2. **Init MapLibre** → create map container with style + center/zoom.  
3. **Build UI** → sidebar sections (`timebox`, `layerbox`, `legendbox`).  
4. **Bind events** → slider input updates year, toggles change visibility, sliders adjust opacity.  
5. **Update map** → MapLibre layers/sources updated live.

---

## Adding a New Layer

1. Place raster tiles → `web/tiles/...`  
   or GeoJSON → `web/vectors/...`  
2. Add entry in `app.config.json`. Example:

```json
{
  "id": "railroads-1900",
  "title": "Railroads (c. 1900)",
  "group": "Vectors",
  "type": "geojson",
  "path": "./vectors/infrastructure/railroads_1900.geojson",
  "opacity": 1.0,
  "visible": true,
  "time": { "start": "1900-01-01", "end": "1900-12-31" },
  "paint": {
    "line": { "line-color": "#d97706", "line-width": 1.6, "line-opacity": 0.95 }
  }
}
