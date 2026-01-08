<div align="center">

# 🗺️🛰️ KFM Web Viewers

**Browser-first geospatial viewers for the Kansas Frontier Matrix (KFM)**  
🗺️ 2D Explorer (MapLibre) • 🛰️ 3D Globe (Cesium) • 📚 Story Nodes • 🔍 Focus Mode

</div>

---

## 🧭 What lives in `web/viewers/`

This folder is the **front-end visualization layer** for KFM: the pieces that turn cataloged assets (layers, events, story artifacts, 3D models) into an **interactive map/globe experience**.

### ✅ Core promises

- **One dataset, many lenses**: the same underlying artifacts can be explored in 2D, 3D, and narrative modes.
- **Catalog-driven UX**: viewers are powered by **catalog + provenance** contracts (STAC/DCAT/PROV patterns), not hard-coded layers.
- **Story-first exploration**: “Story Nodes” provide curated waypoints; “Focus Mode” provides deep dives with evidence and overlays.
- **Governed UI boundary**: UI consumes data via **API contracts** (no direct coupling to the graph DB).

> [!IMPORTANT]
> Treat the viewer as **a contract consumer**: it should render whatever is present in the catalogs and gracefully degrade when data is missing, redacted, or gated.

---

## 🧩 Viewer lineup

### 🗺️ MapLibre viewer (2D)

Best for:
- Vector & raster exploration (roads, parcels, boundaries, annotations)
- Fast interaction (hover/inspect, filter, cluster)
- “Cartographic clarity” (legends, symbol systems, print-ish layouts)

Typical features:
- 🧱 Layer toggles + legend
- 🕰️ Timeline slider (time-window filtering)
- 🧷 Event markers + clustering
- 🧪 Small charts / spark-lines for metrics panels

**Expected subfolder:** `web/viewers/maplibre/`

---

### 🛰️ Cesium viewer (3D)

Best for:
- Terrain, elevation, subsurface/volumetric storytelling (when applicable)
- 3D assets (tilesets, GLB models, photogrammetry)
- Camera-path narratives and “cinematic” flythroughs

Typical features:
- 🌍 Globe + terrain
- 🧊 3D Tiles / GLB asset rendering
- 🎥 Camera paths for Story Nodes
- ⏱️ Time-dynamic overlays (where data supports it)

**Expected subfolder:** `web/viewers/cesium/`

---

### 🔀 Hybrid mode

A hybrid shell enables:
- A single URL/state model across 2D and 3D
- Seamless switching (e.g., same Story Node can open in 2D or 3D)
- Shared “Focus Mode” UI (narrative + evidence drawer)

**Expected subfolder:** `web/viewers/shared/`

---

## 🗂️ Suggested folder layout

> This layout is intentionally simple. The actual repo can evolve, but keeping the mental model stable matters. ✅

```text
web/
└─ viewers/
   ├─ 📄 README.md                # (you are here)
   ├─ 🧩 shared/                  # state, contracts, UI primitives
   │  ├─ router/                  # URL <-> app state mapping
   │  ├─ layer-registry/          # catalog-driven layer loading
   │  ├─ story-nodes/             # story node parsing + rendering helpers
   │  └─ ui/                      # panels, drawers, legend components
   ├─ 🗺️ maplibre/                # 2D viewer app
   ├─ 🛰️ cesium/                  # 3D viewer app
   ├─ 🧪 examples/                # minimal demos / smoke tests
   └─ 🧾 schemas/                 # client-side JSON schema mirrors (optional)
```

---

## 🧠 Core concepts (the “language” of KFM viewers)

### 1) 📦 Layer Registry (catalog-driven)

A viewer should not “know” about datasets directly. It should:
- Load a **layer manifest** (from API/catalog)
- Render supported formats
- Respect sensitivity gates (redaction, access rules, CARE labels)

**Practical implication:** adding a new dataset should feel like:
1) publish catalog entries + metadata  
2) viewer discovers it  
3) user toggles it on  

No front-end rebuild required when possible.

---

### 2) 📚 Story Nodes

A **Story Node** is a narrative waypoint: “here’s a place/time/topic + what to look at.”

A Story Node should be able to:
- Set **camera** (2D center/zoom or 3D camera path)
- Enable **layers**
- Show **assets** (images, charts, tables, 3D models)
- Provide **citations/provenance** as first-class UI

#### Minimal (proposed) Story Node shape

```json
{
  "id": "sn_kansas__example_001",
  "title": "Example Story Node",
  "time": { "start": "1870-01-01", "end": "1875-12-31" },
  "view": {
    "preferred": "2d",
    "center": [-96.5, 38.5],
    "zoom": 7,
    "bearing": 0,
    "pitch": 0
  },
  "layers": [
    { "id": "hydrology.streamflow", "visibility": "on" },
    { "id": "boundaries.counties_1870", "visibility": "on" }
  ],
  "assets": [
    { "type": "image", "href": "assets/story_nodes/sn_kansas__example_001/figure_1.png", "alt": "…" },
    { "type": "3d", "href": "assets/story_nodes/sn_kansas__example_001/model.glb", "alt": "…" }
  ],
  "narrative_md": "…",
  "citations": [{ "label": "Source A", "ref": "…" }]
}
```

