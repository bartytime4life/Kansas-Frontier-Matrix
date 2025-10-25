---
title: "🧩 Kansas Frontier Matrix — Staging TMP Layer (Temporary Normalized Workspace)"
path: "data/work/staging/tabular/normalized/tmp/README.md"
document_type: "Data Staging · Temporary Normalization Workspace Specification"
version: "v2.0.0"
last_updated: "2025-10-25"
review_cycle: "Continuous / Daily ETL Cleanups"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v2.0.0/sbom.spdx.json"
manifest_ref: "releases/v2.0.0/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
owners: ["@kfm-data-engineering", "@kfm-architecture"]
approvers: ["@kfm-validation", "@kfm-qa", "@kfm-governance"]
status: "Operational · MCP-DL v6.3 Aligned"
maturity: "Stable"
mcp_version: "MCP-DL v6.3"
tags: ["Staging", "TMP", "Normalization", "ETL", "Data Pipeline", "Reproducibility", "Integrity", "Governance"]
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **Staging TMP Layer (Temporary Normalized Workspace)**  
`data/work/staging/tabular/normalized/tmp/README.md`

**Purpose:** Serve as the **ephemeral, sandbox-level workspace** for pre-validation, pre-ingestion, and intermediate ETL operations before finalized data is promoted to the main normalized tabular datasets within the **Kansas Frontier Matrix (KFM)**.  
This layer enables **safe, auditable, and reversible data experimentation** within the MCP-DL documentation-first architecture.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../docs/architecture/repo-focus.md)
[![STAC Validate](https://img.shields.io/badge/STAC-Validated-success)]()
[![ISO 25012](https://img.shields.io/badge/ISO--25012-Data%20Quality%20Model-orange)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen)]()
[![Status: Active](https://img.shields.io/badge/Status-Active-green)]()

</div>

---

## 🗂️ Directory Layout

```plaintext
tmp/
├── etl_runs/                   # Temporary logs from running ETL jobs (auto-purged weekly)
├── validation_scratch/         # Intermediate schema validation outputs
├── normalization_buffer/       # Cached normalized tabular data prior to commit
├── conflict_resolution/        # Folder for auto/manual resolution of merge or schema conflicts
├── provenance_staging/         # Temporary provenance JSON-LD entities awaiting ledger registration
├── audit_sandbox/              # Validation audit scratchpad for data reviewers
├── README.md                   # ← You are here
└── .gitkeep                    # Ensures directory retention in Git
```

---

## 🧭 Overview

The **TMP Layer** is a sandbox zone used during active **Extract-Transform-Load (ETL)** operations.  
It allows data engineers and validation teams to execute normalization workflows, perform schema transformations, and test data mappings **without impacting the main normalized tabular datasets** under production control.

Temporary data stored here are:
- **Ephemeral:** Automatically cleaned and versioned nightly.  
- **Traceable:** Tagged with source and operation metadata.  
- **Reproducible:** Every operation logged with SHA-256 checksum and script reference.  
- **Controlled:** Accessible only through official ETL and validation workflows (`make data`, `make validate`).

---

## ⚙️ Data Lifecycle

```mermaid
flowchart TD
    A[Raw Source Data] --> B[ETL Pipeline (src/pipelines/normalize.py)]
    B --> C[Staging TMP Layer (data/work/staging/tabular/normalized/tmp)]
    C --> D[Schema Validation + Provenance Audit]
    D --> E[Commit to Normalized Tabular Dataset]
    E --> F[Checksums + Governance Ledger Update]
    F --> G[Archive TMP Logs & Cleanup (make clean-tmp)]
```
%% END OF MERMAID %%

---

## 🧩 Workflow Integration

### 1️⃣ ETL Buffering  
During normalization, incoming data (e.g., treaty CSVs, OCR text, metadata YAML) passes through TMP as a **pre-validated buffer**:
- Transforms raw fields to normalized schema (dates, entity IDs, relationships).
- Stores schema conformity reports in `/validation_scratch/`.
- Generates initial STAC-compatible metadata files.

### 2️⃣ Validation Sandbox  
AI-generated or human-curated tabular summaries (e.g., treaty metadata or signatory lists) are validated here before being merged into main repositories:
- Semantic validation via `make stac-validate`.
- Ontological alignment using CIDOC CRM/OWL-Time mapping.
- FAIR+CARE compliance audit before publication.

### 3️⃣ Conflict Resolution  
If two ETL processes attempt concurrent updates to the same normalized dataset, TMP automatically isolates and logs conflicts under `/conflict_resolution/`:
- Each conflict is hashed, compared, and documented.
- Human reviewers assess discrepancies through `make tmp-diff`.
- Only reconciled results advance to `/data/work/staging/tabular/normalized/treaties/`.

---

## 🧮 Metadata & Provenance Rules

Each TMP file must include:
- **TMP ID** (UUID): `tmp_{timestamp}_{process_id}`
- **Provenance JSON-LD** (recording ETL step and data lineage)
- **Checksum Manifest** (auto-generated by `make checksums-tmp`)
- **Schema Reference:** Links to validation schema (STAC/DCAT/CIDOC CRM)
- **Retention Flag:** `ttl_days: <integer>` (time-to-live before purge)

Example TMP provenance stub:

```json
{
  "@context": "https://www.w3.org/ns/prov#",
  "@id": "urn:kfm:tmp:2025-10-25T13:33:00Z:normalize_treaty_001",
  "prov:wasGeneratedBy": "normalize_treaty_data.py",
  "prov:used": ["data/raw/treaties/1867_medicine_lodge.csv"],
  "prov:wasAttributedTo": "@kfm-data-engineering",
  "prov:generatedAtTime": "2025-10-25T13:33:00Z",
  "prov:value": "Normalized field schema version v6.3",
  "prov:invalidatedAtTime": "2025-10-26T00:00:00Z"
}
```

---

## 🔒 Governance & Cleanup Policy

| Policy | Enforcement | Description |
|--------|--------------|-------------|
| **Automatic Cleanup** | `make clean-tmp` | Deletes all TMP files older than 24 hours unless marked with retention flag. |
| **Integrity Verification** | `make checksums-verify` | Runs checksum comparison across TMP and normalized files. |
| **Ledger Linking** | `make tmp-register-ledger` | Registers provenance JSON-LD entities to Governance Ledger. |
| **Audit Review** | Weekly via CI (`tmp-audit.yml`) | Samples TMP logs for validation and compliance with FAIR+CARE. |
| **Human Override** | Admin or @kfm-validation | Allows retention extension for ongoing analysis. |

TMP cleanup runs nightly via automated CI/CD:
- Logs are exported to `/logs/etl/tmp_cleanup.log`.  
- Each deletion is hashed, timestamped, and archived in `/checksums/archive/tmp/`.

---

## 📈 Data Validation Telemetry

Metrics logged in `telemetry/tmp_validation_metrics.json`:

| Metric | Description | Target |
|--------|--------------|---------|
| Schema Validation Rate | % of TMP files passing validation schema | ≥ 95% |
| Provenance Coverage | % of TMP records with JSON-LD provenance | 100% |
| STAC Compliance | % of temporary STAC items generated correctly | ≥ 98% |
| Cleanup Efficiency | % of expired TMP files auto-purged | 100% |
| Integrity Drift | Detected mismatches vs normalized data | ≤ 1% |

---

## 🧾 FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Findable** | TMP files indexed by UUID in `/telemetry/tmp_index.json`. |
| **Accessible** | Temporary open access within internal ETL environment. |
| **Interoperable** | Follows standardized schemas and JSON-LD. |
| **Reusable** | Retention-limited but reproducible via provenance logs. |
| **CARE (Ethics)** | TMP staging protects restricted Indigenous datasets until review. |

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Notes |
|----------|------|---------|-----------|--------|
| v2.0.0 | 2025-10-25 | @kfm-data-engineering | @kfm-validation | Added retention metadata, cleanup automation, and CIDOC/FAIR integration. |
| v1.1.0 | 2025-10-24 | @kfm-data-engineering | @kfm-governance | Introduced checksum and provenance tracking for TMP files. |
| v1.0.0 | 2025-10-23 | @kfm-data-engineering | — | Initial creation of TMP staging workspace documentation. |

---

<div align="center">

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]()
[![STAC Validated](https://img.shields.io/badge/STAC-Validated-success)]()
[![ISO 25012](https://img.shields.io/badge/ISO--25012-Data%20Quality%20Model-orange)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![Governance Ledger](https://img.shields.io/badge/Ledger-Registered-yellow)]()

</div>
