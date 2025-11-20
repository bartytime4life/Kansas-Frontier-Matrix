---
title: "🌦️ Kansas Frontier Matrix — Raw Climate Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/climate/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-climate-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-climate-readme"
event_source_id: "ledger:data/raw/climate/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-climate-v11.json"
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
intent: "raw-climate-data"
role: "raw-climate-domain"
category: "Data · Raw · Climate · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Low — public climate records (source-dependent exceptions)"
sensitivity_level: "Low"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Low"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-raw-climate-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-raw-climate-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative"
  - "unverified historical claims"

machine_extractable: true
classification: "Public Data / Low Sensitivity"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next raw-climate-domain update"
---

<div align="center">

# 🌦️ Kansas Frontier Matrix — **Raw Climate Data**  
`data/raw/climate/README.md`

**Purpose**  
Contain **unaltered, source-level climate datasets** from:

- NOAA (NCEI, CPC)  
- NIDIS  
- USDM (U.S. Drought Monitor)  
- Daymet / NASA  
- Other open climate archives  

The raw climate layer provides:

- Immutable baselines for climate analysis and reanalysis  
- Strong provenance and checksum integrity  
- FAIR+CARE-compliant ingestion and governance workflows  

</div>

---

## 1. 📘 Overview

The **Raw Climate Data Layer** stores all primary inputs for:

- Temperature anomalies and climatologies  
- Precipitation records and extremes  
- Drought indices and impacts  
- Gridded reanalysis and downscaled climate datasets  

Characteristics:

- Files are stored **exactly as delivered** by upstream providers.  
- No cleaning or transformation is performed here.  
- All files are accompanied by **checksums, provenance, and pre-audit FAIR+CARE metadata**.  

This layer is the **legal and scientific anchor** for all downstream climate products.

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/climate/
├── README.md
│
├── noaa_global_temp_1900_2025.csv        ← NOAA global temperature anomalies
├── cpc_precipitation_daily.csv           ← NOAA CPC daily precipitation
├── usdm_drought_monitor.json             ← U.S. Drought Monitor (weekly)
├── ndis_drought_risk.csv                 ← NIDIS drought severity/impacts
├── daymet_daily_1980_2025.nc             ← Daymet daily gridded climate (NetCDF)
├── cpc_climate_normals_1991_2020.csv     ← CPC climate normals (30-year means)
│
├── metadata.json                         ← provenance & checksum manifest (JSON-LD)
└── source_licenses.json                  ← licensing & access metadata (per provider)
~~~~

Domain-specific `README.md` files under `data/raw/` may provide additional detail for sub-sources or special feeds.

---

## 3. 🧭 Data Acquisition Workflow

~~~~mermaid
flowchart TD
    SRC["External Climate Sources\n(NOAA · NIDIS · USDM · NASA/Daymet)"]
      --> ING["Ingestion Jobs\n(ETL · API · bulk downloads)"]

    ING --> PRE["FAIR+CARE Pre-Audit\n(ethics · license · sensitivity)"]
    PRE --> REG["Checksum & Provenance Registration\n(data/raw/climate/metadata.json)"]
    REG --> PROMO["Promotion to Staging\n(data/staging/climate/*)"]
~~~~

### Steps

1. **Acquisition**  
   - Retrieve via API, FTP, HTTPS, or institutional repositories.  
   - Capture **source URL**, **provider info**, and **official license text**.  

2. **Verification**  
   - Compute SHA-256 checksum for each file.  
   - When upstream checksums provided, verify parity.  

3. **FAIR+CARE Pre-Audit**  
   - Evaluate licensing, attribution, and any sensitive or community-specific issues.  
   - Record notes and flags in `metadata.json` and governance logs.  

4. **Registration**  
   - Log provenance events and acquisition context to `provenance` structures.  
   - Update global governance ledger with source-level entries.  

5. **Promotion**  
   - Promote raw files to `data/staging/climate/` (still with clear link back to raw) for transformation.  

---

## 4. 🧩 Example Source Metadata Record (JSON)

