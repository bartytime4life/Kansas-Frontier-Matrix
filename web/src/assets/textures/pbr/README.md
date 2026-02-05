<div align="center">

# 🧱 PBR Texture Library

**📍 Path:** `web/src/assets/textures/pbr/`  
**🎯 Goal:** consistent, performant **Physically Based Rendering (PBR)** materials for the KFM web client

![PBR](https://img.shields.io/badge/PBR-metal%2Froughness-6f42c1?logo=webgl&logoColor=white)
![Target](https://img.shields.io/badge/Target-CesiumJS%20%2B%20WebGL-0b7285)
![Policy](https://img.shields.io/badge/Policy-Provenance%20First-orange)

</div>

---

## ✨ What this folder is for

KFM’s web front-end is a **React/TypeScript** map application that supports **2D maps (MapLibre GL JS)** and a **3D globe/terrain view (CesiumJS)**.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

This folder contains **PBR texture sets** used by our **3D materials** (e.g., glTF / 3D Tiles / custom WebGL shaders) and any other “material-like” visuals that benefit from physically-based shading.

KFM’s UI bundles styles plus static assets (images/icons) inside the web app, so we keep these textures versioned in-repo for reproducibility and consistent builds.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> 🧾 **Provenance-first rule (applies here too):** KFM’s system principle is that *nothing enters without provenance* and black-box outputs are unacceptable. Every texture set must have a source + license trail.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 When to use these textures

### UI / decorative use
If an image is purely visual design (not semantic content), prefer CSS `background-image` rather than an `<img>` tag.  [oai_citation:3‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

### 3D / material use
Use these textures when:
- a 3D model (glTF) needs physically plausible shading (roughness/metalness, normals, AO, etc.)
- a Cesium scene needs a tileable material (e.g., terrain-like surfaces, stylized “Kansas sandstone,” etc.)
- you’re building a reusable “material kit” for scenes, overlays, or 3D storytelling elements

---

## 📁 Folder layout

We store textures as **named sets** (one folder per material), plus shared utilities.

```text
📂 web/src/assets/textures/pbr/
├── 📄 README.md
├── 📂 _shared/                      # reusable masks, noise, LUTs (if needed)
│   └── 📄 (optional assets)
└── 📂 <material-slug>/              # one material per folder
    ├── 🖼️ <material-slug>_basecolor.(png|jpg)
    ├── 🖼️ <material-slug>_normal.(png)
    ├── 🖼️ <material-slug>_roughness.(png)
    ├── 🖼️ <material-slug>_metallic.(png)
    ├── 🖼️ <material-slug>_ao.(png)
    ├── 🖼️ <material-slug>_height.(png)         # optional
    ├── 🖼️ <material-slug>_emissive.(png)       # optional
    ├── 🖼️ <material-slug>_orm.(png)            # optional packed map (AO/Rough/Metal)
    ├── 🧾 meta.json                             # REQUIRED: provenance + license summary
    └── 📜 LICENSE.txt                           # REQUIRED if not covered by repo-wide policy
```

---

## 🏷️ Naming conventions

### Material slug
- ✅ `kebab-case` (lowercase, hyphens)
- ✅ short but descriptive
- ✅ Kansas-friendly when relevant (`flint-hills-limestone`, `prairie-dirt`, `red-clay`, etc.)

**Examples**
- `prairie-dirt`
- `limestone-block`
- `weathered-wood`

### File naming pattern
```
<material-slug>_<map-type>.<ext>
```

---

## 🧩 Supported PBR maps

> We use the **metallic/roughness** workflow (glTF-friendly).

| Map Type | Suffix | Typical Use | Color Space | Notes |
|---|---|---:|---|---|
| Base Color (Albedo) | `_basecolor` | ✅ Required | **sRGB** | No baked lighting if possible |
| Normal (Tangent) | `_normal` | Optional | Linear | Prefer OpenGL-style normals (Y+) |
| Roughness | `_roughness` | Optional | Linear | White = rough (matte), black = smooth |
| Metallic | `_metallic` | Optional | Linear | White = metal, black = dielectric |
| Ambient Occlusion | `_ao` | Optional | Linear | Often packed in ORM |
| Height / Displacement | `_height` | Optional | Linear | Use sparingly (expensive) |
| Emissive | `_emissive` | Optional | sRGB | For glow/signage effects |

### 🎛️ Packed texture (recommended for web performance)
**ORM** convention:
- **R = AO**
- **G = Roughness**
- **B = Metallic**

File: `<material-slug>_orm.png`

---

## 🗜️ Formats & compression guidelines

Image format choices matter: incorrect formats and uncompressed assets can balloon download size and harm performance.  [oai_citation:4‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

### Recommended defaults
- **Base color:** `.jpg` (if photographic) or `.png` (if needs crisp edges/alpha)
- **Normals / Roughness / Metallic / AO / ORM / Height:** `.png` (lossless, stable values)
- Avoid unnecessary alpha channels (alpha costs memory)

> 💡 Designers may mix formats across assets to keep quality high *and* file sizes sane (e.g., a PNG asset alongside JPG assets when needed).  [oai_citation:5‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

### Quick rules of thumb
- Use PNG for **limited-color** / **hard-edge** graphics (logos, masks, UI shapes).  [oai_citation:6‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)
- Use JPG for **photos** / high-color images where small loss is acceptable.
- Always **compress** (exporting “correct format” isn’t enough).  [oai_citation:7‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

---

## 📏 Resolution & tiling standards

### Size
- ✅ power-of-two where possible: `256 / 512 / 1024 / 2048 / 4096`
- ✅ start at `1024` for most tiling materials
- ✅ reserve `2048+` for hero assets only

### Tiling
- If a texture is meant to repeat: make it **seamless** (tileable) and test at multiple scales.
- Avoid strong directional lighting baked into basecolor (it fights dynamic lighting).

---

## 🧾 Provenance & licensing

Because KFM is provenance-first, every texture set must include `meta.json` (and `LICENSE.txt` when applicable).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### `meta.json` minimum schema

```json
{
  "material": "prairie-dirt",
  "source": {
    "name": "Example Pack Name",
    "author": "Author or Organization",
    "url": "https://example.com/source",
    "license": "CC-BY-4.0",
    "licenseUrl": "https://creativecommons.org/licenses/by/4.0/"
  },
  "ingestion": {
    "addedBy": "github-handle",
    "addedAt": "2026-02-05",
    "tools": ["Substance Painter", "GIMP"],
    "notes": "Any edits, channel packing, scale, etc."
  },
  "technical": {
    "workflow": "metallic-roughness",
    "packedMaps": ["orm"],
    "colorSpace": {
      "basecolor": "sRGB",
      "dataMaps": "linear"
    }
  }
}
```

> 🔒 If a texture’s license is unclear, treat it as **non-shippable** until resolved.

---

## ➕ Adding a new texture set

1. **Create a folder**: `web/src/assets/textures/pbr/<material-slug>/`
2. Add maps using the naming pattern:
   - `<slug>_basecolor.(png|jpg)`
   - `<slug>_normal.png` (optional)
   - `<slug>_orm.png` (recommended) **or** separate `_roughness/_metallic/_ao`
3. Add **`meta.json`** with full provenance & license
4. Add **`LICENSE.txt`** if the license text must travel with the asset
5. Verify:
   - no accidental gamma on data maps (normals/roughness/metallic/ao)
   - file sizes are reasonable and compressed (textures can “make or break” performance)  [oai_citation:9‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

---

## 🧪 QA checklist

- [ ] Filenames match `<slug>_<map>.<ext>`
- [ ] Base color is **sRGB**; data maps are **linear**
- [ ] Normal map looks correct (no “inside-out” shading / green channel mismatch)
- [ ] Resolution is appropriate (avoid 4K unless justified)
- [ ] ORM packing correct (R=AO, G=Roughness, B=Metallic) if used
- [ ] `meta.json` present and complete
- [ ] License is compatible with project distribution

---

## 🔗 Source PDFs used while authoring this README

- KFM Technical Blueprint  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Learn to Code HTML & CSS (Shay Howe)  [oai_citation:11‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- Professional Web Design Techniques & Templates  [oai_citation:12‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  

---
