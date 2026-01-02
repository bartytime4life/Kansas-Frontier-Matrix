# 🌾🗺️ `web/` — Kansas Frontier Matrix Web Viewer

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Frontend](https://img.shields.io/badge/frontend-MapLibre%20%7C%20Leaflet%20%7C%20React-blue)
![3D](https://img.shields.io/badge/3D-Cesium%20(optional)-informational)
![License](https://img.shields.io/badge/license-see%20LICENSE-lightgrey)

A browser-based **interactive map + timeline** experience for the Kansas-Frontier-Matrix (KFM).  
This is where users **explore spatiotemporal layers**, **toggle historical eras**, and **open linked documents / insights** in a human-centered way. 🧭✨

---

## 🧩 What lives in `web/`?

This folder is the **front-end viewer** and GitHub Pages-ready site:

- **Static site assets** (e.g., `index.html`, `app.js`, `style.css`) for a lightweight deploy 🚀  
- **Precomputed JSON** used by the UI (e.g., document index, timeline configuration, layer manifests) 🧾  
- The **interactive map UI** that renders geospatial layers (vector + raster) and connects them to narrative / archival context 📚🗺️

> 🧠 In practice, the repo supports both a “static viewer” approach and a more componentized “app” approach:
> - **Static viewer**: MapLibre/Leaflet + vanilla JS (fast to iterate, easy to deploy)
> - **App viewer**: React components (MapView / Sidebar / TimelineSlider / ChartPanel / DataTable) for richer UI patterns

---

## ✨ What the viewer is designed to do

### Core experience (2D)
- 🗺️ **Map rendering** via open web mapping libraries (MapLibre GL JS recommended; Leaflet supported)
- 🧅 **Layer toggles** with time-aware visibility (turn layers on/off by era)
- ⏳ **Timeline slider** (drag, step, play/pause animation) for temporal navigation
- 🪟 **Popups / side panels** showing:
  - layer metadata & provenance
  - feature attributes
  - linked document excerpts + citations / references
- 🔎 **Search & filtering** (place names, tags, date ranges, “sites of interest”)

### Optional experience (3D)
- 🌍 **3D globe mode** (CesiumJS) to visualize terrain + time-indexed overlays  
- 🛰️ Raster tile overlays, GeoJSON draped vectors, and time-dynamic updates tied to the same timeline UI

---

## 🚀 Quickstart (local)

> ⚠️ **Do not open `index.html` by double-clicking** (you’ll hit CORS/file:// limits). Always run a local server.

### Option A — Static viewer (no build step) ✅
From the repo root:

```bash
cd web

# Python (simple)
python -m http.server 8000

# OR Node (simple)
npx serve -l 8000
```

Open:
- `http://localhost:8000`

### Option B — React/dev server (if this folder contains a package.json) ⚛️
If you see `web/package.json`:

```bash
cd web
npm install
npm run dev    # or: npm start
```

Open the URL printed in your terminal.

---

## ⚙️ Configuration (`.env`)

Front-end builds often need **public** configuration (tile endpoints, public tokens, base API URL).

Create a local env file **without committing secrets**:

```bash
cp ../.env.example ../.env
# or (if scoped to web only)
cp .env.example .env
```

### Common env keys (recommended)
```bash
# Backend API (if running services)
VITE_API_BASE_URL=http://localhost:8080

# Map tiles / styles
VITE_MAP_STYLE_URL=/data/styles/kfm-style.json
VITE_TILE_BASE_URL=/tiles

# Optional: Map provider key (keep it public-scope only)
VITE_MAPTILER_KEY=YOUR_PUBLIC_KEY
```

✅ If it’s a **secret**, it should NOT be in the web bundle.  
Frontend tokens must be considered “public enough” and restricted (domain restrictions, quotas).

---

## 🗂️ Suggested `web/` structure

> This is the recommended layout that supports both “static” and “app” styles cleanly.

```text
web/
├─ 🧾 index.html
├─ 🎨 style.css
├─ 🧠 app.js                 # static entry (or compiled entry)
├─ 📦 package.json           # optional (only if using a build tool)
├─ 🧩 src/                   # optional React source
│  ├─ 🗺️ components/
│  │  ├─ MapView/
│  │  ├─ Sidebar/
│  │  ├─ TimelineSlider/
│  │  ├─ ChartPanel/
│  │  └─ DataTable/
│  ├─ 🔌 api/
│  ├─ 🧱 state/
│  └─ 🧪 tests/
├─ 📚 data/
│  ├─ 🗃️ catalog/            # STAC-like layer manifests (JSON)
│  ├─ ⏳ timeline.json        # timeline config (ticks, eras)
│  ├─ 🧾 doc_index.json       # document knowledge base index (precomputed)
│  ├─ 🗺️ styles/             # MapLibre style JSON + sprites/fonts if local
│  └─ 🧭 ui_config.json       # optional UI defaults
└─ 🖼️ assets/
   ├─ logos/
   └─ icons/
```

---

## 🧠 UI architecture (how we think about the app)

If you’re building the richer UI (React-style), the mental model is:

- 🗺️ **MapView**: owns the map instance + rendering lifecycle
- 🧰 **Sidebar**: layer toggles, legend, filters, metadata
- ⏳ **TimelineSlider**: global time control (ticks + playback)
- 📈 **ChartPanel**: time-series, histograms, comparisons (Plotly/Chart.js/D3)
- 📋 **DataTable**: exportable tables and provenance
- 🧭 **Header/Nav**: mode switching (2D/3D), global controls, settings

State patterns:
- 🧠 Global UI state (selected time, active layers, selected feature) via **Redux** or **Context/hooks**
- 🔁 Keep **URL-deep-linkable state** when possible (shareable exploration links)

---

## 🗺️ Data contracts (what the web viewer expects)

KFM is built around **traceable, reproducible, time-aware layers**.

### 1) Layer catalog (STAC-like JSON)
Each layer should have:
- `id`, `title`, `description`
- `bbox`, `crs`
- `time` coverage (single date, range, or discrete list)
- `assets`:
  - raster tiles / COGs
  - vector sources (GeoJSON / tiles)
  - optional KML/KMZ exports
- `source` + attribution
- processing notes (how it was derived)

Example sketch:

```json
{
  "id": "ks_hillshade",
  "title": "Kansas LiDAR Hillshade",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "time": { "type": "static" },
  "assets": {
    "raster_tiles": { "type": "xyz", "url": "/tiles/ks_hillshade/{z}/{x}/{y}.png" }
  },
  "provenance": {
    "source_name": "KARS GeoPlatform (ArcGIS REST)",
    "license": "see source",
    "processing": ["download", "reproject", "COG", "tile"]
  }
}
```

### 2) Document index (knowledge base)
A lightweight JSON index the UI can query by:
- place
- date / era
- tags / themes
- linked geometry (point/line/polygon) or nearest-feature lookup

UI behavior:
- Clicking a feature can show linked excerpts and citations
- Searching a place can jump to geometry + related documents

---

## ⏳ Time slider semantics (the “4D” promise)

Time changes should synchronize:
- 🗺️ visible layers (swap sources or filter features)
- 📈 chart indicators (vertical marker at current time)
- 🧾 derived stats panels (“current value at T”)
- 🧭 bookmarks / share links (optional)

Recommended patterns:
- Discrete time steps when data is episodic (historic maps by year)
- Continuous slider + snapping for dense time series (remote sensing)

---

## 🌐 API integration (optional but powerful)

If the backend services are running, the web viewer can:
- fetch metadata + data products via REST
- stream updates via WebSockets / SSE for real-time dashboards (sensor feeds, job progress)

Typical calls:
- `GET /api/catalog` → layer manifests
- `GET /api/layers/:id?time=YYYY-MM-DD` → time-filtered assets
- `GET /api/docs?bbox=...&time=...` → document mentions in view
- `WS /ws` → live updates (progress, sensor streams)

---

## ♿ UX + accessibility checklist (non-negotiable)

We build for humans first (and we mean it). 🧑‍🤝‍🧑🌱

- ⌨️ Keyboard navigation (map focus, slider control, sidebar)
- 🏷️ ARIA labels for:
  - timeline slider
  - layer toggles
  - dialogs / popovers
- 🎨 Color isn’t the only signal (patterns, labels, tooltips)
- 📱 Mobile-first layouts (map + panels stack cleanly)
- 🧾 Provenance shown where users make decisions (sources, uncertainty, “what changed?”)

---

## ⚡ Performance rules of thumb

Geospatial web apps can melt laptops if we’re not careful 🔥💻 — here’s how we keep it smooth:

- 🧊 Prefer **tiled raster (WMTS/XYZ)** and **vector tiles** for large layers
- 🧬 Simplify geometry at small zoom levels (server-side or build-time)
- 🧰 Lazy-load heavy layers (only when toggled)
- 🧠 Cache aggressively (HTTP caching headers for tiles + manifests)
- 🧵 Offload parsing to Web Workers for big GeoJSON (if needed)
- 🗜️ Compress JSON (gzip/brotli) and prefer NDJSON for big streams

---

## 🚢 Deployment

### GitHub Pages (recommended)
This folder is designed to be the **publish root** for Pages.

- Keep assets relative (`./data/...`, `./assets/...`)
- Avoid absolute `/` paths unless you control the domain root
- If using a build step, configure the base path so routing works in Pages

### Docker (optional)
If you prefer containerized local preview:

```bash
# Example pattern (adjust to your repo setup)
docker run --rm -p 8000:80 -v "$(pwd)/web:/usr/share/nginx/html:ro" nginx:alpine
```

Then open `http://localhost:8000`.

---

## 🧪 Dev quality: linting + consistency

- Follow repo-wide conventions: `../.editorconfig`
- Use repo pre-commit hooks: `../.pre-commit-config.yaml` (when available)
- Keep map styling changes reviewable (prefer JSON style files + small diffs)

---

## 🤝 Contributing

- Start here: `../CONTRIBUTING.md` ✅  
- Security reporting: `../.github/SECURITY.md` 🔒  
- PR format: `../.github/PULL_REQUEST_TEMPLATE.md` 🧾

When contributing to `web/`:
- Keep UI changes **traceable** (screenshots + notes in PR)
- Prefer **open formats** (GeoJSON, COG, KML/KMZ exports)
- Preserve **provenance metadata** whenever you add/modify layers

---

## 📚 Project Reading Room (why there are so many PDFs 😄)

This project is intentionally multidisciplinary: mapping, visualization, data engineering, AI, statistics, simulation, and ethics.

<details>
<summary><b>📖 Click to expand the full project library</b></summary>

### 🌐 Web / UI / Graphics
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `Computer Graphics using JAVA 2D & 3D.pdf`

### 🗺️ GIS / Mapping / Remote Sensing
- `Geographic Information System Basics - geographic-information-system-basics.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `geoprocessing-with-python.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Google Maps API Succinctly - google_maps_api_succinctly.pdf`
- `google-maps-javascript-api-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `Google Earth Engine Applications.pdf`

### 🧱 Data engineering / Systems
- `Scalable Data Management for Future Hardware.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf`
- `Introduction-to-Docker.pdf`
- `Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf`

### 🤖 AI / ML / Data mining
- `AI Foundations of Computational Agents 3rd Ed.pdf`
- `deep-learning-in-python-prerequisites.pdf`
- `Artificial-neural-networks-an-introduction.pdf`
- `Data Mining Concepts & applictions.pdf`
- `applied-data-science-with-python-and-jupyter.pdf`
- `Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`

### 📊 Statistics / Experimentation
- `Understanding Statistics & Experimental Design.pdf`
- `Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf`
- `regression-analysis-with-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `Bayesian computational methods.pdf`

### 🧪 Modeling / Simulation / Optimization
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Spectral Geometry of Graphs.pdf`
- `MATLAB Programming for Engineers Stephen J. Chapman.pdf`

### 🧭 Architecture / Humanism
- `clean-architectures-in-python.pdf`
- `implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf`
- `Introduction to Digital Humanism.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🧠 KFM core docs
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`

</details>

---

## ✅ Next implementation targets (web)

- [ ] Finalize `data/catalog/*.json` schema + validator
- [ ] Implement TimelineSlider (ticks + play/pause) tied to layer visibility
- [ ] Add “Document mentions near cursor/feature” panel
- [ ] Add robust error UI (missing tiles, slow network, stale manifests)
- [ ] Ship a “demo dataset” bundle for instant onboarding 📦

---

> 🔙 Back to project root: `../README.md`