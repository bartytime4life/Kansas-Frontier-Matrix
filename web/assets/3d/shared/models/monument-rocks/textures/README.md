<!--
KFM Asset Doc ✅
Path: web/assets/3d/shared/models/monument-rocks/textures/README.md
-->

# 🪨🎨 Monument Rocks — Texture Set (PBR)

![Asset](https://img.shields.io/badge/asset-3D%20textures-blue)
![Material](https://img.shields.io/badge/material-PBR%20%28metallic--roughness%29-informational)
![Target](https://img.shields.io/badge/target-WebGL%20%2F%20CesiumJS%20%2F%20MapLibre-success)
![Governance](https://img.shields.io/badge/governance-provenance--first%20%E2%9C%85-critical)
![Policy](https://img.shields.io/badge/policy-fail--closed%20%E2%9B%94-important)

> **What this folder is:** runtime-ready texture maps for the **Monument Rocks** 3D model used in KFM’s 3D experiences (Cesium globe / 3D Tiles / story nodes).
>
> **KFM principle:** *no “pretty colors” without traceability* — every visible artifact should be attributable, versioned, and governed.

---

## 📦 Folder Contract

This directory is the **published texture bundle** for the `monument-rocks` model.

### ✅ Allowed here
- PBR texture images (BaseColor / Normal / ORM, etc.)
- A **texture manifest** (recommended) and attribution notes (recommended)
- Small thumbnails/previews (optional)

### 🚫 Not allowed here
- “Mystery textures” (no license, no provenance, no source)
- Unbounded/huge originals (put source-of-truth in `data/raw/` or an artifact store)
- Ad-hoc manual edits with no version bump or provenance trail

---

## 🗂️ Suggested Layout (with examples)

> These names are **conventions**, not a guarantee of what currently exists. If your files differ, keep the *roles* the same and document the mapping below.

```text
📁 web/assets/3d/shared/models/monument-rocks/
├─ 📄 monument-rocks.glb (or .gltf)
└─ 🎨 textures/
   ├─ 📄 README.md  ✅ (you are here)
   ├─ 🧾 textures.manifest.json  (recommended)
   ├─ 🖼️ rock_baseColor_2048.webp
   ├─ 🧩 rock_normal_2048.png
   ├─ 🧪 rock_orm_2048.png        (R=AO, G=Roughness, B=Metallic)
   ├─ 🌫️ rock_height_2048.png     (optional)
   └─ 🪪 ATTRIBUTION.md            (optional but encouraged)
```

---

## 🎨 Texture Roles (PBR)

KFM’s 3D stack is built around **WebGL-friendly PBR**, and typically streams 3D content (including textured meshes) into a 3D globe experience.

### Core maps
| Map Role | Typical Filename | Color Space | Notes |
|---|---|---:|---|
| **Base Color** (Albedo) | `*_baseColor_*` | **sRGB** | No baked lighting if possible. |
| **Normal** | `*_normal_*` | Linear | Prefer **lossless** to avoid artifacts. |
| **ORM** (packed) | `*_orm_*` | Linear | **R=AO**, **G=Roughness**, **B=Metallic** (common glTF pattern). |
| **Emissive** (rare) | `*_emissive_*` | sRGB | Only if needed. |

### Optional maps
- **Height / Displacement** (`*_height_*`) — only if your mesh/material actually uses it.
- **Opacity / Alpha** — avoid unless necessary (sorting cost + artifacts).
- **Detail maps** — only if they materially improve close-range viewing.

---

## 🌈 Color & Encoding Rules

If textures look “off,” it’s usually color space.

- **sRGB:** BaseColor + Emissive  
- **Linear:** Normal + ORM + AO + Roughness + Metallic + Height

> 🧠 Tip: Don’t gamma-correct Normal/ORM. Doing so will wreck shading.

---

## ⚡ Performance Budgets (Web + Offline Packs + AR)

KFM emphasizes **interactive performance**, **offline data packs**, and future **AR experiences**. Textures are one of the biggest levers for runtime smoothness and “field use” reliability.

### Recommended targets (guidance, not law)
- Prefer **1024–2048** for most surfaces.
- Avoid > **4096** unless you have a strong reason (and measure).
- Keep total per-material texture payload reasonable for mobile/offline.

### Multi-resolution strategy (good for 3D Tiles & mobile)
If needed, ship multiple resolutions:
- `*_1024.*` (mobile/offline default)
- `*_2048.*` (desktop default)
- `*_4096.*` (opt-in “ultra”)

---

## 🧾 Provenance, Licensing, and “Evidence-First” Publishing

KFM treats assets as **auditable evidence**, not anonymous files.

### Minimum provenance for this texture set
At minimum, you should be able to answer:
- Where did these textures come from?
- Under what license can we use and redistribute them?
- What transformations were applied (and by what tool/version)?
- Who validated the output?

### Recommended: `textures.manifest.json`
A small manifest makes the bundle self-describing and supports KFM’s “provenance-first” and “contract-first” workflows.

Example schema (adapt as needed):

```json
{
  "kfm_asset_id": "kfm.3d.monument-rocks.textures",
  "title": "Monument Rocks — Texture Set",
  "version": "1.0.0",
  "classification": "public",
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "TODO: required attribution text"
  },
  "source": {
    "type": "photogrammetry|scan|artist|ai-assisted",
    "origin": "TODO: capture method + capture date",
    "links": ["TODO: source URL(s) or archive references"]
  },
  "maps": [
    {
      "role": "baseColor",
      "path": "rock_baseColor_2048.webp",
      "colorSpace": "sRGB",
      "sha256": "TODO"
    },
    {
      "role": "normal",
      "path": "rock_normal_2048.png",
      "colorSpace": "linear",
      "sha256": "TODO"
    },
    {
      "role": "orm",
      "path": "rock_orm_2048.png",
      "colorSpace": "linear",
      "channels": { "r": "ao", "g": "roughness", "b": "metallic" },
      "sha256": "TODO"
    }
  ],
  "build": {
    "tools": [
      { "name": "Blender", "version": "TODO" },
      { "name": "ImageMagick|KTX-Tools|Other", "version": "TODO" }
    ],
    "notes": "TODO: what was done (bake, denoise, resize, pack channels, etc.)"
  },
  "provenance": {
    "prov_ref": "TODO: link/id to PROV record (preferred)",
    "dcat_ref": "TODO: link/id to DCAT dataset record (preferred)",
    "stac_ref": "TODO: link/id to STAC item/collection (preferred)"
  }
}
```

> ✅ Why this matters: KFM’s UI and AI systems are designed to surface provenance (citations, “map behind the map”) and enforce governance checks. A manifest makes those connections trivial instead of manual archaeology.

---

## 🛡️ Governance & Sensitivity (CARE / FAIR-ready)

Even “just textures” can be sensitive depending on context (cultural restrictions, private property interiors, sacred content, etc.).

### If *any* restrictions apply
- Mark them in the manifest:
  - `classification`: `public | sensitive | restricted`
  - Optional CARE/TK labels (if applicable)
- Ensure the UI can enforce:
  - blurred/generalized outputs where required
  - access control for restricted artifacts

---

## 🧊 Versioning & Immutability (Append-Only Mindset)

KFM favors **append-only** change management:
- Don’t silently overwrite textures.
- Bump `version` when bytes change.
- Keep prior versions accessible when feasible.

### Optional: Content-addressable storage for big bundles
If this texture set grows large, consider storing it as an **artifact** (OCI registry) and referencing immutable digests:
- Push bundle via **ORAS**
- Sign via **Cosign**
- Reference by **SHA-256 digest** in catalogs/manifest

This keeps Git lean while preserving strong provenance and reproducibility.

---

## ✅ Quick QA Checklist (Definition of Done)

Use this before merging changes:

### Visual correctness
- [ ] No obvious seams, stretching, or UV mismatches
- [ ] Normal map orientation correct (no “inside-out” lighting)
- [ ] ORM channels packed correctly (R=AO, G=Roughness, B=Metallic)
- [ ] BaseColor does not contain baked shadows unless intentionally stylized

### Performance
- [ ] Texture sizes/resolutions match intended targets
- [ ] No accidental 8K uploads / uncompressed monsters
- [ ] Formats chosen appropriately (lossless where needed)

### Governance
- [ ] License is explicit (SPDX where possible) ✅
- [ ] Attribution text is present ✅
- [ ] Provenance is recorded (manifest + linked catalog/prov when available) ✅
- [ ] Classification/sensitivity tags are correct ✅

---

## 🧪 Integration Notes (glTF / Cesium / Three.js)

### glTF expectations
- Textures should be reachable relative to the `.gltf` if external, or embedded if `.glb` includes images.
- Prefer **stable filenames**; breaking names breaks cached scenes and story nodes.

### Three.js example (preview only)
```js
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

new GLTFLoader().load(
  "/assets/3d/shared/models/monument-rocks/monument-rocks.glb",
  (gltf) => scene.add(gltf.scene)
);
```

> Tip: always preview the model after texture changes (desktop + mobile if possible).

---

## 🧭 Why Monument Rocks Matters in KFM

Monument Rocks is explicitly part of KFM’s vision for **2D/3D storytelling** (e.g., “Kansas From Above”-style experiences with 3D points of interest). This texture set is a building block for that: it makes the model believable in the 3D globe, story nodes, and future AR modes.

---

## 📚 Project References (All KFM source docs that shaped this README)

> These documents collectively define KFM’s principles used here: provenance-first publishing, contract-first organization, UI transparency (“map behind the map”), policy enforcement, offline + AR future, and supply-chain style integrity for artifacts.

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🏗️ **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- 🧭🤖 **Kansas Frontier Matrix (KFM) – AI System Overview**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview**
- 📥 **Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide**
- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)**
- 🧪 **Additional Project Ideas** (artifact storage, ORAS/Cosign patterns, design packs)
- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals**
- 🗺️ **Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design**
- 📦 **AI Concepts & more** *(PDF portfolio — extract/open to access embedded resources)*
- 🌍 **Maps / Google Maps / Virtual Worlds / Archaeological / Computer Graphics / Geospatial WebGL** *(PDF portfolio)*
- 🧰 **Various programming languages & resources 1** *(PDF portfolio)*
- 🗄️ **Data Management / Theories / Architectures / Data Science / Bayesian Methods / Programming Ideas** *(PDF portfolio)*

---

## 🧷 TODOs (Nice-to-have)
- [ ] Add `textures.manifest.json` with sha256 digests for every file
- [ ] Add `ATTRIBUTION.md` and/or `LICENSES/` for third-party assets
- [ ] Add a small `preview.jpg` for quick visual reference in PRs
- [ ] (Optional) Add an OCI artifact pipeline for heavyweight texture bundles

---
*Last touched:* `2026-01-25` (update when you change files)

