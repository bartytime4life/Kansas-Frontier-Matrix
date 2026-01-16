---
title: "🧩 PNG Textures — Shared 3D Texture Library"
path: "web/assets/3d/shared/textures/png/README.md"
version: "v1.0.0"
status: "active"
doc_kind: "Asset README"
last_updated: "2026-01-15"
license: "CC-BY-4.0"

# Protocols / governance
markdown_protocol_version: "KFM-MDP v11.2.6"
pipeline_contract_version: "TBD"
governance_ref: "TBD"
ethics_ref: "TBD"

# FAIR+CARE
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

# Identity
semantic_document_id: "kfm.web.assets.3d.shared.textures.png.readme"
doc_uuid: "urn:kfm:doc:web-assets:3d:shared:textures:png:readme:v1.0.0"
commit_sha: "<set-on-commit>"
doc_integrity_checksum: "sha256:<set-by-ci>"
---

# 🖼️ PNG Textures (Shared 3D Library)

![Format](https://img.shields.io/badge/format-PNG-4c1)
![Scope](https://img.shields.io/badge/scope-shared%20textures-08c)
![Use](https://img.shields.io/badge/3D-WebGL%20%7C%20Cesium%20%7C%20glTF-555)

Lossless **PNG** textures shared across multiple 3D assets (models, tilesets, landmarks) in KFM’s web delivery stack. Prefer this folder when **multiple** assets reuse the same texture and when PNG’s strengths matter (alpha, crisp masks, exact normals, UI-like detail).

> ✅ Rule of thumb: **PNG for alpha/masks/normal/ID maps**; **JPG for photo-like basecolor with no alpha**; **Atlases for packing many small textures**.

---

## 📘 Overview

### 🎯 Purpose
Provide a canonical home for **shared** PNG textures used by 3D assets so they remain:
- **Reusable** (no duplicate copies across models)
- **Auditable** (clear provenance + license)
- **Performant-ready** (optimized PNGs, predictable naming)

### 👥 Audience
- 🧑‍💻 Frontend + 3D pipeline devs (WebGL / Cesium / glTF)
- 🧱 Asset authors (Blender/Substance/etc.)
- 🧾 Reviewers doing license/provenance QA

---

## 🔭 Scope

| ✅ In Scope | ❌ Out of Scope |
|---|---|
| Shared PNG textures referenced by **multiple** assets | Landmark-only textures → `web/assets/3d/landmarks/<slug>/textures/` |
| PNGs requiring **alpha** (decals, cutouts, UI planes) | JPG-appropriate phototextures (no alpha) → `../jpg/` |
| Data textures (masks, ORM, IDs, normals) | Packed atlases → `../atlases/` |
| “Source-of-truth” PNGs that may be transcoded later | Generated outputs/cache artifacts |

---

## 🧭 Directory Map

```text
🌐 web/
└─ 🧊 assets/
   └─ 🧭 3d/
      └─ 🤝 shared/
         └─ 🧵 textures/
            ├─ 🟦 png/            ← (YOU ARE HERE)
            │  ├─ 🖼️ *.png
            │  ├─ 🧾 *.meta.json  (recommended; required for 3rd-party)
            │  └─ 📄 README.md
            ├─ 🟨 jpg/
            │  └─ 📄 README.md
            └─ 🧩 atlases/
               └─ 📄 README.md
```

---

## 🏷️ Naming Conventions

### ✅ Required
- **lower_case_with_underscores**
- No spaces, no Unicode punctuation, no `()`; keep paths URL-safe
- Stable names (treat names as API)

### 🧱 Recommended Pattern
Use a consistent suffix for meaning (channel + intent):

```
<theme_or_asset>_<material>_<channel>[_<variant>].png
```

**Channel suffixes (suggested):**
- `_basecolor` (or `_albedo`)
- `_normal` (tangent-space, OpenGL +Y unless noted)
- `_roughness`
- `_metallic`
- `_ao`
- `_emissive`
- `_opacity` / `_alpha`
- `_mask` (generic binary/soft mask)
- `_id` (flat-color ID map)

**Examples**
- `kfm_shared_woodplank_basecolor.png`
- `kfm_shared_woodplank_normal.png`
- `kfm_shared_signage_mask.png`
- `kfm_shared_decals_cracks_alpha.png`

---

## 🧪 Texture Technical Rules

### 📐 Dimensions & mipmaps
- Prefer **power-of-two** where mipmaps/repeat are expected: 256/512/1024/2048/4096
- Keep textures as small as quality allows (avoid 8K unless justified)

### 🎨 Color space (critical)
- **sRGB**: basecolor/albedo, emissive
- **Linear**: normal, roughness, metallic, AO, masks, IDs

> If you can’t guarantee correct color-space handling in the runtime, **document it** in `*.meta.json`.

### 🧼 Alpha rules
- Default: **straight alpha** (not premultiplied)
- If premultiplied alpha is required, document it explicitly in metadata.

### 🧭 Normal maps
- Tangent-space normals: `*_normal.png`
- If a texture is **DirectX (-Y)**, it must say so in metadata and/or be converted.

---

## ⚙️ Optimization Guidelines (PNG)

PNG is lossless, but it can still be **bloated** if exported naïvely.

✅ Recommended:
- Strip metadata unless required for provenance
- Run a lossless optimizer before commit (example tools: `oxipng`, `pngcrush`)
- For UI-style textures with limited colors, consider **palette PNG** (still lossless)

🚫 Avoid:
- Interlaced PNGs unless you have a specific streaming reason
- Unreviewed “lossy PNG” workflows unless the artifact is acceptable and documented

---

## 🧾 Provenance & Metadata

### ✅ Sidecar metadata (recommended; required for 3rd-party assets)
For any non-trivial or third-party texture, add:

- `my_texture.png`
- `my_texture.meta.json`

**Minimum recommended fields**
```json
{
  "asset_id": "kfm.web.assets.3d.shared.textures.png.my_texture",
  "source": {
    "kind": "original | derived | third_party",
    "origin": "TBD",
    "author": "TBD",
    "retrieved_at": "YYYY-MM-DD"
  },
  "license": {
    "spdx": "TBD",
    "attribution": "TBD",
    "source_url": "TBD"
  },
  "texture": {
    "channel": "basecolor | normal | roughness | metallic | ao | mask | emissive | id",
    "color_space": "srgb | linear",
    "alpha": "none | straight | premultiplied",
    "normal_convention": "opengl_plus_y | directx_minus_y"
  },
  "transform": {
    "tools": ["TBD"],
    "notes": "TBD"
  }
}
```

> 🧷 If a texture is generated/edited from another asset, record the transformation steps (tool + settings) in `transform`.

---

## 📜 Licensing & Attribution

- Every third-party PNG **must** be attributable and license-compatible.
- Put attribution in the `*.meta.json` and/or in the nearest relevant attribution document (project policy may require both).
- If in doubt: **don’t ship it** until provenance is clear.

---

## ✅ QA Checklist (Pre-Commit)

- [ ] Filename is `lower_case_with_underscores` and describes channel
- [ ] PNG opens/decodes correctly (no truncated chunks)
- [ ] Dimensions are appropriate (POT if mipmaps/repeat)
- [ ] Color space is correct **and recorded**
- [ ] File size is reasonable (no accidental 30MB exports)
- [ ] `*.meta.json` exists for any third-party or derived texture
- [ ] License + attribution are complete (SPDX where possible)

---

## 🔗 Related Docs

- 🟨 JPG textures: `../jpg/README.md`
- 🧩 Atlases: `../atlases/README.md`

---

## 📚 Sources

- KFM technical overview (architecture + web stack context):  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM Markdown governance + front-matter patterns:  [oai_citation:1‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  
