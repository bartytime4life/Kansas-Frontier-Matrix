---
title: "🌬️ Kansas Frontier Matrix — Air Domain Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/air/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · Atmospherics Working Group · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:docs:pipelines:air:index:v11.2.2"
semantic_document_id: "kfm-pipelines-air-index"
event_source_id: "ledger:docs/pipelines/air/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/air-domain-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/air-domain-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public Document"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I2-R3"
care_label: "CARE · Responsible Environmental Data Handling"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
indigenous_rights_flag: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🌬️ **Kansas Frontier Matrix — Air Domain Pipelines (v11.2.2)**  
`docs/pipelines/air/README.md`

**Purpose**  
Provide the authoritative overview of the **Air Domain pipelines** in KFM v11, including ingestion, transformation, STAC/DCAT cataloging, temporal normalization, atmospheric modeling, health-impact overlays, FAIR+CARE governance, lineage, and sustainability telemetry.

</div>

---

## 📘 1. Overview

The **Air Domain** integrates Kansas-wide environmental air-quality datasets, including:

- **AirNow** (real-time & historical AQ)  
- **EPA AQS**  
- **NOAA HRRR smoke & particulate forecasts**  
- **Satellite-derived aerosols** (Sentinel-5P / MODIS / VIIRS)  
- **Local/municipal sensors** (AQMesh, PurpleAir, low-cost sensor networks)  
- **Atmospheric chemistry models** (CMAQ, CAMx – v11.4 expansion)  

These pipelines support:

- Public health analysis  
- Hazard mapping (smoke, ozone, PM2.5)  
- Environmental justice assessments  
- Climate & hydrology cross-domain joins  
- Story Node v3 narratives (smoke events, ozone episodes)  
- Focus Mode v3 interpretability layers  

Every pipeline in this domain must follow **FAIR+CARE** standards and KFM’s reproducible, governed architecture.

---

## 🗂️ 2. Directory Layout (Emoji Style A, v11.2.2)

```text
docs/pipelines/air/
├── 📄 README.md
│
├── 📂 airnow/                      # AirNow ingest, UTC normalization, STAC/DCAT
│   ├── 📄 README.md
│   └── 📂 ingest/
│
├── 📂 aqs/                         # EPA AQS ingest & harmonization
│   └── 📄 README.md
│
├── 📂 hrrr/                        # HRRR smoke, particulate, & forecasts
│   └── 📄 README.md
│
├── 📂 satellite/                   # S5P / MODIS / VIIRS aerosols, AI fusion layers
│   └── 📄 README.md
│
├── 📂 sensors/                     # Low-cost sensor networks (AQMesh, PurpleAir)
│   └── 📄 README.md
│
└── 📂 stac/                        # Air domain STAC collections + metadata profiles
    └── 🌐 air-domain-collection.json
```

All submodules follow **KFM-MDP v11.2.2**, with enforced:

- Single H1  
- Required front-matter fields  
- Directory-diagram formatting  
- No broken boxes  
- STAC, DCAT, PROV-O, and CARE alignment  

---

## 🌬️ 3. Air Domain Architecture (v11.2.2)

```mermaid
flowchart TD
    A["Raw Air Datasets\n(AirNow · AQS · HRRR · Satellites · Sensors)"]
        --> B["Ingest Layer\n(time normalization · schema validation)"]

    B --> C["Transformation Layer\n(harmonization · bias correction · QA/QC)"]

    C --> D["Fusion Layer\n(model blends · PM2.5 estimators · smoke overlays)"]

    D --> E["Catalog Layer\n(STAC · DCAT · JSON-LD provenance)"]

    E --> F["Lineage + Telemetry\n(OpenLineage · OTel v11 · Energy/Carbon)"]

    F --> G["KFM Lake\n(GeoParquet · COG · Tiles · Graph ingestion)"]

    G --> H["Apps & Analytics\n(Focus Mode · Story Nodes · Hazards UI · EJ tools)"]
```

Architecture pillars:

- **Temporal integrity**  
- **FAIR+CARE governance**  
- **Reproducibility & lineage**  
- **Atmospheric science correctness**  
- **Cross-domain join safety**  

---

## 🧩 4. Air Domain Modules (Summary)

### 4.1 AirNow (Ingest + Time Normalization)
- UTC normalization  
- Offset/DST explicit handling  
- Period alignment enforcement (period_begin)  
- STAC Item production  
- Validation + telemetry  

Location:  
`docs/pipelines/air/airnow/`

---

### 4.2 AQS (EPA) Integration
- Regulated monitoring station data  
- QA/QC flags  
- Harmonized pollutants (PM2.5, O₃, NO₂, SO₂)  
- Long-term trend joins  

Location:  
`docs/pipelines/air/aqs/`

---

### 4.3 HRRR Atmospheric Model
- Smoke (near-surface + vertically integrated)  
- PM2.5 forecast surrogates  
- Plume transport modeling  
- Raster → COG normalization  

Location:  
`docs/pipelines/air/hrrr/`

---

### 4.4 Satellite Aerosols (S5P / MODIS / VIIRS)
- NO2, SO2, AOD, UVAI  
- Orbital → Level-2 → gridded KFM tiles  
- AI super-resolution (v11.3+)  

Location:  
`docs/pipelines/air/satellite/`

---

### 4.5 Low-Cost Sensor Networks
- PurpleAir, AQMesh, Clarity  
- Calibration & bias-correction models  
- Neighborhood-scale AQ  

Location:  
`docs/pipelines/air/sensors/`

---

## 🌐 5. STAC & DCAT Integration (Air Domain)

Air domain STAC Collections MUST include:

- Spatial extent (Kansas full domain)  
- Temporal extent (dataset-level)  
- STAC fields:  
  - `datetime` / `start_datetime` / `end_datetime`  
  - Asset-level media types  
  - `kfm:airQualityVariable`  
  - `kfm:temporalNormalization`  

Root Air STAC Collection:  
`docs/pipelines/air/stac/air-domain-collection.json`

---

## 🔗 6. Provenance & Lineage (OpenLineage v2.5)

Air pipelines emit lineage for:

- Ingest steps  
- Time normalization  
- QA/QC stages  
- Harmonic blends  
- Forecast runs  
- AI aerosol estimates  

Facets emitted:

- TimeNormalizationFacet  
- AtmosphericVariableFacet  
- EnergyFacet  
- CarbonFacet  
- CAREFacet  

---

## 🌱 7. Telemetry & Sustainability

Metrics captured:

- `energy_wh`  
- `carbon_gco2e`  
- `runtime_sec`  
- `rows_processed`  
- anomaly counts (DST, missing data, extreme outliers)  

Telem bundles stored at:

```
../../../releases/v11.2.2/air-domain-telemetry.json
docs/reports/telemetry/air/air-domain-*.json
```

---

## ⚖️ 8. FAIR+CARE Considerations

- All datasets maintain license + usage rules  
- Environmental justice layers require correct AIR/HRRR/NOAA crosswalk  
- No sensitive health-related locations stored  
- CARE compliance for datasets intersecting culturally significant boundaries  

---

## 🕰️ 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-28 | Air domain index created; full emoji layout; STAC/DCAT integration; lineage + telemetry sections added. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🌬️ Air Domain Pipelines v11.2.2 · FAIR+CARE Certified · Temporal Integrity · Diamond⁹ Ω / Crown∞Ω  

[⬅️ Back to Pipelines Root](../README.md) •  
[🌬️ AirNow Module](airnow/README.md) •  
[🌀 AQS](aqs/README.md) •  
[🔥 HRRR](hrrr/README.md)  

</div>
~~~~markdown

