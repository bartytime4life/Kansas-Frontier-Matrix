---
title: "📦 Kansas Frontier Matrix — Q4 2025 Data Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/2025Q4/README.md"

version: "v11.2.6"
archive_release_version: "v10.0.0"
last_updated: "2025-12-11"

release_stage: "Stable · Governed Archive"
lifecycle: "Long-Term Preservation (LTP)"
review_cycle: "Quarterly · Archive & Governance Council"
content_stability: "stable"
status: "Active · Archive Index"

doc_kind: "Archive Index"
intent: "archive-2025Q4-index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "data-archive"
  applies_to:
    - "data/archive/2025Q4/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; aggregated domain products)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
indigenous_rights_flag: false
risk_category: "Data Archive"
redaction_required: false
data_steward: "KFM Archive & Governance Council"

ttl_policy: "Permanent"
sunset_policy: "Superseded only by later consolidated archive indices; data immutable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"

immutability_status: "archive-immutable"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📦 Kansas Frontier Matrix — **Q4 2025 Data Archive**  
`data/archive/2025Q4/README.md`

**Purpose**  
Serve as the **governed index** for all **FAIR+CARE-certified data releases** archived during the **Q4 2025 cycle** of the Kansas Frontier Matrix (KFM).

This archive:

- Captures the **v10.0.0 data release** in an **immutable, checksum-verified** form.  
- Aligns with the **KFM v11.2.6 documentation and governance standards**.  
- Provides a single reference point for **provenance**, **FAIR+CARE status**, and **long-term preservation**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)](../../../docs/README.md)
[![KFM-MDP v11.2.6](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.6-informational.svg)](../../../docs/standards/kfm_markdown_protocol_v11.2.6.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Q4%202025%20Archive%20Certified-gold.svg)](../../../docs/standards/faircare-validation.md)
[![ISO 16363](https://img.shields.io/badge/ISO-16363%20Trusted%20Repository-green.svg)]()

</div>

---

## 📘 Overview

This directory documents all datasets, metadata, and governance records archived under the **Kansas Frontier Matrix Q4 2025 data release (v10.0.0)**.

The **archive itself** is described by this v11.2.6-compliant README, while the **data payloads** remain frozen at **v10.0.0**:

- All archived datasets are **FAIR+CARE-certified** and **governance-approved**.  
- Artifacts are **immutable**, **checksum-verified (SHA-256)**, and **catalog-integrated** via **STAC** and **DCAT**.  
- Preservation follows **ISO 16363** trusted digital repository practices, with **provenance** captured in a dedicated ledger and supporting reports.

High-level guarantees:

- **Reproducibility** — every dataset is linked to schemas, validation reports, and checksums.  
- **Transparency** — FAIR+CARE governance and audit trails are discoverable from this index.  
- **Longevity** — retention and sustainability policies are explicit and enforced.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 data/
    └── 📁 archive/
        └── 📁 2025Q4/
            ├── 📄 README.md                      # This file — Q4 2025 Archive overview & governance
            │
            ├── 📁 hazards_v10.0.0/               # Certified hazards datasets (floods, tornadoes, droughts)
            ├── 📁 climate_v10.0.0/               # Finalized climate datasets (temperature, precipitation)
            ├── 📁 hydrology_v10.0.0/             # Streamflow and aquifer summary datasets
            ├── 📁 landcover_v10.0.0/             # Vegetation and soil classification archives
            │
            ├── 📁 metadata/                      # FAIR+CARE certification, schemas, and governance docs
            ├── 📁 checksums/                     # SHA-256 integrity manifests for Q4 2025 datasets
            │   └── 📄 manifest.json              # Machine-readable checksum manifest
            │
            └── 📄 provenance.json                # Q4 archival provenance summary registry
~~~

**Directory rules**

- All archival subdirectories (`*_v10.0.0/`) are **append-only** once sealed.  
- `metadata/` and `checksums/` provide **machine-readable** inputs for validation and CI.  
- `provenance.json` is the **single authoritative summary** of the archive cycle-level provenance.

---

## 📦 Data & Metadata

### Archived Dataset Summary

| Domain    | Dataset                             | Records | Format                 | FAIR+CARE Status | Governance Registered |
|----------:|-------------------------------------|--------:|------------------------|------------------|-----------------------|
| Hazards   | Tornado and Flood Composite         | 32 421  | GeoJSON, Parquet       | ✅ Certified      | ✅                    |
| Climate   | NOAA Temperature & Precipitation    | 120 512 | CSV, Parquet           | ✅ Certified      | ✅                    |
| Hydrology | USGS Streamflow & Groundwater       | 47 638  | CSV, GeoJSON           | ✅ Certified      | ✅                    |
| Landcover | NDVI & Vegetation Index Mosaics     | 88 935  | GeoTIFF, JSON          | ✅ Certified      | ✅                    |

Each row corresponds to:

- One or more **STAC Collections/Items** (for asset-level access).  
- A **DCAT Dataset** representation (for catalog and federation).  
- Entries in the **provenance ledger** and **FAIR+CARE audit reports**.

### Provenance Metadata Schema (Archive-Level Pattern)

The archive-level provenance summary (in `provenance.json`) follows a simple, machine-readable pattern:

~~~json
{
  "archive_cycle": "2025Q4",
  "kfm_release_version": "v10.0.0",
  "archive_index_version": "v11.2.6",
  "datasets": [
    {
      "id": "hazards_v10.0.0",
      "checksum_verified": true,
      "faircare_status": "certified",
      "governance_ref": "data/reports/audit/data_provenance_ledger.json"
    },
    {
      "id": "climate_v10.0.0",
      "checksum_verified": true,
      "faircare_status": "certified",
      "governance_ref": "data/reports/audit/data_provenance_ledger.json"
    }
  ],
  "archived_by": "@kfm-data",
  "timestamp": "2025-11-10T19:40:00Z"
}
~~~

### Example Checksum Record

Checksum records in `checksums/manifest.json` provide file-level integrity:

~~~json
{
  "file": "climate_v10.0.0/noaa_precipitation_annual.csv",
  "checksum_sha256": "sha256:0d57a9ecb42e1a67e3f6a92c0b7a8f6aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "records": 124560,
  "validated": true,
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
~~~

---

## 🧭 Context

The **Q4 2025 Data Archive** is one node in KFM’s **quarterly archival timeline**:

- Upstream ETL, graph, and catalog pipelines generate **release candidates**.  
- Datasets pass **schema validation**, **checksum verification**, and **FAIR+CARE review**.  
- Once certified, they are **snapshotted into `data/archive/2025Q4/`** under versioned domain directories.  
- This README is updated to the **current documentation standard (KFM-MDP v11.2.6)** while the underlying **data remain frozen at v10.0.0**.

The archive serves:

- **Researchers** — as a stable reference for Q4 2025 analyses.  
- **Governance & auditors** — as a compact entry point to provenance and FAIR+CARE records.  
- **Pipeline maintainers** — as a ground truth for regression tests and backfills.

---

## 🌐 STAC, DCAT & PROV Alignment

Archival datasets are integrated into KFM’s catalog stack as follows:

- **STAC (authoritative spatial/temporal layer)**  
  - Each domain archive has one or more STAC Collections and Items under `data/stac/**`.  
  - Items reference archived assets via stable `href`s into `data/archive/2025Q4/**`.  
  - STAC metadata conform to **KFM-STAC v11** and domain extensions.

- **DCAT (derived discovery/federation layer)**  
  - `dcat:Dataset` and `dcat:Distribution` records are **derived from STAC** using the **STAC → DCAT crosswalk** and **STAC → DCAT derivation model**.  
  - These DCAT views power portals, catalogs, and external federation.

- **PROV-O (provenance layer)**  
  - Archive-level and dataset-level activities are modeled as `prov:Activity`, with datasets as `prov:Entity` linked via `prov:wasGeneratedBy` and `prov:wasDerivedFrom`.  
  - The `provenance.json` registry and `data/reports/audit/data_provenance_ledger.json` together describe:
    - The **release workflow** (ETL + validation).  
    - The **archive sealing** event for 2025Q4.

This alignment ensures that **every archived file** is traceable to:

- Its **source datasets and workflows**, and  
- Its **catalog representations** (STAC & DCAT).

---

## ⚖ FAIR+CARE & Governance

### FAIR+CARE Archival Governance Matrix

| Principle              | Implementation                                                            | Oversight               |
|------------------------|---------------------------------------------------------------------------|-------------------------|
| **Findable**           | Indexed in STAC/DCAT catalogs with stable IDs and, where applicable, DOIs.| `@kfm-data`             |
| **Accessible**         | Public/open formats (CSV, GeoJSON, Parquet, GeoTIFF) with clear licensing.| `@kfm-accessibility`    |
| **Interoperable**      | Schema alignment with STAC 1.0 and DCAT 3.0, plus KFM profiles.          | `@kfm-architecture`     |
| **Reusable**           | Permanent schema, provenance, and audit trails captured in ledgers.      | `@kfm-design`           |
| **Collective Benefit** | Datasets chosen for environmental transparency and public education.     | `@faircare-council`     |
| **Authority to Control** | Council sign-off on archive integrity and visibility constraints.      | `@kfm-governance`       |
| **Responsibility**     | Validation reports and logs retained for forensic and governance review. | `@kfm-security`         |
| **Ethics**             | Sensitive data redacted or generalized according to CARE and sovereignty policies. | `@kfm-ethics`  |

### Sustainability & Preservation Policy

| Category            | Duration  | Policy                                         |
|---------------------|----------:|-----------------------------------------------|
| Certified Datasets  | Permanent | Immutable archival retention.                 |
| FAIR+CARE Reports   | Permanent | Retained for governance reproducibility.      |
| Telemetry Records   | 5 years   | Used for energy, performance, and usage reports. |
| Checksum Manifests  | Permanent | Cross-verified each new release cycle.        |
| Metadata            | Permanent | Preserved under ISO 16363 repository practices.|

### Audit & Verification Standards

| Standard       | Scope                                    | Verified By            |
|----------------|------------------------------------------|------------------------|
| **ISO 16363**  | Trusted Digital Repository certification | `@kfm-governance`      |
| **ISO 19115**  | Metadata lineage & documentation         | `@kfm-data`            |
| **ISO 14064 / 50001** | Carbon & energy accountability    | `@kfm-sustainability`  |
| **FAIR+CARE**  | Ethics & accessibility framework         | `@faircare-council`    |
| **MCP-DL v6.3**| Documentation-first & provenance standards | `@kfm-architecture` |

---

## 🧪 Validation & CI/CD

Creation and maintenance of the Q4 2025 archive are subject to CI/CD controls:

- **Schema & Contract Validation**
  - Each dataset must conform to its **data contract** (`docs/contracts/data-contract-v3.json`).  
  - Validation summaries live in `data/reports/validation/schema_validation_summary.json`.

- **Checksum & Integrity Checks**
  - SHA-256 checksums are generated and stored in `data/archive/2025Q4/checksums/manifest.json`.  
  - CI verifies that on-disk hashes match those in the manifest before sealing the archive.

- **Catalog Validation**
  - STAC entries are validated against STAC 1.0 + KFM-STAC v11 profile.  
  - Derived DCAT records are validated against KFM-DCAT v11 and crosswalk rules.

- **Governance & Telemetry**
  - Archive creation is logged in governance records (`data/reports/audit/data_provenance_ledger.json`).  
  - Telemetry for this cycle is recorded in `releases/v10.0.0/focus-telemetry.json`, including:
    - Validation counts and error categories.  
    - Selected energy and runtime metrics for archival workflows.

Validation failures **block archival sealing** until resolved.

---

## 🕰️ Version History

| Version   | Date       | Author           | Summary                                                                                     |
|----------:|------------|------------------|---------------------------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-archive`   | Realigned Q4 2025 archive README with KFM-MDP v11.2.6; added scope, governance metadata, and clarified STAC/DCAT/PROV alignment while keeping data frozen at v10.0.0. |
| v10.0.0   | 2025-11-10 | `@kfm-archive`   | Upgraded to v10 release; updated paths and badges; aligned checksum, ledger, and telemetry references. |
| v9.7.0    | 2025-11-06 | `@kfm-archive`   | Hardened paths and badges; refreshed ISO and FAIR+CARE references.                          |
| v9.6.0    | 2025-11-03 | `@kfm-archive`   | Added governance provenance schema and energy telemetry integration.                        |
| v9.5.0    | 2025-11-02 | `@kfm-governance`| Updated checksum validation and STAC indexing process.                                      |
| v9.3.2    | 2025-10-28 | `@kfm-core`      | Established structured quarterly archival workflow for certified datasets.                  |

---

<div align="center">

📦 **Kansas Frontier Matrix — Q4 2025 Data Archive**  
FAIR+CARE Data Ethics · Provenance Transparency · Sustainable Stewardship  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[📂 Data Index](../README.md) ·  
[⚖ Data Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md) ·  
[📊 FAIR+CARE Reports](../../reports/fair/faircare_summary.json)

</div>
