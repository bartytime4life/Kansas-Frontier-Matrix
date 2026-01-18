# 🧱 Fort Scott — 3D Texture Pack (KFM) 🎨

![asset](https://img.shields.io/badge/asset-3D%20Textures-blue)
![pbr](https://img.shields.io/badge/shading-PBR%20(Metallic--Roughness)-informational)
![scope](https://img.shields.io/badge/scope-Fort%20Scott%20(KS)-success)
![target](https://img.shields.io/badge/target-web%20viewer%20assets-orange)

📍 **Path:** `web/assets/media/models-3d/textures/fort-scott/`  
🧭 **Purpose:** Web-ready, performance-conscious textures for Fort Scott-related 3D model(s) in the KFM experience.

---

## ✨ What lives in this folder?

This folder is for **optimized** texture maps (typically PBR) that are loaded by the **web viewer** (2D/3D) when rendering Fort Scott models.

✅ Put here:
- **Web-ready** texture maps (PNG / WebP / KTX2 — depending on pipeline)
- Material variants / LOD texture sets (if you support more than one resolution)
- A small manifest (optional, recommended) describing what each file is

🚫 Do **not** put here:
- Raw photogrammetry capture sets (hundreds of photos)
- High-bit-depth “source of truth” scans (unless specifically required)
- Gigantic working files (PSD/PSB/EXR) unless you have a strict reason + governance approval

---

## 🗂️ Recommended structure

```text
📁 web/assets/media/models-3d/textures/fort-scott/
├── 📄 README.md
├── 📄 manifest.texturepack.json        (optional, recommended)
├── 🖼️ fort-scott__walls__basecolor_2k.webp
├── 🖼️ fort-scott__walls__normal_2k.webp
├── 🖼️ fort-scott__walls__orm_2k.webp   (AO/Roughness/Metallic packed)
├── 🖼️ fort-scott__roof__basecolor_2k.webp
├── 🖼️ fort-scott__roof__normal_2k.webp
└── 🖼️ fort-scott__roof__orm_2k.webp
```

> Tip 💡: If you ship multiple resolutions, use consistent suffixes like `1k | 2k | 4k` (and keep them power-of-two when possible).

---

## 🧩 Texture “contract” (what we expect)

KFM assets are easiest to maintain when every material follows a predictable set of maps.

### ✅ Common PBR map set (Metallic–Roughness)
- **Base Color / Albedo**: `__basecolor__` (remember: **sRGB**)
- **Normal**: `__normal__` (linear)
- **ORM packed**: `__orm__` (linear)  
  - **R** = Ambient Occlusion  
  - **G** = Roughness  
  - **B** = Metallic

### Optional maps (only if needed)
- **Emissive**: `__emissive__` (sRGB)
- **Opacity / Alpha**: either embedded in baseColor alpha or separate `__opacity__`
- **Height**: `__height__` (linear) — only if parallax/displacement is supported

---

## 🏷️ Naming conventions (please don’t freestyle 😅)

Use **kebab-case** and keep names deterministic:

```text
fort-scott__<material_or_part>__<map>_<res>.<ext>
```

Examples:
- `fort-scott__brick__basecolor_2k.webp`
- `fort-scott__brick__normal_2k.webp`
- `fort-scott__brick__orm_2k.webp`

Rules of thumb:
- `fort-scott` stays constant for this folder (helps bundling + search)
- `<material_or_part>` should match the model’s material slot names **or** a stable internal naming map
- `<map>` is one of: `basecolor | normal | orm | emissive | opacity | height`
- `<res>` is `1k | 2k | 4k` (avoid ambiguous “hd”, “final”, “newnew2” 😭)

---

## ⚙️ Integration notes (WebGL / Cesium / 3D Tiles)

This folder is designed for **fast runtime loading**:
- Prefer **compressed formats** where your pipeline supports it (WebP/KTX2)
- Keep consistent UV assumptions per material
- Validate normal map handedness (OpenGL vs DirectX “green channel” flips)

If this texture pack is used in a **glTF/GLB** pipeline, the canonical PBR model is:

```json
{
  "pbrMetallicRoughness": {
    "baseColorTexture": { "index": 0 },
    "metallicRoughnessTexture": { "index": 1 }
  },
  "normalTexture": { "index": 2 },
  "occlusionTexture": { "index": 3 }
}
```

> Packing ORM reduces requests + improves load performance on the web 📉⚡

---

## 🧾 Provenance & licensing (required mindset ✅)

Even if these are “just textures,” they’re still **publishable artifacts** that should be traceable.

At minimum, track:
- Source capture (photos/scans), dates, contributors
- Tools used (photogrammetry / baking / compression)
- License + attribution requirements
- Any restrictions (privacy, cultural sensitivity, site protection)

### Optional: `manifest.texturepack.json` template

```json
{
  "id": "fort-scott-textures",
  "version": "0.1.0",
  "updated": "YYYY-MM-DD",
  "maps": [
    {
      "material": "walls",
      "baseColor": "fort-scott__walls__basecolor_2k.webp",
      "normal": "fort-scott__walls__normal_2k.webp",
      "orm": "fort-scott__walls__orm_2k.webp"
    }
  ],
  "provenance": {
    "source": "photogrammetry / archival / procedural",
    "contributors": [],
    "tools": [],
    "license": "TBD",
    "notes": ""
  }
}
```

---

## ✅ QA checklist (before merging)

- [ ] Texture names follow the folder contract (no “final_FINAL_v7”)
- [ ] Resolutions are consistent (and power-of-two if possible)
- [ ] BaseColor is **sRGB**; Normal/ORM/Height are **linear**
- [ ] Normal map looks correct (no “inside-out” lighting)
- [ ] Seams minimized (UV edges checked)
- [ ] File sizes are reasonable for web delivery
- [ ] Provenance + license info exists somewhere discoverable

---

## 🔗 Related docs (repo)

If present in this repo, these are the “north star” references:
- `docs/MASTER_GUIDE_v13.md`
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- `docs/standards/KFM_STAC_PROFILE.md`
- `docs/standards/KFM_DCAT_PROFILE.md`
- `docs/standards/KFM_PROV_PROFILE.md`

---

## 🧭 Why Fort Scott?

Fort Scott is a key Kansas history anchor point and is commonly referenced in conflict-era and settlement narratives. This texture pack exists so Fort Scott-themed 3D content can render consistently across KFM stories and views.

🧡 Keep it clean, fast, and provable.
