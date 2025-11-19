---
title: "⚠️ Kansas Frontier Matrix — Processed Hazards Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/hazards/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-hazards-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-hazards-readme"
event_source_id: "ledger:data/processed/hazards/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-hazards-processed-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "processed-hazards-datasets"
role: "hazards-domain"
category: "Data · Hazards · FAIR+CARE · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed — community-impacted hazards"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Dataset-level"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"

ontology_alignment:
  cidoc: "E5 Event / E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-hazards-processed-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-hazards-processed-v11-shape.ttl"

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
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next hazards-domain update"
---

<div align="center">

# ⚠️ **Kansas Frontier Matrix — Processed Hazards Data**  
`data/processed/hazards/README.md`

Authoritative, FAIR+CARE-certified **multi-hazard datasets** harmonized from:

- FEMA  
- NOAA (NCEI / SPC)  
- USGS  
- KDHE  
- Other allied state/federal sources  

Supporting:

- 🌍 Public hazard communication  
- 🧪 Research & planning  
- 🧠 Focus Mode v3 hazard narratives  
- 📡 STAC/DCAT-based discovery  
- 🕸 Neo4j hazard graph integration  

All layers are **checksum-verified, schema-aligned, and ethically governed**.

</div>

---

## 1. 📘 Domain Overview

The **Processed Hazards Layer** stores final, schema-validated, and FAIR+CARE-certified datasets representing:

- ⚡ Hazard events (tornadoes, hail, wind, winter storms)  
- 🌊 Flood hazards (FEMA NFHL, riverine flood zones)  
- 🌵 Drought severity and spatiotemporal patterns  
- 🔥 Wildfire occurrences and perimeters  
- 🧮 Multi-hazard composites and hazard intensity indices  
- 👥 Exposure and vulnerability layers (population, assets, infrastructure)  

Key properties:

- All geometries normalized to **EPSG:4326**  
- Temporal values standardized to **ISO 8601**  
- Lineage expressed via **PROV-O** + **ISO 19115**  
- Datasets cataloged via **STAC 1.x** and **DCAT 3.0**  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/processed/hazards/
├── README.md                              ← this file
│
├── hazards_composite_v11.0.0.geojson      ← multi-hazard integrated dataset
├── hazard_intensity_index_v11.0.0.csv     ← per-unit composite severity index
├── hazard_event_frequency_v11.0.0.csv     ← event counts & recurrence metrics
├── flood_risk_zones_v11.0.0.geojson       ← FEMA/USGS-derived flood hazard polygons
├── tornado_tracks_1950_2025_v11.0.0.geojson ← historical tornado tracks
├── wildfire_history_v11.0.0.geojson       ← historical wildfire perimeters
├── drought_severity_index_v11.0.0.parquet ← drought index per H3 cell & time
├── exposure_pop_tract_v11.0.0.parquet     ← population/infrastructure exposure by tract
│
├── stac_collection.json                   ← hazards STAC Collection (v11)
└── metadata/
    ├── checksums.json                     ← SHA-256 checksums for hazards datasets
    ├── faircare_certification.json
    ├── provenance.json                    ← PROV-O lineage exports
    └── schema_validation.json
~~~~

---

## 3. 🔄 Hazards Data Lifecycle

~~~~mermaid
flowchart TD
  A["raw/hazards/*"] --> B["staging/hazards/*\ncleaning · dedupe · CRS fix"]
  B --> C["validation\nschema · FAIR+CARE · QC"]
  C --> D["processing\nper-hazard enrichment"]
  D --> E["integration\nmulti-hazard composites"]
  E --> F["checksums & provenance\nSHA-256 · PROV-O"]
  F --> G["publication\ndata/processed/hazards/*"]
  G --> H["catalog sync\nSTAC/DCAT · Streaming STAC · Focus Mode"]
~~~~

A dataset may enter `data/processed/hazards/` **only if**:

