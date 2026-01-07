# 🎨 KFM Web Assets — `web/assets/`

[![Assets](https://img.shields.io/badge/web-assets-111827?logo=files&logoColor=white)](#-kfm-web-assets--webassets)
[![Maps](https://img.shields.io/badge/maps-MapLibre%20%7C%20Leaflet-2b9348)](#️-map-assets-styles-sprites-glyphs--ramps)
[![3D](https://img.shields.io/badge/3D-WebGL%20%7C%20Cesium%20%7C%203D%20Tiles-0b7285)](#-3d-assets-models-textures-shaders--tiles)
[![UX](https://img.shields.io/badge/ux-responsive%20images%20%7C%20mobile%20mapping%20%7C%20a11y-ff922b)](#️-images--icons-responsive-by-default)
[![Policy](https://img.shields.io/badge/policy-no%20secrets%20%7C%20licensed%20%7C%20optimized-red)](#-non-negotiables)
[![Integrity](https://img.shields.io/badge/integrity-checksums%20%7C%20hashing%20%7C%20deterministic%20builds-7048e8)](#-build--caching-rules)

> 🧭 **Purpose:** `web/assets/` is the **static, versioned, front-end-facing** asset library for Kansas Frontier Matrix (KFM).  
> It feeds the UI’s **maps, charts, and 3D views** while staying consistent with KFM’s governed boundaries: **assets are presentation**, not data authority, not policy, not secrets. 🧱🛡️  
> **Rule of thumb:** if it changes the meaning of a map or chart, treat it like evidence infrastructure (review + provenance + licensing).

---

## 🔗 Quick links

- [🧱 Non-negotiables](#-non-negotiables)
- [🧭 Canonical pipeline alignment](#-canonical-pipeline-alignment-assets-cannot-leapfrog-governance)
- [🗂️ Recommended structure](#️-recommended-structure)
- [🖼️ Images & icons](#️-images--icons-responsive-by-default)
- [🎨 Chart themes & visual integrity](#-chart-themes--visual-integrity-palettes-patterns-tokens)
- [🗺️ Map assets](#️-map-assets-styles-sprites-glyphs--ramps)
- [🧊 3D assets](#-3d-assets-models-textures-shaders--tiles)
- [🧯 Security & supply chain](#-security--supply-chain-assets-are-an-attack-surface)
- [📦 Build + caching rules](#-build--caching-rules)
- [🧾 Attribution & licensing](#-attribution--licensing-required)
- [✅ PR checklist](#-pr-checklist-assets)
- [📚 Sources & influence map](#-sources--influence-map-uses-every-project-file)

---

## 🧱 Non-negotiables

### 🔒 1) No secrets. Ever.
Assets ship to the browser. Treat everything here as **world-readable**.

✅ OK  
- images, icons, fonts (licensed), shader files, map style JSON, UI screenshots (non-sensitive)

🚫 NOT OK  
- API keys, credentials, private dataset URLs, internal endpoints, unredacted sensitive exports

> [!CAUTION]
> Map style JSON can accidentally leak secrets via embedded URLs/querystrings. Treat style JSON as **security-reviewed**.

---

### 🧼 2) Optimize by default (performance is a feature)
The UI must remain responsive on laptops **and** mobile devices.

- use responsive images (`srcset` / `sizes` / `<picture>`)
- keep large/rare assets lazy-loaded (3D, heavy textures, demo videos)
- enforce size budgets per folder (see [Build + caching rules](#-build--caching-rules))

---

### 🧭 3) Visual design choices are part of “truth”
Cartography and charts are arguments — not decoration. 🎯  
Assets (ramps, legends, icons, badges) must avoid implying certainty that doesn’t exist.

- sequential vs diverging ramps must match the semantics
- “warning” colors should mean something and not be overused
- uncertainty should have a visual grammar (bands, hatching, opacity rules)

---

### 🧩 4) Assets support clean boundaries (don’t bury logic here)
Assets are **data for rendering** (styles, textures, icons).  
They are not business rules, not governance logic, not backend contracts.

> [!TIP]
> If you’re writing conditionals or decision logic, you’re in `web/src/`, not `web/assets/`.

---

### 🧾 5) Licensing and provenance are mandatory
If we ship third-party assets:
- we must track **source + license + what changed**
- we must be able to remove/replace assets cleanly

See [Attribution & licensing](#-attribution--licensing-required).

---

## 🧭 Canonical pipeline alignment (assets cannot leapfrog governance)

KFM is governed by a strict order:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Assets (presentation)**

That means `web/assets/` must **never** become a backdoor for:
- shipping “real datasets” (that belongs in catalogs and API, not assets)
- bypassing license and provenance requirements
- “hardcoding conclusions” through misleading legends/icons

> [!IMPORTANT]
> Assets can **explain** and **visualize** governed outputs — they cannot replace governance.

---

## 🗂️ Recommended structure

> Keep this folder **boring and predictable**. If you add a new category, add it here + add license/provenance rules.

```text
🌐 web/
└── 🎨 assets/
    ├── 🖼️ images/                    # photos, screenshots, UI illustrations (optimized)
    ├── 🧩 icons/                     # SVG icons + icon sets (prefer SVG)
    ├── 🎨 charts/                    # palettes, patterns, theme tokens (no data)
    │   ├── 🎚️ palettes/              # sequential/diverging/categorical palettes (JSON)
    │   ├── 🧵 patterns/              # hatching/dots for uncertainty overlays (SVG/PNG)
    │   └── 🧱 tokens/                # design tokens (color/spacing/typography) (JSON/TS)
    ├── 🗺️ maps/
    │   ├── 🎛️ styles/                # MapLibre style JSON (+ versioned dirs)
    │   ├── 🧷 sprites/               # sprite.png + sprite.json (if used)
    │   ├── 🔤 glyphs/                # self-hosted glyphs (WOFF/PKBF or engine format)
    │   ├── 🎚️ legends/               # legend images + ramp definitions
    │   └── 🧭 patterns/              # map fill patterns (hatching, textures)
    ├── 🧊 3d/
    │   ├── 🧱 models/                # glTF/GLB preferred; OBJ only when unavoidable
    │   ├── 🧵 textures/              # compressed textures (KTX2/Basis where possible)
    │   ├── ✨ shaders/               # GLSL chunks (versioned + linted)
    │   └── 🧊 tiles/                 # 3D Tiles manifests or pointers (avoid large tiles here)
    ├── 🎞️ media/                    # short mp4/webm clips, demos (avoid huge files)
    ├── 🔤 fonts/                    # licensed fonts (WOFF2 preferred)
    ├── 🧪 samples/                  # tiny sample assets for dev/test only
    ├── 🧾 ATTRIBUTION.md            # REQUIRED: every third‑party asset tracked here
    ├── 🧾 LICENSES/                 # OPTIONAL: vendored license texts, if needed
    └── 📘 README.md                 # you are here
```

> [!NOTE]
> The UI should import assets via stable paths. If you introduce breaking moves, update `web/src/` imports + changelog notes.

---

## 🖼️ Images & icons (responsive by default)

### ✅ Preferred formats (practical defaults)
- **SVG** → icons, glyphs, simple diagrams (scales perfectly)
- **PNG** → crisp UI overlays, line art, legends needing pixel precision
- **JPEG** → photos and heavy imagery (smaller, lossy)
- **WebP/AVIF** → optional modern formats for photos (with PNG/JPEG fallback)

> [!TIP]
> If an image includes text, consider: should this be actual HTML instead? Text-in-image is rarely accessible.

### 📏 Practical rules
- keep icons tiny and local (SVG where possible)
- compress screenshots aggressively (especially if only for docs)
- strip unnecessary metadata (EXIF) where feasible
- avoid “mystery assets” — name files descriptively

**Naming convention suggestion**
- `kfm_<feature>_<role>_<variant>@2x.<ext>`  
  Example: `kfm_storynode_badge_verified@2x.png`

### ♿ Accessibility reminders
If an asset carries meaning, it needs:
- descriptive alt text (for `<img>`)
- labels for icon-only buttons
- avoid using color alone to convey state (pair with shape/text)

---

## 🎨 Chart themes & visual integrity (palettes, patterns, tokens)

Charts and maps share a core requirement: **don’t mislead**.

### ✅ What belongs in `assets/charts/`
- color palettes (JSON)
- uncertainty patterns (SVG/PNG)
- “credibility” badges (e.g., V&V status icons)
- default typography tokens (font stacks and sizes)

### 🎚️ Palette rules (maps + charts)
- use **sequential** palettes for magnitude-only metrics (e.g., NDVI level)
- use **diverging** palettes for signed deltas (e.g., anomaly vs baseline)
- use **categorical** palettes for classes (land cover types)

> [!IMPORTANT]
> If you include a palette, include:
> - name + intended use
> - accessibility notes (contrast, colorblind considerations)
> - “don’t use this for ___” warnings when appropriate

### 🧵 Uncertainty patterns (recommended)
Use patterns when opacity/color alone can be ambiguous:
- hatching for “low confidence”
- dots/noise for “insufficient coverage”
- dashed outlines for “estimated boundaries”

---

## 🗺️ Map assets (styles, sprites, glyphs, ramps)

KFM’s map UI depends on assets that are **stable** and **auditable**.

### 🎛️ Style JSON rules
Keep style JSON:
- versioned (`/styles/v1/`, `/styles/v2/`)
- stable layer IDs (layer IDs are UI state keys)
- attribution blocks accurate and visible when required

**Hard rule:** style JSON must not contain secrets or private endpoints.

### 🧷 Sprites & glyphs
If you self-host sprites/glyphs:
- include generation instructions (or a script path in repo)
- pin versions and document expected paths
- keep sprite sheets minimal and deterministic (avoid nondeterministic packing)

### 🎚️ Legends & ramps
Legend design affects interpretation.
- keep ramp definitions in machine-readable form when possible (JSON ramp spec)
- keep legend images consistent with ramp spec
- avoid “rainbow ramps” unless you can justify the semantics

---

## 🧊 3D assets (models, textures, shaders, tiles)

3D is powerful and expensive. Ship only what the UX can defend.

### ✅ Preferred formats
- models: **glTF/GLB**
- textures: **KTX2/Basis** when possible, otherwise PNG/JPEG with explicit budgets
- tiles: **3D Tiles** (store externally when large; reference/pointer here)

### ⚠️ OBJ policy
OBJ parsing is an attack surface and a performance risk.
If OBJ is used:
- keep models tiny
- validate/sanitize in a hardened pipeline
- do not load arbitrary user-provided models in-browser

### 🧭 Coordinate + unit sanity
Every 3D asset set must document:
- units (meters? feet?)
- origin (where is (0,0,0)?)
- axis orientation (right/left-handed assumptions)
- CRS relationship (if georeferenced)

### ✨ Shaders are code
Treat shaders like code assets:
- version them with the UI feature they support
- keep chunks composable and small
- lint/format if possible (or enforce a style guide)
- avoid dynamic string-concatenated shader injection patterns

---

## 🧯 Security & supply chain (assets are an attack surface)

Assets can be weaponized through:
- malicious SVG/GeoJSON-like payloads (script injection attempts)
- huge meshes/textures causing crashes
- style JSON pointing to hostile endpoints
- “harmless” third-party packs with unclear licensing

### Defensive posture ✅
- escape/sanitize any asset-derived strings before rendering as HTML
- constrain what SVGs you accept (prefer internal, audited sets)
- enforce size/complexity budgets (vertex limits, texture size limits)
- allowlist external hosts if remote assets are ever referenced
- keep CI checks for forbidden strings (keys, tokens, internal domains)

> [!IMPORTANT]
> If an asset can’t be explained, verified, and licensed — it doesn’t ship.

---

## 📦 Build + caching rules

### 🧠 Cache-friendly naming
Prefer:
- content-hashed filenames via bundler output for most images/fonts
- versioned directories for map styles and shared ramps (e.g., `maps/styles/v1/…`)

### 🧾 Asset manifest (recommended)
Add a machine-readable manifest for critical assets:
- `assets/manifest.assets.json`
- includes file path → sha256 → license ref → owner

This enables:
- integrity checks
- provenance auditing
- deterministic “what changed?” diffs

### ⚙️ Deterministic builds
Sprite packing, legend generation, and any asset build step must be deterministic:
- same inputs → same outputs
- pinned tool versions
- stable ordering

---

## 🧾 Attribution & licensing (required)

Every third-party asset must be tracked in `web/assets/ATTRIBUTION.md` with:
- source
- license
- author/owner
- what we changed (if anything)
- where it is used (optional but helpful)

**Suggested entry format:**

| Asset | Source | License | Changes | Notes |
|---|---|---|---|---|
| `icons/foo.svg` | `...` | MIT | recolored | used in Layer Toggle |
| `maps/styles/v1/base.json` | `...` | ODbL/CC? | adapted | attribution required |

> [!CAUTION]
> If the license is unclear, do not commit the asset. Use a pointer or replace it.

---

## ✅ PR checklist (assets)

- [ ] No secrets, internal URLs, tokens, or sensitive exports added
- [ ] File sizes are reasonable (and compressed)
- [ ] Responsive handling exists for large images (`srcset` / `<picture>`)
- [ ] Legends/ramps are intentional and not misleading
- [ ] 3D assets documented (units, axes, coordinate assumptions)
- [ ] Shaders reviewed like code (no unsafe patterns, minimal complexity)
- [ ] Third-party assets recorded in `ATTRIBUTION.md`
- [ ] Paths remain stable (or `web/src/` imports updated)
- [ ] If new category: README updated + license/provenance rules included

---

## 📚 Sources & influence map (uses every project file)

> This table maps **every project file** in the KFM library pack to a concrete `web/assets/` rule or expectation.

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

| Project file | How it influences `web/assets/` |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | Boundary discipline (assets ≠ data ≠ logic), governance mindset, stable IDs and auditable presentation layers |
| `Latest Ideas.docx` | “Demo-first but governed” posture, Story/3D direction, stable extension mindset, operational QA hooks for asset changes |
| `responsive-web-design-with-html5-and-css3.pdf` | Responsive images, mobile-first constraints, semantic structure + accessibility expectations |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | Mobile mapping realities, offline constraints, location sensitivity → asset size budgets + careful UX symbolism |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | Practical image format tradeoffs and why format choice is part of performance + clarity |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | Cartographic clarity, hierarchy, legend integrity, “maps persuade” → ramps/symbology treated as evidence |
| `python-geospatial-analysis-cookbook.pdf` | CRS sanity expectations + geospatial conventions that affect map styles, labels, and legends |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | Remote-sensing visualization patterns (composites, indices) → ramp specs + time-aware legends |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | WebGL coordinate mental models, canvas vs clipspace mapping, shader discipline, model loading cautions |
| `Generalized Topology Optimization for Structural Design.pdf` | Mesh realism: decimation, constraints, and parameter sensitivity → 3D asset guidelines + metadata requirements |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | Simulation credibility mindset → “V&V badges”, uncertainty patterns, and “assumptions visible” visual assets |
| `Understanding Statistics & Experimental Design.pdf` | Avoid misleading visuals; chart themes should support uncertainty, sample-size visibility, and honest comparisons |
| `graphical-data-analysis-with-r.pdf` | EDA-first visual grammar → distribution-friendly palettes, outlier-safe defaults, exploratory readability |
| `regression-analysis-with-python.pdf` | Regression diagnostics expectations → residual-plot-ready themes, avoid “trendline as truth” styling |
| `Regression analysis using Python - slides-linear-regression.pdf` | Lightweight regression UI outputs → consistent coefficient table styling + fit summary icons |
| `think-bayes-bayesian-statistics-in-python.pdf` | Credible intervals + posterior uncertainty → uncertainty bands/pattern assets and labeling conventions |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | AI output labeling → icons/badges for “AI-assisted”, provenance affordances, accountability symbolism |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | ML practicality: ship model *explanations* and visual affordances, not weights; versioned model-card visuals |
| `Introduction to Digital Humanism.pdf` | Human-centered constraints → avoid manipulative assets/dark patterns; transparency + agency visuals |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | Autonomy/feedback thinking → UI should make control loops visible; icons shouldn’t imply false control/certainty |
| `Data Spaces.pdf` | Pointer-over-payload philosophy → prefer referencing governed stores; asset manifests + provenance links |
| `Scalable Data Management for Future Hardware.pdf` | Caching/streaming mindset → hashed assets, size budgets, and performance-first media choices |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | Stable identifiers + “don’t ship DB blobs to browser” intuition; naming/versioning discipline for assets |
| `Spectral Geometry of Graphs.pdf` | Graph visualization direction → node/edge styling assets, community palettes, explainable link symbolism |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | Threat modeling posture → assets are attack surface; scanning, allowlists, and policy checks |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | Defensive paranoia → treat parsers/loaders cautiously; never trust SVG/OBJ blindly |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | Deterministic pipelines and bounded work → avoid nondeterministic sprite packing; enforce complexity limits |
| `A programming Books.pdf` | Contributor shelf: general ecosystem reference pack (helps maintainers navigate tools) |
| `B-C programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `D-E programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `F-H programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `I-L programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `M-N programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `O-R programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `S-T programming Books.pdf` | Contributor shelf: general ecosystem reference pack |
| `U-X programming Books.pdf` | Contributor shelf: general ecosystem reference pack |

</details>

---

✨ If you’re new: start by adding a tiny SVG icon, updating `ATTRIBUTION.md`, wiring it into `web/src/components/`, and keeping the diff small and auditable.