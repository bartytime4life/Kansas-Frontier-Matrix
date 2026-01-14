# 🖼️ Chart Preview Assets (KFM Web)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-0b7285?style=flat&logo=leaflet&logoColor=white)
![UI](https://img.shields.io/badge/web-assets%2Fcharts%2Fpreviews-111827?style=flat&logo=vercel&logoColor=white)
![A11y](https://img.shields.io/badge/a11y-first-1f2937?style=flat&logo=accessible-icon&logoColor=white)
![Provenance](https://img.shields.io/badge/provenance-first-111827?style=flat&logo=bookstack&logoColor=white)

This folder contains **small, fast, deterministic preview images** used by the KFM web UI wherever we ask a human to “pick a chart” (e.g., a chart gallery, layer analytics panel, a “visualize this attribute” wizard, etc.). 🎛️📈

> **Design intent:** previews should communicate *shape & semantics* (line vs histogram vs choropleth vs network) without implying any *real-world claim* or embedding *real user data*. ✅

---

## 📌 Contents

- [✅ What lives here](#-what-lives-here)
- [📐 Preview spec](#-preview-spec)
- [🧾 Naming conventions](#-naming-conventions)
- [🧪 Provenance metadata](#-provenance-metadata)
- [⚙️ How to add or update a preview](#️-how-to-add-or-update-a-preview)
- [🔒 Safety and security notes](#-safety-and-security-notes)
- [🚦Review checklist](#-review-checklist)
- [📚 Project reference shelf](#-project-reference-shelf)

---

## ✅ What lives here

Typical contents (examples only):

```text
📁 web/
  📁 assets/
    📁 charts/
      📁 previews/
        📄 README.md
        🖼️ line.webp
        🖼️ bar.webp
        🖼️ scatter.webp
        🖼️ histogram.webp
        🖼️ choropleth.webp
        🧾 previews.manifest.json
        🧪 line.preview.json
```

**This folder is for:**
- 🧩 **Chart picker thumbnails** (static previews)
- 🧭 **Documentation thumbnails** (if the docs reuse these assets)
- 🧪 **Deterministic / synthetic** representations (seeded data only)

**This folder is *not* for:**
- ❌ User uploads / user-generated images
- ❌ Screenshots of real datasets, real people, real addresses, or sensitive locations
- ❌ High-res marketing graphics (put those in a proper marketing/media folder)

---

## 📐 Preview spec

Previews must be optimized for **fast UI rendering** and **consistent visual meaning**.

### Recommended defaults

| Item | Recommended | Why |
|---|---:|---|
| Format | `.webp` (lossless when needed) | Small + modern browser support |
| Fallback | `.png` | When sharp text/lines suffer or WebP tooling is missing |
| Aspect ratio | **16:10** (e.g., 512×320) | Reads well in galleries + cards |
| DPR strategy | Render at 2×, downscale to 1× | Crisp lines without huge files |
| Target size | **≤ 50 KB** each (ideally ≤ 25 KB) | Keeps chart libraries snappy |
| Background | Transparent or “theme surface” | Supports light/dark UI |

### Text and labeling rules

- Keep text minimal: **“Time”, “Value”, “Count”, “Latitude/Longitude”** are fine.
- Avoid dense tick labels (they become illegible at thumbnail size).
- Prefer “shape” cues: gridlines, axes, a single legend chip, a single annotation.

---

## 🧾 Naming conventions

Keep names boring, stable, and grep-friendly. 🧱

### Pattern

```text
<chartId>.<ext>
<chartId>@2x.<ext>              (optional)
<chartId>.preview.json          (recommended provenance sidecar)
```

Examples:

```text
line.webp
scatter.webp
choropleth.webp
network-graph.webp
line.preview.json
```

### `chartId` rules
- `kebab-case` only
- no spaces
- no version numbers in the filename (version in metadata instead)
- the `chartId` should match the ID used by the UI’s chart registry / manifest

---

## 🧪 Provenance metadata

KFM’s broader philosophy is “📚 **show your sources**” and “🔎 **make it inspectable**.”  
Even previews benefit from provenance so we don’t end up with mystery thumbnails.

### Sidecar file (recommended)

Create: `chartId.preview.json`

```json
{
  "id": "line",
  "title": "Time series (line)",
  "family": "timeseries",
  "dataset": {
    "type": "synthetic",
    "seed": 42,
    "notes": "No real data. Seeded for deterministic rendering."
  },
  "render": {
    "width": 512,
    "height": 320,
    "dpr": 2,
    "format": "webp",
    "background": "transparent"
  },
  "generator": {
    "tool": "playwright|node|python|r",
    "entry": "scripts/charts/render-previews.(ts|py|R)",
    "version": "0.1.0"
  },
  "created_at": "YYYY-MM-DD",
  "notes": [
    "Keep labels short for thumbnail legibility.",
    "Avoid misleading axes (no truncated y-axis unless chart type requires it)."
  ]
}
```

### Optional manifest (recommended)

If the UI enumerates previews dynamically, keep a single manifest:

`previews.manifest.json`

```json
{
  "line": { "src": "line.webp", "alt": "Line chart preview" },
  "bar":  { "src": "bar.webp", "alt": "Bar chart preview" }
}
```

---

## ⚙️ How to add or update a preview

### 1) Choose the right chart “semantic”
Use the simplest chart that matches the question. A preview should **teach the user what the chart *means***.

Examples:
- “How does it change over time?” → **Line / area**
- “How are values distributed?” → **Histogram / density / box**
- “How do two variables relate?” → **Scatter + trend**
- “Where is it?” → **Choropleth / point map / heatmap**
- “How are things connected?” → **Network graph / adjacency**

### 2) Generate the preview (deterministically)
Use any deterministic pipeline that fits the chart type:

- 🧑‍💻 **Web charts**: render the actual React/D3/Canvas/SVG component headlessly and screenshot
- 🐍 **Python**: matplotlib / plotly export to PNG/WebP
- 📊 **R**: ggplot2 export
- 🌐 **WebGL** (3D): render a known camera pose + screenshot (avoid dynamic lighting randomness)

> If you can’t automate yet, do it manually **once**, but write down the steps in the sidecar JSON so we can automate later.

### 3) Optimize the asset
- Convert to WebP (lossless if needed)
- Strip metadata
- Verify file size target (≤ 50 KB)

### 4) Add/update provenance
- Add or update `chartId.preview.json`
- Update `previews.manifest.json` if used

---

## 🔒 Safety and security notes

Even “just images” can be risky in web pipelines. 🛡️

### SVG: treat it as code
If you use SVG previews:
- **Do not** allow `<script>` or event handlers (`onload=`, `onclick=`…)
- Run an SVG sanitizer / optimizer (and consider rasterizing to PNG/WebP)

### No PII, no sensitive geo
- Never embed real addresses, names, phone numbers, emails, or sensitive coordinates.
- Avoid “too realistic” geography screenshots if they could be interpreted as claims.

### Supply chain + CI sanity
- Keep image tooling pinned (lockfiles)
- Prefer deterministic builds to avoid “preview drift”

---

## 🚦 Review checklist

Before committing a new/updated preview:

- [ ] **Correct semantic** for the chart family (preview teaches the right idea)
- [ ] **No real data** / no PII / no sensitive locations
- [ ] **Readable at thumbnail size** (test at 128–256px wide)
- [ ] **Consistent aspect ratio** with the rest of the gallery
- [ ] **Optimized** (≤ 50 KB, no bloated metadata)
- [ ] **Accessible**: alt text exists in manifest or UI registry
- [ ] **Safe format handling** (especially if SVG is involved)
- [ ] **Sidecar provenance** added/updated (`.preview.json`)

---

## 🗺️ Preview pipeline (suggested)

```mermaid
flowchart LR
  A["🧪 Seeded synthetic data"] --> B["📦 Chart component / renderer"]
  B --> C["🖥️ Headless render"]
  C --> D["📸 Screenshot / export"]
  D --> E["🧼 Optimize (webp/png)"]
  E --> F["🧾 Manifest + provenance"]
  F --> G["✅ Commit + review"]
```

---

## 📚 Project reference shelf

These project files inform how we design previews (truthfulness, statistical integrity, cartographic clarity, performance, security, and long-term maintainability). 📚✨

<details>
<summary><strong>📊 Statistics, experiments, and ML (chart semantics)</strong></summary>

- **Understanding Statistics & Experimental Design** — choosing correct encodings; error bars; avoiding misleading visuals. <!--  [oai_citation:0‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd) -->
- **Regression analysis with Python** — scatter + fit line, residual thinking, model literacy. <!--  [oai_citation:1‡think-bayes-bayesian-statistics-in-python.pdf](file-service://file-LXwJApPMVhRZgyqLb9eg7c) -->
- **Regression analysis using Python (slides)** — quick linear regression visual patterns. <!--  [oai_citation:2‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L) -->
- **Think Bayes (Bayesian statistics in Python)** — posterior plots, credible intervals, distribution previews. <!--  [oai_citation:3‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM) -->
- **Graphical Data Analysis with R** — classic exploratory visuals and when to use them. <!--  [oai_citation:4‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR) -->
- **Deep Learning for Coders (fastai + PyTorch)** — ML workflow visuals (learning curves, confusion matrices). <!--  [oai_citation:5‡Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf](file-service://file-GqygtUWf5Xyi3AjEaqEdQB) -->
- **(If present) Understanding Machine Learning: From Theory to Algorithms** — generalization mindset; what “good” visuals should communicate. <!--  [oai_citation:6‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M) -->

</details>

<details>
<summary><strong>🧭 GIS, cartography, remote sensing (map-like charts)</strong></summary>

- **Making Maps (GIS map design)** — visual hierarchy, symbol clarity, legend discipline. <!--  [oai_citation:7‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj) -->
- **Python Geospatial Analysis Cookbook** — spatial analysis patterns and outputs. <!--  [oai_citation:8‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp) -->
- **Cloud-Based Remote Sensing with Google Earth Engine** — time-series + NDVI-like visuals; remote sensing chart patterns. <!--  [oai_citation:9‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV) -->
- **Mobile Mapping: Space, Cartography and the Digital** — mobile constraints; meaning at small sizes. <!--  [oai_citation:10‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2) -->
- **Archaeological 3D GIS** — 3D/stratigraphic visualization cues and interpretation discipline. <!--  [oai_citation:11‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY) -->

</details>

<details>
<summary><strong>🧠 Modeling, simulation, graphs (advanced visual families)</strong></summary>

- **Scientific Modeling & Simulation (NASA-grade)** — reproducibility, uncertainty bands, validation-first visuals. <!--  [oai_citation:12‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8) -->
- **Generalized Topology Optimization** — field/mesh result previews; scalar fields; convergence visuals. <!--  [oai_citation:13‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd) -->
- **Spectral Geometry of Graphs** — eigen/spectrum plots and network structure representations. <!--  [oai_citation:14‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd) -->
- **Principles of Biological Autonomy** — feedback/phase-space thinking; system behavior visuals. <!--  [oai_citation:15‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf) -->

</details>

<details>
<summary><strong>🌐 Web UI, rendering, and assets (how previews behave on real screens)</strong></summary>

- **Responsive Web Design (HTML5 + CSS3)** — responsive images, layout-driven aspect choices, small-screen legibility. <!--  [oai_citation:16‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK) -->
- **WebGL Programming Guide** — deterministic camera poses and stable rendering for 3D previews. <!--  [oai_citation:17‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7quELMw4FrspPczB9Y3BTp) -->
- **Compressed image file formats (JPEG/PNG/GIF/… )** — trade-offs: crisp lines vs file size vs transparency. <!--  [oai_citation:18‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) -->

</details>

<details>
<summary><strong>🗄️ Data systems, performance, scale (keep the UI fast)</strong></summary>

- **PostgreSQL Notes for Professionals** — data sourcing patterns for analytics demos and synthetic generators. <!--  [oai_citation:19‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC) -->
- **Database Performance at Scale** — performance mindset; caching; avoid heavy asset payloads. <!--  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) -->
- **Scalable Data Management for Future Hardware** — interactive analytics constraints at scale. <!--  [oai_citation:21‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE) -->
- **Data Spaces** — interoperability and metadata thinking (helps provenance + manifests). <!--  [oai_citation:22‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq) -->

</details>

<details>
<summary><strong>🧩 Architecture, maintainability, ethics, and security</strong></summary>

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** — provenance-first UI; trust-centered UX; modular web layer. <!--  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) -->
- **Kansas-Frontier-Matrix (Open-Source Geospatial Historical Mapping Hub Design)** — UI patterns for layer exploration and explanation. <!--  [oai_citation:24‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA) -->
- **Flexible Software Design** — stable identifiers, change-tolerant asset contracts, long-lived conventions. <!--  [oai_citation:25‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY) -->
- **Introduction to Digital Humanism** — human-centered systems; transparency; avoid deceptive visuals. <!--  [oai_citation:26‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ) -->
- **On the path to AI Law’s prophecies…** — interpretability, prediction-vs-explanation literacy in ML visuals. <!--  [oai_citation:27‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv) -->
- **Ethical Hacking & Countermeasures** — threat modeling for asset pipelines. <!--  [oai_citation:28‡ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf](file-service://file-Q7EeqPb17SD9sV8Fb12LQX) -->
- **Gray Hat Python** — defensive awareness: inputs can be hostile; don’t treat SVG/HTML as “safe.” <!--  [oai_citation:29‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf) -->
- **Concurrent real-time & distributed programming (Java)** — real-time constraints; deterministic “preview drift” avoidance. <!--  [oai_citation:30‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6) -->

</details>

<details>
<summary><strong>🧰 Programming library bundles (tooling + build scripts)</strong></summary>

These are reference compilations used across the project for build tooling, scripting, and implementation patterns:

- **B-C programming Books** <!--  [oai_citation:31‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ) -->
- **F-H programming Books** <!--  [oai_citation:32‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY) -->
- **I-L programming Books** <!--  [oai_citation:33‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a) -->
- **O-R programming Books** <!--  [oai_citation:34‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE) -->
- **S-T programming Books** <!--  [oai_citation:35‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K) -->
- **A / D-E / M-N / U-X programming Books** (project shelf; may not be indexed here but are part of the repo/library)

</details>

---

<!--
📎 Internal citation anchors for the chat workspace (kept hidden so GitHub rendering stays clean):

 [oai_citation:36‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  [oai_citation:37‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)  [oai_citation:38‡M-N programming Books.pdf](file-service://file-EYCp5md89QY2cy5PCYS18e)  [oai_citation:39‡B-C programming Books.pdf](file-service://file-7V9zHZSJakZZrJAw9ASCMJ)  [oai_citation:40‡U-X programming Books.pdf](file-service://file-3hYtSGHtHmb6wyTtavym6M)  [oai_citation:41‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  [oai_citation:42‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:44‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
-->
