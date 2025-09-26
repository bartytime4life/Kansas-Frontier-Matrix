# `web/config/` — Kansas-Frontier-Matrix Viewer Configuration (Rebuilt)

This folder contains **declarative JSON configs** that power the MapLibre viewer (`web/app.js`).
Configs define **what** to load (layers), **how** to render it (style/legend/categories), and **when** to show it (time slider).

The design goal: **zero hand-tuning in code**—everything should be controllable here or generated from STAC.

---

## What lives here (and why)

| File               | Required? | Purpose                                                       | Who edits it          | Source of truth    |
| ------------------ | --------: | ------------------------------------------------------------- | --------------------- | ------------------ |
| `app.config.json`  |         ✅ | Final, merged viewer config (defaults + layers)               | *Generated* from STAC | **Yes**            |
| `viewer.json`      |         ➖ | Full, hand-edited config for local/dev override               | Devs                  | No (fallback Only) |
| `layers.json`      |         ➖ | Layers-only catalog for quick tests                           | Devs                  | No (fallback Only) |
| `time_config.json` |         ➖ | Overrides the active config’s `time` block (and adds presets) | Devs                  | Merges over active |
| `legend.json`      |         ➖ | Global symbology tokens (colors, widths, dash arrays)         | Devs/Cartography      | Referenced by UI   |
| `categories.json`  |         ➖ | Sidebar grouping & labels                                     | Devs/Cartography      | Referenced by UI   |
| `sources.json`     |         ➖ | Human map of layer IDs → source/STAC/context                  | Devs/Data             | Helpful for audits |
| `schema.json`      |         ➖ | JSON Schema used by CI and local validators                   | Devs                  | Guards structure   |

> **Rule of thumb**: Keep `app.config.json` generated; use `viewer.json` / `layers.json` only for quick experiments.

---

## Loading order (runtime)

`web/app.js` selects the first file that exists:

1. `./config/app.config.json`
2. `./config/viewer.json`
3. `./config/layers.json`
4. `./layers.json` *(legacy root)*

If `time_config.json` exists, its `time` block **overrides** the active config.
If `legend.json` or `categories.json` exist, the UI will use them for symbols and grouping.

---

## Generate the viewer config from STAC

```bash
# 1) Build/refresh STAC items from your data
make stac

# 2) Render the viewer config from STAC items
kgt render-config \
  --stac stac/items \
  --output web/config/app.config.json \
  --pretty
```

Re-run after adding, removing, or changing any STAC items.

---

## The contract: config shape (authoritative)

