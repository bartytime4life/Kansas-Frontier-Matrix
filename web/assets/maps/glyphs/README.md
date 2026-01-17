# 🗺️ Map Glyphs (Fonts) — `web/assets/maps/glyphs/`

![MapLibre GL JS](https://img.shields.io/badge/MapLibre-GL%20JS-1f6feb)
![WebGL](https://img.shields.io/badge/WebGL-rendering-333333)
![Offline-friendly](https://img.shields.io/badge/offline--friendly-yes-2ea043)
![Provenance-first](https://img.shields.io/badge/provenance--first-yes-2ea043)

This folder is the **local “glyphs endpoint”** for our web map styles: it hosts the font glyph ranges needed for **map label rendering** (town names, roads, rivers, annotations, etc.). 🅰️✨  
Keeping glyphs in-repo makes the map viewer more **portable** (static hosting / GitHub Pages / local dev), and aligns with KFM’s ethos: **everything visible in the UI should be traceable, attributable, and reproducible**. 🔎🧾

> [!NOTE]
> In MapLibre/Mapbox-style terminology, **glyphs ≈ font glyph PBF ranges** (requested as `{fontstack}/{range}.pbf`).  
> Icons typically live in **sprites** (often `sprite.json` + `sprite.png`), not here.

---

## 🧠 Quick mental model

- **Style JSON** contains a `glyphs` URL template  
- MapLibre requests glyph ranges like:
  - `.../glyphs/{fontstack}/0-255.pbf`
  - `.../glyphs/{fontstack}/256-511.pbf`
- The `text-font` on label layers must match the **fontstack folder name(s)** in this directory.

---

## 📦 Folder layout

```text
web/
└─ 📁 assets/                         # 🖼️ Web-shipped static assets
   └─ 🗺️ maps/                        # 🗺️ Map rendering assets (styles, sprites, glyphs, tiles)
      └─ 🔤 glyphs/                   # 🔤 MapLibre glyph endpoint: {fontstack}/{range}.pbf
         ├─ 📄 README.md              # 📘 You are here: how glyphs are built/served + URL pattern + licensing
         ├─ 🔤 <Font Stack Name 1>/   # 🔤 Folder name MUST match style “text-font” / {fontstack} value
         │  ├─ 🔤📦 0-255.pbf          # 🔤 Glyph pack for Unicode codepoints 0–255
         │  ├─ 🔤📦 256-511.pbf        # 🔤 Glyph pack for Unicode codepoints 256–511
         │  ├─ 🔤📦 512-767.pbf        # 🔤 Glyph pack for Unicode codepoints 512–767
         │  └─ ➕ …                    # 🔤 Additional 256-codepoint ranges as needed
         └─ 🔤 <Font Stack Name 2>/   # 🔤 Alternate/fallback font stack (e.g., extra scripts, weight, brand)
            ├─ 🔤📦 0-255.pbf          # 🔤 Glyph pack for Unicode codepoints 0–255
            ├─ 🔤📦 256-511.pbf        # 🔤 Glyph pack for Unicode codepoints 256–511
            └─ ➕ …                    # 🔤 Additional 256-codepoint ranges as needed
```

> [!TIP]
> Keep folder names **exactly** as they appear in your style’s `text-font` values (case + spacing included).  
> A “font mismatch” is the #1 cause of missing labels.

---

## 🔗 How styles should reference glyphs

In your MapLibre style JSON (commonly `web/assets/maps/styles/*.json`), ensure there is a `glyphs` template pointing to this directory:

```json
{
  "version": 8,
  "name": "KFM Map Style",
  "glyphs": "./assets/maps/glyphs/{fontstack}/{range}.pbf",
  "sprite": "./assets/maps/sprites/kfm",
  "sources": {},
  "layers": []
}
```

And label layers should use matching `text-font` stacks:

```json
{
  "id": "place-labels",
  "type": "symbol",
  "source": "composite",
  "source-layer": "place",
  "layout": {
    "text-field": ["get", "name"],
    "text-font": ["KFM Sans Regular", "Arial Unicode MS Regular"],
    "text-size": 12
  }
}
```

---

## ✅ Conventions we follow (KFM-style rules)

### 1) 📛 Naming
- **Font stack folder name** = the name used by the style in `text-font`
- Prefer stable names (avoid version numbers in the folder name unless your style explicitly needs them)

### 2) 🧾 Provenance + licensing are not optional
Even though these are “just assets,” they still shape what users see. Treat glyph packs like any other KFM-visible artifact:

- record **source** (where the font came from)
- record **license** + attribution
- record **how it was generated** (toolchain + config)

> [!NOTE]
> KFM’s architecture is contract/provenance-first: anything shown in the UI should not be a “mystery layer.”  
> The same mindset applies to fonts/glyphs too.

### 3) 🪶 Keep glyph packs lean
Fonts can get big fast. Prefer:
- subsets (only the scripts/languages we actually need)
- the minimum number of font stacks that satisfy cartographic needs
- compression (gzip/brotli at the server layer)

---

## 🛠️ Adding or updating a font stack

> [!IMPORTANT]
> The exact build command depends on your toolchain (Node/Python/CI). The steps below are the “golden path” we recommend for this repo.

### Step-by-step
1. **Choose the font** (and verify licensing/attribution).
2. **Decide what scripts you need**
   - Latin only? Latin + extended? Special symbols?
3. **Subset if possible**
   - Smaller payload → faster label rendering → better mobile UX 📱
4. **Generate glyph PBF ranges**
   - Output into: `web/assets/maps/glyphs/<Font Stack Name>/`
5. **Smoke test**
   - Load the map and verify:
     - labels render at multiple zoom levels
     - no missing glyph boxes (□)
     - no 404 requests for glyph ranges in the network tab
6. **Commit**
   - Include a short changelog note in the PR describing:
     - font stack(s) added/updated
     - size impact (approx.)
     - license + source

---

## 🧾 Recommended “glyph asset contract” (manifest)

To align with KFM’s data-contract mindset, we recommend adding a lightweight manifest alongside glyph packs.

**Suggested file**: `web/assets/maps/glyphs/manifest.glyphs.json` (or per-font `meta.json`)

```json
{
  "id": "kfm-glyphs-default",
  "type": "map-glyphs",
  "owner": "web/maps",
  "source": {
    "name": "Font Source Name",
    "url": "https://example.com/font-source"
  },
  "license": {
    "spdx": "OFL-1.1",
    "attribution": "Required attribution text"
  },
  "fontstacks": [
    {
      "name": "KFM Sans Regular",
      "ranges": ["0-255", "256-511", "512-767"]
    }
  ],
  "build": {
    "tool": "glyph-pipeline",
    "version": "x.y.z",
    "notes": "subset: Latin + Latin-1 Supplement"
  }
}
```

> [!TIP]
> This “asset contract” can be used later to auto-generate attribution in UI footers, map credits, or story-node references—exactly the way KFM treats datasets.

---

## ⚡ Performance notes (labels should feel instant)

| Goal 🎯 | Recommendation ✅ | Why it matters |
|---|---|---|
| Fast first paint | subset fonts, fewer stacks | reduces initial glyph downloads |
| Smooth pan/zoom | cache aggressively, use CDN for static assets | reduces network jitter |
| Mobile friendly | keep total glyph payload small | mobile radios + memory constraints |
| Predictable builds | deterministic generation + manifest | avoids “it works on my machine” |

---

## ♿ Accessibility & cartographic UX

Label glyphs are part of accessibility:
- Prefer clear, readable type at small sizes
- Avoid overly thin weights for baseline labels
- Keep symbology consistent across layers (fonts contribute to perceived consistency) 🧭

> [!NOTE]
> Our web UI emphasizes legends, layer toggles, and time navigation; labels must remain readable as the user scrubs time and toggles layers.

---

## 🧯 Troubleshooting

| Symptom 🐛 | Likely cause | Fix 🔧 |
|---|---|---|
| Labels don’t render, network shows 404s | `glyphs` URL wrong OR fontstack mismatch | confirm `glyphs` template + folder names |
| Some labels render as “□” | missing characters in subset | regenerate with broader unicode coverage |
| Only one language renders correctly | subset too aggressive | include needed scripts/ranges |
| Labels look “off” vs expected | wrong font stack order | ensure `text-font` array order is correct |

---

## 🧩 Related folders (usually edited together)

- `🧩 web/assets/maps/styles/` — Style JSON(s) that reference `glyphs`
- `🖼️ web/assets/maps/sprites/` — Icon sprites (separate from glyphs)
- `🎨 web/styles/` — UI styling (layout + responsive rules)
- `🧾 data/catalog/` — Dataset catalog + provenance (design philosophy alignment)

---

## 📚 Project reference shelf (the “why” behind our conventions)

<details>
  <summary><strong>Click to expand 📖</strong></summary>

### 🗺️ Cartography, GIS & Mapping UX
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 🌐 Web mapping & 3D rendering
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`

### 📱 Responsive web design & typography
- `responsive-web-design-with-html5-and-css3.pdf`

### 🗄️ Data systems, scaling & performance
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

### 📊 Statistics, modeling & analytics (for future “analytic glyph overlays”)
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `graphical-data-analysis-with-r.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`

### 🧠 Theory & ethics context (project-wide)
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

### 🔐 Security mindset (supply chain + hardening)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🖼️ File formats & compression literacy
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🧰 Engineering library bundles
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

### 🧾 Core platform docs
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`

</details>

---

## ✅ Contribution checklist (PR-ready)

- [ ] Folder name matches `text-font` exactly 🔤  
- [ ] Glyph ranges included for required scripts (no □) ✅  
- [ ] License + attribution recorded 🧾  
- [ ] Size impact noted (rough estimate is fine) 📦  
- [ ] Map smoke test completed (no 404 glyph requests) 🔍  

---

_If you’re looking for icons, head to sprites 🖼️. If you’re looking for labels, you’re in the right place._ ✨
