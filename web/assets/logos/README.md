# 🧭 KFM Logos & Brand Assets (`web/assets/logos/`)

![assets](https://img.shields.io/badge/assets-logos-2ea44f?style=flat-square)
![format](https://img.shields.io/badge/format-SVG%20%E2%86%92%20PNG%2FWebP-informational?style=flat-square)
![provenance](https://img.shields.io/badge/provenance-required-blueviolet?style=flat-square)
![a11y](https://img.shields.io/badge/a11y-alt%20text%20required-orange?style=flat-square)
![security](https://img.shields.io/badge/security-SVG%20sanitized-critical?style=flat-square)

This folder is the **single source of truth** for KFM’s visual identity assets used across the web UI: **marks, lockups, favicons, app icons, and approved partner/project logos**.

> [!IMPORTANT]
> KFM’s culture is **provenance-first** and **human-centered**. Logos are “data” too:
> every exported asset should be traceable to its source (who made it, how it was exported, and under what license).

---

## 🧩 What belongs here

✅ **Include**
- KFM core brand assets (marks, lockups, wordmarks)
- UI-facing icons that are brand-adjacent (e.g., “KFM Verified”, “Provenance Badge”)
- Partner/agency logos (only if licensing permits)
- Event/special-mode logos (hackathons, demos, pilots) — **time-bounded + documented**

🚫 **Do NOT include**
- Map tiles, basemaps, rasters (store under data/ or map assets)
- Large photos/hero images (store under `web/assets/images/`)
- Unlicensed logos or “found via Google” images
- Raw design working files (unless explicitly agreed, see “Source Files” policy below)

---

## 📁 Suggested folder layout

> If this repo already uses a different layout, keep the existing structure — but **use the naming + provenance rules** below.

```text
web/assets/logos/
├─ kfm/ 🧭
│  ├─ marks/
│  ├─ lockups/
│  ├─ favicons/
│  ├─ app-icons/
│  └─ badges/
├─ partners/ 🤝
│  ├─ kshs/
│  ├─ usgs/
│  └─ ...
└─ _meta/ 🧾
   ├─ README.md (this file)
   └─ templates/
      └─ logo.meta.yaml
```

---

## ⚡ Quick usage (Web)

### HTML
```html
<img
  src="/assets/logos/kfm/lockups/kfm-lockup-horizontal.svg"
  alt="Kansas Frontier Matrix"
  width="220"
/>
```

### React / Vite (typical patterns)
```ts
import KfmLockup from "@/assets/logos/kfm/lockups/kfm-lockup-horizontal.svg";

export function HeaderBrand() {
  return <img src={KfmLockup} alt="Kansas Frontier Matrix" height={28} />;
}
```

### Responsive (preferred)
Use SVG whenever possible. If raster is necessary (e.g., legacy email templates), ship `1x/2x` and use `srcset`.

```html
<img
  src="/assets/logos/kfm/lockups/kfm-lockup-horizontal@1x.png"
  srcset="
    /assets/logos/kfm/lockups/kfm-lockup-horizontal@1x.png 1x,
    /assets/logos/kfm/lockups/kfm-lockup-horizontal@2x.png 2x
  "
  alt="Kansas Frontier Matrix"
  width="220"
/>
```

---

## 🏷️ Naming conventions

### ✅ Base pattern
`<org>-<asset>-<variant>[-<theme>][@<scale>].<ext>`

Examples:
- `kfm-mark-primary.svg`
- `kfm-lockup-horizontal-dark.svg`
- `kfm-lockup-vertical-light.svg`
- `kfm-favicon-32.png`
- `kfm-appicon-512.png`
- `partner-usgs-logo.svg`
- `partner-kshs-logo.svg`

### 🎨 Theme suffixes
- `-light` → for light backgrounds
- `-dark` → for dark backgrounds
- `-mono` → single-color (preferred for overlays/watermarks)

### 📐 Scale suffixes (raster only)
- `@1x`, `@2x`, `@3x`

---

## 🖼️ Formats: what to use and why

### ✅ Preferred: SVG (vector)
Use SVG for:
- UI headers, nav, footer
- badges, icons
- anything that must scale cleanly

**SVG rules**
- No embedded scripts (`<script>`) ❌
- No external references (`<image href="http…">`) ❌
- Prefer shapes/paths over embedded rasters ✅
- Keep viewBox correct ✅

### ✅ PNG / WebP (raster)
Use raster when:
- platform constraints require it (email, legacy embeds)
- texture-like usage in 3D contexts (WebGL/Cesium overlays)
- you need pixel-perfect rendering at known sizes

**PNG**
- Use for transparency + sharp edges
- Keep background truly transparent (not “white matte”)

**WebP**
- Use for performance if your build pipeline supports it
- Don’t use WebP as the *only* format unless your app guarantees support

### 🚫 Avoid JPEG for logos
JPEG introduces edge artifacts and destroys flat color boundaries.

---

## 🧠 Brand rules (practical, “don’t break the UI” edition)

### Clear space 🧼
- Keep at least **1× mark height** of padding around the logo.
- Never cram the mark into tight corners next to UI controls.

### Minimum size 🔎
- Mark-only: **≥ 20px** height (UI)
- Lockups: **≥ 24–28px** height (UI)
- Favicon: ship dedicated raster sizes (don’t downscale a lockup)

### Backgrounds 🗺️
KFM is a mapping platform — logos are often placed over:
- aerial imagery
- terrain shading
- old scanned maps
- charts & heatmaps

**Therefore**:
- Provide a `-mono` variant for overlays
- Use a subtle “chip” or scrim in UI where contrast is unpredictable

---

## ♿ Accessibility requirements

✅ Always provide meaningful `alt` text:
- If it’s the primary brand: `alt="Kansas Frontier Matrix"`
- If it’s decorative: `alt=""` and `aria-hidden="true"`

✅ Don’t bake text into images when possible (use real text for slogans/taglines).

✅ Ensure contrast when placed on UI backgrounds; don’t rely on color alone to convey meaning.

---

## 🔒 Security (SVG hygiene)

SVG is powerful — and can be dangerous if treated as “just an image”.

**Rules**
- Treat inbound SVG like untrusted input.
- Strip scripts, events, foreignObjects, external refs.
- Prefer a “sanitize step” in CI.

**Recommended checks**
- Ensure no `<script>`, `onload=`, `onclick=`, `xlink:href` to remote URLs
- Ensure `viewBox` is present
- Ensure no huge embedded base64 blobs unless explicitly required

---

## 🚀 Performance tips (logos shouldn’t be your bottleneck)

- Prefer SVG for UI chrome (tiny, cacheable, crisp)
- Cache aggressively (immutable hash filenames are best)
- Keep raster icons power-of-two **if used as WebGL textures** (e.g., 128/256/512)
- Avoid loading “full-size app icon” in normal UI routes

---

## 🧾 Provenance & licensing (non-negotiable)

Every logo should have **documented provenance**.

### Required: sidecar metadata
For each top-level brand asset (and every partner logo), add a sidecar file:

`<filename>.meta.yaml`

Example:
```yaml
name: "KFM Lockup (Horizontal)"
slug: "kfm-lockup-horizontal"
owner: "Kansas Frontier Matrix"
type: "lockup"
source:
  created_by: "YOUR_NAME_OR_TEAM"
  created_on: "YYYY-MM-DD"
  toolchain: ["Figma", "Illustrator"]  # or ["Inkscape"]
license:
  spdx: "CC-BY-4.0"      # or "All-Rights-Reserved", "CC-BY-NC-ND-4.0", etc.
  proof: "link-or-path-to-permission"
exports:
  - file: "kfm-lockup-horizontal.svg"
    role: "primary"
  - file: "kfm-lockup-horizontal-dark.svg"
    role: "dark"
notes: >
  Any constraints, required attribution text, or usage limits.
ai:
  generated: false
  model: null
  prompt: null
```

> [!NOTE]
> If an asset is AI-assisted, record it. If an asset is trademarked, record it. If usage is restricted, record it.

---

## ✅ “Add a new logo” checklist

1. **Confirm license & permission** ⚖️  
2. Create or import **vector master** (preferred) 🧩  
3. Export required variants:
   - `primary`, `dark`, `light`, `mono` (as applicable) 🎨  
4. Create `*.meta.yaml` provenance file 🧾  
5. Optimize assets (SVGO / PNG optimizer) 🧼  
6. Verify accessibility + contrast ♿  
7. Confirm no SVG security hazards 🔒  
8. Commit with a clear message: `assets(logos): add <name> + provenance`

---

## 🧱 Tooling suggestions (optional but recommended)

> These are intentionally standard + cross-platform.

### SVG optimize
```bash
npx svgo -f web/assets/logos --recursive
```

### PNG optimize
```bash
# lossless
oxipng -o 4 -i 0 --strip all web/assets/logos/**/*.png
```

### WebP (if used)
```bash
cwebp -q 90 input.png -o output.webp
```

---

## 📚 Project file influences (why this folder is strict)

This repo spans **GIS, remote sensing, web rendering, databases, modeling, stats/ML, and digital ethics** — logos must work across all of it.

- 🧭 **KFM vision & provenance culture** → logos include traceability + metadata, and UI-safe variants for map overlays
- 🗺️ **Cartography & mobile mapping** → contrast, legibility over complex basemaps, and responsive layout behavior
- 🎛️ **WebGL/3D** → texture-friendly sizes, predictable alpha, and efficient asset delivery
- 🧮 **Modeling, stats, ML** → visual language favors clarity, “no black box” vibes, and honest representation
- 🔐 **Security** → SVG treated as code-adjacent input, sanitized in CI
- 🧑‍🤝‍🧑 **Digital humanism & governance** → respectful, inclusive branding + clear licensing

### Reference library (project files)
> Keep these in your repo’s docs/research area (or wherever you store project PDFs). This list mirrors the current project library.

#### 🌍 Core KFM + architecture
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`

#### 🗺️ GIS / cartography / mapping practice
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

#### 🧠 Stats / ML / analysis literacy
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `Understanding Machine Learning: From Theory to Algorithms.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`

#### 🗄️ Data systems / performance
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

#### 🌐 Web UI / rendering
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

#### 🧩 Modeling / optimization / theory
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Spectral Geometry of Graphs.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

#### 🧭 Ethics / governance / security
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

#### 📦 Programming compendiums (project-wide reference)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

---

## 🗺️ Roadmap (nice-to-have)
- [ ] Add `web/assets/logos/_meta/templates/logo.meta.yaml`
- [ ] Add CI rule: reject SVG with scripts/external refs
- [ ] Add build step: generate `logos.manifest.json` for UI
- [ ] Add story-mode “Provenance badge” variants for map overlays

🧡 Keep it clean. Keep it traceable. Keep it readable on a noisy basemap.
