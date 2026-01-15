# 🎨 Shared 3D Textures (Web)  
![scope](https://img.shields.io/badge/path-web%2Fassets%2F3d%2Fshared%2Ftextures-blue)
![target](https://img.shields.io/badge/target-WebGL%20%2F%20Cesium%20%2F%20Three.js-6aa84f)
![format](https://img.shields.io/badge/preferred-.ktx2%20(Basis%20Universal)-f39c12)
![fallback](https://img.shields.io/badge/fallback-.png%20%7C%20.jpg-7f8c8d)
![policy](https://img.shields.io/badge/policy-provenance--first-8e44ad)

Shared, production-ready textures used across **all** 3D experiences in the web app (terrain, models, overlays, UI sprites, decals, etc.).  
This folder is optimized for **reuse**, **performance**, and **traceability** 🧭

---

## ✅ Quick Rules (Read this first)
- 🧩 **Prefer reuse**: if a texture already exists, reference it—don’t duplicate.
- 🧾 **No “mystery textures”**: every texture must have provenance + license recorded (see **Texture Contracts**).
- 🪶 **Ship web-ready outputs only**: optimized formats here; keep masters elsewhere.
- 📉 **Performance matters**: smaller files + fewer requests + mipmaps.
- 🎛️ **Color-space correctness** is non-negotiable (sRGB vs Linear).

---

## 📌 Table of Contents
- [📦 What belongs here](#-what-belongs-here)
- [🗂️ Recommended folder layout](#️-recommended-folder-layout)
- [🧾 Texture Contracts (provenance + license)](#-texture-contracts-provenance--license)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧱 PBR map types](#-pbr-map-types)
- [🖼️ Formats & compression](#️-formats--compression)
- [📐 Resolution, tiling, mipmaps](#-resolution-tiling-mipmaps)
- [🎚️ Color management](#️-color-management)
- [🛠️ Authoring workflow](#️-authoring-workflow)
- [🧪 QA checklist](#-qa-checklist)
- [🧩 Usage notes](#-usage-notes)

---

## 📦 What belongs here

### ✅ Good candidates
- 🧱 **Material textures** (PBR sets: basecolor/normal/ORM/emissive)
- 🗺️ **Small geo “drape” textures** used in demos/samples (not full statewide rasters)
- 🏷️ **Decals** (labels, stamps, survey marks, overlays)
- 🧭 **UI sprites** used by 3D scenes (icons, pins, markers)

### ❌ Not here
- 🧊 **Gigantic geospatial rasters** (COGs/tiles/imagery pipelines belong in `data/` catalogs + tile serving)
- 🧰 **Master files** (PSD, XCF, BLEND, EXR, full-res TIFF) → store in a *source-of-truth* location (DVC/LFS or `*_source/` area), not in web runtime assets
- 🔁 Duplicate copies of the same texture in multiple formats without a reason

---

## 🗂️ Recommended folder layout

> This is a *recommended* structure for clarity + reuse. Create folders as needed. 🧠

```text
web/
└─ assets/
   └─ 3d/
      └─ shared/
         └─ textures/
            ├─ 📁 materials/        # tiling PBR materials (stone, soil, brick, etc.)
            ├─ 📁 decals/           # stamps, labels, surface marks
            ├─ 📁 terrain/          # small drape textures (demo-scale, not statewide)
            ├─ 📁 ui/               # pins, sprites, markers used in 3D scenes
            ├─ 📁 atlases/          # packed atlases (spritesheets / decals)
            ├─ 📁 _source/          # OPTIONAL: only if repo strategy allows (otherwise DVC/LFS)
            └─ 📄 README.md
```

---

## 🧾 Texture Contracts (provenance + license)

KFM is provenance-first. Textures are treated like **data assets**:  
every texture must be traceable to a source + license, and must document processing steps 🔍

### ✅ Requirement
For each logical texture set, include a sidecar JSON “contract”:

- **Material set**: `materials/limestone.texture.json`
- **Single texture**: `ui/pin-blue.texture.json`

### 📄 Minimal contract fields
- `id` (stable identifier)
- `title`
- `license` (SPDX-ish string when possible)
- `attribution` (human-readable)
- `source` (where it came from)
- `maps` (outputs in this folder)
- `color_space` (per map)
- `processing` (how outputs were generated)
- `created`, `modified`

### 🧪 Example: material texture contract
```json
{
  "id": "materials/limestone",
  "title": "Limestone (tiled PBR)",
  "license": "CC0-1.0",
  "attribution": "Fill in required credit text here",
  "source": {
    "type": "url|archive|scan|internal",
    "value": "<link or archive reference>",
    "author": "<person/org if known>"
  },
  "maps": {
    "basecolor": "materials/limestone__basecolor.ktx2",
    "normal": "materials/limestone__normal.ktx2",
    "orm": "materials/limestone__orm.ktx2"
  },
  "color_space": {
    "basecolor": "sRGB",
    "normal": "linear",
    "orm": "linear"
  },
  "processing": [
    { "step": "crop", "tool": "gimp|photoshop|krita", "notes": "Made tile seamless" },
    { "step": "encode", "tool": "toktx|basisu", "notes": "KTX2 encoded for web runtime" }
  ],
  "created": "2026-01-15",
  "modified": "2026-01-15"
}
```

### 🗺️ Geo-texture add-on fields (only when applicable)
If the texture is tied to real-world geography (e.g., a draped orthophoto sample), add:
- `bbox` (minLon, minLat, maxLon, maxLat)
- `crs` (e.g., `EPSG:4326` / `EPSG:3857`)
- `resolution` (meters-per-pixel or similar)
- `time_range` (if time-bound imagery)

---

## 🏷️ Naming conventions

### ✅ General rules
- Use **kebab-case** for words: `limestone-smooth`, `pin-blue`
- Avoid spaces, uppercase, and “final_v2_REAL” energy 😅
- Keep names stable; version by **contract metadata** or explicit suffix when necessary

### 🧩 Recommended pattern
`<name>__<map>.<ext>`

Examples:
- `limestone__basecolor.ktx2`
- `limestone__normal.ktx2`
- `limestone__orm.ktx2`
- `pin-blue__sprite.png`

---

## 🧱 PBR map types

| Map | Suffix | Color space | Notes |
|---|---|---:|---|
| Base Color (Albedo) | `__basecolor` | sRGB | No lighting baked in (avoid AO/shadows baked into basecolor unless intentional + documented) |
| Normal (tangent) | `__normal` | Linear | Prefer **PNG/KTX2**, avoid JPEG artifacts |
| ORM (Occlusion/Roughness/Metallic) | `__orm` | Linear | **R=AO, G=Roughness, B=Metallic** (common glTF packing) |
| Roughness (solo) | `__roughness` | Linear | Only when not using ORM packing |
| Metallic (solo) | `__metallic` | Linear | Only when not using ORM packing |
| Emissive | `__emissive` | sRGB | Use sparingly (performance + aesthetic) |
| Opacity/Alpha | `__opacity` | Linear | Often stored in basecolor alpha instead |
| Height/Displacement | `__height` | Linear | Usually offline/baked; document usage |

> 🧠 Tip: Prefer **packed textures** (like ORM) to reduce HTTP requests + GPU bindings.

---

## 🖼️ Formats & compression

### ✅ Preferred (runtime)
- **`.ktx2`** (Basis Universal) → best for WebGL performance + transfer size

### ✅ Acceptable (fallback / simple assets)
- **`.png`** → UI sprites, decals, alpha cutouts, normals (lossless)
- **`.jpg`** → photo-like imagery (no alpha), avoid for normals/ORM

### 🚫 Avoid (unless there’s a strong reason)
- `.gif` (palette + not ideal for 3D)
- `.bmp` (huge)
- `.tif/.tiff` (master/raw pipeline formats; don’t ship to web runtime)

---

## 📐 Resolution, tiling, mipmaps

### 📏 Resolution guidelines (soft targets)
- 🧱 Tiling materials: **1024–2048** square (power-of-two)
- 🏷️ Decals: **256–1024** depending on on-screen size
- 🧭 UI sprites: **64–512**
- 🗺️ Drape samples: keep small; document scale + extent in contract

### 🧩 Tiling
- Make textures **seamless** (tileable) when intended to repeat
- Avoid visible seams: pad edges when atlasing (2–8px bleed is typical)

### 🧊 Mipmaps
- Required for anything that can appear smaller than native resolution
- Prefer KTX2 pipelines that include mipmaps
- If mipmaps are generated at runtime, verify no shimmering/aliasing

---

## 🎚️ Color management

### ✅ sRGB textures (color)
- `basecolor`
- `emissive`

### ✅ Linear textures (data)
- `normal`
- `orm / roughness / metallic / ao`
- `height / opacity / masks`

> ⚠️ Common mistake: importing a normal map as sRGB. It will look “wrong” and break lighting.

---

## 🛠️ Authoring workflow

### 1) Source & license 🧾
- Verify license and attribution requirements **before** importing.
- Capture provenance in the `.texture.json` contract (source, author, terms).

### 2) Create or clean the master 🎨
- Remove baked lighting if it’s a material map (unless intended + documented).
- Ensure tiling (if applicable).
- Keep a master copy in `_source/` or in the project’s large-file strategy (DVC/LFS).

### 3) Export maps 🧱
- Export basecolor, normal, ORM (or rough/metal/ao)
- Validate channel packing if using ORM

### 4) Encode for web 🚀
- Prefer KTX2 (Basis). Keep PNG/JPG only when justified.

<details>
<summary>📎 Example encode commands (illustrative)</summary>

```bash
# Example only — actual tooling/flags depend on the repo build pipeline

# Encode basecolor (sRGB)
toktx --t2 --genmipmap --assign_oetf srgb limestone__basecolor.ktx2 limestone_basecolor.png

# Encode normals (linear)
toktx --t2 --genmipmap --assign_oetf linear limestone__normal.ktx2 limestone_normal.png

# Encode ORM (linear)
toktx --t2 --genmipmap --assign_oetf linear limestone__orm.ktx2 limestone_orm.png
```
</details>

### 5) Write/update the contract ✅
- Add/modify `*.texture.json`
- Include processing steps (what tools you used + what changed)

---

## 🧪 QA checklist

### ✅ Must pass
- [ ] Texture has a matching `*.texture.json` contract 🧾
- [ ] License + attribution are present (and correct)
- [ ] File names follow conventions (`name__map.ext`)
- [ ] Color space is correct (sRGB vs linear)
- [ ] No obvious seams (when intended to tile)
- [ ] Sizes are reasonable (don’t ship 8k unless you *really* mean it 😅)
- [ ] No duplicates (check before adding)
- [ ] Visual test in a representative scene (near + far + grazing angles)

### ⭐ Nice to have
- [ ] ORM packing used where appropriate (fewer fetches)
- [ ] KTX2 includes mipmaps
- [ ] Contract includes checksums for outputs (optional but great for audits)

---

## 🧩 Usage notes

### 🧱 Shared materials
- Prefer referencing a shared PBR set rather than embedding unique textures per model.
- If exporting glTF: keep glTF’s texture references relative and stable.

### 🗺️ Drape textures (terrain / orthophoto samples)
- If draping imagery over a DEM, ensure consistent extent + pixel sizing between raster layers.
- Document any reprojection/resampling in the contract.

### 🧭 Provenance UX (why we care)
Textures can encode “truth claims” (map overlays, scanned artifacts, historical reconstructions).  
Treat them as first-class evidence: source it, document it, and keep it auditable 🧠

---

🧰 **Maintainers**: If you add new rules here, keep them enforceable (CI checks) and keep the contracts minimal-but-sufficient.
