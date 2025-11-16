---
title: "🗺️ Kansas Frontier Matrix — MapLibre Integration Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/maplibre/README.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/maplibre-guide-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "web-maplibre-integration"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed"
sensitivity_level: "Varies by layer"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — MapLibre Integration Guide**
`docs/guides/maplibre/README.md`

**Purpose**  
Define the **official MapLibre GL JS integration standard** for the Kansas Frontier Matrix (KFM) web platform  
and pipeline system.  
This guide governs **frontend map rendering**, **layer orchestration**, **CARE v2 governance overlays**,  
**temporal synchronization**, **STAC asset visualization**, and **MapLibre-specific telemetry hooks**.

This document applies to:
- Web platform (`web/src/components/MapView/`)
- Map pipelines (geospatial preprocessing, mask generation)
- Focus Mode v2 spatial cues
- Story Node v3 spatial previews
- STAC/DCAT map rendering flows

</div>

---

# 📘 Overview

MapLibre is the **primary spatial visualization engine** of KFM (2D mode).  
It integrates with:

- KFM **STAC layer registry**  
- KFM **temporal engine** (TimelineView)  
- CARE v2 governance overlays (masking, sovereignty warnings)  
- Focus Mode v2 entity-highlighting  
- Story Node v3 footprints  
- Dataset previews (COG overlays, vector footprints)  
- KFM Telemetry v2 system  
- Neo4j spatial query surfaces (optional)

This guide defines:
1. Canonical file structure  
2. Layer orchestration model  
3. MapLibre governance integration  
4. Timeline & Focus sync  
5. STAC → MapLibre conversion rules  
6. Telemetry & lineage hooks  
7. Performance & WCAG requirements

---

# 🗂️ Directory Layout (Authoritative)

~~~text
web/src/components/MapView/
├── MapViewContainer.tsx          # Entry point; orchestrates all sublayers
├── MapCanvas.tsx                 # Low-level MapLibre map instance
├── LayerManager.tsx              # Registers layers & sources
├── LegendPanel.tsx               # Legend UI with governance info
├── MapControls.tsx               # Zoom, basemap, layer toggles
├── StoryNodeLayer.tsx            # Story Node v3 footprints
├── FocusHighlightLayer.tsx       # Focus Mode v2 spatial highlighting
├── DatasetFootprintLayer.tsx     # STAC footprints (COG/Vector)
├── SovereigntyMaskLayer.tsx      # H3/BBOX governance overlays
└── CursorHUD.tsx                 # On-map HUD (coords, value cursor)
~~~

Governance & masking primitives live under:

~~~text
web/src/components/MapView/primitives/
~~~

---

# 🧱 MapLibre Architecture (GitHub-Safe Mermaid)

