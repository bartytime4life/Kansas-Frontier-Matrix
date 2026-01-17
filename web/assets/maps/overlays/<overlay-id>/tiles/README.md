# 🧩 Overlay Tiles — `<overlay-id>`

![Tiles](https://img.shields.io/badge/tiles-XYZ-0B7285?style=flat-square)
![Projection](https://img.shields.io/badge/CRS-EPSG%3A3857-364FC7?style=flat-square)
![TileSize](https://img.shields.io/badge/tileSize-256px-2B8A3E?style=flat-square)
![Provenance](https://img.shields.io/badge/provenance-required-9C36B5?style=flat-square)

> **Purpose 🎯**  
> This folder contains **pre-rendered map tiles** (static files) for a single overlay in the Kansas Frontier Matrix (KFM) web map.  
> Use tiles for **stable, frequently accessed layers** where performance matters and serving static files is preferred.

---

## ✅ Quick facts (fill these in)

| Field | Value |
|---|---|
| **Overlay ID** | `<overlay-id>` |
| **Overlay Type** | `raster` (PNG/WebP/JPG) / `vector` (PBF) |
| **Tile scheme** | `XYZ` (`{z}/{x}/{y}`) |
| **CRS / Projection** | `EPSG:3857` (Web Mercator) |
| **Tile size** | `256 × 256` px *(unless otherwise configured)* |
| **Zoom range** | `minzoom: __` → `maxzoom: __` |
| **Coverage** | Kansas-wide / Region / Site-specific |
| **Source & License** | **Required** → see “Provenance & attribution” 🧾 |

---

## 📦 Folder layout

This `README.md` lives *inside* the tiles payload so it never gets separated from the layer.

```text
web/
└─ assets/
   └─ maps/
      └─ overlays/
         └─ <overlay-id>/
            ├─ tiles/ 🧱
            │  ├─ README.md ✅ (this file)
            │  └─ {z}/
            │     └─ {x}/
            │        └─ {y}.png  (or .webp / .jpg / .pbf)
            ├─ overlay.json      (recommended) 🧾
            ├─ legend.png        (optional) 🗝️
            └─ thumbnail.jpg     (optional) 🖼️
```

> **Tip 💡**  
> If this overlay is **vector tiles**, you’ll typically store `.pbf` tiles here and load them as a `vector` source in MapLibre.  
> If this overlay is **raster**, you’ll store `.png/.webp/.jpg` tiles and load them as a `raster` source.

---

## 🗺️ Tile grid conventions (XYZ)

### URL template
From the web app, tiles are addressed using the standard “slippy map” pattern:

```text
.../assets/maps/overlays/<overlay-id>/tiles/{z}/{x}/{y}.png
```

### Coordinate rules
- `z` = zoom level (0 = world, higher = closer)
- `x` = tile column (increases left ➡️ right)
- `y` = tile row (increases top ⬇️ bottom) **for XYZ**
- Origin is **top-left** (XYZ).  
  ⚠️ If you generated **TMS** tiles (origin bottom-left), you must flip `y` or regenerate as XYZ.

---

## 🧭 How the web map should load this overlay (MapLibre examples)

### Raster tiles (PNG/WebP/JPG)
```js
map.addSource("<overlay-id>", {
  type: "raster",
  tiles: [
    "assets/maps/overlays/<overlay-id>/tiles/{z}/{x}/{y}.png"
  ],
  tileSize: 256,
  minzoom: 0,
  maxzoom: 14,
  attribution: "REQUIRED: <source org> (<license>)"
});

map.addLayer({
  id: "<overlay-id>",
  type: "raster",
  source: "<overlay-id>",
  paint: {
    "raster-opacity": 0.85
  }
});
```

### Vector tiles (PBF)
```js
map.addSource("<overlay-id>", {
  type: "vector",
  tiles: [
    "assets/maps/overlays/<overlay-id>/tiles/{z}/{x}/{y}.pbf"
  ],
  minzoom: 0,
  maxzoom: 14,
  attribution: "REQUIRED: <source org> (<license>)"
});

// Then add one or more layers referencing a source-layer name:
map.addLayer({
  id: "<overlay-id>-fill",
  type: "fill",
  source: "<overlay-id>",
  "source-layer": "<source-layer-name>",
  paint: {
    "fill-opacity": 0.6
  }
});
```

---

## 🧾 Provenance & attribution (KFM “no mystery layers” rule)

KFM layers are **provenance-first**: anything visible in the UI must be traceable to:
- a **source** (who/where it came from),
- a **license** (how it can be used),
- and **processing steps** (how it was generated).

### Minimum expectations for this overlay ✅
- **Attribution text** exists (shown in UI)  
- **License** is known and compatible  
- **Processing summary** exists (even if brief)  
- **Source references** exist (IDs, archive references, dataset name, etc.)

### Recommended: `../overlay.json` “mini-contract”
Store a tiny, UI-friendly contract adjacent to tiles (and link it to the deeper data catalog if applicable).

<details>
<summary><strong>📄 Example overlay.json</strong> (click to expand)</summary>

```json
{
  "id": "<overlay-id>",
  "title": "Human-friendly overlay name",
  "type": "raster",
  "tileScheme": "xyz",
  "tileSize": 256,
  "format": "png",
  "minzoom": 0,
  "maxzoom": 14,
  "boundsWGS84": [-102.051, 36.993, -94.588, 40.004],
  "attribution": "Source Org — License Name",
  "license": {
    "name": "CC-BY-4.0",
    "spdx": "CC-BY-4.0"
  },
  "sources": [
    {
      "name": "Dataset / Archive reference",
      "ref": "KHS-<catalog-id> / DOI / accession / etc."
    }
  ],
  "processing": {
    "generatedBy": "gdal2tiles / MapTiler / pipeline name",
    "generatedAt": "YYYY-MM-DD",
    "notes": "Brief steps + key parameters (CRS, resampling, color, nodata)."
  }
}
```
</details>

---

## 🛠️ Generating or updating tiles

> **Rule of thumb 🧠**  
> Generate tiles **from a georeferenced source** (GeoTIFF, COG, MBTiles, vector dataset) in **EPSG:3857**.

### Option A: GDAL (`gdal2tiles.py`) — quick + standard
```bash
# Example: generate XYZ tiles from a GeoTIFF
gdal2tiles.py \
  -z 0-14 \
  -w none \
  -r bilinear \
  input.tif \
  web/assets/maps/overlays/<overlay-id>/tiles
```

### Option B: MBTiles-first workflow (recommended for larger sets)
```text
source → build MBTiles → extract tiles → optimize → publish
```

### Tile optimization (strongly recommended)
- PNG: `oxipng`, `pngquant` 🧊
- WebP: `cwebp` 🌿
- Remove junk files (`.DS_Store`, `Thumbs.db`) 🧹

---

## ✅ QA checklist (must pass before merging)

### Grid / rendering
- [ ] Tiles follow `XYZ` `{z}/{x}/{y}` (no TMS flip)
- [ ] Overlay aligns with basemap at **multiple zoom levels**
- [ ] `tileSize` matches client config (`256` unless explicitly `512`)
- [ ] No obvious seams, edge halos, or resampling artifacts at tile borders

### Coverage
- [ ] Zoom range is correct and documented (`minzoom/maxzoom`)
- [ ] Empty tiles are not bloating the folder (avoid oceans of transparent tiles)

### Performance
- [ ] Typical tile sizes are reasonable (avoid multi‑MB tiles)
- [ ] Folder size is acceptable for the repo (see scaling note below)

### Provenance
- [ ] Attribution is present and correct
- [ ] License is recorded
- [ ] `overlay.json` exists (recommended) and is filled in 🧾

---

## 📈 Scaling note (when tiles get huge)

If this overlay becomes **very large** (lots of zoom levels, big coverage, or frequent updates), consider:
- serving tiles via a **tile server / CDN** (static hosting scales well),
- switching to **COGs** (Cloud-Optimized GeoTIFF) for raster access patterns,
- or using **vector tiles** for data-driven styling and smaller footprints.

---

## 🔗 Related KFM concepts (context)
- **Map UI**: layer toggles, opacity controls, legends, metadata on click 🖱️
- **Evidence-first UX**: users should be able to see “the map behind the map” 🧠
- **Contracts**: metadata is a first-class requirement, not an afterthought 🧾

---

## 🧷 Maintainers
- Owner: `@<name-or-team>`
- Last regenerated: `YYYY-MM-DD`
- Notes: `...`
