<!--
📍 File: web/src/state/README.md
🧠 Purpose: Global + cross-cutting UI state for the KFM web app
-->

# 🧠 KFM UI State (`web/src/state`)

![Contract-first](https://img.shields.io/badge/Contract--First-✅-0b7285?style=for-the-badge)
![Provenance-first](https://img.shields.io/badge/Provenance--First-🔎-364fc7?style=for-the-badge)
![Evidence-backed AI](https://img.shields.io/badge/Focus%20Mode-Evidence--Backed-845ef7?style=for-the-badge)
![React + TS](https://img.shields.io/badge/React%20%2B%20TypeScript-SPA-087f5b?style=for-the-badge)
![MapLibre + Cesium](https://img.shields.io/badge/MapLibre%20%2B%20Cesium-2D%2F3D-5f3dc4?style=for-the-badge)

> **Non‑negotiable pipeline order** (a.k.a. “don’t put the cart before the horse”):  
> **ETL → STAC/DCAT/PROV → Graph → APIs → React/Map UI → Story Nodes → Focus Mode** ✅:contentReference[oaicite:0]{index=0}

This folder is the **single canonical home** for **global/cross-feature UI state** that makes KFM feel cohesive:
- 🗺️ Map view (2D/3D) + layer toggles/opacity/legends
- 🕰️ Timeline slider + temporal filtering + event markers
- 🎬 Story Nodes playback (Markdown narrative + JSON map actions)
- 🧠 Focus Mode panel state (questions, context selection, citations)
- 🔍 Search / selection / “inspect this feature” UX
- 🔒 Auth + roles (what the UI shows/enables)
- 🧾 Provenance hooks (“map behind the map” tooltips, citations, metadata)

KFM’s front-end is a React (TypeScript) SPA with **MapLibre GL JS** for 2D and **CesiumJS** for 3D, with layer toggles/opacity/legends and a timeline slider.:contentReference[oaicite:1]{index=1}

---

## 🧭 Table of Contents

- [🎯 Design Goals](#-design-goals)
- [🚧 Guardrails](#-guardrails)
- [🧩 What Belongs in State](#-what-belongs-in-state)
- [🗂️ Suggested Layout](#️-suggested-layout)
- [🔁 Data Flow](#-data-flow)
- [🗺️ Map + Timeline State](#️-map--timeline-state)
- [🎬 Story Nodes State](#-story-nodes-state)
- [🧠 Focus Mode State](#-focus-mode-state)
- [🔎 Provenance & Sensitivity](#-provenance--sensitivity)
- [⚡ Performance Rules](#-performance-rules)
- [💾 Persistence Rules](#-persistence-rules)
- [🧪 Testing](#-testing)
- [🧰 Debugging & DevTools](#-debugging--devtools)
- [➕ Adding a New Slice](#-adding-a-new-slice)
- [📚 Project Sources](#-project-sources)

---

## 🎯 Design Goals

1. **One mental model**: predictable “single source of truth” for global UI behavior.
2. **Provenance everywhere**: anything visible is explainable and traceable (metadata + citations).:contentReference[oaicite:2]{index=2}
3. **Contract-first**: state stores *typed* shapes that match API contracts (no random JSON blobs).:contentReference[oaicite:3]{index=3}
4. **Performance by design**: map apps die from accidental re-renders and huge in-memory GeoJSON.
5. **Composable features**: map, timeline, stories, and Focus Mode must interlock without “repo drift”.:contentReference[oaicite:4]{index=4}

---

## 🚧 Guardrails

### 1) API boundary rule (hard)
The frontend must **never** query Neo4j directly. All data access flows through the governed API layer.:contentReference[oaicite:5]{index=5}

✅ UI state stores **IDs + view preferences + request status**  
🚫 UI state stores **raw graph query strings / direct drivers / credentials**

---

### 2) Evidence-first UI (hard)
Focus Mode and Story Nodes must remain **grounded** and **inspectable**:
- Focus Mode is **assistive**, not autonomous, and answers are **evidence-backed**.:contentReference[oaicite:6]{index=6}
- Focus Mode has a hard gate: **only provenance-linked content** is allowed; “no sources → no answer.”:contentReference[oaicite:7]{index=7}

---

### 3) New features must connect back to provenance (hard)
If you add a new UI layer/feature, you must tie it to:
- Dataset catalog metadata
- Citation/provenance panels
- Sensitivity rules (e.g., coordinate redaction when needed):contentReference[oaicite:8]{index=8}

---

## 🧩 What Belongs in State

Think in 3 buckets:

### ✅ Bucket A: **UI state** (this folder)
Stuff the user manipulates directly:
- active layer IDs + visibility/opacity
- selected time range / cursor year
- selected feature IDs
- story playback step
- Focus Mode panel open/closed + selected context items
- auth role + feature gating flags
- toasts, modals, keyboard shortcuts, etc.

### ✅ Bucket B: **Server/cache state** (fetch layer)
Fetched datasets, responses, and caching. Prefer a dedicated cache layer (e.g., React Query/TanStack Query, SWR, etc.).  
Store only references in UI state (IDs, request keys, pagination cursors).

### ✅ Bucket C: **Local component state**
Ephemeral: form drafts, hover highlights, temporary UI toggles that don’t affect other parts of the app.

---

## 🗂️ Suggested Layout

> This README documents the intended organization. If files differ, update the tree to match reality ✍️

```text
📁 web/src/state/
├─ 📄 README.md               # you are here 🙂
├─ 📄 index.ts                # re-exports (public surface area)
├─ 📁 slices/                 # feature “domains” (small, focused)
│  ├─ 🗺️ map.slice.ts
│  ├─ 🕰️ timeline.slice.ts
│  ├─ 🧱 layers.slice.ts
│  ├─ 🎬 story.slice.ts
│  ├─ 🧠 focusMode.slice.ts
│  ├─ 🔎 search.slice.ts
│  ├─ 🔒 auth.slice.ts
│  └─ 🧾 provenance.slice.ts
├─ 📁 selectors/              # derived state (pure, memoized)
├─ 📁 persistence/            # localStorage/IndexedDB wiring (safe subset only)
├─ 📁 middleware/             # logging, devtools, telemetry hooks
└─ 📁 types/                  # IDs, schema helpers, shared state types
```

> **Rule of thumb**: slices hold **minimal canonical state + actions**. Anything derived belongs in selectors.

---

## 🔁 Data Flow

```mermaid
flowchart LR
  ETL[🛠️ ETL jobs] --> CATS[🗂️ STAC/DCAT/PROV catalogs]
  CATS --> GRAPH[🧠 Knowledge Graph]
  GRAPH --> API[🔌 Governed APIs]
  API --> CACHE[📦 Client Fetch/Cache]
  CACHE --> STATE[🧠 UI State (this folder)]
  STATE --> UI[🖥️ React + MapLibre/Cesium]
  UI --> STORY[🎬 Story Nodes]
  UI --> FOCUS[🧠 Focus Mode]
  STORY --> STATE
  FOCUS --> STATE
```

The order and responsibilities match the v13 pipeline rules.:contentReference[oaicite:9]{index=9}

---

## 🗺️ Map + Timeline State

### Map (2D/3D)
KFM uses MapLibre for 2D and Cesium for 3D; users toggle layers, adjust opacity, and view legends.:contentReference[oaicite:10]{index=10}

State should typically include:
- `viewMode`: `"2d" | "3d"`
- `camera`: `{ center, zoom }` (2D) and/or `{ position, heading, pitch, roll }` (3D)
- `selectedFeatureIds`: stable IDs (not whole geometries)
- `inspectPanel`: open/closed + active entity ID
- `interactionMode`: pan/measure/draw/select, etc.

> 🚫 Don’t put full **GeoJSON feature collections** in global state. Store IDs + bounding boxes + request keys.

### Timeline
The UI includes a timeline slider; time-filtered layers respond to slider movement and can show event markers (e.g., Dust Bowl).:contentReference[oaicite:11]{index=11}

State should include:
- `timeCursor`: a canonical “current time” (year/date)
- `timeRange`: optional range selection
- `timelineEvents`: IDs of curated event markers (resolved from catalog/API)
- `animation`: `{ playing, speed, loop }`

---

## 🎬 Story Nodes State

Story Nodes are Markdown narratives + JSON “map actions”. The front-end reads the Markdown and uses the JSON to drive map behavior (e.g., activate layer, set camera, set time).:contentReference[oaicite:12]{index=12}

State should include:
- `activeStoryId`
- `activeStepIndex`
- `stepStatus`: `"idle" | "transitioning" | "ready"`
- `playback`: `{ playing, speed }`
- `userOverride`: whether user interactions temporarily override story-driven camera/layers

💡 Pattern suggestion:
- Store **desired** story-driven map directives separately from **actual** camera state coming from map events:
  - `storyDesiredView` vs `mapActualView`
  - a reconciler decides which wins based on `playback` + `userOverride`

---

## 🧠 Focus Mode State

Focus Mode is an assistive layer: users ask questions and receive narrative answers grounded in KFM data, with references users can verify.:contentReference[oaicite:13]{index=13}

The UI pattern described:
- user selects a topic (place/time layer set)
- Focus Mode gathers relevant graph/data context and returns answer + citations
- users can click citations and jump to map layers / features / docs:contentReference[oaicite:14]{index=14}

State should include:
- `threadId` / `sessionId`
- `messages[]`: `{ role, content, citations[], createdAt }`
- `selectedContext`: `{ placeIds[], layerIds[], timeRange, documentIds[] }`
- `status`: `"idle" | "thinking" | "error"`
- `lastEvidenceCheck`: for “no citations → block response” UX:contentReference[oaicite:15]{index=15}

> ✅ Focus Mode answers must be **distinguished** from human-authored content (UI labeling) and always be **evidence-backed**.:contentReference[oaicite:16]{index=16}

---

## 🔎 Provenance & Sensitivity

KFM’s philosophy: show “the map behind the map”—tooltips/inspect panels should expose data sources and metadata instead of hiding them.:contentReference[oaicite:17]{index=17}

### Provenance in state: minimum viable pattern
Store **provenance references** alongside anything user can see or cite.

Example shape (illustrative):
```ts
type ProvRef = {
  // stable reference keys (prefer IDs over raw URLs)
  datasetId?: string;      // DCAT dataset id
  assetId?: string;        // STAC item/asset id
  provActivityId?: string; // PROV activity/lineage id
  citations?: Array<{
    title: string;
    locator?: string;      // page/line/section
    uri?: string;          // optional external link
  }>;
};
```

### Sensitivity rules
If something is sensitive (e.g., precise coordinates for a protected site), the UI must:
- generalize / redact coordinate display
- gate download/export controls
- preserve provenance even when redacting details:contentReference[oaicite:18]{index=18}

---

## ⚡ Performance Rules

### 1) Normalize entities (IDs first)
Prefer “entity maps” over nested duplication:
- `layersById`, `placesById`, `datasetsById`
- arrays store ordering only

This aligns with “generic entities” thinking: unify synonymous “things” behind stable identifiers to reduce duplication and drift.:contentReference[oaicite:19]{index=19}

### 2) Store *references*, not payloads
- ✅ store `layerId`, `datasetId`, `tileSourceId`, `bbox`, `timeKey`
- 🚫 store huge GeoJSON, raw raster arrays, full 3D tiles, etc.

### 3) Selector discipline
- derive “visibleLayers” via selectors
- memoize expensive computations
- subscribe narrowly (avoid re-rendering whole app when 1 layer opacity changes)

### 4) Streaming + windowing mindset
KFM can deal with time series and “moving windows” (timeline, NDVI series, etc.). Build state updates as:
- incremental events
- bounded buffers/ring buffers
- checkpoints for resumability (especially for long-running UI sessions)

(See stream/window semantics notes for stateful systems.):contentReference[oaicite:20]{index=20}

---

## 💾 Persistence Rules

KFM can be configured to work as a static site / PWA for offline demos and learning scenarios, so persistence is useful—but must be safe.:contentReference[oaicite:21]{index=21}

Persist **only**:
- theme, units, panel layout
- last map view (optional)
- last selected story step (optional)

Never persist:
- secrets, tokens, raw API keys
- private documents
- sensitive coordinates / restricted features

---

## 🧪 Testing

Minimum bar for each slice:
- ✅ reducer/action tests (pure state transitions)
- ✅ selector tests (derived outputs)
- ✅ “integration” tests for cross-slice flows (e.g., story step updates layers + timeline)

Suggested test table:
| Test Type | What to verify | Example |
|---|---|---|
| Unit | actions update minimal canonical state | toggle layer visibility |
| Selector | derived state correctness | visible layers obey time cursor |
| Flow | cross-feature choreography | story step sets camera + time |
| Regression | bug never returns | “opacity slider flicker” |

---

## 🧰 Debugging & DevTools

Recommended dev-only helpers:
- 🧾 “Last N actions” log (bounded)
- 🧪 state snapshot export/import (for reproducible bug reports)
- 🛰️ perf markers around heavy selector work
- 🧠 Focus Mode evidence inspector (why was an answer allowed/blocked?)

Remember: the goal is not just debugging—it’s **auditability** (proof a UI outcome was grounded and reproducible).:contentReference[oaicite:22]{index=22}

---

## ➕ Adding a New Slice

Checklist ✅

1. **Name the domain** (map, story, focusMode, etc.) and create `*.slice.ts`
2. **Define the minimal canonical state**
   - don’t store derived state
   - don’t store raw heavy payloads
3. **Add actions with clear intent**
   - prefer `setX`, `toggleY`, `selectZ`
4. **Add selectors** for computed views
5. **Wire provenance**
   - every visible thing has a provenance hook:contentReference[oaicite:23]{index=23}
6. **Respect the API boundary**
   - no direct graph access:contentReference[oaicite:24]{index=24}
7. **Add tests** for actions + selectors
8. **Update this README** if you add new conventions or domains ✍️

---

## 📚 Project Sources

### Core governance / architecture (must-read)
- **KFM Technical Documentation** (platform, UI, Focus Mode, 2D/3D, timeline, provenance) :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26}  
- **MASTER_GUIDE v13** (pipeline ordering, API boundary, provenance rules, Focus Mode gates) :contentReference[oaicite:27]{index=27}

### Engineering references used in this README
- **Database Performance at Scale** (performance mindset & bottlenecks) :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29}  
- **Scalable Data Management for Future Hardware** (windowing/stateful systems thinking) :contentReference[oaicite:30]{index=30} :contentReference[oaicite:31]{index=31}  
- **Flexible Software Design** (generic entities / ID-first modeling) :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33}  
- **Archaeological 3D GIS** (3D GIS context) :contentReference[oaicite:34]{index=34} :contentReference[oaicite:35]{index=35}  
- **Understanding Machine Learning** (ML concepts for model result UX) :contentReference[oaicite:36]{index=36}  
- **Implementing Programming Languages** (pipeline mental model) :contentReference[oaicite:37]{index=37}  
- **MATLAB Notes / Bash Notes** (tooling references) :contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39}  

<details>
<summary>📦 Full project reference shelf (PDFs provided in this workspace)</summary>

> Tip: treat this as a “stack of lenses” 🥽—mapping, simulation, stats, ML, databases, UI, and ethics all inform how we design *trustworthy* state.

- 🛰️ Cloud-Based Remote Sensing with Google Earth Engine (Fundamentals and Applications)
- 🧮 Regression analysis with Python
- 📈 Understanding Statistics & Experimental Design
- 🧠 Think Bayes (Bayesian statistics in Python)
- 🗺️ Making Maps (map design for GIS)
- 🧭 Mobile Mapping (space, cartography, digital)
- 🌐 Responsive Web Design (HTML5/CSS3)
- 🎮 WebGL Programming Guide
- 🧱 PostgreSQL Notes for Professionals
- 🧾 Data Spaces
- 🧬 Principles of Biological Autonomy
- 🤖 Introduction to Digital Humanism
- ⚖️ On the path to AI Law’s prophecies…
- 🧯 Ethical Hacking & Countermeasures (security mindset)
- 🐍 Gray Hat Python (historical reference; use responsibly)
- 🖼️ Compressed Image File Formats (JPEG/PNG/GIF/etc.)
- 🧊 Generalized Topology Optimization (structural design)
- 🧠 Spectral Geometry of Graphs
- 🧪 Scientific Modeling and Simulation (NASA-grade guide)
- 🧰 Programming Books Bundles (A, B–C, D–E, F–H, I–L, M–N, O–R, S–T, U–X)

</details>

