---
title: "🌡📚 KFM v11 — Climate AI Training Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/training/climate/datasets/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/climate-training-datasets-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-training-climate-datasets-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Dataset Group"
intent: "climate-training-datasets"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Climate-Sensitive"

classification: "Public (Governed)"
sensitivity: "Moderate (hazard + climate implications)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌡📚 **KFM v11 — Climate AI Training Datasets**  
`docs/pipelines/ai/training/climate/datasets/`

**Purpose**  
Define the **canonical governed dataset suite** for all climate AI training pipelines,  
including atmospheric chemistry, PM2.5/ozone modeling, smoke/visibility prediction,  
heat-risk estimation, fire danger metrics, and climate–surface interaction modeling.

This document specifies dataset lineage, validation, provenance, FAIR+CARE rules,  
STAC/DCAT contracts, and sustainability metrics required for training-safe climate AI.

</div>

---

## 📘 1. Overview

Climate AI models in KFM ingest **heterogeneous, multi-resolution datasets**, including:

- **CAMS** (Copernicus Atmosphere Monitoring Service) reanalysis & forecast fields  
- **ERA5/ERA5-Land** atmospheric reanalysis  
- **NOAA HRRR/RTMA** high-frequency atmospheric fields  
- **AQS / AirNow** air-quality observations  
- **NLCD/CDL** landcover & land-use layers  
- **MODIS/VIIRS** fire, smoke, AOD, vegetation indices  
- **WRF-Chem / CMAQ** chemistry model surrogates for training  
- **Topography** (DEM, slope, aspect, TPI, TRI)  
- **Soil & hydrology** context layers  
- **H3 partitions** for scalable spatial slicing & privacy  

This module defines **standards for ingestion, storage, lineage, validation,  
and FAIR+CARE governance** of all climate training datasets.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/training/climate/datasets/
├── 📄 README.md
│
├── 🌍 cams/                         # CAMS reanalysis & forecast fields
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
├── 🌬️ era5/                        # ERA5 / ERA5-Land training fields
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
├── 🌀 hrrr/                         # NOAA HRRR/RTMA high-frequency atmospheric fields
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
├── 🧪 air/                          # AQS/AirNow observational training data
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
├── 🏞️ landcover/                   # NLCD/CDL landcover layers
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
├── 🔥 fire/                         # Fire/smoke/AOD/FRP training datasets
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
├── 🌱 soil/                         # Soil moisture / hydric soils / derived layers
│   ├── 📄 README.md
│   ├── 🗂️ stac/
│   └── 🧪 validation/
│
└── 💧 hydro/                        # Hydrological training datasets
    ├── 📄 README.md
    ├── 🗂️ stac/
    └── 🧪 validation/
~~~

---

## 🧬 3. Dataset Requirements (v11)

Each climate training dataset MUST include:

### Required Metadata

| Field | Description | Required |
|-------|-------------|----------|
| `dataset_id` | Unique KFM dataset ID | ✔ |
| `version` | Dataset version | ✔ |
| `source` | CAMS / ERA5 / HRRR / AQS / NLCD / etc. | ✔ |
| `temporal_coverage` | Time range | ✔ |
| `spatial_coverage` | Bounding box or region | ✔ |
| `crs` | Coordinate reference system | ✔ |
| `kfm:h3_res` | Spatial indexing resolution | ✔ |
| `kfm:domain` | `"climate"` | ✔ |
| `stac_item` | STAC Item metadata | ✔ |
| `provenance` | PROV-O block | ✔ |
| `lineage_source` | OpenLineage run linking | ✔ |
| `kfm:sensitivity_flag` | CARE classification | ✔ |
| `kfm:energy_wh` | Energy used to ingest/process | ✔ |
| `kfm:carbon_gco2e` | Carbon footprint | ✔ |

### Required Assets

- GeoParquet / Zarr / NetCDF / GRIB  
- STAC Collection  
- Dataset dictionary (variables, units, methods)  
- JSON-LD metadata block (domain-specific semantics)  
- Provenance bundle  

