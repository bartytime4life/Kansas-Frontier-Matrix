# `web/config/` — Kansas-Frontier-Matrix Viewer Configuration (2025-09)

This folder holds **declarative JSON** that drives the MapLibre viewer (`web/app.js`).
Configs define **what** to load (layers), **how** to render (legend/categories/style), and **when** to show it (time).

Design goal: **zero hand-tuning in code** — the viewer should be driven by STAC + these configs.

---

## What lives here (and why)

| File                     | Required? | Purpose                                                   | Edited by           | Source of truth        |
| ------------------------ | --------: | --------------------------------------------------------- | ------------------- | ---------------------- |
| `app.config.json`        |         ✅ | Final merged viewer config (defaults + layers + time)     | Generated from STAC | **Yes**                |
| `viewer.json`            |         ➖ | Full, hand-edited config for local/dev override           | Devs                | No (fallback only)     |
| `layers.json`            |         ➖ | Layers-only catalog for quick tests/dev                   | Devs                | No (fallback only)     |
| `time_config.json`       |         ➖ | Overrides active config’s `time` + presets                | Devs                | Merges over active     |
| `legend.json`            |         ➖ | Global symbology tokens; may bind to layer IDs            | Devs/Cartography    | Referenced by UI       |
| `categories.json`        |         ➖ | Sidebar grouping: labels + order (+ optional layer lists) | Devs/Cartography    | Referenced by UI       |
| `sources.json`           |         ➖ | (Optional) audit registry for layers → data sources       | Devs/Data           | Helpful for provenance |
| `story_layers.json`      |         ➖ | Curated “themes” (layersOn/off, opacity, flyTo)           | Editors/Outreach    | Used by story UI       |
| `schema.json`            |         ➖ | Pack of JSON Schemas (legend / categories / sources)      | Devs                | Used by CI/local       |
| `app.config.schema.json` |         ➖ | Schema for `app.config.json`                              | Devs                | Used by CI/local       |
| `layers.schema.json`     |         ➖ | Schema for `layers.json`                                  | Devs                | Used by CI/local       |

> **Rule of thumb**: Keep **`app.config.json` generated**. Use `viewer.json`/`layers.json` only for experiments.

---

## Load order (runtime)

`web/app.js` loads the first file found:

1. `./config/app.config.json`
2. `./config/viewer.json`
3. `./config/layers.json`
4. `./layers.json` *(legacy root)*

If `time_config.json` exists, its `time` block **overrides** the active config.
If `legend.json` / `categories.json` exist, the UI uses them for **legend chips** and **sidebar grouping**.

---

## Generate the viewer config from STAC

```bash
# 1) Build/refresh STAC items
make stac

# 2) Render viewer config
kgt render-config \
  --stac stac/items \
  --output web/config/app.config.json \
  --pretty
```

Re-run after adding/removing/changing any STAC items.

---

## Contract: top-level shape (authoritative)

### Top-level (`app.config.json` / `viewer.json`)

```jsonc
{
  "version": "1.3.0",
  "generated": "2025-09-26T18:00:00Z",
  "title": "Kansas-Frontier-Matrix",
  "subtitle": "Time-aware Kansas GIS",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "bounds": [-102.051, 36.993, -94.588, 40.003],

  "time": { "min": "1800-01-01", "max": "2025-12-31", "defaultYear": 1930, "step": 1, "loop": false, "fps": 12 },

  "defaults": {
    "minzoom": 0, "maxzoom": 15, "opacity": 1.0, "visible": true,
    "time": { "start": null, "end": null }
  },

  "layers": [ /* see layer schema below */ ]
}
```

### Layer schema (common keys)

