---
title: "🔐 Kansas Frontier Matrix — Data Checksums & Integrity Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/checksums/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-checksums-v10.json"
governance_ref: "../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
---

<div align="center">

# 🔐 Kansas Frontier Matrix — **Data Checksums & Integrity Registry**
`data/checksums/README.md`

**Purpose:**  
Define and operate the **checksum verification system**, integrity tracking, and provenance linkage for all datasets across the **Kansas Frontier Matrix (KFM)**.  
Guarantee that every artifact—from ingestion to public release—is cryptographically verified and immutably registered in the **Governance Ledger**.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../LICENSE)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Integrity%20Certified-gold.svg)](../../docs/standards/faircare-validation.md)
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Checksum Integrity Registry** maintains SHA-256 verification manifests for datasets, catalogs, and release artifacts.  
Each checksum serves as a **verifiable fingerprint** binding a dataset’s digital identity to governance, provenance, and FAIR+CARE compliance records.

**Checksums are used to:**
- Authenticate dataset and release integrity.  
- Detect data drift or unauthorized modification.  
- Cross-link entries in the **Governance Ledger** and **STAC/DCAT** catalogs.  
- Enable public verification via command-line or API.

---

## 🧭 System Architecture

```mermaid
flowchart TD
    A["ETL & Validation Pipelines"] --> B["Checksum Generator (SHA-256)"]
    B --> C["Integrity Registry (data/checksums/manifest.json)"]
    C --> D["Governance Ledger (data/reports/audit/data_provenance_ledger.json)"]
    D --> E["Public Release Verification (releases/v10.0.0)"]
```

### Description
1. **Generation:** Pipelines compute checksums after each run or artifact mutation.  
2. **Registration:** Results are written to `manifest.json` and linked to release manifests.  
3. **Verification:** The Governance Ledger cross-audits entries against SBOM hashes.  
4. **Publication:** Each release provides a verified checksum set for reproducibility.

---

## 🗂️ Directory Layout

```plaintext
data/checksums/
├── README.md                    # This file — checksum registry documentation
├── manifest.json                # Master SHA-256 manifest (all datasets)
├── processed_datasets.json      # Checksums for FAIR+CARE-certified outputs
├── staging_datasets.json        # Checksums for schema-aligned staging artifacts
├── work_datasets.json           # Checksums for ETL/TMP workspaces
└── release_hashes.json          # Checksums mapped to SBOM + manifest.zip entries
```

---

## ⚙️ Manifest Structure

Each manifest lists **dataset identifiers**, **checksums**, and **metadata references**.

```json
{
  "version": "v10.0.0",
  "generated_on": "2025-11-10T19:25:00Z",
  "hash_algorithm": "SHA-256",
  "datasets": [
    {
      "id": "hazards_processed_v10.0.0",
      "path": "data/processed/hazards/hazards_composite_v10.0.0.geojson",
      "checksum": "sha256-2f1e3b8c97df84b5d2c3e39bbd95b9e8d12b64ad38a62400f745d68ec6d1b75e",
      "fairstatus": "certified",
      "governance_ref": "data/reports/audit/data_provenance_ledger.json"
    },
    {
      "id": "climate_staging_v10.0.0",
      "path": "data/work/staging/climate/climate_aggregate_v10.0.0.parquet",
      "checksum": "sha256-a8373fa4d12d49be5f5f2178a91d79981b1d28b947f05eaa52e9e7e8d2cfadcd",
      "fairstatus": "pending"
    }
  ]
}
```

---

## 🧩 FAIR+CARE Integrity Governance

| Principle | Implementation | Verified By |
|---|---|---|
| **Findable** | Checksums indexed in catalogs and SBOM manifests. | `@kfm-data` |
| **Accessible** | JSON files published under CC-BY 4.0 for public verification. | `@kfm-accessibility` |
| **Interoperable** | JSON-LD-ready structure compatible with STAC/DCAT and SPDX. | `@kfm-architecture` |
| **Reusable** | Immutable, versioned checksum logs with ledger links. | `@kfm-governance` |
| **Collective Benefit** | Guarantees public trust in integrity of open data. | `@faircare-council` |
| **Authority to Control** | FAIR+CARE Council certifies checksum workflows. | `@kfm-governance` |
| **Responsibility** | Telemetry-backed coverage and periodic re-verification. | `@kfm-security` |
| **Ethics** | Integrity validation prevents tampering and inequitable access. | `@kfm-ethics` |

---

## 🧮 Validation Workflows

| Workflow | Description | Output |
|---|---|---|
| `checksum-verify.yml` | Generates & verifies SHA-256 hashes for datasets. | `manifest.json` |
| `faircare-validate.yml` | Aligns checksum process with FAIR+CARE ethics. | `data/reports/fair/faircare_summary.json` |
| `governance-ledger.yml` | Syncs hashes with provenance ledger. | `data/reports/audit/data_provenance_ledger.json` |
| `sbom-validate.yml` | Confirms checksums match SPDX SBOM entries. | `releases/v10.0.0/sbom.spdx.json` |

> All workflows are automated in `.github/workflows/`.

---

## 📊 Example CLI Verification

```bash
# Compute and compare a file checksum
sha256sum data/processed/hazards/hazards_composite_v10.0.0.geojson

# Query a specific dataset checksum from the manifest
jq '.datasets[] | select(.id=="hazards_processed_v10.0.0")' data/checksums/manifest.json
```

---

## 🌱 Sustainability & Provenance Metrics

| Metric | Target | Verified By |
|---|---|---|
| Checksum Coverage | 100% of released datasets | `@kfm-validation` |
| Governance Ledger Sync | 100% hash alignment | `@kfm-governance` |
| SBOM Alignment | ≥ 99.9% parity | `@kfm-architecture` |
| Energy Efficiency | ≤ 10 Wh per batch | `@kfm-sustainability` |
| FAIR+CARE Compliance | Certified | `@faircare-council` |

**Telemetry:** `../../releases/v10.0.0/focus-telemetry.json`

---

## 🗂️ Directory Conventions

- **File naming:** `<domain>_<layer>_v<semver>.<ext>` (e.g., `hazards_composite_v10.0.0.geojson`).  
- **Hash field:** `checksum` must be prefixed with `sha256-`.  
- **Immutability:** Once published under a release tag, entries are append-only; corrections are new records with `supersedes` pointers in the ledger.

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Data Checksums & Integrity Registry (v10.0.0).
Checksum governance, cryptographic verification, and FAIR+CARE-integrated integrity processes for KFM releases.
Ensures dataset immutability, reproducibility, and public verifiability across versions.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | `@kfm-data` | Upgraded registry to v10; bumped SBOM/manifest/telemetry refs; added JSON-LD/SPDX guidance and CLI examples. |
| v9.7.0  | 2025-11-06 | `@kfm-data` | Initial registry README; governance mapping, manifest example, and telemetry metrics. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Data Integrity × FAIR+CARE Trust × Sustainable Provenance*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Data Architecture](../README.md) · [Governance Charter](../../docs/standards/governance/DATA-GOVERNANCE.md) · [FAIR+CARE Summary](../../data/reports/fair/data_care_assessment.json)

</div>
