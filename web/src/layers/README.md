# 🗺️ `web/src/layers` — Map Layers Registry + Rendering Adapters

<p align="center">
  <img alt="Kansas Frontier Matrix - Layers" src="https://img.shields.io/badge/KFM-Layers%20System-2b6cb0?style=for-the-badge">
</p>

<p align="center">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-ready-3178C6?logo=typescript&logoColor=white">
  <img alt="React" src="https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=000">
  <img alt="MapLibre" src="https://img.shields.io/badge/MapLibre-2D%20Maps-1f2937">
  <img alt="Cesium" src="https://img.shields.io/badge/Cesium-3D%20Globe-111827">
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance-First-16a34a">
</p>

> [!IMPORTANT]
> **KFM’s core promise:** every visual layer is **traceable** to its original source (“the map behind the map”).  
> This folder is where the *web app* declares “what a layer is”, **how it’s rendered**, and **how it exposes provenance** in the UI. ✅

---

## 🎯 What this folder is for

This directory is the **front-end contract** for map layers used by the KFM web client:

- 🧩 **Layer definitions** (IDs, titles, grouping, default visibility)
- 🎨 **Rendering config** (MapLibre styles, Cesium primitives, symbology rules)
- 🧾 **Attribution + licensing** metadata (what must be displayed in the UI)
- 🧭 **Discoverability hooks** (tags, categories, search keywords)
- 🛡️ **Governance-awareness** (sensitivity flags, role gating, policy-driven visibility)
- 🧪 **Validation** (unique IDs, required metadata, safe defaults)

> [!NOTE]
> The UI **must not** “invent layers” at runtime by guessing. Layers are declared here so the app stays **predictable, reviewable, and governed**.

---

## 🚫 What does *not* belong here

- ❌ Direct database queries (PostGIS/Neo4j/etc.)  
- ❌ Hardcoded secrets, keys, or private endpoints  
- ❌ “Mystery layers” with no license / attribution / provenance  
- ❌ Huge embedded datasets (GeoJSON dumps, raster blobs, etc.)

> [!TIP]
> KFM follows a strict “truth path” (Raw → Processed → Catalog → DB → API → UI).  
> The web app consumes layers through the **governed API**, not by bypassing it.

---

## 🧠 Mental model: What is a “Layer” in KFM?

A KFM layer is a **renderable, queryable view** of a dataset that:

1. 📌 Has a stable identity (`layerId`)
2. 🗺️ Can be rendered (2D/3D)
3. 🧾 Carries attribution & license
4. 🧬 Is linked to provenance (catalog record, STAC/DCAT entry, processing lineage)
5. 🧯 Can be governed (access rules + sensitivity handling)

---

## 🧱 Layer types we support (conceptual)

| Type | Example Use | Render Target |
|------|-------------|--------------|
| 🧭 **Base / Reference** | counties, roads, hydrography | MapLibre |
| 🧷 **Vector Thematic** | land parcels, census choropleths | MapLibre |
| 🛰️ **Raster / Imagery** | COG tiles, NDVI, historical maps | MapLibre (raster) / Cesium (imagery) |
| 🧊 **3D / Terrain / Point Cloud** | LiDAR-derived terrain, 3D contexts | Cesium |
| 🧾 **Annotation / Story** | narrative pins, event footprints | MapLibre + UI overlays |
| 🤖 **AI-derived Outputs** | change detection, classification | MapLibre/Cesium (must include provenance) |

> [!WARNING]
> AI-derived layers are **first-class datasets** and must ship with the **same provenance & licensing discipline** as any other layer.

---

## 🔁 “Truth Path” (how a layer becomes visible)

```mermaid
flowchart LR
  A[Raw Sources 📥] --> B[ETL / Processing 🏭]
  B --> C[Catalog (STAC/DCAT) 🗂️]
  C --> D[Runtime Stores (PostGIS/Objects/Search/Graph) 🗃️]
  D --> E[Governed API (FastAPI + Policy) 🌐🛡️]
  E --> F[web/src/layers (Declared Layers) 🧩]
  F --> G[UI Renderers (MapLibre / Cesium) 🗺️🧊]
  G --> H[User clicks "Sources" → Provenance Panel 🧾🔎]
```

---

## 🧾 Layer Definition Contract (recommended shape)

Even if implementations vary, **every layer should be representable** with a single object that includes:

- ✅ **identity**
- ✅ **render config**
- ✅ **data endpoints**
- ✅ **provenance/attribution**
- ✅ **governance flags**

Example (TypeScript *pattern*; adapt to actual project types):

