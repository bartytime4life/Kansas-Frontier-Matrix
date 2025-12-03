---
title: "🧩 KFM v11.2.3 — Cesium Layer Registry Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed JSON schema contracts for Cesium layer registries (tilesets, regions, sensors) in the KFM web stack."
path: "web/cesium/layers/schemas/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v11.2.3 layer-registry-schema compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:web-cesium-layers-schemas-v11.2.3"
semantic_document_id: "kfm-web-cesium-layers-schemas-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:layers:schemas:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-cesium-release-v1.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Schema Overview"
intent: "web-cesium-layers-schemas"
status: "Active · Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "SoftwareApplication"
  cidoc: "E73 Information Object"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/web-cesium-layers-schemas-v1.json"
shape_schema_ref: "../../../schemas/shacl/web-cesium-layers-schemas-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded on next breaking Cesium layer schema update"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Cesium Layer Registry Schemas**  
`web/cesium/layers/schemas/README.md`

**Purpose:**  
Define the **JSON schema contracts** that govern the Cesium layer registries in KFM:

- `tilesets.json` — 3D Tileset layers  
- `regions.json` — cultural & environmental region overlays  
- `sensors.json` — sensor/telemetry overlays  

These schemas guarantee that all Cesium layer definitions are **machine-valid**, **graph-safe**, and **FAIR+CARE-aligned**.

</div>

---

## 📘 1. Overview

The Cesium layer registries under `web/cesium/layers/` are the **declarative wiring** between:

- KFM datasets / STAC entries / region registries  
- CesiumJS primitives (3D Tilesets, imagery, region overlays, glyphs)  
- CARE + sovereignty constraints and provenance

This directory:

- Holds **schema files** that describe the **valid shapes** of those registries.  
- Ensures every layer entry can be safely:
  - Loaded by web code  
  - Linked to provenance & governance metadata  
  - Interpreted by CI, ETL, and graph loaders

For the conceptual and operational overview of layers, see:

- `web/cesium/layers/README.md`  

---

## 🗂️ 2. Directory Layout

~~~text
web/cesium/layers/schemas/
├── 📄 README.md                          # This file — schema overview & contracts
│
├── 🧩 tilesets.schema.v1.json            # Schema for web/cesium/layers/tilesets.json
├── 🧩 regions.schema.v1.json             # Schema for web/cesium/layers/regions.json
└── 🧩 sensors.schema.v1.json             # Schema for web/cesium/layers/sensors.json
~~~

**Directory contract:**

- Each `*.schema.v1.json` file defines the **allowed shape** of its registry file.  
- New schema versions (e.g., `v2`) must **not** silently replace v1; they are added side-by-side and wired explicitly in CI.  
- Schemas in this directory may be referenced by:
  - Web CI workflows  
  - Validation scripts (e.g., `make validate-web-cesium-layers`)  
  - Documentation generators

---

## 🧩 3. Common Layer Schema Concepts

All three schemas share a common conceptual core:

- **Identity & linkage**
  - `id` — internal layer identifier used by web components  
  - `kfm_data_id` — KFM dataset / STAC / registry ID  
  - `provider_id` — Cesium provider configuration entry  

- **Kind & behavior**
  - `kind` — `"tileset"`, `"region"`, `"sensor"`, etc.  
  - `visibility` — default on/off, zoom bounds, modes (`focus-mode`, `debug-3d`, etc.)

- **Governance**
  - `care.sensitivity` — `"generalized"` / `"restricted-generalized"`  
  - `care.visibility_rules` — `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`, etc.  
  - `care.notes` — brief explanation of constraints

- **Provenance**
  - `provenance.stac_id` or equivalent dataset identifier  
  - `provenance.provenance_ref` — PROV-O log path/URN

The schemas enforce:

- Presence and **type correctness** of these fields  
- Prevention of layer definitions that omit CARE or provenance  
- Stable naming and value ranges for `kind`, `sensitivity`, visibility modes, etc.

---

## 🧱 4. `tilesets.schema.v1.json` — 3D Tileset Layers

**Target file:** `web/cesium/layers/tilesets.json`

### 4.1 Purpose

Validate 3D Tileset layer entries representing:

- Archaeology & heritage tilesets  
- Built environment models  
- Environmental (e.g., hydrology / DEM) 3D Tiles where applicable

### 4.2 Required Fields (per tileset entry)

The schema MUST require:

- `id` — string, unique within `tilesets.json`  
- `kfm_data_id` — string, link to KFM dataset/registry  
- `provider_id` — string, must match an existing provider in `web/cesium/config/cesium-providers.json`  
- `kind` — `"tileset"`  
- `url` — string (relative or absolute), valid tileset URL  
- `visibility` object:
  - `default_enabled` — boolean  
  - `min_zoom` — number/integer  
  - `max_zoom` — number/integer  

- `care` object:
  - `sensitivity` — enum (`"generalized"`, `"restricted-generalized"`)  
  - `visibility_rules` — enum (e.g., `"polygon-generalized"`, `"h3-only"`, `"no-exact-boundaries"`)  
  - `notes` — string (optional)

- `provenance` object:
  - `stac_id` — string (or equivalent dataset ID)  
  - `provenance_ref` — string path/URN to PROV-O log  

Optional additional fields (constrained by schema):

- `style` — string (styling theme ID)  
- `region_slug` — string (link into region registry)  
- `debug_only` — boolean

---

## 🗺️ 5. `regions.schema.v1.json` — Region Overlay Layers

**Target file:** `web/cesium/layers/regions.json`

### 5.1 Purpose

Validate region overlays representing:

- Cultural landscape regions (Flint Hills, Smoky Hill, Arkansas River Basin, etc.)  
- Hydrological basins, watersheds, and related spatial contexts

