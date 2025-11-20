---
title: "💧 Kansas Frontier Matrix — Raw Hydrology Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/hydrology/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-hydrology-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-hydrology-readme"
event_source_id: "ledger:data/raw/hydrology/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-hydrology-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Public Domain / Open Government Data"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "raw-hydrology-data"
role: "raw-hydrology-domain"
category: "Data · Raw · Hydrology · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Low–Moderate (water resource context dependent)"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Moderate"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-raw-hydrology-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-raw-hydrology-readme-v11-shape.ttl"

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
sunset_policy: "Superseded upon next raw-hydrology-domain update"
---

<div align="center">

# 💧 Kansas Frontier Matrix — **Raw Hydrology Data**  
`data/raw/hydrology/README.md`

**Purpose**  
Immutable repository for **unaltered hydrological datasets** from:

- USGS (NWIS streamflow, water levels, water quality)  
- EPA (watershed and water quality datasets)  
- KDHE (state groundwater and monitoring programs)  
- Kansas DASC (aquifer extents, hydrologic boundaries)  

These raw files provide foundational inputs for:

- 🌊 Streamflow modeling  
- 💧 Aquifer recharge and sustainability analysis  
- 🗺 Watershed and basin mapping  
- 🧠 Focus Mode v3 hydrology narratives  

