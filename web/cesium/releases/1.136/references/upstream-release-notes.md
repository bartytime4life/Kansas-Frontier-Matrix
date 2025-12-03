---
title: "📰 KFM v11.2.3 — CesiumJS v1.136 Upstream Release Notes (Curated Summary · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Curated, license-respecting summary of key CesiumJS v1.136 upstream release notes as relevant to the Kansas Frontier Matrix web stack."
path: "web/cesium/releases/1.136/references/upstream-release-notes.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 reference-summary compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136-upstream-notes"
semantic_document_id: "kfm-web-cesium-release-1.136-upstream-notes"
event_source_id: "ledger:kfm:web:cesium:release:1.136:references:upstream"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT (KFM summary · Cesium upstream docs under their respective licenses)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Upstream Release Summary"
intent: "web-cesium-release-1-136-upstream-summary"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📰 **KFM — CesiumJS v1.136 Upstream Release Notes (Curated Summary)**  
`web/cesium/releases/1.136/references/upstream-release-notes.md`

**Purpose:**  
Provide a **short, curated summary** of the upstream **CesiumJS v1.136** release notes as they relate to the Kansas Frontier Matrix (KFM), with links for further reading and explicit KFM impact annotations.

This document does **not** reproduce full upstream content; it is a governed summary that points to Cesium’s own documentation.

</div>

---

## 📘 1. Upstream Source Pointers

Use these links as starting points when consulting upstream material for Cesium v1.136:

- **Main CesiumJS Release Notes Index**  
  - Location: Cesium official documentation / blog (version-specific release notes page).  
  - Example pattern:  
    - `https://cesium.com/learn/cesiumjs/releases/`  

- **CesiumJS API Reference (v1.136)**  
  - Location: Cesium reference docs (Scene, Globe, Terrain, Billboard, Label, etc.).  
  - Example pattern:  
    - `https://cesium.com/learn/cesiumjs/ref-doc/`  

All URLs in this document are **illustrative patterns**; the authoritative locations are whichever URLs Cesium publishes for v1.136.

---

## 🔍 2. Picking & Interaction Changes (Upstream Summary)

**Upstream highlights (curated):**

- Introduction/standardization of **asynchronous picking** via `Scene#pickAsync`.  
- Improved handling of pick operations under heavy load and tile transitions.  
- Clarified semantics for null/failed picks and how they interact with scene state.

**KFM-relevant notes:**

- KFM adopts `scene.pickAsync` as the **preferred API** for interactive picking workflows.  
- Synchronous `scene.pick` remains present but is treated as **legacy** and should be phased out in high-frequency interaction paths.  
- Upstream guidance emphasizes:
  - Avoiding blocking operations inside the render loop.  
  - Handling promises and errors gracefully in UI integration code.

See also:

- `web/cesium/releases/1.136/references/api-links.md` (entry for `Scene#pickAsync`).  
- `web/cesium/releases/1.136/references/integration-notes.md` (picking strategy section).

---

## 🏔️ 3. Terrain & DEM Sampling Improvements (Upstream Summary)

**Upstream highlights (curated):**

- Performance optimizations in terrain picking and height sampling.  
- Improved caching/quadtree-like behaviors when sampling terrain repeatedly.  
- Reduced jitter and artifacts during LOD transitions for elevation queries.

**KFM-relevant notes:**

- Upstream notes indicate:
  - More efficient sampling for `sampleTerrainMostDetailed` and related helpers.  
  - Better behavior when combining imagery + terrain at a variety of zoom levels.

- For KFM tools (watershed exploration, elevation Story Nodes, etc.), this translates to:
  - **Lower per-sample latency**, especially in batch queries.  
  - More stable cursor elevation readouts and line-profile tools.  

KFM wraps these APIs in a terrain service / hook so upstream changes are centralized.

---

## 🖼️ 4. Billboards, Labels & Rendering Fixes (Upstream Summary)

**Upstream highlights (curated):**

- Fixes to billboard rendering when depth testing is enabled.  
- More robust behavior for **image sub-region** rendering, especially for atlas-based sprites.  
- Stabilization of **SVG billboard scaling** across zoom levels.  
- Reduced halo/outline artifacts for text labels and icon strokes.

