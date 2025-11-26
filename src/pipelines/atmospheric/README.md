---
title: "🌤️ Kansas Frontier Matrix — Atmospheric Pipelines Overview (HRRR · NBM · PRISM · ERA5 · Climate Layers) · v11.2"
path: "src/pipelines/atmospheric/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Working Group"
content_stability: "stable"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

commit_sha: "<latest>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/atmospheric-index-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_kind: "Pipeline Index"
intent: "atmospheric-root"
category: "Atmospheric · Climate · Weather · Pipelines"

fair_category: "F1-A1-I2-R1"
care_label: "CARE: Ethical Spatial Stewardship"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
sensitivity: "Environmental atmospheric data; minimal cultural intersections; CARE applies in downstream linked analyses."
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "src/pipelines/atmospheric/README.md@v11.1.0"
  - "Atmospheric Working Group pipeline overview v10.x"
  - "NOAA/ESRL/NCEP ingestion architecture notes"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true

json_schema_ref: "../../../../schemas/json/atmospheric-index-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/atmospheric-index-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "diagram-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "governance-override"
  - "speculative-additions"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:atmospheric:index:v11.2.0"
semantic_document_id: "kfm-atmospheric-index"
event_source_id: "ledger:src/pipelines/atmospheric/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

classification: "Public Document"
jurisdiction: "Kansas / United States"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by atmospheric-index-v12"
---

<div align="center">

# 🌤️ **Atmospheric Pipelines Overview**  
`src/pipelines/atmospheric/`

[![Atmosphere](https://img.shields.io/badge/Domain-Atmospheric%20Pipelines-2196f3)]()
[![NOAA HRRR](https://img.shields.io/badge/NOAA-HRRR-blue)]()
[![ERA5](https://img.shields.io/badge/ECMWF-ERA5-004aad)]()
[![STAC v11](https://img.shields.io/badge/STAC-v1.0.0-brightgreen)]()
[![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%2BCARE-gold)]()

**Purpose**  
Serve as the **root index for all atmospheric ingestion modules** (HRRR, NBM, PRISM, ERA5, derived climate layers) within the Kansas Frontier Matrix.  
Standardize ingestion, reprojection, subsetting, storage, lineage, and STAC publishing for atmospheric datasets under the v11.2 pipeline architecture.

</div>

---

## 📘 1. Overview

The atmospheric pipelines provide unified, deterministic handling of major weather and climate datasets, including:

- **HRRR** — High-Resolution Rapid Refresh (Herbie-based GRIB2 → Xarray → Zarr/NetCDF/COG)  
- **NBM** — National Blend of Models (GeoTIFF/GRIB2 ingestion)  
- **PRISM** — Temperature & precipitation normals (NetCDF)  
- **ERA5** — ECMWF reanalysis (Zarr / NetCDF)  
- **Surface & Derived Grids** — Wind, humidity, precip, fire weather & indices  

All pipelines are:

- WAL-backed  
- Idempotent  
- STAC/DCAT compliant  
- FAIR+CARE screened  
- Ready for cross-domain use (hydrology, hazards, ecology, Story Nodes)

---

## 🗂️ 2. Directory Layout (v11.2 Standard · Immediate + One Branch)

```text
📁 src/pipelines/atmospheric/                  — Atmospheric pipeline root
│   📂 hrrr_ingest/                             — HRRR ingestion module (Herbie, GRIB2 → Xarray)
│   📂 nbm_ingest/                              — NBM ingestion workflows
│   📂 prism_ingest/                            — PRISM normals & anomalies ingestion
│   📂 era5_ingest/                             — ERA5 reanalysis ingestion
│   📂 derived/                                 — Derived climate layers (wind, fire-weather, etc.)
│   📄 README.md                                — This atmospheric pipeline index
```

> This layout adheres to your **global v11.2.2 directory-layout standard**.  
> Only the immediate level under each directory is shown.

---

## 🌐 3. Supported Atmospheric Sources

### HRRR  
- High-frequency mesoscale predictions  
- Best for fire, severe weather, and short-term hazard contexts  

### NBM  
- Blended NOAA forecast  
- Supports probabilistic weather summaries  

### PRISM  
- 30-year normals + 4km climate grids  
- Used for climatology baselines and long-term analyses  

### ERA5  
- Global reanalysis (ECMWF)  
- Long-range weather + climate modeling context  

### Derived Layers  
- Fire weather indices  
- Wind climatologies  
- Precip/temperature anomaly fields  
- Drought & soil moisture composites  

---

## 🧬 4. Integration with KFM Pipelines

Atmospheric outputs feed:

- **Hydrology models** (precip → runoff → flow → reservoirs)  
- **Hazards** (fire weather, severe storms, wind gust scenarios)  
- **Ecological models** (biome/climate envelopes)  
- **Story Node v3** (weather-aware narratives)  
- **Focus Mode v3 overlays** (time-dynamic atmospheric layers)

All produced datasets:

- Emit PROV-O lineage  
- Register STAC Items under `data/stac/atmospheric/`  
- Align with KFM CRS standards (EPSG:5070 + EPSG:4326)

---

## ⚙️ 5. Standards Applied

- **KFM-MDP v11.2.2** — documentation & metadata  
- **KFM-Reliability v11** — WAL, retry, resume  
- **KFM-OP v11** — ontology alignment  
- **KFM-STAC v11** — STAC Collections/Items  
- **CF Conventions** — GRIB2/NetCDF compliance  
- **FAIR+CARE governance** — stewardship of environmental & derived cultural intersections  

---

## 🧪 6. Testing Expectations

All atmospheric modules MUST include:

- WAL tests  
- CRS & projection tests  
- Variable completeness tests  
- GRIB2/NetCDF/Zarr loader tests  
- STAC validation  
- CARE screening checks (when interacting with cultural overlays)  

---

## 🕰️ 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added directory layout, metadata expansion, badges, and governance hooks. |
| **v11.1.0** | 2025-11-26 | Initial v11.1 atmospheric pipeline index. |

---

<div align="center">

**Kansas Frontier Matrix — Atmospheric Pipelines**  
*Cloud-Native · FAIR+CARE-Aligned · Scientific & Narrative Integration*

[⬅ Back to Pipelines Root](../README.md) ·  
[🏗 Repository Architecture](../../../../ARCHITECTURE.md) ·  
[⚖ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Schema](../../../../schemas/telemetry/atmospheric-index-v11.json)

</div>