---
title: "📊 Kansas Frontier Matrix — Raw Tabular Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/tabular/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-tabular-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-tabular-readme"
event_source_id: "ledger:data/raw/tabular/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-tabular-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "raw-tabular-data"
role: "raw-tabular-domain"
category: "Data · Raw · Tabular · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed — structured data, context-dependent sensitivity"
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

json_schema_ref: "../../../schemas/json/data-raw-tabular-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-raw-tabular-readme-v11-shape.ttl"

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
sunset_policy: "Superseded upon next raw-tabular-domain update"
---

<div align="center">

# 📊 Kansas Frontier Matrix — **Raw Tabular Data**  
`data/raw/tabular/README.md`

Repository for **unaltered structured datasets** used by the Kansas Frontier Matrix (KFM) for:

- Demographic and census analysis  
- Historical treaty and archival crosswalks  
- Socioeconomic and administrative modeling  
- Focus Mode v3 correlation and narrative contexts  

All assets are **exactly as acquired** from verified open sources and are governed by **FAIR+CARE** ethics and provenance rules.

</div>

---

## 1. 📘 Overview

The **Raw Tabular Data Layer** holds original tabular datasets from:

- U.S. Census Bureau  
- U.S. Bureau of Land Management (BLM)  
- BEA and state economic agencies  
- NARA and other archival repositories  
- Kansas state archives and open data portals  

Characteristics:

- No cleaning, transformation, or reformatting occurs in `data/raw/tabular/`.  
- Each dataset has:
  - A SHA-256 checksum  
  - Source URL and license metadata  
  - FAIR+CARE pre-audit information  
  - A governance reference  

These files are the **structured backbone** for normalization, validation, and downstream analytics.

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/tabular/
├── README.md                              ← this file
│
├── census_population_kansas_1900_2020.csv ← U.S. Census historical population data (Kansas)
├── blm_land_ownership.csv                 ← BLM property and land ownership records
├── treaty_documents_metadata.csv          ← historical treaty metadata crosswalks
├── kansas_economic_indicators.csv         ← BEA / KS economic indicators by county
├── noaa_historical_weather_stations.csv   ← NOAA station metadata for climate linkage
│
├── metadata.json                          ← checksums, provenance, FAIR+CARE fields (JSON/JSON-LD)
└── source_licenses.json                   ← licensing & acquisition metadata (per source)
~~~~

---

## 3. 🧭 Data Acquisition Summary

| Dataset                         | Source / Provider               | Records | Format | License        | Integrity |
|---------------------------------|---------------------------------|--------:|--------|----------------|----------:|
| Census Population (1900–2020)   | U.S. Census Bureau              | 21,125  | CSV    | Public Domain  | ✅        |
| BLM Land Ownership              | U.S. Bureau of Land Mgmt.       | 14,205  | CSV    | Public Domain  | ✅        |
| Treaty Documents Metadata       | NARA / Kansas archives          | 1,024   | CSV    | Public Domain  | ✅        |
| Kansas Economic Indicators      | BEA / KS Dept. of Commerce      | 2,468   | CSV    | Public Domain  | ✅        |
| NOAA Station Metadata           | NOAA NCEI                       | 840     | CSV    | Public Domain  | ✅        |

---

## 4. 🧩 Example Source Metadata Record

