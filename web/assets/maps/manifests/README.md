# 🗺️ Map Manifests (Front-End) — `web/assets/maps/manifests/`

![KFM](https://img.shields.io/badge/KFM-Maps%20%26%20Manifests-1f6feb?style=for-the-badge)
![Provenance](https://img.shields.io/badge/Provenance--First-%E2%9C%85-2ea44f?style=for-the-badge)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20WebGL-111?style=for-the-badge)
![Cesium](https://img.shields.io/badge/Cesium-3D%20Tiles-111?style=for-the-badge)

**This folder is the “front-end layer catalog.”**  
It contains **manifest files** that tell the web app **what map layers exist**, **how to load them**, **how to style them**, and **how to cite them**.

> If `data/sources/` is the backend’s “source manifest shelf,” this is the UI’s **“layers manifest shelf.”** 📚✨  
> The goal is the same: *everything mappable is inspectable, attributable, and reproducible.*

---

## 🎯 What lives here?

Manifests in this folder should be small, human-reviewable JSON (or YAML if the project standardizes it later) that describe:

- **Layer identity** (stable `id`, title, description)
- **Data access** (tiles, COGs, WMS/WMTS, API endpoints, 3D Tiles, etc.)
- **Rendering** (MapLibre style refs, paint/layout overrides, legend rules)
- **Scale rules** (min/max zoom, visibility defaults)
- **Time rules** (timeline-enabled layers)
- **Provenance** (source, license, attribution, processing/pipeline lineage)
- **UI hints** (category, tags, search keywords, thumbnails)

---

## 📦 Recommended layout (convention)

```text
web/assets/maps/
  manifests/
    README.md                👈 you are here
    layers/
      *.layer.json           🧩 one manifest per layer
    styles/
      *.style.json           🎨 MapLibre styles (or style fragments)
    legends/
      *.legend.json          🗂️ legend rules (optional)
    thumbs/
      *.webp / *.png         🖼️ thumbnails (optional)
```

> **Naming rule:** `kebab-case` ids and filenames.  
> Example: `ks-county-boundaries.layer.json`

---

## 🧩 Layer manifest (minimum schema)

Every layer manifest **must** include these fields:

```json
{
  "manifestVersion": "1.0",
  "id": "ks-county-boundaries",
  "title": "Kansas County Boundaries",
  "kind": "vector-tiles",
  "description": "County boundaries for Kansas (generalized for web).",
  "ui": {
    "category": "Boundaries",
    "tags": ["admin", "county", "kansas"],
    "defaultVisible": false
  },
  "visibility": {
    "minzoom": 5,
    "maxzoom": 14
  },
  "source": {
    "type": "tilejson",
    "url": "/api/tiles/ks-county-boundaries/tilejson"
  },
  "style": {
    "type": "maplibre-style-fragment",
    "targetSourceLayer": "counties",
    "paint": {
      "line-color": "#ffffff",
      "line-width": 1.25,
      "line-opacity": 0.85
    }
  },
  "attribution": {
    "text": "KFM • Source: Kansas GIS / authoritative boundary dataset",
    "license": {
      "name": "CC BY 4.0",
      "spdx": "CC-BY-4.0",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    }
  },
  "provenance": {
    "sourceName": "Kansas GIS (authoritative boundaries)",
    "sourceUrl": "https://example.org/source/ks-boundaries",
    "retrievedAt": "2026-01-15",
    "processing": [
      {
        "step": "simplify",
        "tool": "mapshaper",
        "params": { "pct": 10 }
      },
      {
        "step": "tile",
        "tool": "tippecanoe",
        "params": { "maxzoom": 14 }
      }
    ],
    "outputs": [
      { "type": "vector-tiles", "format": "pbf", "location": "/api/tiles/ks-county-boundaries/{z}/{x}/{y}.pbf" }
    ]
  }
}
```

### ✅ Notes on minimum fields
- `id` is a **stable identifier**: once published, changing it breaks stories, bookmarks, and links.
- `kind` controls how the viewer loads the layer (`vector-tiles`, `raster-tiles`, `cog`, `wms`, `3d-tiles`, etc.).
- `source` must be resolvable by the web app in deployed environments.

---

## 🧠 Supported `kind` values (current + planned)

### 2D (MapLibre)
- `vector-tiles` — PBF (TileJSON or template URL)
- `vector-geojson` — GeoJSON URL (use sparingly; heavy)
- `raster-tiles` — XYZ/WMTS-style tiles
- `cog` — Cloud-Optimized GeoTIFF served via range requests / tile gateway
- `wms` / `wmts` — server-rendered raster layers (fallback / legacy)

### 3D (Cesium)
- `3d-tiles` — Cesium 3D Tiles tileset.json
- `terrain` — terrain provider config (if used)
- `point-cloud` — if standardized later (often still 3D Tiles under the hood)

> **Performance rule of thumb:** prefer **vector tiles** for interactive vectors and **COG/tiles** for big rasters. 🏎️

---

## ⏳ Temporal layers (timeline-ready)

If a layer changes over time (years, dates, timestamps), add a `temporal` block.

```json
{
  "temporal": {
    "enabled": true,
    "type": "discrete",
    "items": [
      { "label": "1885", "time": "1885-01-01", "sourceOverride": { "url": "/tiles/historic/topo/1885/{z}/{x}/{y}.png" } },
      { "label": "1930", "time": "1930-01-01", "sourceOverride": { "url": "/tiles/historic/topo/1930/{z}/{x}/{y}.png" } }
    ],
    "defaultTime": "1930-01-01"
  }
}
```

### Temporal types
- `discrete` — a list of known time “slices”
- `range` — server supports time parameters (e.g., `?time=YYYY-MM-DD` or WMS TIME)

---

## 🎨 Styling options

### Option A — Reference a full MapLibre style
Use when the layer needs multiple sublayers, labels, patterns, or complex styling.

```json
{
  "style": {
    "type": "maplibre-style",
    "url": "../styles/kfm-base.style.json",
    "layerIds": ["ks-county-boundaries-outline", "ks-county-boundaries-labels"]
  }
}
```

### Option B — Style fragment (preferred for simple overlays)
Use when you just need a single MapLibre layer definition.

```json
{
  "style": {
    "type": "maplibre-style-fragment",
    "layerType": "line",
    "targetSourceLayer": "counties",
    "paint": { "line-color": "#fff", "line-width": 1.25 }
  }
}
```

---

## 🧾 Provenance & attribution (non-negotiable)

Every manifest should make it easy for the UI to show “**the map behind the map**”:

- Source org + dataset name
- Source URL (or citation URL)
- License + usage constraints
- Retrieval date (or release version)
- Processing steps (what we did to it)
- Output locations (what the viewer actually loads)

### 🚫 Don’ts
- Don’t embed API keys, tokens, or secrets in manifests.
- Don’t ship layers without license clarity.
- Don’t “handwave” provenance; add the real link or mark as `unknown` with a TODO.

---

## 🧪 Validation & quality gates

Recommended checks for every PR that touches manifests:

- ✅ JSON parses
- ✅ `id` unique across all manifests
- ✅ `source.url` reachable in dev + prod
- ✅ attribution present (text + license)
- ✅ bounds/minzoom/maxzoom are sane
- ✅ temporal layers have consistent time formats

> If/when we add a linter, put it in `tools/` and run it in CI. 🔧

---

## 🧭 How the app uses these manifests

Typical flow:

1. **Layer Catalog UI** scans `manifests/layers/` and builds the toggle list.
2. **Map Viewer** (2D) reads `source` + `style` and registers the layer in MapLibre.
3. **3D Viewer** (if enabled) reads `3d-tiles` manifests and registers a Cesium tileset.
4. **Timeline** uses `temporal.enabled` layers to sync visible data to the chosen time.
5. **Info Panels** pull `provenance` and `attribution` to display citations.

---

## ➕ Adding a new layer (fast checklist)

1. Create `web/assets/maps/manifests/layers/<id>.layer.json`
2. Pick the correct `kind`
3. Configure `source`
4. Add at least one styling approach (`style`)
5. Add `attribution` + `provenance`
6. Add `ui.category`, `ui.tags`, and `ui.defaultVisible`
7. (Optional) add a thumbnail to `thumbs/`
8. Verify it loads in the map viewer and displays attribution

---

## 🧯 Troubleshooting

- **Layer toggles but nothing shows:** check `minzoom/maxzoom`, bounds, and `source.url`.
- **Vector tiles load but styling doesn’t:** confirm `targetSourceLayer` matches tileset layer names.
- **Raster layer is slow:** consider switching from dynamic render to cached XYZ tiles or COG access.
- **Timeline doesn’t affect the layer:** ensure `temporal.enabled: true` and that the viewer supports the `temporal.type`.

---

## 🗺️ Future niceties (wishlist)

- `schema.json` + `jsonschema` CI validation
- auto-generated layer catalog docs
- thumbnail/legend generation in pipelines
- a “provenance viewer” drawer that shows processing lineage as a mini graph

---

### ⭐ Golden rule
If a user asks **“Where did this layer come from?”** the answer must be one click away. 🧭💡
