# 🗺️ Shared Map Overlays (`_shared`)

![KFM](https://img.shields.io/badge/KFM-Maps%20%26%20Overlays-0b7285)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20Viewer-1f6feb)
![Cesium](https://img.shields.io/badge/Cesium-3D%20Viewer-6f42c1)
![GeoJSON](https://img.shields.io/badge/GeoJSON-Vector%20Data-2ea043)
![Provenance](https://img.shields.io/badge/Provenance-No%20Mystery%20Layers-f85149)

> 📌 **Purpose:** this folder holds **small, reusable map overlays** that ship with the web client and are used across multiple pages/stories (context boundaries, masks, UI affordances, small annotation layers, etc.).

---

## 🧭 Where this fits in KFM

KFM’s web UI is built around interactive map viewers (2D + 3D) with a **layer list/catalog**, legends, and story-driven map state. Shared overlays are the *tiny, always-available building blocks* used by those viewers and stories.

✅ **Use `_shared` when:**
- The overlay is **static**, **small**, and **reused** in multiple places.
- It’s **UI context** (e.g., outlines, grids, masks), not a full dataset product.
- Shipping it with the web bundle makes sense (fast load, no API call required).

🚫 **Don’t use `_shared` when:**
- The overlay is **large** (big geometry, many features) or needs tiling.
- The overlay is **time-varying** / query-driven.
- It’s an **official curated dataset output** → that belongs in `data/processed/` with metadata in `data/catalog/` (and provenance).

---

## 📌 Table of Contents

- [🗂️ Folder conventions](#️-folder-conventions)
- [🏷️ Naming rules](#️-naming-rules)
- [📦 Supported formats](#-supported-formats)
- [🌍 CRS rules](#-crs-rules)
- [🧾 Overlay metadata contract](#-overlay-metadata-contract)
- [🧑‍🔧 Add a new shared overlay](#-add-a-new-shared-overlay)
- [🧪 QA checklist](#-qa-checklist)
- [♿ Cartography & accessibility](#-cartography--accessibility)
- [🧩 Usage examples](#-usage-examples)
- [🔐 Attribution & licensing](#-attribution--licensing)

---

## 🗂️ Folder conventions

**Expected shape (examples):**

```text
📁 web/assets/maps/overlays/
  ├─ 📁 _shared/
  │  ├─ 📄 README.md  ✅ (this file)
  │  ├─ 🗺️ ks_state_outline.geojson
  │  ├─ 🧾 ks_state_outline.overlay.json
  │  ├─ 🗺️ us_plss_grid_simplified.topo.json
  │  ├─ 🧾 us_plss_grid_simplified.overlay.json
  │  └─ 🖼️ vignette_mask.png
  │     🧾 vignette_mask.overlay.json
  └─ 📁 <story_id>/        (story-specific overlays live next to the story)
     ├─ 🗺️ <story_id>_annotations.geojson
     └─ 🧾 <story_id>_annotations.overlay.json
```

> 💡 **Rule of thumb:** `_shared` should stay **boring + lightweight**. If you’re debating whether something is “too big,” it probably is.

---

## 🏷️ Naming rules

Keep filenames predictable so we can register/scan overlays automatically.

✅ **Recommended file naming:**
- `lower_snake_case`
- `topic + intent + variant` (when needed)
- One overlay = one stable ID

Examples:
- `ks_state_outline.geojson`
- `ks_county_outlines_simplified.geojson`
- `historic_map_frame_mask.png`

✅ **Sidecar metadata file naming:**
- `same_basename.overlay.json`

Examples:
- `ks_state_outline.overlay.json`
- `historic_map_frame_mask.overlay.json`

---

## 📦 Supported formats

| Format | Best for | Notes |
|---|---|---|
| **GeoJSON** (`.geojson`) | small vector overlays (points/lines/polygons) | easiest to author + debug |
| **TopoJSON** (`.topo.json`) | medium-small vectors where size matters | good for shared boundaries/grids |
| **PNG** (`.png`) | masks, soft overlays, image UI affordances | must support transparency |
| **SVG** (`.svg`) | icons / lightweight shapes | avoid complex, heavy SVG paths |
| **Vector tiles** (`.mvt`) | **NOT** stored here | should be served via tile endpoints when heavy |

> 🚀 For heavy/static vectors (roads, rivers, dense polygons): generate **vector tiles** and serve them via a tile endpoint. `_shared` should reference them via metadata, not embed the dataset.

---

## 🌍 CRS rules

🎯 **Display standard:** `WGS84 / EPSG:4326` (lat/lon).

✅ Requirements:
- All committed GeoJSON/TopoJSON overlays in `_shared` **must be EPSG:4326**.
- If you authored in a different CRS (State Plane / Lambert / etc.), **reproject before committing**.
- Always record the **original CRS** and transformation steps in the overlay’s metadata (see below).

---

## 🧾 Overlay metadata contract

### Why metadata is non-negotiable 🧠
KFM’s architecture treats map layers as governed artifacts: **license**, **source attribution**, **spatial/temporal extent**, and **lineage** should never be a mystery.

### Required: `*.overlay.json`

Each overlay MUST have a matching sidecar JSON file with:

✅ **Minimum fields**
- `id` (stable string)
- `title`
- `description`
- `type` (`vector` | `raster`)
- `format` (`geojson` | `topojson` | `png` | `svg` | `tilejson` | etc.)
- `crs` (expected display CRS: `EPSG:4326`)
- `bbox` (WGS84 bbox)
- `license`
- `attribution` (human-readable)
- `sources[]` (where it came from)
- `provenance` (how it was made)

### Minimal template (copy/paste)

```json
{
  "id": "ks_state_outline",
  "title": "Kansas State Outline",
  "description": "Lightweight outline used for context and focus framing in multiple views.",
  "type": "vector",
  "format": "geojson",
  "file": "ks_state_outline.geojson",

  "crs": "EPSG:4326",
  "bbox": [-102.05, 36.99, -94.59, 40.00],

  "license": "CC-BY-4.0 OR Public Domain (verify!)",
  "attribution": "Source: <org/name>. Derived/processed by KFM.",

  "sources": [
    {
      "name": "Original dataset name",
      "publisher": "Publisher / archive / agency",
      "url": "https://example.org/source",
      "accessed": "YYYY-MM-DD",
      "license": "License string or URL"
    }
  ],

  "provenance": {
    "created_by": "your-name-or-handle",
    "created_at": "YYYY-MM-DD",
    "method": "manual|pipeline",
    "pipeline_ref": "pipelines/<...> (if applicable)",
    "inputs": [
      "data/sources/<manifest>.json (if applicable)"
    ],
    "notes": "Simplified geometry, reprojected to EPSG:4326 for web display."
  },

  "display": {
    "defaultVisible": false,
    "defaultOpacity": 0.8,
    "minZoom": 4,
    "maxZoom": 14,
    "legendLabel": "Kansas outline"
  }
}
```

> 🧩 Optional but encouraged: include a `catalog_ref` pointing to the official dataset entry in `data/catalog/` if this overlay corresponds to a curated pipeline output.

---

## 🧑‍🔧 Add a new shared overlay

1) **Decide placement** 🧭  
   - Small + shared + static → `_shared/`  
   - Big/heavy → tiles (API) + register as dataset layer  
   - Story-only → `overlays/<story_id>/`

2) **Author the overlay** ✍️  
   - QGIS/GeoPandas/etc.
   - Simplify geometry (keep visual intent; remove excess vertices).
   - Reproject to **EPSG:4326**.

3) **Export + commit** ✅  
   - Add the overlay file (`.geojson`, `.topo.json`, `.png`, etc.)
   - Add the matching `*.overlay.json`

4) **Register in the UI** 🧩  
   - Add it to the layer registry / story config / viewer config (wherever overlays are enumerated in the web app).

5) **Run validation** 🧪  
   - Validate geometry, required metadata fields, and licensing.

---

## 🧪 QA checklist

Before merging, confirm:

- [ ] File is in **EPSG:4326** (vector overlays)
- [ ] Overlay loads at the correct place (no offset / mirroring)
- [ ] Geometry is valid (no self-intersections / broken rings)
- [ ] Size is reasonable (avoid shipping megabytes in `web/assets/`)
- [ ] Sidecar metadata exists (`*.overlay.json`)
- [ ] Metadata includes **license + attribution + source**
- [ ] Provenance notes explain how the overlay was produced
- [ ] Styling is legible and doesn’t overwhelm basemap/story layers
- [ ] Works in both desktop + mobile layouts (no tiny hit targets)

> 🔍 Tip: consider adding an automated “overlay QA” check alongside catalog QA so broken metadata can’t sneak in.

---

## ♿ Cartography & accessibility

KFM’s map UI aims for clarity and inclusion:

- 🧭 Prefer intuitive symbology and avoid clutter.
- 🌓 Ensure overlays remain readable in **high-contrast** or alternate themes.
- 🏷️ If an overlay is toggleable, ensure it has a meaningful legend label + description.
- 🧑‍🦯 UI controls that expose overlays should be screen-reader friendly (semantic labels, ARIA where appropriate).

---

## 🧩 Usage examples

<details>
<summary><strong>🗺️ MapLibre (GeoJSON overlay)</strong></summary>

```js
// Example only — adapt to your project’s map loader / registry
map.addSource("ks_state_outline", {
  type: "geojson",
  data: "/assets/maps/overlays/_shared/ks_state_outline.geojson"
});

map.addLayer({
  id: "ks_state_outline",
  type: "line",
  source: "ks_state_outline",
  paint: {
    "line-width": 2
  }
});
```

</details>

<details>
<summary><strong>🌍 Cesium (GeoJSON overlay)</strong></summary>

```js
// Example only — adapt to your Cesium viewer wiring
const ds = await Cesium.GeoJsonDataSource.load(
  "/assets/maps/overlays/_shared/ks_state_outline.geojson",
  { clampToGround: true }
);

viewer.dataSources.add(ds);
```

</details>

<details>
<summary><strong>🧱 Suggested lifecycle (Mermaid)</strong></summary>

```mermaid
flowchart LR
  A[📥 Source archive / agency] --> B[🛠️ Pipelines / tooling]
  B --> C[🗄️ data/processed/]
  C --> D[🗂️ data/catalog/ + provenance]
  D --> E[🌐 API / tiles / layer registry]
  E --> F[🖥️ Web viewer (MapLibre/Cesium)]
  B --> G[🧩 web/assets/.../_shared (only small overlays)]
  G --> F
```

</details>

---

## 🔐 Attribution & licensing

Every overlay must be shippable and redistributable:

- ✅ Include a **license** and **attribution** in the sidecar metadata.
- ✅ If derived from third-party data, ensure the license allows redistribution.
- ✅ If uncertain: **don’t merge** until clarified.

---

## 🧾 Maintenance notes

- Keep `_shared` lean: if it grows beyond “small utilities,” migrate heavy layers to a tiled workflow.
- Prefer **derivable overlays**: when possible, build overlays from curated datasets/pipelines so they remain reproducible.

---