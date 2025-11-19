---
title: "🧾 Kansas Frontier Matrix — Processed Data Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-readme-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-readme"
event_source_id: "ledger:data/processed/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-processed-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / Open Data Commons Attribution License"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "data-processed-layer-architecture"
role: "publication-ready-datasets"
category: "Data · Processed · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (Dataset-dependent variations)"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/data-processed-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/data-processed-readme-v11-shape.ttl"

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
classification: "Varies by dataset"
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next processed-layer update"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — Processed Data Layer  
`data/processed/README.md`

The **Processed Data Layer** is the canonical, publication-ready dataset repository of the Kansas Frontier Matrix (KFM).  
All contents here have passed:

- ✔ FAIR+CARE governance  
- ✔ Schema validation (Data Contract v3, STAC/DCAT, JSON Schema, SHACL)  
- ✔ Checksum verification (SHA-256; SBOM parity)  
- ✔ Spatial & temporal normalization  
- ✔ Provenance & lineage registration (PROV-O, governance ledger)  
- ✔ AI explainability/fairness review (where applicable)  

These datasets support:

- Focus Mode v3  
- Story Node v3  
- STAC/DCAT catalogs  
- Neo4j graph ingestion  
- Scientific, educational, and ethical open-data use  

</div>

---

# 1. 📘 Overview

The Processed Data Layer contains **clean, normalized, validated, and certified datasets** that represent the final step before public release and graph ingestion.

Its responsibilities:

- Guarantee **reproducibility**  
- Enforce **FAIR+CARE governance**  
- Provide **STAC/DCAT-aligned metadata**  
- Preserve **lineage and integrity**  
- Deliver **machine-ready data** for pipelines, apps, and visualization  

---

# 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/processed/
├── README.md                      ← this file
│
├── climate/                       ← climate indices, normals, anomalies, rasters
├── hazards/                       ← tornado tracks, storm events, wildfire perimeters
├── hydrology/                     ← streamflow, groundwater, aquifer, water quality
├── landcover/                     ← vegetation, NLCD classes, LCMS change
├── ecology/                       ← biodiversity aggregates (GBIF/eBird)
├── tabular/                       ← census, socioeconomic, treaty metadata
├── spatial/                       ← geospatial layers (GeoJSON, Parquet, TopoJSON)
└── metadata/                      ← FAIR+CARE-certified metadata bundles (JSON/JSON-LD)
~~~~

Each subdirectory requires:

- `README.md` with domain-specific schema + examples  
- At least one checksum manifest entry  
- STAC/DCAT metadata references  

---

# 3. 🔄 Processed Data Lifecycle

~~~~mermaid
flowchart TD
  A["raw/\n(immutable sources)"]
    --> B["staging/\n(cleaned + standardized)"]

  B --> C["validation/\n(schema · FAIR+CARE · quality · AI checks)"]

  C --> D["alignment/\n(STAC · DCAT · ISO 19115 · CRS/temporal)"]

  D --> E["checksums/\nSHA-256 lineage + SBOM verification"]

  E --> F["publication/\n(data/processed/*)"]

  F --> G["catalog-sync/\n(STAC/DCAT + Focus Mode v3)"]
~~~~

### Lifecycle Guarantees

- No dataset enters `processed/` without verified integrity  
- All processed datasets produce lineage edges for the Neo4j graph  
- Telemetry records energy, carbon, and validation durations  

---

# 4. 📐 Cross-Domain Architecture Standards

All processed datasets must follow:

### 4.1 Spatial Standards
- CRS: **EPSG:4326**  
- Optional internal CRS used during ETL, but final outputs must convert to WGS84  
- GeoJSON → must use RFC 7946  
- Parquet → geometry stored as WKB/WKT/Arrow Extension type  
- Raster → must be **COG** with proper overviews  

### 4.2 Temporal Standards
- Use ISO 8601 timestamps  
- `start_time`, `end_time`, `temporal_accuracy` fields recommended  
- Temporal intervals mapped to OWL-Time intervals in the graph  

### 4.3 Provenance Requirements
- PROV-O fields:  
  - `prov:wasDerivedFrom`  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
- Link to:  
  - checksums  
  - governance decisions  
  - original STAC/DCAT entries  

### 4.4 FAIR+CARE Rules
- All sensitive data must have CARE tags  
- Indigenous datasets must include sovereignty metadata  
- Public exposure must match governance decisions  

---

# 5. 🧩 Schema & Metadata Requirements

All processed datasets must include:

### Required fields:
- `id`  
- `kfm_id`  
- `domain`  
- `schema_version`  
- `license`  
- `checksum`  
- `fairstatus`  
- `created`  

### Required metadata references:
- `stac_ref`  
- `dcat_ref`  
- `governance_ref`  
- `data_contract_ref`  

---

# 6. 🧬 Domain-Level Schema Tables (v11)

Below are **schema summaries** for each processed domain.  
Full schemas live in `schemas/processed/**`.

---

## 6.1 🌦 Climate Domain Schema

~~~~text
Field                Type          Notes
-------------------  ------------  ----------------------------------------
kfm_id               string        Stable ID
timestamp            datetime      ISO 8601
variable             string        e.g., tmax, tmin, precip, drought_index
value                float         Normalized units
unit                 string        SI-standardized
spatial_extent       array         [minLon, minLat, maxLon, maxLat]
source               string        NOAA, PRISM, Daymet, USDM
quality_flag         string        QC metadata
checksum             string        sha256-…
fairstatus           string        certified/pending
~~~~

