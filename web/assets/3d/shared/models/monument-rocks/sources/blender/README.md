# 🪨 Monument Rocks — Blender Source (KFM 3D Asset)

![Blender](https://img.shields.io/badge/Blender-Source-orange?logo=blender&logoColor=white)
![glTF](https://img.shields.io/badge/Export-glTF%202.0-blue)
![CesiumJS](https://img.shields.io/badge/Viewer-CesiumJS%20%2F%203D%20Tiles-0B3D91?logo=cesium&logoColor=white)
![KFM](https://img.shields.io/badge/KFM-Provenance--First-brightgreen)

**Path:** `web/assets/3d/shared/models/monument-rocks/sources/blender/README.md` 📁

This folder contains the **authoritative Blender source** for the **Monument Rocks** 3D model used by the Kansas Frontier Matrix (KFM) to support **2D→3D storytelling**, **3D terrain/landmark views**, and future **AR** experiences. KFM’s UI architecture explicitly supports **2D map rendering (MapLibre GL)** and **3D visualization (CesiumJS / 3D Tiles)** with a **2D/3D toggle**. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Quick nav

- [🎯 Purpose](#-purpose)
- [📦 What lives here](#-what-lives-here)
- [🧱 Blender scene conventions](#-blender-scene-conventions)
- [🌍 Geospatial placement](#-geospatial-placement)
- [📤 Export pipeline](#-export-pipeline)
- [✅ QA checklist](#-qa-checklist)
- [🔐 Provenance, policy, and licensing](#-provenance-policy-and-licensing)
- [🧩 How KFM uses this model](#-how-kfm-uses-this-model)
- [🧰 Troubleshooting](#-troubleshooting)
- [📚 Project reference library](#-project-reference-library)

---

## 🎯 Purpose

Monument Rocks is explicitly called out as an example of a **Kansas landmark** that can be highlighted when KFM transitions from a **2D historical map** into a **3D terrain/landmark** experience.:contentReference[oaicite:2]{index=2}

This README documents:

- how we keep the Blender source **clean, reproducible, and web-ready**
- how we export to **glTF/GLB** (and optionally **3D Tiles**)
- how we preserve **provenance + metadata**, consistent with KFM’s “evidence-first” stance:contentReference[oaicite:3]{index=3}
- how we keep the asset compatible with KFM’s **UI**, **Story Nodes**, and future **AR** workflows:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}

---

## 📦 What lives here

### ✅ Expected contents

> If you don’t see one of these, it’s either stored elsewhere (raw capture data), or it hasn’t been added yet. Keep this folder focused on **Blender-authoring** files.

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🤝 shared/
            └── 🧩 models/
                └── 🪨 monument-rocks/
                    └── 🧪 sources/
                        └── 🎛️ blender/
                            ├── 📄 README.md                 👈 📍 you are here
                            ├── 🎛️ monument-rocks.blend      (authoritative scene; recommended)
                            ├── 🧵 textures/                 (PBR textures: albedo/normal/rough/AO…)
                            ├── 📷 reference/                (reference images if license allows)
                            └── 🐍 scripts/                  (optional Blender export helpers)
```

### 🚫 Keep out of Git (recommended)

- `*.blend1`, `*.blend2`
- bake caches
- huge raw scans / raw photogrammetry source images (store as “raw” assets per provenance policy; see below)

---

## 🧱 Blender scene conventions

KFM’s broader approach is “**no mystery layers**” — everything should be explainable, provenance-backed, and auditable.:contentReference[oaicite:6]{index=6}

### 1) Units & scale 📏

- **1 Blender unit = 1 meter** (recommended)
- Model should be **real-world scale** (important for Cesium & AR)

### 2) Naming & organization 🗂️

Use clear naming and stable collection structure:

- Collections:
  - `COLL_RENDER`
  - `COLL_LOD0`, `COLL_LOD1`, `COLL_LOD2` (optional)
  - `COLL_HELPERS` (empties, rig helpers, measurement guides)

- Objects:
  - `MR_Rock_A`, `MR_Rock_B`, …
  - `MR_Ground`, `MR_Debris_*`

### 3) Materials 🎨

- Prefer **Principled BSDF**
- PBR texture conventions:
  - Base Color: sRGB
  - Normal/Roughness/AO/Metallic: Non-Color

### 4) Topology & performance 🧩

Keep the scene **web-friendly**:

- avoid ultra-dense meshes if a decimated version can preserve silhouette
- consider LODs if the model is intended to be viewed at varying distances (Cesium camera zoom)

---

## 🌍 Geospatial placement

KFM uses **WGS84 (EPSG:4326)** as an internal standard for web-facing geospatial representation.:contentReference[oaicite:7]{index=7}

### Recommended approach ✅

- Keep the Blender scene in **local coordinates** near origin `(0,0,0)` for numerical stability.
- Store the geospatial anchor (lat/lon/height + heading/pitch/roll) in a **model metadata file** adjacent to the exported asset (or in the KFM catalog/graph, depending on repo conventions).

> Why? Cesium and 3D Tiles handle global placement cleanly; Blender stays stable and artist-friendly.

### Minimal “anchor” record (example)

```json
{
  "asset_id": "monument-rocks",
  "crs": "EPSG:4326",
  "anchor": {
    "lat": 0.0,
    "lon": 0.0,
    "height_m": 0.0
  },
  "orientation": {
    "heading_deg": 0.0,
    "pitch_deg": 0.0,
    "roll_deg": 0.0
  }
}
```

> ⚠️ If a dataset is sensitive (not Monument Rocks, but other sites), KFM may **generalize locations** (coarsen/fuzz) and apply access controls instead of publishing exact coordinates.:contentReference[oaicite:8]{index=8}

---

## 📤 Export pipeline

KFM’s ingestion philosophy generalizes well to 3D assets: **ingest → validate → transform → publish**, with reproducible, deterministic runs and rich metadata/provenance.:contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

### A) Manual export (Blender UI) 🖱️

1. Open `monument-rocks.blend`
2. Confirm:
   - scale looks correct
   - transforms applied (`Ctrl+A` → Rotation & Scale)
   - normals are correct (no inside-out faces)
3. Export:
   - `File → Export → glTF 2.0`
   - Format: **glTF Binary (.glb)** (recommended for single-file portability)
   - Include: Meshes, Materials, Textures
   - Apply Modifiers: ✅
   - Compression: (optional, if your toolchain supports it)

### B) Scripted export (recommended for reproducibility) 🤖

KFM places a premium on repeatable processes and traceable outputs. Document and version your export environment/configs so someone else can reproduce the exact build later.:contentReference[oaicite:11]{index=11}

Example pattern:

```bash
# Example only — adapt to your repo’s scripting conventions
blender -b monument-rocks.blend -P ./scripts/export_gltf.py -- \
  --out ../../exports/monument-rocks.glb
```

### C) Optional: 3D Tiles packaging 🧊

KFM’s 3D stack is designed around Cesium and supports **3D Tiles** for efficient streaming and interaction.:contentReference[oaicite:12]{index=12}:contentReference[oaicite:13]{index=13}

If your deployment uses 3D Tiles:

- Convert `monument-rocks.glb` → tileset (tooling varies)
- Apply world transform using WGS84 anchor metadata
- Validate in the KFM web viewer’s 3D mode (Cesium)

---

## ✅ QA checklist

KFM uses automated quality gates in multiple stages and prefers “**fail closed**” enforcement (nothing publishes unless it passes minimum standards).:contentReference[oaicite:14]{index=14}

### Visual & geometry ✅

- [ ] Scene opens without missing textures
- [ ] No flipped normals / non-manifold spikes
- [ ] Reasonable draw calls (materials not exploding into hundreds of variants)
- [ ] Model scale matches reality (meter-ish)

### Export correctness ✅

- [ ] GLB loads in a glTF viewer
- [ ] PBR looks right (no glossy rock due to inverted roughness)
- [ ] Texture sizes are sane for web (prefer multiple smaller maps over a single massive texture)

### Metadata / governance ✅

- [ ] **License** recorded (no “unknown license” assets):contentReference[oaicite:15]{index=15}
- [ ] **Sensitivity classification** present (even if “public”):contentReference[oaicite:16]{index=16}
- [ ] **Provenance completeness**: inputs + processing steps declared:contentReference[oaicite:17]{index=17}

> 🧠 Treat “mesh cleanup” the same way KFM treats “data cleaning”: errors and inconsistencies distort results, so cleaning and preparation are essential before downstream analysis/visualization.:contentReference[oaicite:18]{index=18}

---

## 🔐 Provenance, policy, and licensing

KFM’s governance model explicitly emphasizes metadata completeness (STAC/DCAT/PROV), known licenses, sensitivity labeling, and declared provenance steps — enforced through automated gates and CI policy checks.:contentReference[oaicite:19]{index=19}

### Provenance essentials 🧬

At minimum, keep (somewhere in the repo’s expected location):

- what raw data was used (photos, scans, LiDAR, references)
- who created/edited the model
- what tools + versions were used
- what transformations were applied (decimation, baking, retopo, texture generation)
- checksums for published exports

KFM’s ingestion pipelines are designed to preserve provenance and run deterministically using run contexts and structured metadata records.:contentReference[oaicite:20]{index=20}

### Cultural & sensitive data 🪶

KFM explicitly considers cultural protocols and sensitive handling patterns (permissions, coordinate rounding/generalization, and respectful governance).:contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}

Even though Monument Rocks is a public landmark, we keep the *same machinery* so the pipeline is consistent across assets.

### Artifact publishing (advanced) 📦🔏

KFM explores using OCI artifact registries to distribute and verify datasets/artifacts, including signatures and provenance attachments (e.g., ORAS + cosign; attach PROV/SLSA documents).:contentReference[oaicite:23]{index=23}

If your deployment supports it, consider publishing `monument-rocks.glb` as a signed artifact, alongside:

- `provenance.jsonld`
- `checksums.txt`
- an SBOM for tooling where applicable

---

## 🧩 How KFM uses this model

### 1) UI integration 🗺️🧊

KFM’s UI architecture supports:

- 2D map mode (MapLibre GL)
- 3D mode (CesiumJS / 3D Tiles)
- a toggle between modes while preserving user context:contentReference[oaicite:24]{index=24}

Additionally, KFM’s UI is designed so layers and content can be traced back to provenance/metadata (sources, lineage, citations).:contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}

### 2) Story Nodes 📖🎬

KFM story nodes are a **folder-based convention** (Markdown + optional JSON config) used for guided narratives and camera transitions.:contentReference[oaicite:27]{index=27}

A “Kansas From Above” **2D→3D story** is explicitly planned using a Markdown/JSON story convention, enabling camera transitions into 3D terrain views.:contentReference[oaicite:28]{index=28}

> If you are authoring a story node that references this model, ensure the node includes **source attributions** and links to the model’s metadata record (so Focus Mode + UI can cite it).

### 3) AR & offline field use 📱✨

KFM’s roadmap includes AR overlays (e.g., scanning a location and seeing historical imagery/3D content) and offline-capable packs for field use.:contentReference[oaicite:29]{index=29}:contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}

That means 3D assets must be:

- small enough to stream
- robust across devices
- packaged with complete metadata and licensing

---

## 🧰 Troubleshooting

### “Model is tiny / huge in Cesium” 📏
- verify Blender unit scale and applied transforms
- ensure you didn’t export with an unintended scale factor

### “Textures look wrong / too shiny” 🧴
- confirm roughness map is in **Non-Color**
- verify metallic is correct (rocks should rarely be metallic)

### “Z-fighting / flicker” ⚡
- avoid coplanar surfaces
- slightly offset decals or merged geometry

### “CI/policy gate failed” 🚦
Common causes:
- missing license
- missing sensitivity classification
- missing provenance steps / inputs declared:contentReference[oaicite:32]{index=32}

---

## 📚 Project reference library

These project documents inform the standards and decisions reflected in this README:

### Core KFM docs 🧭🌾
- **KFM Technical Documentation** :contentReference[oaicite:33]{index=33}  
- **KFM Architecture, Features, and Design** :contentReference[oaicite:34]{index=34}  
- **KFM UI System Overview** :contentReference[oaicite:35]{index=35}  
- **KFM Data Intake – Technical & Design Guide** :contentReference[oaicite:36]{index=36}  
- **KFM AI System Overview** :contentReference[oaicite:37]{index=37}  
- **Innovative Concepts to Evolve KFM** :contentReference[oaicite:38]{index=38}  
- **Latest Ideas & Future Proposals** :contentReference[oaicite:39]{index=39}  
- **Additional Project Ideas** :contentReference[oaicite:40]{index=40}  
- **Open-Source Geospatial Historical Mapping Hub Design** :contentReference[oaicite:41]{index=41}  
- **MARKDOWN_GUIDE (v13)** :contentReference[oaicite:42]{index=42}  

### Supporting library (research & engineering) 📚🧠
- **AI Concepts & more (PDF portfolio)** :contentReference[oaicite:43]{index=43}  
- **Data Management (PDF portfolio)** :contentReference[oaicite:44]{index=44}  
- **Maps / WebGL / Virtual Worlds (PDF portfolio)** :contentReference[oaicite:45]{index=45}  
- **Various programming languages & resources (PDF portfolio)** :contentReference[oaicite:46]{index=46}  
- **Data Mining Concepts & applications** :contentReference[oaicite:47]{index=47}  
- **Scientific Method / Master Coder Protocol Documentation** :contentReference[oaicite:48]{index=48}  
- **Python Geospatial Analysis Cookbook** :contentReference[oaicite:49]{index=49}  

> 🧩 Note: Some items above are **PDF portfolios** and may require Acrobat/Reader to browse the embedded contents.

---

## 🏷️ Changelog (optional)

- `v0.1` — Initial README + conventions (this file)


