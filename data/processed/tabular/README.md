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

Authoritative repository of **FAIR+CARE-certified multi-hazard datasets** harmonized from:

- FEMA  
- NOAA (NCEI/SPC)  
- USGS  
- KDHE  
- Other allied state and federal sources  

This layer provides validated, reproducible, and ethically governed datasets for:

- 🌍 Open use and public risk communication  
- 🧪 Risk modeling and scenario analysis  
- 🧠 Focus Mode v3 hazard intelligence and narratives  
- 🌐 STAC/DCAT discovery and graph integration  

All layers are **checksum-verified**, **schema-aligned**, and **governance-certified**.

</div>

---

## 1. 📘 Overview

The **Processed Hazards Layer** contains final, schema-validated, FAIR+CARE-certified datasets representing:

- Hazard events (tornadoes, hail, wind, winter storms)  
- Flood hazards (FEMA NFHL-derived and USGS-supported)  
- Drought severity indices  
- Wildfire events and perimeters  
- Multi-hazard composites and hazard intensity indices  
- Exposure and vulnerability layers for people and infrastructure  

All layers:

- Are normalized to **EPSG:4326**  
- Carry **ISO 19115** metadata and **PROV-O** lineage  
- Are registered as **STAC 1.x Items/Collections** and **DCAT 3.0 Datasets**  
- Feed **Focus Mode v3** overlays and Story Nodes  

---

## 2. 🗂️ Directory Layout

~~~~text
data/processed/hazards/
├── README.md                              ← this file
│
├── hazards_composite_v11.0.0.geojson      ← multi-hazard integrated dataset
├── hazard_intensity_index_v11.0.0.csv     ← composite severity index per unit
├── hazard_event_frequency_v11.0.0.csv     ← historical frequency & recurrence
├── flood_risk_zones_v11.0.0.geojson       ← FEMA/USGS flood hazard polygons
├── tornado_tracks_1950_2025_v11.0.0.geojson ← historical tornado tracks
├── wildfire_history_v11.0.0.geojson       ← historical wildfire perimeters
├── drought_severity_index_v11.0.0.parquet ← drought index (H3 or grid-based)
├── exposure_pop_tract_v11.0.0.parquet     ← population exposure by census tract
│
├── stac_collection.json                   ← hazards STAC Collection (v11)
└── metadata/
    ├── checksums.json                     ← SHA-256 checksums
    ├── faircare_certification.json        ← FAIR+CARE review outcomes
    ├── provenance.json                    ← PROV-O lineage exports
    └── schema_validation.json             ← schema validation summary
~~~~

---

## 3. 🔄 Hazards Data Lifecycle

~~~~mermaid
flowchart TD
  A["raw/hazards/*"] --> B["staging/hazards/*\ncleaning · dedupe · CRS fixes"]
  B --> C["validation\nschema · FAIR+CARE · quality"]
  C --> D["processing\nper-hazard enrichment & derivation"]
  D --> E["integration\nmulti-hazard composites & indices"]
  E --> F["checksums & lineage\nSHA-256 · PROV-O · manifest"]
  F --> G["publication\ndata/processed/hazards/*"]
  G --> H["catalog sync\nSTAC/DCAT · Streaming STAC · Focus Mode v3"]
~~~~

Entry condition for `data/processed/hazards/`:

- ✅ Schema validation passed  
- ✅ FAIR+CARE certification complete  
- ✅ Checksums match manifests and SBOM  
- ✅ Governance ledger updated  

---

## 4. 📊 Core Hazards Datasets (v11)

