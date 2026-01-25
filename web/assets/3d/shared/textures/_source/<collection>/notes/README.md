# 🎨 Texture Collection Notes — `<collection>`

![KFM](https://img.shields.io/badge/KFM-3D%20Textures-0b7285?style=flat)
![Provenance](https://img.shields.io/badge/provenance-required-1c7ed6?style=flat)
![Policy Gates](https://img.shields.io/badge/policy%20gates-fail--closed-212529?style=flat)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-enforced-2f9e44?style=flat)

> ✅ **Purpose:** This `notes/` folder is the **audit + provenance hub** for the `<collection>` texture pack.  
> 🔍 In KFM, even “pretty textures” are treated like **evidence artifacts**: traceable, licensed, governed, and optimized for **React · MapLibre · (optional) Cesium** rendering.  
> 🧭 If it can show up in the UI (2D/3D/Story/AR), it needs **source + license + lineage**.

---

## 🧷 Quick Start Checklist

- [ ] Replace all `<collection>` placeholders in this README
- [ ] Fill in **Collection At-a-Glance** (below)
- [ ] Create / update `notes/sources.yml` (upstream source + license + retrieval info)
- [ ] Create / update `notes/texturepack.yml` (normalized manifest for outputs + usage)
- [ ] Ensure exports are **web-ready** (size + compression + color space)
- [ ] Confirm **redistribution rights** (especially for offline packs 📦)

---

## 🗺️ Collection At-a-Glance

| Field | Value |
|---|---|
| **Collection ID** | `<collection>` |
| **What it’s for** | _(terrain drape / building materials / props / story visuals / etc.)_ |
| **Primary usage** | _(Cesium 3D Tiles / glTF materials / UI cards / etc.)_ |
| **License (SPDX if possible)** | `TBD` |
| **Attribution required?** | `yes/no` |
| **Sensitivity classification** | `public / restricted / sensitive` |
| **PBR workflow** | `metallic-roughness (preferred) / spec-gloss` |
| **Target runtime formats** | `ktx2 / webp / png` |
| **Max recommended resolution** | `TBD` |
| **Maintainer / owner** | `@TBD` |

---

## 📁 Folder Layout (Source → Work → Export)

This folder mirrors KFM’s “raw → work → processed” staging pattern, but for **texture assets**.

```text
🧵 web/assets/3d/shared/textures/
└── 🧪 _source/
    └── 🗂️ <collection>/
        ├── 🧱 raw/                 # original downloads / scans (read-only mindset)
        ├── 🛠️ work/                # intermediate edits (cropping, de-lighting, baking)
        ├── 📦 exports/             # runtime-ready outputs (compressed + validated)
        └── 📝 notes/
            ├── ✅ README.md         # 📍 you are here
            ├── 🔗 sources.yml       # upstream sources, licensing, retrieval receipts
            ├── 🧾 texturepack.yml   # normalized “pack manifest” (outputs + rules)
            ├── 🏷️ ATTRIBUTION.md    # human-readable credits (UI-safe text)
            └── 🧷 CHANGELOG.md      # semver-ish history for this collection
```

> 💡 **Rule of thumb:**  
> `raw/` is “what we got”, `work/` is “how we fixed it”, `exports/` is “what the app ships”.

---

## 🚦 Non‑Negotiables (Policy-Gated)

### ⚖️ 1) No license → no publish
Every texture (and every upstream bundle) must have a clear license and attribution requirements documented.

### 🧬 2) Provenance-first publishing
Nothing from this pack should be used in the UI/3D pipeline unless metadata exists (sources + manifest + classification).

### 🔐 3) Sensitive ≠ public
If imagery could expose sensitive locations, culturally restricted knowledge, or private property details, classify it and restrict distribution.

### 🧾 4) Determinism beats mystery
Exports should be reproducible: same inputs + same tools + same settings → same outputs (as much as practical).

---

## 🧾 Required Notes Files

### 1) `sources.yml` (upstream truth)

Use this to record where assets came from, what we’re allowed to do, and what exactly we retrieved.

<details>
<summary>📌 Template: <code>notes/sources.yml</code></summary>

```yaml
collection:
  id: "<collection>"
  title: "TBD"
  description: "TBD"
  intended_use:
    - "TBD"
  tags: ["textures", "pbr", "kfm"]
  created_at: "YYYY-MM-DD"
  updated_at: "YYYY-MM-DD"
  maintainer: "@TBD"

sources:
  - id: "src-001"
    name: "TBD (source name)"
    url: "https://example.com/path/to/source"
    retrieved_at: "YYYY-MM-DD"
    license:
      spdx: "TBD"
      attribution_required: true
      attribution_text: "TBD (copy the exact required credit text if provided)"
      redistribution_allowed: "unknown|yes|no"
      notes: "TBD"
    originals:
      - path: "../raw/TBD.zip"
        sha256: "TBD"
    transform_notes: "TBD (what we did before exporting)"
```

</details>

---

### 2) `texturepack.yml` (what the app can safely use)

This file defines **what exists in `exports/`**, how it should be interpreted (PBR map meanings + color space), and what can be shipped.

<details>
<summary>🧩 Template: <code>notes/texturepack.yml</code></summary>

```yaml
texturepack:
  id: "tex.<collection>"
  version: "0.1.0"
  status: "draft|reviewed|published"

governance:
  classification: "public|restricted|sensitive"
  care:
    authority_to_control: "TBD (if relevant)"
    responsibility_notes: "TBD"
    ethics_notes: "TBD"

license:
  spdx: "TBD"
  attribution_required: true
  attribution_ref: "./ATTRIBUTION.md"

rendering:
  workflow: "pbr-metallic-roughness" # preferred for glTF/Cesium pipelines
  normal_format: "OpenGL"            # be explicit (OpenGL vs DirectX)
  tiling: "seamless|non-seamless|unknown"

color_management:
  # Typical expectations (adjust if your pipeline differs)
  albedo_basecolor: "sRGB"
  emissive: "sRGB"
  normal: "linear"
  roughness: "linear"
  metallic: "linear"
  ao: "linear"
  height: "linear"

outputs:
  - material_id: "<collection>__<material>"
    label: "TBD human name"
    size_px: [2048, 2048]
    maps:
      basecolor: "../exports/<material>_basecolor.ktx2"
      normal: "../exports/<material>_normal.ktx2"
      orm: "../exports/<material>_orm.ktx2"
    channel_packing:
      orm:
        r: "occlusion"
        g: "roughness"
        b: "metallic"
    sha256:
      basecolor: "TBD"
      normal: "TBD"
      orm: "TBD"
    notes: "TBD"

provenance:
  inputs:
    - source_id: "src-001"
      original_path: "../raw/TBD.zip"
      sha256: "TBD"
  processing:
    run_id: "YYYY-MM-DD__<shortid>"
    tools:
      - name: "blender"
        version: "TBD"
      - name: "imagemagick"
        version: "TBD"
      - name: "basisu / toktex"
        version: "TBD"
    steps:
      - "TBD (e.g., de-lighting, seam fix, baking, channel pack, compression)"
```

</details>

---

## 🧱 Texture Naming Convention (Keep it Boring ✅)

### ✅ Recommended patterns

**Raw (as-retrieved):**
- Keep original filenames when possible (helps audits).
- Store in a source folder per upstream provider.

**Exports (runtime-ready):**
```text
<material>_<map>_<res>.<ext>
```

Examples:
```text
limestone_basecolor_2048.ktx2
limestone_normal_2048.ktx2
limestone_orm_2048.ktx2
```

### 🗺️ Map suffixes (standardize!)
| Map | Suffix | Notes |
|---|---|---|
| Base Color / Albedo | `basecolor` | no baked lighting if possible |
| Normal | `normal` | specify OpenGL vs DirectX |
| Occlusion/Roughness/Metallic | `orm` | channel-packed (R=AO, G=Rough, B=Metal) |
| Roughness (single) | `roughness` | only if not packed |
| Metallic (single) | `metallic` | only if not packed |
| Height/Displacement | `height` | be explicit about units/scale |
| Emissive | `emissive` | for glow effects |

---

## 🌈 Color Space Rules (Don’t Let Gamma Chaos In)

- **sRGB:** `basecolor`, `emissive`
- **Linear:** `normal`, `roughness`, `metallic`, `ao`, `height`, `orm`

> 🧪 QA tip: If roughness looks “washed out”, you probably treated it as sRGB by accident.

---

## 📦 Formats & Performance Targets (Web + Offline)

KFM supports both **online streaming** (fast loads) and future **offline packs** (portable bundles). That means textures must be:

- ✅ Small enough for web delivery
- ✅ GPU-friendly (mipmaps + power-of-two where possible)
- ✅ Legally redistributable (offline packs are still redistribution)

### Recommended export formats
- **KTX2 (Basis Universal):** best for GPU compressed delivery (preferred for 3D)
- **WebP / AVIF:** good for UI images (not always ideal for normal maps)
- **PNG:** only when necessary (lossless, but large)

### Resolution guidelines (practical defaults)
- **2K (2048)** for hero assets / close-up materials
- **1K (1024)** for most secondary assets
- **512** for far/LOD or mobile-first packs

> 🧠 If a material is only visible at 200–400px on screen, exporting 4K is just donating bandwidth to the void.

---

## 🛰️ How These Textures Get Used in KFM (2D/3D/Story/AR)

- 🗺️ **2D Map UI:** may display texture-driven UI assets, legends, cards
- 🌍 **3D Globe & Terrain:** Cesium drapes imagery & supports textured 3D content
- 🧱 **3D Tiles & glTF:** textured meshes / buildings / point clouds where applicable
- 📚 **Story Nodes:** narrative scenes can reference 3D moments and materials
- 🕶️ **AR (future):** mobile/AR clients may reuse the same 3D models + textures

**Bottom line:** treat texture packs as first-class assets with provenance, because they can become part of the public narrative experience.

---

## 🧪 QA Checklist (Before “Published”)

### Visual & technical
- [ ] No visible seams (if marked seamless)
- [ ] Basecolor is de-lit (no strong baked shadows) or explicitly documented if not
- [ ] Normal map looks correct (no inverted bumps)
- [ ] ORM channel packing verified (AO/Rough/Metal mapped correctly)
- [ ] Mipmaps present (or generated at build)
- [ ] File sizes make sense (no accidental uncompressed monsters)

### Governance
- [ ] License present, compatible with intended distribution (especially offline packs)
- [ ] Attribution text captured in `ATTRIBUTION.md`
- [ ] Sensitivity classification set (public/restricted/sensitive)
- [ ] Sources and transformations documented (`sources.yml` + `texturepack.yml`)

---

## 🔐 Security & Hygiene (Yes, Even For Textures)

- 🚫 Do **not** commit API keys, tokens, or private URLs in notes.
- ✅ Prefer public, stable, citable source URLs.
- 🧾 Capture checksums for original bundles and exports to detect tampering.

---

## 🧾 Attribution (UI-Safe Copy)

Put the exact credit copy in:

- `notes/ATTRIBUTION.md`

Make it:
- ✅ human-readable
- ✅ copy/paste safe for UI dialogs
- ✅ includes license + source link + author if required

---

## 🧭 Versioning & CHANGELOG

Track changes in `notes/CHANGELOG.md` (recommended):
- `Added` new materials
- `Changed` compression/format
- `Fixed` seams/normal orientation
- `Removed` assets that had licensing issues (with notes)

Use semantic-ish versions:
- `0.x` while the pack is still unstable
- `1.0.0` when it’s “UI-safe + governed + stable”

---

## ❓ FAQ

### “Can I just drop a texture in exports and use it?”
No. Add sources + manifest first. If it can ship, it must be auditable.

### “What if the texture is AI-generated?”
Treat it as **synthetic**:
- record model/tool + version
- record prompt/inputs (if allowed)
- confirm redistribution rights
- label it clearly in `texturepack.yml`

### “Do we store huge source zips in git?”
Prefer not. If binaries are large:
- use Git LFS **or**
- store as a content-addressed artifact (OCI registry, etc.) and record the digest in notes

---

## ✅ “Done” Definition (Published Pack)

A texture pack is considered **Published** when:
- `sources.yml` is complete
- `texturepack.yml` is complete
- exports are optimized and validated
- attribution is correct and UI-ready
- classification is correct
- CI/policy checks pass (fail-closed)

---

### 🔗 See Also (KFM Concepts This Aligns With)

- 🧬 Provenance-first publishing (policy gates)
- 🗺️ “Map behind the map” transparency
- 📦 Offline packs and field use
- 🕶️ AR-ready asset reuse
- 🔐 Supply-chain discipline for artifacts (hashes, signatures, reproducible builds)

