<!--
📁 Path: web/assets/icons/_generated/README.md
⚠️ This folder is build output. Treat everything here as ephemeral.
-->

# 🧩 KFM Icons — `_generated/` Output

![status](https://img.shields.io/badge/status-auto--generated-blue)
![format](https://img.shields.io/badge/format-SVG%20%7C%20PNG%20%7C%20WebP-informational)
![a11y](https://img.shields.io/badge/accessibility-aria%20%2B%20contrast-success)
![provenance](https://img.shields.io/badge/provenance-first%20%F0%9F%94%8D%20traceable-important)

This directory contains **generated icon artifacts** for the Kansas Frontier Matrix (KFM) web UI.  
**Do not hand-edit files in `_generated/`**—regenerate them from source instead ✅

---

## 🗺️ Why this matters in KFM

KFM is built around **provenance-first, auditable outputs**—nothing is a black box. That principle applies to UI assets too: icon origin, license, and generation settings should be trackable just like datasets and layers.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📦 Folder contract

This folder should contain (exact filenames may vary by implementation, but **the concepts are stable**):

- `README.md` ✅ (this file)
- `manifest.json` 🧾  
  - Icon registry: IDs, filenames, sizes, hashes, license metadata, source path(s)
- `sprite.svg` 🧵 *(optional but recommended)*  
  - SVG sprite sheet for minimizing requests + improving cache behavior
- `index.ts` / `icons.ts` 🧠 *(optional but recommended)*  
  - Type-safe icon exports for the web client
- `*.svg` 🧩 *(optional)* individual normalized SVGs
- `*.png` / `*.webp` 🖼️ *(optional)* rasterized sizes for markers/legacy contexts

> **Rule of thumb:** if an icon is referenced anywhere in the app, it should be resolvable via the **generated manifest/registry**, not ad-hoc imports.

---

## 🧱 Recommended project layout

```text
web/ 🌐
└─ assets/
   └─ icons/
      ├─ _source/ 🎨             # human-edited SVG sources (single source of truth)
      ├─ _generated/ 🤖          # build output (this folder)
      │  ├─ README.md
      │  ├─ manifest.json
      │  ├─ sprite.svg
      │  └─ ...
      └─ _licenses/ 📜           # optional: third-party license files & attributions
```

---

## 🧬 “Icons as stable identifiers” (don’t break the UI)

KFM favors **stability over cleverness**. Apply the same thinking to icons:

- ✅ **Stable icon IDs** over “meaningful-but-brittle” names  
- ✅ IDs should be **unique, invariant**, and ideally “information-light”
- ✅ Rename UI labels freely — **do not rename icon IDs casually**

This aligns with flexible-system thinking: **stable identifiers + consistent standards** make long-lived systems easier to evolve.  [oai_citation:1‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)

**Naming rules (recommended):**
- `kebab-case` filenames: `layer-historical-map.svg`
- Prefix categories when helpful:  
  - `ui-` (buttons, chrome), `map-` (symbology), `data-` (datasets), `model-` (analytics), `auth-` (security)
- Avoid spaces, uppercase, and “vague” names like `icon1.svg`

---

## 🎨 Visual style rules (practical + strict)

### SVG geometry
- Use a consistent grid: `24×24` (or `20×20`) with a correct `viewBox`.
- Align strokes to the pixel grid (prevents blur at small sizes).
- Keep shapes simple; icons must read at `16px` and `20px`.

### Color
- Default icons should use `currentColor` (themeable).
- Only bake colors into icons when the color is semantic (e.g., warnings) and approved by design tokens.

### Map icons ≠ UI icons
Cartographic symbols often need stronger constraints for legibility in spatial contexts (zoom, basemap contrast, scale). Treat map symbology like “mini cartography”:
- prioritize silhouette clarity
- test on multiple basemaps (light/dark/satellite)
- ensure “category distance” (icons shouldn’t look too similar)

(These ideas are reinforced by GIS/cartography UX practice and mobile mapping constraints.)  
**Related project references:** *Making Maps* + *Mobile Mapping* (see library below).

---

## ♿ Accessibility (a11y) contract

Icons must not become “mystery meat UI”.

**When decorative:**
- `aria-hidden="true"`
- ensure the button/control still has an accessible name (`aria-label`, visible text, etc.)

**When meaningful:**
- provide a textual label (visible or screen-reader only)
- avoid meaning via color alone
- ensure minimum contrast for icon strokes/fills

---

## ⚡ Performance notes (icons are “hot path” assets)

Icons are tiny but loaded **everywhere**, so treat them like performance-critical resources:

- Prefer **one sprite + a manifest** over dozens of network requests.
- Cache aggressively with fingerprinted filenames/hashes.
- Keep payloads minimal (optimize SVG, strip metadata not needed at runtime).

Thinking in terms of *workload mix* and *item size* (even for small assets) matches the same discipline used for scaling data systems.  [oai_citation:2‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)

---

## 🔒 Security notes (SVG is code)

SVG can embed scripts/external refs. Treat untrusted SVGs like untrusted code:

- sanitize/normalize SVGs in the generator
- strip `<script>`, external references, unknown tags/attributes
- block remote URL loads inside SVGs

Security hygiene matters even for “just icons” (front-end supply chain risk).  
*(See security-focused references in the project library list.)*

---

## 🛠️ Generation pipeline (recommended “compiler mindset”)

Think of the icon generator like a tiny compiler:

1) parse inputs (raw SVG)  
2) normalize (grid, viewBox, IDs, colors)  
3) optimize (SVGO-like passes)  
4) emit outputs (sprite, raster variants, registry/types)

