# `web/config/` — Kansas-Frontier-Matrix Viewer Configuration

This folder contains JSON config files that drive the **MapLibre web viewer** (`web/app.js`).  
They define which layers are loaded, how the timeline behaves, and the defaults for the sidebar UI.

---

## 📂 Files

### `app.config.json` (preferred, auto-generated)
Top-level config used by `app.js`.  
Contains global defaults and a `layers[]` array.

- Generated automatically from STAC items with:
  ```sh
  kgt render-config --stac stac/items --output web/config/app.config.json --pretty

	•	Includes:
	•	version, generated (provenance)
	•	defaults (bounds, min/max zoom, opacity, time)
	•	layers[] (see schema below)

viewer.json (hand-edited, full config)

Human-friendly config for local dev.
Defines viewer title, map center/zoom, and layer list.
Loaded if app.config.json is missing.

layers.json (layers-only fallback)

Minimal layers-only file for quick testing.
Merged with defaults when no other config is found.

time_config.json (optional overrides)

Optional timeline config.
If present, overrides the time block in whichever base config is loaded.

Example:

{
  "time": {
    "min": 1800,
    "max": 2025,
    "step": 1,
    "defaultYear": 1875,
    "loop": true,
    "fps": 12
  },
  "presets": [
    { "label": "Bleeding Kansas", "start": 1854, "end": 1861 },
    { "label": "Dust Bowl", "start": 1930, "end": 1940 }
  ]
}


⸻

🔄 Load Priority

When the app starts, configs are loaded in this order:
	1.	./config/app.config.json
	2.	./config/viewer.json
	3.	./config/layers.json
	4.	./layers.json (legacy root)

If time_config.json exists, its values override the time block in whichever file is active.

⸻

🧩 Layer Schema

Each entry in layers[] should follow this pattern:

{
  "id": "unique_id",
  "title": "Display Title",
  "type": "raster | raster-dem | vector | geojson | image",
  "url": "path/to/source",
  "opacity": 0.8,
  "visible": false,
  "category": "reference | terrain | historical | documents | infrastructure",
  "attribution": "Data source name",
  "time": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }
}

Type notes
	•	raster → tiled raster or local COG/GeoTIFF
	•	raster-dem → elevation / hillshade
	•	vector → vector tiles (TileJSON/MBTiles)
	•	geojson → plain GeoJSON features
	•	image → single image overlay, requires coordinates array (NW, NE, SE, SW corners)

⸻

✅ Example

{
  "id": "usgs_topo_1894_larned",
  "title": "USGS Historic Topo — Larned (1894)",
  "type": "raster",
  "url": "../data/cogs/overlays/usgs_topo_larned_1894.tif",
  "opacity": 0.75,
  "visible": false,
  "category": "historical",
  "attribution": "USGS Historical Topo Map Collection",
  "time": { "start": "1894-01-01", "end": "1894-12-31" }
}


⸻

🛠️ Validation
	•	Run a JSON linter locally:

jq . web/config/app.config.json > /dev/null


	•	CI runs tests/test_web_configs.py to check structure and schema.

⸻

🔗 Tips
	•	Prefer COG for rasters and GeoJSON for small/medium vectors.
	•	Reproject rasters to EPSG:4326 for web alignment.
	•	Large vectors should be tiled or simplified.
	•	Always provide attribution and concise title for clean UI.
	•	Use time.start / time.end for slider filtering; use null if timeless.

⸻

TL;DR:
Keep app.config.json as the source of truth (auto-generated from STAC),
use viewer.json/layers.json only for dev or fallback,
and validate configs before committing.

