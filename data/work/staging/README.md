<div align="center">

# 🚧 Kansas Frontier Matrix — Staging Directory  
`data/work/staging/`

**Mission:** Provide a **controlled staging environment** for data artifacts awaiting validation,  
integration, or transfer between ETL processing and finalized storage —  
ensuring data integrity and traceability within the Kansas Frontier Matrix (KFM) workflows.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/staging/` directory functions as a **temporary holding zone**  
for datasets that have been processed but not yet verified, cataloged, or published.  

Staged data typically represents:
- Outputs waiting for **checksum validation** or **STAC metadata linking**  
- Datasets pending **manual QA/QC or peer verification**  
- Assets awaiting **integration** into `data/processed/`  
- Files being transferred between pipelines or from local to remote storage  

All data in this directory is **transient**, **excluded from version control**, and **safe to delete** once finalized.

---

## 🗂️ Directory Layout

```bash
data/work/staging/
├── README.md
├── terrain/             # Pending elevation datasets before verification
├── hydrology/           # Rivers, floods, aquifers awaiting checksums
├── landcover/           # Land cover or vegetation layers awaiting validation
├── climate/             # Temperature and precipitation data under review
├── hazards/             # Storm, wildfire, drought outputs pending review
├── tabular/             # Statistical tables awaiting schema validation
└── text/                # Document and OCR assets awaiting final metadata
````

> **Note:** The structure mirrors the primary `data/processed/` hierarchy,
> enabling seamless transition once data are verified and approved.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                               |
| :---------------------- | :------------------------------------------------------------------------ |
| **Temporary Storage**   | Files remain here until validation is complete.                           |
| **Controlled Transfer** | Only validated data are promoted to `data/processed/`.                    |
| **No Direct Edits**     | Do not modify staged files manually; changes occur via ETL or QA scripts. |
| **Checksum Validation** | Run `make validate` or pipeline validation before moving files.           |
| **Version Control**     | Staging is `.gitignore`-protected to avoid committing transient data.     |

---

## ⚙️ Typical Use Cases

| Task                        | Example                                                                         |
| :-------------------------- | :------------------------------------------------------------------------------ |
| **Checksum Review**         | Compare generated SHA-256 hashes before final publication.                      |
| **STAC Validation**         | Test metadata structure prior to pushing to catalog.                            |
| **Schema Conformance**      | Validate JSON or CSV schema alignment for tabular data.                         |
| **Raster QA**               | Inspect COG or GeoTIFF outputs before promotion to processed.                   |
| **Cross-Pipeline Transfer** | Temporarily store files passed between ETL domains (e.g., terrain → hydrology). |

---

## 🧹 Cleanup Policy

After successful validation or integration, staged files are automatically moved or removed.

**Makefile target:**

```bash
make clean-staging
```

**Manual cleanup:**

```bash
rm -rf data/work/staging/*
```

**Promotion Example:**

```bash
mv data/work/staging/terrain/ks_1m_dem_2018_2020.tif data/processed/terrain/
```

> **Tip:** Use `make validate` before promotion to ensure checksum and STAC metadata are aligned.

---

## 🧩 Integration with KFM Pipelines

| Linked Component                      | Function                                                       |
| :------------------------------------ | :------------------------------------------------------------- |
| `src/pipelines/*`                     | Writes intermediate outputs to `staging/` prior to validation. |
| `data/checksums/`                     | Validation scripts verify hashes before promotion.             |
| `data/processed/`                     | Final home for all validated and cataloged datasets.           |
| `.github/workflows/stac-validate.yml` | Uses staged files for STAC structure testing in CI/CD.         |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | README defines staging purpose, policy, and promotion process.         |
| **Reproducibility**     | All staged datasets can be reprocessed deterministically.              |
| **Open Standards**      | Uses standardized formats (COG, GeoJSON, CSV, JSON).                   |
| **Provenance**          | Files include temporary logs and checksums linking them to ETL stages. |
| **Auditability**        | Promotion logs ensure traceable validation and data lineage.           |

---

## 📎 Related Directories

| Path              | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `data/work/tmp/`  | Transient workspace for raw ETL intermediates.       |
| `data/processed/` | Finalized, validated datasets ready for publication. |
| `data/checksums/` | Integrity verification and reproducibility tracking. |
| `data/stac/`      | STAC 1.0.0 catalog of validated datasets.            |

---

## 📅 Version History

| Version | Date       | Summary                                                                       |
| :------ | :--------- | :---------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial staging directory documentation (validation and promotion workflows). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Data Awaits Its Final Form.”*
📍 [`data/work/staging/`](.) · Controlled environment for dataset validation and integration.

</div>