| Dataset File                           | Description                                          | Example Use Cases                           |
|----------------------------------------|------------------------------------------------------|---------------------------------------------|
| `hazards_composite_v11.0.0.geojson`    | Multi-hazard surface (all perils)                    | Statewide risk dashboards, Focus Mode maps  |
| `hazard_intensity_index_v11.0.0.csv`   | Composite hazard severity per spatial unit           | Ranking & prioritization                     |
| `hazard_event_frequency_v11.0.0.csv`   | Annual counts & recurrence metrics by hazard type    | Trend & recurrence analysis                  |
| `flood_risk_zones_v11.0.0.geojson`     | Flood hazard polygons (NFHL + derived)               | Floodplain management                        |
| `tornado_tracks_1950_2025_v11.0.0.geojson` | Tornado paths and attributes (historic)          | Historical narratives & model calibration   |
| `wildfire_history_v11.0.0.geojson`     | Wildfire perimeters and severity                     | Fire risk analysis                           |
| `drought_severity_index_v11.0.0.parquet` | Drought index per H3/grid & time                  | Drought monitoring                           |
| `exposure_pop_tract_v11.0.0.parquet`   | Exposure/vulnerability measures per tract            | Social vulnerability & planning              |

---

## 5. 🧱 Hazards Schema Requirements (v11)

All hazards datasets must conform to **hazards-schema-v4.0.0** under `schemas/processed/hazards/`.

### 5.1 Common Schema Fields

~~~~text
kfm_id              string    stable KFM ID
domain              string    always "hazards"
schema_version      string    e.g. "v4.0.0"
created             datetime  ISO 8601
source              string    primary upstream agency/agency code
checksum            string    sha256-...
fairstatus          string    certified / pending / restricted
governance_ref      string    path in governance ledger
~~~~

### 5.2 Tornado Tracks Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
tornado_id       string      SPC/NCEI event ID
start_time       datetime    ISO 8601
end_time         datetime    ISO 8601
geometry         GeoJSON     LineString / MultiLineString
ef_scale         integer     EF-scale 0–5
wind_speed_mph   float       peak wind estimate
fatalities       integer     CARE-sensitive
injuries         integer     CARE-sensitive
source           string      "NOAA_SPC", "NCEI"
checksum         string      sha256-...
~~~~

### 5.3 Flood Risk Zones Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
flood_id         string      NFHL polygon ID
zone             string      A, AE, AO, VE, X, etc.
risk_class       string      high / moderate / low
geometry         GeoJSON     Polygon / MultiPolygon
source           string      "FEMA_NFHL" or derived
effective_date   date        map effective date
checksum         string      sha256-...
~~~~

### 5.4 Wildfire Events Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
fire_id          string      unique fire identifier
start_time       datetime    ignition time
end_time         datetime    containment time
area_ha          float       burned area (hectares)
cause            string      lightning / human / unknown
geometry         GeoJSON     Polygon
source           string      USGS / state fire agency
checksum         string      sha256-...
~~~~

### 5.5 Drought Severity Schema

~~~~text
Field            Type        Notes
---------------  ----------  -----------------------------------------
cell_id          string      H3 index or grid cell ID
period_start     datetime    ISO 8601
period_end       datetime    ISO 8601
drought_index    float       normalized 0–10
category         string      D0–D4 (U.S. Drought Monitor)
source           string      NIDIS / KDHE
checksum         string      sha256-...
~~~~

---

## 6. 💠 Hazard Intensity Index (HII v4.0)

The **Hazard Intensity Index (HII)** is a composite metric that aggregates hazard components into a single severity score per spatial unit.

ASCII-safe formula:

~~~~text
HII = (w1 * tornado_severity)
    + (w2 * flood_risk)
    + (w3 * drought_severity)
    + (w4 * wildfire_severity)

where:
- w1, w2, w3, w4 are domain-specific weights between 0 and 1
- tornado_severity, flood_risk, drought_severity, wildfire_severity are each normalized 0–10
~~~~

Outputs stored in:

- `hazard_intensity_index_v11.0.0.csv`

Used for:

- Focus Mode v3 ranking and overlays  
- Regional risk comparison  
- Multi-hazard prioritization and scenario analysis  

---

## 7. 🧍 Exposure & Vulnerability Modeling

Exposure layers quantify:

- Population distribution (total, age groups, vulnerable groups)  
- Housing and critical facilities (hospitals, schools, shelters)  
- Economic value exposure (property, agriculture, infrastructure)  
- Social vulnerability metrics (SVI-like measures)  

