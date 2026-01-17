---
title: "🧵 Textures (3D Models) — Web Runtime Assets"
path: "web/assets/media/models-3d/textures/"
status: "active"
version: "v1.0.0"
last_updated: "2026-01-17"
ownership: "KFM"
license: "Per-asset (see .meta.json sidecars)"
---

# 🧵 Textures (3D Models)

![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fmedia%2Fmodels--3d%2Ftextures-blue)
![asset-type](https://img.shields.io/badge/asset-PBR%20textures-brightgreen)
![provenance](https://img.shields.io/badge/provenance-required-orange)
![license](https://img.shields.io/badge/license-per--asset-lightgrey)

> 📍 **Folder:** `web/assets/media/models-3d/textures/`  
> 🎯 **Purpose:** ship **web-ready texture maps** referenced by 3D models in the KFM front-end (fast to load, easy to audit, safe to license).

---

## 📌 Contents

- [✅ What belongs here](#-what-belongs-here)
- [🚫 What does not belong here](#-what-does-not-belong-here)
- [🧠 KFM rules applied to textures](#-kfm-rules-applied-to-textures)
- [🗂️ Suggested layout](#️-suggested-layout)
- [🏷️ Naming convention](#️-naming-convention)
- [🧩 Map types and suffixes](#-map-types-and-suffixes)
- [📦 File formats](#-file-formats)
- [⚡ Performance guidelines](#-performance-guidelines)
- [🧾 Provenance and license sidecars](#-provenance-and-license-sidecars)
- [🔁 Adding or updating textures](#-adding-or-updating-textures)
- [✅ Pre-commit checklist](#-pre-commit-checklist)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Related docs](#-related-docs)

---

## ✅ What belongs here

**Runtime textures only** — what the browser should fetch at render-time:

- 🧵 PBR texture maps referenced by `.glb/.gltf` (or a material manifest used by the viewer)
- 🧼 “Production” outputs: resized, compressed, and stripped of unneeded metadata
- 🧾 Textures with **clear provenance + license** recorded via sidecar metadata

---

## 🚫 What does not belong here

Keep this folder lean — it’s part of the web payload.

- 🧱 Source/working files: `.psd`, `.kra`, `.blend`, Substance projects, etc.
- 📸 Massive raw photogrammetry exports / uncompressed “master” textures
- ❓ Unknown-origin textures (“mystery textures”)  
- 🔐 Anything with uncertain rights, restrictive licenses, or unclear attribution requirements

> 🛑 If you can’t explain **where it came from** and **how it can be used**, it doesn’t ship.

---

## 🧠 KFM rules applied to textures

KFM treats “things that show up in the UI” as **auditable assets** — textures included.

**Non-negotiables:**
- 🧾 **Provenance-first:** textures must be traceable (source + processing steps)
- 🧷 **Contract-first:** each texture has a lightweight metadata “contract” (sidecar JSON)
- ⚖️ **License-first:** every texture is shipped with explicit licensing + attribution

---

## 🗂️ Suggested layout

You may keep textures flat, but per-asset grouping scales better.

```text
📦 web/
└─ 🧱 assets/
   └─ 🎬 media/
      └─ 🧊 models-3d/
         ├─ 🧩 models/          # .glb/.gltf geometry
         ├─ 🧵 textures/        # 👈 you are here
         │  ├─ 🏷️ _meta/       # optional: manifests, shared credits
         │  ├─ 🗿 monument-rocks/
         │  │  ├─ monument-rocks__limestone__basecolor__v001.ktx2
         │  │  ├─ monument-rocks__limestone__basecolor__v001.meta.json
         │  │  ├─ monument-rocks__limestone__normal__v001.ktx2
         │  │  ├─ monument-rocks__limestone__normal__v001.meta.json
         │  │  └─ monument-rocks__limestone__orm__v001.ktx2
         │  └─ 🏛️ fort-scott/
         └─ 🧱 materials/       # optional: material defs / manifests
```

---

## 🏷️ Naming convention

**Goals:** stable URLs, predictable lookups, easy debugging.

### ✅ Recommended pattern

`<asset-id>__<material>__<map>__v###.<ext>`

Examples:
- `monument-rocks__limestone__basecolor__v001.ktx2`
- `monument-rocks__limestone__normal__v001.ktx2`
- `monument-rocks__limestone__orm__v001.ktx2`

### ✅ Rules

- 🔡 lowercase only
- ➖ use `-` or `_` (no spaces)
- 🧷 keep `asset-id` consistent with the model ID
- 🧭 version bumps (`v001 → v002`) when visuals materially change

---

## 🧩 Map types and suffixes

| Map type | Suffix | Color space | Notes |
| --- | --- | --- | --- |
| Base Color / Albedo | `basecolor` | sRGB | avoid baked lighting when possible |
| Normal | `normal` | Linear | tangent-space normal map |
| Occlusion-Roughness-Metallic | `orm` | Linear | **R=AO, G=Roughness, B=Metallic** |
| Metallic-Roughness | `mr` | Linear | glTF-style packing (often **G=Roughness, B=Metallic**) |
| Occlusion | `occlusion` | Linear | usually R channel |
| Emissive | `emissive` | sRGB | optional |
| Height / Displacement | `height` | Linear | optional; use sparingly |

> 💡 Prefer **ORM** to reduce texture count and requests.

---

## 📦 File formats

### ✅ Preferred (runtime)
- **`.ktx2`** (highly recommended for WebGL-friendly delivery)

### ✅ Acceptable fallbacks
- **`.png`** (alpha / crisp masks / UI-like textures)
- **`.jpg`** (photographic basecolor without alpha)

### ❌ Avoid
- `.tif`, `.exr`, `.bmp` in `web/` unless there’s a *very* specific reason

---

## ⚡ Performance guidelines

These are guidelines, not hard limits — but follow them unless you have a reason not to.

- 📐 Default texture size: **512–2048 px**
- 🏷️ Typical per-material set: **BaseColor + Normal + ORM**
- 🧼 Strip EXIF (and anything that can leak GPS/device info)
- 📉 Avoid 4K+ unless it’s a “hero” model and reviewed for web impact
- 🧊 Prefer mipmapped/compressed outputs for stable zooming and fewer artifacts

---

## 🧾 Provenance and license sidecars

Every texture should ship with a **sidecar metadata JSON**:

- Same basename + `.meta.json`
  - `...__basecolor__v001.ktx2`
  - `...__basecolor__v001.meta.json`

### ✅ Minimum fields to include

- `id` (stable asset identifier)
- `file` (the texture filename)
- `source` (where it came from, including URLs if applicable)
- `license` (SPDX identifier if possible + attribution text)
- `processing` (what steps/tools were applied)
- `integrity.sha256` (optional but strongly recommended)

### 🧪 Example `.meta.json`

```json
{
  "id": "urn:kfm:asset:texture:monument-rocks:limestone:basecolor:v001",
  "file": "monument-rocks__limestone__basecolor__v001.ktx2",
  "map_type": "basecolor",
  "color_space": "srgb",
  "source": {
    "kind": "photogrammetry|scan|hand-painted|generated",
    "origin": "Describe the original source or dataset",
    "retrieved": "YYYY-MM-DD",
    "url": "https://example.com/original/source",
    "author": "Original creator (if known)"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Attribution text KFM should display",
    "notes": "Any special constraints (e.g., non-commercial, share-alike, etc.)"
  },
  "processing": [
    { "step": "resize", "tool": "ImageMagick", "params": { "max_px": 2048 } },
    { "step": "compress", "tool": "toktx", "params": { "format": "ktx2", "mipmaps": true } }
  ],
  "integrity": {
    "sha256": "REPLACE_WITH_REAL_HASH"
  }
}
```

> ⚖️ **Policy:** If origin/license is unclear → don’t add it to `web/`. Move it to a scratch area and resolve licensing first.

---

## 🔁 Adding or updating textures

1. 🧵 Create the texture(s) (or export from DCC pipeline)
2. 📦 Convert to runtime format (`.ktx2` preferred)
3. 🏷️ Name it using the convention above
4. 🧾 Add the `.meta.json` sidecar
5. 🧩 Update the model/material references (paths must be correct relative to the served site)
6. 👀 Validate in the viewer (2D + optional 3D)

---

## ✅ Pre-commit checklist

- [ ] ✅ Naming convention followed (lowercase, stable, versioned)
- [ ] ✅ Correct suffix/map type used (`basecolor`, `normal`, `orm`, etc.)
- [ ] ✅ Color space is correct (sRGB vs Linear)
- [ ] ✅ Resolution + file size are web-reasonable
- [ ] ✅ Sidecar `.meta.json` exists and includes license + attribution
- [ ] ✅ No EXIF/GPS or unwanted metadata
- [ ] ✅ Model loads and renders correctly in the web viewer

---

## 🧯 Troubleshooting

<details>
<summary>🌀 Normal map looks “inside out”</summary>

- Try flipping the **green channel (Y)** during export.
- Confirm the renderer expects the same tangent-space convention as your authoring tool.
</details>

<details>
<summary>✨ Surface is too shiny / too matte</summary>

- Check roughness/metallic packing (ORM vs MR).
- Verify channel expectations in the material/shader.
</details>

<details>
<summary>🧩 Texture loads locally but not on GitHub Pages</summary>

- Ensure the path is correct and **case-sensitive**.
- Confirm the file is in `web/` and is being served with the site.
</details>

---

## 📚 Related docs

- 🌐 `web/` is the static front-end bundle (served directly to browsers)
- 🧾 Anything displayed in UI should have provenance + licensing information
- 🗺️ 3D may be used in the platform (e.g., Cesium-based views), so texture budgets matter even more

---
