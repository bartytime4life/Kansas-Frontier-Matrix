---
title: "⚠️ Kansas Frontier Matrix — Processed Hazards Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/hazards/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

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
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next hazards-domain update"
---

<div align="center">

# ⚠️ **Kansas Frontier Matrix — Processed Hazards Data**  
`data/processed/hazards/README.md`

Authoritative, FAIR+CARE-certified multi-hazard datasets for:

- 🌍 Public risk communication  
- 🧪 Research & planning  
- 🧠 Focus Mode v3 hazard narratives  
- 🌐 STAC/DCAT-based discovery  
- 🕸 Neo4j hazard graph integration  

All layers are **checksum-verified, schema-aligned, and ethically governed**.

</div>

---

## 1. 🌋 Domain Overview

The **hazards domain** covers geospatial and tabular datasets describing:

- Extreme weather events (tornadoes, hail, wind, winter storms)  
- Flood hazards (FEMA NFHL, riverine flooding)  
- Drought severity and duration  
- Wildfire occurrences and risk  
- Multi-hazard composites and hazard intensity indices  
- Exposure and vulnerability layers (population, assets, infrastructure)  

Data sources include:

- **NOAA NCEI / Storm Events**  
- **NOAA Storm Prediction Center (SPC)**  
- **FEMA National Flood Hazard Layer (NFHL)**  
- **USGS** (streamflow, landslides, debris flow)  
- **KDHE** (drought, water shortages)  
- Other state and federal hazard datasets  

All processed hazards datasets:

- Are normalized to **EPSG:4326**  
- Include **ISO 19115** metadata and **PROV-O** lineage  
- Are indexed as **STAC Items** and **DCAT Datasets**  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/processed/hazards/
├── README.md                      ← this file
│
├── hazards_composite_v11.0.0.geojson
├── hazard_intensity_index_v11.0.0.csv
├── hazard_event_frequency_v11.0.0.csv
├── flood_risk_zones_v11.0.0.geojson
├── tornado_tracks_1950_2025_v11.0.0.geojson
├── wildfire_history_v11.0.0.geojson
├── drought_severity_index_v11.0.0.parquet
├── exposure_pop_tract_v11.0.0.parquet
│
├── stac_collection.json           ← Hazards STAC Collection (v11)
└── metadata/
    ├── checksums.json             ← SHA-256 checksums for domain datasets
    ├── faircare_certification.json
    ├── provenance.json            ← PROV-O lineage exports
    └── schema_validation.json
~~~~

---

## 3. 🔄 Hazards Data Lifecycle

~~~~mermaid
flowchart TD
  A["raw/hazards/\n(NOAA · FEMA · USGS · KDHE)"]
    --> B["staging/hazards/\ncleaning · dedupe · CRS normalization"]
  B --> C["validation\n(schema · FAIR+CARE · QC)"]
  C --> D["processing\nper-hazard enrichment"]
  D --> E["multi-hazard integration\n(hazards_composite)"]
  E --> F["checksums & provenance\n(SHA-256 · PROV-O)"]
  F --> G["publication\n(data/processed/hazards/*)"]
  G --> H["catalog sync\n(STAC/DCAT · Streaming STAC)"]
~~~~

**Entry condition for publication:**  
A dataset can move into `data/processed/hazards/` **only** when:

- Validation reports show no blocking errors  
- FAIR+CARE certification is complete  
- Checksums are recorded and match SBOM/manifest  
- Governance ledger entry is present  

---

## 4. 📊 Core Hazards Datasets

| Dataset File                           | Description                                    | Example Use Cases                           |
|----------------------------------------|-----------------------------------------------|---------------------------------------------|
| `hazards_composite_v11.0.0.geojson`    | Multi-hazard exposure surface (all perils)     | Statewide risk dashboards, Focus Mode maps  |
| `hazard_intensity_index_v11.0.0.csv`   | Per-unit (tract/H3) composite severity index   | Ranking regions by hazard burden            |
| `hazard_event_frequency_v11.0.0.csv`   | Annual event counts & intensities by type      | Recurrence analysis, trend detection        |
| `flood_risk_zones_v11.0.0.geojson`     | FEMA NFHL + derived flood risk classes         | Floodplain management & planning            |
| `tornado_tracks_1950_2025_v11.0.0.geojson` | Historical tornado tracks and attributes | Historic hazard narratives & modeling       |
| `wildfire_history_v11.0.0.geojson`     | Historical wildfire perimeters & severity      | Wildfire risk modeling & planning           |
| `drought_severity_index_v11.0.0.parquet` | Drought index per H3 cell & time           | Drought monitoring & planning               |
| `exposure_pop_tract_v11.0.0.parquet`   | Population & asset exposure metrics by tract   | Vulnerability & impact analysis             |

---

## 5. 🧩 Hazards Schema Requirements (v11)

All hazards datasets must conform to **data-contract** schemas under `schemas/processed/hazards/`.

### 5.1 🧱 Common Fields

All hazards datasets must include:

- `kfm_id` — stable KFM identifier  
- `domain` — `"hazards"`  
- `schema_version` — e.g., `"v4.0.0"`  
- `created` — ISO 8601 timestamp  
- `source` — list of contributing agencies  
- `checksum` — `sha256-…` string  
- `fairstatus` — `"certified"`, `"pending"`, or `"restricted"`  
- `governance_ref` — path to governance ledger entry  

### 5.2 🌪 Tornado Tracks Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
tornado_id       string      Unique event ID (SPC/NCEI)
start_time       datetime    Event start (ISO 8601)
end_time         datetime    Event end (ISO 8601)
geometry         GeoJSON     LineString / MultiLineString path
ef_scale         integer     0–5
wind_speed_mph   float       Peak wind estimate
fatalities       integer     CARE-sensitive
injuries         integer     CARE-sensitive
counties         array       GNIS IDs of intersected counties
source           string      NOAA SPC / NCEI
checksum         string      sha256-…
~~~~

