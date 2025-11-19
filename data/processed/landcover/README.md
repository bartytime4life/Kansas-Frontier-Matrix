---
title: "🌿 Kansas Frontier Matrix — Processed Landcover Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/landcover/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-landcover-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-landcover-readme"
event_source_id: "ledger:data/processed/landcover/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-landcover-processed-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
landcover_contract_version: "landcover-schema-v4.0.0"

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
intent: "processed-landcover-datasets"
role: "landcover-domain"
category: "Data · Landcover · FAIR+CARE · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Low–Moderate (ecological sensitivity varies)"
sensitivity_level: "Low–Moderate"
indigenous_rights_flag: "Dataset-dependent"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-landcover-processed-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-landcover-processed-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative"
  - "unverified claims"

machine_extractable: true
classification: "Public Data / Low Sensitivity"
jurisdiction: "Kansas / United States"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next landcover-domain update"
accessibility_compliance: "WCAG 2.1 AA"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Processed Landcover Data**  
`data/processed/landcover/README.md`

Authoritative FAIR+CARE-certified landcover datasets for:

- 🌱 Vegetation + canopy analysis  
- 🛰 NDVI/soil moisture remote sensing  
- 🌍 Land-use & land-cover change (LUCC)  
- 🧭 Focus Mode v3 ecological narratives  
- 📡 Global STAC/DCAT catalog discovery  

All datasets are **checksum-verified, lineage-linked, and metadata-complete**.

</div>

---

# 1. 📘 Overview

The **Processed Landcover Layer** contains fully validated datasets derived from:

- **USGS NLCD** (landcover classification epochs)  
- **NASA MODIS/VIIRS** (NDVI composites / seasonal metrics)  
- **ESA Copernicus CCI/CLC** (soil moisture, landcover)  
- **Kansas DASC** (state surface/terrain products)  

Datasets here:

- ✔ match **Landcover Schema v4.0.0**  
- ✔ include STAC/DCAT and ISO 19115 metadata  
- ✔ are FAIR+CARE-audited with ecological-site masking  
- ✔ include full PROV-O lineage bundles  

---

# 2. 🗂️ Directory Layout (GitHub Safe)

~~~~text
data/processed/landcover/
├── README.md
│
├── landcover_classifications_v11.0.0.parquet
├── vegetation_index_ndvi_2025_v11.0.0.csv
├── soil_moisture_surface_2025_v11.0.0.csv
├── canopy_cover_trends_2000_2025_v11.0.0.csv
├── landuse_change_matrix_2001_2021_v11.0.0.csv
│
├── stac_collection.json
└── metadata/
    ├── checksums.json
    ├── faircare_certification.json
    ├── provenance.json
    └── schema_validation.json
~~~~

---

# 3. 🔄 Landcover Processing Lifecycle

~~~~mermaid
flowchart TD
  A["raw/landcover/*"] --> B["staging/\nresampling · CRS fix · harmonization"]
  B --> C["validation/\nschema · FAIR+CARE · QC"]
  C --> D["processing/\nclassification · indices · change metrics"]
  D --> E["checksums/\nSHA-256 + SBOM parity"]
  E --> F["publication/\ndata/processed/landcover/*"]
  F --> G["catalog-sync/\nSTAC · DCAT · Streaming STAC"]
~~~~

---

# 4. 🌱 Landcover Domain Schema Requirements

## 4.1 Common Fields

~~~~text
kfm_id             string     stable ID  
domain             string     always "landcover"  
schema_version     string     e.g., "v4.0.0"  
created            datetime   ISO 8601  
source             string     NLCD / MODIS / CCI / DASC  
checksum           string     sha256-...  
fairstatus         string     certified/pending  
governance_ref     string     ledger path  
~~~~

---

# 5. 🌳 Domain-Specific Schema Tables

## 5.1 Landcover Classifications

~~~~text
Field                 Type        Notes
--------------------- ----------- ---------------------------------------
pixel_id              string      unique raster tile or pixel identifier
class_id              integer     NLCD/CLC classification code
class_name            string      human-readable class
geometry              GeoJSON     polygon footprint (optional)
source                string      NLCD / CLC / DASC
epoch_year            integer     classification year
checksum              string      sha256-...
~~~~

