# 🗺️ MapViewer (KFM) — Provenance‑First Map Canvas

> **Location:** `web/src/components/MapViewer/README.md`  
> **Purpose:** The **primary mapping viewport** for Kansas Frontier Matrix (KFM): interactive **2D MapLibre** + optional **3D Cesium**, wired into the **timeline + story + citations** experience.

---

## ✨ Why MapViewer exists

KFM is explicitly **provenance-first**: every map layer, dataset, story, and even AI-assisted answer should be **traceable back to original sources** (“the map behind the map”). MapViewer is the UI surface where that promise becomes visible and testable.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

KFM also enforces a strict “truth path” data flow (**Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI**), and the **UI must never bypass the governed API**. MapViewer is therefore **API-fed** and **policy-respecting by default**.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✅ What MapViewer is / is not

### ✅ MapViewer *is*
- A **map canvas** that initializes and owns the **MapLibre GL map instance** (2D) and optionally a **Cesium Viewer** (3D), with a UX toggle between them.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- A **state-driven renderer**: listens to global UI state (timeline year, active layers, filters) and updates visual layers accordingly.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- A **provenance surface**: ensures the user can reach layer metadata, licensing, and citations from what they see.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ❌ MapViewer is *not*
- A place to run direct DB queries (UI cannot touch PostGIS/Neo4j directly).  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- A data ingestion or ETL tool (that happens earlier in the pipeline).  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- The authority for governance decisions (policy gates exist at boundaries; the UI must comply with responses it receives).  [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧭 Architecture context (Truth Path, in one picture)

```mermaid
flowchart LR
  Raw[📥 Raw] --> Proc[🏭 Processed]
  Proc --> Cat[🗂 Catalog (STAC/DCAT)]
  Cat --> DB[(🗃 Datastores)]
  DB --> API[🌐 Governed API]
  API --> UI[🗺 MapViewer / UI]
  UI --> AI[🤖 Focus Mode]
  AI --> API
```

**Key rules:**
- UI access is mediated by the backend API and governance policies.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- The canonical pipeline order is enforced system-wide.  [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧩 Where MapViewer fits in the UI tree

KFM’s blueprint explicitly places MapViewer under `web/src/components/MapViewer`, alongside Timeline + Story UI components.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

```text
🗂 web/
  🗂 src/
    🗂 components/
      🗂 MapViewer/        🧭 (this folder)
      🗂 TimelineSlider/   ⏳ time navigation
      🗂 StoryPanel/       📖 narrative + citations
      🗂 FocusMode/        🤖 AI assistant UI
```

---

## 🗺 Rendering engines: 2D MapLibre + 3D Cesium

### 2D (MapLibre GL JS)
MapLibre is the intended high-performance browser renderer for **vector tiles** and **raster layers** in KFM.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:13‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

### 3D (Cesium)
Cesium is the intended path for 3D expansion (terrain, 3D tiles, time-dynamic globe views). The blueprint calls for supporting Cesium-friendly formats like **3D Tiles / CZML**, and smooth transitions between 2D and 3D contexts.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## 🔌 Data contracts MapViewer should rely on (API-first)

KFM favors an **API-first** approach where clients consume documented REST/GraphQL APIs.  [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 📚 Dataset discovery + metadata
- `GET /api/v1/datasets/{id}` → returns DCAT summary + links to assets (STAC items, etc.).  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- `GET /api/v1/catalog/search` → search by keyword / bbox / time range.  [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- `GET /api/v1/datasets/{id}/data?format=geojson&bbox=...` → streams features (optionally filtered).  [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🧱 Map tiles for rendering
KFM serves both vector and raster tiles so **multiple clients “drink from the same well.”**  [oai_citation:20‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Vector tiles (MVT): `GET /tiles/{layer}/{z}/{x}/{y}.pbf`  [oai_citation:21‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Raster tiles: `GET /tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)  [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🕸 Knowledge graph queries (optional but powerful)
- `POST /graphql` supports richer “join-like” requests across places ↔ datasets ↔ events ↔ stories, with security constraints.  [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> **MapViewer guidance:** Prefer tiles for visualization (fast), and use feature endpoints only for:
> - Identify-on-click (feature info)
> - Small extents / low feature counts
> - User-driven analysis tools (draw bbox → request subset)

---

## ⏳ Timeline-driven mapping (the “time machine”)

KFM’s blueprint describes a global UI state store (Redux) where the **timeline year** (e.g., `currentYear`) drives which layers are visible, and both the **map component and story panel respond** to those changes.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**MapViewer must:**
- Treat time as a first-class filter (year/decade/range)
- Support “scrub” (drag slider) and “play” (animate)
- Ensure time changes update:
  - Layer visibility
  - Layer source params (e.g., tile URL template with year)
  - Legend + provenance panel for currently visible layers

> A timeline slider / play button approach is explicitly called out as a KFM goal.  [oai_citation:25‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## 🧾 Provenance & metadata (non-negotiable)

KFM requires that published data carries:
- metadata via **STAC/DCAT**
- lineage via **W3C PROV**
…and that visible outputs remain traceable.  [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ✅ What MapViewer should surface for any visible layer
A dependable GIS layer should ship metadata such as identification, quality, spatial reference, distribution, temporal info, contact, and **citation guidance**.  [oai_citation:28‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

**UI checklist (per layer):**
- 🏷️ Title + short description
- 📅 Temporal coverage (time range / vintage)
- 🧭 CRS / projection (where relevant)
- 📦 Data source + license
- 🔗 “Show citations” (human-readable references)
- 🧬 “Provenance chain” (where it came from, transformations)
- 🛡️ Policy status (public / restricted / masked), if returned by API

---

## 🪶 Indigenous data & ethical display (CARE / OCAP alignment)

KFM’s documentation explicitly references **FAIR** and **CARE** principles and emphasizes community rights and privacy.  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Indigenous data sovereignty contexts include frameworks like **CARE** and **OCAP**, and MapViewer must avoid treating sensitive community-linked layers as “just another overlay.”  [oai_citation:30‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

**Practical MapViewer implications:**
- 🧯 Never “auto-enable” sensitive layers (require user intent + explicit acknowledgment, if applicable)
- 🧊 Respect redaction/masking returned by the API (do not attempt client-side “reconstruction”)
- 🧾 Always display authority + usage notes when present
- 🧠 Avoid UI copy that frames communities as deficits (tone matters)

---

## 🧱 Suggested internal module responsibilities

> Even if your actual file names differ, keep these responsibilities separated to preserve sanity 😄

### `MapViewer.tsx` (or equivalent)
- Owns map container + initializes MapLibre/Cesium instances
- Connects to global store selectors (view state, time state, active layers)
- Wires interaction events → dispatches actions / calls callbacks

### `hooks/`
- `useMapLibre()` → create/destroy map, register listeners
- `useCesium()` → create/destroy viewer, sync camera
- `useLayerManager()` → diff layers, add/remove/update efficiently
- `useTimelineSync()` → translate time selection into layer config

### `types.ts`
- Layer descriptors (id, datasetId, style, time behavior, legend/provenance refs)
- View state types (lng/lat/zoom/bearing/pitch + optional altitude)

### `utils/`
- Tile URL builders (`/tiles/{layer}/{z}/{x}/{y}.pbf`, `.png`, `.webp`)  [oai_citation:31‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Debounce/throttle utilities for view state updates
- “Safe style” helpers (avoid untrusted URL injection)

---

## 🧪 Performance & UX guidelines

### Tiles first (speed)
Use vector tiles / raster tiles for interactive display. KFM explicitly provides tile endpoints for this purpose.  [oai_citation:32‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Avoid heavy GeoJSON for wide extents
- Prefer MVT for “lots of features”
- Only fetch GeoJSON on demand (identify, analysis, export)

### Responsive UI + clean markup
Maintain standards-compliant, semantically meaningful markup for controls and panels (important for accessibility and predictability).  [oai_citation:33‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

---

## 🧠 State management expectations

Blueprint expectation:
- A **global state store (Redux)** keeps shared state: map viewport, active layers, timeline year, story selection.  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Recommended state slices:**
- `map.viewState` → center/zoom/bearing/pitch
- `time.currentYear` or `time.range`
- `layers.active[]`
- `ui.mode` → `2d | 3d`
- `story.activeNodeId`
- `provenance.panelOpen` + `provenance.activeLayerId`

---

## 🧑‍💻 Development workflow notes (frontend tooling)

If the web app uses a Create React App style workflow, typical scripts include `start`, `build`, `test` (and optionally `eject`).  [oai_citation:35‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

For dev servers (webpack-dev-server style), `npm start` launches a local server (often on `localhost`) for rapid iteration.  [oai_citation:36‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## 🧾 “Citations panel” UX pattern (recommended)

When a user toggles a layer on:
1. Show the layer in the legend
2. Provide a **“Sources / Citations”** affordance
3. Provide a **“Provenance”** affordance (chain / lineage)

This directly supports KFM’s “map behind the map” promise.  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🖼 Raster compression notes (PNG/JPEG/WebP sanity)

KFM supports raster tiles as `.png` or `.webp`.  [oai_citation:38‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

When choosing raster formats, remember:
- JPEG is powerful for photographic imagery and can achieve major size reductions, but it is typically **lossy** and not ideal for repeated editing or crisp linework.  [oai_citation:39‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)
- Lossless vs lossy tradeoffs matter for cartography (text/lines vs imagery).  [oai_citation:40‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)

---

## 🧷 Troubleshooting

### Map renders blank
- Confirm style JSON is reachable
- Confirm tile endpoints respond (check `/tiles/...`)
- Ensure CORS headers are correct (API gateway / CDN)

### 3D mode is slow
- Verify 3D is only enabled when requested
- Reduce active layers on 3D transitions (especially heavy raster overlays)
- Prefer 3D Tiles where possible (Cesium-friendly streaming)  [oai_citation:41‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

### Timeline slider works, but layers don’t change
- Confirm MapViewer is subscribed to timeline store changes (`currentYear`)
- Confirm layer descriptors include time behavior (visibility rules, templated tile URL)

---

## 🧰 Minimal “expected props” (example contract)

> ⚠️ This is a **recommended** shape to keep MapViewer composable. Adjust to match your implementation.

```ts
export type MapMode = "2d" | "3d";

export interface MapViewState {
  lng: number;
  lat: number;
  zoom: number;
  bearing?: number;
  pitch?: number;
}

export interface LayerDescriptor {
  id: string;              // stable UI id
  datasetId?: string;      // links back to /api/v1/datasets/{id}
  tileLayer?: string;      // name used in /tiles/{layer}/...
  kind: "vectorTile" | "rasterTile" | "geojson";
  visible: boolean;

  // time behavior
  time?: {
    mode: "fixed" | "year" | "range";
    year?: number;
    range?: [number, number];
  };

  // provenance
  citations?: Array<{ label: string; note?: string }>;
  license?: string;
}
```

---

## 📚 Project file references (for this README)

These are the primary project references that informed this component’s contract, ethics, and UI obligations:

- KFM Comprehensive System Documentation (truth path, API, tiles, governance)  [oai_citation:42‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:43‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Node.js / React tooling notes (dev server + scripts)  [oai_citation:44‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  [oai_citation:45‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- Indigenous Statistics (CARE / OCAP context for respectful data governance)  [oai_citation:46‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  
- Learn to Code HTML & CSS (semantic, standards-compliant markup reminders)  [oai_citation:47‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  [oai_citation:48‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- Professional Web Design (general UI discipline reference)  [oai_citation:49‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  [oai_citation:50‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- Image compression notes (lossy vs lossless; JPEG characteristics)  [oai_citation:51‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)  [oai_citation:52‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)  
- Map design / metadata best practices (metadata, interoperability, citation info)  [oai_citation:53‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

---

## ✅ Maintenance checklist (keep MapViewer “KFM-correct”)

- [ ] UI never queries databases directly; only calls governed API endpoints.  [oai_citation:54‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] Timeline state change updates map layers predictably.  [oai_citation:55‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Every visible layer can surface citations + provenance.  [oai_citation:56‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Tile endpoints are the default rendering strategy.  [oai_citation:57‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] Sensitive/controlled datasets respect CARE/OCAP context and do not leak via UI affordances.  [oai_citation:58‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

---
