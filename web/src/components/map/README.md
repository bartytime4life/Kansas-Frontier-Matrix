# 🗺️ Map Component (`web/src/components/map/`)

![React](https://img.shields.io/badge/React-SPA-61DAFB?logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-Typed%20UI-3178C6?logo=typescript&logoColor=white)
![Map](https://img.shields.io/badge/Maps-2D%20%2B%203D-2ea44f)
![Provenance](https://img.shields.io/badge/Provenance-First-6f42c1)
![Time](https://img.shields.io/badge/Time-Timeline%20Driven-orange)

> 🧭 **Purpose:** This folder contains the KFM map surface: a **2D map (MapLibre)** with an optional **3D globe (Cesium)**, plus layer control, feature selection, and **timeline/story-driven** navigation.

---

## 🧩 What Lives Here

This directory is meant to hold the “map system” as reusable UI building blocks:

- 🧠 **MapViewer / MapRoot**: orchestration layer (engine init + state sync + event plumbing)
- 🗂️ **LayerControl**: toggles, ordering, opacity, basemap selection, legend hooks
- 🕰️ **Timeline hooks**: time slider integration + time-filtering logic
- 🧾 **Feature UI**: hover/selection, popups, side panel details
- 🧰 **Utilities**: bbox helpers, style helpers, layer registry helpers

> [!IMPORTANT]
> ✅ **API Boundary Rule**: the map UI consumes **tiles/GeoJSON/etc. via the API** (not direct DB queries).  
> This keeps governance, auth, and provenance enforcement centralized.

---

## 🧠 Core Concepts (KFM-flavored)

### 1) “Map behind the map” 🧬
The UI should always make it easy to answer:
- **What am I looking at?**
- **Where did it come from?**
- **What time slice is this?**
- **What sources support it?**

### 2) Time is a first-class citizen ⏳
Most layers should support one (or more) of:
- **single year / range filtering**
- **time-enabled tiles**
- **time-enabled feature queries** (bbox + time)

### 3) The map is a *coordinator* 🤝
The map is not “just a renderer.” It mediates:
- layer state
- timeline state
- story/scrollytelling “camera moves”
- selection state and cross-component highlighting

---

## 🏗️ Architecture at a Glance

```mermaid
flowchart LR
  UI[🗺️ Map UI<br/>MapViewer + Controls] --> Store[🧠 Global State<br/>(viewport, time, layers, selection)]
  Store --> UI

  UI --> API[🌐 API Boundary]
  API --> Tiles[🧱 Tile Endpoints<br/>Vector/Raster]
  API --> Data[📦 Dataset Endpoints<br/>GeoJSON/CSV/...]
  API --> Graph[🕸️ Graph/Query<br/>GraphQL + safe queries]
```

---

## 🔌 Data Inputs the Map Commonly Consumes

> [!NOTE]
> The exact endpoints and formats depend on the layer type, but the map generally consumes **tiles**, **features**, and **metadata**.

### 🧱 Tiles
Typical patterns:
- **Vector tiles (MVT / PBF)** → for fast rendering + styling in the client
- **Raster tiles (PNG/WEBP)** → for imagery/historic scans/pre-rendered layers

### 🧩 Features (interactive)
Commonly GeoJSON (for click/hover/inspect) with:
- `bbox` filtering (viewport queries)
- optional `time` filters (timeline-driven queries)

### 🗃️ Metadata (for UI/legend/provenance)
- layer titles, descriptions, attribution
- source dataset ids
- temporal coverage
- styling/legend hints

---

## 🧾 Suggested Layer Registry Contract (UI “Contract Artifact”)

If you don’t already have one, this pattern keeps layers predictable and composable:

```ts
// ✅ Suggested shape — adjust to your actual implementation
export type MapMode = "2d" | "3d";
export type LayerKind = "vector-tile" | "raster-tile" | "geojson";

export interface LayerTimeConfig {
  /** Example: "year" | "start_year" etc */
  field?: string;
  /** Example: currentYear value from TimelineSlider */
  current?: number;
  /** Example: inclusive range for filtering */
  range?: { start: number; end: number };
}

export interface MapLayerDefinition {
  id: string;                 // stable + unique
  title: string;              // human-friendly
  kind: LayerKind;

  // Source wiring
  source: {
    /** Optional dataset id for catalog/provenance linking */
    datasetId?: string;

    /** Tile URL template or API route (server-side template) */
    tileUrl?: string;

    /** Feature endpoint for interactivity (GeoJSON) */
    dataUrl?: string;
  };

  // Behavior
  minZoom?: number;
  maxZoom?: number;
  clickable?: boolean;
  time?: LayerTimeConfig;

  // Styling hints (MapLibre-style-ish)
  style?: {
    beforeId?: string;        // layer ordering anchor
    paint?: Record<string, unknown>;
    layout?: Record<string, unknown>;
  };

  // UX / governance hooks
  legend?: {
    items: Array<{ label: string; sample: string }>;
  };
  attribution?: string;
}
```

> [!TIP]
> Keeping **layer definitions declarative** makes it easier to:
> - add/remove layers without touching core map code
> - build consistent legends + tooltips
> - enforce provenance links and temporal behavior

---

## 🧭 Minimal Usage Example (Conceptual)

```tsx
// Example usage — align names/exports to your codebase.
import { MapViewer } from "./components/map/MapViewer";

export function ExplorerPage() {
  return (
    <MapViewer
      mode="2d"
      initialView={{
        center: { lon: -98.0, lat: 38.5 },
        zoom: 6,
      }}
    />
  );
}
```

---

## 🔁 2D ↔ 3D Mode (Expected Behavior)

### 🗺️ 2D (MapLibre)
- initializes a map instance with a base style
- adds/removes sources and layers dynamically
- supports feature picking (click/hover) for interactive layers

### 🌍 3D (Cesium)
- mirrors the 2D viewport context when toggling (best effort)
- supports 3D camera moves triggered by Story Nodes
- uses imagery/terrain sources consistent with configured layers

> [!WARNING]
> Switching modes can be expensive. Avoid frequent re-creation of the 3D viewer; prefer **persist + toggle**.

---

## 🕰️ Timeline + Story Nodes Integration

### TimelineSlider ⏳
Typical responsibilities:
- exposes a `currentYear` (or `range`)
- updates global state (store)
- triggers layer filtering / tile swapping

### StoryPanel / Scrollytelling 📜
Expected behavior:
- story sections entering view trigger:
  - camera fly-to
  - time jump
  - layer toggles
  - focus/highlight of specific features

> [!TIP]
> Keep story-driven transitions **purely state-driven** (store updates), and let the map react to state changes.
> This makes story playback reproducible + testable.

---

## ⚡ Performance Playbook

- 🧊 **Prefer tiles** for dense datasets (vector tiles over huge GeoJSON)
- 🪄 **Throttle/debounce** viewport-driven fetches
- 🧱 Keep a **stable layer ordering** to avoid re-style churn
- 🧠 Cache:
  - layer metadata
  - last viewport query results
  - parsed GeoJSON for selected features
- 🧪 Use feature queries sparingly:
  - only for *interactive* layers
  - limit results (server-side if possible)

---

## ♿ Accessibility + UX Guardrails

- ⌨️ Ensure controls are keyboard navigable (LayerControl, TimelineSlider, StoryPanel)
- 🟦 Maintain visible focus rings and logical tab order
- 🎨 Use colorblind-safe palettes for categorical layers
- 🧘 Respect reduced motion (`prefers-reduced-motion`) for fly-to animations
- 🧾 Provide text equivalents for:
  - legend meaning
  - selected feature details

---

## ➕ Adding a New Map Layer (Checklist ✅)

1. 📦 **Confirm the dataset is registered** (catalog + provenance) and available through the API
2. 🧱 Choose a delivery mode:
   - tiles for performance (recommended for dense layers)
   - GeoJSON endpoint for interactivity / small layers
3. 🗂️ Add a `MapLayerDefinition` entry (id/title/source/time/legend)
4. 🎨 Add styling (MapLibre paint/layout rules, or raster settings)
5. 🧪 Validate:
   - appears at expected zoom levels
   - toggles correctly
   - legend matches styling
   - time filtering behaves correctly
6. 🖱️ If interactive:
   - click/hover returns stable feature ids
   - selection UI shows provenance + key fields
7. 📸 Add screenshots/gifs (optional but helpful)

---

## 🧪 Testing Ideas

- ✅ **Unit tests**
  - layer registry shape validation
  - time-filtering logic
  - selection reducer/store logic
- ✅ **Integration tests**
  - toggling layers updates engine state
  - switching 2D/3D preserves viewport
- ✅ **Manual QA**
  - “blank map” handling
  - slow network behavior
  - mobile responsive controls

---

## 🩹 Troubleshooting

### Blank map 🕳️
- Is the base style reachable?
- Are tiles returning 200s?
- Is the API base URL configured correctly?

### Layers toggle but don’t render 👻
- zoom level out of range (`minZoom/maxZoom`)
- wrong `beforeId` ordering anchor
- source URL template mismatch

### Clicking features doesn’t work 🖱️
- layer not marked `clickable`
- feature picking querying the wrong layer ids
- layer rendered behind a non-interactive fill layer

---

## 🧭 Recommended Folder Layout (Optional)

> [!NOTE]
> This is a suggested structure if you’re still evolving the map module.

```text
🗂️ web/src/components/map/
├─ 📝 README.md
├─ 🗺️ MapViewer.tsx
├─ 🧱 engines/
│  ├─ maplibre/
│  └─ cesium/
├─ 🗂️ layers/
│  ├─ registry.ts
│  ├─ styles.ts
│  └─ legends.ts
├─ 🧠 state/
│  ├─ slice.ts
│  └─ selectors.ts
├─ 🧰 utils/
│  ├─ bbox.ts
│  ├─ geo.ts
│  └─ ids.ts
└─ 🎛️ ui/
   ├─ LayerControl.tsx
   ├─ TimelineBridge.tsx
   └─ FeaturePopup.tsx
```

---

## 🔗 Related Project Areas

- 📁 `api/` → the enforcement boundary for tiles/features/metadata
- 📁 `docs/` → standards + architecture + governance
- 📁 `pipelines/` → produces governed artifacts that eventually become layers
- 📁 `data/` → raw/processed/canonical artifacts (depending on repo conventions)

---

## ✅ Definition of Done (Map Changes)

- [ ] Layer(s) render correctly in 2D
- [ ] If relevant, layer(s) render correctly in 3D
- [ ] Legend + attribution are correct
- [ ] Time behavior is correct (if time-enabled)
- [ ] Selection/hover behavior is correct (if interactive)
- [ ] No direct DB calls from UI (API boundary respected)
- [ ] Basic QA notes/screenshot added to PR