## 5.2 NDVI Index (Annual)

~~~~text
Field                 Type        Notes
--------------------- ----------- ---------------------------------------
pixel_or_unit_id      string      raster grid or H3 cell
ndvi_mean             float       annual mean NDVI
ndvi_min              float       annual minimum
ndvi_max              float       annual maximum
timestamp             datetime    ISO 8601
source                string      MODIS / VIIRS
checksum              string      sha256-...
~~~~

## 5.3 Soil Moisture (Surface)

~~~~text
Field                 Type        Notes
--------------------- ----------- ---------------------------------------
unit_id               string      grid cell or polygon ID
soil_moisture_value   float       volumetric surface moisture
timestamp             datetime    ISO 8601
source                string      ESA CCI
checksum              string      sha256-...
~~~~

## 5.4 Canopy Cover Trends

~~~~text
Field                 Type        Notes
--------------------- ----------- ---------------------------------------
unit_id               string      county or H3 index
canopy_pct            float       canopy cover percent
trend_category        string      rising/stable/declining
start_year            integer     trend start
end_year              integer     trend end
checksum              string      sha256-...
~~~~

## 5.5 Land-Use Change Matrix (LUCC)

~~~~text
Field                 Type        Notes
--------------------- ----------- ---------------------------------------
from_class_id         integer     original class
to_class_id           integer     new class
transition_count      integer     number of pixels transitioning
epoch_pair            string      "2001-2011", "2011-2021", etc.
source                string      NLCD crosswalk
checksum              string      sha256-...
~~~~

---

# 6. ⚖️ FAIR+CARE Governance — Landcover Domain

### Governance Principles:
- Sensitive ecological habitats may be generalized  
- Tribal lands overlay must respect sovereignty policy  
- Ecological survey points may require H3 masking  
- All outputs must include CARE metadata for environmental stewardship  

Governance artifacts:

~~~~text
data/processed/landcover/metadata/faircare_certification.json
docs/reports/audit/data_provenance_ledger.json
~~~~

---

# 7. 🔐 Integrity & Lineage

All files must appear in:

~~~~text
data/checksums/manifest.json
data/archive/2025Q4/checksums/landcover_checksums.json
~~~~

Lineage stored in:

~~~~text
data/processed/landcover/metadata/provenance.json
~~~~

Each dataset includes:

- `prov:wasDerivedFrom`  
- `prov:wasGeneratedBy`  
- `prov:used`  

---

# 8. ♻️ Telemetry & Sustainability

Tracked:

- `energy_wh`  
- `carbon_gCO2e`  
- `validation_failures`  
- `runtime_sec`  
- `records_processed`  

Recorded to:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-landcover-processed-v11.json
~~~~

---

# 9. 🌐 STAC/DCAT Integration

Each dataset is represented as:

- a **STAC Item**  
- an entry in the **landcover STAC Collection**  
- a **DCAT Dataset** with spatial/temporal/lineage metadata  

---

# 10. 🧾 Internal Citation

~~~~text
Kansas Frontier Matrix (2025). Processed Landcover Data (v11.0.0).
FAIR+CARE-certified, checksum-verified landcover datasets integrating NLCD,
MODIS/VIIRS, Copernicus, and DASC sources, aligned to STAC/DCAT 3.0 and
KFM-OP v11 with complete provenance and sustainability metrics.
~~~~

---

# 11. 🕰 Version History

| Version | Date       | Summary                                                                                   |
|--------:|------------|-------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 rewrite: schema tables, FAIR+CARE v11, STAC/DCAT v11, lineage v11, telemetry v4. |
| v10.2.2 | 2025-11-12 | Streaming STAC, Focus v2.1 integration, telemetry v2, governance improvements.            |
| v10.0.0 | 2025-11-09 | Initial landcover processed layer specification.                                          |

<div align="center">

**Kansas Frontier Matrix — Landcover Domain**  
🌿 FAIR+CARE Certified · 🛰 STAC/DCAT Ready · ♻️ Sustainability Validated · 🧭 Focus Mode Enabled  

[⬅️ Back to Processed Layer](../README.md) ·  
[📐 Data Architecture](../../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>