This “phases” approach mirrors proven build pipelines in language tooling.  [oai_citation:3‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)

```mermaid
flowchart LR
  A[🎨 _source/*.svg] --> B[🧼 sanitize + normalize]
  B --> C[🪄 optimize paths + metadata]
  C --> D[🧵 sprite.svg]
  C --> E[🧾 manifest.json]
  C --> F[🧠 typed exports]
  C --> G[🖼️ rasterize PNG/WebP (optional)]
  D --> H[🤖 _generated/]
  E --> H
  F --> H
  G --> H
```

---

## ➕ Add a new icon (checklist ✅)

1. **Create / obtain SVG** in `_source/`
2. Confirm:
   - [ ] license & attribution are documented (if third-party)
   - [ ] `viewBox` is correct
   - [ ] uses `currentColor` unless explicitly semantic
   - [ ] no embedded text, no raster images unless intentional
3. Run the generator
4. Verify:
   - [ ] manifest updated
   - [ ] sprite updated (if used)
   - [ ] visual spot-check at `16/20/24px`
   - [ ] passes security sanitization
5. Commit generated outputs (or ensure CI generates them deterministically)

---

## 🧪 Troubleshooting

- **Icon looks blurry**
  - likely off-grid geometry or odd stroke alignment
  - verify `viewBox` and rounding; avoid fractional strokes where possible

- **Icon color won’t theme**
  - ensure SVG uses `currentColor` or CSS variables
  - remove hardcoded fills/strokes unless required

- **Sprite has collisions**
  - duplicate IDs inside SVG (`id="path0"` etc.)
  - generator should namespace IDs; fix source if needed

- **WebGL marker looks wrong**
  - rasterize to appropriate sizes and consider power-of-two textures if needed
  - avoid ultra-thin strokes for textures

---

## 📚 Project library used to shape this icon system

> This list documents **why** the icon pipeline is designed the way it is (performance, provenance, GIS/3D, security, and scientific tooling).

<details>
<summary><strong>📦 Core principles & architecture</strong> (click to expand)</summary>

