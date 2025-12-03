---
title: "🔗 KFM v11.2.3 — CesiumJS v1.136 Key API Links (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index of key CesiumJS v1.136 APIs used in the Kansas Frontier Matrix web stack, with stable links and KFM-specific integration notes."
path: "web/cesium/releases/1.136/references/api-links.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 API-usage-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136-api-links"
semantic_document_id: "kfm-web-cesium-release-1.136-api-links"
event_source_id: "ledger:kfm:web:cesium:release:1.136:references:api-links"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "API Reference Index"
intent: "web-cesium-release-1-136-api-links"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🔗 **KFM — CesiumJS v1.136 Key API Links**  
`web/cesium/releases/1.136/references/api-links.md`

**Purpose:**  
Serve as a **governed index** of CesiumJS v1.136 APIs that are **explicitly relied upon** by KFM’s web stack, with:  
stable documentation links (where available), integration locations, and migration notes.

</div>

---

## 📘 1. Usage Notes

- This file is a **pointer map**, not a full API spec.  
- Each entry should answer:
  - _Which Cesium API?_  
  - _Where is it used in KFM?_  
  - _Why did we adopt it for v1.136?_  
- External links should be:
  - Version-aware where possible (v1.136 or “ref-doc” URLs).  
  - Updateable when Cesium changes its doc hosting, without changing KFM behavior.

If any API is removed, deprecated, or behavior changes significantly in a future Cesium release, this file must be updated alongside:

- `web/cesium/releases/<new-version>/README.md`  
- Any affected KFM components and tests.

---

## 🧩 2. Core Scene & Picking APIs

| API                               | Upstream Doc URL (indicative)                                       | KFM Usage Location(s)                                       | Notes / Migration Guidance                                                  |
|-----------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------|
| `Scene#pickAsync`                 | `https://cesium.com/learn/cesiumjs/ref-doc/Scene.html#pickAsync`    | `web/cesium/components/CesiumGlobe.tsx`<br>`CesiumTimelineScene.tsx` | **Preferred picking API** from v1.136 onward. Used for async entity/feature picking in Focus Mode & Story Nodes. |
| `Scene#pick`                      | `https://cesium.com/learn/cesiumjs/ref-doc/Scene.html#pick`         | Legacy paths in older components (to be phased out)         | Synchronous, can stall frame; keep only as fallback where async is not yet wired. |
| `Globe#pick`                      | `https://cesium.com/learn/cesiumjs/ref-doc/Globe.html#pick`         | Elevation-aware picking helpers (if used)                   | Used for ray-terrain intersection; ensure correct camera/ray setup and null handling. |
| `ScreenSpaceEventHandler`         | `https://cesium.com/learn/cesiumjs/ref-doc/ScreenSpaceEventHandler.html` | `CesiumGlobe.tsx` input utilities                           | Central handler for click/drag/scroll; wired to React event layer and Focus Mode interactions. |

> **Implementation note:** All picking flows must be **wrapped** in KFM utilities, not called ad-hoc, to keep provenance and CARE handling consistent.

---

## 🏔️ 3. Terrain Sampling & Height APIs

| API                                | Upstream Doc URL (indicative)                                               | KFM Usage Location(s)                                        | Notes / Migration Guidance                                                      |
|------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------|
| `sampleTerrainMostDetailed`        | `https://cesium.com/learn/cesiumjs/ref-doc/sampleTerrainMostDetailed.html`  | Terrain probe / elevation tools (hydrology, archaeology)     | Use for high-accuracy DEM sampling; batch queries when possible to reduce load. |
| `Globe#getHeight`                  | `https://cesium.com/learn/cesiumjs/ref-doc/Globe.html#getHeight`            | Quick, approximate height lookups                            | Fast but may be approximate; acceptable for cursors & rough context only.      |
| `Camera#pickEllipsoid`            | `https://cesium.com/learn/cesiumjs/ref-doc/Camera.html#pickEllipsoid`       | Fallback lat/lon picking when terrain data is unavailable    | Use in low-detail scenes or fallback paths; ensure proper ellipsoid handling.  |

> For any terrain-related feature, KFM should prefer **batch APIs** (e.g., `sampleTerrainMostDetailed`) over many single calls in tight loops.

