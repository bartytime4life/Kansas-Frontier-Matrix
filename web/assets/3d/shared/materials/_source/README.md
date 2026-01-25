# 🧱 Shared 3D Materials — `_source` (KFM)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-0b3d91)
![Scope](https://img.shields.io/badge/scope-shared%20materials-222)
![Pipeline](https://img.shields.io/badge/pipeline-provenance%E2%80%91first-2d7d46)
![Target](https://img.shields.io/badge/target-WebGL%20%7C%20Cesium%20%7C%203D%20Tiles-6f42c1)
![Status](https://img.shields.io/badge/status-source%20assets%20only-orange)

> ✅ **Source-of-truth** authoring files for shared 3D materials (PBR-friendly) used across KFM’s 3D stack.  
> ❌ **Not shipped** to production builds (unless explicitly packaged).  
> 🧾 **No mystery materials**: every material must have **license + provenance + intent** recorded.

---

## 🧭 Where this fits in the KFM stack

KFM’s front-end supports a **dual 2D/3D mapping experience** (2D map + 3D globe/terrain). This folder feeds the 3D side of the house — materials used by:

- 🌍 **CesiumJS / 3D Tiles** content (buildings, point clouds, volumetric layers, landmarks)
- 🧊 **glTF assets** (props, monuments, interpretive models)
- 🏞️ **Terrain/DEM drapes** (historic landcover, orthophotos, hillshade blends)
- 📱 **AR / mobile-friendly “wow” moments** (future-facing: lightweight materials + offline packs)

---

## 📦 What lives here vs. what ships

Think of KFM materials like KFM data: **raw/source is sacred**; **exports are reproducible**.

### ✅ Put in `_source/` (authoring + evidence)
- 🎨 Authoring project files (e.g., `.blend`, `.spp`, `.sbs/.sbsar`, `.psd`)
- 🖼️ High-quality texture masters (PNG/TIF/EXR — uncompressed or lossless)
- 🧷 Reference imagery & notes (with attribution + license)
- 🧾 `material.manifest.json` (required) + preview render

### 🚫 Do NOT put in `_source/`
- 🧯 Auto-generated runtime outputs (compressed textures, packed atlases, baked glTF copies)
- 🚨 Anything with unknown / incompatible licensing
- 🔐 Secrets, API keys, private location details, or sensitive content embedded into decals/labels

> 💡 If it’s “derived output,” it belongs in a **sibling export folder** or an **artifact store**, not here.

---

## 🗂️ Recommended layout

📍 You are here: `web/assets/3d/shared/materials/_source/`

```text
📦 web/
└─ 🎨 assets/
   └─ 🧊 3d/
      └─ 🧱 shared/
         └─ 🧵 materials/
            ├─ 📁 _source/                  👈 source-of-truth (this folder)
            │  ├─ 📁 prairie-grass-dry/
            │  │  ├─ 🧾 material.manifest.json
            │  │  ├─ 🖼️  preview.png
            │  │  ├─ 📄 ATTRIBUTION.md
            │  │  ├─ 📁 refs/               (reference photos / scans + notes)
            │  │  ├─ 📁 authoring/          (.blend/.spp/.psd/.sbs…)
            │  │  ├─ 📁 textures_master/    (lossless masters: baseColor/normal/etc)
            │  │  └─ 📁 notes/              (process notes, screenshots, prompts)
            │  └─ 📁 river-silt-wet/
            │     └─ ...
            ├─ 📁 exports/                  (runtime-ready outputs — recommended)
            │  ├─ 📁 prairie-grass-dry/
            │  │  ├─ 🧊 baseColor.ktx2
            │  │  ├─ 🧊 normal.ktx2
            │  │  ├─ 🧊 orm.ktx2
            │  │  └─ 🧾 material.export.json
            │  └─ ...
            └─ 📁 _schemas/                 (optional: JSON schema for manifests)
```

> ✅ **Rule of thumb:** `_source/` is for humans + reproducibility. `exports/` is for browsers.

---

## 🧾 Material Contract (aka “No Mystery Materials”)

Every material folder **must** include:

- `material.manifest.json` ✅ (required)
- `preview.png` ✅ (required — quick visual sanity check)
- `ATTRIBUTION.md` ✅ (required — license + sources + credits)
- At least one source texture or authoring file ✅

### 🔖 `material.manifest.json` (minimum fields)

```json
{
  "id": "prairie-grass-dry",
  "displayName": "Prairie Grass (Dry)",
  "version": "1.0.0",
  "status": "draft",
  "tags": ["terrain", "prairie", "historic", "vegetation"],
  "license": "CC-BY-4.0",
  "authors": [
    { "name": "KFM Contributor", "role": "material-author" }
  ],
  "sources": [
    {
      "type": "photo-reference",
      "title": "Prairie grass reference set",
      "where": "refs/",
      "license": "CC-BY-4.0",
      "credit": "Name / Org",
      "notes": "Describe what was used + why"
    }
  ],
  "intendedUse": {
    "targets": ["cesium", "gltf", "storybook"],
    "notes": "Used for terrain drape + 3D landmark blending."
  },
  "pbr": {
    "maps": {
      "baseColor": "textures_master/baseColor.png",
      "normal": "textures_master/normal.png",
      "orm": "textures_master/orm.png",
      "emissive": null
    },
    "conventions": {
      "baseColorColorSpace": "sRGB",
      "dataMapsColorSpace": "linear",
      "normalSpace": "tangent"
    }
  },
  "governance": {
    "sensitivity": "public",
    "reviewRequired": false
  }
}
```

<details>
<summary>🧠 Recommended extras (strongly encouraged)</summary>

- 🧾 `checksums` (sha256 of source + export files)
- 🔁 `provenance` link to a PROV JSON-LD blob (optional but aligns with KFM ethos)
- 📏 `budgets` (texture sizes, expected memory footprint)
- 🧩 `compat` (glTF extensions, Cesium material constraints)
- 🧪 `qa` (visual test cases / screenshots)

</details>

---

## 🎨 PBR mapping conventions (practical defaults)

We prefer glTF-style PBR texture semantics:

- `baseColor` ✅ (sRGB)
- `normal` ✅ (linear)
- `orm` ✅ packed map (linear)
  - **R** = occlusion
  - **G** = roughness
  - **B** = metallic
- `emissive` optional (sRGB)

> ⚠️ Keep physically plausible values. If a material is stylized, say so in `intendedUse.notes`.

---

## ⚙️ Export expectations (runtime-friendly)

Even if your exports are handled elsewhere, author materials as if they’ll be consumed by:

- **WebGL renderers** (GPU memory is the real budget)
- **3D tiles streaming** (mips + compression matter)
- **Mobile/AR** (texture size ceilings matter)

### 🎯 Suggested budgets (edit as KFM learns)
- 🧊 **Texture dimensions**: 512–2048 (power-of-two preferred)
- 📱 Mobile/AR: keep critical maps ≤ 1024 where possible
- 🧩 Keep unique materials low in any single tileset/model
- 🧠 Avoid 4K maps unless there is a documented reason

### 🧰 Compression (recommended)
If/when the pipeline supports it:
- Prefer **KTX2 / Basis** for runtime
- Keep `_source/` masters lossless (PNG/TIF/EXR)

---

## 🧪 Local preview (fast sanity checks)

If you need a quick preview without wiring into the full KFM app:

1) Create a tiny HTML preview (Three.js or Cesium sandbox) in a scratch folder  
2) Serve it locally

```bash
# Node (common)
npx serve .

# OR Python (simple + ubiquitous)
python -m http.server 8080
```

> 📌 The goal is **repeatable “looks right” checks** before exports land in production.

---

## 🧭 Governance & ethics (FAIR/CARE vibes for assets)

KFM treats provenance + governance as first-class, and materials should follow suit:

- 🧾 **License is mandatory** (no “found on Google”)
- 🧬 **Provenance is mandatory** (what sources + what transformations)
- 🔒 **Sensitivity tagging** is supported (public / restricted / internal)
- 🧯 If a material is used to visualize sensitive subjects (archaeology, endangered species, private infrastructure), ensure the **visual design doesn’t leak restricted detail**.

> ✅ Good: generalized symbology, neutral textures, aggregated visual encodings  
> ❌ Bad: “treasure map” decals, location-encoded textures, identifiable private signage

---

## 🤖 AI-assisted materials (allowed — with receipts)

AI can help, but KFM is evidence-first:

If you used AI for any part of a material (generation, upscaling, removal, style transfer), add:

- `notes/ai.md` containing:
  - model/tool name + version
  - prompt(s) (or workflow description)
  - input sources + licenses
  - any post-processing steps
  - why it’s allowed to redistribute

> 🧾 The goal is the same as Focus Mode citations: **traceable, reviewable, auditable**.

---

## 📦 Big binaries: Git LFS vs Artifact Registry

Source assets get large fast.

**Preferred options:**
- ✅ **Git LFS** for `.blend`, `.spp`, `.psd`, large lossless masters
- ✅ (Optional) **Artifact registry** approach for heavyweight bundles (signed + versioned)

If you publish material bundles externally, keep:
- provenance metadata attached (or referenced)
- checksums available
- version tags consistent

---

## ✅ PR checklist (materials)

Before submitting or merging:

- [ ] `material.manifest.json` exists and is filled out
- [ ] `ATTRIBUTION.md` exists and is correct
- [ ] `preview.png` renders the intended look
- [ ] Masters are lossless and organized
- [ ] No unlicensed references included
- [ ] No sensitive info baked into textures
- [ ] If exports are included: they match the manifest and budgets
- [ ] Material is referenced by at least one consumer (scene/model/story step) or has a clear planned usage note

---

## 📚 Related KFM docs & resource bundles

These project files shaped the rules above — especially around provenance, governance, and 2D/3D/AR integration:

### Core KFM docs (architecture + governance)
- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- 🎛️ **Kansas Frontier Matrix – Comprehensive UI System Overview**
- 📥 **KFM Data Intake – Technical & Design Guide**
- 🧭🤖 **KFM AI System Overview**
- 🌟 **Latest Ideas & Future Proposals**
- 💡 **Innovative Concepts to Evolve KFM**
- 💭 **Additional Project Ideas**

### 📦 Resource bundles (PDF portfolios)
- 🧠 **AI Concepts & more** (AI patterns + governance thinking)
- 🗺️ **Maps/Virtual Worlds/Computer Graphics/WebGL** (geospatial 3D + visualization)
- 🧰 **Various programming languages & resources** (stack/tooling references)
- 🧱 **Data Management/Theories/Architectures/Bayesian methods** (metadata + rigor)

---

## 🧩 TODOs (nice-to-have next upgrades)

- [ ] Add a JSON Schema under `_schemas/` and validate manifests in CI
- [ ] Add a `materials.index.json` generator for fast runtime lookup
- [ ] Add automatic checksum + provenance record generation on build
- [ ] Add a visual regression snapshot test for `preview.png`
- [ ] Add policy checks (license/provenance required) as a CI gate

🛠️ **If it’s not reproducible, it’s not done.**