```jsonc
{
  "id": "unique_id",
  "title": "Display Title",
  "type": "raster | raster-dem | vector | geojson | image",
  "url": "path/or/url/to/source",
  "visible": false,
  "opacity": 0.8,
  "minzoom": 0,
  "maxzoom": 19,
  "category": "reference | terrain | historical | documents | infrastructure | environment | culture",
  "attribution": "Source name / license",
  "time": { "start": "YYYY-MM-DD|null", "end": "YYYY-MM-DD|null" },

  // Optional app-level vector style (camelCase)
  "style": {
    "fillColor": "#A0C4FF",
    "fillOpacity": 0.6,
    "lineColor": "#3A86FF",
    "lineWidth": 1.0,
    "circleColor": "#FF595E",
    "circleRadius": 4,
    "lineDasharray": [2, 2]
  },

  // GeoJSON popups and per-feature time
  "popup": ["name", "type", "year", "year_end"],
  "timeProperty": "year",
  "endTimeProperty": "year_end",

  // Image overlay bounds (clockwise from NW)
  "coordinates": [[lonW,latN],[lonE,latN],[lonE,latS],[lonW,latS]]
}
```

**Type specifics**

* `raster` → tile servers **or** local COG/GeoTIFF
* `raster-dem` → elevation grids; viewer may enable terrain/hillshade
* `vector` → vector tiles (TileJSON)
* `geojson` → inline/URL GeoJSON (tile large datasets or simplify)
* `image` → single image overlay; must include `coordinates`

---

## Time overrides & presets (`time_config.json`)

```json
{
  "version": "1.1.0",
  "generated": "2025-09-26T18:00:00Z",
  "time": {
    "min": "1800-01-01",
    "max": "2025-12-31",
    "step": 1,
    "defaultYear": 1930,
    "loop": false,
    "fps": 12
  },
  "presets": [
    { "label": "Bleeding Kansas", "start": 1854, "end": 1861 },
    { "label": "Dust Bowl", "start": 1930, "end": 1940 }
  ]
}
```

> Dates can be `YYYY` or `YYYY-MM-DD`; the viewer normalizes them.
>
> Filtering uses **layer `time.start/end`** or **feature `timeProperty`/`endTimeProperty`**.

---

## Legend & categories

### `legend.json` (tokens + bindings)

```json
{
  "version": "1.1.0",
  "symbols": {
    "historic_topo": { "raster": true, "preview": "#c6b79e" },
    "dem": { "rasterDem": true, "preview": "#9e9e9e" },
    "hillshade": { "raster": true, "preview": "#7f7f7f" },
    "counties": { "lineColor": "#555", "lineWidth": 1, "fillOpacity": 0.0 },
    "treaties": { "fillColor": "rgba(200,60,60,0.35)", "lineColor": "#a33" },
    "railroads": { "lineColor": "#6b4e16", "lineWidth": 1.5 },
    "events": { "circleColor": "#CC3300", "circleRadius": 4 }
  },
  "layerBindings": {
    "usgs_topo_1894_larned": "historic_topo",
    "ks_dem_2018_2020": "dem",
    "ks_hillshade_2018": "hillshade",
    "kansas_counties": "counties",
    "ks_treaties": "treaties",
    "ks_railroads": "railroads",
    "events_sample": "events"
  }
}
```

### `categories.json` (sidebar)

```json
{
  "version": "1.1.0",
  "generated": "2025-09-26T18:00:00Z",
  "categories": {
    "reference":     { "label": "Reference", "order": 0 },
    "terrain":       { "label": "Terrain & Elevation", "order": 1 },
    "environment":   { "label": "Land & Water", "order": 2 },
    "historical":    { "label": "Historical Maps", "order": 3 },
    "documents":     { "label": "Documents & Treaties", "order": 4 },
    "infrastructure":{ "label": "Trails & Railroads", "order": 5 },
    "culture":       { "label": "Settlements & Sites", "order": 6 }
  }
}
```

---

## Examples

### Historical raster (COG)

```json
{
  "id": "usgs_topo_1894_larned",
  "title": "USGS Historic Topo — Larned (1894)",
  "type": "raster",
  "url": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "opacity": 0.75,
  "visible": false,
  "category": "historical",
  "attribution": "USGS Historical Topographic Map Collection",
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "minzoom": 0,
  "maxzoom": 19
}
```

### Time-aware GeoJSON points

