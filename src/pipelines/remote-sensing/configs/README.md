---
title: "🛰️ Kansas Frontier Matrix — Remote Sensing Pipeline Configuration Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/configs/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-remote-sensing-configs-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Remote Sensing Pipeline Configuration Registry**  
`src/pipelines/remote-sensing/configs/README.md`

**Purpose:**  
Define the **canonical configuration structure**, schemas, and FAIR+CARE governance rules for all Remote Sensing pipelines (Landsat, Sentinel-1, Sentinel-2, NAIP, MODIS/VIIRS, indices, hazards, change-detection) within the KFM v10.3 ecosystem.  
All configs stored here MUST be **schema-validated**, **telemetry-linked**, **provenance-tracked**, and **MCP-DL v6.3 compliant**.

<img alt="Remote Sensing" src="https://img.shields.io/badge/Remote_Sensing-Configs-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Schema" src="https://img.shields.io/badge/JSON_Schema-Required-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

All remote-sensing pipelines in KFM use **external YAML/JSON config files** stored in this directory.

These configs define:

- STAC search parameters  
- AOI sources (state boundary, counties, priority AOIs)  
- Cloud and quality thresholds  
- Preprocessing rules (masking, atmospheric correction, SAR terrain correction)  
- Analysis parameters (NDVI/NDMI thresholds, change-detection windows)  
- Neo4j publishing options  
- RDF export settings  
- AI summarization/tagging options  
- Telemetry & governance bindings  

Configs MUST be declarative, reproducible, portable, and pass:

- **JSON-Schema validation**  
- **FAIR+CARE governance checks**  
- **telemetry-export.yml** consistency rules  
- **docs-lint.yml** KFM Markdown Structural Rules  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/configs/
├── README.md                                 # This file
│
├── landsatlook-stac-ingest.config.yaml       # LandsatLook STAC → Neo4j ingest config
├── sentinel2-stac-ingest.config.yaml         # Sentinel-2 MSI STAC ingest config
├── sentinel1-sar.config.yaml                 # Sentinel-1 SAR terrain correction + flood mapping
├── naip-ingest.config.yaml                   # NAIP aerial imagery ingest + mosaic
├── modis-ingest.config.yaml                  # MODIS/VIIRS thermal/NDVI config
│
├── indices/
│   ├── ndvi.config.yaml                      # NDVI generation parameters
│   ├── ndmi.config.yaml                      # NDMI parameters
│   ├── ndwi.config.yaml                      # NDWI parameters
│   └── savi.config.yaml                      # Soil-adjusted vegetation index
│
├── hazards/
│   ├── burnscar.config.yaml                  # Burn scar detection config
│   ├── flood_extent.config.yaml              # Flood extent SAR/optical config
│   └── drought_signal.config.yaml            # Drought surface/thermal index config
│
├── schemas/
│   ├── remote_sensing_config.schema.json     # Master JSON Schema for all configs
│   ├── stac_query.schema.json                # Subschema for STAC search rules
│   ├── preprocessing.schema.json             # Preprocessing parameters
│   ├── neo4j_publish.schema.json             # Neo4j output schema
│   ├── rdf_export.schema.json                # Linked-data rules
│   └── ai_summarization.schema.json          # AI summarization/tagging schema
│
└── examples/
    ├── minimal_landsat.yaml                  # Minimal Landsat config
    ├── sentinel2_full.yaml                   # Full-featured Sentinel-2 ingest config
    └── flood_extent_ks.yaml                  # Hazard pipeline example
~~~~~

---

## 🧬 Configuration Contract (Master Schema)

All config files MUST validate against:

~~~~~text
src/pipelines/remote-sensing/configs/schemas/remote_sensing_config.schema.json
~~~~~

Core required fields:

| Field | Description |
|-------|-------------|
| `stac.endpoint` | STAC search endpoint |
| `stac.collections` | Allowed dataset collections |
| `stac.datetime_lookback` | ISO-8601 duration (e.g., `P14D`) |
| `aoi.intersects` | GeoJSON/KML/WKT path for AOI |
| `preprocessing` | Cloud mask, atmo-corr, terrain-corr options |
| `analysis` | Index/hazard parameters |
| `neo4j` | Bolt URI, SRID, index labels |
| `rdf` | JSON-LD/Turtle export options |
| `telemetry.log_file` | NDJSON telemetry path |
| `care_label` | Required CARE classification (public/sensitive/restricted) |

---

## 🧩 Example (LandsatLook Minimal Config)

~~~~~yaml
stac:
  endpoint: "https://landsatlook.usgs.gov/stac-server/search"
  collections: ["landsat-c2l2-sr"]
  datetime_lookback: "P7D"
  max_cloud_cover: 20
  limit: 200
  intersects: "data/processed/aoi/kansas_boundary.geojson"

aoi:
  counties: "data/processed/admin/kansas_counties.gpkg#counties"

preprocessing:
  cloud_mask: true
  harmonize_gsd: 30
  reproject: "EPSG:4326"

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
  log_file: "data/processed/telemetry/landsat_ingest.ndjson"

care_label: "public"
~~~~~

---

## ⚖️ FAIR+CARE Governance Requirements

Configs MUST specify:

- **care_label** (public/sensitive/restricted)  
- **masking strategy** for sensitive AOIs  
- **provenance requirements** for STAC + AI outputs  
- Whether **AI summarization** is allowed for this dataset family  
- **Tribal sovereignty overlays**, if applicable  

Governance CI will fail if:

- CARE labels are missing  
- Masking is required but not configured  
- AI is enabled without an approved prompt path  

---

## 📡 Telemetry Bindings

Every config MUST declare where pipeline telemetry is written:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

Aggregated into:

~~~~~text
../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

Telemetry schemas validated via:

- `telemetry-export.yml`  
- `fields.md` & `exporters.md`  
- Remote-sensing telemetry schema  

---

## 🔧 CI Enforcement Rules

Configs MUST pass:

- **JSON Schema validation** (remote_sensing_config.schema.json)  
- **FAIR+CARE validation** (faircare-validate.yml)  
- **Documentation linting** (docs-lint.yml)  
- **STAC rules** if STAC ingestion enabled  
- **Telemetry schema validation**  

---

## 🧱 Governance & Provenance

Each config influences:

- STAC provenance (source endpoint, collections, datetime windows)  
- AI provenance (prompt, model, parameters, refusal logs)  
- Neo4j lineage (indexes, constraints, SRID)  
- RDF provenance (GeoSPARQL context, feature mappings)  

All governance actions logged in:

~~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Added full configuration registry, schema references, FAIR+CARE governance bindings, telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Configuration Registry**  
Declarative Pipelines × FAIR+CARE Ethics × Immutable Provenance × Scientific Integrity  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>