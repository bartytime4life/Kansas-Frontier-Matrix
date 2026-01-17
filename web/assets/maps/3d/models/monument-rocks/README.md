# 🗿 Monument Rocks — 3D Model Asset (KFM)

![Status](https://img.shields.io/badge/status-draft-yellow)
![Format](https://img.shields.io/badge/format-glTF%202.0-blue)
![Mode](https://img.shields.io/badge/mode-3D%20Landmark-6f42c1)
![Viewer](https://img.shields.io/badge/viewer-CesiumJS-informational)
![CRS](https://img.shields.io/badge/CRS-WGS84%20(EPSG%3A4326)-success)
![Provenance](https://img.shields.io/badge/provenance-first-brightgreen)

> 🌾 A Kansas Frontier Matrix (KFM) landmark model intended for the **“Kansas From Above”** 2D ↔ 3D demo/story flow (MapLibre → Cesium).[^kfm-frontend-3d][^kfm-kansas-from-above-1][^kfm-kansas-from-above-2]

---

## ✨ What this folder is for

KFM’s front-end mapping stack is designed to **switch between 2D and 3D**—using **MapLibre GL JS** for 2D maps and **CesiumJS** for 3D globe/terrain—and can stream **3D Tiles** for large 3D datasets.[^kfm-frontend-3d]

This folder is the home for the **Monument Rocks** landmark asset used when a story or UI view transitions into 3D mode (e.g., the “Kansas From Above” showcase concept, which explicitly calls out Monument Rocks as an iconic target location).[^kfm-kansas-from-above-1][^kfm-kansas-from-above-2]

---

## 📦 Expected contents

> ✅ Keep filenames stable: front-end asset URLs should not break across story revisions.

```text
web/assets/maps/3d/models/monument-rocks/
├─ 📄 README.md                        # (this file)
├─ 🧱 monument-rocks.glb               # primary runtime model (recommended)
├─ 🖼️ preview.webp                     # lightweight preview for docs/UI
├─ 🧾 monument-rocks.metadata.json     # “data contract” / provenance metadata (required in KFM)
└─ 🧰 extras/
   ├─ 🧱 monument-rocks-high.obj        # optional: source/high-res mesh
   ├─ 🖼️ textures-source/              # optional: source textures
   └─ 🧪 bake-notes.md                  # optional: photogrammetry / bake notes
```

> If you publish via **3D Tiles**, add:
```text
├─ 🧱 tileset.json
└─ tiles/...
```

---

## 🧭 Coordinate system and units

KFM’s internal web standard is **WGS84 (EPSG:4326)** for consistency, while still tracking original CRS in metadata; elevation units should be explicit (typically meters).[^kfm-wgs84]

### ✅ Requirements for this model

- **CRS for placement:** WGS84 (EPSG:4326)  
- **Units:** meters (scale must be real-world consistent)  
- **Up-axis:** document what you exported (glTF is typically Y-up; Cesium’s world is Z-up internally—orientation matters)  
- **Anchor point:** provide the “place-on-globe” reference in `monument-rocks.metadata.json` (see template below)

---

## 🚀 Quick use in CesiumJS

### Option A — Load the `.glb` as a model entity (simple + great for landmarks)

```ts
import {
  Viewer,
  Cartesian3,
  HeadingPitchRoll,
  Transforms,
} from "cesium";

const viewer = new Viewer("cesiumContainer");

// TODO: Replace with the real placement coordinates (WGS84)
const lon = -100.000000;
const lat =  39.000000;
const heightMeters = 0.0;

const position = Cartesian3.fromDegrees(lon, lat, heightMeters);

// TODO: Adjust heading/pitch/roll until the rock matches terrain orientation
const hpr = HeadingPitchRoll.fromDegrees(0, 0, 0);
const orientation = Transforms.headingPitchRollQuaternion(position, hpr);

const entity = viewer.entities.add({
  name: "Monument Rocks (3D)",
  position,
  orientation,
  model: {
    uri: "/assets/maps/3d/models/monument-rocks/monument-rocks.glb",
    scale: 1.0,
    // clampToGround: true, // (if you use terrain + supported path)
  },
});

viewer.trackedEntity = entity;
```

### Option B — Load as 3D Tiles (best if you add LODs, large textures, or want streaming)

```ts
import { Viewer, Cesium3DTileset } from "cesium";

const viewer = new Viewer("cesiumContainer");

const tileset = await Cesium3DTileset.fromUrl(
  "/assets/maps/3d/models/monument-rocks/tileset.json"
);

viewer.scene.primitives.add(tileset);
viewer.zoomTo(tileset);
```

---

## 🧾 Provenance-first: required metadata (data contract)

KFM’s architecture enforces a **contract-first and provenance-first** rule: anything shown in the UI must be traceable to cataloged sources and provable processing, and “mystery layers” are not allowed.[^kfm-provenance]  
Practically, this means each dataset should ship with a **metadata JSON (“data contract”)** describing source, license, spatial/temporal extent, processing steps, etc.[^kfm-data-contract]

### 📄 `monument-rocks.metadata.json` template

```json
{
  "id": "monument-rocks",
  "title": "Monument Rocks (3D Landmark Model)",
  "summary": "3D landmark asset used by KFM in Cesium 3D mode.",
  "asset_type": "3d-model",
  "formats": [
    { "type": "model/gltf-binary", "path": "monument-rocks.glb" }
  ],
  "crs": "EPSG:4326",
  "units": "meters",

  "anchor": {
    "lon": -100.000000,
    "lat": 39.000000,
    "height_m": 0.0,
    "heading_deg": 0.0,
    "pitch_deg": 0.0,
    "roll_deg": 0.0
  },

  "bbox_wgs84": {
    "west": -100.0000,
    "south": 39.0000,
    "east": -100.0000,
    "north": 39.0000
  },

  "license": "TBD",
  "attribution": "TBD",
  "sources": [
    {
      "name": "TBD (capture/source dataset)",
      "license": "TBD",
      "url": "TBD"
    }
  ],

  "processing_steps": [
    "Capture → photogrammetry/scan",
    "Clean mesh → retopo/decimate",
    "Bake textures → compress",
    "Export glTF/GLB → validate",
    "Place on globe → verify alignment"
  ],

  "qa": {
    "gltf_validated": false,
    "scale_verified": false,
    "anchor_verified": false
  }
}
```

> 💡 Tip: Keep this metadata **adjacent to the asset** in the repo so the UI (and Focus Mode) can always surface source + method trace when this model is used.[^kfm-data-contract]

---

## 🧰 Suggested production pipeline (photogrammetry → web-ready)

If you’re building/updating the asset from field capture, a proven workflow is:

- Generate the initial mesh via **image-based 3D modelling** (e.g., DSLR capture → Agisoft Metashape).
- Optimize/merge point clouds/meshes in tools like **CloudCompare**, and generate a clean surface (e.g., Poisson reconstruction), then export to a standard format (e.g., OBJ) before converting to web formats.[^archaeo-box46]
- It’s common to **scale + georeference** the model as part of this pipeline (example: Metashape model → scaled → georeferenced → exported OBJ → imported into GIS tooling).[^archaeo-metamodel]

If the model **lacks ground control points**, you can still geolocate it by **spatially adjusting it in GIS** using references from other layers (raster/vector basemap), which is specifically called out as a practical approach.[^archaeo-georef-adjust]

<details>
<summary>🧪 Recommended “web-readiness” checklist</summary>

- ✅ Tri-count budget: keep a **runtime** mesh lightweight (consider LODs if needed)
- ✅ Textures: prefer power-of-two sizes; compress (KTX2/Basis) if supported
- ✅ Material model: PBR-friendly, avoid exotic shader features
- ✅ Validate glTF (glTF Validator)
- ✅ Verify **real-world scale** (meters) and **anchor** accuracy in Cesium
- ✅ Provide `preview.webp` and update the changelog below

</details>

---

## ⚙️ Performance targets (guidelines)

These are pragmatic defaults for smooth web/3D map performance:

- **GLB size:** aim ≤ 15–25 MB for first-load (smaller is better for stories)
- **Textures:** prefer a small set of atlased textures over many tiny files
- **LOD strategy:**  
  - LOD0 (hero close): highest detail  
  - LOD1 (mid): 30–50% triangles  
  - LOD2 (far): silhouette only  
- **Don’t** ship raw scan meshes as runtime assets—keep those in `extras/`

---

## ✅ QA checklist (before merging)

- [ ] `monument-rocks.glb` loads in Cesium without console errors  
- [ ] Model is correctly oriented (no upside-down / mirrored normals)  
- [ ] Scale is realistic (**meters**)  
- [ ] Anchor coordinates place the model where expected in WGS84  
- [ ] `monument-rocks.metadata.json` has **license + attribution + sources** filled  
- [ ] Preview image updated (`preview.webp`)  
- [ ] Changelog updated

---

## 🗒️ Changelog

| Date (YYYY-MM-DD) | Version | Changes | By |
|---|---:|---|---|
| 2026-01-17 | 0.1.0 | Initial README + metadata template | @you |

---

## 📚 Notes & references

[^kfm-frontend-3d]: KFM front-end stack: MapLibre GL JS for 2D maps; CesiumJS for 3D globe/terrain; supports streaming 3D Tiles and emphasizes provenance surfaced in UI interactions. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-wgs84]: KFM projection guidance: internal standard WGS84 (EPSG:4326); track original CRS in metadata; serve WGS84 for web consistency. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-kansas-from-above-1]: “Kansas From Above” concept: transitions from 2D historical map to 3D terrain focusing on a landmark “like Monument Rocks” with a 3D model; notes on 2D/3D switching and 3D being opt-in/heavier. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-kansas-from-above-2]: KFM “3D Demo – Kansas From Above”: planning includes preparing high-res 3D terrain tiles for iconic sites like Monument Rocks/Flint Hills and possibly including a 3D model; intended to set a pattern for future 2D/3D stories. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-provenance]: KFM “Contract-First and Provenance-First”: UI-visible data must be traceable to cataloged sources and provable processing; uses open standards (STAC, DCAT, PROV-O); “no mystery layers”. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^kfm-data-contract]: KFM data contract detail: every dataset has a metadata JSON with source/license/extent/processing steps; contract-first ensures provenance record; supports citations in Focus Mode; prohibits unsourced data (“mystery layers”). [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

[^archaeo-box46]: Photogrammetry/mesh pipeline reference: Metashape (DSLR images) + CloudCompare optimization/merging + Poisson reconstruction; export boundary model as OBJ and integrate into GIS; models can be linked to attribute tables for richer analysis/metadata workflows. [oai_citation:6‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

[^archaeo-georef-adjust]: Georeferencing guidance: workflows remain relevant when models lack ground control points and must be spatially adjusted in GIS using raster/vector basemap references. [oai_citation:7‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

[^archaeo-metamodel]: Example pipeline note: model generated in Metashape; then scaled, georeferenced, exported as OBJ, and imported into ArcGIS Pro (illustrating common scale/georef/export practice). [oai_citation:8‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
