```
---
title: "🏔️ Kansas Frontier Matrix — Raw Terrain Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/terrain/README.md"
version: "v11.0.0"
last_updated: "2025-11-19"
review_cycle: "Continuous / Autonomous · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-terrain-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "Public Domain / CC0 · Source-dependent"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Data Layer"
intent: "terrain-raw"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk / Public Geospatial Data"
sensitivity_level: "None"
provenance_chain:
  - "data/sources/usgs_dem.json"
  - "data/sources/usgs_lidar.json"
  - "data/sources/kansas_gis_archive.json"
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
doc_uuid: "urn:kfm:data:raw:terrain:readme:v11"
semantic_document_id: "kfm-data-raw-terrain"
event_source_id: "ledger:data_raw_terrain"
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

# 🏔️ **Kansas Frontier Matrix — Raw Terrain Data Layer**  
`data/raw/terrain/README.md`

**Purpose:**  
Define the **raw, unprocessed terrain datasets** used in KFM v11 ETL pipelines, including DEMs, LiDAR tiles, topographic rasters, and elevation derivatives. This layer contains only *original assets* (or pointers to them) obtained from authoritative public sources and used as the foundation for terrain modeling, hillshades, contour extraction, and Story Node spatial grounding.

</div>

---

## 🌎 Overview

The **Raw Terrain Data Layer** provides the foundational geospatial surfaces representing the physical Kansas landscape. These data feed directly into:

- Elevation-based analyses (flood modeling, watershed derivation, trail slope estimation)  
- 3D map rendering (Cesium terrain tiles, MapLibre hillshading)  
- Focus Mode v3 spatial context (elevation-aware narrative placement)  
- Story Node geometry validation (ensuring topographic alignment)  
- Terrain-informed AI reasoning (context-aware summaries)

Raw terrain assets are stored **outside Git** using DVC/LFS pointers to preserve reproducibility without bloating the monorepo.

---

## 🗂 Directory Structure

```

data/raw/terrain/
├── sources/              # Source JSON pointers for terrain datasets
│   ├── usgs_3dep.json
│   ├── kansas_lidar.json
│   └── historic_topos.json
├── dvc_pointers/         # DVC-tracked .dvc pointer files for remote storage
│   ├── ks_dem_1m.dvc
│   ├── ks_lidar_ql2.dvc
│   └── usgs_ned_10m.dvc
└── README.md             # This file

```

---

## 🏞️ Included Terrain Data (Raw)

### 1. **USGS 3DEP DEM (1m / 10m)**
- High-resolution elevation models
- Format: GeoTIFF (COG-converted during processing)
- CRS: EPSG:4326 (converted during ETL)
- Use: hillshade, contours, slope/roughness analysis

### 2. **Kansas Statewide LiDAR (QL1 / QL2)**
- Point clouds + derived DEMs
- Format: LAZ (raw), raster DEMs (ETL-generated)
- Use: precision elevation & hydrology modeling

### 3. **Historic Topographic Scans (GeoTIFF / TIFF / MrSID)**
- Scanned USGS topo quads, county atlases, and historical terrain maps
- Stored as raw rasters prior to georeferencing
- Use: historical terrain modeling, map overlays, narrative reconstruction

### 4. **Elevation Derivative Inputs**
- Slope, aspect, curvature, roughness (generated in `data/processed/terrain/`)
- Stored here only as raw upstream components

---

## 🏗 ETL Expectations (Raw → Processed)

Raw terrain datasets must satisfy:

- **No modification** (all transformations occur in `data/processed/terrain/`)
- **Metadata presence** via `data/sources/*.json`
- **Provenance linking** via PROV-O (`prov:used`, `prov:wasGeneratedBy`)
- **STAC registration** in `data/stac/terrain/collections/*.json`
- **Deterministic conversions** (COG generation, reprojection)

Example ETL pipeline (simplified):

```

raw DEM (GeoTIFF/LAZ)
↓
Reproject (EPSG:4326)
↓
Convert to COG
↓
Generate hillshade / slope / contours
↓
Register STAC Item

```

---

## 🧭 Spatial & Temporal Metadata

All raw terrain datasets must include:

### Spatial
- `bbox` in WGS84  
- Footprint geometry (if available)  
- Resolution metadata (1m, 10m, 30m, etc.)  

### Temporal
- Acquisition date(s)  
- Publication date  
- Historical coverage notes  

These attributes propagate into STAC Items.

---

## 🔐 Licensing & Ethics (FAIR+CARE)

Terrain datasets are typically **public domain**.  
Still, the following rules apply:

- All sources must list original **license**, **publisher**, **access URL**, **checksum**  
- No inclusion of **restricted LiDAR tiles** without explicit permission  
- Historical maps must respect archival rights (scanned images treated per hosting institution’s terms)

---

## 🧩 Integration Notes (KFM v11)

This raw layer directly supports:

- **3D terrain tiles** for Cesium-based scenes  
- **Focus Mode v3 terrain-aware zooming**  
- **AI elevation reasoning** in narrative summaries  
- **Hydrology & trail analysis pipelines**  
- **Historical landscape reconstruction**

No processed terrain should ever be placed in this directory; only raw or pointer files.

---

## 📜 Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v11.0.0 | 2025-11-19 | Lead Programmer | Initial KFM v11-compliant terrain raw layer README |

---

<div align="center">

**Kansas Frontier Matrix — Raw Terrain Layer**  
🌾 _Foundational elevation data for all Kansas spatial intelligence_  

[⬅️ Back to Raw Data Index](../README.md) •  
[📐 Data Architecture](../../../docs/architecture/system_overview.md) •  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
