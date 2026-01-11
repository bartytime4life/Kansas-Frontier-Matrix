<div align="center">

# 🗺️🛰️ KFM Web Viewers — `web/viewers/`

**Browser-first geospatial viewers for the Kansas Frontier Matrix (KFM)**  
🗺️ 2D Explorer (MapLibre) • 🛰️ 3D Globe (Cesium) • 📚 Story Nodes • 🔍 Focus Mode • 🧾 Provenance UI

<img alt="Status" src="https://img.shields.io/badge/status-active%20development-brightgreen" />
<img alt="Engines" src="https://img.shields.io/badge/engines-MapLibre%20%7C%20Cesium-blue" />
<img alt="Modes" src="https://img.shields.io/badge/modes-explore%20%7C%20story%20%7C%20focus-purple" />
<img alt="Catalog-first" src="https://img.shields.io/badge/catalog-first-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1" />
<img alt="Governance" src="https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043" />
<img alt="Security" src="https://img.shields.io/badge/security-no%20secrets%20%7C%20sanitize%20untrusted%20content-red" />

</div>

> [!IMPORTANT]
> **KFM invariant (non‑negotiable ordering):**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> Viewers are **UI**. They are **contract consumers**, not a backdoor to the graph or raw storage.

---

## 🔗 Quick links

| What | Link |
|---|---|
| 🌾 Back to `web/` | `../README.md` |
| 🎨 Static assets rules | `../assets/README.md` |
| 🗂️ Frontend data assets rules | `../data/README.md` |
| 🧩 Story Nodes runtime rules | `../story_nodes/README.md` |
| 🧾 Report an issue | `https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new/choose` |

---

<details>
<summary><strong>🧭 Table of contents</strong></summary>

