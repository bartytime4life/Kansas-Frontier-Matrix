# 🎨 KFM Web Assets — `web/assets/`

[![Assets](https://img.shields.io/badge/web-assets-111827?logo=files&logoColor=white)](#-kfm-web-assets--webassets)
[![Maps](https://img.shields.io/badge/maps-MapLibre%20%7C%20Leaflet-2b9348)](#-map-assets-styles-sprites-glyphs)
[![3D](https://img.shields.io/badge/3D-WebGL%20%7C%20Cesium-0b7285)](#-3d-assets-models-textures-shaders)
[![UX](https://img.shields.io/badge/ux-responsive-images%20%7C%20a11y-ff922b)](#-images--icons-responsive-by-default)
[![Policy](https://img.shields.io/badge/policy-no-secrets%20%7C%20licensed%20%7C%20optimized-red)](#-non-negotiables)

> 🧭 **Purpose:** `web/assets/` is the **static, versioned, front-end-facing** asset library for Kansas Frontier Matrix (KFM).  
> It feeds the UI’s **maps, charts, 3D views, and visual language** while staying consistent with KFM’s modular architecture and governed boundaries.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)

---

## 🔗 Quick links

- [🧱 Non-negotiables](#-non-negotiables)
- [🗂️ Recommended structure](#️-recommended-structure)
- [🖼️ Images & icons](#️-images--icons-responsive-by-default)
- [🗺️ Map assets](#️-map-assets-styles-sprites-glyphs)
- [🧊 3D assets](#-3d-assets-models-textures-shaders)
- [📦 Build + caching rules](#-build--caching-rules)
- [🧾 Attribution & licensing](#-attribution--licensing-required)
- [✅ PR checklist](#-pr-checklist-assets)

---

## 🧱 Non-negotiables

### 🔒 1) No secrets. Ever.
Assets are publicly shipped to the browser. Treat everything here as **world-readable**.

✅ OK
- images, icons, fonts (licensed), shader files, map style JSON, sample screenshots

🚫 NOT OK
- API keys, credentials, internal endpoints, private dataset URLs, unredacted sensitive exports

---

### 🧼 2) Optimize by default (performance is a feature)
KFM’s UI is designed to be interactive and performant across devices.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)

- Prefer **responsive images** with `srcset` / `sizes` and the `<picture>` element for art-direction.  [oai_citation:3‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- Use media queries for layout/asset tuning (including HiDPI considerations).  [oai_citation:4‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- Keep large/rare assets lazy-loaded (3D libs, large textures, heavy images).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)

---

### 🧭 3) Map design choices are part of “truth”
Cartography isn’t neutral. Favor simplicity, clarity, and honest representation.  [oai_citation:6‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)

- “Less is more” for map composition (avoid clutter).  [oai_citation:7‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)
- Symbology choices (size/texture/pattern/shape) change meaning—apply intentionally.  [oai_citation:8‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)

---

### 🧩 4) Assets support clean boundaries (don’t bury logic here)
KFM follows clean architecture: core logic remains independent of framework/UI details.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)  
Assets should be **data** (or presentation helpers like shaders), not business rules.

---

## 🗂️ Recommended structure

> Keep this folder **boring and predictable**. The UI (in `web/src`) imports from here.  
> If you add a new category, add it to this README + attribution.

```text
🌐 web/
└── 🎨 assets/
    ├── 🖼️ images/                 # photos, screenshots, UI illustrations (web-friendly formats)
    ├── 🧩 icons/                  # SVG icons + icon sets (prefer SVG)
    ├── 🗺️ maps/
    │   ├── 🎛️ styles/             # MapLibre/Mapbox style JSON, style fragments
    │   ├── 🧷 sprites/            # sprite.png + sprite.json (if used)
    │   ├── 🔤 glyphs/             # font glyphs (if self-hosting)
    │   └── 🎚️ legends/            # legend images + ramp definitions
    ├── 🧊 3d/
    │   ├── 🧱 models/             # glTF/GLB preferred; OBJ only when unavoidable
    │   ├── 🧵 textures/           # compressed textures (KTX2/Basis where possible)
    │   └── ✨ shaders/            # GLSL chunks (versioned + linted)
    ├── 🎞️ media/                 # short mp4/webm clips, demos (avoid huge files)
    ├── 🔤 fonts/                 # licensed fonts (WOFF2 preferred)
    ├── 🧪 samples/               # small sample assets for dev/test only
    └── 🧾 ATTRIBUTION.md         # source + license for every third-party asset
```

---

## 🖼️ Images & icons (responsive by default)

### ✅ Preferred formats
- **SVG** for icons and simple diagrams (scales cleanly)
- **AVIF/WebP** for photographs and complex images (fallback to PNG/JPG as needed)
- For responsive UX, use `srcset` / `sizes` and `<picture>` patterns.  [oai_citation:10‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

### 📏 Practical rules
- Keep UI-critical icons small and local.
- Keep screenshots under control (use them for docs/demos; compress aggressively).
- If an image changes frequently, treat it as content (consider CDN or generated pipeline) rather than bloating the repo.

### ♿ Accessibility reminder
If an asset carries meaning, it needs:
- alt text (for images)
- labels/aria descriptions where appropriate (don’t abuse ARIA; prefer semantic HTML)  [oai_citation:11‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## 🗺️ Map assets (styles, sprites, glyphs)

KFM’s mapping stack is built for interactive layers and time-sliced views.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)  
Assets here typically support:

### 🎛️ Style JSON
Store style JSON with:
- clear naming (`kfm_base_light.json`, `kfm_satellite_overlay.json`)
- versioned layer IDs (stable IDs matter for toggles and UI state)
- attribution blocks (keep legal + honest)

### 🧷 Sprites & glyphs
If you self-host sprites/glyphs:
- include generator instructions (or a script in `web/scripts/`)
- pin versions and document expected paths

### 🎚️ Legends & ramps
Legend design affects interpretation—use consistent visual variables and avoid misleading ramps.  [oai_citation:13‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)

---

## 🧊 3D assets (models, textures, shaders)

KFM uses WebGL for efficient rendering of large spatial data (GPU acceleration).  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)

### ✅ Preferred: glTF / GLB
- modern web pipeline
- efficient packing
- predictable loading

### ⚠️ OBJ is allowed but treated as higher-risk
OBJ pipelines often require parsing, and parsing is an attack surface. The WebGL reference material explicitly calls out OBJ formats and parser code patterns in example viewers.  [oai_citation:15‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
If you must use OBJ:
- keep models tiny
- pre-validate and sanitize
- never load arbitrary user-provided OBJ files in-browser without a hardened pipeline

### 🧭 Coordinate sanity (don’t “flip axes” casually)
WebGL uses x/y/z axes with a conventional right-handed mental model for learning.  [oai_citation:16‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
Also, `<canvas>` pixel space differs from WebGL coordinates and requires mapping.  [oai_citation:17‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  
**Rule:** document the coordinate conventions for every 3D dataset (units, origin, axis orientation).

### 🧵 Shaders
Shaders are “code assets”:
- keep them small, composable (chunks)
- version them with the UI feature they support
- lint/format them (or at least enforce consistent style)

---

## 📦 Build + caching rules

### 🧠 Cache-friendly naming
Prefer:
- content-hashed filenames via bundler output (recommended)
- stable public paths for base style assets (maps/styles can be versioned directories)

### 🧪 Local dev sanity
If you add assets that impact initial load:
- ensure they’re lazy-loaded or behind feature flags
- don’t break offline/dev mode

---

## 🧾 Attribution & licensing (required)

Every third-party asset must be tracked in `web/assets/ATTRIBUTION.md` with:
- source link
- license type
- author/owner
- what we changed (if anything)

> 🧩 Why: asset provenance is part of governance and reproducibility—same mindset as data provenance in KFM workflows.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)

**Suggested entry format:**

| Asset | Source | License | Notes |
|---|---|---|---|
| `icons/foo.svg` | `https://...` | MIT | recolored + simplified |
| `images/bar.webp` | `https://...` | CC-BY 4.0 | cropped |

---

## ✅ PR checklist (assets)

- [ ] No secrets, internal URLs, or sensitive exports added
- [ ] File sizes reasonable (and compressed)
- [ ] Responsive handling added for large images (`srcset`/`picture`)  [oai_citation:19‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- [ ] Map symbology/legend is intentional and not misleading  [oai_citation:20‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)
- [ ] 3D assets documented (units, axes, coordinate assumptions)  [oai_citation:21‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)
- [ ] Third-party assets recorded in `ATTRIBUTION.md`
- [ ] Asset paths stable (no breaking imports without updating `web/src/`)

---

## 📚 Project sources used (library → conventions)

- **KFM – Master Technical Specification** (clean architecture, responsive + interactive Web UX, WebGL usage)  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf](file-service://file-MLtTh4CX1AqH6dNnKyYYEp)
- **Responsive Web Design with HTML5 and CSS3** (responsive images, media queries, semantic HTML + ARIA guidance)  [oai_citation:24‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
- **WebGL Programming Guide** (coordinate systems; 3D model formats + parsing considerations)  [oai_citation:25‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)  [oai_citation:26‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7Nd7iS68ES97NmWhPiRWTP)
- **Geographic Information System Basics** (cartographic design principles; symbology variables)  [oai_citation:27‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)  [oai_citation:28‡Geographic Information System Basics - geographic-information-system-basics.pdf](file-service://file-Kjn2enYFqXQtK3J4zN2DWz)
- **Geoprocessing with Python** (vector/raster IO, formats, spatial reference systems context)  [oai_citation:29‡geoprocessing-with-python.pdf](file-service://file-NkXrdB4FwTruwhQ9Ggn53T)
- **Google Maps JavaScript API Cookbook** (GeoJSON/KML layer handling patterns; layer lifecycle considerations)  [oai_citation:30‡google-maps-javascript-api-cookbook.pdf](file-service://file-6w897pmf6KhF1cHXFQ1zdf)

---
✨ If you’re new: start by adding a small SVG icon, updating `ATTRIBUTION.md`, and wiring it into `web/src/components/` — ship tiny, then scale up.