```mermaid
flowchart TD

A["MapCanvas<br/>MapLibre instance"] --> B["LayerManager<br/>sources · layers · ordering"]
B --> C["FocusHighlightLayer<br/>entity focus"]
B --> D["StoryNodeLayer<br/>v3 footprints"]
B --> E["DatasetFootprintLayer<br/>STAC footprints"]
B --> F["SovereigntyMaskLayer<br/>CARE v2 masking"]
A --> G["MapControls<br/>zoom · basemap · toggles"]
A --> H["LegendPanel<br/>metadata · governance"]
A --> I["CursorHUD<br/>coords · pixel readout"]
````

---

# 1️⃣ MapCanvas (Base Engine)

`MapCanvas.tsx` handles:

* MapLibre initialization
* Style loading + basemap selection
* Initial camera position/state
* Integration with React lifecycle
* Error boundaries + telemetry

Required features:

* `preserveDrawingBuffer: true` for Focus Mode screenshots
* WCAG-compliant color profiles
* GPU resource cleanup on unmount
* Sanity fallback if WebGL fails

---

# 2️⃣ LayerManager (Orchestration)

`LayerManager.tsx` is responsible for:

* Defining **sources** (raster, vector, geojson)
* Defining **layers** (fills, lines, symbols, rasters)
* Establishing **draw order**
* Watching React/Context state:

  * TimeContext → filter geometries
  * FocusContext → highlight entities
  * GovernanceContext → masking
  * STAC selections → load footprints

KFM Layer Registration Pattern:

```ts
registerLayer({
  id: "storynode-layer",
  source: "storynode-src",
  type: "fill",
  paint: {
    "fill-color": "#6a5acd",
    "fill-opacity": 0.25
  }
})
```

---

# 3️⃣ CARE v2 Governance Overlays

`SovereigntyMaskLayer.tsx` implements governance masking using:

* H3 hex generalization
* Buffered bounding boxes
* Precision reduction
* “Remove geometry” fallback for restricted sites

Examples:

* Burial sites → centroid-only
* Tribal land boundaries → H3 R7
* Cultural sites → H3 R5
* Critical ecology → reduced precision

Governance metadata is visualized via **LegendPanel** with:

* careLabel
* maskingStrategy
* sovereigntyFlags[]
* AOI overlay toggles

Publishing is **blocked** if masking is bypassed.

---

# 4️⃣ STAC → MapLibre Integration

STAC assets may include:

* COG rasters
* GeoJSON footprints
* VectorTiles
* 3-band or 4-band composites
* Cloud masks

STAC → MapLibre conversion follows these rules:

### Raster (COG)

* Loaded using `@mapbox/mapbox-gl-supported` + `maplibre-gl` raster source
* Uses STAC `assets.data.href` or COG URL
* Color ramps rendered client-side or via tile server

### Vector (GeoJSON)

* Loaded via `GeoJSONSource`
* Must include CRS conversion to EPSG:4326
* Uses entity-level governance metadata

### Footprints

* Drawn via fill/line layers
* Governed by CARE v2 masking

---

# 5️⃣ Timeline Synchronization

`MapView` must respond to temporal filters from:

* `TimeContext`
* TimelineView user interactions
* Story Node temporal ranges
* Focus Mode temporal summaries

Behavior:

* Layers filter features outside selected time window
* Opacity fades for near-window features
* Telemetry logs temporal scrubbing

---

# 6️⃣ Focus Mode v2 Integration

`FocusHighlightLayer.tsx` visualizes:

* Selected entity polygon
* Related Story Node footprints
* Highlight pulse/halo effect
* Soft glow + focus outline

When a user selects:

* Feature → FocusContext updated
* FocusPanel updates narrative
* MapView highlights geometry
* Timeline marks intervals
* STAC/DCAT previews filtered

Outputs include accessibility metadata:

* `<aria-label>` for selected geometry
* Descriptive narrative summaries

---

# 7️⃣ Story Node v3 Integration

`StoryNodeLayer.tsx` maps:

* Story Node footprints
* Place references
* Narrative anchor locations
* Entity relations

Requirements:

* Geometry generalized for sensitive historical locations (CARE v2)
* Temporal filtering
* Provenance chips in LegendPanel
* Layer toggles controlled via MapControls

---

# 8️⃣ Map Controls

`MapControls.tsx` includes:

* Zoom In/Out
* Basemap switcher (terrain/vector/colorblind-safe)
* Layer toggles
* Timeline “sync lock”
* Focus reset

All controls must be:

* Fully keyboard-navigable
* Screen-reader accessible
* WCAG AA contrast verified

---

# 9️⃣ Legend Panel

`LegendPanel.tsx` renders:

* Layer colors
* Symbol explanations
* Governance details
* CARE v2 notices
* Sovereignty warnings

Legend entries must include:

* color swatches
* pattern previews
* narration for screen readers
* STAC/metadata tooltips

---

# 🔟 Cursor HUD

`CursorHUD.tsx` displays:

* Mouse geographic coordinates
* Pixel value (if available)
* Feature name/ID on hover
* Governance notice if geometry is masked

---

# 1️⃣1️⃣ Telemetry v2 Integration

MapLibre components must emit telemetry:

* `map:init`
* `map:move`
* `map:zoom`
* `map:layer-toggle`
* `map:footprint-hover`
* `map:focus-entity`
* `map:mask-activated`
* `map:error`

Telemetry fields:

* timestamp
* duration
* entity id
* bounding box
* h3 index(es)
* sovereignty conflicts
* energy/CO₂ calculations (optional client-estimated)

---

# 1️⃣2️⃣ Performance Requirements

MapLibre rendering must:

* Avoid over-zoomed raster tiles
* Simplify polygons before render
* Debounce interactions to reduce CPU load
* Use `requestIdleCallback` for non-critical updates
* Drop large layers outside viewport
* Follow KFM FPS thresholds:

  * 55–60 FPS target
  * Never below 20 FPS for >500ms

---

# 1️⃣3️⃣ Accessibility Requirements (WCAG 2.1 AA)

* All map controls keyboard-accessible
* Focus rings visible
* Colorblind-safe palette available
* Alt-values for every legend symbol
* Screen-reader narration for selected geometry
* Reduced-motion mode disables animations
* High-contrast basemap mode

---

# 1️⃣4️⃣ Developer Checklist

* [ ] MapCanvas initializes with WCAG-safe palette
* [ ] LayerManager registers deterministic layer ordering
* [ ] CARE v2 masking enforced on all sensitive footprints
* [ ] SovereigntyMaskLayer operational with AOI overlays
* [ ] STAC footprints link to dataset browser
* [ ] Focus Mode v2 highlighting functional
* [ ] Story Node v3 footprints correct
* [ ] Telemetry v2 events firing
* [ ] CRS/geometry validated
* [ ] All CI workflows green

---

# 🕰 Version History

| Version | Date       | Summary                                                                                                                               |
| ------: | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Initial MapLibre integration guide for KFM v10.4.2; aligned with CARE v2, lineage v2, telemetry v2, STAC/DCAT mapping, Focus Mode v2. |

---

<div align="center">

**Kansas Frontier Matrix — MapLibre Integration Guide (v10.4.2)**
Spatial Integrity × CARE v2 × Provenance × Accessible Cartography
© 2025 Kansas Frontier Matrix — MIT License · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