### Top-level (`app.config.json` or `viewer.json`)

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

  "time": { "min": "1850-01-01", "max": "2025-12-31", "defaultYear": 1930, "step": 1, "loop": false, "fps": 12 },

  "defaults": {
    "minzoom": 0, "maxzoom": 15, "opacity": 1.0, "visible": true,
    "time": { "start": null, "end": null }
  },

  "layers": [ /* array of layer objects (schema below) */ ]
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

  // Optional styling for vector/geojson
  "style": {
    "fillColor": "#A0C4FF",
    "fillOpacity": 0.6,
    "lineColor": "#3A86FF",
    "lineWidth": 1.0,
    "circleColor": "#FF595E",
    "circleRadius": 4,
    "lineDasharray": [2, 2]
  },

  // GeoJSON popups and time mapping
  "popup": ["name", "type", "year", "year_end"],
  "timeProperty": "year",     // layer-level feature time (if features encode time)
  "endTimeProperty": "year_end",

  // Image overlays (georeferenced image bounds)
  "coordinates": [
    [lonW, latN], [lonE, latN], [lonE, latS], [lonW, latS]
  ]
}
```

**Type specifics**

* `raster` → tile servers **or** local COG/GeoTIFF
* `raster-dem` → elevation; viewer may derive hillshade (if enabled in app.js)
* `vector` → vector tiles (TileJSON)
* `geojson` → inline/URL GeoJSON (tile large datasets or simplify)
* `image` → single image overlay; must include **`coordinates`** in clockwise order from NW

---

## Time configuration (override file)

`time_config.json` lets you override the active config’s `time` block and add presets:

```json
{
  "time": {
    "min": "1800-01-01",
    "max": "2025-12-31",
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
```

* Dates can be `YYYY` or `YYYY-MM-DD`; the viewer normalizes them.
* Layer filtering uses:

  * layer-level `time.start`/`time.end` (or)
  * per-feature `timeProperty`/`endTimeProperty` for GeoJSON.

---

## Symbology & categories

### `legend.json` (global design tokens)

```json
{
  "treaties":    { "fillColor": "#FFCA3A", "lineColor": "#B08900" },
  "trails":      { "lineColor": "#4361EE", "lineDasharray": [2, 2] },
  "railroads":   { "lineColor": "#8D99AE" },
  "tornado":     { "lineColor": "#D00000" },
  "wildfire":    { "fillColor": "#E76F51" }
}
```

### `categories.json` (sidebar grouping)

```json
{
  "reference":     { "label": "Reference", "order": 0 },
  "terrain":       { "label": "Terrain & Elevation", "order": 1 },
  "environment":   { "label": "Land & Water", "order": 2 },
  "historical":    { "label": "Historical Maps", "order": 3 },
  "documents":     { "label": "Documents & Records", "order": 4 },
  "infrastructure":{ "label": "Trails & Rails", "order": 5 },
  "culture":       { "label": "Settlements & Sites", "order": 6 }
}
```

---

## Examples

### A historical raster layer (COG)

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

### A time-aware GeoJSON points layer

```json
{
  "id": "ks_settlements",
  "title": "Settlements, Forts, Trading Posts",
  "type": "geojson",
  "url": "data/processed/towns_points.json",
  "category": "culture",
  "time": { "start": null, "end": null },
  "timeProperty": "year",
  "endTimeProperty": "year_end",
  "popup": ["name", "type", "year", "year_end"],
  "style": { "circleColor": "#FF595E", "circleRadius": 4 },
  "visible": true,
  "attribution": "Compiled / KFM"
}
```

---

## Quality & performance conventions

* **Rasters**: Prefer **COG** (Cloud-Optimized GeoTIFF). Reproject to **EPSG:4326**.
* **Vectors**: Use **GeoJSON** only for small/medium datasets. For large ones, **tile** or simplify.
* **Metadata**: Always set a meaningful `title`, `category`, and `attribution`.
* **Time**: Provide `time.start`/`time.end` if the whole layer is time-bounded; otherwise use per-feature properties.
* **IDs**: `snake_case`, stable across releases; include a hint for source and vintage (e.g., `usgs_topo_1894_larned`).

---

## Validation & CI

**Local quick check**

```bash
jq . web/config/app.config.json > /dev/null
```

**Schema validation (if `schema.json` present)**

```bash
ajv validate -s web/config/schema.json -d web/config/app.config.json
```

**CI guarantees**

* `tests/test_web_configs.py` validates structure, URLs, categories, and time blocks.
* STAC → `app.config.json` generation is run in workflows; broken STAC yields a failed build.

---

## Troubleshooting

* **Layer doesn’t show**
  Check `type`, `url`, `minzoom/maxzoom`, and that the file exists and is web-servable. For GeoTIFF, confirm it’s a COG.
* **Timeline not filtering**
  Ensure `time` exists (layer or feature-level). For feature-level, set `timeProperty` (and optionally `endTimeProperty`).
* **Legend missing**
  Add `legend.json` and ensure the keys match your layers or your UI wiring.
* **Sidebar grouping wrong**
  Verify `category` matches a key in `categories.json`.
* **Slow rendering**
  Tile big GeoJSONs or simplify geometries. Use vector tiles for statewide dense layers.

---

## Common workflows

Generate from STAC (fresh):

```bash
make stac
kgt render-config --stac stac/items --output web/config/app.config.json --pretty
```

Add a new time preset (does not regenerate STAC):

```bash
jq '.presets += [{ "label":"Santa Fe Trail", "start":1821, "end":1880 }]' \
  web/config/time_config.json > /tmp/time && mv /tmp/time web/config/time_config.json
```

Audit a layer’s provenance (if you keep `sources.json`):

```bash
jq '.["ks_settlements"]' web/config/sources.json
```

---

## Philosophy

* **Generated first**: Prefer machine-generated `app.config.json` from STAC.
* **Text-first overrides**: Small, intentional human edits go in `time_config.json`, `legend.json`, `categories.json`.
* **Reproducible**: Every change here should be lintable, schema-checked, and traceable to STAC or documented overrides.

---

### TL;DR

* Generate **`app.config.json`** from STAC and treat it as the viewer **source of truth**.
* Use **`time_config.json`**, **`legend.json`**, and **`categories.json`** to tweak behavior & UX without code.
* Validate configs and prefer COG/tiles and EPSG:4326 for smooth, scalable rendering.
