---
title: "KFM 🧱 3D Materials Library"
path: "web/assets/3d/shared/materials/library/README.md"
version: "v0.1.0"
last_updated: "2026-01-25"
status: "active"
doc_kind: "Asset Library README"
audience:
  - "3D Artists / Asset Authors"
  - "WebGL Developers (CesiumJS / Three.js)"
  - "Data Stewards (Provenance / Licensing)"
defaults:
  pbr_workflow: "metallicRoughness"
  sensitivity: "public"
  license: "TBD"
---

# 🧱 3D Materials Library (Shared)  

![PBR](https://img.shields.io/badge/PBR-metallic--roughness-blue)
![WebGL](https://img.shields.io/badge/WebGL-ready-success)
![CesiumJS](https://img.shields.io/badge/CesiumJS-compatible-informational)
![Governance](https://img.shields.io/badge/Governance-provenance%20%2B%20licensing-important)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-purple)

Welcome to the **shared, runtime-ready** material library for KFM’s web 3D experiences 🌎✨  
This directory exists so we can reuse **consistent, performant, well-documented** materials across:

- 🗺️ **2D/3D storytelling workflows** (Map + story nodes)
- 🌐 **3D globe/terrain & time-dynamic scenes** (CesiumJS-first)
- 🧪 **Experimental WebGL prototypes** (e.g., Three.js terrain/scene tests)
- 📦 **Offline/field “data packs”** where assets must be portable, cached, and attributable

> [!IMPORTANT]
> **Everything in `library/` is expected to be ship-ready.**  
> If it can’t be shipped (license missing, provenance unclear, huge/unoptimized textures), it doesn’t belong here.

---

## 🧭 What belongs here

✅ **In scope**
- PBR material packs (textures + metadata) intended for **glTF / 3D Tiles / Three.js** usage
- Shared “utility” materials (selection highlight, ghost/preview, heat/pulse glow, mask materials)
- Period-aware materials used for historical reconstruction (optional time validity metadata)

🚫 **Out of scope**
- Raw scan source folders, photogrammetry dumps, camera originals
- `.blend`, `.sbs/.sbsar`, heavy authoring files (put those in a dedicated source/art pipeline area)
- Unlicensed textures or “found online” images without explicit reuse permission
- UI icons (those belong in UI asset folders, not 3D materials)

---

## 🗂️ Directory layout

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🤝 shared/
            └── 🧱 materials/
                └── 📚 library/
                    ├── 🧾 index.json                         (recommended: catalog for UI + loaders)
                    ├── 🧰 _templates/                        (starter packs; copy to create new materials)
                    │   ├── 🧾 material.json
                    │   └── 🏷️ ATTRIBUTION.md
                    └── 🏷️ <material-id>/                     (one folder per material pack)
                        ├── 🧾 material.json                   ✅ required (machine-readable metadata contract)
                        ├── 🏷️ ATTRIBUTION.md                  ✅ required (human-readable credits + context)
                        ├── 📜 LICENSE                         ✅ required (license text or pointer)
                        ├── 🖼️ preview.webp                    ✅ required (small/fast preview)
                        ├── 🏞️ preview_full.webp               ⭐ optional (nicer hero preview)
                        ├── 🧵 textures/
                        │   ├── 🎨 baseColor.(ktx2|png|jpg)
                        │   ├── 🧊 normal.(ktx2|png)
                        │   ├── 🪙 metallicRoughness.(ktx2|png)  (if metallic-roughness workflow)
                        │   ├── 🌑 occlusion.(ktx2|png)          (optional)
                        │   ├── ✨ emissive.(ktx2|png)           (optional)
                        │   └── 🏔️ height.(png|exr)             (optional: parallax/displacement)
                        └── 🧪 samples/
                            ├── 🪩 sphere.glb                   (optional: quick sanity check)
                            └── 📝 notes.md                     (optional: authoring decisions, gotchas)
```

> [!TIP]
> Keep `preview.webp` **small** (e.g., 512px wide). This helps any in-app “material picker” stay snappy.

---

## 🧩 Material ID rules (naming conventions)

We name folders and `material.json.id` so they are:
- **stable** (can be referenced from story nodes / glTF exports)
- **human-scannable**
- **sortable**

### ✅ Recommended format
`<domain>_<material-name>__v<major>`

Examples:
- `terrain_prairie_soil__v1`
- `built_aged_brick__v2`
- `ui_pulse_glow__v1`

### Rules
- lowercase only
- use `_` between words
- use `__v<major>` for breaking changes (texture set changes, workflow swap, scale change)

---

## 🎛️ PBR workflow expectations

Default workflow: **Metallic/Roughness** (glTF-friendly)

### Texture map conventions
| Map | File name | Color space | Notes |
|---|---|---|---|
| Base Color | `baseColor.*` | sRGB | no baked lighting if possible |
| Normal | `normal.*` | linear | tangent-space normal |
| MetallicRoughness | `metallicRoughness.*` | linear | packed map (common in glTF) |
| Occlusion | `occlusion.*` | linear | often packed in glTF “occlusionTexture” |
| Emissive | `emissive.*` | sRGB | for glow/pulse/markers |
| Height | `height.*` | linear | optional; used for parallax/displacement |

> [!NOTE]
> If a material uses a **non-default workflow** (spec/gloss, custom shader, etc.), it must be explicitly declared in `material.json` and include a minimal sample asset in `samples/`.

---

## ⚡ Performance & web-delivery guidelines

### Texture sizing
- Prefer power-of-two (512 / 1024 / 2048)
- Avoid > 4K unless there is a measured need
- Keep total pack size reasonable (think “offline pack friendly”)

### Compression
- Prefer `.ktx2` for runtime delivery when available
- Use `.png` for masks/height where compression artifacts hurt
- Use `.jpg` for photographic baseColor if it materially reduces size and artifacts are acceptable

### Determinism
- Avoid “mystery transforms” in the repo
- If a texture is derived (downscaled, converted, compressed), record that in metadata so we can reproduce it later

---

## 🧾 `material.json` (metadata contract)

This file is both:
- 🧠 **a loader contract** (what files exist / how to interpret them)
- 🧬 **a provenance & licensing anchor** (where did it come from / can we ship it)

### Minimal required fields
```json
{
  "id": "terrain_prairie_soil__v1",
  "title": "Prairie Soil",
  "description": "Neutral prairie soil used for terrain patches and recon scenes.",
  "pbr_workflow": "metallicRoughness",
  "scale_meters_per_tile": 1.0,
  "maps": {
    "baseColor": "textures/baseColor.ktx2",
    "normal": "textures/normal.ktx2",
    "metallicRoughness": "textures/metallicRoughness.ktx2"
  },
  "attribution": {
    "author": "TBD",
    "source": "TBD",
    "license": "TBD"
  },
  "governance": {
    "sensitivity": "public",
    "care_label": "n/a",
    "restrictions": []
  },
  "version": "1.0.0"
}
```

### Strongly recommended fields (make the system smarter)
- `tags`: `["soil", "prairie", "kansas"]`
- `ontology_refs`: `["kfm:material/soil", "kfm:biome/prairie"]`
- `time_validity`: `{ "start": "1854-01-01", "end": "1900-12-31" }` (for historical recon / 4D scenes)
- `checksums`: `{ "sha256": { "textures/baseColor.ktx2": "..." } }`
- `derived_from`: list of source assets (IDs, URLs, archive refs, or internal evidence IDs)

> [!IMPORTANT]
> If we can’t answer **“Where did this come from?”** and **“Are we allowed to ship it?”** from this metadata, the material is not complete.

---

## 🧠 How KFM uses this library

### 1) Story-driven 3D scenes (map + story nodes)
Materials here are intended to be referenced by:
- glTF models used in story scenes
- 3D overlays / reconstructions
- highlight/pulse materials to draw attention during narrative playback

### 2) Cesium-first rendering
Cesium tends to consume:
- glTF materials embedded in models, or
- external textures referenced by models / tilesets

This library gives us a **single source of truth** for shared textures, attribution, and performance constraints.

### 3) Offline & field-friendly packaging
When we bundle “offline data packs,” we want:
- predictable file paths
- small preview images
- explicit licensing & provenance
- controlled footprint

---

## 🛡️ Governance, sensitivity, and “don’t leak” rules

Some assets can be **technically “non-personal”** but still sensitive when combined or rendered in context.

### Required governance stance
Each material must declare a sensitivity classification in `material.json.governance`:
- `public`
- `restricted`
- `sensitive`
- `sacred_or_cultural` (or project-defined equivalent)

If a material is:
- derived from restricted imagery,
- tied to culturally sensitive designs,
- likely to reveal a protected site/location when used in context,

…then it must be marked appropriately and may require review before shipping.

> [!WARNING]
> **Outputs can leak information.**  
> Even “derived” assets can reveal sensitive source context when combined with other layers, time sliders, or narrative playback.

---

## ✅ Contribution workflow (add a new material)

1. 📁 Copy `_templates/` → `library/<your-material-id>/`
2. 🧾 Fill `material.json` (don’t leave provenance/licensing as “TBD” for long)
3. 🪪 Add `LICENSE` + `ATTRIBUTION.md`
4. 🖼️ Add `preview.webp`
5. 🎛️ Add textures under `textures/` using naming conventions
6. 🧪 (Optional but recommended) add a `samples/sphere.glb`
7. 🧹 Validate:
   - filenames match metadata
   - textures are correct color space & dimensions
   - file sizes are sane
8. 🧾 Update `index.json` (if we’re using it) so the UI/loader can discover it

---

## 🧪 PR checklist (definition of done)

- [ ] `material.json` exists + valid JSON
- [ ] `ATTRIBUTION.md` exists and is accurate
- [ ] `LICENSE` exists and matches `material.json.attribution.license`
- [ ] Preview image exists (`preview.webp`)
- [ ] Textures are optimized (no accidental 8K)
- [ ] Governance fields filled (sensitivity + restrictions)
- [ ] Any “derived from” sources are listed
- [ ] (If time-dynamic) `time_validity` is provided

---

## 🗺️ Future-friendly extensions (optional patterns)

### 🔥 Pulse / Attention materials
If we implement “Pulse Threads” or conceptual attention overlays, keep those materials here as:
- `ui_pulse_glow__v1`
- `ui_attention_highlight__v1`

### 🕰️ 4D / time-dynamic scenes
If we move toward continuous 4D animations, consider materials that evolve over time (e.g., weathering, land-use changes).  
Use `time_validity` or `variants` in metadata.

### 📦 Artifact packaging (advanced)
If we publish large bundles or want supply-chain assurance:
- treat each material pack as an “artifact”
- attach provenance as metadata
- sign bundles (design goal; implementation may vary)

---

## 📚 Project reference pack (used to shape this README)

> Some “reference” PDFs in this project are **PDF portfolios** (they open best in Acrobat/Adobe Reader). That’s okay—treat them as offline libraries.

### 🧭 Core KFM
- 📄 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf
- 📄 Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf
- 📄 Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf
- 📄 Kansas Frontier Matrix – Comprehensive UI System Overview.pdf
- 📄 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf
- 📄 Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf
- 📄 Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf
- 📄 Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf
- 📄 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf
- 📄 Additional Project Ideas.pdf

### 🧠 AI / Data / Methods libraries
- 📦 AI Concepts & more.pdf (PDF portfolio)
- 📦 Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf (PDF portfolio)
- 📄 Data Mining Concepts & applictions.pdf
- 📄 Scientific Method _ Research _ Master Coder Protocol Documentation.pdf

### 🗺️ Maps / Graphics / WebGL libraries
- 📦 Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf (PDF portfolio)
- 📦 Various programming langurages & resources 1.pdf (PDF portfolio)
- 📄 KFM- python-geospatial-analysis-cookbook-v1.pdf

### 🧾 Documentation protocol
- 📄 KFM_REDESIGN_BLUEPRINT_v13.md.gdoc
- 📄 MARKDOWN_GUIDE_v13.md.gdoc
- 📄 Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx

