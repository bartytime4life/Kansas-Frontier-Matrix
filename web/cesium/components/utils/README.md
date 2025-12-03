---
title: "🧰 KFM v11.2.3 — Cesium Web Utils Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed, side-effect-free TypeScript utilities for CesiumJS integration in the Kansas Frontier Matrix web stack: camera, coordinates, and layer helpers."
path: "web/cesium/components/utils/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 utils-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-utils-v11-2-3"
semantic_document_id: "kfm-web-cesium-utils-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:components:utils:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Utils Library Overview"
intent: "web-cesium-utils"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — Cesium Web Utils Library**  
`web/cesium/components/utils/README.md`

**Purpose:**  
Describe the **governed, side-effect-free TypeScript utilities** that support CesiumJS integration in the KFM web stack:  
camera helpers, coordinate conversions, and layer expansion utilities used by Cesium components & hooks.

</div>

---

## 📘 1. Overview

Utilities in `web/cesium/components/utils/`:

- Provide **pure functions** to support Cesium hooks and components.  
- Contain **no React hooks**, **no DOM access**, and **no global side effects**.  
- Are fully **TypeScript-typed** and designed for:
  - Camera state conversions & bookmarking  
  - Coordinate conversions between Cesium and KFM representations  
  - Expansion of layer/tileset configs into Cesium-ready structures  

These utils help ensure:

- KFM-specific logic is **centralized and tested**.  
- Cesium upgrade surface is **limited** to a few well-defined modules.  
- FAIR+CARE and provenance decisions can be implemented consistently at higher layers.

For context:

- Components overview: `web/cesium/components/README.md`  
- Hooks overview: `web/cesium/components/hooks/README.md`  

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/components/utils/
│
├── 📄 README.md                        # This file — utils library overview & contracts
│
├── 🎥 cesiumCameraUtils.ts             # Camera conversions, presets, bookmark encoding/decoding
├── 📍 cesiumCoordinateUtils.ts         # Coordinate conversions (Cartesian/Cartographic/KFM IDs)
└── 🗺️ cesiumLayerUtils.ts              # Layer registry → Cesium config expansion helpers
~~~

**Directory contract:**

- Only **pure, non-React** utilities are allowed here.  
- Each file must:
  - Export **named, typed functions**.  
  - Have no external side effects when imported.  
  - Avoid hard-coded URLs, provider IDs, or dataset IDs (take them as inputs instead).

---

## 🎥 3. `cesiumCameraUtils.ts` — Camera Helpers

**Responsibility:**

- Provide **helper functions** for working with Cesium camera state and KFM concepts (regions, bookmarks, Story Nodes).

**Typical functions (illustrative):**

- `cameraToBookmark(camera: Cesium.Camera): KfmCameraBookmark`  
- `bookmarkToCameraView(bookmark: KfmCameraBookmark): CameraViewOptions`  
- `fitRegionExtent(regionExtent): CameraViewOptions`

**Use cases:**

- `CesiumCameraController.tsx`:
  - Saving and restoring camera bookmarks from Story Nodes or KFM UI.  
- Syncing MapLibre 2D and Cesium 3D:
  - Converting between KFM 2D view state and Cesium camera view.

**Constraints:**

- Functions must be **deterministic** given inputs.  
- No direct access to DOM or URL; those are managed by higher-level components.  
- Any FAIR+CARE logic related to **where cameras may go** belongs in components/hooks, not here.

---

## 📍 4. `cesiumCoordinateUtils.ts` — Coordinate Conversions

**Responsibility:**

- Provide safe, well-typed conversions between:

  - Cesium Cartesian types (`Cartesian3`, etc.)  
  - Cesium `Cartographic` (lat/long/height)  
  - KFM coordinate representations (e.g., `{ lat, lon }`, H3 indices, region IDs)

**Typical functions (illustrative):**

