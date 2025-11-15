---
title: "🗄️ Kansas Frontier Matrix — Data System Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/ARCHITECTURE.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../releases/v10.4.0/manifest.zip"
telemetry_ref: "../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-architecture-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "data-system-architecture"
fair_category: "F1-A1-I1-R1"
care_label: "Variable — Dataset Dependent"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false
provenance_chain:
  - "data/ARCHITECTURE.md@v10.0.0"
  - "data/ARCHITECTURE.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../schemas/json/data-architecture.schema.json"
shape_schema_ref: "../schemas/shacl/data-architecture-shape.ttl"
doc_uuid: "urn:kfm:doc:data-architecture-v10.4.0"
semantic_document_id: "kfm-doc-data-architecture"
event_source_id: "ledger:data/ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Varies by dataset"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next data-platform update"
---

<div align="center">

# 🗄️ **Kansas Frontier Matrix — Data System Architecture**  
`data/ARCHITECTURE.md`

**Purpose:**  
Define the **complete architecture** for all data ingestion, storage, governance, validation, lineage, provenance,
and STAC/DCAT catalog integration in the Kansas Frontier Matrix (KFM).  
This governs all contributors working on `data/**`, ensuring FAIR+CARE compliance, provenance integrity, sustainable
data processing, and reproducibility across ETL, AI, and geospatial pipelines.

</div>

---

## 📘 Overview

The KFM **Data System** is a multi-layered, ontology-aligned, FAIR+CARE-certified data platform supporting:

- Raw ingestion (scanned maps, CSVs, rasters, shapefiles, sensor data)  
- Normalization & cleaning processes  
- AI enrichment (OCR, NER, entity linking, summarization)  
- Geospatial harmonization & CRS normalization  
- Temporal normalization & OWL-Time alignment  
- Provenance and governance metadata extraction  
- STAC/DCAT catalog publication  
- Neo4j loading (CIDOC-CRM, GeoSPARQL, PROV-O)  
- Redaction/generalization for CARE-sensitive datasets  
- Telemetry for energy, performance, and drift  

The `data/` layer forms the **foundation** of the KFM knowledge graph, Focus Mode reasoning, and Story Node v3
generation.

---

## 🧱 Directory Structure

A canonical data architecture tree using `~~~text`:

~~~text
data/                                 # KFM data platform root
├── ARCHITECTURE.md                   # This architecture specification
├── README.md                         # High-level data platform overview
│
├── raw/                              # Original ingested datasets (immutable)
│   ├── hydrology/                    # NOAA, USGS, precipitation, streamflow
│   ├── geology/                      # Geologic maps, DEMs, LiDAR
│   ├── history/                      # Census, archival docs, scans
│   ├── remote-sensing/               # Landsat, Sentinel, NAIP, COGs
│   └── sovereignty/                  # Indigenous boundaries (CARE-governed)
│
├── work/                             # Intermediate cleaned/preprocessed data
│   ├── tabular/                      # Cleaned CSV/Parquet
│   ├── geospatial/                   # GeoJSON, geoparquet, TopoJSON
│   ├── stac-temp/                    # Pre-STAC items
│   └── ocr/                          # OCR outputs, NER tags, spans
│
├── processed/                        # Final processed outputs
│   ├── stac/                         # STAC Collections/Items (v1.0.0)
│   ├── dcat/                         # DCAT v3 dataset metadata
│   ├── features/                     # Merged vector layers (GeoJSON, Parquet)
│   ├── rasters/                      # Tile-ready COGs and derivatives
│   └── storynodes/                   # Story Node v3 enriched data bundles
│
├── lineage/                          # Provenance tracking & PROV-O exports
│   ├── prov/                         # PROV-O RDF/Turtle lineage
│   ├── manifests/                    # Metadata manifests, per-run lineage
│   └── logs/                         # Detailed process logs
│
├── governance/                       # CARE, sovereignty, ethics controls
│   ├── masking/                      # Masking/generalization configs
│   ├── redaction/                    # Culturally sensitive removals
│   ├── licenses/                     # SPDX license files
│   └── care/                         # CARE metadata attachments
│
└── telemetry/                        # Data pipeline metrics
    ├── energy/                       # Processing energy logs (Wh)
    ├── carbon/                       # CO₂ estimates (gCO₂e)
    ├── drift/                        # Dataset drift reports (tabular/geospatial)
    └── quality/                      # Data quality metrics & validation
~~~

---

## 🧩 Data Lifecycle Architecture

The KFM Data Platform follows a **6-phase lifecycle**:

### 1. **Ingestion Phase (raw/)**
- Accepts raw raster, vector, tabular, archival, sensor, and external datasets.  
- No transformations applied; checksummed on arrival.  
- CARE-protected datasets immediately flagged for masking.