**KFM-relevant notes:**

- Direct positive impact on:
  - Archaeology and heritage glyphs rendered as billboards.  
  - Hydrology and sensor icon overlays.  
  - Label readability in dense Story Node or Focus Mode views.

- KFM validates:
  - Icon scaling remains crisp at near and far zoom.  
  - Labels do not exhibit heavy halo artifacts after the upgrade.  
  - Overlapping stacks of glyphs behave more predictably than in previous releases.

Related KFM docs:

- `web/cesium/releases/1.136/README.md` — billboard/label fixes section.  
- `web/cesium/releases/1.136/tests/rendering-smoke.md` — glyph scenarios.

---

## 🧱 5. General Rendering, Stability & Performance (Upstream Summary)

**Upstream highlights (curated):**

- Incremental improvements to:
  - WebGL2 resource management and memory usage.  
  - Tile load ordering and backpressure behavior.  
  - Camera transitions and animation stability.

- Various bugfixes that reduce:
  - Unnecessary allocations  
  - Visual glitches during heavy 3D Tiles or imagery activity

**KFM-relevant notes:**

- These improvements help maintain:
  - Acceptable frame times during Focus Mode time scrubbing.  
  - Stable user experience when multiple layers (3D Tiles + imagery + vector overlays) are active.  

- KFM complements upstream improvements with:
  - Telemetry for frame-time and tile loading metrics.  
  - Smoke tests tracking regressions across Cesium versions.

See:

- `web/cesium/releases/1.136/tests/README.md` & `rendering-smoke.md`  
- `web/cesium/releases/1.136/artifacts/metrics.json` (optional metrics snapshot)

---

## 🧩 6. Deprecated / Changed APIs (As Noted Upstream)

This section should be updated as upstream notes are reviewed; examples of typical content:

- **Deprecated or discouraged patterns**:
  - Certain legacy terrain APIs or pick-related helpers may be flagged by upstream as deprecated.  
  - Any such APIs used in KFM must be **tracked and scheduled for migration**.

- **Backward-compatibility notes**:
  - Where upstream guarantees compatibility (e.g., “no breaking change to X”), KFM still records:
    - Where we rely on that guarantee (which components).  
    - How we plan to adapt if the guarantee changes in future versions.

When upstream explicitly marks an API as deprecated in v1.136:

1. Add a brief note here.  
2. Update `api-links.md` with deprecation context.  
3. Mark dependent KFM code with TODOs and migration plans.

---

## 🧬 7. Licensing & Attribution

CesiumJS documentation, release notes, and API references are:

- Owned and licensed by the **Cesium** team / its maintainers.  
- Subject to their own **license and terms of use**.

KFM’s obligations:

- Do **not** include large verbatim chunks of upstream documentation in this repository.  
- When quoting short snippets:
  - Attribute to Cesium.  
  - Keep excerpts minimal and clearly marked as quotes or paraphrases.

This file therefore:

- Uses **high-level summaries** instead of direct copy.  
- Encourages engineers to consult the official Cesium documentation for full details.

---

## 🔗 8. Cross-References Within KFM

Use this file in combination with:

- **KFM v1.136 Release Notes**  
  - `web/cesium/releases/1.136/README.md`  

- **KFM API Links**  
  - `web/cesium/releases/1.136/references/api-links.md`  

- **KFM Integration Notes**  
  - `web/cesium/releases/1.136/references/integration-notes.md`  

- **KFM Tests & Artifacts**  
  - `web/cesium/releases/1.136/tests/README.md`  
  - `web/cesium/releases/1.136/tests/rendering-smoke.md`  
  - `web/cesium/releases/1.136/artifacts/README.md`

Together, these documents form the **complete KFM v1.136 Cesium integration bundle**, tying upstream behavior to downstream implementation and governance.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Created curated, license-respecting upstream summary for CesiumJS v1.136; aligned with KFM release notes, tests, and API links. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Summary & Index Only · Cesium upstream docs under their own licenses)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium v1.136 References](README.md) · [⬅ Back to Cesium v1.136 Release Notes](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../../README.md)

</div>
