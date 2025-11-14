---
title: "🌱 Kansas Frontier Matrix — Vegetation & Spectral Index Pipeline Configurations (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/configs/indices/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-indices-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌱 **Kansas Frontier Matrix — Vegetation & Spectral Index Pipeline Configurations**  
`src/pipelines/remote-sensing/configs/indices/README.md`

**Purpose:**  
Define **validated, FAIR+CARE-compliant configuration templates** for vegetation and spectral index pipelines (NDVI, NDMI, NDWI, SAVI) in the Kansas Frontier Matrix (KFM).  
These configs parameterize STAC ingestion, atmospheric correction, cloud masking, index computation, Neo4j publishing, and RDF/GeoSPARQL linked-data preparation.

<img alt="Indices" src="https://img.shields.io/badge/Indices-NDVI_·_NDMI_·_NDWI_·_SAVI-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="STAC" src="https://img.shields.io/badge/STAC-Compliant-blue"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Vegetation/spectral index pipelines in KFM compute:

- **NDVI** — Normalized Difference Vegetation Index  
- **NDMI** — Moisture Index  
- **NDWI** — Water Index  
- **SAVI** — Soil-Adjusted Vegetation Index  

These pipelines consume **Landsat**, **Sentinel-2**, or **NAIP** data depending on configuration.

Each configuration here:

- Is **JSON-Schema validated**  
- Defines **STAC ingest rules**  
- Ensures **cloud masking and harmonized GSD**  
- Provides **index-specific thresholds and formulas**  
- Produces **COG/GeoParquet** derivatives  
- Publishes results to Neo4j (`:IndexLayer`)  
- Emits telemetry to NDJSON logs  
- Applies FAIR+CARE governance (mask sensitive plant/soil signatures when required)

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/configs/indices/
├── README.md                   # This file
├── ndvi.config.yaml            # NDVI computation rules
├── ndmi.config.yaml            # Moisture index rules
├── ndwi.config.yaml            # Water index config
└── savi.config.yaml            # Soil-adjusted vegetation index
~~~~~

---

## 🍃 NDVI Configuration Example (ndvi.config.yaml)

~~~~~yaml
stac:
  endpoint: "https://landsatlook.usgs.gov/stac-server/search"
  collections: ["landsat-c2l2-sr"]
  datetime_lookback: "P3D"
  limit: 150
  intersects: "data/processed/aoi/kansas_boundary.geojson"

preprocessing:
  cloud_mask: true
  harmonize_gsd: 30
  reproject: "EPSG:4326"

analysis:
  ndvi:
    formula: "(nir - red) / (nir + red)"
    min_valid: -0.2
    max_valid: 0.9
    classify_bins:
      - { min: -1.0, max: 0.1, label: "barren" }
      - { min: 0.1, max: 0.3, label: "low_veg" }
      - { min: 0.3, max: 0.6, label: "moderate_veg" }
      - { min: 0.6, max: 1.0, label: "high_veg" }

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

## 💧 NDMI Configuration (ndmi.config.yaml)

~~~~~yaml
stac:
  endpoint: "https://earth-search.aws.element84.com/v1/search"
  collections: ["sentinel-2-l2a"]
  datetime_lookback: "P5D"
  limit: 200
  intersects: "data/processed/aoi/kansas_boundary.geojson"

preprocessing:
  cloud_mask: true
  harmonize_gsd: 10

analysis:
  ndmi:
    formula: "(nir - swir1) / (nir + swir1)"
    classify_bins:
      - { min: -1.0, max: -0.1, label: "very_dry" }
      - { min: -0.1, max: 0.2, label: "dry" }
      - { min: 0.2, max: 0.5, label: "moist" }
      - { min: 0.5, max: 1.0, label: "wet" }

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"

telemetry:
  log_file: "data/processed/telemetry/ndmi.ndjson"

care_label: "public"
~~~~~

---

## 🌊 NDWI Configuration (ndwi.config.yaml)

~~~~~yaml
stac:
  endpoint: "https://earth-search.aws.element84.com/v1/search"
  collections: ["sentinel-2-l2a"]
  datetime_lookback: "P5D"
  limit: 150
  intersects: "data/processed/aoi/kansas_boundary.geojson"

preprocessing:
  cloud_mask: true
  reproject: "EPSG:4326"

analysis:
  ndwi:
    formula: "(green - nir) / (green + nir)"
    water_threshold: 0.2   # classify pixels above threshold as water

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"

rdf:
  enable: true
  out_dir: "data/processed/rdf/ndwi/"
  context: "schemas/rdf/geosparql.context.jsonld"

telemetry:
  log_file: "data/processed/telemetry/ndwi.ndjson"

care_label: "public"
~~~~~

---

## 🌾 SAVI Configuration (savi.config.yaml)

~~~~~yaml
stac:
  endpoint: "https://landsatlook.usgs.gov/stac-server/search"
  collections: ["landsat-c2l2-sr"]
  datetime_lookback: "P10D"
  limit: 200
  intersects: "data/processed/aoi/kansas_boundary.geojson"

preprocessing:
  cloud_mask: true
  harmonize_gsd: 30

analysis:
  savi:
    formula: "((nir - red) / (nir + red + 0.5)) * 1.5"
    classify_bins:
      - { min: -1.0, max: 0.1, label: "bare_soil" }
      - { min: 0.1, max: 0.4, label: "sparse" }
      - { min: 0.4, max: 1.0, label: "dense" }

neo4j:
  uri: "bolt://localhost:7687"
  user: "neo4j"
  secret_ref: "secrets/neo4j.txt"

telemetry:
  log_file: "data/processed/telemetry/savi.ndjson"

care_label: "public"
~~~~~

---

## ⚖️ FAIR+CARE Governance Requirements

All index configs MUST:

- Declare **care_label**.  
- Apply masking/generalization when vegetation signatures overlap with:
  - Tribal ecological stewardship zones  
  - Sensitive species habitats  
  - Private agricultural zones (if required by CARE governance)  
- Log AI or spectral misclassification risks (e.g., NDWI false water detection due to shadows).  
- Emit telemetry fields required for sustainability and ethics tracking.

Governance CI validates:

- Masking strategies  
- CARE label correctness  
- FAIR interoperability fields  
- JSON-Schema configuration validity  

---

## 📡 Telemetry Requirements

Each index config declares a telemetry NDJSON path:

~~~~~text
data/processed/telemetry/<index>.ndjson
~~~~~

Telemetry aggregated into:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Tracked fields:

- `stage`  
- `pixels_processed`  
- `cloud_masked_percent`  
- `index_min` / `index_max`  
- `index_distribution`  
- `care_violations`  
- `energy_wh`  
- `co2_g`  

---

## 🧭 Usage

~~~~~bash
# Run NDVI pipeline using config
python -m remote_sensing.indices.ndvi \
  --config src/pipelines/remote-sensing/configs/indices/ndvi.config.yaml
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Added full vegetation & spectral index configuration suite with FAIR+CARE governance + telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — Vegetation & Spectral Index Configuration Suite**  
Ethical Spectral Analytics × FAIR+CARE Governance × Repeatable Science  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>