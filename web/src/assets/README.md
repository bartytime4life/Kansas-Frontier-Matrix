# 🎒 `web/src/assets/` — KFM UI Assets

> **Static, versioned, front-end assets** for the Kansas Frontier Matrix (KFM) web app 🗺️✨  
> Think: **icons, images, map UI sprites, fonts, and visual resources** — not datasets.

---

## ✅ What belongs here?

These assets are **UI-only** resources used by the React app (and the map UI) for presentation:

- 🧩 **Icons** (UI controls, toolbars, layer toggles, legend symbols)
- 🖼️ **Images** (UI illustrations, empty states, backgrounds, story banners *if they’re purely visual*)
- 🔤 **Fonts** (web fonts + any mapping typography resources used by the UI)
- 🧭 **Map UI assets** (MapLibre sprites, style JSON snippets, marker packs, etc.)
- 🎞️ **Micro-animations** (e.g., Lottie JSON) where appropriate

---

## 🚫 What does *not* belong here?

KFM is **evidence-first**. Anything that is “data” (or could be mistaken as evidence) must live in governed locations and flow through the canonical pipeline.

**Do not store these in `web/src/assets/`:**
- 🧪 Raw/processed datasets (GeoJSON, CSV, Parquet, rasters, LiDAR, etc.)
- 🗃️ Catalog artifacts (STAC/DCAT/PROV outputs)
- 🧾 “Evidence images” that are used as *sources* (scans, archival documents, etc.)
- 🧱 Map tiles (PMTiles/MVT pyramids), large basemaps, or time-series imagery

> 🧠 Rule of thumb: **If it can be cited as evidence, it’s not a UI asset.**  
> Put it in governed data/docs locations and serve it through APIs (the “truth path”).

---

## 🗂️ Recommended folder layout

You can adapt this structure as the UI grows. Keep it boring, predictable, and searchable. 🧼

```text
web/src/assets/
├── 🧩 icons/                  # UI icons (SVG preferred)
│   ├── ui/                    # buttons, controls, panels
│   └── map/                   # map-related icons (markers, layer icons)
├── 🖼️ images/                 # UI imagery (photos/illustrations)
│   ├── ui/                    # empty states, onboarding, misc UI images
│   ├── story/                 # story visuals used in the UI (NOT evidence scans)
│   └── placeholders/          # skeletons, fallback images
├── 🧭 map/                    # Map UI assets (MapLibre/Cesium helpers)
│   ├── styles/                # style JSON, theme fragments, basemap configs
│   ├── sprites/               # MapLibre sprite sheets + JSON manifest
│   ├── markers/               # marker packs + legend icons
│   └── legends/               # legend swatches/icons (UI-only)
├── 🔤 fonts/                  # web fonts (subset where possible)
├── 🧪 textures/               # Cesium / 3D textures (if needed)
├── 📄 attributions/           # attribution snippets + source notes (UI assets)
└── 📘 README.md               # you are here ✨
```

---

## 🏷️ Naming conventions (keep it consistent)

- Use **kebab-case**: `layer-toggle-on.svg`
- Prefer **semantic names** over generic: `timeline-handle.svg` ✅ vs `icon12.svg` ❌
- For variants, use suffixes:
  - Theme: `kfm-logo-dark.svg`, `kfm-logo-light.svg`
  - Density: `marker-school@2x.png` (only for bitmap assets)
- If an asset is shared broadly, prefix it:
  - `kfm-…` (brand/global)
  - `map-…` (mapping)
  - `ui-…` (interface)

---

## 🧾 Formats: pick the right tool for the job

| Use case 🎯 | Preferred ✅ | Avoid 🚫 | Notes 📝 |
|---|---|---|---|
| Logos / icons / simple shapes | **SVG** | PNG/JPG | Small, crisp, themeable, ideal for UI |
| Photos / complex images | **JPG** (or WebP if supported) | PNG | JPG compresses well for photos |
| Flat art w/ transparency | **PNG** | JPG | PNG keeps sharp edges + alpha |
| Map sprites / marker sheets | **PNG + JSON** | JPG | Sprites often need alpha + precise pixels |
| Animations | **Lottie (JSON)** / MP4 | GIF | GIF is heavy + low-fidelity for most UI use |
| Tiny repeating textures | PNG | JPG | Avoid artifacts on repeating patterns |

> ⚡ Performance mindset: “**Every KB competes with map tiles**.”  
> Keep assets lean so map interactivity stays snappy.

---

## 🗺️ Map assets notes (MapLibre + Cesium)

### 🧭 MapLibre sprites
If you use MapLibre sprite sheets, keep **all paired files together**:

- `kfm-sprite.png`
- `kfm-sprite@2x.png` (optional)
- `kfm-sprite.json`

**Do:**
- ✅ Keep sprite pixel grid aligned
- ✅ Keep consistent icon styling (stroke, corner radius, visual weight)
- ✅ Document symbol meaning (especially if used in legends)

**Don’t:**
- 🚫 Dump random icons into the sprite sheet without design consistency
- 🚫 Change sprite names without updating the style JSON

### 🌍 Cesium / 3D
If Cesium is enabled for a 3D view, you may need:
- 🌌 skybox textures
- 🧱 terrain/imagery UI placeholders
- 🧪 light textures / simple materials (rare)

Keep 3D-specific assets in `textures/` to prevent cross-contamination with 2D UI concerns.

---

## 🧑‍⚖️ Licensing & attribution (non-negotiable)

KFM’s trust model depends on provenance and clarity — **even for UI assets**.

When adding third‑party assets (icons/fonts/images):
- ✅ Include the license text or reference in `attributions/`
- ✅ Record source + author + license + version/date
- ✅ Prefer permissive licenses compatible with the repo

> 🧾 If an asset has licensing ambiguity, don’t ship it.

---

## ➕ Adding a new asset (checklist)

1. 🔎 **Decide if it’s UI-only**
   - If it’s evidence/data → it **does not** belong here.
2. 🗂️ Put it in the right folder (`icons/`, `images/`, `map/`, etc.)
3. 🧼 Optimize it
   - SVG: remove editor metadata, compress paths (SVGO-style workflow)
   - PNG/JPG: export at the **actual** display size, then compress
4. ♿ Make it accessible
   - Ensure the calling component supplies `alt=""` or meaningful alt text
   - Avoid text baked into images unless unavoidable
5. 🧾 Add attribution if needed (`attributions/`)
6. 🧪 Verify usage
   - No broken imports
   - No unused “dead” assets

---

## 🧯 Common pitfalls

- 🧱 **Large “assets” creeping in** (photos at 6000px wide, giant PNGs)
- 🗺️ **Map symbols drifting** (inconsistent icon sets across layers)
- 🎨 **Theme mismatch** (dark-mode icons that disappear)
- 📦 **Untracked licensing** (the fastest way to create future cleanup pain)

---

## 🔗 Related (in-repo) docs

- 📚 KFM master guide: `../../../docs/MASTER_GUIDE_v13.md`
- 🏛️ Architecture docs: `../../../docs/architecture/`
- 🧾 Story content (governed): `../../../docs/reports/story_nodes/`
- 🗃️ Data & catalogs (governed): `../../../data/`

---

<details>
<summary>✨ Philosophy: “The map behind the map” (why this folder is strict)</summary>

KFM is built so that the UI is *never* the source of truth.  
Assets are allowed to make the interface beautiful and usable — but evidence must remain governed, traceable, and API-served.

**UI ≠ data.**  
This folder stays clean so the “truth path” stays defensible. 🧭✅

</details>