Typical schema:

~~~~text
Field                Type        Notes
-------------------  ----------  -----------------------------------------
unit_id              string      census tract / block group / H3 index
population_total     integer     persons
population_65_plus   integer     elderly population
population_under_5   integer     children
housing_units        integer     dwellings
critical_facilities  integer     count of facilities
exposure_score       float       normalized 0–10 exposure indicator
checksum             string      sha256-...
~~~~

---

## 8. ⚖️ FAIR+CARE Governance — Hazards Domain

Hazards data is ethically sensitive. Governance rules include:

- CARE-informed handling of fatalities, injuries, and severe impacts  
- Aggregation or masking for vulnerable or sensitive communities  
- H3-based generalization for critical facilities or locations with re-identification risk  
- Additional review for hazard datasets intersecting tribal lands or cultural sites  

Governance outputs:

~~~~text
data/processed/hazards/metadata/faircare_certification.json
docs/reports/audit/data_provenance_ledger.json
docs/standards/faircare/HAZARDS-GUIDE.md
~~~~

---

## 9. 🔐 Integrity & Lineage

Integrity is guaranteed via:

- SHA-256 checksums recorded in:
  - `data/checksums/manifest.json`
  - `data/archive/2025Q4/checksums/hazards_checksums.json`

Lineage is represented via PROV-O:

- `prov:Entity` for each processed dataset  
- `prov:wasDerivedFrom` linking to raw/staging data  
- `prov:wasGeneratedBy` referencing ETL or AI pipeline runs  
- `prov:used` for key transformation configs and models  

Lineage materialization:

~~~~text
data/processed/hazards/metadata/provenance.json
docs/reports/audit/data_provenance_ledger.json
~~~~

---

## 10. 🌱 Telemetry & Sustainability

For each hazards ETL/validation run, telemetry includes:

- `energy_wh` — estimated energy spent  
- `carbon_gCO2e` — carbon-equivalent emissions  
- `runtime_sec` — job duration  
- `records_processed` — count of features/rows  
- `validation_failures` — counts and categories  

Telemetry aggregation:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-hazards-processed-v11.json
~~~~

This supports:

- Sustainability dashboards  
- Performance tuning of hazard pipelines  
- Transparent governance of compute resources  

---

## 11. 🌐 STAC/DCAT & Focus Mode Integration

Hazards datasets are integrated into:

- **STAC**  
  - Collection in `stac_collection.json`  
  - Items per dataset or per spatiotemporal slice  

- **DCAT**  
  - DCAT datasets in `data/dcat/*.jsonld`  
  - Include LIC, provenance, spatial/temporal coverage  

- **Focus Mode v3**  
  - Uses hazards layers for map overlays, timelines, and narrative explanations  
  - Relies on high-quality metadata, stable `kfm_id`, and normalized fields  

---

## 12. 🧾 Internal Citation

~~~~text
Kansas Frontier Matrix (2025). Processed Hazards Data (v11.0.0).
Multi-hazard, FAIR+CARE-certified, checksum-verified hazard datasets for Kansas,
supporting open risk communication, resilience planning, and Focus Mode v3
integration. Aligned with STAC 1.x, DCAT 3.0, ISO 19115, and KFM-OP v11 ontologies.
~~~~

---

## 13. 🕰 Version History

| Version | Date       | Summary                                                                                   |
|--------:|------------|-------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 upgrade; schema tables, FAIR+CARE v11, STAC/DCAT v11, telemetry v4, lineage v11.|
| v10.2.2 | 2025-11-12 | Streaming STAC, Focus v2.1 integration, telemetry v2, governance path updates.           |
| v10.0.0 | 2025-11-09 | Initial processed hazards README & directory structure.                                   |

<div align="center">

**Kansas Frontier Matrix — Hazards Domain**  
⚠️ FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

[⬅️ Back to Processed Layer](../README.md) ·  
[📐 Data Architecture](../../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>