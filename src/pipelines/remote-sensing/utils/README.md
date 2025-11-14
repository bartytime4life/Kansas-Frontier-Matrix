---
title: "🛠️ Kansas Frontier Matrix — Remote Sensing Utility Modules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/utils/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-utils-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Remote Sensing Utility Modules**  
`src/pipelines/remote-sensing/utils/README.md`

**Purpose:**  
Provide **shared, deterministic utility modules** for all Remote Sensing pipelines (LandsatLook, Sentinel-1/2, NAIP, MODIS/VIIRS, hazards, indices).  
These utilities support **STAC ingestion**, **geometry normalization**, **index math**, **SAR preprocessing**, **cloud masking**, **AI-safe metadata extraction**, **Neo4j-ready spatial transforms**, and **FAIR+CARE governance**.

<img alt="Utils" src="https://img.shields.io/badge/Utils-Remote_Sensing-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Integrated-orange"/>
<img alt="Deterministic" src="https://img.shields.io/badge/Deterministic-Yes-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Stable-success"/>

</div>

---

## 📘 Overview

These modules provide **pure functions** and **side-effect-controlled helpers**, enabling:

- Reliable STAC asset manipulation  
- Spectral band extraction & index computation  
- Geometry standardization for AOI operations  
- SAR pre-processing utilities  
- Sensor harmonization (GSD, CRS)  
- Cloud and shadow masking  
- Json-LD / provenance utilities  
- Telemetry-safe logging wrappers  
- CARE-governed masking & H3 generalization utilities  

All utilities here are imported by multiple pipelines and MUST remain:

- Deterministic  
- Fully typed  
- FAIR+CARE-ready  
- Schema-safe  
- MCP-DL v6.3 compliant  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/utils/
├── README.md                   # This file
│
├── stac_utils.py               # STAC asset helpers, pagination, roles, checksum logic
├── geometry_utils.py           # CRS transforms, centroid/bbox extraction, dissolve ops
├── spectral_utils.py           # Band math (NDVI, NDMI, NDWI, SAVI, custom indices)
├── sar_utils.py                # SAR terrain-correction, speckle filtering wrappers
├── cloud_mask_utils.py         # Cloud/shadow masking for Landsat/S2
├── ai_utils.py                 # AI-safe metadata extraction for summarization pipelines
├── provenance_utils.py         # JSON-LD lineage, STAC → RDF mapping helpers
├── neo4j_spatial_utils.py      # WKT/POINT generation, spatial constraints
├── telemetry_utils.py          # Structured telemetry logging for ETL stages
└── care_masking_utils.py       # Sensitive-area masking & H3 generalization
~~~~~

---

## 🧩 Module Summaries

### 1. **stac_utils.py**
Deterministic helpers for:

- STAC Item/Collection loading  
- Asset role parsing & validation  
- Pagination (`links[].rel == "next"`)  
- Checksums & deduplication  
- Datetime normalization  
- STAC → KFM metadata mapping  

---

### 2. **geometry_utils.py**
Geometry operations include:

- CRS reprojection (pyproj/Shapely)  
- Polygon dissolve → single polygon  
- Centroid computation (EPSG:4326)  
- BBOX extraction  
- AOI intersection tests  
- Precision reduction for sensitive areas  

Used in all overlap/hazard/index pipelines.

---

### 3. **spectral_utils.py**
Index math (vectorized or raster-cell):

- NDVI = (nir − red) / (nir + red)  
- NDMI = (nir − swir1) / (nir + swir1)  
- NDWI = (green − nir) / (green + nir)  
- SAVI = ((nir − red) / (nir + red + L)) × (1 + L)  

Supports:

- Threshold-based classification  
- Out-of-range corrections  
- Histogram/quantile summaries for telemetry  

---

### 4. **sar_utils.py**
SAR preprocessing:

- Terrain correction (RTC) wrappers  
- Speckle filters: Lee / Refined Lee  
- Radiometric normalization  
- Mask invalid pixels  
- Convert GRD → sigma0/decibel grids  

---

### 5. **cloud_mask_utils.py**
Supports:

- Fmask-style cloud masks  
- Sentinel-2 cloud probability ingestion  
- Combine cloud + shadow + snow masks  
- Propagate mask to spectral calculations  
- Telemetry: `cloud_masked_percent`

---

### 6. **ai_utils.py**
**AI-safety utilities** used by pipelines:

- Safe metadata extraction (no PII)  
- Prompt variable assembly  
- Controlled-vocabulary tags enforcement  
- Refusal detection & logging  
- JSON schema validation for AI outputs  

---

### 7. **provenance_utils.py**
Implements:

- JSON-LD lineage templates  
- STAC → RDF/GeoSPARQL mapping (WKT + Feature classes)  
- Dataset → Scene → County → AOI lineage export  
- Checksum lineage chain building  

Used by RDF exports + governance logging.

---

### 8. **neo4j_spatial_utils.py**
Standardized Neo4j spatial handling:

- POINT generation `{lon,lat,srid:4326}`  
- WKT generation for polygons  
- Constraint/index helper methods  
- Scene → County relationship writer helpers  

---

### 9. **telemetry_utils.py**
Structured NDJSON telemetry:

- Stage-based metrics  
- Pixel counts, overlap metrics  
- AI summary stats  
- Hazard index stats  
- Energy/CO₂e estimates  
- Error classification  
- Writes normalized events for CI aggregation  

Writes to paths defined by pipeline config:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

Aggregated into:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

### 10. **care_masking_utils.py**
Governance-critical utilities:

- H3 hex generalization for sensitive polygons  
- Massaging geometries to legal shareable resolution  
- CARE rule enforcement:
  - sovereignty  
  - cultural sensitivity  
  - habitat masking  
- Detects if a Scene intersects any protected areas  

---

## ⚖️ FAIR+CARE & Governance Integration

All utils MUST:

- Respect `care_label` as passed by pipeline config  
- Apply masking/generalization when required  
- Maintain provenance references when altering geometry  
- Avoid exporting sensitive detail in logs or summaries  
- Log governance flags into NDJSON telemetry  

Governance ledger reference:

~~~~~text
../../../../../docs/reports/audit/data_provenance_ledger.json
~~~~~

---

## 📡 Telemetry Compliance

All modules follow observability fields defined in:

~~~~~text
src/pipelines/architecture/observability/fields.md
~~~~~

Telemetry schemas validated via:

~~~~~text
../../../../../schemas/telemetry/pipelines-remote-sensing-utils-v1.json
~~~~~

---

## 🧪 Testing Requirements

Each utility module MUST include:

- Unit tests (pytest)  
- Type-checked signatures  
- Deterministic outputs  
- Golden-file outputs for geometry + spectral index cases  
- CI validation through:  
  - `codeql.yml`  
  - `trivy.yml`  
  - `telemetry-export.yml`  
  - `faircare-validate.yml`  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Introduced complete Remote Sensing utility suite; aligned with FAIR+CARE, telemetry, RDF, Neo4j integration. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Utility Suite**  
Deterministic Helpers × FAIR+CARE Ethics × GeoSPARQL × Remote Sensing Excellence  
© 2025 Kansas Frontier Matrix — MIT License  

</div>