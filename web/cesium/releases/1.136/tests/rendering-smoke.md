---
title: "🧪 KFM v11.2.3 — CesiumJS v1.136 Rendering Smoke Scenarios (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Step-by-step rendering and interaction smoke scenarios for CesiumJS v1.136 within the Kansas Frontier Matrix web stack."
path: "web/cesium/releases/1.136/tests/rendering-smoke.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 smoke-scenario-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136-rendering-smoke"
semantic_document_id: "kfm-web-cesium-release-1.136-rendering-smoke"
event_source_id: "ledger:kfm:web:cesium:release:1.136:tests:rendering-smoke"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Test Scenarios"
intent: "web-cesium-release-1-136-rendering-smoke"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧪 **KFM — CesiumJS v1.136 Rendering & Interaction Smoke Scenarios**  
`web/cesium/releases/1.136/tests/rendering-smoke.md`

**Purpose:**  
Provide **concrete, repeatable smoke scenarios** for validating **CesiumJS v1.136** inside KFM:  
base rendering, tilesets, STAC overlays, picking, terrain sampling, glyphs, timeline, and basic performance.

This file is the **step-by-step companion** to:  
`web/cesium/releases/1.136/tests/README.md`

</div>

---

## 📘 1. Test Route & Setup

### 1.1 Target Route (Example)

KFM implementations should expose a **Cesium test page** such as:

- `/dev/cesium-smoke` or  
- `/lab/cesium/release/1.136`

The exact route must be documented in:

- `web/cesium/tests/rendering-smoke.md` (this file) **and/or**  
- The web routing documentation for the project.

### 1.2 Pre-conditions

- CesiumJS is locked to **v1.136** in the build.  
- The app is running in **dev/staging** with:
  - Valid Cesium env config (`web/cesium/config/cesium-env.example.json` → real env).  
  - Accessible providers as declared in `web/cesium/config/cesium-providers.json`.  

Optional but recommended:

- Open browser dev tools console and **Network** panel for diagnostics.

---

## 🗺️ 2. Scenario A — Base Globe & Terrain

**Goal:** Confirm basic Cesium rendering and camera behavior.

### Steps

1. Open the Cesium smoke route in a browser.  
2. Observe initial **globe load**:
   - [ ] No red tiles or unhandled errors in the console.  
   - [ ] Default imagery appears over the full globe.

3. Interact with the camera:
   - [ ] Zoom in/out (mouse wheel or UI control).  
   - [ ] Pan horizontally (drag).  
   - [ ] Tilt the camera (right-drag / equivalent controls).  

4. Verify terrain:
   - [ ] Elevation variation visible where expected (mountainous regions).  
   - [ ] No obvious terrain “plateau” artifacts or flat Earth behavior.

### Acceptance Criteria

- No Cesium-related errors in the console during basic interactions.  
- Camera controls feel **smooth and responsive**.  
- Base imagery and terrain are visually coherent.

---

## 🧱 3. Scenario B — 3D Tileset Rendering

**Goal:** Validate 3D Tiles rendering and interaction for at least one tileset.

### Steps

1. Enable a **3D Tileset** via:
   - A test UI toggle on the smoke route, or  
   - A dev-only “load tileset” button.

2. Confirm tileset loading:
   - [ ] Tiles gradually appear at the expected location.  
   - [ ] No continuous error spam in the console.

3. Camera interactions:
   - [ ] Orbit around the tileset.  
   - [ ] Zoom close to check for geometry artifacts.  
   - [ ] Zoom out to see overall footprint.

4. Visual checks:
   - [ ] No severe z-fighting or obvious tile “popping” beyond normal LOD.  
   - [ ] Buildings or features rest on terrain as expected (if applicable).  

### Acceptance Criteria

- Tileset loads **fully** and is navigable.  
- No persistent rendering artifacts or error loops.  
- Tileset remains visible across near/far zoom ranges.

---

## 🛰️ 4. Scenario C — STAC Imagery Overlay

**Goal:** Confirm STAC imagery overlay renders correctly and interacts well with base layers.

### Steps

1. Use the smoke page to load a **STAC imagery layer**:
   - e.g., a single-date satellite snapshot or analysis layer.

2. Visual checks:
   - [ ] Imagery overlay aligns with base imagery/terrain.  
   - [ ] No unusual color banding or extreme brightness issues.  

3. Toggle behavior:
   - [ ] Turn the STAC overlay **on and off** via the UI.  
   - [ ] Confirm the globe correctly updates without ghosting.

4. Opacity / blending:
   - [ ] Adjust overlay opacity (if supported).  
   - [ ] Check that underlying imagery remains visible where expected.

### Acceptance Criteria

- STAC overlay loads without errors.  
- Toggling and opacity changes work as expected.  
- The overlay improves context without severe visual artifacts.

---

## 🖱️ 5. Scenario D — Async Picking (`scene.pickAsync`)

**Goal:** Validate KFM’s use of `scene.pickAsync` for picking operations.

### Steps

