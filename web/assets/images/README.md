# 🖼️ `web/assets/images/` — Image Asset Library

> **Kansas Frontier Matrix (KFM)** web image assets, managed **provenance-first** 📌  
> This folder is for *runtime-ready* images used by the web client (UI, maps, thumbnails, textures, diagrams).

---

## 🎯 Purpose

This directory exists to keep KFM’s visuals:

- **Fast** ⚡ (small, cacheable, responsive)
- **Trustworthy** ✅ (auditable + source-traceable)
- **Consistent** 🎨 (shared design language across UI + maps)
- **Safe to ship** 🛡️ (licensed, privacy-aware, no mystery assets)

KFM’s platform goal is “searchable, mappable, auditable, and modelable” spatial truth with **citations and metadata as first-class data**—this folder follows the same philosophy for visual assets.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ What belongs here

**Put the “built/served” version here**, not giant raw sources.

### Typical assets
- 🧩 **UI icons** (prefer SVG)
- 🧭 **Map UI icons** (pins, legends, compass, scalebars)
- 🗺️ **Map thumbnails** / preview images
- 🛰️ **Remote sensing previews** (RGB composites, NDVI screenshots, etc.)
- 🧱 **WebGL textures** (tilesets, normal maps, sprites)
- 📚 **Documentation images** used by the web app (tutorials, onboarding)

### 🚫 Don’t put here
- ❌ Raw GeoTIFFs / huge satellite exports  
- ❌ Unlicensed screenshots from proprietary sources  
- ❌ Images with sensitive personal data (faces, license plates, private addresses)
- ❌ “Mystery files” with no attribution or provenance

> Rule of thumb: if it’s **not ready to be served publicly**, it does **not** belong here.

---

## 🗂️ Folder layout convention

Keep structure predictable. Suggested layout (adjust as the repo evolves):

| Folder | Use | Preferred formats |
|---|---|---|
| `icons/` | Small UI icons (mono/duotone) | `svg` |
| `logos/` | Project/org logos | `svg`, `png` |
| `ui/` | Illustrations, onboarding, UI imagery | `svg`, `png`, `webp` |
| `maps/` | Thumbnails, legends, symbology exports | `png`, `webp` |
| `satellite/` | Remote sensing previews for UI | `webp`, `jpg` |
| `textures/` | WebGL textures/material maps | `png`, `ktx2` (if used) |
| `tiles/` | Raster tiles or tile previews | `png`, `jpg`, `webp` |
| `docs/` | Images embedded in in-app docs/help | `png`, `webp` |

✨ If you add a new top-level category, add it to this table.

---

## 🏷️ Naming rules

### ✅ DO
- Use **kebab-case**: `map-legend-streamflow.png`
- Keep names **semantic**: `ui-onboarding-step-2.webp`
- Include resolution hints only when needed:
  - `@2x` / `@3x` for retina assets (especially PNG)
  - `-thumb` for thumbnails

### 🚫 DON’T
- Don’t use spaces or “final_final2.png”
- Don’t bake meaning that will change into a *stable identifier* (see below)

---

## 🧱 Stable identifiers (cache + long-term sanity)

KFM design is big on **stability** and avoiding fragile identifiers. Apply that here too:

- Treat **asset IDs** as stable (don’t rename casually)
- Prefer either:
  - **Content hashing** (best for caching): `legend.ab12cd34.webp`
  - Or **information-light IDs**: `kfm-asset-0193.webp`

This reduces breakage when map layers, labels, or UI wording evolves. (This echoes the “stable identifier” mindset used in flexible system design.)  [oai_citation:1‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)

---

## 🧪 Provenance & metadata sidecars (required for derived/third‑party)

Any asset that is **(a)** derived from data, **(b)** based on a historical scan, **(c)** exported from Earth Engine, **(d)** AI-assisted, or **(e)** copied from elsewhere must include a **sidecar** file:

- `your-image.webp`
- `your-image.webp.meta.json`

### Minimal `*.meta.json` schema (recommended)
```json
{
  "id": "maps-kansas-territory-1860-thumb",
  "title": "Kansas Territory 1860 — thumbnail",
  "kind": "thumbnail",
  "created_at": "2026-01-14",
  "created_by": "kfm-web",
  "license": "Public Domain | CC BY 4.0 | CC0 | ...",
  "sources": [
    {
      "label": "Archive / collection name",
      "locator": "catalog-id-or-url-or-internal-path",
      "accessed_at": "2026-01-14"
    }
  ],
  "derived_from": [
    "data/rasters/kansas_1860_georef.tif"
  ],
  "processing": [
    "crop: bounds=(...)",
    "resize: 1024x768",
    "encode: webp q=80"
  ],
  "notes": "Anything a reviewer needs to trust this image."
}
```

### When metadata is optional
For purely original UI icons you drew in-house (SVG), you can skip the sidecar **if**:
- The SVG is clean + authored by the project
- No third-party source material was traced/copied

---

## 🧊 Formats & compression rules

### Format picks (pragmatic defaults)
- **SVG** ✅ for icons, logos, simple illustrations
- **PNG** ✅ for transparency + crisp UI raster
- **JPG** ✅ for photos (no transparency)
- **WebP** ✅ default for modern web delivery (good compression)
- **AVIF** ✅ optional if pipeline supports it reliably
- **KTX2/Basis** ✅ optional for GPU textures if we adopt it