- **KFM – Comprehensive Technical Documentation** (provenance-first, clean architecture, transparency)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Flexible Software Design** (stable identifiers, consistent standards, change-ready systems)  [oai_citation:5‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  
- **Database Performance at Scale** (treat frequent small artifacts as “hot path” assets; think workload + item size)  [oai_citation:6‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  
- **Data Spaces** (metadata-first thinking; linking artifacts to context)

</details>

<details>
<summary><strong>🗺️ GIS, cartography, and 3D context</strong> (click to expand)</summary>

- **Making Maps: A Visual Guide to Map Design for GIS** (symbol clarity & cartographic design)
- **Mobile Mapping: Space, Cartography and the Digital** (field/mobile constraints; icon legibility)
- **Archaeological 3D GIS** (3D analysis workflows & “3D mode” affordances)  [oai_citation:7‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- **WebGL Programming Guide** (textures, sprites, GPU-friendly icon usage)
- **Python Geospatial Analysis Cookbook** (geospatial workflows that influence UI semantics)
- **Cloud-Based Remote Sensing with Google Earth Engine** (remote-sensing layers that need clear iconography)

</details>

<details>
<summary><strong>🌐 Web UI, formats, compression</strong> (click to expand)</summary>

- **Responsive Web Design with HTML5 and CSS3** (icons across breakpoints + touch targets)
- **Compressed Image File Formats (JPEG/PNG/GIF/… )** (choose correct formats; understand tradeoffs)
- **Scalable Data Management for Future Hardware** (pipeline thinking + efficient I/O patterns)

</details>

<details>
<summary><strong>🧠 Data science & modeling UX (why we need “analysis” icons)</strong> (click to expand)</summary>

- **SciPy Lecture Notes / Scientific Python** (tooling patterns for reproducible pipelines)  [oai_citation:8‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K)  
- **Scientific Modeling & Simulation (NASA-grade guide)** (reproducibility mindset)
- **Regression Analysis with Python** + **Linear Regression Slides** (analytics UX affordances)
- **Understanding Statistics & Experimental Design** (uncertainty, results, validity indicators)
- **Think Bayes** (probability/uncertainty icons)
- **Understanding Machine Learning: From Theory to Algorithms** (ML workflow semantics)  [oai_citation:9‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  
- **Basics of Linear Algebra for Machine Learning** (math/graph glyphs and notation support)  [oai_citation:10‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  

</details>

<details>
<summary><strong>🔐 Security & ethics (why SVG sanitization + neutral iconography)</strong> (click to expand)</summary>

- **Ethical Hacking and Countermeasures** (threat mindset for “small” assets)
- **Gray Hat Python** (offense/defense awareness; supply-chain caution)
- **Introduction to Digital Humanism** (human-centered, transparent UI)
- **On the path to AI Law’s prophecies…** (policy-aware UI semantics)

</details>

<details>
<summary><strong>🧩 Engineering references (cross-platform + toolchain mindset)</strong> (click to expand)</summary>

- **Bash Notes for Professionals** (automation scripts)  [oai_citation:11‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  
- **MATLAB Notes for Professionals** (scientific workflows; future tooling)  [oai_citation:12‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e)  
- **Objective-C Notes for Professionals** (cross-platform client possibilities)  [oai_citation:13‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  
- **Implementing Programming Languages** (pipeline/phases thinking)  [oai_citation:14‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  
- **Concurrent Real-Time and Distributed Programming in Java** (future service + tooling constraints)
- **PostgreSQL Notes for Professionals** (asset metadata storage patterns)
- **Spectral Geometry of Graphs** / **Generalized Topology Optimization** / **Principles of Biological Autonomy** (scientific domains that may influence module icon sets)
- **A / B-C / D-E / F-H / I-L / M-N / O-R / S-T / U-X Programming Books** (broad language ecosystem references)
- **Deep Learning for Coders with fastai and PyTorch** (training/inference UX affordances)

</details>

---

## ✅ Summary

- `_generated/` is **output**, not authoring space.
- Icons should have **stable IDs**, be **themeable**, **accessible**, **secure**, and **fast**.
- Keep icon provenance/attribution as first-class metadata—KFM expects traceability everywhere.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
