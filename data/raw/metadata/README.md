---
title: "📚 Kansas Frontier Matrix — Raw Data Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/metadata/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.2.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-metadata-v10.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Open Data Commons / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📚 Kansas Frontier Matrix — **Raw Data Metadata Registry**  
`data/raw/metadata/README.md`

**Purpose:**  
Central repository for **source-level metadata, provenance manifests, checksum registries, and FAIR+CARE pre-audit summaries** for all Kansas Frontier Matrix (KFM) raw datasets.  
Ensures transparency, data lineage integrity, and governance-ready metadata alignment with **STAC 1.0**, **DCAT 3.0**, and **ISO 19115** standards.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/README.md)
[![License: Open Data](https://img.shields.io/badge/License-Open%20Data-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Metadata%20Governed-gold.svg)](../../../docs/standards/faircare.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Metadata Layer** documents the provenance and FAIR+CARE pre-audit details of all **raw, unaltered datasets** in the KFM system.  
It is the **single source of truth** for dataset integrity verification, source attribution, and licensing compliance prior to staging and transformation.

**v10.2.2 Enhancements**
- Introduced **JSON-LD provenance graphs** for interoperable metadata exchange.  
- Linked **Streaming STAC** and **telemetry v2** for continuous metadata updates.  
- Expanded FAIR+CARE pre-audit schema to include consent tokens and community notes.

### Core Functions

- Maintain source-level provenance metadata for each raw dataset.  
- Track licensing, attribution, and checksum validation.  
- Provide FAIR+CARE pre-audit context (sensitivity, consent, community input).  
- Facilitate **crosswalk between STAC, DCAT, and ISO 19115** for interoperability.  
- Power lineage traceability in the **Governance Ledger**.

---

## 🗂️ Directory Layout

```plaintext
data/raw/metadata/
├── README.md
├── provenance.json              # Source acquisition lineage and metadata records
├── checksums.json               # SHA-256 checksums and integrity results
├── faircare_preaudit.json       # FAIR+CARE pre-audit summary for all raw domains
├── stac_catalog.json            # STAC 1.0 catalog for raw data assets
├── dcat_catalog.json            # DCAT 3.0 export for external interoperability
└── metadata_index.json          # Unified registry with JSON-LD provenance contexts
```

---

## 🧩 Example Metadata Index Record

```json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "id": "raw_data_metadata_registry_v10.2.2",
  "source_domains": ["climate", "hydrology", "hazards", "terrain", "text", "tabular"],
  "checksum_records": 254,
  "fairstatus": "pre-certified",
  "records_updated": "2025-11-12T21:45:00Z",
  "validator": "@kfm-metadata-lab",
  "governance_registered": true,
  "provenance_graph": "data/raw/metadata/provenance.json",
  "linked_catalogs": {
    "stac": "data/raw/metadata/stac_catalog.json",
    "dcat": "data/raw/metadata/dcat_catalog.json"
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | STAC/DCAT metadata indexed by dataset UUID and domain. | `@kfm-data` |
| **Accessible** | JSON-LD and CSV exports openly available for review. | `@kfm-accessibility` |
| **Interoperable** | Dual exports using STAC 1.0 + DCAT 3.0 schemas. | `@kfm-architecture` |
| **Reusable** | Includes complete provenance, checksums, and licenses. | `@kfm-design` |
| **Collective Benefit** | Open publication strengthens reproducibility & trust. | `@faircare-council` |
| **Authority to Control** | Council certifies metadata accuracy & ethical compliance. | `@kfm-governance` |
| **Responsibility** | Validators maintain lineage and checksum integrity. | `@kfm-security` |
| **Ethics** | Sensitive data flagged; license compliance reviewed. | `@kfm-ethics` |

---

## 🧠 Metadata Validation & Publication

| Process | Description | Output |
|---|---|---|
| **Checksum Audit** | Verifies data integrity per file using SHA-256. | `data/raw/metadata/checksums.json` |
| **Provenance Log** | Records acquisition, review, and validation lineage. | `data/raw/metadata/provenance.json` |
| **FAIR+CARE Pre-Audit** | Captures ethics and licensing pre-checks. | `data/raw/metadata/faircare_preaudit.json` |
| **Catalog Generation** | Publishes STAC & DCAT metadata for discovery. | `data/raw/metadata/{stac,dcat}_catalog.json` |

**Automations:**  
`metadata_sync.yml` — continuous synchronization to governance ledgers and telemetry feeds.

---

## ⚖️ Retention & Integrity Policy

| Data Type | Retention | Policy |
|---|---|---|
| Provenance Logs | Permanent | Immutable lineage tracking (ISO 19115). |
| Checksum Records | Permanent | Long-term data integrity evidence. |
| FAIR+CARE Pre-Audits | 5 Years | Periodic review under Council oversight. |
| STAC/DCAT Catalogs | Permanent | Continuous update via streaming bridge. |

**Telemetry Source:** `../../../releases/v10.2.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Data Metadata Registry (v10.2.2).
Centralized metadata registry for provenance, checksums, and FAIR+CARE pre-audits of unaltered raw datasets.
Implements JSON-LD interoperability and governance lineage tracking under MCP-DL v6.3.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.2 | 2025-11-12 | `@kfm-data` | Added JSON-LD provenance, Streaming STAC links, telemetry v2 fields, FAIR+CARE pre-audit expansion. |
| v10.0.0 | 2025-11-09 | `@kfm-data` | Established unified metadata registry; added checksum and DCAT support. |
| v9.7.0 | 2025-11-06 | `@kfm-data` | Initial FAIR+CARE pre-audit registry; governance integration. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Metadata Transparency × FAIR+CARE Ethics × Provenance Integrity*  
© 2025 Kansas Frontier Matrix — Open Data Commons / FAIR+CARE Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>