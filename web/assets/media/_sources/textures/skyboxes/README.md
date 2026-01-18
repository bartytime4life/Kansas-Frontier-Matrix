<div align="center">

# 🌌 Skyboxes (Source Textures)

![Asset](https://img.shields.io/badge/asset-skybox%20textures-6d28d9?style=flat-square)
![Scope](https://img.shields.io/badge/scope-web%20viewer-0284c7?style=flat-square)
![Folder](https://img.shields.io/badge/location-_sources%2Ftextures%2Fskyboxes-f59e0b?style=flat-square)

</div>

> 🧭 **Purpose:** This folder holds **high-quality *source*** skybox textures used by the KFM web front-end (and future 3D viewers) as environment backgrounds and/or lighting inputs.  
> ✅ *Source-in, optimized-out.* Treat everything here as **inputs** to an optimization/build pipeline — not production-ready assets.

---

## 📍 Where you are

**Path:** `web/assets/media/_sources/textures/skyboxes/`

- `web/` is the front-end’s home for browser-based visualization (static site/app assets) 🧩
- `_sources/` is for **unoptimized originals** (large, lossless, HDR, etc.) 🧱

---

## 🗂️ Recommended folder layout

Keep each skybox self-contained in its own folder with **faces + attribution metadata + preview**.

```text
📁 skyboxes/
├─ 📄 README.md                       👈 you are here
├─ 📁 kansas_clear_day/
│  ├─ 🖼️ px.jpg                       (positive X / right)
│  ├─ 🖼️ nx.jpg                       (negative X / left)
│  ├─ 🖼️ py.jpg                       (positive Y / up)
│  ├─ 🖼️ ny.jpg                       (negative Y / down)
│  ├─ 🖼️ pz.jpg                       (positive Z / front)
│  ├─ 🖼️ nz.jpg                       (negative Z / back)
│  ├─ 🧾 attribution.yml              ✅ REQUIRED
│  └─ 🖼️ preview.webp                 ✅ Recommended (512–1024px)
└─ 📁 studio_neutral_hdr/
   ├─ 🌈 equirect.hdr                 (optional source format)
   ├─ 🧾 attribution.yml              ✅ REQUIRED
   └─ 🖼️ preview.webp                 ✅ Recommended
```

> 💡 **Tip:** If your source starts as a single equirectangular HDRI (`.hdr` / `.exr`), keep it here — but prefer generating cubemap faces for runtime.

---

## 🧾 Attribution is non-negotiable

KFM is “provenance-first” 🧬 — even for “just visuals.” Every skybox must ship with clear attribution & license info.

### ✅ Required file: `attribution.yml`

Minimal template (copy/paste and fill in):

```yaml
id: kansas_clear_day
title: "Kansas Clear Day"
type: cubemap # cubemap | equirect
projection: cube # cube | equirectangular

source:
  url: "https://example.com/original"
  author: "Creator Name"
  publisher: "Site / Organization"
  downloaded_at: "YYYY-MM-DD"

license:
  spdx: "CC-BY-4.0" # use SPDX identifier when possible
  url: "https://creativecommons.org/licenses/by/4.0/"
  attribution_required: true

files:
  # If cubemap:
  faces_order: [px, nx, py, ny, pz, nz]
  # If equirect:
  # equirect: "equirect.hdr"

processing:
  notes: "Any edits performed (crop, denoise, seam fix, tone-map, etc.)"
  tools: ["toolname@version", "script-name-if-any"]
  color_space: "sRGB" # sRGB | linear | HDR
  flip_y: false

integrity:
  sha256: "PUT_HASH_HERE"
```

<details>
<summary>📦 Why so strict?</summary>

KFM’s culture is: **no black boxes**. If an asset appears in the UI, users should be able to trace:
- where it came from,
- what license governs it,
- what transformations were applied.

That’s how the platform stays trustworthy and reusable across schools, agencies, and collaborators. ✅

</details>

---

## 🧊 Cubemap naming conventions

Different engines name faces differently. In KFM, we standardize on:

| Face | Meaning | Filename |
|------|---------|----------|
| +X | right | `px.*` |
| -X | left | `nx.*` |
| +Y | up | `py.*` |
| -Y | down | `ny.*` |
| +Z | front | `pz.*` |
| -Z | back | `nz.*` |

✅ Accepted extensions (source): `.png`, `.jpg`, `.hdr`, `.exr`  
⚠️ Prefer **lossless** (`.png`, `.exr`) for sources if you plan to generate optimized derivatives.

---

## 🏎️ Performance guidance (for eventual production builds)

> 📌 This folder is `_sources` — so it can be heavy.  
> But **sources should still be sane** so repo size stays manageable.

**Recommended:**
- LDR skyboxes (background-only): `jpg` quality ~80–92
- HDR lighting sources: keep `hdr/exr`, but consider storing *one* master and generating derivatives
- Keep face sizes reasonable:
  - 🟢 1024–2048 for general use
  - 🟡 4096 only if you truly need it (and preferably via LFS or external artifact storage)

**Avoid:**
- ❌ Massive uncompressed PNGs if they don’t improve the final result
- ❌ “Unknown license” downloads
- ❌ Watermarked imagery

---

## 🧪 Quick validation checklist

Before committing a new skybox:

- [ ] All 6 faces exist (if cubemap) and match resolution
- [ ] No visible seams at edges
- [ ] Orientation looks correct (no upside-down horizons)
- [ ] `attribution.yml` is complete ✅
- [ ] A `preview.webp` exists for quick browsing 👀
- [ ] File sizes are reasonable (no accidental 100MB commits)

---

## 🧩 Runtime usage patterns (examples)

> ⚠️ These are *examples*. The web app should reference **built/optimized outputs**, not `_sources`.

### CesiumJS-style skybox (future 3D mode) 🪐

```js
viewer.scene.skyBox = new Cesium.SkyBox({
  sources: {
    positiveX: "…/px.jpg",
    negativeX: "…/nx.jpg",
    positiveY: "…/py.jpg",
    negativeY: "…/ny.jpg",
    positiveZ: "…/pz.jpg",
    negativeZ: "…/nz.jpg",
  },
});
```

### Three.js-style skybox (WebGL) 🧊

```js
const sky = new THREE.CubeTextureLoader()
  .setPath("…/skyboxes/kansas_clear_day/")
  .load(["px.jpg", "nx.jpg", "py.jpg", "ny.jpg", "pz.jpg", "nz.jpg"]);

scene.background = sky;
```

---

## 🔧 Adding a new skybox (step-by-step)

1) **Create a folder** with a clear, lowercase slug:
   - `prairie_sunset/`
   - `stormy_overcast/`

2) Drop in either:
   - ✅ **cubemap faces** `px/nx/py/ny/pz/nz`, **or**
   - ✅ a single `equirect.hdr` (then generate faces later)

3) Add **`attribution.yml`** (required) 🧾

