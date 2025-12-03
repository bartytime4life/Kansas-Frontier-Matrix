---
title: "🧪 KFM v11.2.3 — CesiumJS v1.136 Rendering & Interaction Smoke Tests (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed smoke-test suite for CesiumJS v1.136 in the Kansas Frontier Matrix web stack: rendering, picking, terrain sampling, and glyph validation."
path: "web/cesium/releases/1.136/tests/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 smoke-test-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136-tests"
semantic_document_id: "kfm-web-cesium-release-1.136-tests"
event_source_id: "ledger:kfm:web:cesium:release:1.136:tests"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Test Suite"
intent: "web-cesium-release-1-136-tests"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧪 **KFM — CesiumJS v1.136 Rendering & Interaction Smoke Tests**  
`web/cesium/releases/1.136/tests/README.md`

**Purpose:**  
Define the **governed smoke-test suite** for validating **CesiumJS v1.136** inside KFM’s web stack:  
rendering correctness, picking behavior, terrain sampling stability, glyph fidelity, and basic performance.

</div>

---

## 📘 1. Scope & Test Philosophy

These tests are **smoke-level checks**, not exhaustive specs. They are designed to:

- Catch **breaking regressions** between Cesium versions.  
- Ensure **core interaction paths** (pick, hover, timeline scrubbing) behave as expected.  
- Provide **repeatable manual + CI-guided scenarios** for KFM operators.  

They are organized around:

1. **Rendering correctness** (tiles, imagery, terrain, glyphs)  
2. **Picking / interaction** (sync vs async, under load)  
3. **Terrain sampling & DEM queries**  
4. **Performance sanity** (no catastrophic regressions)  

For the high-level release notes, see:

- `web/cesium/releases/1.136/README.md`

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/releases/1.136/tests/
│
├── 📄 README.md                    # This file — test suite definition
│
└── 📄 rendering-smoke.md           # Detailed scenario list & checklists (optional, recommended)
~~~

**Directory contract:**

- `README.md` defines **what must be tested** and **acceptance criteria**.  
- `rendering-smoke.md` (if present) captures **step-by-step** scenarios, screenshots, and notes.

---

## 🔍 3. Test Matrix Overview

Minimum coverage before promoting Cesium v1.136 to **Stable / Governed**:

| Area              | Test Category             | Required | Notes                                              |
|-------------------|---------------------------|---------:|----------------------------------------------------|
| Rendering         | Tiles, imagery, terrain   |   ✅     | Basic globe + layers render without errors        |
| Picking           | `scene.pickAsync` flow    |   ✅     | Async picking used in key interactions            |
| Terrain sampling  | Height queries / probes   |   ✅     | Stable & performant elevation sampling            |
| Glyphs / labels   | Billboards, labels, SVG   |   ✅     | Icon scaling & halos are visually correct         |
| Timeline          | Time-linked scenes        |   ✅     | Scrubbing + camera transitions are smooth         |
| Performance       | Frame time & load sanity  |   ✅     | No catastrophic regressions vs previous baseline  |

---

## 🧭 4. Rendering Smoke Tests

### 4.1 Base Globe + Terrain

**Goal:** Verify that Cesium v1.136 renders the base scene correctly.

**Checklist:**

- [ ] Globe renders with default imagery.  
- [ ] Primary terrain provider loads (no red tiles, no error flood).  
- [ ] Camera zoom / pan / tilt are smooth and error-free.  

**Data sources (typical):**

- Default imagery provider from `web/cesium/config/cesium-providers.json`.  
- Default terrain (e.g., `"terrain-kfm-primary"`).

---

### 4.2 3D Tilesets (Heritage / Built Environment)

**Goal:** Ensure 3D Tiles render correctly and are pickable.

**Checklist:**

- [ ] Heritage or built-environment tileset loads and appears at expected location.  
- [ ] No obvious z-fighting or tile flicker.  
- [ ] Tileset responds correctly to camera zoom/pan changes.  

**Edge cases:**

- [ ] Tileset visible both at near and far zoom levels.  
- [ ] No unexpected clipping through terrain or imagery.

---

### 4.3 STAC Imagery / Overlays

