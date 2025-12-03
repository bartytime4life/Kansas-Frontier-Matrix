---
title: "🧩 KFM v11.2.3 — CesiumJS v1.136 Integration Notes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Deeper technical notes, design decisions, and migration guidance for integrating CesiumJS v1.136 into the Kansas Frontier Matrix web stack."
path: "web/cesium/releases/1.136/references/integration-notes.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 integration-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136-integration-notes"
semantic_document_id: "kfm-web-cesium-release-1.136-integration-notes"
event_source_id: "ledger:kfm:web:cesium:release:1.136:references:integration-notes"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Integration Notes"
intent: "web-cesium-release-1-136-integration-notes"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧩 **KFM — CesiumJS v1.136 Integration Notes**  
`web/cesium/releases/1.136/references/integration-notes.md`

**Purpose:**  
Capture deeper **engineering notes, trade-offs, and migration details** for CesiumJS **v1.136** in KFM, beyond what fits in the high-level release notes or API index.

This file is intended for **engineers and maintainers** working on:
- `web/cesium/components/*`
- `web/cesium/layers/*`
- 3D Tiles, terrain, and Focus Mode globe integration.

</div>

---

## 📘 1. Context & Design Goals

Cesium v1.136 is **not** a ground-up rewrite, but it introduces enough behavior changes that we explicitly document:

- Why we adopted **`scene.pickAsync`** as the preferred picking path.  
- How we expect terrain sampling improvements to affect KFM tools.  
- The implications of billboard/label fixes on our glyph stacks.  
- How these changes interact with **FAIR+CARE**, masking, and sovereignty constraints.

Core design goals for this upgrade:

1. **Smooth user experience** under heavy 3D load (3D Tiles + imagery + STAC overlays).  
2. **Stable, debuggable picking flows** using async APIs.  
3. **Cleaner glyph rendering** with minimal regressions in existing maps.  
4. **Predictable performance envelope** validated via smoke tests and metrics.

For high-level release content, see:

- `web/cesium/releases/1.136/README.md`  
- API index: `web/cesium/releases/1.136/references/api-links.md`

---

## 🔍 2. Picking Strategy — From Sync to Async

### 2.1 Rationale for `scene.pickAsync`

Prior to v1.136, KFM used `scene.pick(...)` in many components. Under heavy load:

- Synchronous picking could **block the render loop**.  
- Rapid interactions during tile loading caused **frame stalls** and intermittent glitches.

With v1.136:

- `scene.pickAsync(windowPosition)` is the **preferred API**, returning a Promise.  
- It allows the render loop to continue while picking is in progress.

### 2.2 Integration Pattern

At the component level, picking must follow a **single, well-governed pattern**, e.g.:

~~~ts
async function handleClick(windowPosition: Cesium.Cartesian2) {
  const scene = viewer.scene;
  try {
    const picked = await scene.pickAsync(windowPosition);
    // Route through KFM’s pick handler (provenance + CARE-aware)
    if (picked) {
      handleKfmPickResult(picked);
    }
  } catch (err) {
    // Centralized logging & telemetry hook
    logCesiumPickError(err);
  }
}
~~~

Implementation requirements:

- Async picks should **never** be scattered through UI code; always route via a shared pick handler / hook.  
- Errors must be handled centrally so they can be:
  - Telemetry’d (pick failure rate, latency).  
  - Upgraded to alerts only when warranted (not every benign null pick).

### 2.3 Fallback & Legacy Paths

- `scene.pick(...)` is allowed **only** as:
  - A fallback in environments where `pickAsync` misbehaves.  
  - A short-term compatibility shim for older components not yet migrated.

These paths should be:

- Clearly marked in code (e.g., `// LEGACY_PICK_PATH`).  
- Easy to find via search when we fully deprecate sync picking.

---

## 🏔️ 3. Terrain Sampling — Practical Considerations

### 3.1 Batch vs Single-Point Sampling

KFM uses terrain sampling for:

- Hydrology & watershed tools.  
- Archaeology context around sites/regions.  
- Floodplain & elevation Story Nodes.

Cesium offers:

- `sampleTerrainMostDetailed(terrainProvider, positions)` — recommended for **batch** queries.  
- `globe.getHeight(cartographic)` — faster, but approximate.

Integration guidance:

- For **UI hover** cases, `getHeight` is acceptable.  
- For **analysis** flows (profiles, cross-sections, baseline computations), prefer `sampleTerrainMostDetailed`.

### 3.2 Caching & Rate Limiting

