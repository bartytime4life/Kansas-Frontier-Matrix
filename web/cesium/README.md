---
title: "🌍 KFM v11.2.3 — Cesium Web Integration Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed overview of CesiumJS integration in the Kansas Frontier Matrix web stack, including directory layout, architecture, telemetry, and governance for 3D geospatial visualization."
path: "web/cesium/README.md"
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
doc_uuid: "urn:kfm:doc:web-cesium-overview-v11-2-3"
semantic_document_id: "kfm-web-cesium-overview-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:overview:v11.2.3"

sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Subsystem Overview"
intent: "web-cesium-subsystem"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌍 **Kansas Frontier Matrix — Cesium Web Integration Overview**  
`web/cesium/README.md`

**Purpose:**  
Define the **governed integration contract** for CesiumJS within the KFM web stack, including directory layout, architecture, performance/telemetry hooks, and FAIR+CARE governance for 3D geospatial visualization.

</div>

---

## 📘 1. Overview

CesiumJS is the primary **3D globe and scene engine** used by KFM for:

- 3D Tiles (sites, buildings, terrain, archives)  
- Time-dynamic STAC overlays (climate, hydrology, atmosphere, land use)  
- Archaeology and heritage Story Nodes rendered in 3D context  
- Combined **MapLibre + Cesium dual-view** experiences in Focus Mode  

This document governs:

- How Cesium is organized under `web/cesium/`  
- How Cesium integrates with React, MapLibre, and Story Nodes  
- How performance & errors are measured (telemetry)  
- How FAIR+CARE and sovereignty constraints are respected in 3D views  

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/
│
├── 📄 README.md                             # This file — Cesium web integration overview
│
├── ⚙️ config/                               # Cesium-specific configuration & wiring
│   ├── 📄 cesium-env.example.json           # Example env config (keys, asset paths, toggles)
│   ├── 📄 cesium-providers.json             # Allowed imagery/terrain/tileset providers (governed)
│   └── 📄 cesium-feature-flags.json         # Feature toggles (async pick, debug layers, etc.)
│
├── 🧩 components/                           # React/TS components wrapping CesiumJS
│   ├── 📄 CesiumGlobe.tsx                   # Main globe wrapper (camera, base layers, controls)
│   ├── 📄 CesiumTimelineScene.tsx          # Timeline-aware globe (Story Nodes, Focus Mode)
│   ├── 📄 CesiumRegionOverlay.tsx          # Cultural region & hydrology overlays (polygons/H3)
│   └── 📄 CesiumDebugLayerToggle.tsx       # Optional debug overlay controller
│
├── 🗺️ layers/                              # Layer wiring between KFM data + Cesium primitives
│   ├── 📄 tilesets.json                     # Registry of 3D Tilesets used by KFM
│   ├── 📄 regions.json                      # Cultural region ↔ Cesium layer mapping
│   └── 📄 sensors.json                      # Sensor/telemetry overlays for Cesium
│
├── 🧪 tests/                                # Visualization + interaction smoke tests
│   ├── 📄 rendering-smoke.md                # Manual/CI test scenarios for Cesium views
│   └── 📄 perf-baseline.md                  # Guidance for performance baselines (FPS, latency)
│
├── 🗄️ releases/                            # Versioned CesiumJS release notes (governed)
│   └── 1.136/
│       └── 📄 README.md                     # CesiumJS v1.136 KFM-governed release notes
│
└── 📚 docs/                                 # Additional Cesium-specific documentation
    ├── 📄 integration-patterns.md           # Patterns for React, MapLibre, Focus Mode
    ├── 📄 governance-hooks.md               # How FAIR+CARE, sovereignty, masking apply in 3D
    └── 📄 troubleshooting.md                # Common Cesium issues & remediation in KFM
~~~

**Layout notes:**

