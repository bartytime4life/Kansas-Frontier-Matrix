# 🧾 Shared 3D Asset Metadata (`web/assets/3d/shared/meta/`)

![Contract-First](https://img.shields.io/badge/Contract--First-%E2%9C%85-blue)
![Provenance-First](https://img.shields.io/badge/Provenance--First-%F0%9F%94%8D-success)
![CRS](https://img.shields.io/badge/CRS-EPSG%3A4326%20(WGS84)-informational)
![3D](https://img.shields.io/badge/3D-glTF%20%7C%203D%20Tiles-purple)

> This folder is the **shared, UI-friendly metadata layer** for 3D assets (models + tilesets) used across the web app.  
> Goal: **zero “mystery models”** ✅ — every 3D thing we render must be attributable, governed, and linkable to evidence.

---

## 📌 What lives here

**This directory contains** small **JSON “meta manifests”** that the Web UI can load quickly to:
- show a friendly title/summary 🏷️
- power search/filter tags 🔎
- set initial camera/lighting hints 🎥
- define how to load the asset (local path vs. remote URL) 🌐
- link back to canonical catalogs/provenance (STAC/DCAT/PROV) 🔗

Think: *“runtime manifest / UI contract”* — not *“the one true dataset record.”*

---

## 🚫 What does **not** live here

- ❌ The canonical dataset record (that belongs in the governed catalogs)
- ❌ Unattributed models (“found it online” doesn’t ship)
- ❌ Private/restricted assets in a public build
- ❌ Huge binaries by default (prefer streaming / external hosting)

---

## 🗂️ Expected neighborhood

This README documents `meta/` specifically, but it’s meant to work alongside a shared 3D asset layout like:

```text
web/assets/3d/
  shared/
    meta/          🧾 JSON manifests (this folder)
    models/        🧱 small glTF/GLB assets (optional)
    tilesets/      🧊 Cesium 3D Tiles roots (optional)
    thumbnails/    🖼️ preview images (optional)
    materials/     🎨 shared textures/material refs (optional)
```

> If the repo structure differs, keep the *principle* the same: **meta files are stable pointers + UI hints**, not the authoritative evidence store.

---

## 🧠 How the UI uses these manifests

The front-end (React) can render:
- **2D** via MapLibre (default)
- **3D** via Cesium (opt-in / when needed)

These `meta/*.json` files help the UI decide:
- which viewer to use (MapLibre-only vs. Cesium)
- what to load (glTF vs. 3D Tiles)
- how to frame the scene (camera defaults)
- what to display in the “info” panel (credits/licensing)

---

## 🧩 Core invariants (don’t break these)

✅ **Contract-first:** every asset has a machine-readable manifest  
✅ **Provenance-first:** every asset links to evidence + lineage  
✅ **No leapfrogging:** UI must not invent data that bypasses catalogs  
✅ **Geo-consistent:** location is expressed in WGS84/EPSG:4326 for display  
✅ **Governed visibility:** restrictions propagate (no public exposure by accident)

---

## 📄 Metadata contract (JSON)

### ✅ Minimal required fields

| Field | Type | Why |
|------|------|-----|
| `id` | `string` | Stable reference key used by UI + stories |
| `title` | `string` | Human-readable display name |
| `kind` | `"gltf"` \| `"3d-tiles"` \| `"czml"` \| `"kml"` | Loader + viewer routing |
| `summary` | `string` | Short description for panels/search |
| `license` | `string` | License/SPDX-ish identifier or project license key |
| `attribution` | `string[]` | Credits shown in UI (human-readable) |
| `spatial` | `object` | Bounding + placement in WGS84 |
| `assets` | `object` | Where the actual 3D content lives |
| `links` | `object` | References to governed catalogs / provenance |

---

### 🧭 Spatial object (recommended shape)

```json
{
  "crs_display": "EPSG:4326",
  "bbox_wgs84": [-101.95, 38.70, -101.94, 38.71],
  "anchor": { "lng": -101.945, "lat": 38.705, "height_m": 0 },
  "units": { "elevation": "m" }
}
```

Notes:
- `bbox_wgs84` is `[minLng, minLat, maxLng, maxLat]` 🌍  
- `anchor.height_m` is meters by default (keep it boring + consistent) 📏

---

### 🧱 Asset loaders by `kind`

| kind | Required `assets` keys | Typical use |
|------|-------------------------|-------------|
| `gltf` | `model` | Small/medium objects (GLB/GLTF) |
| `3d-tiles` | `tileset` | Large streaming content (LiDAR point clouds, buildings) |
| `czml` | `czml` | Time-dynamic entities in Cesium |
| `kml` | `kml` | Lightweight geospatial overlays |

---

### 🔗 Links object (the “evidence hooks”)

This is where we connect UI-facing manifests back to governed metadata:

```json
{
  "stac_item": "stac-item-id-or-url",
  "dcat_dataset": "dcat-id-or-url",
  "prov": "prov-bundle-id-or-url",
  "source_landing_page": "https://example.org/dataset"
}
```

✅ Prefer **stable IDs** or **API URLs**.  
✅ If your build is static/offline, these can be relative paths to checked-in catalog artifacts.

---

## 🧪 Example manifest (copy/paste starter)

<details>
<summary><strong>📦 Example: <code>monument-rocks.json</code></strong></summary>

```json
{
  "id": "kfm-3d-monument-rocks",
  "title": "Monument Rocks (3D)",
  "summary": "A 3D landmark model for story transitions and terrain-context scenes.",
  "kind": "gltf",

  "tags": ["landmark", "geology", "story-node"],

  "license": "CC-BY-4.0",
  "attribution": [
    "Source: <ORG/ARCHIVE NAME>",
    "Processed by: KFM pipeline (see provenance)"
  ],

  "spatial": {
    "crs_display": "EPSG:4326",
    "bbox_wgs84": [-101.9500, 38.7000, -101.9400, 38.7100],
    "anchor": { "lng": -101.9450, "lat": 38.7050, "height_m": 0 },
    "units": { "elevation": "m" }
  },

  "assets": {
    "model": "../models/monument-rocks/model.glb",
    "thumbnail": "../thumbnails/monument-rocks.jpg"
  },

  "viewer": {
    "engine": "cesium",
    "initial_camera": {
      "lng": -101.9450,
      "lat": 38.7050,
      "height_m": 350,
      "heading_deg": 25,
      "pitch_deg": -30
    }
  },

  "links": {
    "stac_item": "<STAC_ITEM_ID_OR_URL>",
    "dcat_dataset": "<DCAT_DATASET_ID_OR_URL>",
    "prov": "<PROV_BUNDLE_ID_OR_URL>",
    "source_landing_page": "<PUBLIC_DATASET_PAGE>"
  }
}
```
</details>

---

## ✅ Validation checklist (Definition of Done)

Before merging a new/updated 3D asset manifest:

- [ ] **Attribution present** (human-readable credits)
- [ ] **License declared**
- [ ] **Spatial is sane** (`bbox_wgs84` valid, `anchor` within bbox)
- [ ] **Asset paths resolve** (or URLs are reachable in target environment)
- [ ] **Links present** to STAC/DCAT/PROV (or documented exception)
- [ ] **No restricted content** accidentally routed to a public build
- [ ] **Performance sanity**: prefer streaming (3D Tiles) for large assets 🧊

---

## 🧊 3D Tiles guidance (when to use)

Use **3D Tiles** when:
- the dataset is huge (point clouds, dense city/building meshes)
- you need progressive loading while zooming
- you want Cesium-native streaming behavior

Keep `meta/` lightweight; point `assets.tileset` to:
- a local `tileset.json` (only if small enough)
- or a hosted `tileset.json` endpoint (preferred for big content)

---

## 🔒 Governance & safety notes

If a source dataset is sensitive/restricted:
- mark it as such in the canonical metadata
- ensure any derived 3D assets inherit the restriction level
- avoid shipping those assets into public `web/` builds

> When in doubt: treat “web assets” as public-by-default, and route sensitive content through governed APIs instead.

---

## 🔗 Helpful project references

These are the **canonical** docs that define governance, catalogs, and contracts:

- 📘 `docs/MASTER_GUIDE_v13.md`
- 🧭 `docs/standards/` (STAC/DCAT/PROV profiles)
- 🧬 `data/stac/` + `data/catalog/dcat/` + `data/prov/` (governed metadata artifacts)

*(Links are intentionally relative-to-repo-root; adjust if your directory layout differs.)*
