# 🗺️ Overlay: `<overlay-id>`

[![KFM](https://img.shields.io/badge/KFM-map%20overlay-2ea44f)](../../../../../README.md)
![status](https://img.shields.io/badge/status-draft-lightgrey)
![type](https://img.shields.io/badge/type-raster%20tiles-blue)
![crs](https://img.shields.io/badge/CRS-EPSG%3A3857-success)
![provenance](https://img.shields.io/badge/provenance-required-brightgreen)

> ✅ **Purpose:** This folder contains **UI-ready assets** for a single map overlay used in the KFM web viewer.  
> 🔎 **Rule:** Nothing here is a mystery—every pixel/feature must trace back to a source + processing steps.

📍 **Path:** `web/assets/maps/overlays/<overlay-id>/`  
⬅️ Back to overlays index: `../README.md`

---

## 🧾 Quick facts

| 🧩 Field | ✅ Value |
|---|---|
| **Overlay ID** | `<overlay-id>` |
| **Title** | `<Human-friendly title>` |
| **Overlay kind** | `raster-tiles` \| `vector-tiles` \| `image-overlay` |
| **Theme** | `<e.g., historical map, land cover, boundaries, DEM, risk surface>` |
| **Projection** | `EPSG:3857` (Web Mercator) |
| **Extent (W,S,E,N)** | `<-102.05, 36.99, -94.59, 40.00>` |
| **Time range** | `<YYYY..YYYY>` or `<YYYY-MM-DD..YYYY-MM-DD>` |
| **Zoom range** | `<minZoom>–<maxZoom>` |
| **Default opacity** | `<0.0–1.0>` |
| **Blend mode** | `normal` \| `multiply` \| `screen` |
| **License** | `<SPDX or license name>` |
| **Attribution** | `<required credit line>` |
| **Maintainer** | `@<github-handle>` |
| **Last built** | `<YYYY-MM-DD>` |

---

## 👀 Preview

![Overlay preview](./thumbnail.jpg)

> 🧠 If `thumbnail.jpg` doesn’t exist yet, add one (1280×720 recommended) so PR reviews are fast 🔍

<details>
<summary>🖼️ Suggested extra screenshots (optional)</summary>

- `./preview-before-after.jpg` (overlay OFF vs ON)
- `./preview-legend.jpg` (overlay + legend visible)
- `./preview-maxzoom.jpg` (sharpness check at max zoom)

</details>

---

## 📁 Folder contents

```text
📦 web/assets/maps/overlays/<overlay-id>/
├─ 📝 README.md                # you are here
├─ 🧾 overlay.json             # machine-readable manifest for the web app
├─ 🖼️ thumbnail.jpg            # quick preview for PRs + catalog UI
├─ 🗺️ legend.(svg|png|json)    # legend used by the layer panel (optional)
├─ 🔐 checksums.sha256         # integrity checks (recommended)
└─ 🧱 tiles/                   # ONLY if using XYZ tile folders
   └─ {z}/{x}/{y}.(webp|png)
```

> 💡 If you use **PMTiles**, replace `tiles/` with a single `overlay.pmtiles` and update `overlay.json`.

---

## 🧾 Machine-readable manifest (`overlay.json`)

The viewer should be able to render the overlay using **only** this manifest (plus the assets in this folder).

```json
{
  "id": "<overlay-id>",
  "title": "<Human-friendly title>",
  "description": "<1–3 sentences: what is it, why does it matter?>",
  "type": "raster-tiles",
  "projection": "EPSG:3857",
  "bounds": [-102.05, 36.99, -94.59, 40.00],
  "minZoom": 4,
  "maxZoom": 14,
  "tileSize": 256,
  "format": "webp",

  "tiles": ["./tiles/{z}/{x}/{y}.webp"],
  "pmtiles": null,

  "default": {
    "visible": false,
    "opacity": 0.75,
    "blendMode": "multiply"
  },

  "legend": {
    "type": "image",
    "src": "./legend.svg",
    "title": "<Legend title>"
  },

  "attribution": "<Required credit line (shown in-map)>",
  "license": {
    "spdx": "<SPDX-ID>",
    "url": "<license-url>"
  },

  "catalog": {
    "stac_item": "../../../../../data/stac/<overlay-id>.json",
    "dataset_record": "../../../../../data/catalog/<overlay-id>.json",
    "provenance": "../../../../../data/provenance/<overlay-id>.prov.jsonld"
  },

  "tags": ["kansas", "overlay", "<topic>"],

  "quality": {
    "georeferencing_rmse_m": "<number-or-null>",
    "known_issues": ["<optional>"]
  }
}
```

### ✅ Minimal required fields

- `id`, `title`, `type`, `bounds`, `minZoom`, `maxZoom`
- one of:
  - `tiles` (XYZ folder tiles), **or**
  - `pmtiles` (single-file tiles)
- `attribution` + `license`

---

## 🧩 Using this overlay in the web map

### MapLibre GL JS (raster tiles)

```js
map.addSource("<overlay-id>", {
  type: "raster",
  tiles: ["assets/maps/overlays/<overlay-id>/tiles/{z}/{x}/{y}.webp"],
  tileSize: 256,
  minzoom: 4,
  maxzoom: 14,
  bounds: [-102.05, 36.99, -94.59, 40.00]
});

map.addLayer({
  id: "<overlay-id>",
  type: "raster",
  source: "<overlay-id>",
  paint: {
    "raster-opacity": 0.75
  }
});
```

### Leaflet (XYZ tiles)

```js
L.tileLayer("assets/maps/overlays/<overlay-id>/tiles/{z}/{x}/{y}.webp", {
  opacity: 0.75,
  minZoom: 4,
  maxZoom: 14,
  bounds: L.latLngBounds([36.99, -102.05], [40.00, -94.59]),
  attribution: "<Required credit line>"
}).addTo(map);
```

> 🧠 Tip: Keep overlays **off by default** unless they’re lightweight and broadly useful.

---

## 🔎 Traceability & provenance (non‑negotiable)

This overlay must be traceable back to:

1. **Source material** (scans, datasets, URLs, archive IDs)
2. **Processing pipeline** (georeferencing, warps, color correction, tiling)
3. **Quality checks** (alignment, errors, limitations)

### Links to authoritative records

- 📚 Dataset record: `data/catalog/<overlay-id>.json`
- 🗂️ STAC item/collection: `data/stac/<overlay-id>.json`
- 🧬 Provenance bundle: `data/provenance/<overlay-id>.prov.jsonld`
- 🧪 Build log: `data/provenance/<overlay-id>.build.log` (optional)

> 🚫 If any of these are missing, the overlay is **not** “production‑ready” for KFM.

---

## 📚 Sources & citations

List **everything** a historian, scientist, or auditor would need to reproduce the overlay.

### Primary source(s)

- **Title:** `<…>`
- **Publisher / Archive:** `<…>`
- **Date:** `<…>`
- **Identifier:** `<call number / DOI / catalog id>`
- **URL:** `<…>`
- **License / Terms:** `<…>`
- **Notes:** `<e.g., scan resolution, page numbers, map sheet name>`

### Derived / supporting data (optional)

- `<gazetteer>`, `<boundary dataset>`, `<DEM>`, `<QA basemap>`, etc.

---

## ⚙️ Processing pipeline

> Keep this section specific to **this overlay**. Link scripts, parameters, and outputs.

1. 📥 **Acquire** source(s)
   - `data/raw/<...>`
2. 🧭 **Georeference**
   - GCPs: `<count>` | RMSE: `<m>` | method: `<thin plate spline / polynomial / …>`
3. 🧱 **Standardize formats**
   - raster → COG (`.tif`) / vector → GeoJSON
4. 🧩 **Generate web tiles**
   - XYZ tiles **or** PMTiles
5. ✅ **QA**
   - alignment vs. basemap, seam checks, nodata handling, min/max zoom sanity
6. 📦 **Publish**
   - copy assets into `web/assets/maps/overlays/<overlay-id>/`
   - update catalog + provenance records

<details>
<summary>🧪 Example “build command” block (replace with real commands)</summary>

```bash
# 1) Create/refresh the authoritative raster (COG)
python scripts/build_cog.py --in data/raw/<source>.tif --out data/processed/<overlay-id>.tif

# 2) Generate tiles for the web viewer
python scripts/build_tiles.py --in data/processed/<overlay-id>.tif \
  --out web/assets/maps/overlays/<overlay-id>/tiles \
  --minzoom 4 --maxzoom 14 --format webp --tile-size 256

# 3) Write/update metadata + provenance
python scripts/write_catalog_record.py --id <overlay-id>
python scripts/write_provenance.py --id <overlay-id>
```

</details>

---

## ✅ QA checklist

- [ ] Tiles load at all zooms in range (`minZoom`→`maxZoom`)
- [ ] No visible “tile seams” at typical zoom levels
- [ ] Overlay aligns with known control points / basemap (spot check ≥ 5 locations)
- [ ] Default opacity feels right (not washing out basemap)
- [ ] Legend matches symbology (if present)
- [ ] Attribution appears in the UI
- [ ] Catalog + provenance links resolve (no broken paths)
- [ ] License/terms verified and compatible with publication

---

## 📝 Changelog

| Date | Change | By |
|---|---|---|
| `<YYYY-MM-DD>` | Initial import | `@<handle>` |
| `<YYYY-MM-DD>` | Retiled at higher max zoom | `@<handle>` |

---

## 🆘 Troubleshooting

- **Tiles look “shifted”** → check CRS (must be Web Mercator tiling), confirm warp parameters and bounds.
- **Overlay is blurry** → verify max zoom + tile size; consider 512px tiles if appropriate.
- **Weird colors** → check gamma/color profile; ensure consistent preprocessing.
- **Repo size exploded** → consider PMTiles or store tiles with DVC/LFS and publish via CDN.

---

## 🤝 Maintainer notes

- Preferred contact: `@<handle>` / `<email or Discord>`
- Reviewers: `@<handle>`, `@<handle>`
- Related issue(s): `#<id>`