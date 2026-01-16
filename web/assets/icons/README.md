# Icons 🧩🗺️  
<kbd>SVG‑first</kbd> <kbd>A11y</kbd> <kbd>Provenance‑friendly</kbd> <kbd>Secure</kbd> <kbd>Fast</kbd> <kbd>Themeable</kbd>

This folder is the **single source of truth** for the Kansas Frontier Matrix web UI iconography.  
Icons here should stay **consistent**, **accessible**, **lightweight**, and **governance-aware** (KFM is evidence-first and provenance-linked by design).

---

## TL;DR ✅ (read this before adding anything)

- **Prefer `SVG`** for nearly everything (scales cleanly, smallest for simple shapes).
- Use **`currentColor`** so icons auto-theme (light/dark, map overlay palettes, etc.).
- Keep file names **kebab-case** and **stable** (don’t bake size/color into the name).
- **Optimize** every SVG (SVGO or equivalent) and keep paths clean.
- **No scripts** or external references inside SVGs.
- Icons that imply truth/status (✅ verified / ⚠️ uncertain / 🤖 AI-suggested) must be **unambiguous** and **consistent** across the app.

---

## What belongs in `web/assets/icons/` 📦

### ✅ Good fits
- UI controls (zoom, layers, search, filters, timeline)
- Data type indicators (vector/raster/3D, document/media)
- Governance & provenance indicators (citations, source-linked, restricted)
- Status indicators (verified, disputed, estimated, incomplete)
- Domain symbols (remote sensing, archaeology, simulation, graph/network)

### ❌ Not good fits
- Large illustrations, hero art, or full-color scenes  
- Logos that must keep complex gradients (use a dedicated `logos/` bucket or raster)
- One-off icons that aren’t reused (push back into the feature component if truly unique)

---

## Recommended folder structure 🗂️✨

> If folders don’t exist yet, create them as needed — but keep the taxonomy tight.

```text
web/
└─ 📁 assets/
   └─ 🧷 icons/
      ├─ 📄 README.md
      ├─ 🧭 ui/            # general interface icons
      ├─ 🗺️ map/           # map controls + cartographic UI
      ├─ 🗂️ data/          # data types, formats, catalogs, provenance
      ├─ 🚦 status/        # verification, warning, error, uncertainty, AI
      ├─ 🧭 domain/        # archaeology, remote sensing, simulation, graphs, etc.
      ├─ 🏷️ brand/         # strictly controlled brand marks (prefer SVG, allow PNG)
      └─ 🤖 _generated/    # build artifacts (sprite sheets, manifests) — do not hand-edit
```

---

## File format rules 🧾

### SVG (preferred) 🥇
**Use when:** simple to medium complexity, UI icons, any icon that must scale.  
**Rules:**
- Must include a correct **`viewBox`**
- Prefer **`stroke="currentColor"`** / **`fill="currentColor"`** (or `none`)
- Avoid hard-coded colors unless the icon is *semantically colored* (rare; document it)
- Keep shapes aligned to a grid (see “Design spec”)

### PNG (fallback) 🧩
**Use when:** brand marks, pixel-perfect raster details, or complex multi-tone art.  
**Rules:**
- Provide `@1x` + `@2x` when used at fixed sizes
- Use transparency when needed
- Keep filesize small; don’t use PNG for what could be a 1–2KB SVG

### Avoid (generally) 🚫
- JPEG for icons (lossy edges)
- GIF for “icons” (only consider for legacy animation needs — prefer CSS/SVG animation)

---

## Naming conventions 🏷️

### File naming
- **kebab-case**
- **no sizes** in file names
- **no colors** in file names
- prefix with category when ambiguity exists

**Examples**
- `ui/search.svg`
- `map/layers.svg`
- `status/verified.svg`
- `status/ai-suggested.svg`
- `data/stac.svg`
- `domain/remote-sensing-satellite.svg`

### Variants
If an icon needs variants, encode *intent*, not presentation:
- ✅ `status/verified.svg` vs `status/unverified.svg`
- ✅ `ui/panel-open.svg` vs `ui/panel-closed.svg`
- 🚫 `search-24px.svg`, `search-blue.svg`

---

## Design spec 🎛️

### Grid & geometry
- Design on a **24×24** grid (default), aligned to whole pixels when possible.
- Standard stroke widths: **1.5–2px** (choose one for the pack; be consistent).
- Use rounded caps/joins if the pack uses them (don’t mix styles).

### “Feels like KFM”
KFM is map-first and evidence-first. Icons should:
- Be **legible at small sizes** (16–20px) for dense map UI
- Avoid “cute” ambiguity (especially for provenance/status)
- Prefer **universal metaphors** over culture-specific ones when possible
- Play nicely on **busy basemaps** (simple silhouette, strong negative space)

---

## Accessibility rules ♿

Icons are UI, and UI must be accessible.

### Decorative icons
If the icon is purely decorative:
- mark it as **hidden from assistive tech** (`aria-hidden="true"`)
- don’t add redundant text

### Meaningful icons
If the icon conveys meaning:
- provide a **text label** (visible or screen-reader-only)
- or provide an **ARIA label** / `<title>` inside SVG when used as `role="img"`

Also:
- ensure touch targets are **large enough** (icon can be 20px, target should be larger)
- don’t rely on color alone (use shape + label for statuses)

---

## Security rules 🛡️

SVG is **code-like**. Treat it that way.