---

## 6.2 🌪 Hazards Domain Schema

~~~~text
Field                Type          Notes
-------------------  ------------  ----------------------------------------
hazard_id            string        Unique event ID
hazard_type          string        tornado, hail, flood, wildfire, etc.
start_time           datetime      ISO 8601
end_time             datetime      ISO 8601
geometry             GeoJSON       Polygon/LineString/Point
intensity            string/float  Domain-specific metric (EF-scale, magnitude)
source               string        NOAA SPC, USGS, FEMA
area_sqkm            float         Computed area for polygons
stac_ref             string        STAC item link
checksum             string        sha256-…
~~~~

---

## 6.3 💧 Hydrology Domain Schema

~~~~text
Field                Type          Notes
-------------------  ------------  ----------------------------------------
site_id              string        USGS NWIS site
timestamp            datetime      ISO 8601
discharge_cfs        float         Streamflow
water_level_m        float         Depth/height
water_quality        float/object  WQP or KDHE parameters
geometry             GeoJSON       Point
source               string        USGS, EPA, KDHE, KGS
checksum             string        sha256-…
~~~~

---

## 6.4 🌱 Landcover Domain Schema

~~~~text
Field                Type          Notes
-------------------  ------------  ----------------------------------------
pixel_id             string        Unique raster or tile ID
landcover_class      integer       NLCD/LCMS class values
class_name           string        Human-readable class
geometry             GeoJSON       Polygon or pixel footprint
acquisition_date     date          Data year (e.g., 2016)
raster_ref           string        Link to COG raster
checksum             string        sha256-…
~~~~

---

## 6.5 🐦 Ecology Domain Schema

~~~~text
Field                Type          Notes
-------------------  ------------  ----------------------------------------
species              string        Latin species name
count                integer       Observations
geometry             GeoJSON       Point or aggregated H3 cell
observation_time     datetime      ISO 8601
uncertainty_m        float         Spatial uncertainty
source               string        GBIF, eBird, VEGMAP
checksum             string        sha256-…
~~~~

---

## 6.6 📊 Tabular Domain Schema

~~~~text
Field                Type          Notes
-------------------  ------------  ----------------------------------------
kfm_id               string        Stable ID
name                 string        Entity name
value                any           Numeric or categorical
date                 date          Standardized
category             string        Census, economic, treaty metadata
source               string        Census bureau, NARA, etc.
checksum             string        sha256-…
~~~~

---

# 7. ⚙️ Integrity Architecture

Processed datasets must undergo **checksum, schema, and governance validation**.

### Required validation steps:

- `checksum_audit.py` → SHA-256 verification  
- `schema_check.py` → STAC/DCAT + Data Contract v3 schema validation  
- `faircare_validator.py` → CARE, sovereignty, licensing, ethics  
- `ai_explainability_audit.py` (if dataset uses ML)  

Validation outputs stored in:

~~~~text
data/reports/self-validation/**
data/reports/audit/**
~~~~

---

# 8. 🔐 Provenance Architecture (PROV-O)

Each dataset in `processed/` must have:

- A `prov:Entity` representation  
- Incoming edges:
  - `prov:wasDerivedFrom` (source datasets)  
  - `prov:used` (tools, configs)  
- Outgoing edges:
  - `prov:wasGeneratedBy` (ETL task or AI model)

Stored in:

- JSON-LD metadata in `metadata/`  
- Graph layer (Neo4j ingestion pipeline)  

---

# 9. 🌱 Sustainability Architecture

Telemetry fields:

- `energy_wh`  
- `carbon_gco2e`  
- `runtime_sec`  
- `validation_failures`  
- `data_volume_mb`  

Recorded into:

~~~~text
../../releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-processed-*.json
~~~~

Dataset-level sustainability summaries included in STAC/DCAT where applicable.

---

# 10. 🧾 Example STAC/DCAT Linkage

~~~~json
{
  "stac_ref": "data/stac/items/hazards_v11_2025Q4.json",
  "dcat_ref": "data/dcat/hazards_v11_2025Q4.jsonld",
  "provenance": {
    "prov:wasDerivedFrom": ["data/staging/hazards/hazards_aggregate.parquet"],
    "prov:wasGeneratedBy": "etl_hazards_pipeline_v11.0.0"
  }
}
~~~~

---

# 11. 🧠 Focus Mode Integration

Processed datasets are the **primary source** for:

- Story Node v3 inputs  
- Map layers in Focus Mode  
- Temporal-scoped visualizations  
- Multi-domain contextual overlays  
- Predictive narratives (AI-assisted)  

Focus Mode requires:

- Clean geometry  
- Unit consistency  
- Thorough metadata  
- Temporal precision  

---

# 12. 🕰️ Version History

| Version | Date       | Summary                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 rewrite; added domain schema tables, ontology mapping, STAC/DCAT upgrades, telemetry. |
| v10.2.2 | 2025-11-12 | Streaming STAC sync, telemetry v2 updates, governance path fixes.                               |
| v10.0.0 | 2025-11-09 | Initial processed-layer structure; sustainability v2 equipped.                                  |

<div align="center">

**Kansas Frontier Matrix — Processed Data Layer**  
*FAIR+CARE Certified · Provenance Aligned · Open-Science Compliant*  

© 2025 Kansas Frontier Matrix — CC-BY 4.0 / ODC Attribution License  

[Back to Data Architecture](../ARCHITECTURE.md) ·  
[Back to Data Directory](../README.md) ·  
[Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
