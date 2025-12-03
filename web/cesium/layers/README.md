---
title: "🗺️ KFM v11.2.3 — Cesium Layer Registry & Mappings (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed registry for wiring Kansas Frontier Matrix (KFM) datasets, regions, and sensors into CesiumJS layers in the web stack."
path: "web/cesium/layers/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 layer-registry compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-layers-registry-v11-2-3"
semantic_document_id: "kfm-web-cesium-layers-registry-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:layers:registry:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Subsystem Registry"
intent: "web-cesium-layers-registry"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Cesium Layer Registry & Mappings**  
`web/cesium/layers/README.md`

**Purpose:**  
Define the **governed, declarative layer registry** that connects KFM datasets, regions, and sensors to **CesiumJS** primitives (3D Tiles, imagery, region overlays, sensor glyphs) in the web stack, with explicit **provenance** and **FAIR+CARE** constraints.

</div>

---

## 📘 1. Overview

The `web/cesium/layers/` registry is the **single source of truth** for:

- Which **datasets** appear as layers in Cesium  
- How those layers are **styled**, **masked**, and **gated by CARE**  
- How each layer is linked to:
  - STAC / dataset IDs  
  - PROV-O provenance logs  
  - Governance & sovereignty constraints  

No Cesium layer should be created in application code without a corresponding **registry entry** here.

This document focuses on:

- Directory layout and file roles  
- The JSON **contract** for layer entries  
- Integration with provenance, metadata, and telemetry  
- FAIR+CARE and sovereignty rules around visibility and masking  

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/layers/
│
├── 📄 README.md                     # This file — Cesium layer registry overview & contract
│
├── 🧱 tilesets.json                 # 3D Tileset registry (sites, buildings, volumetric tiles)
├── 🗺️ regions.json                  # Region overlays registry (cultural regions, hydrology, basins)
├── 📡 sensors.json                  # Sensor/telemetry overlays (gauges, stations, instruments)
│
└── 🧩 schemas/                      # Optional local schemas for layer JSON (if not in global schemas/)
    ├── 📄 tilesets.schema.v1.json
    ├── 📄 regions.schema.v1.json
    └── 📄 sensors.schema.v1.json
~~~

**Directory contract:**

- **This README** defines the layer registry contract and KFM governance.  
- JSON registry files (`tilesets.json`, `regions.json`, `sensors.json`) are **declarative**, **CI-validated**, and **graph-safe**.  
- `schemas/` is optional; global schemas under `schemas/web/` may also be used.  

---

## 🧩 3. Common Layer Entry Contract

All layer registries share a **common core** structure:

- **`id`** — local layer identifier (used in web code & feature flags)  
- **`kfm_data_id`** — link to the KFM dataset/STAC/registry ID  
- **`provider_id`** — entry in `web/cesium/config/cesium-providers.json`  
- **`kind`** — `"tileset"`, `"region"`, `"sensor"`, etc.  
- **`visibility`** — initial on/off + zoom constraints  
- **`care`** — CARE + masking semantics  
- **`provenance`** — pointers into PROV-O & metadata

Illustrative (conceptual) shape:

~~~json
{
  "id": "smoky-hill-drainage-tileset",
  "kfm_data_id": "urn:kfm:data:tileset:smoky-hill-drainage-v1",
  "provider_id": "terrain-kfm-primary",
  "kind": "tileset",
  "visibility": {
    "default_enabled": true,
    "min_zoom": 4,
    "max_zoom": 14,
    "modes": ["focus-mode", "debug-3d"]
  },
  "care": {
    "sensitivity": "generalized",
    "visibility_rules": "polygon-generalized",
    "notes": "Generalized drainage extents only; no site-level detail."
  },
  "provenance": {
    "stac_id": "kfm-tiles-smoky-hill-drainage-v1",
    "provenance_ref": "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/smoky-hill-region-v1.json"
  }
}
~~~

> **Important:** Actual validation rules live in the JSON schemas referenced by CI. This snippet is illustrative only.

---

## 🧱 4. `tilesets.json` — 3D Tileset Layers

### 4.1 Purpose

`tilesets.json` describes all **3D Tiles** layers:

- Archaeology & heritage tilesets (sites, excavations, reconstructions)  
- Built environment (structures, terrain-aligned models)  
- Environmental & hydrological 3D Tiles (where applicable)  

### 4.2 Required Fields (per tileset entry)

Each entry MUST include:

- `id` — stable layer ID (e.g., `"flint-hills-heritage-tileset"`)  
- `kfm_data_id` — dataset/tileset registry ID  
- `provider_id` — Cesium provider configuration ID  
- `url` — Tileset URL (from provider configuration or absolute)  
- `kind` = `"tileset"`  
- `visibility` block:
  - `default_enabled` (bool)  
  - `min_zoom`, `max_zoom` (integers)  
- `care` block:
  - `sensitivity` (`"generalized"` / `"restricted-generalized"`)  
  - `visibility_rules` (e.g., `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`)  
- `provenance` block:
  - `stac_id` or equivalent  
  - `provenance_ref` path/URN (PROV-O log)

Optional:

- `style` theme ID  
- `debug_only` flag  
- `region_slug` (for cultural region association)

---

## 🗺️ 5. `regions.json` — Region Overlay Layers

### 5.1 Purpose

`regions.json` is the wiring table for:

- **Cultural landscape regions** (Flint Hills, Smoky Hill, Arkansas River Basin, etc.)  
- Hydrological & drainage regions  
- Administrative or analysis regions used in Focus Mode context

Each entry maps a **KFM region** to:

- One or more Cesium primitives (polygons, H3 mosaics, extruded overlays)  
- CARE-driven **visibility/masking** logic