```json
{
  "id": "events_sample",
  "title": "Sample Events",
  "type": "geojson",
  "url": "data/demo_events.json",
  "category": "historical",
  "time": { "start": "1800-01-01", "end": "1950-12-31" },
  "timeProperty": "date",
  "popup": ["title", "date", "summary", "url"],
  "style": { "circleColor": "#E63946", "circleRadius": 5, "circleOpacity": 0.9 },
  "visible": false,
  "attribution": "Demo dataset"
}
```

---

## Validation & CI

**Local quick checks**

```bash
# lint JSON
jq . web/config/app.config.json > /dev/null

# schema validation (app/layers)
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
ajv validate -s web/config/layers.schema.json -d web/config/layers.json

# schema pack (legend/categories/sources)
ajv validate -s web/config/schema.json -d web/config/legend.json    -r web/config/schema.json
ajv validate -s web/config/schema.json -d web/config/categories.json -r web/config/schema.json
ajv validate -s web/config/schema.json -d web/config/sources.json    -r web/config/schema.json
```

**CI guarantees**

* `tests/test_web_configs.py` validates structure, URLs, categories, time, and legend bindings.
* STAC → `app.config.json` generation is checked; broken STAC = failed build.

---

## Troubleshooting

* **Layer not visible** → Check `type`, `url`, `minzoom/maxzoom`, file availability. For GeoTIFFs, ensure they are **COGs**.
* **Timeline no-op** → Provide `time` block (layer) or `timeProperty` (feature); validate date formats.
* **Legend chip missing** → Add `legend.json` `layerBindings[layerId] = symbolId`, and ensure `symbols[symbolId]` exists.
* **Wrong sidebar group** → Verify `category` matches a key in `categories.json`.
* **Slow vectors** → Tile or simplify statewide/dense GeoJSON; prefer vector tiles for large datasets.

---

## Story themes (`story_layers.json`)

Curated toggles for demos/tours, e.g.:

```json
{
  "schema": "kfm-story/1.1",
  "version": "1.1.0",
  "title": "Curated Story Themes",
  "themes": [
    {
      "id": "bleeding_kansas",
      "title": "Bleeding Kansas & Treaties",
      "year": 1856,
      "layersOn": ["ks_treaties", "ks_railroads", "kansas_counties"],
      "opacity": { "ks_treaties": 0.9, "ks_railroads": 0.9, "kansas_counties": 0.5 },
      "flyTo": { "center": [-96.9, 39.1], "zoom": 6.5 }
    }
  ]
}
```

---

## Common workflows

**Generate fresh from STAC**

```bash
make stac
kgt render-config --stac stac/items --output web/config/app.config.json --pretty
```

**Add a time preset (no STAC regen)**

```bash
jq '.presets += [{ "label":"Santa Fe Trail", "start":1821, "end":1880 }]' \
  web/config/time_config.json > /tmp/time && mv /tmp/time web/config/time_config.json
```

**Audit a layer’s provenance (if `sources.json` present)**

```bash
jq '.sources["ks_railroads"]' web/config/sources.json
```

---

## Future-proofing & conventions

* **Rasters**: prefer **COG**; reproject to **EPSG:4326**.
* **Vectors**: **GeoJSON** only for small/medium; otherwise **tiles**.
* **IDs**: `snake_case`, stable across releases; include source + vintage (e.g., `usgs_topo_1894_larned`).
* **Categories**: keep in sync with `categories.json`; pick exactly one per layer.
* **Legend**: keep `layerBindings` in sync with actual `layers[].id`.
* **Time**: whole-layer `time` for uniform timespans; feature `timeProperty` for heterogeneous data.
* **Schemas**: update `*.schema.json` when adding new keys; CI will enforce.

---

### TL;DR

* Generate **`app.config.json`** from STAC and treat it as **source of truth**.
* Use **`time_config.json`**, **`legend.json`**, **`categories.json`**, and **`story_layers.json`** to tweak UX without code.
* Validate configs; prefer COG/tiles and EPSG:4326 for smooth, scalable rendering.