4) Add **`preview.webp`** (recommended) 👀

5) If your workflow generates optimized assets elsewhere:
   - keep those outputs **out of `_sources/`**
   - commit them only in the appropriate “built assets” location (project convention)

---

## 🧯 Troubleshooting

<details>
<summary>🔄 My skybox looks flipped / rotated</summary>

Common causes:
- Y-axis flipped during conversion
- Face order mismatch for your renderer
- “Front/back” swapped (Z axis convention differences)

Fix by:
- verifying face order is `[px, nx, py, ny, pz, nz]`
- toggling `flip_y` in your pipeline and recording it in `attribution.yml`

</details>

<details>
<summary>🧵 Visible seams at cube edges</summary>

Typical causes:
- compression artifacts
- editing each face separately without edge-aware tools
- mismatch in tone mapping between faces

Fix by:
- starting from an equirectangular HDR and generating faces from one source
- using edge-aware cubemap tools and ensuring consistent exposure/tone mapping

</details>

---

## 🔗 Related (project-level)

- 📌 Repo root docs describe KFM’s provenance-first and contract/evidence approach.
- 🌍 The web viewer stack is designed around open web mapping (MapLibre/Leaflet), with optional future 3D expansion (e.g., CesiumJS).

---

<div align="center">

✨ *If it shows up in the UI, it needs provenance.* ✨

</div>
