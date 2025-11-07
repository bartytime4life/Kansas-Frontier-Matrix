---
title: "📊 Kansas Frontier Matrix — Raw Tabular Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/tabular/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-tabular-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 Kansas Frontier Matrix — **Raw Tabular Data**
`data/raw/tabular/README.md`

**Purpose:**  
Repository for **unaltered structured datasets** used by the Kansas Frontier Matrix (KFM) for research, modeling, and historical integration.  
Includes census, administrative, economic, treaty, and archival tabular data ingested directly from verified open sources and public repositories.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![License: Open Data](https://img.shields.io/badge/License-Open%20Data-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Tabular%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Tabular Data Layer** contains original tabular datasets from **U.S. Census Bureau, BEA, NOAA, BLM, NARA, and Kansas state archives**.  
Files here form the structured data backbone for **normalization, validation, and FAIR+CARE governance** across the KFM pipeline.  
All assets are preserved **exactly as acquired** (no transformations), with **provenance, license, and checksum** metadata for full reproducibility.

### Core Responsibilities
- Preserve **unaltered** tabular data and their source context.  
- Maintain **provenance + checksum** evidence for integrity and reuse.  
- Enable **schema validation** and **FAIR+CARE pre-audits** prior to staging.  
- Provide canonical inputs for **AI + Focus Mode** correlation workflows.

---

## 🗂️ Directory Layout

```plaintext
data/raw/tabular/
├── README.md                              # This file — overview of raw tabular data
│
├── census_population_kansas_1900_2020.csv # U.S. Census historical population data
├── blm_land_ownership.csv                 # Bureau of Land Management property records
├── treaty_documents_metadata.csv          # Historical treaty metadata crosswalks
├── kansas_economic_indicators.csv         # BEA economic indicators by county
├── noaa_historical_weather_stations.csv   # NOAA weather station metadata (Kansas)
├── metadata.json                          # Checksums, provenance, FAIR+CARE fields
└── source_licenses.json                   # Licensing & acquisition metadata (per source)
```

---

## 🧭 Data Acquisition Summary

| Dataset                         | Source / Provider                | Records | Format | License       | Integrity |
|--------------------------------|----------------------------------|--------:|--------|---------------|----------:|
| Census Population (1900–2020)  | U.S. Census Bureau               | 21,125  | CSV    | Public Domain | ✅ Verified |
| BLM Land Ownership             | U.S. Bureau of Land Mgmt.        | 14,205  | CSV    | Public Domain | ✅ Verified |
| Treaty Documents Metadata      | National Archives (NARA)         | 1,024   | CSV    | Public Domain | ✅ Verified |
| Kansas Economic Indicators     | BEA / KS Dept. of Commerce       | 2,468   | CSV    | Public Domain | ✅ Verified |
| NOAA Station Metadata          | NOAA NCEI                        | 840     | CSV    | Public Domain | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
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
  "retrieved_on": "2025-11-06T20:22:00Z",
  "validator": "@kfm-tabular-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | DCAT 3.0 catalog entries + governance linkages. | `@kfm-data` |
| **Accessible** | Open CSV/Parquet; public retrieval instructions. | `@kfm-accessibility` |
| **Interoperable** | Native CSV retained; JSON Schema & DCAT fields captured. | `@kfm-architecture` |
| **Reusable** | Source, license, schema, and checksum metadata included. | `@kfm-design` |
| **Collective Benefit** | Enables socioeconomic, environmental, and historical research. | `@faircare-council` |
| **Authority to Control** | Council certifies licensing and ethical ingestion. | `@kfm-governance` |
| **Responsibility** | Stewards verify checksum + schema awareness before staging. | `@kfm-security` |
| **Ethics** | PII redacted/aggregated before acquisition; equity review logged. | `@kfm-ethics` |

---

## 🧠 Data Integrity & Cataloging

| Process              | Description                                   | Output                                           |
|----------------------|-----------------------------------------------|--------------------------------------------------|
| **Checksum Verify**  | SHA-256 hashing; vendor hash comparison.      | `data/raw/tabular/metadata.json`                 |
| **License Audit**    | FAIR+CARE licensing & attribution compliance. | `data/raw/tabular/source_licenses.json`          |
| **Provenance Log**   | Acquisition lineage & reviewer notes.         | `data/reports/audit/data_provenance_ledger.json` |
| **Catalog Publish**  | DCAT/STAC registration for discovery.         | `data/raw/metadata/dcat_catalog.json`            |

---

## 📊 Example Checksum Record

```json
{
  "file": "kansas_economic_indicators.csv",
  "checksum_sha256": "sha256:ac4d2197d61cfc90e0d17f6b9127e34a98c2f6f6d3e9d05b4b56b23d4a8c4d11",
  "validated": true,
  "verified_on": "2025-11-06T20:24:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Sustainability

| Data Type               | Retention | Policy                                                  |
|------------------------|----------:|---------------------------------------------------------|
| Raw Tabular Datasets   | Permanent | Immutable archival for lineage & reproducibility.       |
| Source Metadata        | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records       | Permanent | Long-term integrity evidence.                           |
| FAIR+CARE Pre-Audits   | 5 Years   | Licensing & ethics review archives.                     |
| Ingestion Logs         | 365 Days  | Rotated per governance policy.                          |

**Telemetry reference:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Tabular Data (v9.7.0).
Unaltered tabular datasets from U.S. Census Bureau, BEA, BLM, NARA, and NOAA.
Checksum-verified and FAIR+CARE-aligned for reproducible, ethical data workflows in the Kansas Frontier Matrix.
```

---

## 🕰️ Version History

| Version | Date       | Author         | Summary |
|--------:|------------|----------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-tabular` | Upgraded to v9.7.0; telemetry/schema refs aligned; badges hardened; clarified DCAT governance flow. |
| v9.6.0  | 2025-11-03 | `@kfm-tabular` | Added checksum registry and DCAT 3.0 metadata synchronization. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Integrated FAIR+CARE compliance automation and provenance tracking. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Structured Data × FAIR+CARE Governance × Provenance Integrity*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Data Commons · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>