To avoid overloading the terrain provider:

- Implement **basic caching** keyed by:
  - Terrain provider ID.  
  - Rounded lat/lon (e.g., to 1e-4 or similar).  

- Implement **rate limiting** for high-frequency tools:
  - Avoid firing dozens of terrain requests per frame.  
  - Queue samples and process in batches if needed.

These behaviors should be concentrated in a single TerrainService / hook rather than duplicated.

---

## 🖼️ 4. Glyph & Label Rendering — Stacks & Depth

### 4.1 Glyph Stack Composition

KFM often stacks multiple glyphs at or near the same location, for example:

- Heritage site marker + sensor icon + region anchor.  
- This can produce depth-test conflicts and readability issues.

With v1.136 fixes:

- Depth testing and SVG scaling are more consistent.  
- It becomes safer to rely on **z-ordering** and **pixel offsets** instead of workarounds.

Recommended pattern:

- Group co-located glyphs logically in a wrapper component.  
- Use consistent pixel offsets (e.g., north/up, slight lateral offsets) to prevent total overlap.  
- Let Cesium handle depth, but avoid stacking completely coincident billboards whenever possible.

### 4.2 Label & Halo Tuning

After v1.136:

- Label halos/outlines behave more predictably.

Guidance:

- Keep halo widths modest to avoid clutter.  
- Prefer **short labels** in high-density layers.  
- Use Story Node side panels for verbose text; labels are just anchors.

---

## 🗺️ 5. Layer & Provider Governance

### 5.1 No Raw URLs in Components

All Cesium resource URLs (terrain, imagery, tilesets) must originate from:

- `web/cesium/config/cesium-providers.json`  
- `web/cesium/layers/*.json` (for dataset ↔ tileset mapping)

Components must:

- Read providers via IDs (e.g., `terrain-kfm-primary`).  
- Read layer mapping from `layers/tilesets.json`, `layers/regions.json`, etc.  
- Never embed inline URLs or one-off providers.

### 5.2 CARE & Sovereignty Hints on Layers

Layer registries should carry **minimal CARE hints**, e.g.:

- `care.sensitivity`  
- `care.visibility_rules` (e.g., `"polygon-generalized"`, `"h3-only"`)

Cesium components then:

- Interpret these hints to decide:
  - Whether to show a polygon or H3 mosaic.  
  - Whether to limit zoom level or disable interactions entirely.  

This keeps CARE/sovereignty decisions **data-driven**, not scattered in UI code.

---

## 🧪 6. Testing & Debugging Patterns

### 6.1 Dev-Only Debug Helpers

For debugging complex 3D scenes, we allow **dev-only** helpers:

- Tile bounding volumes.  
- Wireframe overlays.  
- Per-layer visibility toggles.

These should be controlled via:

- `web/cesium/config/cesium-feature-flags.json` (e.g., `enableDebugLayers` in `dev`).  
- Dev-only routes (e.g., `/dev/cesium-smoke`).

They must **not** be active in production profiles.

### 6.2 Console & Error Handling

With v1.136, some warnings may appear only during:

- First-time asset loading.  
- Specific, non-standard browser configurations.

Guidance:

- KFM CI should fail when:
  - We see repeated Cesium errors on standard smoke routes.  

- KFM CI may:
  - Tolerate a finite number of benign warnings, provided they are documented and understood.  

All Cesium errors/warnings should be:

- Aggregated and summarized in `web/cesium/releases/1.136/artifacts/logs.txt` (if captured).  
- Used as input for further tuning or bug reports.

---

## ⏭️ 7. Preparing for Future Upgrades

### 7.1 Version-Pinned Design

This file is **specific to v1.136**. For future upgrades:

- Create a new directory:
  - `web/cesium/releases/<new-version>/...`  
- Copy only relevant integration notes, and **update** them with:
  - New APIs.  
  - Behavior changes.  
  - Deprecations.

### 7.2 Backward Compatibility Strategy

Where possible:

- Keep wrappers and hooks stable.  
- Use KFM-internal abstractions (e.g., `useCesiumPick()`, `TerrainService`) to isolate Cesium API changes.

This ensures:

- Minimal code churn in downstream components.  
- Easier rollbacks if a new Cesium version misbehaves.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial integration notes for CesiumJS v1.136; documented picking, terrain sampling, glyph rendering, provider governance, and debugging patterns. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Integration Notes & Commentary)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium v1.136 References](README.md) · [⬅ Back to Cesium v1.136 Release Notes](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../../README.md)

</div>
