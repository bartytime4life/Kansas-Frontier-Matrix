---
title: "🗂️ Kansas Frontier Matrix — Raw Terrain Source Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/terrain/sources/README.md"
version: "v11.0.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-raw-terrain-sources-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "Public Domain / CC0 · Source-dependent"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Data Source Registry"
intent: "terrain-raw-sources"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk / Public Geospatial Data"
sensitivity_level: "None"
provenance_chain:
  - "data/sources/usgs_3dep.json"
  - "data/sources/ks_lidar.json"
  - "data/sources/historic_topos.json"
ontology_alignment:
  geo: "GeoSPARQL"
  time: "OWL-Time"
  prov: "PROV-O"
  stac: "STAC 1.0.0"
story_node_refs: []
metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
doc_uuid: "urn:kfm:data:raw:terrain:sources:readme:v11"
semantic_document_id: "kfm-data-raw-terrain-sources"
event_source_id: "ledger:data_raw_terrain_sources"
immutability_status: "mutable"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
ai_transform_prohibited:
  - "content-alteration"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "active"
ttl_policy: "Persistent"
sunset_policy: "Reviewed annually"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Raw Terrain Source Registry**  
`data/raw/terrain/sources/README.md`

**Purpose:**  
Central registry describing **all authoritative upstream sources** used to populate the KFM **raw terrain data layer**.  
This directory contains *only* source manifests — not datasets — and serves as the **provenance backbone** for elevation, LiDAR, and historical topographic inputs used throughout KFM’s ETL pipelines.

</div>

---

## 🌎 Overview

This registry provides metadata for each **raw terrain data source** feeding:

- Terrain ETL pipelines  
- Elevation & hydrology modeling  
- Hillshade, slope, and contour generation  
- Cesium/MapLibre 3D terrain surfaces  
- Story Node spatial grounding  
- Focus Mode v3 elevation-aware narratives  

Each manifest must follow **KFM v11 STAC/DCAT/PROV-O alignment** and store:

- Acquisition URLs  
- Licensing details  
- Spatial/temporal extent  
- CRS  
- Checksum(s)  
- Provenance metadata  
- External system identifiers (e.g., USGS metadata IDs)

The manifests in this directory **never** contain data — only references to upstream sources.

---

## 📁 Directory Structure

```

data/raw/terrain/sources/
├── usgs_3dep.json          # USGS 3D Elevation Program DEM source
├── kansas_lidar.json       # Kansas statewide LiDAR source registry
├── historic_topos.json     # Historic USGS topo scans source registry
└── README.md               # This file

```

---

## 🏞️ Source Manifests

### 1. **USGS 3DEP – Elevation Program**  
`usgs_3dep.json`  
Authoritative national DEM dataset used as KFM’s primary elevation foundation.  
- Typical formats: GeoTIFF (raw), IMG  
- Coverage: All Kansas  
- Common resolutions: 1m, 10m  
- License: U.S. Public Domain  
- STAC integration: Yes  
- Notes: Reprojected & COG-converted in `data/processed/terrain/`

---

### 2. **Kansas Statewide LiDAR (QL1/QL2)**  
`kansas_lidar.json`  
High-precision LiDAR point clouds and derived DEMs.  
- Formats: LAZ (raw), DEMs from state agencies  
- Coverage: Statewide; multi-year acquisition  
- License: Public domain unless county-specific constraints apply  
- Notes: Only upstream references stored here; processing occurs via ETL pipelines

---

### 3. **Historic Topographic Maps / Elevation Sheets**  
`historic_topos.json`  
Scanned USGS historic topographic quads and legacy elevation sheets.  
- Formats: TIFF / GeoTIFF / MrSID (raw)  
- Coverage: 19th–20th century Kansas  
- License: Public domain (typically)  
- Notes: Georeferencing handled during ETL; supports historical landscape reconstruction

---

## 🧭 Metadata Requirements (per-source JSON)

Each manifest **must** include:

- `id`  
- `title`  
- `description`  
- `license`  
- `providers`  
- `assets` (URLs, file formats, checksums)  
- `spatial` (bbox, CRS)  
- `temporal` (start/end or acquisition date)  
- `provenance` (PROV-O linking to origin)  
- `stac_version`: `"1.0.0"`

---

## 🔐 FAIR+CARE & Governance Notes

- All terrain sources are **public domain**, but attribution to agencies (USGS, Kansas GIS Archive) is required.  
- Historical map handling must respect **archival rights** of institutions.  
- Provenance chains must remain intact for reproducibility and ethical transparency.  

---

## 📜 Version History

| Version | Date       | Author          | Summary |
|---------|------------|-----------------|---------|
| v11.0.0 | 2025-11-19 | Lead Programmer | Initial KFM v11-compliant terrain source registry |

---

<div align="center">

**Kansas Frontier Matrix — Source Registry (Terrain Layer)**  
🗺️ _Canonical reference for all upstream elevation and terrain inputs._

[⬅️ Back to Raw Terrain README](../README.md) •  
[📐 Data Architecture](../../../../docs/architecture/system_overview.md) •  
[⚖️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