- `cartesianToLatLon(cartesian: Cesium.Cartesian3): { lat: number; lon: number; height: number }`  
- `latLonToCartographic(lat: number, lon: number, height?: number): Cesium.Cartographic`  
- `cartographicToH3(cartographic: Cesium.Cartographic, resolution: number): string` (if used)

**Use cases:**

- `useCesiumPicking.ts`:
  - Map picked positions to lat/lon + height.  
- `useCesiumTerrainSampling.ts`:
  - Convert lat/lon arrays to `Cartographic[]` for terrain APIs.  

**Constraints & FAIR+CARE:**

- Utils must **not** enforce CARE or sovereignty rules themselves.  
- However, they must be implemented in a way that:
  - Does not silently clamp or transform coordinates unexpectedly.  
  - Leaves higher layers free to apply masking/generalization rules correctly.

---

## 🗺️ 5. `cesiumLayerUtils.ts` — Layer Expansion Helpers

**Responsibility:**

- Convert KFM layer registry entries into **Cesium-ready configuration objects**, without touching the actual `Viewer`/`Scene`.

**Typical functions (illustrative):**

- `expandTilesetConfig(layerConfig: TilesetLayerConfig): ExpandedTilesetOptions`  
- `expandImageryConfig(layerConfig: ImageryLayerConfig): ExpandedImageryOptions`  
- `expandRegionLayerConfig(layerConfig: RegionLayerConfig): ExpandedRegionOptions`

Where `layerConfig` types correspond to entries in:

- `web/cesium/layers/tilesets.json`  
- `web/cesium/layers/regions.json`  
- `web/cesium/layers/sensors.json`

**Use cases:**

- `useCesiumLayers.ts`:
  - Reads JSON from `web/cesium/layers/` and calls these helpers to obtain:
    - URLs  
    - Styling options  
    - CARE/visibility hints  
    - Provenance and dataset IDs

**Constraints:**

- No calls to Cesium constructors or global objects.  
- No network requests or environment variable reads.  
- Functions take plain objects and return plain objects.

---

## 🧪 6. Testing & CI Expectations

Each utils file should:

- Be **TypeScript-typed** with clear function signatures.  
- Have unit tests where logic is non-trivial (e.g., coordinate transformations, camera bookmark math).  
- Be verified by:

  - TypeScript type checking  
  - Linting (ESLint)  
  - Any dedicated unit test runner configured for the repo  

CI should:

- Ensure this README and `.ts` files pass:
  - Markdown formatting rules.  
  - Type/lint checks.  
- Optionally run focused unit tests for these utilities.

---

## ⚖ 7. FAIR+CARE & Sovereignty Considerations

Although utils are “low-level,” they **must not** undermine FAIR+CARE guarantees:

- **No built-in hard-coded masks or offsets** for sensitive data:
  - Those belong in CARE-aware hooks and components.  

- **No logging** or debug output that might leak raw coordinates or IDs:
  - Logging must be performed at higher layers with appropriate redaction.

- **Where generalization is involved** (e.g., converting coordinates to H3 or regions), ensure:
  - The function is clearly named and documented.  
  - Higher layers control when and how generalization is applied.

---

## 🧭 8. Authoring & Maintenance Workflow

When adding or modifying a util:

1. **Determine scope**  
   - Ensure the behavior belongs in a **pure** utility (not a hook or component).  

2. **Add or update util file**  
   - Keep functions small and focused.  
   - Use descriptive names and types.  

3. **Document here**  
   - Update this README with:
     - New file name  
     - Responsibility summary  
     - Key usage notes  

4. **Add tests where needed**  
   - Especially for transformations, serialization logic, or math-heavy helpers.  

5. **Run CI**  
   - Confirm type checks and lints pass.  

6. **Coordinate with hooks/components**  
   - Update any code that consumes these utils if signatures change.  
   - Maintain backward compatibility where practical, or document breaking changes.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial governed Cesium utils overview; defined contracts for camera, coordinate, and layer helpers with side-effect-free guarantees. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Utils Library)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Components Overview](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../README.md) · [⬅ Back to Web Root](../../../README.md)

</div>