(See the image-format reference in the project library.) `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### Compression targets (budget mindset)
- `icons/*.svg`: as small as possible (SVGO-clean)
- `ui/*`: aim **< 200 KB**
- `maps/*` thumbnails: aim **< 250 KB**
- `satellite/*` previews: aim **< 500 KB** (unless justified)
- Anything above **1 MB** should trigger a “why?” discussion in PR

---

## 📱 Responsive usage checklist (frontend)

When referencing images in the UI:

- Use `srcset` + `sizes` for raster images where applicable
- Prefer CSS/HTML layouts that don’t distort aspect ratio
- Avoid embedding text inside images (i18n + accessibility)

(Aligned with responsive web layout practices.) `responsive-web-design-with-html5-and-css3.pdf`

Example (generic HTML):
```html
<img
  src="/assets/images/maps/kansas-thumb.webp"
  srcset="/assets/images/maps/kansas-thumb.webp 1x,
          /assets/images/maps/kansas-thumb@2x.webp 2x"
  alt="Thumbnail map of Kansas layers"
  loading="lazy"
/>
```

---

## 🗺️ Geospatial + cartography notes

Images in this folder often represent **map truth**. For map-related exports:

- 🧭 Include context when needed: legend, scale, date, layer names
- 🎚️ Avoid misleading symbology (don’t “beautify” away meaning)
- 🧾 Record styling choices if the image is used as evidence (in `*.meta.json`)
- 📐 If a screenshot is used for interpretation, label it as such

Helpful project references:
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `python-geospatial-analysis-cookbook.pdf`

---

## 🛰️ Remote sensing preview rules

For satellite/remote sensing derived imagery:

- Store only **UI-scale previews** here (not analysis rasters)
- Always record:
  - band combination / index used (RGB, NDVI, etc.)
  - date range
  - cloud masking steps (if any)
  - resampling method
- Keep the **original analytic output** outside this folder (data pipeline)

Reference: `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

---

## 🧊 WebGL / 3D texture rules (if applicable)

If the web client uses WebGL rendering:

- Prefer **power-of-two** textures (e.g., 256/512/1024) when it matters
- Keep normal maps / roughness maps clearly named:
  - `terrain-albedo.webp`
  - `terrain-normal.png`
  - `terrain-roughness.png`
- Document intended usage (tiling, UVs, color space)

Reference: `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`  
3D GIS reference context:  [oai_citation:2‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)

---

## ♿ Accessibility rules (non-negotiable)

- Every image used in UI needs appropriate **alt text**
- Decorative images should use empty alt (`alt=""`) if applicable
- Don’t rely on color alone to communicate categories (legends/icons)
- Avoid tiny text in raster images—use real UI text when possible

---

## 🛡️ Security + ethics

KFM is built to augment humans with **transparent, evidence-backed** outputs—visuals must follow the same spirit.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Never commit:
- credentials, tokens, keys in screenshots
- private user data
- operational security-sensitive system diagrams intended for internal only

Security mindset references:
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

Ethics / governance references:
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

---

## ✅ PR checklist for adding/updating images

- [ ] File name follows conventions (kebab-case)
- [ ] File size is reasonable (or PR explains why not)
- [ ] Format is appropriate (SVG/PNG/WebP/etc.)
- [ ] If derived/third-party: `*.meta.json` present and complete
- [ ] If map/satellite: processing steps + date recorded
- [ ] UI usage includes alt text + responsive handling
- [ ] License is compatible with KFM’s open distribution goals

---

## 📚 Project reference shelf (used to shape these standards)

These docs informed the design philosophy, performance expectations, provenance practices, and map/media considerations behind this folder.

### Core system & trust model
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Flexible Software Design (stable identifiers + adaptability mindset)  [oai_citation:5‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
- Database Performance at Scale (performance + scaling mindset)  [oai_citation:6‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)

### Geospatial / mapping / 3D
- Archaeological 3D GIS  [oai_citation:7‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
- making-maps-a-visual-guide-to-map-design-for-gis.pdf
- Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf
- python-geospatial-analysis-cookbook.pdf

### Web / UI / rendering
- responsive-web-design-with-html5-and-css3.pdf
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
- compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf

### Modeling / analysis context (why images appear: charts, plots, outputs)
- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- Understanding Statistics & Experimental Design.pdf
- regression-analysis-with-python.pdf
- Regression analysis using Python - slides-linear-regression.pdf
- think-bayes-bayesian-statistics-in-python.pdf
- graphical-data-analysis-with-r.pdf
- Data Spaces.pdf
- Scalable Data Management for Future Hardware.pdf
- Spectral Geometry of Graphs.pdf
- Generalized Topology Optimization for Structural Design.pdf
- Understanding Machine Learning: From Theory to Algorithms  [oai_citation:8‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)

### Governance / human-centered guardrails
- Introduction to Digital Humanism.pdf
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf

### Tooling / programming reference library (project bookshelf)
> These are broad references that may influence how we generate, validate, and ship image assets.
- A programming Books.pdf
- B-C programming Books.pdf
- D-E programming Books.pdf
- F-H programming Books.pdf
- I-L programming Books.pdf
- M-N programming Books.pdf
- O-R programming Books.pdf
- S-T programming Books.pdf
- U-X programming Books.pdf

Also surfaced references:
- Objective-C Notes for Professionals (GoalKicker)  [oai_citation:9‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- Implementing Programming Languages (tooling mindset; compilers/pipelines)  [oai_citation:10‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  
- MATLAB Notes for Professionals  [oai_citation:11‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e)  
- Bash Notes for Professionals + Linear Algebra for ML excerpt  [oai_citation:12‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  

---

## 🧩 Optional (recommended next files in this folder)

If/when we formalize this folder further, consider adding:

- `manifest.json` → maps logical asset IDs → paths (esp. if hashed filenames)
- `ATTRIBUTIONS.md` → consolidated attributions for third-party imagery/icons
- `LICENSES/` → copies of licenses required by specific asset packs (if needed)

🧭 Keep it simple: the goal is *trust + performance*, not paperwork.