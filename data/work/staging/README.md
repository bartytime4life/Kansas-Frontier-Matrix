<div align="center">

# 🚧 Kansas Frontier Matrix — **Staging Directory**  
`data/work/staging/`

**Mission:** Maintain a **controlled staging environment** for data artifacts pending validation,  
integration, and transfer between ETL processing and finalized publication — ensuring **integrity**,  
**reproducibility**, and **traceability** within the **Kansas Frontier Matrix (KFM)** data system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Staging Directory (data/work/staging/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-architecture"]
tags: ["staging","etl","validation","qa","checksum","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - STAC 1.0.0 (Spatiotemporal Asset Catalog)
  - FAIR Principles (Data Curation & Transparency)
---
```

---

## 📚 Overview

The `data/work/staging/` directory serves as a **transitional environment** for  
datasets that have completed ETL processing but await **validation**, **checksum verification**,  
and **STAC metadata linkage** before integration into `data/processed/`.

It ensures that all data undergo **structured QA/QC review** and lineage verification  
before being promoted to permanent storage or publication.

### Typical staged artifacts include:

- Datasets pending **checksum and validation verification**  
- Outputs queued for **manual QA review** or **peer inspection**  
- Files under **schema validation or metadata linkage testing**  
- Temporary storage during **cross-domain data integration** (e.g., terrain → hydrology)

All contents are **temporary**, **non-versioned**, and fully **regenerable** from upstream ETL pipelines.

---

## 🗂️ Directory Layout

```bash
data/work/staging/
├── README.md
├── terrain/             # Elevation datasets awaiting validation
├── hydrology/           # Stream, aquifer, and flood models pending checksums
├── landcover/           # Land cover or vegetation layers under review
├── climate/             # Climate rasters and time-series awaiting QA
├── hazards/             # Storm, fire, and drought datasets in validation
├── tabular/             # Tabular or statistical outputs under schema testing
└── text/                # OCR and document artifacts awaiting metadata review
```

> **Note:** Folder hierarchy mirrors `data/processed/` for seamless promotion after validation.

---

## ⚙️ Usage Guidelines

| Policy                  | Description                                                                 |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Temporary Storage**   | Datasets remain here until validation and QA are completed.                 |
| **Controlled Transfer** | Only validated and checksum-verified data move to `data/processed/`.        |
| **Automated Governance**| All modifications are pipeline-driven; manual edits are prohibited.         |
| **Checksum Verification** | Run `make validate` or equivalent before promotion to processed storage.  |
| **Version Safety**      | `.gitignore` prevents staging files from being committed inadvertently.     |

---

## 🧩 Typical Use Cases

| Task                        | Example Use Case                                                   |
| :-------------------------- | :---------------------------------------------------------------- |
| **Checksum Review**         | Verify SHA-256 integrity prior to publication.                    |
| **STAC Validation**         | Confirm metadata alignment before adding to the global catalog.   |
| **Schema Conformance**      | Run JSON or CSV schema validation before merging tables.          |
| **Raster QA**               | Inspect GeoTIFF or COG alignment and completeness.                |
| **Cross-Pipeline Exchange** | Hold outputs between ETL domains (e.g., terrain → hydrology).     |

---

## 🧰 Workflow Integration

The staging directory is fully integrated into **KFM’s ETL pipelines and CI/CD workflows**.

| Linked Component                      | Function                                                     |
| :------------------------------------ | :----------------------------------------------------------- |
| `src/pipelines/*`                     | Writes intermediate validated data to `staging/`.            |
| `data/checksums/`                     | Compares hashes before data promotion.                       |
| `data/processed/`                     | Receives validated and cataloged datasets.                   |
| `.github/workflows/stac-validate.yml` | Performs CI-based metadata and schema checks on staged data. |

**Promotion Command Example**

```bash
mv data/work/staging/terrain/ks_1m_dem_2020.tif data/processed/terrain/
```

> ✅ Always validate before promotion using `make validate` or STAC validation workflows.

---

## 🧹 Cleanup Policy

The staging area is cleared automatically upon dataset promotion or via manual cleanup.

**Automated Cleanup**

```bash
make clean-staging
```

**Manual Cleanup**

```bash
rm -rf data/work/staging/*
```

---

## 🔒 Governance & Validation Rules

| Rule                   | Implementation                                                                 |
| :--------------------- | :------------------------------------------------------------------------------ |
| **Access Control**     | Pipeline-managed only; restricted manual changes.                              |
| **Retention Duration** | Files persist until checksums and QA tasks complete.                           |
| **Audit Trail**        | Logs capture all dataset promotions and validation events.                      |
| **Format Policy**      | Open standards enforced — GeoTIFF, GeoJSON, CSV, NetCDF, JSON.                 |
| **Traceability**       | STAC metadata ensures reproducible lineage for every staged artifact.          |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README defines staging purpose, hierarchy, and lifecycle.                   |
| **Reproducibility**     | Staged artifacts regenerate deterministically via ETL workflows.            |
| **Open Standards**      | Uses COG, GeoJSON, CSV, JSON, and NetCDF for compatibility.                 |
| **Provenance**          | Checksum manifests and STAC records link back to pipeline origins.          |
| **Auditability**        | Promotion and validation actions logged in CI/CD workflows.                 |

---

## 🧩 Maintenance Recommendations

1. **Validate Before Promotion:** Always run `make validate` to confirm checksums and metadata.  
2. **Enforce Automation:** Avoid manual moves; use pipeline automation for consistency.  
3. **Track Provenance:** Ensure lineage links between `staging/` and `processed/` datasets.  
4. **Monitor Disk Usage:** Limit staging capacity to active ETL cycles.  
5. **Clean Frequently:** Run `make clean-staging` to prevent data drift or accumulation.  

---

## 📎 Related Directories

| Path              | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `data/work/tmp/`  | Temporary workspace for ETL intermediates.           |
| `data/processed/` | Final validated datasets ready for publication.      |
| `data/checksums/` | Integrity verification manifests for datasets.       |
| `data/stac/`      | STAC catalog for globally discoverable assets.       |

---

## 📅 Version History

| Version | Date       | Summary                                                            |
| :------ | :--------- | :----------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial staging directory documentation created.                 |
| **v1.2.0** | 2025-10-16 | Aligned with MCP-DL v6.2, FAIR principles, and CI/CD governance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Data Awaits Its Final Form.”*  
📍 [`data/work/staging/`](.) · Controlled environment for dataset validation and integration.

</div>
