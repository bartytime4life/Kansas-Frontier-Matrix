# 🧱 Materials Texture Sources (KFM)

![KFM](https://img.shields.io/badge/KFM-media%20assets-0b7285?style=flat-square)
![Scope](https://img.shields.io/badge/scope-_sources-blue?style=flat-square)
![Type](https://img.shields.io/badge/type-textures%2Fmaterials-purple?style=flat-square)
![Policy](https://img.shields.io/badge/policy-provenance--first-orange?style=flat-square)
![License](https://img.shields.io/badge/license-required-red?style=flat-square)

> **📍 You are here:** `web/assets/media/_sources/textures/materials/`  
> **🎯 Purpose:** editable *source-of-truth* texture sets for **materials** used by the KFM web experience (2D/3D + WebGL renderers).  
> **✅ Rule:** if we can’t prove **where it came from** *and* **how it was transformed**, it doesn’t ship.

---

## ✅ TL;DR

- This folder stores **source textures** (high-res + editable) for **PBR-ish material sets** (wood, stone, soil, brick, etc.).
- **Do not** point the app to `_sources/`. Runtime textures should live in a **generated/optimized** folder (ex: `web/assets/media/textures/materials/`) ✅
- Every material must include:
  - `material.meta.yml` (or `.json`) 🧾
  - license + attribution 🔒
  - preview image 🖼️
  - map set (basecolor/normal/roughness/etc.) 🧵

---

## 🗺️ Repo context (quick mental map)

```text
📦 web/
  🖼️ assets/
    🎞️ media/
      🧪 _sources/                 ← raw/editable assets (this is NOT runtime)
        🧵 textures/
          🧱 materials/            ← ✅ you are here
      🚀 textures/                 ← optimized runtime textures (generated)
```

> [!IMPORTANT]
> `_sources/` is for **editable origins** (scans, high-bit-depth exports, layered files, reference captures).  
> Anything served to users should come from an **optimized build output** (smaller, compressed, cache-friendly).

---

## 📦 Folder contract

### ✅ Recommended structure

```text
🧱 materials/
  🏞️ terrain/
    🌾 prairie-grass/
      🧾 material.meta.yml
      🖼️ preview.jpg
      📁 raw/          ← original capture(s) / scans / reference
      📁 maps/         ← cleaned maps for export pipeline
        basecolor.png
        normal.png
        roughness.png
        ao.png
        height.png
  🧱 built/
    🪨 limestone-block/
      ...
  🧰 utility/
    🧪 debug-checkerboard/
      ...
```

### ✅ “One folder = one material”
A **material folder** is treated like a small “asset package”:
- stable ID
- documented provenance
- deterministic rebuild potential
- ready for indexing into a registry/manifest

---

## 🏷️ Naming conventions

### Folder names
- ✅ `kebab-case` (lowercase, hyphen-separated)
- ✅ category folders are optional but encouraged (`terrain/`, `built/`, `artifacts/`, `utility/`)
- ❌ no spaces, no uppercase, no “final_final_v3” 😅

Examples:
- `terrain/prairie-grass`
- `built/weathered-wood-planks`
- `artifacts/parchment-aged`

### Map filenames
Keep map filenames predictable inside `maps/`:

| Map | Filename | Notes |
|---|---|---|
| Base color | `basecolor.png` | aka “albedo” (no baked lighting) |
| Normal | `normal.png` | tangent-space normal (WebGL-friendly orientation) |
| Roughness | `roughness.png` | linear values |
| Metallic | `metallic.png` | if applicable |
| Ambient occlusion | `ao.png` | optional |
| Height | `height.png` | prefer 16-bit if practical |
| Emissive | `emissive.png` | optional |
| Opacity | `opacity.png` | optional (or alpha in basecolor) |
| Packed | `orm.png` | optional: Occlusion/Roughness/Metallic packing |

> [!TIP]
> If you need multiple variants, version at the **material level** (metadata + folder naming) rather than inventing lots of filename suffixes.

---

## 🎛️ Map types & color spaces

> [!NOTE]
> Think “pixels” vs “texels”: textures are images mapped onto geometry; in rendering pipelines we often call texture pixels **texels**. 🧠

Suggested defaults:

| Map | Colorspace | What it represents |
|---|---|---|
| `basecolor` | **sRGB** | “paint” color, no light/shadow |
| `normal` | **Linear** | surface direction changes |
| `roughness` | **Linear** | micro-surface scatter |
| `metallic` | **Linear** | metalness mask |
| `ao` | **Linear** | ambient occlusion mask |
| `height` | **Linear** | displacement/height scalar |
| `emissive` | **sRGB** | glow color (if used) |

---

## 🖼️ File formats (source vs runtime)

### Source (this folder)
Goal: **quality + editability**.
- ✅ PNG for lossless maps (especially normals, masks, UI-safe details)
- ✅ TIFF/EXR/PSD allowed if needed (use Git LFS for big files—see below)
- ⚠️ JPEG can be OK for photographic `raw/` captures, but avoid JPEG for normals/masks (compression artifacts)

### Runtime (generated)
Goal: **fast + small + cacheable**.
- likely outputs: resized PNG/WebP, or GPU-friendly formats (ex: KTX2) depending on engine choices

> [!IMPORTANT]
> Store **source** here. Store **build outputs** elsewhere.  
> That separation is what makes rebuilds and audits possible.

---

## 🧾 Metadata contract (required)

Each material folder must include:

- `material.meta.yml` (preferred) **or** `material.meta.json`
- Must contain at minimum:
  - `id`, `title`
  - `license.spdx` (or equivalent)
  - `source` (where did it come from?)
  - `attribution` (who to credit?)
  - `maps` (what files exist + colorspace expectations)
  - `scale` (real-world assumptions for tiling)

### Example `material.meta.yml`

```yaml
id: terrain/prairie-grass
title: Prairie Grass (Short)
tags: [terrain, vegetation, kansas]

license:
  spdx: CC0-1.0
  attribution: "Public domain / CC0 source (see links)"
  notes: "If attribution is required, specify exact text here."

source:
  kind: capture            # capture | scan | procedural | derived | mixed
  links:
    - label: "Source pack / archive"
      url: "https://example.com/source-pack"
  captured_at: "2026-01-01"
  captured_by: "KFM Team"
  notes: "Describe capture setup or source rationale."

maps:
  basecolor: { file: "maps/basecolor.png", colorspace: "sRGB" }
  normal:    { file: "maps/normal.png",    colorspace: "linear" }
  roughness: { file: "maps/roughness.png", colorspace: "linear" }
  ao:        { file: "maps/ao.png",        colorspace: "linear", optional: true }
  height:    { file: "maps/height.png",    colorspace: "linear", optional: true }

scale:
  meters_per_tile: 2.0              # how much real-world area a single tile represents
  texel_density_px_per_m: 512       # useful for consistent look across scenes

provenance:
  transformations:
    - id: delight-v1
      tool: "substance-designer"
      notes: "Removed baked lighting, normalized tone."
    - id: seam-fix-v1
      tool: "krita"
      notes: "Made tile seamless."
```

> [!TIP]
> The goal is “contract-first assets”: the metadata is the **truth** about what the files mean and how they’re allowed to be used.

---

## 🔒 Licensing & ethics (non-negotiable)

- ✅ Use assets you have rights to use (CC0/CC-BY/public domain/owned)
- ✅ Keep attribution text *exactly as required*
- ❌ Don’t add “cool textures from random websites” (no provenance, no ship)
- ⚠️ Cultural heritage / sensitive materials:
  - ensure permissions & correct context
  - prefer community-reviewed sources where applicable

> [!IMPORTANT]
> A texture is still *published media*. It must meet the same provenance bar as datasets and narrative artifacts.

---

## 🧰 Git LFS (for big source files)

If you add layered or high-bit-depth sources (`.psd`, `.tif`, `.exr`, etc.), use **Git LFS** so the repo stays usable.

Example:

```bash
git lfs install
git lfs track "*.psd" "*.tif" "*.tiff" "*.exr"
git add .gitattributes
```

> [!NOTE]
> Keep `maps/` reasonably sized; keep the heavy stuff in `raw/` + LFS when needed.

---

## 🚀 Build/optimization pipeline (expected behavior)

Even if the exact script name evolves, the pipeline should generally:

1. Read each `material.meta.*`
2. Validate required fields + required maps
3. Generate runtime outputs:
   - resize to target levels (ex: 512/1024/2048)
   - generate mipmaps (if engine requires)
   - optionally pack channels (ex: ORM)
   - compress for the web (format depends on rendering stack)
4. Emit a manifest/registry used by the app (ex: `materials.manifest.json`)

> [!TIP]
> The pipeline should be **deterministic**: same inputs + same config ⇒ same outputs.

---

## 🧩 Using a material in the web app (example)

Your runtime manifest might look like:

```json
{
  "id": "terrain/prairie-grass",
  "title": "Prairie Grass (Short)",
  "maps": {
    "basecolor": "textures/materials/terrain/prairie-grass/basecolor.ktx2",
    "normal": "textures/materials/terrain/prairie-grass/normal.ktx2",
    "orm": "textures/materials/terrain/prairie-grass/orm.ktx2"
  },
  "scale": {
    "meters_per_tile": 2.0
  },
  "license": {
    "spdx": "CC0-1.0"
  }
}
```

> [!NOTE]
> Paths above are illustrative—match whatever the runtime output folder is in this repo.

---

## ✅ Definition of Done (DoD) checklist

When adding a new material:

- [ ] Folder follows the contract (`category/material-id/…`)
- [ ] `material.meta.yml` exists + includes **license + attribution + source**
- [ ] `preview.jpg` included (so designers/devs can browse quickly)
- [ ] Maps are placed under `maps/` with standard filenames
- [ ] No baked lighting in `basecolor`
- [ ] Normals/masks are not stored as lossy JPEG
- [ ] Big layered sources use Git LFS
- [ ] Material can be rebuilt via the asset pipeline (no “only on my machine” steps)

---

## 🧠 FAQ

### Why keep `_sources/` separate from runtime assets?
Because KFM is “provenance-first”: we want rebuildable, inspectable origins separated from optimized outputs.

### Can I add procedural materials?
Yes—include:
- the generator file(s) (graph, nodes, script) in `raw/`
- export maps into `maps/`
- describe the procedure in `material.meta.yml`

### Where do I put non-material textures (icons, UI sprites, etc.)?
Not here 🙂  
This folder is strictly **materials** (repeatable surface textures), not UI imagery.

---

## 🔗 Related docs (project library / internal standards)

- 📘 `MARKDOWN_GUIDE_v13` — repo invariants, provenance-first publishing, versioning rules
- 📘 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation` — system architecture + governance principles
- 📗 `WebGL Programming Guide` — texture mapping concepts + WebGL texture parameters
- 📙 `Compressed Image File Formats (JPEG/PNG/GIF/…)` — foundational compression tradeoffs

---
🧱 **Keep it clean. Keep it attributable. Keep it rebuildable.**
