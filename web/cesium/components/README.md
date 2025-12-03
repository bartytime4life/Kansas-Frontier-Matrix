---
title: "🧩 KFM v11.2.3 — Cesium Web Components Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed React/TypeScript components wrapping CesiumJS for the Kansas Frontier Matrix web stack, including globe, timeline scenes, region overlays, and debug tooling."
path: "web/cesium/components/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 component-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-components-v11-2-3"
semantic_document_id: "kfm-web-cesium-components-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:components:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-cesium-components"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Cesium Web Components Library**  
`web/cesium/components/README.md`

**Purpose:**  
Define the **governed React/TypeScript component layer** that wraps **CesiumJS** for KFM:  
globes, timeline scenes, region overlays, and debug utilities that are provenance- and CARE-aware.

</div>

---

## 📘 1. Overview

Components under `web/cesium/components/` are the **only sanctioned way** to use CesiumJS in the KFM web stack.

Design goals:

- **Wrapper-first:** KFM code should never talk directly to Cesium globals from random locations.  
- **Typed & declarative:** All components are **TypeScript-first** and configured via props + JSON registries.  
- **Governed interactions:** Picking, terrain sampling, and overlays are routed through **CARE- and provenance-aware hooks**.  
- **Focus Mode-aligned:** Components integrate cleanly with Story Nodes, timelines, and MapLibre dual-view patterns.

For higher-level Cesium subsystem context, see:

- `web/cesium/README.md`  
- `web/cesium/releases/1.136/README.md`

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/components/
│
├── 📄 README.md                          # This file — Cesium component library overview
│
├── 🌐 CesiumGlobe.tsx                    # Core globe wrapper (camera, base layers, basic overlays)
├── 🕰️ CesiumTimelineScene.tsx            # Timeline-aware 3D scene (Story Nodes, Focus Mode)
├── 📍 CesiumRegionOverlay.tsx            # Cultural region & hydrology overlays (polygons/H3)
├── 🎯 CesiumPickController.tsx           # Picking controller using scene.pickAsync + KFM handlers
├── 🧭 CesiumCameraController.tsx         # Camera presets, bookmarks, & Story Node jumps
├── 🧪 CesiumDebugLayerToggle.tsx         # Dev-only debug overlays (tileset bounds, wireframes)
│
├── 🪝 hooks/                             # Reusable hooks (typed, governable)
│   ├── 📄 useCesiumViewer.ts             # Initializes Viewer, wires up providers & events
│   ├── 📄 useCesiumPicking.ts            # Async picking, routed through CARE/provenance handlers
│   ├── 📄 useCesiumTerrainSampling.ts    # Batched terrain sampling & caching
│   └── 📄 useCesiumLayers.ts             # Layer registry → Cesium primitives wiring
│
└── 🧰 utils/                             # Pure helpers (no side effects)
    ├── 📄 cesiumCameraUtils.ts           # Camera conversion & bookmarking helpers
    ├── 📄 cesiumCoordinateUtils.ts       # Conversions between Cartographic, Cartesian, KFM IDs
    └── 📄 cesiumLayerUtils.ts            # Helpers to expand layer/tileset configs into Cesium types
~~~

**Layout contract:**

- Root-level `.tsx` files are **exported components** meant for direct use by application code.  
- `hooks/` and `utils/` are internal to this library; they encapsulate Cesium-specific logic.  
- All Cesium usage should flow through:
  - `useCesiumViewer`, `useCesiumPicking`, `useCesiumTerrainSampling`, `useCesiumLayers`  
  - No ad-hoc calls to `new Cesium.Viewer(...)` scattered around the codebase.

---

## 🌐 3. `CesiumGlobe.tsx` — Core Globe Wrapper

**Role:**

- Provide a **generic 3D globe** with:
  - Base imagery & terrain providers configured via `web/cesium/config`.  
  - Optional overlays (tilesets, regions, sensors) resolved via `web/cesium/layers`.  
  - Standard camera controls and events.

**Key responsibilities:**

- Create and dispose Cesium `Viewer` safely.  
- Wire **providers** using IDs from `cesium-providers.json`.  
- Expose:
  - Camera state callbacks (for synchronization with MapLibre / URL).  
  - Hooks for adding/removing layer components.

**Governance:**

- Must respect CARE & sovereignty hints passed in via layer props (e.g., hide sensitive overlays).  
- All picks / interactions must fold into `CesiumPickController` or `useCesiumPicking`.

---

## 🕰️ 4. `CesiumTimelineScene.tsx` — Time-Linked Scene

**Role:**

- Provide a **timeline-aware** Cesium scene for Focus Mode and Story Nodes.

**Features:**

- Integrates Cesium `Clock`, `Timeline`, or custom time controls with:
  - STAC imagery layers.  
  - 3D Tilesets that vary by epoch/time.  
  - Focus Mode Story Nodes representing events in time.

**Key behaviors:**

- Reacts to KFM’s time model (e.g., OWL-Time-aligned intervals).  
- Handles scrubbing, play/pause, and camera transitions.  
- Surfaces temporal provenance & CARE chips for time-dependent layers.

---

## 📍 5. `CesiumRegionOverlay.tsx` — Region Overlays (Polygons & H3)

**Role:**

- Render **cultural landscape regions, hydrology regions, and other masks** over the globe.

**Inputs:**

- Region definitions from:
  - `web/cesium/layers/regions.json`  
  - Or direct props referencing region IDs (e.g., `flint-hills-region`, `arkansas-river-basin-region`).

**Behaviors:**

- Selects **polygons vs H3 mosaics** based on CARE/visibility hints.  
- Applies styling consistent with KFM design (color, opacity, borders).  
- Respects zoom-level & visibility policies for sensitive regions.

