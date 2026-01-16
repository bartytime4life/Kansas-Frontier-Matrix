# 🪨 Monument Rocks (Chalk Pyramids) — 3D Model

![Asset](https://img.shields.io/badge/asset-3D%20model-7b2cbf)
![Format](https://img.shields.io/badge/format-glTF%20%2F%20GLB-1f6feb)
![Use](https://img.shields.io/badge/use-web%20%2B%20map%20scenes-2ea44f)
![Anchor](https://img.shields.io/badge/anchor-WGS84%20(EPSG%3A4326)-555)
![Provenance](https://img.shields.io/badge/provenance-first%20%F0%9F%94%8E-required-brightgreen)
![License](https://img.shields.io/badge/license-define%20in%20metadata-lightgrey)

> Shared 3D model asset used by **Kansas Frontier Matrix (KFM)** web experiences (2D/3D map + narrative scenes).  
> **Goal:** ship a WebGL-friendly model that is **traceable, auditable, and properly attributed** (no “mystery assets”). ✅

---

## 🧭 Quick Nav

- [📦 What’s in this folder](#-whats-in-this-folder)
- [🌐 Where it shows up in KFM](#-where-it-shows-up-in-kfm)
- [🚀 Quick use in the web client](#-quick-use-in-the-web-client)
- [🧷 Spatial reference & placement](#-spatial-reference--placement)
- [✅ Provenance & data contract](#-provenance--data-contract)
- [⚡ Performance budgets](#-performance-budgets)
- [🧪 QA checklist](#-qa-checklist)
- [📜 License & attribution](#-license--attribution)
- [🛠️ Updating this asset](#-updating-this-asset)

---

## 📦 What’s in this folder

**Path:** `web/assets/3d/shared/models/monument-rocks/`

Recommended layout (your exact filenames may differ):

```text
📁 monument-rocks/
├─ 📄 README.md
├─ 🧾 monument-rocks.metadata.json          # ✅ required “data contract” (see template below)
├─ 🪨 monument-rocks.glb                    # primary runtime model (Web)
├─ 🪨 monument-rocks.lod1.glb               # optional LODs
├─ 🪨 monument-rocks.lod2.glb
├─ 🖼️ preview.webp                         # optional preview image for docs/UI
├─ 📁 textures/                             # optional (if not embedded in GLB)
│  ├─ monument-rocks_baseColor.ktx2
│  ├─ monument-rocks_normal.ktx2
│  └─ monument-rocks_orm.ktx2
└─ 📄 LICENSE.txt                            # optional (or rely on repo license + metadata)
```

> 💡 **Tip:** Prefer a single `.glb` with embedded textures for simplicity, *unless* you’re intentionally using KTX2/streamed textures.

---

## 🌐 Where it shows up in KFM

This model is intended to support KFM’s **2D ⇄ 3D storytelling flow**, where a narrative can transition from historical 2D maps into a 3D terrain/landmark moment (e.g., focusing on **Monument Rocks** as a featured landmark). 🎥🌎

---

## 🚀 Quick use in the web client

### Option A — Cesium (recommended when the app is in “3D globe/terrain mode”)

```js
// Example: place the model at an anchor point (lon/lat/height) with a heading/pitch/roll transform.
// Note: adjust imports/APIs to your Cesium version.

import {
  Cartesian3,
  HeadingPitchRoll,
  Math as CesiumMath,
  Transforms,
  Model,
} from "cesium";

const url = "/assets/3d/shared/models/monument-rocks/monument-rocks.glb";

// ✅ Fill these from the metadata contract:
const lon = -99.000000;     // degrees (WGS84)  <-- TODO
const lat =  38.000000;     // degrees (WGS84)  <-- TODO
const heightM = 0.0;        // meters above ellipsoid/terrain (decide standard) <-- TODO

const heading = CesiumMath.toRadians(0); // <-- TODO
const pitch   = CesiumMath.toRadians(0); // <-- TODO
const roll    = CesiumMath.toRadians(0); // <-- TODO

const position = Cartesian3.fromDegrees(lon, lat, heightM);
const hpr = new HeadingPitchRoll(heading, pitch, roll);
const modelMatrix = Transforms.headingPitchRollToFixedFrame(position, hpr);

const model = await Model.fromGltfAsync({
  url,
  modelMatrix,
  scale: 1.0, // keep scale 1.0 when units are meters
});

viewer.scene.primitives.add(model);
```

### Option B — three.js (useful for “scene cards”, UI callouts, or local mini-scenes)

```js
import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
loader.load(
  "/assets/3d/shared/models/monument-rocks/monument-rocks.glb",
  (gltf) => {
    const root = gltf.scene;

    // Optional: normalize orientation/scale if the asset isn't already standardized.
    root.position.set(0, 0, 0);
    root.rotation.set(0, 0, 0);
    root.scale.setScalar(1);

    scene.add(root);
  }
);
```

> ✅ **Rule of thumb:**  
> - Use **Cesium** for true geo-placement (WGS84 + terrain).  
> - Use **three.js** for “contained” experiences (UI previews, cards, controlled scenes).

---

## 🧷 Spatial reference & placement

### Coordinate system expectations (model-local)
- **Units:** meters (preferred)
- **Axis convention:** glTF is typically **right-handed / Y-up** (standardize your exporter settings)
- **Origin:** keep the model’s pivot sensible (e.g., at ground contact / center-of-mass / known reference)

### Geo-anchor expectations (world placement)
KFM’s web mapping standard expects **WGS84 (EPSG:4326)** for web consistency. 🌍  
This model should therefore ship with a **WGS84 anchor** in the metadata contract:

- `anchor.lon` / `anchor.lat` (degrees, EPSG:4326)
- `anchor.height_m` (meters; define whether ellipsoid vs terrain-relative)
- Optional: `heading/pitch/roll` and `scale`

---

## ✅ Provenance & data contract

KFM is **contract-first + provenance-first**: anything that appears in the UI should be traceable to sources and documented processing, with **required metadata** and no unsourced “mystery” assets. 🔎✅

This folder must include a **metadata JSON contract** (suggested name: `monument-rocks.metadata.json`) that captures:

- **Source(s)** and how to verify them
- **License** and required attribution text
- **Spatial extent** (including WGS84 anchor)
- **Processing steps** (toolchain + what was changed)
- **File inventory** (hashes/sizes recommended)

### 📄 Minimal contract template (copy/paste)

> Save as: `monument-rocks.metadata.json`

```json
{
  "id": "monument-rocks",
  "type": "3d-model",
  "title": "Monument Rocks (Chalk Pyramids) — 3D Model",
  "description": "Shared 3D model used in KFM 3D scenes and landmark callouts.",
  "keywords": ["kansas", "landmark", "geology", "3d", "cesium", "webgl"],

  "formats": [
    { "path": "monument-rocks.glb", "media_type": "model/gltf-binary" }
  ],

  "spatial": {
    "crs": "EPSG:4326",
    "anchor": {
      "lon": 0.0,
      "lat": 0.0,
      "height_m": 0.0
    },
    "orientation_hpr_deg": { "heading": 0.0, "pitch": 0.0, "roll": 0.0 },
    "scale": 1.0,
    "units": "meters"
  },

  "provenance": {
    "sources": [
      {
        "name": "TBD",
        "type": "capture|scan|photogrammetry|archive|other",
        "url": "TBD",
        "accessed": "YYYY-MM-DD",
        "notes": "What this source contributed."
      }
    ],
    "processing_steps": [
      {
        "date": "YYYY-MM-DD",
        "tool": "Blender|RealityCapture|Metashape|MeshLab|other",
        "version": "TBD",
        "summary": "Retopo / decimation / UVs / texture bake / cleanup / export settings."
      }
    ]
  },

  "license": {
    "spdx": "TBD",
    "attribution": "TBD (required credit line)",
    "restrictions": "TBD (if any)"
  },

  "integrity": {
    "files": [
      { "path": "monument-rocks.glb", "sha256": "TBD" }
    ]
  },

  "contacts": [
    { "role": "maintainer", "name": "TBD", "email": "TBD" }
  ]
}
```

> 🧠 If Focus Mode AI needs to reference this model, this contract is where it should pull **attribution + provenance** from.

---

## ⚡ Performance budgets

Keep this asset friendly for web + mobile:

- **Prefer LODs** (LOD0 / LOD1 / LOD2) if the model is heavy  
- **Texture discipline:** fewer textures > many textures  
- **Materials:** merge where possible (materials drive draw calls)
- **Compression:** consider draco/meshopt + KTX2 textures when applicable

Suggested targets (adjust to your scene needs):
- 📉 Mobile-friendly: **≤ 50k–100k triangles**
- 🖥️ Desktop-friendly: **≤ 150k–300k triangles**
- 🧠 Texture max: **2K** (4K only if justified and gated)

---

## 🧪 QA checklist

Before considering the asset “done” ✅

- [ ] Model loads in the target renderer (Cesium and/or three.js)
- [ ] Orientation is correct (up axis, facing direction)
- [ ] Scale is correct (meters) and `scale: 1.0` works
- [ ] Anchor coordinates validated (EPSG:4326 lon/lat)
- [ ] No missing textures (check console + visual inspection)
- [ ] File size is reasonable for web delivery
- [ ] `monument-rocks.metadata.json` is complete (source, license, processing steps)
- [ ] Attribution text matches license requirements
- [ ] Preview image exists (`preview.webp`) *or* the consuming UI has another thumbnail source

---

## 📜 License & attribution

🚫 **Do not ship** this model into shared assets without a clear license.

- Put the license in **metadata** (required)
- Optionally include `LICENSE.txt` here if the license requires bundling text
- If attribution is required, make sure the UI can surface it (metadata is the source of truth)

---

## 🛠️ Updating this asset

When updating **geometry / textures / placement**:

1. Update the model file(s) (`.glb`, LODs, textures)
2. Update `monument-rocks.metadata.json`:
   - add a new `processing_steps[]` entry
   - update `integrity.files[].sha256`
   - update `spatial.anchor` / orientation if placement changed
3. Update / regenerate `preview.webp` (optional but recommended)
4. Run any repo validators/CI checks that enforce data contracts ✅

<details>
<summary>📌 Suggested commit message style</summary>

- `assets(3d): add Monument Rocks GLB + metadata contract`
- `assets(3d): optimize monument-rocks LODs + KTX2 textures`
- `assets(3d): fix monument-rocks anchor + update provenance`

</details>

---

## 🧾 Changelog

- **YYYY-MM-DD** — Initial import (TBD)
- **YYYY-MM-DD** — Optimization pass (TBD)
