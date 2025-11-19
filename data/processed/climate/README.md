---
title: "📦 Kansas Frontier Matrix — Q4 2025 Data Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/2025Q4/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_cycle: "2025Q4"
release_stage: "Stable / Governed"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-archive-2025Q4-v11.0.0"
semantic_document_id: "kfm-doc-data-archive-2025Q4"
event_source_id: "ledger:data/archive/2025Q4/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
release_registry_ref: "../../../releases/v11.0.0/release-registry.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-archive-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Archive"
intent: "quarterly-archive"
role: "immutable-release"
category: "Data · Archive · Provenance · Release"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed — Dataset-Dependent"
sensitivity_level: "Variable"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Domain-dependent"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Controlled"
redaction_required: false

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-archive-2025Q4-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-archive-2025Q4-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
jurisdiction: "Kansas / United States"
classification: "Public Data / Mixed Sensitivity"
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent (archival)"
sunset_policy: "Never expires — append-only"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Q4 2025 Data Archive**  
`data/archive/2025Q4/README.md`

**Purpose**  
This directory contains the **FAIR+CARE-certified, checksum-verified, governance-approved** data preserved for the **Q4 2025 release** of the Kansas Frontier Matrix.

These datasets:

- Passed **all lifecycle validation steps** (schema, checksum, FAIR+CARE, sustainability, explainability).
- Are considered **historically immutable** and preserved under **ISO 16363 trusted repository** rules.
- Are indexed into **STAC/DCAT catalogs**, **Streaming-STAC**, and the **Release Registry**.
- Are permanently recorded in the **Governance Ledger** and **Provenance Chain**.

</div>

---

# 1. 📘 Archive Overview

The **Q4 2025 Archive** contains finalized datasets for the KFM v11 release cycle.  

Each dataset here:

- Has a **frozen checksum** recorded in `checksums/`
- Has a **FAIR+CARE certification record**
- Is linked to **STAC Items/Collections** and **DCAT Datasets**
- Has **PROV-O lineage** to its raw and staged versions  
- Is immutable and part of the **permanent scientific record** of KFM  

Archive contents span:

- Hazards  
- Climate  
- Hydrology  
- Landcover  
- Ecology  
- Tabular (Historical/Census/Treaty)  

---

# 2. 🗂️ Directory Layout (GitHub Safe)

~~~~text
data/archive/2025Q4/
├── README.md                         ← this file
│
├── hazards_v11.0.0/                  ← Tornado, flood, wildfire composites
├── climate_v11.0.0/                  ← Temperature/precip indices & anomalies
├── hydrology_v11.0.0/                ← Streamflow & water-level summaries
├── landcover_v11.0.0/                ← NDVI, LCMS, vegetation products
├── ecology_v11.0.0/                  ← Biodiversity aggregates (GBIF/eBird)
│
├── metadata/                         ← FAIR+CARE certification + governance docs
│   ├── faircare_certification.json
│   ├── schema_validation.json
│   ├── provenance_chain.json
│   └── masking_policies.json
│
├── checksums/                        ← SHA-256 signed manifests
│   ├── manifest_verified_2025Q4.json
│   ├── hazards_checksums.json
│   ├── climate_checksums.json
│   └── hydrology_checksums.json
│
└── provenance.json                   ← Archive-wide provenance summary
~~~~

---

# 3. 🔄 Archive Lifecycle Architecture

~~~~mermaid
flowchart TD
    A["processed/\n(certified outputs)"]
      --> B["governance review\n(FAIR+CARE + sovereignty)"]

    B --> C["checksums\n(SHA-256 + SBOM parity)"]

    C --> D["archive registration\n(write to data/archive/2025Q4)"]

    D --> E["catalog sync\n(STAC/DCAT + Streaming STAC)"]

    E --> F["release registry\n(versioned manifest)"]

    F --> G["Focus Mode · Public Access\n(if allowed)"]
~~~~

### Summary of guarantees:

- No dataset enters the archive without **validated checksums**  
- Archival entries must have STAC/DCAT + JSON-LD metadata  
- Governance ledger must contain a **matching entry**  
- Archive entries cannot be modified (append-only model)  

---

# 4. 🧾 Q4 2025 Dataset Summary Table

| Domain | Dataset | Records | Formats | FAIR+CARE | Integrity | Public? |
|--------|---------|--------:|---------|-----------|-----------|---------|
| Hazards | Tornado/Flood Composite | 34,987 | GeoJSON, Parquet | ✔ Certified | ✔ SHA-256 | Yes |
| Climate | Temp/Precip Indices | 124,560 | CSV, Parquet | ✔ Certified | ✔ SHA-256 | Yes |
| Hydrology | Streamflow/Aquifer | 48,271 | CSV, GeoJSON | ✔ Certified | ✔ SHA-256 | Yes |
| Landcover | NDVI/LCMS | 90,412 | COG, JSON | ✔ Certified | ✔ SHA-256 | Yes |
| Ecology | GBIF/eBird Aggregates | 18,450 | Parquet, GeoJSON | ✔ Certified | ✔ SHA-256 | Mixed |
| Tabular | Census/History/Treaty | 51,992 | Parquet | ✔ Certified | ✔ SHA-256 | Yes |