---

## 🎯 6. `CesiumPickController.tsx` — Governed Picking

**Role:**

- Central controller for user picks on the globe, using **`scene.pickAsync`**.

**Patterns:**

- Attaches click handlers via `ScreenSpaceEventHandler`.  
- Uses `useCesiumPicking` internally to:
  - Run `scene.pickAsync(windowPosition)`.  
  - Map pick results to KFM entities (regions, sites, tilesets, sensors).  
  - Apply CARE/provenance filters (e.g., hide or aggregate sensitive data).

**Outputs:**

- Emits structured pick events:
  - `{ type, id, datasetId, provenanceRef, careMetadata, ... }`  
- Downstream UI (Story Node side panels, chips) use this structure for explainability.

---

## 🧭 7. `CesiumCameraController.tsx` — Camera Governance

**Role:**

- Manage camera presets and navigation consistent with Focus Mode & Story Nodes.

**Features:**

- Handles camera bookmarks:
  - Per-region, per-Story Node, or per-layer.  
- Smoothly transitions between:
  - Region-scale views.  
  - Site-level contexts (when allowed by CARE).  
- Optionally synchronizes:
  - MapLibre 2D viewport and Cesium 3D camera.

**Implementation notes:**

- Uses utilities in `cesiumCameraUtils.ts` for conversions and tweening.  
- All camera jumps should be recorded or loggable to maintain provenance over “what the user saw”.

---

## 🪝 8. Hooks — `hooks/`

### 8.1 `useCesiumViewer.ts`

- Initializes and manages lifecycle of `Cesium.Viewer`.  
- Injects configuration from:
  - `web/cesium/config/cesium-env.example.json` (real env runtime).  
  - `web/cesium/config/cesium-providers.json`.

### 8.2 `useCesiumPicking.ts`

- Encapsulates all picking logic:
  - Async `scene.pickAsync`  
  - Fallback to `scene.pick` if required.  
- Maps Cesium pick results to KFM entities and CARE/provenance metadata.

### 8.3 `useCesiumTerrainSampling.ts`

- Provides a **batched, caching** interface for DEM sampling.  
- Uses terrain APIs (`sampleTerrainMostDetailed`, `globe.getHeight`) based on context.  
- Ensures we do not flood terrain providers with excessive requests.

### 8.4 `useCesiumLayers.ts`

- Reads layer definitions (tilesets, regions, sensors) from `web/cesium/layers/*.json`.  
- Constructs Cesium primitives and manages their lifecycle.  
- Applies CARE/visibility decisions (e.g., H3-only, polygon-generalized).

---

## 🧰 9. Utils — `utils/`

- **`cesiumCameraUtils.ts`**  
  - Camera conversions (Cartographic ↔ world coordinates ↔ KFM region/sensor IDs).  
  - Helpers for bookmarking and restoring camera states.

- **`cesiumCoordinateUtils.ts`**  
  - Lat/lon ↔ Cesium `Cartographic` ↔ 3D Cartesian conversions.  
  - Grid/H3 integration for region tiles.

- **`cesiumLayerUtils.ts`**  
  - Translate layer registry entries to Cesium types.  
  - Enforce naming and provider ID conventions.

All utils must be:

- **Pure** (no side effects, no direct DOM access).  
- Well-typed and tested where complexity warrants.

---

## 📊 10. Telemetry & Error Handling

Components in this directory should:

- Expose **hooks** or callbacks for:
  - Frame-time stats (optional).  
  - Pick latency & error counts.  
  - Terrain sampling duration & error rates.

- Route telemetry into:
  - `../../releases/v11.2.3/web-cesium-telemetry.json`  
  - Under schema: `../../schemas/telemetry/web-cesium-release-v1.json`

Error handling:

- Centralize Cesium-related error logging (picks, terrain, tilesets).  
- Avoid noisy logs; aggregate and summarize where possible.  
- Provide clear error surfaces in dev mode, non-intrusive in production.

---

## ⚖ 11. FAIR+CARE & Sovereignty in Components

All Cesium components must:

- Respect **CARE** and sovereignty policies encoded in:
  - Layer registries (`web/cesium/layers/*.json`).  
  - Dataset metadata and provenance.  

Concrete rules:

- Do **not** display site-level geometry for sensitive datasets.  
- Use **generalized regions** or **H3 mosaics** for sensitive overlays.  
- Ensure picking handlers redact or aggregate sensitive information before surfacing to UI.

Whenever a new component is added:

- Include CARE/sovereignty considerations in its JSDoc / TS doc comments.  
- Confirm behavior with the FAIR+CARE Council if new interaction patterns are introduced.

---

## 🧭 12. Authoring & Maintenance Workflow

When adding or updating components:

1. **Design in terms of wrappers/hooks**, not raw Cesium usage.  
2. **Update this README** if:
   - A new top-level component is introduced.  
   - An existing component’s contract changes.  
3. **Wire config + layers**:
   - Ensure necessary entries exist in `web/cesium/config` and `web/cesium/layers`.  
4. **Add tests**:
   - Where possible, add/extend smoke scenarios in `web/cesium/releases/1.136/tests`.  
5. **Run validation**:
   - Type checks, linting, and markdown validation.  
6. **Governance review**:
   - For new interaction patterns or layers that touch sensitive data.

---

## 🕰️ 13. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial governed Cesium web components overview; established wrapper-first architecture, hooks, utils, and CARE/provenance-aware interaction patterns. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Component Library)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Web Integration Overview](../README.md) · [⬅ Back to Web Root](../../README.md)

</div>