- ✅ Schema validation passes  
- ✅ FAIR+CARE certification is complete  
- ✅ Checksums match SBOM + manifest  
- ✅ Governance ledger entry exists  

---

## 4. 📊 Core Hazards Datasets

| Dataset File                           | Description                                    | Example Use Cases                           |
|----------------------------------------|-----------------------------------------------|---------------------------------------------|
| `hazards_composite_v11.0.0.geojson`    | Multi-hazard exposure surface (all perils)     | Statewide risk dashboards, Focus Mode maps  |
| `hazard_intensity_index_v11.0.0.csv`   | Per-unit (tract/H3) composite severity index   | Ranking regions by hazard burden            |
| `hazard_event_frequency_v11.0.0.csv`   | Annual event counts & intensities by type      | Recurrence analysis, trend detection        |
| `flood_risk_zones_v11.0.0.geojson`     | FEMA NFHL + derived flood risk classes         | Floodplain management & planning            |
| `tornado_tracks_1950_2025_v11.0.0.geojson` | Historical tornado tracks                   | Historic hazard narratives & modeling       |
| `wildfire_history_v11.0.0.geojson`     | Historical wildfire perimeters & severity      | Wildfire risk modeling & planning           |
| `drought_severity_index_v11.0.0.parquet` | Drought index per H3 cell & time            | Drought monitoring & planning               |
| `exposure_pop_tract_v11.0.0.parquet`   | Population & asset exposure metrics by tract   | Vulnerability & impact analysis             |

---

## 5. 🧱 Hazards Schema Requirements (v11)

All hazards datasets must conform to **hazards-schema-v4.0.0** under `schemas/processed/hazards/`.

### 5.1 Common Fields

~~~~text
kfm_id             string   stable KFM hazard ID
domain             string   always "hazards"
schema_version     string   e.g., "v4.0.0"
created            datetime ISO 8601
source             string   data agency codes (e.g., NOAA_SPC, FEMA_NFHL)
checksum           string   sha256-...
fairstatus         string   certified / pending / restricted
governance_ref     string   path in governance ledger
~~~~

### 5.2 🌪 Tornado Tracks Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
tornado_id       string      SPC/NCEI event ID
start_time       datetime    ISO 8601
end_time         datetime    ISO 8601
geometry         GeoJSON     LineString / MultiLineString
ef_scale         integer     0–5
wind_speed_mph   float       estimated peak winds
fatalities       integer     CARE-sensitive
injuries         integer     CARE-sensitive
source           string      "NOAA_SPC", "NCEI"
checksum         string      sha256-...
~~~~

### 5.3 🌊 Flood Risk Zones Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
flood_id         string      NFHL polygon ID
zone             string      A, AE, AO, VE, X, etc.
risk_class       string      high / moderate / low
geometry         GeoJSON     Polygon or MultiPolygon
source           string      FEMA NFHL / USGS
effective_date   date        effective map date
checksum         string      sha256-...
~~~~

### 5.4 🔥 Wildfire Events Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
fire_id          string      unique fire identifier
start_time       datetime    ignition time
end_time         datetime    contained time
area_ha          float       burned area in hectares
cause            string      lightning / human / unknown
geometry         GeoJSON     Polygon
source           string      USGS / state agency
checksum         string      sha256-...
~~~~

### 5.5 🌵 Drought Severity Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
cell_id          string      H3 index
period_start     datetime    ISO 8601
period_end       datetime    ISO 8601
drought_index    float       normalized 0–10
category         string      D0–D4 (U.S. Drought Monitor)
source           string      NIDIS / KDHE
checksum         string      sha256-...
~~~~

---

## 6. 💠 Hazard Intensity Index (HII v4.0)

The **Hazard Intensity Index (HII)** combines multiple hazard components into one severity value per spatial unit.

ASCII-safe formula:

~~~~text
HII = (w1 * tornado_severity)
    = (w2 * flood_risk)
    + (w3 * drought_severity)
    + (w4 * wildfire_severity)

