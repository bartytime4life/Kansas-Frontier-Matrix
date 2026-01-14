# 🧊 3D Assets (`web/assets/3d/`)

![assets](https://img.shields.io/badge/assets-3D%20%2B%20geospatial-0b7285)
![webgl](https://img.shields.io/badge/rendering-WebGL%20ready-3b5bdb)
![cesium](https://img.shields.io/badge/3D%20globe-Cesium%20friendly-7048e8)
![provenance](https://img.shields.io/badge/provenance-required-2f9e44)
![performance](https://img.shields.io/badge/perf-budgets%20enforced-f59f00)

This folder contains **3D-ready web assets** used by Kansas Frontier Matrix (KFM) experiences (e.g., landmarks, terrain, 3D overlays, and story-driven “Kansas From Above” moments).  
The goal is: **fast, portable, attributable, geospatially correct** 3D.

---

## 🎯 What belongs here

✅ **Discrete 3D models** (landmarks, artifacts, buildings, props)  
✅ **Geospatial 3D tiles** (terrain, photogrammetry tilesets, point clouds)  
✅ **Textures & material maps** (PBR-friendly)  
✅ **Metadata + provenance contracts** (non-negotiable for KFM)

🚫 Don’t put here:
- Source project files (e.g., `.blend`, `.max`, `.spp`) unless explicitly needed for reproducibility
- Random “test” models without metadata
- Anything with unclear license/ownership

---

## 🗂️ Recommended folder layout

> Keep it boring. Boring scales. 😌

# 🧊 `web/assets/3d/` Asset Library Layout

![Assets](https://img.shields.io/badge/assets-3D%20library-0b7285)
![Format](https://img.shields.io/badge/format-GLB%20%2B%20WebP-5f3dc4)
![Metadata](https://img.shields.io/badge/metadata-meta.json%20required-2f9e44)

## 🧭 Emoji Legend
- 📁 Folder
- 📄 Markdown / docs
- 🧩 JSON
- 🧊 3D model (`.glb`)
- 🖼️ Image / texture (`.webp`)
- 🗺️ 3D Tiles manifest (`tileset.json`)
- 🧱 Tile payloads (`tiles/...`)

## 🌲 Folder Tree (with emojis)

```text
📁 web/assets/3d/
├─ 📄 README.md
├─ 🧩 _registry.json                # optional: generated index for UI pickers / lazy-loading
│
├─ 📁 landmarks/                    # iconic places, “wow” moments
│  └─ 📁 monument-rocks__kfm_0001/
│     ├─ 🧊 model.glb
│     ├─ 🖼️ thumbnail.webp
│     ├─ 🧩 meta.json               # required
│     └─ 📁 textures/
│        ├─ 🖼️ basecolor.webp
│        ├─ 🖼️ normal.webp
│        └─ 🖼️ orm.webp
│
├─ 📁 archaeology/                  # site models, trench surfaces, artifacts
│  └─ 📁 sample-trench__kfm_0101/
│     ├─ 🧊 model.glb
│     ├─ 🧩 meta.json
│     └─ 📄 sources.md              # optional (great for human-readable context)
│
├─ 📁 terrain/                      # large-scale elevation / surfaces
│  └─ 📁 kansas-dem__kfm_1001/
│     ├─ 🗺️ tileset.json            # if 3D Tiles
│     ├─ 🧩 meta.json
│     └─ 🧱 tiles/...
│
└─ 📁 shared/                       # reusable materials, LUTs, env maps
   ├─ 📁 env/
   └─ 📁 materials/
```

**Rule of thumb:** One asset = one folder = **everything needed to render it** (plus metadata).

---

## 📦 Supported formats (opinionated)

### 🥇 Preferred
- **glTF 2.0 (`.glb`)** for most “single object” models  
  - Single binary is easiest to ship and cache
- **3D Tiles** (`tileset.json` + tile payloads) for “big” geospatial datasets  
  - Terrain, LiDAR point clouds, large photogrammetry, city-scale geometry

### ✅ Allowed (with a plan)
- `.gltf` (JSON + external buffers/textures) only when necessary (streaming / patching)
- `.obj` as an *intermediate* artifact (do **not** treat OBJ as a final web format)

---

## 🌍 Geospatial expectations

If the asset is meant to sit on the map/globe, it must be **geospatially unambiguous**:

- **CRS/Datum:** standardize around **WGS84 (EPSG:4326)** for web alignment  
- **Units:** meters (unless explicitly documented otherwise)
- **Orientation:** document axis convention (glTF is typically right-handed, Y-up)
- **Anchoring:** either:
  - include a georeferenced tileset (preferred for large datasets), or
  - store a clear anchor transform in `meta.json` (lat/lon/height + heading/pitch/roll)

---

## 🧾 Provenance-first metadata (required)

KFM follows a strict philosophy: **anything visible must be traceable**.  
So every asset folder must include:

### ✅ `meta.json` (minimum)
At a minimum, capture:

- `id` (stable, info-free)
- `title`
- `description`
- `license` (SPDX if possible)
- `sources[]` (URLs, citations, archives, scans, or field logs)
- `created_by` + `created_at`
- `processing[]` (what tools/steps produced the web-ready asset)
- `spatial` (bbox / anchor / CRS)
- `files[]` (checksums + sizes)

> If we can’t explain where it came from, it can’t ship. 🧠✨

---

## 🆔 Naming + IDs (stable by design)

Use **stable, information-free identifiers** for asset IDs and folders:

- ✅ `monument-rocks__kfm_0001`
- ✅ `artifact-bowl__kfm_0342`
- ❌ `monument-rocks-2026-final-v7`
- ❌ `kansas_dem_epsg4326_fixed`

**Why:** names, locations, formats, and “final versions” change. IDs shouldn’t.

### Convention
- **Folder name:** `slug__kfm_NNNN`
- **Metadata id:** `kfm:NNNN` (or similar stable namespace)
- **Human labels live in metadata**, not in the identifier.

---

## ⚡ Performance budgets (web reality check)

3D can get expensive fast. Keep assets lean:

### Targets (per discrete model)
- **Compressed size:** aim < **10–15 MB** (mobile-friendly)
- **Triangles:** start < **100k** (depends on view distance & LOD)
- **Textures:** prefer **2K max** unless justified; reuse materials

### For large geospatial datasets
- Use tiling + LOD (3D Tiles)
- Ensure progressive loading is possible (don’t force “download the world”)

---

## 🧰 Textures & materials

- Prefer **PBR-friendly** workflow
- Keep texture sets consistent:
  - `basecolor`
  - `normal`
  - `orm` (occlusion/roughness/metallic packed) when applicable
- Use web-friendly formats (`webp`, `png`, `jpg`, or GPU-compressed textures when supported)

---

## ✅ Add a new asset checklist

### 1) Create the folder
- `web/assets/3d/<category>/<slug>__kfm_NNNN/`

### 2) Add renderable files
- `model.glb` **or** `tileset.json` (with tile payloads)
- `thumbnail.webp` (strongly recommended for UI)

### 3) Add metadata
- `meta.json` **required**
- Include license + sources + processing steps + spatial anchoring

### 4) Validate
- Loads in the target viewer (Three.js / Cesium / WebGL layer)
- Looks correct (scale/orientation)
- Performs within budget (no giant textures, no accidental 4M-tri meshes)

### 5) Keep the commit clean
- No mystery binaries
- No unlabeled derivatives
- No license ambiguity

---

## 🧪 Quick validation tips

- Open the model in a glTF viewer and confirm:
  - orientation, scale, materials, texture paths
- Profile:
  - download size
  - GPU memory pressure (textures)
  - draw calls / material count

---

## 🧩 Metadata template (copy/paste)

<details>
<summary><strong>📄 meta.json template</strong> (minimal-but-real)</summary>

```json
{
  "id": "kfm:0001",
  "title": "Monument Rocks (simplified landmark model)",
  "description": "Web-ready model used for 3D storytelling and map context.",
  "license": "CC-BY-4.0",
  "sources": [
    {
      "type": "url",
      "citation": "Field capture + public reference photos",
      "url": "https://example.com/source-or-archive",
      "retrieved_at": "2026-01-14"
    }
  ],
  "created_by": "KFM Pipeline",
  "created_at": "2026-01-14",
  "processing": [
    {
      "step": "Photogrammetry reconstruction",
      "tool": "Agisoft Metashape",
      "notes": "Dense cloud → mesh → texture bake"
    },
    {
      "step": "Web optimization",
      "tool": "Blender",
      "notes": "Decimate, UV cleanup, export glTF/GLB"
    }
  ],
  "spatial": {
    "crs": "EPSG:4326",
    "anchor": { "lat": 38.752, "lon": -100.601, "height_m": 0 },
    "bbox": [-100.602, 38.751, -100.600, 38.753]
  },
  "files": [
    { "path": "model.glb", "sha256": "REPLACE_ME", "bytes": 12345678 },
    { "path": "thumbnail.webp", "sha256": "REPLACE_ME", "bytes": 234567 }
  ],
  "tags": ["landmark", "kansas", "story"]
}
```
</details>

---

## 🧭 Design principles (why this folder looks like this)

- **Web-first portability:** assets should run in-browser without plugins (desktop → mobile)  
- **3D is opt-in:** use 3D when it adds meaning, not just sparkle ✨  
- **Contract-first & provenance-first:** trust comes from traceability  
- **Stable IDs > “final_v9”:** future-proofing beats patchwork fixes  
- **Performance is a feature:** “loads fast” is part of the content

---

## 🔒 Licensing & attribution

Every asset must:
- declare a **license**
- declare **source(s)**
- preserve attribution requirements in metadata

If unsure, treat it as **not shippable** until clarified.

---

## 📌 TODO (nice upgrades)
- Auto-generate `_registry.json` from `meta.json` files
- CI check: require `meta.json`, checksums, and license fields
- Add a tiny “asset linter” script to enforce naming + budgets

—  
🧊 If it’s in 3D, it’s also in **metadata**. That’s the deal.
