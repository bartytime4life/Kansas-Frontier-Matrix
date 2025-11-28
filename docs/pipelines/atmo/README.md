---
title: "🌀 KFM v11.2.2 — Atmospheric Pipelines Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmo/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../releases/v11.2.2/signature.sig"
attestation_ref: "../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/atmo-telemetry.json"
telemetry_schema: "../../schemas/telemetry/atmo-overview-v11.2.2.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Pipeline Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/atmo"
  applies_to:
    - "etl"
    - "subsetting"
    - "harmonization"
    - "forecast-derivatives"
    - "stac-publication"

semantic_intent:
  - "atmospheric-data"
  - "geospatial-etl"
  - "climate-normalization"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:atmo:index:v11.2.2"
semantic_document_id: "kfm-pipelines-atmo-index-v11.2.2"
event_source_id: "ledger:pipelines-atmo-index-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🌀 **Kansas Frontier Matrix — Atmospheric Pipelines (v11.2.2)**  
`docs/pipelines/atmo/README.md`

**Purpose:**  
Serve as the authoritative index for all atmospheric ETL pipelines in the Kansas Frontier Matrix.  
Includes HRRR, HRRR-derivatives, Air Quality (AQS/AirNow), satellite-based atmos layers, climate harmonization routines, and STAC v11 dataset publication.

</div>

---

## 📘 Overview

The **Atmospheric ETL subsystem** unifies meteorological, climate, and air-quality data for Kansas.  
All pipelines follow:

- Deterministic, seed-controlled ETL  
- FAIR+CARE-aligned metadata generation  
- KFM-STAC v11 publishing  
- Full PROV-O lineage  
- Energy + carbon telemetry collection  
- Harmonization to **EPSG:4326**, **UTC**, and **CF-v1.11**  

Supported atmospheric domains:

- **HRRR (High-Resolution Rapid Refresh)**  
- **Surface & upper-air variables**  
- **Wind fields & gust diagnostics**  
- **AQS / AirNow AQI ETL**  
- **Smoke, PM2.5, visibility**  
- **ERA5 / reanalysis hooks (future)**  
- **Climate normals & climatology fusion**

These pipelines power:

- Real-time overlays  
- Historic atmos change detection  
- Story Nodes for environmental interpretation  
- Focus Mode narratives tied to weather, smoke, or visibility events

---

## 🧱 Pipeline Index (Current Atmospheric Suite)

| Pipeline | Description |
|----------|-------------|
| **HRRR Smart Subsetting** | AOI-aware clipping, delta engine, STAC v11 export |
| **Climate Normalization (UTC/CF)** | Harmonizes temporal & units across models |
| **AQS / AirNow ETL** | Air quality ingestion and pollutant-level STAC datasets |
| **Wind & Smoke Derivatives** | HRRR post-processing for wind stress & visibility |
| **Raster Harmonization Engine** | Reprojection, grid alignment, COG conversion |
| **Atmospheric Story Node Writer** | Generates narrative semantic nodes from atmos events |

---

## 📦 Directory Layout (Full-Form, Emoji-Semantic)

    docs/pipelines/atmo/
    ├── 📄 README.md                          # This file (index)
    │
    ├── 📁 hrrr-smart-subsetting/             # HRRR delta-aware ETL
    │   └── 📄 README.md
    │
    ├── 📁 climate-normalization/             # UTC/unit harmonization routines
    │   └── 📄 README.md
    │
    ├── 📁 wind-smoke-derivatives/            # Wind/smoke/visibility transforms
    │   └── 📄 README.md
    │
    ├── 📁 air-quality/                       # AQS + AirNow ingestion
    │   └── 📄 README.md
    │
    ├── 📁 raster-harmonization/              # Grid reprojection + COG conversion
    │   └── 📄 README.md
    │
    └── 🤖 .github/workflows/                 # CI for atmospheric pipelines
        ├── 🌀 hrrr-smart-subsetting.yml
        ├── 🌀 climate-normalization.yml
        ├── 🌀 wind-smoke-derivatives.yml
        ├── 🌀 air-quality.yml
        └── 🌀 raster-harmonization.yml

---

## 🔧 Standards Alignment

All atmospheric pipelines comply with:

- **CF Conventions v1.11**  
- **KFM Temporal Contract v11** (UTC normalization)  
- **KFM Spatial Contract v11** (EPSG:4326 baseline)  
- **STAC 1.0.0** with KFM-STAC v11 extensions  
- **DCAT 3.0 dataset cataloguing**  
- **PROV-O lineage** for ingest → transform → publish  
- **FAIR+CARE** ethics and openness requirements  

---

## 🧪 Validation & CI/CD

Atmospheric pipelines run:

- ETL unit tests  
- Threshold contract tests (KFM-PDC v11)  
- STAC schema validation  
- Lint checks (flake8, black, mypy)  
- FAIR+CARE audits  
- Telemetry generation (energy_kwh, carbon_gco2e)  

---

## 🧠 Story Node & Focus Mode Integration

Atmospheric data drives:

- Wind-stress interpretations for archaeological landscapes  
- Smoke visibility interactions in hydrology clusters  
- Climate pattern context for multi-period analyses  
- Automated atmospheric Story Nodes (`data/story/atmo/`)  
- Focus Mode v3 environmental narratives  

Each node cites:

- HRRR/AQS assets  
- STAC lineage  
- Explanatory metadata (PROV-O)  

---

## 🕰️ Version History

- **v11.2.2** — New emoji-mapped full directory tree; v11.2.2 metadata; upgraded CI + STAC integration  
- **v11.0.0** — Initial atmospheric pipeline index  

---

<div align="center">

### 🔗 Footer

[🌐 KFM Home](../../README.md) · [📚 Standards](../../standards/README.md) · [📦 STAC Catalog](../../data/stac/)

</div>

