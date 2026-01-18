---
title: "🧊 3D Model Samples — README"
path: "web/assets/samples/3d/models/README.md"
version: "v1.0.0"
last_updated: "2026-01-17"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
pipeline_contract_version: "KFM-Pipeline-Contract v0.0.0"

governance_ref: "docs/governance/README.md"
security_ref: "SECURITY.md"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:assets:samples:3d:models:readme:v1.0.0"
commit_sha: "<set-at-merge>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

# 🧊 3D Model Samples

Small, well-documented **3D model fixtures** used by the KFM web UI for **demos, tests, and dev workflows** (WebGL/Three/Cesium/Map experiences).  
These assets are **not** “production content” and **must remain lightweight** and provenance-rich.

---

## ✅ What belongs here

- 🧪 **UI/Rendering fixtures** (known-good models for regression testing)
- 🧭 **Geospatial alignment demos** (models with clear origin/units/up-axis metadata)
- 🧰 **Performance baselines** (low/medium poly exemplars for FPS/VRAM checks)
- 🧱 **Material/lighting samples** (PBR materials, normal maps, transparency edge cases)

### 🚫 What does *not* belong here

- 🐘 Huge assets (put in LFS/external storage + reference via manifest)
- 🔒 Restricted / sensitive models (cultural heritage constraints, private locations, etc.)
- 🧑‍⚖️ Anything without clear license + attribution

---

## 📁 Recommended layout

> Keep it boring + predictable. One model = one folder.

```text
web/assets/samples/3d/models/
├─ README.md
├─ _meta/ 🧾
│  ├─ manifest.models.json            # registry for sample models
│  ├─ schema.model_meta.schema.json   # JSON schema for per-model meta
│  └─ thumbnails/                     # optional shared thumbs
├─ glb/ 🧊
│  ├─ <model_id>/
│  │  ├─ model.glb
│  │  ├─ preview.png
│  │  ├─ meta.json
│  │  └─ LICENSE.txt
│  └─ ...
├─ gltf/ 🧩
│  ├─ <model_id>/
│  │  ├─ scene.gltf
│  │  ├─ textures/
│  │  ├─ preview.png
│  │  ├─ meta.json
│  │  └─ LICENSE.txt
│  └─ ...
└─ tiles3d/ 🏙️
   ├─ <tileset_id>/
   │  ├─ tileset.json
   │  ├─ content/...
   │  ├─ preview.png
   │  ├─ meta.json
   │  └─ LICENSE.txt
   └─ ...
```

---

## 🧱 Supported formats (preferred order)

1. ✅ **GLB** (`.glb`) — preferred (single file, easy caching, simplest load path)
2. ✅ **glTF** (`.gltf` + textures) — acceptable when you need inspectable assets
3. ✅ **3D Tiles** (Cesium tilesets) — only for tileset-specific demos

> Prefer **meters** for units and keep **scale = 1.0** whenever possible.

---

## 🏷️ Naming & IDs

### Folder naming
- `kfm_<theme>_<variant>_<vNN>`  
  Examples:
  - `kfm_marker_poi_v01`
  - `kfm_building_blockout_v02`
  - `kfm_terrain_patch_v01`

### File naming (within a model folder)
- `model.glb` **or** `scene.gltf`
- `meta.json` (required)
- `preview.png` (required)
- `LICENSE.txt` (required if non-KFM-created)

---

## 🧾 Required per-model metadata (`meta.json`)

Each model **must** ship with a `meta.json` describing provenance, license, and runtime expectations.