### 2. **Cleaning Phase (work/)**
- Normalize CRS (EPSG:4326 / project-specific CRS)  
- Apply OCR + NER + entity linking  
- De-duplicate and harmonize attributes  
- Clean nulls, unexpected values, temporal gaps  

### 3. **Processing Phase (processed/)**
- Convert to machine-friendly formats (COG, geoparquet, Parquet)  
- Run summarization, clustering, segment extraction for Story Node v3  
- Produce geospatially consistent layers (TopoJSON, COG pyramids)

### 4. **Cataloging Phase (STAC / DCAT)**
- Generate STAC Items & Collections (v1.0.0)  
- Publish DCAT v3 metadata objects  
- Assign licensing, provenance, temporal/spatial extents  
- Validate with `schema_check.py` + `stac-validator`

### 5. **Loading Phase (Neo4j)**
- Convert STAC/DCAT/processed layers into graph nodes (CIDOC-CRM, PROV-O, GeoSPARQL)  
- Maintain entity linking integrity and temporal reasoners  
- Validate with SHACL before ingestion

### 6. **Publication Phase**
- Versions included in:
  - Releases  
  - SBOM  
  - Manifest  
  - Governance ledgers  
  - Telemetry bundles  

---

## 🗺️ Geospatial Architecture

### Spatial Standards
- EPSG:4326 baseline  
- Support for:
  - USGS Albers  
  - UTM zones  
  - Equal Earth projections for display  
- Hierarchy:
  - Raw → normalized → harmonized → published

### Spatial Data Types
- Vector (GeoJSON, TopoJSON, GeoParquet)  
- Raster (COG, GeoTIFF, cloud-optimized pyramids)  
- 3D terrain (DTM/DSM)  
- Categorical grid layers (land cover, geology)

### Spatial Indexing
- H3 integration for:
  - Generalization  
  - Sensitive site masking  
  - Aggregation  

---

## 🧬 Temporal Architecture

- OWL-Time alignment for events, datasets, Story Nodes  
- Temporal extents required in:
  - STAC → `extent.temporal.interval`  
  - DCAT → `dct:temporal`  
- All datasets must include:
  - `start_time`  
  - `end_time`  
  - Temporal uncertainty when available  
- Time normalization supports:
  - Gregorian  
  - Historical dates  
  - Fuzzy temporal bounds  

---

## 🔐 Governance & CARE Architecture

Governance metadata is mandatory at all layers.

### CARE Rules Applied
- Generalization for sacred or sensitive sites  
- Spatial redaction based on sovereignty domain  
- Cultural data must include CARE tags:
  - Authority-to-control  
  - Collective benefit  
  - Responsibility  
  - Ethics  

### Licensing
- SPDX-driven: MIT, CC-BY, public domain, dataset-specific  
- Every dataset requires:
  - `license`  
  - `source`  
  - `rights_holder`  
  - `attribution`  

### Provenance
- PROV-O  
- JSON-LD metadata  
- Transformation logs  
- Toolchain info from `tools/**`  
- SBOM references  

---

## 📈 Telemetry & Quality Architecture

Telemetry includes:

- Performance of pipeline jobs  
- Energy usage & carbon footprint  
- Data quality metrics:
  - Missingness  
  - Outlier checks  
  - CRS errors  
  - Geometry validity  
- Drift detection for:
  - Tabular  
  - Raster  
  - Vector datasets  

Telemetry outputs are aggregated into:

`releases/<version>/focus-telemetry.json`

---

## 🧪 Validation Architecture

Validation includes:

- Schema validation (JSON, YAML, STAC, DCAT)  
- Spatial validation:
  - Topology checks  
  - Geometry validity  
  - CRS uniformity  
- Tabular validation:
  - Null/duplicate detection  
  - Range checks  
- Raster validation:
  - COG compliance  
  - Geotransform integrity  
  - Resolution matching  

All validations must pass before publishing.

---

## 🧠 AI & Enrichment Architecture

AI pipelines enrich raw data into structured entities:

- OCR extraction, text cleanup, language normalization  
- NER + entity linking to Neo4j  
- Topic modeling for Story Node v3  
- Raster segmentation  
- Change detection  
- Predictive modeling (climate/hydrology)  

AI-derived content must include:

- Confidence  
- Lineage  
- CARE disclaimers  
- Model metadata  
- Restrictions (per `ai_transform_prohibited`)  

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Complete rebuild under KFM-MDP v10.4; added lifecycle model, governance, telemetry, STAC/DCAT alignment |
| v10.3.2 | 2025-11-14 | Added drift + sustainability tracking; improved provenance |
| v10.3.1 | 2025-11-13 | Initial data platform architecture |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>