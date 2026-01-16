# 🗺️ Map Adapter (`web/src/adapters/map`)

![Status](https://img.shields.io/badge/status-draft-orange)
![Layer](https://img.shields.io/badge/layer-web%20UI-blue)
![Pattern](https://img.shields.io/badge/pattern-adapter%20%2F%20port--adapter-7a3df0)
![Map](https://img.shields.io/badge/map-MapLibre%20%7C%20Leaflet%20%7C%20Cesium-0aa)

> A **thin, testable wrapper** around our mapping engine (primarily **MapLibre GL JS**) that exposes a **stable map API** to the rest of the React app — including **timeline / time-slice** behavior for historical eras. 🧭

---

## ✨ Why this folder exists

KFM’s map UI is designed to be *modular* and *swappable* (MapLibre today, potentially Leaflet/Cesium later). This adapter layer keeps map-engine details from spreading across components and lets us:

- ✅ Swap map engines without rewriting the UI
- ✅ Keep business/UI logic independent of MapLibre/Leaflet APIs
- ✅ Centralize time-enabled layer rules (slider/playback) ⏳
- ✅ Create mocks for unit tests (no WebGL in CI) 🧪
- ✅ Enforce KFM “API boundary” thinking (map renders what API provides; it does not become a data client) 🔒

---

## 🧠 What this adapter is responsible for

**In scope** ✅

- 🗺️ Map lifecycle: mount/unmount, resize, style load, cleanup
- 🎛️ Camera control: fit bounds, flyTo, set center/zoom/bearing/pitch
- 🧱 Layer/source orchestration: add/remove/update/visibility/opacity
- 🧩 Interaction plumbing: click/hover/select, feature query helpers
- ⏱️ Temporal controls: time cursor + time-slice layer toggling/filtering
- 🧾 Layer metadata hooks (provenance badge, license/source tooltip, etc.)

**Out of scope** ❌

- 🚫 Fetching business data (Neo4j, raw STAC crawling, etc.)
- 🚫 Deciding *what* layers should exist (that’s app state / API contracts)
- 🚫 Domain inference (“this county is relevant…”) — belongs upstream
- 🚫 Hardcoding datasets or bypassing governed endpoints

---

## 🗂️ Expected folder layout (recommended)

> This is the “shape” we aim for. The exact filenames may differ — keep the idea: **one contract**, **one engine implementation**, **one test mock**.

```text
📁 web/
  📁 src/
    📁 adapters/
      📁 map/
        📄 README.md
        📄 index.ts                # public exports
        📄 types.ts                # shared types / contracts
        📄 MapPort.ts              # the stable interface the app uses
        📁 engines/
          📁 maplibre/
            📄 MapLibreAdapter.ts
            📄 maplibreHelpers.ts
          📁 leaflet/              # optional (if/when used)
            📄 LeafletAdapter.ts
          📁 cesium/               # future (if/when used)
            📄 CesiumAdapter.ts
        📁 __mocks__/
          📄 MockMapAdapter.ts
        📁 __tests__/
          📄 map.port.test.ts
```

---

## 🧩 How it fits in the KFM web UI

```mermaid
flowchart LR
  UI[🧑‍💻 React components] -->|calls| Port[🧩 MapPort (stable contract)]
  Port --> Adapter[🗺️ Map Adapter (this folder)]
  Adapter --> Engine1[🧠 MapLibre GL JS]
  Adapter --> Engine2[🧠 Leaflet (optional)]
  Adapter --> Engine3[🌍 Cesium (future)]
  UI -->|loads layer configs + data via| API[(🔒 Governed API)]
```

**Rule of thumb:** If a React component imports `maplibre-gl` directly, we’re probably bypassing the adapter and should refactor. 🧯

---

## 🚀 Quick start (React)

> Pseudocode illustrating the intended usage pattern.

```ts
import { createMapAdapter } from "@/adapters/map";

export function MapView() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;

    const map = createMapAdapter({ engine: "maplibre" });

    let handle: Awaited<ReturnType<typeof map.mount>> | null = null;

    (async () => {
      handle = await map.mount(ref.current!, {
        styleUrl: "/styles/kfm-base.json",
        center: [-98.5, 38.5],
        zoom: 6,
      });

      // Example: register layers from app state (already vetted by API)
      handle.addLayer({
        id: "usgs_topo_1894",
        kind: "raster",
        source: {
          type: "raster-tiles",
          tiles: ["/tiles/usgs/topo/1894/{z}/{x}/{y}.png"],
        },
        temporal: { start: "1894-01-01", end: "1894-12-31" },
        opacity: 0.85,
      });

      // Hook UI time slider to adapter
      handle.setTimeCursor("1894-06-01");
    })();

    return () => {
      handle?.destroy();
    };
  }, []);

  return <div ref={ref} className="MapCanvas" />;
}
```

---

## 🧾 The contract: `MapPort` (stable API)

### Design goals 🎯
- **Small** surface area: only what the UI needs
- **Typed** and engine-agnostic
- **Deterministic** behaviors (e.g., layer id collisions, ordering rules)
- **Mockable** (tests should not need WebGL)

### Suggested minimal interface (example)

```ts
export type TimeCursor = string; // ISO date (preferred) or "YYYY"

export interface MapInitOptions {
  styleUrl: string;
  center: [number, number]; // [lng, lat]
  zoom: number;
  bearing?: number;
  pitch?: number;
}

export interface MapHandle {
  // lifecycle
  destroy(): void;
  resize(): void;

  // camera
  fitBounds(bounds: [[number, number], [number, number]], opts?: { padding?: number }): void;
  flyTo(view: { center?: [number, number]; zoom?: number; bearing?: number; pitch?: number }, opts?: { durationMs?: number }): void;

  // time
  setTimeCursor(t: TimeCursor): void;
  getTimeCursor(): TimeCursor;

  // layers
  addLayer(layer: MapLayerSpec): void;
  updateLayer(id: string, patch: Partial<MapLayerSpec>): void;
  removeLayer(id: string): void;
  setLayerVisibility(id: string, visible: boolean): void;

  // interaction
  on(evt: MapEventName, fn: (e: MapEvent) => void): () => void;
  queryFeatures(opts: QueryFeaturesOptions): MapFeature[];
}

export type MapLayerSpec =
  | RasterLayerSpec
  | VectorLayerSpec
  | GeoJsonLayerSpec;

export interface TemporalWindow {
  start: string; // ISO date
  end: string;   // ISO date
}

export interface BaseLayerSpec {
  id: string;
  title?: string;
  opacity?: number;
  visible?: boolean;

  // 🧠 KFM-friendly metadata
  provenance?: {
    source?: string;
    license?: string;
    attribution?: string;
    datasetId?: string; // stable ID from API/contracts
  };

  // ⏳ Time-aware layers
  temporal?: TemporalWindow;
}
```

> ⚠️ This README intentionally shows a **suggested contract**. The actual exported contract in this repo should be treated as the source of truth.

---

## ⏳ Timeline support: “time-slice” layers

KFM’s UI is meant to **move through historical eras** with a slider (or play button) that changes which layers are visible, and/or filters features within layers.

### Two common strategies

1) **Toggle whole layers** (best for raster tiles per year/era) 🧱  
   - Each layer has `temporal.start/end`
   - When `setTimeCursor()` changes, the adapter:
     - sets visibility on layers whose temporal window contains the cursor
     - optionally fades between adjacent layers (nice UX ✨)

2) **Filter features** (best for vector layers with feature timestamps) 🎚️  
   - Single layer with a timestamp property (e.g., `year`, `date`)
   - Adapter applies engine-native filters (MapLibre expressions / Leaflet plugin filters)

### Recommended behavior contract ✅
- If a layer has `temporal`, it participates in time filtering.
- If a layer is explicitly `visible: false`, time logic must not override it.
- Time filtering must be deterministic:
  - “inclusive start/end”
  - stable ordering rules when multiple layers match

---

## 🧱 Supported sources & formats (pragmatic)

This adapter should be able to render the most common KFM delivery formats:

- 🧊 **Vector tiles** (preferred for scale)  
- 🟧 **Raster tile layers** (historical scans, hillshade, overlays)
- 🟩 **GeoJSON** (small-to-medium feature sets; debugging; prototypes)
- 🧾 **COGs** (Cloud-Optimized GeoTIFF)  
  - typically served via tile endpoints
  - (optional) client-side loading only when same-origin and performance-safe

---

## 🖱️ Events & interaction model

### Must-have events
- `click` → feature inspect + “show linked docs” panel 📚
- `hover` → highlight + quick tooltip 🪄
- `moveend` → persist map view / update viewport queries 🧭

### Recommended event payload
- geographic coordinates (lng/lat)
- screen pixel coordinates
- matched features + layer ids
- optional “picked” feature id for stable selection state

---

## 🧪 Testing & mocks

### Unit tests (fast) ⚡
- Use `MockMapAdapter` that implements `MapPort` without WebGL
- Validate:
  - layer state transitions (add/update/remove)
  - time cursor behavior (which layers become visible)
  - event subscription/unsubscription logic

### Integration tests (slower) 🧪🧱
- Run a real engine (MapLibre) in a browser runner (Playwright/Cypress)
- Smoke tests:
  - map mounts
  - one raster layer renders
  - time slider toggles expected layers
  - click returns a feature

---

## ⚡ Performance notes & footguns

- 🧊 Prefer **vector tiles** for large datasets; GeoJSON can kill FPS fast.
- 🧱 Don’t spam `addLayer/removeLayer` every render — diff and patch.
- 🎛️ Debounce camera-driven queries (`move` vs `moveend`).
- 🧼 Always `destroy()` on unmount to avoid WebGL context leaks.
- 🧯 Keep engine objects behind the adapter; never expose raw `maplibre.Map`.

---

## 🤝 Contributing rules (for this folder)

### ✅ Do
- Add capability by **extending the contract first** (contract-first mindset 📜)
- Keep adapter code *thin* — coordinate transformations are ok; domain logic is not
- Update mocks + tests alongside changes 🧪
- Document new layer kinds and time behaviors in this README 📝

### ❌ Don’t
- Import MapLibre/Leaflet directly in UI components (unless explicitly approved)
- Make network calls to core data systems from the adapter (use API layer)
- Add “just one quick dataset” hardcoded in map code (it will rot)

---

## 🔗 Useful repo links (expected)

> These are referenced by KFM’s documentation standards and are typically the canonical places to learn “the rules of the road.”

- 📘 `docs/MASTER_GUIDE_v13.md` (pipeline + invariants)
- 🧱 `docs/architecture/` (overall system architecture)
- ⚖️ `docs/governance/` (ethics, sovereignty, review gates)
- 🧾 `schemas/` (contracts for UI/config/telemetry as they mature)

---

## ✅ Checklist (when you change map behavior)

- [ ] Updated the `MapPort` contract (or verified no contract change needed)
- [ ] Updated `MockMapAdapter` to match
- [ ] Added/updated tests for new behaviors
- [ ] Documented the change here (especially time filtering rules)
- [ ] Verified no direct engine imports leaked into UI components
- [ ] Confirmed data still flows through governed APIs (no shortcuts 🔒)

---

> 🧭 If you’re unsure whether something belongs here: **if it’s engine-specific → adapter; if it’s domain/story-specific → upstream**.
