---
title: "📦 Kansas Frontier Matrix — Data Tools & Validation Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/data/README.md"
version: "v9.3.3"
last_updated: "2025-11-02"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.3.3/sbom.spdx.json"
manifest_ref: "../../../releases/v9.3.3/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
owners: ["@kfm-data", "@kfm-etl", "@kfm-validation", "@kfm-governance"]
status: "Stable"
maturity: "Production"
tags: ["data-tools", "etl", "validation", "stac", "checksum", "schema", "governance"]
alignment:
  - MCP-DL v6.4.3
  - FAIR+CARE
  - ISO 19115 Metadata Standards
  - OGC STAC / DCAT 3.0
preservation_policy:
  retention: "data validation logs retained 10 years · manifests permanent"
  checksum_algorithm: "SHA-256"
---

<div align="center">

# 📦 Kansas Frontier Matrix — **Data Tools & Validation Utilities**
`tools/data/README.md`

**Purpose:** Documents the command-line and automation tools used to validate, transform, and manage data in the Kansas Frontier Matrix.  
Ensures every dataset meets FAIR+CARE, STAC, and governance requirements before integration into the knowledge graph.

[![🧮 Data Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/data-validate.yml/badge.svg)](../../../.github/workflows/data-validate.yml)  
[![🌍 FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../../docs/standards/faircare-validation.md)  
[![🔐 Provenance Audited](https://img.shields.io/badge/Data-Governance%20Ledger%20Linked-blueviolet)](../../../reports/audit/governance-ledger.json)  
[![📘 Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The **Data Tools Suite** supports KFM’s ETL pipelines and validation workflows.  
These tools enforce quality control, schema consistency, and governance provenance for every dataset ingested, transformed, or published.  
All data operations are logged and certified under the **Immutable Governance Chain**, ensuring transparency and traceability.

**Core Capabilities:**
- 🧩 Validate **STAC**, **DCAT**, and **FAIR+CARE** metadata  
- 🧱 Automate data **extraction**, **transformation**, and **loading (ETL)**  
- 🔍 Verify **checksums**, **schemas**, and **licenses**  
- ⚙️ Normalize geospatial formats (GeoJSON, GeoTIFF, NetCDF)  
- 🧾 Export validation results for audits and governance ledgers  

---

## 🗂️ Directory Layout

```plaintext
tools/data/
├── README.md               # This file — documentation and governance overview
│
├── validate_stac.py        # Validates STAC JSON against schema and OGC standards
├── checksum_verify.py      # Performs SHA-256 checksum validation for all datasets
├── etl_runner.py           # Orchestrates ETL ingestion from external sources into KFM data layers
├── transform_normalize.py  # Converts raw datasets into standardized open formats (GeoJSON, CSV, NetCDF)
└── schema_validate.py      # Checks datasets for compliance with declared schema contracts
```

**File Descriptions:**

- **`validate_stac.py`** — Confirms that all STAC items and collections follow OGC-compliant JSON schemas.  
  Generates reports in `reports/self-validation/stac-validation-summary.json`.

- **`checksum_verify.py`** — Verifies file integrity by calculating and comparing SHA-256 checksums against manifests.  
  Ensures no corruption or unauthorized alteration of data.

- **`etl_runner.py`** — Automates dataset ingestion, applying transformation, enrichment, and metadata embedding via ETL pipelines.

- **`transform_normalize.py`** — Standardizes incoming data to FAIR+CARE-compliant formats.  
  Supports GeoJSON, CSV, NetCDF, and Cloud-Optimized GeoTIFF (COG).

- **`schema_validate.py`** — Cross-checks datasets against KFM’s schema definitions (`docs/contracts/data-contract-v3.json`).

---

## ⚙️ Example Usage

### ✅ Validate STAC Metadata
```bash
python tools/data/validate_stac.py --input data/stac/catalog.json --schema schemas/stac/item-spec.json
```

### 🔍 Checksum Verification
```bash
python tools/data/checksum_verify.py --input data/processed/ --manifest releases/v9.3.3/manifest.zip
```

### 🧱 Execute ETL Workflow
```bash
python tools/data/etl_runner.py --source data/raw/ --target data/processed/ --pipeline configs/etl_config.yml
```

### ⚙️ Transform & Normalize Data
```bash
python tools/data/transform_normalize.py --input data/raw/hydro.json --output data/processed/hydro.geojson
```

### 🧩 Schema Validation
```bash
python tools/data/schema_validate.py --input data/processed/ --contract docs/contracts/data-contract-v3.json
```

---

## 🧠 Governance & FAIR+CARE Integration

Each tool is linked to the **Immutable Governance Ledger** to ensure consistent traceability across datasets.

| Workflow | Tool | Output |
|-----------|------|---------|
| STAC Validation | `validate_stac.py` | `reports/self-validation/stac-validation-summary.json` |
| Checksum Verification | `checksum_verify.py` | `reports/audit/data-integrity.json` |
| ETL Execution | `etl_runner.py` | `reports/audit/etl-run-log.json` |
| Data Normalization | `transform_normalize.py` | `reports/audit/data-normalization.json` |
| Schema Compliance | `schema_validate.py` | `reports/audit/schema-validation.json` |

**Governance Chain Artifacts:**
```
reports/audit/governance-ledger.json
reports/fair/data-validation-summary.json
releases/v9.3.3/manifest.zip
```

---

## 🧩 FAIR+CARE Validation Criteria

These tools enforce compliance with FAIR+CARE principles through automated evaluation:

| Principle | Implementation | Validation |
|------------|----------------|-------------|
| **Findable** | Indexed STAC catalogs with dataset UUIDs | `validate_stac.py` |
| **Accessible** | Public data with open API endpoints | `etl_runner.py` |
| **Interoperable** | DCAT, GeoJSON, and COG formats | `transform_normalize.py` |
| **Reusable** | License and attribution metadata verified | `checksum_verify.py` |
| **Collective Benefit (CARE)** | Ethics and stewardship flags in dataset metadata | `schema_validate.py` |

---

## 🛡️ Security & Provenance

- **Checksums:** All datasets validated against SHA-256 digests stored in manifest files.  
- **Provenance:** Each data transformation appends metadata for audit tracking (creator, date, checksum).  
- **License Verification:** Automated scans confirm public-domain or CC-BY 4.0 compliance.  
- **Immutable Logs:** Validation reports timestamped and hashed before release inclusion.

Reports are stored under:
```
reports/audit/
reports/self-validation/
reports/fair/
```

---

## 🧾 Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.3.3 | 2025-11-02 | @kfm-data | Added schema validation and automated STAC/DCAT compliance reporting. |
| v9.3.2 | 2025-10-30 | @kfm-etl | Enhanced ETL normalization with GeoTIFF and NetCDF support. |
| v9.3.1 | 2025-10-27 | @bartytime4life | Integrated checksum verification and FAIR+CARE audit hooks. |
| v9.3.0 | 2025-10-25 | @kfm-governance | Created base data toolset under MCP-DL v6.4.3 for reproducible data pipelines. |

---

<div align="center">

**Kansas Frontier Matrix — Immutable Data Validation Framework**  
*“Every dataset verified. Every schema enforced. Every byte accounted.”* 🔗  
📍 `tools/data/README.md` — FAIR+CARE-aligned data management and validation tool documentation.

</div>