where:
- w1, w2, w3, w4 are weights in [0, 1]
- tornado_severity, flood_risk, drought_severity, wildfire_severity are normalized 0–10
~~~~

Outputs are stored in:

`hazard_intensity_index_v11.0.0.csv`

Used for:

- Focus Mode ranking and sorting  
- Regional hazard comparison  
- Long-term resilience planning  

---

## 7. 🧍 Exposure & Vulnerability Modeling

Exposure datasets estimate:

- Population totals and breakdowns  
- Critical infrastructure presence  
- Economic valuations (property, agriculture)  
- Social vulnerability indicators  

Spatial units:

- Census tracts  
- Block groups  
- H3 hex cells  

Example fields:

~~~~text
unit_id, population_total, population_65_plus, population_under_5,
housing_units, critical_facilities, exposure_score
~~~~

---

## 8. ⚖️ FAIR+CARE Governance — Hazards Domain

The hazards domain requires **strict ethical governance**:

- CARE review for data depicting harm, loss, or trauma  
- Masking/generalization of sensitive geometries, especially for:
  - Shelters, critical facilities  
  - Vulnerable communities  
  - Tribal/sovereign lands  

Governance artifacts:

~~~~text
data/processed/hazards/metadata/faircare_certification.json
docs/reports/audit/data_provenance_ledger.json
docs/standards/faircare/HAZARDS-GUIDE.md
~~~~

---

## 9. 🔐 Integrity & Lineage

Integrity is enforced via:

- SHA-256 checksums:
  - `data/checksums/manifest.json`
  - `data/archive/2025Q4/checksums/hazards_checksums.json`
- Manifest parity with `sbom_ref` and `manifest_ref`

Lineage is expressed as:

- `prov:Entity` for each processed dataset  
- `prov:wasDerivedFrom` linking back to raw/staging datasets  
- `prov:wasGeneratedBy` linking to ETL/AI pipeline runs  

Lineage exports:

~~~~text
data/processed/hazards/metadata/provenance.json
docs/reports/audit/data_provenance_ledger.json
~~~~

---

## 10. 🌱 Telemetry & Sustainability

For hazards pipelines, telemetry tracks:

- `energy_wh` per job  
- `carbon_gCO2e` per job  
- runtime, data volume, validation failure counts  

Recorded in:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-hazards-processed-v11.json
~~~~

These metrics support:

- Sustainability assessments  
- Governance dashboards  
- Infrastructure optimization  

---

## 11. 🌐 STAC/DCAT & Focus Mode Integration

Hazards datasets:

- Are represented in a STAC Collection (`stac_collection.json`)  
- Have corresponding STAC Items & DCAT Datasets  
- Provide spatial/temporal extents and lineage fields for graph ingestion  

Focus Mode:

- Renders hazard overlays with narrative context  
- Uses metadata fields (hazard_type, intensity, dates) for explanation and UI  

---

## 12. 🧾 Internal Citation

~~~~text
Kansas Frontier Matrix (2025). Processed Hazards Data (v11.0.0).
Multi-hazard, FAIR+CARE-certified, checksum-verified datasets for Kansas hazard
assessment and resilience planning, aligned to STAC 1.x, DCAT 3.0, ISO 19115,
and KFM-OP v11 with full provenance and sustainability telemetry.
~~~~

---

## 13. 🕰 Version History

| Version | Date       | Summary                                                                                   |
|--------:|------------|-------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 upgrade; added schema tables, FAIR+CARE v11, STAC/DCAT v11, and telemetry v4.   |
| v10.2.2 | 2025-11-12 | Streaming STAC, Focus v2.1 integration, telemetry v2, governance path updates.           |
| v10.0.0 | 2025-11-09 | Initial processed hazards README & directory structure.                                   |

<div align="center">

**Kansas Frontier Matrix — Hazards Domain**  
⚠️ FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

[⬅️ Back to Processed Layer](../README.md) ·  
[📐 Data Architecture](../../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>