---
title: "🗺️ Kansas Frontier Matrix — Map & Layer Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/map/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-map-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-map-utilities"
fair_category: "F1-A1-I1-R1"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map & Layer Utilities**  
`web/src/utils/map/README.md`

**Purpose:**  
Describe the **MapLibre-focused utility modules** used to render, style, and synchronize geospatial layers  
in the KFM React client — including **STAC/DCAT → MapLibre transforms**, **layer styling tokens**, **bbox  
and fit-to-view operations**, and **feature selection logic** used by Focus Mode v2 and the timeline.

</div>

---

## 🧭 Overview

The `web/src/utils/map/` module provides **pure, side-effect-free helpers** that sit between:

- STAC/DCAT/graph metadata and MapLibre’s runtime style, and  
- Knowledge graph entities (Places, Events, Story Nodes) and on-screen features.

These utilities ensure that:

- All map layers are **deterministic**, **typed**, and **reusable**  
- Layer creation & updates are **declarative** (no ad-hoc style mutations)  
- Bboxes and viewports are computed consistently for **timeline & Focus Mode**  
- FAIR+CARE metadata (source, license, sensitivity flags) is preserved and attachable to the UI  

No module in `utils/map/` directly talks to the network or DOM. They operate only on JS/TS data structures.

---

## 📂 Directory Layout

Expected layout for this module:

```

web/src/utils/map/
│
├── stacToMaplibre.ts      # STAC Item → MapLibre source/layer definitions
├── layerStyles.ts         # Shared style tokens (colors, opacities, zoom thresholds)
├── bboxUtils.ts           # Bbox ops (merge, pad, fit-to-view helpers)
├── featureSelectors.ts    # Feature selection and filtering by ID / properties
├── interactions.ts        # Hit-testing helpers wired into MapLibre events
└── legends.ts             # Legend/value mapping helpers for categorical/continuous layers

````

---

## 🧱 Module Descriptions

### 🧩 `stacToMaplibre.ts`

**Goal:** Convert STAC Items/Collections into **MapLibre-ready** source + layer configs.

Typical responsibilities:

- Map a STAC Item’s `assets` → MapLibre `source` definitions (raster, vector, geojson)
- Respect `bbox`, `geometry`, `proj` extension data, and media type
- Attach KFM-specific metadata (e.g., CARE labels, layer category, timeline range)

Example (conceptual):

```ts
interface MapLayerDescriptor {
  id: string;
  source: maplibregl.AnySourceData;
  layers: maplibregl.LayerSpecification[];
  temporal?: { start: string; end?: string };
  faircare?: { license: string; sensitivity?: "public" | "restricted" };
}

function stacItemToMapLayer(item: StacItem): MapLayerDescriptor { /* ... */ }
````

This function is the main bridge from **data catalog (STAC/DCAT)** to **runtime map**.

---

### 🎨 `layerStyles.ts`

Centralizes KFM’s **map style tokens**, so the visual language is consistent:

* Color palettes for historical vs. modern layers
* Opacity and blending rules for overlay maps (e.g., historic topo over DEM)
* Category → color mappings for treaty types, land use, hazards, etc.
* Min/max zoom for different layer types

Example patterns:

```ts
export const treatyBoundaryStyle = {
  lineColor: "#ffcc00",
  lineWidth: 2,
  lineDashArray: [2, 2]
};

export const focusHighlightStyle = {
  lineColor: "#ff2d55",
  lineWidth: 3
};
```

All map components use these tokens instead of hard-coded styles.

---

### 📦 `bboxUtils.ts`

Helpers for working with bounding boxes:

* Merge multiple bboxes into a single extent
* Pad bboxes by % for better framing
* Convert between `[west, south, east, north]` arrays and typed structs
* Compute “best fit” for mixed precision (single points vs. large polygons)

Example (conceptual):

```ts
fitViewportToBboxes(
  map: maplibregl.Map,
  bboxes: [number, number, number, number][],
  options?: { padding?: number }
): void;
```

Used heavily by:

* Focus Mode v2 to fit all relevant locations
* Timeline navigation to pan/zoom when selecting an era or Story Node
* “Zoom to layer” actions in the legend and layer browser

---

### 🎯 `featureSelectors.ts`

Given a MapLibre source + feature set, these helpers:

* Select features by **stable IDs** (e.g., graph `placeId`, `eventId`)
* Filter features by property predicates (e.g., `feature.properties.year <= 1870`)
* Map selections back to **knowledge graph IDs** for Focus Mode

Typical patterns:

```ts
selectFeaturesByIds(
  geojson: GeoJSON.FeatureCollection,
  ids: string[],
  idProperty: string = "id"
): GeoJSON.Feature[];

filterFeaturesByTime(
  geojson: GeoJSON.FeatureCollection,
  startYear: number,
  endYear: number
): GeoJSON.Feature[];
```

These functions are leveraged by:

* Hover/click interactions
* “Show only relevant features for this Focus Mode context”
* Story Node card highlights on the map

---

### 🖱️ `interactions.ts`

Pure helpers to **interpret** MapLibre event payloads and return stable, typed data:

* Convert `map.on('click', ...)` event → `{ featureId, layerId, coords }`
* Resolve which logical entity was clicked (Place, Event, Story Node span, etc.)
* Provide fallbacks for overlapping features (e.g., prioritize focus-highlight layers)

These functions separate **event mechanics** from **domain logic**, simplifying React components.

---

### 🧷 `legends.ts`

Legend utilities that compute:

* Category→label→color mappings (e.g., treaty categories, land-use classes)
* Gradient stops for continuous layers (e.g., elevation, drought index)
* Legend metadata from STAC Items (e.g., `raster:bands`, units)

Outputs are used by the web UI’s legend components to keep the map + legend in sync.

---

## 🧪 Testing Requirements

All `utils/map` modules must be covered by unit tests under:

```
tests/web/utils/map/*.test.ts
```

Tests MUST verify:

* Deterministic transforms from STAC → MapLibre descriptors
* Stable bbox operations across edge cases (antimeridian, tiny extents, mixed features)
* Correct feature selection and time-filtering semantics
* No side effects on global MapLibre state (functions operate on data only)
* Preservation of FAIR+CARE metadata (license, provenance flags) when round-tripping layer descriptors

Where possible, tests should use **small synthetic fixtures** (mock STAC Items, GeoJSON feature collections).

---

## ⚙️ Development Standards

All `web/src/utils/map/` modules MUST:

* Be implemented in **TypeScript**
* Export **typed, pure functions** only (no classes, no side effects)
* Avoid direct use of `document`, `window` (MapLibre `Map` instances may be passed as arguments, but not created here)
* Be linted with ESLint + Prettier
* Include complete JSDoc docstrings (parameters, return types, error conditions)
* Follow KFM’s **color/contrast** and **accessibility** guidelines when defining styles
* Respect CARE tags on sensitive geometries (e.g., avoid exposing coordinates for restricted sites in helper defaults)

---

## 🧭 Future Extensions (v10.5+)

Planned improvements for `utils/map`:

* Helper for **3D terrain integration** (DEM extrusion, hillshade blending)
* Vector tile layer generator from large GeoJSON features (client-side tiling helpers)
* Time-animated layer construction (for “playable” historical sequences)
* Multi-graph federation visual hints (showing cross-region links with different stroke patterns)
* Support for **Story Node “spacetime” geometry** conveniences (direct mapping of Story Node schema into layers)

---

## 🏁 Version History

| Version | Date       | Changes                                         |
| ------- | ---------- | ----------------------------------------------- |
| v10.4.1 | 2025-11-15 | Initial creation under KFM-MDP v10.4 standards. |

---