> [!NOTE]
> Treat the schema above as **WIP scaffolding**. The key requirement is that Story Nodes remain **portable** (2D ↔ 3D) and **evidence-forward**.

---

### 3) 🔍 Focus Mode

Focus Mode is the “deep dive” experience:
- anchored to a feature/site/region
- enriched with timeline, provenance, and cross-layer context
- built for analysts, not just casual browsing

Typical UI primitives:
- 🧾 Evidence drawer (sources, datasets, provenance bundles)
- 🧠 Context panel (related events, linked entities)
- 🕰️ Timeline scrubber
- 🏷️ CARE/FAIR indicators and gating notices

---

### 4) 🛰️ On-map Automation & Provenance Badges

KFM viewers should be able to overlay **automation status** directly on mapped features:
- ✅ healthy / ⚠️ degraded / ⛔ failing / ⏳ running
- “last run” timestamps
- links to attestation/SBOM/manifests (shown in a drawer UI)

This keeps the map honest: users see *not just the data*, but how recently and how reliably it was produced.

---

## 📦 Data contracts & formats

### 🗺️ 2D viewer formats

- **Vector tiles** (preferred for scale)
- **GeoJSON** (small / ad-hoc / debug)
- **GeoParquet / Arrow IPC** (preferred for large analytical overlays; avoid JSON bloat)

Patterns:
- stream/filter columnar data for tables/charts
- tile on read for map rendering
- keep CRS explicit

---

### 🛰️ 3D viewer formats

- **Terrain** (DEM-derived)
- **Tilesets** (3D Tiles / similar)
- **GLB/GLTF** for discrete models
- **CZML / time-dynamic** assets (when needed)

---

### 🧾 Metadata and governance hooks

Viewers must treat metadata as UI-critical:
- dataset license & usage notes
- provenance links (what generated this, when)
- sensitivity/redaction flags
- CARE labels & required messaging
- checksums / integrity info (when present)

> [!TIP]
> Metadata should be visible **without leaving the map** (drawer, tooltip, info panel).

---

## 🗺️ Cartography & legend conventions

Good cartography is a feature.

Recommended map UI elements:
- 🧭 clear legend (qualitative vs quantitative symbol rules)
- 🧱 figure–ground hierarchy (what’s foreground, what’s context)
- 🏷️ label discipline (avoid clutter; scale-dependent labels)
- 🎚️ layer opacity controls and blend modes (when relevant)

Also support **mobile mapping realities**:
- small screens
- intermittent connectivity
- location-permission UX (when used)
- fat-finger friendly controls

---

## 🌊 Example thematic layers (KFM patterns)

The viewer stack should be ready to host thematic stacks such as:

- 💧 **Water systems**: streamflow, flood stage, groundwater wells, watershed units
- ⚠️ **Hazards**: multi-hazard overlays, event timelines, impact footprints
- 🌡️ **Climate anomaly signals**: anomaly clusters + time windows  
  *(Important: don’t frame these as emergency alerts unless explicitly certified)*
- 🌫️ **Air quality**: sensor networks, AQ indicators, comparisons over time

> [!CAUTION]
> Viewer UX must clearly differentiate:
> - **historical narrative**
> - **observations**
> - **model outputs**
> - **alerts** (if any; usually not)

---

## ⚡ Performance & scalability checklist

### 🎛️ Rendering performance

- Prefer **tiled** representations for large layers (MVT, raster tiles, 3D tiles)
- Minimize draw calls (batch symbols; avoid excessive per-feature DOM)
- Use WebGL-friendly encoding (typed arrays, binary formats)
- Offload heavy parsing to workers where practical

### 🧠 Data performance

- Prefer **Arrow/Parquet** for large attribute tables and analytics overlays
- Push filters down (server-side or columnar scan)
- Cache aggressively (ETags + immutable asset URLs where possible)
- For interactive analytics, consider approximate queries with error bounds (when appropriate)

### 🖼️ Asset optimization

- Choose image formats intentionally:
  - photos → lossy (where acceptable)
  - line art/symbols → lossless
- Keep icon sets consistent and versioned
- Use checksums to detect drift

---

## 📱 Responsive UX & accessibility

Baseline commitments:
- Semantic HTML for UI controls (menus, buttons, dialogs)
- Keyboard navigation (Tab, Enter/Escape)
- ARIA labels for map controls and drawers
- Progressive enhancement (core navigation works without “fancy” features)

