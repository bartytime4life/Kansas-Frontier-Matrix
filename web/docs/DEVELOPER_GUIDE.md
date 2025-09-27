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

- **Basemap/terrain rasters** (`url`)  
- **GeoJSON overlays** (`path`)  
- **Temporal windows** (`time.start`, `time.end`)  
- **Legend info** (`legend[]`)  
- **Groups** for sidebar sections (`groups[]`)

👉 See [`STYLE_GUIDE.md`](STYLE_GUIDE.md) §3 for the schema-lite.

---

## How `index.html` / `app.js` Works

1. **Load config** → fetch JSON, normalize `layers[]`.  
2. **Init MapLibre** → create map container with style + center/zoom.  
3. **Build UI** → sidebar sections (`timebox`, `layerbox`, `legendbox`).  
4. **Bind events** →  
   - Timeline slider input updates year  
   - Layer toggles show/hide overlays  
   - Opacity sliders adjust raster/GeoJSON alpha  
5. **Update map** → MapLibre sources/layers are updated live without reload.  

```mermaid
flowchart TD
  A["Config:\napp.config.json"] --> B["index.html / app.js"]
  B --> C["MapLibre:\nmap + sources"]
  C --> D["UI:\nsidebar + time slider"]
````

---

## Adding a New Layer

1. Place assets in repo:

   * Raster tiles → `web/tiles/...`
   * GeoJSON → `web/vectors/...`

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
```

3. (Optional) Add legend items:

```json
"legend": [
  { "type": "line", "label": "Rail line (c. 1900)", "color": "#d97706", "width": 1.6 }
]
```

4. Rebuild config (if using STAC → config generator) or refresh `index.html`.

---

## Debugging & Testing

### JSON validation

```sh
jq . web/app.config.json > /dev/null
```

### Serve locally

```sh
npx http-server web -p 8080
# → open http://localhost:8080/
```

### Common pitfalls

* ❌ `../` in paths → will 404 on GitHub Pages.
* ❌ Missing `id` or wrong `type` → UI skips the layer.
* ❌ Large (>10 MB) GeoJSON → slow render → convert to tiles.

---

## Extending the Viewer

* **New groups:** add to `groups[]` in config for sidebar sections.
* **Timeline behavior:** uses `time.start`/`time.end` (ISO); null = open-ended.
* **Paint styles:** support `line`, `fill`, `circle` (auto-split into separate MapLibre layers).
* **Plugins:** optional globals (`window.LegendControl`, `window.attachPopup`) extend UI.

---

## Contribution Notes

* Follow commit prefixes from [`STYLE_GUIDE.md`](STYLE_GUIDE.md) §7.
* Keep configs web-relative (`./vectors/...`, `./tiles/...`).
* Test across Chrome/Firefox/Safari; check dark mode and reduced-motion.

---

✅ This guide keeps developer workflows simple: **add → test → push** without breaking the viewer.

```