**Goal:** Confirm STAC-linked imagery overlays render correctly over base layers.

**Checklist:**

- [ ] STAC imagery loads (e.g., a single time slice).  
- [ ] Transparency / blending behaves as expected.  
- [ ] Turning STAC imagery on/off updates the globe correctly.  

Optional:

- [ ] A second imagery layer (e.g., mask or analysis overlay) can be toggled.

---

## 🖱️ 5. Picking & Interaction Tests

### 5.1 Async Picking (`scene.pickAsync`)

**Goal:** Validate KFM’s migration to `scene.pickAsync`.

**Checklist:**

- [ ] Click on a tileset feature returns a correct pick result via `pickAsync`.  
- [ ] Click on terrain returns a height sample or appropriate result.  
- [ ] Rapid clicks do not freeze the scene or cause dropped frames.  

**Under load:**

- [ ] Picking remains stable while tiles are loading.  
- [ ] No repeated pick-related errors in the console.

---

### 5.2 Hover & Tooltip Behavior

**Goal:** Verify hover-based interactions still work correctly.

**Checklist:**

- [ ] Hovering over key layers shows tooltips or highlight effects.  
- [ ] Moving the mouse quickly does not cause lingering highlights.  
- [ ] Hover behavior does not produce console errors.

---

## 🏔️ 6. Terrain Sampling & DEM Queries

**Goal:** Validate terrain sampling performance and correctness.

**Recommended tests:**

- [ ] Sample elevation at multiple locations across the region (e.g., valley, plateau).  
- [ ] Check that **elevation values are plausible** vs known references.  
- [ ] Run a small script or interaction that samples elevation along a line/segment; confirm no obvious spikes or NaNs.  

**Performance checks:**

- [ ] Terrain sampling does not cause noticeable frame rate drops.  
- [ ] No repeated network or tile errors during sampling.

---

## 🖼️ 7. Glyphs, Billboards & Labels

**Goal:** Ensure glyphs render correctly following v1.136 fixes.

**Layer types:**

- Archaeology / heritage icons  
- Hydrology gauges / station icons  
- Sensor / telemetry glyphs

**Checklist:**

- [ ] Icons appear at correct locations.  
- [ ] No clipping through terrain/buildings when depth test is enabled.  
- [ ] SVG icons scale correctly at **near and far** zoom levels.  
- [ ] Halos / outlines around labels are clean (no heavy artifacts).  

Optional:

- [ ] Take a reference screenshot and store in `web/cesium/releases/1.136/artifacts/billboard-scaling.png`.

---

## ⏱️ 8. Performance Sanity Checks

These are **sanity-level** checks, not full benchmarks.

**Goals:**

- Confirm there is no **catastrophic regression** vs previous Cesium version.  
- Provide a **quick performance profile** for v1.136 scenes.

**Checklist:**

- [ ] Basic globe scene: frame time is stable and within expected range.  
- [ ] Globe + tileset + STAC imagery: still interactive.  
- [ ] Timeline scrubbing with a moderate dataset: no severe stutters.  

Optional:

- [ ] Capture a small summary (FPS, frame time) in:  
  - `web/cesium/releases/1.136/artifacts/metrics.json`

---

## 🧪 9. How to Run These Tests

### 9.1 Local Development

1. Start the web app in dev mode.  
2. Open the **Cesium test route** (e.g., `/dev/cesium-smoke` if present).  
3. Walk through the checklists in this document and (optionally) `rendering-smoke.md`.

### 9.2 CI / Automation

- CI can perform basic checks by:
  - Launching a headless browser.  
  - Loading a minimal Cesium test page.  
  - Asserting that:
    - The page loads (HTTP 200).  
    - No Cesium-related console errors occur.  
    - Optional synthetic interactions behave as expected (via test harness).  

Any failures should:

- Block promotion of Cesium v1.136 to **Stable / Governed**.  
- Trigger review of:
  - Release notes  
  - Config changes  
  - Provider and layer definitions

---

## 🕰️ 10. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial smoke-test definition for CesiumJS v1.136 within KFM; covers rendering, picking, terrain sampling, glyphs, and performance sanity checks. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Test Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium v1.136 Release Notes](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../../README.md)

</div>
