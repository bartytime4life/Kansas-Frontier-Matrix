# 🪨 Monument Rocks (Chalk Pyramids) — 3D Landmark Pack (`kfm_0001`)

![KFM](https://img.shields.io/badge/KFM-Asset%20Pack-1f6feb?style=flat-square)
![Type](https://img.shields.io/badge/Type-3D%20Landmark-7c3aed?style=flat-square)
![Formats](https://img.shields.io/badge/Formats-GLB%20%7C%20glTF%20%7C%203D%20Tiles-0ea5e9?style=flat-square)
![Provenance](https://img.shields.io/badge/Provenance-Required-f97316?style=flat-square)

> [!IMPORTANT]
> This folder is a **provenance-first** 3D landmark “asset pack” for **Kansas Frontier Matrix (KFM)**.  
> ✅ Every mesh/texture must be traceable to a **source + license + processing notes**.

---

## 📌 Quick facts

| Key | Value |
|---|---|
| **KFM Asset ID** | `kfm_0001` |
| **Slug** | `monument-rocks` |
| **Folder** | `web/assets/3d/landmarks/monument-rocks__kfm_0001/` |
| **Type** | 🗺️ Landmark (natural feature) |
| **Location** | Gove County, Kansas, USA |
| **Center (WGS84)** | `lat 38.7905688`, `lon -100.7623657` *(approx.)* |
| **Approx. elevation** | `802 m` *(approx.)* |
| **Recommended primary deliverable** | `model.glb` ✅ |
| **Optional streaming deliverable** | `tileset/tileset.json` 🧩 (Cesium 3D Tiles) |

> [!NOTE]
> Monument Rocks is on **private property** in Kansas. The landowners allow visitors, but access rules can change—treat capture permissions as **required provenance**.

---

## 🧭 What this asset represents

Monument Rocks (“Chalk Pyramids”) are chalk formations in western Kansas. In KFM, this landmark is a prime candidate for “iconic site” storytelling in a 2D ↔ 3D demo flow (e.g., **Kansas From Above**).

---

## 🗂️ Folder contract

Below is the **recommended** contract for this landmark folder. If you deviate, document it here and in `kfm.asset.json`.

```text
📦 monument-rocks__kfm_0001/
├─ 📄 README.md                  # you are here ✅
├─ 🧾 kfm.asset.json             # REQUIRED: metadata + provenance + integrity
├─ 🖼️ preview.webp               # REQUIRED: 16:9 preview image (web-friendly)
│
├─ 🧱 model.glb                  # REQUIRED (unless using tileset/ instead)
├─ 🧱 model.glb.dvc              # OPTIONAL: if model is tracked via DVC (pointer file)
│
├─ 📁 textures/                  # OPTIONAL: only if textures not embedded in GLB
│  ├─ 🖼️ albedo.webp
│  ├─ 🖼️ normal.webp
│  └─ 🖼️ orm.webp                # packed Occlusion/Roughness/Metallic
│
├─ 📁 tileset/                   # OPTIONAL: Cesium 3D Tiles output
│  ├─ 🧩 tileset.json
│  └─ 📁 tiles/
│     └─ ...
│
└─ 📁 sources/                   # REQUIRED: human-readable provenance trail
   ├─ 📄 SOURCES.md              # where did it come from? ✅
   ├─ 📄 CAPTURE_NOTES.md        # how was it captured? ✅
   ├─ 📄 PROCESSING_NOTES.md     # how was it processed/optimized? ✅
   └─ 📁 licenses/               # retain source licenses/terms ✅
      ├─ 📄 SOURCE_LICENSES.md
      └─ 📄 MODEL_LICENSE.txt
```

✅ **Default preference:** embed textures inside `model.glb` for simpler static hosting.  
🧩 **Use `tileset/`** when you need streaming + LOD (especially in Cesium scenes).

---

## 🌐 How the web app should load this asset

### Static URL (expected)
Because this lives under `web/assets/...`, it should be available to the front-end as:

```text
/assets/3d/landmarks/monument-rocks__kfm_0001/model.glb
```

### Story node / scene config (pseudo-example)
Adapt this to the current story schema, but keep the essentials: **id + uri + WGS84 placement**.

```json
{
  "id": "landmark.kfm_0001",
  "title": "Monument Rocks (Chalk Pyramids)",
  "mode": "3d",
  "model": {
    "uri": "/assets/3d/landmarks/monument-rocks__kfm_0001/model.glb",
    "wgs84": { "lon": -100.7623657, "lat": 38.7905688, "height_m": 0 },
    "scale": 1.0
  }
}
```

### CesiumJS snippet (pseudo-example)
```ts
// Pseudo-code — adapt to the KFM Cesium wrapper.
const url = "/assets/3d/landmarks/monument-rocks__kfm_0001/model.glb";

const position = Cesium.Cartesian3.fromDegrees(
  -100.7623657, // lon
  38.7905688,   // lat
  0             // height meters
);

viewer.entities.add({
  name: "Monument Rocks (kfm_0001)",
  position,
  model: {
    uri: url,
    minimumPixelSize: 64
  }
});
```

---

## 🧾 `kfm.asset.json` contract (required)

This JSON is the **canonical truth** for:
- 🔎 search + indexing
- 🧬 provenance
- ✅ integrity checks
- 🧩 runtime configuration (what to load)

### Minimum required fields
- `kfm_id`, `slug`, `title`, `type`
- `location.center_wgs84` *(lon/lat)*
- `license` *(prefer SPDX)*
- `provenance.sources[]` *(each with license + access date)*
- `provenance.processing[]` *(tools + versions + steps)*
- `integrity.hashes` *(sha256 strongly recommended)*

### Example scaffold
```json
{
  "kfm_id": "kfm_0001",
  "slug": "monument-rocks",
  "title": "Monument Rocks (Chalk Pyramids)",
  "type": "landmark",
  "location": {
    "country": "US",
    "state": "KS",
    "county": "Gove",
    "center_wgs84": { "lon": -100.7623657, "lat": 38.7905688 },
    "elevation_m_approx": 802
  },
  "deliverables": {
    "primary": { "kind": "glb", "path": "model.glb" },
    "preview": { "kind": "image", "path": "preview.webp" },
    "optional": [
      { "kind": "3d-tiles", "path": "tileset/tileset.json" }
    ]
  },
  "license": "TBD",
  "provenance": {
    "sources": [
      {
        "name": "TODO: capture dataset / scan / photogrammetry inputs",
        "type": "capture",
        "license": "TBD",
        "notes": "Add links/paths + permissions here."
      }
    ],
    "processing": [
      {
        "step": "TODO: mesh cleanup + decimation",
        "tools": [
          { "name": "Blender", "version": "TBD" }
        ]
      },
      {
        "step": "TODO: export + compression",
        "tools": [
          { "name": "gltf-transform", "version": "TBD" }
        ]
      }
    ]
  },
  "integrity": {
    "hashes": {
      "model.glb": "sha256:TODO",
      "preview.webp": "sha256:TODO"
    }
  },
  "updated_at": "YYYY-MM-DD"
}
```

### Generate SHA-256 hashes
```bash
# from this folder:
shasum -a 256 model.glb preview.webp
```

---

## 🧾 Provenance & licensing checklist ✅

- [ ] **Capture permission** confirmed (📍 private land)
- [ ] Source materials listed in `sources/SOURCES.md`
- [ ] License(s) compatible with KFM distribution policy
- [ ] Attribution text included (human-readable)
- [ ] No personal data in textures/metadata (faces/plates/etc.)
- [ ] No encouragement of fossil collecting or site damage (educational framing only)

---

## ⚡ Performance budgets (web + 3D)

Targets (tune per scene importance):

- 🧱 **Triangles:** ≤ 150k (hero) / ≤ 50k (standard)
- 🧵 **Textures:** prefer 2K; avoid >4K unless justified
- 🗜️ **Compression:** meshopt/Draco encouraged *(document which one)*
- 🧊 **Texture formats:** WebP for static; KTX2/BasisU if supported

---

## ✅ QA smoke test

- [ ] Loads in a clean browser session (no cache)
- [ ] Scale reads as meters (no “giant” or “tiny” landmark)
- [ ] Up-axis + orientation correct (no unexpected flip)
- [ ] No missing textures (watch console + network)
- [ ] Bounding volume reasonable (camera frames it)
- [ ] Works in 2D → 3D transitions (if used in story mode)

---

## 📚 Context references (non-capture)

These are **for factual context / UI copy**, not a substitute for capture provenance:

- GeoKansas (Kansas Geological Survey): `https://geokansas.ku.edu/monument-rocks`
- GeoKansas gallery: `https://geokansas.ku.edu/monument-rocks-gallery`
- USGS-style coordinate listing: `https://www.topozone.com/kansas/gove-ks/park/monument-rocks-national-natural-landmark/`

---

## 🧩 Change log

| Date | Change | By |
|---|---|---|
| YYYY-MM-DD | Initial `kfm_0001` scaffold | @you |
