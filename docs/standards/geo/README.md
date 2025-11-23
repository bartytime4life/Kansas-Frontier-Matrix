---
title: "🌎 Kansas Frontier Matrix — Geo Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Semiannual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-geo-readme-v11.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-geo-standards-readme-v11"
doc_uuid: "urn:kfm:docs:standards:geo:index:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🌎 **Kansas Frontier Matrix — Geo Standards Index (v11)**  
`docs/standards/geo/README.md`

**Purpose:**  
Provide the centralized entrypoint for all **KFM v11 geospatial standards**, including STAC/DCAT geocoding rules, vertical-axis definitions, coordinate systems, tiling, DEM/DoD conventions, hydrology schemas, and CRS harmonization.  
This index ensures deterministic, FAIR+CARE-aligned, metadata-safe use of spatial data across ETL, AI, Neo4j, API, and UI layers.

</div>

---

# 📘 Overview

KFM v11 requires all geospatial datasets — raster, vector, tabular, STAC Items, DEMs, hydrology models, archaeological spatial layers, and map overlays — to conform to **machine-verifiable geospatial standards**.  
This directory contains the authoritative specifications that govern:

- Coordinate Reference Systems (CRS)  
- Vertical datums & geoid models  
- DEM/DoD conventions  
- Geospatial metadata (STAC/DCAT/JSON-LD)  
- Horizontal & vertical accuracy requirements  
- FAIR+CARE-compliant handling of sensitive spatial information  
- UI (MapLibre/Cesium) rendering requirements  
- Spatial validation rules for CI/CD  

All KFM pipelines and STAC catalogs reference these standards during ingestion, validation, and rendering.

---

# 🗂 Directory Layout

```text
docs/standards/geo/
│
├── README.md                     # This index file
│
├── vertical-axis-and-dod.md      # Vertical datum, CF z-axis, and DoD sign convention standard
│   # Defines: NAVD88/GEOID18 rules, CF positive="up/down", DoD erosion/deposition
│
├── crs-standard.md               # Horizontal CRS requirements (EPSG:4326, 26914; reprojection SOPs)
│   # Defines: allowed CRSs, required metadata, transformation lineage
│
├── tiling-and-pyramids.md        # Raster tiling, COG overviews, MapLibre/Cesium tile Grid rules
│   # Defines: tile matrix sets, zoom logic, pyramids, COG mandatory structure
│
├── stac-geo-spec.md              # STAC geospatial metadata extensions for KFM
│   # Defines: proj:, geospatial fields, bbox, geometry, temporal bounding, lineage
│
├── hydrology-standards.md        # Hydrology STAC/geometry/CF-time rules
│   # Defines: streamflow, bathymetry, WID dredging, lake models, water elevation schemas
│
└── archaeology-sensitive-locations.md
    # Defines: H3 generalization, masking rules, Indigenous sovereignty compliance
```

---

# 🧩 Core Geo Standards (Summary)

The following standards govern all KFM geospatial assets:

## 📐 Vertical Axis & DoD  
From `vertical-axis-and-dod.md`  
- NAVD88 mandatory for orthometric heights  
- GEOID18 required  
- CF `positive="up"` for elevation, `positive="down"` for depth  
- DEM-of-Difference:  
  - **Erosion = negative**  
  - **Deposition = positive**  
- Mandatory STAC vertical metadata  
- Mandatory UI legend text  
- PROV-O lineage required

## 🗺 CRS Standard  
- Allowed CRSs: EPSG:4326 (WGS84), EPSG:26914 (NAD83 / UTM14N)  
- Reprojection required for STAC Item alignment  
- CRS must be declared in: metadata, STAC, and file headers  
- All ETL reprojections require PROV-O lineage

## 🧱 Tiling & Pyramids  
- Cloud Optimized GeoTIFFs mandatory for rasters  
- Overviews at powers-of-2 required  
- MapLibre tile compatibility enforced across 3D/2.5D/2D renderers

## 🛰 STAC Geo Spec  
- Mandatory `bbox`, `geometry`, `proj:*`, `vertical:*` fields  
- JSON-LD compatible  
- DCAT 3.0 alignment for dataset-level metadata

## 💧 Hydrology Standards  
- CF-Time required  
- Depth/Water Surface elevation must use orthometric heights  
- Streamflow rasters must specify datum & hydrological reference plane

## 🛡 Archaeology & Sensitive Locations  
- H3 generalization required  
- Masking required for Indigenous sites  
- CARE-compliant location restrictions

---

# ⚙ CI/CD Requirements

All geo-related artifacts MUST pass:

- **stac-validate** (static catalog)  
- **crs-lint** (CRS compliance)  
- **cf-axis-validate** (vertical axis metadata)  
- **geojson-schema-validate**  
- **raster-meta-validate** (COG, overviews, CRS, geotransforms)  
- **provenance-audit** (PROV-O completeness)  
- **faircare-audit** (ethical + FAIR compliance)  

Any violation → **PR blocked**.

---

# 🕰 Version History

- **v11.0.0 (2025-11-22):** Initial v11 release, fully updated for KFM-MDP v11 and Geo Standards reorganization.

---

<div align="center">

**Kansas Frontier Matrix — Geo Standards Index (v11)**  
*Semantic · Spatial · Deterministic · FAIR+CARE*

</div>

---

### 🔗 Footer  
[⬅ Back to Standards](../README.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

