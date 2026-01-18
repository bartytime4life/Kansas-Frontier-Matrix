<!-- Path: web/assets/samples/tiles/<tileset-id>/README.md -->

# 🧱 Sample Tileset: `<tileset-id>`

![KFM](https://img.shields.io/badge/KFM-provenance--first-blue)
![tiles](https://img.shields.io/badge/tiles-sample-orange)
![scheme](https://img.shields.io/badge/scheme-XYZ-lightgrey)
![web](https://img.shields.io/badge/web-MapLibre%20ready-6aa84f)

A **small, repo-safe tileset** intended for **development/demo** use in the KFM `web/` app (ex: MapLibre viewer).  
This folder lives under `web/assets/…` so it can be served as **static files** during local dev and simple deploys.

> [!IMPORTANT]
> ✅ Samples are allowed to live in `web/assets/…` for convenience.  
> 🧾 If this is meant to become an **official layer**, it should graduate into the governed pipeline (contracts/catalogs/provenance) and be served via the platform’s normal data interfaces.

---

<details>
  <summary><strong>📌 Table of contents</strong></summary>

- 🧭 Overview
- 🗂️ Folder layout
- ⚡ Quick start (MapLibre)
- 🧾 Tileset metadata (contract)
- 🔎 Provenance & attribution checklist
- 🧪 QA / sanity checks
- 🔁 Regeneration notes
- 🧾 Changelog

</details>

---

## 🧭 Overview

**Tileset ID:** `<tileset-id>`  
**What it shows:** _TODO: one sentence describing the map layer_  
**Intended use:** UI dev, story/node demos, offline-ish demos, screenshots, automated tests  
**Not intended for:** production serving, authoritative catalog publishing, high-zoom detail

### ✅ Quick facts

| Field | Value |
|---|---|
| Type | `vector` \| `raster` |
| Tile format | `.pbf` (vector) \| `.png`/`.webp`/`.jpg` (raster) |
| Tile scheme | `XYZ` (`{z}/{x}/{y}`) |
| Min zoom | `__` |
| Max zoom | `__` |
| Bounds (WGS84) | `[west, south, east, north] = [__, __, __, __]` |
| License for derived tiles | `__` |
| Required attribution | `__` |

---

## 🗂️ Folder layout

Recommended structure (keep it predictable 🧠):

```text
📦 <tileset-id>/
├─ 📄 README.md
├─ 🧾 tileset.contract.json        # ✅ required: metadata/provenance contract for this tileset
├─ 🧾 tilejson.json                # (optional) TileJSON helper for tools/viewers
├─ 🖼️ preview.png                  # (recommended) quick visual check
├─ 🧾 attribution.md               # (optional) verbose attribution + license text
└─ 🧱 tiles/
   └─ {z}/{x}/{y}.{ext}            # XYZ tiles (ext = pbf | png | webp | jpg)
```

> [!TIP]
> Keep sample tiles **small** (tight bounds + limited zooms). If you need “big data”, point the UI at a real tile endpoint instead.

---

## ⚡ Quick start (MapLibre)

### 🧩 Vector tiles example (`.pbf`)

```js
// Example: add a vector source backed by static sample tiles
map.addSource("<tileset-id>", {
  type: "vector",
  tiles: [
    "/assets/samples/tiles/<tileset-id>/tiles/{z}/{x}/{y}.pbf"
  ],
  minzoom: /* __ */,
  maxzoom: /* __ */,
  attribution: "TODO: required attribution string"
});

// Example: add a layer (you MUST know the source-layer name inside the PBF)
map.addLayer({
  id: "<tileset-id>-fill",
  type: "fill",
  source: "<tileset-id>",
  "source-layer": "TODO_SOURCE_LAYER_NAME",
  paint: {
    // TODO styling
  }
});
```

### 🖼️ Raster tiles example (`.png/.webp/.jpg`)

```js
map.addSource("<tileset-id>", {
  type: "raster",
  tiles: [
    "/assets/samples/tiles/<tileset-id>/tiles/{z}/{x}/{y}.png"
  ],
  tileSize: 256,
  minzoom: /* __ */,
  maxzoom: /* __ */,
  attribution: "TODO: required attribution string"
});

map.addLayer({
  id: "<tileset-id>-raster",
  type: "raster",
  source: "<tileset-id>"
});
```

---

## 🧾 Tileset metadata (contract)

KFM treats **metadata + lineage** as first-class. Even for samples, we want a minimal “contract” so nothing becomes a mystery layer later.

Create (or update) this file:

📄 `tileset.contract.json`

Suggested shape (edit freely, but keep the spirit ✅):

```json
{
  "id": "<tileset-id>",
  "title": "TODO: human-readable title",
  "description": "TODO: 1–3 sentences (what/why/limits)",

  "role": "sample",
  "type": "vector",
  "format": "pbf",
  "scheme": "xyz",

  "minzoom": 0,
  "maxzoom": 10,
  "bounds_wgs84": [-102.05, 36.99, -94.59, 40.00],

  "source": [
    {
      "name": "TODO: source dataset name",
      "publisher": "TODO",
      "license": "TODO (SPDX if possible)",
      "url": "TODO",
      "retrieved_at": "YYYY-MM-DD"
    }
  ],

  "processing": [
    {
      "step": 1,
      "summary": "TODO: reproject/clean/simplify/clip",
      "tool": "TODO (ex: tippecanoe, gdal, ogr2ogr)",
      "command": "TODO (optional)",
      "notes": "TODO"
    }
  ],

  "projections": {
    "original": "TODO: EPSG:____",
    "served": "TODO: web-friendly CRS/assumptions"
  },

  "attribution": {
    "required": "TODO: short attribution string for UI",
    "full_text_path": "./attribution.md"
  },

  "maintainers": [
    "TODO: @github-handle"
  ],

  "generated_at": "YYYY-MM-DD",
  "version": "0.1.0"
}
```

> [!NOTE]
> If the source’s license requires a **specific attribution string**, copy it verbatim into `attribution.required`.

---

## 🔎 Provenance & attribution checklist ✅

Before merging tiles into `web/assets/…`:

- [ ] ✅ **Source is public / shareable** (and allowed to be redistributed)
- [ ] ✅ **License is recorded** (prefer SPDX identifiers)
- [ ] ✅ **Attribution is included** (UI-ready short string + optional full text)
- [ ] ✅ **Processing steps are documented** (clip/simplify/reproject/generalize)
- [ ] ✅ **Spatial extent & zoom range are documented**
- [ ] ✅ **No sensitive / private data** in sample tiles
- [ ] ✅ A `preview.png` exists (fast sanity check)

---

## 🧪 QA / sanity checks

### 🧭 Visual smoke test
- Load the tileset in the map viewer.
- Pan/zoom around bounds.
- Confirm: no “tile seams”, no weird offsets, styling behaves.

### 🧰 Developer sanity checks (optional)
- Verify directory has expected `{z}/{x}/{y}` coverage for the declared zoom range.
- Confirm file extensions match `type/format`.
- Confirm attribution renders somewhere in the UI when the layer is enabled.

---

## 🔁 Regeneration notes

This tileset is a **derived artifact**. If you regenerate it:

1. Keep the **same `id`** (unless it’s fundamentally a new dataset)
2. Update:
   - `tileset.contract.json -> generated_at`
   - `tileset.contract.json -> processing[]` (add a new step or revise)
   - `version`
3. Replace tiles in `tiles/…` (or adjust bounds/zooms if needed)
4. Refresh `preview.png`

> [!TIP]
> For heavy layers, consider generating tiles in the pipeline and serving them via tile endpoints instead of committing large tile folders into the web bundle.

---

## 🧾 Changelog

- `0.1.0` — Initial sample publish (TODO: date)
- `0.1.1` — TODO