- [What lives in `web/viewers/`](#-what-lives-in-webviewers)
- [Non-negotiables](#-non-negotiables)
- [Where viewers fit in the KFM pipeline](#-where-viewers-fit-in-the-kfm-pipeline)
- [Viewer contract](#-viewer-contract-one-state-model-many-engines)
- [Viewer lineup](#-viewer-lineup)
  - [MapLibre viewer (2D)](#-maplibre-viewer-2d)
  - [Cesium viewer (3D)](#-cesium-viewer-3d)
  - [Hybrid shell](#-hybrid-shell)
  - [Capability matrix](#-capability-matrix)
- [Suggested folder layout](#-suggested-folder-layout)
- [Contracts & schemas](#-contracts--schemas)
- [Data inputs & formats](#-data-inputs--formats)
- [Story Nodes + Focus Mode integration](#-story-nodes--focus-mode-integration)
- [Provenance & governance UI](#-provenance--governance-ui)
- [Performance budgets & caching](#-performance-budgets--caching)
- [Accessibility & mobile mapping](#-accessibility--mobile-mapping)
- [Security & privacy](#-security--privacy)
- [Local development](#-local-development)
- [Testing & CI gates](#-testing--ci-gates)
- [Roadmap](#-roadmap)
- [Project library influence map](#-project-library-influence-map)

</details>

---

## 🧭 What lives in `web/viewers/`

This folder is the **front-end visualization layer** for KFM: the pieces that turn **cataloged, governed artifacts** (layers, events, Story Nodes, 3D assets, evidence bundles) into an **interactive map / globe experience**.

### ✅ Core promises

- **One dataset, many lenses**: the same cataloged artifacts can be explored in 2D, 3D, and narrative modes.
- **Catalog-driven UX**: viewers are powered by **catalog + provenance** patterns (STAC/DCAT/PROV), not hard-coded layers.
- **Story-first exploration**: Story Nodes provide curated waypoints; Focus Mode provides deep dives with evidence panels.
- **Governed UI boundary**: the viewer consumes data through **contracted endpoints or catalog pointers** (no direct coupling to graph DB).

> [!TIP]
> The viewer should render what is present, and **degrade gracefully** when data is missing, redacted, gated, or offline.

---

## 🧱 Non-negotiables

### 1) Pipeline ordering is absolute
Viewers never leapfrog upstream governance:

- 🚫 no “grab a file from a bucket and show it”
- 🚫 no “pull from Neo4j directly”
- ✅ render from **API contracts** or **catalog pointers** (STAC/DCAT/PROV)

### 2) No secrets. Ever.
Anything in `web/` is effectively world-readable.

- 🚫 no API keys that grant privileged access
- 🚫 no internal endpoints or private dataset URLs baked into styles/manifests
- ✅ if it’s sensitive, it must be gated/redacted upstream

### 3) Evidence-first UI
If the UI can show it, the UI must be able to answer:

- what is it?
- where did it come from?
- what changed it?
- what license governs it?
- what uncertainty / caveats apply?

### 4) Stable identifiers (IDs are contracts)
IDs are UI state keys and deep-link keys. Treat them like public APIs:

- **stable layer IDs** (don’t encode changing facts into IDs)
- versions live in metadata (`version`, `run_id`, `stac:version`, `prov:wasGeneratedBy`)
- keep “display names” separate from IDs

### 5) Treat all external content as hostile input
Metadata, Story Node markdown, GeoJSON properties, SVG, and style JSON are all untrusted:

- sanitize/escape before rendering
- avoid unsafe DOM sinks (`innerHTML` from untrusted input)
- enforce strict URL allowlists when fetching remote assets

---

## 🧭 Where viewers fit in the KFM pipeline

```mermaid
flowchart LR
  DATA["🗃️ Data (raw/processed)"] --> CAT["🗂️ Catalogs (STAC/DCAT/PROV)"]
  CAT --> GRAPH["🕸️ Graph / Index (derived)"]
  CAT --> API["🛡️ API boundary (contracts + policy + redaction)"]
  API --> UI["🌐 Viewers (this folder)"]
  CAT --> UI
  UI --> STORY["📚 Story Nodes + Focus Mode (evidence-linked)"]
````

> [!IMPORTANT]
> Viewers are downstream. They **do not create truth** — they **present governed outputs** with trust cues.

---

## 🧠 Viewer contract (one state model, many engines)

A KFM viewer should share a common **state model** so deep-links and reproducibility work across engines:

### ✅ Recommended state keys

* `engine`: `maplibre | cesium | hybrid`
* `time`: `date | range | step`
* `view`: `center | zoom | bearing | pitch` (2D) and/or `camera` (3D)
* `layers[]`: `{ id, visibility, opacity, styleVariant?, timeBehavior? }`
* `focus`: `{ featureId? | bbox? | placeId? }`
* `story`: `{ storyNodeId?, storyNodeVersion? }`
* `locks`: `{ versionLock: true/false, layerVersions?: {} }`

### URL conventions (suggested)

* `?engine=maplibre`
* `&time=1880-01-01`
* `&layers=boundaries.counties,transport.railroads`
* `&story=sn.ks.rail.1880.v1`
* `&lock=1`

> [!TIP]
> If it can’t be deep-linked, it can’t be reviewed. If it can’t be reproduced, it can’t be trusted.

---

## 🧩 Viewer lineup

### 🗺️ MapLibre viewer (2D)

Best for:

* fast pan/zoom exploration
* vector & raster layering
* “cartographic clarity” (legends, label discipline, print-ish layouts)
* time-aware overlays (timeline-driven visibility)

Expected subfolder: `web/viewers/maplibre/`

Typical features:

* 🧱 layer toggles + legend
* 🕰️ timeline slider (time-window filtering)
* 🧷 feature inspect + identify
* 🧾 provenance drawer (license + sources + runs)

---

### 🛰️ Cesium viewer (3D)

Best for:

* terrain and elevation context
* 3D Tiles / GLB models
* camera-path narratives (cinematic Story Nodes)
* time-dynamic primitives when data supports it

Expected subfolder: `web/viewers/cesium/`

Typical features:

* 🌍 globe + terrain
* 🧊 3D Tiles / GLB rendering
* 🎥 Story Node camera paths
* 🧾 evidence/provenance panels (same contract as 2D)

---

### 🔀 Hybrid shell

Hybrid enables:

* a single URL/state model across 2D and 3D
* seamless switching (same Story Node can open in 2D or 3D)
* shared Focus Mode UI (narrative + evidence drawer)

Expected subfolder: `web/viewers/shared/`

---

### 🧾 Capability matrix

| Capability                  | MapLibre (2D) |      Cesium (3D) | Shared/hybrid |
| --------------------------- | ------------: | ---------------: | ------------: |
| Timeline scrubber           |             ✅ |                ✅ |             ✅ |
| Vector tiles (MVT)          |             ✅ | ⚠️ (via adapter) |             ✅ |
| Raster tiles / COG previews |             ✅ | ⚠️ (via adapter) |             ✅ |
| 3D terrain                  |     ⚠️ (2.5D) |                ✅ |             ✅ |
| 3D Tiles / GLB              |            🚫 |                ✅ |             ✅ |
| Story Nodes                 |             ✅ |                ✅ |             ✅ |
| Focus Mode evidence drawer  |             ✅ |                ✅ |             ✅ |
| Version lock (repro UX)     |             ✅ |                ✅ |             ✅ |

---

## 🗂️ Suggested folder layout

> This is a **target shape**. If the repo differs, keep the intent: **shared contracts + shared state + engine adapters + examples + tests**.

```text
web/
└─ viewers/
   ├─ README.md
   ├─ shared/
   │  ├─ router/                 # URL <-> app state mapping
   │  ├─ contracts/              # schema + types (source of truth for viewer inputs)
   │  ├─ layer-registry/         # catalog-driven layer discovery and resolution
   │  ├─ story-nodes/            # story node parsing/render helpers
   │  ├─ focus-mode/             # evidence drawer + context panels
   │  ├─ provenance-ui/          # license/prov/run badges, disclaimers, kill-switch notices
   │  └─ ui/                     # panels, drawers, legend, timeline primitives
   ├─ maplibre/
   │  ├─ adapters/               # render adapters (MVT, raster tiles, PMTiles, GeoJSON)
   │  └─ app/                    # 2D bootstrap
   ├─ cesium/
   │  ├─ adapters/               # render adapters (3D Tiles, GLB, terrain, CZML)
   │  └─ app/                    # 3D bootstrap
   ├─ examples/
   │  ├─ smoke/                  # minimal demos
   │  └─ story-node-demo/        # “Kansas From Above” style hybrid demo
   ├─ schemas/                   # optional mirrors if you keep schemas near viewers
   └─ __tests__/
      ├─ contracts.schema.test.* # schema validation
      ├─ router.state.test.*     # deep-link reproducibility tests
      └─ smoke.e2e.test.*        # Playwright / e2e smoke
```

---

## 📦 Contracts & schemas

Viewers should be **schema-first** because UI is downstream of governance.

### Recommended contract set

Keep these in one place (pick one and standardize):

* `web/viewers/shared/contracts/`
* `web/data/schemas/`
* `schemas/` (repo-wide)

**Minimum schemas (suggested):**

* `layer.manifest.schema.json` (UI “view” of STAC + render hints)
* `timeline.schema.json`
* `storyNode.schema.json` (front matter / metadata contract)
* `evidenceBundle.schema.json` (Focus Mode payload)
* `provenanceBadge.schema.json` (automation / health / last-run)
* `redactionPolicy.schema.json` (UI-visible gating rules)

### Validation rule

* ✅ validate at build-time (CI)
* ✅ validate at runtime (defensive parsing)
* ✅ fail closed for restricted content if policy is unclear

> [!IMPORTANT]
> Story Nodes and metadata are untrusted. Schema validation ≠ sanitization. Do both.

---

## 🗺️ Data inputs & formats

Viewers should prefer **pointers over payloads**:

* authoritative assets are hosted and referenced via STAC/DCAT/PROV
* demo/offline assets live in `web/data/` and must be tiny + checksummed

### 2D-friendly formats

* Vector tiles (preferred at scale)
* Raster tiles for quicklooks
* GeoJSON for small curated overlays
* PMTiles/MBTiles for offline demos
* COG for “real-ish” streaming previews (when you control hosting)

### 3D-friendly formats

* Terrain (DEM-derived)
* 3D Tiles (tilesets)
* GLB/GLTF for discrete models
* CZML for time-dynamic primitives (optional)

---

## 📚 Story Nodes + Focus Mode integration

Story Nodes are narrative waypoints that drive:

* time
* camera
* layer visibility
* evidence panels
* optional 2D ↔ 3D engine switching

Focus Mode is the “reading cockpit”:

* story on one side
* map/globe + timeline on the other
* evidence drawer always one click away

> [!TIP]
> Keep Story Nodes portable: the same node should render in MapLibre or Cesium if the contracts are satisfied.

---

## 🧾 Provenance & governance UI

### Trust cues must be visible *in* the viewer

At minimum, the viewer should surface:

* license + attribution (displayed, not hidden)
* provider/source
* dataset/stac IDs
* “how produced” (PROV / run ID / timestamp)
* uncertainty / caveats
* sensitivity flags + redaction banners

### A safe default for AI-assisted UI

If Focus Mode includes AI assistance:

* user-controlled (opt-in)
* evidence-grounded (citations only)
* clearly labeled as AI-assisted
* never leaks sensitive locations by accident

---

## ⚡ Performance budgets & caching

### Practical budgets (heuristics)

* keep interaction smooth on laptops and mobile
* avoid multi‑MB GeoJSON blobs at runtime (tile instead)
* cache what’s reused; invalidate deterministically when versions change

### Caching rules of thumb

* cache within a **time/window** (recent queries / recent tiles)
* reuse computed results when users scrub time or revisit a location
* prefer immutable, hashed asset URLs when possible

> [!TIP]
> Treat “time scrub + pan” as the hot path. Optimize for repeated, similar queries.

---

## 📱 Accessibility & mobile mapping

Baseline commitments:

* semantic controls (buttons, menus, dialogs)
* keyboard navigation (Tab, Enter, Esc)
* ARIA labels for map controls and drawers
* no color-only encoding (patterns + labels + tooltips)
* responsive layouts (map always reachable; no scroll traps)

---

## 🛡️ Security & privacy

Front-ends are inspectable. Assume:

* client code can be reverse engineered
* network traffic can be observed
* untrusted content will be rendered (metadata, Story Nodes, external docs)

Recommended practices:

* never ship secrets
* sanitize Markdown and never render untrusted HTML
* escape feature properties by default (XSS posture)
* enforce strict CSP (especially on GitHub Pages)
* treat SVG, style JSON, and GeoJSON as potential injection vectors
* respect CARE/sovereignty flags and redaction policies

---

## 🧪 Local development

> Commands are illustrative; match the repo’s chosen tooling (Vite/React/static).

```bash
# from repo root
cd web

# install deps (if applicable)
npm install

# run dev server
npm run dev
```

### Typical env vars (examples)

```bash
# contracts boundary
KFM_API_BASE_URL=http://localhost:8080

# optional feature flags
KFM_ENABLE_CESIUM=true
KFM_ENABLE_MAPLIBRE=true
```

---

## ✅ Testing & CI gates

### Minimum bar

* schema validation for layer manifests, Story Nodes, evidence bundles
* router/deep-link tests (state ↔ URL is reversible)
* smoke tests (map loads, toggle layers, open story node, open focus mode)
* snapshot/visual tests for “golden” Story Nodes and legend layouts

### CI should fail if:

* a Story Node references missing evidence links
* a layer is missing license/provenance/sensitivity metadata
* a manifest is invalid
* a viewer starts depending on direct graph access

---

## 🛣️ Roadmap

* [ ] Unified URL state model across 2D/3D
* [ ] Layer Registry + render adapters (MVT, PMTiles, raster, COG previews)
* [ ] Portable Story Node renderer (2D ↔ 3D)
* [ ] Focus Mode evidence drawer + citation UI
* [ ] Provenance/automation badges on-map (health, last-run, attestation links)
* [ ] Performance budgets (fps/memory/tile latency) + CI regression gates
* [ ] Accessibility audit + keyboard-first flows

---

## 📚 Project library influence map

> These references inform viewer design decisions. Respect upstream licenses.

<details>
<summary><strong>📦 Expand: Project files → what they influence in <code>web/viewers/</code></strong></summary>

### 🧭 KFM system vision & governance

* **Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design / Technical Documentation** — pipeline ordering, viewer boundaries, evidence-first posture, sensitivity/redaction UI expectations.
* **KFM Markdown/Protocol guide** — Story Nodes + Focus Mode definitions, “no story without evidence”, AI labeling & opt-in expectations.
* **Design audit docs** — domain roadmap gaps that viewers must support (oral histories, hydrology, treaty narratives, uncertainty-first presentation).

### 🌐 Web UI, rendering, performance

* **Responsive Web Design (HTML/CSS)** — progressive enhancement, mobile-first layout constraints for map + panels.
* **WebGL Programming Guide** — GPU cost awareness, shader discipline, batching, avoiding fragment hotspots.
* **Compressed image formats** — correct asset formats for legends/sprites/thumbnails.
* **Scalable Data Management for Future Hardware** — caching/reuse mindset and “move less data” thinking.
* **Concurrent/distributed programming** — bounded work, avoiding unbounded parsing on the client.

### 🗺️ GIS, cartography, remote sensing

* **Making Maps (GIS design)** — legend truthfulness, visual hierarchy, avoiding misleading ramps/symbols.
* **Mobile Mapping** — offline constraints, location sensitivity, and small-screen map UX reality.
* **Python Geospatial Analysis Cookbook** — CRS sanity, vector/raster conventions, PostGIS/GeoJSON interoperability.
* **Cloud-Based Remote Sensing (GEE)** — time-series visualization patterns; why remote-sensing outputs need provenance and careful legends.

### 📈 Modeling, ML, statistics, simulation

* **Scientific Modeling & Simulation** — V&V posture: display uncertainty, assumptions, and validation artifacts.
* **Understanding Statistics & Experimental Design** — avoid misleading comparisons; clearly separate observation vs inference.
* **Regression/EDA/Bayes references** — diagnostic-friendly visual defaults and uncertainty-first UI patterns.
* **Understanding Machine Learning (theory/algorithms)** — model outputs are not “truth”; require evaluation context and clear caveats in UI.
* **Deep Learning references** — model cards, dataset shift awareness, avoid shipping weights to client by default.

### 🧠 Graphs, structure, optimization

* **Spectral geometry / topology optimization** — future network/graph overlays and scenario viewers; communicate assumptions and parameter sensitivity.

### 🔒 Security & human systems

* **Ethical hacking / Gray Hat (defensive posture)** — treat content as hostile input; reduce attack surface; sanitize everything.
* **Digital Humanism / autonomy / AI law framing** — sovereignty, accountability, and “assist not assert” UX patterns.

### 🧰 Programming reference shelves

* Programming bundles (A…U-X) — quick lookup for maintainers across languages and tooling.

</details>

---

## 🤝 Contributing

If you’re adding or changing viewer behavior:

1. Start with **contracts** (schemas, manifests, catalog fields).
2. Add/adjust **render adapters** (MapLibre / Cesium).
3. Add a **Story Node** or example view that demonstrates the change.
4. Add tests (schema + smoke + snapshot).

Small, testable, catalog-driven changes scale best. ✅
