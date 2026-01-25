# 🧼 Grime Decal Textures

![asset](https://img.shields.io/badge/asset-3D%20decal%20textures-blue)
![category](https://img.shields.io/badge/category-grime%20%26%20weathering-6c757d)
![pbr](https://img.shields.io/badge/PBR-glTF%20metal%2Froughness-success)
![provenance](https://img.shields.io/badge/provenance-source.json%20%2B%20checksums.sha256-critical)

📍 **Path:** `web/assets/3d/shared/textures/decals/grime/`  
⬅️ **Up one level:** `../` (decals)

---

## 📌 What this folder is

This folder holds **grime / weathering decal textures** used to add believable dirt, soot, stains, splatter, and age to 3D surfaces (without baking that detail into every model). Think: wagon wheels, brick facades, trail markers, fort interiors, signage, artifacts, terrain props, etc.

Decals are especially useful for KFM’s **3D globe / terrain storytelling** and future **AR overlays** because they let us “age” a scene dynamically while keeping core 3D assets reusable. 🧭✨

---

## 🧭 When to use grime decals (vs. tiling materials)

Use grime decals when you need:

- ✅ **Localized** wear (a stain under a window, soot near a chimney, mud splash along a wall)
- ✅ **Story-specific** details (a building looks different in different timeline eras)
- ✅ **Reusable models** that get “context dressing” at runtime

Avoid decals when you need:

- ❌ A fully repeating surface material (use a tiling PBR material instead)
- ❌ Massive unique baked detail that should live in the base model textures

---

## ✅ What belongs here

- 🟦 **Runtime-ready textures** intended for web rendering (prefer GPU-friendly formats where supported)
- 🧩 **Decal masks / alphas** (grime decals typically rely on alpha)
- 🧾 **Attribution + provenance sidecars** (see `source.json`)
- 🔐 **Checksums** for auditability (see `checksums.sha256`)
- 🖼️ **Lightweight preview images** for humans (e.g., `preview.webp`)

---

## 🚫 What does NOT belong here

> [!IMPORTANT]
> This directory is for **web-runtime outputs**. Editable sources are usually huge and slow CI down.

- ❌ Large editable sources (`.psd`, `.kra`, `.spp`, `.sbs`, `.blend`)  
- ❌ Unlicensed / unknown-origin textures
- ❌ Any imagery with recognizable logos/brands, copyrighted art, or “pulled from Google”
- ❌ “Mystery meat” files with no metadata (these should fail CI by design)

---

## 🧱 PBR decal map conventions

KFM decals follow **glTF 2.0 metal/rough** expectations (even when used outside glTF).

### Required (minimum viable decal)
| Map | Purpose | Notes |
|---|---|---|
| **Base Color + Alpha** | Color + decal cutout | Alpha = decal mask (straight alpha) |

### Recommended (best results)
| Map | Purpose | Notes |
|---|---|---|
| **Normal** | Adds depth without geometry | Use **OpenGL (+Y)** normal convention |
| **ORM** (Occlusion/Roughness/Metallic) | Material response | **R=AO, G=Roughness, B=Metallic** (glTF packing) |

### Color space rules 🎨
- **sRGB:** Base Color (and Emissive if ever used)
- **Linear:** Normal, ORM, Roughness, Metallic, AO, Height

### Alpha rules ✂️
- Use **straight (un-premultiplied) alpha**
- Include **edge dilation** (a few pixels) to prevent dark halos when mipmapped

---

## 🗂️ Recommended folder structure

This structure scales well as the library grows and keeps provenance attached to each decal:

```text
web/assets/3d/shared/textures/decals/grime/
├─ 📄 README.md                          # 📘 Decal rules: structure, metadata, usage (e.g., dirt, leaks, soot, wear)
├─ 🧾 manifest.json                     # Optional index for tooling and runtime (maps decals to metadata)
├─ 💧 grime_splatter_a/                   # Decal unit: grime splatter (splat, residue)
│  ├─ 💨 grime_splatter_a_basecolor_1024.ktx2   # Basecolor texture (PBR)
│  ├─ 🌪 grime_splatter_a_normal_1024.ktx2      # Normal map (surface detail)
│  ├─ 🛠 grime_splatter_a_orm_1024.ktx2         # ORM map (occlusion, roughness, metallic)
│  ├─ 🌄 preview.webp                    # Small thumbnail for quick asset preview (optional)
│  ├─ 🧾 source.json                    # Metadata: asset origin, licensing, author, etc.
│  └─ 🔑 checksums.sha256                # Integrity checksum for file verification
└─ 💧 grime_streaks_vertical_b/            # Decal unit: grime streaks (vertical drips, streaking dirt)
   ├─ 💨 grime_streaks_vertical_b_basecolor_1024.ktx2   # Basecolor texture (PBR)
   ├─ 🌪 grime_streaks_vertical_b_normal_1024.ktx2      # Normal map (surface detail)
   ├─ 🛠 grime_streaks_vertical_b_orm_1024.ktx2         # ORM map (occlusion, roughness, metallic)
   ├─ 🌄 preview.webp                    # Small thumbnail for quick asset preview (optional)
   ├─ 🧾 source.json                    # Metadata: asset origin, licensing, author, etc.
   └─ 🔑 checksums.sha256                # Integrity checksum for file verification
```

> [!NOTE]
> If the library is small, you *can* keep textures in the folder root — but once you pass ~10 decals, per-decal folders prevent chaos. 😄

---

## 🏷️ Naming convention (contract)

**Rule of thumb:** predictable names = predictable loading + easier caching.

**Pattern:**
```
grime_<descriptor>_<variant>_<map>_<resolution>.<ext>
```

**Examples:**
- `grime_splatter_a_basecolor_1024.ktx2`
- `grime_splatter_a_normal_1024.ktx2`
- `grime_splatter_a_orm_1024.ktx2`
- `grime_streaks_vertical_b_basecolor_512.webp`

### Map suffixes (standard)
- `basecolor` (includes alpha for decals)
- `normal`
- `orm`
- `roughness` (only if you’re not packing ORM)
- `ao` (only if you’re not packing ORM)
- `metallic` (rare for grime decals; usually ~0)

---

## 📦 Formats & performance guidance (web-first)

### Prefer ✅
- **KTX2** (`.ktx2`) for GPU-friendly delivery (mipmapped, compressed)
- Power-of-two textures where possible (256/512/1024/2048)

### Acceptable 👍
- **WebP** for previews and lightweight albedo-only decals
- **PNG** as a fallback or “source-of-truth output” when compression tooling isn’t wired up yet

### Avoid ❌
- Giant unique textures unless there’s a strong reason (web memory is finite)
- Non–power-of-two sizes unless you’ve verified the renderer’s mip + sampling behavior
- Shipping dozens of unique 4K decals when 1K would do

> [!TIP]
> If you need *lots* of decals on screen: consider **atlasing** (many decals packed into one texture) to reduce texture binds.

---

## 🔒 Provenance & governance (yes, even for textures)

KFM treats *everything visible* as auditable — decals included. 🧾🔍  
Each decal **must** carry origin + license metadata and integrity hashes.

### `source.json` (required)
Keep it short, but complete. Example:

```json
{
  "asset_id": "kfm.decals.grime.grime_splatter_a",
  "title": "Grime Splatter A",
  "description": "Mud + dust splatter decal for exterior surfaces.",
  "license": "CC-BY-4.0",
  "attribution": "Your Name (or Organization)",
  "created": "2026-01-25",
  "tags": ["grime", "mud", "splatter", "decal"],
  "source": {
    "method": "procedural | hand-painted | photogrammetry | mixed",
    "derived_from": [
      {
        "type": "photo",
        "title": "Reference photo set (optional)",
        "where": "path-or-url-if-allowed",
        "license": "license-if-applicable"
      }
    ]
  },
  "build": {
    "toolchain": ["optional: Substance/PS/GIMP", "optional: basisu/ktx2"],
    "notes": "Any important processing notes go here."
  },
  "ai_assistance": {
    "used": false,
    "model": null,
    "prompt": null,
    "seed": null
  }
}
```

### `checksums.sha256` (required)
A simple hash list for integrity/audit:

```text
<sha256>  grime_splatter_a_basecolor_1024.ktx2
<sha256>  grime_splatter_a_normal_1024.ktx2
<sha256>  grime_splatter_a_orm_1024.ktx2
<sha256>  preview.webp
<sha256>  source.json
```

---

## 🧪 QA checklist (Definition of Done)

Before you open a PR, confirm:

- [ ] ✅ `source.json` exists and includes **license + attribution**
- [ ] ✅ `checksums.sha256` exists and matches the committed files
- [ ] ✅ Basecolor includes a clean **alpha mask** (no jagged edges unless intentional)
- [ ] ✅ No halo/fringe on edges (dilation + correct alpha handling)
- [ ] ✅ Normal map (if present) is **OpenGL +Y**
- [ ] ✅ ORM packing matches **R=AO, G=Roughness, B=Metallic**
- [ ] ✅ Preview exists (`preview.webp`) and is representative
- [ ] ✅ File sizes are reasonable for web delivery (no accidental multi‑MB PNGs if KTX2 is available)

---

## 🤝 Contribution workflow (quick)

1. 🧩 Add a new decal folder: `grime_<something>_<variant>/`
2. 🎨 Export maps (BaseColor+Alpha minimum; Normal/ORM recommended)
3. ⚡ Produce optimized runtime textures (prefer `.ktx2` if supported in tooling)
4. 🧾 Add `source.json`
5. 🔐 Generate `checksums.sha256`
6. ✅ Run whatever asset validation / CI checks exist for KFM

---

## 🔗 See also

- `web/assets/3d/shared/textures/decals/` (parent category)
- KFM UI principles: **accessibility, modularity, transparency**
- KFM offline/field direction: **offline packs** + future **AR experiences**
- KFM governance direction: **metadata-first + policy enforcement**

