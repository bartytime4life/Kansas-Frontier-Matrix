web/config/ — Kansas-Frontier-Matrix Viewer Configuration

This folder holds JSON config files that drive the MapLibre web viewer (web/app.js) — including map sources/layers, sidebar defaults, and the timeline model. It supports both auto-generated configs from STAC and hand-edited fallbacks, so you can iterate quickly and still keep things reproducible.  ￼ ￼

⸻

Files at a glance

app.config.json (preferred, auto-generated)

Single, top-level config used by app.js. When present, it’s loaded first and should contain:
	•	version, generated — provenance metadata
	•	defaults — global map/timeline defaults (bounds, min/max zoom, tileSize, visibility, opacity, time)
	•	layers[] — array of layer definitions (see Layer schema below)

Generate this from STAC with the CLI (recommended):
kgt render-config --stac stac/items --output web/config/app.config.json --pretty  ￼

viewer.json (hand-edited, “full” config)

Human-friendly config for local dev. Contains viewer UI defaults (title, center, zoom) and a layers[] list. If app.config.json is absent, app.js falls back to this. Keep it small; prefer STAC-generated app.config.json for the main site.  ￼

layers.json (layers-only fallback)

A minimalist, layers-only file for quick testing. app.js merges it with sensible defaults if viewer.json and app.config.json aren’t found.

time_config.json (optional overrides)

Overrides the timeline block of whichever base config is loaded. Useful for demos, presets, or autoplay tweaks:

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

Load order (in web/app.js)
	1.	./config/app.config.json
	2.	./config/viewer.json
	3.	./config/layers.json
	4.	./layers.json (legacy root fallback)

If time_config.json exists in ./config/, its time block overrides the effective config after the above is loaded/merged. This makes time controls adjustable without touching layer definitions.  ￼

⸻

Layer schema (expected by app.js)

Each entry in layers[] should follow this shape (MapLibre-compatible):

Common fields (all types)
	•	id (string, unique)
	•	title (string, shown in sidebar)
	•	type (one of: raster, raster-dem, vector, geojson, image)
	•	url (string; COG/GeoTIFF, raster/XYZ, GeoJSON, vector tiles, or single image path)
	•	opacity (0–1)
	•	visible (boolean)
	•	category (string; e.g., reference, terrain, historical, infrastructure, documents)
	•	attribution (string)
	•	time (object with ISO8601 start/end or null when timeless)

Type-specific notes
	•	raster: url may be an XYZ template or a local/served COG/GeoTIFF
	•	raster-dem: DEM source or rendered hillshade; typically hidden by default
	•	geojson: url should point to a .json/.geojson file; optional paint for styling
	•	vector: vector tiles; include url to a TileJSON or style source
	•	image: a single image with explicit coordinates (four corner lon/lat pairs in NW, NE, SE, SW order)

⸻

Example layers

Basemap raster

{
  "id": "basemap_osm",
  "title": "Basemap — OpenStreetMap",
  "type": "raster",
  "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
  "opacity": 1.0,
  "attribution": "© OpenStreetMap contributors",
  "category": "reference",
  "time": { "start": null, "end": null },
  "visible": true,
  "minzoom": 0,
  "maxzoom": 19,
  "tileSize": 256
}

Historic topo (COG overlay)

{
  "id": "usgs_topo_1894_larned",
  "title": "USGS Historic Topo — Larned (1894)",
  "type": "raster",
  "url": "../data/cogs/overlays/usgs_topo_larned_1894.tif",
  "opacity": 0.75,
  "attribution": "USGS Historical Topographic Map Collection",
  "category": "historical",
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "visible": false
}

Vector (GeoJSON)

{
  "id": "ks_railroads",
  "title": "Kansas Railroads (19th c.)",
  "type": "geojson",
  "url": "../data/vectors/ks_railroads.json",
  "opacity": 0.9,
  "attribution": "Kansas Historical GIS",
  "category": "infrastructure",
  "time": { "start": "1850-01-01", "end": "1950-12-31" },
  "visible": false,
  "paint": {
    "line-color": "#6b4e16",
    "line-width": 1.5
  }
}

Tip: Prefer COG for rasters and GeoJSON for small/medium vectors. For large vectors, consider tiling. The repo’s ETL already standardizes formats and derives app.config.json from STAC items.  ￼

⸻

Regeneration workflow (STAC → config)
	1.	Fetch/process sources via Make/ETL (producing COGs/GeoJSON)
	2.	Ensure STAC Collections/Items are created/updated under stac/
	3.	Render viewer config:

kgt render-config \
  --stac stac/items \
  --output web/config/app.config.json \
  --pretty


	4.	Validate configs before commit (see Validation & tests)

This keeps the viewer declarative and reproducible, matching the platform’s data/catalog design.  ￼ ￼

⸻

Validation & tests
	•	Keep a JSON Schema or structural checks in tests/test_web_configs.py to catch broken keys, missing id, or invalid type early in CI. For example, assert layers[] exists, item fields are present, and time.start/end are either null or ISO8601.  ￼
	•	Use a lightweight linter (jq) locally:

jq . web/config/app.config.json > /dev/null


	•	In CI, run both schema validation and a dry-load in a headless harness if available.  ￼

⸻

Styling & UI considerations
	•	opacity and visible map directly to sidebar controls; avoid per-layer bespoke flags that aren’t reflected in UI.
	•	For image overlays, supply four corner coordinates in map lon/lat order (NW, NE, SE, SW) so MapLibre can anchor correctly.
	•	Provide concise title and attribution for clean display in the sidebar and popups. GUI guidance favors clear, reusable UI components and tidy layouts.  ￼ ￼

⸻

Troubleshooting
	•	Layer not showing?
	•	Check type matches the actual source.
	•	Verify the url path (relative to web/ when served) and CORS if using remote tiles.
	•	Confirm time window contains the current slider value (or set time.start/end to null while testing).
	•	Raster looks misaligned?
	•	Ensure the COG/GeoTIFF is EPSG:4326 or the viewer’s source includes the proper projection metadata. The ETL recommends reprojecting historic rasters to WGS84 for web display.  ￼
	•	Big vectors perform poorly?
	•	Simplify, split per-county/year, or move to vector tiles. Reference the ETL guide for conversion patterns.  ￼

⸻

Provenance
	•	This config model aligns with the project’s STAC-driven map hub design and regeneration flow.  ￼ ￼
	•	UI/GUI patterns follow the project’s cross-platform GUI guidance (clear event-driven components, retained UI, responsive layout).  ￼

⸻

TL;DR: Prefer app.config.json → keep viewer.json/layers.json slim → drive everything from STAC → validate in CI → enjoy a stable, declarative viewer.