~~~~json
{
  "id": "census_population_kansas_1900_2020_raw",
  "domain": "tabular",
  "source": "U.S. Census Bureau Historical Data",
  "data_url": "https://www.census.gov/data.html",
  "provider": "United States Census Bureau",
  "format": "CSV",
  "license": "Public Domain (Census Bureau)",
  "records_fetched": 21125,
  "checksum_sha256": "sha256:df12a9b8e46a37f4e1b2319eabf8d80e51c2b67a9b90b96e0d3b57b49a3a2c8f",
  "retrieved_on": "2025-11-12T20:22:00Z",
  "validator": "@kfm-tabular-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 5. ⚙️ FAIR+CARE Compliance Matrix

| Principle            | Implementation                                                | Oversight           |
|----------------------|---------------------------------------------------------------|---------------------|
| 🔍 **Findable**      | DCAT 3.0 catalog entries with dataset UUID and domain tags.  | `@kfm-data`         |
| 🔓 **Accessible**    | Open CSV files; retrieval instructions and caveats captured. | `@kfm-accessibility`|
| 🔗 **Interoperable** | Native CSV retained; JSON Schema and DCAT fields documented. | `@kfm-architecture` |
| 🔁 **Reusable**      | Source, license, schema, and checksum metadata included.     | `@kfm-design`       |
| 🤝 **Collective Benefit** | Enables socioeconomic, historical, and environmental research. | `@faircare-council` |
| 🛡️ **Authority**     | Council certifies licensing and ethical ingestion.           | `@kfm-governance`   |
| 📋 **Responsibility**| Stewards verify checksums and schema awareness before staging.| `@kfm-security`    |
| 🧠 **Ethics**        | PII is either not ingested or pre-aggregated; equity review logged. | `@kfm-ethics`   |

---

## 6. 🧠 Data Integrity & Cataloging

### 6.1 Checksum & Provenance

Integrity processes include:

- SHA-256 checksum generation and storage in:

~~~~text
data/raw/tabular/metadata.json
data/checksums/manifest.json
~~~~

- Provenance logs for each acquisition:

~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~

### 6.2 License & Attribution

Licensing and attribution for each provider stored in:

~~~~text
data/raw/tabular/source_licenses.json
~~~~

Each entry must:

- Specify upstream license or terms (Public Domain, CC, ODC, etc.)  
- Record required attribution texts  
- Flag any restrictive or unusual terms  

### 6.3 Catalog Publication

Raw tabular datasets can be surfaced in catalogs through:

- DCAT 3.0 datasets in `data/raw/metadata/dcat_catalog.json`  
- Optional STAC-like structures for tabular assets (where relevant)  

This allows tabular datasets to be linked into:

- Focus Mode narratives  
- Search and browse experiences  
- External catalog integrations  

---

## 7. ♻️ Retention & Sustainability

| Data Type              | Retention | Policy                                                 |
|------------------------|----------:|--------------------------------------------------------|
| Raw Tabular Datasets   | Permanent | Immutable archival for lineage & reproducibility       |
| Source Metadata        | Permanent | ISO 19115 lineage retention                            |
| Checksum Records       | Permanent | Long-term integrity evidence                           |
| FAIR+CARE Pre-Audits   | 5 Years   | Licensing & ethics review archive                      |
| Ingestion Logs         | 365 Days  | Rotated per governance and compliance policy          |

Retention configuration referenced via:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 8. 🌱 Telemetry & Sustainability Metrics

Ingestion telemetry captured for tabular domain:

- `energy_wh` — energy per ingestion run  
- `carbon_gCO2e` — carbon-equivalent estimate  
- `files_ingested` — number of tabular files acquired/updated  
- `validation_failures` — ingestion-time metadata or checksum issues  

Telemetry aggregated into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-tabular-v11.json
~~~~

These signals support:

- Governance and oversight reporting  
- Performance and cost optimization  
- Focus Mode introspection features  

---

## 9. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Tabular Data (v11.0.0).
Unaltered tabular datasets from U.S. Census Bureau, BEA, BLM, NARA, NOAA,
and Kansas state archives forming the FAIR+CARE-governed backbone for
normalization, modeling, and Focus Mode v3 correlation workflows in KFM.
~~~~

---

## 10. 🕰 Version History

| Version | Date       | Author         | Summary                                                                                         |
|--------:|------------|----------------|-------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | `@kfm-tabular` | Upgraded to v11; telemetry v4, FAIR+CARE pre-audit schema v11, ROOT-GOVERNANCE alignment.       |
| v10.2.2 | 2025-11-12 | `@kfm-tabular` | Streaming STAC hooks, telemetry v2, expanded license/sensitivity notes for raw tabular sources. |
| v10.0.0 | 2025-11-09 | `@kfm-tabular` | Initial v10 raw tabular spec; telemetry & DCAT mapping added.                                   |

<div align="center">

**Kansas Frontier Matrix — Raw Tabular Data Layer**  
📊 Structured Baselines · ⚖️ FAIR+CARE Governance · 🧬 Provenance Integrity  

[⬅️ Back to Raw Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
