<!--
File: web/src/components/map/layers/README.md
Purpose: Developer guide for adding & maintaining KFM map layers (2D / MapLibre-first).
-->

# 🗺️ KFM Map Layers (`web/src/components/map/layers/`)

![status](https://img.shields.io/badge/status-draft-yellow)
![scope](https://img.shields.io/badge/scope-frontend%20map%20layers-blue)
![engine](https://img.shields.io/badge/engine-MapLibre%20GL%20JS-2b7)
![governance](https://img.shields.io/badge/governance-provenance--first%20%2B%20policy--aware-purple)

This folder houses **front-end layer definitions** and **layer wiring** for KFM’s interactive maps—primarily **MapLibre GL JS (2D)**, with patterns that can be extended to 3D/Cesium where needed.

A “layer” in the UI is usually a **bundle**: *one data source* (vector tile / raster tile / GeoJSON) + *multiple MapLibre style layers* (fill/line/symbol/etc.) + *metadata* (title, provenance hooks, sensitivity class, etc.).

---

## 🔒 Non‑negotiables (KFM rules that affect this folder)

> [!IMPORTANT]
> **Trust membrane:** the UI must not bypass governance. Avoid direct connections to DB/object stores; prefer governed API endpoints and policy-checked URLs.

- **No direct DB access from the browser.** All data access must be mediated through governed APIs (policy + validation + audit).  
- **Policy-aware rendering:** some datasets may require redaction/generalization, or role-based access. The layer implementation must **not** “work around” these constraints.
- **Evidence-first UX:** layers should be traceable (dataset/version/provenance links) wherever possible—especially when used by Focus Mode or Story Mode.

---

## 🧠 Mental model: “Logical layer” vs “Style layers”

### Logical layer (what users toggle)
Example: **Historic Trails**.

### Style layers (what MapLibre renders)
A single “Historic Trails” logical layer might expand into:

- `historic_trails-line` (line)
- `historic_trails-label` (symbol)
- `historic_trails-hover` (line highlight)

MapLibre layer definitions follow the **style spec `layers` model** (`id`, `type`, `source`, optional `source-layer`). ✅

---

## 🧩 Where layers sit in the UI architecture

```mermaid
flowchart LR
  User[User actions<br/>Layer toggle, story step, timeline] --> UI[LayerControl / StoryPanel / Timeline]
  UI --> Store[(Global state<br/>activeLayers, time, viewport)]
  Store --> Registry[Layer registry + adapters<br/>this folder]
  Registry --> Map[MapViewer (MapLibre Map instance)]
  Map -->|tiles/styles/data| API[/Governed API endpoints<br/>e.g. /api/v1/tiles/* or /api/tiles/*/]
  Map -->|feature pick| Interactions[queryRenderedFeatures<br/>popups/inspect]
```

---

## 📁 Folder layout (expected pattern)

> [!NOTE]
> The exact files in this folder may evolve. This is the **recommended** organization to keep layers composable, testable, and governance-aware.

```text
web/src/components/map/layers/
├─ README.md                 # you are here
├─ registry.ts               # central list/order of logical layers (recommended)
├─ types.ts                  # shared TS types: KfmLayerBundle, sensitivity, etc. (recommended)
├─ basemap/                  # basemap style helpers (optional)
├─ overlays/                 # domain layers (optional)
│  ├─ land/
│  ├─ hazards/
│  ├─ environment/
│  └─ history/
└─ utils/                    # MapLibre helpers: ensureSource/ensureLayer/order (optional)
```

---

## 🧾 Layer contract (recommended)

> [!TIP]
> Keep **layer definitions declarative**. Put imperative logic in `utils/` (add/remove/update) and call it from `MapViewer`.

```ts
// types.ts (recommended)
export type SensitivityClass =
  | "public"
  | "restricted"
  | "sensitive-location"
  | "aggregate-only";

export type LayerKind = "vector-tiles" | "raster-tiles" | "geojson" | "pmtiles";

export interface KfmLayerBundle {
  /** Stable UI key (used by toggles, story steps, and tests) */
  id: string;

  /** What the user sees */
  title: string;
  description?: string;

  /** Linkable governance anchors */
  datasetId?: string;     // e.g., kfm.history.trails.historic_trails (recommended naming)
  version?: string;       // dataset version or artifact version (if available)
  sensitivity?: SensitivityClass;

  /** Rendering */
  kind: LayerKind;

  /**
   * One or more MapLibre sources.
   * Keys are local identifiers; values are MapLibre source definitions.
   */
  sources: Record<string, any>;

  /**
   * One or more MapLibre style layers.
   * Each layer must reference a source defined above.
   */
  styleLayers: any[];

  /** Legend metadata (optional but recommended) */
  legend?: {
    swatches?: Array<{ label: string; examplePaint: Record<string, unknown> }>;
    notes?: string[];
  };

  /** Interaction layer IDs to query for click/hover (optional) */
  interactiveLayerIds?: string[];

  /** Suggested min/max zoom to protect performance */
  minzoom?: number;
  maxzoom?: number;
}
```

---

## ➕ Adding a new layer: checklist + thin-slice workflow

### 1) Pick the delivery shape (GeoJSON vs tiles)

- **GeoJSON overlay**: good for small data you can fetch once and render.
- **Vector tiles (MVT)**: preferred for large, national-scale, or high-feature-count layers.
- **PMTiles**: great for “serverless” distribution and offline-friendly basemaps/layers (range requests).

> [!WARNING]
> If the dataset is large, default to tiles first. Rendering huge GeoJSON will become a UX/perf problem fast.

---

### 2) Confirm governance + sensitivity class

KFM treats some data as sensitive (e.g., ownership/PII, precise archaeology/sensitive species locations, small-count health/crime). **Sensitivity class must be known** before enabling a layer in the public UI.

Recommended sensitivity classes:

- `public`
- `restricted` (role-based access)
- `sensitive-location` (coordinates generalized/suppressed)
- `aggregate-only` (only above thresholds)

---

### 3) Implement the layer bundle module

Create a new file (example path):

```text
web/src/components/map/layers/overlays/history/historicTrails.ts
```

Implement `KfmLayerBundle` with:

- **Stable IDs** for:
  - logical layer bundle `id`
  - each MapLibre style layer `id`
- a **governed URL**:
  - tiles: `/api/v1/tiles/{layer}/{z}/{x}/{y}` (preferred), or older style `/api/tiles/...`
  - GeoJSON: `/api/v1/datasets/{id}/...` (preferred; shape depends on API contract)
- dataset hooks:
  - `datasetId`, `version`, `sensitivity` (when available)

---

### 4) Register it in the registry (recommended)

```ts
// registry.ts (recommended)
import { historicTrails } from "./overlays/history/historicTrails";

export const KFM_LAYERS = [
  // basemap(s) first
  // overlays next (ordered by typical cartographic priority)
  historicTrails,
] as const;
```

Also decide:

- default visibility
- ordering (before/after key layers)
- story-driven enablement (if story steps control layers)

---

### 5) Wire UI controls + legend

- Add the layer to **LayerControl** toggles
- Provide legend/notes
- Add “ⓘ provenance” affordance (recommended):
  - link to dataset detail + evidence bundle when available

---

### 6) Add tests (minimum)

**Unit / component tests** (recommended):

- registry contains the layer
- IDs are stable and unique
- bundle validates (sources referenced by layers, etc.)

**E2E tests** (recommended, esp. for story-driven layers):

- toggling shows/hides the layer
- clicking a feature yields expected popup behavior
- if restricted, verify it is denied/hidden in unauthorized roles

---

## 🖱️ Interaction patterns (click/hover/inspect)

### “Click to inspect feature”
MapLibre supports feature hit-testing via rendered feature queries. Recommended pattern:

- define `interactiveLayerIds` in the bundle
- MapViewer registers a shared click handler:
  - `map.queryRenderedFeatures(point, { layers: interactiveLayerIds })`
- show a popup / side panel with:
  - human-friendly fields
  - link to dataset/provenance (when available)

> [!TIP]
> Keep interaction logic in MapViewer (or a shared hook), not inside each layer module. Layers should only declare *which* style layers are interactive.

---

## 🧱 PMTiles pattern (optional, great for basemaps)

PMTiles can be integrated with MapLibre using `addProtocol('pmtiles', ...)`.

**Recommended:**
- register the protocol **once** at app startup (or MapViewer init)
- keep a shared `PMTiles` instance in memory
- reference `pmtiles://...` URLs in style sources

---

## ⚡ Performance checklist (MapLibre)

Use these knobs before blaming React:

- Prefer **vector tiles** for high-volume features
- Use **clustering** for dense point layers
- Constrain `minzoom`/`maxzoom` for heavy layers
- Avoid expensive styling (many overlapping symbols, heavy outlines, etc.)
- Use MapLibre debug toggles when diagnosing:
  - tile boundaries, collision boxes, overdraw inspector (for GPU overdraw symptoms)

> [!NOTE]
> If you see “it works but becomes janky at zoom 10+”, it’s often an overlap/collision or data volume issue, not React.

---

## 🧯 Troubleshooting

### Layer doesn’t appear
- Source URL reachable? (check network panel)
- For vector tiles:
  - correct `source-layer` name?
  - layer `minzoom`/`maxzoom` filtering it out?
- Is the layer added **after** the style loads?
- Is there a filter that excludes features at the current timeline year?

### Works locally, fails in production
- CORS settings on tile/PMTiles host
- API gateway auth/policy returning 403/404
- wrong base URL env var

### Click doesn’t return features
- ensure you query the correct layer IDs
- ensure the layer is rendered (not just present)
- ensure the clicked feature is not under another layer capturing interaction

---

## ✅ Definition of Done (adding a new layer)

- [ ] Logical layer has a stable `id` and user-facing `title`
- [ ] All MapLibre style layer IDs are stable and unique
- [ ] Uses **governed API endpoints** (no direct DB access; no bypassing policy)
- [ ] Sensitivity class declared: `public | restricted | sensitive-location | aggregate-only`
- [ ] If not `public`, confirm:
  - [ ] backend returns redacted/generalized geometry as required
  - [ ] layer is hidden/denied appropriately for unauthorized roles
- [ ] Legend entry exists (or rationale documented)
- [ ] Interaction behavior documented (if clickable)
- [ ] Tests added (unit + at least one E2E path for critical layers)

---

## 🔗 References (engineering)

- MapLibre Style Spec (layers model): https://maplibre.org/maplibre-style-spec/
- MapLibre GL JS API: https://maplibre.org/maplibre-gl-js/docs/API/
- PMTiles: https://docs.protomaps.com/pmtiles/
- Martin tile server (MapLibre-first tile stack): https://maplibre.org/martin/

> [!NOTE]
> For KFM architecture/governance context, see repo architecture docs (e.g., `docs/architecture/system_overview.md`) if present.