1. Enable a test layer with **pickable features** (e.g., a 3D Tileset with feature metadata or site markers).  
2. Click on several features:
   - [ ] A popup or side panel shows information about the clicked feature.  
   - [ ] Repeated clicks produce consistent results (no null spam where geometry clearly exists).  

3. Quickly click around:
   - [ ] The globe remains responsive; no freeze or major jitter.  
   - [ ] Console remains clean of `pickAsync`-related errors.

4. Stress test:
   - [ ] Click while tiles are **still loading**.  
   - [ ] Confirm the app handles **pending picks** gracefully.

### Acceptance Criteria

- `pickAsync` is used (checked in code; not strictly manual).  
- Picks succeed at a high rate where visual features exist.  
- No `unhandled promise` or `pickAsync` related error spam.

---

## 🏔️ 6. Scenario E — Terrain Sampling & Elevation Probes

**Goal:** Ensure terrain height queries are correct and reasonably fast.

### Steps

1. Activate a simple **elevation probe** tool (if available), or:
   - Use a debug UI to show elevation under the cursor.  

2. Sample several points:
   - [ ] Low-lying areas (coastal/plain).  
   - [ ] Mountainous/rough terrain.  

3. Observe:
   - [ ] Elevation values change smoothly with cursor movement.  
   - [ ] No obvious spikes to absurd values (e.g., tens of thousands of meters).  

4. Performance:
   - [ ] Probe behavior does not noticeably degrade frame rate.  

### Acceptance Criteria

- Elevation outputs are **plausible** for tested locations.  
- No visible stalls or error floods during sampling.  
- Terrain queries remain responsive under normal usage.

---

## 🖼️ 7. Scenario F — Glyphs, Billboards & Labels

**Goal:** Verify billboard and label fixes in v1.136 produce correct glyph behavior.

### Steps

1. Enable layers with glyphs (icons + labels):
   - Archaeology/heritage icons.  
   - Hydrology gauges or sensor glyphs.

2. Visual checks:
   - [ ] Icons are visible at expected positions.  
   - [ ] Labels are readable; halos/outlines look clean.  

3. Zoom tests:
   - [ ] Zoom in very close; confirm icons do not explode, distort, or vanish.  
   - [ ] Zoom out; icons should shrink or cluster per the configured logic (if any).  

4. Depth test:
   - [ ] Where applicable, confirm markers do **not** clip strangely through nearby terrain/buildings.  

5. Optional screenshot:
   - [ ] Capture a reference screenshot and store in  
     `web/cesium/releases/1.136/artifacts/billboard-scaling.png`.

### Acceptance Criteria

- Billboards and labels behave as expected at multiple zoom levels.  
- No major artifacts or clipping issues.  
- New rendering fixes clearly improve over prior issues (if known).

---

## ⏱️ 8. Scenario G — Timeline & Camera Behavior

**Goal:** Check time-linked scenes and camera transitions.

### Steps

1. Open a **timeline-aware scene** (if available on the smoke route).  
2. Scrub the timeline:
   - [ ] Time-dependent layers (imagery, tilesets, overlays) visibly change.  
   - [ ] No severe stutter or lock-ups when scrubbing through moderate ranges.  

3. Camera transitions:
   - [ ] Use UI controls to jump between pre-defined camera bookmarks.  
   - [ ] Confirm camera moves smoothly between locations.  

### Acceptance Criteria

- Timeline interactions are smooth at moderate dataset sizes.  
- Camera transitions are predictable and stable.

---

## ⛽ 9. Scenario H — Performance Sanity

**Goal:** Quick performance sanity check; identify catastrophic regressions.

### Steps

1. With a typical “heavy” KFM scene (terrain + imagery + 3D Tiles + one overlay):

   - [ ] Interact for at least **30–60 seconds** (rotate, zoom, tilt).  
   - [ ] Note any significant stutters or freezes.

2. Optional metrics capture:
   - [ ] If available, record FPS/frame-time into:
     - `web/cesium/releases/1.136/artifacts/metrics.json`  

   Example structure (illustrative):

   ~~~json
   {
     "scene": "dev cesium-smoke",
     "cesium_version": "1.136",
     "frames_sampled": 600,
     "fps_mean": 50.2,
     "fps_p95": 42.1,
     "fps_p99": 35.0
   }
   ~~~

### Acceptance Criteria

- No catastrophic performance regressions vs previous baseline.  
- General interactions remain usable on KFM’s target hardware/browser stack.

---

## ✅ 10. Recording Results

For each run, record a brief summary (wherever your team tracks test outcomes), including:

- Date, Cesium version, browser(s) tested.  
- Scenario(s) executed (A–H).  
- Pass/fail + short notes for each scenario.  
- Links to any artifacts:
  - Screenshots (`artifacts/*.png`).  
  - Metrics (`artifacts/metrics.json`).  

If **any scenario fails**, Cesium v1.136 should **not** be promoted to or remain in **Stable / Governed** status without:

- Root cause analysis.  
- A mitigation plan or revert.  
- Updated release notes documenting the issue.

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Test Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium v1.136 Test Overview](README.md) · [⬅ Back to Cesium v1.136 Release Notes](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../../README.md)

</div>
