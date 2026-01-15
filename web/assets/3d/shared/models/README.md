<div align="center">

# 🌄 Terrain Packs

**Static, provenance-aware terrain datasets for the Kansas Frontier Matrix (KFM) 3D viewer** 🗺️✨

![Viewer](https://img.shields.io/badge/viewer-CesiumJS-blue)
![Format](https://img.shields.io/badge/terrain-quantized--mesh%20%7C%203D%20Tiles-orange)
![Governance](https://img.shields.io/badge/governance-contract--first%20%2B%20provenance--first-success)
![Location](https://img.shields.io/badge/path-web%2Fassets%2F3d%2Fterrain%2Fpacks-informational)

</div>

---

## 🧭 What lives here?

This folder contains **terrain packs**: versioned bundles of **terrain/elevation data** (DEM/DTM-derived) that the web app can load as **static assets** for **fast 3D rendering** (especially in Cesium-based views) ⚡️.

Terrain packs are designed to be:

- ✅ **Drop-in**: Each pack is a self-contained folder.
- ✅ **Auditable**: Every pack ships with **metadata + provenance** (no “mystery terrain”).
- ✅ **Performant**: Packs can be **local (dev/offline)** or **mirrored to a CDN** for production.

---

## 🧩 How KFM uses terrain packs

Terrain packs are meant to support:

- 🌍 **3D globe / terrain views** (CesiumJS)
- 🧱 **3D Tiles streaming** (when terrain is represented as tiles or when paired with other 3D assets)
- 📖 **Story Nodes** that “fly” the camera over a landscape (ex: *Kansas From Above* style experiences)

> 🧠 Philosophy: KFM is *provenance-first* — terrain is treated like a first-class dataset with sources, licensing, and processing steps baked in.

---

## 🗂️ Folder layout (pack convention)

```text
📁 web/assets/3d/terrain/packs/
├─ 📄 README.md
└─ 📁 <pack-id>/                         # kebab-case ID recommended
   ├─ 🧾 pack.json                        # UI/loader-friendly manifest
   ├─ 🧾 contract.json                    # provenance + governance “data contract”
   ├─ 🖼️ preview.jpg                      # optional thumbnail for catalog / chooser UI
   ├─ 📄 LICENSE                          # optional (or point to license in contract.json)
   ├─ 📁 terrain/                         # Cesium quantized-mesh terrain (recommended)
   │  ├─ 🧾 layer.json
   │  └─ 📁 0/ 1/ 2/ ...                   # tile pyramid (implementation-specific)
   └─ 📁 tileset/                         # optional: 3D Tiles terrain/mesh
      ├─ 🧾 tileset.json
      └─ 🧱 tiles/ ...
```

---

## ✅ Required files

| File | Required | Purpose |
|------|----------|---------|
| `pack.json` | ✅ | Small manifest used by the **web app** to list/load packs |
| `contract.json` | ✅ | **Data contract**: provenance, license, processing steps, spatial metadata |
| `terrain/` or `tileset/` | ✅ | The actual terrain payload (choose at least one format) |
| `preview.*` | ⛳ Optional | Thumbnail for a terrain picker UI |
| `LICENSE` | ⛳ Optional | Helpful when packs are redistributed independently |

---

## 🧾 `pack.json` (manifest) — recommended shape

Keep this file **tiny** and “frontend-friendly”. It should answer: *what is this pack and where is the payload?*

<details>
<summary><strong>📄 Example <code>pack.json</code></strong></summary>

```json
{
  "id": "kansas-dem-10m",
  "title": "Kansas DEM (10m) 🌾",
  "description": "Statewide terrain derived from a public DEM source. Optimized for web 3D viewing.",
  "type": "cesium-terrain",
  "baseUrl": "./terrain/",
  "attribution": "See contract.json",
  "tags": ["kansas", "dem", "terrain", "statewide"],
  "recommended": true,

  "bounds": {
    "west": -102.0,
    "south": 36.9,
    "east": -94.6,
    "north": 40.0
  },

  "minZoom": 0,
  "maxZoom": 12
}
```

</details>

**Notes 📝**
- `baseUrl` should be **relative** so the pack works when served from `/assets/...`.
- `bounds` is strongly recommended for UI filtering + sanity checks.

---

## 🧾 `contract.json` (data contract) — provenance & governance 💡

KFM treats datasets as governed artifacts: **metadata is not optional**.

Your contract should make it possible to answer:

- Where did this terrain come from?
- What license governs it?
- What processing steps produced these tiles?
- What CRS / vertical datum / units apply?
- How can we verify integrity (hashes/checksums)?

<details>
<summary><strong>📄 Example <code>contract.json</code> (template)</strong></summary>

```json
{
  "kind": "kfm.data_contract",
  "contract_version": "1.0.0",

  "dataset": {
    "id": "kansas-dem-10m",
    "title": "Kansas DEM (10m)",
    "description": "Terrain tiles for 3D viewing. Derived from a statewide DEM source.",
    "theme": ["elevation", "terrain"],
    "created_utc": "2026-01-15T00:00:00Z"
  },

  "spatial": {
    "crs": "EPSG:4326",
    "vertical_datum": "UNKNOWN_OR_DECLARE_ME",
    "units": "meters",
    "bounds_wgs84": [-102.0, 36.9, -94.6, 40.0],
    "resolution": {
      "horizontal": "10m (nominal)",
      "vertical": "source-dependent"
    }
  },

  "source": {
    "name": "DECLARE_SOURCE_NAME",
    "publisher": "DECLARE_PUBLISHER",
    "download_url": "DECLARE_URL",
    "retrieved_utc": "DECLARE_UTC_TIMESTAMP",
    "license": {
      "name": "DECLARE_LICENSE_NAME",
      "url": "DECLARE_LICENSE_URL",
      "attribution": "DECLARE_ATTRIBUTION_TEXT"
    }
  },

  "processing": {
    "summary": "Reproject → clip to AOI → build tile pyramid → validate.",
    "steps": [
      {
        "name": "reproject",
        "tool": "gdalwarp",
        "params": {
          "dst_crs": "EPSG:4326"
        }
      },
      {
        "name": "build-terrain",
        "tool": "DECLARE_TERRAIN_BUILDER",
        "params": {
          "format": "quantized-mesh",
          "maxZoom": 12
        }
      }
    ]
  },

  "integrity": {
    "checksums": [
      { "path": "pack.json", "sha256": "DECLARE_SHA256" },
      { "path": "terrain/layer.json", "sha256": "DECLARE_SHA256" }
    ]
  },

  "contacts": [
    { "role": "maintainer", "name": "DECLARE_NAME", "email": "DECLARE_EMAIL" }
  ]
}
```

</details>

### 🔎 Contract “minimum bar”
A pack PR should be considered incomplete if `contract.json` does **not** include:
- ✅ `source` + license
- ✅ `processing.steps` (even if high-level)
- ✅ `spatial.crs` + `bounds_wgs84`

---

## 🧪 Loading a pack (typical patterns)

### A) Use as static assets (local/dev/offline) 🧑‍💻
If the web app is serving `web/` statically, packs will be available under something like:

```text
/assets/3d/terrain/packs/<pack-id>/...
```

**Pseudo-code (Cesium terrain provider):**
```ts
// Example intent only — use the Cesium API shape your codebase standardizes on.
const url = "/assets/3d/terrain/packs/kansas-dem-10m/terrain/";
viewer.terrainProvider = await Cesium.CesiumTerrainProvider.fromUrl(url);
```

### B) Serve heavy packs via CDN ☁️
If packs are huge, don’t commit them into the repo. Instead:
- publish the pack folder as a versioned artifact (release, object storage, CDN)
- keep a **small stub** in-repo (manifest + contract + preview) and point `baseUrl` to the CDN

---

## 📦 Size & performance guidance (please read)

Terrain data can get big fast 😅

- 🚫 **Avoid committing massive statewide high-zoom packs** directly into Git.
- ✅ Prefer **derived products** and **appropriate max zoom** for the intended experience.
- ✅ Use **LOD** wisely: lower-res terrain when zoomed out; increase detail only when needed.
- ✅ If/when packs are hosted externally, use **versioned URLs** (so caches don’t break story reproducibility).

---

## ✅ PR checklist for new packs

- [ ] Pack folder name is stable + kebab-case: `my-pack-id`
- [ ] `pack.json` exists and is minimal
- [ ] `contract.json` exists and includes **source + license + processing**
- [ ] Terrain payload is present (`terrain/` and/or `tileset/`)
- [ ] Bounds are correct (basic sanity check in 2D map)
- [ ] Preview image added (optional, but helpful)
- [ ] No sensitive/private data included
- [ ] Repo size impact considered (CDN/release artifact if needed)

---

## 🧯 Troubleshooting

**Terrain loads but looks “spiky” / wrong height**
- Likely a **vertical datum / unit mismatch** or a bad conversion step.
- Confirm the source DEM metadata and declare it in `contract.json`.

**Terrain is invisible**
- Check `baseUrl` paths and that `layer.json` / `tileset.json` is reachable.
- Check browser devtools for 404s.

**Terrain is shifted to the wrong place**
- CRS mismatch. Confirm `spatial.crs` and the conversion pipeline.

---

## 📚 Glossary (quick)

- **DEM**: Digital Elevation Model
- **DTM**: Digital Terrain Model (ground surface)
- **Quantized-mesh**: Cesium-friendly terrain tiling format
- **3D Tiles**: Streaming standard for 3D geospatial content (meshes, point clouds, etc.)
- **LOD**: Level of Detail (resolution varies by zoom)

---

## 🧠 Design principle reminder

> If a user can’t inspect a pack’s *source, license, and processing steps*, it doesn’t belong here. ✅
