---
title: "🌪️ Kansas Frontier Matrix — Q4 2025 Hazards Dataset Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/2025Q4/hazards_v9.7.0/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-hazards-archive-v4.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
---

<div align="center">

# 🌪️ Kansas Frontier Matrix — **Q4 2025 Hazards Dataset Archive**
`data/archive/2025Q4/hazards_v9.7.0/README.md`

**Purpose:**  
Documents the **Q4 2025 FAIR+CARE-certified hazards dataset**, including flood, tornado, drought, and severe weather events across Kansas.  
This archive provides verified, immutable data for geospatial and historical hazard analysis, ensuring full provenance and governance traceability under **MCP-DL v6.3** and **ISO 19115** standards.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../../LICENSE)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Hazards%20Certified-gold.svg)](../../../../docs/standards/faircare-validation.md)
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-blue.svg)]()

</div>

---

## 📘 Overview

The **Q4 2025 Hazards Dataset Archive** integrates multiple public and historical data sources into a unified, ethically governed dataset.  
It provides spatially indexed information on **floods, tornadoes, droughts, and severe storms**, including frequency, intensity, and affected regions across Kansas.

All files are:
- **Checksum-verified (SHA-256)** and immutably logged in the provenance ledger.  
- **FAIR+CARE-certified**, ensuring accessibility, reusability, and ethical data governance.  
- **Geo-temporally aligned**, allowing timeline and map-based analyses in Focus Mode.  
- **Published under open license (CC-BY 4.0)** with ISO 19115 metadata descriptors.

---

## 🗂️ Directory Layout

```plaintext
data/archive/2025Q4/hazards_v9.7.0/
├── README.md                               # This file — documentation for hazards dataset archive
│
├── hazards_tornado_flood.geojson           # Tornado & flood event polygons (1850–2025)
├── hazards_summary.parquet                 # Consolidated hazard metrics (normalized format)
├── hazards_validation_report.json          # FAIR+CARE + checksum validation report
├── metadata.json                           # STAC/DCAT metadata (ISO 19115-aligned)
└── checksums.json                          # File-level SHA-256 checksum registry
```

---

## ⚙️ Dataset Specifications

| Field | Description | Example |
|---|---|---|
| `event_id` | Unique identifier for each recorded hazard event. | `KFM_HAZ_2025_03412` |
| `event_type` | Type of hazard (Flood, Tornado, Drought, etc.). | `Tornado` |
| `start_date` | ISO 8601 date of event occurrence. | `2025-05-13` |
| `end_date` | ISO 8601 date of event conclusion. | `2025-05-14` |
| `location_name` | Common name of affected region or county. | `Sedgwick County` |
| `geometry` | GeoJSON polygon or point geometry. | `{"type": "Polygon", "coordinates": [...]}` |
| `severity_index` | Numeric intensity measure (0–10). | `8.3` |
| `economic_damage_usd` | Estimated financial impact (2025 USD). | `2450000` |
| `fairstatus` | FAIR+CARE certification status. | `certified` |
| `checksum_sha256` | SHA-256 cryptographic hash. | `sha256:97b3f6a8a3c1c7b...` |

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | Indexed via STAC Item & DCAT metadata. | `@kfm-data` |
| **Accessible** | Open GeoJSON & Parquet under CC-BY 4.0. | `@kfm-accessibility` |
| **Interoperable** | Schema aligns with ISO 19115 & STAC 1.0. | `@kfm-architecture` |
| **Reusable** | Metadata-rich files with provenance & checksums. | `@kfm-design` |
| **Collective Benefit** | Supports community resilience research. | `@faircare-council` |
| **Authority to Control** | FAIR+CARE Council validates final datasets. | `@kfm-governance` |
| **Responsibility** | Verification workflows ensure authenticity. | `@kfm-security` |
| **Ethics** | Data reviewed for equity, safety, and sensitivity. | `@kfm-ethics` |

Governance verification logs:  
`data/reports/audit/data_provenance_ledger.json`

---

## 🧩 Validation & Provenance Linkage

| Process | Tool / Workflow | Output |
|---|---|---|
| **Schema Validation** | `schema_validation.py` | `hazards_validation_report.json` |
| **Checksum Verification** | `checksum-verify.yml` | `checksums.json` |
| **FAIR+CARE Certification** | `faircare-validate.yml` | `data/reports/fair/faircare_summary.json` |
| **Governance Registration** | `governance-ledger.yml` | `data_provenance_ledger.json` |
| **STAC Catalog Update** | `stac-validate.yml` | `data/stac/catalog.json` |

---

## 📊 Example Provenance Record

```json
{
  "id": "hazards_v9.7.0_tornado_flood",
  "records": 32421,
  "checksum_verified": true,
  "fairstatus": "certified",
  "schema_version": "v3.0.1",
  "validated_on": "2025-11-06T19:50:00Z",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json",
  "archived_by": "@kfm-data"
}
```

---

## 🌱 Sustainability & Preservation Metrics

| Metric | Value | Verified By |
|---|---|---|
| File Integrity | 100% (62 checksums verified) | `@kfm-validation` |
| Energy Usage | 12.4 Wh per ETL + validation cycle | `@kfm-sustainability` |
| FAIR+CARE Compliance | Certified | `@faircare-council` |
| Retention Policy | Permanent (ISO 16363) | `@kfm-governance` |

Telemetry reference:  
`../../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Hazards Dataset Archive (v9.7.0, Q4 2025).
Contains FAIR+CARE-certified hazards datasets including tornado, flood, and drought events across Kansas.
Implements ISO 19115 metadata, SHA-256 integrity validation, and STAC/DCAT interoperability for transparent open science.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v9.7.0 | 2025-11-06 | `@kfm-data` | Created Q4 2025 hazards dataset archive README; aligned metadata, governance, and checksum verification. |
| v9.6.0 | 2025-11-03 | `@kfm-archive` | Added governance provenance schema and STAC/DCAT integration. |
| v9.3.2 | 2025-10-28 | `@kfm-core` | Established baseline hazard data archival standards. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Hazards Data Integrity × FAIR+CARE Ethics × Provenance Governance*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Q4 Archive](../README.md) · [Governance Charter](../../../../docs/standards/governance/DATA-GOVERNANCE.md) · [FAIR+CARE Reports](../../../../data/reports/fair/faircare_summary.json)

</div>

