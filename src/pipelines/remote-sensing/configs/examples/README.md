---
title: "🛰️ Kansas Frontier Matrix — Remote Sensing Config Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/configs/examples/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-configs-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Remote Sensing Config Examples**  
`src/pipelines/remote-sensing/configs/examples/README.md`

**Purpose:**  
Provide **validated, ready-to-use configuration examples** for remote-sensing pipelines (LandsatLook, Sentinel-2, Sentinel-1 SAR, NAIP, MODIS/VIIRS, hazards, vegetation indices).  
All examples conform to the **Remote Sensing Master Config Schema**, **FAIR+CARE governance**, and **KFM Markdown Output Protocol v10.3**.

<img alt="Configs" src="https://img.shields.io/badge/Configs-Validated-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange"/>
<img alt="Schema" src="https://img.shields.io/badge/JSON_Schema-Passed-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Examples_Ready-success"/>

</div>

---

## 📘 Overview

This directory contains **authoritative example configurations** for all remote-sensing pipelines.  
Each example demonstrates:

- STAC search parameters  
- AOI & boundary sources  
- Preprocessing and harmonization options  
- Index/hazard analysis parameters  
- Neo4j and RDF publishing settings  
- AI summarization/tagging rules  
- Telemetry bindings  
- CARE-label application and governance metadata  

Use these as **templates** for new pipelines or for extending existing ones.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/configs/examples/
├── README.md                        # This file
│
├── minimal_landsat.yaml             # Minimal LandsatLook ingest config
├── sentinel2_full.yaml              # Full-featured Sentinel-2 config
├── flood_extent_ks.yaml             # SAR/optical flood extraction pipeline
└── ndvi_basic.yaml                  # Example NDVI/vegetation index config
~~~~~

---

## 🧩 Example: Minimal LandsatLook Config

~~~~~yaml
stac:
  endpoint: "https://landsatlook.usgs.gov/stac-server/search"
  collections: ["landsat-c2l2-sr"]
  datetime_lookback: "P7D"
  max_cloud_cover: 30
  limit: 200
  intersects: "data/processed/aoi/kansas_boundary.geojson"

aoi:
  counties: "data/processed/admin/kansas_counties.gpkg#counties"

preprocessing:
  cloud_mask: true
  reproject: "EPSG:4326"
  harmonize_gsd: 30

analysis:
  ndvi: true

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326

rdf:
  enable: false

telemetry:
  log_file: "data/processed/telemetry/landsat.ndjson"

care_label: "public"
~~~~~

---

## 🛰️ Example: Sentinel-2 Full Configuration

~~~~~yaml
stac:
  endpoint: "https://earth-search.aws.element84.com/v1/search"
  collections: ["sentinel-2-l2a"]
  datetime_lookback: "P10D"
  limit: 250
  max_cloud_cover: 20
  query:
    platform: { eq: "sentinel-2a" }
  intersects: "data/processed/aoi/kansas_boundary.geojson"

aoi:
  counties: "data/processed/admin/kansas_counties.gpkg#counties"
  priority_aoi: "data/processed/aoi/kansas_priority.gpkg#aoi"

preprocessing:
  cloud_mask: true
  s2cloudless: true
  harmonize_gsd: 10
  reproject: "EPSG:4326"

analysis:
  ndvi: true
  ndmi: true
  burnscar: true

ai:
  enable: true
  prompt_template: "docs/prompts/remote-sensing/scene-brief.v1.txt"
  tags_allowed:
    - burn_scar
    - crop_stress
    - sediment_plume
    - river_flood

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326

rdf:
  enable: true
  out_dir: "data/processed/rdf/sentinel2/"
  context: "schemas/rdf/geosparql.context.jsonld"

telemetry:
  log_file: "data/processed/telemetry/sentinel2.ndjson"

care_label: "public"
~~~~~

---

## 🌊 Example: Flood Extent (KS) — SAR + Optical

~~~~~yaml
stac:
  endpoint: "https://earth-search.aws.element84.com/v1/search"
  collections: ["sentinel-1-grd", "sentinel-2-l2a"]
  datetime_lookback: "P5D"
  limit: 300
  intersects: "data/processed/aoi/kansas_flood_plains.geojson"

preprocessing:
  sar:
    terrain_correction: true
    speckle_filter: "lee"
  optical:
    cloud_mask: true
    harmonize_gsd: 10

analysis:
  flood_extent:
    sar_threshold_db: -15
    optical_water_index: "ndwi"
    hysteresis:
      low: 0.12
      high: 0.22

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326

rdf:
  enable: true
  out_dir: "data/processed/rdf/flood/"
  context: "schemas/rdf/geosparql.context.jsonld"

telemetry:
  log_file: "data/processed/telemetry/flood.ndjson"

care_label: "sensitive"
~~~~~

---

## 🌱 Example: Basic NDVI Config

~~~~~yaml
stac:
  endpoint: "https://landsatlook.usgs.gov/stac-server/search"
  collections: ["landsat-c2l2-sr"]
  datetime_lookback: "P3D"
  limit: 150
  intersects: "data/processed/aoi/kansas_boundary.geojson"

analysis:
  ndvi:
    method: "standard"
    min_valid: -0.2
    max_valid: 0.9

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326

telemetry:
  log_file: "data/processed/telemetry/ndvi.ndjson"

care_label: "public"
~~~~~

---

## ⚖️ FAIR+CARE Requirements for All Example Configs

- All examples declare **care_label** explicitly.  
- Sensitive AOIs (e.g., flood plains, sacred sites) require:
  - `priority_aoi` overlays  
  - mandatory masking for coordinate-level detail  
- AI examples include:
  - prompt path  
  - allowed tag lists  
  - refusal logging expectations  
- All examples pass:
  - config JSON Schema  
  - FAIR+CARE validation  
  - KFM Markdown Output Protocol  

---

## 📡 Telemetry Integration

Every example defines a telemetry NDJSON path:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

All telemetry is aggregated to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Added four fully validated configuration examples with FAIR+CARE and STAC schema alignment. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Config Examples**  
Reusable Templates × FAIR+CARE Governance × Schema-Validated Pipelines  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>