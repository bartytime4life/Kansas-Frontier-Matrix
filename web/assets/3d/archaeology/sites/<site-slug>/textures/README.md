# 🎨 Textures (PBR) — Archaeology Site `"<site-slug>"`

![KFM](https://img.shields.io/badge/KFM-Evidence--First-2ea44f)
![3D](https://img.shields.io/badge/3D-Archaeology%20Site%20Assets-blue)
![PBR](https://img.shields.io/badge/PBR-ready-informational)
![Preferred](https://img.shields.io/badge/Preferred-KTX2%20(BasisU)-8a2be2)
![Policy](https://img.shields.io/badge/Policy-Fail--Closed-critical)

> [!NOTE]
> This folder contains **web-ready** (runtime) texture assets for the archaeology site at:
> `web/assets/3d/archaeology/sites/<site-slug>/textures/`

---

## 🧭 Why this folder exists

KFM’s archaeology experiences (3D globe/terrain, guided stories, and optional AR-style overlays) can include **3D site models**. This `textures/` directory is the **single source of truth for runtime textures** used by those models—optimized for fast web delivery and consistent rendering across devices. 🗺️✨

---

## 📌 Golden rules (non‑negotiables)

✅ **1) Runtime-only in `web/assets/`**  
This folder is for **optimized deliverables** (what the web app actually loads).  
Raw captures (photogrammetry photos, scans, originals) should live in KFM’s *raw evidence* area (not here).

✅ **2) Evidence-first, always**  
Every texture set must be traceable to:
- its **source** (where it came from),
- its **license** (how we can use it),
- its **pipeline** (how it was produced / compressed / packed).

✅ **3) Sensitivity-aware** 🛡️  
If a texture could increase risk (e.g., revealing fragile or lootable site details), mark it as **restricted** and follow KFM sensitivity policy (including access control + generalization patterns where appropriate).

✅ **4) Performance budgets matter** ⚡  
Textures can be the #1 performance killer in WebGL/Cesium scenes. Favor **compressed** + **mipped** textures, and avoid shipping “artist originals” directly.

---

## 🗂️ Suggested folder layout

> [!TIP]
> You can keep everything flat for small sites, but subfolders per material are cleaner as a site grows.

```text
📁 web/assets/3d/archaeology/sites/<site-slug>/
├─ 📁 textures/  👈 you are here
│  ├─ 📄 README.md
│  ├─ 📄 textures.manifest.json        # required: provenance + license + mapping
│  ├─ 📄 checksums.sha256              # required: integrity & reproducibility
│  ├─ 📁 materials/
│  │  ├─ 📁 sandstone/
│  │  │  ├─ 🖼️ sandstone_baseColor.ktx2
│  │  │  ├─ 🖼️ sandstone_normal.ktx2
│  │  │  └─ 🖼️ sandstone_orm.ktx2
│  │  └─ 📁 timber/
│  │     ├─ 🖼️ timber_baseColor.ktx2
│  │     ├─ 🖼️ timber_normal.ktx2
│  │     └─ 🖼️ timber_orm.ktx2
│  └─ 📁 thumbnails/                   # optional: UI cards / story node previews
│     └─ 🖼️ preview.webp
└─ 📁 model/
   └─ 🧩 site.glb (or 3D Tiles tileset)
```

---

## 🧱 Naming convention

Use names that are:
- **stable** (don’t change paths unless absolutely required),
- **machine-friendly** (no spaces),
- **portable** across OS + CDNs.

### ✅ Recommended pattern
```text
<material>_<map>[_vNN].<ext>
```

Examples:
- `sandstone_baseColor_v01.ktx2`
- `sandstone_normal_v01.ktx2`
- `sandstone_orm_v01.ktx2`
- `plaster_emissive_v02.ktx2`

> [!IMPORTANT]
> **Keep `<map>` consistent.** This allows simple tooling + CI checks.

---

## 🧪 Map types (PBR expectations)

| Map (suffix) | Purpose | Color space | Notes |
|---|---|---:|---|
| `baseColor` | Albedo / diffuse | **sRGB** | Avoid baked lighting when possible |
| `normal` | Surface detail | **Linear** | Prefer OpenGL (+Y) normals |
| `orm` | Packed channels | **Linear** | **R=AO**, **G=Roughness**, **B=Metallic** |
| `emissive` | Glow | **sRGB** | Optional |
| `opacity` | Cutouts | Depends | Often embedded as alpha in `baseColor` |

> [!TIP]
> `orm` packing keeps bandwidth low and plays nicely with glTF-style PBR.  
> If a workflow requires separate AO/Roughness/Metallic maps, you *may* ship them separately—but document it in the manifest.

---

## 📦 File formats & compression

### ✅ Preferred
- **`.ktx2`** (Basis Universal / GPU-friendly)
  - Great for WebGL/Cesium performance
  - Small downloads
  - Mipmaps supported

### Allowed (fallback / special cases)
- `.png` (lossless; use sparingly—files get big fast)
- `.webp` (UI thumbnails; not recommended for PBR normals/ORM)
- `.jpg` (only for baseColor *when quality is acceptable*; avoid for ORM/normal)

> [!WARNING]
> Don’t commit giant uncompressed textures “because it’s temporary.”  
> KFM’s system design assumes artifacts are curated, validated, and reproducible.

---

## 📏 Resolution & performance budgets (practical)

**Aim for power-of-two** sizes (512, 1024, 2048, 4096) to maximize GPU friendliness + mipmapping.

### Suggested caps
- **Mobile-first / field use:** 1024–2048
- **Desktop story scenes:** 2048–4096 (only where it truly matters)
- **Hero assets:** 4096 max, *and only a few*

> [!TIP]
> If you need extreme detail, prefer **detail normal tiling** + **trim sheets** over pushing every material to 8K.

---

## 🧾 Required metadata: `textures.manifest.json`

KFM’s philosophy treats every output as an auditable artifact. This manifest is the “receipt” that makes textures:
- discoverable,
- reviewable,
- safe to publish.

### ✅ Minimal manifest example
```json
{
  "site": "<site-slug>",
  "updated": "YYYY-MM-DD",
  "textures": [
    {
      "id": "sandstone",
      "maps": {
        "baseColor": "materials/sandstone/sandstone_baseColor_v01.ktx2",
        "normal": "materials/sandstone/sandstone_normal_v01.ktx2",
        "orm": "materials/sandstone/sandstone_orm_v01.ktx2"
      },
      "license": {
        "spdx": "CC-BY-4.0",
        "attribution": "Source org / author name",
        "source_url": "https://example.org/source"
      },
      "provenance": {
        "inputs": [
          "data/raw/archaeology/sites/<site-slug>/photogrammetry/<capture-id>/"
        ],
        "pipeline": "pipelines/archaeology/texture_bake_v1",
        "tool_versions": {
          "blender": "4.x",
          "gltf-transform": "x.y.z",
          "toktx": "x.y.z"
        }
      },
      "sensitivity": {
        "classification": "public",
        "notes": "Set to restricted if this texture increases site-risk."
      }
    }
  ]
}
```

> [!NOTE]
> The exact pipeline paths may differ per repo layout—what matters is that the manifest captures **inputs + method + license + classification** in a consistent schema.

---

## 🔐 Sensitive content & cultural protocols

Archaeology can be sensitive. **Textures can leak context** (identifiable features, tool marks, exact surface detail, or content that communities consider restricted).

**When in doubt:**
- mark the texture as `restricted`,
- avoid publishing to public builds,
- consult KFM governance/sensitivity policies.

> [!IMPORTANT]
> Also scrub metadata: raw images and some conversions may preserve EXIF/GPS or author info.  
> Don’t ship private coordinates or identifying metadata in publicly served files.

---

## ✅ Integrity: `checksums.sha256`

Every committed texture should be listed in a checksum file to support:
- reproducibility,
- caching correctness,
- provenance linking,
- supply-chain confidence.

Suggested format:
```text
<sha256>  materials/sandstone/sandstone_baseColor_v01.ktx2
<sha256>  materials/sandstone/sandstone_normal_v01.ktx2
<sha256>  materials/sandstone/sandstone_orm_v01.ktx2
```

---

## 🧰 Adding or updating textures (quick workflow)

1) **Create/obtain sources** 🧪  
   Capture or acquire source imagery/scans (store as raw evidence elsewhere).

