---
title: "🔐 Kansas Frontier Matrix — Archived Treaty Data Checksums & Integrity Manifest"
path: "data/work/staging/tabular/normalized/treaties/checksums/archive/README.md"
document_type: "Data Integrity · Checksum Archive Specification"
version: "v2.0.0"
last_updated: "2025-10-25"
review_cycle: "Quarterly / Data Integrity & Governance"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v2.0.0/sbom.spdx.json"
manifest_ref: "releases/v2.0.0/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
owners: ["@kfm-data-integrity", "@kfm-architecture"]
approvers: ["@kfm-validation", "@kfm-governance"]
status: "Production · FAIR+CARE+ISO Aligned"
maturity: "Stable"
mcp_version: "MCP-DL v6.3"
tags: ["Data Integrity", "Checksums", "FAIR", "ISO", "Governance", "Archival", "Verification", "Provenance"]
---

<div align="center">

# 🔐 Kansas Frontier Matrix — **Archived Treaty Data Checksums & Integrity Manifest**  
`data/work/staging/tabular/normalized/treaties/checksums/archive/README.md`

**Purpose:** Maintain immutable checksum manifests for **all archived treaty data artifacts**, including AI-generated summaries, validation logs, and metadata.  
This directory provides **verifiable, cryptographically hashed lineage** for every versioned asset in the **Kansas Frontier Matrix (KFM)** data pipeline, ensuring **data integrity**, **traceability**, and **scientific reproducibility**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../docs/architecture/repo-focus.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![ISO 25012](https://img.shields.io/badge/ISO--25012-Data%20Quality%20Model-orange)]()
[![Data Integrity](https://img.shields.io/badge/Integrity-Verified-green)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen)]()

</div>

---

## 🗂️ Directory Layout

```plaintext
checksums/archive/
├── treaties_2025_Q4.sha256       # Primary checksum manifest for Q4 2025 treaties
├── treaties_2025_Q3.sha256       # Previous quarter manifest
├── ai_logs_2025_Q4.sha256        # AI inference & validation log checksum list
├── provenance_chain_2025.sha256  # Provenance hash chain for PROV-O entities
├── metrics_snapshot_2025.json    # Hash statistics (failure/success rate, coverage)
├── archive_index.json            # Machine-readable manifest index of checksum files
└── README.md                     # ← You are here
```

---

## 🧭 Overview

Checksum archives are a **core component** of the KFM data integrity infrastructure.  
They allow for cryptographic verification of every **treaty dataset**, **AI summary**, and **validation log** stored in both **staging** and **archive** repositories.

Checksums are generated and validated under the **MCP-DL Integrity Chain Specification**, ensuring that:
- All data is verifiable across time and environments.
- Artifacts cannot be altered post-validation.
- Provenance relationships remain cryptographically trustworthy.
- Auditors can reconstruct the integrity history of any dataset.

The checksum manifests are used in:
- CI/CD integrity pipelines (`checksum-verify.yml`)
- Governance Ledger verification audits
- FAIR repository synchronization
- STAC/DCAT catalog generation

---

## ⚙️ Checksum Generation Process

```mermaid
flowchart TD
    A[Raw Treaty / Summary Data] --> B[Checksum Generator (sha256sum)]
    B --> C[Manifest Consolidation → treaties_YYYY_QN.sha256]
    C --> D[Integrity Validator CI Job]
    D --> E[Governance Ledger Signature]
    E --> F[Immutable Archive Storage]
```
%% END OF MERMAID %%

---

## 🧩 Manifest Schema

Each `.sha256` file follows the standard `sha256sum` format and is accompanied by a **JSON metadata index** for programmatic validation.

### Example: `treaties_2025_Q4.sha256`

```text
d6a74b8918a9e77c8bfc5a84e5c742fcb79f57ef76d3f923e021d2361e981ebf  data/processed/treaties/KS_TREATY_1867_03_MEDICINE_LODGE.geojson
3fa8f236ce10e2d6cfe71b09b79c43e634a6f3f9f8e4a99e3b497bf6cbb94e8f  data/work/staging/tabular/normalized/treaties/metadata/ai/summaries/KS_TREATY_1867_03_MEDICINE_LODGE.json
f5e933cc49b6a4a5523487328b8237e84fd74f889dfb2b7dfb8f772e12e8e31d  logs/ai/archive/2025/10/KS_TREATY_1867_03_MEDICINE_LODGE.jsonld
```

### Example Metadata (`archive_index.json`)

```json
{
  "version": "v2.0.0",
  "generated_at": "2025-10-25T14:30:00Z",
  "manifest_files": [
    "treaties_2025_Q4.sha256",
    "ai_logs_2025_Q4.sha256",
    "provenance_chain_2025.sha256"
  ],
  "total_files_hashed": 438,
  "hash_algorithm": "SHA-256",
  "validation_job_id": "CI_CHECKSUM_2025-10-25_1430",
  "ledger_ref": "governance/ledger/integrity/2025/10/"
}
```

---

## 🔒 Integrity Verification & Audit

| Process | Frequency | Description | Output |
|----------|------------|--------------|---------|
| **Pre-Commit Verification** | Every push | Automatically runs `make checksums-verify`. | Hash validation report in CI logs. |
| **Quarterly Integrity Audit** | Quarterly | Ethics + Governance Council validates checksum integrity against archives. | Signed audit ledger. |
| **Ledger Registration** | Continuous | Every manifest is signed and stored in `/governance/ledger/integrity/`. | Ledger JSON-LD entry with signature. |
| **Checksum Drift Detection** | Real-time | Monitors diffs between staging and archive manifests. | Alerts in `/telemetry/alerts.json`. |

---

## 🧾 Governance Ledger Crosswalk

Each `.sha256` manifest maps directly to a **ledger entry** recording its approval, checksum, and provenance chain.

### Example Ledger Entry

```json
{
  "@context": "https://www.w3.org/ns/prov#",
  "@id": "urn:kfm:checksum:treaties_2025_Q4",
  "prov:wasGeneratedBy": "make checksums-archive",
  "prov:wasAttributedTo": "@kfm-data-integrity",
  "prov:generatedAtTime": "2025-10-25T14:30:00Z",
  "prov:value": "sha256:e981ebf...31d",
  "prov:qualifiedAssociation": {
    "prov:agent": "@kfm-governance",
    "prov:role": "Auditor"
  }
}
```

This integration guarantees **end-to-end verifiability** across data, AI, and governance layers.

---

## 🧮 CI/CD Validation Workflow

| Workflow | Description | Enforcement |
|-----------|--------------|-------------|
| `checksum-verify.yml` | Compares regenerated hashes with archives. | Fails if mismatch > 0.01%. |
| `ledger-integrity.yml` | Validates that every checksum manifest has a ledger entry. | Required for merge to `main`. |
| `audit-notify.yml` | Sends Slack/Email notification for checksum drift or mismatch. | Runs daily. |
| `stac-sync.yml` | Updates STAC catalog with new verified datasets. | Weekly. |

---

## 🧾 FAIR+CARE and ISO Compliance

| Standard | Application | Reference |
|-----------|--------------|------------|
| **FAIR F1** | Unique identifiers for every dataset hash. | archive_index.json |
| **FAIR A1** | Open checksum format for universal verification. | treaties_*.sha256 |
| **CARE Ethics** | Access controlled checksum logs for sensitive materials. | governance/ledger/integrity/ |
| **ISO 25012** | Enforces data accuracy, traceability, and completeness. | CI/CD audit workflows |
| **ISO 19115** | Geospatial integrity metadata linked via STAC/PROV-O. | provenance_chain_2025.sha256 |

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Notes |
|----------|------|---------|-----------|--------|
| v2.0.0 | 2025-10-25 | @kfm-data-integrity | @kfm-governance | Introduced full FAIR+CARE alignment, CI/CD verification, and provenance mapping. |
| v1.1.0 | 2025-10-24 | @kfm-data-integrity | @kfm-validation | Added ledger integration and quarterly audit schema. |
| v1.0.0 | 2025-10-23 | @kfm-data-integrity | — | Initial directory creation and checksum manifest specification. |

---

<div align="center">

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![ISO 25012](https://img.shields.io/badge/ISO--25012-Data%20Quality%20Model-orange)]()
[![Data Integrity](https://img.shields.io/badge/Integrity-Verified-green)]()
[![Governance Ledger](https://img.shields.io/badge/Ledger-Immutable%20%26%20Audited-yellow)]()

</div>
````