### 5.2 Required Fields (per region layer)

- `id` — layer ID (e.g., `"flint-hills-region-overlay"`)  
- `region_slug` — e.g., `"flint-hills-region"`  
- `kfm_data_id` — region dataset/metadata ID  
- `provider_id` — region geometry source (if using a tileset/provider)  
- `kind` = `"region"`  
- `geometry_type` — `"polygon"`, `"h3"`, `"mixed"`  
- `visibility`:
  - `default_enabled`  
  - `min_zoom`, `max_zoom`  
- `care`:
  - `sensitivity`  
  - `visibility_rules` (e.g., `"polygon-generalized"`, `"h3-only"`)  
  - `notes`  

- `provenance`:
  - `stac_id` (region STAC item/collection)  
  - `provenance_ref` (PROV-O log for the region)

These entries are how we **enforce** region-level constraints in Cesium:

- For `"h3-only"` regions, region polygons may not be shown at certain zooms.  
- For sensitive regions, overlays may be disabled in public modes entirely.

---

## 📡 6. `sensors.json` — Sensor & Telemetry Layers

### 6.1 Purpose

`sensors.json` lists layers representing:

- Stream gauges  
- Weather & atmospheric sensors  
- Other spatially anchored instruments & time series

### 6.2 Required Fields (per sensor layer)

- `id` — layer ID (e.g., `"ks-hydrology-stream-gauges"`)  
- `kfm_data_id` — dataset ID for the sensor network  
- `provider_id` — data/tiles provider (if applicable)  
- `kind` = `"sensor"`  
- `symbol` — icon ID / glyph theme  
- `visibility`:
  - `default_enabled`  
  - `min_zoom`, `max_zoom`  

- `care`:
  - `sensitivity`  
  - `visibility_rules`  
  - `notes` (e.g., aggregation or anonymization behavior)

- `provenance`:
  - `metadata_ref` (dataset/registry entry)  
  - `provenance_ref` (sensor provenance / lineage log)

Sensors may have **time series**; the layer registry should not include raw series, but must indicate:

- Whether there is **time-dependent styling**  
- How Focus Mode should treat click/hover interactions (e.g., open time series panel)

---

## ⚖ 7. FAIR+CARE & Sovereignty Rules for Layers

All layer entries must:

- **Respect CARE constraints** defined at the dataset/region level:
  - No layer may expose detail beyond dataset-level governance.  
  - `"restricted-generalized"` layers may only appear in internal modes.  

- **Declare visibility rules**:
  - `"polygon-generalized"` — polygon overlays at region scale only.  
  - `"h3-only"` — use only H3 mosaics; hide underlying polygons.  
  - `"no-exact-boundaries"` — no exact boundaries; rely on shading or coarse cells.

- **Integrate sovereignty constraints**:
  - Certain layers may be completely disabled in public deployments.  
  - Sensitive overlays must never be toggle-able without corresponding governance mode.

Any change that alters `care.sensitivity` or `care.visibility_rules` in a layer entry is a **governance event** and must be:

1. Reflected first in dataset provenance and metadata.  
2. Approved via FAIR+CARE + sovereignty review.  
3. Updated in the layer registry and validated by CI.

---

## 📊 8. Telemetry & Performance Hooks (Optional)

While `web/cesium/layers/` is primarily configuration, layers may be annotated for **telemetry correlation**, e.g.:

- `telemetry_tag` — short ID used in telemetry metrics (e.g., `"tileset:smoky-hill"`)  
- `perf_expectation` — `"low"`, `"medium"`, `"high"` (expected cost)

Telemetry is defined globally in:

- Schema: `../../schemas/telemetry/web-cesium-release-v1.json`  
- Data: `../../releases/v11.2.3/web-cesium-telemetry.json`

Telemetry consumers can:

- Track frame time impact by layer tag  
- Flag extremely heavy layers for optimization or offline usage

---

## 🧪 9. CI & Validation Expectations

Layer registries are **CI-enforced**. Typical jobs:

- `web-cesium-layers-validate.yml` (or equivalent), responsible for:
  - JSON schema validation (`tilesets.schema.v1.json`, `regions.schema.v1.json`, `sensors.schema.v1.json` or global equivalents)  
  - Cross-link checks with:
    - Provider config (`web/cesium/config/cesium-providers.json`)  
    - Dataset registries / STAC IDs  
    - Provenance logs & metadata  

CI must **block**:

- Layers referencing unknown providers or dataset IDs.  
- CARE/visibility values that conflict with dataset/region metadata.  
- Registries that fail schema or introduce duplicate `id`/`kfm_data_id` collisions without explicit override logic.

---

## 🧭 10. Authoring & Maintenance Workflow

When adding or updating a Cesium layer:

1. **Define or update the dataset/region**  
   - Dataset registry, STAC, and provenance must exist or be created.

2. **Update provider config (if needed)**  
   - Add or adjust provider entries in `web/cesium/config/cesium-providers.json`.

3. **Add or modify layer entry**  
   - Update `tilesets.json`, `regions.json`, or `sensors.json` with:
     - IDs, providers, visibility, CARE block, and provenance references.

4. **Run local validation**  
   - Execute layer validation/CI scripts (e.g., `make validate-web-cesium-layers`).

5. **Submit PR & governance review**  
   - Ensure FAIR+CARE & sovereignty checks are satisfied.  
   - Confirm UI/UX behavior in Focus Mode & Story Nodes where applicable.

---

## 🕰️ 11. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Established governed Cesium layer registry contract; defined tilesets/regions/sensors JSON layouts, CARE rules, provenance hooks, and CI expectations for KFM v11.2.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Layer Registry & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Web Overview](../README.md) · [⬅ Back to Web Root](../..//README.md)

</div>