2) **Bake PBR maps** 🎛️  
   Generate `baseColor`, `normal`, and `orm` (or equivalent).

3) **Compress to KTX2** 📦  
   Generate mipmaps and confirm visual parity.

4) **Place outputs here** 📁  
   Keep naming consistent + paths stable.

5) **Update `textures.manifest.json`** 🧾  
   Include license + provenance + classification.

6) **Update `checksums.sha256`** 🔍  
   Add SHA-256 for every new/changed file.

7) **Validate in the viewer** 🧭  
   Check seams, normal direction, roughness response, and lighting consistency.

---

## 🧯 Troubleshooting

<details>
<summary>🟣 My normals look inverted / “puffy”</summary>

- Confirm normal orientation (OpenGL vs DirectX).  
- Ensure the normal texture is treated as **linear**, not sRGB.  
- Verify tangent space matches your exporter (especially if baking outside Blender).

</details>

<details>
<summary>🟠 Roughness/metallic look wrong</summary>

- Confirm channel packing: `orm` should be **R=AO**, **G=Roughness**, **B=Metallic**.  
- Ensure `orm` is **linear** (no gamma correction).  
- Check that the material interprets roughness correctly (some tools invert glossiness/roughness).

</details>

<details>
<summary>🔴 The site is slow to load</summary>

- Texture sizes are usually the culprit.  
- Audit:
  - too many unique materials,
  - too-high resolutions,
  - missing mipmaps,
  - uncompressed PNGs.
- Consider atlasing/trim sheets and reduce variants.

</details>

---

## 🔗 How textures connect to the bigger KFM system

- 🧠 **AI + Knowledge Graph:** Textures (and the 3D assets they support) should be linkable as “assets” in the site’s record, enabling traceability in stories and AI explanations.
- 📚 **Story Nodes:** If a story node “stops” at this site in 3D, the textures are part of the reproducible evidence chain.
- 📡 **Offline / field packs:** Keep assets structured and manifest-driven so they can be bundled for offline use without losing context.

---

## 📚 Reference library (project-aligned)

These project documents shaped the standards in this README (provenance-first ingestion, policy gates, UI traceability, AR/3D direction, and sensitivity governance):

- 🧭 KFM UI / Storytelling / 2D+3D concepts
- 🧱 KFM Architecture, policy gates, metadata backbone (STAC/DCAT/PROV)
- 📥 KFM Data Intake (immutability, deterministic pipelines, provenance)
- 🤖 KFM AI System Overview (retrieval + explainability direction)
- 🧩 Open-source geospatial mapping hub design notes (pipelines + traceability)
- 🧠 Innovative concepts (AR storytelling + cultural protocols)
- 🧪 Data mining/privacy concepts (sensitive output risk)
- 🗺️ Geospatial visualization cookbook (Three.js/DEM/orthophoto workflows)
- 📚 Supporting reference portfolios (AI/graphics/programming/data management)

> [!TIP]
> If you’re adding a brand-new site, consider writing a small “site dossier” (narrative + evidence) that links the 3D model + textures to their sources. That’s the KFM way. ✅

