# 🗺️ Map Overlays (Static Assets)

![Overlays](https://img.shields.io/badge/maps-overlays-1f6feb?style=for-the-badge)
![Contract First](https://img.shields.io/badge/contract--first-required-2ea043?style=for-the-badge)
![No Mystery Layers](https://img.shields.io/badge/no--mystery--layers-ever-f85149?style=for-the-badge)

This folder contains **map overlay assets** that the web UI can load on top of basemaps (2D and 3D).  
Overlays can be **raster tiles**, **vector layers**, **time series**, or **special effects** (masks, highlights, heatmaps).

> [!IMPORTANT]
> **Every overlay MUST be self-describing.** If it renders in the UI, it must ship with a metadata “data contract” (`overlay.json`) and enough provenance info to recreate, audit, and attribute it.

---

## ✨ What counts as an overlay?

✅ Belongs here:
- 🧱 **Raster overlays**: historical scans, classification rasters, hillshades, drought indices, radar loops (pre-tiled).
- 🧬 **Vector overlays**: boundaries, points/lines/polygons, choropleths, label layers, routes.
- 🕰️ **Time-aware overlays**: date-stamped tiles/GeoJSON + metadata explaining time controls.
- 🎛️ **Legends & UI helpers**: legend SVG/PNG, thumbnails, short descriptions, attribution strings.

🚫 Doesn’t belong here:
- Secrets, API keys, raw source dumps, giant unbounded GeoJSON, private datasets.
- “Temporary” outputs without contracts (use a scratch/work area elsewhere).

---

## 📦 Directory layout (recommended)

```text
web/
└─ assets/
   └─ maps/
      └─ overlays/
         ├─ README.md                         👈 you are here
         ├─ manifest.json                     🧭 optional index of overlays
         ├─ _shared/                          ♻️ shared legends/icons/palettes
         └─ <overlay-id>/                     🆔 one overlay per folder
            ├─ overlay.json                   🧾 REQUIRED data contract
            ├─ thumbnail.webp                 🖼️ optional
            ├─ legend.svg                     🧷 optional
            ├─ styles/
            │  ├─ maplibre.json               🎨 optional (MapLibre style snippet)
            │  └─ deckgl.json                 🎛️ optional (Deck.gl layer config)
            └─ data/
               ├─ <anything-you-serve>        📦 tiles, pmtiles, geojson, etc.
               └─ ...
```

> [!TIP]
> Keep **one overlay per folder** and treat that folder as a **versionable artifact**. If you need a breaking change, create a new version folder or bump `version` in `overlay.json`.

---

## 🆔 Naming conventions

- Folder name: `kebab-case` and stable: `historic-topo-1894-ellsworth`
- Overlay id inside contracts: namespaced + descriptive:
  - `kfm__historic_topo__1894__ellsworth`
  - `kfm__ndvi__landsat__annual__2001_2020`
- Avoid spaces, avoid “final_v7_reallyfinal”.

---

## 🧾 The overlay contract (`overlay.json`) — REQUIRED

This is the single source of truth that the UI + validators rely on.

### ✅ Minimal required fields

```json
{
  "schema_version": "v1",
  "id": "kfm__example__overlay",
  "title": "Example Overlay",
  "description": "What it is, what it means, what it is NOT.",
  "type": "raster-tiles",
  "format": "pmtiles",
  "version": "1.0.0",
  "attribution": "Source org / author",
  "license": "CC-BY-4.0",
  "spatial": {
    "crs": "EPSG:3857",
    "bbox": [-99.5, 38.3, -98.8, 38.9]
  },
  "temporal": {
    "start": "1894-01-01",
    "end": "1894-12-31"
  },
  "provenance": {
    "source_url": "https://example.org/dataset",
    "inputs": [],
    "processing_steps": [
      "georeferenced scan",
      "reprojected to EPSG:3857",
      "tiled to z6–z14",
      "packaged as PMTiles"
    ],
    "generated_by": {
      "tool": "gdal/maptiler/tippecanoe/etc",
      "tool_version": "x.y.z",
      "run_date": "2026-01-14"
    }
  },
  "assets": {
    "data": "data/overlay.pmtiles",
    "legend": "legend.svg",
    "thumbnail": "thumbnail.webp"
  },
  "ui": {
    "default_visible": false,
    "minzoom": 6,
    "maxzoom": 14,
    "opacity": 0.8,
    "blend_mode": "normal",
    "interactive": false
  }
}
```

### 🧩 Common optional fields (highly recommended)

- `tags`: `["hydrology", "historic", "remote-sensing"]`
- `sensitivity`: `"public" | "restricted" | "internal"`
- `confidence`: `"measured" | "modeled" | "inferred"`
- `uncertainty`: short explanation + links to methods
- `contact`: who to ping when it breaks
- `checksum`: for big assets so caches can safely invalidate

> [!NOTE]
> Contracts are “metadata as code.” Treat them like code: lint, validate, review, and version.

---

## 🧠 Overlay types we support

| Type 🧩 | Best for ✅ | Avoid when ⚠️ | Typical files |
|---|---|---|---|
| `raster-tiles` 🧱 | scans, hillshade, indices, radar loops | huge single images without tiling | `/{z}/{x}/{y}.png` or `.webp`, or `*.pmtiles` |
| `raster-cog` 🛰️ | large rasters you want to window/stream | offline-only clients | `*.tif` (COG) + optional tile endpoint |
| `vector-geojson` 🧬 | small/medium features, prototyping | nationwide polygons w/ many vertices | `*.geojson` |
| `vector-tiles` 🧊 | large vectors, fast rendering | tiny one-off datasets | `*.pmtiles` / `*.mbtiles` / tile folders |
| `3d-drape` 🧊🗻 | terrain drape, subsurface surfaces | anything that must load instantly | `quantized-mesh`, `3d-tiles`, `glTF` (project-dependent) |
| `ui-mask` 🎭 | focus areas, spotlight overlays | data analysis | `*.geojson` or raster mask |

---

## 🧰 Quick start: add a new overlay in 6 steps

1. 📁 Create a folder: `web/assets/maps/overlays/<overlay-id>/`
2. 🧾 Add `overlay.json` (required).
3. 📦 Drop assets into `data/` (tiles, pmtiles, geojson, etc.).
4. 🧷 Add `legend.svg` + `thumbnail.webp` (recommended).
5. 🧪 Validate locally (see checklist below).
6. 🧭 (Optional) Add entry to `manifest.json` so the UI can auto-discover it.

### Optional `manifest.json` shape (simple + friendly)

```json
{
  "schema_version": "v1",
  "overlays": [
    "historic-topo-1894-ellsworth",
    "ndvi-annual-2001-2020",
    "tornado-tracks-1950-2025"
  ]
}
```

---

## 🎨 Cartography & UX rules (so overlays don’t become chaos)

**The goal:** overlays should *add meaning* without obliterating the basemap.

### Do ✅
- 🫧 Use **opacity** intentionally (0.5–0.85 is typical for rasters).
- 🧷 Always ship a **legend** (or explain why none is needed).
- 🌓 Prefer **perceptually sane palettes** for continuous rasters (avoid rainbow by default).
- 🧩 Simplify geometry by zoom level (or use vector tiles).
- ♿ Ensure accessibility: color isn’t the only channel (add outlines, patterns, labels where appropriate).

### Don’t ❌
- 🔥 Over-saturate everything.
- 🧱 Load a 200MB GeoJSON into the browser.
- 🕳️ Hide provenance (“trust me bro” datasets).

> [!TIP]
> If the overlay is meant to “feel” like it’s *painted on the world* (e.g., haze, burn scars, heat), consider blend modes and WebGL-friendly rendering paths in your style configs.

---

## ⚡ Performance & scaling guidelines

### Raster overlays 🧱
- Prefer **tiled assets** (folder tiles or packed tiles like PMTiles/MBTiles).
- Use `webp` where acceptable; use `png` when you need crisp lines + alpha.
- Avoid gigantic single images unless you have a streaming strategy.

### Vector overlays 🧬
- If it’s big, **tile it**.
- If it’s small, GeoJSON is fine — but **simplify** and **clip** to bbox where possible.

### Time series 🕰️
- Don’t ship 10,000 individual files without an index.
- Include time semantics in `overlay.json` (`temporal`, plus UI hints like step size).

---

## 🧪 QA checklist (PR gate vibes)

Before an overlay is “allowed” into the UI:

- [ ] `overlay.json` exists and is valid JSON
- [ ] `id`, `title`, `license`, `attribution`, `spatial.bbox`, `spatial.crs` present
- [ ] Provenance includes source + processing steps
- [ ] Assets paths exist and match contract
- [ ] Raster tiles align (no flipped Y, no weird bounds, no seams at common zooms)
- [ ] Vectors render at intended zooms (no self-intersections if that matters)
- [ ] No sensitive info in geometry/properties
- [ ] Legend + thumbnail included (or explicitly omitted with rationale)

---

## 🧑‍🍳 Build recipes (practical pipelines)

> [!NOTE]
> These are **reference** workflows. Use the project’s actual tooling stack where available.

### 🛰️ A) From a big raster → COG → tiles/pmtiles
1. Reproject to your target CRS (commonly EPSG:3857 for web tiles).
2. Build overviews/pyramids.
3. Tile and/or package.

Example (conceptual):
```bash
# 1) Reproject + compress
gdalwarp -t_srs EPSG:3857 -r bilinear input.tif output_3857.tif

# 2) Make a COG (tooling varies; pick your standard)
# 3) Tile (gdal2tiles / maptiler / tippecanoe-for-rasters depending on stack)
```

### 🧬 B) From PostGIS/Shapefile → GeoJSON (small) or vector tiles (large)
- Export GeoJSON for small layers.
- For large layers, tile with your vector tiler (e.g., tippecanoe) and store as `pmtiles`.

### ☁️ C) From Earth Engine analysis → exported tables/rasters → overlay
- Reduce/aggregate in EE, export only what you need.
- Keep exports lean: define columns/properties and don’t ship massive geometries unless needed.
- Document your reducers/indices and thresholds in `processing_steps`.

---

## 🔒 Licensing, ethics, and “don’t get us sued” basics

- Every overlay must declare a `license` and `attribution`.
- If the source has usage constraints, reflect them in `sensitivity` and `provenance.consent`.
- If you’re unsure, **treat it as restricted** until proven otherwise.

---

## 🧯 Troubleshooting

**Overlay doesn’t show up**
- Check `minzoom/maxzoom`
- Confirm tile URL/path in `assets.data`
- Confirm CRS expectations (vector coords in EPSG:4326 vs tile world in EPSG:3857)
- If it’s raster tiles: verify z/x/y orientation and bounds

**Looks “washed out” or wrong colors**
- Check gamma/alpha handling
- For rasters: verify colormap + nodata + alpha band
- Try a different blend mode or reduce opacity

**Performance is awful**
- If you’re loading GeoJSON, you probably need vector tiles
- If you’re serving huge rasters, you probably need tiling / COG / caching

---

## ✅ Definition of “done”

An overlay is “done” when:
- It renders correctly across intended zooms 📏
- It has a contract + provenance 🧾
- It has attribution + licensing ✅
- It performs well enough not to melt the UI 🔥
- It’s reviewable by someone who didn’t build it 👀

Happy layering 🌾🗺️🚀