### 5.2 Required Fields (per region layer)

The schema MUST require:

- `id` — string, unique within `regions.json`  
- `region_slug` — string, matching an existing region (e.g., `"flint-hills-region"`)  
- `kfm_data_id` — string, link to region dataset/metadata  
- `provider_id` — optional string (if geometry is sourced via provider)  
- `kind` — `"region"`  
- `geometry_type` — enum (`"polygon"`, `"h3"`, `"mixed"`)  

- `visibility` object:
  - `default_enabled` — boolean  
  - `min_zoom` — number/integer  
  - `max_zoom` — number/integer  

- `care` object:
  - `sensitivity` — enum (`"generalized"`, `"restricted-generalized"`)  
  - `visibility_rules` — enum (e.g., `"polygon-generalized"`, `"h3-only"`)  
  - `notes` — string (optional but recommended for sensitive regions)

- `provenance` object:
  - `stac_id` — string (region STAC item/collection ID)  
  - `provenance_ref` — string path/URN for region PROV-O log  

Optional:

- `label` — string (UI label)  
- `style` — string (region style theme)  
- `modes` — array of strings indicating which app modes can see this layer

The schema ensures that **regions declared here** cannot omit CARE and provenance, and that they are structurally consistent with region datasets.

---

## 📡 6. `sensors.schema.v1.json` — Sensor & Telemetry Layers

**Target file:** `web/cesium/layers/sensors.json`

### 6.1 Purpose

Validate layers representing:

- Hydrology gauges  
- Atmospheric or environmental sensors  
- Other spatial sensors used in KFM overlays

### 6.2 Required Fields (per sensor layer)

The schema MUST require:

- `id` — string, unique within `sensors.json`  
- `kfm_data_id` — string, link to sensor dataset/registry  
- `provider_id` — string (if using a provider for tiles/vector data)  
- `kind` — `"sensor"`  
- `symbol` — string (glyph/icon ID in the KFM icon system)  

- `visibility` object:
  - `default_enabled` — boolean  
  - `min_zoom` — number/integer  
  - `max_zoom` — number/integer  

- `care` object:
  - `sensitivity` — enum (e.g., `"generalized"`, `"restricted-generalized"`)  
  - `visibility_rules` — enum (e.g., `"polygon-generalized"`, `"h3-only"`, `"point-aggregate"`)  
  - `notes` — string (e.g., aggregation/anonymization behavior)

- `provenance` object:
  - `metadata_ref` — string path/URN to sensor dataset metadata  
  - `provenance_ref` — string path/URN to PROV-O sensor provenance log  

Optional:

- `time_series_mode` — enum (`"point"`, `"aggregate"`, `"none"`)  
- `telemetry_tag` — short string used in performance/usage telemetry

---

## ⚖ 7. FAIR+CARE & Sovereignty Constraints in Schemas

These schemas enforce that:

- **No layer** can be defined without a **CARE block** (sensitivity + visibility rules).  
- **No layer** can omit **provenance references**.  
- Values for `sensitivity`, `visibility_rules`, and `kind` are restricted to **governed enums**, preventing ad hoc values in registries.

Governance implications:

- Adding a new enum value (e.g., new `visibility_rules` option) is a **schema change** and thus a **governance event**.  
- Weakening CARE constraints in the schema (e.g., making CARE optional) is **not allowed** for production schemas.

Any change to these schemas that affects CARE or sovereignty:

1. Must be documented and reviewed by the FAIR+CARE Council and sovereignty board.  
2. Must be versioned (e.g., `*.schema.v2.json`) rather than silently mutating v1.  

---

## 🧪 8. CI & Validation Integration

These schemas are wired into web CI, typically via:

- `web-cesium-layers-validate.yml` (or equivalent)

CI responsibilities:

- Validate:
  - `web/cesium/layers/tilesets.json` against `tilesets.schema.v1.json`  
  - `web/cesium/layers/regions.json` against `regions.schema.v1.json`  
  - `web/cesium/layers/sensors.json` against `sensors.schema.v1.json`  

- Cross-link checks (via CI scripts):
  - `provider_id` values must exist in `web/cesium/config/cesium-providers.json`.  
  - `region_slug` values must exist in region registries.  
  - `provenance_ref` paths must point to existing PROV-O logs.  
  - CARE fields consistent with dataset/region metadata.

CI MUST **fail** when:

- Registries violate schema.  
- CARE / sovereignty fields are missing or invalid.  
- Layers reference unknown datasets/providers/provenance.

---

## 🧭 9. Authoring & Maintenance Workflow for Schemas

When updating or adding Cesium layer schemas:

1. **Propose change & rationale**
   - New field? New enum? New version?  
   - Document why (new layer behavior, governance adjustment, etc.).

2. **Update or add schema file**
   - For breaking changes, create `*.schema.v2.json`.  
   - Keep `v1` for backward-compatible flows if needed.

3. **Update documentation**
   - Reflect changes in this `README.md`.  
   - Align `web/cesium/layers/README.md` and any developer docs.

4. **Wire into CI**
   - Update CI workflows to point to the correct schema versions.  
   - Add/update test fixtures for registries.

5. **Governance review**
   - FAIR+CARE, sovereignty, and web architecture reviewers sign off, especially on CARE-related changes.

6. **Merge & monitor**
   - After merge, monitor CI and runtime behavior for regressions.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial schema overview for Cesium layer registries; documented `tilesets.schema.v1.json`, `regions.schema.v1.json`, and `sensors.schema.v1.json` contracts; aligned with KFM-MDP v11.2.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Schema Definitions & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Layer Registry](../README.md) · [⬅ Back to Cesium Web Overview](../../README.md)

</div>