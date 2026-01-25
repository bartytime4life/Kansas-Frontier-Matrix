# 🪧 Signage Decals (Shared Texture Library)

![Asset](https://img.shields.io/badge/asset-3D%20decal%20textures-blue)
![Scope](https://img.shields.io/badge/scope-signage%20%26%20placards-informational)
![Principle](https://img.shields.io/badge/principle-provenance--first-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)
![Runtime](https://img.shields.io/badge/runtime-WebGL%20%2F%20Cesium%20%2F%20MapLibre-orange)

> **Folder:** `web/assets/3d/shared/textures/decals/signage/`  
> **Mission:** reusable **sign faces / placards / wayfinding decals** that can be applied to 3D sign meshes, billboards, and UI-adjacent overlays — while staying **fast, accessible, and ethically governed**. 🧭

---

<details>
<summary><strong>📚 Table of Contents</strong></summary>

- [🎯 What belongs here](#-what-belongs-here)
- [🧩 How KFM uses signage decals](#-how-kfm-uses-signage-decals)
- [📁 Recommended layout](#-recommended-layout)
- [🏷️ Naming and versioning](#️-naming-and-versioning)
- [🧾 Metadata sidecars](#-metadata-sidecars)
- [🎨 Design and accessibility rules](#-design-and-accessibility-rules)
- [⚙️ Technical specs (web-first)](#️-technical-specs-web-first)
- [🛡️ Licensing, sensitivity, and ethics](#️-licensing-sensitivity-and-ethics)
- [🔁 Contribution workflow](#-contribution-workflow)
- [🧪 QA checklist](#-qa-checklist)
- [🧩 Usage patterns](#-usage-patterns)
- [🚧 Roadmap](#-roadmap)

</details>

---

## 🎯 What belongs here

✅ **Belongs here**
- **Sign faces** (e.g., “Historical Marker”, “Trailhead”, “No Entry”, “Warning”, “Museum Exhibit”).
- **Placards & plaques** intended to be mapped onto a **flat/curved sign mesh** (UV-mapped).
- **Billboard-ready** decal art (e.g., marker boards) when the 3D layer needs “readable at a glance” signage.
- **AR-friendly** simplified signage variants (large shapes, minimal text).

🚫 **Does *not* belong here**
- UI-only icons (toolbar, buttons, map legend sprites) → those live in the UI icon system.
- Full 3D models (posts, frames, kiosks) → those belong in `.../models/...`.
- Source PSD/AI files larger than sanity (keep sources in `_src/` or a dedicated source archive, not in the runtime folder).

---

## 🧩 How KFM uses signage decals

KFM’s UI/3D stack is designed around **2D + 3D exploration (MapLibre + Cesium)** and “the map behind the map” (provenance surfaced everywhere). Signage decals participate in that same philosophy:

- **3D world (Cesium / 3D Tiles / glTF):** decals are applied to sign meshes or used as billboard textures for POIs.
- **Story & focus experiences:** signage can act as **visual anchors** for story nodes, tooltips, or “Pulse Thread” affordances (where appropriate).
- **Offline packs & performance:** decals should be light enough to ship in offline bundles without dragging UX down.
- **Governance & trust:** decals may indirectly reveal sensitive places/events. Treat them as **publishable outputs** with the same CARE/FAIR sensitivity discipline used for datasets.

---

## 📁 Recommended layout

Use subfolders to keep preloading and discoverability sane (especially for 3D scenes that can benefit from “load all signage for this theme/area”). 🗂️

```text
web/assets/3d/shared/textures/decals/signage/
├─ 📄 README.md                          # 📘 Signage decal rules: naming, licensing, SVG→raster workflow, and usage constraints
├─ 🧾🗂️ signage.index.json                # Optional registry (generated/curated): decalId → folder + tags + preview + license refs
├─ 🧩 _templates/                         # Copy/paste templates for consistent metadata sidecars
│  └─ 🧩🧾 signage.meta.template.json      # Template: provenance, license, authoring source, intended use, restrictions
├─ 🎨 _src/                               # Optional authoring sources (SVGs, layered masters; avoid huge binaries)
│  └─ 🎨 …                                # Source files live here (not served; keep light or externalize)
├─ 🏛️ historic-marker/                    # Historic marker style decals (placards, interpretive signage; evidence-linked)
├─ 🧭 wayfinding/                         # Wayfinding signage (arrows, labels, navigation cues; keep generic/reusable)
├─ ⚠️ warnings/                           # Warning decals (hazards, cautions; avoid trademarked real-world marks)
├─ 🚫 regulatory/                         # Regulatory signage (only if legally/ethically safe + licensed/approved)
├─ 🏛️ museum/                             # Museum/exhibit signage decals (label cards, exhibit markers; curated)
└─ 🧵 pulse/                               # Pulse Thread markers (if signage art is used as pulse/map markers)
```

> Tip 💡: If a decal is used only by a single experience, consider placing it closer to that feature — but **shared signage** should live here.

---

## 🏷️ Naming and versioning

### Filename format (recommended)

Use **lowercase kebab-case**, ASCII-only, and a predictable suffix strategy:

```text
<category>/<slug>__<lang>__v###.<ext>
```

Examples:
- `historic-marker/kshs-standard-marker__en__v001.png`
- `warnings/no-trespassing__en__v002.ktx2`
- `wayfinding/trailhead-arrow-north__en__v001.png`
- `museum/exhibit-label-template__en__v001.png`

### Variants

Add suffixes **only when truly needed**:
- `__hc` → high-contrast variant  
- `__dark` / `__light` → theme-specific versions (prefer shader tinting first)

Example:
- `warnings/sensitive-location-warning__en__v001__hc.png`

### Version rules

- **Bump `v###`** when the *visual meaning* changes (iconography, wording, symbolism).
- Keep older versions if referenced in published stories/tiles to preserve reproducibility.
- Use metadata to mark a decal as deprecated (instead of deleting).

---

## 🧾 Metadata sidecars

Every runtime decal **must** ship with a metadata sidecar:

```text
<filename>.<ext>
<filename>.meta.json
```

Example:
```text
historic-marker/kshs-standard-marker__en__v001.png
historic-marker/kshs-standard-marker__en__v001.meta.json
```

### Required fields (minimum contract)

```json
{
  "id": "signage.historic-marker.kshs-standard-marker.en.v001",
  "title": "KSHS Standard Historical Marker",
  "category": "historic-marker",
  "language": "en",
  "summary": "Standard Kansas historical marker face decal for sign meshes.",
  "license": "CC-BY-4.0",
  "attribution": "Kansas Historical Society (verify)",
  "sources": [
    {
      "type": "reference",
      "citation": "…",
      "uri": "…",
      "retrieved": "2026-01-25"
    }
  ],
  "sensitivity": "public",
  "created_by": "your-handle",
  "created_at": "2026-01-25",
  "derived_from": [
    {
      "kind": "vector",
      "path": "_src/kshs-standard-marker.svg",
      "notes": "Original vector recreated from public reference."
    }
  ]
}
```

### Recommended fields (KFM-aligned “evidence-first”)

Add these when possible:
- `prov` → link to a PROV-style statement, pipeline run ID, or transformation notes
- `tags` → e.g., `["wayfinding","trail","outdoors"]`
- `usage` → where it’s intended to appear (`"3d-sign-mesh"`, `"billboard"`, `"ar-overlay"`)
- `review_required` → e.g., `["tribal-review"]`, `["legal-review"]`
- `restrictions` → human readable rules (`"no-commercial"`, `"no-derivatives"`, etc.)
- `checksums` → sha256 for `.png` / `.ktx2` artifacts

---

## 🎨 Design and accessibility rules

### 1) Legibility > ornament ✨
KFM signage is often consumed:
- while panning a map,
- in a 3D camera orbit,
- on mobile,
- or in AR overlays.

So: **big shapes, clear symbols, minimal text.**

### 2) Text is a last resort 🔤
If text is required:
- keep it short,
- prefer open-licensed fonts,
- and ensure it survives mipmapping + compression.

If a sign needs paragraphs, consider:
- using the sign mesh as a “header” only, and
- rendering the full text in a UI panel (with provenance + citations).

### 3) Contrast and color-blind safety 👁️
- Provide `__hc` variants when the standard decal risks low contrast.
- Avoid “red vs green only” encoding for meaning.
- Keep a clean silhouette — it matters more than color.

### 4) Style consistency (shared world language) 🧩
- Use consistent stroke weights and corner radii.
- Keep iconography consistent with KFM’s story + map language (Pulse, warnings, POIs).

---

## ⚙️ Technical specs (web-first)

### Preferred formats
- **Authoring:** `SVG` (ideal) or layered source in `_src/`  
- **Runtime:**  
  - `PNG` when alpha fidelity is critical and file size is acceptable  
  - `KTX2` (Basis) when shipping large sets to WebGL/Cesium for GPU-friendly compression

> Rule of thumb: if it’s used *everywhere* and loads often → strongly consider `KTX2`.

### Resolution targets (power-of-two)
- Small decals: **256×256**
- Standard signage: **512×512** or **1024×1024**
- Large placards: **1024×1024** or **2048×2048** (rare — justify in PR)

### Alpha rules
- Store **straight alpha** (avoid premultiplied halos unless your pipeline is consistent end-to-end).
- Add **edge padding/extrusion** (at least 8px) to reduce mip-bleed.

### Color space
- Sign face color textures: **sRGB**
- If you ever add “data textures” (masks): **linear** (and document it in metadata)

### Performance budgets (targets)
These are targets, not laws — but CI may enforce them later:
- Prefer individual decals **< 250 KB PNG** or **< 150 KB KTX2**
- Avoid adding “dozens of 2MB signs” to shared packs
- If a new set is heavy, propose a **pack split** by theme or experience

---

## 🛡️ Licensing, sensitivity, and ethics

This folder is part of the KFM “publishable surface.” That means:

### ✅ License and attribution are mandatory
- Every decal must declare `license` and `attribution`.
- If you derived from third-party icon sets, include the source and license.
- Avoid trademarks/logos unless explicitly cleared.

### ⚠️ Sensitive locations and cultural materials
Signage can leak sensitive information (sometimes unintentionally). Examples:
- a sign that names a protected archaeological site,
- a placard that implies an exact location for endangered species habitat,
- culturally sensitive imagery or language.

**Expect review gates** for anything that touches:
- tribal lands / indigenous cultural data,
- sacred sites,
- endangered species,
- personal data (PII) or modern addresses.

> If in doubt: mark `sensitivity: "sensitive"` and add `review_required`.

### 🤖 AI-generated signage
Allowed only if:
- clearly labeled in metadata (`"generated_by_ai": true`)
- prompt + model + post-processing steps are recorded
- you verify rights/usage (don’t “wash” copyrighted training outputs into the repo)

---

## 🔁 Contribution workflow

1. **Choose a category** folder (or create one).
2. Create the decal (`SVG → PNG/KTX2` export).
3. Add the `.meta.json` sidecar.
4. If needed, update `signage.index.json`.
5. Open a PR with:
   - a screenshot/mock showing intended usage
   - license proof / source citation
   - note any sensitivity concerns

---

## 🧪 QA checklist

Before merging ✅:

- [ ] File name matches conventions (kebab-case + version).
- [ ] `.meta.json` exists and includes **license + attribution + sources**.
- [ ] Looks good at 25%, 50%, 100% scale (mip + blur resistance).
- [ ] No visible alpha halo / edge bleed.
- [ ] Contrast is acceptable (or `__hc` variant provided).
- [ ] Sensitivity classification is set correctly.
- [ ] No forbidden content (trademarks, PII, restricted cultural materials).
- [ ] File size is reasonable for web/offline packs.

---

## 🧩 Usage patterns

### Pattern A: UV-mapped sign mesh (preferred)
- Model a sign board mesh with clean UVs.
- Apply decal as `baseColor` (and optionally `emissive` if needed).
- Keep textures in predictable category folders to enable preloading.

### Pattern B: Billboard signage (when you need “always facing camera”)
- Use a plane with billboard behavior / camera-facing transform.
- Prefer simplified signage with strong silhouettes.

### Pattern C: AR overlay marker
- Use minimal text.
- Use `__hc` variants if outdoors glare is expected.

---

## 🚧 Roadmap

- 🧰 Add `texture_qa` tooling (size/format validation + metadata lint)
- 🧾 Generate `signage.index.json` automatically from sidecars
- 🗜️ Standardize PNG → KTX2 conversion in CI
- 🖼️ Create a small “Signage Gallery” dev page to preview decals
- 🔐 Attach provenance attestations for asset packs (SLSA/SBOM/PROV-friendly)

---

**Maintainer note:** keep this folder boring, predictable, and well-documented. That’s how we scale trust. 🧭✨

