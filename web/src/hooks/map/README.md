# 🗺️ Map Hooks — `web/src/hooks/map/`

> **Purpose:** This folder is the **React hook “control layer”** for KFM’s map experiences — keeping UI components declarative while we safely drive **MapLibre (2D)** and **Cesium (3D)**, synchronize with the **global state store**, and respect **governance + provenance** constraints.  
> _If it touches the map engine instance, layer lifecycle, selection/hover, viewport, or time-sync… it probably belongs here._ 🧭

---

## 🔩 Why hooks exist here (the “glue layer”)

KFM’s UI is map‑centric and stateful: when the user changes the timeline year, **global state updates** and multiple UI surfaces (map + story panel) react together. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Hooks in this folder sit between:

- 🧠 **Global store** (viewport, `currentYear`, active layers, selection, story focus) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- 🗺️ **Map engines** (MapLibre GL JS for 2D; CesiumJS for 3D) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- 🧱 **Data delivery** (vector/raster tiles, GeoJSON overlays, WMS/WFS/WCS, STAC/DCAT catalog) [oai_citation:3‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](sediment://file_00000000ebac71f7ba1281d629a3ff9b) [oai_citation:4‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_0000000000d8722f9ee56b2c59e5a887)
- 🛡️ **Governance signals** (RBAC roles, dataset sensitivity labels, OPA policy decisions, “fail closed”) [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- 🧾 **Provenance** (dataset PROV lineage + audit trails) [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧠 Golden rules (non‑negotiables)

### 1) “No Source, No Answer” applies to map layers too ✅  
If a layer has **missing metadata**, **missing provenance**, **unknown license**, or **unknown sensitivity**, treat it as **not publishable / not renderable** by default (fail closed). [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) Fail closed on access 🛡️  
UI hooks must assume that access can be denied (or sanitized) per role + sensitivity classification; do not “guess” access. The API enforces RBAC + policy, and the UI should reflect those outcomes safely. [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) No “downstream loosening” of restrictions 🔒  
If upstream data is confidential/restricted or generalized/redacted, the UI must **not** present a less restricted view. Classification tags propagate, and any attempt to output a lower classification should be blocked or reviewed. [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 4) One map engine instance per viewer (unless explicitly designed otherwise) 🧱  
Map engines are imperative objects. Re‑initializing them on every render is a classic leak/perf trap. Hooks must manage lifecycle with `useEffect` + cleanup + `useRef`.

### 5) Hooks own side-effects; components own layout ✨  
- ✅ Hooks: create/destroy engine, add/remove layers, attach/detach listeners, fetch tiles/metadata.
- ✅ Components: DOM structure, panels, buttons, composing hooks.
- ❌ Components should not contain deep engine manipulation.

---

## 🧭 Dataflow (how everything stays in sync)

```mermaid
flowchart LR
  Store[(Global Store\nviewport • currentYear • activeLayers • selection)] -->|selectors| Hooks[Map Hooks\n(web/src/hooks/map)]
  Hooks --> Engine[Map Engine\nMapLibre 2D / Cesium 3D]
  Engine -->|events: move, click, hover| Hooks
  Hooks -->|dispatch actions| Store

  Catalog[(Catalog\nSTAC/DCAT + sensitivity + license + PROV)] --> Hooks
  Policy[(Policy decisions\nRBAC/OPA + sanitization)] --> Hooks
```

**Key sync example:** timeline → `currentYear` updates → map filters data by year. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗺️ Map stack snapshot (what hooks must support)

### 2D: MapLibre GL JS  
MapLibre is the primary interactive 2D engine. KFM adds:
- **Tile layers** (raster + vector tiles for large datasets)
- **GeoJSON overlays** (for smaller payloads) [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3D: CesiumJS  
Cesium provides 3D globe/terrain mode with a UI toggle between 2D/3D in the viewer. [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Tiles & services (API side)
KFM supports tile endpoints such as:
- `/tiles/{layer}/{z}/{x}/{y}.pbf` (vector tiles)
- `/tiles/{layer}/{z}/{x}/{y}.png` (raster tiles)
- `/wms` (WMS service) [oai_citation:13‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](sediment://file_00000000ebac71f7ba1281d629a3ff9b)

### Standards & catalog alignment
KFM’s architecture emphasizes interoperability through OGC services (WMS/WFS/WCS), common download formats, and catalog standards including STAC/DCAT. [oai_citation:14‡Kansas Frontier Matrix (KFM) – Unified Technical Blueprint.pdf](sediment://file_0000000000d8722f9ee56b2c59e5a887)

---

## 🧩 Hook taxonomy (recommended organization)

> You don’t need all of these today — but if you add hooks, aim to fit them into one of these buckets.

### 🧱 Engine hooks
Own the lifecycle of map engines and the container ref.

**Responsibilities**
- Create/destroy MapLibre/Cesium instances
- “Mode switch” 2D ⇄ 3D
- Bind core listeners (move, zoom, click)
- Expose a stable “engine handle” object for other hooks

**Recommended contract**
- Always return `{ status, error, engine, containerRef }`
- Never throw in render; surface errors via state

---

### 🗂️ Layer hooks
Translate “active layer set” into engine operations.

**Responsibilities**
- Add/remove sources & layers idempotently
- Apply paint/layout styles
- Update filters when `currentYear` changes (time slicing) [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Maintain legend entries + symbology metadata (for LayerControl)

**Design note:** KFM expects multiple visible layers and a layer control/legend UI. [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

### 🖱️ Interaction hooks
Keep selection and hover behavior consistent across engines.

**Responsibilities**
- Feature picking (click → popup / details panel)
- Hover highlighting and cursor state
- Lasso/box selection (if used)
- Emit selection to store + clear on context changes

---

### 🧭 Viewport hooks
Synchronize camera state (center, zoom, bearing, pitch) with global store.

**Responsibilities**
- Debounce high‑frequency map move events
- Persist viewport (optionally) for back/forward nav
- Normalize “view state” across 2D/3D

---

### 🛡️ Governance + provenance hooks
Make “what the user sees” policy-aware and auditable.

**Responsibilities**
- Interpret dataset sensitivity, access decisions, redaction flags
- Block/disable layers that are not viewable (fail closed) [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Surface provenance and license info for “map behind the map” (UI affordance)

**Why:** KFM enforces RBAC + OPA decisions per request and dataset sensitivity classification. [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧾 Contract-first types (TypeScript sketch)

> These are **recommended** types for predictability and composability (adjust to match the repo’s actual types).

```ts
export type MapMode = "2d" | "3d";

export type LayerKind =
  | "vector-tile"   // .pbf (MVT)
  | "raster-tile"   // .png/.jpg
  | "geojson"       // small overlays
  | "wms";          // OGC service

export type Sensitivity = "public" | "internal" | "confidential" | "restricted";

export type HookStatus = "idle" | "initializing" | "ready" | "error";

export interface LayerSpec {
  id: string;
  title: string;
  kind: LayerKind;
  source: { url: string; layerName?: string };
  sensitivity?: Sensitivity;      // required for publishable layers (fail closed if absent)
  licenseId?: string;             // required for publishable layers
  provId?: string;                // required for publishable layers
  timeField?: string;             // optional: for currentYear filtering
}

export interface MapEngineHandle {
  mode: MapMode;
  // engine-specific references are allowed but keep them behind an abstraction boundary:
  maplibre?: unknown;
  cesium?: unknown;
}
```

**Governance grounding:** missing provenance metadata blocks publication; provenance logging is mandatory. [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧪 Usage pattern (component stays clean)

> Example uses placeholder hook names — adopt the pattern even if the exports differ.

```tsx
import { useMapEngine } from "./useMapEngine";
import { useMapLayers } from "./useMapLayers";
import { useMapInteractions } from "./useMapInteractions";
import { useMapViewportSync } from "./useMapViewportSync";

export function MapViewer() {
  const { containerRef, engine, status, error } = useMapEngine({ initialMode: "2d" });

  useMapLayers(engine, /* activeLayers from store */);
  useMapInteractions(engine, /* selection/hover handlers */);
  useMapViewportSync(engine, /* viewport from store */);

  if (status === "error") return <div role="alert">Map failed: {String(error)}</div>;

  return <div ref={containerRef} className="MapCanvas" />;
}
```

**Why this structure fits KFM:** the global store keeps disparate components in sync and supports structured updates (actions/reducers) and time-travel debugging. [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ➕ Adding a new map layer (checklist that won’t get you burned) 🔥

### ✅ Step 0 — Decide how it should be served
- Large/zoomable: use **vector tiles** (`.pbf`) or **raster tiles** (`.png`) [oai_citation:21‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](sediment://file_00000000ebac71f7ba1281d629a3ff9b)
- Small/simple: **GeoJSON overlay** is fine [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> Reminder from cartography practice: making effective maps often requires multiple tools and transformations — don’t assume a single step gets you “publication quality.” [oai_citation:23‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_000000002d2471fdb19e238af41b3408)

### ✅ Step 1 — Metadata is mandatory (fail closed)
For a layer to be publishable/renderable, ensure it has:
- **License**
- **Sensitivity classification**
- **Provenance (PROV record)**
If missing: it should not proceed / should not be shown. [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:25‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### ✅ Step 2 — Respect CARE + Indigenous data sovereignty
When data is Indigenous/sensitive:
- Align with **CARE principles** (Collective Benefit, Authority to Control, Responsibility, Ethics) alongside FAIR. [oai_citation:26‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)
- Enforce “authority to control” via access policy + group ownership; hide/aggregate for others and support takedown/withdrawal behavior. [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ✅ Step 3 — UI implementation via hooks
- Add `LayerSpec` to the layer registry (or equivalent)
- Layer hook adds/removes it idempotently
- Legend/LayerControl uses `LayerSpec.title` + symbology metadata

### ✅ Step 4 — Time slicing (if applicable)
If the dataset is time-based:
- filter by `currentYear` or timeline range to keep story/map in sync [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### ✅ Step 5 — Verify policy outcomes
- If API returns **403** or “sanitized” response, UI must not attempt to reconstruct hidden details.
- Never display content less restricted than its input. [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ⚡ Performance & reliability notes (map hooks edition)

### 🧽 Always clean up
Map engines register listeners and keep WebGL resources alive. In hooks:
- Remove listeners in `useEffect` cleanup
- Remove layers/sources when unmounting or disabling
- Destroy engine on component unmount

### 🧯 Debounce viewport writes
Move events fire rapidly. Debounce before dispatching to store to avoid render loops.

### 🧠 Prefer tiles for big data
Vector tiles are “lightweight slices” for large layers (and enable styling on client). Raster tiles are appropriate for pre-rendered imagery. (Raster vs vector fundamentals in the mapping stack.) [oai_citation:30‡Scalable Data Management for Future Hardware.pdf](sediment://file_000000007d74722fa87beabc663630f7)

### 🧪 Treat StrictMode as a stress test
React StrictMode may double-invoke certain lifecycles in dev. Hooks must tolerate init/cleanup cycles without leaving zombie listeners.

---

## 🧷 Configuration touchpoints (common ones)

KFM deployment includes environment variables for base URLs and service wiring:
- `KFM_BASE_URL`
- `KFM_API_BASE_URL`
…and related runtime config fields (used so generated links and requests resolve correctly). [oai_citation:31‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔍 Debugging tips

- Use global store tooling (Redux time-travel style debugging is explicitly considered in KFM design) to see what state changes triggered map updates. [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- When a layer “doesn’t show,” check:
  1) Is it **enabled** in store?
  2) Does it have **license/sensitivity/provenance**?
  3) Did policy deny or sanitize access? [oai_citation:33‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
  4) Is the URL correct (base URL env vars)? [oai_citation:34‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📚 Sources used (project files)

> These are the internal project references that informed the contracts and guardrails in this README:

- KFM system governance, tiles, env vars, provenance rules:  [oai_citation:35‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:36‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:37‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- KFM web front-end + map stack (MapLibre/Cesium + store sync):  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
- Indigenous data governance & CARE framing:  [oai_citation:40‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  
- Map design practice reference:  [oai_citation:41‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)  
- Web/UI craft references (general practice):  [oai_citation:42‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)  [oai_citation:43‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  [oai_citation:44‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  

---

## 🗂️ (Optional) Suggested folder snapshot

> If you’re expanding this folder, aim for a layout like this (names are illustrative):

```text
📦 web/src/hooks/map
├── 📄 README.md
├── 🧱 useMapEngine.ts            # create/destroy + 2D/3D switching
├── 🗂️ useMapLayers.ts            # add/remove layers idempotently
├── 🧭 useMapViewportSync.ts      # store <-> map camera sync
├── 🖱️ useMapInteractions.ts      # click/hover/select behaviors
├── 🛡️ useLayerAccess.ts          # policy-aware gating (fail closed)
└── 🧾 useLayerProvenance.ts       # surface license/prov metadata for UI
```

---

### 🧾 Footnotes (evidence pointers)

- Map engines & 2D/3D behavior: MapLibre + Cesium described in KFM blueprint. [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Store-driven sync (timeline → map/story): KFM blueprint state-store description. [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Tile endpoints and WMS listing: KFM system documentation. [oai_citation:47‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](sediment://file_00000000ebac71f7ba1281d629a3ff9b)
- “No Source, No Answer” principle: KFM system documentation.
- Fail-closed governance + RBAC/OPA + sensitivity: KFM system documentation. [oai_citation:48‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- PROV required + provenance logging: KFM system documentation. [oai_citation:49‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- CARE principles framing: Indigenous Statistics reference. [oai_citation:50‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](sediment://file_00000000a58071f586f00793dee712d6)
- No downstream loosening: Master guide governance invariant. [oai_citation:51‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Cartographic note (multi-tool reality): map design guide excerpt. [oai_citation:52‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_000000002d2471fdb19e238af41b3408)
- Raster vs vector fundamentals: Mobile Mapping excerpt. [oai_citation:53‡Scalable Data Management for Future Hardware.pdf](sediment://file_000000007d74722fa87beabc663630f7)