---

## 🖼️ 4. Billboards, Labels & Glyph Rendering

| API / Class                | Upstream Doc URL (indicative)                                                  | KFM Usage Location(s)                                       | Notes / Migration Guidance                                                                 |
|----------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `BillboardCollection`      | `https://cesium.com/learn/cesiumjs/ref-doc/BillboardCollection.html`           | Glyph layers for heritage, hydrology, sensor overlays       | Used for icon glyphs; v1.136 fixes depth + scaling issues. Keep all glyphs routed via wrapper components. |
| `LabelCollection`          | `https://cesium.com/learn/cesiumjs/ref-doc/LabelCollection.html`               | Text labels and annotations                                 | Used for site names, gauge IDs, etc.; verify halos and outlines after 1.136 upgrade.      |
| `Entity` (billboards/labels)| `https://cesium.com/learn/cesiumjs/ref-doc/Entity.html`                       | Higher-level entity-based layers (if used)                  | Where entities are used, ensure styling aligns with depth-test & label/halo fixes.         |

> Any new glyph layer should document its use of `BillboardCollection`/`LabelCollection` in the appropriate KFM component, with CARE/visibility rules.

---

## 🧱 5. 3D Tiles & Imagery Layer APIs

| API / Class           | Upstream Doc URL (indicative)                                                  | KFM Usage Location(s)                                        | Notes / Migration Guidance                                                                 |
|-----------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `Cesium3DTileset`     | `https://cesium.com/learn/cesiumjs/ref-doc/Cesium3DTileset.html`               | 3D Tilesets registered in `web/cesium/layers/tilesets.json` | Primary primitive for buildings, heritage structures, and other 3D tiles; ensure provenance IDs are linked. |
| `ImageryLayer`        | `https://cesium.com/learn/cesiumjs/ref-doc/ImageryLayer.html`                  | STAC imagery overlays, base imagery                          | Used for STAC-driven and base imagery; all imagery providers must be declared in `cesium-providers.json`. |
| `UrlTemplateImageryProvider` / other providers | `https://cesium.com/learn/cesiumjs/ref-doc/UrlTemplateImageryProvider.html` | Imagery entries in `web/cesium/config/cesium-providers.json` | Provider types must match registry definitions; new providers require governance review.   |

> All tilesets/imagery used in KFM must go through the **provider & layer registry**; no inline, hard-coded URLs in components.

---

## 🧪 6. Input & Timeline Utilities

| API / Class                  | Upstream Doc URL (indicative)                                                | KFM Usage Location(s)                                      | Notes / Migration Guidance                                                       |
|------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------|
| `ScreenSpaceEventHandler#setInputAction` | `https://cesium.com/learn/cesiumjs/ref-doc/ScreenSpaceEventHandler.html#setInputAction` | Input bindings in Cesium wrapper components               | Used for click/drag handling; always wrap to enforce CARE-aware interaction flows. |
| `Timeline` / `Clock` / `ClockViewModel`  | `https://cesium.com/learn/cesiumjs/ref-doc/Timeline.html`<br>`Clock.html` | `CesiumTimelineScene.tsx`                                 | Used for time-based scenes; must integrate with Focus Mode’s time model and Story Nodes. |

---

## 📎 7. How to Add or Update API Entries

When KFM begins to **depend on a new Cesium API** or modifies how an existing one is used:

1. **Identify** the API and its upstream doc URL.  
2. **Add or update** the corresponding row in the appropriate table above:
   - Scene/picking, terrain, glyphs, tilesets/imagery, or input/timeline.  
3. **Reference** the KFM usage location(s):
   - File names, components, or layer registry entries.  
4. **Document** any migration or behavior notes:
   - “New in v1.136”, “Deprecated in vX”, or any integration caveats.  
5. **Run CI**:
   - Ensure markdown and link checks pass.

When upgrading beyond v1.136:

- A **new API index** for the new version should be placed under  
  `web/cesium/releases/<new-version>/references/api-links.md`,  
  leaving this file as the historical record for v1.136.

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (API Index & Annotations)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium v1.136 References](README.md) · [⬅ Back to Cesium v1.136 Release Notes](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../../README.md)

</div>