Map accessibility practices:
- Provide **text equivalents** for story maps (narrative + captions)
- Provide **alt text** for story assets and figures
- Ensure color is not the only encoding (patterns, labels, tooltips)

---

## 🛡️ Security & privacy (viewer-specific)

Front-ends are inspectable. Assume:
- client code can be reverse engineered
- network traffic can be observed
- untrusted content may appear (dataset metadata, story text, external sources)

Recommended practices:
- Never ship secrets to the client
- Strict input handling for any rendered HTML/Markdown (sanitize)
- Avoid dangerous DOM sinks (no raw `innerHTML` from untrusted sources)
- Strong CSP and dependency hygiene
- Respect data gates (redaction, access control, sovereign restrictions)

---

## 🧪 Local development

> These commands are illustrative. Align them with whatever build tool the repo standardizes on (Vite/Next/etc.). ✅

```bash
# from repo root
cd web

# install dependencies
npm install

# run dev server
npm run dev
```

### 🔧 Typical env vars (examples)

```bash
# API base URL (contracts boundary)
KFM_API_BASE_URL=http://localhost:8080

# optional: enable/disable specific viewers
KFM_ENABLE_CESIUM=true
KFM_ENABLE_MAPLIBRE=true
```

---

## 🧰 Testing strategy (recommended)

- ✅ Schema validation for:
  - layer manifests
  - story node JSON
  - automation badge payloads
- 🧪 E2E smoke tests (Playwright) for:
  - map loads
  - layer toggles
  - story node navigation
  - focus mode opening
- 🖼️ Visual regression tests:
  - “golden” Story Nodes
  - known legend layouts
  - known 3D camera paths

---

## 🗺️ Roadmap (viewer-side)

- [ ] Unified URL state model across 2D/3D
- [ ] Story Node renderer (portable 2D ↔ 3D)
- [ ] Focus Mode evidence drawer + citation UI
- [ ] On-map automation/provenance badges (stream + fallback polling)
- [ ] Arrow/Parquet ingestion for large overlays + chart panels
- [ ] Accessibility audit + keyboard-first navigation
- [ ] Performance budgets (fps, memory, tile latency) + CI gates

---

## 📚 Project Library (used to design these viewers)

<details>
<summary><b>📖 Expand full library list</b> (engineering + science + design references)</summary>

### 🧭 KFM system & design docs
- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx**
- 📄 **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf**
- 📄 **Latest Ideas.docx**
- 📄 **Other Ideas.docx**

### 🌐 Web UI, rendering, performance
- 📄 **responsive-web-design-with-html5-and-css3.pdf**
- 📄 **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**
- 📄 **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf**
- 📄 **Scalable Data Management for Future Hardware.pdf**
- 📄 **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf**

### 🗺️ GIS, cartography, remote sensing
- 📄 **making-maps-a-visual-guide-to-map-design-for-gis.pdf**
- 📄 **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf**
- 📄 **python-geospatial-analysis-cookbook.pdf**
- 📄 **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**
- 📄 **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf**
- 📄 **Data Spaces.pdf**

### 📈 Statistics, modeling, ML, simulation
- 📄 **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**
- 📄 **Understanding Statistics & Experimental Design.pdf**
- 📄 **regression-analysis-with-python.pdf**
- 📄 **Regression analysis using Python - slides-linear-regression.pdf**
- 📄 **graphical-data-analysis-with-r.pdf**
- 📄 **think-bayes-bayesian-statistics-in-python.pdf**
- 📄 **Understanding Machine Learning_ From Theory to Algorithms.pdf**
- 📄 **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** *(if present in repo storage)*

### 🧠 Graphs, structure, optimization
- 📄 **Spectral Geometry of Graphs.pdf**
- 📄 **Generalized Topology Optimization for Structural Design.pdf**

### ⚖️ Ethics, governance, human-centered systems
- 📄 **Introduction to Digital Humanism.pdf**
- 📄 **Principles of Biological Autonomy - book_9780262381833.pdf**
- 📄 **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf**

### 🛡️ Security (defensive reading)
- 📄 **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf**
- 📄 **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf**

### 🧰 Language & platform reference shelves
- 📄 **A programming Books.pdf**
- 📄 **B-C programming Books.pdf**
- 📄 **D-E programming Books.pdf**
- 📄 **F-H programming Books.pdf**
- 📄 **I-L programming Books.pdf**
- 📄 **M-N programming Books.pdf**
- 📄 **O-R programming Books.pdf**
- 📄 **S-T programming Books.pdf**
- 📄 **U-X programming Books.pdf**

</details>

---

## 🤝 Contributing

If you’re adding or changing viewer behavior:

1) **Start with contracts** (schemas, manifests, catalog fields).  
2) Add/adjust rendering adapters (MapLibre / Cesium).  
3) Add a Story Node or example view that demonstrates the change.  
4) Add tests (schema + smoke + snapshot).

Small, testable, catalog-driven changes scale best. ✅

