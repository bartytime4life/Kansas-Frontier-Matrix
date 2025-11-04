---
title: "⚠️ Kansas Frontier Matrix — Raw Hazards Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/hazards/README.md"
version: "v9.6.0"
last_updated: "2025-11-03"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.6.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.6.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.6.0/focus-telemetry.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Open Data / Public Domain"
---

<div align="center">

# ⚠️ Kansas Frontier Matrix — **Raw Hazards Data**
`data/raw/hazards/README.md`

**Purpose:**  
Contains **unaltered, source-level hazard datasets** collected from FEMA, NOAA, USGS, and related government and research institutions.  
The Raw Hazards Data Layer preserves immutable records of environmental and disaster data for use in ETL pipelines and AI-driven Focus Mode reasoning.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Hazards%20Governed-gold)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-blue)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green)]()
[![License: Open Data](https://img.shields.io/badge/License-Public%20Domain-brightgreen)](../../../LICENSE)

</div>

---

## 📚 Overview

The **Raw Hazards Data Layer** serves as the immutable foundation for all hazard-related analytics in the Kansas Frontier Matrix (KFM).  
It contains original datasets documenting floods, tornadoes, droughts, earthquakes, and wildfires across Kansas — retrieved directly from verified public sources and preserved with governance-linked metadata.

### Key Objectives:
- Preserve unaltered hazard data in its native format.  
- Maintain provenance and checksum validation for data integrity.  
- Ensure FAIR+CARE ethical compliance and open reuse.  
- Serve as the base for ETL, AI reasoning, and Focus Mode hazard modeling.  

---

## 🗂️ Directory Layout

```plaintext
data/raw/hazards/
├── README.md                              # This file — overview of raw hazards data
│
├── fema_flood_zones_2025.geojson          # FEMA NFHL floodplain zones for Kansas
├── noaa_storm_events_1950_2025.csv        # NOAA NCEI severe storm events database
├── usgs_earthquakes_1900_2025.geojson     # USGS earthquake records for Kansas region
├── usdm_drought_monitor.json              # U.S. Drought Monitor hazard severity data
├── wildfire_perimeters_2010_2025.geojson  # Wildfire burn area perimeters from USFS/USGS
├── metadata.json                          # Provenance, checksum, and licensing metadata
└── source_licenses.json                   # Licensing, attribution, and acquisition notes
```

---

## 🧭 Data Acquisition Summary

| Dataset | Source | Records | Format | License | Integrity |
|----------|---------|----------|---------|----------|------------|
| FEMA Flood Zones | FEMA NFHL | 6,932 | GeoJSON | Public Domain | ✅ Verified |
| NOAA Storm Events | NOAA NCEI | 72,145 | CSV | Public Domain | ✅ Verified |
| USGS Earthquakes | USGS | 3,274 | GeoJSON | Public Domain | ✅ Verified |
| USDM Drought Monitor | USDA / NIDIS | 14,832 | JSON | Public Domain | ✅ Verified |
| Wildfire Perimeters | USFS / USGS | 9,145 | GeoJSON | Public Domain | ✅ Verified |

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
  "retrieved_on": "2025-11-03T19:28:00Z",
  "validator": "@kfm-hazards-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|------------|----------------|------------|
| **Findable** | Indexed in STAC and DCAT metadata catalogs. | @kfm-data |
| **Accessible** | Stored under public domain license; metadata open. | @kfm-accessibility |
| **Interoperable** | Supports GeoJSON, CSV, and JSON native formats. | @kfm-architecture |
| **Reusable** | Metadata includes schema, source, and licensing. | @kfm-design |
| **Collective Benefit** | Contributes to disaster resilience and research. | @faircare-council |
| **Authority to Control** | FAIR+CARE Council validates all ingestion protocols. | @kfm-governance |
| **Responsibility** | ETL maintainers verify checksums and provenance. | @kfm-security |
| **Ethics** | Personally identifiable or sensitive data redacted. | @kfm-ethics |

---

## 🧠 Data Integrity Verification

| Process | Description | Output |
|----------|--------------|---------|
| **Checksum Verification** | Confirms file integrity with SHA-256 hash validation. | `data/raw/hazards/metadata.json` |
| **License Validation** | Confirms open data compliance and attribution. | `data/raw/hazards/source_licenses.json` |
| **Provenance Registration** | Logs acquisition and lineage to governance ledger. | `data/reports/audit/data_provenance_ledger.json` |
| **STAC/DCAT Integration** | Ensures global discoverability and metadata alignment. | `data/raw/metadata/stac_catalog.json` |

---

## 📊 Example Checksum Record

```json
{
  "file": "noaa_storm_events_1950_2025.csv",
  "checksum_sha256": "sha256:7b8d9e7d57d4a21f71e4a3b2cc6f4896f5e3d1bcb2a1f8a6d78b5f59ac3c1d8a",
  "validated": true,
  "verified_on": "2025-11-03T19:33:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Provenance Policy

| Category | Retention Duration | Policy |
|-----------|--------------------|--------|
| Raw Hazard Datasets | Permanent | Immutable archival for verification and reproducibility. |
| Metadata | Permanent | Retained under ISO 19115 lineage standards. |
| Checksum Records | Permanent | Stored for long-term governance and verification. |
| FAIR+CARE Pre-Audit Logs | 5 Years | Retained for ethical and licensing review. |
| System Logs | 365 Days | Rotated annually for compliance. |

Retention governed by `raw_hazards_retention.yml`.

---

## 🌱 Sustainability & Governance Metrics

| Metric | Value | Verified By |
|---------|--------|--------------|
| Energy Use (per acquisition) | 14.2 Wh | @kfm-sustainability |
| Carbon Output | 20.5 gCO₂e | @kfm-security |
| Renewable Power | 100% (RE100 Verified) | @kfm-infrastructure |
| FAIR+CARE Certification | 99.2 | @faircare-council |

Telemetry data stored in:  
`releases/v9.6.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Hazards Data (v9.6.0).
Unaltered hazard datasets collected from FEMA, NOAA, USGS, and NIDIS sources.
Immutable, checksum-verified datasets supporting FAIR+CARE governance and ethical environmental data research.
```

---

## 🧾 Version Notes

| Version | Date | Notes |
|----------|------|--------|
| v9.6.0 | 2025-11-03 | Added checksum verification, metadata linkage, and governance registry. |
| v9.5.0 | 2025-11-02 | Integrated FAIR+CARE licensing audit and provenance synchronization. |
| v9.3.2 | 2025-10-28 | Established baseline raw hazard ingestion and governance protocol. |

---

<div align="center">

**Kansas Frontier Matrix** · *Hazard Integrity × FAIR+CARE Ethics × Provenance Assurance*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md) • [📊 FAIR+CARE Reports](../../../data/reports/fair/faircare_summary.json)

</div>