~~~~json
{
  "id": "noaa_precipitation_daily_2025",
  "domain": "climate",
  "source_url": "https://www.cpc.ncep.noaa.gov/",
  "provider": "NOAA Climate Prediction Center",
  "provider_type": "Government / Open Data",
  "format": "CSV",
  "license": "Public Domain (NOAA)",
  "records_fetched": 365240,
  "checksum_sha256": "sha256:b7f19a29d1cc7f98a3c5a9cfcf3f212a91d4e76acb9e5e12a5db4f6c45b7a0c5",
  "retrieved_on": "2025-11-12T19:32:00Z",
  "validator": "@kfm-climate-lab",
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

| Principle            | Implementation                                                      | Oversight            |
|----------------------|---------------------------------------------------------------------|----------------------|
| 🔍 **Findable**      | STAC/DCAT entries in `data/raw/metadata/` (JSON-LD).               | `@kfm-data`          |
| 🔓 **Accessible**    | Public domain license; upstream access notes preserved verbatim.   | `@kfm-accessibility` |
| 🔗 **Interoperable** | Native formats (CSV, JSON, NetCDF) with metadata crosswalks.       | `@kfm-architecture`  |
| 🔁 **Reusable**      | Full source, checksum, schema, and license recorded.               | `@kfm-design`        |
| 🤝 **Collective Benefit** | Supports transparent climate science and public understanding.| `@faircare-council`  |
| 🛡️ **Authority**     | FAIR+CARE Council reviews ethics and licensing for edge cases.     | `@kfm-governance`    |
| 📋 **Responsibility**| Ingestion teams ensure ethics + integrity; logs reviewed regularly.| `@kfm-security`      |
| 🧠 **Ethics**        | Sensitive or misrepresented content flagged and quarantined.       | `@kfm-ethics`        |

---

## 6. 🔐 Data Integrity & Cataloging

### 6.1 Checksum Verification

Checksums are stored in:

~~~~text
data/raw/climate/metadata.json
data/checksums/manifest.json
~~~~

Each checksum entry contains:

- `file` (path under `data/raw/climate/`)  
- `checksum_sha256` (sha256-...)  
- `validated` (true/false)  
- `verified_on` (ISO timestamp)  

### 6.2 Provenance & Cataloging

Provenance is logged via:

- `data/raw/metadata/provenance.json` (domain-level)  
- `docs/reports/audit/data_provenance_ledger.json` (global ledger)  

STAC/DCAT integration for raw sources is optional but recommended, particularly for:

- USDM drought JSON  
- Daymet NetCDF grids (as raw STAC Items)  

---

## 7. ♻️ Retention & Sustainability

| Category           | Retention | Policy                                        |
|--------------------|----------:|-----------------------------------------------|
| Raw Climate Files  | Permanent | Immutable archival for provenance and audits  |
| Source Metadata    | Permanent | ISO 19115 / FAIR+CARE retention               |
| Checksum Records   | Permanent | Integrity evidence                            |
| FAIR+CARE Pre-Audits | 5 years | Ethics/licensing review archive              |
| Ingestion Logs     | 365 days  | Rotated per governance and infra policy       |

Retention automation is defined in:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 8. 🌱 Telemetry & Sustainability Metrics

Ingestion telemetry includes:

- `energy_wh` — energy used per ingestion job  
- `carbon_gCO2e` — carbon-equivalent estimate  
- `files_ingested` — count of new or updated inputs  
- `validation_failures` — ingestion validation issues  

Telemetry is aggregated into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-climate-v11.json
~~~~

These metrics help:

- Understand ingestion costs  
- Optimize job scheduling and infrastructure use  
- Provide transparency on resource usage  

---

## 9. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Climate Data (v11.0.0).
Unaltered, checksum-verified climate datasets from NOAA, NIDIS, CPC, USDM,
Daymet, and related providers used as FAIR+CARE-aligned baselines for all
downstream climate ETL, validation, and Focus Mode v3 analytics.
~~~~

---

## 10. 🕰 Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Upgraded to v11: telemetry v4, FAIR+CARE pre-audits v11, ROOT-GOVERNANCE ref, ontology alignment.    |
| v10.2.2 | 2025-11-12 | Streaming STAC hooks, telemetry v2 bindings, expanded pre-audit fields and JSON-LD metadata.         |
| v10.0.0 | 2025-11-09 | Streaming STAC baseline, telemetry schema refs, lifecycle policy clarified.                           |
| v9.7.0  | 2025-11-06 | Provenance & checksum automation for all climate datasets.                                            |

<div align="center">

**Kansas Frontier Matrix — Raw Climate Data Layer**  
🌦️ Open Climate Baselines · ⚖️ FAIR+CARE Source Governance · 🧬 Provenance Integrity  

[⬅️ Back to Raw Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>