---
collection: "<collection>" # ✅ replace with your folder name
type: "kfm-texture-source"
status: "active"
owner: "KFM 3D / Assets"
---

# 🧱 Texture Sources — `<collection>`

![scope](https://img.shields.io/badge/scope-_source-informational)
![provenance](https://img.shields.io/badge/provenance-required-success)
![license](https://img.shields.io/badge/license-required-success)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)

> [!IMPORTANT]
> This folder is **source-of-truth / evidence-first** storage for *original* texture inputs.  
> ✅ Keep originals **immutable**.  
> ✅ Keep provenance + licensing **complete**.  
> ✅ Generate optimized runtime textures **outside** `_source/`.

---

## 🧭 Quick links

- [Purpose](#-purpose)
- [Folder layout](#-folder-layout)
- [What belongs here](#-what-belongs-here)
- [Rules](#-rules-of-the-road)
- [Required files](#-required-files)
- [Manifest contract](#-manifest-contract-manifesttexturejson)
- [Naming conventions](#-naming-conventions)
- [Build pipeline](#-build-pipeline-source--runtime)
- [Sensitivity & access](#-sensitivity--access)
- [PR checklist](#-pr-checklist)

---

## 🎯 Purpose

Textures in `web/assets/3d/shared/textures/` power **shared visual materials** used across:

- 🌎 3D globe / terrain scenes (e.g., draped imagery, materials)
- 🏛️ 3D Tiles / glTF models (e.g., textured buildings, artifacts, props)
- 🧾 Story scenes + narrative transitions (2D ↔ 3D ↔ AR-ready assets)

This `_source/<collection>/` directory exists so we can:

- 🔎 **Prove where visuals came from** (provenance)
- ⚖️ **Respect licensing & community governance**
- 🧪 **Rebuild outputs deterministically**
- 🚀 Keep the runtime payload small + performant (mobile/offline friendly)

---

## 📦 Folder layout

```text
web/
└─ assets/
   └─ 3d/
      └─ shared/
         └─ textures/
            └─ _source/                      # 🧱 The source directory for original texture files and metadata
               ├─ 📄 README.md               # ✅ REQUIRED: Documentation for the collection, purpose, and usage
               ├─ 🧾 manifest.texture.json   # ✅ REQUIRED: Provenance, license, and intent details (metadata)
               ├─ 🔐 checksums.sha256        # ✅ REQUIRED: Integrity checksums for all files (for reproducibility)
               ├─ ⚖️ LICENSES/               # ✅ REQUIRED: License texts and attribution information
               │  └─ <texture_id>.LICENSE.txt # ⬇️ REQUIRED license for the specific texture
               ├─ 🧱 src/                    # ✅ REQUIRED: Original texture source files (immutable)
               │  └─ <texture_id>/            # One folder per texture
               │     ├─ albedo.<ext>         # e.g., .png, .jpg (diffuse texture)
               │     ├─ normal.<ext>         # e.g., .png, .jpg (normal map)
               │     ├─ roughness.<ext>      # e.g., .png, .jpg (roughness map)
               │     └─ ...                  # Additional maps if applicable
               ├─ 🖼️ previews/               # ✅ RECOMMENDED: Tiny previews (useful for quick review)
               │  └─ <texture_id>.png        # Thumbnails or preview images
               └─ 📝 notes/                  # ⬇️ RECOMMENDED: Logs, emails, and receipts regarding the texture's acquisition
                  └─ <texture_id>.md         # Documentation or receipts for the texture file
```

> [!NOTE]
> If your repo uses a different runtime destination (e.g., hashed bundles, CDN output, OCI artifacts), keep `_source/` as the immutable input boundary and update the **Build Pipeline** section below accordingly.

---

## ✅ What belongs here

| ✅ Put it in `_source/` | ❌ Don’t put it in `_source/` |
|---|---|
| Original textures you can legally redistribute | Generated/compressed outputs (KTX2/WebP/etc.) |
| Highest-quality “evidence” files (PNG/TIFF/EXR) | Working files that can’t be rebuilt (unless required for provenance) |
| License grants + attribution text | Secrets / API keys / credentials (ever) |
| Acquisition notes + receipts | Random “maybe useful later” images with unknown origin |

---

## 🧷 Rules of the road

### 1) 🧾 Provenance-first (no mystery textures)
If we can’t answer **who made it**, **where it came from**, and **how we’re allowed to use it** → it does **not ship**.

### 2) 🧊 `_source/` is immutable
Treat `src/` like evidence storage:
- ✅ Add new versions as new files/IDs
- ❌ Don’t overwrite or “touch up” originals in place

### 3) 🧪 Deterministic builds only
All runtime textures must be reproducible from:
- `_source/<collection>/src/**`
- `manifest.texture.json`
- build tool versions + parameters (recorded)

### 4) 🧰 Optimize for web + offline
Prefer textures that:
- load quickly
- mip well
- compress well
- don’t blow GPU memory on mobile

### 5) 🔒 Sensitivity must propagate
If a texture is sourced from restricted or culturally sensitive material, **derivatives must be at least as restricted**.

---

## 📄 Required files

### `manifest.texture.json` (required)
Single source of truth for:
- provenance
- license / attribution
- intended usage (3D Tiles, terrain drape, UI overlay, etc.)
- sensitivity classification
- build hints (colorspace, normal map convention, etc.)

### `checksums.sha256` (required)
- One line per file in `src/**` and `LICENSES/**`
- Used to prevent silent changes and to support reproducible builds

### `LICENSES/` (required)
At minimum:
- one license file per texture ID (or per upstream pack)
- include attribution text exactly as required by the license/grant

### `previews/` (strongly recommended)
Tiny (~256–512px) previews for PR review and quick browsing.

### `notes/` (recommended)
Capture:
- original URL
- contact emails
- receipts
- “why we chose this” and “what it’s used for”

---

## 🧾 Manifest contract (`manifest.texture.json`)

> [!TIP]
> Keep the manifest **boringly strict**. The goal is to make provenance + licensing auditable and automatable.

### Minimal template

```json
{
  "collection": "<collection>",
  "version": "0.1.0",
  "textures": [
    {
      "id": "kfm_<collection>__<name>",
      "title": "<Human readable name>",
      "description": "<What this is and where it is used>",
      "files": {
        "albedo": "src/kfm_<collection>__<name>/albedo.png",
        "normal": "src/kfm_<collection>__<name>/normal.png"
      },
      "license": {
        "spdx": "CC-BY-4.0",
        "license_file": "LICENSES/kfm_<collection>__<name>.LICENSE.txt",
        "attribution": "© <Creator> — used under CC BY 4.0"
      },
      "provenance": {
        "source_name": "<Archive / website / contributor>",
        "source_url": "<link or internal reference>",
        "acquired_at": "YYYY-MM-DD",
        "acquired_by": "<person | org | bot>",
        "original_format": "png",
        "original_hash_sha256": "<sha256-of-original-file>"
      },
      "sensitivity": {
        "classification": "public",
        "notes": ""
      },
      "build_hints": {
        "colorspace": "sRGB",
        "normal_map_convention": "OpenGL",
        "mipmaps": true
      },
      "runtime": {
        "intended_targets": ["cesium-3dtiles", "gltf", "story-scene"],
        "tags": ["pbr", "tileable"]
      }
    }
  ]
}
```

> [!WARNING]
> If you generated a texture with AI (or heavily edited it), **label it** clearly in `provenance` (and keep the prompt/tooling details in `notes/`). Don’t allow “authentic source” and “synthetic asset” to be indistinguishable.

---

## 🏷 Naming conventions

### Collections
- ✅ `kebab-case` recommended  
  Examples: `terrain-materials`, `historic-buildings`, `story-overlays`

### Texture IDs
- ✅ Stable, lowercase-ish, no spaces
- ✅ Prefer: `kfm_<collection>__<name>`

Examples:
- `kfm_terrain-materials__prairie_grass_01`
- `kfm_story-overlays__paper_map_wash`

### Map suffixes
Use consistent suffixes so build tooling can infer intent:

| Map type | Suggested key | Notes |
|---|---|---|
| Albedo/Base Color | `albedo` | usually sRGB |
| Normal | `normal` | usually linear; specify convention |
| Roughness | `roughness` | linear |
| Metallic | `metallic` | linear |
| Ambient Occlusion | `ao` | linear |
| Height/Displacement | `height` | linear |
| Emissive | `emissive` | usually sRGB |

---

## 🛠 Build pipeline (source → runtime)

> [!IMPORTANT]
> Runtime textures **must not** point at `_source/` paths.  
> `_source/` is evidence storage, not a CDN.

### Suggested stages

1. ✅ **Validate manifest**
   - required fields present
   - referenced files exist
   - sensitivity + license is not empty

2. 🔐 **Verify checksums**
   - detect unexpected mutations

3. 🎛️ **Convert & optimize**
   - generate mipmaps
   - compress to GPU-friendly formats (when applicable)
   - enforce colorspace rules (sRGB vs linear)

4. 🧾 **Emit runtime index**
   - `index.json` mapping IDs → runtime file paths
   - include attribution bundle for UI/tooltips

### Suggested runtime output policy

- Prefer GPU-compressed formats for WebGL (when supported)
- Keep fallback formats for older devices if needed
- Use smaller LOD variants for mobile/offline packs

<details>
<summary>📌 Implementation notes (adapt to your actual tooling)</summary>

- If you already have a KFM policy gate / validation framework, add texture-manifest validation there.
- If your build system is Node-based, consider a `scripts/assets/build_textures.ts` that:
  - reads `manifest.texture.json`
  - emits `web/assets/3d/shared/textures/<collection>/index.json`
  - writes optimized textures under `web/assets/3d/shared/textures/<collection>/<texture_id>/...`
- Pin tool versions (and record them in build logs) so outputs are reproducible.

</details>

---

## 🔒 Sensitivity & access

Textures can unintentionally expose sensitive locations or restricted cultural material. Treat textures like data:

- `public` → OK to ship publicly
- `sensitive` → may require generalization (blur, downsample, remove exact detail)
- `confidential` / `restricted` → do not ship publicly; store separately or behind access controls

> [!TIP]
> If a dataset/layer would show a “lock” icon in the UI, textures derived from it should be treated the same way.

---

## ✅ PR checklist

Use this before submitting a PR that adds/changes textures:

- [ ] Added/updated `manifest.texture.json`
- [ ] Added/updated `LICENSES/**` with correct attribution text
- [ ] Added/updated `checksums.sha256`
- [ ] Included `previews/**` for any new texture IDs
- [ ] Verified sensitivity classification (and that derivatives aren’t less restricted)
- [ ] Ran the texture build pipeline locally (or CI passed)
- [ ] Confirmed runtime outputs are outside `_source/`
- [ ] Confirmed no “mystery files” (unknown origin / unknown license)

---

## 🧯 Troubleshooting

<details>
<summary>🚫 CI fails: “missing license / missing sensitivity / missing provenance”</summary>

That’s expected behavior. Add the missing fields/files:
- license: SPDX + license text (or explicit grant)
- provenance: source + acquisition info
- sensitivity: classification + notes

</details>

<details>
<summary>🐢 Performance tanked after adding a texture</summary>

Common causes:
- texture too large (GPU memory spike)
- no mipmaps (shimmering + bandwidth)
- wrong colorspace (visual artifacts)
- too many unique textures (state changes)

Fix by:
- adding mipmaps
- producing lower-res variants
- reusing materials where possible

</details>

---

## 📚 Related docs (project alignment)

These rules are aligned with KFM’s core goals: **traceability**, **trust**, and **governed publishing**. If you’re unsure, review:

- 📘 KFM Architecture / Policy Gates / Governance
- 🧭 KFM UI Transparency + Provenance Surfacing
- 📥 KFM Data Intake philosophy (provenance-first, deterministic pipelines)
- 🧠 KFM AI / Focus Mode explainability + citations
- 🥽 AR + hybrid 2D/3D storytelling roadmap ideas

---