```ts
export type LayerKind =
  | "vector"
  | "vector-tile"
  | "raster-tile"
  | "image-overlay"
  | "terrain"
  | "cesium-3d"
  | "annotation";

export type LayerVisibility = "default-on" | "default-off" | "hidden";

export interface LayerProvenance {
  datasetId: string;              // catalog ID (stable)
  sourceName: string;             // agency/archive name
  license: string;                // SPDX or plain text (must be explicit)
  attribution: string;            // shown in UI
  lastVerified?: string;          // ISO date (optional, but encouraged)
  stacItemUrl?: string;           // optional reference
  dcatUrl?: string;               // optional reference
}

export interface LayerGovernance {
  sensitivity?: "public" | "restricted" | "sensitive";
  rolesAllowed?: string[];        // e.g. ["public"], ["researcher"], etc.
  piiRisk?: boolean;              // extra caution flag
  caresPrinciples?: boolean;      // CARE-aware handling (if applicable)
}

export interface LayerDefinition {
  id: string;                     // globally unique
  title: string;
  description?: string;
  kind: LayerKind;

  // grouping + UX
  category: "Base" | "Environment" | "History" | "Infrastructure" | "Demographics" | "AI";
  tags?: string[];
  visibility: LayerVisibility;
  minZoom?: number;
  maxZoom?: number;

  // render config
  maplibre?: unknown;             // MapLibre style snippet or builder config
  cesium?: unknown;               // Cesium imagery/3D config

  // data access (always via API gateway)
  endpoints?: {
    tiles?: string;               // XYZ/WMTS/PMTiles gateway URL
    query?: string;               // feature query endpoint
    metadata?: string;            // layer metadata endpoint
  };

  provenance: LayerProvenance;
  governance?: LayerGovernance;
}
```

> [!TIP]
> If you can’t express a new layer in this contract, it’s a sign the layer is missing:  
> **(a)** provenance, **(b)** clear rendering strategy, or **(c)** a governed endpoint.

---

## 🧩 Suggested folder layout

> This is a **recommended** organization to keep layers scalable as the catalog grows.

```text
web/src/layers/
├─ README.md 📘
├─ registry/ 🧩
│  ├─ index.ts            # exports the full layer registry
│  ├─ categories.ts       # shared categories + UI ordering
│  └─ validators.ts       # required fields, ID uniqueness, etc.
├─ definitions/ 📚
│  ├─ base/               # boundaries, roads, hydro
│  ├─ environment/        # landcover, drought, climate
│  ├─ history/            # treaties, land patents, historical maps
│  ├─ demographics/       # census snapshots, county stats
│  └─ ai/                 # AI-derived layers (with strict provenance)
├─ renderers/ 🎨
│  ├─ maplibre/           # style builders, symbol rules
│  └─ cesium/             # imagery/terrain adapters
└─ types/ 🧠
   └─ layer-types.ts      # LayerDefinition + shared enums
```

---

## ➕ Adding a new layer (checklist)

### 1) Confirm it exists in the “truth path” ✅
- [ ] Dataset is ingested/processed properly (or linked as authoritative external service)
- [ ] Catalog record exists (STAC/DCAT/metadata) and includes licensing
- [ ] API exposes a governed endpoint for tiles/query/metadata

### 2) Implement the layer definition 🧩
- [ ] Add a `LayerDefinition` with:
  - [ ] `id` (stable, unique, deterministic)
  - [ ] `title` + `description` (human-readable)
  - [ ] `category` + `tags` (search + UI grouping)
  - [ ] `visibility` defaults (safe + minimal surprise)
  - [ ] attribution + license ✅ (non-optional)

### 3) Add rendering 🗺️
- [ ] MapLibre style (vector/raster) or Cesium config (3D/terrain)
- [ ] Reasonable `minZoom/maxZoom` for performance
- [ ] Styling matches KFM visual language (don’t overwhelm base context)

### 4) Wire it into the registry 🔌
- [ ] Export it from the layer registry
- [ ] Ensure validators pass (unique IDs, required metadata)

### 5) Prove provenance in the UI 🧾
- [ ] “Sources” panel shows dataset name, license, attribution, and catalog link
- [ ] If restricted/sensitive: UI reflects gated access clearly (no silent failure)

---

## 🛡️ Governance + sensitivity rules (UI expectations)

- 🧾 **Attribution is mandatory.** If there’s no attribution/license, the layer should not ship.
- 🔒 **Restricted layers** must:
  - default to hidden for public users
  - show a friendly “why you can’t see this” message
- 🧭 **CARE/Indigenous-sensitive content** should be handled with extra caution:
  - avoid exposing precise coordinates if policy requires redaction
  - avoid casual summarization without citations/context

> [!IMPORTANT]
> Policy decisions belong to the backend policy layer, but the web UI must be **policy-aware** so users experience clear, auditable behavior.

---

## ⚡ Performance tips (practical)

- Prefer **vector tiles** (PBF) for large vector datasets 🚀
- Prefer **COGs/PMTiles** for rasters and cache aggressively 🧊
- Avoid rendering “everything at once”: use zoom thresholds + clustering
- Keep style expressions simple; precompute classes server-side when possible
- Measure layer cost:
  - initial load time
  - pan/zoom FPS impact
  - memory growth over time

---

## 🔗 Related docs in this repo (recommended reading)

- 🏗️ Architecture overview: `../../../docs/architecture/system_overview.md`
- 🤖 AI / Focus Mode design: `../../../docs/architecture/AI_SYSTEM_OVERVIEW.md`
- 🧠 Ollama integration: `../../../docs/architecture/ai/OLLAMA_INTEGRATION.md`
- 🏭 Pipelines: `../../../pipelines/README.md`

---

## 📚 Source material used to shape this module

- Kansas Frontier Matrix — Comprehensive System Documentation  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Node.js / web platform reference (server + web fundamentals)  [oai_citation:1‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- Web design & front-end structure reference  [oai_citation:2‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  

---

## ✅ Quick definition of success

A layer in KFM is “done” when:

- it renders correctly ✅  
- it performs well ✅  
- it has attribution + license ✅  
- it’s discoverable ✅  
- and a user can always click **Sources** and see “the map behind the map” 🧾🗺️  

---
