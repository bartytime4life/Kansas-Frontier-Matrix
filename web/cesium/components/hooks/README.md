---
title: "🪝 KFM v11.2.3 — Cesium Web Hooks Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed React/TypeScript hooks for CesiumJS integration in the Kansas Frontier Matrix web stack: viewer lifecycle, picking, terrain sampling, and layer wiring."
path: "web/cesium/components/hooks/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 hook-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-hooks-v11-2-3"
semantic_document_id: "kfm-web-cesium-hooks-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:components:hooks:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Hook Library Overview"
intent: "web-cesium-hooks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🪝 **Kansas Frontier Matrix — Cesium Web Hooks Library**  
`web/cesium/components/hooks/README.md`

**Purpose:**  
Define the **governed React/TypeScript hook layer** that encapsulates CesiumJS usage in KFM, covering:  
viewer lifecycle, picking, terrain sampling, and layer wiring — all in a FAIR+CARE-aware way.

</div>

---

## 📘 1. Overview

Hooks under `web/cesium/components/hooks/`:

- Provide **shared Cesium logic** for all KFM Cesium components.  
- Are the **only allowed place** to manage low-level Cesium state in React.  
- Enforce:
  - Consistent use of **`scene.pickAsync`**  
  - Batched, cache-aware **terrain sampling**  
  - Layer wiring based on **governed registries** (providers, layers, regions)  
  - CARE/sovereignty-sensitive behavior for visibility and interaction

Downstream application code should call:

- `CesiumGlobe.tsx`, `CesiumTimelineScene.tsx`, etc.  
- Those components then compose these hooks.

For the broader components overview, see:

- `web/cesium/components/README.md`

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/components/hooks/
│
├── 📄 README.md                     # This file — hook library overview & contracts
│
├── 🌐 useCesiumViewer.ts            # Viewer lifecycle, providers, and event wiring
├── 🎯 useCesiumPicking.ts           # Async picking (scene.pickAsync) + KFM entity mapping
├── 🏔️ useCesiumTerrainSampling.ts    # Batched terrain sampling, caching, and throttling
└── 🗺️ useCesiumLayers.ts            # Layer registry → Cesium primitives (tilesets, regions, sensors)
~~~

**Directory contract:**

- All hooks must be **typed** (TypeScript) and **side-effect scoped** to React lifecycles.  
- Hooks should not:
  - Directly touch global variables.  
  - Bypass KFM provider/layer registries.  
  - Ignore CARE/sovereignty hints passed via props/registries.

---

## 🌐 3. `useCesiumViewer.ts` — Viewer Lifecycle & Providers

**Responsibility:**

- Create, configure, and manage the lifecycle of `Cesium.Viewer` within a React component.  

**Key behaviors:**

- Initialize `Viewer` using:
  - `CESIUM_BASE_URL` and other envs derived from KFM config (`web/cesium/config/cesium-env.example.json`).  
  - Provider IDs from `web/cesium/config/cesium-providers.json`.

- Wire:
  - Base imagery and terrain providers by ID.  
  - Default camera settings (startup view, world extents).  
  - Basic event handlers (resize, error logging hooks).

**Contract:**

- Returns:
  - `viewer` (or a typed wrapper)  
  - References to `scene`, `camera`, `globe` as needed  
  - A clean-up function (or `useEffect` return) that **destroys** the Viewer correctly.

- **No** direct DOM manipulation beyond the React ref/container.  
- Errors during initialization must be:
  - Logged via KFM logging utilities.  
  - Optionally surfaced via telemetry.

---

## 🎯 4. `useCesiumPicking.ts` — Async Picking & Entity Mapping

**Responsibility:**

- Encapsulate **all picking logic** using **`scene.pickAsync`** as the primary API.

**Core pattern (conceptual):**

- Accepts:
  - `viewer` / `scene` reference.  
  - KFM mapping functions (e.g., entity ID resolvers).  
  - Optional filters (e.g., layers or entity classes to consider).

- Exposes:
  - `pickAt(windowPosition)` → Promise of a **KFM pick result**:
    - `{ type, id, datasetId, provenanceRef, careMetadata, rawCesiumObject, ... }`

**Behavioral requirements:**

- Use `scene.pickAsync(...)` whenever available.  
- Catch and handle:
  - Promise rejections.  
  - Null results.  
  - Expected “no hit” cases gracefully.

- Integrate CARE/provenance:

  - Map raw Cesium primitives/entities to KFM **dataset + provenance + CARE** metadata.  
  - Redact or aggregate sensitive results (e.g., hide exact site when policy demands generalized regions).

**Governance:**

- No direct `scene.pick(...)` usage inside this hook except as:
  - Documented, temporary fallback.  
- All call sites should go through this hook or a thin controller using it.

---

## 🏔️ 5. `useCesiumTerrainSampling.ts` — DEM Sampling & Caching

