<div align="center">

# 🏷️ Decal Label Textures  
`web/assets/3d/shared/textures/decals/labels/`

![Asset Type](https://img.shields.io/badge/asset-decal%20labels-blue)
![Target](https://img.shields.io/badge/target-2D%20%7C%203D%20%7C%20AR-orange)
![Formats](https://img.shields.io/badge/formats-PNG%20%7C%20WEBP%20%7C%20KTX2%20(optional)-success)
![Governance](https://img.shields.io/badge/policy-provenance--first%20%2B%20FAIR%2FCARE-purple)

**Curated, reusable label plates** for 3D scenes, terrain overlays, and AR “floating labels” in KFM.  
Designed to be **readable**, **performant**, and **traceable** (license + provenance + sensitivity).

</div>

---

## 🧭 What lives here (and why)

KFM supports **2D maps + 3D globe/terrain + story nodes + offline packs + future AR experiences**. This folder exists for **label-style decal textures** that can be:

- 🛰️ **Billboard labels** in 3D (CesiumJS “pins/nameplates” style)
- 🧱 **Projected decals** onto meshes/terrain (signage plates, overlays)
- 📱 **AR floating labels** (big readable plates, minimal clutter, mobile-friendly)
- 🎬 **Story-stop callouts** (e.g., “Kansas From Above” style guided flyovers)

> [!NOTE]
> Dynamic text (true runtime typography) is usually better handled via **SDF/MSDF font atlases**.
> This folder is specifically for **hand-authored / art-directed / branded** label plates where a texture is the right tool.

---

## 🚫 What does *not* belong here

Keep this folder focused. Don’t put:

- ❌ Full PBR material sets (albedo/normal/roughness/metallic) → use a `materials/` or model-specific `textures/`
- ❌ Generic UI icons → use `web/assets/.../icons/` (or the UI icon set directory)
- ❌ User-uploaded or raw evidence images → those belong in the **data intake** flows (raw/processed + catalogs)
- ❌ Unlicensed/unknown-provenance art (CI/policy should reject this anyway)

---

## 📁 Suggested structure

We keep the **final, runtime-ready** textures here. If you maintain source files (SVG/PSD/etc.), store them in a sibling `_source/` folder (or repo-wide design folder) and treat them as “raw evidence” for art.

```text
web/
 └── assets/
    └── 3d/
       └── shared/
          └── textures/
             └── decals/
                └── labels/
                   ├─ 📄 README.md                 # 📘 You are here: overview, usage guidelines for label decals
                   ├─ 📁 place/                    # 🗺️ Landmarks, towns, rivers, regions
                   ├─ 📁 story/                    # 🎬 Story-specific callouts / chapter plates
                   ├─ 📁 ui/                       # 🧭 Generic in-world UI plates (e.g., "Tap to learn more")
                   ├─ 📁 governance/               # 🛡️ Sensitivity, TK, consent, disclaimers
                   ├─ 📁 dataset/                  # 📦 Dataset-driven overlays (only if truly needed)
                   └─ 📁 _meta/                    # 🧾 Indices, manifests, attributions
```

> [!TIP]
> Keep names stable and use metadata for “meaning”. Don’t encode your whole taxonomy into filenames.

---

## 🏷️ Naming convention

Use a **stable, predictable** filename scheme so the runtime can load assets deterministically and offline packs can be built reproducibly.

**Recommended pattern**
```text
<category>/<slug>__<variant>__v<semver>.<ext>

# examples
place/monument-rocks__default__v1.0.0.png
place/flint-hills__dark__v1.1.0.webp
story/kansas-from-above__chapter-01__v1.0.0.png
governance/tk-sacred__warning__v1.0.0.png
```

**Rules**
- ✅ `kebab-case` only
- ✅ `slug` is the stable ID (don’t rename casually)
- ✅ `variant` is for theme/contrast/layout differences (`default`, `dark`, `hi-contrast`, `mobile`, etc.)
- ✅ `v<semver>` bumps when pixels change
- ✅ extensions: `.png` (preferred), `.webp` (optional), `.ktx2` (optional future)

---

## 🎨 Visual design guidelines (readability first)

These labels must work across:
- bright satellite imagery ✅
- shaded terrain ✅
- dense overlays ✅
- mobile screens ✅
- AR camera feed ✅

**Baseline rules**
- 🧊 Prefer a **plate/background** (pill/rounded rect) behind text.
- 🖊️ Use **outline + subtle shadow** to avoid “disappearing” on high-frequency terrain.
- 🧑‍🦯 Maintain accessible contrast (plan for high-contrast mode variants).
- 🔠 Keep type large; avoid thin fonts; avoid tiny subtext.
- 🌎 If localized: design for longer strings (German problem) and multi-line wrapping.

**Recommended layouts**
- `plate` — rounded rectangle with padding (best general-purpose)
- `tag` — small banner with pointer/chevron
- `sign` — faux physical signage for historical scenes

---

## 🧪 Technical constraints (WebGL/Cesium-friendly)

### ✅ Formats
- **PNG (preferred)**: lossless + alpha; best for crisp edges and UI plates.
- **WEBP (optional)**: smaller files; verify alpha + decode perf on your target devices.
- **KTX2 (optional)**: GPU-friendly compression (future-facing; good for big packs).

### ✅ Dimensions & scaling
- Prefer **power-of-two** sizes where practical (helps mipmapping workflows and avoids edge cases).
- Common sizes: `256`, `512`, `1024` square, or `1024x512` for wide plates.
- Always include **safe padding** (min 16px) so mipmaps don’t bleed edges.

### ✅ Alpha & edge quality
- Use **straight alpha** exports (avoid dark fringes).
- Ensure the border pixels around transparent regions are **color-extended** (or padded) to prevent haloing.

### ✅ Filtering & mipmaps (practical defaults)
- Labels should look good at distance → mipmaps often help.
- If you see shimmer/aliasing, test:
  - mipmaps on + trilinear filtering  
  - or clamp + linear filtering for NPOT assets  
  - or provide a dedicated `mobile` variant that is simpler/bolder

---

## 🧾 Provenance, licensing & governance (non-negotiable)

KFM’s core principle: **nothing is a “mystery layer”** — that applies to visuals too.  
Every label texture must be traceable and policy-compliant.

### Required metadata (sidecar)
For each texture, add a sidecar metadata file:

```text
place/monument-rocks__default__v1.0.0.png
place/monument-rocks__default__v1.0.0.asset.json   ✅ required
```

<details>
<summary><strong>📄 Suggested <code>.asset.json</code> schema (minimal)</strong></summary>

```json
{
  "id": "kfm.decal.label.place.monument-rocks",
  "title": "Monument Rocks — Label Plate",
  "type": "decal.label",
  "tags": ["place", "landmark", "story"],
  "language": "en",
  "era": { "start": "1850-01-01", "end": null },

  "files": [
    {
      "path": "place/monument-rocks__default__v1.0.0.png",
      "mime": "image/png",
      "sha256": "TODO",
      "pixelSize": { "w": 1024, "h": 512 }
    }
  ],

  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "Kansas Frontier Matrix contributors",
    "notes": "If derived from third-party art/fonts, include full attribution + license here."
  },

  "provenance": {
    "source": [
      { "kind": "design", "ref": "source file path or ticket id" },
      { "kind": "dataset", "ref": "kfm.dataset.id (if label relates to a dataset)" }
    ],
    "createdBy": {
      "agent": "human",
      "toolchain": ["Inkscape", "pngquant", "oxipng"]
    }
  },

  "governance": {
    "classification": "public",
    "sensitivity": "none",
    "restrictions": []
  }
}
```
</details>

### Sensitive content & “TK-style” labels 🛡️
Some labels are not just visual—they encode cultural or privacy meaning.

- If a label relates to **sacred sites**, **restricted knowledge**, **endangered species**, or **precise archaeological locations**:
  - store in `governance/`
  - use metadata fields to indicate classification + restrictions
  - consider **generalized variants** (e.g., “Sensitive Area” without pinpointing)
  - ensure only authorized roles can access the exact label set (when implemented)

> [!IMPORTANT]
> If it can cause harm when made easier to find, it **must not ship as a precise label** in the public bundle.

### AI-generated labels 🤖
AI assistance is allowed *only* if it stays evidence-based and reviewable.

If AI touched the pixels, the `.asset.json` must include:
- model/tool name + version
- prompts / parameters (or a reference to where stored)
- human reviewer sign-off
- the same license/provenance rules as human-made assets

---

## 🧰 Adding a new label (contributor workflow)

### 1) Design
- Create source art (prefer vector) and decide the **plate layout** + **contrast variant(s)**.
- Ensure the label won’t clash with a busy basemap/terrain.

### 2) Export
- Export **PNG with alpha** at target resolution (and `@2x` if you use that convention).
- Keep text crisp; avoid rasterizing at too small a size.

### 3) Optimize
<details>
<summary><strong>⚙️ Example optimization commands</strong></summary>

```bash
# lossless optimize (PNG)
oxipng -o 4 --strip safe *.png

# lossy-but-clean PNG (optional)
pngquant --quality=70-90 --strip --force --output out.png in.png

# webp variant (optional)
cwebp -q 85 -alpha_q 90 in.png -o out.webp
```
</details>

### 4) Add provenance metadata
- Create the `.asset.json`
- Include license + attribution + classification (public/restricted)
- Add a sha256 (CI can automate this)

### 5) Register (index/atlas)
- Add the asset to a local index (see next section)
- If you maintain a texture atlas, rebuild it deterministically

### 6) Preview
- Test in:
  - 2D (MapLibre context)
  - 3D (Cesium context)
  - “story step” playback (camera motion + fade transitions)
  - mobile viewport + (future) AR readability assumptions

---

## 📦 Index + atlas strategy (so runtime stays fast)

As this folder grows, **don’t rely on directory listing at runtime**.

### Recommended: `labels.index.json`
Store in `labels/_meta/labels.index.json`:

- stable list of all labels
- maps `id` → file paths → metadata
- supports offline pack building and integrity checks

### Optional: texture atlas
If you have many tiny labels:
- build an atlas (sprite sheet)
- include padding between sprites
- generate a deterministic mapping JSON

> [!NOTE]
> Atlasing is a performance tradeoff: fewer requests vs. bigger decode/memory. Use it for *many tiny assets*, not for a handful of plates.

---

## ✅ QA checklist (before merging)

- [ ] Filename follows convention (category/slug/variant/version)
- [ ] Asset has `.asset.json` with license + attribution + provenance
- [ ] Classification/sensitivity is set correctly
- [ ] Readable at target sizes (desktop + mobile)
- [ ] No edge halos / alpha fringes
- [ ] File size is reasonable (avoid megabyte plates unless absolutely needed)
- [ ] (If used in stories) tested during camera motion + transitions
- [ ] (If sensitive) includes generalized public-safe variant (or stays restricted)

---

## 📚 Project references (why these rules exist)

These conventions align with KFM’s core design pillars:
- **2D/3D/AR storytelling** (labels used as narrative anchors and AR markers)
- **provenance-first + evidence-based UI** (every visualization has traceable context)
- **FAIR/CARE governance** (sensitive data and cultural protocols are first-class)
- **deterministic pipelines + policy-as-code** (repeatable builds; CI rejects violations)

Reference documents in this repo/library:
- 📘 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*  
- 🧭 *Kansas Frontier Matrix – Comprehensive UI System Overview*  
- 📥 *Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide*  
- 🤖 *Kansas Frontier Matrix (KFM) – AI System Overview*  
- 🏗️ *Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design*  
- 🌟 *Kansas Frontier Matrix – Latest Ideas & Future Proposals*  
- 💡 *Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)*  
- 🧩 *Additional Project Ideas*  
- 📚 *AI Concepts & more* (PDF portfolio; embedded AI/ML references)  
- 🗺️ *Maps–GoogleMaps–VirtualWorlds–Archaeological–Computer Graphics–Geospatial–WebGL* (PDF portfolio; embedded WebGL/graphics references)  
- 🧰 *Various programming languages & resources 1* (PDF portfolio; embedded web/security/engineering references)  
- 🗄️ *Data Management–Theories–Architectures–Data Science–Bayesian Methods–Some Programming Ideas* (PDF portfolio; embedded data engineering/governance references)

---

### 🧾 Maintainers: policy hook ideas (optional but recommended)

> [!TIP]
> Consider enforcing these via the Policy Pack / CI:
> - reject textures without `.asset.json`
> - reject unknown licenses
> - reject restricted assets in public builds
> - verify sha256 + file headers (anti-spoofing)
> - enforce max dimensions/bytes for mobile/offline pack tiers

