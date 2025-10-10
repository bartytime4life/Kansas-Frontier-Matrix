<div align="center">

# 🚧 Kansas Frontier Matrix — Staging Directory  
`data/work/staging/`

**Mission:** Provide a **controlled staging environment** for data artifacts awaiting validation,  
integration, or transfer between ETL processing and finalized storage —  
ensuring data integrity and traceability within the Kansas Frontier Matrix (KFM) workflows.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/staging/` directory functions as a **temporary holding zone**  
for datasets that have been processed but not yet validated, cataloged, or published.  

Typical staged data includes:
- Outputs pending **checksum validation** or **STAC metadata linkage**  
- Datasets awaiting **manual QA/QC review** or **peer verification**  
- Assets queued for **integration into `data/processed/`**  
- Files transferring between ETL stages or local/remote storage  

All contents are **transient**, **excluded from Git**, and **safe to remove** once promoted.

---

## 🗂️ Directory Layout

```bash
data/work/staging/
├── README.md
├── terrain/             # Elevation datasets awaiting validation
├── hydrology/           # Streams, floods, aquifers awaiting checksums
├── landcover/           # Land cover or vegetation outputs under review
├── climate/             # Temperature & precipitation layers pending QA
├── hazards/             # Storm, wildfire, drought data awaiting validation
├── tabular/             # Tabular or statistical outputs under schema testing
└── text/                # OCR and document assets pending metadata completion
````

> **Note:** This mirrors the `data/processed/` hierarchy,
> simplifying final promotion once validation is complete.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                     |
| :---------------------- | :-------------------------------------------------------------- |
| **Temporary Storage**   | Files remain until QA and validation are complete.              |
| **Controlled Transfer** | Only validated datasets move to `data/processed/`.              |
| **No Direct Edits**     | Manual edits are prohibited; pipelines manage updates.          |
| **Checksum Validation** | Run `make validate` or pipeline validation before moving files. |
| **Version Control**     | `.gitignore` protects this folder from accidental commits.      |

---

## ⚙️ Typical Use Cases

| Task                        | Example                                                                   |
| :-------------------------- | :------------------------------------------------------------------------ |
| **Checksum Review**         | Compare SHA-256 hashes before dataset publication.                        |
| **STAC Validation**         | Test metadata structure before catalog ingestion.                         |
| **Schema Conformance**      | Validate JSON or CSV schema alignment for tabular files.                  |
| **Raster QA**               | Inspect COG or GeoTIFF output for completeness and coordinate alignment.  |
| **Cross-Pipeline Transfer** | Hold intermediate assets between ETL domains (e.g., terrain → hydrology). |

---

## 🧹 Cleanup Policy

Staged files are deleted or moved automatically after validation and integration.

**Makefile target**

```bash
make clean-staging
```

**Manual cleanup**

```bash
rm -rf data/work/staging/*
```

**Promotion Example**

```bash
mv data/work/staging/terrain/ks_1m_dem_2020.tif data/processed/terrain/
```

> **Tip:** Always run `make validate` to confirm checksums and STAC compliance before promotion.

---

## 🧩 Integration with Pipelines

| Linked Component                      | Function                                                      |
| :------------------------------------ | :------------------------------------------------------------ |
| `src/pipelines/*`                     | Writes interim outputs to `staging/` for post-ETL validation. |
| `data/checksums/`                     | Validation scripts compare hashes prior to promotion.         |
| `data/processed/`                     | Destination for verified and cataloged datasets.              |
| `.github/workflows/stac-validate.yml` | Tests STAC structure using staged files in CI/CD.             |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | README defines staging role, lifecycle, and promotion policies.        |
| **Reproducibility**     | Staged data can be regenerated deterministically from ETL pipelines.   |
| **Open Standards**      | Uses COG, GeoJSON, CSV, and JSON formats for compatibility.            |
| **Provenance**          | Each staged dataset linked to ETL step logs and checksum records.      |
| **Auditability**        | Promotion actions and validation logs maintain clear lineage tracking. |

---

## 📎 Related Directories

| Path              | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `data/work/tmp/`  | Temporary workspace for ETL intermediates.           |
| `data/processed/` | Finalized datasets ready for catalog publication.    |
| `data/checksums/` | Integrity verification and reproducibility tracking. |
| `data/stac/`      | STAC 1.0.0 catalog for validated datasets.           |

---

## 📅 Version History

| Version | Date       | Summary                                                             |
| :------ | :--------- | :------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial staging directory documentation created.                    |
| v1.0.1  | 2025-10-09 | Added metadata, JSON-LD schema, badges, and MCP compliance details. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Data Awaits Its Final Form.”*
📍 [`data/work/staging/`](.) · Controlled environment for dataset validation and integration.

</div>