**Responsibility:**

- Provide a **managed interface** for terrain height sampling, using Cesium terrain APIs.

**Inputs:**

- `terrainProvider` (from Viewer or explicit)  
- Sampling options:
  - Strategy: `"batch"` vs `"single"`  
  - Desired resolution / LOD hints  

**Features:**

- Offers APIs such as:

  - `sampleHeights(points: Cartographic[]): Promise<number[]>`  
  - `sampleProfile(line: LineStringLike, options)`

- Uses:
  - `sampleTerrainMostDetailed` for **batch** sampling where appropriate.  
  - `globe.getHeight` for **fast cursors / low-accuracy** cases.

**Performance & caching:**

- Implements caching keyed on:
  - Provider ID  
  - Rounded lat/lon (configurable precision)

- Optional rate limiting:
  - Avoids firing large numbers of terrain requests per frame.  
  - May batch calls when multiple samples are requested in a short time.

**Governance:**

- Must respect CARE:
  - Terrain inspection for sensitive regions should not accidentally expose sensitive features without proper masking/hints.  
  - For example, certain tools may need to be disabled or aggregated in CARE-restricted regions.

---

## 🗺️ 6. `useCesiumLayers.ts` — Layer Registry → Primitives

**Responsibility:**

- Translate **KFM layer registries** into Cesium primitives and manage their lifecycle.

**Inputs:**

- Layer configuration from:
  - `web/cesium/layers/tilesets.json`  
  - `web/cesium/layers/regions.json`  
  - `web/cesium/layers/sensors.json` (or similar)

- Options:
  - Which layer IDs to enable.  
  - Zoom or time filters.  
  - CARE/visibility constraints.

**Outputs:**

- A managed collection of:
  - `Cesium3DTileset` instances  
  - `ImageryLayer` instances  
  - Region polygons / H3 primitives  
  - Glyph/label layers

**Responsibilities:**

- Mount/unmount primitives in the Viewer scene.  
- Apply styling from layer configs.  
- Enforce CARE rules:

  - Use polygons vs H3 based on `care.visibility_rules`.  
  - Disable or coarsen layers when sensitivity demands.

---

## 📊 7. Telemetry, Logging & Error Handling in Hooks

Hooks must:

- Route relevant metrics into the telemetry pipeline (where appropriate), e.g.:

  - `useCesiumPicking.ts`: pick latency, success/failure counts.  
  - `useCesiumTerrainSampling.ts`: sampling durations, error counts.  

- Use **centralized logging** utilities for errors:
  - Avoid `console.log`/`console.error` scattered inside hooks (except maybe in dev-only branches).  
  - Surface **aggregate** telemetry into `web-cesium-telemetry.json` via the configured schema.

Error handling principles:

- Hooks should **fail fast** in dev and:  
  - Return safe defaults or raise explicit errors.  
- In production profiles, hooks should:
  - Avoid breaking the entire scene on recoverable issues.  
  - Prefer to disable a misbehaving layer or fall back to simpler behavior.

---

## ⚖ 8. FAIR+CARE & Sovereignty Considerations

Hook-level responsibilities:

- **`useCesiumPicking`**  
  - Must enforce redaction/aggregation rules **before** exposing results to components.  
  - Example: if a pick targets a sensitive site, the hook may:
    - Return a generalized “region” result instead of a site ID.  

- **`useCesiumLayers`**  
  - Must interpret CARE metadata from layer configs and:
    - Hide certain layers entirely in public deployments.  
    - Replace detailed geometry with generalized/H3 layers as required.  

- **`useCesiumTerrainSampling`**  
  - Must avoid providing high-resolution sampling in zones where it would expose sensitive context beyond policy.

If CARE rules change in KFM:

- These hooks are one of the **primary enforcement points** for Cesium interactions.

---

## 🧭 9. Authoring & Maintenance Workflow

When adding or updating a hook:

1. **Design for reuse**:
   - Hooks should be composable and focused on a single responsibility.  

2. **Document in this README**:
   - Add or update sections for new hooks.  
   - Briefly describe responsibilities and key invariants.

3. **Type & test**:
   - Ensure hooks are fully typed.  
   - Add unit/integration tests where practical (especially for complex logic).

4. **Wire telemetry and logging**:
   - Decide which metrics/errors matter.  
   - Hook into telemetry/logging utilities accordingly.

5. **CARE & governance review**:
   - Confirm new behaviors are consistent with FAIR+CARE policies.  
   - Review with Web Visualization Systems WG + FAIR+CARE Council for high-impact changes.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial governed Cesium hooks overview; defined contracts for viewer, picking, terrain sampling, and layer wiring with CARE/provenance alignment. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Hooks Library)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Components Overview](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../README.md) · [⬅ Back to Web Root](../../../README.md)

</div>
