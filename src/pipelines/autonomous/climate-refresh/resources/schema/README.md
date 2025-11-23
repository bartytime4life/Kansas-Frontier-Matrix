---
title: "📑 KFM v11 — Climate Schema Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/climate-refresh/resources/schema/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/telemetry/autonomous-climate-refresh.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomous-climate-refresh-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Schema Module"
semantic_document_id: "kfm-climate-schema-module-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:climate-refresh:resources:schema:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📑 **Climate Schema Module (v11)**  
`src/pipelines/autonomous/climate-refresh/resources/schema/README.md`

**Purpose:**  
Define and document the JSON Schemas used by the **Autonomous Climate Refresh Pipeline**.  
These schemas enforce structural, unit, CRS, temporal, and semantic contracts for normalized climate records  
and climate STAC Items, ensuring deterministic, CI-enforced data quality for KFM v11.

</div>

---

# 📘 Overview

The `schema/` directory hosts the **authoritative JSON Schema definitions** that:

- Govern **station-based** climate records (tabular / Parquet outputs)  
- Govern **gridded** climate products (COGs, NetCDF, multi-band rasters)  
- Constrain climate-specific STAC metadata blocks (`climate:*` fields)  
- Align all climate outputs with:
  - **CRS Standard v11** (EPSG:4326, EPSG:26914)  
  - **Vertical Axis v11** (NAVD88, GEOID18)  
  - **STAC Geospatial Spec v11**  
  - **Tiling & Pyramids v11** (COG + WebMercatorQuad)  
  - **DCAT 3.0** and **PROV-O** lineage requirements  
  - **Data Contract v3** for units and variable semantics  

All schemas here are:

- JSON Schema **draft 2020-12**  
- Versioned and pinned via this README  
- Required in CI before any climate data promotion to the graph or public STAC catalogs  

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/climate-refresh/resources/schema/
│
├── README.md                 # This file (schema module overview)
└── climate_v1.schema.json    # Core climate variable + metadata schema
```

Future schemas (e.g., `climate_v2.schema.json`, STAC-specific item schemas) MUST be added here and documented in this file.

---

# 🌡 climate_v1.schema.json — Core Climate Schema

This schema defines the structure and types for **normalized climate datasets** produced by:

- `normalize_station.py` (station time-series)  
- `normalize_gridded.py` (gridded raster products)  

## 🎯 Goals

- Provide a single canonical representation for climate variables across:
  - NOAA NCEI daily/hourly data  
  - PRISM gridded normals/analyses  
  - Daymet 1 km daily grids  
  - Kansas Mesonet station networks  
  - Derived drought indices (SPEI/SPI/Palmer)  
- Enforce consistent variable names, units, and CRS  
- Make records directly convertible into STAC Items and graph nodes  

## 🧱 Required Station Fields (Conceptual)

At a minimum, **station records** MUST include:

- `STATION_ID` (string)  
- `SOURCE_SYSTEM` (string; e.g. `noaa_ncei`, `mesonet`)  
- `DATE` (string; ISO 8601 `YYYY-MM-DD` or full `datetime`)  
- `LAT` (number; EPSG:4326 latitude)  
- `LON` (number; EPSG:4326 longitude)  

Plus at least one of these variables (and associated units):

- `TMAX_C` (number; max temperature, °C)  
- `TMIN_C` (number; min temperature, °C)  
- `PRCP_MM` (number; precipitation, mm)  
- `SRAD_WM2` (number; solar radiation, W/m²)  
- `VPD_KPA` (number; vapor pressure deficit, kPa)  
- `WS_MPS` (number; wind speed, m/s)  

Optional station fields (recommended):

- `QC_FLAGS` (string/array)  
- `ELEV_M` (number; station elevation, m)  
- `NETWORK` (string; e.g. `COOP`, `ASOS`, `MESONET`)  

## 🧱 Required Gridded Fields (Conceptual)

For **gridded products** (rasters / multi-band COGs), the schema MUST enforce:

- Spatial metadata (stored in STAC, but derived from schema):
  - `proj:epsg` ∈ {26914 (processing), 4326 (geometry)}  
  - `climate:spatial_resolution_m` (number; grid spacing in meters)  

- Variable bands and units:
  - `tmax` → °C  
  - `tmin` → °C  
  - `prcp` → mm  
  - `vpd` → kPa  
  - `srad` → W/m²  

- Temporal dimension:
  - `DATE` or `DATETIME` for each grid (ISO 8601)  
  - Or `start_datetime` / `end_datetime` for composites  

Schema constraints MUST support:

- Mapping to CF-compliant variable names in NetCDF  
- Tiling/COG generation per Tilings Standard v11  
- Multi-band vs single-band configuration  

---

# 🌐 Spatial & Temporal Constraints

- `LAT` ∈ [-90, 90], `LON` ∈ [-180, 180]  
- Coordinates MUST be WGS84 (EPSG:4326) for tabular station data  
- Gridded metadata MUST reflect CRS transitions (26914→4326) correctly  
- `DATE` / `DATETIME` MUST be valid ISO 8601 strings  
- If `start_datetime`/`end_datetime` are used, `end_datetime ≥ start_datetime`  

These constraints guarantee OWL-Time and GeoSPARQL compatibility.

---

# 🧾 Schema Versioning & Evolution

Versioning rules:

- `climate_v1.schema.json` is **frozen** for KFM v11.x climate pipelines  
- Breaking changes require:
  - A new file (`climate_v2.schema.json`)  
  - README update with compatibility notes  
  - DAG + node updates to reference the new version  

Backward-compatible changes (e.g., adding **optional** fields) MUST:

- Bump the internal `version` field in `climate_v1.schema.json`  
- Update this README `version` and `last_updated`  
- Update CI schema tests as needed  

---

# 🔍 CI/CD Enforcement

CI MUST:

- Validate station outputs of `normalize_station.py` against `climate_v1.schema.json`  
- Validate gridded outputs of `normalize_gridded.py` against appropriate schema sections  
- Fail PRs when:
  - Required fields missing  
  - Types mismatch schema  
  - Units violate Data Contract v3  
  - Spatial or temporal ranges are invalid  

Additional checks:

- Ensure STAC Items derived via `build_stac_items.py` map correctly from schema fields  
- Ensure all climate-related STAC extensions (`climate:*`, `proj:*`, `vertical:*`) have valid, schema-backed sources  

---

# 🧭 Integration with STAC & Neo4j

From records conforming to `climate_v1.schema.json`, the pipeline:

- Builds STAC Items with:
  - `climate:vars` populated from the variables present  
  - `climate:temporal_resolution` (e.g. `daily`, `hourly`, `monthly`)  
  - `climate:spatial_resolution_m` for gridded datasets  
  - OWL-Time intervals from DATE / DATETIME fields  
  - CRS + vertical metadata (EPSG:4326/26914, NAVD88/GEOID18)  

- Syncs into Neo4j as:
  - `ClimateObservation` (station records)  
  - `ClimateGrid` (gridded rasters)  
  - Linked to `Place` (GeoSPARQL geometry) and `TimeSpan` (OWL-Time)  
  - Including variable units & semantics consistent with Data Contract v3  

Schema correctness is essential for consistent graph queries and Focus Mode narratives.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial climate schema module for KFM v11 (`climate_v1.schema.json` defined as canonical normalized climate schema).

---

<div align="center">

**Kansas Frontier Matrix — Climate Schema Module (v11)**  
*Typed · Validated · Climate-Ready*

</div>

---

### 🔗 Footer  
[⬅ Back to Climate Resources](../README.md) · [🌡 Climate Pipeline](../../README.md) · [🧰 Autonomous Utils](../../../utils/README.md) · [🏛 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