```json
{
  "model_id": "kfm_marker_poi_v01",
  "title": "KFM POI Marker (Sample)",
  "description": "A small POI marker used for UI placement + picking tests.",
  "kind": "sample",
  "format": "glb",

  "source": {
    "type": "internal|external",
    "origin": "kfm|vendor|museum|author",
    "source_url": "https://example.invalid/replace-me",
    "retrieved_at": "2026-01-17"
  },

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Author Name / Organization",
    "attribution_url": "https://example.invalid/replace-me",
    "notes": "Any special requirements or constraints."
  },

  "geometry": {
    "units": "m",
    "up_axis": "Y",
    "approx_triangles": 1200,
    "bbox_local": { "min": [-0.5, 0.0, -0.5], "max": [0.5, 1.2, 0.5] }
  },

  "georeference": {
    "mode": "none|anchor|ecef|enu|tileset",
    "epsg": "EPSG:4326",
    "anchor": {
      "lon": -97.0,
      "lat": 38.5,
      "height_m": 0.0,
      "heading_deg": 0.0,
      "pitch_deg": 0.0,
      "roll_deg": 0.0
    }
  },

  "rendering": {
    "pbr": true,
    "transparent": false,
    "two_sided": false,
    "expected_fps_tier": "low|mid|high"
  },

  "integrity": {
    "sha256": "sha256:<to-be-filled>",
    "files": ["model.glb", "preview.png", "meta.json", "LICENSE.txt"]
  }
}
```

### Notes on georeferencing modes
- `none`: pure local-space sample (most common)
- `anchor`: single lat/lon/height anchor for demo placement
- `ecef`: absolute ECEF placement (advanced)
- `enu`: local tangent frame anchored at a lat/lon/height
- `tileset`: 3D Tiles semantics

---

## ⚡ Size & performance rules (fail-closed mindset)

- 📦 **Target size:** under **10–25 MB** per model folder (compressed)
- 🧮 Provide `approx_triangles` (estimate is fine)
- 🖼️ Include `preview.png` (fast browsing + docs)
- 🧹 Strip unused nodes/materials/textures before commit
- 🧪 Add at least one “edge case” model per category (transparency, normals, heavy textures)

---

## 🧑‍⚖️ Licensing & attribution (non-negotiable)

Every sample model must be:
- ✅ clearly licensed (SPDX where possible)
- ✅ attributable (who made it, where it came from)
- ✅ auditable (what was changed, when)

If **any** license terms conflict with repo policy, **do not add the asset**.

---

## 🧩 How the web app should consume these

### Option A: Read via manifest (preferred)
- `_meta/manifest.models.json` lists all available sample models for UI pickers + tests.
- UI can lazy-load thumbnails first, then fetch the model on demand.

### Option B: Direct import (fixtures only)
Hardcode a known test asset path in a unit/e2e test.

---

## 🧪 Example: minimal manifest entry (`_meta/manifest.models.json`)

```json
{
  "version": "v1",
  "updated_at": "2026-01-17",
  "models": [
    {
      "model_id": "kfm_marker_poi_v01",
      "format": "glb",
      "path": "web/assets/samples/3d/models/glb/kfm_marker_poi_v01/model.glb",
      "thumb": "web/assets/samples/3d/models/glb/kfm_marker_poi_v01/preview.png",
      "meta": "web/assets/samples/3d/models/glb/kfm_marker_poi_v01/meta.json",
      "tags": ["ui", "picking", "small"]
    }
  ]
}
```

---

## ➕ Adding a new sample model (checklist)

1. 🧊 Pick format (**GLB first**)
2. 🧹 Optimize (remove unused textures/materials, compress textures)
3. 🧾 Add `meta.json` + `preview.png` + `LICENSE.txt`
4. 🧪 Add a manifest entry
5. ✅ Run any asset lint / schema validation (if available)

---

## ✅ Definition of Done (DoD)

- [ ] Folder name follows conventions (`kfm_<theme>_<variant>_<vNN>`)
- [ ] `meta.json` present + valid (schema)
- [ ] `preview.png` present
- [ ] License + attribution included (`LICENSE.txt` or equivalent)
- [ ] Model loads in local dev (no console errors)
- [ ] Size/perf targets met (or explicitly justified)
- [ ] No sensitive content (CARE / sovereignty / privacy)

---

## 🔗 Related (nearby) sample assets

- `web/assets/samples/3d/` (root for other 3D fixtures)
- `web/assets/media/illustrations/` (2D/diagram assets)
- `web/assets/media/maps/` (map layers, legends, textures)

---