### Required Governance Fields

- CARE metadata  
- Sovereignty compliance (no sensitive-region leakage)  
- Data license + usage rights  
- Validation logs (schema, spatial, temporal)  
- Energy/carbon metrics  

---

## 🧪 4. Validation Requirements (v11)

All climate training datasets MUST pass:

### ✔ Schema Validation  
- Variable names, units, types, ranges  
- Grid consistency (lat/lon or projected)  
- Time axis monotonicity & completeness  

### ✔ Spatial Validation  
- CRS correctness  
- H3 partition alignment  
- No spatial discontinuities  
- Terrain/ocean masks consistent  

### ✔ Temporal Validation  
- Matching CAMS/ERA5/HRRR cadence  
- No duplicated timestamps  
- Leap second/day edge handling  

### ✔ FAIR+CARE Validation  
- CARE-sensitive regions masked/generalized  
- ACES: Authority, Collective Benefit, Ethics, Sustainability compliance  
- Model suitability tags  

### ✔ Sustainability Validation  
- Energy & carbon usage below governance threshold  
- Logged + stored in telemetry pipeline  

Validation failures → block ingestion & require governance review.

---

## 🌐 5. Provenance & STAC/DCAT Integration

Each dataset MUST provide:

### STAC Metadata

- Collection + Item  
- `datetime` / temporal interval  
- Spatial extent  
- Variables + units  
- Links to provenance, lineage, explainability (if relevant)  

### PROV-O Lineage

- `prov:Activity` — ingestion/processing run  
- `prov:used` — raw data sources  
- `prov:generated` — processed dataset  
- `prov:wasAssociatedWith` — execution agent  

### OpenLineage

- Run ID  
- Inputs (raw streams)  
- Outputs (processed artifacts)  
- Runtime & resource metrics  

---

## 🧩 6. Climate Training Dataset Types

### 🌍 CAMS  
Global atmospheric chemistry & aerosol fields (PM2.5, ozone, wind, humidity).

### 🌬️ ERA5 / ERA5-Land  
Reanalysis for historical climate training.

### 🌀 HRRR / RTMA  
Sub-hourly, high-resolution fields for nowcasting + dynamic training.

### 🧪 Observations (AQS / AirNow)  
Training targets for PM2.5/ozone surrogates.

### 🏞️ Landcover / Surface  
NLCD/CDL + MODIS/VIIRS surrogates.

### 🔥 Fire & Smoke  
AOD, FRP, smoke plume height, HRRR-Smoke, NRT VIIRS.

### 🌱 Soil & Surface Moisture  
Soil moisture (ESA-SMOS, NOAA), hydric soils, infiltration factors.

### 💧 Hydrology  
Runoff, infiltration, snowcover, water-balance, river discharge surrogates.

---

## 📡 7. Telemetry & Sustainability

Each dataset ingest MUST record:

- `kfm.energy_wh`  
- `kfm.carbon_gco2e`  
- `kfm.records_processed`  
- Compute hardware class  
- Storage footprint  
- Temporal coverage processed  

Telemetry flows into:

- `releases/v11.2.3/climate-training-datasets-telemetry.json`  
- Reliability SLO dashboards  
- Focus Mode sustainability overlays  

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Training datasets generate Story Nodes for:

- Dataset lineage (where it came from)  
- Climate variables included  
- Temporal/spatial coverage  
- FAIR+CARE notes  
- Sustainability impact  
- Governance compliance  

These nodes feed into Focus Mode Climate Explorer.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 climate training dataset specification; full lineage, CARE, STAC compliance. |

---

<div align="center">

🌡📚 **Kansas Frontier Matrix — Climate Training Datasets (v11.2.3)**  
Transparent · Governed · FAIR+CARE · Provenance-Rich · Energy-Aware  

[📘 Docs Root](../../../../../..) · [🤖 Climate Training Pipelines](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>