All under **FAIR+CARE** and **ISO 19115** governance, with telemetry-backed ingestion.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)](../../../docs/README.md)  
[![Public Domain](https://img.shields.io/badge/License-Public%20Domain-brightgreen.svg)](../../../LICENSE)  
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Hydrology%20Governed-gold.svg)](../../../docs/standards/faircare.md)  
[![STAC 1.x](https://img.shields.io/badge/STAC-1.x%20Compliant-0052cc.svg)](#)  
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)](#)

</div>

---

## 1. 📘 Overview

The **Raw Hydrology Layer** stores **unaltered, source-acquired hydrological data** used throughout KFM for:

- Watershed analysis  
- Streamflow and flood modeling  
- Groundwater sustainability assessment  
- Water quality and contamination monitoring  

Every raw file:

- Is preserved in its original format and structure  
- Has a corresponding **checksum** and **provenance record**  
- Has a **FAIR+CARE pre-audit** entry documenting license, sensitivity, and usage constraints  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/hydrology/
├── README.md
│
├── usgs_streamflow_daily.csv              ← USGS daily streamflow (KS)
├── usgs_streamflow_realtime.json          ← USGS realtime streamflow (NWIS API snapshots)
├── kdhe_groundwater_levels.csv            ← KDHE groundwater observation wells
├── epa_watershed_boundaries.geojson       ← EPA WBD watershed boundaries
├── kansas_aquifers.geojson                ← Kansas aquifer extents (DASC)
├── precipitation_basins.json              ← precipitation basins & drainage areas
│
├── metadata.json                          ← checksums, provenance, FAIR+CARE pre-audit (JSON/JSON-LD)
└── source_licenses.json                   ← per-source license & acquisition metadata
~~~~

---

## 3. 🧭 Data Acquisition Workflow

~~~~mermaid
flowchart TD
    SRC["External Hydrology Sources\n(USGS · EPA · KDHE · DASC)"]
      --> ING["Ingestion Jobs\n(API · FTP · batch download)"]

    ING --> PRE["FAIR+CARE Pre-Audit\n(license · ethics · sensitivity)"]
    PRE --> REG["Checksum & Provenance Registration\n(data/raw/hydrology/metadata.json)"]
    REG --> PROMO["Promotion to Staging\n(data/staging/hydrology/*)"]
~~~~

### 3.1 Ingestion Steps

1. **Acquisition**  
   - Use NWIS APIs, EPA WBD services, KDHE downloads, and DASC services.  
   - Capture source URLs, versions, and native documentation.  

2. **Checksum Verification**  
   - Compute SHA-256 for each retrieved file.  
   - Compare with vendor checksums when provided.  

3. **FAIR+CARE Pre-Audit**  
   - Evaluate licensing (Public Domain/Open Government Data).  
   - Mark any datasets that intersect with sensitive or sovereign contexts.  

4. **Provenance Registration**  
   - Record acquisition events, parameters, and reviewers in `metadata.json`.  
   - Mirror essential entries into the global governance ledger.  

5. **Promotion to Staging**  
   - Once recorded, files are ready for transformation pipelines in `data/staging/hydrology/`.  

---

## 4. 🧩 Example Source Metadata Record

~~~~json
{
  "id": "usgs_streamflow_realtime_2025_raw",
  "domain": "hydrology",
  "source": "USGS National Water Information System (NWIS) — Realtime",
  "data_url": "https://waterservices.usgs.gov/nwis/iv/",
  "provider": "United States Geological Survey (USGS)",
  "format": "JSON",
  "license": "Public Domain (USGS)",
  "records_fetched": 2543892,
  "checksum_sha256": "sha256:0c7e5a1b8e49ed0a3a6c1bc5ef43e7afb63f5aeb0b9cb3e6d0b1a9812e7dac91",
  "retrieved_on": "2025-11-12T19:41:00Z",
  "validator": "@kfm-hydro-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 5. ⚖️ FAIR+CARE Compliance Matrix (Hydrology Domain)

| Principle            | Implementation                                                           | Oversight          |
|----------------------|--------------------------------------------------------------------------|--------------------|
| 🔍 **Findable**      | Raw hydrology sources indexed in STAC/DCAT metadata and JSON-LD lists.   | `@kfm-data`        |
| 🔓 **Accessible**    | Public-domain access; upstream documentation retained.                   | `@kfm-accessibility`|
| 🔗 **Interoperable** | Native formats (CSV, GeoJSON, JSON) with CRS & schema documentation.     | `@kfm-architecture`|
| 🔁 **Reusable**      | Detailed metadata, license, checksums, and provenance for each file.     | `@kfm-design`      |
| 🤝 **Collective Benefit** | Supports water management & environmental stewardship.            | `@faircare-council`|
| 🛡️ **Authority**     | FAIR+CARE Council reviews any potential sensitive content.               | `@kfm-governance`  |
| 📋 **Responsibility**| ETL & data stewards maintain integrity and transparency.                  | `@kfm-security`    |
| 🧠 **Ethics**        | Sensitive well locations may be masked in downstream workflows.          | `@kfm-ethics`      |

---

## 6. 🔐 Integrity & Cataloging

### 6.1 Checksum Verification

Checksums are stored in:

~~~~text
data/raw/hydrology/metadata.json
data/checksums/manifest.json
~~~~

Each entry contains:

- `file` — path to the raw hydrology dataset  
- `checksum_sha256` — SHA-256 in `sha256-...` format  
- `validated` — boolean flag  
- `verified_on` — ISO timestamp  

### 6.2 Catalog Hooks

Raw hydrology sources can optionally be referenced in:

- STAC Catalogs as upstream `links` to processed Items  
- DCAT as source datasets for DCAT distributions  

This provides full transparency from raw → processed → archived layers.

---

## 7. ♻️ Retention & Sustainability

| Data Type           | Retention | Policy                                          |
|---------------------|----------:|-------------------------------------------------|
| Raw Hydrology Files | Permanent | Immutable archival for provenance & audit use   |
| Source Metadata     | Permanent | ISO 19115 lineage retention                     |
| Checksum Records    | Permanent | Integrity evidence for each release             |
| FAIR+CARE Pre-Audits | 5 years  | Licensing and ethics review history            |
| Ingestion Logs      | 365 days  | Rotated per governance + infra policy           |

Retention is governed by:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 8. 🌱 Telemetry & Sustainability Metrics

Hydrology ingestion jobs emit telemetry:

- `energy_wh` — energy consumption per job  
- `carbon_gCO2e` — carbon-equivalent estimate  
- `files_ingested` — number of raw hydrology files ingested/updated  
- `validation_failures` — ingestion-time issues (schema or checksum)  

Telemetry is aggregated into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-hydrology-v11.json
~~~~

These metrics:

- Inform sustainability reporting  
- Help optimize ingestion schedules  
- Feed governance dashboards  

---

## 9. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Hydrology Data (v11.0.0).
Unaltered hydrological datasets from USGS, EPA, KDHE, and Kansas DASC forming
the FAIR+CARE-governed baseline for all downstream hydrology ETL, modeling,
and Focus Mode v3 hydrologic narratives in the Kansas Frontier Matrix.
~~~~

---

## 10. 🕰 Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Upgraded to v11; telemetry v4, FAIR+CARE pre-audits v11, ROOT-GOVERNANCE alignment, sustainability metrics. |
| v10.2.2 | 2025-11-12 | Streaming STAC hooks (NWIS), telemetry v2 bindings, expanded pre-audit fields for hydrologic feeds.         |
| v10.0.0 | 2025-11-09 | Streaming STAC baseline, telemetry schema references, lifecycle policy clarified.                           |
| v9.7.0  | 2025-11-06 | Checksum & governance audits; sustainability metrics introduced.                                             |

<div align="center">

**Kansas Frontier Matrix — Raw Hydrology Data Layer**  
💧 Water Integrity · ⚖️ FAIR+CARE Raw Governance · 🧬 Provenance Assurance  

[⬅️ Back to Raw Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>