- **Releases** are governed per-version (e.g., `releases/1.136/README.md`).  
- **components/** encapsulate Cesium usage so downstream code never talks to raw Cesium randomly.  
- **layers/** map KFM concepts (regions, tilesets, sensors) to Cesium primitives in a **governed, declarative** way.  

---

## 🧱 3. Architecture & Integration Model

### 3.1 Core Principles

KFM Cesium integration follows these rules:

- **Wrapper-first:** all Cesium usage goes through **typed React/TS components**.  
- **Declarative data wiring:** layers are described in JSON registries, not hard-coded.  
- **Provenance-aware:** layers know which datasets/tilesets they visualize and can surface provenance & CARE info.  
- **Focus Mode-aware:** globe interactions are always compatible with Story Node + timeline semantics.

### 3.2 Integration Layers

1. **React + Cesium Wrapper Components**  
   - `components/CesiumGlobe.tsx`  
   - `components/CesiumTimelineScene.tsx`  

   Responsibilities:
   - Create and manage Cesium `Viewer` / `Scene`.  
   - Register input handlers (click, hover, camera changes).  
   - Bridge camera state with React + URL state.

2. **Layer Registries (`layers/*.json`)**  
   - Link **KFM data IDs** → **Cesium primitives**:  
     - 3D Tilesets  
     - Imagery layers  
     - Region polygons / H3 mosaics  
     - Sensor overlays  

   Each entry includes:
   - Data ID / STAC or registry reference  
   - CARE / visibility policy hints  
   - Provenance pointer(s)

3. **Config (`config/*.json`)**  
   - Provider endpoints (Cesium Ion, self-hosted terrain, 3D Tiles endpoints).  
   - Feature flags (async pick, debug overlays, experimental tilesets).  
   - Environment-specific toggles (dev, staging, prod).

---

## 🧠 4. Focus Mode & Story Node Integration

Cesium is used in **two primary Focus Mode patterns**:

1. **Globe Context Panel**  
   - Displays regions, tilesets, and site clusters relevant to the active Story Node.  
   - Uses **asynchronous picking** (`scene.pickAsync`) to show provenance & CARE badges on click/hover.  

2. **Timeline-Linked Scene**  
   - Uses `CesiumTimelineScene.tsx` for time-linked visualizations.  
   - Binds Cesium’s built-in timeline or custom time controls to:
     - STAC imagery  
     - 3D Tiles with epoch-based visibility  
     - Hydrology or climate time series  

Key rules:

- Every interaction must be explainable in terms of **Story Node + dataset + provenance**.  
- No direct user-facing Cesium state without a corresponding **KFM object** behind it.

---

## 🗺️ 5. Data, Providers & Provenance

### 5.1 Providers

All Cesium providers used in KFM must be declared in:

- `config/cesium-providers.json`

Each provider entry includes:

- Provider ID (e.g., `"terrain-kfm-primary"`)  
- Type (`"terrain"`, `"imagery"`, `"3d-tiles"`)  
- Endpoint/URL  
- License / usage notes  
- CARE or sovereignty notes (if applicable)

### 5.2 Tilesets & Layers

3D Tilesets and thematic layers are declared in:

- `layers/tilesets.json`  
- `layers/regions.json`  
- `layers/sensors.json`

Each entry includes:

- `kfm:data_id` or STAC/registry reference  
- Provider IDs and URLs  
- CARE constraints and visibility rules (e.g., `"polygon-generalized"`, `"h3-only"`)  
- PROV-O provenance link(s)

### 5.3 Provenance Path

For every visualized object (site, region, tileset):

1. **KFM dataset / STAC entry**  
2. **Provenance log** (PROV-O)  
3. **Layer registry entry**  
4. **Cesium primitive** (tile, primitive, entity, etc.)  

This chain must be **unbroken** and testable in CI.

---

## 📊 6. Performance & Telemetry (FAIR+CARE)

Telemetry for Cesium is:

- **Opt-in**  
- **Hash/redaction-first** for any potentially identifying signals  
- Used only for **performance & reliability**, not user tracking

### 6.1 Metrics (Indicative)

- Picking latency (`scene.pickAsync`)  
- Terrain sampling latency (DEM queries)  
- Frame time statistics (mean, p95, p99)  
- Tile load counts & errors  
- GPU memory pressure indicators (if available)

### 6.2 Schema & Storage

- Schema: `../schemas/telemetry/web-cesium-release-v1.json`  
- Storage: `../releases/v11.2.3/web-cesium-telemetry.json`  

Telemetry is consumed by:

- CI dashboards  
- Ops & reliability tooling  
- The **KFM performance SLO/Error Budget** framework

---

## ⚖ 7. FAIR+CARE, Sovereignty & Masking

Cesium must respect the **same governance constraints** as 2D maps:

- **Location masking** for sensitive sites or regions:  
  - Use **H3-only** or region-level generalized polygons where required.  
  - Never expose raw coordinates for sensitive archaeological or cultural locations.  

- **Zoom-level constraints:**  
  - Some layers may be visible only at certain zooms.  
  - Tilesets or overlays may be completely disabled in public deployments.  

- **Provenance & CARE surfacing:**  
  - On click/hover, globe UI should be able to display:
    - Source dataset  
    - CARE label + sensitivity  
    - Short provenance chip  

Rules and patterns for this live in:

- `docs/web/cesium/docs/governance-hooks.md` (referenced above)

---

## 🧪 8. Testing & CI Expectations

Cesium integration participates in **web CI** via:

- Unit tests and integration harnesses (if present)  
- Manual/automated scenarios described in:

  - `web/cesium/tests/rendering-smoke.md`  
  - `web/cesium/tests/perf-baseline.md`

CI expectations:

- No uncontrolled console errors in core scenes.  
- Basic smoke scenes render without:
  - Tile flood  
  - Exception spam  
  - Frozen camera or pick handlers  

Where possible, CI should collect a small **performance snapshot** to detect regressions across releases.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial governed Cesium web integration overview; aligned directory layout, config, layers, governance, and telemetry with CesiumJS v1.136 and KFM-MDP v11.2.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Integration Code & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Web Root](../README.md) · [⬅ Back to Cesium Releases](./releases/1.136/README.md)

</div>
