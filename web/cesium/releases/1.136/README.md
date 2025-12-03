---
title: "🌍 KFM v11.2.3 — CesiumJS v1.136 Release Notes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed, provenance-tracked documentation of CesiumJS v1.136 for use within the Kansas Frontier Matrix frontend and 3D geospatial visualization stack. Includes rendering changes, performance gains, governance hooks, and UI/UX impacts."
path: "docs/web/cesium/releases/1.136/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136"
semantic_document_id: "kfm-web-cesium-release-v1.136"
event_source_id: "ledger:kfm:web:cesium:release:1.136"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Release Notes"
intent: "web-cesium-release-1-136"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌍 CesiumJS v1.136 — KFM-Governed Release Summary  
`docs/web/cesium/releases/1.136/README.md`

**Purpose:**  
Capture the **governed, provenance-tracked** upgrade to **CesiumJS v1.136** for the Kansas Frontier Matrix (KFM) web stack, including:  
rendering changes, performance gains, governance hooks, and UI/UX implications for Focus Mode, Story Nodes, and 3D Tiles workloads.

</div>

---

## 📘 Overview

CesiumJS **v1.136 (December 2025)** delivers improvements that directly impact:

- 3D terrain visualization and sampling  
- Scene picking and interactive probes  
- Billboard/label rendering fidelity  
- Overall stability under heavy 3D Tiles + telemetry workloads  

This release has been reviewed under the **KFM v11 Visualization Compatibility Matrix** and is approved for:

- **MapLibre + Cesium dual-view** usage  
- **Focus Mode v2/v3** Story Node interactions  
- **STAC-driven** temporal 3D scenes  
- All **v11.2.3 LTS** web deployments

---

## 🗂️ Directory Layout (Emoji-Prefix Standard)

~~~text
docs/web/cesium/releases/1.136/
│
├── 📄 README.md                     # This file — governed v1.136 release notes
│
├── 🧪 tests/                        # Optional smoke tests for rendering, picking, terrain sampling
│   └── 📄 rendering-smoke.md        # Scenario list + manual/automated checks
│
├── 🗄️ artifacts/                    # Optional performance captures, screenshots, QA output
│   ├── 📸 terrain-picking.png       # Visual confirmation of terrain sampling stability
│   ├── 📸 billboard-scaling.png     # Icon scaling and label halo checks
│   └── 🧾 metrics.json              # Frame time, tile loads, pick latency snapshots
│
└── 📚 references/                   # Upstream links, API notes, compatibility context
    └── 📄 upstream-release-notes.md # Mirrored/summarized Cesium upstream release notes
~~~

**Directory contract:**

- This `README.md` is the **governed root** for v1.136 in KFM.  
- `tests/`, `artifacts/`, and `references/` are **optional but recommended** for full CI + manual validation.  
- All additional files must be **traceable** via PROV-O and included in the web SBOM/manifest as needed.

---

## ✨ High-Impact Improvements in CesiumJS v1.136

These items have **direct KFM impact** across hydrology, archaeology, climate overlays, and cross-domain 3D Tiles visualization.

---

### 🔍 1. Asynchronous Scene Picking (`scene.pickAsync`)

**What changed**

Cesium now exposes an asynchronous picking API:

- **New API:** `scene.pickAsync(windowPosition)`  
- Returns a **Promise** that resolves to the pick result without blocking the render loop.

Example pattern (conceptual):

~~~js
const picked = await scene.pickAsync(windowPosition);
if (picked) {
  // KFM interaction logic here
}
~~~

**KFM impact**

- Eliminates **UI frame stalls** during selection under heavy load.  
- Enables **stable interactive probes** over:
  - 3D Tiles (sites, buildings, hydrology structures)  
  - Terrain DEMs (elevation sampling)  
  - Time-dynamic STAC overlays  
- Required for future **Focus Mode v11.3** Story Node globe interactions where:
  - Multiple picks run per frame  
  - Telemetry overlays and region masks are active simultaneously.

**KFM guidance**

- Synchronous `scene.pick(...)` remains available but is **discouraged** for new work.  
- Existing code paths should be progressively migrated to `pickAsync` where feasible.

---

### 🏔️ 2. Terrain Picking Performance Gains

**What changed**

Cesium v1.136 introduces quadtree-based improvements and better caching for:

- **Terrain height sampling**  
- **Ray-terrain intersection** queries  
- **Pick performance** over complex DEMs

**Observed benefits (expected in KFM scenarios)**

- Lower latency per height query (especially at higher zoom levels).  
- Smoother cursor movement and elevation readouts.  
- More consistent behavior across LOD transitions and tile loads.

**KFM use cases**

- Hydrology:
  - Watershed boundary exploration  
  - Cross-section and profile sampling  

- Archaeology:
  - Site vicinity elevation checks  
  - Landscape-scale visibility/line-of-sight tooling  

- Risk / environmental modeling:
  - Floodplain visualization with **vertical exaggeration**  
  - DEM-based Story Node narratives (e.g., before/after scenarios)

---

### 🖼️ 3. Billboard / Label Rendering Fixes

**What changed**

Cesium fixed several billboard/label issues that previously affected KFM glyphs:

