---
title: "📑 KFM v11 — Hazards Schema Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hazards-refresh/resources/schema/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/telemetry/autonomous-hazards-refresh.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomous-hazards-refresh-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Schema Module"
semantic_document_id: "kfm-hazards-schema-module-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hazards-refresh:resources:schema:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📑 **Hazards Schema Module (v11)**  
`src/pipelines/autonomous/hazards-refresh/resources/schema/README.md`

**Purpose:**  
Define and document the JSON Schemas used by the **Autonomous Hazards Refresh pipeline**.  
These schemas enforce **structural, unit, CRS, and semantic contracts** for normalized hazard events  
and generated STAC Items, ensuring deterministic, CI-enforced data quality.

</div>

---

# 📘 Overview

The `schema/` directory hosts the **authoritative JSON Schema definitions** that:

- Govern normalized hazard event tables (tabular/Parquet outputs)  
- Govern hazard-specific STAC Item metadata blocks  
- Align events with:
  - KFM **CRS Standard v11**  
  - **STAC Geospatial Spec v11**  
  - **Hydrology & Hazards Standards v11**  
  - **DCAT 3.0** and **PROV-O** lineage requirements  

All schemas here are:

- JSON Schema **draft 2020-12**  
- Versioned and pinned via this README  
- Required in CI checks before any hazards data is promoted  

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hazards-refresh/resources/schema/
│
├── README.md                 # This file (schema module overview)
└── hazards_v1.schema.json    # Core hazards event schema (normalized records)
```

Future schemas (e.g., `hazards_v2.schema.json`, STAC-specific schemas) MUST be added here and documented in this file.

---

# 🧬 hazards_v1.schema.json — Core Event Schema

This schema defines the structure and types for **normalized hazard events** produced by `normalize_events.py`.

## 🎯 Goals

- Provide a single canonical representation of hazards across:
  - NOAA Storm Events
  - NWS warnings
  - FEMA disasters
  - USGS earthquakes
- Enforce consistent units, CRS, and field naming
- Make events directly convertible into STAC Items and graph nodes

## 🧱 Required Top-Level Fields (Conceptual)

At a minimum, `hazards_v1.schema.json` MUST require:

- `EVENT_ID` (string; unique within provider)  
- `HAZARD_TYPE` (string; controlled vocabulary)  
- `SOURCE_SYSTEM` (string; e.g., `noaa`, `fema`, `usgs`)  
- `START_TIME` (string; ISO 8601)  
- `END_TIME` (string; ISO 8601 or null)  
- `LAT` (number; degrees, EPSG:4326)  
- `LON` (number; degrees, EPSG:4326)  
- `GEOM_WKT` (string; optional WKT geometry)  
- `COUNTY_FIPS` (string; 5-digit FIPS)  
- `SEVERITY` (string; `minor|severe|extreme`)  
- `INJURIES` (integer; ≥ 0)  
- `FATALITIES` (integer; ≥ 0)  
- `DAMAGE_USD` (number; ≥ 0)  

Additional optional fields (e.g., `NARRATIVE`, `EVENT_CATEGORY`, `CONFIDENCE`) SHOULD be included but not required.

## 🌐 Spatial & Temporal Constraints

- `LAT` and `LON` MUST be in WGS84 (EPSG:4326) and valid Earth ranges  
- `START_TIME` and `END_TIME` MUST be valid ISO 8601  
- `END_TIME` MUST be ≥ `START_TIME` when both are present  

These constraints ensure OWL-Time and GeoSPARQL compatibility.

---

# 🧾 Schema Versioning & Evolution

Versioning rules:

- `hazards_v1.schema.json` is **frozen** for v11.x pipelines  
- Any breaking changes require:
  - New file (`hazards_v2.schema.json`)  
  - README update with compatibility notes  
  - Pipeline DAG updates to reference the new version  

Backward-compatible additions (e.g., adding optional fields) may be allowed but MUST be accompanied by:

- Schema patch bump  
- README `version` and `last_updated` update  
- CI schema validation update  

---

# 🔍 CI/CD Enforcement

CI MUST:

- Validate normalized hazard outputs against `hazards_v1.schema.json`  
- Fail PRs when:
  - Required fields are missing  
  - Types mismatch schema  
  - Values violate constraints (e.g., invalid lat/lon, negative injuries)  

Additional checks:

- Validate STAC field mappings derived from this schema (via `build_stac_items.py`)  
- Ensure any new schema file has:
  - Documented purpose in this README  
  - Version and compatibility notes  

---

# 🧭 Integration with STAC & Graph

From normalized records that conform to `hazards_v1.schema.json`, the pipeline:

- Builds STAC Items:
  - `hazard:type` ← `HAZARD_TYPE`  
  - `hazard:severity` ← `SEVERITY`  
  - `hazard:people_affected` ← `INJURIES + FATALITIES`  
  - `hazard:property_damage_usd` ← `DAMAGE_USD`  
  - `geometry`/`bbox`/`datetime`/`interval` from `LAT/LON` and `START_TIME/END_TIME`  

- In Neo4j:
  - Creates `HazardEvent` nodes  
  - Links to `Place` (using `COUNTY_FIPS` and geometry)  
  - Links to `TimeSpan` (from start/end)  
  - Annotates severity and impact measures  

Schema correctness is therefore critical for downstream integrity.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial hazards schema module for KFM v11 (defines `hazards_v1.schema.json` as the canonical normalized hazard event schema).

---

<div align="center">

**Kansas Frontier Matrix — Hazards Schema Module (v11)**  
*Typed · Validated · Graph-Ready*

</div>

---

### 🔗 Footer  
[⬅ Back to Hazards Resources](../README.md) · [⚡ Hazards Pipeline](../../README.md) · [🧰 Autonomous Utils](../../../utils/README.md) · [🏛 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

