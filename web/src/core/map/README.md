# 🗺️ Map Core (`web/src/core/map`)

![Module](https://img.shields.io/badge/module-map--core-0B7285?style=for-the-badge)
![Runtime](https://img.shields.io/badge/runtime-browser-3B82F6?style=for-the-badge)
![Render](https://img.shields.io/badge/render-2D%20%7C%203D-8B5CF6?style=for-the-badge)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%2F%20DCAT%20%2F%20PROV-16A34A?style=for-the-badge)
![A11y](https://img.shields.io/badge/a11y-WCAG%20%2B%20ARIA-F59E0B?style=for-the-badge)

> **One map, many truths — always with receipts 🧾**  
> This module is the **engine-agnostic mapping backbone** for Kansas Frontier Matrix (KFM): layers, time, provenance, interactions, and performance rules — without tying us to a single renderer.

---

## 🧭 Quick Links

- 📘 Platform guide: `../../../../docs/MASTER_GUIDE_v13.md`
- 🏛️ Architecture: `../../../../docs/ARCHITECTURE.md`
- 🧪 Data pipeline: `../../../../docs/PIPELINE.md`
- 🧾 Provenance standards: `../../../../docs/standards/` *(STAC/DCAT/PROV profiles)*
- 🔐 Security & privacy: `../../../../SECURITY.md` + `../../../../docs/governance/`

---

## ✨ Why this exists

KFM is a **historical + geospatial + documentary** exploration system. The map isn’t “just a basemap” — it’s the primary lens for:

- **Toggling layers by time period ⏳**
- **Inspecting features to see linked documents / AI insights 🔎**
- **Comparing change across eras (2D overlays + optional 3D terrain) 🧩**
- **Always surfacing dataset provenance (sources, citations, lineage) 🧾**

This folder exists to ensure we can build that experience **once** and plug it into different viewers (Map viewer, Story viewer, 4D/timeline viewer) **without duplicating logic**.

---

## ✅ Module responsibilities

| ✅ Owns | Examples | 🚫 Does *not* own |
|---|---|---|
| **Map state model** | view state, selection state, time window | React components / DOM layout |
| **Layer lifecycle** | register → load → show/hide → unload | Raw data ingestion / ETL |
| **Adapter contract** | MapLibre, Leaflet, Cesium bridges | Picking a single engine forever |
| **Provenance + attribution rules** | “every layer has receipts” | Writing STAC/DCAT/PROV files |
| **Interaction semantics** | click/hover/select/box-zoom rules | UI styling of panels & modals |
| **Performance guardrails** | caching, throttling, budgets | Backend query tuning (owned server-side) |
| **Redaction/safety constraints** | “can’t zoom past blur”, safe popup text | Auth policies and enforcement rules source |

---

## 🧱 Non‑negotiable invariants (the “map contract”)

### 🧾 Provenance-first
- Every visible layer must have a **stable `layerId`** and a **provenance reference** (STAC item / DCAT dataset / PROV lineage).
- The map must always display **attribution & source credits** (and expose them programmatically to UI).

### 🔌 UI is a view, not a database
- The UI must not contain “secret data.”  
  If it can’t be obtained from the **API** (and allowed for the user), it can’t render on the client.

### 🕵️ Privacy & sovereignty
- Redaction rules must be enforced in *behavior*, not just styling:
  - blur/aggregation **must not be bypassable** by zoom, tilt, pitch, or measurement tools.
  - feature inspection must never reveal coordinates that policy says must be protected.

### ♿ Accessibility-first
- All core interactions must be representable through **keyboard + screen reader compatible** affordances (even if the viewer chooses different UI chrome).

---

## 🧩 Core concepts

### 1) **MapController**
The orchestration brain. Owns:
- current view (center/zoom/bearing/pitch)
- active time window
- active layer set + layer states
- selection/highlight
- event emission

### 2) **LayerRegistry**
A typed registry of:
- layer definitions (what it is)
- sources (where it comes from)
- render rules (how it appears)
- provenance (why we can trust it)

### 3) **MapAdapter**
A small interface that isolates renderer specifics.

> 🧠 Design goal: **all map logic** talks to the adapter, never directly to MapLibre/Cesium APIs.

### 4) **TimeController**
Applies a time window to:
- layer visibility (era toggles)
- feature filtering (per‑feature time attributes)
- animation / scrubbing

### 5) **Inspection + Evidence**
Feature clicks yield a **HitResult** that includes:
- feature identity
- dataset provenance
- document links / citations
- optional “AI insight” pointers (from the reasoning layer)

---

## 🧩 Architecture (high-level)

```mermaid
flowchart LR
  UI[🖥️ Viewer UI (React)] -->|commands| MC[🧠 MapController]
  UI <-->|events| MC

  MC --> TC[⏳ TimeController]
  MC --> LR[📚 LayerRegistry]
  MC --> EV[🧾 Evidence / Provenance Model]

  MC --> AD[🔌 MapAdapter]
  AD --> ENG[🗺️ Map Engine<br/>MapLibre / Leaflet / Cesium]

  LR --> API[🔌 API Client]
  EV --> API
```

---

## 🗂️ Suggested folder layout

> ⚠️ This is the intended shape of the module. If the code differs, update this README to match reality.

```text
📁 web/src/core/map/
├── 📄 README.md
├── 📁 controller/
│   ├── 📄 MapController.ts
│   ├── 📄 TimeController.ts
│   └── 📄 types.ts
├── 📁 layers/
│   ├── 📄 LayerRegistry.ts
│   ├── 📄 layerTypes.ts
│   ├── 📁 builders/
│   └── 📁 filters/
├── 📁 adapters/
│   ├── 📁 maplibre/
│   ├── 📁 leaflet/
│   └── 📁 cesium/
├── 📁 interactions/
│   ├── 📄 picking.ts
│   ├── 📄 selection.ts
│   └── 📄 gestures.ts
├── 📁 provenance/
│   ├── 📄 ProvenanceRef.ts
│   ├── 📄 Attribution.ts
│   └── 📄 EvidenceBundle.ts
├── 📁 performance/
│   ├── 📄 tileBudget.ts
│   ├── 📄 throttling.ts
│   └── 📄 cache.ts
└── 📁 utils/
    ├── 📄 geo.ts
    └── 📄 projections.ts
```

---

## 🧾 Provenance & metadata model

KFM’s data catalog is **STAC-like** and KFM’s governance requires cross-linking:

- **STAC** for spatial/temporal items & assets  
- **DCAT** for dataset discovery & publishing metadata  
- **PROV** for lineage (how derived artifacts were made)

### Minimal layer descriptor (recommended)

```ts
export type LayerId = string;   // stable, globally unique
export type DatasetId = string; // stable, globally unique

export type ProvenanceRef = {
  stacItemId?: string;       // e.g. "stac:item:ks:historic_map_1856"
  dcatDatasetId?: string;    // e.g. "dcat:dataset:usgs:dem_10m"
  provActivityId?: string;   // e.g. "prov:activity:georef:2025-01-10"
  citations?: Array<{
    title: string;
    uri?: string;
    note?: string;
  }>;
};

export type LayerDescriptor = {
  id: LayerId;
  name: string;
  kind: "vector" | "raster" | "terrain" | "labels" | "3d";
  time?: { start?: string; end?: string };     // ISO strings
  bbox?: [number, number, number, number];     // WGS84
  source: {
    type: "geojson" | "mvt" | "wms" | "wmts" | "cog" | "tiles3d";
    url: string;
  };
  style?: Record<string, unknown>;             // renderer-specific style
  provenance: ProvenanceRef;
  policy?: {
    sensitivity?: "public" | "restricted" | "redacted";
    redactionMode?: "blur" | "aggregate" | "mask";
  };
};
```

### Attribution rules (cartography hygiene ✅)
For any active layer, the UI must be able to render:
- **data source credit**
- **license / usage notice** (when known)
- **date/time coverage**
- **processing notes** (when derived)

---

## ⏳ Time & narrative support

KFM includes a “map + timeline” story mode:
- time slider scrubs across eras
- layers enable/disable based on their temporal coverage
- “story nodes” can set the map to a known state (camera + layers + annotations)

### Story step → map state (suggested)

```ts
type StoryStep = {
  id: string;
  title?: string;
  time?: { start?: string; end?: string };
  view?: { center: [number, number]; zoom: number; bearing?: number; pitch?: number };
  layers?: { enable?: LayerId[]; disable?: LayerId[] };
  highlight?: { layerId: LayerId; featureId: string };
};
```

---

## 🎨 Cartography & UX requirements

### 🧭 Map essentials checklist
When shipping a new viewer or major map UX change:

- [ ] Title/context shown somewhere (even in “Focus Mode”) 🏷️  
- [ ] Legend available when symbology is non-trivial 🗂️  
- [ ] Scale bar (or clear distance indicator) 📏  
- [ ] North arrow/rotation indicator 🧭 *(especially if bearing/pitch enabled)*  
- [ ] Data source credits + license surfaced 🧾  
- [ ] Date/era context surfaced when time filter is active ⏳  

### 📱 Responsive + mobile expectations
- Mobile-first layouts are encouraged
- Touch affordances must not block map navigation
- Any “off-canvas” menus should remain keyboard accessible ♿

---

## ⚡ Performance guardrails

This is a **WebGL-heavy** surface area. Treat performance as a feature.

### Raster layers (COG & tiles)
- Prefer Cloud-Optimized GeoTIFF (COG) + server-side tile endpoints for very large rasters.
- Use HTTP range reads when supported, and avoid loading full rasters in-browser.

### Vector layers
- Prefer vector tiles (MVT) for large feature sets.
- Avoid huge GeoJSON payloads; if unavoidable, stream / chunk and simplify.

### Browser budgets (starter defaults)
- Keep interactive FPS stable during pan/zoom
- Avoid style recalculations on every pointer move
- Offload heavy parsing / transforms to Web Workers when possible

---

## 🔐 Security & safety notes

### Popups & side panels
- Never inject untrusted HTML from data sources.
- Sanitize strings and render “rich text” using a strict allowlist.

### Sensitive locations (policy)
- If a layer is marked `redacted`, the adapter must:
  - prevent high-precision coordinate readout
  - prevent precision recovery via measure tools / snapping / feature export
  - apply aggregation/blur consistently across interactions

---

## ✅ Testing strategy (recommended)

- **Unit tests**: layer registry, time filtering, provenance wiring  
- **Integration tests**: adapter contract & event emission  
- **Visual regression**: snapshot map states (fixed camera + deterministic tiles where possible)  
- **Accessibility**: keyboard navigation + screen reader smoke checks

---

## 🧰 Recipes

### Add a new layer type (example flow)
1. Add a new `kind` (if needed) to `layerTypes.ts`
2. Define `source.type` support (geojson / mvt / cog / etc.)
3. Implement builder: `layers/builders/<kind>.ts`
4. Ensure provenance requirements are met:
   - `LayerDescriptor.provenance` must be present
   - attribution must be derivable
5. Add time behavior:
   - layer-level time window gating
   - feature-level time filtering if applicable
6. Add tests and a minimal story step demo ✅

### Add a new renderer adapter
1. Implement `MapAdapter` interface:
   - create/destroy
   - add/remove sources
   - add/remove layers
   - set camera
   - query rendered features (for picking)
2. Ensure event translation is consistent:
   - click → feature hit
   - hover → highlight
   - move → view state updates
3. Validate redaction handling
4. Add a minimal “adapter conformance” test suite

---

## 🧭 Glossary

- **STAC**: SpatioTemporal Asset Catalog (items/assets with bbox + time + metadata)
- **DCAT**: Data Catalog Vocabulary (dataset discovery metadata)
- **PROV**: Provenance model (activities, entities, agents; lineage)
- **COG**: Cloud-Optimized GeoTIFF (optimized for HTTP range reads)
- **MVT**: Mapbox Vector Tiles (efficient vector tiling format)
- **HitResult**: the structured output of feature picking (id + dataset + evidence)

---

## 📚 References & project library

<details>
<summary>📦 Core KFM docs used to shape this module</summary>

- **KFM Technical Documentation** (architecture, pipeline, UI contract)
- **KFM Mapping Hub Design** (map + timeline UX, layer toggles, 2D/3D rendering goals)
- **MASTER_GUIDE_v13** (repo structure, invariants, governance expectations)

</details>

<details>
<summary>📚 Supporting references (design, performance, security, GIS)</summary>

- 🗺️ Cartography & map UX: *Making Maps*  
- 🧭 Mobile mapping & context: *Mobile Mapping: Space, Cartography and the Digital*  
- 🧱 WebGL fundamentals: *WebGL Programming Guide*  
- 🛰️ Remote sensing visualization: *Cloud-Based Remote Sensing with Google Earth Engine*  
- 🧬 GIS tooling patterns: *Python Geospatial Analysis Cookbook*  
- 🧮 Performance thinking: *Database Performance at Scale* + *Scalable Data Management for Future Hardware*  
- 🔐 Threat modeling mindset: *Ethical Hacking and Countermeasures* + security notes in the programming compendiums  
- 🧠 Reproducibility/rigor: *Scientific Modeling and Simulation* + statistics/experimental design references  
- 🧑‍⚖️ Governance & ethics: *Data Spaces* + *Digital Humanism* + AI governance papers

</details>

---

## 🧩 Maintainers

- 🧑‍💻 **Core owners:** KFM Web Core Team
- 🗂️ **Related modules:** `web/src/viewers/`, `web/src/core/catalog/`, `web/src/core/evidence/`

> If you change anything that affects the “map contract” (provenance, privacy, adapter interface), update this README **in the same PR** ✅

