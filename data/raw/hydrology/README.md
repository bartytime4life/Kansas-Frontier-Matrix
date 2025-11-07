---
title: "💧 Kansas Frontier Matrix — Raw Hydrology Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/hydrology/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-hydrology-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Government Data"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 Kansas Frontier Matrix — **Raw Hydrology Data**
`data/raw/hydrology/README.md`

**Purpose:**  
Immutable repository for **unaltered hydrological datasets** from **USGS, EPA, KDHE, and Kansas DASC**.  
These raw files provide foundational inputs for streamflow modeling, aquifer recharge analysis, and watershed mapping under **FAIR+CARE** and **ISO 19115** standards.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![Public Domain](https://img.shields.io/badge/License-Public%20Domain-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Hydrology%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Hydrology Layer** stores **unaltered, source-acquired hydrological data** used across KFM for watershed analysis, streamflow monitoring, and groundwater sustainability assessment.  
All files are accompanied by **provenance, checksum, and licensing** metadata to ensure reproducibility and governance continuity.

### Core Objectives
- Preserve authentic, unmodified hydrology datasets.  
- Maintain **checksum validation** for integrity assurance.  
- Provide **licensing and provenance** per FAIR+CARE standards.  
- Support downstream **ETL, AI modeling, and validation** workflows.  

---

## 🗂️ Directory Layout

```plaintext
data/raw/hydrology/
├── README.md
├── usgs_streamflow_daily.csv              # USGS daily streamflow (KS)
├── kdhe_groundwater_levels.csv            # KDHE groundwater observation wells
├── epa_watershed_boundaries.geojson       # EPA WBD watershed boundaries
├── kansas_aquifers.geojson                # Kansas aquifer extents (DASC)
├── precipitation_basins.json              # Precipitation basin & drainage areas
├── metadata.json                          # Checksums, provenance, FAIR+CARE fields
└── source_licenses.json                   # Licensing & acquisition metadata
```

---

## 🧭 Data Acquisition Summary

| Dataset                | Source / Provider                   | Records  | Format  | License        | Integrity |
|------------------------|-------------------------------------|---------:|---------|----------------|----------:|
| USGS Streamflow        | USGS NWIS                           | 1,238,450| CSV     | Public Domain  | ✅ Verified |
| KDHE Groundwater       | Kansas Dept. of Health & Environment|   81,249 | CSV     | Public Domain  | ✅ Verified |
| EPA Watershed Boundaries| EPA WBD / USGS                     |    3,452 | GeoJSON | Public Domain  | ✅ Verified |
| Kansas Aquifers        | Kansas DASC                         |    1,204 | GeoJSON | Public Domain  | ✅ Verified |
| Precipitation Basins   | USGS                                |      820 | JSON    | Public Domain  | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "usgs_streamflow_daily_2025",
  "source": "USGS National Water Information System (NWIS)",
  "data_url": "https://waterdata.usgs.gov/",
  "provider": "United States Geological Survey (USGS)",
  "format": "CSV",
  "license": "Public Domain (USGS)",
  "records_fetched": 1238450,
  "checksum_sha256": "sha256:f1a293dfed8c29b74cc7b1e13aef9c6e8b87e3e2b1a6d1e6a1a4d9d0e5f8b123",
  "retrieved_on": "2025-11-06T19:41:00Z",
  "validator": "@kfm-hydro-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | STAC/DCAT index and governance linkage. | `@kfm-data` |
| **Accessible** | Public domain access; open retrieval notes. | `@kfm-accessibility` |
| **Interoperable** | Native formats (CSV/GeoJSON/JSON) retained. | `@kfm-architecture` |
| **Reusable** | Complete source, schema, and checksum records. | `@kfm-design` |
| **Collective Benefit** | Supports sustainable water management & education. | `@faircare-council` |
| **Authority to Control** | Council validates licensing & acquisition. | `@kfm-governance` |
| **Responsibility** | Stewards verify checksum & metadata completeness. | `@kfm-security` |

---

## 🧠 Integrity & Cataloging

| Process            | Description                                  | Output                                           |
|-------------------|----------------------------------------------|--------------------------------------------------|
| **Checksum Verify** | SHA-256 per file; vendor hash comparison.     | `data/raw/hydrology/metadata.json`               |
| **Provenance Log**  | Acquisition lineage & reviewer notes.         | `data/reports/audit/data_provenance_ledger.json` |
| **License Audit**   | FAIR+CARE licensing & attribution review.     | `data/raw/hydrology/source_licenses.json`        |
| **Catalog Publish** | STAC/DCAT registration for discoverability.   | `data/raw/metadata/stac_catalog.json`            |

---

## 📊 Example Checksum Record

```json
{
  "file": "kdhe_groundwater_levels.csv",
  "checksum_sha256": "sha256:7c4eaa98b2fd98c1a63d33cb93a16fdcba8a7a7c4c2e3e9bfb2d99d8f8f3dcb1",
  "validated": true,
  "verified_on": "2025-11-06T19:45:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Sustainability

| Data Type             | Retention | Policy                                                  |
|----------------------|----------:|---------------------------------------------------------|
| Raw Hydrology Data   | Permanent | Immutable archival for reproducibility and lineage.     |
| Source Metadata      | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records     | Permanent | Integrity evidence for audits.                           |
| FAIR+CARE Pre-Audits | 5 Years   | Licensing/ethics review archive.                        |
| Ingestion Logs       | 365 Days  | Rotated per governance policy.                          |

**Telemetry reference:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Hydrology Data (v9.7.0).
Unaltered hydrological datasets sourced from USGS, EPA, KDHE, and DASC for FAIR+CARE-aligned environmental research.
Includes watershed, streamflow, and aquifer datasets preserved with full checksum and governance traceability.
```

---

## 🕰️ Version History

| Version | Date       | Author        | Summary |
|--------:|------------|---------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-hydro`  | Upgraded to v9.7.0; telemetry/schema refs aligned; badges & governance clarified; added sustainability table. |
| v9.6.0  | 2025-11-03 | `@kfm-hydro`  | Added checksum & provenance validation for USGS/EPA data. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Integrated FAIR+CARE audit & license compliance reports. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Hydrological Stewardship × FAIR+CARE Governance × Provenance Integrity*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Government Data · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>