---
title: "🧾 Kansas Frontier Matrix — Raw Metadata Repository (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/metadata/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-metadata-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0 / FAIR+CARE Governance License"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Raw Metadata Repository**
`data/raw/metadata/README.md`

**Purpose:**  
Central repository for **source-level metadata, provenance manifests, and checksum registries** associated with raw datasets in the Kansas Frontier Matrix (KFM).  
Ensures transparent, auditable, and **FAIR+CARE** compliant traceability for all data ingestion workflows.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Metadata%20Certified-gold.svg)](../../../docs/standards/faircare-validation.md)
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Metadata Repository** provides structured records linking raw datasets to their **provenance, checksums, licensing, and FAIR+CARE** validation.  
It is the base of the **metadata lineage chain** used across ETL, validation, release, and archival workflows.

### Core Functions
- Store **FAIR+CARE-certified** source metadata and provenance.  
- Maintain **checksums** for integrity verification.  
- Generate **STAC 1.0** and **DCAT 3.0** catalogs for discovery and exchange.  
- Synchronize with governance ledgers for ethical transparency.

---

## 🗂️ Directory Layout

```plaintext
data/raw/metadata/
├── README.md
├── provenance_manifest.json      # Master lineage → governance ledger map
├── checksums.json                # SHA-256 registry for all raw files
├── faircare_preaudit.json        # Pre-ingestion ethics & licensing audit
├── stac_catalog.json             # STAC 1.0 catalog for discoverability
├── dcat_catalog.json             # DCAT 3.0 dataset/distribution registry
├── metadata_summary.csv          # Human-readable inventory index
└── metadata.json                 # Root overview: schema, checksums, governance links
```

---

## 🧭 Metadata Governance Summary

| Record                    | Description                                   | Standard   | Validation |
|--------------------------|-----------------------------------------------|------------|------------|
| `provenance_manifest.json` | Dataset lineage & acquisition history         | ISO 19115  | ✅ Verified |
| `checksums.json`           | File-level SHA-256 integrity entries          | ISO/FAIR   | ✅ Verified |
| `faircare_preaudit.json`   | Attribution, license, and ethics pre-checks   | FAIR+CARE  | ✅ Verified |
| `stac_catalog.json`        | Spatio-temporal discovery metadata            | STAC 1.0   | ✅ Verified |
| `dcat_catalog.json`        | Interoperability/exchange catalog             | DCAT 3.0   | ✅ Verified |

---

## 🧩 Example Provenance Record

```json
{
  "id": "raw_data_provenance_2025_11_06",
  "datasets": [
    {
      "name": "noaa_precipitation_daily.csv",
      "domain": "climate",
      "source": "NOAA CPC",
      "checksum_sha256": "sha256:e5f8c71b93254a1926d8ffb53c63b28f7f3a6b9cd38d9c17ac721ae4df4b9a4c",
      "license": "Public Domain",
      "retrieved_on": "2025-11-06T19:33:00Z"
    },
    {
      "name": "fema_flood_zones_2025.geojson",
      "domain": "hazards",
      "source": "FEMA NFHL",
      "checksum_sha256": "sha256:c8d13e7b2e71aa12e37f4f2c8cb67b9acb1d7f32e8dcfb472e8d2a64e8c6e2f4",
      "license": "Public Domain"
    }
  ],
  "validator": "@kfm-metadata-lab",
  "archived_on": "2025-11-06T20:30:00Z",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | STAC/DCAT registry & metadata_summary.csv index. | `@kfm-data` |
| **Accessible** | JSON/CSV exports under CC-BY 4.0. | `@kfm-accessibility` |
| **Interoperable** | ISO 19115 + STAC 1.0 + DCAT 3.0 alignment. | `@kfm-architecture` |
| **Reusable** | Provenance, license, and checksums embedded. | `@kfm-design` |
| **Collective Benefit** | Transparent lineage for trustworthy reuse. | `@faircare-council` |
| **Authority to Control** | Council verifies ingestion/audit compliance. | `@kfm-governance` |
| **Responsibility** | Curators maintain schema & checksum integrity. | `@kfm-security` |

---

## 🧠 Data Integrity & Audit Process

| Step                 | Description                                   | Output                     |
|----------------------|-----------------------------------------------|----------------------------|
| **Checksum Verify**  | SHA-256 hashing & vendor comparison.          | `checksums.json`           |
| **FAIR+CARE Pre-Audit** | Ethics, licensing, and attribution checks.  | `faircare_preaudit.json`   |
| **Provenance Register** | Lineage entries linked to governance ledger.| `provenance_manifest.json` |
| **Catalog Index**    | STAC/DCAT publication for discovery.          | `stac_catalog.json` · `dcat_catalog.json` |

Automation: `metadata_validation_sync.yml`

---

## 📊 Example Checksum Entry

```json
{
  "file": "blm_land_ownership.csv",
  "checksum_sha256": "sha256:b2f13d8a97b2df7a1b32c1a1e2a7b9c3e8f4e8b3c9f8a7a9b3e2d8c7f3c9e2a1",
  "validated": true,
  "verified_on": "2025-11-06T20:32:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Compliance & Retention Policy

| File Type            | Retention | Policy                                            |
|---------------------|----------:|---------------------------------------------------|
| Provenance Manifest | Permanent | Immutable archival for lineage verification.      |
| Checksum Records    | Permanent | Retained indefinitely for reproducibility.        |
| FAIR+CARE Pre-Audits| 5 Years   | Ethics and licensing reference.                   |
| Catalogs (STAC/DCAT)| Permanent | Interoperability artifacts retained.              |
| Logs                | 365 Days  | Rotated annually per governance policy.           |

**Telemetry:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Metadata Repository (v9.7.0).
Central FAIR+CARE-certified metadata repository linking all raw data sources to provenance, checksums, and governance records.
Aligned with ISO 19115, STAC 1.0, and DCAT 3.0 for traceable, ethical data stewardship.
```

---

## 🕰️ Version History

| Version | Date       | Author           | Summary |
|--------:|------------|------------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-metadata`  | Upgraded to v9.7.0; telemetry/schema references aligned; badges hardened; governance index clarified. |
| v9.6.0  | 2025-11-03 | `@kfm-metadata`  | Added FAIR+CARE audit metadata, STAC/DCAT catalogs, and checksum registry. |
| v9.5.0  | 2025-11-02 | `@kfm-governance`| Introduced governance manifest automation and sustainability telemetry. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Metadata Integrity × FAIR+CARE Ethics × Provenance Transparency*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>