---

# 5. 🧠 FAIR+CARE Governance Overview (Q4 2025)

All archived datasets have:

- Completed the **FAIR+CARE Ethics Review**
- Passed cultural sensitivity checks  
- Complied with sovereignty masking rules  
- Received approval for dataset-level exposure  

Governance artifacts stored in:

~~~~text
data/archive/2025Q4/metadata/faircare_certification.json
docs/reports/audit/data_provenance_ledger.json
~~~~

Governance obligations:

- Indigenous datasets require CARE metadata  
- Sensitive geometries → H3 generalization  
- Sensitive records → field-level masking or redaction  

---

# 6. 🔐 Provenance Schema (Archive-Level)

~~~~json
{
  "archive_cycle": "2025Q4",
  "kfm_version": "v11.0.0",
  "datasets": [
    {
      "id": "hazards_v11.0.0",
      "derived_from": ["data/processed/hazards/hazards_composite_v11.0.0.geojson"],
      "checksum_verified": true,
      "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
    }
  ],
  "archived_by": "@kfm-data",
  "timestamp": "2025-11-19T19:40:00Z"
}
~~~~

---

# 7. 📐 Domain-Level Archive Requirements

## 7.1 Hazards

~~~~text
Requirement                Detail
-------------------------  ----------------------------------------------
Geometry                  GeoJSON (RFC 7946), Parquet (WKB), or COG raster
Temporal                  ISO 8601 start/end
Attributes                hazard_type, intensity, source_agency
Governance                CARE required for tribal lands impacts
Checksum                  sha256-…
~~~~

## 7.2 Climate

~~~~text
Requirement                Detail
-------------------------  ----------------------------------------------
Variables                 tmax, tmin, precip, drought_index
Temporal                  Daily/monthly with ISO timestamps
Projections               Supported (CMIP-like or LOCA-like)
Governance                Standard FAIR+CARE validation
~~~~

## 7.3 Hydrology

~~~~text
Requirement                Detail
-------------------------  ----------------------------------------------
Metrics                   discharge_cfs, level_m, quality indicators
Sources                   USGS NWIS, KDHE, EPA WQP
Geometry                  Point geometries; CRS: EPSG:4326
~~~~

## 7.4 Landcover

~~~~text
Requirement                Detail
-------------------------  ----------------------------------------------
Formats                   COG rasters
Classification            NLCD, LCMS, or custom vegetation classes
Change Detection          Must provide year-to-year metadata
~~~~

---

# 8. 🧮 Integrity & Checksum Verification

Checksum manifests stored in:

~~~~text
data/archive/2025Q4/checksums/*
~~~~

Rules:

- Use `sha256-` prefix  
- All archived files must have entries  
- SBOM must match all checksums (SBOM parity)  
- Governance ledger stores all checksum validation events  

---

# 9. 🌱 Sustainability Metrics (v11)

Telemetry metrics recorded at archival time:

- `energy_wh` — energy spent validating the dataset  
- `carbon_gco2e` — carbon-estimate  
- `storage_mb` — storage footprint  
- `validation_runtime_sec`  

Recorded into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-archive-2025Q4.json
~~~~

---

# 10. 📡 STAC / DCAT / Streaming-STAC Integration

Each domain folder contains:

- STAC Item  
- STAC Collection (if applicable)  
- DCAT Dataset  
- JSON-LD context  
- Telemetry + provenance references  

Streaming-STAC feeds automatically update when:

- Assets are replaced (rare; archival updates create new entries)  
- Metadata fields change outside the data asset  
- New link relations are added  

---

# 11. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Q4 2025 Data Archive (v11.0.0).
Immutable FAIR+CARE-certified archive for hazards, climate, hydrology,
landcover, and ecology datasets produced during the Q4 2025 KFM lifecycle.
Integrates STAC/DCAT metadata, PROV-O lineage, checksum verification,
and sustainability telemetry under KFM-MDP v11 architecture.
~~~~

---

# 12. 🕰️ Version History

| Version | Date       | Author         | Summary                                                                 |
|--------:|------------|----------------|-------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | @kfm-archive   | Full v11 rebuild; added domain schemas, sustainability v4, STAC/DCAT integration. |
| v10.2.2 | 2025-11-12 | @kfm-archive   | Previous archive spec; checksum + governance integration.               |
| v10.0.0 | 2025-11-09 | @kfm-archive   | Initial archive record structure.                                      |

<div align="center">

**Kansas Frontier Matrix — Q4 2025 Immutable Archive**  
FAIR+CARE Certified · Cultural Sovereignty Aware · Sustainability Validated  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

© 2025 Kansas Frontier Matrix — CC-BY 4.0

[Back to Archive Index](../README.md) ·  
[Data Architecture](../../ARCHITECTURE.md) ·  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
