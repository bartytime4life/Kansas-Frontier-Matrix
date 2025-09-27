# Kansas Geo Timeline — Web App

**Time · Terrain · History** — a tiny, dependency-light MapLibre viewer with a time slider.  
It reads layers from a **STAC-derived config** (preferred), or from a simple
`viewer.json` / `layers.json` (fallback). Designed for **GitHub Pages**.

---

## Folder contents

```text
web/
├─ index.html              # MapLibre bootstrap + UI (loads config JSON, builds UI)
├─ style.css               # unified tokens, layout, legend, toggles, accessibility
├─ app.config.json         # (preferred) generated from STAC (see below)
├─ layers.json             # (fallback) dev/preview catalog
├─ config/                 # optional UI/config overrides
│  ├─ app.config.json      # alt location for generated config
│  ├─ viewer.json          # dev override (same shape as app.config.json)
│  ├─ layers.json          # layers-only dev override
│  ├─ time_config.json     # overrides time/defaultYear/timeUI + presets
│  ├─ legend.json          # symbol tokens + layerBindings
│  ├─ categories.json      # sidebar groups (id → {label, order})
│  ├─ sources.json         # provenance/audit registry (optional)
│  └─ schema.json          # JSON Schemas (legend/categories/sources)
└─ assets/
   ├─ logo.png
   └─ favicon.svg
````

> Load order at runtime (first hit wins):
> `./app.config.json` → `./config/app.config.json` → `./config/viewer.json` → `./config/layers.json` → `./layers.json`
> If `./config/time_config.json` exists, it **overrides** `time`, `defaultYear`, and `timeUI`.

---

## Quick start

### Option A — Python one-liner

```bash
cd web
python -m http.server 8080
# open http://localhost:8080
```

### Option B — Docker (compose profile)

```bash
# from repo root
docker compose --profile dev up -d site
# open http://localhost:8080
```

---

## Build the data + configs

From the repo root:

```bash
# Discover tools/env
make env

# Produce terrain derivatives (COGs → tiles via pipeline)
make terrain

# Fallback site manifest at web/layers.json
make site

# Preferred: STAC → web/config/app.config.json (and sync UI)
make stac stac-validate site-config
```

Optional DEM override:

```bash
make terrain DEM=/path/to/dem.tif
```

---

## Configs the web app understands

### 1) STAC-driven (preferred) — `app.config.json`

Created by:

```bash
make site-config
```

Top-level shape (simplified):

```json
{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 12 },
  "defaults": {
    "minzoom": 0, "maxzoom": 15, "opacity": 1.0, "visible": true,
    "time": { "start": null, "end": null }
  },
  "layers": [
    {
      "id": "usgs_topo_1894_larned",
      "title": "USGS Historic Topo — Larned (1894)",
      "type": "raster",
      "url": "./tiles/historic/usgs_1894_larned/{z}/{x}/{y}.png",
      "opacity": 0.7,
      "visible": true,
      "category": "historical",
      "legendKey": "historic_topo",
      "time": { "start": "1894-01-01", "end": "1894-12-31" }
    },
    {
      "id": "ks_settlements",
      "title": "Settlements, Forts, Trading Posts",
      "type": "geojson",
      "data": "data/processed/towns_points.json",
      "category": "culture",
      "legendKey": "towns",
      "time": { "start": "1800-01-01", "end": null },
      "timeProperty": "year",
      "style": {
        "circleColor": "#FF595E",
        "circleRadius": 4,
        "circleOpacity": 0.95,
        "circleStrokeColor": "#FFFFFF",
        "circleStrokeWidth": 1
      },
      "popup": ["name", "type", "year", "year_end"]
    }
  ]
}
```

### 2) Fallback — `viewer.json` / `layers.json`

Use for quick dev iterations (same keys as above, but minimal). Example `layers.json`:

```json
{
  "version": "1.3.0",
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "layers": [
    {
      "id": "ks_hillshade_2018",
      "title": "Hillshade (2018–2020)",
      "type": "raster",
      "url": "./tiles/terrain/hillshade/{z}/{x}/{y}.png",
      "opacity": 0.9,
      "visible": true,
      "time": { "start": "2018-01-01", "end": "2020-12-31" }
    },
    {
      "id": "ksriv_channels",
      "title": "Kansas River — Channels",
      "type": "geojson",
      "data": "./data/processed/hydrology/kansas_river/channels.geojson",
      "style": { "lineColor": "#1e88e5", "lineWidth": 1.6, "lineOpacity": 1.0 },
      "visible": true,
      "time": { "start": "1850-01-01", "end": null }
    }
  ]
}
```

> **Do not** point rasters at raw `.tif` in the web app. Serve tiles (e.g., `…/{z}/{x}/{y}.png`).
> Vectors use `data` (or `path`) for GeoJSON; rasters use `url` (or `tiles`).

---

## How layers load (`index.html`)

* **Rasters** → MapLibre `raster` source from `url`/`tiles` (PNG/JPEG tiles).
* **GeoJSON** → MapLibre `geojson` source from `data` (or `path`).
* **Styles** → Single `style` block with camelCase keys:

  * lines: `lineColor`, `lineWidth`, `lineOpacity`, `lineDasharray`
  * fills: `fillColor`, `fillOpacity`, `fillOutlineColor`
  * circles: `circleColor`, `circleRadius`, `circleOpacity`, `circleStrokeColor`, `circleStrokeWidth`
* **Legend** → Either auto from `layers[].legend` or via `config/legend.json` + `legendKey` / `layerBindings`.
* **Time filter** → Layer-level `time.start/end` or feature-level `timeProperty`/`endTimeProperty`.

---

## Publishing to GitHub Pages

1. Ensure **`web/`** has a valid config (`app.config.json` preferred, or `config/viewer.json`/`layers.json`).
2. CI target (recommended): run `make prebuild` to validate STAC + render configs.
3. Configure Pages to serve from `web/` (or a built `site/` directory).
4. Optional link-check: keep `.lychee.toml` at repo root:

```toml
base_url = "https://<user>.github.io/<repo>/"
include = ["site/**", "README.md", "web/**"]
fail_if_empty = false
```

---

## Troubleshooting

* **Blank map / 404s** → Check console, verify tile/GeoJSON paths relative to `web/`. Serve via HTTP, not `file://`.
* **Tiles not rendering** → Ensure your pipeline emitted tiles (`./tiles/.../{z}/{x}/{y}.png`).
* **Slider inert** → Missing `time` or `timeProperty`. Add them, or ensure `time_config.json` merges in.
* **Legend chip missing** → `legendKey` must match `config/legend.json.symbols` or add `layerBindings[id]`.
* **Slow vectors** → Tile or simplify; use raw GeoJSON only for small sets.

---

## Conventions

* **IDs**: `snake_case`, stable, include vintage when helpful (`usgs_topo_1894_larned`).
* **Categories**: one per layer (`reference`, `terrain`, `environment`, `historical`, `documents`, `infrastructure`, `culture`, `hazards`).
* **CRS**: store/serve COGs in pipelines; web uses EPSG:3857/4326 tiles.
* **Schema**: update `web/config/schema.json` when adding keys; validate in CI.

---

## Roadmap (web)

* Vector tiles (PMTiles/TiTiler).
* Permalinks (center/zoom/year/layers in query).
* Story mode powered by `config/story_layers.json` presets.

**License:** MIT (see repo root)
**Questions / ideas?** Open an issue in the repo.

```
```
