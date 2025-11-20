---
title: "⚠️ Kansas Frontier Matrix — Raw Hazards Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/hazards/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-hazards-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-hazards-readme"
event_source_id: "ledger:data/raw/hazards/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-hazards-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Open Data / Public Domain"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "raw-hazards-data"
role: "raw-hazards-domain"
category: "Data · Raw · Hazards · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed — community-impacted hazards"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"

ontology_alignment:
  cidoc: "E5 Event / E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-raw-hazards-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-raw-hazards-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative"
  - "unverified historical claims"

machine_extractable: true
classification: "Public Data / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next raw-hazards-layer update"
---

<div align="center">

# ⚠️ Kansas Frontier Matrix — **Raw Hazards Data**  
`data/raw/hazards/README.md`

**Purpose**  
Contain **unaltered, source-level hazard datasets** collected from:

- FEMA  
- NOAA (NCEI / SPC)  
- USGS  
- USFS  
- Other allied public institutions  

The Raw Hazards Layer preserves immutable records of environmental and disaster data for:

- ETL pipelines  
- Graph & STAC/DCAT ingestion  
- FAIR+CARE-governed Focus Mode v3 hazard reasoning  

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)](../../../docs/README.md)  
[![Open Data](https://img.shields.io/badge/License-Public%20Domain-brightgreen.svg)](../../../LICENSE)  
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Hazards%20Governed-gold.svg)](../../../docs/standards/faircare.md)  
[![STAC 1.x](https://img.shields.io/badge/STAC-1.x%20Compliant-0052cc.svg)](#)  
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)](#)

</div>

---

## 1. 📘 Overview

The **Raw Hazards Data Layer** is the immutable foundation for all hazard analytics in KFM.  

It contains original datasets for:

- Floods  
- Tornadoes & severe storms  
- Drought  
- Earthquakes  
- Wildfires  

These datasets:

- Are preserved in their **native, unmodified formats**  
- Are accompanied by **checksums, provenance, and FAIR+CARE pre-audits**  
- Serve as authoritative inputs for all downstream hazards processing and modeling  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/hazards/
├── README.md
│
├── fema_flood_zones_2025.geojson          ← FEMA NFHL floodplain zones (Kansas)
├── noaa_storm_events_1950_2025.csv        ← NOAA NCEI severe storm database
├── spc_lsr_2004_2025.csv                  ← NOAA SPC Local Storm Reports (hail/wind/tornado)
├── usgs_earthquakes_1900_2025.geojson     ← USGS earthquake catalog (KS region)
├── usdm_drought_monitor.json              ← U.S. Drought Monitor (weekly indices)
├── wildfire_perimeters_2010_2025.geojson  ← USFS/USGS burn area perimeters
│
├── metadata.json                          ← provenance & checksum manifest (JSON-LD)
└── source_licenses.json                   ← per-source license & attribution notes
~~~~

Each file must be referenced in `metadata.json` and in global checksum manifests.

---

## 3. 🧭 Data Acquisition Workflow

~~~~mermaid
flowchart TD
    SRC["External Hazard Sources\n(FEMA · NOAA · USGS · USFS · NIDIS)"]
      --> ING["Ingestion Jobs\n(API · FTP · batch download)"]

    ING --> PRE["FAIR+CARE Pre-Audit\n(license · ethics · sensitivity)"]
    PRE --> REG["Checksum & Provenance Registration\n(data/raw/hazards/metadata.json)"]
    REG --> PROMO["Promotion to Staging\n(data/staging/hazards/*)"]
~~~~

### 3.1 Workflow Stages

1. **Acquisition**  
   - Fetch hazard datasets from official providers.  
   - Capture URLs, providers, documentation links, and license text.  

2. **Verification**  
   - Compute SHA-256 checksums for each file.  
   - Compare against upstream hashes when available.  

3. **FAIR+CARE Pre-Audit**  
   - Review ethical implications, community impacts, and licensing conditions.  
   - Flag any special handling (e.g., sensitive facility locations).  

4. **Registration**  
   - Record acquisition events in `metadata.json`.  
   - Mirror to `docs/reports/audit/data_provenance_ledger.json`.  

5. **Promotion**  
   - Once recorded, raw files are eligible to feed into `data/staging/hazards/` for normalization.  

---

## 4. 🧩 Example Source Metadata Record

~~~~json
{
  "id": "spc_lsr_2004_2025_raw",
  "domain": "hazards",
  "source": "NOAA Storm Prediction Center — Local Storm Reports",
  "data_url": "https://www.spc.noaa.gov/wcm/#data",
  "provider": "NOAA SPC",
  "provider_type": "Government / Open Data",
  "format": "CSV",
  "license": "Public Domain (NOAA)",
  "records_fetched": 210384,
  "checksum_sha256": "sha256:51a4c0e5668b1f3e2a9e5b7d1c3a4f6b9c2d1e4f7a8b9c0d1e2f3a4b5c6d7e8f",
  "retrieved_on": "2025-11-12T19:28:00Z",
  "validator": "@kfm-hazards-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 5. ⚖️ FAIR+CARE Compliance Matrix

| Principle            | Implementation                                                        | Oversight            |
|----------------------|-----------------------------------------------------------------------|----------------------|
| 🔍 **Findable**      | STAC/DCAT entries for raw sources in `data/raw/metadata/`.           | `@kfm-data`          |
| 🔓 **Accessible**    | Public-domain or open data; upstream access notes preserved.         | `@kfm-accessibility` |
| 🔗 **Interoperable** | Native formats (GeoJSON, CSV, JSON) preserved with schema mapping.   | `@kfm-architecture`  |
| 🔁 **Reusable**      | Source description, schema, checksum, and provenance recorded.       | `@kfm-design`        |
| 🤝 **Collective Benefit** | Enables hazard science & public resilience work.               | `@faircare-council`  |
| 🛡️ **Authority**     | Governance & FAIR+CARE Council review ingestion processes.           | `@kfm-governance`    |
| 📋 **Responsibility**| ETL teams validate integrity and ethical usage constraints.          | `@kfm-security`      |
| 🧠 **Ethics**        | Sensitive impacts or locations flagged for masking in downstream use.| `@kfm-ethics`        |

Governance artifacts:

~~~~text
docs/reports/audit/data_provenance_ledger.json
docs/reports/fair/data_care_assessment.json
~~~~

---

## 6. 🔐 Integrity & Cataloging

### 6.1 Checksum Verification

Checksums for raw hazards files are stored in:

~~~~text
data/raw/hazards/metadata.json
data/checksums/manifest.json
~~~~

Each entry includes:

- `file` → path to file in `data/raw/hazards/`  
- `checksum_sha256` → computed SHA-256 (sha256-...)  
- `validated` → whether verified against upstream hash  
- `verified_on` → timestamp  

### 6.2 STAC/DCAT Hooks

Raw hazards sources can be referenced in STAC/DCAT metadata:

- As **upstream collections** for processed hazards Items  
- For certain feeds (e.g., USDM drought JSON) as direct STAC Items  

This ensures upstream origin is visible in catalogs and graph lineage.

---

## 7. ♻️ Retention & Sustainability

| Category             | Retention | Policy                                         |
|----------------------|----------:|------------------------------------------------|
| Raw Hazard Datasets  | Permanent | Immutable archival for verification & audits   |
| Source Metadata      | Permanent | ISO 19115 lineage retention                    |
| Checksum Records     | Permanent | Integrity evidence each release cycle          |
| FAIR+CARE Pre-Audits | 5 years   | Licensing & ethics review archive              |
| Ingestion Logs       | 365 days  | Rotated per governance/infrastructure policy   |

Retention logic is defined in:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 8. 🌱 Telemetry & Sustainability Metrics

Ingestion telemetry for raw hazards includes:

- `energy_wh` — energy used per ingestion job  
- `carbon_gCO2e` — carbon equivalent estimate  
- `files_ingested` — number of new or updated raw files  
- `validation_failures` — ingestion-time schema or checksum issues  

Telemetry aggregated into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-hazards-v11.json
~~~~

These metrics help:

- Quantify the resource impact of large hazard ingests  
- Guide scheduling and optimization decisions  
- Feed governance dashboards  

---

## 9. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Hazards Data (v11.0.0).
Unaltered, checksum-verified hazard datasets from FEMA, NOAA, USGS, USFS,
and allied sources, forming the FAIR+CARE-governed baseline for all downstream
hazard ETL, modeling, and Focus Mode v3 hazard analytics.
~~~~

---

## 10. 🕰 Version History

| Version | Date       | Summary                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Upgraded to v11; telemetry v4 integration, FAIR+CARE pre-audits v11, ROOT-GOVERNANCE reference alignment. |
| v10.2.2 | 2025-11-12 | Streaming STAC hooks, telemetry v2, expanded pre-audit fields (USDM/SPC/NWIS).                             |
| v10.0.0 | 2025-11-09 | Streaming STAC baseline, telemetry schema refs, lifecycle policy clarified.                                |
| v9.7.0  | 2025-11-06 | Checksum & governance audits; sustainability metrics added.                                                |

<div align="center">

**Kansas Frontier Matrix — Raw Hazards Data Layer**  
⚠️ Hazard Integrity · ⚖️ FAIR+CARE Raw Governance · 🧬 Provenance Assurance  

[⬅️ Back to Raw Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>