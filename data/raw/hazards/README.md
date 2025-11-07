---
title: "⚠️ Kansas Frontier Matrix — Raw Hazards Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/hazards/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-hazards-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Open Data / Public Domain"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ⚠️ Kansas Frontier Matrix — **Raw Hazards Data**
`data/raw/hazards/README.md`

**Purpose:**  
Contains **unaltered, source-level hazard datasets** collected from FEMA, NOAA, USGS, USFS, and related institutions.  
The Raw Hazards Layer preserves immutable records of environmental and disaster data for ETL pipelines and **Focus Mode** reasoning under **FAIR+CARE** governance.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![Open Data](https://img.shields.io/badge/License-Public%20Domain-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Hazards%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Hazards Data Layer** is the immutable foundation for all hazard analytics in KFM.  
It contains original datasets for **floods, tornadoes, droughts, earthquakes, and wildfires** across Kansas—retrieved directly from verified public sources and preserved with governance-linked metadata.

### Objectives
- Preserve **unaltered** hazard data in native formats.  
- Maintain **provenance + checksum** validation for integrity.  
- Ensure **FAIR+CARE** ethical compliance and open reuse.  
- Serve as inputs for **ETL, AI reasoning, and Focus Mode** hazard modeling.

---

## 🗂️ Directory Layout

```plaintext
data/raw/hazards/
├── README.md
├── fema_flood_zones_2025.geojson          # FEMA NFHL floodplain zones (Kansas)
├── noaa_storm_events_1950_2025.csv        # NOAA NCEI severe storm database
├── usgs_earthquakes_1900_2025.geojson     # USGS earthquake records (KS region)
├── usdm_drought_monitor.json              # U.S. Drought Monitor severity indices
├── wildfire_perimeters_2010_2025.geojson  # USFS/USGS burn area perimeters
├── metadata.json                          # Provenance, checksums, licensing
└── source_licenses.json                   # Per-source license & attribution notes
```

---

## 🧭 Data Acquisition Summary

| Dataset              | Source                | Records | Format  | License        | Integrity |
|---------------------|-----------------------|--------:|---------|----------------|----------:|
| FEMA Flood Zones    | FEMA NFHL             |   6,932 | GeoJSON | Public Domain  | ✅ Verified |
| NOAA Storm Events   | NOAA NCEI             |  72,145 | CSV     | Public Domain  | ✅ Verified |
| USGS Earthquakes    | USGS                  |   3,274 | GeoJSON | Public Domain  | ✅ Verified |
| USDM Drought Monitor| USDA / NIDIS          |  14,832 | JSON    | Public Domain  | ✅ Verified |
| Wildfire Perimeters | USFS / USGS           |   9,145 | GeoJSON | Public Domain  | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "fema_flood_zones_2025_raw",
  "source": "FEMA National Flood Hazard Layer (NFHL)",
  "data_url": "https://hazards.fema.gov/femaportal/",
  "provider": "Federal Emergency Management Agency (FEMA)",
  "format": "GeoJSON",
  "license": "Public Domain (FEMA)",
  "records_fetched": 6932,
  "checksum_sha256": "sha256:3c8a97a5e2f17a29b8fd2a14a97bcba8a1d07e6c90f24d34f9a5a63a9d3a9c25",
  "retrieved_on": "2025-11-06T19:28:00Z",
  "validator": "@kfm-hazards-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | STAC/DCAT entries in `data/raw/metadata/`. | `@kfm-data` |
| **Accessible** | Public domain access; open retrieval workflow notes. | `@kfm-accessibility` |
| **Interoperable** | Native formats retained (GeoJSON/CSV/JSON). | `@kfm-architecture` |
| **Reusable** | Complete source, schema, and checksum provenance. | `@kfm-design` |
| **Collective Benefit** | Supports resilience research and public safety. | `@faircare-council` |
| **Authority to Control** | Council validates ingestion protocols & attribution. | `@kfm-governance` |
| **Responsibility** | ETL maintainers verify checksums, provenance, and ethics. | `@kfm-security` |

---

## 🧠 Integrity & Cataloging

| Process              | Description                                  | Output                                           |
|---------------------|----------------------------------------------|--------------------------------------------------|
| **Checksum Verify** | SHA-256 per file; vendor hash comparison.     | `data/raw/hazards/metadata.json`                 |
| **Provenance Log**  | Acquisition lineage & reviewer notes.         | `data/reports/audit/data_provenance_ledger.json` |
| **License Audit**   | FAIR+CARE licensing and attribution review.   | `data/raw/hazards/source_licenses.json`          |
| **Catalog Publish** | STAC/DCAT registration for discoverability.   | `data/raw/metadata/stac_catalog.json`            |

---

## 📊 Example Checksum Record

```json
{
  "file": "noaa_storm_events_1950_2025.csv",
  "checksum_sha256": "sha256:7b8d9e7d57d4a21f71e4a3b2cc6f4896f5e3d1bcb2a1f8a6d78b5f59ac3c1d8a",
  "validated": true,
  "verified_on": "2025-11-06T19:33:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Sustainability

| Category            | Retention | Policy                                                  |
|--------------------|----------:|---------------------------------------------------------|
| Raw Hazard Data    | Permanent | Immutable archival for verification & reproducibility.  |
| Source Metadata    | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records   | Permanent | Long-term integrity evidence.                           |
| FAIR+CARE Pre-Audit| 5 Years   | Licensing/attribution review archive.                   |
| Ingestion Logs     | 365 Days  | Rotated per governance policy.                          |

**Telemetry reference:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Hazards Data (v9.7.0).
Unaltered hazard datasets collected from FEMA, NOAA, USGS, and allied sources.
Immutable, checksum-verified inputs for FAIR+CARE-governed ETL and Focus Mode hazard analytics.
```

---

## 🕰️ Version History

| Version | Date       | Author         | Summary |
|--------:|------------|----------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-hazards` | Upgraded to v9.7.0; telemetry/schema refs added; governance & badges aligned. |
| v9.6.0  | 2025-11-03 | `@kfm-hazards` | Added checksum verification, metadata linkage, governance registry. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Integrated licensing audit and provenance sync. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Hazard Integrity × FAIR+CARE Ethics × Provenance Assurance*  
© 2025 Kansas Frontier Matrix — Open Data / Public Domain · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>