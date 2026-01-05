# 🗺️ Layers (web/src/features/layers)

![Feature](https://img.shields.io/badge/feature-layers-2563eb)
![Subsystem](https://img.shields.io/badge/subsystem-UI%20(web)-16a34a)
![Map](https://img.shields.io/badge/map-MapLibre-0ea5e9)
![State](https://img.shields.io/badge/state-Redux-764abc)

> [!NOTE]
> This feature owns the **Layer Registry** (what layers exist + their metadata) and the **Layer State** (what the user has enabled, opacity/order, etc.).  
> The *map renderer* lives elsewhere (e.g. `web/src/features/map/`) and **consumes** this feature via selectors/hooks.

---

## 🧭 Quick links

- [✨ Responsibilities](#-responsibilities)
- [🧠 Mental model](#-mental-model)
- [🧱 Non-negotiables](#-non-negotiables)
- [📁 Suggested folder structure](#-suggested-folder-structure)
- [📦 Layer definition contract](#-layer-definition-contract)
- [🧰 Public API](#-public-api)
- [➕ Adding a new layer](#-adding-a-new-layer)
- [⏱️ Temporal layers + timeline integration](#️-temporal-layers--timeline-integration)
- [🔐 Governance](#-governance)
- [🚀 Performance notes](#-performance-notes)
- [🧪 Testing + validation](#-testing--validation)
- [🧯 Troubleshooting](#-troubleshooting)
- [🔗 Related](#-related)

---

## ✨ Responsibilities

This feature should be the **single source of truth** for:

- ✅ **Registry** of available layers (ids, labels, types, temporal coverage, styles, provenance)
- ✅ **User state** for layers:
  - visibility (on/off)
  - opacity
  - stacking order
  - per-layer settings (where applicable)
- ✅ **Layer UI** building blocks (layer list, toggles, legends, info popovers)
- ✅ **Mapping-library adapters** (turn `LayerDefinition` → MapLibre sources/layers)
- ✅ **Policy hooks** (classification/redaction UI behaviors, provenance display affordances)

Non-goals (keep elsewhere):

- ❌ Map initialization / lifecycle (belongs to `map` feature)
- ❌ Timeline slider widget itself (belongs to `timeline` feature)
- ❌ Data pipeline / catalog generation (belongs to `src/pipelines/` + `data/*`)
- ❌ Direct database/graph access (never from UI)

---

## 🧠 Mental model

Think of “layers” as two halves:

1) **Static definition (registry)** 🧾  
   “What is this layer, where does it come from, how is it styled, what time does it cover?”

2) **Runtime state (user selections)** 🎛️  
   “Is it enabled right now? What opacity? Where in the stack? What date/time?”

### 🔁 Flow (high-level)

```mermaid
flowchart LR
  A[📦 Registry: LayerDefinition[]] --> B[🧠 Redux: layer state]
  C[⏱️ Timeline state: currentDate] --> B
  B --> D[🪝 Selectors/hooks: active layers]
  D --> E[🗺️ Map feature renders via adapter]
  A --> F[🧾 Provenance/Legend UI]
```

---

## 🧱 Non-negotiables

> [!IMPORTANT]
> These rules come from the KFM v13 pipeline/contract approach and apply to **every** layer we ship.

- **API boundary rule** 🚧  
  The UI must never query the graph/database directly. All layer data must come through the governed API layer (`src/server/`) or stable published artifacts it exposes.
- **Provenance-first** 🧬  
  A layer must be traceable back to cataloged sources (STAC/DCAT/PROV). If it’s not registered, it shouldn’t be in the registry.
- **Classification propagation** 🔒  
  No layer output can be *less restricted* than its inputs. UI must implement safeguards (e.g., generalization/blur/zoom clamps) when required.
- **Open/Closed mindset** 🧩  
  Adding a layer should usually be “add config + (maybe) add a new adapter class,” not “edit core layer manager logic.”

---

## 📁 Suggested folder structure

> [!TIP]
> Your folder may not match this *exactly* yet — treat this as the target organization for a clean, feature-based UI.

```text
📦 web/src/features/layers/
├─ 📄 README.md                     # you are here 🙂
├─ 📄 layerRegistry.ts              # all LayerDefinition entries (or loader for them)
├─ 📄 layerTypes.ts                 # LayerDefinition + related types
├─ 📄 layersSlice.ts                # Redux slice (visibility, opacity, order, etc.)
├─ 📄 selectors.ts                  # selectVisibleLayers, selectLayerById, ...
├─ 📄 hooks.ts                      # useLayers(), useActiveLayers(), useLayer(id), ...
├─ 📁 adapters/                     # MapLibre (and future) rendering adapters
│  ├─ 📄 maplibreAdapter.ts
│  ├─ 📄 styleBuilders.ts
│  └─ 📄 index.ts
├─ 📁 components/                   # Layer UI widgets
│  ├─ 📄 LayerList.tsx
│  ├─ 📄 LayerToggleRow.tsx
│  ├─ 📄 LayerLegend.tsx
│  ├─ 📄 LayerInfoPopover.tsx
│  └─ 📄 index.ts
└─ 📁 __tests__/                    # unit + integration tests for this feature
   ├─ 📄 layersSlice.test.ts
   └─ 📄 selectors.test.ts
```

---

## 📦 Layer definition contract

> [!NOTE]
> The *exact* schema is up to this repo, but the goal is consistent: **every layer is declarative, self-describing, and provenance-linked**.

### ✅ What a `LayerDefinition` should capture

- **Identity**
  - `id` (stable)
  - `title` + `description`
  - `group` (for sidebar grouping)
- **Type**
  - raster (tiles/COG-derived tiles)
  - vector (GeoJSON / vector tiles)
  - annotations / AI artifacts (still treated as evidence artifacts)
- **Data source**
  - API endpoint(s) or published asset URLs
  - optional `availableDates` endpoint for temporal layers
- **Temporal**
  - none / continuous / discrete steps
  - available range or list of dates
- **Style**
  - paint/layout defaults
  - legend spec
- **Provenance**
  - references into STAC/DCAT/PROV (ids/links)
- **Governance**
  - classification tag(s)
  - redaction rules / maximum zoom / generalization requirements

### Example (TypeScript-ish)

```ts
export type LayerKind = "vector" | "raster" | "annotation";

export interface LayerProvenanceRef {
  stacItemId?: string;
  stacCollectionId?: string;
  dcatDatasetId?: string;
  provBundleId?: string;
}

export interface LayerTemporalSpec {
  mode: "none" | "continuous" | "discrete";
  // For discrete layers, prefer an API that returns available timestamps.
  availableDatesEndpoint?: string;
  start?: string; // ISO date
  end?: string;   // ISO date
}

export interface LayerDefinition {
  id: string;
  title: string;
  description?: string;

  kind: LayerKind;
  group?: string; // "Basemaps", "Boundaries", "Treaties", etc.

  source: {
    type: "geojson" | "vector-tiles" | "raster-tiles";
    // Keep URLs/paths API-centric (never DB-centric).
    url: string;
    // Optional template params (e.g., {time})
    urlTemplate?: string;
  };

  temporal?: LayerTemporalSpec;

  defaultOpacity?: number;
  defaultVisible?: boolean;

  legend?: {
    title?: string;
    items: Array<{ label: string; symbol?: string; color?: string }>;
  };

  provenance: LayerProvenanceRef;

  classification?: "public" | "restricted" | "sensitive";
  safeguards?: {
    maxZoom?: number;
    blurAtZoomOrAbove?: number;
    generalizeGeometry?: boolean;
  };
}
```

---

## 🧰 Public API

> [!TIP]
> The rest of the UI should import *from this feature* instead of re-implementing layer logic.

Typical exports:

- **Registry**
  - `getLayerRegistry()` / `layerRegistry`
  - `getLayerDefinition(id)`
- **State**
  - `layersReducer`
  - `layersActions` (`toggleLayer`, `setOpacity`, `setOrder`, …)
  - selectors (`selectActiveLayerIds`, `selectActiveLayers`, …)
- **Hooks**
  - `useLayers()`, `useLayer(id)`, `useActiveLayers(currentDate)`
- **UI components**
  - `<LayerList />`, `<LayerLegend />`, `<LayerInfoPopover />`
- **Adapters**
  - `toMapLibreSourcesAndLayers(activeLayers, currentDate)`

---

## ➕ Adding a new layer

> [!IMPORTANT]
> “Add a layer” in KFM means **add evidence** + **add provenance** + **expose through governed API** + **register in UI**.

### ✅ Checklist

1) **Data exists & is publishable** 📦  
   Confirm the dataset (or evidence artifact) is produced into `data/processed/...` and has the required metadata records (STAC/DCAT/PROV).

2) **API exposure** 🚪  
   Provide an API endpoint (tiles, GeoJSON, vector tiles, or query endpoint) that the UI can call.  
   - If the layer is sensitive, ensure the API enforces redaction/classification.

3) **Register the layer** 🧾  
   Add a new `LayerDefinition` entry in `layerRegistry.ts` (or wherever registry lives).

4) **Legend + provenance** 🧬  
   Include a legend spec and provenance references (STAC/DCAT/PROV ids or links).

5) **Sidebar grouping** 🗂️  
   Add it to the correct UI group (and consider mutual exclusivity rules if needed).

6) **Tests** 🧪  
   - reducer: toggle/opacity/order behavior
   - selector: active layer list is correct for current date
   - adapter: builds correct MapLibre source/layer configs

7) **Validation pass** ✅  
   Run UI checks (lint/test/build) and verify:
   - it renders
   - time slider integration works (if temporal)
   - provenance is visible somewhere in UI (info/legend/popup)

### “Config-first” pattern (preferred)

> [!NOTE]
> Most new layers should be added by **configuration only**. Create new adapter logic only if the layer introduces a new source type or rendering strategy.

---

## ⏱️ Temporal layers + timeline integration

Temporal layers should react to a global `currentDate` (or similar) state.

### What happens when the timeline changes?

- Timeline slider dispatches an action updating `currentDate`
- Layers feature selectors compute the **active** set of layers for that date
- Map adapter updates:
  - time parameter in tile URL, *or*
  - filter expression for vector layers, *or*
  - picks the closest discrete timestamp from `availableDates`

### Recommended patterns

- **Discrete layers** 🧷  
  Use `availableDatesEndpoint` and snap to the nearest valid timestamp.
- **Continuous layers** 🌊  
  Use a time param (e.g. `?time=YYYY-MM-DD`) and let the server handle slicing.
- **Animation** ▶️  
  Keep animation logic in `timeline`, but provide helpers here:
  - `getNextTimeStep(layerId, currentDate)`
  - optional prefetch for adjacent steps (careful with bandwidth)

---

## 🔐 Governance

> [!WARNING]
> A “pretty map layer” can still be a compliance breach if it leaks sensitive info.

### Required UI behaviors (examples)

- Show **classification badges** on layer rows (e.g. `🔒 restricted`)
- Enforce **UI safeguards** if declared:
  - clamp max zoom
  - blur/generalize at high zoom
  - hide raw coordinates in tooltips/popups when forbidden
- Always provide **provenance access**:
  - Layer info panel should include source references (STAC/DCAT/PROV)
  - Popups should link back to evidence, not just display claims

---

## 🚀 Performance notes

- Keep layer ids **stable** (MapLibre uses ids as keys)
- Prefer **vector tiles** over huge GeoJSON blobs
- Memoize selectors/hook outputs to avoid map churn
- Consider code-splitting heavy rendering modes (e.g., optional 3D)

---

## 🧪 Testing + validation

### Unit tests

- reducer logic: toggle/opacity/order
- selectors: active layers by date + classification behavior

### Integration tests

- adapter output matches expectations (sources/layers created correctly)
- timeline change triggers correct adapter updates

### Manual validation checklist

- ✅ Layer toggles appear in sidebar
- ✅ Toggle on/off updates map without full reload
- ✅ Opacity/order controls behave
- ✅ Temporal layers change with the timeline slider
- ✅ Provenance is visible (layer info / legend / popup)
- ✅ Sensitive layers respect safeguards

---

## 🧯 Troubleshooting

### “Layer toggle does nothing”
- Confirm the layer is **registered** and the id matches adapter output
- Confirm map adapter is consuming **selectors/hooks** from this feature (not duplicating state)

### “Layer is enabled but invisible”
- Check opacity is not 0
- Check the layer’s spatial coverage intersects the current viewport
- For temporal layers, confirm `currentDate` is within range / snapped to available dates

### “Temporal layer flickers or reloads too much”
- Ensure adapter updates are incremental (update source params/filter rather than rebuilding style)
- Add caching/prefetch for adjacent time steps if needed (careful with scale)

### “Sensitive data appears at high zoom”
- Add/verify safeguards in `LayerDefinition`
- Confirm API is also enforcing redaction (UI is not a security boundary)

---

## 🔗 Related

- 🗺️ Map renderer: `web/src/features/map/`
- ⏱️ Timeline: `web/src/features/timeline/`
- 🌐 API clients: `web/src/services/` (or equivalent)
- 📜 System contracts & pipeline rules:
  - `docs/MASTER_GUIDE_v13.md`
  - `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
  - `docs/standards/` (STAC/DCAT/PROV profiles)

---

### 🧾 Glossary

- **STAC**: metadata for spatial assets (collections/items)
- **DCAT**: dataset catalog/discovery metadata
- **PROV**: lineage/provenance metadata (how a dataset was produced)
- **Registry**: declarative list of available layers
- **Adapter**: mapping-library specific renderer builder (MapLibre sources/layers)