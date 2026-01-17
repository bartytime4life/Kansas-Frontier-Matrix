# 🗺️ KFM Map Styles (MapLibre / Mapbox Style Spec v8)

![Style Spec](https://img.shields.io/badge/style%20spec-v8-blue)
![Folder](https://img.shields.io/badge/path-web%2Fassets%2Fmaps%2Fstyles-orange)
![Principles](https://img.shields.io/badge/design-provenance%20%E2%9C%93%20timeline%20%E2%9C%93%20accessible%20%E2%9C%93-brightgreen)

This folder contains **map style artifacts** used by the KFM web map UI:
- 🎨 **Style JSON** (MapLibre/Mapbox Style Spec v8)
- 🧩 **Sprites** (icons + `sprite.json`)
- 🔤 **Glyphs / fonts** (PBF stacks) and any font assets we ship
- 🧵 **Patterns** / textures (if used for accessibility or uncertainty)

> [!IMPORTANT]
> Treat a style file like a **contract**. The UI, legends, timeline slider, and Story Nodes often expect specific IDs and metadata conventions.

---

## 🧭 Contents

- [What belongs here](#-what-belongs-here)
- [Core style philosophy](#-core-style-philosophy)
- [Folder layout](#-folder-layout)
- [MapLibre style anatomy](#-maplibre-style-anatomy)
- [KFM metadata conventions](#-kfm-metadata-conventions)
- [Layer naming + ordering](#-layer-naming--ordering)
- [Legend + UI integration](#-legend--ui-integration)
- [Temporal layers (timeline-ready)](#-temporal-layers-timeline-ready)
- [Performance rules](#-performance-rules)
- [Accessibility rules](#-accessibility-rules)
- [Security rules](#-security-rules)
- [How to add or modify a style](#-how-to-add-or-modify-a-style)
- [Style review checklist](#-style-review-checklist)
- [Appendix: Example “KFM-ready” style snippet](#-appendix-example-kfm-ready-style-snippet)
- [Appendix: Project reference shelf](#-appendix-project-reference-shelf)

---

## ✅ What belongs here

### ✅ Yes
- `*.style.json` or `*.json` that is **directly loadable** by MapLibre.
- sprites: `sprite.png`, `sprite@2x.png`, `sprite.json`
- glyphs: `{fontstack}/{range}.pbf`
- any **local** assets referenced by `sprite` / `glyphs` URLs inside the style file

### 🚫 No
- raw datasets, ETL outputs, or “mystery” files
- ad-hoc copies of sources that already exist in canonical data/catalog locations
- hard-coded “private” endpoints or secrets (tokens, keys, internal URLs)

---

## 🧠 Core style philosophy

KFM maps are persuasive artifacts. Our default stance:

- 🧾 **Provenance-first:** every visible layer should be able to explain what it is, where it came from, and how reliable it is.
- 🕰️ **Timeline-ready:** temporal layers should be style-able and filter-able by a global time control.
- 📱 **Mobile-first:** style decisions must work on small screens and touch input.
- ♿ **Accessible by default:** color-only encoding is not enough.
- ⚡ **Performance-aware:** styles can DOS the renderer as easily as code can.

> [!TIP]
> “Pretty” is optional. **Legible, honest, fast** is mandatory.

---

## 🗂️ Folder layout

The repo may evolve, but the intent stays constant. Recommended structure:

```text
web/
└─ 📁 assets/
   └─ 🗺️ maps/
      └─ 🎨 styles/
         ├─ 📄 README.md                 # 👈 you are here 📌 How map styles are organized, composed, and referenced
         ├─ 🧱 basemaps/                 # 🧱 Full base styles (background, land/water, core labels)
         │  ├─ 🌞🎨🧾 kfm-light.style.json # Light default basemap style
         │  └─ 🌙🎨🧾 kfm-dark.style.json  # Dark default basemap style
         ├─ 🧩 overlays/                 # 🧩 Style add-ons for thematic layers (boundaries, transport, etc.)
         │  ├─ 🧩🎨🧾 kfm-boundaries.style.json # Boundary lines/polygons styling bundle
         │  └─ 🧩🎨🧾 kfm-transport.style.json  # Roads/rails/transit styling bundle
         ├─ 🧃 sprites/                  # 🧃 Sprite assets referenced by styles (icons, shields, markers)
         │  └─ 🧷 kfm/
         │     ├─ 🖼️🧷 sprite.png        # Sprite sheet @1x
         │     ├─ 🖼️✨🧷 sprite@2x.png    # Sprite sheet @2x (retina)
         │     └─ 🧾🧷 sprite.json        # Sprite index (name → x/y/w/h)
         ├─ 🔤 glyphs/                   # 🔤 Glyph endpoint for label rendering: {fontstack}/{range}.pbf
         │  └─ 🔤 {fontstack}/
         │     └─ 🔤📦 {range}.pbf        # 256-codepoint glyph pack (e.g., 0-255, 256-511…)
         └─ 🧵 patterns/                 # 🧵 Raster pattern fills (a11y/print overlays; optional)
            ├─ 🧵🖼️ diagonal-hatch.png    # Diagonal hatch fill pattern
            └─ 🧵🖼️ dots.png              # Dot fill pattern
```

> [!NOTE]
> If your actual directory differs, keep the **concepts** consistent and update this README.

---

## 🧩 MapLibre style anatomy

A style JSON is a *rendering recipe*. At minimum it includes:

- `"version": 8`
- `"name"` (human-friendly)
- `"sources"` (vector tiles, raster tiles, geojson, raster-dem, etc.)
- `"glyphs"` (URL template)
- `"sprite"` (URL base)
- `"layers"` (ordered list)

Common gotchas:
- `sprite` path is **base URL without extension** (MapLibre adds `.png`/`.json`)
- `glyphs` is a **templated URL**: `.../{fontstack}/{range}.pbf`
- layer order matters (later layers draw on top)

---

## 🏷️ KFM metadata conventions

MapLibre allows freeform `metadata` at the style-level and layer-level. We use this to make styles “UI-aware” without hardcoding behavior in React.

### 🎯 Style-level metadata (recommended)

Use `metadata` to declare:
- a stable style ID
- the theme (light/dark/print)
- semantic version
- default UI affordances (legend/timeline defaults)

Example (top-level):

```json
{
  "version": 8,
  "name": "KFM Light",
  "metadata": {
    "kfm:style_id": "urn:kfm:style:basemap:light",
    "kfm:style_version": "1.0.0",
    "kfm:theme": "light",
    "kfm:ui_defaults": {
      "showLegend": true,
      "showScaleBar": true
    }
  }
}
```

### 🧷 Layer-level metadata (recommended)

Each user-facing layer should declare:
- **what it represents**
- **how the UI should label it**
- **where the evidence lives** (dataset/catalog IDs)
- **how to build a legend**
- **time behavior** (if temporal)

Example (per-layer):

```json
{
  "id": "kfm.boundaries.county.fill",
  "type": "fill",
  "source": "kfm-boundaries",
  "source-layer": "county",
  "metadata": {
    "kfm:title": "County boundaries",
    "kfm:domain": "boundaries",
    "kfm:interactive": true,
    "kfm:dataset_ref": "urn:kfm:dcat:dataset:county-boundaries:v1",
    "kfm:legend": {
      "kind": "categorical",
      "items": [
        { "label": "County", "swatch": "#000000" }
      ]
    }
  },
  "paint": {
    "fill-color": "rgba(0,0,0,0)",
    "fill-outline-color": "rgba(0,0,0,0.35)"
  }
}
```

> [!IMPORTANT]
> `kfm:dataset_ref` should point to *cataloged evidence* (STAC/DCAT/PROV-backed) — not a random URL.

---

## 🧱 Layer naming & ordering

### IDs must be stable

Use dot-separated, human-readable IDs:

`kfm.<domain>.<entity>.<geometry>.<role>`

Examples:
- `kfm.transport.rail.line.base`
- `kfm.hydro.river.line.label`
- `kfm.landuse.cover.fill`
- `kfm.story.focus.highlight`

### Ordering conventions (suggested)

1. **Background** (water/land)
2. **Terrain / hillshade**
3. **Large polygons** (landuse, admin fills)
4. **Lines** (rivers, roads)
5. **Points** (sites, markers)
6. **Labels** (most important last)
7. **Interaction layers** (hover/selection outlines on top)

> [!TIP]
> Prefer multiple small layers (fill + outline + label) over one mega-layer with complex expressions.

---

## 🧭 Legend + UI integration

A style is “UI-friendly” when the UI can auto-generate:
- a legend
- toggles
- a layer list grouped by domain
- hover/click behavior
- attribution

Recommended conventions:
- `kfm:title` → what the UI shows in the layer panel
- `kfm:domain` → grouping category
- `kfm:legend` → legend generator payload
- `kfm:interactive` → include in hit-testing / feature inspection
- `kfm:attribution` → layer-level override if needed

> [!NOTE]
> Sources also support `attribution`. Use it for legal requirements, but keep UI-friendly text in `kfm:*` metadata too.

---

## 🕰️ Temporal layers (timeline-ready)

If a layer represents *change over time* (events, periods, evolving boundaries, time-series rasters), add time metadata so the UI can filter it.

### Required fields (recommended)

```json
"kfm:time": {
  "property": "year",
  "type": "number",
  "inclusive": true
}
```

### Recommended patterns

**Pattern A — filter by a numeric year**
- feature property: `year: 1871`
- UI sets layer filter like: `["<=", ["get","year"], selectedYear]`

**Pattern B — filter by start/end**
- feature properties: `start_year`, `end_year`
- UI sets filter like:
  - `start_year <= t AND (end_year is null OR end_year >= t)`

**Pattern C — ISO dates**
- feature property: `date: "1871-03-12"`
- UI parses and applies date range filtering

> [!IMPORTANT]
> If your time logic requires custom behavior, encode it in `kfm:time` (contract) and implement a single shared UI interpreter — don’t hand-roll ad-hoc filters in random components.

---

## ⚡ Performance rules

Map rendering performance is affected by:
- number of layers
- complexity of expressions
- label density
- expensive geometry at low zoom
- sprite size, font size, and glyph requests

**Rules of thumb**
- use `minzoom` / `maxzoom` aggressively
- simplify geometry in tiles for small zooms
- avoid heavy `match`/`case` chains in labels if you can preprocess attributes
- cap label collisions by zoom scaling and sensible `text-allow-overlap`
- prefer vector tiles over massive GeoJSON whenever possible

> [!TIP]
> When in doubt, inspect GPU/CPU usage in browser devtools and reduce layer complexity before blaming “MapLibre.”

---

## ♿ Accessibility rules

### Don’t rely on color alone
- use outlines, patterns, or icon shapes for category differences
- for uncertainty: consider hatch patterns + tooltip text, not just low opacity

### Contrast & readability
- labels must remain readable on both light/dark basemaps
- avoid “thin gray on satellite” label schemes

### Motion & interaction
- keep animated paint properties minimal
- don’t use flashing indicators for urgency; use shape + text + legend

> [!NOTE]
> Accessible maps are not just a UI concern — they start in the style file.

---

## 🔐 Security rules

Style JSON is “data,” but it can still create security and privacy problems.

- do **not** embed tokens, API keys, or internal-only URLs
- prefer allowlisted endpoints for `sources`, `sprite`, `glyphs`
- validate style JSON before shipping (schema + policy lint)
- be careful with external attributions/HTML: avoid unsanitized injection

> [!WARNING]
> A malicious style can exfiltrate user IPs via remote asset URLs (sprites/glyphs/tiles). Treat remote URLs as a security boundary.

---

## 🛠️ How to add or modify a style

### 1) Choose your base
- start from the closest existing style (light/dark) to preserve conventions

### 2) Define stable metadata
- set `kfm:style_id`, `kfm:style_version`, and `kfm:theme`
- if you’re adding a new “product style,” give it a durable URN-like ID

### 3) Add / update sources
- keep sources named by domain (`kfm-roads`, `kfm-hydro`, etc.)
- include `attribution` when required
- avoid duplication: one source should map to one canonical tileset/data product

### 4) Add layers with predictable IDs
- keep a consistent prefix and ordering
- add `kfm:*` metadata for the UI

### 5) Preview
- load the style in the local map UI and verify:
  - layering order
  - label collisions
  - legend correctness
  - timeline behavior (if applicable)

### 6) Validate + commit
- run whatever validators the repo provides (style-spec validation + lint)
- commit with a clear message: `maps(styles): …`

---

## ✅ Style review checklist

Use this checklist for PRs touching styles:

- [ ] Style loads with no errors in MapLibre
- [ ] `version` is `8` and style JSON is valid
- [ ] `sprite` and `glyphs` references resolve in the target environment
- [ ] Every user-facing layer has:
  - [ ] stable `id` naming
  - [ ] `kfm:title`
  - [ ] `kfm:domain`
  - [ ] `kfm:dataset_ref` (or a documented reason it’s missing)
  - [ ] `kfm:legend` (or a documented reason it’s missing)
- [ ] Temporal layers have `kfm:time` and behave correctly with timeline controls
- [ ] Mobile readability check (small screen + touch)
- [ ] Colorblind/accessibility check (color not the only encoder)
- [ ] Performance sanity check (layer count, label density, minzoom/maxzoom)
- [ ] No secrets / internal endpoints / non-allowlisted remote assets

---

## 📎 Appendix: Example “KFM-ready” style snippet

```json
{
  "version": 8,
  "name": "KFM Light (Example)",
  "metadata": {
    "kfm:style_id": "urn:kfm:style:example:light",
    "kfm:style_version": "0.1.0",
    "kfm:theme": "light"
  },
  "glyphs": "/assets/maps/styles/glyphs/{fontstack}/{range}.pbf",
  "sprite": "/assets/maps/styles/sprites/kfm/sprite",
  "sources": {
    "kfm-boundaries": {
      "type": "vector",
      "tiles": [
        "/tiles/boundaries/{z}/{x}/{y}.pbf"
      ],
      "attribution": "Boundary data: see dataset metadata"
    }
  },
  "layers": [
    {
      "id": "kfm.boundaries.county.outline",
      "type": "line",
      "source": "kfm-boundaries",
      "source-layer": "county",
      "metadata": {
        "kfm:title": "County boundaries",
        "kfm:domain": "boundaries",
        "kfm:interactive": true,
        "kfm:dataset_ref": "urn:kfm:dcat:dataset:county-boundaries:v1",
        "kfm:legend": {
          "kind": "simple",
          "items": [{ "label": "County", "line": { "width": 1 } }]
        }
      },
      "paint": {
        "line-color": "rgba(0,0,0,0.35)",
        "line-width": 1
      }
    }
  ]
}
```

---

## 📚 Appendix: Project reference shelf

This style system is intentionally informed by **the broader KFM library** (design, GIS, performance, ethics, statistics). Use these as “why” documents when style debates happen.

<details>
<summary><strong>📖 Click to expand the shelf</strong></summary>

### 🗺️ Cartography & GIS visualization
- **Making Maps: A Visual Guide to Map Design for GIS** → hierarchy, labeling, legibility, visual variables  
- **Mobile Mapping: Space, Cartography and the Digital** → mobile constraints, trust/authority of maps  
- **Archaeological 3D GIS** → 3D + web GIS visualization patterns

### 🌍 Web map rendering & UI
- **WebGL Programming Guide** → rendering constraints, GPU mindset  
- **Responsive Web Design with HTML5 and CSS3** → typography + layout fundamentals across devices  
- **Programming Books (A–X bundles)** → reference material for CSS/JS/UI patterns

### 🛰️ Remote sensing & scientific layers
- **Cloud-Based Remote Sensing with Google Earth Engine** → styling data by properties, palettes, legends  
- **Scientific Modeling and Simulation (NASA-grade)** → reproducibility mindset for simulation-driven layers

### 📈 Stats, uncertainty, and “don’t lie with maps”
- **Understanding Statistics & Experimental Design** → communicate uncertainty + comparisons responsibly  
- **Regression Analysis with Python** (+ slides) → choropleths based on model outputs, residual maps  
- **Think Bayes** → credible intervals, uncertainty-first visual encodings  
- **Graphical Data Analysis with R** → exploratory analysis for choosing classifications & bins

### 🗄️ Data & performance foundations
- **Database Performance at Scale** → latency budget thinking, caching, bottlenecks  
- **Scalable Data Management for Future Hardware** → “one fact, one place” + scalable conventions  
- **PostgreSQL Notes for Professionals** → PostGIS-friendly attribute conventions + indexing awareness  
- **Data Spaces** → trust/value framing and metadata-as-product thinking

### 🧭 Governance, ethics, and safety
- **Introduction to Digital Humanism** → human-centered, transparent systems  
- **On the path to AI Law’s prophecies…** → labeling, responsibility, and governance for ML/AI layers  
- **Ethical Hacking & Countermeasures / Gray Hat Python** → threat modeling for asset URLs and pipelines

### 🧠 Optional “systems thinking” inspiration
- **Principles of Biological Autonomy** → feedback loops + boundaries (useful for thinking about UI + provenance)

</details>

---

🧩 **If you’re adding a new layer:** start by asking “What does the user need to *understand*?”  
Then style it so the layer is **readable, honest, and traceable**.
