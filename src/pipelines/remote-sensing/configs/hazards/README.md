---
title: "🔥 Kansas Frontier Matrix — Remote Sensing Hazard Pipeline Configurations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/configs/hazards/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-hazards-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔥 **Kansas Frontier Matrix — Remote Sensing Hazard Pipeline Configurations**  
`src/pipelines/remote-sensing/configs/hazards/README.md`

**Purpose:**  
Define the FAIR+CARE-certified configuration templates for **hazard-focused remote-sensing pipelines** in KFM, including **burn scars**, **flood extents**, **drought indicators**, and **severe-weather–related environmental effects**.  
These configurations govern STAC search strategy, preprocessing, analysis thresholds, Neo4j publishing, and RDF/GeoSPARQL linked-data exports.

<img alt="Hazards" src="https://img.shields.io/badge/Hazards-Remote_Sensing-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="STAC" src="https://img.shields.io/badge/STAC-Compliant-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Hazard pipelines rely on **multi-sensor fusion** (SAR + optical + thermal) to detect and map:

- Wildfire burn scars  
- Flood extents  
- Drought surface/thermal anomalies  
- Sediment plumes  
- Snowmelt/ice events  
- Post-storm ecological impacts  

This directory defines **config files** that parameterize these pipelines in a **declarative**, **schema-validated**, **FAIR+CARE-aligned**, and **governance-ready** manner.

Each config:

- Must validate against the **Remote Sensing Config Master Schema**  
- Must include `care_label` (public/sensitive/restricted)  
- Must define masking strategy when sensitive AOIs are involved  
- Must specify telemetry output path  
- Must declare STAC query + analysis rules  
- Must align with **KFM Markdown Output Protocol** requirements  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/configs/hazards/
├── README.md                           # This file
├── burnscar.config.yaml                # Optical multispectral burn scar detection
├── flood_extent.config.yaml            # SAR + optical flood extent mapping
└── drought_signal.config.yaml          # Thermal/optical drought detection config
~~~~~

---

## 🌋 burnscar.config.yaml — Burn Scar Detection

~~~~~yaml
stac:
  endpoint: "https://earth-search.aws.element84.com/v1/search"
  collections: ["sentinel-2-l2a"]
  datetime_lookback: "P7D"
  limit: 250
  max_cloud_cover: 20
  intersects: "data/processed/aoi/kansas_boundary.geojson"

preprocessing:
  cloud_mask: true
  s2cloudless: true
  harmonize_gsd: 10
  reproject: "EPSG:4326"

analysis:
  burnscar:
    ndvi_threshold: -0.05
    nbr: true
    nbr2: true
    severity_bins:
      - { min: -1.0, max: -0.25, label: "high" }
      - { min: -0.25, max: -0.1, label: "moderate" }
      - { min: -0.1, max: 0.1, label: "low" }

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326

telemetry:
  log_file: "data/processed/telemetry/burnscar.ndjson"

care_label: "sensitive"
~~~~~

---

## 🌊 flood_extent.config.yaml — Flood Mapping (SAR + Optical)

~~~~~yaml
stac:
  endpoint: "https://earth-search.aws.element84.com/v1/search"
  collections: ["sentinel-1-grd", "sentinel-2-l2a"]
  datetime_lookback: "P3D"
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
      low: 0.10
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

## 🌾 drought_signal.config.yaml — Drought Surface/Thermal Index

~~~~~yaml
stac:
  endpoint: "https://landlook.gov/stac/search"
  collections: ["landsat-c2l2-sr", "landsat-c2l2-st"]
  datetime_lookback: "P7D"
  limit: 200
  intersects: "data/processed/aoi/kansas_boundary.geojson"

preprocessing:
  cloud_mask: true
  thermal:
    emissivity_correction: true
    lst_scale: 0.00341802
    offset: 149.0

analysis:
  drought_signal:
    ndvi_min: 0.1
    lst_max_celsius: 40
    dryness_index:
      weight_ndvi: 0.4
      weight_lst: 0.6

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"
  spatial_srid: 4326

telemetry:
  log_file: "data/processed/telemetry/drought.ndjson"

care_label: "public"
~~~~~

---

## ⚖️ FAIR+CARE Governance Requirements

- **Mandatory CARE labels** for all hazard configs  
- Hazard datasets involving burned structures, critical infrastructure, or sacred lands require:
  - Masking or H3 generalization  
  - Priority AOI overlay validation  
  - Governance escalation  
- Thermal drought configs must avoid identifying:
  - Individual farms  
  - Small tribal parcels  
  - Sensitive ecological species locations  

All hazard configs undergo:

- `faircare-validate.yml`  
- `stac-validate.yml` (if STAC ingest)  
- `telemetry-export.yml`  
- JSON-Schema validation  

---

## 📡 Telemetry Integration

Telemetry NDJSON files declared in each config are aggregated into:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Telemetry fields include:

- `stage`  
- `items`  
- `filtered_cloud`  
- `pixels_classified`  
- `hazard_area_km2`  
- `energy_wh`  
- `co2_g`  
- `care_violations`  

---

## 🧭 Usage

Use example configs as templates:

~~~~~bash
python -m remote_sensing.hazards.burnscar \
  --config src/pipelines/remote-sensing/configs/hazards/burnscar.config.yaml
~~~~~

Hazard pipelines will:

- Fetch → Validate → Analyze → Publish → Export RDF → Emit Telemetry  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Added full hazard configuration suite with FAIR+CARE masking rules, SAR + optical fusion examples, telemetry schema integration. |

---

<div align="center">

**Kansas Frontier Matrix — Hazard Configuration Suite**  
Ethical Hazard Detection × FAIR+CARE Governance × STAC-Aligned Pipelines  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>