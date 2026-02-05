# 🗺️ MapLibre Renderer — `web/src/layers/renderers/maplibre/`

![Renderer](https://img.shields.io/badge/renderer-MapLibre%20GL%20JS-informational)
![UI](https://img.shields.io/badge/ui-React%20%2B%20TypeScript-blue)
![Data](https://img.shields.io/badge/data-vector%20tiles%20%7C%20raster%20tiles%20%7C%20GeoJSON-success)
![KFM](https://img.shields.io/badge/KFM-evidence--first%20mapping-9cf)

> 🎯 **Purpose:** This folder is the **MapLibre GL JS adapter** for KFM’s layer system: it converts *KFM layer definitions + app state* into **MapLibre sources/layers**, and keeps them in sync (visibility, opacity, filtering by time, and interaction hooks).

---

## 🔎 Quick navigation

- [What this renderer is responsible for](#-what-this-renderer-is-responsible-for)
- [How it fits the KFM “truth path”](#-how-it-fits-the-kfm-truth-path)
- [Supported data delivery modes](#-supported-data-delivery-modes)
- [Layer lifecycle contract](#-layer-lifecycle-contract)
- [Time slider & scrollytelling hooks](#-time-slider--scrollytelling-hooks)
- [Cartography & UX guardrails](#-cartography--ux-guardrails)
- [Testing & debugging](#-testing--debugging)
- [Contributing: adding new layer types](#-contributing-adding-new-layer-types)
- [Sources](#-sources)

---

## ✅ What this renderer is responsible for

### 🧠 Core responsibilities
- **Register sources** in MapLibre (vector tiles, raster tiles, GeoJSON overlays).
- **Add style layers** with consistent IDs, ordering, and paint/layout defaults.
- **Apply state-driven updates** (toggle visibility, adjust opacity, update filters for time slices).
- **Remove cleanly** (no orphan sources/layers, no duplicate IDs).
- **Emit interaction events** (click/hover/select) in a way that the UI can:
  - show feature details
  - show provenance & citations (“map behind the map”)
  - keep story + map synchronized

<!-- KFM uses MapLibre GL JS for 2D mapping and adds layers as tiles or GeoJSON; plus frontend is React+TS. -->
<!--  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->
<!--  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->

### 🚫 Non-goals (keep it clean)
- This folder should **not** fetch directly from databases or filesystems.
- This folder should **not** implement business rules about what the user is allowed to see.
- This folder should **not** become a dumping ground for UI components (keep UI in UI layers).

---

## 🧬 How it fits the KFM “truth path”

KFM’s architecture is explicitly designed so that **every map layer, chart, and AI answer is traceable back to original sources** (“the map behind the map”). The UI is part of a governed pipeline where data flows through a canonical sequence and **no component bypasses that path**.  
That means the MapLibre renderer should treat the API as its source of truth for:
- tile URLs
- dataset metadata (license, citation, temporal coverage)
- feature payloads and their provenance fields

<!-- “map behind the map” + evidence-first + provenance + societal trust -->
<!--  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->
<!-- “truth path” and UI can’t query DB directly; must go through governed API; provenance logging -->
<!--  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->

### 🧾 Practical implications for this folder
✅ Do:
- Accept **layer descriptors** (IDs, styling hints, source endpoints) that originate from the **catalog/API**.
- Attach “source metadata handles” (dataset IDs, citations, licenses) to layers so the UI can show them.

❌ Don’t:
- Hardcode DB table names, filesystem paths, or direct storage URLs.
- “Fix” provenance gaps in the renderer (renderer should surface gaps, not hide them).

---

## 📦 Supported data delivery modes

KFM’s mapping approach uses:
- **Vector tiles (MVT)** for large/complex datasets
- **Raster tiles** for imagery/elevation and other raster products
- **GeoJSON overlays** for smaller datasets that can be sent directly

<!-- MapLibre: tile layers (raster or vector tiles) for large datasets, GeoJSON overlays for smaller -->
<!--  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->

### 1) 🧩 Vector tiles (MVT / `.pbf`)
Typical API pattern:
- `GET /tiles/{layer}/{z}/{x}/{y}.pbf`

Used when:
- dataset is large
- styling is best expressed via MapLibre layers
- you want smooth pan/zoom and good performance

<!-- API serves vector tiles via /tiles/{layer}/{z}/{x}/{y}.pbf -->
<!--  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->

### 2) 🖼️ Raster tiles (`.png` / `.webp`)
Typical API pattern:
- `GET /tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)

Used when:
- it’s raster data (imagery, scanned map tiles, hillshade, etc.)
- you need opacity blending over the basemap

<!-- API serves raster tiles via /tiles/{layer}/{z}/{x}/{y}.png (or .webp) -->
<!--  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->

### 3) 🧷 GeoJSON overlays
Typical API pattern:
- `GET /api/v1/datasets/{id}/data?format=geojson&bbox=...`

Used when:
- dataset is small enough to ship to the browser
- you want simple overlays and fast iteration during prototyping

<!-- Dataset endpoint can stream features as GeoJSON with bbox filtering -->
<!--  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->

---

## 🔁 Layer lifecycle contract

> The single biggest source of MapLibre pain is **ID collisions + partial teardown**.  
> Treat MapLibre as a state machine: if you add it, you must be able to remove it.

### ✅ Recommended lifecycle shape (conceptual)

```ts
/**
 * Conceptual contract — the exact names/types may differ in code,
 * but this is the “shape” we want everywhere for predictability.
 */
export interface MaplibreLayerRenderer {
  mount(map: maplibregl.Map, ctx: RenderContext): void;
  update(map: maplibregl.Map, ctx: RenderContext, prev: RenderContext): void;
  unmount(map: maplibregl.Map): void;
}
```

### 🏷️ ID conventions (strongly recommended)
- **Source ID:** `${layerId}__src`
- **Style layer IDs:** `${layerId}__lyr__${role}`  
  Examples: `__fill`, `__line`, `__symbol`, `__circle`, `__raster`

This makes it easy to:
- ensure uniqueness
- implement deterministic ordering
- bulk-remove by prefix

---

## ⏳ Time slider & scrollytelling hooks

KFM’s front-end uses a **global state** that keeps map + story in sync. When the user changes the timeline, the global state updates `currentYear`, and the map should respond (e.g., filtering features or swapping which layers are visible).  
Additionally, story content can drive map changes as the user scrolls (“scrollytelling”), via scripts that define target map state (center, zoom, visible layers, timeline year, annotations).

<!-- currentYear updates in global store and map filters by year; story panel responds -->
<!--  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->
<!-- story JSON script can define mapState including layers/year/opacity and timeline -->
<!--  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->

### 🧭 Implementation strategies (pick per layer type)
- **Vector tiles:** apply a MapLibre filter expression keyed off `currentYear` (best when features include year attributes).
- **Raster tiles:** swap tile endpoints or toggle layer groups per era (best when rasters are pre-sliced by time).
- **GeoJSON:** refetch within bbox/time window (only when small + cached).

> ⚠️ Avoid refetch-on-every-tick for the slider. Prefer debouncing and/or discrete “stops” for heavy layers.

---

## 🎨 Cartography & UX guardrails

KFM’s UI explicitly aims for good cartographic practice: visual hierarchy, clarity, accessibility, and supporting context like legends/scales. The renderer is where those intentions become real.

<!-- KFM: map rendering follows cartographic design principles, color schemes for clarity/accessibility, legends/scales -->
<!--  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->

### 🧱 Visual hierarchy (figure/ground)
- Make primary thematic layers read clearly over the basemap.
- Keep reference layers subtle.
- Don’t overwhelm: prefer progressive disclosure via zoom thresholds.

<!-- Figure/ground and visual hierarchy concepts from map design guidance -->
<!--  [oai_citation:11‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) -->

### ♿ Accessibility
- Avoid “information only by color” whenever possible.
- Use line style, width, and symbol shape to reinforce meaning.
- Ensure labels remain readable against varied backgrounds (halo/opacity patterns).

### 🧾 Metadata & citation expectations
Digital mapping should treat metadata as first-class: identification, quality, spatial reference, **citation information**, and **temporal information** are all part of dependable geodata practice.

<!-- Metadata categories include citation info + temporal info -->
<!--  [oai_citation:12‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) -->

### ©️ Copyright & historical maps
When rendering scanned/historical map products, remember: maps themselves (as representations) can be copyrighted even if facts/data are not. Renderer + UI should make it easy to show the layer’s license/usage notes right next to the visualization.

<!-- Copyright notes: representation (line weights/colors/symbols) is copyrighted; assume copyrighted unless known otherwise -->
<!--  [oai_citation:13‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) -->

---

## 🧪 Testing & debugging

### 🧰 Debug checklist
- **Network tab:** confirm tiles are loading (watch for 401/403/404; watch for mixed content).
- **Style inspection:** dump the active style JSON and confirm your source IDs + layer IDs exist.
- **Ordering:** if something “disappears”, it may be rendered under a solid fill layer.
- **Teardown:** toggling a layer on/off repeatedly should not grow the style graph.

### ✅ Test ideas (pragmatic)
- **Unit tests:** given a layer descriptor, assert the computed source/layer definitions (pure functions).
- **Integration tests:** mount renderer into a real MapLibre instance and assert `getStyle()` includes expected IDs.
- **E2E tests:** Playwright screenshot tests for “golden map states” (with stable basemap + deterministic layers).

---

## 🧩 Contributing: adding new layer types

### 1) Define your layer descriptor (domain)
Ensure the layer has:
- stable `id`
- data access mode: `vectorTile | rasterTile | geojson`
- provenance handle: dataset/catalog identifier(s)
- styling intent: minimal but sufficient

### 2) Implement renderer (adapter)
- Add source (if missing)
- Add one or more style layers
- Wire updates (opacity/visibility/filter)
- Ensure clean unmount

### 3) Document it
Add a small “recipe” section here:
- what it renders
- expected source schema (properties you rely on)
- time behavior (how it responds to `currentYear`)
- how provenance is surfaced

---

## 📚 Sources

<details>
<summary>📌 Project docs used (grounding)</summary>

- KFM evidence-first + “map behind the map” + truth-path constraints  
  <!--  [oai_citation:14‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->
  <!--  [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->

- KFM front-end MapLibre usage patterns (tiles vs GeoJSON) + timeline state sync  
  <!--  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->
  <!--  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) -->

- KFM API tile endpoint shapes + dataset GeoJSON access example  
  <!--  [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->
  <!--  [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) -->

- Cartographic metadata/citation + copyright considerations  
  <!--  [oai_citation:20‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) -->
  <!--  [oai_citation:21‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) -->

</details>

---

### 🧾 Maintainers’ note
If you’re here because a layer “won’t show up”, start with:
1) source exists, 2) layer exists, 3) layer order, 4) filter/time, 5) opacity/visibility, 6) teardown duplicates.

Happy mapping 🌾🧭