- **Never** accept untrusted SVGs directly from users into this folder.
- Strip:
  - `<script>` tags
  - external references (remote images/fonts)
  - event handlers (`onload=`, etc.)
- Keep a strict Content Security Policy in the app (especially if inlining SVGs).
- Prefer a **known-safe optimization pipeline** (SVGO + review).

---

## Performance rules ⚡

- Prefer **one icon = one file** for clarity, but consider a **sprite** at build time.
- Keep SVG paths minimal:
  - remove editor cruft
  - merge shapes when safe
  - avoid huge coordinate precision
- Cache aggressively in production (icons should be immutable + hashed by build).

---

## Adding a new icon 🧰 (workflow)

### 1) Pick the right home
- UI control? → `ui/`
- Map interaction? → `map/`
- Data/provenance? → `data/`
- Status/governance? → `status/`
- Domain concept? → `domain/`

### 2) Export rules
- `viewBox` set correctly
- no embedded bitmap unless explicitly required
- set fills/strokes to `currentColor` where possible

### 3) Optimize (required)
Example (SVGO):
```bash
# from repo root (example)
npx svgo web/assets/icons --recursive
```

### 4) Quick QA checklist ✅
- [ ] Looks correct at 16px, 20px, 24px
- [ ] Works on light + dark backgrounds
- [ ] No hard-coded colors unless intentionally semantic
- [ ] No scripts / external refs
- [ ] Has an accessible label when used meaningfully
- [ ] Naming follows conventions

---

## Using icons (patterns) 🧩

### Inline SVG (themeable, styleable)
Best for icons that need CSS control.

```html
<!-- Decorative -->
<svg aria-hidden="true" focusable="false" class="Icon">
  <use href="#icon-search"></use>
</svg>

<!-- Meaningful -->
<svg role="img" aria-label="Search" class="Icon">
  <title>Search</title>
  <use href="#icon-search"></use>
</svg>
```

### `<img>` tag (simple, less controllable)
Best for brand marks or when you don’t need CSS styling of paths.

```html
<img src="/assets/icons/ui/search.svg" alt="" aria-hidden="true" />
```

---

## Governance-aware iconography 🧭🔍

Some icons affect user trust. Treat them as **policy UI**:

### Provenance & citations
- Provide clear icons for “has citations”, “source-linked”, and “no sources”.
- Don’t let “citation present” look like “verified”.

### AI / analysis outputs
- “AI suggested” must be **visually distinct** from “verified”.
- Always pair with text/tooltips when stakes are high.

### Classification & sensitivity
- Provide consistent icons for:
  - Public
  - Restricted
  - Sensitive / redacted
- Never allow a “public-looking” icon to label restricted content.

---

## Domain icon packs 🧠🌎

KFM spans multiple disciplines. Keep domain icons consistent, but distinct from UI icons.

| Pack | Examples | Notes |
|------|----------|------|
| 📊 analysis | regression, bayes, histogram | used in dashboards + evidence panels |
| 🛰️ remote-sensing | satellite, cloud, raster tiles | used for Earth Engine / imagery layers |
| 🧱 archaeology | excavation, 3D artifact, trench | used for archaeological GIS modules |
| 🧬 systems | autonomy, agent, feedback loop | used for modeling concepts + narratives |
| 🕸️ graphs | node, edge, spectral | used for knowledge graph + network views |
| 🧮 simulation | model, run, validate | used for scenario layers + reproducibility |
| 🗄️ data-platform | database, ingest, API | used for pipeline transparency |

---

## Wishlist / backlog ideas 🧾✨

If you’re adding a new module, consider whether we need icons for:

- `status/uncertain.svg`
- `status/disputed.svg`
- `status/ai-suggested.svg`
- `data/provenance-linked.svg`
- `data/license.svg`
- `data/stac.svg`, `data/dcat.svg`, `data/prov.svg`
- `domain/archaeology-3d.svg`
- `domain/remote-sensing-satellite.svg`
- `domain/graph-network.svg`
- `domain/simulation-model.svg`

---

<details>
<summary>📚 Reference shelf (project PDFs that inform icon constraints & semantics)</summary>

These are part of the project’s “shared brain” — icon packs and UI semantics should align with the same domain language:

- Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- Understanding Statistics & Experimental Design.pdf
- regression-analysis-with-python.pdf
- Regression analysis using Python - slides-linear-regression.pdf
- think-bayes-bayesian-statistics-in-python.pdf
- graphical-data-analysis-with-r.pdf
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf
- python-geospatial-analysis-cookbook.pdf
- PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf
- Data Spaces.pdf
- Scalable Data Management for Future Hardware.pdf
- Database Performance at Scale.pdf
- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
- Spectral Geometry of Graphs.pdf
- Generalized Topology Optimization for Structural Design.pdf
- Archaeological 3D GIS_26_01_12_17_53_09.pdf
- making-maps-a-visual-guide-to-map-design-for-gis.pdf
- Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf
- compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf
- Principles of Biological Autonomy - book_9780262381833.pdf
- Introduction to Digital Humanism.pdf
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf
- Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf
- ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf
- concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf
- A programming Books.pdf
- B-C programming Books.pdf
- D-E programming Books.pdf
- F-H programming Books.pdf
- I-L programming Books.pdf
- M-N programming Books.pdf
- O-R programming Books.pdf
- S-T programming Books.pdf
- U-X programming Books.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf

</details>

---

## Maintainer note 🧑‍🔧
If you change conventions (grid, stroke, naming, sprite strategy), update this README in the same PR so contributors don’t drift.
