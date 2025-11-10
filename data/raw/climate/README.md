---
title: "🌦️ Kansas Frontier Matrix — Raw Climate Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/climate/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-climate-v10.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Government Data"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ Kansas Frontier Matrix — **Raw Climate Data**
`data/raw/climate/README.md`

**Purpose:**  
Contain **unaltered, source-level climate datasets** from **NOAA, NIDIS, CPC, USDM, and Daymet/NASA**.  
This raw layer provides immutable baselines for climate analysis, reanalysis, and **FAIR+CARE**-compliant ETL workflows within KFM.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![Public Domain](https://img.shields.io/badge/License-Public%20Domain-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Climate%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview
The **Raw Climate Data Layer** stores all primary datasets for temperature, precipitation, drought, and reanalysis workflows.  
Files are preserved in their **original structure and format**, with **provenance and checksum** metadata for full reproducibility.

**v10 Enhancements**
- **Streaming STAC** registration for frequently updated feeds (USDM weekly, Daymet annual).  
- **Telemetry v2** bindings (energy/CO₂, validation coverage) for ingestion runs.  
- Expanded FAIR+CARE pre-audit fields (licensing nuances, sensitivity flags, community notes).

### Key Responsibilities
- Store original NOAA/NIDIS/CPC/USDM/Daymet datasets.  
- Maintain **immutable source integrity** via SHA-256 hashes.  
- Provide **standardized metadata** for FAIR+CARE audit traceability.  
- Support **AI explainability** and longitudinal reanalysis pipelines.  

---

## 🗂️ Directory Layout
```plaintext
data/raw/climate/
├── README.md
├── noaa_global_temp_1900_2025.csv        # NOAA global temperature anomalies
├── cpc_precipitation_daily.csv           # NOAA CPC daily precipitation
├── usdm_drought_monitor.json             # U.S. Drought Monitor (weekly)
├── ndis_drought_risk.csv                 # NIDIS drought severity/impacts
├── daymet_daily_1980_2025.nc             # Daymet daily grids (NetCDF)
├── cpc_climate_normals_1991_2020.csv     # CPC climate normals (30-year means)
├── metadata.json                         # Provenance & checksum manifest (per-file)
└── source_licenses.json                  # Licensing & access metadata (per provider)
```

---

## 🧭 Data Acquisition Summary
| Dataset               | Source / Provider   | Records  | Format | License        | Integrity |
|-----------------------|---------------------|---------:|--------|----------------|----------:|
| NOAA Global Temp      | NOAA NCEI           | 1,521,034| CSV    | Public Domain  | ✅ Verified |
| CPC Precipitation     | NOAA CPC            |   365,240| CSV    | Public Domain  | ✅ Verified |
| USDM Drought Monitor  | USDA / NIDIS        |    22,650| JSON   | Public Domain  | ✅ Verified |
| NIDIS Drought Risk    | NIDIS               |    14,320| CSV    | Public Domain  | ✅ Verified |
| Daymet Daily          | ORNL DAAC (NASA)    | millions | NetCDF | Public Domain  | ✅ Verified |
| CPC Climate Normals   | NOAA CPC            |    10,240| CSV    | Public Domain  | ✅ Verified |

---

## 🧩 Example Source Metadata Record
```json
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
  "retrieved_on": "2025-11-09T19:32:00Z",
  "validator": "@kfm-climate-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix
| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | STAC/DCAT entries in `data/raw/metadata/`. | `@kfm-data` |
| **Accessible** | Public domain access; retrieval notes preserved. | `@kfm-accessibility` |
| **Interoperable** | CSV/JSON/NetCDF kept in native source standards. | `@kfm-architecture` |
| **Reusable** | Source, checksum, and provenance captured in metadata. | `@kfm-design` |
| **Collective Benefit** | Enables transparent climate research & education. | `@faircare-council` |
| **Authority to Control** | Council reviews licensing/ethics for each source. | `@kfm-governance` |
| **Responsibility** | Ingestion teams validate integrity & ethics compliance. | `@kfm-security` |

---

## 🧠 Data Integrity & Cataloging
| Process              | Description                                   | Output                                             |
|----------------------|-----------------------------------------------|----------------------------------------------------|
| **Checksum Verify**  | SHA-256 per file; vendor hash comparison.     | `data/raw/climate/metadata.json`                   |
| **Provenance Log**   | Acquisition metadata & reviewer notes.        | `data/reports/audit/data_provenance_ledger.json`   |
| **License Audit**    | FAIR+CARE legal/ethics compliance.            | `data/raw/climate/source_licenses.json`            |
| **Catalog Publish**  | STAC/DCAT registration for discoverability.   | `data/raw/metadata/stac_catalog.json`              |

---

## ⚖️ Retention & Sustainability
| Category               | Retention | Policy                                                  |
|-----------------------|----------:|---------------------------------------------------------|
| Raw Climate Datasets  | Permanent | Immutable archival for reproducibility.                 |
| Source Metadata       | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records      | Permanent | Long-term integrity evidence.                           |
| FAIR+CARE Pre-Audits  | 5 Years   | Licensing & attribution review archive.                 |
| Ingestion Logs        | 365 Days  | Rotated per governance compliance.                      |

**Telemetry reference:** `../../../releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation
```text
Kansas Frontier Matrix (2025). Raw Climate Data (v10.0.0).
Unaltered, checksum-verified climate datasets (NOAA, NIDIS, CPC, USDM, Daymet) for FAIR+CARE-aligned open science.
Provides foundational inputs for ETL, validation, and Focus Mode climate analytics.
```

---

## 🕰️ Version History
| Version | Date       | Author            | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | `@kfm-climate`    | Upgraded to v10: Streaming STAC hooks, telemetry v2 bindings, expanded pre-audit fields, Daymet added. |
| v9.7.0  | 2025-11-06 | `@kfm-climate`    | Telemetry/schema refs added; governance/badge alignment; clarified acquisition flow. |
| v9.6.0  | 2025-11-03 | `@kfm-climate`    | Provenance & checksum registry automation for all climate datasets. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Introduced FAIR+CARE metadata auditing and licensing validation. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Climate Integrity × FAIR+CARE Governance × Provenance Assurance*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Government Data · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>