### 5.3 🌊 Flood Risk Zones Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
flood_id         string      NFHL polygon ID
zone             string      Flood zone code (A, AE, AO, VE, X, etc.)
risk_class       string      High / Moderate / Low
geometry         GeoJSON     Polygon
source           string      FEMA NFHL / USGS
updated_at       datetime    ISO 8601
checksum         string      sha256-…
~~~~

### 5.4 🔥 Wildfire Events Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
fire_id          string      Unique fire identifier
start_time       datetime    ignition time
end_time         datetime    contained time
area_ha          float       burned area in hectares
cause            string      lightning, human, unknown
geometry         GeoJSON     Polygon
source           string      USGS / state agency
checksum         string      sha256-…
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
checksum         string      sha256-…
~~~~

---

## 6. 💠 Hazard Intensity Index (HII v4.0)

The **Hazard Intensity Index (HII)** provides a unified severity metric per spatial unit.

~~~~text
HII = (w1 * tornado_severity)
    + (w2 * flood_risk)
    + (w3 * drought_severity)
    + (w4 * wildfire_severity)

Where:
- w1, w2, w3, w4 are domain-specific weights (0–1)
- tornado_severity, flood_risk, drought_severity, wildfire_severity are normalized 0–10
~~~~

Outputs stored in the file:

`hazard_intensity_index_v11.0.0.csv`

HII is used for:

- Focus Mode ranking & highlighting  
- Regional risk comparison  
- Scenario modeling inputs  

---

## 7. 🧍 Exposure & Vulnerability Modeling

Exposure datasets quantify:

- Population (total, age groups, vulnerable groups)  
- Buildings & critical infrastructure  
- Economic value (property, agriculture, infrastructure)  
- Social vulnerability indicators (e.g., SVI-like scores)  

Spatial units:

- Census tracts & block groups  
- H3 hex cells  
- Custom administrative regions  

Outputs typically live in:

- `exposure_pop_tract_v11.0.0.parquet`  
- Additional exposure layers under `data/processed/hazards/`  

---

## 8. ⚖️ FAIR+CARE Governance — Hazards Domain

Given the sensitive nature of hazard impacts on communities, the hazards domain applies **strong governance**:

- **CARE Principles**  
  - Consider impacts on Indigenous and marginalized communities  
  - Document community benefit and potential risks  
  - Provide contextual information about limitations and biases  

- **Sovereignty Controls**  
  - Tribal lands and culturally sensitive sites are masked or aggregated via H3  
  - Any disaggregated data for Indigenous communities require explicit approval  

Governance artifacts:

~~~~text
data/processed/hazards/metadata/faircare_certification.json
docs/reports/audit/data_provenance_ledger.json
docs/standards/faircare/HAZARDS-GUIDE.md
~~~~

---

## 9. 🔐 Integrity & Lineage

Integrity is maintained via:

- **Checksums**  
  - All files in `data/processed/hazards/` have SHA-256 checksums in:  
    - `data/checksums/manifest.json`  
    - `data/archive/2025Q4/checksums/hazards_checksums.json`

- **Lineage (PROV-O)**  
  - Each hazard dataset is a `prov:Entity` with:  
    - `prov:wasDerivedFrom` → raw and staged datasets  
    - `prov:used` → ETL scripts, model configurations  
    - `prov:wasGeneratedBy` → ETL/AI runs  

Lineage exports:

~~~~text
data/processed/hazards/metadata/provenance.json
docs/reports/audit/data_provenance_ledger.json
~~~~

---

## 10. 🌱 Telemetry & Sustainability

For each hazards ETL/validation run:

- Metrics collected:
  - `energy_wh`  
  - `carbon_gCO2e`  
  - `runtime_sec`  
  - `records_processed`  
  - `validation_failures`  

Telemetry aggregated into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-hazards-processed-v11.json
~~~~

These metrics support:

- Carbon accounting and optimization  
- Governance dashboards  
- Performance tuning and risk assessment  

---

## 11. 🌐 STAC/DCAT & Focus Mode Integration

Hazards datasets are exposed via:

- **STAC**  
  - Collection: `data/processed/hazards/stac_collection.json`  
  - Items: one per dataset or per spatiotemporal slice  

- **DCAT**  
  - Hazards datasets defined in `data/dcat/*.jsonld`  
  - Includes `dct:temporal`, `dct:spatial`, `dct:license`, and provenance links  

- **Focus Mode**  
  - Uses hazards layers for map overlays, timelines, and narrative context  
  - Requires high-quality metadata and geometry for explanations  

---

## 12. 🧾 Internal Reference & Citation

~~~~text
Kansas Frontier Matrix (2025). Processed Hazards Data (v11.0.0).
Multi-hazard, FAIR+CARE-certified, checksum-verified datasets for hazard
assessment and public resilience planning. Aligned to STAC 1.x, DCAT 3.0,
ISO 19115, and KFM-OP v11 with full provenance and sustainability metrics.
~~~~

---

## 13. 🕰️ Version History

| Version | Date       | Summary                                                                                   |
|--------:|------------|-------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 domain architecture; added schema tables, governance & sustainability sections. |
| v10.2.2 | 2025-11-12 | Streaming STAC, Focus v2.1 integration, telemetry v2, governance path updates.           |
| v10.0.0 | 2025-11-09 | Initial processed hazards README & directory structure.                                   |

<div align="center">

**Kansas Frontier Matrix — Hazards Domain**  
⚠️ FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Processed Layer](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>