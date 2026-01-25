---
title: "Monument Rocks — 3D Source Exports"
kfm:
  asset_id: "kfm:3d:model:monument-rocks"
  component: "web/assets/3d/shared/models"
  status: "generated"
  visibility: "public"
  last_reviewed: "2026-01-25"
tags:
  - kansas
  - landmark
  - monument-rocks
  - 3d
  - gltf
  - cesium
  - provenance-first
---

# 🪨 Monument Rocks — `sources/exports/`

[⬅️ Model root](../..) · [⬆️ Sources](..)

![asset](https://img.shields.io/badge/asset-3D%20model-blue)
![formats](https://img.shields.io/badge/formats-GLB%20%7C%20glTF%20%7C%203D%20Tiles-informational)
![kfm](https://img.shields.io/badge/KFM-evidence--first%20%2B%20provenance--first-6e40c9)
![target](https://img.shields.io/badge/target-CesiumJS%20%2F%20WebGL-orange)
![governance](https://img.shields.io/badge/governance-FAIR%2BCARE%20%2B%20policy--as--code-success)

> [!IMPORTANT]
> This folder contains **generated exports** of the Monument Rocks 3D asset.
>
> ✅ Make changes in the **source project** (in `../`) and re-export  
> ❌ Do **not** hand-edit meshes/textures here — it breaks reproducibility, provenance, and downstream caching

---

## 🧭 Quick navigation

- [What this folder is](#-what-this-folder-is-and-what-it-is-not)
- [Expected contents](#-expected-contents)
- [How KFM uses this asset](#-how-kfm-uses-this-asset)
- [Export contract](#-export-contract-must-haves)
- [Regenerating exports](#-regenerating-exports)
- [Metadata templates](#-metadata-files-templates)
- [Runtime usage examples](#-runtime-usage-examples)
- [Large files strategy](#-large-files-strategy-git-is-not-a-warehouse)
- [Definition of Done](#-definition-of-done-dod-checklist)
- [Project file crosswalk](#-project-file-crosswalk)

---

## 🧪 What this folder is (and what it is not)

KFM treats “things that power the UI” like research outputs:

- **Sources** are the *authoritative* work products (analogous to `data/raw/`): keep originals, don’t rewrite history 🧱
- **Exports** (this folder) are **reproducible artifacts** produced from sources (analogous to `data/processed/`) ♻️

This `sources/exports/` directory exists to:

- hold **portable exchange formats** (`.glb`, `.gltf`, `.obj`, `.fbx`, …)
- feed the **runtime build** (optimized web-ready assets and/or 3D Tiles)
- support KFM’s “**map behind the map**” UX by linking visuals to provenance + metadata

---

## 🧬 Pipeline map (where this folder fits)

```mermaid
flowchart LR
  A[📸 Capture / References] --> B[🧰 Source Project<br/>(Blender / Photogrammetry)]
  B --> C[📤 Source Exports<br/>(this folder)]
  C --> D[⚙️ Optimize + LOD + Compression]
  D --> E[🌍 Runtime Asset<br/>(GLB / 3D Tiles)]
  E --> F[🗺️ KFM UI<br/>(2D↔3D • Story Nodes • AR)]
  E --> G[🧾 Provenance Panel<br/>+ AI citations]
```

---

## 📦 Expected contents

> [!NOTE]
> File names vary by pipeline, but the **roles** below are the contract.

```text
📁 monument-rocks/
  📁 sources/
    📁 exports/  ← you are here
      📦 *.glb / *.gltf         # export(s) for Cesium/WebGL preview and/or runtime
      📦 *.obj / *.fbx          # optional: interchange exports (hi-poly, baking, etc.)
      🧱 tileset.json / tiles/  # optional: 3D Tiles packaging for streaming
      🖼️ textures/             # if glTF is non-embedded
      🧾 asset.manifest.json    # machine-readable: files + hashes + toolchain
      🧾 prov.jsonld            # provenance record (or pointer to central PROV)
      🔐 checksums.sha256       # integrity + cache keys
      🧪 preview.png            # optional: thumbnail for UI / asset browser
      📄 README.md              # this file 🙂
```

### ✅ “Dual-format” mindset (archive vs runtime)

KFM often keeps **two flavors** derived from the same sources:

- **Archive / hi-res exports** → preserve detail for future re-processing / baking / LOD generation 🗃️
- **Runtime exports** → optimized for browser performance + static hosting 🚀

If you only keep one thing in-repo, keep the **runtime** artifact + manifest, and store hi-res exports via LFS/OCI (see below).

---

## 🧠 How KFM uses this asset

This model is designed to plug into:

- 🌍 **3D Globe & Terrain mode** (Cesium) — landmark flyovers and “Kansas From Above” style stories
- 📚 **Story Nodes** — narrative chapters can “camera cut” from 2D maps into this 3D landmark
- 📱 **Mobile / Offline packs** — ship a lighter LOD for field use + AR overlays
- 🧾 **Layer Provenance** — users can inspect *what* they’re seeing and *where it came from*

---

## 🧱 Export contract (must-haves)

### 1) Spatial reference & units 📏🌐

- **Display / integration CRS:** WGS84 (`EPSG:4326`) is KFM’s standard for web alignment.
- **Units:** meters (especially for elevation and Cesium placement).
- **Placement:** exports should include (or be paired with) a clear **anchor**:
  - lon/lat/height (WGS84) + local origin (ENU), *or*
  - a precomputed transform matrix used by the runtime loader

> [!TIP]
> If you can’t embed georeferencing in the model format, store it next to the export:
> `placement.json` (or inside `asset.manifest.json`).

### 2) Determinism & reproducibility ♻️

- exports should be regenerable from **the same sources + settings**
- any “fix” must be expressed as:
  - a source change, or
  - a scripted export/optimization step (not a manual edit)

### 3) Provenance-first publishing 🧾🔍

Before a model is referenced by the UI, it must have:

- **license + attribution**
- **hashes/checksums**
- **manifest + provenance** linking it to:
  - source inputs (photos/scans/reference data)
  - the export activity (tool versions, parameters, run id)
  - the responsible agent (human and/or CI)

---

## 🔁 Regenerating exports

> [!IMPORTANT]
> Prefer automation. Manual steps are listed only to make the “happy path” explicit.

### A) Source edits (do these in `../`)

1. Open the master source project (Blender / photogrammetry project / etc.)
2. Apply transforms + naming conventions
3. Confirm:
   - scale is correct (meters)
   - normals are clean
   - UVs exist (if textured)
   - object origins are intentional (pivot matters for placement)

### B) Export (write into this folder)

Export one or more of:

- `*.glb` (preferred single-file runtime export)
- `*.gltf` + `textures/` (if you need external textures or human-diffable JSON)
- optional `*.obj` / `*.fbx` (interop)

### C) Optimize (recommended)

Typical web optimizations:

- mesh decimation + **LODs**
- geometry compression (Draco or meshopt extensions)
- texture compression (KTX2/Basis) + reasonable max resolution
- remove unused materials, vertex colors, and animations

### D) Generate/update metadata (required)

Produce:

- `checksums.sha256`
- `asset.manifest.json`
- `prov.jsonld` (or update the central PROV record that references these exports)

### E) Validate (don’t skip ✅)

Minimum validations:

- files referenced in the manifest exist
- hashes match
- model loads in target viewer(s) (Cesium/WebGL)
- license is present + compatible

---

## 🧾 Metadata files (templates)

<details>
<summary><strong>📄 asset.manifest.json (example)</strong></summary>

```json
{
  "asset_id": "kfm:3d:model:monument-rocks",
  "title": "Monument Rocks (3D Model)",
  "status": "generated",
  "visibility": "public",
  "crs_display": "EPSG:4326",
  "units": "meters",
  "placement": {
    "anchor_wgs84": { "lon": null, "lat": null, "height_m": null },
    "method": "ENU",
    "notes": "Fill in once placement is finalized"
  },
  "exports": [
    {
      "path": "monument-rocks.lod1.glb",
      "role": "runtime",
      "sha256": "<fill>"
    },
    {
      "path": "monument-rocks.lod0.glb",
      "role": "archive",
      "sha256": "<fill>"
    }
  ],
  "toolchain": {
    "source_app": "Blender (version TBD)",
    "optimizers": ["(optional) glTF pipeline tool (version TBD)"],
    "run_id": "<iso8601-or-ci-run-id>"
  },
  "license": {
    "spdx": "TBD",
    "attribution": ["TBD"]
  },
  "provenance": {
    "prov": "prov.jsonld",
    "notes": "PROV should link this export activity to its sources"
  }
}
```

</details>

<details>
<summary><strong>🔐 checksums.sha256 (example)</strong></summary>

```text
<sha256>  monument-rocks.lod1.glb
<sha256>  monument-rocks.lod0.glb
<sha256>  asset.manifest.json
<sha256>  prov.jsonld
```

</details>

---

## 🌍 Runtime usage (examples)

### CesiumJS (glTF/GLB primitive)

```js
// Pseudo-code. Replace lon/lat/height with the placement values from the manifest.
const url =
  "/assets/3d/shared/models/monument-rocks/sources/exports/monument-rocks.lod1.glb";

const model = await Cesium.Model.fromGltfAsync({
  url,
  modelMatrix: Cesium.Transforms.eastNorthUpToFixedFrame(
    Cesium.Cartesian3.fromDegrees(lon, lat, heightMeters)
  ),
  scale: 1.0
});

viewer.scene.primitives.add(model);
```

### CesiumJS (3D Tiles tileset)

```js
const tileset = await Cesium.Cesium3DTileset.fromUrl(
  "/assets/3d/shared/models/monument-rocks/sources/exports/tileset.json"
);
viewer.scene.primitives.add(tileset);
await viewer.zoomTo(tileset);
```

### three.js quick sanity check

```js
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

new GLTFLoader().load(
  "/assets/3d/shared/models/monument-rocks/sources/exports/monument-rocks.lod1.glb",
  (gltf) => scene.add(gltf.scene)
);
```

> [!TIP]
> Many “it doesn’t load” bugs are static-hosting issues. Run a local server for previews:
> `python -m http.server 8080`

---

## 📦 Large files strategy (Git is not a warehouse)

If exports get too big for normal Git workflows:

### Option 1) Git LFS (simple, familiar)

- keep runtime LOD(s) in Git
- put hi-res exports / raw scans in LFS

### Option 2) OCI Artifact Registry (recommended for KFM-style provenance)

KFM’s roadmap includes treating data artifacts like container images:

- push `*.glb` / tilesets as an **OCI artifact**
- sign with **cosign**
- reference the immutable digest in `asset.manifest.json` (and/or STAC/DCAT distributions)

<details>
<summary><strong>🧪 Example ORAS workflow</strong></summary>

```bash
# Example only — pick your registry namespace.
oras push ghcr.io/<org>/kfm/monument-rocks:lod1 \
  --artifact-type application/vnd.kfm.3dmodel \
  monument-rocks.lod1.glb:application/octet-stream \
  asset.manifest.json:application/json \
  prov.jsonld:application/ld+json

# Optional: sign the artifact (supply chain / provenance attestation)
cosign sign ghcr.io/<org>/kfm/monument-rocks:lod1
```

</details>

---

## ✅ Definition of Done (DoD) checklist

Before merging changes to this folder:

- [ ] Export(s) load in target viewer(s) (Cesium + at least one fallback preview)
- [ ] `checksums.sha256` updated and matches files
- [ ] `asset.manifest.json` updated (paths, hashes, toolchain, placement)
- [ ] Provenance updated (`prov.jsonld` or centralized PROV record)
- [ ] License + attribution included and accurate
- [ ] If file names changed: any consuming code/config updated
- [ ] Size/performance is reasonable for static hosting + mobile (add LODs if needed)

---

## 📚 Project file crosswalk

<details>
<summary><strong>🧩 How this README uses the project docs (all project files)</strong></summary>

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**  
  → WGS84 (`EPSG:4326`) as web standard, and the 2D↔3D (“Kansas From Above”) storytelling concept.

- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**  
  → dual-format packaging mindset, Cesium 3D demo + AR roadmap, supply-chain provenance/attestations.

- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**  
  → modular visualization stack, offline/mobile considerations, governance/policy expectations.

- 🧭 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**  
  → transparency, reproducibility, and provenance surfaced for users (AI + citations).

- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**  
  → 3D globe mode, Story Nodes, provenance UI, AR/offline UX goals.

- 📥 **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**  
  → provenance-first + deterministic pipeline rules, checksums, and STAC/DCAT/PROV expectations.

- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**  
  → immersive/hybrid storytelling concepts and forward-looking AR/field use patterns.

- 🧪 **Additional Project Ideas.pdf**  
  → evidence manifests, OCI artifacts (ORAS+cosign), and “everything is an auditable artifact” mindset.

- 🗺️ **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf**  
  → static-site constraints (GitHub Pages), MapLibre + future Cesium integration, Cesium-friendly formats.

- 🧠 **AI Concepts & more.pdf** *(PDF portfolio)*  
  → reference pack for AI patterns that reinforce explainability + governance (open in Acrobat to explore).

- 🧾 **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** *(PDF portfolio)*  
  → reference pack for data governance and reproducible processing concepts (open in Acrobat to explore).

- 🌐 **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** *(PDF portfolio)*  
  → reference pack for web-based 3D/virtual-world mapping patterns (open in Acrobat to explore).

- 🧰 **Various programming langurages & resources 1.pdf** *(PDF portfolio)*  
  → general programming resource pack supporting the wider KFM toolchain (open in Acrobat to explore).

</details>

---

If you add a new export format or pipeline step, update this README + `asset.manifest.json` so future contributors can reproduce it. ✨