| Fix / Change                          | KFM Benefit                                                 |
|--------------------------------------|-------------------------------------------------------------|
| Depth testing consistency            | Site markers no longer clip through buildings/terrain      |
| `imageSubRegion` rendering corrected | Stable atlas-based STAC symbology                          |
| SVG billboard scaling stabilized     | Iconography remains crisp at near/far zoom levels          |
| Halo/outline artifacts reduced       | Cleaner overlays for sensor markers & annotations          |

**KFM layers affected**

- Heritage & archaeology icon sets (sites, regions, Story Node anchors)  
- Hydrology gauging station icons & event markers  
- Sensor/telemetry glyphs from atmospheric and climate pipelines  
- Combined multi-category glyph stacks in MapLibre/Cesium dual view

---

### 🧱 4. Stability & Rendering Improvements

**Highlights**

- Improved **memory usage** under WebGL2-heavy scenes  
- More predictable **tile load ordering** for 3D Tiles and imagery  
- Smoother **camera transitions** under rapid user interactions  
- Minor CesiumJS API housekeeping to track upstream web standards

**Result in KFM**

- Fewer dropped frames during:
  - 3D Tiles + imagery + vector hybrid scenes  
  - Fast time-slider scrubbing in Focus Mode  
  - Multi-terrain switching (e.g., switching STAC basemaps or terrain providers)  

- More consistent **interaction feel** across browsers and hardware profiles.

---

## 🧩 KFM Integration Notes (v11.2.3 Alignment)

### ✅ Automatic Compatibility

All current KFM components using **Cesium v1.120–1.135** are **forward-compatible** if they:

- Do not rely on internal/undocumented Cesium APIs.  
- Use standard Cesium + Resium (or vanilla Cesium) integration patterns.  

No breaking changes are expected for:

- KFM Story Node map components  
- Cesium-driven 3D archival visualizations  
- HRRR/terrain overlays embedded in 3D scenes

---

### 🔁 Recommended Migration Steps

**Step 1 — Upgrade package**

Use your package manager (example):

~~~bash
npm install cesium@1.136
~~~

Ensure build tooling (Webpack/Vite/Rollup) is still configured to:

- Copy Cesium static assets (if applicable).  
- Respect tree-shaking rules for your bundler.

---

**Step 2 — Prefer async picks**

Where possible, migrate:

~~~diff
- const picked = scene.pick(endPosition);
+ const picked = await scene.pickAsync(endPosition);
~~~

Apply primarily to:

- Focus Mode globe interactions  
- High-frequency probes (hover-inspect tools)  
- Any pick operation inside an animation / interaction loop

---

**Step 3 — Re-test SVG billboards & glyph stacks**

Perform a **visual QA pass** for:

- `src/web/assets/icons/*.svg`  
- Layered glyphs (heritage + hydrology + sensor overlays)  
- Zoom extremes (very near & far) in Story Node maps

Record any regressions via:

- `artifacts/billboard-scaling.png`  
- Notes in `tests/rendering-smoke.md`

---

**Step 4 — Terrain sampling benchmarks (optional but recommended)**

In hydrology/terrain-heavy views:

- Run simple terrain sampling loops across representative extents.  
- Compare pick latency and frame time vs. previous release.  

Capture metrics in:

- `artifacts/metrics.json` (frame times, pick timings, etc.)

---

## 📊 Telemetry Hooks (FAIR+CARE Compliant)

Telemetry for Cesium v1.136 within KFM is:

- **Opt-in**  
- **FAIR+CARE-compliant**  
- **Redacted at ingestion** to avoid any sensitive user or location leakage

**Metrics (optional)**

- Picking latency distribution (`scene.pickAsync`)  
- Terrain sampling duration (DEM queries, line-of-sight probes)  
- Billboard/label render-call counts per frame  
- Camera frame stability (frame time jitter, dropped frames)

**Schema & storage**

- Telemetry schema:  
  `schemas/telemetry/web-cesium-release-v1.json`  

- Telemetry data:  
  `releases/v11.2.3/web-cesium-telemetry.json`  

Telemetry is intended for:

- Performance regression detection  
- Capacity planning & GPU load analysis  
- UX tuning for Focus Mode & Story Node interactions

---

## 🔗 Upstream References

Canonical upstream documentation and references should be mirrored or linked from:

- `docs/web/cesium/releases/1.136/references/upstream-release-notes.md`

Recommended content:

- CesiumJS official **December 2025** release notes  
- API reference for:
  - `scene.pickAsync`  
  - Terrain sampling utilities (if documented separately)  
- Any upstream notes on:
  - WebGL2/3D Tiles performance changes  
  - Deprecated APIs or forward-looking migration advice

All external URLs referenced in that file should be:

- Stable where possible  
- Versioned (pointing at Cesium v1.136, not “latest”)  

---

## 🧭 Version History

| KFM Version | Date       | Author                             | Summary                                                                |
|------------|------------|------------------------------------|------------------------------------------------------------------------|
| v11.2.3    | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial governed CesiumJS v1.136 release summary; documented async picking, terrain gains, billboard fixes, and telemetry hooks. |
| v11.2.4    | Pending    | Web Visualization Systems WG       | Planned: deeper terrain benchmarks, extended Focus Mode integration notes, and expanded rendering-smoke test suite. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Release Notes Content)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Web Visualization Standards](../../../README.md) · [⬅ Back to Cesium Release Index](../README.md)

</div>