<div align="center">

# 🌾 Kansas Frontier Matrix — Land Cover Checksums  
`data/processed/checksums/landcover/`

**Mission:** Verify, preserve, and document the **integrity and reproducibility**  
of all processed land cover datasets using SHA-256 checksums — ensuring data consistency, transparency, and auditability  
across the Kansas Frontier Matrix (KFM) spatiotemporal knowledge system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **SHA-256 checksum files (`.sha256`)** for all processed **land cover datasets**  
within Kansas Frontier Matrix.  

Checksums are essential for:
- **Integrity verification:** Detecting accidental file corruption or tampering  
- **Reproducibility:** Confirming ETL outputs remain consistent across environments  
- **Provenance:** Linking each dataset’s lineage between metadata, STAC, and source files  
- **Auditability:** Enforcing CI validation and transparent data tracking  

All checksum files are generated automatically by the **land cover ETL pipeline** (`make landcover`)  
and validated during continuous integration workflows.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/landcover/
├── README.md
├── nlcd_1992_2021.tif.sha256
├── kansas_vegetation_1850s.tif.sha256
├── landcover_change_1992_2021.geojson.sha256
└── crop_distribution_2020.geojson.sha256
````

> **Note:** Each `.sha256` file corresponds directly to a processed dataset
> in `data/processed/landcover/`. All hashes are validated automatically via `sha256sum -c`.

---

## 🔐 Purpose of Checksums

| Objective           | Description                                                                    |
| :------------------ | :----------------------------------------------------------------------------- |
| **Integrity**       | Detects data corruption or modification between versions and transfers.        |
| **Reproducibility** | Guarantees identical ETL outputs from consistent input data and parameters.    |
| **Provenance**      | Links output artifacts to their metadata, STAC entries, and source references. |
| **CI Enforcement**  | Hash verification is built into automated pipelines and validation workflows.  |

---

## 🧮 Example `.sha256` File

```bash
# File: nlcd_1992_2021.tif.sha256
1e8a2a99ef45f582f821a4b8ac3adcc48f0c52b7c1d7ce1f92f4cb045c54cc54  nlcd_1992_2021.tif
```

This checksum ensures the file
`data/processed/landcover/nlcd_1992_2021.tif` has not changed since validation.

---

## ⚙️ Checksum Generation Workflow

Checksums are generated as the final step in the ETL pipeline.

**Makefile target:**

```bash
make landcover-checksums
```

**Equivalent Python command:**

```bash
python src/utils/generate_checksums.py data/processed/landcover/ --algo sha256
```

**Workflow Steps:**

1. Scan `data/processed/landcover/` for raster and vector outputs.
2. Compute SHA-256 hashes for all files.
3. Save results as `<filename>.sha256` in this directory.
4. Validate hashes in CI/CD (`stac-validate.yml` + `integrity-check.yml`).

---

## 🧰 CI/CD Validation

During GitHub Actions runs, checksums are re-verified to ensure data consistency:

```bash
sha256sum -c data/processed/checksums/landcover/*.sha256
```

If any mismatch is detected, the workflow halts, blocking commits or deployments
until regeneration is performed and hashes are revalidated.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                                | Purpose                                                           |
| :---------------------------------------------- | :---------------------------------------------------------------- |
| `data/processed/metadata/landcover/`            | Metadata files cross-reference checksum assets                    |
| `src/pipelines/landcover/landcover_pipeline.py` | Handles checksum generation and verification                      |
| `.github/workflows/stac-validate.yml`           | CI job for validation of data integrity and metadata              |
| `data/stac/landcover/`                          | STAC items embed checksum file paths and hashes in their metadata |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                     |
| :---------------------- | :----------------------------------------------------------------- |
| **Documentation-first** | Every dataset has an accompanying `.sha256` file and documentation |
| **Reproducibility**     | Hashes validate deterministic ETL runs                             |
| **Open Standards**      | FIPS 180-4 compliant SHA-256 algorithm                             |
| **Provenance**          | Checksum → STAC → Metadata → Source linkage                        |
| **Auditability**        | CI workflows automatically confirm hash validity                   |

---

## 📅 Version History

| Version | Date       | Summary                                                             |
| :------ | :--------- | :------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial release of land cover checksum documentation and hash files |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Pixel Proven: Verifying the Surface of Change.”*
📍 [`data/processed/checksums/landcover/`](.) · Linked to the **Land Cover STAC Collection**

</div>
